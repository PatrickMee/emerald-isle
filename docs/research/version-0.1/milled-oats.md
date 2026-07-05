# Research Brief: Milled Oats

**Research ID:** RSC-005
**Feature:** PR-01 / FO-01 Milled Oats
**Release:** Version 0.1 - The First Holding
**Researcher:** Codex
**Reviewer:** Patrick Mee
**Status:** Approved
**Historical review:** Approved
**Gameplay review:** Approved with conditions
**Date:** 2026-07-05
**Approved:** 2026-07-05
**Research Definition of Ready:** Passed with conditions
**Approved scope:** `docs/product/version-0.1-approved-scope.md`
**Implementation authorized:** No

## Question and Design Need

Is a distinct `milled oats` ingredient historically defensible and valuable enough
to justify an intermediate processing item between raw oats and oat foods in
Version 0.1?

This brief tests two independent propositions:

1. people in early medieval Ireland processed oats by milling as part of domestic
   cereal preparation; and
2. representing that processing as a separate RimWorld item creates decisions worth
   its bills, hauling, storage, art, localization, compatibility, and maintenance
   costs.

It does not define final recipes, yields, work amounts, nutrition, shelf life, art,
or XML. Those belong to later specification and planning gates.

## Scope

**Primary period:** Early medieval Ireland, approximately AD 400-1100.
**Supporting evidence:** Modern cereal science only where it explains oat anatomy;
later Irish practice only where clearly labeled as continuity or comparison.
**Geography:** The island of Ireland, without inventing regional processing rules.
**Subject:** Cleaned and ground oat material suitable for further food preparation.
**Working English term:** `milled oats`, a deliberately broad gameplay label.
**Language references:** Modern Irish `min choirce` means oatmeal; it is evidence for
terminology, not proof of an unchanged medieval product name.
**Excluded:** A complete flour system; industrial roller milling; mechanized kilning;
oat bran, groats, flakes, hull by-products, quality grades, milling skill systems,
weather-dependent drying, watermills, and final oat-food design.

## Executive Finding

The historical proposition is supported at **medium-to-high confidence**. Oats were
a major early medieval Irish crop, rotary hand querns were ordinary domestic grain
processing equipment, and cereals were made into bread, gruel, and porridge. The
evidence does not establish one standardized product matching a modern package of
oatmeal, nor does it document a complete oat-specific preparation sequence for
Version 0.1 to reproduce.

`Milled oats` is therefore defensible as a transparent gameplay abstraction for
ground oat material, not as a claim that all early medieval Irish households made an
identical product by an identical method.

The gameplay proposition is **Recommended with Conditions**. A separate intermediate
can create stockpiling, labor-allocation, and production-scheduling choices while
connecting the hand quern to several foods. It becomes unjustified compulsory labor
if all oats must pass through it for only one routine recipe, if conversion creates
free nutrition or preservation, or if a direct oat-food recipe would produce the
same decisions more simply.

## Historical Background

### Oats and Cereal Processing

McCormick, Kerr, McClatchie, and O'Sullivan's archaeological synthesis found oat in
80% of 165 analysed early medieval Irish site phases or areas, with hulled barley and
oat the dominant crops in the wider research program [1, pp. 48-54; 2]. The evidence
supports oats as ordinary working grain, while preservation and identification limits
prevent exact reconstruction of every crop or processing stage.

The same synthesis documents rotary hand querns as domestic equipment and
water-powered mills as part of the early medieval milling landscape [1, pp. 39-41].
It reports that drying grain helped hand milling and that damp Irish conditions made
drying important before storage and processing. These observations support a
grain-to-ground-product transformation without proving an oat-exclusive workflow.

The report identifies bread, gruel, porridge, brewing, and fodder among early
medieval cereal uses [1, pp. 45-46]. Those are cereal-wide findings. Version 0.1 may
use them to frame downstream questions, but it must not attribute every use
specifically to oats until the Oat Foods brief evaluates the evidence.

### Product Identity

Grinding changes cereal grain into particles that can be cooked or baked. For this
project, `milled oats` means the usable ground ingredient after whatever cleaning,
drying, hull management, and grinding were necessary. It does not assert a specific
particle size or modern commercial grade.

Modern oat science distinguishes the inedible fibrous hull from the groat and
describes industrial cleaning, dehulling, heat stabilization, cutting, flaking, and
flour production [3]. This is useful anatomical context only. Projecting that modern
sequence or equipment into AD 400-1100 would be anachronistic.

The archaeological synthesis notes the broader processing difficulty of hulled
cereals and the storage protection a hull can provide [1, p. 63]. It does not supply
a secure, oat-specific domestic dehulling recipe. Version 0.1 should abstract the
uncertain preliminary steps instead of inventing a second workstation or hull item.

## Cultural Significance

Oats fit the project's focus on ordinary holdings, domestic work, and practical food
security. Milled oats can make that labor visible without treating hand processing
as primitive, uniquely Irish, or culturally static. Hand querns coexisted with
larger mills; a domestic quern represents accessible household-scale production.

The cultural meaning should remain modest. The evidence supports everyday cereal
processing, not a national emblem, ceremonial food, or universal diet. Later images
of rural poverty and nineteenth-century subsistence must not be projected backwards
onto early medieval households.

## Geographic Context

Oat remains occur across all four Irish provinces in the archaeological dataset,
although excavation intensity and sample size vary [1, pp. 48, 51-54]. Quern and
watermill evidence likewise demonstrates a wider milling practice rather than a
single local invention [1, pp. 39-41].

No secure evidence reviewed here supports province-specific milled-oat mechanics,
regional recipes, or biome restrictions. Version 0.1 should represent one plausible
holding and leave regional variation for future research.

## Historical Time Period

The target is AD 400-1100. This period contains strong evidence for oats as a crop
and rotary querns as household grain-processing equipment. Later folklore can
illustrate the persistence of hand processing but cannot establish medieval details.

A 1930s Schools' Collection account titled “Oats-Making Long Ago” records later
memory of oat preparation [6]. It is valuable as folklore and terminology, not as a
primary early medieval source. It must not be used to fill archaeological gaps.

## Production Methods

The evidence supports the following high-level transformation:

1. harvest and separate cereal grain from the crop;
2. clean and dry the grain as needed;
3. manage the hull sufficiently to expose usable grain;
4. grind grain between quern stones;
5. use the ground material in a later food preparation.

Confidence is high for harvesting, drying, and milling as cereal-processing stages;
medium for applying the broad sequence to oats; and low for any exact domestic
dehulling technique, particle grade, batch size, or oat-specific sequence. The game
should compress steps 2-4 into one bill at the hand quern.

This compression is an explicit transformation for playability. Separate drying,
winnowing, dehulling, sifting, and grinding bills would simulate labor without
creating enough distinct decisions for Version 0.1.

## Materials

- **Input:** harvested oat grain, represented by the approved raw-oats item.
- **Tool:** the conditionally approved rotary hand quern, primarily stone.
- **Output:** ground oat material, represented by `milled oats`.
- **Fuel or power:** none for the Version 0.1 hand-operated process.
- **Excluded outputs:** hulls, bran, dust, waste, and graded flour fractions.

The historical process required skill and physical labor, but this brief does not
support consuming extra wood, cloth, water, fuel, or additives in the milling bill.

## Historical Claims and Confidence

| Claim | Evidence | Confidence | Design relevance |
|---|---|---:|---|
| Oats were a major cereal in early medieval Ireland. | Archaeobotanical synthesis and peer-reviewed review [1, pp. 48-54; 2] | High | Supports the input crop. |
| Domestic rotary querns processed grain during the target period. | Archaeological synthesis [1, pp. 39-41] | High | Supports a household milling step. |
| Drying aided storage and hand milling in Ireland's damp conditions. | Archaeological synthesis [1, pp. 32, 41] | High for cereals generally | Supports process context, not a drying mechanic. |
| Cereals were made into bread, gruel, and porridge. | Archaeological and documentary synthesis [1, pp. 45-46] | High for cereals generally | Supports downstream food research. |
| Hulled cereals require processing before milling or eating. | Archaeological synthesis and modern anatomy [1, p. 63; 3] | Medium for the precise historical oat sequence | Justifies abstraction, not extra content. |
| A standardized product called `milled oats` existed across Ireland. | No direct evidence identified. | Low | Prohibited claim; term is a gameplay abstraction. |
| Milling improved storage life. | Modern processing literature does not support a simple benefit [3]. | Low/contrary | No automatic preservation bonus. |

## Primary and Secondary Reference Assessment

### Primary or Near-Primary Evidence

- Archaeobotanical crop remains and excavated milling contexts synthesized in EMAP
  reports are the closest material evidence used here [1]. The synthesis is not a
  substitute for every excavation report, and most plant remains do not preserve a
  named finished product.
- Early medieval legal and documentary references quoted by the archaeological
  synthesis support cereal uses, but this brief relies on the scholars' translation
  and interpretation rather than claiming a new reading of the original texts [1].
- The Dúchas account is primary evidence for twentieth-century collected memory, not
  for the early medieval period [6].

### Secondary and Technical Evidence

- The peer-reviewed archaeobotanical review confirms crop prevalence at program
  level [2].
- Modern oat-processing science clarifies kernel anatomy and the consequences of
  breaking the grain structure [3]. It cannot establish medieval equipment or
  recipes.
- Teanglann provides official modern dictionary evidence for `min choirce` and
  related terminology [4, 5]. It does not approve a player-facing historical label.

## Uncertainty and Contestation

- Charred grain survives more readily than soft prepared foods, so archaeology
  identifies crops more securely than finished dishes or particle grades.
- Oat species identification is often incomplete because diagnostic structures are
  absent [1, pp. 50, 63].
- Exact early medieval Irish oat cleaning and dehulling techniques remain unresolved.
- A quern could produce different textures depending on grain preparation and stone
  adjustment; one uniform output is a gameplay simplification.
- `Oatmeal` can mean ground oats or a prepared porridge depending on dialect. Using
  it for the intermediate could confuse the ingredient with a future dish.
- Modern shelf-life and heat-stabilization findings must not be projected backwards.
- The proposed item may be technically feasible but mechanically redundant. That is
  a gameplay question, not a historical one.

Remaining uncertainty is recorded as implementation constraints and downstream
questions. None requires inventing additional Version 0.1 content.

## Cultural Sensitivities and Misconceptions

Avoid these claims and presentations:

- oats or oatmeal as timeless shorthand for all Irish food;
- hand milling as evidence that Irish communities lacked water-powered technology;
- a single unchanging recipe across six centuries and the whole island;
- nineteenth-century famine, poverty, or cottage imagery used as medieval evidence;
- modern health-food marketing projected into the past;
- labor added solely because historical households performed it;
- invented Irish labels presented as attested early medieval language.

The feature should communicate ordinary food preparation and player choice, not a
romantic reconstruction.

## Language and Naming

**Recommended English item label:** `milled oats`.

This label is understandable, distinguishes the ingredient from a prepared bowl of
porridge, and avoids claiming the finer texture implied by `oat flour`. It is a
modern descriptive interface term, not an attested product name.

Official modern Irish dictionaries give `min choirce` for oatmeal and use
`brachán (mine) coirce` for oatmeal porridge [4, 5]. Any Irish localization should
receive language review in context. The English name remains authoritative during
research.

## Images and Visual References

No image is copied into the repository during research.

Useful visual references for later licensed original art are:

- EMAP report figures and photographs of early medieval grain-processing evidence
  and quern stones [1];
- the approved Hand Quern brief's archaeological object references;
- modern photographs of coarse ground oats only as texture reference, not as proof
  of medieval appearance.

The likely item icon needs to read as a small pile or shallow container of coarse
ground cereal at RimWorld scale. Final composition, color, container, and texture
remain art decisions. Source images are link-only until provenance and reuse rights
are reviewed.

## RimWorld Vanilla Comparison

Verified RimWorld `1.6.4871 rev595` Core data establishes these baselines [7]:

- raw rice and corn are directly edible `PlantFoodRawBase` items and are accepted by
  nutrition-based meal recipes;
- simple meals consume raw-food nutrition through ordinary XML recipe filters;
- wort is a distinct, non-drinkable XML-defined intermediate created by a bill and
  consumed by a later production stage;
- wort has its own stack, mass, value, deterioration, and rot behavior, showing that
  intermediate resources carry real storage and hauling costs;
- Core contains no generic flour, oats, quern, or universal milling framework.

The wort pattern proves that an XML-only intermediate is technically normal. It
does not prove that milled oats should copy wort's values, rot time, categories, or
specialized fermentation behavior.

The strongest vanilla comparison is therefore not “flour already exists,” but the
production-chain principle: an intermediate is justified when it changes scheduling
and enables a meaningful later transformation.

## Existing Mod Comparison

### Vanilla Cooking Expanded

Vanilla Cooking Expanded uses flour and large-batch baking within a broad cooking
framework [8]. Its workshop description explicitly favors accessible gameplay over
strict simulation. This demonstrates player familiarity with flour-like
intermediates, but its framework scale, dependencies, recipes, assets, and balance
are outside Version 0.1.

### Medieval Overhaul

Medieval Overhaul includes a much broader medieval production environment with
grain-processing concepts [9]. It is an adjacent design reference, not a template.
Emerald Isle should not import its definitions, art, terminology, or system breadth.

### Compatibility Lesson

Different mods often define conceptually similar flour resources that are not
interchangeable. Version 0.1 should use a narrow, namespaced item and recipes rather
than claim to be a universal flour framework. Cross-mod substitutions require later
explicit compatibility evidence and policy review.

## Gameplay Validation

Gameplay is evaluated independently from historical authenticity.

### What Meaningful Player Decision Does Milled Oats Create?

The intended decision is **when and how much of the raw oat reserve to process**.
Raw oats remain flexible crop inventory; milled oats commit pawn labor and storage to
a downstream food chain. Bills and stockpile targets can let a player prepare winter
food inputs, respond to cook availability, or defer processing during emergencies.

This is meaningful only if raw oats retain at least one useful path and milled oats
unlock at least two worthwhile food uses, or one use with a clear production-
scheduling benefit.

### What Gameplay Problem Does It Solve?

It decouples grain milling from final cooking. That separation lets a low-skill or
differently scheduled worker prepare ingredients before the cook needs them and gives
the hand quern a coherent production role. It also establishes a reusable XML
production-chain pattern for future content.

If the same pawn performs both jobs consecutively and the item has only one use, no
problem has been solved; the process has merely been lengthened.

### What New Stories Does It Enable?

- a holding mills part of its harvest before winter and protects the processed stock;
- labor shortages force a choice between immediate raw-food flexibility and future
  prepared-food benefits;
- a damaged or inaccessible quern interrupts one food route without erasing all food;
- a productive harvest creates a milling backlog that the player can schedule rather
  than an automatic stat bonus.

These are modest colony-management stories consistent with vanilla RimWorld. They do
not require bespoke events or narrative code.

### What Would Players Lose If Milled Oats Did Not Exist?

They would lose the visible connection between crop, quern, and oat foods; the
ability to stockpile a prepared ingredient; and the labor-timing decision. They would
not lose the ability to have oats or oat foods, because direct cooking is a viable
simpler design.

The omission cost is therefore **moderate**, not fundamental. Historical presence
alone cannot make the item mandatory.

### Does It Add Strategy or Simply Additional Clicks?

Standard RimWorld bills can automate target quantities, so the process need not add
repeated manual clicks. It adds strategy only when players can choose conversion
timing and downstream use. A mandatory one-input/one-output step on every food path
would add hauling and work without strategy.

### Does It Create a Meaningful Tradeoff or Compulsory Labor?

The intended tradeoff is labor and inventory commitment in exchange for access to a
bounded food benefit and more controllable production scheduling. The work becomes
compulsory labor if milled products are the only practical use for oats or if their
benefit simply repays an arbitrary penalty imposed on raw oats.

Raw oats must remain useful. Processed foods may improve convenience, mood, storage,
or nutrition efficiency only within the project's balance rules and only after the
Oat Foods research supports the choice. Milled oats themselves should not receive a
free nutrition or shelf-life upgrade.

### Could the Same Gameplay Be Achieved More Simply?

Yes. A stove recipe could consume raw oats directly and include extra work to
abstract milling. That removes one item, one bill, one icon, one stockpile category,
and extra hauling.

The separate item earns its place only if the downstream scope uses it more than
once or creates a clear scheduling/stockpiling role. The Oat Foods brief must compare
the direct-recipe alternative explicitly.

### Does the Added Complexity Justify Itself?

Provisionally, yes. The technical and art costs are small, the item makes the hand
quern legible, and the production chain is visible to players. The justification is
fragile: one unremarkable downstream recipe would not pay for the added inventory
and labor layer.

**Gameplay recommendation: Recommended with Conditions**

**Conditions:**

1. Raw oats retain a useful non-milling path.
2. Milled oats support at least two materially distinct downstream uses, or one use
   with a demonstrated scheduling or stockpiling benefit that a direct recipe lacks.
3. Raw-to-milled conversion conserves nutrition within rounding and does not create
   a dominant value loop.
4. Milled oats receive no automatic shelf-life, nutrition, beauty, quality, or market
   premium merely for adding labor.
5. Batch size, work, hauling, stack behavior, and storage burden remain proportionate.
6. The Oat Foods research compares this design with direct cooking from raw oats.
7. If these conditions fail, Version 0.1 should omit both the separate ingredient and
   the hand-quern processing step rather than preserve historical labor for its own
   sake.

## Gameplay Opportunities

### Supported Opportunities

- target-quantity bills that let players maintain a chosen processed reserve;
- a visible crop-to-quern-to-food chain;
- different work timing for milling and cooking;
- multiple oat-food recipes sharing one ingredient, if the next brief supports them;
- a reusable XML recipe/intermediate pattern for future production chains.

### Opportunities to Reject for Version 0.1

- milling quality grades or skilled-quality outputs;
- health, ideology, ritual, mood, or cultural-essentialism mechanics;
- hulls, bran, animal-feed by-products, or waste recovery;
- powered mills, watermills, mill buildings, or a generic flour system;
- weather, moisture, drying, sifting, or infestation simulation;
- compatibility aliases that make unrelated mod flours universally interchangeable.

## Balance Considerations

### Intended Decision

The player chooses whether to spend labor now for later food-production options. The
intermediate should not increase total nutrition by itself. Any benefit belongs to a
downstream food and must be paid for by work, ingredients, cooking requirements, or
another visible constraint.

### Preliminary Boundaries

- total nutrition after conversion must be no greater than input nutrition except
  for explicitly balanced downstream recipe effects;
- no processing loss is required merely for realism, but integer rounding must not
  generate free nutrition;
- work and batch size should make the bill worth scheduling without producing a
  large hauling tax;
- raw oats cannot be deliberately crippled to manufacture demand for milling;
- shelf life must be based on gameplay and evidence, not an assumption that ground
  grain preserves better;
- market value should not create profitable milling independent of food use;
- animals, caravans, nutrient paste, and ordinary meal filters must be tested for
  accidental consumption or value loops.

### Abuse and Failure Cases

- conversion multiplies nutrition through count rounding;
- pawns eat the intermediate directly and bypass the intended foods;
- ordinary meal recipes consume milled oats unintentionally;
- traders turn labor into risk-free profit;
- stockpiles become cluttered with tiny batches;
- all oat use requires two jobs and extra hauling for no differentiated outcome;
- another mod's flour filters absorb the item unexpectedly, or vice versa.

## Technical Implementation Considerations

### Expected XML Surface

Research supports, but does not yet authorize:

- one namespaced `ThingDef` for milled oats;
- one ordinary `RecipeDef` on the conditional hand quern;
- standard ingredient and fixed filters restricted to the approved oat item;
- one original item graphic and localization keys;
- ordinary bill, hauling, storage, stack, deterioration, trade, and save behavior.

No custom component, map ticking, UI, database, or serialized custom state is
indicated.

### Item Classification and Ingestibility

The safest preliminary direction is a processing ingredient that pawns do not choose
as ordinary food. RimWorld Core's wort demonstrates that a non-ingestible resource
can function as an XML intermediate [7]. However, nutrition-based cooking filters may
require a different classification or explicit recipe counts.

The specification must verify the exact `ThingDef`, category, nutrition, ingredient,
food-type, storage, and recipe-filter contracts against the supported 1.6 build. This
brief does not choose between a non-ingestible resource and a tightly controlled food
ingredient.

### XML vs C# Recommendation

**Recommendation: XML only.**

Core already supports the required item, recipe, bill, stockpile, rot, and later
ingredient relationships declaratively [7]. There is no research basis for custom
C#, Harmony, custom jobs, or a generic milling framework. Discovery of a real Core
contract limitation would require evidence, scope review, and the applicable ADR;
it would not silently authorize code.

### DLC Policy

- **Required:** RimWorld 1.6 Core.
- **Optional enhancements:** None identified.
- **Absent DLC behavior:** The item and recipe must work with no DLC installed.
- **Official DLC review:** Royalty, Ideology, Biotech, Anomaly, and Odyssey require
  compatibility checks during specification and testing, but no dependency.

### Save and Removal Considerations

The item and recipe create stable Def-name contracts once released. Removing or
renaming the item later can affect maps, stockpiles, bills, caravans, and saves.
Namespacing and stable IDs are required. Uninstall behavior and in-progress bills
must be tested before release.

### Performance

One passive item and one standard bill have negligible inherent runtime cost. The
meaningful risks are excessive bill scanning from broad filters and unnecessary
hauling from poor batch sizes. Narrow filters and vanilla behavior should keep the
feature within the performance budget.

### Art and Localization

Art effort is low but nonzero: one original RimWorld-readable item icon. It must be
visually distinct from raw oats, flour from other mods, and finished porridge.
Localization must distinguish the intermediate from the food and avoid unsupported
historical Irish terminology.

## Risks

| Risk | Likelihood | Impact | Research response |
|---|---:|---:|---|
| Intermediate adds compulsory work without a decision | Medium | High | Retention is conditional on downstream comparison. |
| Exact historical product is overstated | Medium | High | Use broad term and record the abstraction. |
| Nutrition or value duplication | Medium | High | Require conversion accounting and abuse tests. |
| Pawns or recipes consume the item unintentionally | Medium | Medium | Verify classification and filters against Core 1.6. |
| Extra hauling overwhelms small benefit | Medium | Medium | Test batch, stack, stockpile, and work behavior. |
| Shelf life implies unsupported processing benefit | Medium | Medium | Do not grant automatic preservation. |
| Flour-like items conflict across mods | Medium | Medium | Namespace narrowly; no universal compatibility claims. |
| Art reads as modern packaged oatmeal or flour | Low | Medium | Use original coarse-ground visual with art review. |
| Scope expands into a milling system | Low | High | Enforce explicit exclusions and frozen scope. |

## Implementation Notes

### Oat Foods Research Resolutions

- Oat porridge and oat flatbread are historically supported broad food forms.
- They provide a fresh everyday path and a portable processed path.
- Prior milling can stage labor and support the two-way food choice, subject to
  specification and playtest evidence.
- Raw oats retain ordinary Core food and feed uses.
- Direct raw-oat cooking remains the required simpler comparison and fallback.

### Notes for Specification and Testing

1. Should the item be non-ingestible, emergency-only, or an explicitly filtered food
   ingredient under verified Core behavior?
2. Which work type and skill best fit milling without creating job-priority friction?
3. What batch size minimizes hauling while preserving a scheduling decision?
4. How will nutrition conservation be calculated across integer item counts?
5. Which vanilla recipes, animals, caravans, paste systems, traders, and stockpiles
   can select the item?
6. What rot, deterioration, stack, mass, and market values avoid an artificial bonus?

### Human Review Resolutions

- `milled oats` is accepted as the English abstraction despite the lack of a single
  standardized archaeological product.
- The gameplay recommendation is approved with all seven conditions.
- The omission rule is accepted: if Oat Foods cannot prove the intermediate's value,
  remove the separate milling step rather than add compulsory labor.

## ADR Assessment

No new ADR is required at this research stage. The canonical Version 0.1 scope
already includes milled oats through a conditional hand quern and targets XML-only
implementation. A future move to C#, Harmony, a generic flour framework, new resource
families, or scope beyond the approved chain would require governed review and, where
appropriate, an ADR.

Oat Foods research is approved. Final retention remains conditional on specification
and playtesting demonstrating meaningful choices without excessive labor or hauling.

## Approved Research Recommendation

Advance `milled oats` into specification as one XML-only intermediate, subject to the
gameplay conditions in this brief.

Treat it as ground oat material, not a reconstructed standardized commodity. Do not
give processing an inherent preservation, nutrition, quality, or value bonus. Require
the Oat Foods research to prove that the item supports distinct downstream choices or
a useful production-scheduling role. If it cannot, use direct raw-oat cooking and
remove the otherwise redundant milling layer.

## Research Review

### Summary

Early medieval Irish evidence strongly connects oats, grain drying, domestic rotary
querns, and cereal foods, but does not preserve one standardized `milled oats`
product. The item is a reasonable and legible abstraction. Its historical foundation
is stronger than its gameplay necessity, so inclusion remains conditional.

### Recommended Gameplay Implementation

One automatable intermediate resource that lets the player choose when and how much
of the oat reserve to process. It should connect the hand quern to more than one
meaningful downstream use, or demonstrate a clear scheduling benefit over direct
cooking. It must not create nutrition, preservation, or profit by itself.

### Recommended Version 0.1 Implementation

Conditionally retain one `milled oats` item and one XML-only hand-quern recipe. Use
standard bills, narrow filters, stable namespaced IDs, one original icon, and no
custom systems. Final retention depends on specification and playtest evidence.

### Human Review Decision

- Historical abstraction and English working name approved.
- Gameplay direction approved with all stated conditions.
- Direct cooking remains the required fallback if Oat Foods does not justify the
  intermediate.

### Historical Review Gate

**Decision:** Approved
**Reviewer/date:** Patrick Mee, 2026-07-05
**Corrections or conditions:** Preserve uncertainty around product standardization.
**Approved claims and uses:** Oats were milled in the early medieval Irish
cereal economy; `milled oats` may represent ground oat material as a broad gameplay
abstraction, not a standardized product reconstruction.

### Gameplay Review Gate

**Decision:** Approved with conditions
**Reviewer/date:** Patrick Mee, 2026-07-05
**Corrections or conditions:** All seven Gameplay Validation conditions remain binding.
**Approved gameplay direction:** `Recommended with Conditions` as stated in
Gameplay Validation; Oat Foods satisfies the downstream research dependency, while
final retention remains dependent on specification and playtesting.

### Research Definition of Ready Checklist

This checklist records readiness to leave research, not readiness to implement.

#### Product and Identity

- [x] Research ID, feature, frozen scope, period, and abstraction are explicit.
- [x] Constitution, Design Bible, and approved Version 0.1 scope are applied.
- [x] Explicit exclusions prevent a generic milling or flour system.
- [x] Intended player experience and failure condition are stated.
- [x] Human reviewer accepts the name and scope transformation.

#### Evidence and Historical Review

- [x] Historical background, cultural significance, geography, period, methods, and
  materials are documented.
- [x] Archaeological, documentary, modern technical, and later folklore evidence are
  distinguished.
- [x] Claims carry confidence and unsupported standardization is prohibited.
- [x] Sources, visual references, uncertainty, and cultural risks are recorded.
- [x] Historical review gate is approved by a human reviewer.

#### Gameplay Review

- [x] Meaningful decision, problem, stories, and omission cost are explicit.
- [x] Strategy, clicks, tradeoff, labor burden, and simpler alternative are evaluated.
- [x] Complexity costs and seven measurable retention conditions are recorded.
- [x] Direct cooking is documented as the required fallback.
- [x] Gameplay review gate is approved with conditions by a human reviewer.

#### Engineering

- [x] XML-only feasibility is supported by verified RimWorld 1.6 Core patterns.
- [x] Exact item classification is deferred to verification rather than assumed.
- [x] No C#, Harmony, custom UI, ticker, or serialized custom state is justified.
- [x] DLC, save, performance, balance, art, localization, and compatibility risks are
  bounded.
- [x] ADR assessment is recorded.

#### Delivery and Dependencies

- [x] Oat Foods research questions and downstream acceptance tests are explicit.
- [x] Source and asset provenance requirements are recorded.
- [x] Specification and implementation remain unauthorized.
- [x] Human questions are resolved and approvals recorded.

**Research decision:** Passed with conditions
**Project Definition of Ready:** Not evaluated. Readiness Review approval,
specification, planning, and implementation authorization remain outstanding.

## Sources

Accessed 2026-07-05 unless otherwise stated.

1. Finbar McCormick, Thomas Kerr, Meriel McClatchie, and Aidan O'Sullivan,
   *The Archaeology of Livestock and Cereal Production in Early Medieval Ireland,
   AD 400-1100*, EMAP Report 5.1 (2011), especially printed pp. 32, 39-41, 45-54,
   and 63.
   [UCD repository record](https://researchrepository.ucd.ie/entities/publication/172fb4d4-9100-4788-b615-169f391da57f) |
   [report PDF](https://researchrepository.ucd.ie/server/api/core/bitstreams/163e8ed5-382c-4c50-962f-590c684a7244/content).
   Source type: archaeological synthesis of excavated animal and plant evidence with
   documentary comparison; strongest period-specific source used here.
2. Meriel McClatchie, Amy Bogaard, Sue Colledge, Nicki Whitehouse, Rick J. Schulting,
   Philip Barratt, and Thomas R. McLaughlin, “Early medieval farming and food
   production: a review of the archaeobotanical evidence from archaeological
   excavations in Ireland,” *Vegetation History and Archaeobotany* 24.1 (2015):
   179-186. [DOI](https://doi.org/10.1007/s00334-014-0478-7) |
   [Queen's University Belfast record](https://pure.qub.ac.uk/en/publications/early-medieval-farming-and-food-production-a-review-of-the-archae/).
   Source type: peer-reviewed archaeobotanical synthesis.
3. Eric A. Decker, Devin J. Rose, and Derek Stewart, “Processing of oats and the
   impact of processing operations on nutrition and health benefits,” *British
   Journal of Nutrition* 112.S2 (2014): S58-S64.
   [DOI](https://doi.org/10.1017/S000711451400227X) |
   [Cambridge Core article](https://www.cambridge.org/core/journals/british-journal-of-nutrition/article/processing-of-oats-and-the-impact-of-processing-operations-on-nutrition-and-health-benefits/12103B74748A0B4FFD8ABC1B5699786F).
   Source type: peer-reviewed modern food science; used for anatomy and processing
   cautions only, not historical reconstruction.
4. Foras na Gaeilge, “oat,” *English-Irish Dictionary*, Teanglann.
   [dictionary entry](https://www.teanglann.ie/en/eid/OAT).
   Source type: official modern language reference; not evidence of medieval usage.
5. Foras na Gaeilge, “brachán,” *Foclóir Gaeilge-Béarla*, Teanglann.
   [dictionary entry](https://www.teanglann.ie/en/fgb/Brach%C3%A1n).
   Source type: official modern language reference; not evidence of medieval usage.
6. “Oats-Making Long Ago,” *The Schools' Collection*, Dúchas.ie, collected in the
   late 1930s. [catalogue page](https://www.duchas.ie/en/cbes/5009058/4982015/5119194).
   Source type: later folklore collection; explicitly excluded as direct medieval
   evidence.
7. Ludeon Studios, locally installed RimWorld `1.6.4871 rev595` Core data,
   `Data/Core/Defs/ThingDefs_Items/Items_Resource_RawPlant.xml`,
   `Data/Core/Defs/ThingDefs_Items/Items_Food.xml`,
   `Data/Core/Defs/RecipeDefs/Recipes_Meals.xml`, and
   `Data/Core/Defs/Drugs/Alcohol_Beer.xml`, inspected 2026-07-05.
   Source type: proprietary current technical reference; behavior and values are
   paraphrased, and no XML is copied into the project.
8. Sarg Bjornson and Vanilla Expanded team, *Vanilla Cooking Expanded*, Steam
   Workshop item 2134308519.
   [Workshop page](https://steamcommunity.com/sharedfiles/filedetails/?id=2134308519).
   Source type: adjacent mod comparison; definitions, framework, balance, and assets
   were not reused.
9. Medieval Overhaul team, *Medieval Overhaul*, Steam Workshop item 3219596926.
   [Workshop page](https://steamcommunity.com/sharedfiles/filedetails/?id=3219596926).
   Source type: adjacent mod comparison; definitions, balance, and assets were not
   reused.

## Source and Asset Notes

- Period-specific claims rely primarily on archaeological sources [1] and [2].
- Source [3] limits false assumptions about modern oat products; it does not fill
  medieval evidence gaps.
- Sources [4] and [5] inform modern terminology only.
- Source [6] is explicitly later evidence and cannot establish medieval practice.
- Source [7] establishes technical feasibility, not design approval.
- Existing mods are comparisons only; no source XML, code, Def names, balance, art,
  texture, audio, translation, or other asset was copied.
- No gameplay XML, C#, textures, or package metadata were created.
