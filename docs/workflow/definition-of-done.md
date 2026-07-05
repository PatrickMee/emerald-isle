# Definition of Done

A feature is complete only when applicable evidence passes:

## Behavior and Quality

- [ ] All acceptance, edge, failure, and safe-degradation scenarios pass.
- [ ] Static, unit, integration, regression, and configuration checks pass.
- [ ] Exact packaged build passes clean-load and complete in-game player-path tests.
- [ ] Save/load, removal/upgrade, and relevant DLC/mod matrix tests pass.
- [ ] Performance budget passes in representative worst-case conditions.
- [ ] Logs contain no new unresolved errors, warnings, or recurring spam.

## Product and Presentation

- [ ] Gameplay purpose and meaningful tradeoffs survive playtesting.
- [ ] Balance hypothesis is accepted, revised, or explicitly bounded by known issues.
- [ ] Art/audio passes in-game states and vanilla-readability review.
- [ ] Player text is clear, accessible, localized by key, and language-reviewed as required.
- [ ] Cultural and canon review conditions are satisfied.
- [ ] Post-implementation Design Review passes gameplay, historical integrity,
      vanilla fit, technical quality, balance, scope, maintainability, and compatibility.

## Memory and Release

- [ ] The specification, durable decisions, tests, and playtest evidence reflect final behavior.
- [ ] Only affected project-memory records are updated; redundant summaries are not created.
- [ ] Feature Catalog state, glossary, risk, and debt registers are updated where affected.
- [ ] Attribution, licenses, changelog, known issues, upgrade and rollback notes are complete.
- [ ] Required code/design/release reviews approve the exact change.
- [ ] No blocker/critical defect or expired exception remains.

**Decision:** Done | Not Done  
**Approved by/date:** [maintainer, YYYY-MM-DD]  
**Release/version:** [target]
