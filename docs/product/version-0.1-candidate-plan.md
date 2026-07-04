# Version 0.1 Scope Review and Recommended Plan

**Status:** Recommended; pending Research Sprint execution and human scope freeze

**Release concept:** The First Holding

**Implementation authorized:** No

## Executive Verdict

The previous five-candidate plan was not optimal. It contained two related food
features, two loosely related stone features, and a milling feature whose value was
conditional. It risked becoming a checklist of implementation patterns rather than
a coherent player experience.

Version 0.1 should be a small settlement-foundation slice: cultivate a hardy grain,
process it, turn it into useful food, and establish a recognizable dry-stone-built
holding. The release is intentionally narrow and Core-first. It demonstrates crop,
resource, production, recipe, food, building, construction, art, localization,
testing, compatibility, documentation, and release workflows without custom C#.

The recommended scope contains four gameplay features, not five. Fewer features
produce a more complete and testable vertical slice.

## Evidence Used in This Review

- Canonical Constitution, Design Bible, Vision, roadmap, Feature Catalog, and
  Version 0.1 Research Sprint
- Installed RimWorld `1.6.4871 rev595` Core and all supported DLC data
- Core crop definitions in `Data/Core/Defs/ThingDefs_Plants/Plants_Cultivated_Farm.xml`
- Core wall definition in `Data/Core/Defs/ThingDefs_Buildings/Buildings_Structure.xml`
- Core recipes and production buildings in `Data/Core/Defs/RecipeDefs/` and
  `Data/Core/Defs/ThingDefs_Buildings/Buildings_Production.xml`

The installed Core already has five stone block families, a Stonecutting research
project, stone-block recipes, and a stonecutter's table. That makes a new generic
"worked local stone" resource redundant unless research later identifies a distinct
gameplay role. Core has no dedicated bread, porridge, oat, grain-processing, or
milling definitions, so the oat chain occupies clearer design space.

## Review of the Previous Recommendations

### PL-01 Oat-Like Cool-Climate Grain: Retain, Promote to Walking Skeleton

The candidate has the best combination of visible value, XML feasibility, bounded
art, vanilla comparison, and complete player lifecycle. The previous plan correctly
ranked it highly but understated its value as the first end-to-end workflow test.

### BL-01 Dry-Stone Wall Family: Retain, Narrow

Retain one initial dry-stone wall variant, not a family. The vanilla wall uses Stuff,
linked graphics, appearance handling, heavy terrain, roof support, and construction
rules; duplicating all behavior and art variants immediately is unnecessary risk.
Version 0.1 should prove one balanced, visually distinct construction choice using
vanilla stone blocks. Expansion into fences, gates, corners, ringfort sets, or
material families waits for evidence.

### FO-01 Oat Bread and Porridge Chain: Retain, Bound to Two Foods Maximum

Retain as the payoff for the crop/processing loop. Scope should remain one everyday
food and one differentiated prepared food at most. Research must prove each has a
distinct role; otherwise ship only one. Do not create a parallel meal taxonomy.

### RS-02 Worked Local Stone Set: Remove from Version 0.1

Defer. Core already provides sandstone, granite, limestone, slate, and marble blocks
through an established Stonecutting workflow. A new stone material would add Defs,
art, storage, recipes, market balance, and compatibility without a demonstrated
decision. BL-01 should consume vanilla stone blocks unless research proves a new
resource creates value beyond theme.

### PR-01 Quern and Milling Workflow: Retain Conditionally, XML-Only

Retain because it connects crop to food and proves a reusable production pattern.
However, it is accepted only if research/playtest planning shows milling creates a
meaningful labor, storage, portability, or efficiency decision rather than mandatory
busywork. Implementation must use standard worktable/bill/RecipeDef patterns. If it
requires custom C#, Harmony, or an unnecessary multi-stage inventory chain, defer it
and allow direct oat cooking in FO-01.

### RE-01, QL-01: Do Not Promote as Gameplay Features

A dedicated Vernacular Masonry research node is low-value gating at this scale; use
existing Stonecutting or an appropriate vanilla prerequisite if balance requires it.
A custom Emerald Isle build category for one wall and one worktable would increase
menu clutter. Categorization is release integration work and should follow actual
content volume.

## Final Recommended Version 0.1 Scope

### 1. PL-01: Oats

**Purpose:** Add a hardy cereal crop and harvested raw grain that establishes the
agricultural base of the first Emerald Isle holding.

**Gameplay value:** A new crop is justified only through a distinct yield/growth,
fertility, shelf-life, nutrition, or climate tradeoff against rice, potatoes, corn,
and haygrass. It becomes the input for the rest of the food slice.

**Dependencies:** P-01 and T-01 through T-04 research; final naming/language review;
RimWorld 1.6 Core. No DLC required. DLC behavior should remain additive or neutral.

**Implementation:** XML only: plant, harvested item, categories, sowing and harvest
properties, translations. No C# or Harmony.

**Art effort:** Medium: mature and immature plant graphics plus harvested grain icon;
normal zoom, wind, growth, blight, snow, and harvest readability.

**Testing effort:** Medium: sowing, growth, fertility, hydroponics decision, harvest,
nutrition, rot, stacking, animals, bills, save/load, Core-only and supported-DLC matrix.

**Implementation effort:** Small to medium after research.

**Why Version 0.1:** It is visible, low-risk, system-native, enables the food chain,
and exercises the complete content pipeline without custom code.

### 2. BL-01: Dry-Stone Wall

**Purpose:** Add one recognizable vernacular construction choice that makes a colony
look like an Emerald Isle holding while creating a balanced defensive/material decision.

**Gameplay value:** A constrained alternative to vanilla walls. The final tradeoff
must emerge from research and balance, potentially through work, block cost,
durability, beauty, roof support, cover, or terrain requirements. It cannot be a
cheaper equal wall.

**Dependencies:** B-01/R-01/T-01/T-02 research; PL-01 only as workflow precedent;
vanilla stone blocks and construction systems. No new stone resource.

**Implementation:** XML only using supported building, Stuff, linked-graphic, damage,
designation, and construction behavior. No C# or Harmony.

**Art effort:** Medium to high: one coherent linked wall texture set, menu icon, and
in-game adjacency/damage validation. Avoid a family of variants in 0.1.

**Testing effort:** Medium: construction materials, replacement, linking, pathing,
cover, combat damage, fire, roofs, zones, blueprints, deconstruction, save/load,
and mixed vanilla-wall adjacency.

**Implementation effort:** Medium.

**Why Version 0.1:** It adds immediate visual identity and establishes the building,
construction, Stuff, linked-art, and combat-validation patterns needed by all later architecture.

### 3. PR-01: Hand Quern and Milled Oats

**Purpose:** Introduce a compact manual production step between harvested oats and
prepared food, if that step produces a real choice.

**Gameplay value:** Converts raw grain through pawn labor and a small work site,
potentially trading time and storage complexity for cooking efficiency, shelf life,
or access to distinct foods. The exact advantage must be evidence-led.

**Dependencies:** PL-01; U-03/F-01/T-01/T-02 research; accepted no-busywork balance
hypothesis; one stable intermediate item at most.

**Implementation:** XML only through worktable, bills, RecipeDef, ingredients,
products, work amount, skills, and translations. If standard XML cannot deliver the
accepted design, defer instead of adding C#.

**Art effort:** Medium: small quern worktable with required rotations/states and one
milled-oats icon.

**Testing effort:** Medium: bills, ingredient filters, hauling, reservations, work
skill/speed, bulk decision, storage, cancellation, destruction, save/load, and DLC matrix.

**Implementation effort:** Medium.

**Why Version 0.1:** It establishes the production/manufacturing/recipe pattern that
future brewing, dairy, flax, textile, and craft features will reuse.

### 4. FO-01: Oat Foods

**Purpose:** Complete the player loop with one or two culturally grounded foods made
from oats or milled oats.

**Gameplay value:** Provides a visible payoff and a food decision differentiated by
labor, nutrition, mood, portability, shelf life, or cooking access. It must not be a
strictly better simple meal or a cosmetic recipe duplicate.

**Dependencies:** PL-01; PR-01 if milling survives its gate; F-01/T-02 research;
food naming and cultural review; Core cooking facilities.

**Implementation:** XML only using ThingDef and RecipeDef patterns, bills, ingredient
filters, ingestible properties, thoughts only if existing XML patterns safely support
the accepted design. No custom food framework.

**Art effort:** Low to medium: one icon per shipped food; reuse normal bill and
facility presentation.

**Testing effort:** Medium: recipe availability, filters, nutrition, mood, rot,
caravans, prisoners/animals where relevant, Ideology food interactions, save/load,
and no-DLC/all-DLC behavior.

**Implementation effort:** Small to medium.

**Why Version 0.1:** It turns separate implementation patterns into a coherent player
experience and proves end-to-end balance from field through labor to consumption.

## Reusable Implementation Patterns

| Feature | Patterns established | Later consumers |
|---|---|---|
| PL-01 Oats | Crop, harvested resource, growth art, raw-food categories, agricultural balance | Flax, forage plants, animal feed, biome crops |
| BL-01 Dry-Stone Wall | Building, construction, Stuff/material filters, linked graphics, damage/combat testing | Ringforts, monastic buildings, field boundaries, architecture kits |
| PR-01 Quern | Production building, manufacturing bill, RecipeDef, intermediate resource, work/hauling flow | Brewing, dairy, flax, dyes, craft and preservation |
| FO-01 Oat Foods | Food item, cooking recipe, ingredient filter, nutrition/rot/mood balance | Dairy foods, feast foods, preserved foods, hospitality systems |

Version 0.1 deliberately does not establish terrain, decoration, custom research,
animals, apparel, quests, rituals, factions, world generation, or custom C# patterns.
Creating unused patterns would violate milestone discipline.

## Cohesion Review

The four-feature scope is coherent under **The First Holding**:

1. Plant oats suited to the colony's conditions.
2. Decide whether manual processing is worth the labor and storage.
3. Turn the crop into useful food with visible tradeoffs.
4. Shape the holding with a recognizable dry-stone construction choice.

The food loop supplies mechanical cohesion; the wall supplies spatial and visual
identity. Both concern the earliest acts of establishing a settlement: feeding
people and defining/protecting place. No feature requires the later culture,
mythology, faction, or world systems to make sense.

The release fails cohesion if milling is only a mandatory click tax, oat foods are
stat clones, or the wall is a cheaper vanilla wall. Those are explicit research and
Feature Acceptance Checklist failure conditions.

## Implementation Order

### 1. PL-01 Oats — Walking Skeleton

Comes first because it has no gameplay dependency, is likely compact XML, and
exercises research, specification, naming, art, Defs, balance, save/load, DLC matrix,
documentation, packaging, and release evidence. It enables every food-chain feature.

### 2. BL-01 Dry-Stone Wall

Comes second because it is independent of the oat chain and validates a different,
high-value architectural pattern after the first pipeline is proven. It enables
future structure sets and provides visible identity early.

### 3. PR-01 Hand Quern and Milled Oats

Comes third because it depends on the oat resource and must be evaluated against the
actual harvested item and labor economy. It enables FO-01 and future production chains.

### 4. FO-01 Oat Foods

Comes last because recipe balance depends on final crop yields and the milling
decision. It completes the vertical loop and supplies the strongest release-level
cohesion and player payoff.

### 5. Release Integration — Not a Gameplay Feature

Validate menu placement, terminology, compatibility, attribution, full save path,
clean package, playtest, and release notes. Create a custom category only if the
actual content volume demonstrates a navigation problem.

## Walking Skeleton Decision

**PL-01 Oats is the ideal walking skeleton.**

It is smaller than the dry-stone wall after inspecting RimWorld 1.6: the wall's
Stuff behavior and linked graphic set make it a broader visual/construction test.
Oats can exercise the complete workflow with a bounded plant Def, harvested item,
translations, a small asset set, vanilla crop comparisons, observable in-game
growth/harvest behavior, save/load, DLC absence behavior, documentation, packaging,
and a test release.

The walking skeleton is complete only after:

`Research -> Specification -> Acceptance -> Plan -> XML implementation -> Static checks -> In-game growth/harvest test -> Save/load/DLC matrix -> Documentation -> Packaged test release -> Lessons learned`

This does not authorize implementation. P-01 and T-01 through T-05 research must be
executed, PL-01 must pass the Feature Acceptance Checklist, and its implementation
plan must pass Definition of Ready first.

## Deferred Catalog Review

| Deferred IDs | Reason for postponement |
|---|---|
| RS-02 | Duplicates Core stone-block/Stonecutting space without proven gameplay value |
| RE-01, QL-01 | Low independent player value; add only if real gating/navigation needs emerge |
| AN-01, AN-02 | High animal art, balance, AI/training, and Biotech interaction burden |
| PL-02 | Multi-output processing and textile balance expand the first slice |
| FO-02, PR-02 | Aging/fermentation, addiction, storage, and production complexity belong after the first chain |
| RS-01 | Extraction, terrain, fuel filters, environmental framing, and likely code risk |
| BL-02, BL-03 | Large footprints, generation/vertical abstraction, quests, and high art scope |
| FU-01, FU-02 | Multi-role furniture risks custom behavior and weak standalone value |
| WP-01, WP-02, AR-01, AR-02 | Combat balance and compatibility require a mature test baseline |
| AP-01, AP-02 | Body-type/layer art workload and cultural review exceed the first slice |
| RE-02 | Depends on later knowledge/culture systems |
| RT-01, RT-02, ID-01, ID-02 | Ideology/ritual/social state and DLC fallback need code and broader design |
| FA-01, FA-02 | Faction AI, generation, quests, lore, and save state are later architecture |
| WG-01, WG-02 | World generation and save irreversibility are high-risk Version 2/3 work |
| QU-01, QU-02, EV-01, EV-02 | Quest/event frameworks and narrative content need mature foundations |
| ST-01, ST-02 | Storyteller tuning has expansion-wide balance and compatibility impact |
| MY-01, MY-02 | Reserved for 1.5; cultural, Anomaly, event, art, and code scope is high |
| EX-01, EX-02 | Site/world/expedition generation depends on later quest and world architecture |
| QL-02 | Runtime diagnostics require C# and a demonstrated support problem |

## Scope Freeze Gate

This review recommends the scope but does not freeze it. Freeze requires:

- completion and review of Priority 1 Research Sprint briefs
- confirmed XML-only feasibility for all four features
- explicit rejection or acceptance of the milling busywork hypothesis
- verified art estimates and Core-only/all-supported-DLC test design
- human approval of this plan

After freeze, each feature still advances independently through specification and
Definition of Ready. Scope freeze does not authorize batch implementation.
