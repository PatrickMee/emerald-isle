# Product Governance

This document operationalizes `GOVERNANCE.md`. Higher authorities remain the
Constitution and Design Bible.

## Approval Matrix

| Change | Required proposal | Required approval | Record |
|---|---|---|---|
| Routine design within accepted spec | PR | Maintainer | PR |
| Feature approval (Gate 1) | Specification with approval checklist | Maintainer | Feature specification |
| Feature done (Gate 2) | PR with in-game and playtest evidence | Maintainer | PR and specification |
| Architecture decision | Inline review or ADR when durable | Technical maintainer | Feature record or ADR |
| Design Bible amendment | Impact proposal | Founding Maintainer plus affected domain review | Bible version/history |
| Constitution amendment | Governance proposal | Founding Maintainer | Constitution version/report |
| Roadmap change | Outcome/scope/dependency analysis | Product authority | Roadmap change and issue |
| Milestone closure | Exit evidence and open-risk review | Founding Maintainer and release/QA authority | Closure audit |
| Release (Gate 3) | Release checklist and exact artifact evidence | Release authority | Tag and release record |

No AI agent holds approval authority. Authors may prepare evidence but disclose
self-review. Sensitive cultural or Irish-language content is registered as
features merge and receives qualified review once per release; high-risk content
may request earlier review.

## Backlog Promotion

1. Candidate exists in the Feature Catalog.
2. Product triage confirms possible milestone and player value.
3. One feature specification resolves material uncertainty, defines bounded scope
   and acceptance, and records the architecture decision; standalone research,
   architecture, or plan documents exist only when they add decision value, and
   durable decisions receive ADRs.
4. The specification's approval checklist (Definition of Ready) passes and one
   maintainer approval authorizes implementation.

Implementation cannot begin from a catalog row, issue, prompt, or roadmap bullet.

## ADR Acceptance

An ADR author identifies decision scope, drivers, options, consequences,
compatibility, validation, and revisit triggers. Affected domain owners review it.
The technical maintainer sets Accepted or Rejected. Constitution or Bible conflicts
must amend the higher authority first. Supersession uses a new ADR and reciprocal links.

## Roadmap Changes

Roadmap changes state evidence, player/product impact, capacity, dependency and
compatibility impact, displaced work, and whether milestone success/exit criteria
change. Moving an idea is easier than broadening an active milestone.

## Milestone Closure

Closure requires every exit criterion, completed deliverable inventory, risk/debt
review, documentation/link validation, unresolved issue disposition, release or
baseline evidence, and maintainer sign-off. Exceptions identify owner, expiry, and
why closure remains honest despite the exception.

## Tags and Releases

Annotated tags use `vMAJOR.MINOR.PATCH` and point to a reviewed commit. The tag
message names the milestone/release. Published releases attach or identify the exact
verified artifact, changelog, support matrix, known issues, and rollback target.
Tags are never moved or reused; corrections receive a new version.

## Foundation Authorities

Documents listed in `docs/foundation-baseline.md` are stable authorities. Material
changes normally require an ADR plus any document-specific amendment process.

Stability does not require ceremony around routine feature work. Governance records
the smallest evidence needed to protect product identity, public contracts, cultural
integrity, contributor coordination, and release quality. Working software and
observed player outcomes remain the measure of delivery.
