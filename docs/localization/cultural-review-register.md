# Cultural Review Register

**Purpose:** Accumulates Irish-language and culturally sensitive content as
features merge, for batched qualified review at each release gate
(Constitution 4.0.0, ADR-0004, `GOVERNANCE.md`). A suitably qualified reviewer
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

## Version 0.2 (reviewed)

| Item | Feature | Player-facing? | Sensitivity notes | Review status |
|---|---|---|---|---|
| Flax, raw flax, linen, and linen tunic names, descriptions, gameplay framing, and runtime art | FS-006 | Yes | Functional English; the linen tunic is inspired by the `leine` garment category without claiming an exact reconstruction, universal cut, status, or color; no Irish-language text | Approved 2026-07-13 |
| Central hearth name, description, gameplay framing, and runtime art | FS-007 | Yes | Functional English; broad domestic-hearth framing without claiming one exact Irish archaeological form, ritual meaning, or decorative shorthand; no Irish-language text | Approved 2026-07-13 |

No Irish-language player-facing strings ship in Version 0.2. Patrick Mee reviewed
the low-risk English framing and runtime art as an Irish citizen with lived
cultural familiarity; this approval does not claim Irish-language or specialist
archaeological authority.

## Review Log

| Release | Reviewer | Qualification basis | Date | Outcome |
|---|---|---|---|---|
| v0.1.0 | Patrick Mee | Irish citizen with lived cultural familiarity; review scope limited to low-risk player-facing English and general cultural framing, not Irish-language translation or specialist archaeological validation | 2026-07-12 | Pass — all five Version 0.1 entries approved; no Irish-language content present |
| v0.2.0 | Patrick Mee | Irish citizen with lived cultural familiarity; review scope limited to FS-006/FS-007 low-risk English names, descriptions, gameplay framing, and runtime art, not Irish-language translation or specialist archaeological validation | 2026-07-13 | Pass - FS-006 and FS-007 approved; no Irish-language content present |
