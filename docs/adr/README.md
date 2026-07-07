# Architecture Decision Records

ADRs capture durable decisions and their tradeoffs when the decision is made.
Create one for triggers listed in `docs/architecture.md` or whenever reversal
would be expensive, compatibility-affecting, or hard to infer from code.

Copy `templates/adr.md` to `docs/adr/NNNN-short-title.md`. Numbers are sequential.
Status is Proposed, Accepted, Superseded, or Rejected. Accepted ADRs are not
rewritten to hide history; a new ADR supersedes them and links both directions.

An ADR states context, decision drivers, considered options, decision,
consequences, compatibility/migration impact, validation, and review triggers.

## Records

| ADR | Status | Decision |
|---|---|---|
| [0001](0001-oats-medium-cycle-xml.md) | Accepted | Oats use a medium-cycle, XML-only processing-grain design |
| [0002](0002-version-0.1-package-build-contract.md) | Accepted | Version 0.1 uses a root-level XML-first package and clean staging contract |
| [0003](0003-three-gate-lifecycle.md) | Accepted | Features use the three-gate Approved, Done, Released lifecycle |
