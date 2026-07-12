# Feature Lifecycle

**Status:** Stable baseline under Constitution 4.0.0 and ADR 0004. Material
changes normally require an ADR.

This is the operational workflow. Use the lightest path that safely matches the
change; do not generate one document per stage.

## 1. Classify

- **Routine:** no new gameplay and no public compatibility-contract change.
- **Standard:** small gameplay using known XML/vanilla patterns. This is the
  default.
- **High-Risk:** C#/Harmony, persistence or migration, new systems/frameworks,
  difficult rollback, performance hot paths, meaningful configuration branching,
  or sensitive cultural/Irish-language material.

When uncertain, start Standard and escalate only when a concrete risk appears.

## 2. Approve Gameplay Scope

Routine work skips this feature gate. Standard and High-Risk work record:

- player value and active milestone;
- smallest coherent in-scope slice and explicit exclusions;
- closest vanilla alternative and meaningful tradeoff;
- historical/cultural basis only where it affects the design;
- XML/C# boundary, public IDs, saves, DLC/mod compatibility, and assets;
- a short list of observable acceptance checks.

The record may be an issue, direct maintainer request, PR, or specification. One
explicit maintainer approval authorizes implementation. High-Risk work adds only
the supporting records needed to resolve its specific risks.

## 3. Implement and Verify

Deliver the smallest playable slice. Every change receives:

- relevant static/build validation;
- one complete in-game path through the changed behavior;
- log review for new errors or recurring warnings;
- maintainer gameplay or visual review;
- focused regression coverage for the defect or risk being addressed.

Add save/load, DLC/mod combinations, performance checks, localization/cultural
review, or broader regression only when the change makes them relevant. Record
results once in the PR, issue, or feature record. Update only affected durable
memory such as public IDs, ADRs, provenance, changelog, or actual risks.

The feature is **Done** when the maintainer accepts the implemented result.

## 4. Merge and Release

Merge focused, reviewed work. At release time, test the exact staged package,
confirm developer assets are excluded, perform clean-load and representative
smoke tests, complete applicable attribution/localization/cultural and
compatibility checks, publish, and retain rollback information.

Do not rerun every historical feature test when neither the feature nor its shared
dependency changed. Release evidence is version-level evidence.

## Escalation Triggers

Use the expanded [Ready](definition-of-ready.md) or
[Done](definition-of-done.md) prompts only when they help with High-Risk work.
Create an ADR when reversal would be expensive, compatibility-affecting, or hard
to infer from the implementation. A failed check returns work to the earliest
incorrect assumption.
