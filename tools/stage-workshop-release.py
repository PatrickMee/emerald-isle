#!/usr/bin/env python3
"""Download and stage the exact GitHub release artifact for Steam upload."""

from __future__ import annotations

import argparse
import subprocess
import sys
import tempfile
import urllib.request
from pathlib import Path

from release_lib import directory_manifest, extract_archive, replace_directory


def read_build_info(package: Path) -> dict[str, str]:
    path = package / "About" / "BuildInfo.txt"
    if not path.is_file():
        raise ValueError("release artifact is missing About/BuildInfo.txt")
    return dict(line.split("=", 1) for line in path.read_text().splitlines() if "=" in line)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("version", help="published GitHub tag, for example v0.5.0")
    parser.add_argument("--archive", type=Path, help="use a previously downloaded release ZIP")
    parser.add_argument("--destination", type=Path, default=Path.home() / "Library/Application Support/Steam/steamapps/common/RimWorld/RimWorldMac.app/Mods/EmeraldIsle")
    args = parser.parse_args()
    repo = Path(__file__).resolve().parent.parent
    archive = (args.archive or repo / "build" / "downloads" / f"EmeraldIsle-{args.version}.zip").resolve()
    if args.archive is None:
        archive.parent.mkdir(parents=True, exist_ok=True)
        url = f"https://github.com/PatrickMee/emerald-isle/releases/download/{args.version}/{archive.name}"
        print(f"Downloading exact GitHub release asset: {url}")
        urllib.request.urlretrieve(url, archive)
    if not archive.is_file():
        parser.error(f"archive does not exist: {archive}")

    with tempfile.TemporaryDirectory(prefix="emerald-isle-release-") as temporary:
        try:
            package = extract_archive(archive, Path(temporary))
            info = read_build_info(package)
        except ValueError as error:
            print(f"Steam staging refused: {error}", file=sys.stderr)
            return 1
        expected = {
            "version": args.version,
            "packageId": "patrickmee.emeraldisle",
            "workshopId": "3763433723",
        }
        for key, value in expected.items():
            if info.get(key) != value:
                print(f"Steam staging refused: BuildInfo {key} is {info.get(key)!r}, expected {value!r}", file=sys.stderr)
                return 1
        validators = [
            [str(repo / "tools" / "validate-release-safety.sh"), str(package)],
            [sys.executable, str(repo / "tools" / "validate-texture-paths.py"), str(package)],
            [sys.executable, str(repo / "tools" / "validate-runtime-contracts.py"), str(package)],
        ]
        for command in validators:
            subprocess.run(command, check=True)
        replace_directory(package, args.destination.resolve())
        if directory_manifest(package) != directory_manifest(args.destination.resolve()):
            print("Steam staging refused: installed package differs from the release archive", file=sys.stderr)
            return 1

    print(f"Exact {args.version} release artifact staged at {args.destination.resolve()}")
    print("MAINTAINER UPLOAD STEPS:")
    print("  1. Launch RimWorld through Steam and select the local EmeraldIsle mod folder.")
    print("  2. Upload to existing Workshop item 3763433723; do not create a new item.")
    print("  3. Paste the approved change note, finish the upload, then verify from another subscriber machine.")
    print(f"  4. On that machine run: python3 tools/verify-workshop-release.py {args.version}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
