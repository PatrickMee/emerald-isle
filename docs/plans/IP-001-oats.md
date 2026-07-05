# IP-001 — Oats Implementation Plan

**Status:** Approved<br>
**Approved by/date:** Patrick Mee, 2026-07-05<br>
**Feature:** [FS-001 — Oats](../specifications/FS-001-oats.md)<br>
**Architecture:** [AR-001 — Oats](../architecture/AR-001-oats.md)<br>
**Milestone:** Version 0.1 — The First Holding<br>
**Branch:** `003-oats-specification`<br>
**Owner:** Patrick Mee<br>
**Prepared:** 2026-07-05<br>
**Implementation authorized:** Yes — Patrick Mee, 2026-07-05

## Objective

Implement the frozen FS-001 behavior through the smallest Core-only architecture in
AR-001, then produce static, in-game, save, compatibility, performance, visual, and
balance evidence. This plan makes no gameplay or balance decision. If implementation
cannot reproduce FS-001 exactly, work stops and returns to specification review.

No XML, C#, texture, package metadata, or implementation work is created by this
planning document.

## Required Inputs

- [FS-001 — Oats](../specifications/FS-001-oats.md), approved and frozen.
- [AR-001 — Oats](../architecture/AR-001-oats.md), approved.
- [ADR-0001](../adr/0001-oats-medium-cycle-xml.md), accepted.
- [Oats research](../research/version-0.1/oats.md), approved.
- [Version 0.1 approved scope](../product/version-0.1-approved-scope.md), frozen.
- RimWorld 1.6 Core and the officially supported DLC test installations.
- The Version 0.1 package/build contract, including a loadable `About/About.xml`,
  package ID, staging command, static validator, and clean test installation.

## Start Gate

Implementation may begin only after all of these are true:

- [x] Human architecture review approves AR-001.
- [x] Human implementation-plan review approves IP-001.
- [x] The Feature Acceptance Checklist says Accept for planning.
- [x] The Version 0.1 build/package contract exists and ADR-0002 is accepted.
- [x] Art production must record its producer and provenance; Patrick Mee owns human
      art acceptance under the creative-asset policy.
- [x] The FS-001 Definition of Ready is completed and approved by Patrick Mee.
- [x] Patrick Mee explicitly authorizes implementation.

All start-gate items passed on 2026-07-05. This record authorizes implementation but
does not mark the feature complete or released.

## Definition of Ready Record

| Area | Result | Evidence |
|---|---|---|
| Product and identity | Pass | PL-01, frozen Version 0.1 scope, FS-001, Constitution, and Design Bible |
| Evidence and design | Pass | Approved Oats research, frozen balance/acceptance scenarios, art and localization requirements |
| Engineering | Pass | ADR-0001, accepted ADR-0002, approved AR-001/IP-001, XML-only boundary, save/DLC/performance/test plan |
| Delivery | Pass | Package gate verified in RimWorld 1.6; implementation slices and owners are actionable; no blocking question remains |

**Decision:** Ready<br>
**Approved by/date:** Patrick Mee, 2026-07-05<br>
**Conditions:** Preserve the frozen FS-001 behavior and stop for human review if
implementation exposes a missing gameplay decision or architecture conflict.

## Frozen Implementation Contract

The implementer must reproduce these contracts without tuning:

| Area | Required implementation outcome |
|---|---|
| Plant identity | Public definition `EI_Plant_Oats`, label `oat plant` |
| Item identity | Public definition `EI_RawOats`, label `oats` |
| Inheritance | Plant uses `PlantBase`; item uses `PlantFoodRawBase` |
| Availability | No research prerequisite and no sow-skill minimum |
| Sowing | Ground only, minimum fertility 0.70, no hydroponics |
| Growth | 8.0 grow days, fertility sensitivity 1.0 |
| Work and yield | 170 sow work, 200 harvest work, 15 raw oats at mature base harvest |
| Plant food | Full-growth plant nutrition 0.30; normal plant/RawBad grazing behavior |
| Raw item | Nutrition 0.05, RawBad, 2% fixed human poisoning chance, Seed food type |
| Economy | Market value 1.1; normal raw-food trade eligibility; no dedicated stock rule |
| Logistics | Stack 75, mass 0.03, 45-day rot start, normal deterioration |
| Integration | Existing `PlantFoodRaw`/`FoodRaw` hierarchy; normal recipes, paste, policies, animals, storage, caravans, and trade |
| Threats and saves | Normal Core plant/item behavior and definition-based persistence |
| DLC | No required or optional DLC content; same Core feature in every supported configuration |
| Runtime | No C#, Harmony, custom component, custom state, custom UI, patch, or new framework |

Non-design structural values follow the exact current Core grain pattern identified
in AR-001. An implementer may not add convenience behavior, compatibility patches,
extra art states, categories, defs, recipes, or abstractions.

## Planned Files

### Create

1. `docs/art/assets/FS-001-oats.md`
2. `Textures/Things/Plant/Oats/EI_Plant_Oats/EI_Plant_Oats_a.png`
3. `Textures/Things/Plant/Oats/EI_Plant_Oats/EI_Plant_Oats_b.png`
4. `Textures/Things/Plant/Oats/EI_Plant_Oats_Immature/EI_Plant_Oats_Immature_a.png`
5. `Textures/Things/Plant/Oats/EI_Plant_Oats_Immature/EI_Plant_Oats_Immature_b.png`
6. `Textures/Things/Item/Resource/PlantFoodRaw/EI_RawOats.png`
7. `Languages/English/DefInjected/ThingDef/EI_Oats.xml`
8. `Defs/ThingDefs_Items/EI_RawOats.xml`
9. `Defs/ThingDefs_Plants/EI_Oats.xml`
10. `docs/qa/evidence/FS-001-oats-test-matrix.md`

### Modify

1. `docs/specifications/FS-001-oats.md`
2. `docs/product/feature-catalog.md`
3. `docs/glossary.md`
4. `docs/project/risk-register.md`
5. `CHANGELOG.md`

### Explicitly Untouched

- `About/About.xml` and preview art: release-integration ownership.
- `Patches/`: no vanilla, DLC, or mod patch is allowed.
- `Assemblies/` and `Source/`: no C# or compiled output is allowed.
- DLC/load-folder directories: no conditional content is needed.
- Other feature specifications and definitions: FS-001 cannot implement downstream
  content.

## Order of Work

### Milestone 0 — Confirm the Gate and Environment

1. Record AR-001 and IP-001 human approvals.
2. Complete the FS-001 Definition of Ready and explicit implementation authorization.
3. Confirm the current Git branch contains only approved FS-001 and prerequisite
   package/build changes.
4. Record the exact RimWorld build, operating system, DLC versions, clean mod list,
   build command, staged-package path, and Player.log location in the test record.
5. Verify that the shared static validator and clean package staging process work on
   a package with no Oats content.

**Checkpoint 0:** No gameplay file is created until all start-gate items pass. The
empty/base package loads in Core without an Emerald Isle error.

### Milestone 1 — Produce and Approve Art Assets

1. Create the asset record with gameplay function, references, creator, source
   location, license, export settings, runtime paths, and required acceptance views.
2. Produce mature silhouette sketches and compare them in grayscale against rice,
   corn, haygrass, and blight at normal zoom.
3. Produce two mature variants with a shared oat-panicle identity and enough
   variation to avoid obvious tiling.
4. Produce two immature variants that remain recognizably related to the mature crop
   without being confused with rice or haygrass.
5. Produce the harvested-item graphic and check readability as a single item, a
   stack, and a small UI icon.
6. Export the five final PNGs with exact casing and transparency. Record checksums
   and export settings in the asset record.
7. Use a minimal package load to verify current random-graphic filename discovery and
   all three runtime texture paths before freezing the exports.

**Checkpoint 1:** Art reviewer accepts silhouette, scale, case, state distinction,
provenance, and license. Every texture resolves from a clean staged package. No
temporary or unlicensed art remains.

### Milestone 2 — Add Localization and Raw-Oat Item

1. Add the four English def-injected entries exactly as frozen in AR-001.
2. Add the harvested item using `PlantFoodRawBase`.
3. Apply only the frozen raw-item identity, graphic, nutrition, food type, poisoning,
   stack, mass, value, rot, deterioration, sound, category, and trade contracts.
4. Confirm that no custom thing category, recipe filter, stock generator, comp, or
   patch was introduced.
5. Run static validation for parsing, duplicate identifiers, parent resolution,
   texture path, translation key, numeric contract, and filename case.

**Checkpoint 2:** A development-mode spawn of `EI_RawOats` shows the correct label,
description, graphic, stats, stack behavior, mass, value, rot contract, raw-food
preference, and no config/log error.

### Milestone 3 — Add the Oat Plant

1. Add the plant using `PlantBase` and reference `EI_RawOats` as its only harvest.
2. Apply the frozen ground sowing, fertility, growth, work, yield, nutrition,
   availability, graphic, and normal food-crop structural contracts.
3. Confirm there is no research prerequisite, hydroponic tag, wild spawn, secondary
   product, unique disease, custom temperature behavior, or new designation.
4. Run static validation across both definitions and every reference.
5. Load a clean Core-only colony and confirm oats appear in the normal crop selector.

**Checkpoint 3:** Oats designate, sow, grow, rest, inspect, take damage, blight, burn,
graze, cut, and harvest through normal Core behavior. A healthy mature base harvest
targets 15 `EI_RawOats`. The log is clean.

### Milestone 4 — Verify the Complete Core Player Path

1. Test a new colony and an existing pre-Oats save.
2. Verify ground and fertility boundaries, including rejection below 70% fertility
   and in hydroponics.
3. Verify raw eating, ordinary meal families, packaged survival meals when unlocked,
   nutrient-paste hopper selection, food policies, eligible/ineligible animals,
   stockpiles, shelves, refrigeration, freezing, deterioration, hauling, caravans,
   eligible traders, destruction, and rot.
4. Verify failed harvest and pawn-skill modifiers do not alter the frozen base
   contract.
5. Save and reload immature, mature, damaged, blighted, stored, rotting, caravaned,
   and trader-held oats.
6. Attempt documented mod removal on a disposable save and record the actual warning
   and loss behavior without claiming removal safety.

**Checkpoint 4:** AC-001 through AC-012 pass in Core only. The exact staged package,
save fixtures, screenshots, log excerpts, and results are linked from the test record.

### Milestone 5 — Verify DLC and Mod Compatibility

Test these configurations from clean staged packages:

1. Core only.
2. Core + Royalty.
3. Core + Ideology.
4. Core + Biotech.
5. Core + Anomaly.
6. Core + Odyssey.
7. Core + all officially supported DLC.

For each, test definition loading, crop availability, a short sow/harvest path,
raw-food classification, save/load, and a clean log. Add targeted Ideology food-rule,
Biotech plant/pollution, and Odyssey caravan/environment observations without adding
feature-specific behavior.

If a current RimWorld 1.6 Vanilla Expanded crop pack is available, record its exact
package ID, version, load order, and duplicate-oat behavior. Confirm coexistence
without ID collision or Emerald Isle patching. If no current test target is available,
record the integration as Unassessed rather than claiming compatibility.

**Checkpoint 5:** AC-013 passes. No DLC is required, no optional-content reference is
unresolved, each configuration contains one Emerald Isle plant and item definition,
and every compatibility claim has evidence.

### Milestone 6 — Verify Art, Performance, and Frozen Balance

1. Capture mature, immature, selected, damaged/blighted, snow, rain, darkness, rich
   soil, ordinary soil, stockpile, shelf, trade, caravan, and inventory views beside
   rice, corn, and haygrass.
2. Run the controlled 100-tile comparisons at 70%, 100%, and 140% fertility from
   FS-001. Record actual growth, yield, nutrition, sow/harvest work, hauling, storage,
   and spoilage.
3. Run the required seasonal two-year and year-round one-year colony tests.
4. Measure representative and worst-case large fields against the project performance
   budget and verify no custom recurring work or steady-state allocation exists.
5. Conduct the five-player comprehension test defined by FS-001.

Implementation may fix a defect that prevents the frozen values from being realized.
It may not tune those values. A balance, comprehension, or player-value failure stops
work and requests a reviewed FS-001 amendment.

**Checkpoint 6:** AC-014 and AC-015 plus every FS-001 balance success criterion pass.
Any failed gameplay hypothesis is escalated rather than silently tuned.

### Milestone 7 — Reconcile Documentation and Release Handoff

1. Complete the test matrix with build, environment, scenario, expected/actual result,
   evidence, date, tester, and disposition for every required case.
2. Update FS-001 status and link the approved architecture, implementation plan,
   asset record, and test record without editing frozen gameplay behavior.
3. Update PL-01 state in the Feature Catalog.
4. Add `oat plant` and `oats` to the Glossary as functional English UI terms.
5. Reconcile all FS-001 risks in the Risk Register.
6. Add the Oats feature to the unreleased changelog.
7. Verify the clean staged package contains only allowed runtime files and excludes
   source art, test evidence, editor backups, and local files.
8. Hand the exact staged package and evidence record to Version 0.1 release integration.

**Checkpoint 7:** The feature satisfies the project Definition of Done at feature
scope, documentation matches tested behavior, and release integration has an exact
artifact. Release remains a separate human gate.

## Test Checkpoints

| Gate | Required evidence | Stop condition |
|---|---|---|
| Static | XML parses; unique IDs; valid parents/references; exact values; translation and texture paths resolve; correct case; no prohibited folders/files | Any parse, reference, ID, path, value, or scope error |
| Asset | Provenance/license, export record, normal-zoom comparison, all required environmental/UI views | Missing rights, unreadable state, wrong case, or unresolved path |
| Core smoke | Clean startup, selector, sow, grow, harvest, spawn, inspect, consume, store, destroy, clean log | Any config error, missing asset/string, or broken primary path |
| Functional | AC-001 through AC-012 with screenshots/log/save fixtures | Any acceptance failure |
| Save/removal | New and existing save, state matrix, disposable removal test | Unexpected state loss within supported behavior or undocumented removal result |
| DLC | Core, five individual DLC configurations, all-DLC configuration | Required DLC, duplicate definition, unresolved reference, or behavior drift |
| Mod coexistence | Exact tested mod/version/load order or explicit Unassessed record | ID collision, forced patch, or unsupported compatibility claim |
| Performance | Representative and worst-case field measurements | Project investigation threshold exceeded or recurring Emerald Isle error/allocation |
| Balance/playtest | Controlled fields, long colonies, comprehension test | Any frozen success/failure criterion fails; return to specification review |
| Package | Exact clean staged artifact, manifest/checksum, no source/test/editor leakage | Developer-tree-only success or package mismatch |

## Asset Creation Order

1. Approve the asset record and references.
2. Approve mature silhouette and grayscale readability.
3. Produce mature variation pair.
4. Produce immature variation pair.
5. Produce harvested-item graphic.
6. Export and verify exact runtime paths and casing.
7. Validate in-game states and UI sizes.
8. Freeze exports for the tested build; later replacements retain the same paths.

No AI-generated or third-party asset may enter the package without the provenance,
license, and human art-direction controls required by the Art Guide.

## Documentation Update Order

1. Asset record at art production start.
2. Test record at environment setup; append evidence at every checkpoint.
3. Risk Register whenever a risk is discovered or resolved.
4. FS-001 status/evidence links after verification, without changing frozen behavior.
5. Feature Catalog and Glossary after player-visible behavior is verified.
6. Changelog after the exact staged artifact passes feature verification.

## Rollback and Failure Handling

- Before public release, rollback is a branch-level revert of all FS-001 runtime files
  and corresponding status claims. Do not leave orphaned localization or textures.
- A failed static or functional checkpoint returns to the smallest responsible file.
- A failed architecture assumption returns to AR-001 review and triggers an ADR only
  if the replacement introduces a durable architecture decision.
- A failed gameplay or balance criterion returns to the frozen specification; the
  implementer cannot tune values independently.
- After public release, `EI_Plant_Oats`, `EI_RawOats`, translation keys, and texture
  paths are compatibility contracts. Removal or rename requires migration analysis,
  release notes, save fixtures, and explicit support-level review.

## Plan Review Checklist

- [x] Every implementation file has an owner and purpose.
- [x] Work is ordered so assets and package validity are proven before full gameplay
  verification.
- [x] Every FS-001 acceptance criterion maps to a checkpoint.
- [x] Core, DLC, save, mod, performance, visual, balance, and package paths are covered.
- [x] No XML, C#, Harmony, gameplay content, balance change, or speculative framework
  is introduced by planning.
- [x] Scope failures and balance failures return to human review rather than being
  silently resolved during implementation.
- [x] The package/build prerequisite is explicit and cannot be mistaken for FS-001
  scope.

**Plan result:** Approved and Ready for implementation. Post-implementation
playtesting, Design Review, Definition of Done, and release approval remain required.
