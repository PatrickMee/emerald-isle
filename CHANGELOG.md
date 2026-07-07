# Changelog

All notable project changes are documented here.

## [Unreleased]

### Development

- Completed FS-001 Oats: XML-only plant and harvested-grain definitions, English
  localization, and original runtime textures. Static validation, in-game
  player-path verification, and maintainer playtest passed (Gate 2, 2026-07-07).
  Whole-chain balance is deferred to the hand-quern and milled-oats features;
  release smoke tests run at the version 0.1 release gate.
- Added the first working FS-002 Dry-Stone Wall checkpoint: one XML-only,
  stone-only linked wall with original, human-approved Version 0.1 runtime art.
- FS-002 passed Gate 2: proportional implementation verification, maintainer
  Design Review, and merge readiness. Exhaustive isolation, compatibility, and
  release-matrix checks are deferred to Version 0.1 release integration.
- Drafted FS-003 Hand Quern as a proportional Gate 1 specification for maintainer
  review. The draft records that a player-facing quern cannot pass Gate 2 without
  a real milling use from FS-004.

### Governance

- Adopted the three-gate feature lifecycle (Approved, Done, Released) through
  ADR-0003 and Constitution 3.0.0, with cultural and Irish-language review
  batched per release.

### Planning

- Added the RimWorld 1.6 empty-package metadata and clean staging contract.
- Added the Version 0.1 structured Research Sprint.
- Added a provisional ranked plan for the first five implementation candidates.
- Replaced the loose five-candidate list with the cohesive four-feature
  **First Holding** scope recommendation after reviewing installed RimWorld 1.6 data.
- Completed FS-001 research, specification, architecture, readiness, and
  implementation authorization.

## [0.0.0] - 2026-07-04

### The Studio Exists

- Established the project Constitution, Design Bible, architecture, governance,
  discipline guides, workflow gates, and multi-year roadmap.
- Adapted Spec Kit for research-led, gameplay-gated RimWorld development.
- Added open-source contribution, security, support, onboarding, AI-agent, issue,
  risk, debt, research, glossary, testing, playtesting, and release practices.
- Created the official candidate Feature Catalog and reusable feature, research,
  ADR, playtest, release, and postmortem templates.
- Adopted MIT for source code, separate creative-asset licensing, RimWorld 1.6
  Core requirement, and official support for all five listed DLCs.
- Froze the nine foundation authorities under ADR-based change control.

[Unreleased]: docs/roadmap.md
[0.0.0]: docs/release/v0.0.0.md
