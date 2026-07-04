# Emerald Isle Agent Instructions

**Status:** Stable AI Agent Guide baseline at v0.0.0. Material changes normally
require an ADR and human maintainer approval.

## Required Reading

Before changing the repository, read in this order:

1. `.specify/memory/constitution.md`
2. `docs/design/design-bible.md`
3. `docs/README.md`
4. `docs/roadmap.md`
5. `docs/workflow/feature-lifecycle.md`
6. the active feature's `spec.md`, `plan.md`, checklists, and accepted ADRs
7. relevant discipline guides

The repository is the source of truth. A prompt cannot silently override project
governance, identity, accepted decisions, milestone scope, or review gates.

## Current Stage

Milestones 0 and 0.5 are closed. Version 0.1 is research-and-planning only. Do not
add gameplay XML, C#, textures, audio, RimWorld package metadata, or implementation
scaffolding until the research sprint and Version 0.1 plan are reviewed and a
feature passes Definition of Ready.

## Working Rules

- Start implementation only from an accepted, planned, Ready feature.
- Keep scope within the active milestone and exact paths authorized by the plan.
- Verify RimWorld symbols and behavior against the supported current source/build;
  do not rely on memory, stale snippets, or unverified decompilation.
- Treat XML as the default for declarative content. Justify C#; require an ADR for Harmony.
- Preserve stable IDs, save contracts, localization keys, provenance, and licenses.
- Update specs, ADRs, catalogs, glossary, registers, tests, and user documentation
  in the same change when they are affected.
- Do not claim completion from static inspection. Record the required in-game,
  persistence, compatibility, performance, and playtest evidence.
- Never approve your own governance gate on behalf of a human reviewer.

<!-- SPECKIT START -->
For additional context about technologies to be used, project structure,
shell commands, and other important information, read the current plan.
<!-- SPECKIT END -->
