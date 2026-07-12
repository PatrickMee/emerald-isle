# Product Governance

This document operationalizes `GOVERNANCE.md`. Higher authorities remain the
Constitution and Design Bible.

## Approval Matrix

| Change | Required proposal | Required approval | Record |
|---|---|---|---|
| Routine maintenance within accepted behavior | Commit or PR | Maintainer | Commit or PR |
| Standard gameplay approval | Short issue, request, PR, or spec | Maintainer | Existing feature record |
| High-Risk gameplay approval | Concise spec plus risk-triggered records | Maintainer and affected domain | Spec and applicable ADR/review |
| Feature done | PR or feature record with affected-path evidence | Maintainer | Existing PR or feature record |
| Architecture decision | Inline review or ADR when durable | Technical maintainer | Feature record or ADR |
| Design Bible amendment | Impact proposal | Founding Maintainer plus affected domain review | Bible version/history |
| Constitution amendment | Governance proposal | Founding Maintainer | Constitution version/report |
| Roadmap change | Short outcome/scope rationale | Product authority | Roadmap edit or issue |
| Milestone closure | Delivered/deferred scope and open-risk review | Founding Maintainer | Roadmap/release record |
| Release (Gate 3) | Release checklist and exact artifact evidence | Release authority | Tag and release record |

No AI agent holds approval authority. Authors may prepare evidence but disclose
self-review. Sensitive cultural or Irish-language content is registered as
features merge and receives qualified review once per release; high-risk content
may request earlier review.

## Backlog Promotion

1. Product triage confirms the active milestone and player value.
2. A short feature record states bounded scope, tradeoff, implementation boundary,
   compatibility risk, and acceptance checks.
3. High-Risk work adds only the research, ADR, architecture, plan, migration, or
   verification records required by its identified risks.
4. One explicit maintainer approval authorizes implementation.

A direct maintainer request may serve as the Standard feature record when it
contains the required decisions. A catalog or roadmap bullet alone is insufficient.

## ADR Acceptance

An ADR author identifies decision scope, drivers, options, consequences,
compatibility, validation, and revisit triggers. Affected domain owners review it.
The technical maintainer sets Accepted or Rejected. Constitution or Bible conflicts
must amend the higher authority first. Supersession uses a new ADR and reciprocal links.

## Roadmap Changes

Roadmap changes state the reason, player/product effect, and any displaced active
scope or compatibility obligation. A roadmap edit is sufficient unless the change
needs discussion. Moving an idea is easier than broadening an active milestone.

## Milestone Closure

Closure records what shipped, what was deferred, any unresolved blocker or public
compatibility risk, the release/baseline evidence, and maintainer confirmation. A
separate closure audit is not required. Exceptions state why closure remains honest
and where the remaining work lives.

## Tags and Releases

Annotated tags use `vMAJOR.MINOR.PATCH` and point to a reviewed commit. The tag
message names the milestone/release. Published releases attach or identify the exact
verified artifact, changelog, support matrix, known issues, and rollback target.
Tags are never moved or reused; corrections receive a new version.

## Foundation Authorities

Documents listed in `docs/foundation-baseline.md` are stable authorities. Material
changes normally require an ADR plus any document-specific amendment process.

Stability does not require ceremony around Routine or Standard work. Governance
records the smallest evidence needed to protect product identity, public contracts,
cultural integrity, contributor coordination, and release quality. Working software
and observed player outcomes remain the measure of delivery.
