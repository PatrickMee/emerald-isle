# ADR 0002: Version 0.1 Uses a Root-Level, XML-First Package Contract

**Status:** Accepted<br>
**Date:** 2026-07-05<br>
**Decision owner:** Patrick Mee<br>
**Accepted by/date:** Patrick Mee, 2026-07-05<br>
**Related:** `docs/engineering/build-strategy.md`,
`docs/release/package-build-contract.md`, AR-001, IP-001

## Context

Emerald Isle has approved its first feature architecture but does not yet have a
loadable RimWorld mod package. The repository needs the smallest stable package and
staging contract that can appear in RimWorld 1.6's Mods list, load with Core only,
and later receive XML-first Version 0.1 content without changing package identity.

The current scope contains no gameplay definitions, code, patches, or assets. The
contract must not create placeholder content or speculative C# infrastructure.

## Decision

### Package Identity

- Display name: `Emerald Isle`
- Author: `Patrick Mee`
- Package ID: `patrickmee.emeraldisle`
- Supported RimWorld version: `1.6`
- Project URL: `https://github.com/PatrickMee/emerald-isle`

The package ID is lowercase to avoid case-dependent identity differences and is a
durable compatibility contract.

### Package Layout

RimWorld metadata lives at `About/About.xml`. Runtime content uses root-level
`Defs`, `Languages`, `Textures`, `Patches`, `Sounds`, and `Assemblies` directories
only when content requires them.

The initial repository tracks empty `Defs`, `Textures`, and English DefInjected
language structure with `.gitkeep` markers. The staging process excludes these
markers and creates the empty runtime directories explicitly.

`LoadFolders.xml` is omitted. Emerald Isle supports one game version and has no
version-specific or DLC-conditional content. Adding load folders later requires a
demonstrated content boundary and architecture review.

`Assemblies` and `Source` are omitted. No accepted feature requires C#. If C# becomes
necessary, a later ADR must select the .NET target, pinned SDK/compiler, analyzers,
test framework, references, assembly layout, and CI build environment before source
or binaries are added.

### Staging Contract

`tools/stage-mod.sh` creates a clean package at `build/EmeraldIsle` by default or at
an explicit dedicated destination. It copies only recognized runtime directories,
excludes repository markers and editor metadata, validates `About/About.xml`, and
checks the stable package ID and supported-version declaration.

The `--verify-empty` mode additionally fails if any runtime content exists under
`Defs`, `Textures`, `Languages`, `Patches`, `Sounds`, or `Assemblies`. This mode is
the acceptance check for the infrastructure-only package and is intentionally not
used after gameplay content is approved.

The staging environment is Bash on macOS or Linux with `xmllint` from libxml2.
Windows contributors use WSL or an equivalent environment until a native workflow is
justified. The intended future CI environment is a Linux runner executing the same
script; no CI workflow is added before the repository has approved runtime content.

### Build and Test Scope

There is no compilation, dependency restore, unit-test framework, analyzer, or
proprietary game reference in the empty package. Static verification covers metadata,
runtime-file allowlisting, absence of gameplay content, and staging determinism.

RimWorld itself remains the authority for package discovery and load behavior. The
exact staged package was verified by Patrick Mee in RimWorld 1.6.4871 rev597 with
Core only; the Mods list, restart, and Player.log checks passed on 2026-07-05.

## Alternatives Considered

### Add `LoadFolders.xml` Immediately

Rejected. One supported game version and no conditional content require no load
mapping. An unused mapping adds a compatibility surface without value.

### Create Empty `Assemblies` and `Source` Trees

Rejected. Empty code scaffolding implies an architecture the approved XML-only
feature does not need and would force premature .NET and test-toolchain decisions.

### Run the Repository Directly as the Mod

Rejected. RimWorld would see documentation, source-control, test, and contributor
files that do not belong in a distributable mod. A clean staging boundary is required
for reliable verification and release.

### Use Version-Specific `1.6/` Content Immediately

Rejected. Root-level content is the simplest correct layout for a package supporting
only RimWorld 1.6. A version folder is introduced only when multiple load contracts
exist.

## Consequences

### Positive

- The package identity and supported-version declaration are stable before features
  create save or integration dependencies.
- The staged package contains only files RimWorld needs.
- The same staging command supports the empty package and later XML content.
- C#, Harmony, DLC adapters, and version routing remain absent until justified.

### Negative

- Bash and `xmllint` are required for staging.
- Windows requires WSL or an equivalent environment.
- Human in-game verification is still required; static checks cannot prove Mods-list
  discovery or a clean RimWorld load.

### Neutral

- Empty directory markers exist only for source-control structure and are never
  included in staged packages.
- Preview art and Workshop metadata remain release concerns, not validity
  requirements for this empty local package.

## Validation

The decision is validated when:

1. `./tools/stage-mod.sh --verify-empty` succeeds.
2. The staged package contains `About/About.xml` and no runtime content files.
3. The metadata reports `patrickmee.emeraldisle` and RimWorld `1.6`.
4. The package appears as `Emerald Isle` in the RimWorld 1.6 Mods list.
5. Core plus Emerald Isle restarts with no Emerald Isle error or warning.
6. Player.log contains no package, metadata, XML, or content error caused by the mod.

All six validation conditions passed on 2026-07-05. The expected empty-package log
message, `Mod Emerald Isle did not load any content`, was recorded without an Emerald
Isle error or warning.

## Revisit When

- Emerald Isle supports another RimWorld version.
- DLC or version-specific content requires load-folder routing.
- An accepted feature requires C#, an assembly, Harmony, or proprietary references.
- CI or a native Windows staging workflow becomes a release requirement.
- The package ID, author identity, or repository location must change.
