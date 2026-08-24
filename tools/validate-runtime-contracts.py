#!/usr/bin/env python3
"""Validate cumulative player-facing runtime contracts in a staged package."""

from __future__ import annotations

import argparse
import math
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


REQUIRED_DEF_NAMES = {
    "EI_BratCloak",
    "EI_CentralHearth",
    "EI_CookOatFlatbread",
    "EI_CookOatFlatbreadBulk",
    "EI_CookOatPorridge",
    "EI_CookOatPorridgeBulk",
    "EI_DoBillsCookCentralHearth",
    "EI_DoBillsMillOats",
    "EI_DryStoneWall",
    "EI_FarmhouseCheese",
    "EI_HandQuern",
    "EI_KerryCattle",
    "EI_Linen",
    "EI_LinenFabric",
    "EI_LinenTunic",
    "EI_MakeFlakJacketWithLinen",
    "EI_MakeFlakPantsWithLinen",
    "EI_MakeFlakVestWithLinen",
    "EI_MakeIndustrialMedicineWithLinen",
    "EI_MakeMolotovCocktailsWithLinen",
    "EI_MakeFarmhouseCheese",
    "EI_MilledOats",
    "EI_MillOats",
    "EI_MillOatsBulk",
    "EI_OatFlatbread",
    "EI_OatPorridge",
    "EI_Plant_Flax",
    "EI_Plant_Oats",
    "EI_ProcessFlax",
    "EI_RawFlax",
    "EI_RawOats",
    "EI_SmokeMeat",
    "EI_SmokeMeatBulk",
    "EI_SmokedMeat",
    "EI_MakeOatWort",
    "EI_Wolfhound",
}


def load_defs(package: Path) -> dict[str, ET.Element]:
    definitions: dict[str, ET.Element] = {}
    for xml_path in sorted((package / "Defs").rglob("*.xml")):
        root = ET.parse(xml_path).getroot()
        for element in root:
            def_name = element.findtext("defName")
            if def_name:
                definitions[def_name] = element
    return definitions


def load_typed_defs(package: Path) -> dict[tuple[str, str], ET.Element]:
    definitions: dict[tuple[str, str], ET.Element] = {}
    for xml_path in sorted((package / "Defs").rglob("*.xml")):
        root = ET.parse(xml_path).getroot()
        for element in root:
            def_name = element.findtext("defName")
            if def_name:
                definitions[(element.tag, def_name)] = element
    return definitions


def validate_wolfhound_contracts(
    definitions: dict[tuple[str, str], ET.Element],
) -> list[str]:
    errors: list[str] = []
    thing = definitions.get(("ThingDef", "EI_Wolfhound"))
    kind = definitions.get(("PawnKindDef", "EI_Wolfhound"))

    if thing is None:
        return ["missing ThingDef EI_Wolfhound"]
    if kind is None:
        return ["missing PawnKindDef EI_Wolfhound"]

    expected_thing_values = {
        "statBases/MoveSpeed": "5.4",
        "statBases/MarketValue": "380",
        "statBases/ComfyTemperatureMin": "-30",
        "statBases/Wildness": "0",
        "race/baseBodySize": "1.05",
        "race/baseHungerRate": "0.60",
        "race/baseHealthScale": "1.0",
        "race/gestationPeriodDays": "12",
        "race/trainability": "Intermediate",
        "race/nuzzleMtbHours": "24",
        "race/lifeExpectancy": "8",
    }
    for path, expected in expected_thing_values.items():
        actual = thing.findtext(path)
        if actual != expected:
            errors.append(
                f"EI_Wolfhound/{path}: expected {expected}, found {actual!r}"
            )

    if thing.find("statBases/FilthRate") is not None:
        errors.append(
            "EI_Wolfhound must inherit Core domestic-animal filth rate"
        )

    special_trainables = thing.findall("race/specialTrainables/li")
    if len(special_trainables) != 1:
        errors.append("EI_Wolfhound must declare exactly one special trainable")
    else:
        special = special_trainables[0]
        if (special.text or "").strip() != "AttackTarget":
            errors.append("EI_Wolfhound special trainable must be AttackTarget")
        if special.get("MayRequire") != "Ludeon.RimWorld.Odyssey":
            errors.append(
                "EI_Wolfhound AttackTarget must be conditional on Odyssey"
            )

    for forbidden in ("herdAnimal", "predator", "packAnimal"):
        if thing.find(f"race/{forbidden}") is not None:
            errors.append(f"EI_Wolfhound must not declare race/{forbidden}")

    trade_tags = [
        (element.text or "").strip() for element in thing.findall("tradeTags/li")
    ]
    if trade_tags != ["AnimalUncommon", "AnimalFighter"]:
        errors.append(
            "EI_Wolfhound trade tags must be AnimalUncommon and AnimalFighter only"
        )

    life_stage_ages = [
        (element.text or "").strip()
        for element in thing.findall("race/lifeStageAges/li/minAge")
    ]
    if life_stage_ages != ["0", "0.3", "0.8"]:
        errors.append(
            "EI_Wolfhound life-stage ages must remain 0, 0.3, and 0.8 years"
        )

    litter_points = [
        (element.text or "").strip()
        for element in thing.findall("race/litterSizeCurve/points/li")
    ]
    if litter_points != ["(0.5, 0)", "(1, 1)", "(2, 0.35)", "(2.5, 0)"]:
        errors.append("EI_Wolfhound litter-size curve changed unexpectedly")

    bite_power = None
    for tool in thing.findall("tools/li"):
        capacities = {
            (element.text or "").strip()
            for element in tool.findall("capacities/li")
        }
        if "Bite" in capacities:
            bite_power = tool.findtext("power")
            break
    if bite_power != "16":
        errors.append(
            f"EI_Wolfhound bite power: expected 16, found {bite_power!r}"
        )

    if kind.findtext("combatPower") != "88":
        errors.append(
            "EI_Wolfhound combatPower must remain 88 pending controlled playtests"
        )
    for forbidden in ("wildGroupSize", "ecoSystemWeight"):
        if kind.find(forbidden) is not None:
            errors.append(f"EI_Wolfhound must not declare PawnKindDef/{forbidden}")

    return errors


def validate_oat_bulk_recipe_contracts(
    definitions: dict[tuple[str, str], ET.Element],
) -> list[str]:
    errors: list[str] = []
    expected = {
        "EI_CookOatPorridgeBulk": {
            "workAmount": "480",
            "product": ("EI_OatPorridge", "4"),
            "displayPriority": "111",
        },
        "EI_CookOatFlatbreadBulk": {
            "workAmount": "1680",
            "product": ("EI_OatFlatbread", "4"),
            "displayPriority": "112",
        },
    }

    for def_name, values in expected.items():
        recipe = definitions.get(("RecipeDef", def_name))
        if recipe is None:
            errors.append(f"missing RecipeDef {def_name}")
            continue

        for path, expected_value in {
            "workAmount": values["workAmount"],
            "workSpeedStat": "CookSpeed",
            "requiredGiverWorkType": "Cooking",
            "effectWorking": "Cook",
            "soundWorking": "Recipe_CookMeal",
            "workSkill": "Cooking",
            "ingredients/li/count": "40",
            "ingredients/li/filter/thingDefs/li": "EI_MilledOats",
            "fixedIngredientFilter/thingDefs/li": "EI_MilledOats",
            "displayPriority": values["displayPriority"],
        }.items():
            actual = recipe.findtext(path)
            if actual != expected_value:
                errors.append(f"{def_name}/{path}: expected {expected_value}, found {actual!r}")

        product_def, product_count = values["product"]
        product = recipe.find(f"products/{product_def}")
        if product is None or (product.text or "").strip() != product_count:
            actual = None if product is None else (product.text or "").strip()
            errors.append(
                f"{def_name}/products/{product_def}: expected {product_count}, found {actual!r}"
            )

        users = [
            (element.text or "").strip()
            for element in recipe.findall("recipeUsers/li")
        ]
        if users != ["Campfire", "FueledStove", "ElectricStove"]:
            errors.append(
                f"{def_name}/recipeUsers: expected Campfire, FueledStove, ElectricStove, found {users!r}"
            )
        if recipe.find("targetCountAdjustment") is not None:
            errors.append(f"{def_name} must not use targetCountAdjustment")

    central_hearth = definitions.get(("ThingDef", "EI_CentralHearth"))
    if central_hearth is not None:
        hearth_recipes = [
            (element.text or "").strip()
            for element in central_hearth.findall("recipes/li")
        ]
        for def_name in expected:
            if hearth_recipes.count(def_name) != 1:
                errors.append(
                    f"EI_CentralHearth/recipes/{def_name}: expected exactly once, found {hearth_recipes.count(def_name)}"
                )

    return errors


def validate_oat_bulk_milling_recipe_contract(
    definitions: dict[tuple[str, str], ET.Element],
) -> list[str]:
    errors: list[str] = []
    def_name = "EI_MillOatsBulk"
    recipe = definitions.get(("RecipeDef", def_name))
    if recipe is None:
        return [f"missing RecipeDef {def_name}"]

    expected_values = {
        "workAmount": "720",
        "workSpeedStat": "GeneralLaborSpeed",
        "requiredGiverWorkType": "Crafting",
        "effectWorking": "CutStone",
        "soundWorking": "Recipe_MakeStoneBlocks",
        "workSkill": "Crafting",
        "workSkillLearnFactor": "0.5",
        "ingredients/li/count": "40",
        "ingredients/li/filter/thingDefs/li": "EI_RawOats",
        "fixedIngredientFilter/thingDefs/li": "EI_RawOats",
        "displayPriority": "110",
    }
    for path, expected in expected_values.items():
        actual = recipe.findtext(path)
        if actual != expected:
            errors.append(f"{def_name}/{path}: expected {expected}, found {actual!r}")

    product = recipe.find("products/EI_MilledOats")
    actual_product = None if product is None else (product.text or "").strip()
    if actual_product != "40":
        errors.append(
            f"{def_name}/products/EI_MilledOats: expected 40, found {actual_product!r}"
        )

    users = [
        (element.text or "").strip()
        for element in recipe.findall("recipeUsers/li")
    ]
    if users != ["EI_HandQuern"]:
        errors.append(
            f"{def_name}/recipeUsers: expected EI_HandQuern, found {users!r}"
        )

    if recipe.find("targetCountAdjustment") is not None:
        errors.append(f"{def_name} must not use targetCountAdjustment")
    if recipe.find("bulkRecipeCount") is not None:
        errors.append(f"{def_name} must not use bulkRecipeCount")

    return errors


def validate_oat_food_contracts(
    definitions: dict[tuple[str, str], ET.Element],
) -> list[str]:
    errors: list[str] = []
    expected = {
        "EI_OatPorridge": {
            "marketValue": "11",
            "mass": "0.44",
            "workToMake": "120",
            "nutrition": "0.9",
            "daysToRotStart": "2",
            "humanlikeOffset": None,
        },
        "EI_OatFlatbread": {
            "marketValue": "11",
            "mass": "0.44",
            "workToMake": "420",
            "nutrition": "0.8",
            "daysToRotStart": "14",
            "humanlikeOffset": "6",
        },
    }

    for def_name, values in expected.items():
        food = definitions.get(("ThingDef", def_name))
        if food is None:
            errors.append(f"missing ThingDef {def_name}")
            continue

        expected_stats = {
            "statBases/MarketValue": values["marketValue"],
            "statBases/Mass": values["mass"],
            "statBases/WorkToMake": values["workToMake"],
            "statBases/Nutrition": values["nutrition"],
            "ingestible/preferability": "MealSimple",
            "comps/li/daysToRotStart": values["daysToRotStart"],
        }
        for path, expected_value in expected_stats.items():
            actual = food.findtext(path)
            if actual != expected_value:
                errors.append(
                    f"{def_name}/{path}: expected {expected_value}, found {actual!r}"
                )

        offset = food.find("ingestible/optimalityOffsetHumanlikes")
        actual_offset = None if offset is None else (offset.text or "").strip()
        expected_offset = values["humanlikeOffset"]
        if expected_offset is None:
            if offset is not None:
                errors.append(
                    f"{def_name}/ingestible/optimalityOffsetHumanlikes: "
                    "porridge must retain the inherited fresh-food path"
                )
        elif actual_offset != expected_offset:
            errors.append(
                f"{def_name}/ingestible/optimalityOffsetHumanlikes: expected "
                f"{expected_offset}, found {actual_offset!r}"
            )

    return errors


def validate_linen_compatibility_recipe_contracts(
    definitions: dict[tuple[str, str], ET.Element],
) -> list[str]:
    errors: list[str] = []
    expected = {
        "EI_MakeFlakVestWithLinen": {
            "product": ("Apparel_FlakVest", "1"),
            "workAmount": "9000",
            "workSpeedStat": "GeneralLaborSpeed",
            "effectWorking": "Smith",
            "soundWorking": "Recipe_Machining",
            "workSkill": "Crafting",
            "unfinishedThingDef": "UnfinishedTechArmor",
            "recipeUsers": ["TableMachining"],
            "researchPrerequisite": "FlakArmor",
            "skillRequirements": [("Crafting", "4")],
            "ingredients": [
                ("EI_Linen", "30"),
                ("Steel", "60"),
                ("ComponentIndustrial", "1"),
            ],
        },
        "EI_MakeFlakPantsWithLinen": {
            "product": ("Apparel_FlakPants", "1"),
            "workAmount": "9000",
            "workSpeedStat": "GeneralLaborSpeed",
            "effectWorking": "Smith",
            "soundWorking": "Recipe_Machining",
            "workSkill": "Crafting",
            "unfinishedThingDef": "UnfinishedTechArmor",
            "recipeUsers": ["TableMachining"],
            "researchPrerequisite": "FlakArmor",
            "skillRequirements": [("Crafting", "4")],
            "ingredients": [
                ("EI_Linen", "30"),
                ("Steel", "60"),
                ("ComponentIndustrial", "1"),
            ],
        },
        "EI_MakeFlakJacketWithLinen": {
            "product": ("Apparel_FlakJacket", "1"),
            "workAmount": "14000",
            "workSpeedStat": "GeneralLaborSpeed",
            "effectWorking": "Smith",
            "soundWorking": "Recipe_Machining",
            "workSkill": "Crafting",
            "unfinishedThingDef": "UnfinishedTechArmor",
            "recipeUsers": ["TableMachining"],
            "researchPrerequisite": "FlakArmor",
            "skillRequirements": [("Crafting", "4")],
            "ingredients": [
                ("EI_Linen", "50"),
                ("Steel", "70"),
                ("ComponentIndustrial", "1"),
            ],
        },
        "EI_MakeIndustrialMedicineWithLinen": {
            "product": ("MedicineIndustrial", "1"),
            "workAmount": "700",
            "workSpeedStat": "DrugSynthesisSpeed",
            "effectWorking": "Cook",
            "soundWorking": "Recipe_CookMeal",
            "workSkill": "Intellectual",
            "recipeUsers": ["DrugLab"],
            "researchPrerequisite": "MedicineProduction",
            "skillRequirements": [("Crafting", "4"), ("Intellectual", "4")],
            "ingredients": [
                ("MedicineHerbal", "1"),
                ("Neutroamine", "1"),
                ("EI_Linen", "3"),
            ],
        },
        "EI_MakeMolotovCocktailsWithLinen": {
            "product": ("Weapon_GrenadeMolotov", "1"),
            "workAmount": "6000",
            "workSpeedStat": "GeneralLaborSpeed",
            "effectWorking": "Smith",
            "soundWorking": "Recipe_Smith",
            "workSkill": "Crafting",
            "unfinishedThingDef": "UnfinishedGun",
            "recipeUsers": ["TableMachining"],
            "researchPrerequisite": "Machining",
            "skillRequirements": [],
            "ingredients": [("EI_Linen", "25"), ("Chemfuel", "80")],
        },
    }

    for def_name, values in expected.items():
        recipe = definitions.get(("RecipeDef", def_name))
        if recipe is None:
            errors.append(f"missing RecipeDef {def_name}")
            continue

        for path in (
            "workAmount",
            "workSpeedStat",
            "effectWorking",
            "soundWorking",
            "workSkill",
            "researchPrerequisite",
        ):
            expected_value = values[path]
            actual = recipe.findtext(path)
            if actual != expected_value:
                errors.append(
                    f"{def_name}/{path}: expected {expected_value}, found {actual!r}"
                )

        expected_unfinished = values.get("unfinishedThingDef")
        actual_unfinished = recipe.findtext("unfinishedThingDef")
        if actual_unfinished != expected_unfinished:
            errors.append(
                f"{def_name}/unfinishedThingDef: expected {expected_unfinished}, found {actual_unfinished!r}"
            )

        users = [
            (element.text or "").strip()
            for element in recipe.findall("recipeUsers/li")
        ]
        if users != values["recipeUsers"]:
            errors.append(
                f"{def_name}/recipeUsers: expected {values['recipeUsers']}, found {users}"
            )

        skill_requirements = [
            (element.tag, (element.text or "").strip())
            for element in recipe.find("skillRequirements") or []
        ]
        if skill_requirements != values["skillRequirements"]:
            errors.append(
                f"{def_name}/skillRequirements: expected {values['skillRequirements']}, found {skill_requirements}"
            )

        ingredients = []
        for ingredient in recipe.findall("ingredients/li"):
            ingredient_def = ingredient.findtext("filter/thingDefs/li")
            ingredients.append((ingredient_def, ingredient.findtext("count")))
        if ingredients != values["ingredients"]:
            errors.append(
                f"{def_name}/ingredients: expected {values['ingredients']}, found {ingredients}"
            )

        fixed_ingredients = [
            (element.text or "").strip()
            for element in recipe.findall("fixedIngredientFilter/thingDefs/li")
        ]
        expected_fixed = [ingredient[0] for ingredient in values["ingredients"]]
        if fixed_ingredients != expected_fixed:
            errors.append(
                f"{def_name}/fixedIngredientFilter: expected {expected_fixed}, found {fixed_ingredients}"
            )

        product_def, product_count = values["product"]
        product = recipe.find(f"products/{product_def}")
        actual_product = None if product is None else (product.text or "").strip()
        if actual_product != product_count:
            errors.append(
                f"{def_name}/products/{product_def}: expected {product_count}, found {actual_product!r}"
            )

        if recipe.find("targetCountAdjustment") is not None:
            errors.append(
                f"{def_name} must not use targetCountAdjustment; one bill produces one vanilla item"
            )
        if recipe.find("bulkRecipeCount") is not None:
            errors.append(
                f"{def_name} must not use bulkRecipeCount; duplicate-output behavior is not approved"
            )

    return errors


def validate_hearth_larder_contracts(
    definitions: dict[tuple[str, str], ET.Element],
) -> list[str]:
    errors: list[str] = []
    hearth = definitions.get(("ThingDef", "EI_CentralHearth"))
    if hearth is None:
        return ["missing ThingDef EI_CentralHearth"]

    expected_hearth_values = {
        "statBases/WorkTableWorkSpeedFactor": "0.65",
        "statBases/MeditationFocusStrength": "0.0",
        "comps/li[1]/fuelConsumptionRate": "6.0",
        "comps/li[2]/glowRadius": "10",
        "comps/li[3]/heatPerSecond": "16",
        "comps/li[3]/heatPushMaxTemperature": "26",
    }
    for path, expected in expected_hearth_values.items():
        actual = hearth.findtext(path)
        if actual != expected:
            errors.append(f"EI_CentralHearth/{path}: expected {expected}, found {actual!r}")

    refuelable = hearth.find("comps/li[@Class='CompProperties_Refuelable']")
    if refuelable is None or refuelable.findtext("canEjectFuel") != "true":
        errors.append("EI_CentralHearth refuelable comp must allow fuel ejection")

    meditation = hearth.find("comps/li[@Class='CompProperties_MeditationFocus']")
    if meditation is None:
        errors.append("EI_CentralHearth must use the verified Campfire Flame meditation component")
    else:
        expected_meditation = {
            "statDef": "MeditationFocusStrength",
            "focusTypes/li": "Flame",
            "offsets/li[1]/offset": "0.12",
            "offsets/li[2]/offsetPerBuilding": "0.02",
            "offsets/li[2]/radius": "9.9",
            "offsets/li[2]/maxBuildings": "8",
            "offsets/li[2]/explanationKey": "MeditationFocusPerFlame",
            "offsets/li[2]/explanationKeyAbstract": "MeditationFocusPerFlameAbstract",
        }
        for path, expected in expected_meditation.items():
            actual = meditation.findtext(path)
            if actual != expected:
                errors.append(f"EI_CentralHearth/meditation/{path}: expected {expected}, found {actual!r}")

    expected_recipe_order = [
        "EI_SmokeMeat",
        "EI_SmokeMeatBulk",
        "EI_CookOatPorridge",
        "EI_CookOatFlatbread",
        "EI_CookOatPorridgeBulk",
        "EI_CookOatFlatbreadBulk",
        "EI_MakeFarmhouseCheese",
        "EI_MakeFarmhouseCheeseBulk",
        "EI_MakeOatWort",
    ]
    recipes = [(element.text or "").strip() for element in hearth.findall("recipes/li")]
    positions = [recipes.index(def_name) if def_name in recipes else -1 for def_name in expected_recipe_order]
    if any(position < 0 for position in positions) or positions != sorted(positions):
        errors.append("EI_CentralHearth recipe visibility/order does not match the Hearth/Larder contract")

    expected_central_hearth_recipe_users = {
        "EI_SmokeMeat": [],
        "EI_SmokeMeatBulk": [],
        "EI_MakeFarmhouseCheese": ["FueledStove", "ElectricStove"],
        "EI_MakeFarmhouseCheeseBulk": ["FueledStove", "ElectricStove"],
        "EI_MakeOatWort": [],
    }
    for def_name in expected_recipe_order:
        recipe = definitions.get(("RecipeDef", def_name))
        if recipe is None:
            continue
        direct_count = recipes.count(def_name)
        users = [(element.text or "").strip() for element in recipe.findall("recipeUsers/li")]
        central_user_count = users.count("EI_CentralHearth")
        effective_count = direct_count + central_user_count
        if direct_count != 1:
            errors.append(
                f"EI_CentralHearth/recipes/{def_name}: expected exactly once, found {direct_count}"
            )
        if effective_count != 1:
            errors.append(
                f"{def_name}/effective central-hearth exposure: expected exactly once, found {effective_count}"
            )
        if def_name in expected_central_hearth_recipe_users:
            expected_users = expected_central_hearth_recipe_users[def_name]
            if users != expected_users:
                errors.append(
                    f"{def_name}/recipeUsers: expected {expected_users}, found {users}"
                )

    smoked_meat = definitions.get(("ThingDef", "EI_SmokedMeat"))
    if smoked_meat is None:
        errors.append("missing ThingDef EI_SmokedMeat")
    else:
        if smoked_meat.get("ParentName") != "MealBase":
            errors.append("EI_SmokedMeat must inherit MealBase for vanilla meal ingestion and ingredient provenance")
        expected_food_values = {
            "statBases/MarketValue": "15",
            "statBases/Mass": "0.44",
            "statBases/WorkToMake": "600",
            "statBases/Nutrition": "0.8",
            "ingestible/preferability": "MealSimple",
            "ingestible/optimalityOffsetHumanlikes": "6",
            "comps/li/ daysToRotStart": "30",
        }
        for path, expected in expected_food_values.items():
            normalized_path = path.replace("li/ ", "li/")
            actual = smoked_meat.findtext(normalized_path)
            if actual != expected:
                errors.append(f"EI_SmokedMeat/{normalized_path}: expected {expected}, found {actual!r}")

    for def_name, count, work_amount, priority in (
        ("EI_SmokeMeat", "0.60", "600", "104"),
        ("EI_SmokeMeatBulk", "2.40", "2400", "114"),
    ):
        recipe = definitions.get(("RecipeDef", def_name))
        if recipe is None:
            errors.append(f"missing RecipeDef {def_name}")
            continue
        expected_values = {
            "workAmount": work_amount,
            "workSpeedStat": "CookSpeed",
            "requiredGiverWorkType": "Cooking",
            "effectWorking": "Cook",
            "soundWorking": "Recipe_CookMeal",
            "ingredientValueGetterClass": "IngredientValueGetter_Nutrition",
            "ingredients/li/count": count,
            "ingredients/li/filter/categories/li": "MeatRaw",
            "fixedIngredientFilter/categories/li": "MeatRaw",
            "defaultIngredientFilter/categories/li": "MeatRaw",
            "skillRequirements/Cooking": "4",
            "displayPriority": priority,
        }
        for path, expected in expected_values.items():
            actual = recipe.findtext(path)
            if actual != expected:
                errors.append(f"{def_name}/{path}: expected {expected}, found {actual!r}")
        disallowed = [element.text.strip() for element in recipe.findall("defaultIngredientFilter/disallowedThingDefs/li")]
        if disallowed != ["Meat_Human", "Meat_Megaspider", "Meat_Twisted"]:
            errors.append(f"{def_name} default meat exclusions changed: {disallowed!r}")
        product = recipe.find("products/EI_SmokedMeat")
        expected_product = "1" if def_name == "EI_SmokeMeat" else "4"
        if product is None or (product.text or "").strip() != expected_product:
            errors.append(f"{def_name}/products/EI_SmokedMeat must be {expected_product}")
        if recipe.find("researchPrerequisite") is not None:
            errors.append(f"{def_name} must not require research")

    wort = definitions.get(("RecipeDef", "EI_MakeOatWort"))
    if wort is None:
        errors.append("missing RecipeDef EI_MakeOatWort")
    else:
        expected_wort_values = {
            "description": "Mix raw oats and hops into wort for fermentation in a fermenting barrel.",
            "workAmount": "900",
            "workSpeedStat": "DrugCookingSpeed",
            "workSkill": "Cooking",
            "effectWorking": "Cook",
            "soundWorking": "Recipe_Brewing",
            "targetCountAdjustment": "1",
            "researchPrerequisite": "Brewing",
            "ingredients/li[1]/filter/thingDefs/li": "EI_RawOats",
            "ingredients/li[1]/count": "20",
            "ingredients/li[2]/filter/thingDefs/li": "RawHops",
            "ingredients/li[2]/count": "5",
            "products/Wort": "5",
            "displayPriority": "105",
        }
        for path, expected in expected_wort_values.items():
            actual = wort.findtext(path)
            if actual != expected:
                errors.append(f"EI_MakeOatWort/{path}: expected {expected}, found {actual!r}")
        if [element.text.strip() for element in wort.findall("fixedIngredientFilter/thingDefs/li")] != ["EI_RawOats", "RawHops"]:
            errors.append("EI_MakeOatWort fixed ingredient filter must be EI_RawOats and RawHops")

        effective_work = 5 * 900 / 0.65
        if not math.isclose(effective_work, 6923.076923, rel_tol=0, abs_tol=0.001):
            errors.append(f"oat wort effective full-barrel work changed: {effective_work}")
        if not effective_work > 5 * 1000:
            errors.append("oat wort full-barrel work must remain slower than vanilla brewery wort")

    return errors


def validate(package: Path) -> list[str]:
    errors: list[str] = []
    definitions = load_defs(package)
    typed_definitions = load_typed_defs(package)
    missing = sorted(REQUIRED_DEF_NAMES - definitions.keys())
    if missing:
        errors.append("missing released definitions: " + ", ".join(missing))

    expected_values = {
        ("EI_MillOats", "workSkillLearnFactor"): "0.5",
        ("EI_Plant_Flax", "plant/harvestYield"): "9",
    }
    for (def_name, path), expected in expected_values.items():
        element = definitions.get(def_name)
        actual = element.findtext(path) if element is not None else None
        if actual != expected:
            errors.append(f"{def_name}/{path}: expected {expected}, found {actual!r}")

    errors.extend(validate_wolfhound_contracts(typed_definitions))
    errors.extend(validate_oat_food_contracts(typed_definitions))
    errors.extend(validate_oat_bulk_recipe_contracts(typed_definitions))
    errors.extend(validate_oat_bulk_milling_recipe_contract(typed_definitions))
    errors.extend(validate_linen_compatibility_recipe_contracts(typed_definitions))
    errors.extend(validate_hearth_larder_contracts(typed_definitions))

    about_path = package / "About" / "About.xml"
    if not about_path.is_file():
        errors.append("missing About/About.xml")
    else:
        about = ET.parse(about_path).getroot()
        if about.findtext("packageId") != "patrickmee.emeraldisle":
            errors.append("About/About.xml has an unexpected packageId")

    published_id = package / "About" / "PublishedFileId.txt"
    if not published_id.is_file() or published_id.read_text().strip() != "3763433723":
        errors.append("About/PublishedFileId.txt must contain Workshop item 3763433723")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("package", nargs="?", type=Path, default=Path("build/EmeraldIsle"))
    args = parser.parse_args()
    package = args.package.resolve()
    if not package.is_dir():
        parser.error(f"staged package does not exist: {package}")
    errors = validate(package)
    if errors:
        print("Runtime-contract validation failed:", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        return 1
    print(f"Runtime-contract validation passed for {package}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
