# Research Brief: Dry-Stone Wall

**Research ID:** RSC-003
**Feature:** BL-01 Dry-Stone Wall
**Release:** Version 0.1 - The First Holding
**Researcher:** Codex
**Reviewer:** Patrick Mee
**Status:** Approved
**Historical review:** Approved
**Gameplay review:** Approved
**Date:** 2026-07-05
**Approved:** 2026-07-05
**Research Definition of Ready:** Passed
**Approved scope:** `docs/product/version-0.1-approved-scope.md`
**Implementation authorized:** No

## Question and Design Need

Can one dry-stone wall variant provide historically grounded architectural identity
and a meaningful RimWorld construction choice without becoming a cheaper or stronger
vanilla stone wall?

This brief determines the historical frame, gameplay role, material abstraction, and
XML feasibility for BL-01. It does not approve final statistics, art, naming, or
implementation.

## Scope

**Primary period:** Early medieval Ireland, approximately AD 400-1100.
**Primary form:** Dry-stone enclosure walls associated with cashels and farmsteads.
**Supporting forms:** Early medieval field boundaries and building walls where their
dating and function are sufficiently clear.
**Later evidence:** Traditional and modern walling practice may explain material and
construction principles but is not assumed to reproduce early medieval work.
**Geography:** Ireland, with emphasis on rocky western landscapes where cashels and
surviving stone boundaries are prominent; this is not an exclusively western practice.
**Excluded:** A family of variants; new stone resources; ringfort generation; gates;
retaining walls; diagonal walls; mortared masonry; a nineteenth-century famine-wall
simulation; a reconstruction of one named monument.

## Executive Finding

Dry-stone construction is well supported in early medieval Ireland, but “dry-stone
wall” covers several materially and chronologically different things. The strongest
Version 0.1 reference is the **cashel**: a stone-walled counterpart to an earthen rath,
normally enclosing a farmstead or household space. Cashels varied greatly in size,
height, thickness, status, and defensive value [1, pp. 21-24]. Caherconnell provides
excavated evidence for a substantial, high-status example built around the late tenth
century, but its 3 m-high wall and more than 40 m enclosure were exceptional rather
than typical [2, pp. 133-134].

Early medieval farming landscapes also used stone walls, banks, ditches, and wooden
fences. Their chronology is much harder to establish because boundaries rarely
contain datable material. The familiar dense field-wall network visible in Ireland
today should not be presented as uniformly ancient: Ireland's National Inventory of
Intangible Cultural Heritage states that most of the current network was built in the
nineteenth century [3].

The preliminary gameplay recommendation is one **cashel-inspired, full-height exterior
wall** made from vanilla stone blocks. Its intended niche is material-efficient
perimeter definition with reduced durability and/or reduced structural utility, plus
a meaningful construction-work cost. It must not be a stronger “ancient stone wall.”
The expected implementation is XML only.

## Historical Background

### Dry-Stone Construction Across Periods

Dry-stone construction means building with stone and no mortar. Ireland preserves
examples from multiple periods and functions, including prehistoric field systems,
early medieval settlement and ecclesiastical enclosures, buildings, later field
boundaries, and continuing craft practice [3]. The longevity of the technique does
not make standing walls self-dating. Similar-looking fabric may belong to very
different centuries.

Ireland joined the multinational UNESCO Representative List entry for the art of dry
stone construction in 2024 [4]. This recognizes living knowledge and practice across
thirteen participating countries. It is evidence of continuing cultural value, not
proof that one technique is uniquely Irish or unchanged since prehistory.

### Cashels and Early Medieval Settlement

The Early Medieval Archaeology Project uses `cashel` for stone-walled settlement
enclosures and `rath` for earth-banked enclosures. Both bounded household or domestic
space that could contain dwellings, livestock, craft, storage, and other activities
[1, p. 21]. Cashels were not simply castles.

Cashels are most characteristic of rocky country with suitable building stone and are
more common in western Ireland. The absence of quarry ditches at many sites led the
EMAP authors to suggest that fieldstone may often have supplied the walls, although
this remains an inference [1, p. 22]. Local geology affected available stone, wall
appearance, and construction possibilities.

Cashel form was diverse. Internal diameters, wall thicknesses, and surviving heights
vary substantially; smaller enclosures need not have possessed the monumentality of
Staigue or Griannan of Aileach [1, p. 23]. Caherconnell in the Burren is unusually
large, more than 40 m in diameter with walls surviving to about 3 m. Radiocarbon
evidence places activity from the tenth century onward and the excavators distinguish
the site as an elevated-status example [2, pp. 133-134]. It cannot be treated as the
default wall for every household.

The word `ringfort` can mislead. Archaeological arguments summarized by EMAP find
that raths were primarily settlement and social enclosures, not purpose-built military
fortifications. They might be defensible or protect livestock during raids without
being optimized forts [1, pp. 23-24]. A RimWorld wall may participate in combat, but
its historical description should emphasize enclosing and protecting a holding rather
than claiming castle-grade defense.

### Field Boundaries

Early medieval Ireland had managed fields divided by banks, ditches, wooden fences,
or stone walls [1, p. 124]. Boundaries separated crops, preserved grazing, livestock,
households, and routes. Some stone boundaries survive around cashels and in regions
such as the Burren.

Dating is the central limitation. Field fences rarely contain diagnostic artifacts or
well-stratified samples. A radiocarbon sample beneath a dry-stone wall at Clonmoney
West produced an AD 350-610 range, but that is a terminus after which the wall was
built, not necessarily its construction date. Other boundaries are dated by associated
occupation or artifacts, often circumstantially [1, pp. 124-126].

Most of the extensive field-wall network visible today is much later. The National
Inventory records major nineteenth-century construction connected with land ownership,
landlord projects, farming, and periods of famine [3]. Version 0.1 must not call its
wall a “famine wall” or use later suffering as decorative authenticity.

## Cultural Significance

Dry-stone walls turn local material and skilled labor into place. Historically they
could define the household, separate fields, manage livestock, clear cultivable land,
provide shelter, and express continuity or status. Modern practice remains a living
vernacular craft recognized in Ireland's intangible cultural heritage inventory and
the UNESCO multinational inscription [3][4].

The feature should emphasize stewardship, skilled construction, and the act of making
a holding legible. It should not imply that Irish identity is timeless stonework, that
all communities built alike, or that monumental enclosure walls represent ordinary
households everywhere.

## Geographic Context and Materials

Stone availability follows geology. EMAP associates cashel concentration with rocky
country, especially western Ireland [1, p. 22]. Modern Irish wall references show
regional forms using limestone, granite, sandstone, rounded fieldstone, and mixed
material, with technique responding to stone shape and size [5][6].

Likely material categories include:

- locally gathered fieldstone or surface stone;
- larger foundation and facing stones;
- smaller pinning and hearting stone in double-faced walls;
- longer bonding or through stones where suitable;
- coping stones or other stable top courses;
- limited shaping tools and substantial manual handling labor.

These categories come mainly from documented modern craft. They explain physical
logic but do not prove that every early medieval wall used the same named components
or standardized sequence.

## Construction Methods

Current Irish guidance describes several regional wall forms rather than one national
standard. General structural principles include stone-to-stone contact, bonding across
joints, pinning, a packed heart, inward batter, large stones low in the wall, through
stones where available, and a stable coping course [5]. Single walls may use stones
that span the full width; double walls use two faces with smaller hearting between.

| Principle | Structural purpose | Historical confidence | RimWorld translation |
|---|---|---|---|
| No mortar | Stability comes from selection, placement, mass, and friction | Definitional | Visual identity and description, not a mortar resource |
| Broad base and batter | Lowers center of gravity and resists outward failure | High for modern craft; plausible historically | Readable tapered/irregular art; no custom physics |
| Bonding and through stones | Ties courses or faces together | High for modern craft | Construction work and durability abstraction |
| Hearting and pinning | Stabilizes voids and faces | High for double-wall modern forms | Implied by block cost and texture |
| Local stone selection | Form follows available geology and stone shape | High | Vanilla stone Stuff colors; no new local-stone Def |
| Repair by restacking | Failed sections can be rebuilt with compatible stone | High for living practice [6] | Vanilla repair/deconstruction behavior unless testing rejects it |

Construction without mortar is not synonymous with effortless or cheap. Skilled
selection, handling, fitting, and maintaining batter can be labor intensive. The
future specification should model any material efficiency against construction work,
durability, and structural capability.

## Historical Claims and Confidence

| Claim | Evidence | Confidence | Design use |
|---|---|---|---|
| Cashels were stone-walled counterparts to earthen raths | EMAP settlement synthesis [1, pp. 21-22] | High | Primary historical frame |
| Cashels were mainly optimized military forts | EMAP defensive review rejects this simplification [1, pp. 23-24] | Rejected | Describe household/perimeter protection, not a castle wall |
| Cashels were more common in rocky western areas | EMAP synthesis and distribution scholarship [1, p. 22] | High | Local-material identity without regional rules |
| Fieldstone often supplied cashel walls | Inference from geology and absence of quarry ditches [1, p. 22] | Medium | Supports material efficiency as a hypothesis |
| Early medieval field landscapes could include stone walls | Archaeology and documentary synthesis [1, pp. 124-126] | Medium to high | Supports boundary function |
| Any surviving field wall near an early site is early medieval | Dating limitations directly contradict this [1, pp. 124-126] | Rejected | Never date by appearance alone |
| Today's dense field-wall network is ancient | National Inventory says most was built in the nineteenth century [3] | Rejected | Avoid iconic-landscape anachronism |
| Caherconnell represents a normal household wall | Excavators identify exceptional size and status [2] | Rejected | Visual reference, not a universal template |
| One dry-stone technique is uniquely Irish | UNESCO inscription is multinational and regional styles vary [4][5] | Rejected | Specific Irish context without exceptionalism |

## Uncertainty and Contestation

- Stone structures may be repaired, robbed, rebuilt, or conserved, obscuring their
  original height and fabric.
- Standing form alone cannot securely date a dry-stone wall.
- Many field boundaries are dated by association rather than direct evidence.
- Material below a wall provides a terminus post quem, not an exact build date.
- Cashels vary by geology, region, date, household status, and later reuse.
- “Defensive,” “defensible,” symbolic, domestic, and livestock functions can overlap.
- Modern craft terminology and best practice cannot be projected unchanged into the
  early medieval period.
- Major monuments are overrepresented in visual sources because they survive and are
  photographed; they are not automatically representative.

## Cultural Sensitivities and Misconceptions

- Do not call every stone enclosure a fort, castle, or military installation.
- Do not present monumental elite sites as the normal dwelling of all people.
- Do not merge prehistoric monuments, early medieval cashels, monastic buildings,
  nineteenth-century field walls, and modern craft into one timeless style.
- Do not use famine labor or dispossession as picturesque flavor.
- Do not imply western landscapes are culturally more authentic than other regions.
- Do not describe mortarless construction as primitive or unskilled.
- Do not copy conserved or reconstructed monument fabric as though every visible
  course were original.

## Language and Naming

Modern Irish dictionary evidence gives `caiseal` both for an ancient stone fort and
an unmortared stone wall. `Balla fuar` also denotes a dry or unmortared wall, while
`balla cloiche` is a general stone wall [7]. These terms overlap but are not
interchangeable in every context.

Preliminary naming policy:

- Use the English source label `dry-stone wall` for immediate player comprehension.
- Use `cashel-inspired` in design documentation, not necessarily as the UI label.
- Do not call a single wall tile `cashel`; a cashel is an enclosure/site concept.
- Record `caiseal` and `balla fuar` as language notes pending qualified review.
- Avoid apostrophe variants such as `drystone` unless the localization style guide
  later standardizes them.

## Visual References

References are for study only. No photograph or illustration is cleared for reuse.

| Reference | Useful information | Rights and interpretation note |
|---|---|---|
| National Monuments Service, *Irish Field Monuments*, cashel/ringfort section [8] | Official overview and a conserved Leacanabuaile cashel image | Conservation may alter visible fabric; link only |
| Comber and Hull, Caherconnell figures [2] | Excavated high-status cashel, wall scale, Burren limestone context | Royal Irish Academy copyright; link only |
| Caherconnell Field School reports and photographs [9] | Stratigraphy, tumble, continuing excavation context | Preliminary reports can be revised; clear rights before reuse |
| Teagasc wall-type and construction diagrams [5] | Single, double, combination, batter, hearting, through stones | Modern craft, not medieval reconstruction; link only |
| Dry Stone Wall Association of Ireland illustrations [6] | Stone contact, shadow, regional wall character | Illustrations are credited; do not copy |
| Ask About Ireland regional gallery [10] | Granite, sandstone, limestone, and Feidin wall variation | Images have named copyright holders; link only |
| UNESCO 2024 inscription media [4] | Contemporary multinational practice | Not specifically early medieval or exclusively Irish; reuse requires rights review |

Original RimWorld art should read as irregular, gravity-set stone at normal zoom.
It should use shadowed joints and a less regular silhouette than vanilla dressed-block
walls while remaining compatible with straight grid placement and connected corners.

## RimWorld Vanilla Comparison

Verified against locally installed RimWorld `1.6.4871 rev595` Core definitions on
2026-07-05 [11]. These are comparison inputs, not proposed BL-01 values.

### Vanilla Wall

Core's wall is one Stuff-based `ThingDef`. It costs 5 units, has base 300 hit points
and 135 work, is impassable, fills its tile, blocks light and wind, holds roofs,
supports wall attachments, seals supported environments, uses heavy terrain for
stone, and links to walls and rock. Stone Stuff adds 140 work before a large work
factor and applies stone-specific hit-point factors.

| Material | Effective HP factor | Approximate wall HP | Relevant distinction |
|---|---:|---:|---|
| Sandstone blocks | 1.4 | 420 | Lowest stone HP; faster stone construction factor |
| Marble blocks | 1.2 | 360 | Lowest HP, higher beauty |
| Slate blocks | 1.3 | 390 | Modest HP and slight beauty factor |
| Limestone blocks | 1.55 | 465 | Mid-high durability |
| Granite blocks | 1.7 | 510 | Highest vanilla stone durability |

The final displayed work and beauty values must be captured in-game because Stuff
offset/factor calculation and inspection presentation are runtime concerns.

### Vanilla Fence

Core's fence costs 1 Stuff, has base 40 hit points and 70 work, allows passage at a
large path cost, does not block wind, and participates in pen containment rather than
full room or roof behavior [11]. It is a closer functional comparison for a low field
boundary, but not for the approved full wall variant.

### Design Space

BL-01 fails if it is merely a textured wall with identical statistics or a cheaper
wall with equal durability and structural utility. The credible space is a perimeter
wall that trades some combination of:

- fewer stone blocks for less durability;
- skilled/greater construction work for material efficiency;
- exterior enclosure utility for reduced roof or environmental sealing capability;
- distinct irregular art for a narrower material set;
- early accessibility for a real late-game limitation.

Whether the wall holds roofs or seals vacuum is a major specification decision. A
cashel-inspired exterior wall has historical support for standing enclosure use; full
vanilla structural behavior is a gameplay convention, not a historical requirement.

## Existing Mod Comparison

This comparison records adjacent player expectations. It does not authorize code or
asset reuse.

| Mod | Observed approach | Lesson | Verification limit |
|---|---|---|---|
| Fortifications - Medieval | Adds stronger lithic walls and describes dry-stacked stone as part of a broader medieval material/fortification suite [12] | Emerald Isle should avoid a stronger-wall arms race, new rubble resources, and broad medieval overhaul dependencies | Exact current Def values and licenses not inspected |
| Mixed Stone Blocks | Combines multiple stone types into Stuff usable by vanilla walls; current 1.6 notes document coloring and compatibility complexity [13] | Stuff color and custom wall graphics are a real compatibility surface; reuse vanilla stone blocks without mixed-stone processing | Dedicated to material mixing, not Irish wall identity |
| Medieval Walls and large medieval packs | Offer multiple castle/fortification pieces and broad themed architecture | Version 0.1 should ship one restrained wall, not a castle kit or new research tree | Current exact variants and stats remain unassessed |

The targeted scan did not identify a current standalone RimWorld 1.6 mod whose narrow
purpose and historical frame exactly match this cashel-inspired wall. Before release,
test at least one wall-texture replacement and one broad medieval architecture mod for
linking, icon, category, and replacement behavior.

## Gameplay Opportunities

### Strong Opportunities

1. **Define the first holding:** A visible perimeter makes the release concept legible
   in ordinary colony construction.
2. **Material-versus-strength choice:** Reduced block consumption can extend local
   stone at the cost of durability, work, or structural capability.
3. **Exterior compound planning:** A wall suited to yards, fields, and settlement
   edges can differ from an all-purpose room wall.
4. **Local material expression:** Vanilla stone Stuff preserves map geology and
   player choice without a new resource.
5. **Reusable architecture pattern:** Establishes linked art, Stuff filtering,
   construction, combat, roof, room, and save tests for later architecture.

### Opportunities to Reject for Version 0.1

- full ringfort or cashel generation;
- curved or diagonal wall systems;
- special gates, stairs, terraces, parapets, or embrasures;
- automatic moss, plant habitat, weathering, collapse, or restacking simulation;
- gathering fieldstone directly from terrain;
- new rubble, mortar, limestone, or mixed-stone resources;
- a beauty aura, cultural mood bonus, or ideology precept;
- exceptional resistance to explosions, breaching, or siege tools;
- regional build bonuses or named historic monuments.

## Balance Considerations

The intended player decision is: “Do I conserve processed stone and accept a less
durable or less structurally capable perimeter, or spend more blocks on a versatile
vanilla wall?”

The specification must compare:

- block cost and stonecutting work per protected tile;
- construction work and Construction skill threshold;
- HP across all five Core stone types;
- melee, bullet, explosion, breach, fire, and deconstruction outcomes;
- repair cost and time;
- roof support, room sealing, temperature, light, wind, and Odyssey vacuum behavior;
- cover/pathing and enemy targeting;
- beauty, wealth, meditation, paint, wall attachments, doors, vents, and coolers;
- replacement behavior between dry-stone and vanilla walls;
- early-, mid-, and late-game usefulness;
- exploit cases using cheaper material with unchanged defensive value.

Preliminary balance boundaries:

- never exceed the corresponding vanilla stone wall's HP;
- do not combine lower material cost, lower work, equal HP, and equal structural use;
- retain stone-type differences unless a specification proves that flattening them
  creates a better decision;
- avoid a custom research prerequisite for one vernacular wall;
- test complete perimeter cost rather than one tile in isolation.

## Technical Implementation Considerations

### Expected Core Def Surface

The intended feature appears expressible using standard RimWorld 1.6 XML:

- one building `ThingDef` using supported wall/building behavior;
- a Stony Stuff filter using existing Core stone blocks;
- linked graphics, blueprint, menu icon, damage presentation, and Stuff color;
- construction, terrain, designation, replacement, roof, room, and attachment fields;
- stable `EI_` Def and localization keys;
- no runtime component, custom worker, or patch.

This is feasibility analysis rather than XML design. Inheriting directly from the
named vanilla wall may also inherit relationships or future changes that are not
appropriate. The implementation plan must compare inheritance with an explicit
project base and validate the supported build.

### Material Recommendation

Use vanilla stone blocks as a deliberate abstraction. Historical fieldstone is not
equivalent to cut blocks, but adding raw-stone Stuff or one Def per geology would
expand resources, recipes, storage, art, and compatibility beyond Version 0.1. The
wall texture and lower material efficiency can communicate irregular construction
while retaining RimWorld's established stone economy.

### XML vs C# Recommendation

**Recommendation: XML only. C# and Harmony are not justified.**

Core already supplies construction, Stuff-derived stats, linked rendering, rooms,
roofs, cover, damage, repair, deconstruction, replacement, and serialization. If the
accepted design later requires custom collapse, topology, or adaptive material mixing,
the correct Version 0.1 response is to simplify or defer that behavior.

### DLC Policy

| Environment | Preliminary behavior |
|---|---|
| RimWorld 1.6 Core only | Full wall available using Core stone blocks |
| Royalty absent/present | No required behavior change; verify meditation/style interactions |
| Ideology absent/present | No required behavior change; verify styles and precepts do not misclassify it |
| Biotech absent/present | No required behavior change; verify pollution and mech construction paths only if affected |
| Anomaly absent/present | No required behavior change; verify related doors/attachments and breach threats |
| Odyssey absent/present | Explicitly verify airtightness, vacuum exchange, gravship restrictions, and related barriers |

No DLC is required. Optional DLC enhancements are not recommended for BL-01.

### Save and Removal Considerations

- The wall Def name becomes a save contract when implementation begins.
- Adding a new buildable should be low risk but requires an existing-save test.
- Removing the mod from a save containing wall instances can create missing Defs,
  alter rooms/roofs, expose temperature or vacuum, and remove defenses.
- Replacing vanilla walls must preserve attachments, zones, roofs, and resources.
- No custom serialized state is expected.
- The release must state the tested save-compatibility level.

### Performance

A static building with no ticker or custom code should have negligible simulation
cost. Linked graphics can still affect map mesh rebuilds and visual performance in
large perimeters. Test long walls, mixed materials, rapid blueprint placement,
damage, repair, fire, roof changes, and zoom levels. No per-tick behavior is acceptable.

### Art Requirements

Art effort is medium to high. One “variant” still requires enough connected states to
avoid broken corners, T-junctions, ends, doors, damage, blueprints, selection, snow,
night lighting, paint/Stuff colors, and mixed adjacency. The visual must:

- read as irregular dry-laid stone rather than dressed brick;
- preserve stone-material recognition without relying on color alone;
- avoid excessive noise at normal zoom;
- connect intentionally to itself and define whether it connects to vanilla walls,
  natural rock, doors, fences, and future Emerald Isle walls;
- remain original and traceable, not copied from source photographs or other mods.

## Risks

| Risk | Likelihood | Impact | Mitigation or gate |
|---|---|---|---|
| Wall is a cheaper equal vanilla wall | High | High | Require a visible durability, work, or structural limitation |
| Historical field wall and cashel are conflated | High | High | Use cashel enclosure as primary frame and label later field evidence |
| Cashels are presented as castles | Medium | High | Emphasize domestic enclosure, status, livestock, and bounded defense |
| Monumental Caherconnell becomes universal template | Medium | Medium | Record exceptional scale/status; use restrained art |
| Vanilla blocks undermine fieldstone authenticity | Medium | Medium | Document the gameplay transformation and avoid a new resource |
| Roof/vacuum behavior creates exploits or surprise | High | High | Make structural behavior explicit and test Core/Odyssey paths |
| Linked art fails at corners, doors, or mixed walls | High | Medium | Enumerate adjacency matrix and test at normal zoom |
| Texture replacement and wall mods conflict | Medium | Medium | Use project paths/IDs and targeted compatibility tests |
| Removal damages rooms or roofs | Medium | High | Declare removal behavior and test documented rollback |
| Irish term is used incorrectly | Low | Medium | English default and qualified review before visible Irish |

## Open Questions

### Questions Answerable During Specification and Testing

1. Does the wall hold roofs, create airtight rooms, and support wall attachments, or
   is it explicitly an exterior perimeter?
2. Which combination of block cost, work, HP, and structural limitation creates a
   useful choice without becoming an upgrade?
3. Should it connect visually to vanilla walls, natural rock, doors, and fences?
4. Should its stone filter accept all Core Stony Stuff and modded stone blocks, or a
   narrower supported category?
5. Should it be paintable, styleable, and a meditation focus like the vanilla wall?
6. What replacement tags permit safe wall-to-wall conversion without deleting
   attachments?
7. How should it behave with breaches, explosions, sappers, fire, temperature, and
   Odyssey vacuum?
8. Which current wall/texture mods form the supported compatibility sample?

### Human Review Resolutions

- The early medieval cashel enclosure is approved as the primary historical frame;
  the later field-wall network is explicitly excluded from that role.
- A full-height exterior perimeter wall is approved, with roof and airtight behavior
  deferred to specification.
- Existing vanilla stone blocks are approved as the Version 0.1 material abstraction.
- Material efficiency must be balanced through lower durability, greater work, or
  reduced structural utility.
- The evidence is sufficient. BL-01 may advance after the remaining ordered research
  briefs are completed and approved.

## Preliminary Recommendation

Advance BL-01 toward specification after completion of the ordered Version 0.1
research sprint.

The future specification should examine one cashel-inspired, full-height dry-stone
exterior wall using vanilla stone blocks and standard Core behavior. It should be
more material-efficient than a vanilla stone wall only if it is less durable, more
laborious, or less structurally versatile. It should add no new resource, gate,
generation, C#, Harmony, collapse simulation, or variant family.

## Research Review

### Summary

Early medieval Irish cashels provide strong evidence for substantial dry-stone
settlement enclosures, while field-boundary evidence supports wider agricultural use
but is difficult to date. The iconic modern field-wall landscape is largely later and
must not be treated as uniformly ancient. Material, form, and walling practice varied
with geology, function, status, region, repair, and date.

### Recommended Gameplay Implementation

One visually irregular, cashel-inspired stone perimeter wall that conserves some
material while sacrificing durability, construction time, or full structural utility.
It should help players define and protect a holding without replacing vanilla walls.

### Recommended Version 0.1 Implementation

Use one XML-only building and existing Core stone blocks. Focus on exterior enclosure,
linked art, material/work/HP tradeoffs, vanilla construction integration, and explicit
Core/Odyssey structural testing. Do not add a gate or wall family.

### Human Review Decision

**Decision:** Approved
**Reviewer/date:** Patrick Mee, 2026-07-05
**Corrections:** None; approved design boundaries are recorded in
`docs/product/version-0.1-approved-scope.md`.
**Approved uses:** Historical foundation and design input for the future BL-01
feature specification.

### Research Definition of Ready Checklist

This checklist records readiness to leave research, not readiness to implement.

#### Product and Identity

- [x] Catalog ID, milestone, purpose, and one-variant boundary are assigned.
- [x] The player decision and preliminary niche are explicit.
- [x] Constitution and Design Bible constraints are applied.
- [x] Explicit historical and Version 0.1 exclusions are recorded.
- [x] Human reviewer approves the cashel-based design frame.

#### Evidence and Design

- [x] Chronology, geography, form, materials, production, and cultural context are sourced.
- [x] Primary/field evidence and secondary synthesis are distinguished.
- [x] Later craft evidence is labeled rather than projected backward.
- [x] Uncertainty, dating limits, reconstruction risk, and sensitivities are recorded.
- [x] Vanilla and existing-mod comparisons identify measurable design questions.
- [x] Human reviewer confirms that the evidence is sufficient.

#### Engineering

- [x] XML-only feasibility is supported by verified RimWorld 1.6 Core behavior.
- [x] No new resource, C#, or Harmony need is identified.
- [x] Material abstraction and compatibility consequences are explicit.
- [x] DLC, save, performance, linked-art, and removal risks are recorded.
- [x] Specification-stage roof, room, attachment, replacement, and balance questions
  are recorded as non-blocking follow-up work.

#### Delivery

- [x] Art, localization, testing, and compatibility work are bounded.
- [x] Downstream architecture patterns and exclusions are recorded.
- [x] Human questions are resolved and approval recorded.

**Research decision:** Passed
**Project Definition of Ready:** Not yet evaluated. Hand-quern, milled-oats, and
oat-food research must be approved before specification and planning may begin.

## Sources

Accessed 2026-07-05 unless otherwise stated.

1. Aidan O'Sullivan, Finbar McCormick, Thomas R. Kerr, and Lorcan Harney,
   *Early Medieval Dwellings and Settlements in Ireland, AD 400-1100, Volume 1:
   Text*, Early Medieval Archaeology Project (2010), especially pp. 20-25 and
   124-126.
   [UCD repository record](https://researchrepository.ucd.ie/entities/publication/8ec7329a-4fd5-4555-a3b4-e0c2d6530b1f) |
   [report PDF](https://researchrepository.ucd.ie/rest/bitstreams/42708/retrieve).
   Source type: archaeological synthesis incorporating excavation evidence; not
   peer reviewed according to the repository record.
2. Michelle Comber and Graham Hull, “Excavations at Caherconnell Cashel, the Burren,
   Co. Clare: implications for cashel chronology and Gaelic settlement,”
   *Proceedings of the Royal Irish Academy* 110C (2010): 133-171.
   [DOI](https://doi.org/10.3318/PRIAC.2010.110.133) |
   [University of Galway record](https://research.universityofgalway.ie/en/publications/excavations-at-caherconnell-cashel-the-burren-co-clare-implicatio/) |
   [article PDF](https://www.burrengeopark.ie/wp-content/uploads/2014/08/Excavations_at_Caherconnell_Cashel_the_Burren_Co.pdf).
   Source type: peer-reviewed excavation publication.
3. Department of Culture, Communications and Sport, “Dry Stone Construction,”
   Ireland's National Inventory of Intangible Cultural Heritage.
   [National Inventory](https://nationalinventoryich.ccs.gov.ie/dry-stone-construction/).
   Source type: official heritage inventory; broad historical and living-practice
   overview, not a substitute for period-specific archaeology.
4. UNESCO, “Art of dry stone construction, knowledge and techniques,” Representative
   List of the Intangible Cultural Heritage of Humanity, multinational nomination
   extended to Ireland in 2024.
   [UNESCO](https://ich.unesco.org/en/RL/art-of-dry-stone-walling-knowledge-and-techniques-02106).
   Source type: official living-heritage record and contemporary media.
5. Teagasc, “Dry Stone Wall Building,” including modern Irish wall types,
   methodology, tools, and repair guidance.
   [Teagasc](https://teagasc.ie/rural-economy/rural-development/diversification/dry-stone-wall-building/).
   Source type: modern official craft guidance; not evidence of medieval technique.
6. Dry Stone Wall Association of Ireland, “What is a Dry Stone Wall?”
   [DSWAI](https://www.dswai.ie/what-is-a-dry-stone-wall).
   Source type: practitioner guidance and modern construction definition.
7. Teanglann, *Focloir Gaeilge-Bearla* entries `caiseal`, `balla`, and `cloiche`.
   [caiseal](https://www.teanglann.ie/en/fgb/caiseal) |
   [balla](https://www.teanglann.ie/ga/fgb/Balla) |
   [cloiche](https://www.teanglann.ie/ga/fgb/cloiche).
   Source type: authoritative dictionary reference; player-facing Irish still
   requires competent speaker review.
8. National Monuments Service, *Irish Field Monuments*, ringfort/cashel guidance.
   [NMS PDF](https://www.archaeology.ie/app/uploads/2025/01/irish-field-monuments.pdf).
   Source type: official public monument guidance; images include conserved sites.
9. Caherconnell Archaeology Field School, “Archaeology Dig Reports.”
   [Field School](https://caherconnell.com/archaeology/dig-reports/).
   Source type: primary preliminary excavation reporting; explicitly subject to
   revision before final publication.
10. Ask About Ireland, “Dry-Stone Walling,” regional examples and functions.
    [Ask About Ireland](https://www.askaboutireland.ie/learning-zone/secondary-students/art/design-craftwork/traditional-crafts-of-ireland/stone/dry-stone-walling/).
    Source type: educational overview and copyrighted visual reference.
11. Ludeon Studios, locally installed RimWorld `1.6.4871 rev595` Core data:
    `Data/Core/Defs/ThingDefs_Buildings/Buildings_Structure.xml` and
    `Data/Core/Defs/ThingDefs_Misc/Various_Stone.xml`, inspected 2026-07-05.
    Proprietary reference data; values paraphrased for design comparison.
12. AOBA, *Fortifications - Medieval*, Steam Workshop item 2501486827.
    [Steam Workshop](https://steamcommunity.com/sharedfiles/filedetails/?id=2501486827).
    Source type: current adjacent mod comparison; no code or assets reused.
13. The Nerd Wonder, *Mixed Stone Blocks*, Steam Workshop item 2076686656.
    [Steam Workshop](https://steamcommunity.com/sharedfiles/filedetails/?id=2076686656).
    Source type: current adjacent mod and compatibility comparison; no code or assets
    reused.

## Source and Asset Notes

- Period-specific historical claims rely primarily on sources [1] and [2].
- Living-craft sources [3]-[6] explain current practice and terminology; they do not
  establish an unchanged medieval method.
- Visual references remain link-only until license and provenance review.
- No source XML, code, texture, illustration, or mod asset was copied.
