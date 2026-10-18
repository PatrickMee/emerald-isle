from __future__ import annotations

import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


REPO = Path(__file__).resolve().parents[2]


class HearthSocialEligibilityTests(unittest.TestCase):
    def test_all_bonus_gates_and_gain_factor(self) -> None:
        if not shutil.which("mcs") or not shutil.which("mono"):
            self.skipTest("Mono compiler/runtime unavailable")
        with tempfile.TemporaryDirectory() as temporary:
            executable = Path(temporary) / "HearthSocialEligibilityTests.exe"
            subprocess.run(
                [
                    "mcs",
                    "-warnaserror",
                    f"-out:{executable}",
                    str(REPO / "Source/EmeraldIsle/HearthSocialEligibility.cs"),
                    str(REPO / "tools/tests/HearthSocialEligibilityTests.cs"),
                ],
                check=True,
            )
            subprocess.run(["mono", str(executable)], check=True)
