# FS-001 Oats Test Evidence

**Status:** Checkpoints 0–3 and basic save/reload complete; Checkpoints 4–6 pending<br>
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

## Pending In-Game Verification

- Clean definition load and texture discovery, including both random mature and
  immature variants.
- Crop-selector visibility, ground/hydroponic boundary, sowing, growth, threats,
  grazing, harvest, and base yield.
- Raw eating, meals, nutrient paste, animals, storage, rot, trade, caravan, and food
  policy integration.
- New-save, existing-save, save/reload state, and disposable removal behavior.
- Core-only, individual supported DLC, and all-supported-DLC configurations.
- Normal-zoom art review, performance, controlled crop balance, long-colony play,
  and player comprehension.

No pending scenario is marked passed until observed in RimWorld. Any behavior that
contradicts FS-001 stops implementation for human review rather than being tuned
silently.

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
| AC-002 | Planting boundary: 70%+ fertility, no hydroponics | Pending | |
| AC-003 | 8.0 grow days | Pass | XML confirmed |
| AC-004 | Base yield 15, no secondary | Pass | XML confirmed |
| AC-005 | Fertility sensitivity 1.0 | Pending | |
| AC-006 | Nutrition 0.05, RawBad, 2% poison | Pass | In-game inspect |
| AC-007 | Vanilla food integration | Pending | |
| AC-008 | Animal integration | Pending | |
| AC-009 | Stack 75, mass 0.03, rot 45 days | Pass | XML + in-game inspect |
| AC-010 | Market value 1.1, normal trade | Pass | In-game inspect |
| AC-011 | Normal threats (cold, blight, fire, grazing) | Partial | Cold confirmed; blight/fire/grazing pending |
| AC-012 | Save/load | Partial | Basic plant/item save-reload passed; detailed state matrix pending |
| AC-013 | DLC absence | Pending | |
| AC-014 | Art distinguishable from rice/corn/haygrass | Partial | Normal-zoom field confirmed; formal vanilla comparison pending |
| AC-015 | Performance | Pending | |
| AC-016 | Scope (no C#, Harmony, secondary, research, wild spawn) | Pass | Staged package confirmed by staging script |

### Remaining Checkpoints

- **Checkpoint 4:** Full Core player path — fertility boundaries, food/cooking/animals/storage/trade/save-load (AC-002, AC-005, AC-007, AC-008, AC-011 full, AC-012)
- **Checkpoint 5:** DLC + mod compatibility (AC-013)
- **Checkpoint 6:** Art comparison, controlled balance fields, performance, comprehension test (AC-014 full, AC-015)
