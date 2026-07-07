<!--
Sync Impact Report
- Version: 2.0.0 -> 3.0.0
- Modified principle: VI. Proportional Design and Traceability now folds the
  Feature Acceptance Checklist and readiness review into single-gate
  specification approval
- Modified section: Development Quality Gates collapses from seven gates to
  three (Approved, Done, Released) per ADR 0003
- Modified section: Governance adds per-release batching for cultural and
  Irish-language review
- Templates updated: templates/feature-spec.md
- Runtime guidance updated: docs/workflow/development-workflow.md,
  docs/workflow/feature-lifecycle.md, docs/workflow/definition-of-ready.md,
  docs/workflow/definition-of-done.md, docs/workflow/product-governance.md,
  GOVERNANCE.md, CONTRIBUTING.md, AGENTS.md
- Removed sections: none
- Deferred: .specify/templates/* update opportunistically on next use per
  ADR 0003; historical records under the seven-gate lifecycle are not rewritten
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
Every gameplay feature MUST have an approved specification covering player value,
vanilla comparison, balance intent, implementation approach, and test intent
before implementation. Design Bible conformance is verified through the approval
checklist inside the specification, with review depth proportional to risk. One
maintainer approval of the specification constitutes acceptance, readiness, and
authorization to implement.

Research MUST be performed when historical, cultural, gameplay, or technical
uncertainty could change the design; findings live inside the specification
unless a standalone research brief adds decision value. A standalone Architecture
Review or Implementation Plan MUST be created only when it materially reduces
uncertainty, coordinates multiple files or contributors, protects a compatibility
contract, or improves verification. Otherwise the specification, issue, or pull
request MAY hold the necessary implementation detail. Significant technical or
product decisions MUST receive an ADR when the decision is made. XML is preferred
for declarative content; C# requires a documented behavioral need; Harmony
patching requires an ADR and compatibility plan.

### VII. Whole-System Verification
Passing static checks is necessary but insufficient. Every feature MUST be
verified through its complete in-game player path, including save/load where
state persists, relevant DLC configurations, failure cases, and interactions
with affected vanilla systems. Claims of completion MUST cite current evidence.

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

A feature advances through three gates. Evidence depth is proportional to risk,
but no gate may be silently skipped; a non-applicable requirement needs a concise
written rationale in the feature record.

1. **Approved**: the specification resolves material uncertainty, defines player
   value, scope, tradeoffs, technical boundary, compatibility, and test intent,
   and passes its approval checklist. One maintainer approval authorizes
   implementation. Standalone research, architecture, and plan documents exist
   only when they add decision value.
2. **Done**: the implemented feature passes static validation, its complete
   in-game player path, save/load where state persists, applicable compatibility
   and performance checks, and maintainer playtest covering comprehension,
   balance, and friction. Evidence is recorded in the specification or pull
   request. Design review of the implemented result happens here.
3. **Released**: once per version, the exact staged package passes the release
   checklist, including attribution, localization, batched cultural review,
   compatibility, rollback, and release-quality checks for every feature in the
   version.

Gates MAY iterate; failed evidence returns to the earliest invalid assumption.

## Process Proportionality

Working, stable, enjoyable software is the primary measure of progress. Documents
MUST exist only when they materially improve implementation, maintenance,
onboarding, verification, release, or future decisions. Contributors MUST reuse and
link authoritative records instead of producing parallel summaries.

Small, low-risk features MUST NOT inherit the documentation burden of foundational
systems. Research depth MUST track uncertainty. Architecture and implementation
planning MUST track technical risk and coordination needs. Generalization MUST
follow repeated implemented evidence; anticipated future reuse is not sufficient.
If maintaining a process artifact costs more than the decision or memory it
protects, the team SHOULD simplify or retire the redundant artifact through normal
review.

## Governance

This constitution outranks all other project documents. Amendments require a
written proposal describing motivation, affected workflows, migration impact,
and template changes. Maintainers approve amendments through review. Versioning
uses semantic versioning: MAJOR for incompatible governance changes, MINOR for
new or materially expanded obligations, and PATCH for non-semantic clarification.

Every feature review and release review MUST include a constitution check.
The Design Bible is the canonical creative and product authority beneath this
Constitution. ADRs, milestone plans, discipline guides, and feature records MUST
conform to it and cannot silently override it. Exceptions MUST be time-bounded,
documented in the feature plan, and approved by
a maintainer. Compliance is reviewed at each milestone retrospective.

Culturally sensitive and Irish-language content is tracked in the terminology
and canon records as features merge and receives qualified review once per
release at the Released gate. Content flagged high-risk during specification MAY
request earlier review. This batching does not waive the qualified-reviewer
requirement in `GOVERNANCE.md`.

**Version**: 3.0.0 | **Ratified**: 2026-07-04 | **Last Amended**: 2026-07-07
