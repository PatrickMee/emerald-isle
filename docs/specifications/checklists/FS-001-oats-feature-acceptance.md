# FS-001 Oats — Feature Acceptance Checklist

**Feature:** [FS-001 — Oats](../FS-001-oats.md)<br>
**Milestone:** Version 0.1 — The First Holding<br>
**Review date:** 2026-07-05<br>
**Decision:** Accept for planning<br>
**Reviewer:** Patrick Mee<br>
**Recorded by:** Codex

This record captures Patrick Mee's approval of FS-001 and authorization to enter
Architecture & Implementation Planning. It does not approve AR-001, IP-001, the
Definition of Ready, implementation, or release.

AR-001, IP-001, Definition of Ready, and implementation authorization were approved
later on 2026-07-05. This checklist remains the historical Feature Acceptance record;
post-implementation Design Review and release approval are still pending.

## Identity and Scope

- [x] It conforms to the Constitution and Design Bible.
- [x] It serves Version 0.1 and has a bounded one-plant/one-item slice.
- [x] Its early medieval Irish inspiration is specific and research-supported.
- [x] It transforms that inspiration into a Rim crop rather than literal Earth history.
- [x] It avoids stereotypes, romantic reconstruction, and unsupported hardiness claims.
- [x] It fits existing Emerald Isle canon without a canon amendment.

## Gameplay and RimWorld Fit

- [x] It creates a harvest-cadence, field-labor, batch-risk, storage, and future-processing decision.
- [x] Field loss, seasonal timing, labor pressure, storage, and recovery can generate stories.
- [x] It uses normal crop, food, animal, storage, trade, and UI concepts.
- [x] Rice, potatoes, and corn are the explicit vanilla comparisons.
- [x] It is not a strict upgrade at comparable access and total cost.
- [x] Its timing and labor advantages carry output, soil, hydroponic, and storage costs.
- [x] Start availability and economy effects are specified and testable.

## Research and Cultural Review

- [x] Period, geography, terminology, sources, and uncertainty are recorded in RSC-002.
- [x] Archaeology, interpretation, later folklore, and project invention are distinguished.
- [x] The transformation from widespread cereal evidence to medium-cycle Rim crop is explicit.
- [x] English functional naming avoids unreviewed player-facing Irish.
- [x] The feature is understandable without historical knowledge.

## Technical and Architectural Fit

- [x] Core XML and supported inheritance were evaluated first.
- [x] C# is not required.
- [x] Harmony is not required.
- [x] Existing systems meet the need more simply than a custom framework.
- [x] Core-only dependencies are minimal and optional DLC absence is safe.
- [x] Public definitions, translation keys, texture paths, save impact, and removal limits are documented in AR-001.
- [x] Runtime scale and performance validation are defined.
- [x] The feature creates no disproportionate maintenance or test-matrix cost.

## Art, Audio, Language, and Accessibility

- [x] Required assets, states, runtime paths, provenance, and acceptance views are defined in AR-001.
- [x] Visual acceptance requires normal-zoom comparison with vanilla crops.
- [x] Player-facing terminology is functional and localization-ready.
- [x] No player-facing Irish is included; competent review remains mandatory if that changes.
- [x] New audio is explicitly not applicable; vanilla sounds are reused.

## Decisions, Verification, and Release

- [x] ADR-0001 was reviewed and no supersession is required.
- [x] Acceptance scenarios cover normal, edge, failure, and missing-DLC paths.
- [x] Save/load, DLC, removal, and selected-mod matrix cases are planned.
- [x] Balance and comprehension hypotheses have structured playtest questions.
- [x] Documentation, attribution, changelog, package handoff, and rollback impacts are known.
- [x] Future milling depends on one stable raw-item contract without speculative infrastructure.

## Decision Record

**Failed or conditional items:** None at the Feature Acceptance gate.<br>
**Required changes:** Human review must approve AR-001 and IP-001; the separate
Version 0.1 build/package prerequisite must be resolved before implementation.<br>
**Accepted rationale:** FS-001 is historically grounded, gameplay-bearing,
vanilla-fluent, bounded, XML-only, and testable.<br>
**Related ADR:** [ADR-0001](../../adr/0001-oats-medium-cycle-xml.md)
