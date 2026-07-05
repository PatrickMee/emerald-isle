# AR-001 — Oats Architecture Review

**Status:** Approved<br>
**Approved by/date:** Patrick Mee, 2026-07-05<br>
**Feature:** [FS-001 — Oats](../specifications/FS-001-oats.md)<br>
**Milestone:** Version 0.1 — The First Holding<br>
**Owner:** Patrick Mee<br>
**Prepared:** 2026-07-05<br>
**Vanilla reference build:** RimWorld 1.6.4871 rev595<br>
**Implementation authorized:** Yes — Patrick Mee, 2026-07-05

## Decision Summary

FS-001 is implemented as two original RimWorld Core definitions: one cultivated oat
plant and one harvested raw-oat item. Both use existing vanilla inheritance,
categories, work, plant, ingestion, storage, trade, rendering, localization, and
serialization behavior. No vanilla or DLC definition is patched.

The architecture adds no C# assembly, Harmony patch, custom component, custom save
state, new category, new research project, or DLC adapter. It creates a narrow input
contract for later Version 0.1 milling and food specifications through the harvested
item identifier `EI_RawOats`.

## Feature Boundaries

### Implemented by FS-001

- One player-sowable oat plant available without research.
- One harvested raw-oat item.
- The exact lifecycle, work, nutrition, fertility, storage, trade, food, animal, and
  hydroponics behavior frozen in FS-001.
- Vanilla growing-zone, plant-work, cooking, nutrient-paste, food-policy, animal,
  storage, caravan, and trade integration through existing Core contracts.
- Original plant and item textures.
- English def-injected localization for both public definitions.
- Static, in-game, save, DLC, compatibility, visual, performance, and balance-test
  evidence for the feature.

### Explicitly Not Implemented

- Hand Quern, Milled Oats, Oat Porridge, Oat Flatbread, or any recipe.
- New research, work type, designation category, thing category, ingredient category,
  stat, job, alert, gizmo, user interface, or runtime behavior.
- Straw, seeds, chaff, drying, threshing, crop rotation, disease, soil, rainfall,
  temperature, biome, or world-generation systems.
- Hydroponic or wild oat growth.
- Vanilla/DLC definition patches or automatic interoperability patches for other
  mods' oats.
- C#, Harmony, a compiled assembly, or custom serialized data.
- Package metadata, preview art, package identity, build tooling, or release
  integration. Those are Version 0.1 release-integration responsibilities.

## RimWorld Architecture

### Definition Boundary

| Public definition | Vanilla parent | Responsibility | References |
|---|---|---|---|
| `EI_Plant_Oats` | `PlantBase` | Cultivated plant lifecycle, sowing, growth, threats, harvest, grazing, and plant rendering | Harvests `EI_RawOats` |
| `EI_RawOats` | `PlantFoodRawBase` | Stackable raw food, ingestion, recipes, nutrition, animal feeding, storage, rot, trade, caravan use, and item rendering | Used by `EI_Plant_Oats`; later features may consume it |

The plant follows the current Core rice/potato structural pattern for ordinary food
crops while applying only values frozen in FS-001. The raw item follows the current
Core raw-rice structural pattern because rice is the closest grain contract. Parent
inheritance supplies standard behavior; the feature overrides only identity,
references, graphics, and FS-001 values.

No new abstract parent is created. Two definitions do not justify a shared Emerald
Isle crop framework.

### Frozen Behavior Mapping

This table maps approved design requirements to existing RimWorld capabilities. It
does not prescribe XML syntax.

| FS-001 contract | Vanilla capability used |
|---|---|
| Start-available crop, no skill or research minimum | Standard cultivated plant availability with no research prerequisite and no sow-skill threshold |
| Ground at 70% fertility or higher; no hydroponics | Plant fertility threshold and ground-only sowing tag |
| 8.0 grow days, fertility sensitivity 1.0 | Standard plant growth and fertility calculation |
| 170 sow work, 200 harvest work, yield 15 | Standard grower sow/harvest work and plant harvest yield |
| Growing-plant nutrition 0.30 | Standard plant ingestion nutrition |
| Normal blight, fire, damage, light, temperature, rest, grazing, and harvest failure | Core `Plant` behavior and normal grower jobs |
| Raw nutrition 0.05, raw-bad preference, 2% fixed human poisoning chance | `PlantFoodRawBase` ingestion behavior |
| Seed-type animal and human diet compatibility | Existing `Seed` food type |
| Ordinary meals, fine/lavish meals where valid, survival meals, and nutrient paste | Existing `PlantFoodRaw` → `FoodRaw` category hierarchy and vanilla recipe/hopper filters |
| Stack 75, mass 0.03, market value 1.1 | Standard resource stacking, mass, and trade stats |
| Rot after 45 unrefrigerated days; normal deterioration | Standard rottable component and organic-product deterioration |
| Normal trader eligibility without guaranteed stock | Existing raw-food category stock generators and standard tradeability |
| Standard food policies, stockpiles, shelves, caravans, and save/load | Existing Thing filters, storage, transfer, and definition-based serialization |

Any implementation requirement not traceable to this table or FS-001 is a scope
change. If a missing value affects gameplay, implementation stops and returns to a
formal specification amendment; architecture may not invent it.

### Vanilla Systems Used

| System | Use | Change to vanilla content |
|---|---|---|
| Definition database and inheritance | Load the two public definitions from Core parents | None |
| Plant system | Growth, health, light/temperature checks, resting, blight, fire, damage, grazing, and harvest readiness | None |
| Growing zones | Expose oats in the normal crop selector and enforce ground-only sowing | None |
| Grower work | Use normal sow, cut, and harvest work assignment and skill effects | None |
| Harvest system | Convert a mature oat plant into the approved base yield of raw oats | None |
| Fertility and terrain | Read existing terrain fertility and apply the normal sensitivity curve | None |
| Research | No research dependency or unlock is created | None |
| Nutrition and ingestion | Provide raw nutrition, raw-food preference, poisoning chance, and plant/seed diet flags | None |
| Recipe filtering | Make raw oats eligible through the existing raw-plant-food hierarchy | None |
| Nutrient paste | Allow hopper selection through existing raw-food storage filters | None |
| Food policies | Allow/forbid oats through the standard per-definition food filter | None |
| Animal feeding | Permit animals whose diets include seeds or plants to eat the corresponding item or crop | None |
| Storage and hauling | Use normal thing categories, stockpiles, shelves, stacks, mass, and hauling jobs | None |
| Rot and deterioration | Use the standard rottable and organic-product behavior | None |
| Trade and trader stock | Use standard tradeability and category-based raw-food stock generation | None |
| Caravans | Use normal item transfer, mass, nutrition, and consumption behavior | None |
| Graphics and UI | Use normal plant/item graphics in the map, crop selector, inspect pane, resource list, bills, trade, and caravan UI | None |
| Localization | Use English def-injected labels and descriptions | None |
| Save/load | Persist normal plant and Thing state through public definition references | None |

### Structural Values Not Reopened by Architecture

FS-001 defines all intentional gameplay values. Ordinary structural behavior not
called out by the specification follows the closest current Core grain pattern:

- the plant is selectable, uses normal food-crop harvest tags and purpose, dies when
  leafless, and uses normal low crop path cost and wind response;
- plant durability uses the ordinary low food-crop baseline rather than corn's tall,
  tougher profile;
- the raw item uses standard grain sounds, organic-item hit points, deterioration,
  resource stacking, and all-party tradeability; and
- rot destroys the raw item as it does comparable raw crops.

These are implementation defaults required to realize “normal cultivated crop” and
“comparable raw plant food” from FS-001. Changing them to create a new strength or
weakness is prohibited without amending the specification.

## Required Assets

### Game-Ready Textures

| Asset ID | File | Runtime texture path | Purpose |
|---|---|---|---|
| `EI_Plant_Oats_Mature_A` | `Textures/Things/Plant/Oats/EI_Plant_Oats/EI_Plant_Oats_a.png` | `Things/Plant/Oats/EI_Plant_Oats` | First mature plant variation |
| `EI_Plant_Oats_Mature_B` | `Textures/Things/Plant/Oats/EI_Plant_Oats/EI_Plant_Oats_b.png` | `Things/Plant/Oats/EI_Plant_Oats` | Second mature plant variation to avoid visible tiling |
| `EI_Plant_Oats_Immature_A` | `Textures/Things/Plant/Oats/EI_Plant_Oats_Immature/EI_Plant_Oats_Immature_a.png` | `Things/Plant/Oats/EI_Plant_Oats_Immature` | First immature plant variation |
| `EI_Plant_Oats_Immature_B` | `Textures/Things/Plant/Oats/EI_Plant_Oats_Immature/EI_Plant_Oats_Immature_b.png` | `Things/Plant/Oats/EI_Plant_Oats_Immature` | Second immature plant variation |
| `EI_RawOats_Item` | `Textures/Things/Item/Resource/PlantFoodRaw/EI_RawOats.png` | `Things/Item/Resource/PlantFoodRaw/EI_RawOats` | Harvested-item map and UI graphic |

RimWorld 1.6 resolves each `Graphic_Random` path as a folder containing the variant
PNGs. The first in-game load exposed and corrected an invalid flat-file layout; the
public runtime paths did not change. All exports must be original, case-correct PNGs
with transparency and recorded provenance.

No separate crop-selector, command, trade, inventory, or resource icon is required;
RimWorld derives those views from the plant or harvested-item graphic. No audio asset
is required; existing plant, harvest, grain-drop, and eating sounds are reused.

### Localization Contract

`Languages/English/DefInjected/ThingDef/EI_Oats.xml` owns four stable entries:

| Key | Approved English source text |
|---|---|
| `EI_Plant_Oats.label` | `oat plant` |
| `EI_Plant_Oats.description` | `A medium-cycle grain crop. It matures more slowly than rice but sooner than corn, producing oats for food, feed, trade, storage, and processing.` |
| `EI_RawOats.label` | `oats` |
| `EI_RawOats.description` | `Harvested oat grain. It can be eaten raw, cooked, fed to animals, stored, traded, or processed into other foods.` |

No keyed translation entry and no player-facing Irish term is needed. Translator
context must identify both entries as functional English UI, not a claim about a
specific historical cultivar.

### Asset Control

`docs/art/assets/FS-001-oats.md` records the art owner, references, source location,
license, export settings, dimensions, runtime paths, and acceptance screenshots.
Layered source art is not committed until the project adopts the required source-art
hosting/LFS decision. The five game-ready exports remain governed by the separate
creative-asset license.

### Package Metadata

FS-001 does not own or modify `About/About.xml`. Version 0.1 release integration
provides the approved package/build contract in
`docs/release/package-build-contract.md`. Its empty package passed static staging and
human RimWorld 1.6 Core load verification on 2026-07-05.

## File Plan

### Files Created During Implementation

| Path | Type | Purpose |
|---|---|---|
| `Defs/ThingDefs_Plants/EI_Oats.xml` | Gameplay XML | Define `EI_Plant_Oats` only |
| `Defs/ThingDefs_Items/EI_RawOats.xml` | Gameplay XML | Define `EI_RawOats` only |
| `Languages/English/DefInjected/ThingDef/EI_Oats.xml` | Localization XML | Supply the four stable English entries |
| `Textures/Things/Plant/Oats/EI_Plant_Oats/EI_Plant_Oats_a.png` | Texture | Mature variation A |
| `Textures/Things/Plant/Oats/EI_Plant_Oats/EI_Plant_Oats_b.png` | Texture | Mature variation B |
| `Textures/Things/Plant/Oats/EI_Plant_Oats_Immature/EI_Plant_Oats_Immature_a.png` | Texture | Immature variation A |
| `Textures/Things/Plant/Oats/EI_Plant_Oats_Immature/EI_Plant_Oats_Immature_b.png` | Texture | Immature variation B |
| `Textures/Things/Item/Resource/PlantFoodRaw/EI_RawOats.png` | Texture | Harvested raw-oat item |
| `docs/art/assets/FS-001-oats.md` | Asset record | Provenance, license, export, and visual acceptance evidence |
| `docs/qa/evidence/FS-001-oats-test-matrix.md` | Test record | Static, functional, save, DLC, compatibility, performance, visual, and balance evidence |

### Existing Files Modified During Implementation

| Path | Change |
|---|---|
| `docs/specifications/FS-001-oats.md` | Advance implementation/verification status and link evidence without changing frozen behavior |
| `docs/product/feature-catalog.md` | Record implementation and release state for PL-01 |
| `docs/glossary.md` | Add approved functional English terms `oat plant` and `oats` |
| `docs/project/risk-register.md` | Reconcile duplicate-content, save-removal, asset, and integration risks |
| `CHANGELOG.md` | Add the player-facing Oats change under the unreleased Version 0.1 section |

### Test Code and Package Files

FS-001 creates no C# or feature-specific test executable. Static validation is a
shared Version 0.1 build concern and must be supplied by the build-contract/release-
integration work before implementation starts. The Oats test record stores the exact
inputs, expected results, evidence, and dispositions required by the shared validator
and human in-game tests.

`About/About.xml`, preview art, load folders, build scripts, and release manifests are
not modified by FS-001. The release-integration owner must supply them independently.

## Compatibility Review

### RimWorld 1.6 Core

The architecture was checked against locally installed Core definitions from
RimWorld 1.6.4871 rev595. `PlantBase`, `PlantFoodRawBase`, `PlantFoodRaw`, `FoodRaw`,
standard meal filters, hopper filters, raw-food trader generators, and vanilla plant
work provide the complete required surface.

The support policy covers RimWorld 1.6, not only this revision. Any later 1.6 update
requires definition-load and behavior revalidation before a compatibility claim.

### Supported DLC

No DLC definition is referenced and no DLC load folder or patch is created.

| Configuration | Architecture result |
|---|---|
| Core only | Full feature |
| Core + Royalty | Same Core definitions and behavior |
| Core + Ideology | Same definitions; existing ideology food rules observe normal raw-plant-food classification |
| Core + Biotech | Same definitions; existing plant/pollution behavior applies without an Emerald Isle adapter |
| Core + Anomaly | Same definitions; no anomaly content reference |
| Core + Odyssey | Same definitions; no biome, vacuum, or travel adapter |
| All supported DLC | One copy of each Oats definition; no conditional content |

### Vanilla Expanded Philosophy and Mods

The design follows the relevant vanilla-expanded philosophy: additive content,
familiar systems, vanilla visual scale, no global overrides, and no framework
dependency. That is a design statement, not a blanket compatibility claim with every
Vanilla Expanded mod.

If a current RimWorld 1.6 Vanilla Expanded crop pack supplies another oat crop, both
features may coexist under distinct public identifiers. FS-001 does not merge items,
rewrite recipes, add load-order metadata, or claim semantic equivalence. A current
installed version may be tested and classified under the project compatibility
policy; without exact version and in-game evidence it remains Unassessed.

### Existing Saves

- Adding the two definitions to an existing 1.6 save creates no retroactive plants,
  fields, stacks, policies, or bills. Oats become available for future use.
- Saving and loading relies only on normal plant and Thing state plus the two public
  definition references.
- Removing Emerald Isle from a save containing planted or stored oats may drop
  content or produce missing-definition warnings. FS-001 does not claim S3
  removal-safe compatibility.
- The first public Version 0.1 release should claim no more than S1 same-version save
  compatibility until release evidence supports a stronger level.

### Future Emerald Isle Features

- `EI_RawOats` is the sole Oats input contract for Hand Quern, Milled Oats, and Oat
  Foods.
- Future recipes should filter the exact public item where exclusivity is intended;
  FS-001 does not create a generic flour or grain framework.
- Later features may add recipes that consume `EI_RawOats` but may not rename it,
  remove its vanilla raw-food category, or alter the FS-001 lifecycle without an
  approved specification amendment and migration review.
- No future feature may depend on the physical XML file name; only public definitions
  and documented runtime paths are contracts.

## Save and Compatibility Contracts

These names become durable once a public build containing FS-001 is released:

| Contract | Identifier or path | Consequence of change |
|---|---|---|
| Plant definition | `EI_Plant_Oats` | Existing planted crops and references can break or disappear |
| Harvested-item definition | `EI_RawOats` | Stored stacks, caravans, bills, policies, recipes, and later features can break |
| Plant label key | `EI_Plant_Oats.label` | Existing translations become orphaned |
| Plant description key | `EI_Plant_Oats.description` | Existing translations become orphaned |
| Item label key | `EI_RawOats.label` | Existing translations become orphaned |
| Item description key | `EI_RawOats.description` | Existing translations become orphaned |
| Mature plant texture stem | `Things/Plant/Oats/EI_Plant_Oats` | Released definitions and replacement art references break |
| Immature plant texture stem | `Things/Plant/Oats/EI_Plant_Oats_Immature` | Immature rendering breaks |
| Raw-item texture path | `Things/Item/Resource/PlantFoodRaw/EI_RawOats` | Map and UI rendering breaks |

No research identifier, recipe identifier, C# type, serialized field, API, or Harmony
target is created. The repository package ID will also be a compatibility contract,
but it belongs to release integration and is not selected by AR-001.

## Risks

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Core parent or filter behavior changes in a later 1.6 update | Low | High | Re-run load, recipe, hopper, animal, trade, and save tests against the exact supported build |
| Broad `PlantFoodRaw` membership integrates with more recipes than expected | Medium | Medium | Treat broad vanilla compatibility as intentional per FS-001; enumerate actual recipe and hopper behavior in evidence |
| Random plant texture naming or discovery is incorrect | Medium | Medium | Prove both texture stems in the first asset-loading checkpoint before content work continues |
| Case mismatch works on one platform and fails on another | Medium | High | Enforce exact case in paths and validate from a clean case-sensitive package |
| Another mod exposes a duplicate player-facing oat label | High | Medium | Preserve unique public IDs, avoid automatic unification, and document coexistence |
| Public definitions are renamed after saves or later recipes depend on them | Low | High | Freeze IDs at first release; require migration analysis for any change |
| Mod removal loses planted or stored oats | High when removed | Medium | Declare the supported save level and publish removal limitations |
| Package staging regresses or diverges from the tested artifact | Low | High | Re-run ADR-0002 static and Core-only smoke checks after metadata or staging changes |
| Art provenance or redistribution rights are incomplete | Low | High | Require the asset record and license review before committing game-ready exports |
| A future food chain pressures FS-001 into a generic grain framework | Medium | Medium | Keep one exact item contract; require future specs to justify any new abstraction |

## Constitution Review

| Principle | Result | Evidence |
|---|---|---|
| XML-first | Pass | Two Core definitions and def-injected localization; no code or patch |
| Simplicity | Pass | Two definitions, five texture exports, one locale, no framework or custom category |
| Vanilla feel | Pass | Existing plant, work, food, animal, storage, trade, caravan, UI, and save systems only |
| Scope discipline | Pass | All quern, milled-oat, food, research, package, and release work remains outside FS-001 |
| Long-term maintainability | Pass | Stable names, narrow dependency direction, no runtime code, no external-mod coupling |
| Tradeoffs and gameplay | Pass by frozen spec | Architecture reproduces FS-001 values without tuning or new advantages |
| Whole-system verification | Pass for planning | File plan and test matrix cover the full player path, save state, DLC, performance, and failure cases |
| Modular compatibility | Pass | Core-only definitions; optional content absent safely; future features depend only on `EI_RawOats` |

## ADR Review and Architecture Recommendation

[ADR-0001](../adr/0001-oats-medium-cycle-xml.md) is satisfied. AR-001 introduces no
Harmony patch, assembly, save schema, API, hard dependency, or shared framework, so
it does not require a new feature ADR.

The repository-wide build/package contract required by
`docs/engineering/build-strategy.md` is defined by accepted ADR-0002 and
`docs/release/package-build-contract.md`. The package gate is complete.

**Decision:** Approved by Patrick Mee on 2026-07-05. Definition of Ready and explicit
implementation authorization passed later that day. Post-implementation verification,
playtesting, Design Review, and release gates remain mandatory.
