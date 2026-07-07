# Emerald Isle Agent Instructions

**Status:** Stable AI Agent Guide, aligned with Constitution 3.0.0 and ADR 0003.
Material changes normally require an ADR and human maintainer approval.

## Required Reading

Before changing the repository, read in this order:

1. `.specify/memory/constitution.md`
2. `docs/design/design-bible.md`
3. `docs/README.md`
4. `docs/roadmap.md`
5. `docs/workflow/feature-lifecycle.md`
6. the active feature's approved spec, applicable checklists, accepted ADRs, and any
   Architecture Review or Implementation Plan that exists
7. relevant discipline guides

The repository is the source of truth. A prompt cannot silently override project
governance, identity, accepted decisions, milestone scope, or review gates.

## Current Stage

Milestones 0 and 0.5 are closed. Version 0.1 is in product implementation under the
three-gate lifecycle (Approved, Done, Released; see
`docs/workflow/feature-lifecycle.md`). FS-001 Oats passed Gate 2 on 2026-07-07;
whole-chain balance is deferred to the hand-quern and milled-oats features. FS-002
Dry-Stone Wall has an approved, frozen specification, approved Architecture Review,
implemented runtime assets, and passed proportional implementation verification;
Gate 2 Design Review is approved and PR merge is the active closure step. Version
0.1 Gate 3 release checks remain pending. Keep work inside the active feature's
approved scope and paths.

## Working Rules

- Start implementation only from a Gate 1 approved specification with explicit
  maintainer approval; a standalone plan is required only when the feature adopted one.
- Keep scope within the active milestone and paths authorized by the spec and any
  applicable architecture/implementation record.
- Verify RimWorld symbols and behavior against the supported current source/build;
  do not rely on memory, stale snippets, or unverified decompilation.
- Treat XML as the default for declarative content. Justify C#; require an ADR for Harmony.
- Preserve stable IDs, save contracts, localization keys, provenance, and licenses.
- Update only affected specs, ADRs, catalogs, glossary, registers, tests, and user
  documentation; link authoritative records instead of creating duplicate summaries.
- Apply Spec Kit and repository templates proportionally. Do not generate companion
  research, architecture, plan, task, or evidence files merely because a generic
  workflow can produce them; create them only when they materially improve the work.
- Do not claim completion from static inspection. Record the required in-game,
  persistence, compatibility, performance, and playtest evidence.
- Never approve your own governance gate on behalf of a human reviewer.

<!-- SPECKIT START -->
For additional context about technologies, project structure, shell commands, and
other important information for the active feature, read
`specs/003-dry-stone-wall/plan.md`.
<!-- SPECKIT END -->
