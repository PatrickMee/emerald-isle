# Development Workflow

**Status:** Stable workflow baseline under Constitution 2.0.0
**Purpose:** Ship playable, maintainable Emerald Isle features with the least process
that safely preserves quality and project memory.

## What Counts as Progress

Progress is measured by working features, gameplay quality, player experience,
stability, balance, compatibility, playtesting evidence, and release quality.
Documentation supports those outcomes; document volume is not an outcome.

The foundation documents remain authoritative and should change slowly. Feature work
links to them and records only new decisions, contracts, evidence, and lessons that
future contributors need.

## Streamlined Feature Workflow

1. **Research when necessary:** Resolve only the historical, cultural, gameplay, or
   technical uncertainty capable of changing the feature. Skip a standalone brief
   when accepted evidence already answers the question.
2. **Specification:** Define player value, frozen behavior, tradeoffs, scope,
   acceptance criteria, compatibility, and playtest intent.
3. **Architecture review:** Confirm XML/C#, dependencies, public contracts, saves,
   assets, and verification. Record this inline for routine work; create an AR or ADR
   only when the decision benefits from a durable standalone record. Create an
   Implementation Plan only when sequencing, coordination, or risk makes it useful.
4. **Implementation:** Deliver the smallest playable slice, verifying it continuously
   rather than deferring integration until the end.
5. **Playtesting:** Observe comprehension, choices, balance, friction, exploits, and
   stories in representative colonies.
6. **Design review:** Evaluate the implemented feature—not just its documents—for
   gameplay, historical integrity, vanilla fit, technical quality, balance, scope,
   maintainability, and compatibility. Fix the feature or explicitly return to an
   earlier decision when evidence fails.
7. **Release:** Test the exact staged package, reconcile affected project memory,
   publish support/rollback information, and release through the established gate.

Failed evidence returns to the earliest invalid assumption. Stages may iterate or
overlap when that improves delivery.

## Proportionality Rules

- Research depth follows uncertainty and cultural stakes.
- Specifications are concise for small features and detailed where behavior or
  compatibility is complex.
- Architecture Reviews and Implementation Plans are not automatic deliverables.
- Tests and playtests follow player impact and failure risk.
- ADRs record durable choices, not routine field values or file placement.
- Existing authoritative documents are linked rather than restated.
- Generalize only after multiple implemented features prove a recurring pattern.
- Remove or consolidate guidance that costs more to maintain than the risk it controls.

The [Definition of Ready](definition-of-ready.md) governs implementation entry. The
[Definition of Done](definition-of-done.md) and release checklist govern completion.
The mod must never become subordinate to its process.
