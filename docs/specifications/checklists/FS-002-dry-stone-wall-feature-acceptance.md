# Feature Acceptance Checklist: FS-002 Dry-Stone Wall

**Feature:** [FS-002 — Dry-Stone Wall](../FS-002-dry-stone-wall.md)
**Milestone:** Version 0.1 — The First Holding
**Review date:** 2026-07-05
**Decision:** Accept for planning
**Reviewer:** Patrick Mee
**Prepared by:** Codex

Codex prepared the assessment against the canonical checklist. Patrick Mee reviewed
the feature and accepted it for architecture planning on 2026-07-05.

## Identity and Scope

- [x] It conforms to the Constitution and Design Bible.
- [x] It serves the active milestone and has a bounded one-wall slice.
- [x] It is Irish-inspired through documented early medieval cashel relationships.
- [x] It transforms the inspiration into Rim fiction rather than literal Earth history.
- [x] It avoids stereotypes, later field-wall conflation, and unsupported identity claims.
- [x] It fits existing Emerald Isle canon without a canon amendment.

## Gameplay and RimWorld Fit

- [x] It creates a clear coverage-versus-strength-and-labor decision.
- [x] Perimeter damage, repair, replacement, and scarcity can generate colony stories.
- [x] Players use normal structure, wall, repair, and replacement concepts.
- [x] Vanilla wall and fence comparisons are recorded.
- [x] It is not a strict upgrade at comparable access and total cost.
- [x] The material advantage has visible durability and work costs.
- [x] Starting availability and economy/wealth effects are defined.

## Research and Cultural Review

- [x] Period, geography, terminology, sources, uncertainty, and later evidence limits are linked.
- [x] Archaeology, interpretation, living craft, and project invention are distinguished.
- [x] The transformation from cashel enclosure to Rim perimeter choice is explicit.
- [x] Irish language remains non-player-facing pending competent review.
- [x] Historical knowledge is not required to use the wall.

## Technical and Architectural Fit

- [x] XML and Core wall behavior are the mandatory first approach.
- [x] C# is prohibited because no missing declarative behavior is identified.
- [x] Harmony is prohibited; no ADR is required.
- [x] Existing wall behavior meets the need more simply than a new system.
- [x] Dependencies are Core-only and optional DLC absence is safe by design.
- [x] Save, public-identifier, asset-path, and removal impacts are defined.
- [x] Worst-case scale and performance validation are defined.
- [x] One static wall creates a proportionate maintenance and test surface.

## Art, Audio, Language, and Accessibility

- [x] Required link states, material views, provenance, and acceptance views are defined.
- [x] Visual output must remain readable beside vanilla walls, rock, fences, and doors.
- [x] `Dry-Stone Wall` is functional, consistent, and localization-ready.
- [x] No player-facing Irish term requires review in FS-002.
- [x] Standard stone audio is explicitly sufficient.

## Decisions, Verification, and Release

- [x] ADR-0001 and ADR-0002 were searched; neither conflicts or requires supersession.
- [x] Normal, edge, failure, existing-save, replacement, and DLC paths are specified.
- [x] Save/load and targeted DLC/mod compatibility cases are planned.
- [x] Balance and comprehension hypotheses have measurable playtest questions.
- [x] Provenance, localization, release warning, and rollback impacts are known.
- [x] No speculative framework or later-version feature is introduced.

## Decision Record

**Failed or conditional items:** None.
**Required changes:** None before architecture review.
**Accepted rationale:** One historically grounded, XML-only wall creates a material,
labor, and durability tradeoff while retaining vanilla structural expectations.
**Related ADRs:** ADR-0002 governs the package contract only; no new ADR is proposed.
