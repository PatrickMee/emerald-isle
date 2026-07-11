# Version 0.1 Release Test Matrix

**Status:** Ready for execution — results pending against the exact staged release archive
**Feature set:** FS-001 Oats, FS-002 Dry-Stone Wall, FS-003 Hand Quern,
FS-004 Milled Oats, and FS-005 Oat Foods (per the
[v0.1 release checklist](../release/v0.1-release-checklist.md))
**Policy:** [Supported platforms](../engineering/supported-platforms.md) — test
Core-only plus the all-supported-DLC configuration at minimum; no v0.1 feature
requires or enhances a specific DLC, so per-DLC solo runs are risk-based only.

## Environment

Record before executing. All runs use the exact archive produced by
`tools/stage-mod.sh` from the frozen release commit, not the working tree.

| Input | Value |
|---|---|
| RimWorld build | [1.6.x rev] |
| Release commit | [sha] |
| Archive | [path/checksum] |
| Platform | [macOS/Windows] |
| Tester | [name] |
| Date | [YYYY-MM-DD] |

## Configuration Runs

| ID | Configuration | Save state | Result | Evidence |
|---|---|---|---|---|
| C1 | Core + Emerald Isle only | New colony | Pending | |
| C2 | Core + Emerald Isle only | Existing vanilla save, mod added | Pending | |
| C3 | All supported DLC + Emerald Isle | New colony | Pending | |
| C4 | Core + Emerald Isle, then mod removed | Save with planted oats, stored oats/milled oats/oat foods, built walls, placed quern, and active bills | Pending | |

## Per-Configuration Checks

Run in C1 and C3; C2 checks load and player path only; C4 checks documented
degradation (missing-Def warnings, content loss) matches release notes.

### Load and Logs

- [ ] Clean load with no Emerald Isle errors or warnings in the log
- [ ] Core + Emerald Isle only clean-log certification
      (deferred from FS-002 Gate 2 evidence — this is the closing check)
- [ ] Mod list order has no load-order warnings

### FS-001 Oats

- [ ] Sow, grow, harvest oats through the full cycle
- [ ] Raw oats usable in meals, nutrient paste, and animal feed; tradeable
- [ ] Oats rot at the specified shelf life; no hydroponics sowing allowed
- [ ] Save/load mid-growth and with stored oats preserves state

### FS-002 Dry-Stone Wall

- [ ] Buildable in all five Core stone types with correct tinting
- [ ] Linked rendering, room formation, and roof support behave as specified
- [ ] Save/load with built and blueprinted walls preserves state

### FS-003 / FS-004 Hand Quern and Milled Oats

- [ ] Quern buildable; milling bill converts raw oats to milled oats as specified
- [ ] Milled oats usable per specification; whole-chain labor and value hold
- [ ] Save/load with an active bill, work in progress, and stored milled oats

### FS-005 Oat Foods

- [ ] Cook oat porridge and oat flatbread from milled oats at the supported Core
      cooking buildings
- [ ] Food policies, storage, caravans, traders, animals, prisoners, babies, and
      nutrient paste do not select the foods outside their specified roles
- [ ] Porridge and flatbread nutrition, work, mass, value, and spoilage preserve
      the intended fresh-food versus portable-food tradeoff
- [ ] Save/load with stored foods, active cooking bills, stockpile settings, and
      food policies preserves state

### Whole-Chain Balance (release-blocking, deferred from FS-001)

- [ ] Oats occupy a rational niche against rice, potatoes, and corn in at least
      one colony plan without dominating all plans
- [ ] Milling earns its labor against eating raw oats; neither mandatory nor empty

### Performance

- [ ] No observable stutter or log spam in a colony using all v0.1 content at
      representative scale

## Sign-Off

| Check | Result | Date |
|---|---|---|
| All configuration runs pass | Pending | |
| Blockers resolved or explicitly waived with rationale | Pending | |
| Evidence linked from the v0.1 release checklist | Pending | |
