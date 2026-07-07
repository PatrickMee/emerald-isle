# Feature: [Name]

**Spec ID:** [NNN-slug]  
**Status:** Discovery | Review | Approved | Implementing | Verifying | Released  
**Milestone:** [Milestone]  
**Owner:** [Name]  
**Created/updated:** [YYYY-MM-DD]

**Design Bible conformance:** [reviewed at Gate 1; note any conditions or link
supporting analysis when the feature is high-risk]

## Overview
[One paragraph describing the feature and bounded first slice.]

## Historical Research
[Claims, sources, periods, regions, and uncertainty. Link a research brief when one
was needed; otherwise cite accepted evidence and state why additional research was
not required.]

## Cultural Significance
[Why the inspiration matters, sensitivities, and transformation for the Rim.]

## Gameplay Purpose
[Player problem, decisions, stories, and why this deserves scope.]

## Vanilla Comparison
[Closest vanilla/DLC alternatives and differentiation.]

## Balance Analysis
[Costs, outputs, constraints, progression, abuse cases, and hypothesis.]

## Player Scenarios and Acceptance
1. **Given** [state], **when** [action], **then** [observable result].

## Scope
**In:** [bounded behavior]  
**Out:** [explicit exclusions]

## Technical Design
[Defs, runtime behavior, persistence, compatibility, dependencies, and migration at
the depth needed to implement safely. Link a standalone AR or plan only when useful.]

## XML vs C# Decision
[XML, C#, or hybrid; why; Harmony decision and ADR if relevant.]

## Art Requirements
[Function, assets, states, references, paths, acceptance views.]

## Audio Requirements
[Cues, function, mixing context, provenance, or justified non-applicability.]

## Localization
[Keys, terminology, context, Irish-language review, layout risks.]

## Testing
[Static, unit, integration, in-game, save/load, matrix, playtest questions.]

## Future Expansion
[Extension seams only; no speculative implementation.]

## Dependencies

**Required DLC:** [none or explicit list]  
**Optional DLC enhancements:** [DLC and added behavior]  
**Behavior without DLC:** [fallback, omission, or safe degradation]  
**Save compatibility:** [state, migration, DLC add/remove, feature removal]

[Other game, mod, feature, art, research, and tooling dependencies.]

## Risks
| Risk | Likelihood | Impact | Mitigation | Owner |
|---|---|---|---|---|
| [Risk] | [L/M/H] | [L/M/H] | [Action] | [Name] |

## Gate 1: Approval
[Complete the checklist in `docs/workflow/definition-of-ready.md`. One maintainer
approval accepts, readies, and authorizes the feature.]

**Decision:** Approved | Not Approved
**Approved by/date:** [maintainer, YYYY-MM-DD]
**Conditions:** [none or explicit conditions]

## Gate 2: Evidence
[Record in-game, save/load, compatibility, and playtest evidence per
`docs/workflow/definition-of-done.md`, here or in the pull request. Log
Irish-language and culturally sensitive content in the terminology and canon
records for release-time review.]

**Decision:** Done | Not Done
**Approved by/date:** [maintainer, YYYY-MM-DD]

## Open Questions and Decisions
[Question, owner, due point, and ADR link where applicable.]
