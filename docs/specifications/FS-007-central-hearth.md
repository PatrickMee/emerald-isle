# FS-007 Feature Record: Central Hearth

**Status:** Draft — awaiting maintainer approval<br>
**Milestone:** Version 0.5 — Living Culture<br>
**Risk class:** Standard<br>
**Owner:** Patrick Mee<br>
**Created:** 2026-07-13<br>
**Catalog candidate:** FU-01

## Recommendation

Prepare a small, permanent central hearth as the next Version 0.5 gameplay feature.
It should turn the holding's main room into a visible place of heat, cooking, and
daily gathering without introducing custom social systems, ideology behavior, or
new progression.

This draft does not approve implementation. Public identifiers below are tentative
until maintainer approval and release.

## Risk Class Justification

**Standard.** The intended slice is one XML-first building using proven vanilla
building, fuel, heat, light, and bill patterns. It creates normal save-visible defs
but no custom C#, Harmony patching, serialized state, broad compatibility branch,
or sensitive player-facing Irish-language content.

Reclassify before implementation if the approved behavior requires custom gathering
logic, new social thoughts, altered vanilla campfire behavior, DLC-specific behavior,
or performance-sensitive map scanning.

## Player Value

The feature gives early and mid-game colonies a culturally legible household center:
a more deliberate alternative to the temporary vanilla campfire for settlements that
have begun building in stone. The player decision is whether to spend stone, work,
space, and a fixed indoor footprint for a durable hearth that supports ordinary
room life, or keep using cheaper, more flexible vanilla fire and stove options.

The expected story is modest but visible: the first holding gains a warm core where
pawns cook, recover from cold, and define the room as lived-in rather than merely
functional.

## Scope

In scope:

- one buildable central hearth building;
- use of vanilla stone blocks and wood or another vanilla fuel input;
- heat, light, fueled operation, and cooking bills only if vanilla XML supports the
  complete behavior cleanly;
- placement and balance tuned against the vanilla campfire and fueled stove;
- English localization and original runtime art for the building.

## Explicit Exclusions

Out of scope:

- custom C#, Harmony, custom UI, map-wide gathering logic, or new job drivers;
- Ideology rituals, precepts, thoughts, parties, ceremonies, or room-role logic;
- Irish-language player-facing names;
- new fuel resources such as peat;
- smoke, ventilation, chimney, roof, air-quality, or fire-spread simulation;
- new research projects, tech tree changes, or progression currencies;
- food recipes, preserved foods, dairy systems, brewing, or feasts;
- bedrooms, dining-room redesign, furniture sets, or ringfort building kits;
- any dependency on FS-006 flax, linen, or linen apparel.

## Vanilla Comparison and Tradeoffs

Closest vanilla alternatives are the campfire, fueled stove, torch lamp, passive
cooler, and electric heaters. FS-007 must not replace all of them.

Proposed tradeoff direction:

| Comparison | Hearth advantage | Required cost or limit |
|---|---|---|
| Campfire | More permanent, durable, and settlement-defining | Higher work, stone cost, larger footprint, less portable |
| Fueled stove | Adds visible heat and household identity | Less efficient or less compact cooking role; not a full kitchen upgrade |
| Torch lamp | Combines light with warmth | Fuel burden, heat can be a liability in warm rooms |
| Electric heater | Works without electricity | Fuel and labor burden; poorer temperature precision |

The feature should fail approval if its final values make it the automatic best
early heat, light, or cooking choice at equivalent access.

## Historical and Cultural Basis

The hearth is a broad, low-uncertainty domestic and settlement pattern rather than
a claim about one exact Irish artifact. The design basis is proportional: Emerald
Isle already uses architecture, food, and craft to express ordinary life, and a
central household fire plausibly connects shelter, cooking, warmth, and social
meaning without requiring a precise reconstruction.

Implementation does not need deep historical research unless the final design
claims a specific period form, Irish term, ritual meaning, or named archaeological
type. A restrained English name avoids premature language review.

## DLC and Compatibility Behavior

- **Required DLC:** None.
- **Optional DLC enhancements:** None in this slice.
- **Behavior without DLC:** Complete Core behavior.
- **Compatibility:** Do not patch vanilla campfires, stoves, heaters, room roles,
  thoughts, rituals, or recipes. The hearth should be independently removable
  subject to RimWorld's ordinary missing-def behavior for buildings present in saves.
- **Released-contract note:** If approved and implemented, the building def,
  designation category, thing categories, recipe links, translation keys, and asset
  paths become public compatibility contracts at release.

## XML/C#/Harmony Recommendation

Recommendation: **XML-only**.

Use vanilla building, fueled, heat, light, graphic, construction, and bill patterns
only after verifying the exact RimWorld 1.6 defs during implementation. Do not add
C# to make pawns gather around the hearth, alter room roles, or merge unrelated
campfire and stove behavior. If vanilla XML cannot express a coherent tradeoff,
return the feature for maintainer review rather than expanding implementation.

Tentative public identifiers:

- `EI_CentralHearth`
- `EI_Building_CentralHearth_Label`
- `EI_Building_CentralHearth_Description`

These names are placeholders and are not compatibility commitments until release.

## Art Requirements

One original building texture set sized for normal RimWorld readability, with any
required damaged/selected states dictated by the verified vanilla parent pattern.
The art should read as a stone or stone-lined household hearth beside vanilla stone
walls, campfires, stoves, and early furniture. Ornament must be restrained and
functional, not decorative Celtic shorthand.

No pawn apparel, animal, worn-body, animation, UI framework, or high-variant art is
included.

## Objective Acceptance Checks

- [ ] The hearth can be built from approved vanilla materials on the intended
      terrain and category without adding a custom menu framework.
- [ ] A pawn can fuel and use it through vanilla jobs with no new recurring log
      errors.
- [ ] The hearth provides the approved heat/light behavior and does not outperform
      campfire, fueled stove, and electric heater across their full lifecycles.
- [ ] Any cooking bills included in the approved scope work through vanilla bill
      flow and do not obsolete the fueled stove.
- [ ] The building persists across save/load without broken fuel, bill, graphic,
      or temperature behavior.
- [ ] The complete build, fuel, use, deconstruct, and reinstall-or-non-reinstall
      behavior matches the approved tradeoff.
- [ ] Runtime art is readable at normal zoom, in darkness, and beside released
      Version 0.1 dry-stone walls.
- [ ] Core-only operation loads cleanly; supported DLC absence or presence does
      not change the feature.

## Risks and Stop Conditions

- If the feature is only a decorative campfire clone, stop and revise or reject it.
- If useful gathering or social value requires C#, Ideology hooks, thoughts, or
  custom jobs, stop and reclassify before implementation.
- If combining heat, light, and cooking makes the hearth a dominant early utility
  building, reduce scope or values before approval.
- If vanilla XML cannot produce the intended fueled behavior without patching core
  defs, stop rather than adding Harmony.
- If art scope grows into a broader furniture or architecture set, split the work
  and keep FS-007 to one building.

## Approval

**Decision:** Pending<br>
**Approved by/date:** —<br>
**Required maintainer decision:** Approve, reject, or revise FS-007 Central Hearth
as the next Version 0.5 gameplay feature. Implementation, XML, runtime art, and
localization remain unauthorized until explicit approval.

## Done Evidence

Not started. No gameplay files, XML, C#, textures, localization, architecture
records, implementation plans, task lists, or checklists have been created.
