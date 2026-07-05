# Version 0.1 Research Completion Summary

**Release:** Version 0.1 - The First Holding
**Status:** Complete
**Completed:** 2026-07-05
**Approved by:** Patrick Mee
**Canonical scope:** `docs/product/version-0.1-approved-scope.md`
**Readiness review:** `docs/product/version-0.1-readiness-review.md`
**Implementation authorized:** No

## Outcome

All five required Version 0.1 research briefs are approved and have passed their
Research Definition of Ready. The historical and gameplay foundations are sufficient
to enter feature specification. No gameplay specification, implementation plan,
gameplay XML, C#, Harmony patch, texture, audio, or package metadata was created
during research.

`Passed with conditions` means the research gate is complete while named balance and
complexity hypotheses remain mandatory inputs to specification and playtesting. It
does not authorize implementation.

## Approved Research Briefs

| ID | Brief | Research DoR | Approved direction | Associated ADR |
|---|---|---|---|---|
| RSC-002 | [Oats](oats.md) | Passed | Medium-cycle, XML-only processing grain; never a broadly superior hardy crop | [ADR-0001](../../adr/0001-oats-medium-cycle-xml.md) |
| RSC-003 | [Dry-Stone Wall](dry-stone-wall.md) | Passed | One cashel-inspired, material-efficient perimeter wall using vanilla stone blocks | None required at research stage |
| RSC-004 | [Hand Quern](hand-quern.md) | Passed with conditions | One compact, unpowered rotary quern retained only if milling creates a decision | None; the project owner explicitly waived a new ADR |
| RSC-005 | [Milled Oats](milled-oats.md) | Passed with conditions | One XML-only processing intermediate with no inherent nutrition or preservation bonus | None required at research stage |
| RSC-006 | [Oat Foods](oat-foods.md) | Passed | Everyday oat porridge and portable oat flatbread, both simple-meal tier and XML-only | None required at research stage |

## ADR Reconciliation

### Accepted

- **ADR-0001: Oats Use a Medium-Cycle XML-Only Design** establishes the durable crop
  niche, forbids a broadly superior hardy-crop design, selects XML, and requires
  complete-chain balance.

### Not Required During Research

- The dry-stone wall remains within the approved one-variant, vanilla-block,
  XML-only boundary.
- The hand quern is already conditional in canonical scope, and the project owner
  explicitly stated that no new ADR was required for its research approval.
- Milled oats and the two foods implement the already approved processing chain using
  ordinary Core items, recipes, bills, and cooking infrastructure.

A new ADR is required if specification proposes custom C#, Harmony, a generic crop,
milling, flour, bread, or food framework, a new cooking building, a third oat food,
new stone resources, or another material departure from frozen scope or baseline
architecture.

## Canonical Gameplay Loop

The approved production loop is maintained in the
[Oat Foods brief](oat-foods.md#canonical-version-01-gameplay-loop):

```text
Oats
  ↓
Hand Quern (conditional)
  ↓
Milled Oats
  ↓
Choice
  ├── Oat Porridge
  └── Oat Flatbread
```

The purpose of the loop is player choice, not historical completeness. Raw oats must
remain useful. The quern and intermediate must be simplified or removed if their
labor, hauling, and inventory costs do not create distinct decisions.

## Remaining Implementation Assumptions

These are specification and test inputs, not unresolved research blockers.

### Oats

- Set exact growth time, yield, fertility sensitivity, sow skill, nutrition, market
  value, mass, stack, deterioration, rot, raw ingestibility, animal-feed behavior,
  hydroponics behavior, and crop disease interactions.
- Prove a medium-cycle niche against rice, potatoes, and corn across complete
  lifecycles rather than making oats best in marginal conditions.
- Select stable `EI_` identifiers, translation keys, and original plant/item art.

### Dry-Stone Wall

- Select block cost, construction work, durability, beauty, wealth, repair, terrain,
  roof support, airtightness, attachment, replacement, breach, explosion, sapper,
  paint/style, and Odyssey-vacuum behavior.
- Prove material efficiency is paid for by lower durability, greater work, reduced
  structural utility, or another visible constraint.
- Verify visual joins with vanilla walls, doors, natural rock, and supported wall
  mods without adding curved or procedural walls.

### Hand Quern

- Decide footprint, construction materials, research access, work type, skill,
  throughput, batch size, recipe filters, bill counting, and selected construction
  stuff.
- Confirm milling can be scheduled independently enough to create value rather than
  splitting one compulsory cooking job into two bills.
- Remove the quern from the final specification if the simpler direct-food path
  produces equivalent gameplay.

### Milled Oats

- Decide item classification, ingestibility, food/ingredient categories, stack,
  mass, value, rot, deterioration, conversion ratio, batch size, storage, trade,
  caravan, animal, nutrient-paste, and ordinary-meal interactions.
- Conserve nutrition and value across integer item counts; processing alone grants no
  shelf-life, quality, beauty, or market premium.
- Keep filters narrow and namespaced rather than claiming universal flour
  compatibility.

### Oat Foods

- Set complete-chain work, skill, nutrition, unit size, stack, value, food
  preferability, food poisoning, rot, deterioration, caravan value, and recipe-user
  behavior.
- Keep porridge fresh and everyday, with any lower final-cooking burden paid by prior
  independently scheduled milling and short keeping time.
- Keep oat flatbread moderately portable but substantially less preserved than
  pemmican and packaged survival meals.
- Test the direct-recipe alternative and simplify the chain if two foods do not
  produce distinct player behavior.

### Platform, Save, and Delivery

- Require RimWorld 1.6 Core; no DLC is required by the approved research direction.
- Verify Core-only, each relevant supported DLC, and all-supported-DLC behavior in
  the future specification and test matrix.
- Treat public Def names, translation keys, bills, food policies, and saved stacks as
  compatibility contracts once implemented.
- Define save addition, removal, missing-Def, suspended-bill, planted-crop, stockpile,
  caravan, and DLC add/remove scenarios before implementation authorization.
- Produce original, licensed, provenance-recorded art and localization-ready English
  text; player-facing Irish remains optional and requires competent review.

## Open Risks

| Risk | Current assessment | Required response |
|---|---|---|
| Processing chain becomes compulsory busywork | Open, high design importance | Compare full chain with direct cooking; simplify if decisions do not emerge |
| Nutrition or market-value multiplication | Open, high impact | Model every integer conversion and test exploit loops |
| Oats or wall become strict vanilla upgrades | Open, high impact | Use lifecycle comparisons and explicit tradeoffs |
| Duplicate oats, flour, walls, or food filters conflict with mods | Open, medium likelihood | Namespace narrowly and define a risk-based compatibility sample |
| Save contracts are chosen casually | Deferred until specification, high impact | Freeze IDs deliberately and write add/remove/save scenarios |
| Art or terminology collapses historical periods | Controlled but ongoing | Use original art, source notes, English functional labels, and review |
| DLC-specific food, wall, or caravan behavior is missed | Controlled but ongoing | Execute Core-only and supported-DLC matrices |

No open risk requires more historical research before specification. Risks remain
capable of narrowing or removing conditional content during specification,
implementation planning, or playtesting.

## Research Exit Checklist

- [x] Oats research approved and Research DoR passed.
- [x] Dry-stone wall research approved and Research DoR passed.
- [x] Hand-quern research approved and Research DoR passed with explicit conditions.
- [x] Milled-oats research approved and Research DoR passed with explicit conditions.
- [x] Oat-food research approved and Research DoR passed.
- [x] Historical claims, uncertainty, anachronism, and cultural risks are recorded.
- [x] Gameplay validation is independent from historical support.
- [x] Vanilla, DLC, XML, save, performance, compatibility, art, and localization
  concerns are bounded at research depth.
- [x] ADR-0001 is accepted; no missing research-stage ADR is identified.
- [x] Frozen scope remains internally consistent and has not expanded.
- [x] Remaining uncertainty is assigned to specification, testing, or playtesting.
- [x] No specification or implementation was started.

## Next Gate

The [Version 0.1 Readiness Review](../../product/version-0.1-readiness-review.md)
recommends transition from Research to Specification. A human maintainer must approve
that review before any feature specification is created. Implementation remains
blocked until each feature later passes acceptance, architecture, planning, and the
project Definition of Ready.
