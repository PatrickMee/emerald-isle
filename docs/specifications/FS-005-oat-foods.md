# FS-005 — Oat Foods

**Status:** Approved — Frozen<br>
**Gate 1 status:** Approved by Patrick Mee, 2026-07-07<br>
**Milestone:** Version 0.1 — The First Holding<br>
**Catalog feature:** FO-01<br>
**Feature branch:** `codex/fs-005-oat-foods-specification`<br>
**Owner:** Patrick Mee<br>
**Created:** 2026-07-07<br>
**Vanilla balance baseline:** RimWorld 1.6.4871 rev595<br>
**Research:** [RSC-006 Oat Foods](../research/version-0.1/oat-foods.md),
[RSC-005 Milled Oats](../research/version-0.1/milled-oats.md),
[RSC-004 Hand Quern](../research/version-0.1/hand-quern.md)<br>
**Implementation authorized:** Yes — as a bundled FS-003 + FS-004 + FS-005
vertical slice.

## Authority and Boundaries

This specification defines the Version 0.1 oat-food pair that completes the first
holding's approved oat-processing chain. It conforms to the
[Version 0.1 approved scope](../product/version-0.1-approved-scope.md),
[Version 1.0 Vision](../product/version-1.0-vision.md),
[Design Bible](../design/design-bible.md), and the approved Version 0.1 research
briefs.

FS-005 is the missing gameplay payoff for FS-003 Hand Quern and FS-004 Milled Oats.
Without at least one oat food, the quern and milled-oats item produce a dead
intermediate. The intended implementation path after Gate 1 approval is one
playable vertical slice:

```text
Oats
  ↓
Hand Quern
  ↓
Milled Oats
  ↓
Choice
  ├── Oat Porridge
  └── Oat Flatbread
```

This document contains no XML, C#, Harmony patch, file layout, texture path,
public `defName`, or implementation sequence.

## Overview

FS-005 adds two simple-tier foods made from milled oats:

- **Oat porridge:** a fresh everyday food with a low final-cooking burden because
  milling has already been done.
- **Oat flatbread:** a plain, plant-only, moderately keeping food for reserves and
  short travel, paid for by substantially more total work and weaker preservation
  than pemmican or packaged survival meals.

The design goal is choice, not historical completeness. If implementation or
playtesting shows that the two foods do not create distinct player behavior, the
chain must be simplified rather than expanded with more mechanics.

## Historical Research

The approved Oat Foods research brief supports a broad two-food pair. Early
medieval Irish documentary synthesis distinguishes pot-based cereal foods from
breads and records flat breads made from oats and other cereals. Archaeobotanical
evidence supports oats as an ordinary crop, and quern evidence supports domestic
grain processing.

The evidence does not recover exact recipes, portions, textures, spoilage times, or
ingredient ratios at game-stat precision. `Oat porridge` and `oat flatbread` are
clear English gameplay labels for plausible food forms, not claims of standardized
recipes across all of early medieval Ireland.

## Cultural Significance

The foods express ordinary domestic life: grain grown in the holding, processed by
household labor, and turned into daily meals or portable reserves. They should feel
practical and modest.

The feature must avoid:

- turning oats into a universal symbol of Irish food;
- framing ordinary cereal food as poverty flavor or cultural inferiority;
- mapping historical social rank of cereals onto pawn class or mood penalties;
- importing famine-era, cottage, modern health-food, or packaged-breakfast imagery;
- using Irish words as decorative authenticity;
- adding labor only because historical labor existed.

English player-facing names are `oat porridge` and `oat flatbread`. Irish-language
localization is not required for Version 0.1 and should be reviewed later if added.

## Gameplay Purpose

FS-005 makes the processing chain useful by giving milled oats two destinations:

- porridge supports fast final meal preparation after prior milling;
- flatbread supports a longer-keeping plant-only food for short-term reserves and
  travel.

Raw oats remain useful through ordinary FS-001 paths. Milled oats are useful because
these foods consume them. The player decides whether to keep oats raw, prepare a
fresh-food reserve, or invest extra work into more portable food.

## Vanilla Comparison

The baseline vanilla comparisons are:

- **Simple meal:** broad input flexibility, 300 cooking work, 0.9 nutrition, rots
  after 4 days.
- **Pemmican:** plant-and-meat preserved food, high work, rots after 70 days.
- **Packaged survival meal:** researched, skilled, non-rotting travel food.
- **Raw oats:** flexible raw crop usable through ordinary food and feed paths.

Oat porridge must not become a superior simple meal. Its advantage is reduced final
cooking time after separate milling; its costs are prior labor, extra hauling,
narrow input, and shorter keeping time.

Oat flatbread must not replace pemmican or packaged survival meals. Its advantage is
plant-only moderate keeping; its costs are higher complete-chain work, narrower
input, lower preservation, and no advanced-food bonuses.

## Gameplay Design

### Oat Porridge

Oat porridge is the everyday fresh-food path.

Target behavior:

- input: 10 milled oats;
- output: 1 oat porridge;
- nutrition: 0.9;
- final cooking work: 120 work;
- complete processing work: 180 milling + 120 cooking = 300 work, plus extra
  hauling and storage;
- food tier: simple meal equivalent;
- shelf life: 2 days unrefrigerated before rot begins;
- cooking access: existing Core cooking buildings that can make simple meals;
- research and skill gate: none beyond ordinary cooking behavior;
- special effects: none.

The player benefit is moving most work out of the final cooking bottleneck. The
short shelf life keeps porridge a near-term meal, not reserve food.

### Oat Flatbread

Oat flatbread is the portable processed-food path.

Target behavior:

- input: 10 milled oats;
- output: 1 oat flatbread;
- nutrition: 0.8;
- final cooking work: 420 work;
- complete processing work: 180 milling + 420 cooking = 600 work, plus extra
  hauling and storage;
- food tier: simple meal equivalent;
- shelf life: 14 days unrefrigerated before rot begins;
- cooking access: existing Core cooking buildings that can make simple meals or
  pemmican;
- research and skill gate: none beyond ordinary cooking behavior;
- special effects: none.

The player benefit is a plant-only ready food that keeps longer than fresh meals.
The lower nutrition output, higher work, and much shorter preservation than
pemmican prevent it from becoming the best travel food.

### Player Decisions

- **Raw oats:** maximum flexibility; no milling; ordinary food/feed/trade paths.
- **Porridge:** fastest final cooking after prior milling; poor for storage.
- **Flatbread:** more work and lower nutrition output for moderate keeping.
- **Direct fallback:** if the chain creates friction without choices, use raw oats
  in ordinary systems and simplify the chain through review.

## Balance Analysis

### Balance Hypotheses

**Porridge hypothesis:** Porridge is useful when a colony can mill ahead of time and
needs fast final cooking. It remains balanced because complete-chain work equals a
simple meal before extra hauling/storage, the input is narrow, and shelf life is
shorter than a simple meal.

**Flatbread hypothesis:** Flatbread is useful when a colony has spare work and wants
a plant-only reserve that keeps longer than meals. It remains balanced because it
costs twice the complete processing work of porridge, produces less nutrition, and
keeps far less well than pemmican or packaged survival meals.

### Balance Targets

| Dimension | Oat porridge | Oat flatbread | Design intent |
|---|---:|---:|---|
| Input | 10 milled oats | 10 milled oats | One FS-004 milling batch per food |
| Output nutrition | 0.9 | 0.8 | Porridge equals simple meal; flatbread pays for keeping |
| Final cooking work | 120 | 420 | Porridge fast at stove; flatbread labor-intensive |
| Complete work with milling | 300 | 600 | Porridge equals simple-meal work before logistics; flatbread is costly |
| Shelf life | 2 days | 14 days | Fresh meal vs moderate reserve |
| Food tier | Simple | Simple | No mood or luxury bonus |
| Mass | No lower than comparable meals | No lower than comparable meals | No caravan mass exploit |
| Market value | No profit loop over ingredients | No profit loop over ingredients | Cooking is for use, not trade arbitrage |
| Research | None | None | Version 0.1 early holding |
| DLC dependency | None | None | Core-only behavior |

### Required Tradeoffs

| Food | Strength | Required cost |
|---|---|---|
| Porridge | Low final cooking work | Prior milling, extra logistics, short shelf life, narrow ingredient |
| Flatbread | Moderate plant-only keeping | High work, lower output nutrition, narrow ingredient, preservation far below pemmican |

### Abuse and Failure Cases

The design fails if:

- porridge becomes strictly better than simple meals in most colonies;
- flatbread replaces pemmican or packaged survival meals as the dominant travel
  food;
- conversion from raw oats to milled oats to food creates nutrition or value loops;
- pawns universally prefer one oat food and erase the intended choice;
- bills clutter every cooking building without adding decisions;
- caravans exploit flatbread through unusually low mass or high days of food;
- food policies, ideology, babies, animals, nutrient paste, or prisoners select
  unintended foods;
- players always mill all oats and produce only one food indefinitely.

## Player Scenarios and Acceptance

1. **Given** a colony has milled oats and a normal cooking building, **when** the
   player cooks oat porridge, **then** one milling batch produces one fresh simple
   food with low final cooking work and short shelf life.

2. **Given** a colony has milled oats and a normal cooking building, **when** the
   player cooks oat flatbread, **then** one milling batch produces one plain
   plant-only simple food with higher work, lower nutrition than porridge, and
   moderate shelf life.

3. **Given** raw oats are available, **when** the player chooses not to mill them,
   **then** raw oats remain useful through ordinary FS-001 food, feed, storage,
   trade, and caravan paths.

4. **Given** the complete chain is compared to direct raw-oat cooking, **when**
   work, hauling, storage, nutrition, and spoilage are evaluated, **then** the oat
   foods must create distinct behavior or the chain must be simplified.

5. **Given** a colony is preparing for short travel without meat, **when** it makes
   oat flatbread, **then** flatbread is useful for short reserves but remains
   materially worse preserved than pemmican and packaged survival meals.

6. **Given** a save contains raw oats, milled oats, porridge, flatbread, bills,
   stockpiles, food policies, and caravans, **when** the save is reloaded, **then**
   ordinary item, food, policy, and bill state persists without custom serialized
   data.

7. **Given** official DLC are absent or present, **when** the foods are loaded,
   cooked, stored, eaten, carried, and restricted, **then** no DLC is required and
   optional DLC behavior remains safe.

## Scope

### In

- One oat porridge food item.
- One oat flatbread food item.
- One porridge recipe consuming milled oats.
- One flatbread recipe consuming milled oats.
- Existing Core cooking buildings only.
- Standard nutrition, ingestibility, food tier, rot, deterioration, mass, stack,
  market value, food poisoning, ingredient history, food policies, trade, caravan,
  bill, storage, and save behavior.
- Two original food icons.
- English localization-ready labels and descriptions.

### Out

- New cooking buildings, hearths, griddles, ovens, bowls, utensils, containers, or
  furniture.
- Milk, honey, salt, water, dairy, seasoning, meat, egg, pulse, garnish, or
  enriched variants.
- Fine, lavish, ritual, ideology, medical, baby, invalid, comfort, temperature, or
  mood foods.
- Food quality, stale states, reheating, fermentation, preservation jars, or bulk
  recipe variants unless later playtesting proves a specific need.
- Generic bread, dough, flour, baking, soup, stew, or cooking framework.
- Direct cross-mod compatibility with other flour, bread, or food systems.
- Custom C#, Harmony, custom jobs, custom UI, custom thoughts, custom tickers, or
  custom serialized state.

## Technical Design

Implementation should use vanilla declarative food and recipe behavior:

- two passive food items;
- two narrow recipes consuming only milled oats;
- recipe availability on existing Core cooking buildings;
- standard food poisoning, ingredient history, rot, storage, food-policy, caravan,
  trade, save/load, and localization behavior;
- no custom runtime assembly.

Public compatibility contracts created at implementation include the food
definitions, recipe definitions, translation keys, texture paths, recipe-user
relationships, food policy behavior, and saved stacks.

If vanilla XML cannot express the approved narrow behavior, stop and request review.
Do not add code, Harmony, new buildings, or a broader cooking framework silently.

## XML vs C# Decision

**Decision target:** XML-only.

Core RimWorld already supports food items, nutrition, ingestibility, rot, recipes,
ingredient filters, cooking buildings, food poisoning, caravans, policies, trade,
save persistence, and localization. FS-005 does not require custom logic, custom UI,
custom thoughts, custom serialization, or Harmony.

C# is not approved. Harmony is out of scope and would require a new ADR and
compatibility plan.

## Art Requirements

Required art:

- one original oat-porridge icon;
- one original oat-flatbread icon.

The porridge icon should read as a simple prepared cereal food, not baby food,
soup, stew, packaged oatmeal, or a luxury dish. The flatbread icon should read as
plain cooked bread, not a wheat loaf, cracker packet, cake, pemmican, packaged
survival meal, or decorative pastry.

Both assets must match vanilla readability at normal zoom and avoid green identity
markers, knotwork, decorative carving, modern packaging, or copied reference
imagery.

## Audio Requirements

No custom audio is required. Existing cooking and eating sounds are sufficient for
Version 0.1.

## Localization

English source labels:

- `oat porridge`;
- `oat flatbread`.

Descriptions must explain the gameplay role without unsupported historical claims:

- porridge is a fresh cooked oat food;
- flatbread is a plain, moderately keeping oat food;
- neither is a luxury, health, ritual, ideology, or medicine food;
- neither description should claim exact medieval recipes, measured historical
  shelf life, or modern nutrition benefits.

Irish-language terms remain research notes unless qualified language review later
approves localized entries.

## Testing

Gate 2 evidence must cover the complete player path with FS-003 and FS-004:

- static XML validation for food and recipe definitions;
- clean Core-only load with no new unresolved errors or warnings;
- cooking both foods from milled oats at supported cooking buildings;
- porridge and flatbread target counts, bill suspension, ingredient search, and
  output hauling work normally;
- raw oats remain useful without milling;
- milled oats are consumed by the oat-food recipes and do not become a dead
  intermediate;
- generic meals, nutrient paste, animals, babies, prisoners, food policies, ideology
  rules, caravans, traders, and stockpiles do not select unintended items;
- nutrition, market value, mass, rot, and complete-chain work avoid loops and
  strict upgrades;
- save/load works with crops, querns, milled oats, foods, bills, policies,
  stockpiles, caravans, and stored stacks;
- official DLC absence/presence does not create hard dependencies;
- maintainer playtest confirms players understand the porridge versus flatbread
  decision.

## Future Expansion

Later releases may consider dairy-enriched porridges, oatcake variants, feasts,
hospitality foods, broader bread systems, powered milling, or food-framework
compatibility only after Version 0.1 proves the narrow chain creates real choices.
FS-005 must not add placeholder categories, hidden hooks, or speculative food
systems for those possibilities.

## Dependencies

**Required DLC:** None. RimWorld 1.6 Core is required.

**Optional DLC enhancements:** None for Version 0.1.

**Behavior without DLC:** Full food and recipe behavior through Core item, food,
recipe, cooking, policy, storage, and caravan systems.

**Save compatibility:** Released food and recipe definitions become save contracts
for maps, inventories, caravans, stockpiles, food policies, bills, and trade.
Renaming or removing them after release requires migration and missing-def analysis.

**Feature dependencies:**

- FS-001 Oats supplies raw crop fallback.
- FS-003 Hand Quern supplies the production building.
- FS-004 Milled Oats supplies the processed ingredient and milling recipe.

## Risks

| Risk | Likelihood | Impact | Mitigation | Owner |
|---|---|---:|---|---|
| Porridge is a better simple meal | Medium | High | Keep complete work equal before logistics; short shelf life; narrow ingredient | Maintainer |
| Flatbread replaces pemmican | Medium | High | Preserve much shorter shelf life, lower nutrition, higher work | Maintainer |
| Chain becomes mandatory busywork | High | High | Preserve raw-oat paths; test direct-cooking fallback; simplify if behavior converges | Maintainer |
| Nutrition or value loop | Medium | High | Test complete raw-to-milled-to-food accounting | Implementer |
| Food-policy or DLC behavior surprises players | Medium | Medium | Include Core and supported-DLC food selection checks | Implementer |
| Bill clutter exceeds value | Medium | Medium | Exactly two foods; no variants or bulk recipes by default | Maintainer |
| Art reads as modern or generic | Medium | Medium | Validate icons beside vanilla meals, pemmican, raw oats, and milled oats | Maintainer |
| Scope expands into cuisine framework | Medium | High | Enforce out-of-scope list; require ADR for broader systems | Maintainer |

## Gate 1: Approval Checklist

- [x] Catalog ID, owner, and active milestone are assigned; the feature belongs to
      the current approved Version 0.1 scope.
- [x] Player problem, meaningful decision, story value, and bounded first slice are
      clear; explicit exclusions prevent scope leakage.
- [x] Constitution and Design Bible conformance are reviewed, including tradeoffs
      over power and vanilla-native fit.
- [x] Material historical, cultural, gameplay, and technical uncertainty is
      resolved to specification depth through approved research.
- [x] Vanilla/DLC comparison and balance hypothesis are measurable.
- [x] Irish-language and culturally sensitive content is identified; no early
      qualified review is requested because player-facing English remains
      functional and low-risk.
- [x] XML-first decision is documented; C# and Harmony are rejected; public
      contracts, save impact, and compatibility are stated.
- [x] Acceptance, edge, failure, and persistence scenarios exist; test and playtest
      intent is actionable.
- [x] Art, audio, and localization needs are defined or marked not applicable.
- [x] Dependencies are explicit: FS-005 completes the first processing vertical
      slice with FS-003 and FS-004.

**Decision:** Approved<br>
**Approved by/date:** Patrick Mee, 2026-07-07<br>
**Conditions:** If playtesting shows porridge and flatbread do not create distinct
decisions, simplify the chain rather than expanding scope.

## Gate 2: Evidence

Bundled implementation and technical validation are recorded in
[FS-003/FS-004/FS-005 Oat Processing Test Evidence](../qa/evidence/FS-003-004-005-oat-processing-test-matrix.md).

Static validation, package staging, release-safety checks, texture path checks,
maintainer-provided in-game production-path evidence, and final oat food art
approval pass. The complete player path across oats, hand quern, milled oats,
porridge, and flatbread is implemented.

Patrick Mee completed the final in-game smoke test for the exact staged package
on 2026-07-10 and confirmed that the oat-processing path works correctly.

**Decision:** Done<br>
**Approved by/date:** Patrick Mee, 2026-07-10

## Open Questions and Decisions

| Question | Owner | Due point | Status |
|---|---|---|---|
| Do porridge and flatbread create distinct player behavior in practice? | Maintainer | Complete-chain playtest | Must simplify if no |
| Can the supported RimWorld 1.6 XML contracts keep milled oats narrow without unintended generic meal use? | Implementer | During implementation discovery | Verify before XML finalization |
| Are the proposed food targets understandable from labels, descriptions, stats, and bills? | Maintainer | Gate 2 playtest | Verify in game |
