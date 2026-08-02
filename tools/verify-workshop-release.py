#!/usr/bin/env python3
"""Verify Steam's public item and a subscriber cache against a release package."""

from __future__ import annotations

import argparse
import json
import sys
import tempfile
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

from release_lib import directory_manifest, directory_size, extract_archive


ITEM_ID = "3763433723"


def public_details() -> dict[str, object]:
    data = urllib.parse.urlencode({"itemcount": "1", "publishedfileids[0]": ITEM_ID}).encode()
    request = urllib.request.Request(
        "https://api.steampowered.com/ISteamRemoteStorage/GetPublishedFileDetails/v1/",
        data=data,
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        payload = json.load(response)
    return payload["response"]["publishedfiledetails"][0]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("version")
    parser.add_argument("--archive", type=Path, help="downloaded GitHub release ZIP")
    parser.add_argument(
        "--subscription",
        type=Path,
        default=Path.home() / f"Library/Application Support/Steam/steamapps/workshop/content/294100/{ITEM_ID}",
    )
    args = parser.parse_args()
    repo = Path(__file__).resolve().parent.parent
    archive = (args.archive or repo / "build" / "downloads" / f"EmeraldIsle-{args.version}.zip").resolve()
    if args.archive is None:
        archive.parent.mkdir(parents=True, exist_ok=True)
        url = f"https://github.com/PatrickMee/emerald-isle/releases/download/{args.version}/{archive.name}"
        print(f"Downloading exact GitHub release asset: {url}")
        urllib.request.urlretrieve(url, archive)
    with tempfile.TemporaryDirectory(prefix="emerald-isle-verify-") as temporary:
        try:
            expected = extract_archive(archive, Path(temporary))
        except ValueError as error:
            print(f"Verification refused: {error}", file=sys.stderr)
            return 1
        build_info_path = expected / "About" / "BuildInfo.txt"
        if not build_info_path.is_file():
            print("Verification refused: archive is missing About/BuildInfo.txt", file=sys.stderr)
            return 1
        build_info = build_info_path.read_text(encoding="utf-8")
        if f"version={args.version}\n" not in build_info:
            print("Verification refused: archive BuildInfo version does not match", file=sys.stderr)
            return 1
        details = public_details()
        expected_size = directory_size(expected)
        public_size = int(details["file_size"])
        updated = datetime.fromtimestamp(int(details["time_updated"]), tz=timezone.utc).isoformat()
        print(f"Steam public content manifest: {details.get('hcontent_file')}")
        print(f"Steam public update time: {updated}")
        print(f"Expected/public uncompressed bytes: {expected_size}/{public_size}")
        if public_size != expected_size:
            print("FAILED: Steam's public package size does not match the release artifact.", file=sys.stderr)
            return 1
        subscription = args.subscription.resolve()
        if not subscription.is_dir() or directory_manifest(subscription) != directory_manifest(expected):
            print("FAILED: this machine's Workshop subscription is not the published release artifact.", file=sys.stderr)
            print("Exit RimWorld and Steam, restart Steam, then unsubscribe/resubscribe and run this check again.", file=sys.stderr)
            return 1
    print(f"PASS: Steam and this subscriber both contain the exact {args.version} release content.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
