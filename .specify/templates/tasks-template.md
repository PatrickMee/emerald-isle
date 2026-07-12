# Tasks: [FEATURE NAME]

Create a standalone task list only when sequencing or coordination adds value.
Standard one-session work normally uses the approved feature record and PR.

**Input:** [approved issue/request/PR/spec and risk-triggered records]

Use `[ID] [P?] action with exact path`. `[P]` means different files and no
unresolved dependency.

## Scope and Stop Conditions

- [ ] T001 Confirm approved in/out scope and public contracts
- [ ] T002 Identify concrete conditions that require maintainer review before
      continuing

## Delivery Slices

For each slice, implement the smallest behavior, run relevant static validation,
exercise its affected in-game path, and fix defects before continuing.

- [ ] T003 [Concrete implementation task and path]
- [ ] T004 [Relevant validation and in-game proof]

## Completion

- [ ] T005 Obtain human gameplay/visual review
- [ ] T006 Record results once in the issue, PR, or feature record
- [ ] T007 Update only affected public-contract, provenance, decision, risk, or
      release memory, then merge

Release packaging and version-level smoke checks belong to the release checklist.

## Dependencies and Checkpoints

[Only real dependency order, parallel work, owners, and stop conditions.]
