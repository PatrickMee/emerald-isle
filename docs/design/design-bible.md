# Emerald Isle Design Bible

**Status:** Stable baseline at v0.0.0; material changes require an ADR and Bible amendment review  
**Version:** 1.0.0  
**Adopted:** 2026-07-04  
**Owner:** Project maintainers  
**Review trigger:** Every milestone boundary and any proposed identity change

## Purpose and Authority

This Bible defines what Emerald Isle is. The Constitution governs how the project
works; this document governs creative and product identity. ADRs, milestone plans,
feature records, art briefs, and implementation must conform to both.

When documents conflict, use this order:

1. Constitution
2. Design Bible
3. Accepted ADRs
4. Active milestone and approved feature record
5. Discipline guides
6. Feature records

Changing project identity requires a reviewed Bible amendment with impact notes.
Feature work may refine details but cannot redefine the project by accumulation.

## 1. Project Identity

Emerald Isle is a lore-friendly RimWorld expansion imagining how an
Irish-inspired civilization might emerge on the Rim. It translates historical,
cultural, linguistic, architectural, agricultural, geographic, and mythological
inspiration into original RimWorld systems.

The desired player reaction is: "I recognize the inspiration, I understand the
RimWorld purpose, and this feels as though it has always belonged on the Rim."

### Product Pillars

- **Recognizable transformation:** specific inspiration, re-authored for the Rim.
- **Gameplay purpose:** every inclusion changes a decision, story, or strategy.
- **Vanilla fluency:** readable, restrained, systemic, and interoperable.
- **Tradeoffs:** strengths create costs, risks, dependencies, or lost alternatives.
- **Cultural care:** evidence, plurality, context, and freedom from caricature.
- **Expandable restraint:** stable seams for tomorrow, minimal machinery today.

## 2. Core Design Philosophy

Gameplay comes first. Research creates possibilities and constraints, not a duty
to reproduce history. Prefer a small system with rich interactions over many
isolated objects. Prefer mechanics that create stories over passive bonuses.
Prefer familiar RimWorld concepts before inventing new UI or currencies.

Every feature must explain:

- the player decision it creates
- the story it can produce
- why Irish inspiration materially shapes it
- why it belongs in the active milestone
- why a vanilla or existing project system cannot already do the job

## 3. Meaning of Irish-Inspired

"Irish-inspired" means drawing from specific, documented forms, practices,
environments, languages, social ideas, stories, and material culture, then asking
how analogous pressures could shape a society on another world.

It does not mean copying modern Ireland, compressing all eras into one culture,
or attaching green, shamrocks, harps, knots, alcohol, or generic Celtic labels to
ordinary content. Ireland is not culturally or historically uniform. Feature
records identify relevant period, region, community, evidence, and uncertainty.

Recognizability should come from coherent relationships: settlement form responds
to defense and land; food responds to crops and labor; belief responds to memory
and environment; craft responds to material and status. Motifs support that
coherence but cannot replace it.

## 4. Explicit Exclusions

Emerald Isle must not become:

- Earth or an alternative-history simulator
- a museum catalogue of historically attested objects
- a generic medieval, Celtic, druidic, or fantasy overhaul
- a nationalist, sectarian, colonial, or essentialist narrative
- a stereotype package centered on drunkenness, fighting, luck, red hair, or green
- a direct power upgrade over vanilla content
- a required total conversion or closed ecosystem
- a mythology dump detached from colony play
- a framework built for hypothetical features instead of current needs

Real political organizations, recent conflicts, sacred material, living people,
and modern identity claims require exceptional care and clear product relevance.

## 5. RimWorld Gameplay Philosophy

Design through RimWorld verbs: acquire, build, grow, craft, trade, tend, worship,
socialize, defend, travel, recover, and remember. Use existing information
patterns, bills, gizmos, inspect strings, stats, thoughts, quests, and storyteller
events before introducing custom interfaces.

Content should interact with colony wealth, labor, mood, health, ideology,
environment, threats, and storyteller pacing where relevant. A feature that only
adds inventory without changing decisions needs a stronger purpose.

Complexity budgets include concepts learned, clicks, UI, defs, code, patches,
save state, compatibility surface, art states, localization, and test matrix.

## 6. Historical Research Standards

Research follows `docs/research/research-guide.md`. Important claims require
credible sources and triangulation. Records distinguish evidence, interpretation,
folklore, modern revival, and project invention. Sources include page-level
citations when possible and licenses for reusable media.

No feature claims authenticity merely because a source exists. Researchers state
scope, uncertainty, disputes, anachronism risk, cultural sensitivity, and the
specific transformation made for gameplay and the Rim.

## 7. Lore and Canon Rules

Emerald Isle canon belongs entirely to RimWorld's universe. Earth names and
history may inspire development notes but do not appear as literal in-world facts
unless RimWorld canon independently supports them.

### Canon Layers

- **RimWorld canon:** highest fictional authority; do not contradict it casually.
- **Emerald Isle core canon:** facts required across features and approved here or
  in a dedicated lore ADR.
- **Local tradition:** factional, regional, ideological, or storyteller accounts
  that may conflict in-world.
- **Rumor and myth:** intentionally uncertain material.

Prefer partial, situated lore over encyclopedic exposition. Preserve ambiguity
where it creates stories. Do not establish a universal ethnic monoculture; allow
adoption, exchange, migration, syncretism, and variation on the Rim.

## 8. Art Direction

Art follows `docs/art/art-guide.md`. Match vanilla readability, scale,
perspective, outline weight, state communication, and restraint. Cultural identity
comes from silhouette, construction logic, materials, pattern rhythm, landscape,
and coherent sets, not excessive surface ornament.

Palette is grounded and material-led. Green is available but not mandatory or
identity-defining. Ornament has location, function, hierarchy, and breathing room.
Validate assets at normal zoom, in darkness and weather, beside vanilla content,
and in damaged or selected states.

## 9. Naming Conventions

Names must be pronounceable, searchable, consistent, and useful in RimWorld UI.
Player-facing names describe function before lore. Avoid unexplained apostrophes,
fantasy syllable inflation, faux-Gaelic spelling, and multiple terms for one idea.

- Internal identifiers: stable `EI_` prefix and descriptive PascalCase.
- Translation keys: `EI_<Domain>_<Concept>_<Purpose>`.
- Fictional proper names: document meaning, origin, pronunciation, and canon level.
- Earth-specific names: development references only unless explicitly justified.

Maintain a future terminology/glossary file once the first player-facing term is
approved; do not create vocabulary before a design needs it.

## 10. Language Guidelines

English is the source UI language. Irish may be used when it adds meaning,
identity, or texture and remains comprehensible through context. It is not a
decorative cipher or proof of authenticity.

Player-critical actions and stats remain immediately understandable. An Irish
term may lead where its meaning is discoverable through a concise English label,
description, or established context. Avoid hybrid grammar and machine-translated
coinages. Record dialect or standard-form choices. Player-facing Irish requires
review by a competent speaker before release.

Use full translation keys and translator comments. Do not concatenate sentence
fragments. Plan for grammatical gender, mutation, pluralization, word order, and
UI width rather than assuming English structure.

## 11. Gameplay Balance Philosophy

Balance follows `docs/design/balance-guide.md`. Compare complete lifecycles:
availability, research, materials, labor, space, power, upkeep, reliability,
flexibility, output, failure, scaling, wealth, and opportunity cost.

No meaningful feature is strictly better than its closest vanilla alternative at
equivalent access and cost. Asymmetry is desirable when situations determine the
winner. Balance hypotheses must predict player behavior and be tested in play,
not defended only by spreadsheet parity.

## 12. Progression Philosophy

Progression should widen strategic identity rather than replace earlier content
with numerically superior tiers. Early content is accessible but constrained;
later content earns flexibility, reliability, specialization, or integration
through investment and new dependencies.

Avoid parallel research trees, currencies, or skill systems unless repeated
features demonstrate that vanilla progression cannot express the product. DLC
integration enriches paths but core content must remain coherent without optional
DLC unless a release is explicitly scoped as an add-on.

## 13. Architecture Style Guide

Architecture should express material logic and settlement pressures on the Rim.
Forms may draw from ringforts, round towers, monastic organization, vernacular
buildings, field boundaries, and dry-stone construction, but each piece requires
a colony function and coherent construction economy.

Buildings must read in RimWorld's top-down grid, support normal pathing and combat,
and combine with vanilla walls, doors, furniture, power, temperature, and damage.
Avoid oversized monuments that exist only as references. Architectural sets need
rules for footprint, material, modularity, ornament hierarchy, deterioration,
defense implications, and how mixed settlements remain visually coherent.

## 14. Cultural Authenticity Guidelines

Aim for cultural integrity, not impossible total authenticity. Integrity means
specific sources, acknowledged uncertainty, avoidance of stereotype, internal
coherence, respectful transformation, and qualified review when stakes warrant it.

Do not treat one period, province, class, gender role, religious tradition, or
language form as universally Irish. Do not turn trauma, colonization, famine,
conflict, or sacred practice into casual bonuses or flavor text. If harm cannot be
handled with gameplay purpose and adequate expertise, exclude it.

## 15. Mythology Guidelines

Myth is narrative tradition, not a monster catalogue. Identify sources, versions,
later reinterpretations, and uncertainty. Avoid presenting one text as a unified
canon or mapping complex beings directly to generic fantasy races.

Mythology enters through RimWorld-compatible explanations: belief, rumor,
anomaly, ecology, genetic engineering, psychic phenomena, ancient technology, or
deliberately unresolved accounts. Players should be able to engage without the mod
becoming a fantasy overhaul. Mythological content remains primarily reserved for
Version 1.5 unless an earlier feature is a small thematic seed with independent
value.

## 16. XML Versus C# Philosophy

Use XML for declarative content and supported composition. Use C# only for behavior
that definitions and stable extension points cannot express clearly, safely, and
performantly. A feature proposal must name the missing capability, not merely say
that code is easier.

Prefer a small reusable comp, worker, or extension point over special-case logic.
Harmony is last resort and requires an ADR, exact target analysis, guarded failure,
conflict tests, and removal criteria. Never use code to hide a weak design or
avoid learning existing RimWorld systems.

## 17. Performance Philosophy

Optimize architecture before micro-optimization. Avoid work every tick, whole-map
or whole-world scans, repeated allocations in hot paths, uncontrolled caches,
and repeated database lookups that RimWorld already indexes.

Each runtime feature identifies frequency, population scale, worst case, save
impact, and profiling plan. Cache only with clear ownership and invalidation.
Performance changes need measurement in representative colonies. A feature that
cannot meet acceptable simulation responsiveness must simplify or defer.

## 18. Compatibility Philosophy

Core content depends only on declared supported RimWorld versions. Optional DLC
and mod integrations are isolated, detected safely, and absent without errors.
Avoid patching broad external definitions or assuming load order without a stated
contract.

Public def names, package IDs, translation keys, save-visible types and fields,
and public APIs are compatibility promises. Changes require migration analysis.
Compatibility effort is risk-based: support a documented matrix, investigate
conflicts responsibly, and never claim universal compatibility.

## 19. Documentation Standards

Write one authoritative source per rule and link to it. State status, owner, date,
scope, assumptions, and review triggers. Requirements are testable; decisions show
alternatives and consequences; research shows sources and uncertainty; tests show
environment and evidence.

Documentation changes ship with the decision or behavior they describe. Use
repository-relative links and stable file names. Avoid aspirational claims written
as current capability.

## 20. ADR Standards

Use ADRs for durable, costly-to-reverse, compatibility-affecting decisions, not
routine implementation details. Create them at the decision point. Follow
`docs/adr/README.md` and `templates/adr.md`.

An ADR cannot override the Constitution or Bible. If an option requires doing so,
amend the higher authority first. Feature review must search existing ADRs and
state whether the proposal conforms, extends, or requires supersession.

## 21. Testing Philosophy

Test player-visible behavior and complete system paths. Static XML and reference
validation, unit tests, integration checks, clean in-game loading, save/load,
optional dependency behavior, compatibility matrices, and structured playtests
provide different evidence and cannot substitute for one another.

Tests for regressions must fail against the broken behavior. Visual acceptance
uses in-game evidence. Release testing uses the exact packaged artifact. Passing
tests do not excuse a feature that is confusing, unbalanced, or culturally weak.

## 22. Future Expansion Philosophy

Design stable seams, not speculative frameworks. Future milestones influence
namespaces, dependency direction, save contracts, and asset organization only
when the present decision would otherwise block them.

New systems earn abstraction after repeated concrete needs. Optional integrations
stay optional. Each milestone may revise the roadmap from evidence, but may not
quietly import later scope. Long-term ambition is protected by shipping small,
coherent, maintainable releases.

## Design Bible Amendment Process

Proposals state the current rule, proposed change, product reason, affected
features and ADRs, migration needs, and rejected alternatives. Maintainer approval
is required. Use semantic versioning: MAJOR changes project identity or removes a
pillar, MINOR adds or materially expands guidance, PATCH clarifies without changing
meaning. Record the new version and update dependent templates in the same change.
