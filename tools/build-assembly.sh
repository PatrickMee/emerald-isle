#!/usr/bin/env bash

set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd "$script_dir/.." && pwd)"
output="${1:-$repo_root/build/managed/EmeraldIsle.dll}"
managed_dir="${RIMWORLD_MANAGED_DIR:-}"
framework_dir="${MONO_FRAMEWORK_REF_DIR:-/opt/homebrew/lib/mono/4.7.2-api}"
expected_game_sha256=6d06b881d59cb54d05b674e8631fa2e8b1629dc8b8dd294a5bcc928f1e5d2148
expected_compiler_version=3.9.0-6.21124.20

if [[ -z "$managed_dir" || ! -d "$managed_dir" ]]; then
  printf 'Set RIMWORLD_MANAGED_DIR to the installed RimWorld 1.6 Managed directory.\n' >&2
  exit 69
fi

if ! command -v csc >/dev/null 2>&1 || [[ "$(csc -version)" != "$expected_compiler_version"* ]]; then
  printf 'Mono Roslyn csc %s is required.\n' "$expected_compiler_version" >&2
  exit 69
fi

for reference in "$managed_dir/Assembly-CSharp.dll" "$managed_dir/UnityEngine.CoreModule.dll" \
                 "$managed_dir/netstandard.dll" \
                 "$framework_dir/mscorlib.dll" "$framework_dir/System.dll" "$framework_dir/System.Core.dll"; do
  if [[ ! -f "$reference" ]]; then
    printf 'Missing compile reference: %s\n' "$reference" >&2
    exit 69
  fi
done

actual_game_sha256="$(python3 - "$managed_dir/Assembly-CSharp.dll" <<'PY'
import hashlib
import pathlib
import sys
print(hashlib.sha256(pathlib.Path(sys.argv[1]).read_bytes()).hexdigest())
PY
)"
if [[ "$actual_game_sha256" != "$expected_game_sha256" ]]; then
  printf 'RimWorld Assembly-CSharp.dll differs from the verified 1.6.4871 rev597 build. Revalidate the API before compiling.\n' >&2
  exit 65
fi

sources=("$repo_root"/Source/EmeraldIsle/*.cs)
if [[ ! -f "${sources[0]}" ]]; then
  printf 'No Emerald Isle C# source found.\n' >&2
  exit 65
fi

mkdir -p "$(dirname "$output")"
temporary_dir="${output}.tmp.$$"
mkdir -p "$temporary_dir"
trap 'rm -rf "$temporary_dir"' EXIT

csc -nologo -noconfig -target:library -langversion:7.3 -deterministic+ \
  -pathmap:"$repo_root=/_/EmeraldIsle" -optimize+ -warnaserror+ -nostdlib+ \
  -out:"$temporary_dir/EmeraldIsle.dll" \
  -reference:"$framework_dir/mscorlib.dll" \
  -reference:"$framework_dir/System.dll" \
  -reference:"$framework_dir/System.Core.dll" \
  -reference:"$managed_dir/Assembly-CSharp.dll" \
  -reference:"$managed_dir/UnityEngine.CoreModule.dll" \
  -reference:"$managed_dir/netstandard.dll" \
  "${sources[@]}"

if [[ ! -s "$temporary_dir/EmeraldIsle.dll" ]]; then
  printf 'Compiler produced no EmeraldIsle.dll.\n' >&2
  exit 65
fi

mv "$temporary_dir/EmeraldIsle.dll" "$output"
rm -rf "$temporary_dir"
trap - EXIT
printf 'Built EmeraldIsle.dll from %s C# sources at %s\n' "${#sources[@]}" "$output"
