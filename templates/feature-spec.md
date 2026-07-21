# Feature Record: [Name]

This short record may be copied into a GitHub issue, pull request, or repository
file. Standard features should stay short. Expand only the sections whose risks
need durable detail.

**ID/milestone:** [ID and active milestone]<br>
**Owner:** [name]<br>
**Risk class:** Standard | High-Risk<br>
**Status:** Proposed | Approved | Implementing | Done | Released

## Decision

**Player value:** [decision, story, or strategic role]

**In scope:** [smallest coherent slice]

**Out of scope:** [boundaries that prevent scope growth]

**Vanilla comparison and tradeoff:** [closest alternative; why this is not a
strict upgrade]

## Basis

[Only the historical, cultural, gameplay, or technical evidence that changes the
design. Cite sources where claims matter. Flag sensitive or uncertain material.
For progression-facing work, name the documented cultural relationship being
preserved or transformed. Do not create a separate artifact unless its risk
requires one.]

## Implementation Boundary

- XML/C#/Harmony: [choice and why]
- Public IDs/save impact: [contracts or none]
- Required/optional DLC and fallback: [only applicable behavior]
- Art/localization/provenance: [assets and player-facing text]
- Dependencies/compatibility: [credible interactions only]

## Acceptance Checks

- [ ] [Observable player-path result]
- [ ] [Meaningful tradeoff or balance result]
- [ ] [Relevant failure/regression result]

## Approval

**Decision:** Approved | Not Approved<br>
**Maintainer/date:** [name, YYYY-MM-DD]<br>
**Conditions:** [material conditions only]

## Done Evidence

[Static/build result, complete affected in-game path, log review, human review,
and only the save/DLC/performance/cultural checks triggered by actual risk. A PR
link or concise maintainer confirmation is sufficient.]

**Decision:** Done | Not Done<br>
**Maintainer/date:** [name, YYYY-MM-DD]

## High-Risk Additions — Only When Triggered

[Link targeted research, ADR, architecture, implementation, migration, cultural,
performance, or compatibility records. Do not create empty companion documents.]
