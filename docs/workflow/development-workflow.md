# Development Workflow

**Status:** Stable workflow baseline under Constitution 3.0.0 and ADR 0002
**Purpose:** Ship playable, maintainable Emerald Isle features with the least process
that safely preserves quality and project memory.

## What Counts as Progress

Progress is measured by working features, gameplay quality, player experience,
stability, balance, compatibility, playtesting evidence, and release quality.
Documentation supports those outcomes; document volume is not an outcome.

The foundation documents remain authoritative and should change slowly. Feature work
links to them and records only new decisions, contracts, evidence, and lessons that
future contributors need.

## Three-Gate Feature Workflow

1. **Approved:** One specification resolves material uncertainty (research findings
   live inside it unless a standalone brief adds decision value), defines player
   value, frozen behavior, tradeoffs, scope, acceptance criteria, compatibility,
   playtest intent, and the architecture decision (XML/C#, dependencies, public
   contracts, saves, assets, verification). Create an AR, Implementation Plan, or
   ADR only when the decision benefits from a durable standalone record. One
   maintainer approval of the specification accepts, readies, and authorizes the
   feature.
2. **Done:** Deliver the smallest playable slice, verifying continuously rather than
   deferring integration: static checks, the complete in-game player path, save/load
   where state persists, and applicable compatibility checks. Playtest for
   comprehension, choices, balance, friction, exploits, and stories, and review the
   implemented feature against the specification and Design Bible. Record evidence
   in the specification or pull request; merge when it passes.
3. **Released:** Once per version, test the exact staged package, run the release
   checklist for every included feature, complete batched qualified cultural review,
   reconcile affected project memory, and publish support/rollback information.

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

The [Definition of Ready](definition-of-ready.md) is the Gate 1 approval checklist.
The [Definition of Done](definition-of-done.md) is the Gate 2 evidence checklist.
The release checklist governs Gate 3 once per version.
The mod must never become subordinate to its process.
