# Done Prompts

This is an optional expansion aid for High-Risk work, not a mandatory form for
Routine or Standard changes. The canonical workflow is
[`feature-lifecycle.md`](feature-lifecycle.md).

Standard gameplay is done when:

- relevant static/build validation passes;
- one complete in-game path through the changed behavior works;
- the log contains no new unresolved error or recurring warning from the change;
- the maintainer accepts gameplay and visual behavior against the approved scope;
- affected public IDs, provenance, changelog, or durable decisions are updated.

Add only the checks triggered by actual risk:

- save/load for new or changed persistent state;
- DLC/mod combinations where behavior varies;
- focused regression for a repaired defect;
- performance evidence for a credible hot path;
- localization/cultural review for affected player-facing material;
- migration and rollback checks for compatibility changes.

Record results and maintainer acceptance once in the implementation PR. A
separate evidence file is reserved for a High-Risk result that cannot fit clearly
in the PR or a genuinely cross-feature matrix.

Record the Done/Not Done decision, maintainer, and date in the implementation PR,
not in a separate Done document.
