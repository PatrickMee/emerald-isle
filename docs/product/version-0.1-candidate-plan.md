# Historical Version 0.1 Scope Review and Recommended Plan

**Status:** Historical planning record; approved scope is maintained separately

**Release concept:** The First Holding

**Implementation authorized:** No

**Canonical scope:**
[`version-0.1-approved-scope.md`](version-0.1-approved-scope.md). This review records
the reasoning that led to approval; it does not independently define or amend scope.

## Executive Verdict

The previous five-candidate plan was not optimal. It contained two related food
features, two loosely related stone features, and a milling feature whose value was
conditional. It risked becoming a checklist of implementation patterns rather than
a coherent player experience.

Version 0.1 should be a small settlement-foundation slice: cultivate a processing grain,
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

The approved feature set and binding constraints are maintained only in
[`version-0.1-approved-scope.md`](version-0.1-approved-scope.md). The analyses below
remain historical planning rationale and cannot expand that scope.

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

## Scope Freeze Record

The project owner approved the initial scope on 2026-07-04 and established the
canonical approval record on 2026-07-05. The authoritative record is
[`version-0.1-approved-scope.md`](version-0.1-approved-scope.md).

Each feature still advances independently through research review, specification,
and Definition of Ready. Scope freeze does not authorize implementation.
