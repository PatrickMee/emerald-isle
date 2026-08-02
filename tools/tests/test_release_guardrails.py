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

from release_lib import extract_archive  # noqa: E402


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


class ArchiveSafetyTests(unittest.TestCase):
    def test_parent_path_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            archive_path = Path(temporary) / "unsafe.zip"
            with zipfile.ZipFile(archive_path, "w") as archive:
                archive.writestr("EmeraldIsle/../outside.txt", "unsafe")
            with self.assertRaisesRegex(ValueError, "unsafe archive path"):
                extract_archive(archive_path, Path(temporary) / "extract")


if __name__ == "__main__":
    unittest.main()
