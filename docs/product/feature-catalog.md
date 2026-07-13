# Candidate Feature Catalog

**Status:** Official discovery backlog, not approved scope  
**Owner:** Product governance  
**Rule:** A catalog entry does not authorize gameplay implementation.

This catalog preserves candidate ideas before detailed design. Promotion requires
active-milestone triage, a proportionate Design Bible check, an approved feature
record, and research only where uncertainty could change the decision.

## Estimate Legend

- **Value/confidence/complexity/priority:** H, M, L
- **XML:** Y likely XML-only; M mixed/unknown; N code expected
- **C#:** N not expected; M possible; Y expected
- **Harmony:** N not expected; M possible; Y expected
- **Effort:** XS, S, M, L, XL; discovery uncertainty is included

| ID | Category | Candidate | Version | Value | Hist. confidence | XML | C# | Harmony | Art | Research | Effort | Priority |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AN-01 | Animals | Irish wolfhound-inspired working hound | 0.5 | H | H | M | M | N | H | M | L | H |
| AN-02 | Animals | Small hardy cattle landrace | 0.5 | H | H | Y | N | N | H | M | M | M |
| PL-01 | Plants | Oats | 0.1 | M | H | Y | N | N | M | L | S | H |
| PL-02 | Plants | Flax crop and linen textile | 0.5 | H | H | Y | N | N | M | M | M | H |
| FO-01 | Food | Oat bread and porridge chain | 0.1 | M | H | Y | N | N | M | L | S | H |
| FO-02 | Food | Dairy-preservation foods | 0.5 | H | H | M | M | N | M | M | M | M |
| RS-01 | Resources | Cut peat-like fuel | 0.5 | H | H | M | M | M | M | H | L | M |
| RS-02 | Resources | Worked local stone set | 0.1 | M | H | Y | N | N | M | M | S | H |
| BL-01 | Buildings | Dry-stone wall | 0.1 | H | H | Y | N | N | M | M | M | H |
| BL-02 | Buildings | Ringfort settlement kit | 1.0 | H | H | M | M | N | H | H | XL | M |
| BL-03 | Buildings | Round-tower watch/refuge structure | 1.0 | H | H | M | Y | M | H | H | L | M |
| FU-01 | Furniture | Central hearth furnishing | 0.5 | H | H | M | M | N | M | M | M | M |
| FU-02 | Furniture | Storytelling and music gathering seat | 0.5 | M | M | M | M | N | M | M | M | L |
| WP-01 | Weapons | Sling weapon family | 0.5 | M | H | M | M | M | M | M | M | L |
| WP-02 | Weapons | Spear/javelin specialization | 1.0 | M | H | M | M | M | M | M | L | L |
| AR-01 | Armor | Hide-and-textile protective set | 0.5 | M | M | Y | N | N | H | H | M | L |
| AR-02 | Armor | Elite metalwork defensive set | 1.0 | M | M | M | M | N | H | H | L | L |
| AP-01 | Apparel | Brat-inspired cloak | 0.5 | M | H | Y | N | N | H | M | M | M |
| AP-02 | Apparel | Linen tunic (léine-inspired) | 0.5 | M | H | Y | N | N | H | M | M | M |
| RE-01 | Research | Vernacular masonry methods | 0.1 | M | H | Y | N | N | L | M | XS | H |
| RE-02 | Research | Monastic preservation craft | 0.5 | M | H | Y | N | N | L | H | S | M |
| PR-01 | Production | Quern and milling workflow | 0.1 | H | H | M | M | N | M | M | M | H |
| PR-02 | Production | Brewing and distilling chain | 0.5 | H | H | M | M | N | H | H | L | M |
| RT-01 | Rituals | Seasonal communal feast | 0.5 | H | H | N | Y | M | M | H | L | M |
| RT-02 | Rituals | Hospitality oath gathering | 1.0 | H | M | N | Y | M | M | H | L | L |
| ID-01 | Ideology | Hospitality-centered precepts | 0.5 | H | M | M | M | N | M | H | L | M |
| ID-02 | Ideology | Poet/chronicler social role | 1.0 | H | H | N | Y | M | M | H | L | L |
| FA-01 | Factions | Clan-confederation faction | 2.0 | H | M | N | Y | M | H | H | XL | M |
| FA-02 | Factions | Monastic knowledge enclave | 1.0 | H | M | M | Y | M | H | H | L | M |
| WG-01 | World Generation | Oceanic upland biome | 3.0 | H | H | N | Y | M | H | H | XL | M |
| WG-02 | World Generation | Ringfort settlement generation | 2.0 | H | H | N | Y | M | H | H | XL | M |
| QU-01 | Quests | Lost manuscript recovery | 1.0 | H | H | N | Y | M | M | H | L | M |
| QU-02 | Quests | Livestock raid and restitution | 2.0 | H | M | N | Y | M | M | H | L | M |
| ST-01 | Storyteller | Seasonal resilience storyteller | 1.0 | H | L | N | Y | M | M | H | XL | L |
| ST-02 | Storyteller | Clan obligation storyteller | 2.0 | H | M | N | Y | M | M | H | XL | L |
| MY-01 | Mythology | Sidhe-inspired ambiguous encounters | 1.5 | H | M | N | Y | M | H | H | XL | H |
| MY-02 | Mythology | Omen and lament event chain | 1.5 | H | M | N | Y | M | H | H | L | M |
| EV-01 | Events | Seasonal fair gathering | 0.5 | H | H | N | Y | M | M | M | L | M |
| EV-02 | Events | Traveling poet and news event | 1.0 | H | H | N | Y | M | M | H | L | M |
| EX-01 | Exploration | Monastic ruin sites | 1.0 | H | H | N | Y | M | H | H | L | M |
| EX-02 | Exploration | Western-sea expedition chain | 3.0 | H | L | N | Y | M | H | H | XL | M |
| QL-01 | Quality of Life | Emerald Isle build/category organization | 0.1 | M | N/A | Y | N | N | L | L | XS | H |
| QL-02 | Quality of Life | Compatibility/config diagnostic report | 0.5 | H | N/A | N | Y | M | L | L | M | M |

## Promotion States

`Candidate -> Triaged -> Approved -> Active -> Done -> Released -> Retired`

Only one state is current. State changes are recorded in this catalog or an issue
linked from it. Rejected and retired entries remain visible with rationale.

## Version 0.1 Approved Scope

The authoritative Version 0.1 feature set and constraints are maintained in
[`version-0.1-approved-scope.md`](version-0.1-approved-scope.md). Catalog version
estimates remain discovery metadata and do not override that approval record.

**Released state:** Version 0.1 shipped on 2026-07-12. PL-01 Oats, BL-01
Dry-Stone Wall, PR-01 Hand Quern and milling workflow, and FO-01 Oat Foods passed
Approved, Done, and Released. Their public identifiers and runtime paths are
compatibility contracts. Other entries carrying a 0.1 discovery estimate were not
part of the canonical approved scope and remain candidates unless separately
triaged.

## Version 0.5 First-Slice Proposal

PL-02 Flax/Linen and AP-02 Linen Tunic are combined in the concise Standard
feature record [FS-006 — Linen Household](../specifications/FS-006-linen-household.md).
The proposal is not approved and does not authorize gameplay implementation. Its
research rejects the earlier flax-to-brat combination because the brat is a
woollen cloak; flax oil and the brat both remain outside the proposed slice.

## Version 0.5 Next-Slice Approval

FU-01 Central Hearth is approved for implementation in the concise Standard
feature record [FS-007 — Central Hearth](../specifications/FS-007-central-hearth.md).
The approval authorizes only the bounded XML-first, one-building scope in FS-007;
C#, Harmony, custom gathering behavior, Ideology integration, new fuel resources,
and broader furniture or architecture sets remain excluded.
