#!/usr/bin/env python3
"""Validate RimWorld texture references in a staged mod package."""

from __future__ import annotations

import argparse
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


TEXTURE_TAGS = {"texPath", "immatureGraphicPath", "uiIconPath", "wornGraphicPath"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate texture paths in a staged Emerald Isle package."
    )
    parser.add_argument(
        "package",
        nargs="?",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "build" / "EmeraldIsle",
        help="Staged package root (default: build/EmeraldIsle).",
    )
    return parser.parse_args()


def matching_textures(textures_root: Path, texture_path: str) -> tuple[Path, list[Path]]:
    base = textures_root / texture_path
    direct = base.with_suffix(".png")
    variants = sorted(base.parent.glob(f"{base.name}_*.png"))
    if base.is_dir():
        variants.extend(sorted(base.glob("*.png")))
    return direct, variants


def validate(package: Path) -> list[str]:
    defs_root = package / "Defs"
    textures_root = package / "Textures"
    errors: list[str] = []

    if not defs_root.is_dir():
        return [f"Definitions directory does not exist: {defs_root}"]
    if not textures_root.is_dir():
        return [f"Textures directory does not exist: {textures_root}"]

    for xml_path in sorted(defs_root.rglob("*.xml")):
        try:
            root = ET.parse(xml_path).getroot()
        except ET.ParseError as exc:
            errors.append(f"{xml_path}: invalid XML: {exc}")
            continue

        parent_by_child = {child: parent for parent in root.iter() for child in parent}
        for element in root.iter():
            if element.tag not in TEXTURE_TAGS or not element.text:
                continue

            texture_path = element.text.strip()
            direct, variants = matching_textures(textures_root, texture_path)
            parent = parent_by_child.get(element)
            graphic_class = (
                parent.findtext("graphicClass", "").strip()
                if parent is not None
                else ""
            )

            if graphic_class == "Graphic_StackCount":
                if not variants:
                    errors.append(
                        f"{xml_path}: {texture_path}: Graphic_StackCount requires "
                        "a texture variant collection, not only a single PNG"
                    )
                continue

            if not direct.is_file() and not variants:
                errors.append(f"{xml_path}: unresolved texture path: {texture_path}")

    return errors


def main() -> int:
    package = parse_args().package.resolve()
    errors = validate(package)
    if errors:
        print("Texture-path validation failed:", file=sys.stderr)
        for error in errors:
            print(f"  {error}", file=sys.stderr)
        return 1

    print(f"Texture-path validation passed for {package}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
