# Developer Testing Framework

**Status:** Active development infrastructure
**Scope:** Local regression support only; not public gameplay content
**Release rule:** Never include developer-only assets in a public Emerald Isle package

## Purpose

The Developer Testing Framework exists to make Emerald Isle features faster to
verify in RimWorld without weakening release discipline. It provides a separate
development-only companion mod, reusable test scenarios, generated resource starts,
and automated release-safety checks.

This framework supports regression testing for crops, production chains, buildings,
recipes, research, animals, traders, storage, graphics, nutrition, and balance
work. It does not change the public mod.

## Architecture

The framework has four parts:

1. `Dev/Mod/`: source for the development-only companion RimWorld mod.
2. `Dev/TestPacks/`: optional feature-owned resource declarations.
3. `tools/stage-dev-mod.sh`: stages the companion mod for local testing.
4. `tools/validate-release-safety.sh`: fails production staging if developer-only
   assets or identifiers enter the release package.

The public package and developer package are separate:

| Package | Staging command | PackageId | Release status |
|---|---|---|---|
| Emerald Isle | `tools/stage-mod.sh` | `patrickmee.emeraldisle` | Public release candidate |
| Emerald Isle Developer Tools | `tools/stage-dev-mod.sh` | `patrickmee.emeraldisle.devtools` | Local-only; never released |

The developer package depends on and loads after Emerald Isle. It may contain
developer scenarios and generated testing resources because it is never part of
the public artifact.

## Usage

Stage the public package:

```sh
./tools/stage-mod.sh
```

Stage the developer companion package:

```sh
./tools/stage-dev-mod.sh
```

For local RimWorld testing, stage both packages into the RimWorld Mods directory:

```sh
./tools/stage-mod.sh "/Users/patrickmee/Library/Application Support/Steam/steamapps/common/RimWorld/RimWorldMac.app/Mods/EmeraldIsle"
./tools/stage-dev-mod.sh "/Users/patrickmee/Library/Application Support/Steam/steamapps/common/RimWorld/RimWorldMac.app/Mods/EmeraldIsleDevTools"
```

Enable both mods in RimWorld with Emerald Isle loaded before Emerald Isle Developer
Tools.

## Developer Scenarios

The companion package provides development-only scenarios for common verification
paths:

- `EI dev: empty construction`
- `EI dev: farming`
- `EI dev: production chain`
- `EI dev: combat`
- `EI dev: trade`
- `EI dev: long-term colony`
- `EI dev: generated resources`

The generated resources scenario includes common vanilla development resources and
all discovered Emerald Isle item resources under `Defs/ThingDefs_Items/`.

## Resource Generation

`tools/generate-dev-resources.py` scans:

1. built-in common development resources
2. Emerald Isle item definitions under `Defs/ThingDefs_Items/`
3. optional feature test packs under `Dev/TestPacks/`

The generated scenario is written into the staged developer package. Generated XML
is not committed as runtime content.

Current built-in resources include:

- wood
- steel
- components
- all five vanilla stone block types
- simple meals
- industrial medicine
- silver

Emerald Isle item definitions are added automatically when a feature adds an
`EI_` item under `Defs/ThingDefs_Items/`. This covers crops, intermediate products,
and finished products when they use the normal project item structure.

## Feature Test Packs

A feature should add a test pack only when automatic item discovery is not enough
or when the feature needs custom quantities.

Example:

```xml
<?xml version="1.0" encoding="utf-8"?>
<DeveloperTestPack>
  <defName>FS999_Example</defName>
  <label>Example future feature</label>
  <resources>
    <li defName="EI_ExampleRawItem" count="500" />
    <li defName="EI_ExampleFinishedItem" count="100" />
  </resources>
</DeveloperTestPack>
```

Rules:

- Put packs in `Dev/TestPacks/`.
- Keep each pack owned by one feature.
- Do not edit another feature's pack to register new assets.
- Use production `defName` values; do not create dev aliases for public content.
- Files ending in `.disabled` are ignored.

## Regression Coverage

The framework is intended to reduce manual setup time for:

- XML load checks
- definition presence and references
- recipe/bill generation
- production chain verification
- building placement and material testing
- graphics checks at normal zoom
- research unlock checks
- trader and market-value checks
- storage category checks
- nutrition and food policy checks
- balance and pacing playtests

It does not replace in-game validation. It makes in-game validation faster.

## Release Safeguards

The production package is protected by several layers:

1. `tools/stage-mod.sh` copies only runtime roots such as `About`, `Defs`,
   `Languages`, and `Textures`; it does not copy `Dev/`.
2. `tools/stage-mod.sh` runs `tools/validate-release-safety.sh` against the staged
   package before completing.
3. CI runs the same release-safety validator against `build/EmeraldIsle`.
4. CI also stages the developer package separately to ensure the framework itself
   remains valid.

The release-safety validator fails on developer-only paths, package IDs, and
identifier markers such as `EI_Dev`, `EI_Test`, `DevOnly`, and the developer
packageId.

## Extension Rules

- Keep public gameplay definitions in the normal runtime roots.
- Keep developer-only scenarios, test resources, and experimental aids under
  `Dev/`.
- Add feature-owned test packs instead of editing shared generated output.
- Do not add C# or Harmony for developer tooling unless a real recurring testing
  problem cannot be solved with XML and scripts.
- Do not let developer convenience become a public compatibility contract.

## Known Limits

The first implementation generates item resource scenarios. Future animal,
trader, quest, or research-specific test helpers should extend this framework
only when an implemented feature demonstrates the need.
