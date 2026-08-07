#!/usr/bin/env python3
"""Validate cumulative player-facing runtime contracts in a staged package."""

from __future__ import annotations

import argparse
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


REQUIRED_DEF_NAMES = {
    "EI_BratCloak",
    "EI_CentralHearth",
    "EI_CookOatFlatbread",
    "EI_CookOatPorridge",
    "EI_DoBillsCookCentralHearth",
    "EI_DoBillsMillOats",
    "EI_DryStoneWall",
    "EI_FarmhouseCheese",
    "EI_HandQuern",
    "EI_KerryCattle",
    "EI_Linen",
    "EI_LinenFabric",
    "EI_LinenTunic",
    "EI_MakeFarmhouseCheese",
    "EI_MilledOats",
    "EI_MillOats",
    "EI_OatFlatbread",
    "EI_OatPorridge",
    "EI_Plant_Flax",
    "EI_Plant_Oats",
    "EI_ProcessFlax",
    "EI_RawFlax",
    "EI_RawOats",
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
