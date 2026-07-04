# Feature Acceptance Checklist

**Feature:** [link]  
**Milestone:** [name]  
**Review date:** [YYYY-MM-DD]  
**Decision:** Reject | Revise | Accept for planning  
**Reviewers:** [names]

A feature must pass this checklist before implementation planning becomes
executable. A non-applicable item needs a written rationale. One failed critical
item returns the feature to discovery or review.

## Identity and Scope

- [ ] It conforms to the Constitution and Design Bible.
- [ ] It serves the active milestone and has a bounded first slice.
- [ ] It is recognizably Irish-inspired through specific, documented relationships.
- [ ] It is original Rim fiction, not literal Earth history.
- [ ] It avoids explicit exclusions, stereotypes, and unsupported identity claims.
- [ ] It fits existing Emerald Isle canon or proposes an approved canon amendment.

## Gameplay and RimWorld Fit

- [ ] It solves a clear player problem or creates a meaningful decision.
- [ ] It can generate stories rather than only provide passive value.
- [ ] A player can understand it through normal RimWorld concepts and UI.
- [ ] Its closest vanilla/DLC alternatives are identified.
- [ ] It is not a strict upgrade at comparable access and total cost.
- [ ] Advantages have visible, consequential tradeoffs.
- [ ] Progression placement and storyteller/economy effects are credible.

## Research and Cultural Review

- [ ] Period, region, community, terminology, sources, and uncertainty are recorded.
- [ ] Evidence, interpretation, folklore, revival, and invention are distinguished.
- [ ] The transformation from source inspiration to Rim design is explicit.
- [ ] Sensitive, contested, sacred, or language material has appropriate review.
- [ ] The feature remains useful without requiring historical knowledge.

## Technical and Architectural Fit

- [ ] XML and supported extension points were evaluated first.
- [ ] If C# is required, the missing declarative capability is named and justified.
- [ ] If Harmony is required, an ADR and compatibility plan exist.
- [ ] Existing systems or abstractions cannot meet the need more simply.
- [ ] Dependencies are minimal, directional, and safe when optional content is absent.
- [ ] Save, def-name, localization-key, API, and migration impacts are understood.
- [ ] Runtime frequency, worst-case scale, and performance validation are defined.
- [ ] The feature does not create disproportionate maintenance or test-matrix cost.

## Art, Audio, Language, and Accessibility

- [ ] Required assets, states, paths, provenance, and acceptance views are defined.
- [ ] Visual output remains readable and compatible with vanilla presentation.
- [ ] Player-facing terminology is functional, consistent, and localization-ready.
- [ ] Irish usage has meaning, context, documented form, and a review plan.
- [ ] Audio requirements or non-applicability are explicit.

## Decisions, Verification, and Release

- [ ] Existing ADRs were searched; conflicts and supersession needs are documented.
- [ ] Acceptance scenarios cover normal, edge, failure, and missing-dependency paths.
- [ ] Save/load and relevant DLC/mod matrix cases are planned.
- [ ] Balance and comprehension hypotheses have structured playtest questions.
- [ ] Documentation, attribution, release notes, and rollback impacts are known.
- [ ] Future expansion is supported through seams without speculative implementation.

## Decision Record

**Failed or conditional items:** [list]  
**Required changes:** [actions, owners, due stage]  
**Accepted rationale:** [why the feature is ready]  
**Related ADRs:** [links]
