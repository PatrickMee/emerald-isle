# ADR 0001: Oats Use a Medium-Cycle XML-Only Design

**Status:** Accepted
**Date:** 2026-07-05
**Decision owners:** Patrick Mee
**Related:** `docs/research/version-0.1/oats.md`,
`docs/product/version-0.1-scope-freeze.md`, PL-01

## Context

Version 0.1 requires a small agricultural foundation that demonstrates Emerald
Isle's research, specification, balance, art, testing, and release workflow. Oats
are strongly supported by early medieval Irish archaeobotanical evidence and connect
the approved crop, hand-quern, milled-oats, and oat-food scope.

The crop still needs a defensible RimWorld role. A generic crop would add catalog
content without a decision; a broadly superior “hardy” crop would violate the
Constitution's Tradeoffs Over Power principle. The supported RimWorld 1.6 plant and
item systems already expose the declarative behavior expected by PL-01.

## Decision Drivers

- Strong early medieval Irish evidence and clear Version 0.1 thematic fit
- A distinct player decision rather than a cosmetic crop
- Balance against rice, potatoes, corn, and the complete processing chain
- Minimal technical, save, performance, and compatibility risk
- Reusable crop/resource patterns without speculative infrastructure
- The project's XML-first and vanilla-native requirements

## Options Considered

### Exclude Oats from Version 0.1

- Benefits: Smallest possible crop and food surface; no duplicate-content risk.
- Costs and risks: Breaks the approved release loop and removes the strongest
  researched agricultural anchor.

### Add Oats as a Cosmetic Vanilla Crop Variant

- Benefits: Very small design and implementation effort.
- Costs and risks: Creates no meaningful decision and fails the Constitution and
  Design Bible feature gate.

### Add Oats as a Broadly Hardier or More Efficient Crop

- Benefits: Immediately legible incentive to players.
- Costs and risks: Replaces rather than complements vanilla crops, overstates the
  historical evidence, and causes power creep across soil, climate, yield, and labor.

### Add Oats as a Medium-Cycle Processing Grain Using XML

- Benefits: Creates a timing, soil, labor, storage, milling, and food-chain decision;
  uses Core systems; provides a reusable first crop pattern.
- Costs and risks: Requires whole-chain balance and careful ingredient behavior so
  milling is neither bypassed nor empty busywork.

## Decision

Oats are included in the frozen Version 0.1 scope as a medium-cycle processing
grain. They will be designed as a situational alternative to vanilla crops, not as
a “hardier,” objectively superior, or universal default crop.

The implementation target is XML only. PL-01 may use supported RimWorld 1.6 Core
plant, item, food-category, storage, trade, art, and localization mechanisms. It may
not add custom C#, Harmony patches, a custom soil or weather system, a secondary
straw product, or speculative crop infrastructure.

Exact growth, fertility, yield, shelf-life, ingestibility, ingredient, and processing
values remain specification and playtest decisions. An advantage in one dimension
must carry a visible cost or constraint elsewhere in the complete lifecycle.

## Consequences

**Positive:** Version 0.1 retains a historically supported agricultural anchor,
establishes a reusable XML crop/resource pattern, and creates a coherent dependency
for milling and food production.

**Negative:** The feature requires end-to-end labor and nutrition modeling. Existing
crop mods may create duplicate oats, and generic food categories may bypass the
intended processing loop.

**Neutral/follow-up:** Research uncertainties are implementation notes. The future
specification must decide raw ingestibility, animal-feed use, ingredient filters,
hydroponics, exact balance values, art states, and the supported compatibility test
set.

## Compatibility and Migration

- RimWorld 1.6 Core is required; no DLC is required.
- Optional DLC must not change the core crop's availability.
- Public Def names become save contracts when implementation begins.
- Adding the crop to an existing save is expected to be low risk but must be tested.
- Removing a mod containing planted or stored oat Defs may lose content and produce
  missing-Def warnings; release documentation must state the tested compatibility
  level.
- No automatic unification with third-party oat items is approved by this ADR.

## Validation

The decision succeeds when the future feature specification and playtest evidence
show that:

- oats create a comprehensible choice against rice, potatoes, and corn;
- oats are not best across comparable soils, labor, yield, storage, and flexibility;
- milling and food production create value without mandatory busywork;
- the complete feature uses XML and supported Core mechanisms;
- Core-only and all-supported-DLC configurations load, save, and play correctly.

## Revisit When

- Verified RimWorld 1.6 behavior cannot express an accepted requirement in XML.
- Whole-chain modeling cannot produce a meaningful niche without power creep or
  excessive labor.
- A supported compatibility target makes duplicate oats materially harmful.
- Research for milling or oat foods invalidates the processing-grain premise.

Any proposal to add C#, use Harmony, or redefine oats as a broadly superior crop
requires a new ADR that supersedes this one.
