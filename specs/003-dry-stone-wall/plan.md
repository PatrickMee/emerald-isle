# Implementation Plan: FS-002 Dry-Stone Wall

**Status:** Approved
**Approved by/date:** Patrick Mee, 2026-07-06
**Branch:** `004-dry-stone-wall-specification`
**Date:** 2026-07-06
**Spec:** [FS-002](../../docs/specifications/FS-002-dry-stone-wall.md)
**Architecture:** [AR-002](../../docs/architecture/AR-002-dry-stone-wall.md)
**Definition of Ready:** Evidence complete — maintainer Ready decision pending
**Implementation authorized:** No

This compact plan exists because linked wall art, inherited wall behavior, public
save identifiers, and Core/Odyssey structural verification benefit from an explicit
contract. A second standalone IP-002 would duplicate this plan and is not required.

## Summary

Implement one stone-only, Stuff-based wall definition that inherits the current Core
`Wall` behavior. Override only the public identity, material filter, frozen cost/HP/work
values, menu icon, and linked dry-stone atlas. Add English def-injected localization.
Do not patch vanilla content, add runtime behavior, or create an Emerald Isle wall
framework.

## Technical Context

**RimWorld version/DLC:** RimWorld 1.6.4871 rev595 Core; Odyssey is the only
feature-specific DLC verification target; all supported DLC are tested together at
Version 0.1 release integration.
**Required DLC:** None.
**Optional DLC behavior:** No enhancement. Inherited wall behavior must remain safe
when every supported DLC is absent; Odyssey airtight and vacuum behavior must match
an eligible same-material vanilla wall.
**XML/C# decision:** One XML `ThingDef` plus def-injected localization. No C#,
Harmony, patch operation, assembly, or custom save state.
**Persistence:** One public Def name becomes the save contract. All persisted state
is owned by vanilla building, Stuff, paint, construction, attachment, room, and roof
systems. Removal while walls exist is unsupported.
**Dependencies/integrations:** Existing package contract, Core `Wall`, Core `Stony`
Stuff category, Core stone blocks, linked graphics, construction, room/roof,
attachment, replacement, paint, damage, and save systems.
**Art/audio/localization:** One original neutral-grayscale linked atlas and one menu
icon; standard inherited stone audio; English def-injected label and description.
**Testing:** XML/path/package checks; Core functional and visual smoke; Odyssey
airtight smoke; save/load and replacement; controlled work/HP/cost comparison;
proportional playtest and release-integration checks.

## Constitution Check

- [x] Gameplay/story purpose and tradeoff are explicit.
- [x] Design Bible reviewed and Feature Acceptance Checklist accepted.
- [x] RimWorld-native and cultural transformation reviews pass.
- [x] Active milestone and one-wall scope confirmed.
- [x] Vanilla comparison and 20% material/20% HP/~24% work hypothesis recorded.
- [x] XML-first decision applied; C# and Harmony are unnecessary and prohibited.
- [x] Compatibility, persistence, provenance, and localization are addressed.
- [x] Whole-system verification covers construction through save/load and release.
- [x] Planning is proportional; no framework, new resource, or duplicate IP is added.

## Research and Decisions

- Historical and gameplay research is already approved in
  `docs/research/version-0.1/dry-stone-wall.md`.
- RimWorld 1.6.4871 rev595 Core definitions were re-inspected on 2026-07-06.
  Core's named `Wall` definition already supplies every structural behavior frozen
  by FS-002. Official Odyssey and Anomaly content also inherit this parent, confirming
  it as a supported composition point.
- The definition will inherit `Wall`, not copy `BuildingBase`. Copying would create a
  brittle parallel wall contract and increase DLC/maintenance risk.
- The inherited material list will be replaced with `Stony` only. Core's five stone
  blocks are the supported balance set; modded stony materials are best-effort.
- The inherited material-specific wall icon list will be cleared so Core stone
  appearance does not silently replace the Emerald Isle menu icon.
- The inherited wall hotkey will be cleared to avoid a duplicate Structure-category
  shortcut. The wall remains available from the normal build menu.
- The linked graphic will use the vanilla wall link contract for walls and rock.
  Doors work through normal adjacency; fences do not share the wall link contract.
- The vanilla wall blueprint and damage overlays are retained unless the first
  in-game art checkpoint proves them unreadable. No extra placeholder asset is planned.

No separate technical `research.md` is useful: the decisions and official-source
evidence are bounded in AR-002. There is no custom data model or external API, so
`data-model.md` and `contracts/` would duplicate the public-contract table. The
existing package contract plus the verification section below replaces a redundant
feature quickstart.

## Feature Structure

### Runtime files to create during authorized implementation

- `Defs/ThingDefs_Buildings/EI_DryStoneWall.xml`
- `Languages/English/DefInjected/ThingDef/EI_DryStoneWall.xml`
- `Textures/Things/Building/Linked/DryStoneWall/EI_DryStoneWall_Atlas.png`
- `Textures/Things/Building/Linked/DryStoneWall/EI_DryStoneWall_MenuIcon.png`

### Records to create or update with implementation state

- `docs/art/assets/FS-002-dry-stone-wall.md`
- `docs/qa/evidence/FS-002-dry-stone-wall-test-matrix.md`
- `docs/specifications/FS-002-dry-stone-wall.md`
- `docs/product/feature-catalog.md`
- `docs/roadmap.md`
- `README.md`, `docs/README.md`, and `CHANGELOG.md` where state changes require it

`About/About.xml`, `LoadFolders.xml`, `tools/stage-mod.sh`, `Assemblies/`, `Source/`,
and `Patches/` require no planned change. The existing staging allowlist already
copies the four runtime artifacts.

## Delivery Slices

1. **Final art contract:** Produce the original atlas and icon, record provenance,
   verify dimensions/alpha/case, and inspect every link cell before XML references it.
2. **Loadable definition:** Add the wall definition and localization together; run
   XML/reference checks and stage a clean package with no missing texture.
3. **Core construction path:** Verify menu icon, five Core stone choices, cost, work,
   HP, construction, links, rooms, roofs, doors, attachments, paint, damage, repair,
   deconstruction, and bidirectional replacement.
4. **Persistence and Odyssey:** Verify save/load of representative states and compare
   airtight/vacuum behavior with a same-material vanilla wall.
5. **Balance and review:** Run proportional perimeter comparisons, visual review,
   250-tile static performance check, playtest, Design Review, and release integration.

Each slice must pass before the next; a contradiction with FS-002 stops implementation
for human review rather than changing gameplay in XML.

## Verification and Release

- Parse all package XML and reject duplicate `EI_` identifiers or unresolved refs.
- Confirm both PNG files exist at exact case-sensitive runtime paths and satisfy the
  linked-atlas/icon dimensions selected by AR-002.
- Stage with `./tools/stage-mod.sh`; compare staged runtime files with source inputs.
- Review the complete RimWorld log after every in-game checkpoint.
- In Core, compare all five stone materials against vanilla wall cost, HP, work,
  color, construction, damage, and replacement behavior.
- In Odyssey, prove room pressure/airtight behavior matches eligible vanilla stone
  walls and fails normally when a section is incomplete or destroyed.
- Save/load completed, damaged, under-construction, painted, attached,
  roof-supporting, and replacement states.
- Use development tools for the 250-tile performance/visual case; do not require a
  colony to hand-build an artificial test perimeter.
- Record exact build, mod list, steps, expected/actual behavior, logs, screenshots,
  tester, and date in the feature evidence record.
- Test the all-supported-DLC package and risk-based external-mod samples at Version
  0.1 integration, not as a blocker for the first implementation checkpoint.

Rollback before release is removal of the unreleased definition and assets. After a
public build, removal is unsafe for saves containing the wall; preserve the public
Def name and publish the removal warning.

## Complexity Exceptions

| Exception | Why required | Simpler alternative rejected because | ADR |
|---|---|---|---|
| None | The feature uses one inherited Core definition and existing package paths | No exception is needed | None |
