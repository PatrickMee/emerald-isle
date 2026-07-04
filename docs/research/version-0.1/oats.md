# Research Brief: Oats

**Research ID:** RSC-002
**Feature:** PL-01 Oats
**Release:** Version 0.1 - The First Holding
**Researcher:** Codex
**Reviewer:** Project maintainer (required)
**Status:** Review
**Date:** 2026-07-04
**Implementation authorized:** No

## Question and Design Need

Can an oat crop provide a historically grounded, culturally responsible, and
mechanically distinct agricultural foundation for Version 0.1 using RimWorld 1.6
Core XML only?

This brief informs whether PL-01 should advance to specification. It does not set
final Def values, approve art, or authorize implementation.

## Scope

**Primary period:** Early medieval Ireland, approximately AD 400-1100.
**Supporting periods:** Later medieval evidence where it clarifies continuity;
nineteenth- and early-twentieth-century evidence only for explicitly late practice
and visual reference.
**Geography:** The island of Ireland, with regional differences retained where the
evidence permits.
**Botanical subject:** Cultivated oat, principally common oat (*Avena sativa*) where
species-level identification is secure.
**Language:** English player-facing name `oats` is the working default. Modern Irish
`coirce`, oatmeal `min choirce`, and oat porridge terminology are research references,
not approved labels.
**Excluded:** Claims of a single unchanging Irish oat tradition; prehistoric oat
cultivation as established fact; modern nutrition or agronomy projected into the
early medieval period; final recipes; quern design; final balance values.

## Executive Finding

Oats are a strong Version 0.1 candidate. A 2011 synthesis of plant remains from 60
excavated early medieval sites found oat at 80% of 165 analysed phases/areas, second
only to barley at 88%. Oat occurred across all four provinces in the dataset and
became more often dominant in later phases, although sampling, preservation, dating,
and regional excavation intensity limit precision. The evidence supports a common,
workaday cereal associated with food, fodder, storage, drying, and milling. It does
not support presenting oats as Ireland's unique or timeless national crop.

The best RimWorld role is a medium-cycle grain that begins a labor-dependent food
chain. It should compete with rice, potatoes, and corn through resilience and later
processing options, not through superior calorie output. XML-only implementation is
the preliminary technical recommendation.

## Historical Background

### Establishment and Chronology

The strongest evidence belongs to the early medieval period. McCormick, Kerr,
McClatchie, and O'Sullivan's archaeological synthesis reports that barley and wheat
were cultivated in Ireland from the Early Neolithic, while oats and rye occur only
occasionally in prehistoric deposits and are generally thought to have become
cultivated crops from the early medieval period. This is a scholarly interpretation,
not proof that every earlier oat grain was wild or intrusive [1, pp. 45-46].

The same report found oat in 80% of the 165 early medieval site phases/areas that it
examined. Common oat was the most frequently identified oat species, followed by
bristle oat and wild oat, but species identification often failed because diagnostic
floret bases were absent [1, p. 50]. A later peer-reviewed synthesis of the same
60-site program likewise identifies hulled barley and oat as the dominant crops of
the period [2].

Chronology was not static. In the subset with usable radiocarbon dates, barley was
more often dominant in fourth- to seventh-century assemblages. Oat came close to
barley's dominance in seventh- to tenth-century assemblages [1, pp. 51, 53]. That
supports an early-medieval identity while warning against assigning one crop balance
to the entire AD 400-1100 period.

### Cultural Significance

Early medieval cereals were food, fodder, building material, and obligations. The
archaeological synthesis records cereals as inputs to breads, gruels, porridges,
brewing, animal fodder, roofing, bedding, and food-rent, drawing on archaeology and
contemporary documentary evidence [1, p. 45]. These are cereal-wide uses; they must
not all be attributed specifically to oats without feature-level evidence.

An eighth-century law tract, *Bretha Déin Chécht*, lists `corcae` (oat) at the lower
end of a prestige ordering of cereals. The report interprets oat as associated with
the commoner, in contrast with higher-status bread wheat [1, p. 46]. This gives oats
a useful project theme - dependable everyday sustenance - but it must not become a
mechanic that stereotypes ordinary people as culturally inferior.

Oats remained important much later. The Central Statistics Office records 619,000
hectares under oats in 1850, 50.5% of the combined area under wheat, oats, barley,
and potatoes; the series peaks at 672,000 hectares in 1852 [3]. These statistics show
nineteenth-century scale, not uninterrupted continuity from the early medieval period.

### Geographic Context

The 2011 dataset deliberately sampled the island: 7 sites in Ulster, 20 in Munster,
19 in Leinster, and 14 in Connacht. The authors also warn that road schemes and other
infrastructure produced concentrations of evidence, particularly in Galway and
Meath [1, p. 48]. Presence/absence analysis found barley first and oat second in all
four regions [1, pp. 51-52].

The smaller dominance subset suggests oat was more often dominant in Ulster and
Munster, while barley was more often dominant in Leinster and Connacht. The authors
explicitly caution that some regional samples were small [1, p. 54]. Emerald Isle
therefore should not encode a province-specific oat rule in Version 0.1.

Ireland's damp climate made grain drying especially important before storage and
milling [1, p. 32]. This supports a general moisture-management theme, but Version
0.1 should not simulate weather-dependent grain spoilage unless a future feature
earns that complexity.

## Production Methods and Materials

The following sequence is supported at different levels of confidence. It describes
a historical production context, not a mandatory Version 0.1 feature list.

| Stage | Evidence | Materials or tools | Confidence | Version 0.1 relevance |
|---|---|---|---|---|
| Soil preparation and sowing | Documentary synthesis describes suitable tilth, livestock manure, and normal spring sowing [1, pp. 28-29] | Arable soil, seed, manure, digging/ploughing tools | Medium | Supports an ordinary sown crop; no custom soil system |
| Reaping | Autumn harvest, often communal, used sickles rather than scythes in the primary period [1, p. 29] | Sickle/reaping hook, baskets or later sheaves | High for cereal harvest; medium for exact local practice | Vanilla plant-cut work is sufficient |
| Drying | Damp grain could spoil or obstruct milling; cereal-drying kilns are archaeologically widespread [1, p. 32] | Grain, heat, kiln/flue/chamber or simpler drying arrangements | High for cereals; medium for every oat batch | Historical context only in 0.1 |
| Threshing and winnowing | Early texts mention threshing with a stick; the two-part flail was in general use by the eleventh or twelfth century [1, pp. 30-31]. Later folklore records hooks/scythes, sheaves, flails, and milling [4] | Hard floor, stick or flail, sieve/winnowing equipment | Medium; later records are not early-medieval proof | Abstract into harvest; no extra job chain |
| Storage | A probable clay-and-wicker store at Drumadoon contained nearly 20,000 charred oat grains with chaff [1, p. 31] | Dry store, baskets/bins, chaff, protected stack | High for the site; medium for general form | Shelf life and storage burden need balance review |
| Milling | Domestic hand querns and early medieval watermills are well evidenced; drying accelerates hand milling [1, pp. 39-41] | Dried grain, stone quern or millstones, labor/water power | High | Interface to the separate hand-quern and milled-oats briefs |

The Bray/Giltspur excavation provides a useful site-level association: a
grain-drying kiln contained charred oats and wheat, and its backfill included a
granite rotary-quern fragment [5]. Because the report noted that radiocarbon results
were pending, this evidence should not alone establish the site's exact date.

Later National Folklore Collection accounts are valuable records of remembered
practice, not direct medieval testimony. A Westmeath account describes cutting with
hooks or scythes, binding sheaves, drying and stacking, threshing with a flail, and
taking grain to a mill [4]. Its collection context and late tools must remain visible
whenever it informs art or writing.

## Historical Claims and Confidence

| Claim | Evidence | Confidence | Design use |
|---|---|---|---|
| Oats were a major early medieval Irish cereal | 60-site, 165-phase synthesis; oat present in 80% of phases [1, pp. 48, 50]; peer-reviewed review [2] | High | Core identity of the crop |
| Cultivated oats became established in the early medieval period rather than the Neolithic | Archaeobotanical synthesis with occasional prehistoric finds acknowledged [1, pp. 45-46] | Medium | Avoid prehistoric claims; use early medieval focus |
| Oat importance increased relative to barley later in the early medieval period | Radiocarbon-dated dominance subset [1, pp. 51, 53] | Medium | Background flavor only; no era progression in 0.1 |
| Oats were lower-prestige/commoner cereals in an early law-text framework | Secondary interpretation of *Bretha Déin Chécht* [1, p. 46] | Medium | Everyday-food theme; never a social-rank debuff |
| Oats were used specifically for every listed bread, porridge, brewing, and fodder use | Cereal-wide evidence; species-specific allocation varies [1, pp. 45-46] | Low as a universal claim | Requires separate food research |
| Damp conditions made drying important | Technology and archaeological synthesis [1, p. 32] | High at system level | Supports processing context, not weather simulation |
| Oats were dominant everywhere in Ireland | Regional data contradict uniform dominance [1, pp. 51-54] | Rejected | Claim must not appear |

## Uncertainty and Contestation

- Charred plant remains overrepresent plants that encountered fire. Preservation does
  not provide a neutral measure of everything grown or eaten [1, p. 45].
- Several source reports used abundance bands rather than counts, limiting comparison
  beyond presence/absence [1, p. 48].
- Oat species identification requires floret bases, which were often missing. Some
  remains classed broadly as oat may be wild oat [1, p. 50].
- Radiocarbon ranges often span centuries. The report's fourth-seventh and
  seventh-tenth-century comparison includes overlap [1, p. 51].
- Excavation distribution reflects modern development and research history as well as
  historical activity [1, p. 48].
- Legal texts describe normative categories and status, not a census of actual diets.
- Nineteenth- and twentieth-century practices cannot be retrojected unchanged into
  the early medieval period.
- Modern cultivated varieties, yields, and disease resistance are unsuitable proxies
  for historical performance without explicit qualification.

## Cultural Sensitivities and Misconceptions

- Do not define Irish food history solely through potatoes or present oats as a
  novelty that appeared after the potato.
- Do not call oats the uniquely Irish grain. Barley was at least as prominent in the
  early medieval evidence.
- Do not collapse `commoner` in a legal prestige scheme into poverty, backwardness,
  or a negative pawn trait.
- Do not turn hard agricultural labor into pastoral nostalgia. Historical production
  involved weather risk, repetitive work, storage, and processing.
- Do not label later folklore as an unchanged survival from ancient Ireland.
- Do not place Irish words in the UI as decoration. Modern `coirce` and related forms
  require grammatical and speaker review before player-facing use [6].

## Language and Naming

Teanglann's historical dictionaries give modern Irish `coirce` for oats and
`min choirce` for oatmeal; entries also distinguish hulled oats and terms for sowing,
reaping, sheaves, and oat foods [6]. The early law-text form reported in scholarship
is `corcae` [1, p. 46]. These forms belong to different linguistic contexts.

Preliminary naming policy:

- Use concise English labels (`oats`, `oat plant`) in the source locale.
- Record Irish terminology in translator/research notes.
- Do not use the historical form `corcae` as a generic modern label.
- Require competent Irish-language review before any Irish term becomes visible to
  players.

## Visual References

These are study references only. No source image is cleared for redistribution in
Emerald Isle.

| Reference | Useful information | Rights action |
|---|---|---|
| EMAP Report 5.1, Figure 1:23 [1, p. 29] | Archaeological sickle and sickle-like tool silhouettes | Link/cite only unless reuse terms are confirmed |
| EMAP Report 5.1, Figure 1:24 [1, p. 31] | Plan of probable Drumadoon cereal store associated with oats | Link/cite only unless reuse terms are confirmed |
| EMAP Report 5.1, Figure 2.1 [1, p. 49] | Geographic spread and sampling bias of analysed sites | Link/cite only unless reuse terms are confirmed |
| Dúchas, “Oats-Making Long Ago” [4] | Archival handwriting/page and a late traditional workflow | Image and data are marked © National Folklore Collection, UCD; do not copy |
| Excavations.ie, Bray/Giltspur report [5] | Site-level kiln/quern context | Link only; confirm photographer/report rights before reuse |
| Teagasc oat publications [7] | Modern botanical appearance and field structure only | Do not treat as medieval visual evidence; clear rights before reuse |

Original crop art should show a readable cereal panicle and remain visually distinct
from vanilla rice and haygrass at RimWorld camera scale. Historical accuracy does not
require photorealism or a specific modern cultivar.

## RimWorld Vanilla Comparison

The comparison below was verified against the locally installed RimWorld
`1.6.4871 rev595` Core definitions on 2026-07-04 [8]. Values are inputs for a later
balance model, not proposed oat statistics.

| Core crop | Grow days | Harvest yield | Nutrition per harvested unit | Nominal nutrition per mature tile | Fertility behavior | Shelf life |
|---|---:|---:|---:|---:|---|---:|
| Rice | 3.0 | 6 | 0.05 | 0.30 | Default/high sensitivity; hydroponic | 40 days |
| Potatoes | 5.8 | 11 | 0.05 | 0.55 | Sensitivity 0.4; hydroponic | 30 days |
| Corn | 11.3 | 22 | 0.05 | 1.10 | Minimum fertility 0.70; ground only | 60 days |

Ignoring planting/harvest labor, fertility, darkness, temperature, blight, and harvest
failure, these crops cluster close to 0.10 nominal nutrition per grow-day per tile.
That convergence is a design guardrail: oats should not gain a substantially higher
gross calorie rate merely because later processing consumes labor.

Oats need a legible niche. The preliminary comparison hypothesis is:

- a medium growth cycle between potatoes and corn;
- lower dependence on rich soil than rice or corn, subject to playtest evidence;
- raw grain suitable for storage, recipes, and possibly animal feed;
- best human value unlocked through the separately reviewed milling/food chain;
- no hydroponics unless the specification provides a gameplay reason;
- no custom cold-growth code or weather simulation.

The crop should not combine potato-like poor-soil performance, corn-like yield and
shelf life, and rice-like speed. That would erase vanilla choices.

## Existing Mod Comparison

This is a market/compatibility scan, not an endorsement or a source of reusable code
or art.

| Mod | Observed scope | Lesson | Verification limits |
|---|---|---|---|
| `[B18] Oats!` | Workshop listing describes a growable oat plant, harvested oats, and oatmeal [9] | Crop-to-food is established mod territory; Emerald Isle needs stronger balance, provenance, and current support | Obsolete B18 listing; implementation and license not inspected |
| Vanilla Plants Expanded - More Plants / related VE Cooking integration | Current listings describe a broad crop pack; oat can participate in vegetable-milk production when related modules are present [10] | Avoid requiring a framework or making oats useful only through a large content suite; duplication must be tested | Workshop content was not installed locally; exact current oat Def values remain unverified |
| Other crop/food suites | Search results indicate likely oat duplication in broad agriculture mods | A stable Emerald Isle Def name and narrow compatibility policy are required | Treat as unassessed until exact supported versions and package IDs are inspected |

Compatibility should not attempt to merge every oat item automatically. Before
release, test at least one current broad crop suite and document duplicate-content
behavior. Cross-mod recipe patches require a demonstrated player problem and their
own maintenance owner.

## Gameplay Opportunities

### Strong Opportunities

1. **Settlement food foundation:** A recognizable crop starts the complete Version
   0.1 field-to-food loop.
2. **Crop planning:** A medium-cycle, less fertility-sensitive grain can sit between
   fast rice and high-batch corn without replacing either.
3. **Labor conversion:** Raw oats become a production input whose best food uses may
   require milling, if the quern research proves that step creates a decision.
4. **Food/feed tension:** If animals can consume raw oats, colonists choose between
   immediate feed and labor-intensive human food. This requires balance validation.
5. **Storage planning:** Grain shelf life can support seasonal play without matching
   or exceeding corn automatically.

### Opportunities to Reject for Version 0.1

- weather-dependent drying or dampness simulation;
- straw as a second harvest product;
- crop disease unique to oats;
- regional/world-generation bonuses;
- social-class mechanics tied to cereal choice;
- brewing, fodder systems, fertility amendments, or automated mills;
- DLC-gated core behavior.

## Balance Considerations

The intended decision is not “oats are the Irish crop, so plant them.” It is “oats
fit this colony's soil, timing, storage, and planned labor chain better than another
crop.”

The specification must model:

- nutrition per grow-day and per pawn work unit against rice, potatoes, and corn;
- poor, normal, and rich soil performance;
- harvest timing and loss exposure;
- raw nutrition, food poisoning, animal consumption, rot, stack size, mass, and value;
- milling losses or gains without creating free nutrition;
- cooking labor across the complete oat-food chain;
- colony wealth and trade value;
- whether bypassing the quern through generic meals invalidates the production loop;
- whether forbidding generic use makes the crop too brittle with other food mods.

No final number should be approved from spreadsheet parity alone. Controlled in-game
tests must compare equal soil area, elapsed time, plant skill/work, and complete food
labor.

## Technical Implementation Considerations

### Expected Core Def Surface

Research indicates standard Core mechanisms should cover the feature:

- one cultivated `ThingDef` using the vanilla plant lifecycle;
- one harvested-item `ThingDef` using normal resource/raw-food behavior;
- sowing, harvest, rot, storage, trade, food-type, and ingredient categories;
- mature and immature plant graphics plus one harvested-item graphic;
- English Def-injected translation data and stable public Def names;
- optional, narrow compatibility patches only after exact targets are verified.

This is feasibility analysis, not XML design. Exact parent Defs and fields must be
selected during the implementation plan from the supported build.

### XML vs C# Recommendation

**Recommendation: XML only. C# is not justified. Harmony is prohibited for this
feature unless a later accepted ADR changes the frozen scope.**

Vanilla Core already provides sowing, growth, fertility response, blight, harvest,
rot, ingestibility, animal feeding, storage, trade, bills, and save serialization.
The proposed oat role does not need a custom component, tick behavior, or patch.

### DLC Policy

| Environment | Preliminary behavior |
|---|---|
| RimWorld 1.6 Core only | Full crop and harvested item available |
| Royalty absent/present | No required behavior change |
| Ideology absent/present | Core function unchanged; verify food-category/precept interactions |
| Biotech absent/present | Core function unchanged; verify pollution/growth interactions follow vanilla plants |
| Anomaly absent/present | No required behavior change |
| Odyssey absent/present | No required behavior change; test current plant/biome interactions |

No DLC is required. Optional enhancements are not recommended for PL-01 itself.

### Save and Removal Considerations

- Public Def names become persistent contracts at first implementation and must not
  be renamed casually.
- Adding a new plant and item should be safe for existing Core saves, but this must be
  tested rather than assumed.
- Removing the mod from a save containing growing plants or stored oats can lose
  content and produce missing-Def warnings; the release must declare its actual
  compatibility level.
- The harvested item must not serialize custom state.
- Exact add, save/load, update, and removal tests belong in the future specification
  and plan.

### Performance

Standard plant and item Defs should add negligible systemic overhead because they use
vanilla ticking and rendering paths. The plan must still check large fields, mature
plant rendering, fire/blight, and save size. No per-tick custom code is acceptable.

### Art and Localization

Art effort is medium: at minimum a mature plant, immature plant, and harvested-grain
icon must remain distinct from rice, corn, and haygrass through growth, snow, wind,
fire, and normal zoom. Exact file count depends on the verified vanilla graphic class.

English is the source locale. Irish terminology remains metadata until reviewed by a
competent speaker. No text should be embedded in textures.

## Risks

| Risk | Likelihood | Impact | Mitigation or gate |
|---|---|---|---|
| Oats become a cosmetic rice/corn clone | Medium | High | Require a measurable crop-planning decision before specification acceptance |
| Complete oat chain produces excessive nutrition or labor tax | Medium | High | Balance the whole chain, not PL-01 in isolation |
| Generic meal recipes bypass milling | High | Medium | Decide ingredient/category behavior explicitly during food research |
| Raw oats are useless until later features ship | Medium | Medium | Release integration must ship the approved chain together; development builds document incompleteness |
| “Hardy” becomes an unsupported poor-soil/cold superpower | Medium | High | Treat it as a gameplay hypothesis and test against vanilla, not as a historical fact |
| Crop mods add duplicate oats | High | Medium | Document duplication; test selected current mods; avoid broad automatic patching |
| Irish terminology is grammatically wrong or ornamental | Medium | High | English default; qualified language review before visible Irish |
| Source imagery is copied without rights | Low | High | Use sources as reference only; create original assets and record provenance |
| Research overstates uniformity | Medium | High | Preserve regional, temporal, and sampling caveats in spec and writing |

## Open Questions

### Questions Answerable by Later Research or Testing

1. Should raw oats be accepted by generic meal recipes, or should milling be the
   principal human-food route?
2. Should raw oats be edible by humans with vanilla `RawBad` behavior, animal feed
   only, or non-ingestible until processed?
3. What precise fertility sensitivity, growth duration, yield, and shelf life produce
   a distinct but non-dominant choice?
4. Should oats be ground-only or hydroponic-capable?
5. Which current crop mods define oats, and what are their exact package IDs, Def
   names, licenses, and current RimWorld 1.6 support claims?
6. Does the supported build require one or multiple growth graphics to meet the art
   standard?
7. Which ingredient categories preserve compatibility without allowing unintended
   recipe bypasses?

### Questions Requiring Human Review

1. Approve early medieval Ireland (AD 400-1100) as the primary historical frame for
   PL-01, with later evidence clearly labeled as supporting context?
2. Approve “everyday, medium-cycle processing grain” as the design direction, subject
   to later balance tests?
3. Should the specification explore raw oats as animal feed as well as a milling
   input, or keep Version 0.1 entirely human-food focused?
4. Approve English `oats` as the player-facing source label, reserving Irish terms for
   reviewed contextual use?
5. Is the preliminary conclusion strong enough to advance PL-01 to specification
   after the other four ordered research briefs are reviewed, or is another source
   class required first?

## Preliminary Recommendation

Advance PL-01 toward specification **after human approval of this research brief and
after completion of the ordered Version 0.1 research sprint**.

The future specification should examine one XML-only cultivated oat plant and one
harvested oat item. It should target a medium growth cycle, a meaningful but bounded
resilience advantage, and gross nutrition in the vanilla crop envelope. Its primary
purpose is to feed the approved milling-and-food chain. It should add no custom soil,
weather, straw, disease, social-rank, research, or DLC mechanic.

## Research Review

### Summary

Evidence from a large early medieval archaeological dataset makes oats a defensible
and culturally meaningful foundation crop. The evidence is strongest for widespread
importance, ordinary food-production context, and integration with drying, storage,
and milling. It is weaker for species-level identification, precise regional balance,
and assigning particular foods exclusively to oats.

### Recommended Gameplay Implementation

A medium-cycle, XML-only cereal crop that offers a bounded soil/timing alternative to
vanilla staples and becomes the raw input for milling and oat foods. Its strength must
be paid for through yield, labor, storage, or processing tradeoffs.

### Recommended Version 0.1 Implementation

Include one oat plant and one harvested oat item. Use Core systems only; require no
DLC, C#, Harmony, custom research, special terrain, secondary straw product, or
standalone simulation. Ship it only as part of the complete frozen Version 0.1 chain.

### Human Review Decision

**Decision:** Pending
**Reviewer/date:** Pending
**Corrections:** Pending
**Approved uses:** Pending

### Definition of Ready Checklist

This checklist records readiness to begin implementation, not research completeness.
The feature remains **Not Ready** while review, specification, planning, and evidence
gates are open.

#### Product and Identity

- [x] Catalog ID, milestone, and frozen first-slice boundary are assigned.
- [x] Player purpose and preliminary meaningful decision are stated.
- [x] Constitution and Design Bible constraints are reflected in the research.
- [ ] Feature Acceptance Checklist is completed for an actual specification.
- [x] Explicit Version 0.1 exclusions are recorded.

#### Evidence and Design

- [ ] Research brief is approved by the human reviewer.
- [x] Confidence, uncertainty, chronology, geography, and sensitivity are recorded.
- [x] Vanilla comparison and measurable balance questions are documented.
- [ ] Final canon, language, art, accessibility, and localization needs are approved.
- [ ] Acceptance, edge, failure, DLC, and persistence scenarios exist in a specification.

#### Engineering

- [x] XML-first recommendation is documented; C# and Harmony are not justified.
- [ ] Architecture, exact Def surface, public identifiers, save impact, and migration are reviewed in a plan.
- [ ] Relevant ADR check is completed against the future specification.
- [ ] Performance budget and compatibility matrix cases are finalized.
- [ ] Implementation plan names exact paths and independently verifiable slices.
- [ ] Test, playtest, and rollback evidence requirements are actionable in tasks.

#### Delivery

- [ ] Required reviewers and art/localization skills are assigned.
- [ ] Human-review questions and downstream food-chain dependencies are resolved.
- [ ] Tasks are estimated and the first implementation slice has no hidden work.

**Decision:** Not Ready
**Conditions:** Human research approval; remaining ordered research briefs; accepted
feature specification; Feature Acceptance Checklist; implementation plan; final
Definition of Ready approval.

## Sources

Accessed 2026-07-04 unless otherwise stated.

1. Finbar McCormick, Thomas R. Kerr, Meriel McClatchie, and Aidan O'Sullivan,
   *The Archaeology of Livestock and Cereal Production in Early Medieval Ireland,
   AD 400-1100*, Early Medieval Archaeology Project Report 5.1 (2011), especially
   pp. 28-32, 39-46, and 48-54.
   [UCD repository record](https://researchrepository.ucd.ie/entities/publication/172fb4d4-9100-4788-b615-169f391da57f) |
   [report PDF](https://researchrepository.ucd.ie/server/api/core/bitstreams/163e8ed5-382c-4c50-962f-590c684a7244/content).
   Source type: archaeological synthesis and report; combines primary excavation data
   with secondary interpretation.
2. Meriel McClatchie, Finbar McCormick, Thomas R. Kerr, and Aidan O'Sullivan,
   “Early medieval farming and food production: a review of the archaeobotanical
   evidence from archaeological excavations in Ireland,” *Vegetation History and
   Archaeobotany* 24, no. 1 (2015): 179-186.
   [DOI](https://doi.org/10.1007/s00334-014-0478-7) |
   [Queen's University Belfast record](https://pure.qub.ac.uk/en/publications/early-medieval-farming-and-food-production-a-review-of-the-archae/).
   Source type: peer-reviewed secondary synthesis.
3. Central Statistics Office, “Crops and Livestock,” *Statistical Yearbook of
   Ireland 2021*, Table 24.3, area under selected crops 1850-2020.
   [CSO](https://www.cso.ie/en/releasesandpublications/ep/p-syi/statisticalyearbookofireland2021part3/agri/cropsandlivestock/).
   Source type: official statistics; primary quantitative source for the period covered.
4. Joseph Maguire (informant) and Teresa Maguire (collector), “Oats-Making Long Ago,”
   The Downs, Co. Westmeath, Schools' Collection, vol. 0730, p. 104, National
   Folklore Collection, UCD.
   [Dúchas record](https://www.duchas.ie/en/cbes/5009058/4982015/5119194).
   Source type: 1930s folklore/oral-history record; late supporting evidence. Image
   and data © National Folklore Collection, UCD.
5. “Bray/Giltspur,” County Wicklow, excavation report 2004:1853, licence 04E0285,
   *Excavations.ie*.
   [Excavations.ie record](https://excavations.ie/report/2004/Wicklow/0012973/).
   Source type: primary archaeological field report; dating caveat retained.
6. Teanglann, English-Irish Dictionary entry “oat” and *Foclóir Gaeilge-Béarla*
   entry `coirce`.
   [oat](https://www.teanglann.ie/en/eid/oat) |
   [coirce](https://www.teanglann.ie/ga/fgb/coirce).
   Source type: authoritative dictionary reference; competent speaker review still required.
7. Teagasc, “Oats: A high performing native grain” (25 November 2025).
   [Teagasc](https://teagasc.ie/publications/oats-a-high-performing-native-grain/).
   Source type: modern agronomic comparison only; not evidence of medieval practice.
8. Ludeon Studios, locally installed RimWorld `1.6.4871 rev595` Core data:
   `Data/Core/Defs/ThingDefs_Plants/Plants_Cultivated_Farm.xml` and
   `Data/Core/Defs/ThingDefs_Items/Items_Resource_RawPlant.xml`, inspected
   2026-07-04. Proprietary reference data; values paraphrased for design comparison.
9. Arthritis Gaming, `[B18] Oats!`, description preserved in Steam Workshop
   collection 1405231973.
   [Steam Workshop](https://steamcommunity.com/sharedfiles/filedetails/?id=1405231973).
   Source type: obsolete mod listing; no code or asset reuse.
10. Vanilla Expanded team, *Vanilla Plants Expanded - More Plants*, Steam Workshop
    item 2748889667, and associated public release description.
    [Steam Workshop](https://steamcommunity.com/sharedfiles/filedetails/?id=2748889667).
    Source type: current mod-market comparison; exact installed Defs not inspected.

## Source and Asset Notes

- Historical claims above cite the report pages that support them.
- The same research program underlies sources [1] and [2], so they are not treated as
  fully independent confirmation.
- Source images are references only. Emerald Isle will require original artwork and
  recorded provenance.
- No source code, XML, or assets from another mod were copied or inspected for reuse.
