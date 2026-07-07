# Feature Specification: [FEATURE NAME]

**Feature Branch:** `[###-feature-name]`  
**Created:** [DATE]  
**Status:** Draft  
**Milestone:** [ACTIVE MILESTONE]  
**Input:** "$ARGUMENTS"

**Design Bible:** `docs/design/design-bible.md` (mandatory authority)

> Complete the detailed sections in `templates/feature-spec.md`. This Spec Kit
> template defines mandatory acceptance and governance fields.

## Player Value and Scenarios

### Player Story 1 - [Title] (P1)
[Player goal and meaningful decision.]

**Why now:** [Milestone fit]  
**Independent test:** [Observable in-game proof]

1. **Given** [state], **when** [action], **then** [result].

### Edge and Failure Cases
- [Boundary, missing dependency, persistence, or compatibility case]

## Requirements

- **FR-001:** The feature MUST [testable player-visible behavior].
- **FR-002:** The feature MUST [tradeoff or constraint].
- **FR-003:** The feature MUST [safe failure/compatibility behavior].

## Research and Cultural Transformation
[Research brief when needed; otherwise cite accepted evidence and explain why no
additional research is required. Record significance, uncertainty, sensitivities,
and Rim adaptation proportional to the claim.]

## Vanilla Comparison and Balance
[Alternatives; acquisition, costs, outputs, constraints, progression, abuse cases.]

## Scope
**In scope:** [smallest coherent slice]  
**Out of scope:** [future work]

## Cross-Discipline Requirements
**Technical:** [XML/C# direction, persistence, compatibility]  
**Art/audio:** [assets and states]  
**Localization:** [keys and terminology]  
**Required DLC:** [none or list]  
**Optional DLC enhancements:** [DLC and behavior]  
**Behavior without DLC:** [fallback/omission]  
**Save compatibility:** [migration and DLC add/remove]

## Success Criteria
- **SC-001:** [Measurable player or quality outcome].
- **SC-002:** [Measurable balance or reliability outcome].

## Dependencies, Assumptions, and Risks
[Explicit list with mitigations.]

## Gate 1: Approval
Complete the approval checklist in `docs/workflow/definition-of-ready.md`. One
maintainer approval accepts, readies, and authorizes the feature. Flag
Irish-language or culturally sensitive content for the cultural review register.

**Decision:** Approved | Not Approved
**Approved by/date:** [maintainer, YYYY-MM-DD]
**Conditions:** [none or explicit conditions]

## Gate 2: Evidence
Record in-game, save/load, compatibility, and playtest evidence per
`docs/workflow/definition-of-done.md`, here or in the pull request.

**Decision:** Done | Not Done
**Approved by/date:** [maintainer, YYYY-MM-DD]
