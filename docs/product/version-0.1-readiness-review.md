# Version 0.1 Readiness Review

**Release:** Version 0.1 - The First Holding
**Review date:** 2026-07-05
**Review purpose:** Research-to-Specification transition
**Recommendation:** Ready to transition to Specification
**Maintainer decision:** Pending
**Implementation authorized:** No
**Canonical scope:** `docs/product/version-0.1-approved-scope.md`
**Research completion record:** `docs/research/version-0.1/research-completion-summary.md`

## Executive Decision

Version 0.1 is ready to leave the Research phase and enter the Specification phase.
All required research briefs are approved, all Research Definition of Ready gates
have passed, required durable decisions are recorded, and no unresolved historical
or gameplay question prevents specification.

This is a recommendation awaiting human approval. It does not create a feature
specification, approve an implementation plan, pass the project Definition of Ready,
or authorize gameplay work.

## Required Readiness Checks

| Check | Result | Evidence |
|---|---|---|
| All required research is complete | Pass | RSC-002 through RSC-006 are approved |
| Every brief passed Research DoR | Pass | Three `Passed`; two `Passed with conditions` |
| Required ADRs exist and are accepted | Pass | ADR-0001 accepted; no additional research-stage ADR required |
| No unresolved historical question blocks design | Pass | Evidence limits are explicit implementation notes, not missing identity decisions |
| No unresolved gameplay question blocks design | Pass | Core roles, tradeoffs, fallback, and simplification principle are approved |
| Frozen scope is internally consistent | Pass | Crop, conditional processing chain, two foods, and wall remain within approved scope |
| XML-first feasibility is credible | Pass | All proposed behavior maps to verified RimWorld 1.6 Core Def and bill patterns |
| Ready to enter Specification | Pass | Research inputs are sufficient to write bounded, testable feature specifications |

## Research Gate Audit

| Brief | Historical gate | Gameplay gate | Research DoR | Disposition |
|---|---|---|---|---|
| RSC-002 Oats | Approved under original brief review | Approved design intent and ADR | Passed | Advance to specification |
| RSC-003 Dry-Stone Wall | Approved under original brief review | Approved niche and tradeoff | Passed | Advance to specification |
| RSC-004 Hand Quern | Approved | Approved with conditions | Passed with conditions | Specify as conditional; direct path remains fallback |
| RSC-005 Milled Oats | Approved | Approved with conditions | Passed with conditions | Specify only as a decision-bearing intermediate |
| RSC-006 Oat Foods | Approved | Approved | Passed | Specify porridge and oat flatbread with simplification rule |

The split historical/gameplay gate became mandatory after RSC-002 and RSC-003 were
approved. Their recorded human decisions, gameplay intent, vanilla comparisons,
tradeoffs, and Research DoR provide equivalent evidence without reopening approved
research.

## ADR Audit

### Accepted Decision

- [ADR-0001](../adr/0001-oats-medium-cycle-xml.md) includes oats in Version 0.1 as a
  medium-cycle XML-only processing grain and prohibits a broadly superior hardy-crop
  design.

### No Missing ADR

No additional research-stage ADR is required because:

- the dry-stone wall stays within the canonical one-variant XML scope;
- the project owner explicitly stated that no new Hand Quern ADR was required;
- milled oats and both foods use the already approved XML-first production chain;
- exact balance, parent Defs, recipes, filters, art, and test values are specification
  decisions rather than new architecture.

Any later proposal for C#, Harmony, a new framework, a new cooking building, a third
food, new stone resources, or a major scope change triggers a new ADR review.

## Scope Consistency Review

### Oats

Research supports the approved early medieval Irish crop identity, medium growth
cycle, XML-only implementation, vanilla agriculture integration, processing role,
and prohibition on a superior hardy-crop design.

### Dry-Stone Wall

Research supports one cashel-inspired perimeter wall using vanilla stone blocks. The
material-efficiency advantage has explicit durability, work, and structural-utility
tradeoff candidates. No gates, family, new stone, curved walls, or procedural
settlements were added.

### Processing and Foods

Research supports one conditional rotary hand quern, one milled-oats intermediate,
one everyday porridge, and one portable oat flatbread. The chain remains XML-only and
uses normal RimWorld bills and cooking infrastructure.

The chain's governing principle is choice rather than historical completeness. Raw
oats remain useful, and the quern or intermediate must be simplified or removed if
implementation or playtesting cannot demonstrate distinct decisions.

### Release Integration

Release integration requires no separate historical brief. Existing build, test,
compatibility, localization, save, packaging, and release policies provide the
inputs for later feature specifications and the release plan.

### Scope Result

The approved scope remains coherent and unchanged. Research added evidence,
constraints, and a simplification fallback; it did not add gameplay features.

## Historical and Cultural Readiness

- The target remains early medieval Ireland, approximately AD 400-1100.
- Ordinary holdings and domestic life remain the primary frame.
- Archaeology, early documentary synthesis, later folklore, modern language, and
  gameplay invention are distinguished.
- Cashel enclosures are not confused with later field-wall networks.
- Oat foods are broad transformed forms, not standardized recipe reconstructions.
- English functional names are approved: `Oats`, `Hand Quern`, `Milled Oats`,
  `Oat Porridge`, `Oat Flatbread`, and `Dry-Stone Wall`.
- Player-facing Irish remains optional and requires competent review.
- Romantic, famine-era, nineteenth-century, nationalist, generic Celtic, and
  primitive-technology framing remains excluded.

**Result:** Ready for specification. Remaining historical uncertainty constrains
claims and descriptions but does not block design.

## Gameplay Readiness

- Every feature has a stated player purpose and vanilla comparison.
- Oats must be situational rather than universally hardy or efficient.
- Dry-stone walls trade material efficiency for durability, labor, or structural
  utility.
- The hand quern trades low capital and no power for labor, hauling, and throughput.
- Milled oats stage labor and food choices without creating nutrition, preservation,
  quality, or market value by themselves.
- Porridge is the fresh everyday path; oat flatbread is the portable processed path.
- Pemmican and packaged survival meals retain superior preservation roles.
- Direct cooking and chain simplification remain required alternatives for
  specification and playtesting.

**Result:** Ready for specification. Exact numbers and observed player behavior are
specification and playtest questions, not missing gameplay direction.

## Technical Readiness

- Required platform: RimWorld 1.6 Core.
- Official DLC support: Royalty, Ideology, Biotech, Anomaly, and Odyssey.
- Required DLC for the approved features: none.
- Implementation target: XML only.
- C# requirement: none identified.
- Harmony requirement: none; use remains prohibited without a new ADR.
- Expected primitives: plant and item Defs, wall/building Defs, recipe Defs, bills,
  worktables, cooking buildings, rot, ingredients, storage, trade, localization, and
  original textures.
- Runtime state: no custom serialized state or per-tick system identified.
- Performance: passive Def content and standard bills are expected to remain low
  risk; broad filters and hauling behavior require validation.
- Save compatibility: stable namespaced IDs and add/remove scenarios are required
  before implementation.

**Result:** Ready for specification, not implementation. Exact Def inheritance,
filters, work types, recipe users, ratios, save cases, and DLC matrices must be made
testable in feature specifications and plans.

## Discipline Review at Research Depth

| Discipline | Result | Specification obligation |
|---|---|---|
| Product and identity | Pass | Keep exact frozen scope and smallest coherent slices |
| Historical and cultural | Pass | Preserve claim boundaries and transformation notes |
| Gameplay | Pass | Define observable decisions and simplification triggers |
| Vanilla fit | Pass | Use normal bills, stats, work, food, walls, and UI |
| Balance | Pass with hypotheses | Model complete lifecycles and abuse cases before values are accepted |
| Architecture | Pass | Remain XML-only unless new evidence triggers ADR review |
| Art | Pass for specification | Create bounded original asset briefs and in-game acceptance views |
| Language/localization | Pass for specification | Use functional English and translation keys; review any Irish |
| Save/compatibility | Pass for specification | Define stable IDs, matrices, migration, removal, and rollback cases |
| Performance | Pass for specification | Use narrow filters and measure representative behavior |
| QA/playtesting | Pass for specification | Turn research hypotheses into normal, edge, failure, and exploit scenarios |

## Remaining Non-Blocking Inputs

The [Research Completion Summary](../research/version-0.1/research-completion-summary.md)
contains the complete list. The highest-priority specification inputs are:

1. exact crop and wall lifecycle balance;
2. hand-quern work type, worker skill, footprint, throughput, and batch behavior;
3. milled-oats classification and nutrition-safe conversion ratios;
4. porridge and flatbread work, nutrition, rot, unit, and caravan behavior;
5. Core/DLC food, wall, storage, save, and removal scenarios;
6. original art states, paths, provenance, and acceptance views;
7. direct-processing alternatives and measurable simplification triggers.

None requires additional historical research before a specification can be written.
Any specification may return to research if it discovers a new material claim or
invalidates an approved assumption.

## Phase Boundary

After human approval of this review, the project may create feature specifications
one at a time under the established workflow. Specification may refine or narrow the
approved features but cannot expand frozen scope without approval and, where
appropriate, an ADR.

Implementation remains prohibited until each feature has:

- an approved specification;
- a passed Feature Acceptance Checklist;
- an architecture decision and accepted ADRs where required;
- an actionable implementation plan and test intent;
- a passed project Definition of Ready; and
- explicit maintainer authorization.

## Final Recommendation

**Ready to transition from Research to Specification.**

**Maintainer decision:** Pending

**Approved by/date:** Pending

**Conditions:** Preserve frozen scope, XML-only target, independent gameplay value,
vanilla tradeoffs, and the approved simplification fallback. Do not begin
implementation from this review.
