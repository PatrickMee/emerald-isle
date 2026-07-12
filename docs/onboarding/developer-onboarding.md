# Developer Onboarding

## Read First

1. `README.md`
2. Constitution and Design Bible
3. Active milestone in `docs/roadmap.md`
4. `docs/workflow/feature-lifecycle.md`
5. The active issue, request, PR, or spec and only the discipline guides/ADRs
   relevant to the change

Do not read the entire historical Version 0.1 documentation set before ordinary
work. Use it when changing a released contract or when its evidence answers a
current question.

## Current Repository State

Version 0.1 is released. Its public defs, translation keys, texture paths, package
ID, and Workshop ID are compatibility contracts. Later gameplay requires active-
milestone scope and explicit maintainer approval.

## Work Setup

- Clone the repository and keep RimWorld binaries, saves, logs, credentials, and
  downloaded Workshop content outside version control.
- Use a short-lived branch when review or rollback benefits; focused maintainer
  changes may commit directly under the current collaboration policy.
- Classify work as Routine, Standard, or High-Risk.
- Start from the approved record appropriate to that risk; do not create empty
  companion documents.

## Working Agreement

Verify current RimWorld definitions rather than relying on remembered APIs. Keep
changes small, preserve released IDs, record asset/source provenance, and test the
affected path in the real game. Add save, DLC/mod, performance, migration, or
cultural checks only when the change creates that risk.

AI agents follow the same scope and may not grant human approval. Record results
once in the issue, PR, or feature record.

## First Contribution

Routine documentation or metadata work needs normal review. Standard XML gameplay
uses a short feature record and explicit maintainer approval, then implementation,
affected-path validation, human review, and merge. Use the PR template without
inventing not-applicable paperwork.
