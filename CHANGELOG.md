# Changelog

All notable project changes are documented here.

## [Unreleased]

## [0.2.0] - 2026-07-13

### The Hearth and Household

### Governance

- Adopted Constitution 4.0.0 and ADR-0004. Routine maintenance now uses ordinary
  review, Standard gameplay defaults to one short feature record and affected-path
  verification, and only High-Risk work triggers formal research, architecture,
  planning, migration, or test-matrix artifacts.
- Completed the batched low-risk cultural review for FS-006 and FS-007; no
  Irish-language player text or specialist archaeological claim ships in the
  release.

### Planning

- Corrected the Feature Catalog to reflect the completed Version 0.1 release and
  added the Standard FS-006 Linen Household record for Version 0.5. Patrick Mee
  approved its XML-only implementation on 2026-07-12.
  Targeted research rejected a flax-to-brat chain in favor of historically
  defensible flax, linen, and a linen tunic.

### Development

- Implemented the first FS-006 playable checkpoint: ground-grown flax, raw-flax
  processing at three vanilla work locations, linen as a general Fabric, and a
  linen-only everyday tunic. Maintainer playtesting passed on 2026-07-13 after
  correcting stack-count texture paths and the processing bill's vanilla
  work-giver compatibility.
- Approved the reopened flax art pass after in-game review and integrated it into
  the Version 0.2 release candidate.
- Integrated FS-007 Central Hearth: a stone-stuffable, fueled central hearth that
  supports heat, light, gathering-spot behavior, campfire-grade cooking bills, and
  Emerald Isle oat-food bills through vanilla XML behavior.

## [0.1.0] - 2026-07-12

### The First Holding

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
- FS-003 Hand Quern passed Gate 1. Standalone implementation remains blocked; the
  hand quern must be implemented with FS-004 Milled Oats so the first
  player-facing slice has a real milling bill.
- Drafted FS-004 Milled Oats as a proportional Gate 1 specification for maintainer
  review. The draft records that quern plus milled oats is still not a complete
  player-facing chain unless FS-005 supplies at least one food consumer.
- FS-004 Milled Oats passed Gate 1. Implementation remains blocked until FS-005 is
  approved so the first processing implementation is a playable quern, milled-oats,
  and food-consumer vertical slice.
- Drafted FS-005 Oat Foods as a proportional Gate 1 specification for maintainer
  review. The draft defines oat porridge and oat flatbread as the player-facing
  payoff for the Version 0.1 processing chain.
- FS-005 Oat Foods passed Gate 1. The bundled FS-003 Hand Quern, FS-004 Milled
  Oats, and FS-005 Oat Foods vertical slice is implementation-authorized.
- Completed the bundled FS-003 Hand Quern, FS-004 Milled Oats, and FS-005 Oat
  Foods vertical slice with XML-only definitions, English localization, original
  runtime art, and a dedicated vanilla bill work giver. Static validation,
  complete in-game production-path verification, maintainer art review, and
  maintainer playtest passed (Gate 2, 2026-07-10).
- Added a permanent, separately staged developer-testing package with automated
  resource generation and release-safety guards. Developer assets are excluded
  from public packages.

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
[0.2.0]: docs/release/v0.2.0.md
[0.1.0]: docs/release/v0.1.0.md
[0.0.0]: docs/release/v0.0.0.md
