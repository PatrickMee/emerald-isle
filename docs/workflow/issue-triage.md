# Issue Triage Guide

## Intake

Confirm the report is safe to discuss publicly, reproducible enough to act on, in
scope, and not a duplicate. Ask for the minimum missing evidence; remove personal
data and redirect security reports privately.

## Types and Priority

- **Blocker:** prevents load, corrupts data/save, security issue, or blocks release.
- **Critical:** common severe gameplay failure with no reasonable workaround.
- **Major:** material behavior, compatibility, balance, or accessibility defect.
- **Minor:** limited impact or clear workaround.
- **Proposal/research/docs/support:** not ranked as a defect until accepted.

Priority considers impact, prevalence, supported configurations, milestone, and
cost of delay. Popularity alone does not override Design Bible or milestone scope.

## States

`New -> Needs evidence -> Triaged -> Accepted/Deferred/Rejected -> In progress -> Review -> Closed`

Every closure states resolution: fixed, duplicate, cannot reproduce, unsupported,
out of scope, superseded, or documented limitation. An accepted issue may itself
serve as the Standard feature record when it contains the lifecycle's required
scope, tradeoff, boundary, and acceptance checks. High-Risk proposals escalate to
a concise specification and only their risk-triggered records.
