# Cultural Review Register

**Purpose:** Accumulates Irish-language and culturally sensitive content as
features merge, for batched qualified review at each release gate
(Constitution 3.0.0, ADR-0003, `GOVERNANCE.md`). A suitably qualified reviewer
evaluates every open row before a release is approved; this authority is not
presumed from maintainership. Content flagged high-risk at specification time
may request earlier review.

Add a row when a merged feature ships player-facing Irish-language text, names
or depicts a cultural practice, or transforms sensitive material. Design-level
inspiration documented only in research briefs and specifications does not
require a row unless it surfaces to players.

## Version 0.1 (reviewed)

| Item | Feature | Player-facing? | Sensitivity notes | Review status |
|---|---|---|---|---|
| "oat plant" / "oats" labels and descriptions | FS-001 | Yes | Functional English; no Irish-language text; agricultural framing only | Approved 2026-07-12 |
| "dry-stone wall" label and description | FS-002 | Yes | Functional English; cashel inspiration remains design documentation, not player text | Approved 2026-07-12 |
| "hand quern" / "mill oats" labels and descriptions | FS-003 | Yes | Functional English; domestic milling is historically inspired; no Irish-language term or reconstruction claim appears in game | Approved 2026-07-12 |
| "milled oats" label and description | FS-004 | Yes | Functional English; presented as a gameplay ingredient rather than a standardized historical product | Approved 2026-07-12 |
| "oat porridge" / "oat flatbread" labels and descriptions | FS-005 | Yes | Functional English; ordinary food framing; no claim of an exact historical recipe or universal Irish identity | Approved 2026-07-12 |

No Irish-language player-facing strings shipped in Version 0.1. The batched
review confirmed the register and the absence of Irish-language content rather
than reviewing translations.

## Review Log

| Release | Reviewer | Qualification basis | Date | Outcome |
|---|---|---|---|---|
| v0.1.0 | Patrick Mee | Irish citizen with lived cultural familiarity; review scope limited to low-risk player-facing English and general cultural framing, not Irish-language translation or specialist archaeological validation | 2026-07-12 | Pass — all five Version 0.1 entries approved; no Irish-language content present |
