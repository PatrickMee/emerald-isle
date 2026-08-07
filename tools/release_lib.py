#!/usr/bin/env python3
"""Shared helpers for Emerald Isle release tooling."""

from __future__ import annotations

import hashlib
import os
import shutil
import zipfile
from pathlib import Path, PurePosixPath


MAX_ARCHIVE_FILES = 10_000
MAX_ARCHIVE_BYTES = 512 * 1024 * 1024


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def directory_manifest(root: Path) -> dict[str, tuple[int, str]]:
    return {
        path.relative_to(root).as_posix(): (path.stat().st_size, sha256_file(path))
        for path in sorted(root.rglob("*"))
        if path.is_file()
    }


def directory_size(root: Path) -> int:
    return sum(size for size, _digest in directory_manifest(root).values())


def validate_archive_members(archive: zipfile.ZipFile) -> None:
    members = archive.infolist()
    if len(members) > MAX_ARCHIVE_FILES:
        raise ValueError("archive contains too many entries")
    if sum(member.file_size for member in members) > MAX_ARCHIVE_BYTES:
        raise ValueError("archive expands beyond the 512 MiB safety limit")
    names: set[str] = set()
    for member in members:
        if member.flag_bits & 0x1:
            raise ValueError(f"archive contains an encrypted entry: {member.filename}")
        if "\\" in member.filename:
            raise ValueError(f"archive path uses a backslash: {member.filename}")
        if member.filename in names:
            raise ValueError(f"archive contains a duplicate path: {member.filename}")
        names.add(member.filename)
        path = PurePosixPath(member.filename)
        if path.is_absolute() or ".." in path.parts:
            raise ValueError(f"unsafe archive path: {member.filename}")
        if not path.parts or path.parts[0] != "EmeraldIsle":
            raise ValueError(f"archive member is outside EmeraldIsle/: {member.filename}")
        mode = member.external_attr >> 16
        if mode and (mode & 0o170000) == 0o120000:
            raise ValueError(f"archive contains a symbolic link: {member.filename}")


def extract_archive(archive_path: Path, destination: Path) -> Path:
    with zipfile.ZipFile(archive_path) as archive:
        validate_archive_members(archive)
        archive.extractall(destination)
    package = destination / "EmeraldIsle"
    if not (package / "About" / "About.xml").is_file():
        raise ValueError("archive is missing EmeraldIsle/About/About.xml")
    return package


def replace_directory(source: Path, destination: Path) -> None:
    """Replace one explicitly named EmeraldIsle directory, retaining one unscanned backup."""
    if destination.name != "EmeraldIsle":
        raise ValueError(f"refusing unexpected destination: {destination}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    incoming = destination.with_name("EmeraldIsle.incoming")
    legacy_previous = destination.with_name("EmeraldIsle.previous")
    backup_root = destination.parent.parent / "ModStagingBackups"
    previous = backup_root / "EmeraldIsle.previous"
    for path in (destination, incoming, legacy_previous, backup_root, previous):
        if path.is_symlink():
            raise ValueError(f"refusing symbolic-link staging path: {path}")
    if incoming.exists():
        shutil.rmtree(incoming)
    shutil.copytree(source, incoming)
    backup_root.mkdir(parents=True, exist_ok=True)
    if previous.exists():
        shutil.rmtree(previous)
    if legacy_previous.exists():
        shutil.rmtree(legacy_previous)
    if destination.exists():
        os.replace(destination, previous)
    os.replace(incoming, destination)
