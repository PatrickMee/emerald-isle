#!/usr/bin/env python3
"""Build a deterministic release archive from an exact tagged main commit."""

from __future__ import annotations

import argparse
import re
import stat
import subprocess
import sys
import zipfile
from pathlib import Path

from release_lib import directory_manifest, sha256_file


VERSION_PATTERN = re.compile(r"v\d+\.\d+\.\d+(?:-(?:alpha|beta|rc)\.\d+)?$")
FIXED_ZIP_TIME = (1980, 1, 1, 0, 0, 0)


def git(repo: Path, *args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=repo, text=True).strip()


def require_clean_source(repo: Path) -> None:
    if git(repo, "status", "--porcelain"):
        raise RuntimeError("working tree is not clean")


def require_release_source(repo: Path, version: str) -> None:
    require_clean_source(repo)
    if git(repo, "branch", "--show-current") != "main":
        raise RuntimeError("release archives must be built on main")
    commit = git(repo, "rev-parse", "HEAD")
    if git(repo, "rev-parse", "origin/main") != commit:
        raise RuntimeError("HEAD does not match origin/main; fetch and fast-forward first")
    try:
        tag_commit = git(repo, "rev-parse", f"refs/tags/{version}^{{commit}}")
    except subprocess.CalledProcessError as error:
        raise RuntimeError(f"annotated release tag {version} is missing") from error
    if tag_commit != commit:
        raise RuntimeError(f"tag {version} does not identify HEAD")
    tag_type = git(repo, "cat-file", "-t", f"refs/tags/{version}")
    if tag_type != "tag":
        raise RuntimeError(f"tag {version} must be annotated")


def write_deterministic_archive(package: Path, archive_path: Path) -> None:
    with zipfile.ZipFile(archive_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for relative in sorted(directory_manifest(package)):
            source = package / relative
            info = zipfile.ZipInfo(f"EmeraldIsle/{relative}", FIXED_ZIP_TIME)
            info.create_system = 3
            info.external_attr = (stat.S_IFREG | 0o644) << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info, source.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("version", help="annotated release tag, for example v0.5.0")
    parser.add_argument(
        "--candidate",
        action="store_true",
        help="build review candidate before merge/tag; final build must omit this flag",
    )
    args = parser.parse_args()
    if not VERSION_PATTERN.fullmatch(args.version):
        parser.error("version must look like v0.5.0 or v0.5.0-rc.1")

    repo = Path(__file__).resolve().parent.parent
    try:
        if args.candidate:
            require_clean_source(repo)
        else:
            require_release_source(repo, args.version)
    except RuntimeError as error:
        print(f"Release build refused: {error}", file=sys.stderr)
        return 1

    subprocess.run([str(repo / "tools" / "stage-mod.sh")], cwd=repo, check=True)
    package = repo / "build" / "EmeraldIsle"
    build_info = package / "About" / "BuildInfo.txt"
    build_info.write_text(
        f"version={args.version}\n"
        "packageId=patrickmee.emeraldisle\nworkshopId=3763433723\n",
        encoding="utf-8",
    )
    subprocess.run([str(repo / "tools" / "validate-release-safety.sh"), str(package)], check=True)
    subprocess.run([sys.executable, str(repo / "tools" / "validate-texture-paths.py"), str(package)], check=True)
    subprocess.run([sys.executable, str(repo / "tools" / "validate-runtime-contracts.py"), str(package)], check=True)

    archive_path = repo / "build" / f"EmeraldIsle-{args.version}.zip"
    write_deterministic_archive(package, archive_path)
    digest = sha256_file(archive_path)
    checksum_path = archive_path.with_suffix(".zip.sha256")
    checksum_path.write_text(f"{digest}  {archive_path.name}\n", encoding="utf-8")
    print(f"Release archive: {archive_path}")
    print(f"SHA-256: {digest}")
    if args.candidate:
        print("NEXT RELEASE STEP: record this SHA-256 in the release PR and obtain approval.")
        print("After merge, create the annotated tag and run this command again without --candidate.")
    else:
        print("NEXT RELEASE STEP: confirm this SHA-256 matches the approved candidate.")
        print("Publish this exact ZIP and checksum as the GitHub release assets.")
        print(f"Then run: python3 tools/stage-workshop-release.py {args.version}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
