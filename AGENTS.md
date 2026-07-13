# Emerald Isle Agent Instructions

**Status:** Stable AI Agent Guide, aligned with Constitution 4.0.0 and ADR 0004.
Material changes normally require an ADR and human maintainer approval.

## Required Reading

Before changing the repository, read in this order:

1. `.specify/memory/constitution.md`
2. `docs/design/design-bible.md`
3. `docs/README.md`
4. `docs/roadmap.md`
5. `docs/workflow/feature-lifecycle.md`
6. the active change's approved issue, request, PR, or spec; accepted ADRs; and any
   risk-triggered Architecture Review or Implementation Plan that exists
7. relevant discipline guides

The repository is the source of truth. A prompt cannot silently override project
governance, identity, accepted decisions, milestone scope, or review gates.

## Current Stage

Milestones 0 and 0.5 are closed. Version 0.1, The First Holding, passed all three
gates and is released as `v0.1.0`. FS-001 Oats, FS-002 Dry-Stone Wall, FS-003
Hand Quern, FS-004 Milled Oats, and FS-005 Oat Foods are released compatibility
contracts. Do not rename or remove their public definitions, translation keys,
or runtime asset paths without migration review. No later milestone authorizes
gameplay implementation until its scope receives explicit maintainer approval in
an appropriate feature record. FS-006 Linen Household is implemented and passed
maintainer playtesting on 2026-07-13; it remains unreleased pending integration.

## Working Rules

- Classify work as Routine, Standard, or High-Risk under the feature lifecycle.
  Routine maintenance uses normal review. Gameplay requires recorded scope and
  explicit maintainer approval; Standard work may use an issue, request, PR, or
  spec, while High-Risk work adds only its risk-triggered records.
- Keep scope within the active milestone and paths authorized by the spec and any
  applicable architecture/implementation record.
- Verify RimWorld symbols and behavior against the supported current source/build;
  do not rely on memory, stale snippets, or unverified decompilation.
- Treat XML as the default for declarative content. Justify C#; require an ADR for Harmony.
- Preserve stable IDs, save contracts, localization keys, provenance, and licenses.
- Update only affected specs, ADRs, catalogs, glossary, registers, tests, and user
  documentation; link authoritative records instead of creating duplicate summaries.
- Apply Spec Kit and repository templates proportionally. Do not generate companion
  research, architecture, plan, task, checklist, or evidence files merely because
  a generic workflow can produce them.
- Do not claim completion from static inspection. Verify the affected in-game path
  and add persistence, compatibility, performance, or matrix evidence only when the
  change creates that risk.
- Never approve your own governance gate on behalf of a human reviewer.

<!-- SPECKIT START -->
FS-006 Linen Household is the completed post-0.1 implementation awaiting
integration. Read `docs/specifications/FS-006-linen-household.md` before changing
its XML-first slice. Do not preload the Version 0.1 research/specification set
unless changing one of its released compatibility contracts.
<!-- SPECKIT END -->
