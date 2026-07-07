# Definition of Done (Gate 2 Evidence Checklist)

A feature merges to main only when applicable evidence passes. Record evidence
briefly in the specification or pull request; do not create standalone reports
unless a finding has reusable value. Non-applicable items need a concise
rationale.

## Behavior and Quality

- [ ] All acceptance, edge, failure, and safe-degradation scenarios pass.
- [ ] Static validation and any useful automated checks pass.
- [ ] The complete in-game player path works in a real game session.
- [ ] Save/load passes where state persists; relevant DLC/mod matrix checks pass.
- [ ] Logs contain no new unresolved errors, warnings, or recurring spam.
- [ ] Performance is acceptable in representative conditions.

## Product and Presentation

- [ ] Gameplay purpose and meaningful tradeoffs survive maintainer playtest;
      the balance hypothesis is accepted, revised, or explicitly bounded.
- [ ] The implemented feature is reviewed against the specification and Design
      Bible for gameplay, historical integrity, vanilla fit, technical quality,
      and maintainability.
- [ ] Art and audio read correctly in-game against vanilla.
- [ ] Player text is clear, localized by key, and logged in the terminology and
      canon records where Irish-language or culturally sensitive.

## Memory

- [ ] The specification and durable decisions reflect final behavior; only
      affected records are updated and no redundant summaries are created.
- [ ] Feature Catalog state, glossary, and changelog entries are updated where
      affected.

**Decision:** Done | Not Done
**Approved by/date:** [maintainer, YYYY-MM-DD]

Release-time obligations (attribution, batched cultural review, exact-artifact
package tests, rollback) belong to the per-version release checklist at Gate 3.
