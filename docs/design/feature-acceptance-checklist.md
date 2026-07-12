# Expanded Feature Design Review

This is an optional prompt set for High-Risk features. Standard features use the
short record in `templates/feature-spec.md`; they do not complete this checklist.

Review only the sections triggered by the feature's risks.

## Identity and Gameplay

- Does it create a meaningful player decision, story, or strategic role?
- Does specific Irish inspiration shape the feature without becoming stereotype,
  romantic reconstruction, or literal Earth history?
- Does it fit the active milestone, Design Bible, RimWorld tone, and vanilla UI?
- Is the smallest coherent slice explicit?
- Does every advantage carry a visible tradeoff?

## Research and Cultural Risk

- Could uncertain history, regional variation, Irish language, sacred material,
  or living identity change the design?
- Are material claims sourced and uncertainty stated?
- Is qualified review scheduled when the content is genuinely sensitive?

## Technical and Compatibility Risk

- Can XML and established vanilla patterns express the behavior?
- If C# or Harmony is required, is the missing declarative capability clear?
- Are public IDs, saves, migration, DLC/mod branching, performance, and rollback
  risks understood where they actually apply?
- Does this introduce a shared abstraction before repeated implementations justify
  it?

## Acceptance

- Can the player-facing outcome be demonstrated in one complete in-game path?
- Which specific save/load, failure, configuration, performance, localization, or
  regression checks are justified by credible risk?
- Is any requested standalone research, ADR, architecture note, plan, or matrix
  necessary to make or preserve a decision?

**Decision:** Approve | Revise | Reject<br>
**Reviewer/date:** [name, YYYY-MM-DD]<br>
**Conditions:** [material conditions only]
