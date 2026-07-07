# Emerald Isle Product Roadmap

**Status:** Strategic direction, not a promise of individual features  
**Planning rule:** Only the active milestone authorizes implementation.

This roadmap protects long-term coherence while enforcing present-day restraint.
Future releases influence stable contracts and dependency direction; they do not
justify speculative frameworks, unused APIs, or premature content.

## Milestone 0: Build the Studio

**Status:** Complete in v0.0.0.  

**Vision:** A professional, inspectable operating system for a multi-year mod.  
**Goals:** Establish governance, discipline guides, contribution rules, Spec Kit
adaptation, repository boundaries, quality gates, and reusable templates.  
**Scope:** Documentation and process only; no mod metadata, gameplay, code, XML,
art, audio, or distribution.  
**Success criteria:** All 24 foundation deliverables have one authoritative home;
contributors can trace authority, readiness, done, and release requirements.  
**Technical constraints:** Own Git root; generic Spec Kit web assumptions removed;
future package structure documented but not scaffolded.  
**Deliverables:** Constitution, vision, architecture, discipline guides,
contribution guide, workflow, templates, ADR process, documentation map.  
**Exit criteria:** Foundation review approved; license chosen; supported game/DLC
policy recorded; maintainers/review authority assigned; baseline committed.  
**Risks:** Process overgrowth, unresolved ownership, unclear licensing, stale docs.  
**Dependencies:** Project owner decisions and repository hosting.

## Milestone 0.5: Create the Design Bible

**Status:** Complete in v0.0.0.  

**Vision:** One canonical identity reference keeps every human and AI contribution
recognizably Emerald Isle.  
**Goals:** Define creative boundaries, canon, cultural transformation, gameplay,
art, language, balance, progression, architecture, mythology, engineering,
performance, compatibility, documentation, testing, and expansion philosophy.  
**Scope:** Design authority, feature acceptance gate, roadmap contracts, and
workflow propagation; no gameplay implementation.  
**Success criteria:** Every requested identity topic is testable; every future
feature template requires Bible conformance; reviewers can accept or reject a
feature before planning.  
**Technical constraints:** Bible cannot override Constitution; ADRs cannot override
Bible; versioned amendments must propagate to dependent templates.  
**Deliverables:** Design Bible v1.0, Feature Acceptance Checklist, expanded roadmap,
Spec Kit gate updates, Milestone 0 closure audit.  
**Exit criteria:** Bible and checklist approved; cross-links and authority order
validated; Milestone 0 blockers resolved; baseline committed and tagged if desired.  
**Risks:** Excessive prescription, false cultural confidence, duplicated guidance,
identity drift through undocumented exceptions.  
**Dependencies:** Milestone 0 documents and qualified review for sensitive guidance.

## Version 0.1: The First Holding

**Status:** FS-001 Oats and FS-002 Dry-Stone Wall are implemented, verified,
Design Review-approved, and merged. FS-003 Hand Quern passed Gate 1 with bundled
FS-004 implementation as a condition; standalone hand-quern implementation remains
blocked. FS-004 Milled Oats passed Gate 1 with bundled FS-005 implementation as a
condition; standalone milled-oats implementation remains blocked. FS-005 Oat Foods
is in Gate 1 specification review. Version 0.1 integration and release checks
remain pending.

**Vision:** Prove the entire production pipeline with the smallest coherent,
vanilla-friendly Emerald Isle slice.  
**Goals:** Establish a loadable package, build/validation pipeline, naming and
localization practice, art pipeline, and one bounded feature vertical slice.  
**Scope:** The binding feature set, exclusions, historical direction, and phase gate
are maintained only in
[`product/version-0.1-approved-scope.md`](product/version-0.1-approved-scope.md).

**Success criteria:** Clean install/load, complete player path, save/load,
localization readiness, in-game art validation, balanced playtest, clean package.  
**Technical constraints:** XML-first; one core assembly only if proven necessary;
no Harmony without ADR; minimal DLC assumptions; stable `EI_` identifiers.  
**Deliverables:** Package metadata, build tools, compatibility matrix, terminology
record, first accepted feature, tests, playtest evidence, preview release.  
**Exit criteria:** Supported configuration passes release checklist; no critical
defects; pipeline reproducible by a new contributor.  
**Risks:** Choosing an oversized first slice, API/version churn, art bottlenecks,
premature abstractions.  
**Dependencies:** Closed Milestones 0/0.5, license, supported game version, toolchain.

## Version 0.5: Living Culture

**Vision:** The colony experiences a connected culture rather than isolated themed
items.  
**Goals:** Link proven foundations through daily work, food, craft, place, social
meaning, and small story-generating interactions.  
**Scope:** A curated set of interoperating systems selected after 0.1 evidence;
possible agriculture, food, craft, animals, architecture, or social expression.  
**Success criteria:** Features create multiple viable colony patterns, remain
useful independently, and produce recognizable stories without excessive UI.  
**Technical constraints:** Reuse only demonstrated primitives; optional DLC
adapters isolated; avoid bespoke progression currencies and monolithic managers.  
**Deliverables:** Accepted feature set, cross-system balance model, expanded art
and terminology guides, compatibility tests, migration notes, beta release.  
**Exit criteria:** Cohesive gameplay loop passes multi-stage colony playtests and
supported matrix; documentation enables external contribution.  
**Risks:** Feature sprawl, hidden synergies, wealth/economy distortion, cultural
flattening, compatibility matrix growth.  
**Dependencies:** Stable 0.1 pipeline, player telemetry/feedback, art and review capacity.

## Version 1.0: Emerald Isle

**Vision:** A stable, cohesive expansion whose identity, quality, and usability
support broad public adoption.  
**Goals:** Complete the core product promise, stabilize contracts, polish onboarding,
balance progression, and publish maintainable contributor/support practices.  
**Scope:** Only systems required for a complete core identity; later mythology,
large governance, and world/sea ambitions remain outside scope.  
**Success criteria:** New and experienced players understand the offering; long
colonies remain balanced and performant; supported saves and integrations are stable.  
**Technical constraints:** Public IDs and save data treated as durable; no known
critical performance paths; package and optional adapters independently testable.  
**Deliverables:** Stable release, complete core content, translations as available,
compatibility/support matrix, migration policy, credits, full documentation.  
**Exit criteria:** Release candidate passes clean and long-save testing, cultural
and design review, accessibility/localization checks, and rollback rehearsal.  
**Risks:** Polish debt, backward-compatibility burden, support load, late redesign.  
**Dependencies:** Proven 0.5 cohesion, stable RimWorld target, contributor and QA capacity.

## Version 1.5: Echoes of the Sidhe

**Vision:** Mythology-inspired experiences add mystery and consequence without
turning Emerald Isle into a generic fantasy overhaul.  
**Goals:** Translate selected traditions into ambiguous, Rim-compatible stories,
beliefs, threats, opportunities, or phenomena.  
**Scope:** Curated mythological themes with strong opt-in boundaries; not a unified
myth canon or creature catalogue.  
**Success criteria:** Content works as RimWorld gameplay without prior knowledge,
rewards cultural context, preserves ambiguity, and does not dominate core play.  
**Technical constraints:** Isolated module/integration where practical; Anomaly or
other DLC use optional unless explicitly released as add-on; performance bounded.  
**Deliverables:** Research dossiers, mythology canon rules, feature set, bespoke
art/audio where justified, safety/compatibility tests, release documentation.  
**Exit criteria:** Mythology and cultural reviews pass; opt-in/off behavior and
save migration verified; core 1.0 remains coherent without the module.  
**Risks:** Fantasy drift, decontextualization, sacred-content misuse, event spam,
DLC coupling.  
**Dependencies:** Stable 1.0 canon and architecture, specialist research/review, art/audio capacity.

## Version 2.0: The High Kingdoms

**Vision:** Larger social and political structures create colony-scale obligations,
alliances, law, status, and faction stories.  
**Goals:** Explore clan and Brehon-inspired ideas, settlement relations, leadership,
and institutions through RimWorld decisions rather than historical simulation.  
**Scope:** Selected governance/faction/quest systems; no universal recreation of
Irish law or deterministic ethnic hierarchy.  
**Success criteria:** Multiple political strategies remain viable; systems produce
stories, integrate with factions/Ideology where available, and fail safely.  
**Technical constraints:** Requires mature save migrations, event contracts,
faction compatibility, and scalable state; DLC adapters remain optional.  
**Deliverables:** Governance research corpus, canon expansion, accepted systems,
AI behavior and quest tests, migration tooling, major-version release notes.  
**Exit criteria:** Long-campaign simulations and human playtests validate stability,
agency, balance, understandable consequences, and backward migration.  
**Risks:** Simulation complexity, ideology overlap, cultural/political sensitivity,
save breakage, opaque AI decisions.  
**Dependencies:** Stable core and mythology boundaries, mature testing, faction/quest expertise.

## Version 3.0: Beyond the Western Sea

**Vision:** Emerald Isle influences travel, geography, discovery, and the wider Rim
without losing the colony-centered product.  
**Goals:** Explore world generation, biome, ruins, journeys, Odyssey-facing
integrations, and distant cultural variants where platform evidence supports them.  
**Scope:** A selected expansion beyond settlement-scale play; the exact platform
surface remains discovery work until relevant RimWorld APIs/DLC stabilize.  
**Success criteria:** World-scale content creates meaningful expedition and colony
decisions, remains performant, and can be disabled or absent safely.  
**Technical constraints:** No architecture commitment before current APIs are
verified; generated-world and save compatibility require migration and rollback;
integration isolated from the core package where warranted.  
**Deliverables:** Platform research, world/biome architecture ADRs, feature suite,
generation tests, long-save migration, compatibility and release documentation.  
**Exit criteria:** Representative worlds and long campaigns validate generation,
travel, performance, recovery, and optional integration boundaries.  
**Risks:** Unknown future APIs, generation conflicts, save irreversibility, scope
explosion, hardware performance, core-identity dilution.  
**Dependencies:** Mature 2.x platform, supported RimWorld/DLC capabilities, profiling and migration tooling.

## Roadmap Governance

At each milestone start, convert only that milestone into approved feature specs.
At each exit, review evidence, compatibility obligations, player feedback, and the
next milestone's assumptions. Deferring, splitting, or removing roadmap content is
healthy when evidence changes. Advancing with unresolved exit criteria requires a
written exception approved under the Constitution.
