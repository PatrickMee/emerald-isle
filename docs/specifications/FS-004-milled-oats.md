# FS-004 — Milled Oats

**Status:** Approved — Frozen<br>
**Gate 1 status:** Approved by Patrick Mee, 2026-07-07<br>
**Milestone:** Version 0.1 — The First Holding<br>
**Catalog feature:** PR-01 / FO-01<br>
**Feature branch:** `codex/fs-004-milled-oats-specification`<br>
**Owner:** Patrick Mee<br>
**Created:** 2026-07-07<br>
**Vanilla balance baseline:** RimWorld 1.6.4871 rev595<br>
**Research:** [RSC-005 Milled Oats](../research/version-0.1/milled-oats.md),
[RSC-004 Hand Quern](../research/version-0.1/hand-quern.md),
[RSC-006 Oat Foods](../research/version-0.1/oat-foods.md)<br>
**Implementation authorized:** Yes — as a bundled FS-003 + FS-004 + FS-005
vertical slice.

## Authority and Boundaries

This specification defines the Version 0.1 milled-oats intermediate and its
relationship to the approved [FS-003 Hand Quern](FS-003-hand-quern.md). It
conforms to the [Version 0.1 approved scope](../product/version-0.1-approved-scope.md),
[Version 1.0 Vision](../product/version-1.0-vision.md), and
[Design Bible](../design/design-bible.md).

Milled oats are conditional in the same practical sense as the hand quern. A
processing intermediate is justified only if it leads to meaningful downstream
choices. Turning useful raw oats into a dead ingredient is not playable value.

FS-004 may be implemented together with FS-003 as the manual milling slice, but the
player-facing processing chain must not pass Gate 2 unless at least one FS-005 oat
food consumes milled oats in the same release path. The preferred delivery sequence
is: approve FS-004, approve FS-005, then implement the quern, milled oats, and first
food consumer as one playable vertical slice.

This document contains no XML, C#, Harmony patch, file layout, texture path,
public `defName`, or implementation sequence.

## Overview

Milled oats are a processed oat ingredient produced by milling raw oats at the hand
quern. They represent coarse ground oat material suitable for porridge or
flatbread, not modern standardized oatmeal, flour, flakes, bran, or a generic flour
framework.

The gameplay role is stockpiled preparation. Players can decide how much of their
raw oat reserve to commit to a narrower processed ingredient before final cooking.
The item must not create nutrition, preservation, value, mood, health, or trade
benefits by itself.

## Historical Research

The approved Milled Oats research brief supports a broad gameplay abstraction:
oats were a major early medieval Irish cereal, domestic rotary querns processed
grain, and cereal foods included porridges and breads. The evidence does not
preserve one standardized product equivalent to a modern package of oatmeal.

`Milled oats` is therefore a transparent English interface label for ground oat
material. It must not claim a single medieval recipe, a uniform product across
Ireland, or a modern industrial processing sequence.

The research also rejects several tempting expansions for Version 0.1: drying,
dehulling, sifting, hull byproducts, bran, quality grades, flour compatibility, and
powered milling. Those remain out of scope unless a later approved feature proves
gameplay value.

## Cultural Significance

Milled oats make domestic grain labor visible without turning labor into heritage
decoration. The item connects cultivation, household processing, and ordinary food.
It should support Emerald Isle’s first-holding identity through practical colony
management, not through romantic claims or cultural essentialism.

The feature must avoid:

- presenting oats or oatmeal as timeless shorthand for all Irish food;
- implying early medieval Ireland lacked larger mills or technical sophistication;
- projecting nineteenth- or twentieth-century rural imagery backward;
- presenting a modern Irish term as an attested early medieval product name;
- converting historical labor into compulsory busywork.

Player-facing English should use `milled oats`. Irish-language localization is not
required for Version 0.1.

## Gameplay Purpose

Milled oats exist to create an allocation and scheduling decision:

- leave oats raw for flexible ordinary use; or
- mill some oats into a narrower prepared ingredient for the oat-food chain.

The feature should let players prepare an ingredient reserve during quiet periods,
then use that reserve later for fresh or portable oat foods. It earns its place only
if final food choices make that preparation useful.

Milled oats are not intended to be a better food than raw oats. They are not a
storage upgrade, animal-feed upgrade, trade good, health food, or universal flour.

## Vanilla Comparison

The closest vanilla comparison is wort: a passive intermediate created by a bill and
used by a later production stage. Wort demonstrates that XML intermediates can be
legible in RimWorld, but it also demonstrates that intermediates impose real costs:
extra bills, hauling, storage, rot, stockpile filters, and save contracts.

The closest food comparison remains the ordinary raw crop path. Raw rice, corn, and
potatoes can be eaten, cooked, stored, hauled, traded, and fed through broad vanilla
systems. Raw oats from FS-001 deliberately retain that flexibility. Milled oats must
narrow the use case in exchange for later food-production options; otherwise the
item is either pointless or a strict upgrade.

## Gameplay Design

### Production

Milled oats are produced only by milling raw oats at the hand quern.

Target recipe behavior:

- input: 10 raw oats;
- output: 10 milled oats;
- work: 180 work at the hand quern;
- labor channel: non-Cooking production labor, matching FS-003’s requirement that
  milling be schedulable separately from final cooking;
- power and fuel: none;
- research and skill gate: none;
- batch purpose: one batch represents the prepared grain input for one simple-tier
  oat-food recipe.

If the supported RimWorld 1.6 XML contract cannot express non-Cooking production
labor for this bill without custom code, implementation must stop for review. Do
not silently move milling into the final cooking bottleneck.

### Item Role

Milled oats are a processed ingredient, not a direct meal.

Target behavior:

- pawns should not choose milled oats as ordinary direct food;
- animals should not prefer milled oats over raw feed;
- vanilla generic meal or nutrient-paste paths should not consume milled oats
  unless a later approved test proves that behavior is required and balanced;
- FS-005 oat-food recipes are the intended consumers;
- the item may be stored, hauled, counted in bills, carried, traded, and lost like
  an ordinary passive item.

Raw oats remain the flexible crop. Milled oats are the committed preparation path.

### Player Decisions

- **How much to process:** keep a raw reserve or maintain a smaller processed stock.
- **When to process:** mill during low-pressure work periods before cooks need the
  ingredient.
- **Where to store:** accept extra storage and hauling for a narrower downstream
  ingredient.
- **Whether to simplify:** if the chain is not worth the labor, continue using raw
  oats through ordinary systems.

## Balance Analysis

### Balance Hypothesis

Milled oats are balanced if processing changes timing and downstream choice without
creating free value. The item should be useful only because FS-005 foods consume it.
On its own, it should be a narrower, shorter-keeping, no-premium version of raw
oats.

### Balance Targets

| Dimension | Target | Design intent |
|---|---:|---|
| Conversion ratio | 10 raw oats → 10 milled oats | Count-stable, easy to reason about, no free output |
| Nutrition accounting | 10 milled oats equal 0.5 raw-oat nutrition for recipe design | Preserves FS-001 raw-oat nutrition |
| Milling work | 180 work per batch | Meaningful preparation labor without dominating the chain |
| Direct eating | Not ordinary direct food | Prevents the intermediate from replacing raw oats or meals |
| Generic meal use | Not used by generic vanilla meals by default | Keeps the intermediate narrow and intentional |
| Shelf life | 30 days unrefrigerated before rot begins | No preservation bonus; shorter than raw oats |
| Stack limit | 75 units | Matches ordinary crop stack behavior |
| Mass | 0.03 per unit | No caravan mass advantage over raw oats |
| Market value | No higher than raw oats per unit | No labor-to-profit loop |
| Research | None | Version 0.1 early holding, not progression content |
| DLC dependency | None | Core behavior only |

### Required Tradeoffs

| Milled-oat benefit | Required cost or constraint |
|---|---|
| Prepared ingredient for oat foods | Raw oats lose flexibility once milled |
| Separates prep from final cooking | Adds a bill, hauling, storage, and 180 work |
| Enables a visible production chain | No nutrition, shelf-life, value, or mood bonus by itself |
| Supports low-tech food production | Throughput remains limited by pawn labor and hand quern access |

### Abuse and Failure Cases

The design fails if:

- conversion creates extra nutrition through item counts or recipe rounding;
- conversion creates a trade-profit loop;
- milled oats keep longer than raw oats without a specific approved reason;
- pawns eat milled oats as a preferred food and bypass intended recipes;
- generic meals consume milled oats and hide the processing choice;
- all raw oats must be milled before any reasonable use;
- the optimal player behavior is always to mill every oat immediately;
- the item ships without any downstream consumer in a player-facing release.

## Player Scenarios and Acceptance

1. **Given** a colony has raw oats and a hand quern, **when** the player creates a
   milling bill, **then** pawns convert raw oats into milled oats through ordinary
   bill, hauling, work, interruption, and output behavior.

2. **Given** raw oats are scarce, **when** the player chooses not to mill them,
   **then** raw oats remain usable through ordinary FS-001 food, feed, storage,
   trade, and caravan paths.

3. **Given** milled oats are produced, **when** they are stored unrefrigerated,
   **then** they do not keep longer than raw oats and do not create a preservation
   upgrade by themselves.

4. **Given** milled oats are present in storage, **when** ordinary vanilla meal
   production runs, **then** generic meal bills do not accidentally consume the
   processed ingredient unless that behavior is explicitly approved later.

5. **Given** milled oats are present but no FS-005 food consumes them, **when** the
   player-facing chain is reviewed for Gate 2, **then** the feature cannot be
   accepted as Done because the item is a dead intermediate.

6. **Given** the game is saved with raw oats, milled oats, hand-quern bills, and
   stored outputs, **when** the save is reloaded, **then** vanilla-persisted item
   and bill state returns without custom serialized data.

7. **Given** official DLC are absent or present, **when** the item, bill, storage,
   and later recipes are loaded, **then** no DLC is required and no optional DLC
   creates a hard dependency.

## Scope

### In

- One milled-oats ingredient item.
- One hand-quern milling recipe from raw oats to milled oats.
- Standard item storage, hauling, trade, rot, deterioration, stack, mass, bill, and
  save behavior.
- Compatibility with FS-003 Hand Quern and FS-005 Oat Foods.
- One original item icon sufficient to distinguish milled oats from raw oats,
  porridge, flatbread, flour, and other plant resources.
- English localization-ready label and description.

### Out

- Hand-quern building definition and art, except for the recipe-user relationship.
- Oat porridge, oat flatbread, or any final food.
- Direct cooking from raw oats unless invoked as a fallback during playtest.
- Generic flour, grain, dough, bread, baking, dehulling, drying, sifting, hull,
  bran, byproduct, or waste systems.
- Electric mills, watermills, windmills, animal mills, powered processing, or
  throughput upgrades.
- Cross-mod flour substitution or universal ingredient compatibility.
- Mood, health, medical, ideology, ritual, quality, social, or cultural bonuses.
- Custom C#, Harmony, custom jobs, custom UI, custom tickers, or custom serialized
  state.

## Technical Design

Implementation should use vanilla declarative item and recipe behavior:

- one passive ingredient item;
- one hand-quern recipe;
- narrow raw-oat input filter;
- narrow downstream recipe use by FS-005;
- standard storage, hauling, bill counting, rot, deterioration, stack, mass, value,
  trade, save/load, and localization behavior;
- no custom runtime assembly.

Public compatibility contracts created at implementation include the item
definition, translation keys, recipe identity, recipe-user relationship, texture
path, player-facing label, stockpile behavior, and saved item stacks.

If vanilla XML cannot express the approved narrow ingredient behavior, stop and
request review. Do not broaden the item into universal flour or add code silently.

## XML vs C# Decision

**Decision target:** XML-only.

Core RimWorld already supports passive items, recipes, ingredient filters, bills,
storage, rot, trade, save persistence, and localization. FS-004 does not require
custom logic, custom UI, custom serialization, or Harmony.

C# is not approved. Harmony is out of scope and would require a new ADR and
compatibility plan.

## Art Requirements

Required art is one original item icon that reads as coarse ground oats at normal
RimWorld zoom.

The icon must be visually distinct from:

- raw oats;
- porridge;
- flatbread;
- generic wheat flour from other mods;
- packaged modern oatmeal;
- loose sand, dust, stone, or ash.

The art should be modest and material-led. It should not use modern packaging,
decorative Irish motifs, bright green identity markers, or copied reference images.

## Audio Requirements

No custom audio is required. The item itself has no sound. Any work sound belongs
to the hand-quern production behavior and should use vanilla-compatible audio unless
a later release proves a custom sound materially improves comprehension.

## Localization

English source text uses the functional label `milled oats`.

Description requirements:

- describe it as ground oats prepared for cooking;
- state or imply that it is an ingredient, not a finished meal;
- avoid claiming a standardized historical product;
- avoid modern health-food, breakfast-cereal, or industrial-processing language;
- avoid Irish terminology unless qualified language review approves a localization
  entry.

## Testing

Gate 2 evidence must cover the full player path once the related FS-003 and FS-005
content exists:

- static XML validation for item and recipe definitions;
- clean Core-only load with no new unresolved errors or warnings;
- hand-quern bill creates milled oats from raw oats;
- bill suspension, interruption, target counts, ingredient search, and output
  hauling behave normally;
- raw oats remain usable through FS-001 paths without milling;
- milled oats do not unintentionally become preferred direct food, animal feed,
  generic meal input, nutrient-paste input, or universal flour;
- conversion ratio, nutrition accounting, market value, and rot behavior do not
  create a loop or hidden upgrade;
- storage, trade, caravan, food policy, and stockpile behavior are understandable;
- save/load works with raw oats, milled oats, active bills, suspended bills, and
  stored stacks;
- official DLC absence/presence does not create hard dependencies;
- at least one FS-005 food consumes milled oats before the player-facing chain is
  considered Done.

## Future Expansion

Later releases may consider powered mills, broader grain processing, flour
compatibility, food-framework integration, milling quality, or byproducts only if
real play evidence proves that Version 0.1’s narrow manual chain is useful and
needs scaling. FS-004 must not add placeholder categories, unused recipe hooks, or
generic abstractions for those possibilities.

## Dependencies

**Required DLC:** None. RimWorld 1.6 Core is required.

**Optional DLC enhancements:** None for Version 0.1.

**Behavior without DLC:** Full item and recipe behavior through Core item, bill,
storage, and recipe systems.

**Save compatibility:** Released item and recipe definitions become save contracts
for maps, stockpiles, bills, caravans, inventories, and later food recipes. Renaming
or removing them after release requires migration and missing-def analysis.

**Feature dependencies:**

- FS-001 Oats supplies the raw input.
- FS-003 Hand Quern supplies the production building.
- FS-005 Oat Foods must supply at least one consumer before the player-facing
  processing chain can pass Gate 2.

## Risks

| Risk | Likelihood | Impact | Mitigation | Owner |
|---|---|---:|---|---|
| Dead intermediate with no food use | High | High | Do not pass Gate 2 until at least one FS-005 consumer works | Maintainer |
| Mandatory busywork | High | High | Preserve raw-oat paths; compare direct cooking during playtest | Maintainer |
| Nutrition or value loop | Medium | High | Use count-stable conversion and test full-chain accounting | Implementer |
| Generic meals consume milled oats accidentally | Medium | High | Keep filters narrow; test vanilla meal and paste paths | Implementer |
| Work channel collapses into Cooking bottleneck | Medium | High | Use non-Cooking production labor or stop for review | Implementer |
| Extra hauling/storage overwhelms benefit | Medium | Medium | Use 10-unit batches and ordinary stack behavior; playtest stock targets | Maintainer |
| Art reads as flour, dust, or packaged oatmeal | Medium | Medium | Validate original icon beside raw oats and future foods | Maintainer |
| Cross-mod flour expectations create compatibility pressure | Medium | Medium | Namespace narrowly; no universal flour claims | Maintainer |
| Scope expands into grain framework | Medium | High | Enforce out-of-scope list; require ADR for broader systems | Maintainer |

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
- [x] Dependencies are explicit: FS-004 should be implemented with FS-003, and the
      player-facing chain cannot pass Gate 2 without an FS-005 food consumer.

**Decision:** Approved<br>
**Approved by/date:** Patrick Mee, 2026-07-07<br>
**Conditions:** Implementation must wait until FS-005 is approved and then proceed
as a bundled quern/milled-oats/first-food vertical slice. A player-facing quern
recipe that produces a dead ingredient is not Done.

## Gate 2: Evidence

Bundled implementation and technical validation are recorded in
[FS-003/FS-004/FS-005 Oat Processing Test Evidence](../qa/evidence/FS-003-004-005-oat-processing-test-matrix.md).

Static validation, package staging, release-safety checks, texture path checks,
the dedicated quern work giver, and maintainer-provided in-game production-path
evidence pass. `EI_MilledOats` is no longer a dead intermediate because oat
porridge and oat flatbread consume it through vanilla cooking stations.

Patrick Mee completed the final in-game smoke test for the exact staged package
on 2026-07-10 and confirmed that the oat-processing path works correctly.

**Decision:** Done<br>
**Approved by/date:** Patrick Mee, 2026-07-10

## Open Questions and Decisions

| Question | Owner | Due point | Status |
|---|---|---|---|
| Should implementation wait for FS-005 so the first processing slice includes a useful food consumer? | Patrick Mee | Before implementation starts | Resolved 2026-07-07: yes |
| Can RimWorld 1.6 XML express non-Cooking hand-quern labor with narrow recipe filters? | Implementer | During implementation discovery | Verify before XML finalization |
| Does direct raw-oat cooking provide equivalent gameplay with less friction? | Maintainer | Complete-chain playtest after FS-005 | Must simplify if yes |
