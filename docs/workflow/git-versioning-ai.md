# Git, Versioning, and AI Collaboration

## Branching

Use short-lived branches from `main`:

- `feature/<record-id>-<slug>` for approved features
- `fix/<issue>-<slug>` for defects
- `docs/<slug>` for documentation-only changes
- `release/<version>` only for stabilization
- `hotfix/<version>-<slug>` from the affected stable tag

Protect `main`; merge reviewed, passing changes through pull requests. Prefer
squash merges for a coherent feature history. Tags are signed where practical.
Do not maintain long-lived development branches.

## Artifact Versioning

Specs and ADRs are immutable history after acceptance except for status, links,
and explicit amendments. Public def names, translation keys, serialization data,
and package metadata are versioned compatibility surfaces.

## AI Collaboration

AI may research material uncertainties, draft alternatives, implement Ready and
explicitly authorized features, generate tests, and review consistency. AI output
is untrusted until a human verifies claims, licenses, cultural interpretation,
game APIs, current source, and in-game behavior.

Every AI task must identify the active authority and approved scope at the depth
needed for the change. Routine work may rely on the direct request and affected
files. Standard gameplay uses its short issue, request, PR, or spec. High-Risk
work includes its applicable architecture, migration, compatibility, or research
records. Do not create a standalone brief, review, plan, checklist, or process
summary merely because a tool offers one.
Agents must not invent citations, silently broaden scope, introduce dependencies,
or claim success from static inspection alone.

Record meaningful AI assistance in the pull request. Never provide secrets,
private saves, contributor personal data, or unlicensed assets to external models.
Human maintainers own design, cultural, licensing, security, and release decisions.
