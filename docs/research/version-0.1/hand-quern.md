# Research Brief: Hand Quern

**Research ID:** RSC-004
**Feature:** PR-01 Hand Quern
**Release:** Version 0.1 - The First Holding
**Researcher:** Codex
**Reviewer:** Patrick Mee
**Status:** Approved
**Date:** 2026-07-05
**Approved:** 2026-07-05
**Historical review:** Approved
**Gameplay review:** Approved with conditions
**Research Definition of Ready:** Passed with conditions
**Approved scope:** `docs/product/version-0.1-approved-scope.md`
**Implementation authorized:** No

## Question and Design Need

Does the historical and gameplay evidence support one XML-only hand quern as a
meaningful link between oats and milled oats, or would the building add only a
mandatory labor tax and inventory step?

The frozen scope makes the hand quern conditional. This brief evaluates historical
form, household context, materials, labor, gameplay value, vanilla fit, and technical
feasibility. It does not decide milled-oats nutrition, food recipes, exact statistics,
art, or implementation.

## Scope

**Primary period:** Early medieval Ireland, approximately AD 400-1100.

**Primary form:** A small, manually operated rotary quern used for domestic grain
processing.

**Geography:** Ireland, using evidence from secular settlements, cashels, crannogs,
ecclesiastical sites, excavation syntheses, and relevant object records. Regional
stone sources are context, not a gameplay resource system.

**Supporting evidence:** Irish Iron Age adoption; later Irish survival of rotary
querns; experimental rotary-quern studies; early medieval Irish watermills as the
necessary technological comparison.

**Excluded:** Saddle querns as the Version 0.1 design; animal-powered mills;
windmills; watermill simulation; powered automation; new stone resources; regional
quern variants; flour-quality simulation; grinding animations; gender restrictions;
ritual or supernatural mechanics.

## Executive Finding

The historical case is strong. Rotary querns were established before the early
medieval period, quern fragments are common on early medieval Irish settlements, and
the major archaeological synthesis explicitly identifies hand querns as domestic
grain-processing equipment [1, pp. 120-124]. Quernstones occur at ordinary raths,
cashels, crannogs, ecclesiastical sites, and specialized production contexts [1,
pp. 140-141; 2, pp. 67-72].

The evidence does **not** support depicting the quern as Ireland's only milling
technology. Horizontal and vertical watermills existed in Ireland by at least the
early seventh century, and mill building intensified during the eighth and ninth
centuries [1, pp. 120-122; 3]. Hand and water-powered processing coexisted at
different scales.

The RimWorld implementation appears fully expressible in XML as a small unpowered
worktable with bills. Historical authenticity and XML feasibility alone do not prove
gameplay value. A quern should remain in Version 0.1 only if the milled-oats and
oat-food research establishes a real choice between retaining raw oats and spending
pawn labor to unlock a useful processed form. Without that downstream payoff, the
quern should be removed rather than preserved as themed busywork.

## Historical Background

### From Rotary Quern to Early Medieval Household Tool

Hand-operated rotary querns followed earlier reciprocal or saddle-quern technology.
Irish scholarship places rotary-quern introduction in the Iron Age, before the
project's primary period [3][4]. By AD 400-1100, the rotary quern was an established
piece of grain-processing equipment rather than a new invention.

The Early Medieval Archaeology Project (EMAP) describes hand-quern processing as
domestic in scale and identifies it as the method used before early medieval
watermills appeared [1, p. 120]. Quernstones are repeatedly listed among the basic
utilitarian objects recovered from early medieval settlements. Their presence with
hearths, tools, plant remains, and domestic structures supports everyday processing,
though a fragment alone cannot prove which cereal was ground or who operated it.

### Coexistence with Watermills

Early medieval Ireland adopted water-powered milling unusually early. Archaeological
and dendrochronological evidence places horizontal and vertical watermills in Ireland
by at least the early seventh century [1, pp. 120-122; 3]. EMAP records an intense
period of mill construction around AD 750-850, while sites such as Raystown contained
multiple mills and grain-drying facilities [1, pp. 121-122].

This changes the feature interpretation. The hand quern represents local,
low-infrastructure household processing, not technological isolation. Watermills
could process more grain, but required suitable water, construction, maintenance,
and organized access. The evidence does not justify adding those systems to Version
0.1; it does justify leaving a future throughput upgrade seam.

### Archaeological Presence

EMAP records quernstones or their manufacture at settlements across Ireland. Examples
include Lagore and Moynagh in County Meath, Cahercommaun in County Clare, Carraig
Aille in County Limerick, and Nendrum in County Down [1, pp. 140-141; 2, pp. 71-72].
Large fragment counts at some sites may indicate production or exchange, but fragment
counts also reflect breakage, reuse, excavation history, and recovery practice.

A 2021 excavation report describes a complete but unstratified rotary disc quern from
County Wicklow. It comprised two granite stones roughly 0.38-0.42 m across. The upper
stone had a central feed opening and a separate handle hole; the lower had a spindle
hole, and both working faces showed circular wear [5]. Because the object came from
modern disturbance, it is useful for morphology but cannot anchor an early medieval
date or represent every regional form.

### Reuse, Decoration, and Deposition

Some quern fragments were reused in buildings, thresholds, grave markers, or other
contexts. A medieval rotary-quern fragment from a cashel at Caherfurvaus bears
inscribed circular and cross decoration [6]. Such finds show that querns could carry
meaning beyond immediate use, but motives are not uniform or always recoverable.

Version 0.1 should not convert contested interpretations of breakage, deposition, or
decoration into ritual bonuses. The most defensible focus is the quern's ordinary
role in turning household grain into a processed ingredient.

## Cultural Significance

A quern places food labor inside the holding. It connects cultivation, storage,
manual work, and meals at a human scale. Archaeological ubiquity makes it a stronger
marker of ordinary domestic life than a monumental or elite object.

Grinding has often been gendered in historical and ethnographic scholarship, and
modern experimental research has frequently studied female operators [7]. That does
not justify restricting the RimWorld job by gender, importing a universal labor role,
or presenting drudgery as cultural flavor. Any pawn with the relevant work type
should be able to operate the quern.

The feature should communicate skilled repetitive labor without calling the tool
primitive. A rotary quern was an efficient technological development relative to
reciprocal grinding, while watermills later offered larger-scale processing [7].

## Geographic Context

Quern evidence is geographically widespread, but geology affected stone selection
and movement. EMAP notes generally local rock use alongside sourced or exchanged
quern and millstone material. Examples connect quernstones in County Down with the
Mourne Mountains and identify west Wicklow granite production serving parts of
Leinster [2, pp. 71-72].

This supports a broad local-stone visual identity. It does not support a Version 0.1
quarry network, county-specific statistics, or a claim that one rock type defined
Irish querns. The game should use existing vanilla stone materials rather than
simulate geological procurement.

## Form, Materials, and Operation

### Physical Form

A rotary hand quern typically consists of:

- a stationary lower stone;
- an upper stone that rotates against it;
- a central opening through which grain is introduced;
- a spindle or centering arrangement;
- a socket and wooden handle used to turn the upper stone;
- dressed or worn grinding faces.

The precise profiles, handle arrangements, dimensions, and dressing patterns vary.
The Wicklow example provides one measured disc-quern reference, not a universal
template [5].

### Materials

The historical material requirement is primarily suitable stone, with wood for the
handle and possibly small fittings or supports. Recorded Irish examples include
granite and other locally or regionally available stone. Rock selection affected
wear, grit, durability, shaping effort, and grinding performance, but the evidence
does not justify exposing those as separate Version 0.1 mechanics.

### Manufacture

EMAP's stone-working synthesis describes a broad sequence for quern and millstone
production: acquire a suitable rough-out, shape a circular stone, perforate openings,
and dress the grinding surface [2, pp. 71-72]. Some rough-outs were prepared at stone
sources; others may have been completed at settlements. Evidence for actual work
areas is limited because stone waste is difficult to recognize.

The RimWorld construction cost should abstract this labor through vanilla stone
blocks, a small amount of wood if needed, and construction work. Version 0.1 should
not introduce raw quernstone, separate upper/lower-stone items, dressing recipes, or
wear replacement.

### Use and Output

Grain passes between the stones as the upper stone turns, emerging in a ground form.
Experimental output depends heavily on quern form, grain, operator experience,
moisture, stone adjustment, and desired fineness. A modern controlled study used a
rotary rate of 0.05 kg per minute for its specific Iron Age replica and grain, while
explicitly warning that results vary by equipment and output quality [7, pp. 3, 6].

Those measurements establish that hand grinding is real labor and that rotary
technology improves throughput. They are not a direct RimWorld recipe timer.

EMAP notes that damp grain is easier to clear from a hand quern than from a large
mill because the upper quernstone can be lifted and cleaned [1, pp. 123-124]. This
does not justify a moisture mechanic.

## Historical Claims and Confidence

| Claim | Evidence | Confidence | Design use |
|---|---|---|---|
| Hand querns processed grain at domestic scale in early medieval Ireland | EMAP synthesis [1, p. 120] | High | Core historical role |
| Rotary querns were established before AD 400 | Irish archaeological synthesis and Kilbegly comparison [3][4] | Medium to high | Use rotary, not saddle, as primary form |
| Quernstones were common settlement objects | EMAP settlement and craft syntheses [1][2] | High | Ordinary-holding identity |
| Every holding owned and used one quern | Archaeology cannot demonstrate universal ownership | Low | Must not claim universality |
| Oats were always the grain ground in recovered querns | Querns rarely retain species-specific evidence | Low | Oat linkage is gameplay transformation |
| Watermills replaced hand querns during the early medieval period | Evidence shows coexistence and different scales [1][3] | Rejected | Preserve future upgrade space |
| One stone type or shape was standard across Ireland | Regional and chronological variation contradicts this | Rejected | Restrained composite visual reference |
| Quern operation was exclusively women's work | Comparative evidence is gendered but not universally determinative [7] | Rejected | No pawn-gender restriction |
| Decorated or deliberately broken querns had one ritual meaning | Contexts and interpretations vary | Low | No ritual mechanic or mystical description |

## Primary and Secondary Reference Assessment

### Primary or Field Evidence

- Excavated quernstones and production evidence synthesized in EMAP [1][2].
- The measured Wicklow disc quern, with its disturbed context explicitly recorded [5].
- The decorated Caherfurvaus quern fragment and find record [6].
- Archaeological structures and dated material from early Irish watermills [1][3].

### Secondary and Experimental Evidence

- EMAP's national excavation and production syntheses [1][2].
- O'Sullivan and Downey's overview of Irish quernstones [4].
- Overland and O'Connell's peer-reviewed Kilbegly study [3].
- Hora and colleagues' experimental energy and throughput study [7].

No single measured quern or experiment is treated as a universal Irish standard.

## Uncertainty and Contestation

- Quern fragments are portable, frequently reused, and often recovered outside their
  original working position.
- A quern fragment rarely identifies the cereal processed on it.
- Fragment counts do not map directly to household ownership or production volume.
- Morphology changed through the Iron Age, early medieval, medieval, and later
  periods; later survival cannot be projected backward unchanged.
- Stone provenance is known for only a subset of finds.
- Watermill distribution reflects discovery and development bias as well as past use.
- Experimental rates vary with equipment, grain, adjustment, skill, moisture, and
  target fineness.
- Structured deposition and decoration can be meaningful, accidental, practical, or
  the result of reuse; one explanation cannot cover every context.
- The historical evidence proves domestic milling, not that an extra RimWorld
  intermediate item creates good gameplay.

## Cultural Sensitivities and Misconceptions

- Do not call the hand quern primitive, uniquely Irish, or unchanged for millennia.
- Do not imply early medieval Ireland lacked water-powered technology.
- Do not assign operation by pawn gender, social class, ethnicity, or ideology.
- Do not romanticize repetitive food labor or turn hardship into decorative flavor.
- Do not present one decorated fragment as a standard national style.
- Do not convert uncertain deposition into magic, worship, or mood effects.
- Do not use later folk practice as direct evidence for every early medieval detail.
- Do not describe milled oats as historically exclusive when querns processed
  multiple cereals.

## Language and Naming

The English term `hand quern` is precise enough for player-facing use and matches the
canonical scope. `Quern` already means a hand mill, but the modifier distinguishes
the object from future powered milling and helps players unfamiliar with the term.

Modern and historical Irish sources use `bró` for a quern or hand mill. The official
Placenames Database discusses this sense while also demonstrating why placename
etymologies require caution [8].

Preliminary policy:

- Use `hand quern` as the English source label.
- Explain its function directly in the description.
- Record `bró` as a research term, not decorative UI text.
- Do not use `millstone`, `grindstone`, and `quern` interchangeably.
- Any visible Irish term requires competent speaker review.

## Images and Visual References

References are for design study only. No image is cleared for copying into the mod.

| Reference | Useful information | Rights and interpretation note |
|---|---|---|
| Wicklow rotary disc quern report and image [5] | Two-stone proportions, central feed, handle socket, wear | Copyrighted field-report image; unstratified and not a dated template |
| Caherfurvaus decorated quern fragment [6] | Circular/cross incision and handle reconstruction | Link only; fragmentary medieval object awaiting museum deposition |
| EMAP stone-working report [2] | Site range, stone sourcing, manufacture, fragment counts | Academic reference; diagrams/text are not production assets |
| Hora et al. experimental study [7] | Operator posture, rotary motion, physical scale | Modern replica and experiment, not an Irish reconstruction |

The art brief should triangulate multiple references and create an original,
restrained object rather than reproduce the decoration or profile of one find.

## RimWorld Vanilla Comparison

The local supported build inspected for this brief is RimWorld `1.6.4871 rev595`.
Core has no grain-milling building or generic flour intermediate. It does provide the
complete declarative worktable and bill systems needed for the feature [9].

| Vanilla object | Relevant behavior | Lesson for the hand quern |
|---|---|---|
| Crafting spot | 1x1, free, standable, bills, 50% work speed, no hit points | Small low-infrastructure production is vanilla-readable; a permanent quern should not be a free spot clone |
| Hand tailor bench | Unpowered, bill-driven, 50% work speed, 3x1, normal construction | Vanilla communicates manual throughput through worktable speed without custom behavior |
| Stonecutter's table | Bill-driven material conversion using Crafting/General Labor, stone-related, 3x1, Stonecutting-gated | Closest transformation pattern, but too large and technologically broad to serve as the quern |
| Fueled/electric stoves | 3x1 kitchen worktables with bills and explicit power/fuel differences | Milling should remain separate from cooking if the intermediate step survives |
| Butcher spot/table | Low-infrastructure and equipped versions trade efficiency, durability, and footprint | A future powered mill could extend the pattern, but Version 0.1 must not build it speculatively |

Core worktables already handle bill configuration, ingredient search, hauling,
reservations, job interruption, product creation, skill/work-speed modifiers, and
save persistence. A new interface is unnecessary.

## Existing Mod Comparison

This comparison records adjacent expectations and compatibility risk. No code, data,
names, or assets are approved for reuse.

| Mod | Publicly documented approach | Lesson | Verification limit |
|---|---|---|---|
| Medieval Overhaul | Uses a grindstone to turn wheat into flour and later offers automated wind/water processing in a broad medieval conversion economy [10] | Players understand manual-to-automated milling, but Emerald Isle should avoid an overhaul-sized chain, byproducts, and unattended machinery | Exact current Defs, balance, dependencies, and license were not inspected locally |
| Vanilla Cooking Expanded | Uses flour for large bakes within a broad food framework and documents compatibility naming/patch concerns [11] | Flour-like intermediates create integration pressure; Emerald Isle must avoid claiming universal flour compatibility | Framework behavior and current flour Def contracts were not inspected locally |

Public support discussions report duplicate flour and ingredient-category problems
when broad food and medieval overhauls interact. These reports are discovery evidence,
not proof of a specific defect. Before release, the project should inspect current
package IDs and Defs for a small supported compatibility sample.

## Gameplay Validation

This assessment is independent of the strong historical evidence.

### What Meaningful Player Decision Does the Hand Quern Create?

Potentially: “Do I retain oats as flexible raw grain, or commit pawn labor and
hauling to create a processed ingredient that enables a stronger food plan?” The
decision exists only if both paths remain useful. If every valuable oat use requires
milling, operating the quern is compulsory labor rather than strategy.

### What Gameplay Problem Does It Solve?

It can provide an early, unpowered way to transform a storable crop into specialized
food inputs without requiring electricity, fuel, or a large production bench. It
also makes the agricultural chain legible through normal RimWorld bills. It does not
solve a Core deficiency by itself because direct cooking recipes could process oats
without a separate building.

### What New Stories Does It Enable?

- A labor-poor holding chooses immediate raw-grain use over better processed food.
- A harvest surplus becomes a winter milling project when pawn time is available.
- An outage or low-technology colony can continue small-scale food processing.
- A damaged or overcommitted production chain forces prioritization between food now
  and food with a later payoff.

These stories depend on actual scarcity, timing, and alternative uses; the existence
of an extra bill alone does not create them.

### What Would Players Lose If It Did Not Exist?

Players would lose a visible household-processing step, an unpowered production
object, and the raw-versus-processed scheduling decision. They would not lose access
to oat foods if recipes simply incorporated equivalent milling labor at a stove.
Therefore the mechanical loss is moderate and conditional, not foundational.

### Strategy or Additional Clicks?

The bill system can automate repeated work, so the primary cost is pawn labor,
hauling, storage, and another production object rather than continuous manual clicks.
Even so, it becomes inventory churn if players always issue the same bill and always
process every oat. The downstream briefs must prove a reason to vary that behavior.

### Meaningful Tradeoff or Compulsory Labor?

The intended tradeoff is low capital and no power in exchange for slow manual
throughput, plus the opportunity cost of converting flexible raw oats. It becomes
compulsory labor if raw oats have no useful destination or milled oats are required
for all competitive food. Both states must remain viable.

### Could the Same Gameplay Be Achieved More Simply?

Yes. A direct oat-food recipe could include additional cooking work and remove the
quern, milled-oats item, separate bills, hauling, storage, art, and compatibility
surface. That is the default simpler alternative. The separate quern earns its place
only if staging, scheduling, low-tech processing, or multiple downstream uses create
a decision that a longer cooking recipe cannot reproduce.

### Does the Added Complexity Justify Itself?

Not yet unconditionally. The XML and performance costs are low, but player concepts,
art, storage, hauling, recipe filters, save contracts, and mod compatibility are real.
The next two research briefs must establish at least one clear processed-oat benefit,
one useful raw-oat path, nutrition-safe conversion, and manageable labor/hauling.

**Gameplay recommendation: Recommended with Conditions**

Conditions:

- Raw oats retain at least one useful non-milling path.
- Milled oats unlock a clear, bounded benefit rather than a cosmetic rename.
- Milling conserves nutrition and does not create an automatic dominant strategy.
- Total labor, hauling, storage, and bill overhead remain proportionate to the payoff.
- Direct cooking is reconsidered if it provides equivalent gameplay more simply.

## Gameplay Opportunities

### Strong Opportunities

1. **Visible domestic labor:** The crop becomes a task and place within the holding,
   not an icon that jumps directly into a meal.
2. **Low-infrastructure processing:** An unpowered, compact station works in tribal,
   outage, caravan-base, and early-colony conditions.
3. **Raw-versus-processed choice:** Players may retain raw oats for flexible use or
   spend labor to unlock more specialized food value.
4. **Production pattern:** Bills, hauling, batch size, work type, ingredient filters,
   output counts, and storage establish a reusable XML manufacturing pattern.
5. **Future throughput contrast:** A later mill could exchange capital, site, or
   power for throughput without changing the Version 0.1 recipe contract.

### Opportunities to Reject for Version 0.1

- animated rotating stones or pawn-specific animation;
- fuel, power, breakdown, sharpening, wear, or maintenance;
- flour grades, bran, husks, straw, dust, or waste byproducts;
- health effects from stone grit;
- water, wind, or animal-powered upgrades;
- outdoor weather dependence;
- operator gender, status, or ideology restrictions;
- quality levels, masterwork querns, art beauty, or mood bonuses;
- regional stone performance or quarrying;
- grinding non-food resources;
- a generic framework for every future grain.

## Balance Considerations

### Intended Decision

“Do I keep oats in their flexible raw form, or spend pawn time and hauling capacity
to create a processed ingredient that enables a worthwhile food plan?”

The quern is not justified if the answer is always “mill everything” or if all oat
foods require milling and provide no compensating advantage. Historical sequence is
not itself a meaningful tradeoff.

### Lifecycle Comparison

The future specification must model:

- quern construction material, work, skill, footprint, wealth, and availability;
- raw-oat nutrition, storage, trade, feed, and generic meal behavior;
- milling input/output nutrition conservation and stack counts;
- recipe work per unit and the total labor from sowing through eating;
- hauling and storage caused by an additional item;
- batch size and bill frequency;
- work type and skill competition with cooking, crafting, and general labor;
- throughput for one pawn, one quern, and several querns;
- interruption, ingredient reservation, destruction, and unfinished work behavior;
- early-colony value versus later obsolescence;
- compatibility with other oat, grain, flour, and food mods.

### Preliminary Boundaries

- Milling must not create nutrition from nothing.
- The hand quern should require no electricity or fuel.
- Capital cost should be low, but not zero.
- The station should occupy one tile unless art or interaction testing proves that
  two tiles materially improves readability.
- One conversion recipe is preferred; bulk operation should be considered only to
  reduce repetitive hauling and bill overhead.
- Do not apply both an extreme work-speed penalty and excessive recipe work.
- Raw oats must retain at least one useful path if processing is meant to be a choice.
- Milled oats must enable a clear benefit that repays labor without becoming a
  universal superior ingredient.
- If the downstream food briefs cannot satisfy both conditions, reject the quern.

### Abuse Cases

- converting nutrition upward through rounding or stack ratios;
- using modded grain categories to mill unintended ingredients;
- producing high-value output from low-value generic plant matter;
- generating Crafting or Cooking experience faster than comparable vanilla work;
- placing costless disposable querns anywhere for wealth-free production;
- parallel querns removing the intended labor constraint too cheaply;
- allowing raw oats in every target food and making milling pointless;
- disallowing raw oats everywhere and making milling compulsory busywork.

## Technical Implementation Considerations

### Expected XML Surface

Research indicates the smallest supported shape is:

- one `ThingDef` using the standard `Building_WorkTable` behavior;
- one compact unpowered building with an interaction cell and Bills tab;
- existing vanilla stone blocks and, if justified, wood as construction inputs;
- one milling `RecipeDef` supplied by the later milled-oats feature;
- standard ingredient filters, products, work amount, work type, and speed stat;
- one original building graphic with only the rotations and states actually needed;
- stable `EI_` Def and translation keys;
- no custom component, job driver, recipe worker, UI, or serialization.

This is a feasibility boundary, not an implementation plan. Exact inheritance,
fields, paths, identifiers, and numbers belong in specification and planning.

### Work Type and Skill

Vanilla provides several plausible patterns:

- Crafting with `GeneralLaborSpeed`, as used by stonecutting;
- Cooking with `CookSpeed`, emphasizing food preparation;
- an unskilled general-labor conversion.

The research does not resolve which produces the best colony decision. The
specification must choose one existing work type and test priority conflicts. A new
skill, work type, or custom stat is out of scope.

### Construction Materials

Use vanilla resources. Stone blocks are the most consistent historical abstraction
and align with the approved local-stone identity; a wooden handle can be represented
by a small wood cost. The specification must determine whether accepting all Stony
Stuff creates visual or mod compatibility issues. No raw fieldstone, quernstone,
metal fitting, or material family is justified.

### XML vs C# Recommendation

**Recommendation: XML only. C# and Harmony are not justified.**

RimWorld Core already supplies the required worktable, bill, recipe, hauling,
reservation, skill, effect, output, and persistence behavior. If an accepted design
later demands custom grinding animation, dynamic fineness, unattended processing, or
special ingredient unification, Version 0.1 should simplify or defer that behavior.

### DLC Policy

| Environment | Preliminary behavior |
|---|---|
| RimWorld 1.6 Core only | Full hand-quern behavior through standard bills and work |
| Royalty absent/present | No enhancement or dependency; verify styles/meditation do not misclassify it |
| Ideology absent/present | No enhancement or dependency; verify food/precept interactions through outputs |
| Biotech absent/present | No enhancement or dependency; verify child labor settings only through vanilla work rules |
| Anomaly absent/present | No enhancement or dependency |
| Odyssey absent/present | No enhancement or dependency; verify placement and operation on supported maps/gravships if ordinary worktables are allowed |

No DLC-specific patch is recommended.

### Save and Removal Considerations

- The building and output Def names become save contracts when implementation begins.
- Bills and ingredient filters are serialized through vanilla worktable behavior.
- Adding the building to an existing save should be low risk but requires testing.
- Removing the mod can delete the building, bills, stored outputs, and jobs and can
  break food availability; release notes must state tested removal behavior.
- Changing recipe users, input categories, output ratios, or Def names after release
  requires save and compatibility analysis.
- No custom serialized state is expected.

### Performance

A standard worktable without ticking code should have negligible direct simulation
cost. The practical risk is bill scanning, ingredient search, hauling, and job churn
when many querns or restrictive ingredient filters exist. Test empty bills, missing
inputs, large oat stores, multiple stations, suspended bills, and `do until` counts.

No per-tick component, map scan, or custom cache is acceptable.

### Art Requirements

Art effort is low to medium but not trivial. A one-tile building must read as two
stacked stones and a handle at normal RimWorld zoom without resembling a loose chunk,
table, sculpture, or powered mill.

The art brief must decide:

- whether one orientation is sufficient or pawn interaction requires rotations;
- how Stuff color applies without erasing grinding surfaces and handle readability;
- blueprint, construction, damage, snow, darkness, selection, and minified states;
- interaction-cell clarity and pawn overlap;
- original visual synthesis from multiple licensed references.

No texture has been created or authorized during research.

## Risks

| Risk | Likelihood | Impact | Mitigation or gate |
|---|---|---|---|
| Milling is mandatory busywork | High | High | Require downstream proof of raw-versus-processed choice before inclusion |
| Extra item adds hauling/storage friction without value | High | High | Model complete labor and inventory lifecycle |
| Quern is mistaken for Ireland's only milling technology | Medium | High | Document contemporary watermills and household-scale role |
| Historical object is overdecorated or monumentalized | Medium | Medium | Use restrained composite references and ordinary domestic framing |
| Gendered labor becomes a pawn restriction | Low | High | Explicitly prohibit gender restrictions |
| Generic ingredient filters consume unintended grains | High | Medium | Begin with narrow filters; add compatibility deliberately |
| Duplicate flour/oat items conflict with major food mods | High | Medium | Inspect current Defs and publish a bounded compatibility matrix |
| Work type competes poorly with cooking/crafting priorities | Medium | Medium | Test job priority, skill, XP, and colony labor effects |
| Construction is too cheap to constrain parallel throughput | Medium | Medium | Test total station cost and labor, not only recipe work |
| One-tile art is unreadable | Medium | Medium | Validate silhouette and interaction at normal zoom |
| Removal strands food bills or stored output | Medium | High | Test removal and document save support |
| Research creates a speculative mill framework | Low | High | Implement only the current building and recipe contract |

## Implementation Notes

### Downstream Research Resolutions

- Raw oats retain ordinary Core food and feed paths.
- Milled oats stage labor and enable a fresh porridge versus portable flatbread choice.
- Milling itself grants no nutrition or shelf-life bonus; downstream foods create the
  differentiated roles.
- Nutrition conservation and integer conversion are mandatory specification tests.
- Direct cooking remains the required simpler comparison and fallback.
- Batch size remains an implementation note for hauling and bill-frequency testing.

### Notes for Specification and Testing

1. Should operation use Cooking, Crafting, or general labor?
2. What work amount creates visible labor without dominating food production?
3. Should all Stony Stuff be accepted for construction?
4. Does the building require a research prerequisite, or should material access be
   the only gate?
5. Should it be 1x1, and which rotations are necessary?
6. Which vanilla and modded recipe filters prevent bypasses and accidental inputs?
7. How does `do until you have X` count milled oats across storage and caravans?
8. Which current grain/flour mods form the supported compatibility sample?

### Human Review Resolutions

- The evidence is sufficient for a domestic rotary hand quern.
- `hand quern` remains the clear English working name; `bró` remains a research term
  pending qualified language review.
- XML-only feasibility through a compact vanilla worktable and bill pattern is
  accepted for later specification review.
- The low-capital, unpowered, labor-intensive niche is approved for downstream
  validation, not yet implementation.
- Downstream research supports a meaningful processing choice at design level;
  inclusion remains conditional on specification and playtesting proving that choice.

## ADR Assessment

No new ADR is required at this research stage. The canonical scope already defines
the hand quern as conditional and XML-only. A future decision to add C#, Harmony,
custom milling behavior, or a broader processing system would require a new ADR and
scope approval. The Version 0.1 Readiness Review recommends conditional progression
to specification; final inclusion still depends on implementation and playtest evidence.

## Approved Research Recommendation

The historical and technical foundation is approved, while PR-01 remains
**conditional**.

The milled-oats and oat-food briefs now establish at research depth that:

- raw oats retain useful behavior;
- milled oats unlock a clear, bounded food-production advantage;
- the labor and hauling cost creates a decision rather than a compulsory click tax;
- the complete chain is nutrition-safe and XML-only.

The future specification and playtests must validate those findings. If they fail,
remove the quern from Version 0.1 and allow direct oat-food processing. Historical
authenticity does not override gameplay value.

## Research Review

### Summary

Hand-operated rotary querns are strongly supported as ordinary domestic
grain-processing equipment in early medieval Ireland. They coexisted with
water-powered mills and should represent accessible household throughput rather than
technological backwardness. Material, morphology, and stone sourcing varied, while
the strongest universal design signal is a compact two-stone manual grinder.

### Recommended Gameplay Implementation

One low-capital, unpowered, compact worktable that converts oats to milled oats using
standard bills and meaningful pawn labor. Its value must come from a genuine
raw-versus-processed choice established by downstream food research.

### Recommended Version 0.1 Implementation

Conditionally retain one XML-only rotary hand quern. Use vanilla stone materials,
possibly a small wood cost, one milling recipe, standard worktable behavior, and no
custom systems. Reject it if the complete food chain cannot prove value beyond
thematic labor.

### Human Review Decision

#### Historical Review Gate

**Decision:** Approved
**Reviewer/date:** Patrick Mee, 2026-07-05
**Corrections:** None. The domestic rotary hand quern is accepted as the historically
accurate Version 0.1 direction.
**Approved uses:** Historical foundation for PR-01 research and future specification.

#### Gameplay Review Gate

**Decision:** Approved with conditions
**Reviewer/date:** Patrick Mee, 2026-07-05
**Corrections:** Add an explicit gameplay validation independent of historical support.
**Approved gameplay direction:** Downstream research satisfies the conditions at
research depth. Proceed conditionally into specification, where direct processing,
labor, hauling, and player behavior must remain explicit tests.

### Research Definition of Ready Checklist

This checklist records readiness to leave research, not readiness to implement.

#### Product and Identity

- [x] Catalog ID, conditional scope, period, and domestic form are explicit.
- [x] Intended player decision and failure condition are stated.
- [x] Constitution, Design Bible, and canonical Version 0.1 scope are applied.
- [x] Explicit exclusions prevent system and content expansion.
- [x] Human reviewer approves the conditional gameplay direction.

#### Evidence and Design

- [x] Historical background, cultural significance, geography, operation, and
  materials are sourced.
- [x] Primary/field, synthesis, experimental, and later evidence are distinguished.
- [x] Uncertainty, variation, anachronism, and cultural risks are recorded.
- [x] Watermill coexistence prevents a false technological claim.
- [x] Vanilla and existing-mod comparisons identify measurable design questions.
- [x] Human reviewer confirms that the evidence is sufficient.

#### Gameplay Validation

- [x] Meaningful player decision and gameplay problem are explicit.
- [x] Stories, omission cost, and click/labor burden are evaluated.
- [x] Tradeoff and compulsory-labor failure state are distinguished.
- [x] The simpler direct-cooking alternative is evaluated.
- [x] Complexity costs and measurable retention conditions are recorded.
- [x] Gameplay review is approved with conditions by the human reviewer.

#### Engineering

- [x] XML-only feasibility is supported by verified RimWorld 1.6 Core behavior.
- [x] No C#, Harmony, custom UI, ticker, or serialized state is justified.
- [x] DLC, save, performance, work-priority, art, and compatibility risks are recorded.
- [x] Construction and recipe surfaces are bounded without specifying implementation.
- [x] ADR assessment is recorded.

#### Delivery

- [x] Art, localization, testing, and source-rights requirements are bounded.
- [x] Downstream milled-oats and food dependencies are explicit.
- [x] Specification and implementation remain prohibited.
- [x] Human questions are resolved and approval recorded.

**Research decision:** Passed with conditions
**Project Definition of Ready:** Not evaluated. Readiness Review approval,
specification, planning, and implementation authorization remain outstanding.

## Sources

Accessed 2026-07-05 unless otherwise stated.

1. Aidan O'Sullivan, Finbar McCormick, Thomas Kerr, and Lorcan Harney,
   *Early Medieval Ireland: Archaeological Excavations 1930-2009*, EMAP Report 4.5
   (2010), especially printed pp. 120-124, 140-141, and 181.
   [UCD report PDF](https://researchrepository.ucd.ie/rest/bitstreams/42708/retrieve).
   Source type: national archaeological synthesis incorporating excavation records;
   not a substitute for individual context reports.
2. Thomas Kerr, Maureen Doyle, Matthew Seaver, Finbar McCormick, and Aidan
   O'Sullivan, *Industrial Activity on Rural Secular Sites in Ireland, AD 400-1100*,
   EMAP (2012), especially printed pp. 67-72 and the stone-working gazetteer.
   [UCD report PDF](https://researchrepository.ucd.ie/server/api/core/bitstreams/8bf8b480-b9cc-482d-ad3b-c8dc5bbbc641/content).
   Source type: archaeological production synthesis and excavation catalogue.
3. Anette Overland and Michael O'Connell, “New insights into late Holocene farming
   and woodland dynamics in western Ireland with particular reference to the early
   medieval horizontal watermill at Kilbegly, Co. Roscommon,” *Review of
   Palaeobotany and Palynology* 163 (2011): 205-226.
   [DOI](https://doi.org/10.1016/j.revpalbo.2010.10.008).
   Source type: peer-reviewed archaeological and palaeoecological study.
4. Muiris O'Sullivan and Liam Downey, “Quern Stones,” *Archaeology Ireland* 20.2
   (2006): 22-25.
   [JSTOR issue record](https://www.jstor.org/stable/i20559130).
   Source type: specialist public-archaeology overview; full text was not relied on
   for unsupported detail.
5. Tony Bartlett, “Newcastle Middle, County Wicklow,” excavation licence 21E0034,
   *Excavations.ie* 2021 report 31334.
   [Excavation report](https://excavations.ie/report/2021/Wicklow/0031334/).
   Source type: primary field report and measured object record; quern is
   unstratified and its original findspot/date are unknown.
6. Galway Community Archaeology, “Decorated Quern,” recorded 13 March 2017.
   [Object note](https://field-monuments.galwaycommunityheritage.org/content/archaeology/industrial-archaeology/decorated-quern).
   Source type: primary community-archaeology find record pending National Museum
   deposition; not a typological synthesis.
7. Martin Hora, Vojtech Marik, Matej Dundr, Michal Struska, and Vladimir Sladek,
   “Energy expenditure during grain grinding using reciprocal quern and rotary
   quern,” *Journal of Archaeological Science* 180 (2025), 106292.
   [article PDF](https://natur.cuni.cz/data/users/user_549/Hora-et-al_2025_Energy-expenditure-during-grain-grinding-using-reciprocal-quern-and-rotary-quern.pdf) |
   [DOI](https://doi.org/10.1016/j.jas.2025.106292).
   Source type: peer-reviewed modern experiment using specific replica equipment;
   not a direct early medieval Irish production rate.
8. Placenames Branch, Department of Culture, Communications and Sport, “Baile
   Bró/Ballybro,” *Placenames Database of Ireland*.
   [Logainm record](https://www.logainm.ie/en/54341).
   Source type: official language and placename analysis; the particular placename
   derivation is explicitly uncertain, while `bró` is identified as quern/handmill.
9. Ludeon Studios, locally installed RimWorld `1.6.4871 rev595` Core data,
   `Data/Core/Defs/ThingDefs_Buildings/Buildings_Production.xml`,
   `Data/Core/Defs/RecipeDefs/Recipes_Production.xml`, and
   `Data/Core/Defs/RecipeDefs/Recipes_Meals.xml`, inspected 2026-07-05.
   Source type: proprietary current technical reference; behavior and values are
   paraphrased for design comparison.
10. Medieval Overhaul team, *Medieval Overhaul*, Steam Workshop item 3219596926.
    [Workshop page](https://steamcommunity.com/sharedfiles/filedetails/?id=3219596926).
    Source type: adjacent current mod comparison; exact Defs and assets not reused.
11. Sarg Bjornson and Vanilla Expanded team, *Vanilla Cooking Expanded*, Steam
    Workshop item 2134308519.
    [Workshop page](https://steamcommunity.com/sharedfiles/filedetails/?id=2134308519).
    Source type: adjacent current food-mod comparison; exact Defs and framework were
    not inspected.

## Source and Asset Notes

- Period-specific claims rely primarily on archaeological sources [1]-[3].
- Sources [5] and [6] are object references with explicit contextual limitations.
- Source [7] informs labor hypotheses only; it does not set recipe time.
- Visual references remain link-only until license and provenance review.
- No source XML, code, image, texture, audio, or mod asset was copied.
