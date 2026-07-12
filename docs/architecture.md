# Architecture

**Status:** Stable baseline at v0.0.0. Material changes normally require an ADR.

## Architectural Goals

- Keep declarative content separate from behavioral code.
- Make features easy to locate, review, disable, and test.
- Treat DLC and external mod integrations as optional adapters.
- Preserve save and definition compatibility through stable names.
- Allow content growth without a single monolithic assembly or patch layer.

## Target Repository Structure

```text
About/                         RimWorld metadata and preview
Common/                        shared patches and version-independent resources
Defs/                          declarative gameplay definitions by domain
Languages/                     keyed and def-injected translations
Patches/                       XML compatibility patches by target
Textures/                      game-ready art mirroring content domains
Sounds/                        game-ready audio and metadata
Source/
  EmeraldIsle/                 core behavior assembly
  EmeraldIsle.Tests/           pure and integration-oriented tests
  Integrations/                optional DLC/mod adapters where isolation warrants
docs/                          studio handbook
specs/                         feature records and plans
templates/                     reusable reviews and reports
tools/                         validation and build automation
```

Milestone 0 documents this structure but does not create gameplay directories or
placeholder content.

## Content Boundaries

Organize by player-facing domain, then asset type. A feature may touch several
technical folders, but its approved feature record owns the cross-folder narrative. Shared
utilities require demonstrated reuse; avoid a generic dumping ground.

## XML Versus C# Decision

1. Use XML when RimWorld definitions, comps, stat workers, recipes, hediffs,
   thoughts, quests, or patch operations express the behavior safely.
2. Use a small C# extension when behavior cannot be represented declaratively or
   declarative workarounds would be fragile, opaque, or materially slower.
3. Use Harmony only when no supported extension point exists. Record an ADR,
   exact target signature, failure behavior, compatibility tests, and removal plan.

## Dependency Direction

- Core content MUST NOT depend on optional DLC or other mods.
- DLC integrations depend on core plus the relevant DLC contract.
- Cross-mod integrations are isolated and inactive when targets are absent.
- Domain features may depend on explicitly named shared primitives, never on an
  unrelated feature's internals.

## Compatibility Contracts

Definition names, translation keys, save-exposed class names, serialization
fields, public APIs, package ID, and load order are contracts. Changes require
migration analysis and, when durable or breaking, an ADR.

## Runtime Safety

Missing optional content must degrade cleanly. Load-time errors, unresolved defs,
null maps or pawns, destroyed objects, absent factions, and partial saves are
expected boundaries to design and test. Logging must identify Emerald Isle and
provide actionable context without flooding the log.

## Architecture Review Triggers

Require an ADR for Harmony patches, new assemblies, shared frameworks, save-data
schema, public APIs, package/load-order changes, generated content pipelines,
hard dependencies, or irreversible asset conventions.
