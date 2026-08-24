from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path


REPO = Path(__file__).resolve().parents[2]
TOOLS = REPO / "tools"
sys.path.insert(0, str(TOOLS))

from release_lib import extract_archive, replace_directory  # noqa: E402


class RuntimeContractTests(unittest.TestCase):
    def run_validator(self, package: Path) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(TOOLS / "validate-runtime-contracts.py"), str(package)],
            text=True,
            capture_output=True,
        )

    def test_current_staged_package_passes(self) -> None:
        result = self.run_validator(REPO / "build" / "EmeraldIsle")
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_zero_quern_xp_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / "EmeraldIsle"
            shutil.copytree(REPO / "build" / "EmeraldIsle", package)
            recipe = package / "Defs/RecipeDefs/EI_OatProcessing_Recipes.xml"
            recipe.write_text(
                recipe.read_text().replace(
                    "<workSkillLearnFactor>0.5</workSkillLearnFactor>",
                    "<workSkillLearnFactor>0</workSkillLearnFactor>",
                )
            )
            result = self.run_validator(package)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("expected 0.5", result.stderr)

    def test_bulk_oat_milling_work_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / "EmeraldIsle"
            shutil.copytree(REPO / "build" / "EmeraldIsle", package)
            recipe = package / "Defs/RecipeDefs/EI_OatProcessing_Recipes.xml"
            recipe.write_text(
                recipe.read_text().replace(
                    "<workAmount>720</workAmount>",
                    "<workAmount>700</workAmount>",
                    1,
                )
            )
            result = self.run_validator(package)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("EI_MillOatsBulk/workAmount: expected 720", result.stderr)

    def test_flatbread_fresh_food_priority_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / "EmeraldIsle"
            shutil.copytree(REPO / "build" / "EmeraldIsle", package)
            foods = package / "Defs/ThingDefs_Items/EI_OatFoods.xml"
            foods.write_text(
                foods.read_text().replace(
                    "<optimalityOffsetHumanlikes>6</optimalityOffsetHumanlikes>",
                    "<optimalityOffsetHumanlikes>16</optimalityOffsetHumanlikes>",
                    1,
                )
            )
            result = self.run_validator(package)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn(
                "EI_OatFlatbread/ingestible/optimalityOffsetHumanlikes: expected 6",
                result.stderr,
            )

    def test_smoked_meat_nutrition_regression_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / "EmeraldIsle"
            shutil.copytree(REPO / "build" / "EmeraldIsle", package)
            smoked_meat = package / "Defs/ThingDefs_Items/EI_SmokedMeat.xml"
            smoked_meat.write_text(
                smoked_meat.read_text().replace(
                    "<Nutrition>0.8</Nutrition>",
                    "<Nutrition>0.9</Nutrition>",
                    1,
                )
            )
            result = self.run_validator(package)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("EI_SmokedMeat/statBases/Nutrition: expected 0.8", result.stderr)

    def test_smoked_meat_cooking_skill_requirement_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / "EmeraldIsle"
            shutil.copytree(REPO / "build" / "EmeraldIsle", package)
            smoked_meat = package / "Defs/RecipeDefs/EI_SmokedMeat_Recipes.xml"
            smoked_meat.write_text(
                smoked_meat.read_text().replace(
                    "    <skillRequirements>\n      <Cooking>4</Cooking>\n    </skillRequirements>\n",
                    "",
                )
            )
            result = self.run_validator(package)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("EI_SmokeMeat/skillRequirements/Cooking: expected 4, found None", result.stderr)
            self.assertIn("EI_SmokeMeatBulk/skillRequirements/Cooking: expected 4, found None", result.stderr)

    def test_duplicate_central_hearth_recipe_registration_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / "EmeraldIsle"
            shutil.copytree(REPO / "build" / "EmeraldIsle", package)
            recipe_files = {
                "EI_SmokeMeat": package / "Defs/RecipeDefs/EI_SmokedMeat_Recipes.xml",
                "EI_SmokeMeatBulk": package / "Defs/RecipeDefs/EI_SmokedMeat_Recipes.xml",
                "EI_MakeFarmhouseCheese": package / "Defs/RecipeDefs/EI_FarmhouseCheese_Recipes.xml",
                "EI_MakeFarmhouseCheeseBulk": package / "Defs/RecipeDefs/EI_FarmhouseCheese_Recipes.xml",
                "EI_MakeOatWort": package / "Defs/RecipeDefs/EI_OatWort_Recipes.xml",
            }
            trees: dict[Path, ET.ElementTree] = {}
            for recipe_file in set(recipe_files.values()):
                tree = ET.parse(recipe_file)
                trees[recipe_file] = tree
                for recipe in tree.getroot().findall("RecipeDef"):
                    def_name = recipe.findtext("defName")
                    if def_name not in recipe_files or recipe_files[def_name] != recipe_file:
                        continue
                    users = recipe.find("recipeUsers")
                    if users is None:
                        users = ET.SubElement(recipe, "recipeUsers")
                    ET.SubElement(users, "li").text = "EI_CentralHearth"
            for recipe_file, tree in trees.items():
                tree.write(recipe_file, encoding="utf-8", xml_declaration=True)

            result = self.run_validator(package)
            self.assertNotEqual(result.returncode, 0)
            for def_name in recipe_files:
                self.assertIn(
                    f"{def_name}/effective central-hearth exposure: expected exactly once, found 2",
                    result.stderr,
                )

    def test_oat_wort_research_gate_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / "EmeraldIsle"
            shutil.copytree(REPO / "build" / "EmeraldIsle", package)
            wort = package / "Defs/RecipeDefs/EI_OatWort_Recipes.xml"
            wort.write_text(wort.read_text().replace("<researchPrerequisite>Brewing</researchPrerequisite>", "", 1))
            result = self.run_validator(package)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("EI_MakeOatWort/researchPrerequisite: expected Brewing", result.stderr)

    def test_oat_wort_balance_regression_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / "EmeraldIsle"
            shutil.copytree(REPO / "build" / "EmeraldIsle", package)
            wort = package / "Defs/RecipeDefs/EI_OatWort_Recipes.xml"
            wort.write_text(
                wort.read_text().replace(
                    "<workAmount>900</workAmount>",
                    "<workAmount>1000</workAmount>",
                    1,
                )
            )
            result = self.run_validator(package)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("EI_MakeOatWort/workAmount: expected 900", result.stderr)

    def test_hearth_flame_parity_regression_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / "EmeraldIsle"
            shutil.copytree(REPO / "build" / "EmeraldIsle", package)
            hearth = package / "Defs/ThingDefs_Buildings/EI_CentralHearth.xml"
            hearth.write_text(
                hearth.read_text().replace(
                    "<radius>9.9</radius>",
                    "<radius>9.8</radius>",
                    1,
                )
            )
            result = self.run_validator(package)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("radius: expected 9.9", result.stderr)

    def test_old_flax_yield_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / "EmeraldIsle"
            shutil.copytree(REPO / "build" / "EmeraldIsle", package)
            plant = package / "Defs/ThingDefs_Plants/EI_Flax.xml"
            plant.write_text(
                plant.read_text().replace("<harvestYield>9</harvestYield>", "<harvestYield>8</harvestYield>")
            )
            result = self.run_validator(package)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("expected 9", result.stderr)

    def test_advanced_wolfhound_trainability_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / "EmeraldIsle"
            shutil.copytree(REPO / "build" / "EmeraldIsle", package)
            wolfhound = package / "Defs/ThingDefs_Races/EI_Wolfhound.xml"
            wolfhound.write_text(
                wolfhound.read_text().replace(
                    "<trainability>Intermediate</trainability>",
                    "<trainability>Advanced</trainability>",
                    1,
                )
            )
            result = self.run_validator(package)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("race/trainability", result.stderr)

    def test_explicit_wolfhound_filth_rate_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            package = Path(temporary) / "EmeraldIsle"
            shutil.copytree(REPO / "build" / "EmeraldIsle", package)
            wolfhound = package / "Defs/ThingDefs_Races/EI_Wolfhound.xml"
            wolfhound.write_text(
                wolfhound.read_text().replace(
                    "<Wildness>0</Wildness>",
                    "<FilthRate>6</FilthRate>\n      <Wildness>0</Wildness>",
                    1,
                )
            )
            result = self.run_validator(package)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("inherit Core domestic-animal filth rate", result.stderr)


class ArchiveSafetyTests(unittest.TestCase):
    def test_parent_path_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            archive_path = Path(temporary) / "unsafe.zip"
            with zipfile.ZipFile(archive_path, "w") as archive:
                archive.writestr("EmeraldIsle/../outside.txt", "unsafe")
            with self.assertRaisesRegex(ValueError, "unsafe archive path"):
                extract_archive(archive_path, Path(temporary) / "extract")


class WorkshopStagingTests(unittest.TestCase):
    def test_backup_is_kept_outside_scanned_mods_directory(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            mods = root / "RimWorld" / "Mods"
            destination = mods / "EmeraldIsle"
            legacy_previous = mods / "EmeraldIsle.previous"
            source = root / "release" / "EmeraldIsle"
            destination.mkdir(parents=True)
            legacy_previous.mkdir()
            source.mkdir(parents=True)
            (destination / "version.txt").write_text("old")
            (legacy_previous / "version.txt").write_text("older")
            (source / "version.txt").write_text("new")

            replace_directory(source, destination)

            backup = root / "RimWorld" / "ModStagingBackups" / "EmeraldIsle.previous"
            self.assertEqual((destination / "version.txt").read_text(), "new")
            self.assertEqual((backup / "version.txt").read_text(), "old")
            self.assertFalse(legacy_previous.exists())
            self.assertEqual(
                [path.name for path in mods.iterdir() if path.is_dir()],
                ["EmeraldIsle"],
            )


if __name__ == "__main__":
    unittest.main()
