# Development Workflow

**Status:** Stable workflow baseline under Constitution 4.0.0 and ADR 0004<br>
**Purpose:** Ship playable, maintainable Emerald Isle features with the least
process that safely protects quality and project memory.

## What Counts as Progress

Progress is working features, gameplay quality, player experience, stability,
balance, compatibility, playtesting, and reliable releases. Documentation is
useful only when it protects a decision, contract, handoff, or verification result.

## Default Artifact Model

| Work | Required records |
|---|---|
| Routine | Commit or PR |
| Standard gameplay | One approval record plus the implementation PR |
| High-Risk gameplay | Repository specification, implementation PR, and only risk-triggered supporting records |
| Release | One release PR, then immutable tag and GitHub release |

The [Feature Lifecycle](feature-lifecycle.md) is the canonical operating rule.
This page is the quick entry point; if wording differs, follow that lifecycle.

## Choose the Lightest Safe Path

### Routine

Use for documentation, metadata, art polish, refactoring, build maintenance, and
fixes that restore approved behavior without changing a public contract.

1. Make the focused change.
2. Validate the affected surface.
3. Review, commit, and merge.

No feature specification, approval checklist, ADR, or evidence file is required.

### Standard — Default Gameplay Path

Use for small XML-first gameplay built from established vanilla patterns.

1. Choose one short feature record in an issue, direct request, or PR: player
   value; in/out scope; vanilla comparison and tradeoff; XML/C# boundary; public
   IDs, saves, DLC and compatibility; acceptance checks.
2. Receive explicit maintainer approval.
3. Implement the smallest playable slice.
4. Run static validation, exercise the changed player path in RimWorld, inspect
   the log, and obtain human gameplay/visual review.
5. Record verification and maintainer acceptance in the implementation PR, update
   only affected durable memory, then merge.

### High-Risk

Use when work introduces C# or Harmony, save migration, shared infrastructure, a
new gameplay system or UI, difficult rollback, performance-sensitive behavior,
material DLC/mod branching, or sensitive cultural/Irish-language content.

Use a concise repository specification, then add only what resolves the identified
risk: targeted research, ADR, architecture note, implementation plan, migration
plan, or focused test matrix. Reclassify work when implementation reveals a
high-risk trigger.

## Three Outcomes

- **Approved:** the maintainer accepts the recorded scope, tradeoff, boundary,
  risks, and test intent. Standard approval may be a direct request or comment.
- **Done:** the affected player path works, relevant checks pass, and the human
  review accepts the result in the implementation PR.
- **Released:** once per version, the exact staged package passes release safety,
  load/smoke checks, applicable compatibility and cultural review, attribution,
  versioning, and rollback preparation.

Failure returns to the earliest incorrect assumption. Document type is never a
gate by itself.

## Rules of Thumb

- Research only the uncertainty that could change the design.
- Test behavior and credible failure modes, not every theoretical combination.
- Save/load is required when the change adds or changes persistent state.
- DLC/mod matrices are required when behavior actually varies by configuration.
- ADRs record expensive-to-reverse decisions, not routine XML fields.
- Implementation plans exist for coordination or complexity, not chronology.
- One fact gets one authoritative record; link it elsewhere.
- Do not propagate lifecycle state through maps, catalogs, non-owner specs, or
  agent guides.
- Generalize after repeated implementations demonstrate a pattern.

The operational checklist is in
[`feature-lifecycle.md`](feature-lifecycle.md). Expanded Ready and Done prompts
remain available for High-Risk work, but are not mandatory forms for Standard work.
