# Feature Lifecycle

**Status:** Stable Feature Workflow baseline at v0.0.0. Material changes normally
require an ADR.

The lifecycle is evidence-gated, not a one-way waterfall. A failed gate returns to
the earliest invalid assumption.

1. **Idea:** Capture player value and inspiration in the Feature Catalog.
2. **Research:** Scope sources, confidence, uncertainty, sensitivity, and Rim transformation.
3. **Backlog triage:** Assign candidate state, possible milestone, priority, and owner.
4. **Specification:** Define player scenarios, scope, vanilla comparison, balance, and success.
5. **Acceptance review:** Pass Design Bible checklist and discipline gates.
6. **Architecture:** Decide XML/C#, dependencies, persistence, performance, compatibility.
7. **ADR decisions:** Create ADRs whenever a durable decision is reached, not at a fixed late stage.
8. **Implementation plan:** Create testable slices, exact paths, tests, playtests, and rollback.
9. **Ready gate:** Pass Definition of Ready; maintainer authorizes implementation.
10. **Implementation:** Deliver smallest slices with verification and review.
11. **Testing:** Run static through in-game, persistence, compatibility, and performance layers.
12. **Playtesting:** Evaluate comprehension, decisions, balance, pacing, exploits, and stories.
13. **Review:** Resolve product, cultural, technical, art, QA, and documentation findings.
14. **Documentation:** Reconcile specs, ADRs, catalogs, glossary, risk, debt, and user docs.
15. **Done/release gate:** Pass Definition of Done and exact-artifact release checklist.
16. **Release:** Tag immutable commit, publish verified artifact and support information.
17. **Lessons learned:** Write postmortem, update practices, and propose higher-authority changes.

The requested late ADR stage is deliberately changed: documenting decisions after
implementation or playtesting loses alternatives and rationale. ADR review happens
at every architecture-changing decision, with final reconciliation before release.
