# Developer Onboarding

## Read First

1. `README.md`
2. Constitution and Design Bible
3. `docs/README.md`, roadmap, and current `specs/*/plan.md`
4. Governance, contribution guide, lifecycle, Definition of Ready/Done
5. Relevant discipline guides and accepted ADRs

## Current Repository State

Milestones 0 and 0.5 are documentation-only. Do not add gameplay, package, build,
XML, C#, or assets until closure is recorded and a Version 0.1 feature passes Ready.

## Work Setup

- Clone the configured remote after it exists; never work inside another repo.
- Use the documented supported game/toolchain once adopted.
- Keep RimWorld binaries, personal saves, logs, credentials, and Workshop content
  outside version control.
- Create a short-lived branch using the project naming policy.
- Start from a cataloged feature or triaged issue, not an unrecorded prompt.

## Working Agreement

Update repository memory in the same change. Verify current game definitions and
assemblies rather than relying on stale snippets. Preserve exact reproduction and
test evidence. Do not claim compatibility beyond the tested matrix.

AI agents receive the same authorities, bounded paths, active spec and plan,
verification requirements, and prohibited actions. Human approval remains required.

## First Contribution

Documentation corrections and research-source improvements are safest before
Version 0.1. For implementation, select an approved task, confirm Ready, make the
smallest coherent change, run required checks, and complete the PR template.
