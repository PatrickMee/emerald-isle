# Development Workflow

## Improved Feature Lifecycle

The requested lifecycle is retained as gates but adjusted to avoid a rigid
waterfall. Historical, gameplay, balance, architecture, and art concerns often
change one another, so reviews may iterate. ADRs move to the decision point;
waiting until after playtesting would leave implementation decisions undocumented.

1. **Intake and milestone triage**
2. **Research brief**
3. **Concept specification**
4. **Design Bible Feature Acceptance Checklist**
5. **Historical/cultural review**
6. **Gameplay and vanilla-fit review**
7. **Balance review**
8. **Architecture review and ADRs when triggered**
9. **Art/audio feasibility review**
10. **Implementation and verification plan**
11. **Implementation in the smallest testable slices**
12. **Static and automated validation**
13. **In-game verification, including persistence**
14. **Structured playtest and tuning loop**
15. **Release readiness review**
16. **Release and retrospective**

Stages 4 through 8 may run concurrently after the concept is coherent. Failed
gates return the feature to the earliest affected stage. A gate marked not
applicable needs a written reason.

## Definition of Ready

Active milestone fit, player problem, research scope, vanilla comparison, bounded
first slice, dependencies, risks, and assigned reviewers are explicit.

## Definition of Done

Acceptance criteria pass, required reviews are recorded, tests and in-game paths
pass, logs are clean, persistence and optional dependencies are verified,
documentation/localization/attribution are updated, release notes are drafted,
and no unresolved blocker or critical defect remains.
