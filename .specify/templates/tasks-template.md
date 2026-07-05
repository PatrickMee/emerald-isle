# Tasks: [FEATURE NAME]

**Input:** approved specification plus any applicable plan, research, ADRs, and
review conditions. Do not create missing artifact types merely to satisfy this list.

Use `[ID] [P?] [Gate/Slice] action with exact path`. `[P]` means different
files and no unresolved dependency.

## Phase 1: Readiness
- [ ] T001 Confirm milestone scope and constitution check
- [ ] T002 Complete and pass the Feature Acceptance Checklist
- [ ] T003 Resolve applicable research and cultural review conditions
- [ ] T004 Complete gameplay, vanilla-fit, and balance conditions
- [ ] T005 Complete architecture and art/audio conditions

## Phase 2: Verification First
- [ ] T006 Define regression and acceptance evidence
- [ ] T007 Define in-game, save/load, and compatibility scenarios
- [ ] T008 Prepare smallest representative test fixture or prototype plan

## Phase 3+: Delivery Slices
For each slice: define the regression/acceptance proof, add the smallest declarative
content or behavior, integrate assets/localization, and verify the player path. Skip
task categories that do not improve the feature.

- [ ] T009 [Slice 1] [concrete task and path]
- [ ] T010 [Slice 1] Run static and automated validation
- [ ] T011 [Slice 1] Verify complete in-game player path and record evidence

## Final Phase: Playtest, Design Review, and Release
- [ ] T012 Run structured playtest and resolve findings
- [ ] T013 Complete post-implementation Design Review
- [ ] T014 Run clean-package compatibility and persistence matrix
- [ ] T015 Update only affected docs, localization, attribution, changelog, and known issues
- [ ] T016 Complete release checklist and rollback verification

## Dependencies and Checkpoints
[Explicit task graph, parallel work, gate owners, and stop conditions.]
