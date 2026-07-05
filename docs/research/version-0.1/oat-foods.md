# Research Brief: Oat Foods

**Research ID:** RSC-006
**Feature:** FO-01 Oat Foods
**Release:** Version 0.1 - The First Holding
**Researcher:** Codex
**Reviewer:** Unassigned
**Status:** Review
**Historical review:** Pending
**Gameplay review:** Pending
**Date:** 2026-07-05
**Research Definition of Ready:** Review required
**Approved scope:** `docs/product/version-0.1-approved-scope.md`
**Implementation authorized:** No

## Question and Design Need

Which one or two oat-based foods are sufficiently supported by early medieval Irish
evidence and sufficiently distinct in RimWorld gameplay to complete the Version 0.1
oat chain without becoming meal clutter?

This brief evaluates two candidates:

1. **oat porridge**, representing a fresh pot-based cereal food; and
2. **oat flatbread**, representing the oat flat breads recorded in early sources.

It also tests whether those foods justify the approved-but-conditional hand quern and
milled-oats intermediate. It does not define final Def values, recipes, art, research
prerequisites, or XML.

## Scope

**Primary period:** Early medieval Ireland, approximately AD 400-1100.
**Geography:** The island of Ireland; no province-specific recipe is asserted.
**Social setting:** Ordinary domestic holdings, with legal and monastic evidence used
carefully rather than treated as a universal household menu.
**Working English terms:** `oat porridge` and `oat flatbread`.
**Historical terms:** `littiu` is recorded for a common porridge; modern Irish
dictionary terms include `min choirce`, `brachán (mine) coirce`, and `arán coirce`.
These are research references, not approved player-facing Irish labels.
**Excluded:** Brewing; dairy systems; honey or seasoning mechanics; medical foods;
baby-food behavior; food quality; condiments; feast or ritual mechanics; new cooking
buildings; ovens, griddles, pots, or tableware as items; custom thoughts; custom C#;
Harmony; and any third oat food.

## Executive Finding

The historical case supports a two-food pair. Early documentary synthesis divides
cereal foods into pot-based foods and breads, identifies a common porridge, and
records flat breads made from oats as well as other cereals. Archaeological evidence
independently establishes oats as one of the dominant crops and domestic querns as
common equipment. Exact recipes, proportions, textures, serving sizes, and keeping
times are not recoverable at the precision required for game statistics.

The gameplay case is **Recommended with Conditions**. Porridge and flatbread can earn
separate items if they form a readable choice:

- porridge converts prepared grain into a fresh meal with low final-cooking burden
  but short storage life; and
- oat flatbread requires more total labor but provides a ready-to-eat, moderately
  keeping, plant-only food suitable for travel and reserves.

Both remain simple-tier foods. Porridge must not become a superior simple meal, and
flatbread must remain materially worse at long-term preservation than pemmican and
packaged survival meals. If testing cannot sustain these distinctions in XML, the
simpler fallback is one oat-flatbread food or direct oat use in vanilla meals, with
the redundant processing layer removed.

## Historical Background

### Cereal Foods in Early Medieval Ireland

O'Sullivan, McCormick, Kerr, Harney, and Kinsella synthesize archaeological and
documentary evidence for early medieval domestic life [1]. Their food discussion,
drawing particularly on Kelly and Sexton, identifies two broad cereal-food groups:
pot-based foods and bread. It describes several porridges and gruels and records flat
breads made from oats, wheat, barley, or rye [1, printed pp. 102-103].

The same report states that oats and barley were commonly used in porridges, gruels,
and breads [1, printed p. 103]. This is the strongest direct support for the two
Version 0.1 candidates. It does not prove that every household regularly prepared
both, or that one recipe remained unchanged throughout AD 400-1100.

Sexton's peer-reviewed chapter, *Porridges, Gruels, and Breads: The Cereal Foodstuffs
of Early Historic Ireland*, is the specialist study underlying much of that synthesis
[3]. The chapter is bibliographically verified, but its full text was not directly
inspected for this brief. Claims attributed to it here are limited to those reproduced
and contextualized by the EMAP reports.

### Porridge and Gruel

The settlement synthesis identifies `littiu` as the most common named porridge in the
reviewed written evidence and associates it with nourishment for children and sick
people [1, printed p. 102]. Other gruel-like foods appear in penitential and monastic
contexts. These associations show variation in use and meaning; they do not justify
restricting a RimWorld porridge to children, illness, monks, or religious observance.

Soft cooked foods rarely preserve as identifiable archaeological objects. The
historical case therefore depends primarily on early texts as interpreted by food
historians, supported by the archaeological prevalence of cereals, querns, hearths,
and cooking equipment. `Oat porridge` is a defensible broad translation for gameplay,
not a reconstruction of one named recipe.

### Oat Flatbread

The written-source synthesis explicitly records flat breads made from oats, wheat,
barley, or rye [1, printed p. 102]. It distinguishes these from standard wheat loaves
and also notes coarse breads containing barley, oats, or pulses in monastic contexts.
Some breads could include salt, honey, or pulses or be served with other foods, but
those optional combinations do not define a universal oat bread [1, printed p. 102].

The same report describes a griddle, turner, kneading slab, trough, sieve, and hearth
among equipment named in early legal sources. Dough was prepared in a trough, cooked
on a griddle, and turned during cooking [1, printed p. 100]. This supports a flatbread
form and an ordinary cooking bill. It does not require Version 0.1 to add a griddle,
oven, new hearth, or utensil system.

## Cultural Significance

Porridge and oat flatbread express the project's ordinary-holding focus better than a
prestige dish. They connect cultivation, domestic processing, hearth cooking, and
food security. The distinction between pot food and bread also gives the same crop
more than one practical use without inventing a large cuisine system.

Early legal texts ranked cereals in relation to social status, with oats placed near
the common end of that hierarchy [1, printed pp. 102-103; 2, printed pp. 46-47]. The
game must not convert that historical status model into pawn classes, penalties, or a
claim that oat food is inferior culture. Ordinary food can be valued without
romanticizing hardship or reproducing prescriptive hierarchy.

Version 0.1 should also avoid the later “cottage Ireland” image. Oatcakes, griddles,
and open-hearth cooking remained visible in nineteenth- and twentieth-century
folklife, but later continuity cannot fill medieval recipe gaps or dictate the art.

## Geographic Context

Archaeobotanical evidence finds oats widely across early medieval Ireland, while the
documentary food evidence is not precise enough to establish one regional recipe map
[2]. The Version 0.1 pair should represent plausible food in one holding, not a
province-specific tradition or a universal national cuisine.

The evidence also spans rural secular and ecclesiastical settings. Monastic bread and
penitential gruels are relevant comparisons, but the player foods should not be named
or described as monastic unless later research and scope explicitly support that
identity.

## Historical Time Period

The target period is AD 400-1100. The strongest textual discussion draws on law
tracts associated especially with the seventh and eighth centuries, while the
archaeological cereal record covers a broader early medieval range [1, 2, 4].

This chronological mismatch requires restraint. It supports the general presence of
oat-based pot foods and flatbreads, not a claim that ingredients, serving practices,
or terminology were uniform for seven centuries.

## Production Methods

### Oat Porridge

A defensible high-level sequence is:

1. clean, dry, and mill oats into usable meal;
2. combine meal with liquid in a cooking vessel;
3. cook and stir over heat until it becomes a soft cereal food;
4. serve fresh.

The game should abstract water and the vessel, as Core does for ordinary cooking.
Milk, butter, honey, salt, eggs, or other enrichments may have existed in particular
contexts, but requiring them would enlarge scope and convert optional historical
variation into a universal recipe.

### Oat Flatbread

A defensible high-level sequence is:

1. mill oats into meal;
2. combine the meal into a workable dough;
3. shape a thin or compact bread;
4. cook it on or near a heated surface or fire;
5. cool and store or carry it for later eating.

Early sources support kneading and griddle cooking generally [1, printed p. 100].
The exact oat dough composition, thickness, cooking duration, moisture content, and
storage life remain uncertain. `Moderately keeping` is a proposed RimWorld role, not
a historical shelf-life measurement.

## Materials

### Historically Supported or Plausible

- ground oat meal;
- water or another liquid for mixing;
- a vessel and heat for porridge;
- a trough or surface, griddle or hearth, and turner for flatbread;
- optional salt, dairy, honey, pulses, or accompaniments in some contexts.

### Version 0.1 Abstraction

- **Required game ingredient:** milled oats only.
- **Water:** abstracted by the cooking bill.
- **Fuel or power:** supplied by the selected vanilla cooking building.
- **Optional historical ingredients:** omitted rather than made mandatory.
- **Tools and containers:** represented by vanilla cooking infrastructure, not new
  items.

The one-ingredient recipe is a deliberate gameplay simplification. It avoids adding
water, dairy, seasoning, containers, or a hearth system before those concepts have
independent player value.

## Historical Claims and Confidence

| Claim | Evidence | Confidence | Design relevance |
|---|---|---:|---|
| Oats and barley were common early medieval Irish cereals. | Archaeobotanical syntheses [1, printed pp. 102-103; 2, printed pp. 47-54] | High | Supports an ordinary oat-food chain. |
| Early Irish sources describe multiple pot-based cereal foods. | Documentary synthesis [1, printed p. 102; 3; 4] | High | Supports porridge as a food form. |
| Oats were used in porridges and gruels. | EMAP synthesis of early texts [1, printed p. 103] | Medium-high | Supports `oat porridge`; recipe details remain uncertain. |
| Flat breads could be made from oats. | EMAP synthesis citing specialist food history [1, printed p. 102; 3] | High | Supports an oat flatbread. |
| Bread dough could be prepared in a trough and cooked on a griddle. | Early legal-source synthesis [1, printed p. 100; 4] | High for bread generally | Supports cooking context, not a new building. |
| Oat flatbread had a known standardized shelf life. | No period-specific measurement identified. | Low | Preservation duration must be a balance transformation. |
| Porridge was universally a low-status or medical food. | Sources show varied contexts and prescriptive associations [1]. | Rejected | No class, illness, or child restriction. |
| Modern Irish oatcake practice directly reproduces early medieval recipes. | Later folklife evidence only [7]. | Low | Prohibited continuity claim. |

## Primary and Secondary Reference Assessment

### Primary Evidence and Its Limits

- Early law tracts name cereals, household equipment, food obligations, and social
  expectations. They are normative texts, not neutral household surveys or recipe
  books. This brief relies on specialist editions and syntheses rather than claiming
  an independent translation [1, 3, 4].
- Archaeobotanical remains securely establish crop presence and relative importance,
  but usually cannot identify a soft porridge or exact bread recipe [2].
- Querns, hearths, and described baking equipment establish processing capability;
  they do not reveal serving size, taste, or shelf life [1].

### Secondary Evidence

- EMAP Report 4.2 synthesizes settlement archaeology and early documentary food
  evidence at the appropriate period and scale [1].
- EMAP Report 5.1 provides the stronger quantitative crop baseline and explicitly
  discusses breads, porridges, and gruels [2].
- Sexton's peer-reviewed chapter is the specialist food-history reference used by
  both reports [3].
- Kelly's study is a major scholarly synthesis and edition-based analysis of early
  Irish law texts [4]. It was not directly inspected beyond bibliographic and
  secondary citations during this sprint.
- Modern dictionaries and later folklife sources inform terminology and visual
  caution only [5-7].

## Uncertainty and Contestation

- Soft foods and ordinary breads preserve poorly, producing an evidence imbalance
  between crops/equipment and finished dishes.
- `Littiu` is a historical porridge term, but assigning it one exact oat recipe would
  overstate the evidence.
- The exact liquid, cereal proportions, enrichment, texture, and serving size of
  porridge varied or remain unknown.
- Flatbread ingredients and forms varied; `oat flatbread` compresses that variety.
- Sources describe social and monastic contexts unevenly and may not represent every
  household.
- The historical evidence does not quantify spoilage or prove that an oat flatbread
  outlasted another cooked meal by a specific number of days.
- Modern `oatcake` can imply a biscuit, cracker, sweet cake, or regional later form.
  `Oat flatbread` is historically safer but less concise.
- Gameplay needs two distinct foods; history alone does not require two ThingDefs.

These uncertainties are non-blocking only if descriptions stay broad and balance
claims are labeled as RimWorld transformations.

## Cultural Sensitivities and Misconceptions

Do not:

- present oats as the only food of early medieval Ireland;
- turn ordinary cereal food into a poverty joke or negative cultural trait;
- map prescriptive cereal rank directly onto pawn social class;
- imply that women, enslaved people, children, sick people, or monks define the only
  legitimate consumers because particular sources associate them with preparation or
  use;
- call the food primitive, timeless, uniquely Irish, or unchanged into modernity;
- use famine-era equipment, cottages, or imagery as medieval reconstruction;
- add green coloring, shamrocks, knotwork, or decorative Irish words as authenticity;
- claim modern nutrition or health effects.

The appropriate transformation is modest domestic food with clear colony-management
roles.

## Language and Naming

### Recommended English Working Names

- `oat porridge`
- `oat flatbread`

These names describe function immediately and avoid requiring Irish knowledge.
`Oatcake` is a reasonable shorter alternative, but it risks implying a modern sweet
cake or a specific later recipe. Human review should choose between clarity and
brevity before specification.

### Irish Reference Terms

Foras na Gaeilge's modern dictionaries record `min choirce` for oatmeal,
`brachán (mine) coirce` for oatmeal porridge, and `arán coirce` for oaten bread [5,
6]. These modern dictionary forms do not prove early medieval labels. Any Irish
localization requires competent language review and should follow the project's
normal translation workflow.

`Littiu` may remain in research notes as a historical term. It should not become the
default player-facing label without linguistic and contextual review.

## Images and Visual References

No source image is copied into the repository during research.

Useful references for later original art include:

- EMAP Report 4.2's domestic-hearth, cooking-equipment, and settlement context [1];
- UCD's experimental early medieval roundhouse and hearth as environmental context,
  clearly labeled as reconstruction [10];
- National Museum of Ireland folklife images of oatcake and griddle equipment only as
  later comparative material, never as medieval reconstruction [7].

The porridge icon should read as a prepared bowl or portion of coarse cereal food.
The flatbread icon should read as a thin, plain, ready-to-eat bread rather than wheat
loaf, modern cracker packet, or sweet cake. Both require original art and separate
license/provenance records.

## RimWorld Vanilla Comparison

Verified RimWorld `1.6.4871 rev595` Core data provides these baselines [8]:

- a simple meal uses 0.5 raw-food nutrition, produces 0.9 nutrition, takes 300 work,
  has simple-meal preferability, and rots after 4 days;
- pemmican uses plant and meat nutrition, takes 700 work, is eaten in small units,
  and rots after 70 days;
- packaged survival meals require plant and protein ingredients, Cooking 8 and
  research, consume more input nutrition than their output, and never rot;
- the campfire provides simple meals and pemmican at half work speed;
- fueled and electric stoves provide the wider Core meal set;
- Core recipes, food items, rot, ingredient history, food poisoning, stack behavior,
  bills, and cooking buildings are XML-defined;
- Core has no generic porridge, bread, oat-food, or flour system.

Biotech baby food is a useful technical comparison, not a target. It demonstrates a
stackable plant-based mash with specific age and mood behavior, but Version 0.1 must
not depend on Biotech or copy its child-specific purpose [8].

### Intended Vanilla Relationships

| Food path | Intended role | Must not replace |
|---|---|---|
| Raw oats in ordinary Core food paths | Flexible unprocessed reserve | Rice, corn, potatoes, or hay |
| Oat porridge | Fresh simple-tier food with low final-cook burden after prior milling | General simple meals |
| Oat flatbread | Plant-only, ready-to-eat, moderately keeping travel/reserve food | Pemmican or packaged survival meals |
| Pemmican | Long-keeping plant-and-meat travel food | Remains substantially better preserved |
| Packaged survival meal | Researched, skilled, non-rotting travel food | Remains the premium preservation option |

The complete crop-to-food lifecycle must be compared, not just the final cooking
bill. Milling work, hauling, storage, cooking, spoilage, input flexibility, and
research access all count.

## Existing Mod Comparison

### Vanilla Cooking Expanded

Vanilla Cooking Expanded offers large bakes, flour, soup, condiments, cheese, and
other systems through a framework dependency [9]. Its workshop description stresses
simple, intuitive mechanics and explicitly prioritizes gameplay over realism. It is
evidence that players understand flour, bakes, and soup concepts, but it also shows
how quickly cooking scope expands.

Emerald Isle should not reproduce that framework, patch its foods, or assume
interchangeability. The Version 0.1 pair must work independently and remain limited
to one crop chain.

### Medieval Overhaul

Medieval Overhaul is a broad medieval/tribal overhaul with framework dependencies,
many content domains, and explicit compatibility effects [11]. Its scale and goals
are not comparable to one vanilla-friendly food pair. No definitions, recipes,
assets, or balance assumptions should be imported.

### Compatibility Lesson

Food mods frequently alter filters, categories, ingredient histories, meal thoughts,
and stock-count behavior. The proposed foods need stable namespaced IDs, narrow
ingredient filters, normal Core parent behavior where appropriate, and an explicit
compatibility sample. They must not advertise universal flour or food compatibility.

## Gameplay Validation

Gameplay is evaluated independently from historical support.

### What Meaningful Player Decision Do the Foods Create?

The intended decision is how to use a processed oat reserve:

- cook porridge for near-term colony meals when final cooking time matters; or
- invest more work in flatbread for a ready reserve and caravan food that keeps
  longer than a fresh meal, but not as long as dedicated preserved foods.

The player can also leave oats raw for flexibility and ordinary Core food paths.
This produces a three-way allocation decision rather than a mandatory upgrade.

### What Gameplay Problem Do They Solve?

Together they provide the missing payoff for the oat-and-quern chain. Porridge can
move some labor out of the final cooking bottleneck because the grain was prepared
earlier. Flatbread can provide a low-tech, plant-only travel/reserve option without
requiring meat or advanced packaging.

Neither solves a problem alone if it merely copies a simple meal. Their value comes
from contrasting time horizons and labor profiles.

### What New Stories Do They Enable?

- a holding mills grain during a quiet period, then rapidly cooks fresh meals during
  a harvest, raid recovery, or labor shortage;
- a caravan departure turns part of the prepared reserve into flatbread while the
  colony keeps porridge ingredients at home;
- poor scheduling leaves fresh porridge spoiling while durable food was neglected;
- a meat shortage makes plant-only flatbread useful, but the colony pays additional
  work and accepts weaker preservation than pemmican;
- damage to the quern interrupts both specialty foods while raw oats remain usable.

These stories use existing bills, spoilage, labor, caravans, and emergencies rather
than custom events.

### What Would Players Lose If the Foods Did Not Exist?

Without distinct foods, players lose the visible conclusion of the oat-processing
chain and the fresh-versus-portable allocation choice. Oats could still function in
ordinary meals, so the crop remains viable. The hand quern and milled-oats item would,
however, lose most of their gameplay justification.

The omission cost is meaningful for the approved mini-expansion but not sufficient
to preserve weak food design. If the pair fails playtesting, the correct response is
to simplify the chain.

### Do They Add Strategy or Simply Additional Clicks?

Standard RimWorld bills can automate both foods. Strategy comes from setting target
stocks and choosing where limited milled oats and labor go. The design fails if the
optimal policy is always to mill every oat and produce one food indefinitely.

Two food bills, two stockpile targets, and two icons are the maximum acceptable
surface for Version 0.1. Bulk duplicates, enrichment variants, quality levels, and
ingredient toggles would add management without enough new decisions.

### Do They Create Meaningful Tradeoffs or Compulsory Labor?

The proposed tradeoffs are:

- **porridge:** low final-cooking burden and immediate food, paid for by prior milling,
  separate hauling, short shelf life, and narrow ingredient flexibility;
- **flatbread:** portability and moderate keeping, paid for by prior milling, more
  total work, narrow ingredients, and preservation clearly below pemmican and
  packaged survival meals;
- **raw oats:** maximum flexibility and no milling labor, but no specialty-food role.

Milling becomes compulsory if either food is a straight upgrade over Core meals or if
raw oats are artificially made useless. The complete chain must keep all three paths
credible.

### Could the Same Gameplay Be Achieved More Simply?

Partly. One direct raw-oat flatbread recipe could create a portable food with fewer
items and bills. Ordinary simple meals could stand in for porridge. That alternative
is preferable if labor staging cannot be made legible or if the two foods converge in
practice.

The two-food chain earns its extra surface by combining a cook-throughput choice with
a preservation choice and by giving the hand quern multiple downstream uses.

### Does the Added Complexity Justify Itself?

Provisionally, yes. Two XML foods, two narrow recipes, and two icons complete a
coherent crop-to-meal loop and establish reusable food, recipe, rot, caravan, and
ingredient-filter testing patterns. No new system or code is required.

The justification depends on measurable differentiation. Theme, historical presence,
and visual novelty are not enough.

**Gameplay recommendation: Recommended with Conditions**

**Conditions:**

1. Version 0.1 contains exactly two oat foods: porridge and one flatbread form.
2. Both remain simple-tier foods with no inherent mood, health, medical, child,
   ideology, quality, or ritual bonus.
3. Porridge has a lower final-cooking burden than a Core simple meal only because
   milling has already occurred. Milling must be independently schedulable rather
   than consume the same skilled-cook bottleneck; complete-chain work must be equal
   or greater, and spoilage must keep porridge a near-term food.
4. Flatbread provides moderate ready-food keeping and portability, paid for by more
   complete-chain work and/or nutrition loss; it must remain substantially less
   preserved than pemmican and packaged survival meals.
5. Raw oats retain useful ordinary Core food or feed behavior and are not deliberately
   weakened to force milling.
6. Raw oats to milled oats to food conserves nutrition across the complete chain
   except for explicit, bounded preservation losses; no count rounding or market
   value loop may create free output.
7. Recipes require milled oats only. Water and ordinary utensils are abstracted; no
   milk, honey, salt, container, griddle, or new building becomes mandatory.
8. Foods use standard Core bills and supported cooking buildings. No custom C#,
   Harmony, custom UI, or custom thought is permitted.
9. The specification must test the direct-recipe alternative. If the pair cannot
   demonstrate separate player behavior in XML, reduce to one food or ordinary meals
   and remove the redundant milling content through governed scope reconciliation.
10. Final English names and descriptions must state the abstraction without claiming
    a standardized historical recipe or measured historical shelf life.

## Gameplay Opportunities

### Supported Opportunities

- fresh-versus-portable allocation from one processed ingredient;
- cook-bottleneck planning through prior milling;
- plant-only caravan food with bounded preservation;
- low-tech cooking at existing Core campfires and stoves, subject to specification;
- visible oat identity without custom systems;
- reusable XML patterns for meal items, stackable travel food, recipe filters, rot,
  caravans, and ingredient provenance.

### Opportunities to Reject for Version 0.1

- sweet, luxury, fine, lavish, festive, ritual, or ideology-specific oat foods;
- milk porridge, honey porridge, flavored breads, or ingredient variants;
- baby or invalid dietary mechanics;
- medicinal, comfort-food, temperature, or weather bonuses;
- food quality, fermentation, stale states, reheating, bowls, containers, or utensils;
- a generic bread, dough, water, flour, or baking framework;
- automatic cross-mod ingredient substitution.

## Balance Considerations

### Balance Hypotheses

**Porridge hypothesis:** independently scheduled prior milling can reduce the final
bill's skilled-cooking time while the complete chain costs at least as much labor as
a simple meal. Shorter freshness and oat-only input prevent it from replacing general
meals. If milling consumes the same constrained cook labor, this hypothesis weakens
and must be retested against direct cooking.

**Flatbread hypothesis:** additional work can buy moderate ready-food shelf life and
plant-only convenience. Preservation, nutrition efficiency, skill, and research
access remain below Core's dedicated travel foods when their full lifecycles are
compared.

### Required Comparative Model

The future specification must model best, typical, and poor conditions for:

- raw oats eaten or used in ordinary meals;
- Core simple meals;
- oat porridge after milling;
- oat flatbread after milling;
- pemmican;
- packaged survival meals;
- caravan days of food per unit input and carried mass;
- refrigerated and unrefrigerated colony storage;
- one-colonist and larger-colony cooking throughput.

### Preliminary Boundaries

- no food grants a mood thought above simple-meal equivalence;
- total nutrition cannot increase merely because two jobs replace one;
- porridge must spoil no later than the role requires and cannot become reserve food;
- flatbread shelf life cannot approach pemmican's 70 days or non-rotting survival
  meals without much stronger cost and historical/gameplay justification;
- flatbread cannot be both more nutrition-efficient and better preserved than a
  simple meal;
- market value must not make food conversion a risk-free profit engine;
- work savings at the stove must be paid earlier at the quern;
- raw oats cannot be excluded from all Core food systems merely to force the chain.

### Abuse and Failure Cases

- nutrition multiplies through raw, milled, and cooked item-count rounding;
- porridge's short final bill makes it strictly better despite hidden milling work;
- flatbread replaces pemmican because it needs no meat and keeps nearly as long;
- pawns prefer one food universally and erase the intended choice;
- caravans carry flatbread as an unbounded mass- or nutrition-efficient ration;
- standard meal bills consume milled oats or finished foods unintentionally;
- ingredient provenance prevents stacking or causes stock-count confusion;
- food restrictions, ideology, babies, prisoners, animals, or paste systems select an
  unintended item;
- two recipe variants become bill-list clutter on every cooking building.

## Technical Implementation Considerations

### Expected XML Surface

Research supports, but does not authorize:

- one namespaced porridge `ThingDef` and one narrow recipe;
- one namespaced flatbread `ThingDef` and one narrow recipe;
- explicit addition of the recipes to selected existing Core cooking buildings;
- standard nutrition, ingestibility, rot, deterioration, mass, stack, value, food
  poisoning, ingredient-history, and caravan behavior;
- two original item graphics and localization keys.

No new worktable, component, job driver, WorkGiver, thought worker, map component,
ticker, database, or serialized custom state is indicated.

### Recipe and Item Shape

Porridge likely fits the Core meal pattern, while flatbread may fit the small-unit
stack pattern used by pemmican. These are hypotheses, not approved definitions. The
specification must verify:

- exact parent Defs and inherited DLC-sensitive components;
- food type and preferability;
- whether each item records ingredients and stacks correctly;
- bill target counting and bulk behavior;
- food poisoning and cooking-skill behavior;
- caravan auto-selection and days-of-food calculations;
- rot, deterioration, storage categories, and pawn selection;
- narrow acceptance of milled oats without accidental Core meal consumption.

### Cooking Buildings

Core campfires list simple meals, pemmican, and optional Biotech baby food, while
fueled and electric stoves list the broader meal set [8]. XML can add recipes to
existing lists. The specification must decide whether both oat foods belong on the
campfire and both stoves, or whether the flatbread's production access needs a
different constraint.

No new hearth or griddle should be introduced merely to mirror historical equipment.

### XML vs C# Recommendation

**Recommendation: XML only.**

Core already expresses all required item and bill behavior declaratively. C# would be
justified only by a newly demonstrated player requirement that stable XML cannot
express. No such requirement exists. Harmony remains prohibited by frozen scope and
would require a separate ADR and approval.

### DLC Policy

- **Required:** RimWorld 1.6 Core.
- **Royalty:** No dependency or enhancement identified.
- **Ideology:** Verify vegetarian/food-precept classification, ingredient history,
  and food restrictions; Core behavior must remain correct without Ideology.
- **Biotech:** Verify baby and child selection. The porridge is not baby food and must
  not require Biotech.
- **Anomaly:** Verify inherited food infection and meal behavior without introducing
  a hard dependency.
- **Odyssey:** Verify caravan/travel selection and any supported environmental food
  behavior; no dependency identified.
- **Absent DLC behavior:** Both foods and recipes must remain complete and safe with
  Core only.

### Save and Removal Considerations

Released food Def names become save contracts for maps, inventories, caravans,
stockpile filters, bills, policies, and trade. Names must be stable and namespaced.
Removal and upgrade tests must cover existing stacks, suspended bills, food
restrictions, and saves with or without supported DLC.

### Performance

Two passive food items and two ordinary bills have negligible inherent runtime cost.
The meaningful risks are broad ingredient filters, repeated bill scans, excessive
small-stack hauling, and ingredient-history fragmentation. Narrow filters, reasonable
stacking, and standard Core behavior should remain within the performance budget.

### Art and Localization

Art effort is low-to-medium: two original, readable food icons with clear silhouettes
at normal RimWorld zoom. Porridge and flatbread must remain distinguishable from
baby food, simple meals, pemmican, packaged survival meals, raw oats, and milled oats.

English is the source language. Descriptions must explain fresh versus portable roles
without claims of health, authenticity, or exact historical shelf life. Irish
localization requires competent review.

## Risks

| Risk | Likelihood | Impact | Research response |
|---|---:|---:|---|
| Foods duplicate simple meals | Medium | High | Require separate observed roles or simplify. |
| Flatbread replaces pemmican | Medium | High | Cap preservation and charge complete-chain costs. |
| Porridge hides a superior labor conversion | Medium | High | Compare total quern-plus-cook work. |
| Historical recipes are overstated | Medium | High | Use broad names and explicit uncertainty. |
| Two foods fail to justify milling | Medium | High | Preserve direct-cooking fallback and omission rule. |
| Nutrition/value rounding creates output | Medium | High | Model every transformation and count. |
| Bill and stockpile clutter | Medium | Medium | Exactly two foods; no bulk/variant proliferation by default. |
| DLC food selection behaves unexpectedly | Medium | Medium | Test Core and official DLC matrix. |
| Other food mods alter filters or stack behavior | Medium | Medium | Namespace, narrow filters, compatibility sample. |
| Art resembles modern packaged or famine-era food | Low | Medium | Original art and period-aware review. |
| Later terms are presented as medieval Irish | Medium | Medium | English labels; language caveat and review. |

## Open Questions

### Questions Requiring Human Review

1. Approve the two-food direction: oat porridge and oat flatbread?
2. Approve the gameplay recommendation with all ten conditions?
3. Prefer the clearer English label `oat flatbread`, or the shorter `oatcake`?
4. Confirm the fallback: if testing cannot preserve distinct roles in XML, simplify
   the foods and reconcile removal of redundant milling content rather than adding a
   custom system?

### Questions for Specification and Testing

1. What work type, skill, and complete-chain budget make prior milling independently
   schedulable and distinguish porridge from a simple meal?
2. What shelf-life interval makes flatbread useful without approaching pemmican?
3. Should flatbread use meal-sized units or a small stack like pemmican?
4. Which cooking buildings receive each recipe?
5. Should either recipe have a bulk form, or would that exceed Version 0.1's bill
   budget?
6. How do item counts conserve nutrition through raw, milled, and finished states?
7. Which food categories and parent Defs produce correct Core/DLC selection behavior?
8. How do caravans, prisoners, animals, babies, food policies, ingredient history,
   paste, and trade treat both foods?
9. Can players understand each niche from labels, descriptions, stats, and bills?
10. Do playtesters vary production targets, or converge on one mandatory chain?

## ADR Assessment

No new ADR is required at this research stage. Two oat foods are already permitted by
the canonical Version 0.1 scope, and the proposed implementation remains XML-only.

An ADR and scope approval would be required for custom C#, Harmony, a new cooking
building, a generic food framework, a third food, mandatory new resources, custom
thoughts, or another significant departure from the frozen scope. Naming and exact
balance do not require an ADR unless they change a baseline architectural contract.

## Preliminary Recommendation

Advance both **oat porridge** and **oat flatbread** to human research review.

Historically, the pair is well supported at the level appropriate for a transformed
RimWorld feature: oats were a common crop, early sources describe oat use in pot foods
and flatbreads, and domestic milling and cooking equipment are documented. Exact
recipes and preservation are not known and must not be claimed.

For gameplay, retain both only as a fresh-versus-portable pair. Porridge should reward
prior preparation with low final-cook burden and short life. Flatbread should provide
moderate plant-only travel convenience at a larger complete-chain cost and remain
well below dedicated preserved foods. Raw oats remain useful. If XML balance cannot
produce those behaviors, simplify rather than add systems.

## Research Review

### Summary

The evidence supports one pot-based oat food and one oat flatbread without requiring
a detailed historical simulation. The two foods can also satisfy the outstanding
gameplay conditions on milled oats and the hand quern by creating distinct downstream
uses. Their retention depends on complete-chain balance and visible player behavior,
not authenticity alone.

### Recommended Gameplay Implementation

A two-food choice from milled oats:

- fresh, simple-tier porridge with low final-cook burden and short storage life; and
- simple-tier oat flatbread with more total work and moderate portable-food life.

No bonuses, quality, enrichment, new buildings, or custom systems.

### Recommended Version 0.1 Implementation

Conditionally retain exactly two XML-only foods using existing Core cooking
infrastructure and narrow milled-oat recipes. Use original art and stable namespaced
IDs. Validate total labor, nutrition, spoilage, caravan value, Core/DLC selection, and
the simpler direct-recipe alternative during specification and playtesting.

### Questions Requiring Human Review

- Approve or reject the two-food direction.
- Approve, amend, or reject the ten gameplay conditions.
- Select the English flatbread label.
- Confirm the simplification fallback.

### Historical Review Gate

**Decision:** Pending

**Reviewer/date:** Unassigned

**Corrections or conditions:** Human review required.

**Proposed approved claims and uses:** Early medieval Irish evidence supports
pot-based oat food and oat flatbread as broad forms; exact recipes, universal use,
terminology, and shelf life remain unclaimed.

### Gameplay Review Gate

**Decision:** Pending

**Reviewer/date:** Unassigned

**Corrections or conditions:** Human review required.

**Proposed approved gameplay direction:** `Recommended with Conditions`; retain a
fresh porridge and portable flatbread only while their complete-chain tradeoffs remain
distinct, XML-only, and subordinate to relevant vanilla alternatives.

### Research Definition of Ready Checklist

This checklist records readiness to leave research, not readiness to implement.

#### Product and Identity

- [x] Research ID, frozen scope, period, geography, and domestic focus are explicit.
- [x] Constitution, Design Bible, approved scope, and previous research conditions are
  applied.
- [x] Exactly two candidate foods and explicit exclusions prevent cuisine expansion.
- [x] Intended player experience and simplification fallback are stated.
- [ ] Human reviewer approves the transformed food direction and names.

#### Evidence and Historical Review

- [x] Historical background, cultural significance, geography, period, production,
  and materials are documented.
- [x] Archaeological, documentary, scholarly, linguistic, and later folklife evidence
  are distinguished.
- [x] Porridge and flatbread claims carry separate confidence assessments.
- [x] Recipe, terminology, preservation, social, and continuity uncertainties are
  explicit.
- [x] Sources, visual references, cultural risks, and prohibited claims are recorded.
- [ ] Historical review gate is approved by a human reviewer.

#### Gameplay Review

- [x] Meaningful decision, problem, stories, omission cost, and player behavior are
  explicit.
- [x] Strategy, clicks, tradeoffs, compulsory labor, and simpler alternatives are
  evaluated.
- [x] The fresh-versus-portable model and ten retention conditions are recorded.
- [x] Raw oats, simple meals, pemmican, and packaged survival meals are compared.
- [x] Complete-chain nutrition, labor, spoilage, value, and abuse cases are assigned
  to specification and testing.
- [ ] Gameplay review gate is approved or approved with conditions by a human reviewer.

#### Engineering

- [x] XML-only feasibility is supported by verified RimWorld 1.6 Core patterns.
- [x] No C#, Harmony, new building, custom UI, thought, ticker, or serialized custom
  state is justified.
- [x] Core plus all officially supported DLC receive explicit review requirements.
- [x] Save, performance, art, localization, ingredient, bill, caravan, and
  compatibility risks are bounded.
- [x] ADR assessment is recorded.

#### Delivery and Dependencies

- [x] The foods explicitly validate conditions from Hand Quern and Milled Oats.
- [x] Specification and playtest questions are actionable without setting final Def
  values.
- [x] Source and asset provenance requirements are recorded.
- [x] No specification, implementation, XML, C#, or texture was created.
- [ ] Human questions are resolved and approvals recorded.

**Research decision:** Review required
**Project Definition of Ready:** Not evaluated. Human approval, the Version 0.1
Readiness Review, specification, planning, and implementation authorization remain
outstanding.

## Sources

Accessed 2026-07-05 unless otherwise stated.

1. Aidan O'Sullivan, Finbar McCormick, Thomas Kerr, Lorcan Harney, and Jonathan
   Kinsella, *Early Medieval Dwellings and Settlements in Ireland, AD 400-1100*,
   EMAP Report 4.2 (2010), especially printed pp. 100-103.
   [UCD repository record](https://researchrepository.ucd.ie/entities/publication/8ec7329a-4fd5-4555-a3b4-e0c2d6530b1f) |
   [report PDF](https://researchrepository.ucd.ie/server/api/core/bitstreams/b3b9204f-cda6-45ce-a13a-cb83c5d06cc6/content).
   Source type: archaeological and documentary synthesis; not peer reviewed in report
   form. A revised book edition was published by Archaeopress in 2014.
2. Finbar McCormick, Thomas Kerr, Meriel McClatchie, and Aidan O'Sullivan,
   *The Archaeology of Livestock and Cereal Production in Early Medieval Ireland,
   AD 400-1100*, EMAP Report 5.1 (2011), especially printed pp. 45-54.
   [UCD repository record](https://researchrepository.ucd.ie/entities/publication/172fb4d4-9100-4788-b615-169f391da57f) |
   [report PDF](https://researchrepository.ucd.ie/server/api/core/bitstreams/163e8ed5-382c-4c50-962f-590c684a7244/content).
   Source type: quantitative archaeological synthesis with documentary comparison;
   strongest crop baseline.
3. Regina Sexton, “Porridges, Gruels, and Breads: The Cereal Foodstuffs of Early
   Historic Ireland,” in Michael A. Monk and John Sheehan, eds., *Early Medieval
   Munster: Archaeology, History and Society* (Cork: Cork University Press, 1998),
   76-86. [University College Cork record](https://iris.ucc.ie/live/%21W_VA_PUBLICATION.POPUP?LAYOUT=N&OBJECT_ID=272247064).
   Source type: peer-reviewed specialist chapter. Bibliography and secondary use were
   verified; full text was not directly inspected.
4. Fergus Kelly, *Early Irish Farming: A Study Based Mainly on the Law-Texts of the
   7th and 8th Centuries AD* (Dublin: School of Celtic Studies, Dublin Institute for
   Advanced Studies, 1997), especially pages cited by [1] and [2].
   [National Library of Ireland catalogue](https://catalogue.nli.ie/Record/vtls000039584/HoldingsILS).
   Source type: scholarly study and edition-based analysis. The book was not directly
   inspected during this sprint; claims rely on the contextualized citations in EMAP.
5. Foras na Gaeilge, “coirce,” *Foclóir Gaeilge-Béarla*, Teanglann.
   [dictionary entry](https://www.teanglann.ie/en/fgb/coirce).
   Source type: official modern language reference; not evidence of medieval wording.
6. Foras na Gaeilge, “brachán,” *Foclóir Gaeilge-Béarla*, Teanglann.
   [dictionary entry](https://www.teanglann.ie/en/fgb/Brach%C3%A1n).
   Source type: official modern language reference; not evidence of medieval wording.
7. National Museum of Ireland, “Feeding the Family,” Irish Folklife Collection.
   [collection page](https://www.museum.ie/en-ie/collections-research/folklife-collections/folklife-collections-list-%281%29/other/hearth-home/activities-in-the-home/feeding-the-family).
   Source type: nineteenth- and twentieth-century folklife and visual comparison;
   explicitly excluded as direct early medieval evidence.
8. Ludeon Studios, locally installed RimWorld `1.6.4871 rev595` Core and Biotech data,
   `Data/Core/Defs/ThingDefs_Items/Items_Food.xml`,
   `Data/Core/Defs/RecipeDefs/Recipes_Meals.xml`,
   `Data/Core/Defs/RecipeDefs/Recipes_Food.xml`,
   `Data/Core/Defs/ThingDefs_Buildings/Buildings_Production.xml`,
   `Data/Core/Defs/ThingDefs_Buildings/Buildings_Temperature.xml`, and
   `Data/Biotech/Defs/ThingDefs_Items/Items_Food.xml`, inspected 2026-07-05.
   Source type: proprietary current technical reference; behavior and values are
   paraphrased, and no XML is copied into the project.
9. Sarg Bjornson and Vanilla Expanded team, *Vanilla Cooking Expanded*, Steam
   Workshop item 2134308519.
   [Workshop page](https://steamcommunity.com/sharedfiles/filedetails/?id=2134308519).
   Source type: current adjacent mod comparison; definitions, code, frameworks,
   balance, and assets were not reused.
10. University College Dublin, “UCD Archaeology builds new early Medieval roundhouse
    after arson fire,” 9 February 2022.
    [UCD article](https://www.ucd.ie/newsandopinion/news/2022/february/09/ucdarchaeologybuildsnewearlymedievalroundhouseafterarsonfire/).
    Source type: experimental-reconstruction context and visual reference, not a
    direct food reconstruction.
11. Medieval Overhaul team, *Medieval Overhaul*, Steam Workshop item 3219596926.
    [Workshop page](https://steamcommunity.com/sharedfiles/filedetails/?id=3219596926).
    Source type: broad adjacent overhaul comparison; definitions, dependencies,
    code, balance, and assets were not reused.

## Source and Asset Notes

- Period-specific food claims rely primarily on [1]-[4], with limitations stated.
- Archaeology supports crops and equipment more strongly than exact finished foods.
- Modern language sources [5] and [6] do not establish medieval names.
- Later folklife [7] is included to prevent, not encourage, chronological collapse.
- Source [8] establishes technical patterns and vanilla baselines, not approval.
- Existing mods [9] and [11] are comparisons only.
- No source image, XML, code, Def name, recipe, balance value, translation, texture,
  audio, or other asset was copied.
- No gameplay specification or implementation was created.
