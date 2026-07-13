# FS-006 Feature Record: Linen Household

**Status:** Implemented — maintainer playtest passed<br>
**Milestone:** Version 0.5 — Living Culture<br>
**Risk class:** Standard<br>
**Owner:** Patrick Mee<br>
**Created:** 2026-07-12<br>
**Catalog candidates:** PL-02, AP-02

## Decision

**Player value:** Give colonies a soil-grown textile path that exchanges shorter
field time for additional crafting labor, then makes that cultural material
visible through one practical everyday garment. Linen remains useful throughout a
playthrough because it participates in vanilla Fabric recipes rather than forming
a closed Emerald Isle equipment tier.

**In scope:**

- one flax crop;
- raw flax as the harvested intermediate;
- one existing-bench bill that processes raw flax into linen;
- linen as a general Fabric textile;
- one linen-only, léine-inspired everyday tunic with the player-facing name
  **linen tunic**;
- English localization and original runtime art.

**Out of scope:** Flax oil, seeds, retting simulation, water requirements, spindle,
loom, new production building, dyes, embroidery, status colors, a brat cloak,
Irish-language player text, research projects, ideology behavior, C#, Harmony,
and DLC-specific behavior.

## Historical and Cultural Basis

Early medieval evidence supports household textile production, flax used for
linen, linen fragments at Irish sites, and multiple preparation stages before
spinning. The evidence is materially sufficient for a flax-to-linen loop but does
not support presenting one surviving complete garment as a universal reconstruction.

- Emma Hannah's Queen's University Belfast study records linen fragments at
  Ballyvass and Deer Park Farms, identifies tunics (`léine`) among standard dress,
  cites legal references to flax for linen production, and describes drying,
  seed removal, retting, drying, and spinning preparation. It also stresses that
  no complete early medieval Irish textile garment survives. See pp. 70–75:
  <https://pureadmin.qub.ac.uk/ws/portalfiles/portal/222215630/Craft_activity_and_settlement_in_Early_Medieval_Ireland_in_the_fifth_to_twelfth_centuries_AD._Vol._2.pdf>
- The Early Medieval Archaeology Project's economic synthesis describes the brat
  specifically as a woollen cloak and treats textile work as an interconnected
  domestic economy. See pp. 15–16:
  <https://researchrepository.ucd.ie/rest/bitstreams/42714/retrieve>
- Elizabeth Wincott Heckett's published analysis reports an archaeological basis
  for white linen tunics and woollen cloaks in early Irish literary display:
  <https://doi.org/10.1484/J.PERIT.5.112201>

Sources accessed 2026-07-12. These sources support the material and garment
categories, not one universal cut, color, or social meaning.

**Design conclusion:** The original flax-to-brat suggestion is rejected. A brat
belongs to a future wool-based feature. Version 0.5 may use a restrained linen
tunic inspired by the garment category without claiming an exact reconstruction.
The functional English name avoids premature Irish-language authority.

## Gameplay and Balance

Vanilla cotton takes 8 grow-days and directly yields 10 cloth, including in
hydroponics. The proposed linen route deliberately adds processing rather than
becoming better cotton.

### Proposed Crop and Processing Targets

| Target | Flax / linen | Vanilla comparison and intent |
|---|---:|---|
| Grow time | 6 days | Shorter field commitment than cotton's 8 days |
| Harvest | 8 raw flax | Lower harvest than cotton's 10 direct cloth |
| Sowing | Ground only | Cotton retains hydroponic flexibility |
| Processing batch | 20 raw flax → 20 linen | No hidden material loss |
| Processing work | 400 Crafting work | Labor is the cost of faster field turnover |
| Recipe users | Crafting spot; hand/electric tailoring benches | No new building or UI |

### Proposed Linen Stuff Targets

| Stat | Linen | Vanilla cloth | Intent |
|---|---:|---:|---|
| Max hit points | 70 | 80 | Less durable |
| Sharp armor power | 0.30 | 0.36 | Not an armor upgrade |
| Heat armor power | 0.14 | 0.18 | Not protective workwear |
| Cold insulation power | 10 | 18 | Poorer cold-weather textile |
| Heat insulation power | 24 | 18 | Warm-climate niche |
| Mass per unit | 0.022 | 0.026 | Modestly lighter |
| Market value | 1.7 | 1.5 | Processing labor remains economically visible |
| Flammability | 1.2 | 1.2 | No artificial safety advantage |

The linen tunic is an on-skin everyday garment restricted to linen. It targets
heat comfort and low mass, with less cold protection and durability than flexible
vanilla tribalwear. Proposed targets are 50 linen, 2,200 work, 0.35 cold-insulation
multiplier, 1.15 heat-insulation multiplier, and no meaningful armor role.

## Implementation Boundary

- **Recommendation:** XML-only. Installed RimWorld 1.6 Core provides verified
  patterns in `Plant_Cotton`, `Cloth`, `Apparel_TribalA`, Crafting Spot, Hand
  Tailoring Bench, and Electric Tailoring Bench.
- **Tentative public IDs:** `EI_Plant_Flax`, `EI_RawFlax`, `EI_Linen`,
  `EI_ProcessFlax`, `EI_LinenTunic`, and one linen-specific StuffCategoryDef.
  These become compatibility contracts only when released.
- **Persistence:** New plants, items, apparel, bills, stockpile filters, outfits,
  inventories, and trader stock can enter saves. Save/load is therefore an
  applicable Done check; removal retains RimWorld's ordinary missing-def risk.
- **Required DLC:** None.
- **Optional DLC enhancements:** None in this slice.
- **Behavior without DLC:** Complete Core behavior.
- **Compatibility:** Linen participates in vanilla `Fabric` recipes. The tunic
  accepts only linen. No patches, altered vanilla defs, or custom state.
- **Art:** Mature and immature flax, raw flax, linen textile, tunic ground icon,
  and the required worn directions/body coverage. Art must read at normal zoom
  beside cotton, cloth, and tribalwear.
- **Routine field values:** Unlisted XML fields inherit the closest verified
  vanilla pattern. Implementation must stop for review if a default changes the
  approved player tradeoff, scope, compatibility, or visible behavior.

## Acceptance Checks

- [x] Flax appears in growing-zone selection, grows only in ground cultivation,
      and harvests raw flax at the approved targets.
- [x] A pawn can process raw flax into linen at all three approved vanilla work
      locations without a custom work giver.
- [x] Linen stores, trades, and works in representative vanilla Fabric recipes.
- [x] The linen tunic can be made only from linen, equips correctly, and provides
      the approved warm-weather tradeoff without replacing tribalwear.
- [x] Crop, processing, textile, and garment persist across save/load without a
      new log error or broken bill/filter reference.
- [x] Runtime art is readable at normal zoom and original/provenance-recorded.
- [x] The complete flax → linen → tunic path works in RimWorld 1.6 Core with a
      clean relevant log.

## Risks and Stop Conditions

- If the processing bill creates labor with no meaningful crop-choice payoff,
  stop for balance review rather than deleting or adding stages during coding.
- If vanilla XML cannot restrict the tunic to linen while keeping linen usable as
  general Fabric, reclassify the feature before adding C# or patches.
- If worn-apparel art expands beyond a manageable Standard slice, reduce visual
  variants rather than adding framework code or changing gameplay scope.
- Any Irish-language player-facing name requires qualified language review and is
  outside this proposal.

## Approval

**Decision:** Approved<br>
**Approved by/date:** Patrick Mee, 2026-07-12<br>
**Conditions:** Implement the recorded XML-only Standard slice. Stop for review
if a listed stop condition occurs or the approved tradeoff cannot be expressed
through verified vanilla XML.

## Done Evidence

Patrick Mee accepted the affected in-game path on 2026-07-13 after testing the
flax crop, harvested stacks, flax-processing bill, linen, and tunic in RimWorld
1.6. The existing colony and bill survived the restarts used to install corrected
definitions. The final Player.log contains no Emerald Isle definition, texture,
recipe, or job error; unrelated pre-existing game/mod warnings remain outside
this feature.

Static and package verification also passed: all XML parses, all six public defs
resolve, the linen-only Stuff filter coexists with vanilla `Fabric`, all 26 RGBA
runtime textures resolve, the developer scenario automatically discovers all
three new item defs, and public release staging excludes developer content.

Three defects found during playtest were corrected without changing approved
gameplay: stack-count art moved into the directories required by
`Graphic_StackCount`; Developer Tools gained dependency URLs; and the processing
recipe dropped an incorrect `requiredGiverWorkType`, matching vanilla
patchleather so Tailoring benches and the Crafting Spot can use their own vanilla
work givers. FS-006 is implemented but remains unreleased until its release gate.
