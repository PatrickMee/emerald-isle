# Product Governance

This document operationalizes `GOVERNANCE.md`. Higher authorities remain the
Constitution and Design Bible.

## Approval Matrix

| Change | Required proposal | Required approval | Record |
|---|---|---|---|
| Routine design within accepted spec | PR | Domain reviewer/maintainer | PR |
| Feature acceptance | Spec, research, checklist | Product plus required domain gates | Feature record |
| Architecture decision | ADR | Technical maintainer and affected owners | ADR |
| Design Bible amendment | Impact proposal | Founding Maintainer plus affected domain review | Bible version/history |
| Constitution amendment | Governance proposal | Founding Maintainer | Constitution version/report |
| Roadmap change | Outcome/scope/dependency analysis | Product authority | Roadmap change and issue |
| Milestone closure | Exit evidence and open-risk review | Founding Maintainer and release/QA authority | Closure audit |
| Release | Release checklist and exact artifact evidence | Release authority | Tag and release record |

No AI agent holds approval authority. Authors may prepare evidence but disclose
self-review. Sensitive cultural or Irish-language changes require qualified review.

## Backlog Promotion

1. Candidate exists in the Feature Catalog.
2. Product triage confirms possible milestone and player value.
3. Research brief establishes adequate confidence and sensitivities.
4. Feature specification defines bounded scope and acceptance.
5. Feature Acceptance Checklist returns Accept for planning.
6. Required discipline gates approve or state conditions.
7. Maintainer marks the feature Accepted and authorizes planning.

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
