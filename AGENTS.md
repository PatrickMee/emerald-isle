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
6. the active change's chosen feature record; accepted ADRs; and any
   risk-triggered Architecture Review or Implementation Plan that exists
7. relevant discipline guides

The repository is the source of truth. A prompt cannot silently override project
governance, identity, accepted decisions, milestone scope, or review gates.

## Live Project State

Do not maintain a second status dashboard here. The roadmap owns the active
milestone, the chosen feature record owns approval, the implementation PR owns
Done evidence, and immutable Git tags plus GitHub releases own the released
baseline. Published public definitions, translation keys, save contracts, and
runtime asset paths are compatibility contracts and require migration review
before rename or removal.

## Working Rules

- Classify work as Routine, Standard, or High-Risk under the feature lifecycle.
  Routine maintenance uses normal review. Gameplay requires recorded scope and
  explicit maintainer approval. Standard work normally chooses one issue, direct
  request, or PR as its feature record; use a short specification only when durable
  detail cannot fit clearly there. The implementation PR owns Done evidence.
  High-Risk work adds a repository specification and only its risk-triggered records.
- Keep scope within the active milestone and paths authorized by the spec and any
  applicable architecture/implementation record.
- Verify RimWorld symbols and behavior against the supported current source/build;
  do not rely on memory, stale snippets, or unverified decompilation.
- Treat XML as the default for declarative content. Justify C#; require an ADR for Harmony.
- Preserve stable IDs, save contracts, localization keys, provenance, and licenses.
- Update only affected specs, ADRs, catalogs, glossary, registers, tests, and user
  documentation; link authoritative records instead of creating duplicate summaries.
- Do not update roadmaps, catalogs, indexes, agent instructions, art records, or
  specifications merely to mirror a feature or release status held elsewhere.
- Apply Spec Kit and repository templates proportionally. Do not generate companion
  research, architecture, plan, task, checklist, or evidence files merely because
  a generic workflow can produce them.
- Do not claim completion from static inspection. Verify the affected in-game path
  and add persistence, compatibility, performance, or matrix evidence only when the
  change creates that risk.
- Never approve your own governance gate on behalf of a human reviewer.

<!-- SPECKIT START -->
Use Spec Kit artifacts only for High-Risk work or when a concrete coordination
risk requires them. Do not preload historical research/specification sets unless
the change touches the compatibility contract they explain.
<!-- SPECKIT END -->
