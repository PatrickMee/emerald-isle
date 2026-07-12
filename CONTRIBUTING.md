# Contributing to Emerald Isle

Read the [constitution](.specify/memory/constitution.md),
[Design Bible](docs/design/design-bible.md), [vision](docs/vision.md), and
[workflow](docs/workflow/development-workflow.md) before proposing content.

## Before Work Starts

1. Classify the change using the
   [feature lifecycle](docs/workflow/feature-lifecycle.md).
2. Routine maintenance needs no separate feature record. Standard gameplay uses a
   short issue, request, PR, or specification covering player value, scope,
   tradeoff, implementation boundary, compatibility, and acceptance checks.
3. Receive one explicit maintainer approval before gameplay implementation.
   High-Risk work adds only the records required by its concrete risks.

Ideas are welcome, but implementation without an approved feature record may be
closed or redirected.

## Change Expectations

- Keep changes small, cohesive, and independently reviewable.
- Do not mix formatting, refactoring, and feature behavior without justification.
- Add or update tests and in-game verification instructions with behavior changes.
- Record source and license provenance for research, code, audio, and visual work.
- Preserve public definition names and save compatibility unless migration is
  explicitly approved.
- Update affected documentation in the same change; do not create redundant summaries.

## Pull Requests

Describe what changed and why, the authoritative issue/request/spec when one exists,
the affected-path and in-game results, screenshots for visual changes, and any real
compatibility or rollback concern. Do not fill sections that do not apply.

## Conduct and Cultural Care

Critique work, not people. Treat Irish history and living cultures as varied and
contextual. Flag uncertainty, contested interpretations, stereotypes, or sacred
and sensitive material early. Cultural review informs respectful transformation;
it does not require literal simulation.

## Licensing

Source-code contributions are accepted under the repository's MIT License. Creative
assets and writing are governed separately by `CREATIVE_ASSETS_LICENSE.md` and any
asset-specific manifest. Do not contribute material unless you can grant the stated
rights; record external licenses and attribution.
