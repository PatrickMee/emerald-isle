# Feature Lifecycle

**Status:** Stable baseline under Constitution 4.0.0 and ADR 0004. Material
changes normally require an ADR.

This is the canonical operational workflow. Use the lightest path that safely
matches the change and give every fact one owner.

## Status and Evidence Owners

| Outcome | Sole authoritative record |
|---|---|
| Active milestone | Roadmap |
| Candidate | Feature catalog |
| Approved scope | One chosen issue, direct maintainer request, PR, or risk-justified specification |
| Done implementation | Implementation PR, including verification and maintainer acceptance |
| Release candidate approval | One release PR identifying the exact commit and artifact |
| Released baseline | Immutable Git tag and GitHub release |

Other documents may link to these records but must not mirror their current
status. In particular, do not update the catalog, roadmap, docs index, AGENTS,
art records, or non-owner feature specifications merely because a gate changed.

## 1. Classify

- **Routine:** no new gameplay and no public compatibility-contract change.
- **Standard:** small gameplay using known XML/vanilla patterns. This is the
  default.
- **High-Risk:** C#/Harmony, persistence or migration, new systems/frameworks,
  difficult rollback, performance hot paths, meaningful configuration branching,
  or sensitive cultural/Irish-language material.

When uncertain, start Standard and escalate only when a concrete risk appears.

## 2. Choose One Feature Record

Routine work skips the gameplay approval gate. For Standard work, normally choose
one issue, direct maintainer request, or PR and keep the decision there. A short
repository specification is an exception when durable detail cannot fit clearly
in those records. The chosen record states:

- player value and active milestone;
- smallest coherent scope and explicit exclusions;
- closest vanilla alternative and meaningful tradeoff;
- historical or cultural basis only where it changes the design;
- XML/C# boundary, public IDs, saves, DLC/mod behavior, and assets; and
- the smallest observable acceptance checks.

One explicit maintainer approval authorizes implementation. The implementation PR
must link or restate a direct request so a reviewer can see the approved boundary
without searching chat history.

High-Risk work uses a concise repository specification and adds only the research,
ADR, architecture, plan, migration, or test record needed for its named risks.
Do not generate empty companion artifacts.

## 3. Implement and Verify Once

Deliver the smallest playable slice. Every gameplay change receives:

- relevant static/build validation;
- one complete in-game path through the changed behavior;
- log review for new errors or recurring warnings;
- maintainer gameplay or visual review; and
- focused regression coverage for the defect or risk being addressed.

Add save/load, DLC/mod combinations, performance checks, localization/cultural
review, or broader regression only when the change makes them relevant. Put the
results and maintainer acceptance in the implementation PR; link a detailed test
record only when the evidence cannot fit there. Update durable memory only when
the underlying contract, decision, provenance, user guidance, or risk changed.

The feature is **Done** when the implementation PR records passing affected-path
evidence and maintainer acceptance. Done does not create or promise a release.

## 4. Merge and Release Deliberately

Merge focused, reviewed work. Batch Done features into a coherent release when
that produces a clearer player update and fewer publication cycles. A one-feature
release is valid when feedback, urgency, or product coherence justifies it; state
that reason in the release PR.

Use one release PR to freeze scope, identify the exact commit and artifact digest,
run package and affected-path checks, prepare public notes and rollback, and obtain
approval to publish. After merge, create the immutable tag and GitHub release and
upload the same artifact to the distribution channel.

Record post-publication download/smoke verification in the GitHub release body or
a comment on the merged release PR. Do not open a second bookkeeping PR unless a
durable repository fact is wrong or publication differed from the approved
candidate. Release evidence is version-level; unchanged historical features do
not need their old tests rerun.

## Escalation Triggers

Use the expanded [Ready](definition-of-ready.md) or
[Done](definition-of-done.md) prompts only when they help with High-Risk work.
Create an ADR when reversal would be expensive, compatibility-affecting, or hard
to infer from the implementation. A failed check returns work to the earliest
incorrect assumption.
