# Release Candidate: [Version]

Use this checklist in the single release PR. Mark a conditional item N/A with a
short reason instead of creating a separate evidence document.

**Included Done PRs:** [links]<br>
**Release reason/coherence:** [why these changes belong in one release]<br>
**Exact commit:** [full SHA]<br>
**Artifact:** [filename]<br>
**SHA-256:** [digest]

- [ ] Scope is frozen and every included feature is Done
- [ ] Archive was built from the exact clean commit above
- [ ] Relevant static, automated, and targeted regression checks pass
- [ ] Clean in-game load and affected feature paths pass
- [ ] No blocker or critical defects remain
- [ ] Package metadata, dependencies, load order, casing, and exclusions pass
- [ ] Applicable save/load, DLC/mod, performance, and cultural checks pass or are N/A
- [ ] Localization, credits, licenses, and attribution pass
- [ ] Changelog, known issues, install/upgrade notes, and rollback are ready

**Decision:** Approved to publish | Not approved<br>
**Release authority/date:** [name, YYYY-MM-DD]<br>
**Conditions:** [material conditions only]

After publication, record tag, GitHub release, distribution URL, and downloaded
artifact smoke result in the GitHub release body or a comment on the merged release
PR. Do not open a bookkeeping PR unless a durable repository fact is wrong or the
published result differs from this candidate.
