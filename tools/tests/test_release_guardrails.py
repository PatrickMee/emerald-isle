from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile
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
