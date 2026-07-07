# Tasks: [FEATURE NAME]

**Input:** approved specification plus any applicable plan, research, ADRs, and
review conditions. Do not create missing artifact types merely to satisfy this list.

Use `[ID] [P?] [Gate/Slice] action with exact path`. `[P]` means different
files and no unresolved dependency.

## Phase 1: Gate 1 — Approval
- [ ] T001 Confirm milestone scope and constitution check
- [ ] T002 Complete the specification's approval checklist
      (`docs/workflow/definition-of-ready.md`), including research, cultural
      flagging, gameplay, balance, architecture, and art/audio conditions
- [ ] T003 Obtain the single maintainer approval that authorizes implementation

## Phase 2: Verification First
- [ ] T004 Define regression and acceptance evidence
- [ ] T005 Define in-game, save/load, and compatibility scenarios
- [ ] T006 Prepare smallest representative test fixture or prototype plan

## Phase 3+: Delivery Slices
For each slice: define the regression/acceptance proof, add the smallest declarative
content or behavior, integrate assets/localization, and verify the player path. Skip
task categories that do not improve the feature.

- [ ] T007 [Slice 1] [concrete task and path]
- [ ] T008 [Slice 1] Run static and automated validation
- [ ] T009 [Slice 1] Verify complete in-game player path and record evidence

## Final Phase: Gate 2 — Done
- [ ] T010 Run maintainer playtest, review the implemented result against the
      specification and Design Bible, and resolve findings
- [ ] T011 Record Gate 2 evidence (`docs/workflow/definition-of-done.md`) in the
      specification or pull request; log sensitive content in the cultural
      review register
- [ ] T012 Update only affected docs, localization, attribution, changelog, and
      known issues, then merge

Release-time work (exact-artifact matrix, batched cultural review, rollback,
tag) belongs to the per-version Gate 3 release checklist, not feature tasks.

## Dependencies and Checkpoints
[Explicit task graph, parallel work, gate owners, and stop conditions.]
