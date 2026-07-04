# Version 0.1 Research Sprint

**Status:** Active; oats, dry-stone wall, and hand-quern research approved; milled
oats in review
**Milestone:** Version 0.1 Foundations  
**Objective:** Produce enough historical, gameplay, art, language, and RimWorld 1.6
evidence to validate and specify the approved first release with low uncertainty.
**Implementation authority:** None

## Sprint Outcomes

- Reviewed research briefs for every Priority 1 topic and scoped findings for Priority 2.
- Current RimWorld 1.6 vanilla/DLC comparison data captured from the installed game.
- Source, uncertainty, sensitivity, terminology, and asset-rights records completed.
- XML/C#/Harmony feasibility and save/DLC behavior documented for the features in
  the [approved scope](../product/version-0.1-approved-scope.md).
- Approved scope validated without adding replacement features.
- Version 0.1 implementation plan revised, reviewed, and passed through Definition of Ready.

## Source Program

Use these as discovery anchors, then follow citations into peer-reviewed scholarship,
catalog records, excavation reports, critical editions, and specialist publications.

| Code | Source family | Intended use |
|---|---|---|
| NMI | [National Museum of Ireland: Irish Folklife](https://www.museum.ie/collections/collections-and-research/irish-folk-life/) and archaeology collections | Material culture, farming, food, household industry, furniture, clothing |
| NFC | [Dúchas National Folklore Collection](https://www.duchas.ie/en/info/cbe-collections) | Oral tradition and material-culture accounts with date/place context |
| CELT | [UCC Corpus of Electronic Texts](https://celt.ucc.ie/) | Historical, legal, literary, medical, and mythological texts in critical editions |
| ISO | [Irish Sagas Online](https://iso.ucc.ie/) | Parallel source texts and translations for selected medieval narratives |
| EDIL | [Electronic Dictionary of the Irish Language](https://dil.ie/) | Historical Irish vocabulary and attested senses |
| LOG | [Placenames Database of Ireland](https://www.logainm.ie/en) | Official/historical placename forms, sources, and pronunciation records |
| OPW | [Heritage Ireland](https://heritageireland.ie/) and National Monuments records | Architecture, sites, chronology, function, and measured remains |
| NBDC | [National Biodiversity Data Centre](https://biodiversityireland.ie/) | Species distribution and native/introduced status |
| TEA | [Teagasc](https://teagasc.ie/) | Modern agronomy and food-system evidence; not a substitute for historical sources |
| RW | Installed RimWorld 1.6 Core/DLC Defs, assemblies, dev mode, and [modding references](https://rimworldwiki.com/wiki/Modding_Tutorials) | Current technical and vanilla-system truth |

Every brief must cite exact works/pages or collection records. Institutional landing
pages alone do not substantiate a historical claim.

## Animals

| ID | Topic | Why important | Sources to investigate | Gameplay questions | Vanilla comparison | Technical concerns | Effort | Priority |
|---|---|---|---|---|---|---|---|---|
| A-01 | Working hounds and wolfhound traditions | Tests a highly recognizable animal with colony utility | NMI, NFC, archaeological/zooarchaeological studies, breed-history scholarship | Hauling, guarding, hunting, bonding, or combat; what tradeoff prevents a superior dog? | Husky, Labrador retriever, warg, training and nuzzling | PawnKind/ThingDef, body/graphics, trainability, combat balance, Biotech interactions | H | P2 |
| A-02 | Cattle landraces and husbandry | Supports agriculture, dairy, wealth, and social themes | NMI, agricultural history, zooarchaeology, TEA only for modern comparison | Milk/meat/work value; climate hardiness; herd cost and raid/wealth pressure | Cow, yak, muffalo, pen and lactation systems | XML feasibility, life stages, products, pens, Ideology food rules | M | P2 |
| A-03 | Sheep, goats, wool, and fiber economy | Connects animals to clothing and production | NMI, textile archaeology, husbandry histories | Is a new animal necessary or can recipes/stats use vanilla sheep/goats? | Sheep, goat, wool and shearing | Avoid redundant species; textile Defs and art burden | M | P3 |

## Plants and Agriculture

| ID | Topic | Why important | Sources to investigate | Gameplay questions | Vanilla comparison | Technical concerns | Effort | Priority |
|---|---|---|---|---|---|---|---|---|
| P-01 | Oats and cool-climate cereals | Candidate low-risk first crop and food-chain anchor | Archaeobotany, agricultural histories, NMI, TEA for modern traits | Growth season, fertility, nutrition, labor, blight, and why choose it over rice/corn? | Rice, corn, potatoes, haygrass | Plant/ThingDef XML, sow skill, yield, texture states, Biotech pollution | M | P1 |
| P-02 | Flax, fiber, and oil | Potential bridge between agriculture, textiles, and production | Archaeobotany, NMI textile collections, craft histories | One crop or multiple products; processing burden; distinct role from cotton/devilstrand | Cotton, devilstrand, cloth, chemfuel-like chains | Multi-product harvest may need processing; recipe and textile balance | H | P2 |
| P-03 | Bog, hedgerow, and forage ecology | Prevents generic biome assumptions and informs later resources | NBDC, palaeoenvironmental studies, folklore with context | Wild harvest, medicine, cover, fuel, or pure setting? | Healroot, berry bushes, trees, biomes | World/biome scope is later; avoid premature defs | M | P3 |

## Food and Brewing

| ID | Topic | Why important | Sources to investigate | Gameplay questions | Vanilla comparison | Technical concerns | Effort | Priority |
|---|---|---|---|---|---|---|---|---|
| F-01 | Grain staples, milling, porridge, and bread | Creates a complete visible loop from crop to meal | NMI, food histories, archaeology, household accounts | Direct cooking or milling step; nutrition, shelf life, labor, mood, class/status | Simple/fine meals, nutrient paste, bread-like DLC/mod patterns, cooking bills | Recipes, ingredients, products, work amount, Ideology preferences, art reuse | M | P1 |
| F-02 | Dairy preservation | Connects livestock to storage and food resilience | NMI, dairying archaeology/history, folklore with date/place | Cheese/butter roles; aging versus refrigeration; labor and failure | Milk, meals, pemmican, packaged survival meals | Fermentation/aging may require comps or C#; storage and stacking | H | P2 |
| F-03 | Brewing and distillation chronology | Avoids stereotype and anachronism while assessing later production | Food/drink scholarship, excise records, archaeology, NFC | Social/mood value, addiction, trade, time, skill, fire risk | Beer, psychite tea, drug production, barrels | Fermentation comps, chemical tolerance, Ideology and DLC interactions | H | P3 |

## Resources

| ID | Topic | Why important | Sources to investigate | Gameplay questions | Vanilla comparison | Technical concerns | Effort | Priority |
|---|---|---|---|---|---|---|---|---|
| R-01 | Building stone and dry-stone material logic | Grounds the first architecture candidate in real constraints | Geological Survey resources, NMI/OPW, vernacular architecture studies | New resource or vanilla stone blocks; low cost versus cover/HP/work tradeoff | Stone chunks/blocks, walls, barricades | Stuff versus dedicated Defs, terrain variability, path/cover stats | M | P1 |
| R-02 | Peat/turf fuel | High thematic value but potentially broad system impact | Bog archaeology, NMI, environmental histories, NFC | Extraction, renewability, labor, smoke, storage, fuel niche | Wood, chemfuel, fueled buildings | Map resource generation, terrain changes, fuel filters, performance | H | P3 |
| R-03 | Wool, linen, leather, and dyes | Informs later apparel without redundant materials | NMI, textile archaeology, craft and trade histories | Which materials change decisions rather than just labels? | Cloth, wool types, leather types, dye systems | Stuff categories, market value, color, apparel compatibility | M | P2 |

## Architecture

| ID | Topic | Why important | Sources to investigate | Gameplay questions | Vanilla comparison | Technical concerns | Effort | Priority |
|---|---|---|---|---|---|---|---|---|
| B-01 | Dry-stone boundaries and walls | Strong visible identity with likely XML-only implementation | OPW/NMS records, vernacular surveys, archaeological reports | Wall, fence, or barricade; speed, cover, HP, cost, repair, terrain constraints | Stone wall, barricade, fence, embrasure-like mod patterns | ThingDef/building stats, stuff, pathing, cover, blueprints, damage art | M | P1 |
| B-02 | Ringfort form and settlement organization | Long-term architectural grammar and faction/world-generation input | NMS inventories, excavation reports, landscape archaeology | Player-built kit or generated layout; defense versus land/labor cost | Walls, settlements, ancient complexes | Generation and AI scope later; modular footprints and save stability | H | P2 |
| B-03 | Monastic sites and round towers | Future knowledge, refuge, quest, and landmark possibilities | OPW sites, excavation/architectural studies, annals critically read | Watch, refuge, storage, ritual, quest, or symbolic role? | Shelves, towers in mods, ancient dangers, monuments | Multi-cell building, vertical abstraction, quests, art complexity | H | P3 |

## Furniture

| ID | Topic | Why important | Sources to investigate | Gameplay questions | Vanilla comparison | Technical concerns | Effort | Priority |
|---|---|---|---|---|---|---|---|---|
| U-01 | Hearth as room and social center | Could connect food, heat, gathering, and story | NMI Folklife, excavation reports, household histories | Heat/cooking/social role; is combination too strong? | Campfire, stove, heater, gathering spots | Multi-role comps, room stats, bills, Ideology ritual focus | M | P2 |
| U-02 | Storage, seating, bedding, and domestic layout | Defines visual grammar without decorative clutter | NMI furniture collections, vernacular house surveys | Which item changes comfort, storage, work, or social use? | Shelves, stools/chairs, beds, tables | Avoid reskins; art rotations, linking, storage filters | M | P3 |
| U-03 | Quern and hand-milling equipment | Candidate production link for oat foods | NMI objects, archaeological reports, food-production studies | Separate processing decision or unnecessary labor tax? | Crafting spot, fueled/electric stoves, machining tables | WorkGiver/recipe XML, facility links, graphics and bills | M | P1 |

## Clothing and Equipment

| ID | Topic | Why important | Sources to investigate | Gameplay questions | Vanilla comparison | Technical concerns | Effort | Priority |
|---|---|---|---|---|---|---|---|---|
| C-01 | Brat/cloak forms and materials | Recognizable apparel candidate with climate function | NMI, textile archaeology, manuscript/iconographic scholarship | Warmth, rain, status, work penalty, layering, gender neutrality | Duster, cape, parka, prestige apparel | Apparel layers/body coverage, Royalty/Ideology roles, textures | H | P2 |
| C-02 | Léine and layered garments | Prevents generic medieval costume direction | Textile scholarship, material finds, critical visual sources | Functional niche or visual variant; climate and labor effects | Shirt, tribalwear, formal shirts | Body types, layers, color masks, terminology review | H | P3 |
| C-03 | Weapons and protective equipment evidence | Sets later boundaries before catalog promotion | Archaeology, museum catalogs, military histories | Which tools create new tactics rather than stat variants? | Spears, bows, plate/flak, shields if supported | Combat balance, animations, CE/other mod compatibility, likely C# | H | P3 |

## Culture and Society

| ID | Topic | Why important | Sources to investigate | Gameplay questions | Vanilla comparison | Technical concerns | Effort | Priority |
|---|---|---|---|---|---|---|---|---|
| S-01 | Hospitality, feasting, and reciprocity | Candidate social value grounded in player choices | Legal/literary scholarship, CELT texts, archaeology, NFC cautiously | Guests, gifts, food burden, reputation, mood, obligation, refusal | Hospitality quests, Ideology rituals, social gatherings, trade | Quest/ritual code risk, DLC fallbacks, state and abuse prevention | H | P2 |
| S-02 | Kinship, clientship, and legal ideas | Long-term social architecture for Version 2.0 | Early Irish law scholarship and critical editions, not popular summaries | How to preserve agency and avoid ethnic hierarchy simulation? | Factions, titles, ideology roles, relations | Extensive C#/save/AI scope; cultural sensitivity | XL | P3 |
| S-03 | Learning, poetry, craft, and monastic networks | Supports knowledge, quests, roles, and production | CELT, manuscript studies, OPW/NMI, social histories | Skill learning, preservation, trade, memory, or status? | Books/learning where available, research, quests, roles | DLC-specific systems, skill XP, item/quest architecture | H | P2 |

## Mythology

| ID | Topic | Why important | Sources to investigate | Gameplay questions | Vanilla comparison | Technical concerns | Effort | Priority |
|---|---|---|---|---|---|---|---|---|
| M-01 | Source layers and mythology canon method | Prevents treating later retellings as one ancient canon | CELT, ISO, manuscript/folklore scholarship, NFC for later tradition | How should ambiguity, belief, and competing accounts appear? | Anomaly ambiguity, Ideology beliefs, tales and quests | Canon metadata and DLC boundaries; no 0.1 implementation | H | P2 |
| M-02 | Sidhe/fairy traditions across periods | Prepares Version 1.5 without generic fantasy drift | Medieval texts, later folklore collections, specialist scholarship | Encounter, rumor, psychic/anomaly, or social belief; what remains unresolved? | Anomaly entities/events, quests, psychic systems | C#/event/art scope, Anomaly optionality, cultural review | XL | P3 |
| M-03 | Omens, laments, place-lore, and creatures | Builds a responsibly scoped future candidate pool | CELT, ISO, NFC, place-lore scholarship | Story signals versus deterministic mechanics; avoid monster catalog | Mental states, inspirations, incidents, tales | Event frequency, save state, storyteller compatibility | H | P3 |

## Language and Naming

| ID | Topic | Why important | Sources to investigate | Gameplay questions | Vanilla comparison | Technical concerns | Effort | Priority |
|---|---|---|---|---|---|---|---|---|
| L-01 | Naming morphology and placename elements | Establishes coherent original Rim names without faux Irish | LOG sources/audio, EDIL, modern dictionaries, qualified speaker | How much Irish can remain readable and searchable to all players? | RimWorld settlement/faction/pawn naming rules | NameMakerDefs, grammar, Unicode, localization and generation | H | P1 |
| L-02 | Terminology and pronunciation policy | Prevents inconsistent or decorative Irish across features | EDIL for historical terms, modern authoritative dictionaries, speaker review | Irish-first, English-first, or contextual labels by UI function? | Vanilla labels/descriptions and translation conventions | Key stability, grammar, translator notes, font/UI width | M | P1 |
| L-03 | Fictional name generation | Future faction/world support without importing Earth places | LOG morphology studies, corpus analysis with licensing review | Hand-curated lists or grammar; how avoid accidental real/insensitive names? | RulePackDef/NameMakerDef systems | XML grammar feasibility, collisions, deterministic saves | H | P2 |

## RimWorld Technical Research

| ID | Topic | Why important | Sources to investigate | Gameplay questions | Vanilla comparison | Technical concerns | Effort | Priority |
|---|---|---|---|---|---|---|---|---|
| T-01 | RimWorld 1.6 package, Def, and localization contracts | Establishes verified implementation baseline | Installed Core/DLC files, current assemblies, dev-mode config, RW references | Which supported mechanisms cover the five candidates? | Closest Core/DLC Defs and recipes | Package ID, About.xml later, Def inheritance, keys, load order | M | P1 |
| T-02 | Vanilla balance baselines | Prevents invented numbers and power creep | Installed 1.6 Defs plus controlled in-game measurements | What are lifecycle costs/outputs for crops, walls, foods, stone, work tables? | Exact target Defs for each candidate | Data extraction provenance, DLC differences, difficulty/storyteller effects | M | P1 |
| T-03 | DLC-conditional architecture | Required by official support policy | 1.6 LoadFolders/PatchOperations, DLC package IDs, installed Defs | Which candidate behavior is core, required, optional, or absent? | Vanilla DLC integration patterns | Conditional folders/patches, no missing refs, all-DLC matrix | M | P1 |
| T-04 | Save, removal, and migration behavior | Public IDs become long-term contracts at first release | Installed serialization behavior, controlled save fixtures, compatibility guide | What happens when features/DLC are added, removed, renamed, or updated? | Vanilla missing-content behavior and mod warnings | Def removal, Scribe fields, fixtures, declared compatibility level | H | P1 |
| T-05 | Build, validation, and evidence pipeline | First slice must prove repeatable professional delivery | Project build strategy, current toolchain compatibility, clean test installs | Which checks can run before the game and which require human in-game evidence? | Mature mod build layouts, without copying unverified tooling | No proprietary binaries, deterministic staging, CI secrets, artifact manifest | H | P1 |

## Sprint Sequence

1. **Foundation week:** T-01 through T-05, L-01/L-02, and vanilla baseline capture.
2. **Approved-scope research:** P-01, B-01, F-01, R-01, and U-03 in the mandatory
   order recorded by the [approved scope](../product/version-0.1-approved-scope.md).
3. **Context expansion:** Priority 2 topics needed to challenge candidate assumptions.
4. **Review:** cultural, gameplay, balance, architecture, art, QA, and licensing review.
5. **Decision:** confirm, narrow, or reject conditional behavior through governance;
   do not add scope or implement gameplay.

## Exit Criteria

- All P1 briefs are approved or explicitly reject/defer their candidate.
- Every recommended feature has verified vanilla data and a DLC/save behavior matrix.
- Historical claims have exact citations, confidence, and transformation notes.
- XML feasibility is demonstrated; any C#/Harmony need is named and justified.
- Art and localization needs are estimated from in-game constraints.
- The Version 0.1 implementation plan is updated from findings and human-reviewed.
