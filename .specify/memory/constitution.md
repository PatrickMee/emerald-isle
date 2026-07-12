<!--
Sync Impact Report
- Version: 3.0.0 -> 4.0.0
- Modified principle: VI. Proportional Design and Traceability replaces the
  universal standalone specification with risk-tiered feature records
- Modified principle: VII. Affected-Path Verification replaces universal matrix
  testing with checks selected by changed behavior and failure risk
- Modified section: Development Quality Gates keeps Approved, Done, Released
  while allowing approval and evidence to live in an issue, request, PR, or spec
- Modified section: Process Proportionality defines Routine, Standard, and
  High-Risk work and makes Standard the default gameplay path
- Decision record: ADR 0004
- Templates and runtime guidance updated in the same change
- Historical Version 0.1 records and ADR 0003 remain unchanged
-->
# Emerald Isle Constitution

**Baseline:** v0.0.0; material changes normally require an ADR and Constitution amendment review.

## Core Principles

### I. Gameplay and Story First
Every feature MUST create a meaningful player decision, emergent story, or useful
strategic role. Cultural presence alone is not sufficient. Simplicity MUST win
when additional realism does not create proportional gameplay value.

### II. RimWorld-Native Fit
Content MUST read as a civilization that evolved on the Rim, not transplanted
Earth history. Naming, mechanics, presentation, and fiction MUST fit RimWorld's
tone and systemic language. The mod MUST complement vanilla rather than replace
its identity.

### III. Research With Transformation
Historical and cultural claims MUST be traceable to credible sources and reviewed
for context. Research is design material, not a mandate. The team MUST transform
inspiration into original setting fiction and MUST avoid treating contested,
regional, or modern claims as timeless facts.

### IV. Tradeoffs Over Power
No feature MAY be strictly superior to its vanilla comparison at comparable cost
and availability. Every meaningful advantage MUST carry a visible cost,
constraint, risk, setup burden, or opportunity cost. Balance is evaluated across
the complete acquisition and use lifecycle, not isolated statistics.

### V. Milestone Discipline
Work MUST serve the active milestone. Future plans MAY define extension seams,
but MUST NOT justify speculative implementation. The smallest coherent version
of a feature MUST be preferred, and out-of-scope ideas MUST move to the roadmap
or backlog.

### VI. Proportional Design and Traceability
Gameplay work MUST have recorded scope and explicit maintainer approval before
implementation. For ordinary work, the record MAY be a concise issue, request,
pull request, or specification. It states player value, bounded scope, vanilla
comparison and tradeoff, implementation boundary, compatibility risk, and test
intent at the depth needed to avoid an unresolved design decision during coding.

Routine maintenance that does not change approved gameplay or a public
compatibility contract MAY proceed through normal commit or pull-request review
without a separate Gate 1 record. High-risk work MUST use a concise specification
and any targeted research, ADR, Architecture Review, or plan needed to resolve the
specific risk. Document type is never a gate by itself.

Research MUST be performed when historical, cultural, gameplay, or technical
uncertainty could change the result. Significant technical or product decisions
MUST receive an ADR when reversal would be expensive or compatibility-affecting.
XML is preferred for declarative content; C# requires a documented behavioral
need; Harmony patching requires an ADR and compatibility plan.

### VII. Affected-Path Verification
Passing static checks is necessary but insufficient. Every change MUST verify the
player, build, documentation, or release surface it affects in the real system.
Additional save/load, DLC/mod,
failure, performance, localization, and regression checks are required only when
the changed behavior or a credible failure risk makes them relevant. Evidence MAY
be a concise pull-request note or maintainer confirmation; a standalone matrix is
reserved for cross-cutting or release-level risk.

### VIII. Modular Compatibility
Features MUST be cohesive, independently removable where practical, and isolated
behind stable definitions and namespaces. Optional DLC and cross-mod integrations
MUST fail safely. Public definition names and save-visible data are compatibility
contracts and MUST NOT change without migration analysis.

## Content and Technical Constraints

- Milestone 0 MUST NOT add gameplay XML, C#, textures, audio, or distributable
  mod content.
- Supported RimWorld and DLC versions MUST be recorded before Version 0.1 work.
- All identifiers MUST use the `EI_` prefix unless an adopted ADR defines a more
  specific namespace.
- Third-party sources and assets MUST have recorded provenance and compatible
  licenses before inclusion.
- Localization-ready player-facing text MUST use translation keys; lore and
  terminology decisions MUST include pronunciation or usage notes when useful.
- Generated files MUST be reproducible and MUST NOT be edited by hand.

## Development Quality Gates

A gameplay feature advances through three outcomes. The record and evidence scale
with risk; routine maintenance uses ordinary review and does not pretend to be a
feature gate.

1. **Approved**: a maintainer accepts the recorded player value, bounded scope,
   tradeoff, implementation boundary, compatibility risk, and test intent. For
   Standard work, an issue, request, or PR is sufficient. High-Risk work uses a
   concise specification and only the supporting records its risks require.
2. **Done**: the implementation passes static validation, its affected in-game
   player path, maintainer review, and any additional risk-triggered checks.
   Evidence is recorded once in the PR, feature record, or maintainer review.
3. **Released**: once per version, the exact staged package passes the release
   checklist, including attribution, localization, batched cultural review,
   relevant compatibility checks, rollback, and release-quality smoke testing.

Gates MAY iterate; failed evidence returns to the earliest invalid assumption.

## Process Proportionality

Working, stable, enjoyable software is the primary measure of progress. Documents
MUST exist only when they materially improve implementation, maintenance,
onboarding, verification, release, or future decisions. Contributors MUST reuse and
link authoritative records instead of producing parallel summaries.

Work uses three practical risk classes:

- **Routine:** documentation, metadata, art polish, refactoring, build maintenance,
  or defect repair that restores already-approved behavior. Use a commit or PR and
  verify the changed surface.
- **Standard:** the default for small XML-first gameplay built from proven vanilla
  patterns. Use one short feature record, one approval, implementation, affected-
  path validation, human review, and merge.
- **High-Risk:** C# or Harmony, save migration, a shared framework or new gameplay
  system, difficult rollback, performance-sensitive behavior, significant DLC or
  compatibility branching, or sensitive cultural/Irish-language content. Add only
  the targeted research, specification depth, ADR, plan, and verification matrix
  needed for those risks.

Small features MUST NOT inherit the documentation burden of foundational systems.
Research depth tracks uncertainty; planning tracks technical risk and coordination.
Generalization follows repeated implementation evidence. If maintaining an
artifact costs more than the decision or memory it protects, the team SHOULD
consolidate or retire it through normal review.

## Governance

This constitution outranks all other project documents. Amendments require a
written proposal describing motivation, affected workflows, migration impact,
and template changes. Maintainers approve amendments through review. Versioning
uses semantic versioning: MAJOR for incompatible governance changes, MINOR for
new or materially expanded obligations, and PATCH for non-semantic clarification.

Every gameplay approval and release review MUST include a proportionate
constitution check.
The Design Bible is the canonical creative and product authority beneath this
Constitution. ADRs, milestone plans, discipline guides, and feature records MUST
conform to it and cannot silently override it. Exceptions MUST be time-bounded,
documented in the feature record, and approved by
a maintainer. Compliance is reviewed at each milestone retrospective.

Culturally sensitive and Irish-language content is tracked in the terminology
and canon records as features merge and receives qualified review once per
release at the Released gate. Content flagged high-risk during specification MAY
request earlier review. This batching does not waive the qualified-reviewer
requirement in `GOVERNANCE.md`.

**Version**: 4.0.0 | **Ratified**: 2026-07-04 | **Last Amended**: 2026-07-12
