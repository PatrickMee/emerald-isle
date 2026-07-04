# Version 0.1 Candidate Implementation Plan

**Status:** Provisional, pending Research Sprint findings and human review  
**Implementation authorized:** No

## Ranking Method

Candidates were ranked by gameplay value, implementation risk, XML-only
probability, art burden, reusable patterns, workflow coverage, and visible player
value. This is a research queue, not final scope.

## 1. PL-01: Oat-Like Cool-Climate Grain

**Why selected:** A crop is immediately visible, interacts with a mature vanilla
system, and is likely definable in XML. It can demonstrate research, balance,
localization, plant art states, Def naming, DLC testing, and in-game evidence in a
small surface area.

**Why Version 0.1:** It establishes the first complete content pipeline without
requiring custom UI, save state, Harmony, or complex AI.

**Why before others:** It supplies the raw input needed to evaluate oat foods and
milling. Starting downstream would force placeholder ingredients or rework.

**Enables:** FO-01 foods, PR-01 milling, agriculture balance patterns, future crop
and animal-feed research, plant asset conventions.

## 2. BL-01: Dry-Stone Wall Family

**Why selected:** It creates strong visual identity and a clear construction choice
using established building systems. XML is likely sufficient; art is bounded to a
small modular set.

**Why Version 0.1:** It proves architecture can be recognizable, balanced, and
vanilla-readable without a large settlement system.

**Why before others:** It validates wall, material, cover, pathing, damage-state,
blueprint, and compatibility conventions required by every later building set.

**Enables:** RS-02 stone decisions, ringfort modules, monastic architecture,
settlement kits, future architecture art standards.

## 3. FO-01: Oat Bread and Porridge Chain

**Why selected:** It turns the first crop into player-visible decisions around
labor, nutrition, mood, storage, and cooking while remaining likely XML-only.

**Why Version 0.1:** A crop plus food demonstrates a coherent vertical slice rather
than a disconnected object and tests balance across acquisition and consumption.

**Why after PL-01:** Ingredient yield and crop cadence must be understood before
recipe work, nutrition, and value can be balanced honestly.

**Enables:** PR-01 milling, hospitality/feast research, dairy preservation, brewing,
food terminology, production-chain testing.

## 4. RS-02: Worked Local Stone Set

**Why selected:** It can establish resource, Stuff/ThingDef, texture, market-value,
and construction-cost conventions with low runtime risk.

**Why Version 0.1:** Later architecture needs a deliberate answer to whether
Emerald Isle uses vanilla blocks, a dedicated material, or presentation-only
variation. Researching and resolving that contract early prevents rework.

**Why after BL-01:** The wall experiment reveals whether a new resource creates a
real decision or only duplicates vanilla stone. The candidate must be rejected if
the latter is true.

**Enables:** broader vernacular buildings, production recipes, terrain/resource
research, consistent architectural materials.

## 5. PR-01: Quern and Milling Workflow

**Why selected:** A small worktable/recipe chain exercises production bills,
facilities, work types, art, localization, and save-safe definitions. It creates a
meaningful processing decision if research shows the labor step adds value.

**Why Version 0.1:** It completes the agriculture-to-food pipeline and establishes
a reusable production pattern for brewing, dairy, textiles, and craft.

**Why fifth:** Its value depends on findings from PL-01 and FO-01. If it becomes
busywork or needs disproportionate C#, it should be deferred rather than forced.

**Enables:** brewing/distilling, dairy processing, flax/textile production,
facility-link patterns, production-building art and QA.

## Candidates Not Selected for the First Five

- **RE-01 Vernacular masonry research:** low independent player value; include only
  if progression needs a gate proven by research.
- **QL-01 category organization:** necessary presentation work may accompany the
  first content but does not justify an independent gameplay feature.
- Animals, apparel, rituals, factions, mythology, and world systems carry greater
  art, code, balance, cultural, or compatibility risk and remain later candidates.

## Proposed Dependency Order

```text
Technical and historical research
├── PL-01 Oat grain ──> FO-01 Oat foods ──> PR-01 Milling (conditional)
└── BL-01 Dry-stone walls ──> RS-02 Worked stone (conditional)
```

## Planning Gate

After the Research Sprint, re-score all five. A candidate advances only when it has
an approved research brief, feature spec, Feature Acceptance Checklist, DLC/save
matrix, architecture decision, implementation plan, and Definition of Ready.
Implementation order may change, and conditional candidates may be rejected.
