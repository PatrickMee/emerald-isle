# FS-001 — Oats

**Status:** Approved — Frozen<br>
**Specification gate:** Approved by Patrick Mee, 2026-07-05<br>
**Milestone:** Version 0.1 — The First Holding<br>
**Catalog feature:** PL-01<br>
**Feature branch:** `003-oats-specification`<br>
**Owner:** Patrick Mee<br>
**Created:** 2026-07-05<br>
**Vanilla balance baseline:** RimWorld 1.6.4871 rev595<br>
**Specification QA:** [Passed](checklists/FS-001-oats-requirements.md)<br>
**Feature Acceptance:** [Accept for planning](checklists/FS-001-oats-feature-acceptance.md)<br>
**Architecture gate:** AR-001 and IP-001 approved by Patrick Mee, 2026-07-05<br>
**Definition of Ready:** Passed by Patrick Mee, 2026-07-05<br>
**Implementation authorized:** Yes — Patrick Mee, 2026-07-05
**Implementation status:** Feature implementation and Design Review approved by
Patrick Mee, 2026-07-05
**Gate 2 (Done):** Passed — maintainer in-game playtest of the complete player
path by Patrick Mee, 2026-07-07. Whole-chain balance is bounded by the
not-yet-implemented hand-quern and milled-oats features and will be evaluated
with those features; version 0.1 release smoke tests belong to Gate 3.

## Authority and Boundaries

This specification defines what the Oats feature must do. It conforms to the
[Version 0.1 approved scope](../product/version-0.1-approved-scope.md),
[Version 1.0 Vision](../product/version-1.0-vision.md),
[Oats research brief](../research/version-0.1/oats.md), and
[ADR-0001](../adr/0001-oats-medium-cycle-xml.md).

It deliberately contains no source markup, code, Harmony patch, public runtime
identifier, file layout, inheritance choice, or implementation sequence. Those
belong to implementation planning after this specification and the project gates
are approved.

## Purpose

### Historical Purpose

Oats anchor Version 0.1 in the ordinary agricultural life of an early medieval
Irish-inspired holding. Archaeobotanical evidence supports oats as a widespread and
important cereal in Ireland during approximately AD 400–1100, with meaningful
regional, chronological, preservation, and species-identification limits documented
in the research brief.

The feature represents a transformed Rim crop, not a literal reconstruction of one
historical cultivar or a claim that oats were uniquely or uniformly Irish.

### Gameplay Purpose

Oats provide a medium-cycle field grain between the frequent harvests of rice and
the slow, large harvests of corn. They trade slightly lower gross output and normal
soil dependence for an intermediate harvest window, lower field-work frequency than
rice or potatoes, and moderate shelf life.

They also establish the raw input for the approved but separately specified milling
and oat-food chain. Oats remain useful through vanilla food and animal systems, so
future processing must justify itself through a meaningful choice rather than an
artificial prohibition.

### Intended Player Experience

The player chooses oats when a colony can wait longer than a rice cycle but does not
want corn's long exposure to blight, fire, cold snaps, or an interrupted growing
season. The larger, less frequent harvest reduces repeated field work while creating
a more consequential batch to haul and protect.

The choice should feel familiar: select a crop, sow it, manage normal plant threats,
harvest it, and decide whether the grain is eaten, cooked, fed to animals, traded,
stored, or later processed. The feature must not require a new farming system or
historical knowledge.

### Why This Feature Exists

Oats are the smallest feature that connects Emerald Isle's historical identity to a
visible RimWorld decision. They prove the project can turn research into a balanced,
vanilla-fluent crop while establishing a reusable crop/resource contract for the
rest of Version 0.1.

## Gameplay Design

### Crop Lifecycle

1. Oats are available from the start without research and may be sown by any pawn
   permitted to perform ordinary crop work.
2. They may be planted on ground with at least 70% fertility. They may not be planted
   in hydroponic basins.
3. They use the normal cultivated-plant rules for light, temperature, resting,
   fertility, blight, fire, damage, grazing, failed harvests, and seasonal loss.
   They receive no special cold, wet-weather, disease, or poor-soil protection.
4. Under 100% growth conditions, a crop reaches maturity in 8.0 days.
5. A fully mature plant has a base harvest of 15 units of raw oats before pawn,
   difficulty, or health modifiers.
6. Harvest produces only raw oats. There is no straw, seed, chaff, or secondary
   product.
7. Raw oats use normal food storage, cooking, eating, animal-diet, caravan, trade,
   deterioration, and rot behavior.

Oats do not appear as a wild plant and do not require a biome, world-generation, or
weather rule.

### Gameplay Niche

Oats are a **medium-cycle processing grain** whose immediate crop niche is harvest
cadence and field labor:

- rice provides the quickest food response but demands frequent re-sowing and
  harvesting;
- potatoes remain the strongest comparison on poor soil and retain hydroponic use;
- corn provides a larger, slower batch with better shelf life and lower field work
  per nutrition;
- oats provide a middle harvest window, moderate storage, and an input for optional
  later processing.

Oats are not a hardy crop. Their fertility response matches normal fertility-sensitive
grains, and they gain no custom temperature or weather advantage.

### Player Decisions

- **Timing versus exposure:** harvest sooner than corn, or wait for corn's larger and
  more efficient batch.
- **Field work versus responsiveness:** accept a slower response than rice in return
  for fewer crop cycles and less repeated field work.
- **Soil allocation:** use good ordinary soil for oats, or reserve marginal soil and
  hydroponics for potatoes.
- **Use of the harvest:** eat or cook raw oats through normal systems, feed animals,
  trade or store the grain, or commit it to the separately approved processing chain.
- **Batch risk:** protect a moderate batch from fire, blight, temperature events,
  interruption, and spoilage rather than relying on rice's small frequent harvests
  or corn's large delayed harvest.

### Relationship to Future Processing

Raw oats must be eligible wherever comparable vanilla raw plant foods are accepted,
including ordinary meals and nutrient paste. They must also be directly edible with
the normal raw-food penalty. This fallback keeps the crop useful if processing is
temporarily unavailable and avoids forcing historical labor through compatibility
restrictions.

Future Hand Quern, Milled Oats, and Oat Foods specifications may consume raw oats and
offer distinct labor, scheduling, portability, or food-form choices. They may not
silently change this crop's lifecycle or make raw oats unusable. If processing cannot
earn its added labor while this vanilla-compatible fallback exists, the conditional
processing chain must be simplified as approved by research.

### Player Scenarios

#### P1 — Establish a Medium-Cycle Field Crop

**Given** a colony has ordinary fertile ground and can wait longer than a rice
harvest, **when** the player plants oats, **then** the colony receives a moderate
harvest before corn would mature while performing fewer repeated crop cycles than a
rice plan. This scenario independently proves the crop lifecycle and primary niche.

#### P1 — Use the Harvest Without Dedicated Processing

**Given** the future milling chain is unavailable, interrupted, or deliberately not
used, **when** the colony harvests oats, **then** the grain remains usable through
normal eating, cooking, nutrient-paste, animal-feed, storage, caravan, and trade
decisions. This scenario independently proves that FS-001 has player value and fails
safe on its own.

#### P2 — Prefer a Vanilla Crop When Its Strength Matters

**Given** marginal soil, hydroponic production, an urgent food shortage, or a plan
optimized for the largest efficient field batch, **when** the player compares crop
information, **then** potatoes, rice, or corn respectively remain the stronger
choice. This scenario independently proves that oats complement rather than replace
vanilla crops.

#### Edge and Failure Scenarios

- A cold snap, blight, fire, grazing animal, failed harvest, darkness, or loss of
  growing season affects oats through normal cultivated-crop rules.
- A save made with growing, damaged, blighted, stored, rotting, traded, or caravaned
  oats restores the same vanilla-persisted state after reload.
- Core-only play remains complete, and adding or removing a supported DLC neither
  removes nor duplicates oats.
- Another mod may add its own oats without Emerald Isle silently merging or replacing
  either feature.

## Balance Targets

All crop targets below are base values at full plant health and 100% growth
conditions, before pawn skill, difficulty, storyteller, biome, weather, or health
modifiers.

| Dimension | Proposed target | Design intent |
|---|---:|---|
| Growth time | 8.0 days | Clearly between potatoes and corn; enough time for a meaningful batch without corn's full exposure window |
| Mature harvest | 15 units | Produces 0.75 raw nutrition per mature tile and keeps gross output slightly below vanilla staple crops |
| Nutrition | 0.05 per harvested unit | Matches comparable vanilla raw crops; processing must not begin with inflated calories |
| Nominal nutrition rate | 0.09375 per tile per grow-day | Close enough to vanilla to remain viable, but lower than rice, potatoes, and corn at 100% fertility |
| Minimum fertility | 70% | Prevents a poor-soil niche and leaves marginal-ground strength to potatoes |
| Fertility sensitivity | 1.0 | Matches normal fertility-sensitive grains; explicitly rejects a “hardy oat” advantage |
| Sowing work | 170 base work | Uses the ordinary food-crop labor expectation; no hidden planting surcharge or discount |
| Harvest work | 200 base work | Keeps one oat cycle comparable to a vanilla crop cycle while cycle length determines labor frequency |
| Sowing skill | No minimum | Makes the first Version 0.1 crop accessible without adding progression |
| Market value | 1.1 per unit | Matches common raw crops and prevents cultural novelty from creating a trade premium |
| Raw food behavior | 0.05 nutrition, low raw-food preference, 2% fixed human food-poisoning chance | Preserves emergency use without competing with cooked food |
| Growing-plant nutrition | 0.30 at full growth | Allows normal grazing without making oat fields an exceptional animal-food source |
| Shelf life | 45 days unrefrigerated before rot begins | Longer than potatoes and rice, shorter than corn; useful seasonal storage without owning the preservation niche |
| Stack and mass | 75 units per stack; 0.03 mass per unit | Matches ordinary raw crops and avoids storage or caravan advantages unrelated to the design |
| Hydroponics | Not permitted | Keeps oats a field crop and preserves rice and potatoes as hydroponic options |
| Trade | Normal raw-food sale eligibility; no guaranteed trader stock or special price | Supports ordinary colony economy without adding distribution content |

### Vanilla Comparison

| Crop | Grow days | Yield | Nutrition per tile per grow-day | Fertility sensitivity | Hydroponics | Shelf life |
|---|---:|---:|---:|---:|---|---:|
| Rice | 3.0 | 6 | 0.10000 | 1.0 | Yes | 40 days |
| Potatoes | 5.8 | 11 | 0.09483 | 0.4 | Yes | 30 days |
| **Oats target** | **8.0** | **15** | **0.09375** | **1.0** | **No** | **45 days** |
| Corn | 11.3 | 22 | 0.09735 | 1.0 | No | 60 days |

The target creates these explicit tradeoffs:

- Against rice, oats are slower and unavailable in hydroponics, but require far
  fewer field cycles per unit of food and keep five days longer.
- Against potatoes, oats have nearly equal nominal output, lower field work per unit,
  and longer storage, but perform substantially worse on marginal soil and cannot use
  hydroponics.
- Against corn, oats recover food sooner and reduce the amount exposed in one long
  cycle, but produce less nutrition per day, require more recurring field work, and
  spoil sooner.

At 70% fertility, oats take the same proportional growth penalty as rice and corn;
potatoes remain materially better. On rich soil, oats improve normally but retain
their lower base output and ground-only constraint. No tested standard condition
should make oats best simultaneously in output, field labor, soil flexibility,
harvest speed, and storage.

## Integration

### Vanilla Agriculture

Oats use the normal growing-zone selection, sowing, growth inspection, harvest,
cutting, blight, fire, grazing, and plant-work behaviors. They require no research,
special terrain, new work type, or unique alert.

### Cooking

Raw oats are accepted by ordinary vanilla recipes and nutrient paste under the same
conditions as comparable raw plant food. They provide no special meal quality,
nutrition multiplier, mood effect, or food-poisoning protection. Dedicated oat foods
are outside FS-001.

### Animals

Animals able to consume plant-derived raw food may eat harvested oats. Animals able
to graze comparable cultivated plants may graze growing oats. Oats grant no
species-specific bonus, training effect, health effect, or feed efficiency bonus.

### Trade

Oats can be sold to traders that normally accept raw plant food. The feature does not
guarantee oat stock in trader inventories, add a special trader, or change faction
economies.

### Storage and Caravans

Oats use ordinary stockpile, shelf, caravan, hauling, deterioration, refrigeration,
freezing, and rot rules. Their 45-day shelf life and standard mass make them a
moderate stored grain, not a replacement for corn or preserved meals.

### DLC

**Required DLC:** None. RimWorld 1.6 Core is sufficient.

**Optional DLC enhancements:** None in FS-001.

| Configuration | Required behavior |
|---|---|
| Core only | Full feature is available |
| Royalty present or absent | No feature-specific change |
| Ideology present or absent | Oats follow existing food and plant rules; no new precept, meme, or preference |
| Biotech present or absent | Oats follow normal cultivated-plant interactions; no gene, xenotype, pollution, or mech enhancement |
| Anomaly present or absent | No feature-specific change |
| Odyssey present or absent | No feature-specific biome, vacuum, travel, or settlement behavior |
| All supported DLC | The Core behavior and balance targets remain unchanged |

### Future Milling

Oats expose one stable harvested input to later Version 0.1 specifications. FS-001
does not add a mill, processing job, intermediate product, recipe, research project,
or processed food. Later features must be removable from the design without making
the crop nonfunctional.

## Technical Constraints

### Implementation Boundary

- The complete feature must be expressible with RimWorld 1.6 Core declarative data.
- Custom C# and Harmony patches are prohibited.
- No new runtime system, custom save state, recurring scan, or bespoke interface is
  permitted.
- The implementation must not alter vanilla crop, food, animal, storage, trade, or
  recipe behavior globally.
- Public identifiers selected during planning become compatibility contracts and
  must use the project namespace.

### Required Art Assets

The feature requires original, provenance-recorded art for:

- a mature oat plant with a readable panicle silhouette;
- an immature oat plant state; and
- harvested raw oats as a stackable item.

The plant must remain distinguishable from rice, corn, haygrass, and blight at normal
zoom, in rich and ordinary soil, under snow and rain, at night, while selected, and
when partially grown. The item must be legible in stockpiles, shelves, trade lists,
caravans, and inventory UI. No audio asset is required; standard plant, harvest,
grain, and food sounds are sufficient.

### Localization Requirements

- Source-language labels are `oat plant` and `oats`.
- Descriptions must communicate medium-cycle timing and processing potential without
  claiming unique Irishness, superior hardiness, or a reconstructed cultivar.
- All player-facing text must be localization-ready and include translator context.
- No Irish term is player-facing in FS-001. Research terms remain documentation
  until competent language review approves their use.
- Text must not be embedded in art.

### Save Compatibility

- Adding the feature to an existing RimWorld 1.6 save must load without an
  Emerald Isle error. Oats become available for future planting; existing maps and
  fields are not modified retroactively.
- Save and load must preserve planted growth, health, damage, blight, harvest state,
  stored stack count, hit points, deterioration, rot progress, caravan ownership,
  trade inventory presence, and food-policy selection wherever vanilla persists
  those states.
- The feature adds no custom serialized state.
- Adding or removing any supported DLC must not alter, remove, or duplicate oats.
- Removal while plants or harvested oats exist is not promised to preserve that
  content. Release documentation must warn about missing content and state the
  tested save-compatibility level.
- Public identifiers must not change after release without migration analysis and a
  documented compatibility decision.

### Compatibility and Performance

- Coexistence with another mod's oats is acceptable; automatic item unification,
  recipe remapping, and broad compatibility patches are out of scope.
- The feature must add no recurring errors or warnings in Core-only or supported-DLC
  configurations.
- Large oat fields must use only vanilla plant and rendering behavior and remain
  within the project performance budget. No feature-specific per-tick work is allowed.

## Acceptance Criteria

- **AC-001 — Availability:** In a new Core-only colony, oats are visible as a normal
  field crop without research or a minimum Plants skill.
- **AC-002 — Planting boundary:** Oats can be designated on ground at 70% fertility
  or higher and cannot be designated in hydroponic basins or on lower-fertility soil.
- **AC-003 — Lifecycle:** Under controlled 100% growth conditions, healthy oats reach
  maturity at the 8.0-day base target and use normal resting and growth rules.
- **AC-004 — Harvest:** A fully healthy mature plant reports a base yield of 15 raw
  oats and produces no secondary item.
- **AC-005 — Fertility:** Oat growth responds at 1.0 fertility sensitivity. At 70%
  fertility it receives the same proportional penalty as rice and corn and performs
  worse than potatoes.
- **AC-006 — Food value:** Each harvested unit provides 0.05 nutrition, uses the
  normal low raw-food preference and 2% fixed human food-poisoning chance, and adds no
  mood or health benefit.
- **AC-007 — Vanilla food integration:** Raw oats can be consumed raw, used by
  ordinary meals and nutrient paste, and selected by normal food policies wherever a
  comparable raw plant food is valid.
- **AC-008 — Animal integration:** Eligible animals can consume harvested oats and
  graze oat plants under normal diet rules; ineligible animals do not gain an
  exception.
- **AC-009 — Storage:** Raw oats stack to 75, have mass 0.03 per unit, and begin rot
  after 45 unrefrigerated days while standard refrigeration, freezing, outdoor
  deterioration, hauling, shelves, and stockpiles behave normally.
- **AC-010 — Economy:** Base market value is 1.1 per unit; eligible traders accept
  oats without a special price, guaranteed stock, or new trader behavior.
- **AC-011 — Threats:** Blight, fire, grazing, failed harvest, temperature, darkness,
  and seasonal loss affect oats through normal cultivated-crop rules. No hardy-crop
  exception exists.
- **AC-012 — Save/load:** The save scenarios in this specification preserve all
  vanilla-persisted oat plant and item state with no recurring log error.
- **AC-013 — DLC absence:** Core-only and each supported DLC configuration load and
  play with the same core Oats behavior; no missing-content error occurs.
- **AC-014 — Art:** Human review can distinguish mature and immature oats from rice,
  corn, and haygrass at normal zoom in the required environmental views.
- **AC-015 — Performance:** A representative large field introduces no custom
  recurring work, no Emerald Isle log spam, and no performance-budget investigation
  trigger attributable to FS-001.
- **AC-016 — Scope:** Inspection confirms there is no custom C#, Harmony patch,
  secondary harvest, new soil/weather system, unique disease, research project,
  wild spawn, or DLC-specific mechanic.

## Playtesting Strategy

### Functional Testing

Test the exact packaged build, first with Core only and then with the DLC matrix.
Verify crop availability, designation limits, sowing, day/night and temperature
growth, inspection values, blight, fire, grazing, cutting, harvest success/failure,
raw eating, meals, nutrient paste, animal feeding, hauling, shelves, stockpiles,
refrigeration, rot, caravans, eligible traders, and destruction.

Run new-save, existing-save addition, save/reload at immature and mature growth,
save/reload with blight or damage, stored-stack rot, and caravan/trade scenarios.
Review the complete log after each run.

### Controlled Balance Testing

Compare equal 100-tile fields of rice, potatoes, oats, and corn at 70%, 100%, and
140% fertility where each crop is valid. Use the same skilled grower, uninterrupted
light/temperature windows, harvest policy, hauling distance, and observation period.
Record:

- elapsed time to first usable harvest;
- harvested units and nutrition per tile-day;
- sowing, harvest, and hauling work;
- failed or interrupted harvest exposure;
- storage space, spoilage, and market value; and
- player choice when field size, labor, season length, and food reserves change.

The arithmetic targets are hypotheses, not a substitute for in-game results.
Observed values must be reconciled with health, skill, difficulty, resting,
fertility, and engine rounding before a balance change is proposed.

### Long-Term Colony Testing

Run at least:

- one two-year colony in a seasonal biome where an 8-day cycle competes with the end
  of the growing season; and
- one one-year colony with year-round growing where labor and storage, rather than
  season length, drive crop choice.

Each colony must use mixed vanilla crops, ordinary food policies, animals, trade,
freezer disruption, at least one blight or equivalent field-loss exercise, and the
available Version 0.1 processing chain when that chain is later testable.

### Success Criteria

- Actual base behavior matches AC-001 through AC-016.
- Oats remain below the highest vanilla comparator in nominal nutrition per tile-day
  at 70%, 100%, and 140% fertility.
- Potatoes remain the clear poor-soil option; rice and potatoes retain hydroponic
  access; corn retains the best long-cycle field-work and shelf-life profile.
- In a moderated comprehension test, at least four of five experienced RimWorld
  players can identify one situation that favors oats and one that favors a vanilla
  crop without being told the intended answer.
- Across the seasonal and year-round scenarios, oats are selected in at least one
  rational plan but do not become the default food crop in every plan.
- Players can recover from unavailable future processing by eating, cooking, feeding,
  storing, or trading raw oats through normal systems.

### Failure Criteria

The feature returns to specification or balance review if any of these occur:

- oats are best or perceived as best across output, labor, soil, speed, and storage;
- oats are never a rational choice once cultural preference is removed;
- the niche is explained as cold, wet, or poor-soil hardiness rather than cadence and
  labor;
- raw-oat compatibility produces errors, uncontrolled recipe substitution, nutrition
  multiplication, or an economy exploit;
- players cannot distinguish oats visually or understand their role from normal UI;
- save/load, DLC absence, or an ordinary failure case loses state unexpectedly or
  creates recurring errors; or
- later milling adds compulsory labor without creating a distinct player decision.

## Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| The medium-cycle niche is too subtle | Medium | High | Use direct vanilla comparison, UI-readable timing, comprehension tests, and reject the crop if no rational use emerges |
| Lower cycle labor plus storage makes oats a quiet strict upgrade | Medium | High | Keep gross output below comparators, normal fertility sensitivity, ground-only planting, and shorter storage than corn |
| Processing makes an already lower-output crop unattractive | Medium | High | Keep raw vanilla uses available; later processing must add a distinct choice and may be simplified |
| Vanilla recipes bypass the themed processing loop | High | Medium | Treat the fallback as intentional; judge later foods by the value they add rather than forced exclusivity |
| Duplicate oat content from other mods confuses players | High | Medium | Use clear Emerald Isle naming and art, test one current broad crop mod, document duplication, and avoid unowned broad patches |
| Save removal loses planted or stored oats | High if removed | Medium | Declare the actual compatibility level, warn users, test removal, and never imply removal safety without evidence |
| A DLC changes food, plant, caravan, or policy behavior | Low | Medium | Execute Core-only, relevant individual-DLC, and all-DLC scenarios against the supported build |
| Art reads as rice or haygrass | Medium | Medium | Prioritize panicle silhouette, immature-state distinction, and normal-zoom in-game review |
| Writing overstates Irish uniformity or authenticity | Low | High | Link to the research limits, use functional English, and prohibit unique-national-crop or reconstructed-cultivar claims |
| Future balance changes break the processing chain | Medium | Medium | Treat FS-001 values as the input contract and require cross-spec review before changing lifecycle or food behavior |

## Out of Scope

FS-001 does not include:

- the Hand Quern, Milled Oats, Oat Porridge, or Oat Flatbread;
- any other crop, food, recipe, building, resource, or research project;
- straw, chaff, seed selection, crop rotation, manure, drying, threshing, brewing, or
  a secondary harvest;
- custom temperature, rainfall, wetness, wind, disease, soil, fertility, biome, or
  world-generation behavior;
- hydroponic cultivation or wild oat spawning;
- social class, ideology, ritual, mood, health, or cultural-preference mechanics;
- automatic compatibility with third-party oats or broad patches to other mods;
- Irish player-facing terminology;
- custom C#, Harmony, custom UI, runtime systems, or custom serialized state; and
- implementation plans, source files, package metadata, or release integration.

## Design Self-Review

| Challenge | Finding | Revision or retained decision |
|---|---|---|
| Unnecessary complexity | A custom hardiness, weather, drying, seed, or exclusive ingredient system would add concepts without improving the crop decision. | Removed all such behavior; the crop uses ordinary agriculture and food systems. |
| Historical overreach | Evidence supports widespread early medieval importance, not one cultivar, universal dominance, or a timeless national crop. | Historical claims are bounded and no historical trait becomes a special mechanical bonus. |
| Gameplay value | An 8-day crop can create a cadence and labor choice, but its niche is narrower than a hardy-crop design. | Retained the narrower niche and added explicit rejection criteria if players find no rational use. |
| Player friction | Forcing milling by blocking vanilla meals would make the crop brittle and pre-decide the conditional quern question. | Raw oats remain available to normal food systems; processing must earn its place. |
| Maintenance burden | DLC hooks, global recipe changes, mod unification, code, and custom state would expand the compatibility surface. | None are permitted; testing focuses on normal Core behavior and safe DLC absence. |
| Future extensibility | The crop must feed later Version 0.1 features without becoming a framework. | One stable raw input is exposed; later features may consume it but cannot silently rewrite FS-001. |

**Self-review result:** The specification was approved and frozen by Patrick Mee on
2026-07-05. It contains no unresolved design decision required to implement FS-001
after planning. Changes now require explicit human approval and, where appropriate,
an ADR. Architecture and implementation-plan review do not authorize gameplay work.
