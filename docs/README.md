# Documentation Strategy

This directory is the studio handbook. Documents are organized by decision
domain so contributors can find the authority for a question without reading
the whole repository.

## Authority Order

1. `.specify/memory/constitution.md` governs non-negotiable principles.
2. `design/design-bible.md` governs creative and product identity.
3. Accepted ADRs govern durable technical decisions.
4. The active milestone specification and any applicable architecture or
   implementation record govern current scope.
5. Domain guides govern design, art, engineering, research, QA, and release.
6. Feature documents govern one feature and cannot silently override higher
   authorities.

Conflicts are resolved by updating the lower-authority document or formally
amending the higher-authority one.

## Map

- `vision.md`: product identity and boundaries
- `design/design-bible.md`: canonical creative and product identity
- `product/feature-catalog.md`: official discovery backlog
- `product/version-1.0-vision.md`: stable long-term product philosophy after approval
- `product/version-0.1-approved-scope.md`: canonical Version 0.1 approval and scope boundary
- `product/version-0.1-scope-freeze.md`: superseded scope record and compatibility redirect
- `project/`: risk, technical debt, and research memory
- `onboarding/`: contributor startup guidance
- `roadmap.md`: milestone outcomes and release horizons
- `foundation-baseline.md`: frozen v0.0.0 authority manifest
- `architecture.md`: target mod and repository architecture
- `design/`: gameplay and balance rules
- `art/`: visual direction and asset pipeline
- `engineering/`: code, XML, asset, and localization conventions
- `research/`: historical and cultural research practice
- `research/version-0.1-research-sprint.md`: active structured research program
- `research/version-0.1/oats.md`: approved PL-01 historical and gameplay research
- `research/version-0.1/dry-stone-wall.md`: approved BL-01 historical and gameplay research
- `research/version-0.1/hand-quern.md`: approved PR-01 research with gameplay conditions
- `research/version-0.1/milled-oats.md`: approved PR-01 / FO-01 research with gameplay conditions
- `research/version-0.1/oat-foods.md`: approved FO-01 historical and gameplay research
- `research/version-0.1/research-completion-summary.md`: completed Version 0.1 research record
- `product/version-0.1-readiness-review.md`: approved Research-to-Specification transition gate
- `specifications/FS-001-oats.md`: approved, Ready, and implementation-authorized Oats specification
- `specifications/FS-002-dry-stone-wall.md`: approved and frozen Dry-Stone Wall specification
- `specifications/FS-003-hand-quern.md`: approved conditional Hand Quern specification
- `architecture/AR-002-dry-stone-wall.md`: approved Dry-Stone Wall architecture and Ready assessment
- `architecture/AR-001-oats.md`: approved Oats architecture
- `plans/IP-001-oats.md`: approved Oats implementation plan
- `release/package-build-contract.md`: approved Version 0.1 package metadata and staging contract
- `release/v0.1-release-checklist.md`: Version 0.1 release record in preparation
- `localization/cultural-review-register.md`: batched cultural and Irish-language review register
- `qa/version-0.1-release-test-matrix.md`: Version 0.1 exact-artifact release test matrix
- `qa/`: automated, integration, and playtest strategy
- `release/`: packaging, compatibility, and release process
- `workflow/`: feature lifecycle, Git, versioning, and AI collaboration
- `adr/`: durable decision records
- `../templates/`: reusable working documents
- `../specs/`: active and completed Spec Kit workstreams

## Maintenance Rules

- Keep one authoritative home for each rule; link rather than duplicate.
- Create standalone research, architecture, planning, and evidence documents only
  when they materially improve implementation, maintenance, onboarding, or decisions.
- Use repository-relative links.
- State owner, status, and review trigger when a document is provisional.
- Update affected guides and templates in the same change as a policy decision.
- Archive superseded decisions through ADR status; do not erase history.
- Documentation changes receive the same review discipline as implementation.

## Milestone 0 Deliverables Map

| Deliverable | Authority |
|---|---|
| Repository structure | `architecture.md` |
| Documentation strategy | this document |
| Constitution | `../.specify/memory/constitution.md` |
| Vision and roadmap | `vision.md`, `roadmap.md` |
| Design Bible and feature gate | `design/design-bible.md`, `design/feature-acceptance-checklist.md` |
| Architecture | `architecture.md` |
| Balance and art | `design/balance-guide.md`, `art/art-guide.md` |
| Coding, XML, and C# standards | `engineering/coding-standards.md` |
| Contribution and research | `../CONTRIBUTING.md`, `research/research-guide.md` |
| ADR process | `adr/README.md`, `../templates/adr.md` |
| Feature and research templates | `../templates/feature-spec.md`, `../templates/research-brief.md` |
| Assets and localization | `engineering/asset-localization.md` |
| Testing and release | `qa/testing-strategy.md`, `release/release-strategy.md` |
| AI collaboration | `workflow/git-versioning-ai.md` |
| Development workflow | `workflow/development-workflow.md` |
| Branching and versioning | `workflow/git-versioning-ai.md`, `release/release-strategy.md` |
| Feature catalog and lifecycle | `product/feature-catalog.md`, `workflow/feature-lifecycle.md` |
| Ready and Done gates | `workflow/definition-of-ready.md`, `workflow/definition-of-done.md` |
| Build, performance, compatibility | `engineering/build-strategy.md`, `engineering/performance-budget.md`, `engineering/compatibility-policy.md` |
| Project memory registers | `project/risk-register.md`, `project/technical-debt-register.md`, `project/research-catalog.md`, `glossary.md` |
