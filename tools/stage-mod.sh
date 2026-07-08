#!/usr/bin/env bash

set -euo pipefail

usage() {
  printf 'Usage: %s [--verify-empty] [destination]\n' "$(basename "$0")"
  printf 'Default destination: <repository>/build/EmeraldIsle\n'
}

verify_empty=false

if [[ "${1:-}" == "--help" || "${1:-}" == "-h" ]]; then
  usage
  exit 0
fi

if [[ "${1:-}" == "--verify-empty" ]]; then
  verify_empty=true
  shift
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
output="${1:-$repo_root/build/EmeraldIsle}"

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

if ! command -v xmllint >/dev/null 2>&1; then
  printf 'xmllint is required to validate About/About.xml.\n' >&2
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
mkdir -p "$temporary/Defs"
mkdir -p "$temporary/Textures"
mkdir -p "$temporary/Languages/English/DefInjected/ThingDef"

runtime_directories=(About Defs Languages Patches Textures Sounds Assemblies)

for directory in "${runtime_directories[@]}"; do
  source_directory="$repo_root/$directory"

  if [[ ! -d "$source_directory" ]]; then
    continue
  fi

  while IFS= read -r -d '' source_file; do
    case "$(basename "$source_file")" in
      .gitkeep|.DS_Store)
        continue
        ;;
    esac

    relative_path="${source_file#"$repo_root/"}"
    destination_file="$temporary/$relative_path"
    mkdir -p "$(dirname "$destination_file")"
    cp -p "$source_file" "$destination_file"
  done < <(find "$source_directory" -type f -print0)
done

while IFS= read -r -d '' xml_file; do
  xmllint --noout "$xml_file"
done < <(find "$temporary" -type f -name '*.xml' -print0)

about_file="$temporary/About/About.xml"

if [[ ! -f "$about_file" ]]; then
  printf 'Staged package is missing About/About.xml.\n' >&2
  exit 65
fi

xmllint --noout "$about_file"

package_id="$(xmllint --xpath 'string(/ModMetaData/packageId)' "$about_file")"
supported_version="$(xmllint --xpath 'string(/ModMetaData/supportedVersions/li)' "$about_file")"

if [[ "$package_id" != "patrickmee.emeraldisle" ]]; then
  printf 'Unexpected packageId: %s\n' "$package_id" >&2
  exit 65
fi

if [[ "$supported_version" != "1.6" ]]; then
  printf 'Unexpected supported RimWorld version: %s\n' "$supported_version" >&2
  exit 65
fi

if [[ "$verify_empty" == true ]]; then
  for directory in Defs Textures Languages Patches Sounds Assemblies; do
    if [[ -d "$temporary/$directory" ]] &&
       [[ -n "$(find "$temporary/$directory" -type f -print -quit)" ]]; then
      printf 'Empty-package verification failed: %s contains runtime files.\n' "$directory" >&2
      exit 65
    fi
  done
fi

release_safety_validator="$repo_root/tools/validate-release-safety.sh"
if [[ -f "$release_safety_validator" ]]; then
  bash "$release_safety_validator" "$temporary"
else
  printf 'Release-safety validator is missing: %s\n' "$release_safety_validator" >&2
  exit 65
fi

mkdir -p "$(dirname "$output")"
rm -rf "$output"
mv "$temporary" "$output"

trap - EXIT

printf 'Staged Emerald Isle at %s\n' "$output"
printf 'packageId: %s\n' "$package_id"
printf 'supported RimWorld version: %s\n' "$supported_version"

if [[ "$verify_empty" == true ]]; then
  printf 'empty package verification: passed\n'
fi
