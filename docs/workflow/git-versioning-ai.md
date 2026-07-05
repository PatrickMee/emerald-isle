# Git, Versioning, and AI Collaboration

## Branching

Use short-lived branches from `main`:

- `feature/<spec-id>-<slug>` for approved features
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

Every AI task must receive the constitution, active specification, any applicable
architecture or implementation record, allowed scope, paths it may change,
relevant game/version context, and required verification. Do not create a
standalone research brief, Architecture Review, Implementation Plan, or process
summary unless it resolves material uncertainty or improves execution,
maintenance, onboarding, or a future decision.
Agents must not invent citations, silently broaden scope, introduce dependencies,
or claim success from static inspection alone.

Record meaningful AI assistance in the pull request. Never provide secrets,
private saves, contributor personal data, or unlicensed assets to external models.
Human maintainers own design, cultural, licensing, security, and release decisions.
