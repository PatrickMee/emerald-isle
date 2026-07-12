# ADR 0003: Three-Gate Feature Lifecycle

**Amended by:** [ADR 0004](0004-risk-tiered-hobby-workflow.md), which preserves
the three outcomes while making records and verification risk-tiered.

**Status:** Accepted
**Date:** 2026-07-07
**Decision owners:** Patrick Mee
**Related:** `.specify/memory/constitution.md`,
`docs/workflow/feature-lifecycle.md`, `docs/workflow/development-workflow.md`,
`docs/workflow/definition-of-ready.md`, `docs/workflow/definition-of-done.md`,
`docs/workflow/product-governance.md`, `GOVERNANCE.md`, FS-001

## Context

The project is maintained by a single human working with AI agents. The
Constitution 2.0.0 lifecycle defines seven sequential gates per feature
(research, specification, ready, implementation, playtest, design review,
release), each with its own checklist, approval, and evidence record. FS-001
Oats, a deliberately small XML-only crop, required roughly a dozen governance
artifacts across research briefs, a specification, an architecture review, an
implementation plan, acceptance checklists, and readiness sign-off before its
first in-game verification.

Several gates exist to coordinate reviewers and contributors who do not yet
exist. The Ready gate authorizes a maintainer who is also the spec author. The
design review gate asks the designer to review the feature the designer just
playtested. The per-feature release gate duplicates the per-version release
checklist. The Constitution's Process Proportionality section already directs
the team to retire artifacts that cost more than the decisions they protect.

The cultural and Irish-language review requirement in `GOVERNANCE.md` requires
a suitably qualified reviewer for every feature that touches such content. No
such reviewer is currently appointed, which makes the requirement a standing
blocker on each individual feature.

## Decision Drivers

- One maintainer holds every non-cultural review role until reviewers are appointed.
- Gates must catch real failure: broken gameplay, save damage, cultural harm,
  release regressions, and unverified AI output.
- Gates that only coordinate absent humans add cost without protection.
- The roadmap implies dozens of features; per-feature overhead compounds.
- The Constitution's Process Proportionality principle requires simplification
  when artifact cost exceeds protective value.

## Options Considered

### Keep the Seven-Gate Lifecycle

- Benefits: No migration; maximum ceremony available if the team grows.
- Costs and risks: Eight to fifteen artifacts per feature; estimated eight or
  more days of process per small feature; high abandonment risk for a solo,
  multi-year project.

### Abandon Gates in Favor of Ad-Hoc Development

- Benefits: Fastest possible iteration.
- Costs and risks: Loses the protections that matter with AI-heavy
  implementation: verified in-game evidence, balance discipline, cultural
  review, stable identifiers, and release quality. Contradicts the Constitution.

### Collapse to Three Gates with Preserved Evidence Requirements

- Benefits: Keeps every failure-catching check while removing coordination
  ceremony; matches actual team shape; per-version release amortizes release
  cost across features.
- Costs and risks: Requires a Constitution amendment and workflow document
  updates; gates must be re-expanded deliberately if human reviewers join.

## Decision

The feature lifecycle collapses to three gates. Evidence requirements survive;
standalone coordination artifacts and duplicate approvals do not.

**Gate 1: Approved.** One specification per feature carries research findings,
design, balance intent, architecture, and test intent. A standalone research
brief, architecture review, or implementation plan is created only when the
maintainer judges that it materially reduces uncertainty. The Feature
Acceptance Checklist and Definition of Ready merge into a single approval
checklist inside the specification. One maintainer approval means accepted,
ready, and authorized.

**Gate 2: Done.** The feature passes static validation, complete in-game
player-path verification, save/load where state persists, applicable
compatibility checks, and maintainer playtest. Evidence is recorded briefly in
the specification or pull request. Design review is part of this gate rather
than a separate stage.

**Gate 3: Released.** The release checklist runs once per version against the
exact staged artifact, covering all features in that version. Features merge to
main when Gate 2 passes and ship when their version releases.

**Cultural review batches per release.** Irish-language and culturally
sensitive content is tracked in the terminology and canon records as features
merge. A suitably qualified reviewer evaluates the accumulated register at
Gate 3 rather than per feature. Content flagged high-risk during specification
may still request earlier review.

ADRs, the Constitution, the Design Bible, stable `EI_` identifiers, save
contracts, licensing provenance, and the prohibition on AI self-approval are
unchanged.

## Consequences

**Positive:** Per-feature artifacts drop from roughly a dozen to three: a
specification, a pull request with evidence, and a changelog entry. Small
features move from research to merged in days. Release quality checks
consolidate where they are most effective, against the exact shipped artifact.

**Negative:** Fewer formal checkpoints increase reliance on maintainer
discipline at Gate 2. Batched cultural review means an issue found at release
may require rework of merged content.

**Neutral/follow-up:** If additional human reviewers are appointed, gates may
be re-expanded by a future ADR. Historical records written under the seven-gate
lifecycle remain valid as records and are not rewritten.

## Migration

- FS-001 continues under the new lifecycle. Its approved specification,
  architecture, plan, and design review stand as completed Gate 1 and partial
  Gate 2 evidence. Remaining work maps to Gate 2 (whole-chain balance evidence)
  and Gate 3 (version 0.1 release checks).
- Constitution amends to 3.0.0. `feature-lifecycle.md`,
  `development-workflow.md`, `definition-of-ready.md`, `definition-of-done.md`,
  `product-governance.md`, `GOVERNANCE.md`, `CONTRIBUTING.md`,
  `templates/feature-spec.md`, and `AGENTS.md` update in the same change.
- Spec Kit templates under `.specify/templates/` are updated opportunistically
  the next time each template is used; they must not be used to reintroduce
  retired gates.

## Validation

The decision succeeds when the remaining version 0.1 features each ship with a
single specification and evidenced pull request, no regression in in-game
verification quality, and a version 0.1 release that passes the full release
checklist including qualified cultural review of the accumulated register.

## Revisit When

- A second regular human contributor or reviewer joins the project.
- A Gate 2 escape (a defect that a retired gate would have caught) reaches a
  published release.
- Batched cultural review produces rework costly enough that per-feature review
  would have been cheaper.
