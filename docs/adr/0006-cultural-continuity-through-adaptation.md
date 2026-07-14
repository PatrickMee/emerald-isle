# ADR 0006: Cultural Continuity Through Adaptation

**Status:** Accepted
**Date:** 2026-07-14
**Decision owners:** Patrick Mee
**Related:** `docs/design/design-bible.md`, `docs/product/version-1.0-vision.md`,
`docs/roadmap.md`, [ADR-0005](0005-shared-stone-construction-language.md)

## Context

Emerald Isle began with strongly researched early medieval Irish material culture:
oats, dry-stone walls, domestic milling, oat foods, and now flax, linen, and the
central hearth. That direction is correct for the first releases, but it creates a
long-term product risk if treated as the whole identity of the mod. RimWorld
colonies progress from scarcity and vernacular settlement toward industrial,
spacer, ideological, biotech, anomaly, and world-scale play. If Emerald Isle
remains only an early-medieval content set, many authentic features will naturally
become obsolete and the mod will read as an early-game medieval add-on rather than
a durable culture expansion.

The Constitution and Design Bible already require RimWorld-native transformation,
gameplay value, and progression that widens identity rather than replacing earlier
content. This ADR clarifies that long-term product identity before the remaining
Version 0.5 scope is selected, without changing any released feature.

## Decision Drivers

- Emerald Isle should remain interesting across a full RimWorld playthrough.
- Irish inspiration should function as a living design language, not a fixed
  historical technology tier.
- Historical and archaeological evidence should guide durable cultural
  relationships, not force permanent use of obsolete tools.
- Released versions remain frozen and retain their role as the cultural root layer.
- Future releases need permission to express Irish-inspired identity through
  mature colony, high-tech, DLC, mythological, political, and world-scale contexts
  without drifting into generic Celtic fantasy or Earth simulation.

## Options Considered

### Keep Emerald Isle Focused on Early Medieval Material Culture

- Benefits: Very clear historical boundary; low risk of sci-fi pastiche.
- Costs and risks: Content becomes concentrated in early gameplay; later colonies
  outgrow the identity; the project risks becoming a medieval-themed item pack.

### Treat Later Progression as Generic Vanilla Technology

- Benefits: Avoids speculative cultural design for high-tech stages.
- Costs and risks: Emerald Isle identity fades as colonies mature; later features
  become mechanically detached from the mod's cultural roots.

### Add Separate Early, Medieval, Industrial, and Spacer Irish Tiers

- Benefits: Explicit full-progression coverage.
- Costs and risks: Encourages premature frameworks, artificial tech ladders, power
  creep, and content designed around tier-filling rather than player decisions.

### Adopt Cultural Continuity Through Adaptation

- Benefits: Preserves early medieval roots while allowing the culture to adapt
  through RimWorld progression; reinforces existing Constitution principles; keeps
  future features grounded in player decisions, evidence, and vanilla fit.
- Costs and risks: Requires future features to clearly explain which cultural
  relationship is being transformed, not merely claim that advanced content is
  Irish-inspired.

## Decision

Emerald Isle will be designed as an Irish-inspired culture that adapts across the
full RimWorld colony arc, not as an early-medieval technology tier.

Early medieval Ireland remains an important root source, especially for the
released holding content: ordinary domestic life, settlement identity,
agriculture, food, craft, and architecture. Future features may transform those
roots into later-game RimWorld contexts when doing so creates meaningful gameplay
and remains culturally and tonally coherent.

The guiding principle is:

> Emerald Isle should treat Irish inspiration as a living design language, not a
> fixed historical tech tier.

Future features must identify the cultural relationship they preserve or transform,
such as landscape and settlement, food and labor, craft and material, memory and
belief, hospitality and exchange, kinship and obligation, or myth and uncertainty.
They still pass the normal risk-tiered feature review. This decision does not
authorize new scope, new mechanics, new progression systems, C#, Harmony, or
speculative infrastructure.

## Consequences

**Positive:** Emerald Isle can remain recognizable and useful from the first
holding through mature colonies; future releases have a clear product test for
late-game and DLC-facing ideas; early features become cultural roots rather than
obsolete endpoints.

**Negative:** Future high-tech or mythology-facing features require more careful
framing to avoid green sci-fi, generic Celtic fantasy, or ungrounded invention.

**Neutral/follow-up:** The Design Bible, Version 1.0 vision, roadmap, and expanded
feature review prompts are updated with this principle in the same change. The
Constitution already supports the decision and does not require amendment.
Released features remain governed by their frozen records.

## Compatibility and Migration

This ADR changes product interpretation only. It creates no runtime content, Defs,
save data, DLC dependency, package metadata, or migration requirement.

## Validation

The decision succeeds when future proposals:

- keep released content as the root layer rather than rewriting it;
- identify a durable Irish-inspired cultural relationship, not just a historical
  object or visual motif;
- remain useful beyond a narrow early-game window when that is part of their
  stated purpose;
- preserve RimWorld-native play, tradeoffs, and vanilla readability;
- avoid generic medieval, Celtic, fantasy, or sci-fi reskinning; and
- do not introduce speculative frameworks before implemented evidence justifies
  them.

## Revisit When

- Version 0.5 planning cannot identify coherent full-playthrough cultural paths
  without violating the Design Bible.
- Late-game feature proposals repeatedly become generic technology with Irish
  labels.
- Historical review shows that a proposed continuity claim collapses distinct
  eras, regions, communities, or traditions in a misleading way.
- Player testing shows Emerald Isle identity still disappears after early colony
  development.

## Provenance

This decision was originally drafted on 2026-07-06 as a candidate ADR numbered
0003 on the `codex/cultural-continuity-adaptation` branch and adopted here,
renumbered and updated against the current governance and released versions.
