from __future__ import annotations

import os
import re
import shutil
import subprocess
import unittest
from pathlib import Path


REPO = Path(__file__).resolve().parents[2]
ASSEMBLY = REPO / "build/EmeraldIsle/Assemblies/EmeraldIsle.dll"


class HearthSocialAssemblyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        managed = os.environ.get("RIMWORLD_MANAGED_DIR")
        if not managed or not shutil.which("monodis"):
            raise unittest.SkipTest("verified RimWorld references or monodis unavailable")
        if not ASSEMBLY.is_file():
            raise AssertionError("stage the package before running assembly contract tests")
        env = dict(os.environ, MONO_PATH=managed)
        cls.il = subprocess.check_output(["monodis", str(ASSEMBLY)], text=True, env=env)
        if "BROKEN CLASS" in cls.il:
            raise AssertionError("compiled assembly did not resolve against installed RimWorld")

    def method(self, class_name: str, method_name: str) -> str:
        marker = f"end of method {class_name}::{method_name}"
        end = self.il.find(marker)
        self.assertGreaterEqual(end, 0, marker)
        start = self.il.rfind("    .method", 0, end)
        return self.il[start:end]

    def test_real_hearth_and_seat_gates_are_wired(self) -> None:
        ready = self.method("HearthSocialRelaxation", "IsReady")
        seat = self.method("HearthSocialRelaxation", "HasValidSeat")
        candidate = self.method("HearthSocialRelaxation", "IsCandidateSeat")
        for required in ("CompGatherSpot::get_Active", "CompRefuelable::get_HasFuel",
                         "FlickUtility::WantsToBeOn", "IsHearthReady"):
            self.assertIn(required, ready)
        for required in ("GridsUtility::GetEdifice", "get_InteractionCell",
                         "get_Position", "CanApplyBonus"):
            self.assertIn(required, seat)
        self.assertIn("get_InteractionCell", candidate)
        self.assertIn("GenAdj::OccupiedRect", candidate)
        self.assertIn("CellRect::Contains", candidate)

    def test_native_seat_picker_only_creates_bonus_job_for_hearth(self) -> None:
        giver = self.method("EI_JoyGiver_HearthSocialRelax", "TryGiveJob")
        gathering = self.method("EI_JoyGiver_HearthSocialRelax", "TryGiveJobInGatheringArea")
        self.assertIn("JoyGiver_SocialRelax::TryGiveJobInGatheringArea", giver)
        self.assertIn("HearthSocialRelaxation::IsCandidateSeat", giver)
        self.assertRegex(gathering, r"ldnull\s+IL_\w+:  ret")

    def test_only_native_social_tick_is_replaced_without_reserving_hearth(self) -> None:
        driver = self.il.split("  } // end of class EmeraldIsle.EI_JobDriver_HearthSocialRelax")[0]
        driver = driver.split("  .class public auto ansi sealed beforefieldinit EI_JobDriver_HearthSocialRelax")[-1]
        self.assertNotIn("TryMakePreToilReservations", driver)
        iterator = self.method("<MakeNewToils>d__0", "MoveNext")
        for required in ("Toil::socialMode", "Toil::defaultCompleteMode",
                         "Toil::defaultDuration", "Toil::tickIntervalAction",
                         "HearthJoyTick"):
            self.assertIn(required, iterator)
        self.assertEqual(iterator.count("Toil::tickIntervalAction"), 1)

    def test_full_joy_advances_to_native_optional_drink_finish(self) -> None:
        tick = self.method("EI_JobDriver_HearthSocialRelax", "HearthJoyTick")
        self.assertIn("HearthSocialRelaxation::IsReady", tick)
        self.assertIn("HearthSocialRelaxation::HasValidSeat", tick)
        self.assertRegex(
            tick,
            r"ldc\.i4\.1\s+IL_\w+:  ldc\.r4 1\.2[^\n]*\s+IL_\w+:  ldnull\s+"
            r"IL_\w+:  call bool class .*JoyUtility::JoyTickCheckEnd",
        )

