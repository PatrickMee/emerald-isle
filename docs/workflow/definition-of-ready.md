# Ready Prompts

This is an optional expansion aid for High-Risk work, not a mandatory form for
Routine or Standard changes. The canonical workflow is
[`feature-lifecycle.md`](feature-lifecycle.md).

Standard gameplay is ready when one recorded issue, request, PR, or specification
answers four questions and receives explicit maintainer approval:

- What player value and active-milestone outcome does this create?
- What is in scope, out of scope, and the vanilla comparison/tradeoff?
- What are the XML/C# boundary, public IDs, save, DLC/mod, art, and localization
  implications that actually apply?
- What observable checks will prove the smallest playable slice works?

For High-Risk work, additionally resolve only applicable blockers:

- uncertain historical, cultural, gameplay, or technical claims;
- C#, Harmony, migration, shared-framework, or public-contract decisions;
- significant cultural/Irish-language review needs;
- performance, compatibility, dependency, rollback, or coordination risk.

Standalone research, ADR, architecture, or implementation-plan documents are
created only when they materially resolve one of those blockers.

**Decision:** Approved | Not Approved<br>
**Approved by/date:** [maintainer, YYYY-MM-DD]<br>
**Conditions:** [only material conditions]
