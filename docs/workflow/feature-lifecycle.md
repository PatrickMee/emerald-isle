# Feature Lifecycle

**Status:** Stable Feature Workflow baseline under Constitution 2.0.0. Material
changes normally require an ADR.

The canonical philosophy and proportionality rules live in
[`development-workflow.md`](development-workflow.md). This document is the operational
sequence. Evidence may live in a specification, issue, pull request, test report, or
standalone record; the workflow does not require one file per stage.

1. **Research when needed:** Record sources, confidence, uncertainty, sensitivity,
   and Rim transformation only to the depth needed for the decision.
2. **Specification:** Define player scenarios, frozen scope, vanilla comparison,
   balance intent, acceptance criteria, and exclusions. Pass the Feature Acceptance
   Checklist with risk-proportional review.
3. **Architecture and readiness:** Decide XML/C#, dependencies, public contracts,
   persistence, performance, compatibility, assets, tests, and rollback. Create ADRs
   for durable choices. Create a standalone AR or Implementation Plan only when it
   adds implementation value. Pass Definition of Ready and obtain maintainer
   authorization.
4. **Implementation:** Deliver the smallest playable slices. Run static, automated
   where useful, in-game, save, compatibility, and performance checks as the feature
   grows.
5. **Playtesting:** Evaluate comprehension, decisions, balance, pacing, friction,
   exploits, and stories in representative play.
6. **Design review:** Review the implemented result for gameplay, history, vanilla
   fit, technical quality, balance, scope, maintainability, and compatibility. Update
   only affected authoritative records.
7. **Release:** Pass Definition of Done and the exact-artifact release checklist;
   publish the immutable version, support information, and rollback target.

A failed gate returns to the earliest invalid assumption. Postmortems and process
changes are created only when the resulting lesson has reusable value.
