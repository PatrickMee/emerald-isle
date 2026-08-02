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


def validate(package: Path) -> list[str]:
    errors: list[str] = []
    definitions = load_defs(package)
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
