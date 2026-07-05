# FS-001 Oats Test Evidence

**Status:** Feature implementation and Design Review approved; release integration pending<br>
**Feature:** [FS-001 — Oats](../../specifications/FS-001-oats.md)<br>
**Test date:** 2026-07-05<br>
**Tester:** Codex; human in-game reviewer Patrick Mee

## Environment

| Input | Value |
|---|---|
| Installed RimWorld data | `1.6.4871 rev595` |
| Last recorded RimWorld config | `1.6.4871 rev597` |
| Platform | macOS |
| Package ID | `patrickmee.emeraldisle` |
| Source branch | `003-oats-specification` |
| Staging command | `./tools/stage-mod.sh` |
| Staged package | `build/EmeraldIsle` |

The differing installed-data and last-config revision values are recorded rather
than reconciled by assumption. Human verification must report the build displayed by
the launched game.

## Completed Technical Checks

| Check | Result | Evidence |
|---|---|---|
| Shell syntax | Pass | `bash -n tools/stage-mod.sh` |
| XML well-formedness | Pass | `xmllint --noout` on metadata, both defs, and localization |
| Package staging | Pass | Nine allowlisted runtime files staged successfully |
| Package identity | Pass | `patrickmee.emeraldisle`, supported version `1.6` |
| Public identifiers | Pass | `EI_Plant_Oats`, `EI_RawOats` |
| Installed Core/DLC collision | Pass | Neither public identifier exists in installed game defs |
| Texture contract | Pass | Five case-correct 128×128 RGBA PNGs with alpha |
| Prohibited implementation | Pass | No C#, assembly, Harmony, patch, hydroponic tag, research gate, or secondary product |
| Source/package separation | Pass | Staged package excludes documentation, source intermediates, Git files, and `.gitkeep` markers |

## Specification Contract Check

Static inspection confirms the explicit FS-001 values: 8.0 grow days, yield 15,
plant nutrition 0.30, ground-only sowing, inherited fertility minimum 0.70 and
sensitivity 1.0, inherited sow/harvest work 170/200, raw nutrition 0.05, Seed food
type, market value 1.1, stack limit 75, mass 0.03, and rot start at 45 days. Values
listed as inherited were verified against the installed RimWorld 1.6 Core parent
definitions.

## Proportional Verification Disposition

FS-001 is a two-definition, XML-only feature with no code, patch, DLC reference,
custom state, custom job, or recurring runtime work. The initial Core player path,
graphics, base values, save/reload, packaging, and logs were tested directly. The
remaining behavior is inherited from verified RimWorld 1.6 Core parents.

Repeating every inherited food, animal, trade, caravan, threat, DLC, and persistence
path for this isolated crop would add little defect-detection value. Those checks are
deferred to the Version 0.1 integrated production-chain and release tests, where
failures and balance interactions can be observed in their real context.

## Defect Record

### UI-001 — Missing Crop Icon and Plant Graphics

**Observed:** The first installed build displayed `Oat plant` in the crop selector
without an icon. `Player.log` reported that no textures were found at either mature
or immature plant path.

**Cause:** The four variant PNGs were placed beside the configured
`Graphic_Random` paths. RimWorld 1.6 treats each configured path as a folder and
loads the collection from files inside it.

**Correction:** The mature and immature variants were moved into folders matching
their unchanged public runtime paths. No definition name, gameplay behavior, XML
texture path, or art content changed.

**Regression check:** Resolved. Crop selector shows plant icon, mature and immature
textures render in-game, no `Collection cannot init` messages in Player.log.

---

## In-Game Verification — Checkpoints 0–3

**Session:** 2026-07-05<br>
**Tester:** Patrick Mee<br>
**RimWorld build:** 1.6.4871 rev597<br>
**Mod list:** Core + Emerald Isle only<br>
**Staging command:** `./tools/stage-mod.sh` (no `--verify-empty`)

### Checkpoint 0 — Empty Package Load

| Check | Result | Evidence |
|---|---|---|
| Emerald Isle appears in Mods list | Pass | Correct name and author, no unsupported-version warning |
| Core + Emerald Isle restart is clean | Pass | Player.log: `patrickmee.emeraldisle` loaded, `Mod Emerald Isle did not load any content` (expected for empty package), no EI errors |

### Checkpoint 2 — EI_RawOats Item

Dev-spawned `EI_RawOats` in a Core-only colony.

| Check | Required | Actual | Result |
|---|---|---|---|
| Label | `oats` | Oats | Pass |
| Description | AR-001 approved text | Matches exactly | Pass |
| Market value | 1.1 | $1.10 | Pass |
| Nutrition | 0.05 | 0.05 | Pass |
| Mass | 0.03 kg | 0.03 kg | Pass |
| Food poison chance | 2% | 2% | Pass |
| Category | PlantFoodRaw → FoodRaw | Vegetarian \ Raw food \ Foods | Pass |
| Stack size | 75 | 75 | Pass (XML) |
| Rot start | 45 days unrefrigerated | "spoils in 45 days" | Pass |
| Deterioration | Normal outdoor rate | 6 / day unroofed outdoors | Pass |
| Hit points | Standard organic | 60 / 60 | Pass |
| Source | Emerald Isle | Emerald Isle | Pass |
| Log clean | No EI errors | No EI_ errors in Player.log | Pass |

### Checkpoint 3 — EI_Plant_Oats

Core-only colony, dev mode. Plants force-matured via debug action due to cold biome.
Cold death also observed (recorded under AC-011).

| Check | Required | Actual | Result |
|---|---|---|---|
| Crop selector visibility | Without research | Visible, no research requirement | Pass |
| Normal sow behaviour | Standard grower job | Pawn activity "Sowing oat plant" | Pass |
| Grow days | 8.0 | 8.0 | Pass (XML) |
| Base harvest yield | 15 raw oats | 15 | Pass (XML; in-game yield consistent with 15 × Plants-2 modifier) |
| Harvested item | EI_RawOats only | Oats stack, no secondary item | Pass |
| Harvest via normal Core job | Standard harvest job | Normal harvest job completed | Pass |
| Plant art — mature | Readable panicle at normal zoom | Golden panicle silhouette, distinct from vanilla vegetation | Pass |
| Cold threat (AC-011 partial) | Normal cultivated-crop rules | Plants died from cold through normal temperature rules | Pass |
| Basic save/reload | Plants and harvested items persist | Confirmed by Patrick Mee | Pass |
| Log clean | No EI errors | No EI_ errors in Player.log | Pass |

### Acceptance Criteria Status

| AC | Description | Status | Notes |
|---|---|---|---|
| AC-001 | Available without research | Pass | Confirmed in-game |
| AC-002 | Planting boundary: 70%+ fertility, no hydroponics | Pass | `PlantBase` fertility minimum plus Ground-only sow tag; no override |
| AC-003 | 8.0 grow days | Pass | XML confirmed |
| AC-004 | Base yield 15, no secondary | Pass | XML confirmed |
| AC-005 | Fertility sensitivity 1.0 | Pass | Verified inherited Core parent value |
| AC-006 | Nutrition 0.05, RawBad, 2% poison | Pass | In-game inspect |
| AC-007 | Vanilla food integration | Pass | Verified `PlantFoodRawBase`/`PlantFoodRaw` contract; integrated recipe smoke deferred to release |
| AC-008 | Animal integration | Pass | Verified Seed/Plant food types and Core ingestion contract |
| AC-009 | Stack 75, mass 0.03, rot 45 days | Pass | XML + in-game inspect |
| AC-010 | Market value 1.1, normal trade | Pass | In-game inspect |
| AC-011 | Normal threats (cold, blight, fire, grazing) | Pass | Cold confirmed; all other behavior inherited without custom override |
| AC-012 | Save/load | Pass | Basic plant/item save-reload passed; no custom state exists |
| AC-013 | DLC absence | Pass | Core-only load passed; package contains no DLC reference or conditional content |
| AC-014 | Art distinguishable from rice/corn/haygrass | Pass | Selector, mature/immature plant, and item graphics accepted in-game |
| AC-015 | Performance | Pass | No code, patch, custom comp, scan, or per-tick work; vanilla plant rendering only |
| AC-016 | Scope (no C#, Harmony, secondary, research, wild spawn) | Pass | Staged package confirmed by staging script |

## Design Review

| Area | Assessment | Evidence and disposition |
|---|---|---|
| Gameplay | Pass | Medium-cycle crop and raw-versus-processed choice are visible; raw-food dislike preserves the future processing incentive |
| Historical authenticity | Pass | Implementation stays within approved early-medieval oat evidence and makes no hardiness or cultivar claim |
| Vanilla fit | Pass | Standard growing, harvest, raw-food, storage, trade, rendering, and save contracts only |
| Technical quality | Pass | XML is well formed, public IDs are stable, package and installed build match, and the log is clean |
| Balance | Pass with release condition | Frozen numbers preserve the intended rice/potato/corn tradeoffs; whole-chain balance is tested when milling and oat foods exist |
| Scope discipline | Pass | One crop, one harvested item, five textures, one locale; no downstream feature or speculative framework |
| Maintainability | Pass | Two small defs, no code or patches, exact Core parents, and documented public contracts |
| Compatibility | Pass with release condition | Core-only smoke and save/reload pass; one all-supported-DLC smoke remains a Version 0.1 release test |

**AI assessment:** Pass with Version 0.1 integration/release conditions.<br>
**Human Design Review:** Approved by Patrick Mee, 2026-07-05.<br>
**Deferred release checks:** whole oat-chain balance, one all-supported-DLC clean-load
smoke, exact release-package save/load, and targeted regression of any integration
that later modifies raw-oat use.
