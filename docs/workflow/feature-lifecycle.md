# Feature Lifecycle

**Status:** Stable Feature Workflow baseline under Constitution 3.0.0 and
ADR 0003. Material changes normally require an ADR.

The canonical philosophy and proportionality rules live in
[`development-workflow.md`](development-workflow.md). This document is the
operational sequence. Evidence lives in the specification and pull request; the
workflow does not require one file per stage.

## Gate 1: Approved

Write one specification. It carries research findings (sources, confidence,
uncertainty, and Rim transformation to the depth the decision needs), player
scenarios, frozen scope, vanilla comparison, balance intent, acceptance
criteria, exclusions, and an architecture paragraph covering XML/C#,
dependencies, public contracts, persistence, and compatibility. Create a
standalone research brief, Architecture Review, or Implementation Plan only when
it adds decision value; create ADRs for durable choices.

Complete the approval checklist in
[`definition-of-ready.md`](definition-of-ready.md). One maintainer approval
means the feature is accepted, ready, and authorized for implementation.

## Gate 2: Done

Deliver the smallest playable slices. Verify continuously: static validation,
automated checks where useful, the complete in-game player path, save/load where
state persists, and applicable compatibility and performance checks. Playtest
for comprehension, decisions, balance, pacing, friction, exploits, and stories.
Review the implemented result against the specification and Design Bible.

Record the evidence in the specification or pull request using
[`definition-of-done.md`](definition-of-done.md). The feature merges to main
when this gate passes. Log Irish-language and culturally sensitive content in
the terminology and canon records for release-time review.

## Gate 3: Released

Once per version, run the release checklist against the exact staged package:
attribution, localization, batched qualified cultural review of the accumulated
register, compatibility matrix, rollback, and release-quality checks for every
feature in the version. Publish the immutable version, support information, and
rollback target.

A failed gate returns to the earliest invalid assumption. Postmortems and
process changes are created only when the resulting lesson has reusable value.
