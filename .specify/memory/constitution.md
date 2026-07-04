<!--
Sync Impact Report
- Version: 1.0.0 -> 1.1.0
- Added principles: Gameplay and Story First; RimWorld-Native Fit; Research With
  Transformation; Tradeoffs Over Power; Milestone Discipline; Traceable Design;
  Whole-System Verification; Modular Compatibility
- Added sections: Design Bible authority and mandatory feature conformance
- Templates updated: .specify/templates/spec-template.md,
  .specify/templates/plan-template.md, .specify/templates/tasks-template.md
- Deferred: license selection and initial supported RimWorld/DLC matrix
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

### VI. Traceable Design Before Implementation
Every gameplay feature MUST have approved research, specification, vanilla
comparison, balance analysis, technical plan, and test intent before content or
code is merged. Every feature MUST pass the canonical Design Bible's Feature
Acceptance Checklist before implementation planning becomes executable.
Significant technical or product decisions MUST receive an ADR when the decision
is made. XML is preferred for declarative content; C# requires a documented
behavioral need; Harmony patching requires an ADR and compatibility plan.

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

A feature advances only when evidence satisfies the gate for its stage:

1. **Research**: claims sourced, uncertainty and sensitivity recorded.
2. **Concept**: gameplay purpose, player choice, and scope are explicit.
3. **Reviews**: cultural, gameplay, vanilla-fit, balance, architecture, and art
   reviewers approve or record conditions.
4. **Plan**: implementation, dependencies, compatibility, migration, and tests
   are actionable.
5. **Implementation**: static validation and targeted automated tests pass.
6. **In-game verification**: full player path and persistence behavior pass.
7. **Playtest**: balance hypotheses are evaluated against recorded observations.
8. **Release**: packaging, attribution, localization, compatibility, and rollback
   checks pass.

Review stages MAY iterate or run in parallel, but no gate may be silently skipped.
A non-applicable gate requires a written rationale in the feature record.

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

**Version**: 1.1.0 | **Ratified**: 2026-07-04 | **Last Amended**: 2026-07-04
