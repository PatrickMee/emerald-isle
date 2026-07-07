# Definition of Ready (Gate 1 Approval Checklist)

This checklist lives inside or alongside the feature specification. Passing it
with one maintainer approval means the feature is accepted, ready, and
authorized for implementation. Evidence depth is proportional to uncertainty and
risk; a requirement does not imply a standalone document. Non-applicable items
need a concise rationale in the feature record.

- [ ] Catalog ID, owner, and active milestone are assigned; the feature belongs
      to the current approved scope.
- [ ] Player problem, meaningful decision, story value, and bounded first slice
      are clear; explicit exclusions prevent scope leakage.
- [ ] Constitution and Design Bible conformance are reviewed, including
      tradeoffs over power and vanilla-native fit.
- [ ] Material historical, cultural, gameplay, and technical uncertainty is
      resolved in the specification; a standalone research brief exists only
      when it adds decision value.
- [ ] Vanilla/DLC comparison and balance hypothesis are measurable.
- [ ] Irish-language and culturally sensitive content is identified and flagged
      for the release-time register; high-risk content notes whether earlier
      qualified review is requested.
- [ ] The XML-first decision is documented; C# and Harmony needs are justified,
      with ADRs for durable choices; public identifiers, save impact, and
      compatibility are stated.
- [ ] Acceptance, edge, failure, and persistence scenarios exist; test and
      playtest intent is actionable.
- [ ] Art, audio, and localization needs are defined or marked not applicable.
- [ ] No blocking dependency or unresolved question prevents the first slice.

**Decision:** Approved | Not Approved
**Approved by/date:** [maintainer, YYYY-MM-DD]
**Conditions:** [none or explicit conditions]
