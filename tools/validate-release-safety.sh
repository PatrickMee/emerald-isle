#!/usr/bin/env bash

set -euo pipefail

usage() {
  printf 'Usage: %s [staged-package]\n' "$(basename "$0")"
  printf 'Default staged package: <repository>/build/EmeraldIsle\n'
}

if [[ "${1:-}" == "--help" || "${1:-}" == "-h" ]]; then
  usage
  exit 0
fi

if [[ $# -gt 1 ]]; then
  usage >&2
  exit 64
fi

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd "$script_dir/.." && pwd)"
package="${1:-$repo_root/build/EmeraldIsle}"

if [[ "$package" != /* ]]; then
  package="$repo_root/$package"
fi

if [[ ! -d "$package" ]]; then
  printf 'Staged package does not exist: %s\n' "$package" >&2
  exit 66
fi

unsafe_paths=()

while IFS= read -r -d '' path; do
  relative_path="${path#"$package/"}"
  case "/$relative_path" in
    */Dev/*|*/Developer/*|*/DevTools/*|*/TestPacks/*|*/Testing/*|*/Debug/*)
      unsafe_paths+=("$relative_path")
      ;;
  esac
done < <(find "$package" -print0)

unsafe_contents=()
content_pattern='EI_Dev|EI_Test|DevOnly|DEV_ONLY|Developer Testing Framework|Emerald Isle Developer Tools|patrickmee\.emeraldisle\.devtools|TestPack'

while IFS= read -r -d '' file; do
  if LC_ALL=C grep -nE "$content_pattern" "$file" >/dev/null 2>&1; then
    unsafe_contents+=("${file#"$package/"}")
  fi
done < <(
  find "$package" -type f \
    \( -name '*.xml' -o -name '*.txt' -o -name '*.json' -o -name '*.yml' -o -name '*.yaml' \) \
    -print0
)

if [[ ${#unsafe_paths[@]} -gt 0 || ${#unsafe_contents[@]} -gt 0 ]]; then
  printf 'Release-safety validation failed: developer-only assets are present in the staged package.\n' >&2

  if [[ ${#unsafe_paths[@]} -gt 0 ]]; then
    printf '\nUnsafe paths:\n' >&2
    printf '  %s\n' "${unsafe_paths[@]}" >&2
  fi

  if [[ ${#unsafe_contents[@]} -gt 0 ]]; then
    printf '\nUnsafe content markers:\n' >&2
    printf '  %s\n' "${unsafe_contents[@]}" >&2
  fi

  exit 65
fi

printf 'Release-safety validation passed for %s\n' "$package"
