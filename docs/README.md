# Documentation Strategy

This directory is the studio handbook and historical project memory. New
contributors start with the Constitution, Design Bible, roadmap, lifecycle, and
the active feature record; they do not need to read the whole repository.

## Authority Order

1. `.specify/memory/constitution.md` governs non-negotiable principles.
2. `design/design-bible.md` governs creative and product identity.
3. Accepted ADRs govern durable technical decisions.
4. The active milestone and chosen feature record govern current scope, with any
   risk-triggered records.
5. Domain guides govern design, art, engineering, research, QA, and release.
6. Feature documents govern one feature and cannot silently override higher
   authorities.

Conflicts are resolved by updating the lower-authority document or formally
amending the higher-authority one.

## Where Things Live

| Need | Authoritative location |
|---|---|
| Active milestone and long-range outcomes | `roadmap.md` |
| Unapproved ideas and discovery estimates | `product/feature-catalog.md` |
| Standard feature approval | One chosen issue, direct maintainer request, PR, or exceptionally useful short spec |
| High-Risk feature approval | `specifications/` plus only risk-triggered records |
| Feature implementation and Done evidence | The implementation PR |
| Released baseline | Immutable Git tag and GitHub release |
| Durable technical decision | `adr/` |
| Product and discipline rules | `design/`, `art/`, `engineering/`, `research/`, `qa/`, `release/`, `workflow/` |
| Historical feature/release records | `specifications/`, `research/`, `plans/`, `architecture/`, `release/` |
| Project memory | `project/`, `localization/`, `glossary.md` |
| Reusable forms | `../templates/` and `../.github/` |

This index maps kinds of authority, not the current status of individual features
or versions. Browse the directories or repository history for historical records.

## Maintenance Rules

- Keep one authoritative home for each rule, decision, status, and evidence set;
  link rather than duplicate.
- Do not mirror feature or release status in this index, agent instructions, the
  catalog, art records, or other navigation documents.
- Standard work uses one feature record and its implementation PR. A repository
  specification is normally High-Risk and is justified for Standard work only when
  durable detail cannot live clearly in an issue, direct request, or PR.
- Create standalone research, architecture, planning, and evidence documents only
  when a concrete risk makes them useful.
- Use repository-relative links.
- State owner, document status, and review trigger when a document is provisional.
- Update affected guides and templates in the same change as a policy decision.
- Archive superseded decisions through ADR status; do not erase history.
- Documentation changes receive the same review discipline as implementation.

## Foundation Authorities

The complete frozen Milestone 0 authority manifest lives in
[`foundation-baseline.md`](foundation-baseline.md). That historical baseline is
not a live status dashboard. Current operating rules live in the authorities
linked above.
