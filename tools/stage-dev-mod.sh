#!/usr/bin/env bash

set -euo pipefail

usage() {
  printf 'Usage: %s [destination]\n' "$(basename "$0")"
  printf 'Default destination: <repository>/build/EmeraldIsleDevTools\n'
}

if [[ "${1:-}" == "--help" || "${1:-}" == "-h" ]]; then
  usage
  exit 0
fi

if [[ "${1:-}" == -* ]]; then
  printf 'Unknown option: %s\n' "$1" >&2
  usage >&2
  exit 64
fi

if [[ $# -gt 1 ]]; then
  usage >&2
  exit 64
fi

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd "$script_dir/.." && pwd)"
source_root="$repo_root/Dev/Mod"
output="${1:-$repo_root/build/EmeraldIsleDevTools}"

if [[ "$output" != /* ]]; then
  output="$repo_root/$output"
fi

case "$output" in
  /|"$repo_root"|"$repo_root/")
    printf 'Refusing unsafe staging destination: %s\n' "$output" >&2
    exit 64
    ;;
  "$repo_root/build"|"$repo_root/build/"*)
    ;;
  "$repo_root/"*)
    printf 'Refusing destination inside the source tree outside build/: %s\n' "$output" >&2
    exit 64
    ;;
esac

if [[ ! -d "$source_root" ]]; then
  printf 'Developer mod source directory is missing: %s\n' "$source_root" >&2
  exit 65
fi

if ! command -v xmllint >/dev/null 2>&1; then
  printf 'xmllint is required to validate developer package XML.\n' >&2
  exit 69
fi

if ! command -v python3 >/dev/null 2>&1; then
  printf 'python3 is required to generate developer resources.\n' >&2
  exit 69
fi

temporary="${output}.tmp.$$"

cleanup() {
  if [[ -d "$temporary" ]]; then
    rm -rf "$temporary"
  fi
}

trap cleanup EXIT

rm -rf "$temporary"
mkdir -p "$temporary"

while IFS= read -r -d '' source_file; do
  case "$(basename "$source_file")" in
    .gitkeep|.DS_Store)
      continue
      ;;
  esac

  relative_path="${source_file#"$source_root/"}"
  destination_file="$temporary/$relative_path"
  mkdir -p "$(dirname "$destination_file")"
  cp -p "$source_file" "$destination_file"
done < <(find "$source_root" -type f -print0)

python3 "$repo_root/tools/generate-dev-resources.py" \
  --repo-root "$repo_root" \
  --output "$temporary/Defs/ScenarioDefs/EI_Dev_AutoResources.generated.xml"

while IFS= read -r -d '' xml_file; do
  xmllint --noout "$xml_file"
done < <(find "$temporary" -type f -name '*.xml' -print0)

about_file="$temporary/About/About.xml"

if [[ ! -f "$about_file" ]]; then
  printf 'Developer package is missing About/About.xml.\n' >&2
  exit 65
fi

package_id="$(xmllint --xpath 'string(/ModMetaData/packageId)' "$about_file")"
supported_version="$(xmllint --xpath 'string(/ModMetaData/supportedVersions/li)' "$about_file")"

if [[ "$package_id" != "patrickmee.emeraldisle.devtools" ]]; then
  printf 'Unexpected developer packageId: %s\n' "$package_id" >&2
  exit 65
fi

if [[ "$supported_version" != "1.6" ]]; then
  printf 'Unexpected developer package supported RimWorld version: %s\n' "$supported_version" >&2
  exit 65
fi

mkdir -p "$(dirname "$output")"
rm -rf "$output"
mv "$temporary" "$output"

trap - EXIT

printf 'Staged Emerald Isle Developer Tools at %s\n' "$output"
printf 'packageId: %s\n' "$package_id"
printf 'supported RimWorld version: %s\n' "$supported_version"
