# Ringfort Foundations Discovery Decision

**Status:** Rejected at Gate A by Patrick Mee, 2026-10-17<br>
**Owner:** Patrick Mee<br>
**Discovery started:** 2026-08-30<br>
**Milestone considered:** Version 1.0 Ringfort Foundations<br>
**Authority:** [Version 1.0 delivery plan](version-1.0-delivery-plan.md)<br>
**Game baseline checked:** RimWorld 1.6.4871 rev597, installed Core Defs and assembly<br>

## Decision

Do not implement a Ringfort Foundations settlement kit or make a ringfort the
Version 1.0 marquee feature. Patrick found no player value in the concept after
the equal-purpose layout comparison. The kit failed Gate A: its rounded outline
does not create a settlement decision beyond appearance. This withdraws the
ringfort commitment in the original delivery plan; it does not approve a
replacement feature or alter the released `EI_DryStoneWall`.

The tested minimum was the existing dry-stone wall, a stepped irregular-oval
layout, and one developer-only two-cell timber gate based on native
`Building_MultiTileDoor`. A straight-wall in-game test showed the gate opens and
closes. Its other room, pen, breach, raid, fire, repair, and persistence checks
were not completed. Passing them would not solve the shape's product-value
failure. No public gate Def, runtime art, save contract, C#, or Harmony was
created. The prototype Def and visual proof assets were removed after rejection.

## Deciding Comparison

The earlier wall comparison kept the oval fixed and compared different wall
materials. That demonstrated a dry-stone material/labor tradeoff, but did not
answer why a player would choose the oval over a practical rectangle **with the
same wall and gate**. The corrected comparison did:

| Same `EI_DryStoneWall` and two-cell gate | Irregular oval | Compact rectangle | Same-bounds rectangle |
|---|---:|---:|---:|
| Outer dimensions | 35 x 24 | 26 x 24 | 35 x 24 |
| Empty interior cells | 520 | 528 | 726 |
| Perimeter cells including gate | 113 | 96 | 114 |
| Dry-stone wall cells | 111 | 94 | 112 |
| Granite blocks for walls | 444 | 376 | 448 |
| Granite wall construction work | 226,440 | 191,760 | 228,480 |

The compact rectangle encloses eight more empty cells with 17 fewer walls, 68
fewer granite blocks, and 34,680 less wall work. A rectangle covering the oval's
full bounds uses only one more wall and encloses 206 more empty cells. Rectilinear
rooms, crops, and furniture are also easier to fit. The exact oval cell list and
metric script remain recoverable from discovery commit `0b90de9` in Git history;
the developer-facing visual artifacts are not retained in the working tree.

## Why Native Behavior Does Not Rescue the Form

The installed RimWorld build was checked for wall linking, multi-cell door
placement and pathing, room and roof regions, pens and forage, cover and firing
lines, fire, repair, and breaching. Walls link by cardinal neighbors. Rooms and
pens use connected regions and relevant cells; cover uses obstruction and lines
of fire; breaches use traversable grid paths. None supplies a verified reward for
a circular or oval perimeter. Full-height walls also block defenders' shots.
Individual raid outcomes were not proven in-game and are not claimed here.

The gate had a plausible **shape-independent** choice: the prototype used 40
wood, 1,000 work, and 120 HP, versus 50 wood, 1,190 work, and 208 combined HP for
two adjacent wooden doors. Its one flammable object would expose both cells on
failure. This might warrant a future standalone gate proposal, but it does not
justify a ringfort; this decision does not approve that proposal or retain the
prototype for it.

Terrain-following irregular walls, outdoor yards for animals and crops, and
central circular work ranges can all be useful. Vanilla or Emerald Isle walls in
a rectangular or map-adapted plan can serve those purposes without obliging the
player to build a ring. An outer bank, ditch, shape detector, raid modifier, or
custom placement tool would be a different feature beyond this discovery's
approved boundary, not a repair to the failed minimum kit.

The existing [dry-stone research brief](../research/version-0.1/dry-stone-wall.md)
already supports the historical relationship: cashels and raths could enclose
domestic work, animals, storage, and dwellings, with varied form and defensive
value. That evidence inspired the prototype but does not require the game to
reward or prescribe a ring shape.

## Consequences

- Stop permanent Ringfort Foundations work. Do not publish or rename the former
  developer gate into a public Def on this record.
- Keep the released `EI_DryStoneWall` and all other released content unchanged.
- Remove the ringfort-only developer Def and visual prototype artifacts, including
  the staged local test Def. Test saves containing that Def should not be treated
  as supported saves after the local copy is removed.
- Do not proceed to the conditional round tower as a substitute. A revised
  Version 1.0 product promise, scope, and sequence require Patrick's review.

This is a rejection of the current shape-driven marquee feature, not a claim that
Irish-inspired settlement architecture or optional player-built rounded layouts
can never appear in Emerald Isle. Any later proposal needs its own demonstrable
player decision and a direct comparison with a practical rectangular alternative.
