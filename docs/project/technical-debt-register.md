# Technical Debt Register

Technical debt is an explicit tradeoff with a removal condition, not a synonym for
unfinished work or defects.

| ID | Debt | Introduced | Reason | Impact | Repayment trigger | Owner | Status |
|---|---|---|---|---|---|---|---|
| TD-000 | No implementation debt; pre-implementation project | 2026-07-04 | Milestones 0/0.5 contain no runtime work | None | Version 0.1 planning | Tech lead | Baseline |

New entries link the authorizing spec/ADR, quantify ongoing cost, and identify the
event that makes repayment mandatory. Critical security or data-integrity defects
are not debt and cannot be deferred through this register.
