# ADR 0004: Risk-Tiered Hobby Workflow

**Status:** Accepted<br>
**Date:** 2026-07-12<br>
**Decision owner:** Patrick Mee<br>
**Related:** Constitution 4.0.0, ADR 0003

## Context

The foundation process successfully produced an inspectable repository and the
complete Version 0.1 release. It also produced 79 documentation files, including
19 separate specification, research, and QA records for five small XML-first
features. For one or two hobby contributors, repeating that foundation-level
ceremony would consume more capacity than implementation and playtesting.

Constitution 3.0.0 stated that process should be proportional, but still required
an approved specification and broad verification for every gameplay feature. The
operational templates reinforced the heavier interpretation.

## Decision Drivers

- Preserve scope control, player value, save compatibility, provenance, and
  explicit human approval.
- Make working, playable software the dominant use of limited contributor time.
- Keep enough repository memory for a future contributor or AI agent.
- Escalate rigor based on credible risk rather than feature count.
- Avoid rewriting or invalidating the useful historical Version 0.1 records.

## Options Considered

### Keep Constitution 3.0.0 unchanged

- Benefits: no migration and maximum uniformity.
- Costs and risks: continued duplicate records, slow delivery, stale paperwork,
  and contributor burnout.

### Remove formal gates entirely

- Benefits: minimum ceremony.
- Costs and risks: weak scope control, silent compatibility changes, lost design
  intent, and avoidable release defects.

### Keep three outcomes with risk-tiered evidence

- Benefits: retains Approved, Done, and Released while making a short issue, user
  request, or PR sufficient for ordinary work.
- Costs and risks: maintainers must use judgment when classifying risk, and
  different features will have different evidence depth.

## Decision

Adopt Constitution 4.0.0 and a three-class workflow:

1. **Routine:** no separate feature gate. Use normal commit or PR review and
   validate the affected surface.
2. **Standard:** the default gameplay path. Record a short feature card in an
   issue, request, PR, or spec; receive one maintainer approval; implement; test
   the affected player path; obtain human review; merge.
3. **High-Risk:** use a concise specification and add only the research, ADR,
   architecture, planning, migration, compatibility, performance, cultural, or
   test records that resolve an identified risk.

ADR 0003's Approved, Done, Released outcomes remain. This ADR changes the default
record and evidence burden, not the release discipline or human approval model.
Release checks remain version-level and operate on the exact staged package.

## Consequences

**Positive:** Small XML features can move from decision to playtest with one short
record. Evidence is no longer duplicated across specs, matrices, and summaries.
Contributor effort moves toward gameplay, art, debugging, and player feedback.

**Negative:** Risk classification requires maintainer judgment. A feature may be
reclassified when implementation reveals persistence, compatibility, cultural,
or architectural risk.

**Neutral/follow-up:** Existing Version 0.1 research, specifications, plans, and QA
records remain valid historical evidence. They are not retroactively condensed.

## Compatibility and Migration

This is a governance-only change. It does not alter runtime content, public defs,
save data, package metadata, or released artifacts. Current templates and active
workflow guidance are updated together. Historical documents retain the process
and vocabulary under which they were accepted.

## Validation

For the next three gameplay changes, record preparation time, implementation time,
review friction, escaped defects, and whether a missing retired artifact would
have changed a decision. Reintroduce ceremony only for a demonstrated failure mode.

## Revisit When

- A defect escapes because Standard work omitted a clearly relevant check.
- Multiple active contributors need stronger coordination records.
- C# or Harmony becomes common rather than exceptional.
- Release support or compatibility obligations materially expand.
