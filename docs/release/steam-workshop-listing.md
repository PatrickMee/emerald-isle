# Steam Workshop Listing

**Status:** Version 0.6.3 release listing input<br>
**Workshop item:** [Emerald Isle 3763433723](https://steamcommunity.com/sharedfiles/filedetails/?id=3763433723)<br>
**Current release:** `v0.6.3` - Bulk Oat Milling<br>
**Publication owner:** Patrick Mee

Steam listing text is managed separately from `About/About.xml`. The description
below is the approved Version 0.6.3 replacement input. Publish it only with the
exact staged v0.6.3 GitHub release artifact.

## Description

```text
Emerald Isle is a lore-friendly RimWorld expansion inspired by Irish history, archaeology, material culture, language, and mythology.

[h1]Version 0.6.3 - Bulk Oat Milling[/h1]

Version 0.6.2 adds linen alternatives for the vanilla flak vest, flak pants,
flak jacket, industrial medicine, and Molotov cocktail recipes. The original
Cloth bills and normal vanilla item stats remain unchanged.

Version 0.6.3 adds an optional x4 hand-quern bill that mills 40 raw oats into 40
milled oats with exact linear labor and no efficiency bonus. The original
single-batch bill remains available.

Version 0.6 adds vanilla-style x4 cooking bills for oat porridge and oat
flatbread. The bills reduce repetitive setup while preserving exact per-unit
ingredients, labor, output, and food behavior.

Version 0.5 adds the wolfhound, a fast domestic coursing and combat companion. It can be trained to guard and attack but cannot rescue, haul, carry caravan cargo, patrol, hunt, or protect livestock autonomously. It costs more to feed and adds more colony wealth than ordinary utility dogs. The mod remains vanilla-friendly, XML-only, and focused on practical choices rather than strict upgrades.

[h1]Current content[/h1]

[list]
[*][b]Oats[/b] - A medium-cycle grain crop with a hand-quern processing chain for milled oats, oat porridge, and oat flatbread.
[*][b]Oat bulk cooking[/b] - Optional x4 porridge and flatbread bills at the Campfire, central hearth, fueled stove, and electric stove, with exact linear scaling and no efficiency bonus.
[*][b]Bulk oat milling[/b] - Optional x4 hand-quern bill for 40 raw oats -> 40 milled oats, with exact linear scaling and no efficiency bonus.
[*][b]Dry-stone wall[/b] - A material-efficient linked stone wall with original artwork.
[*][b]Flax and linen[/b] - Ground-grown flax is harvested as raw flax and processed into linen at vanilla work locations. Linen is a general Fabric with a warm-weather niche and lower durability than cloth.
[*][b]Linen tunic[/b] - A linen-only everyday garment with original ground and worn artwork.
[*][b]Brat cloak[/b] - A Fabric-stuffable shell-layer cloak with a wool-optimal cold-weather niche, low armor, and original art for all supported body types and directions.
[*][b]Central hearth[/b] - A stone-stuffable, continuously fueled household hearth providing heat, light, gathering-spot behavior, campfire-grade cooking, and Emerald Isle oat-food bills.
[*][b]Kerry cattle[/b] - Small, hardy dairy cattle with lower feed use and milk output per animal than vanilla cows.
[*][b]Farmhouse cheese[/b] - A 35-day milk preserve made at the central hearth or vanilla fueled/electric stoves.
[*][b]Wolfhound[/b] - A fast, rough-coated domestic fighter with Intermediate Guard and Attack training, limited utility, high food cost, and uncommon trader availability.
[/list]

[h1]Compatibility[/h1]

[b]Requires RimWorld 1.6 Core.[/b] No DLC is required. Royalty, Ideology, Biotech, Anomaly, and Odyssey are supported. Odyssey adds Attack Target training to the wolfhound through the vanilla combat-canine pattern; it does not add Comfort.

Existing saves can add the Version 0.6.3 content without custom migration or serialized state. Back up important saves before changing any mod list.

[url=https://github.com/PatrickMee/emerald-isle/blob/main/docs/release/v0.6.3.md]Version 0.6.3 release notes[/url]
```

## Detailed Version 0.6.3 Change Note

```text
Version 0.6.3 - Bulk Oat Milling

Added:
- A vanilla-style x4 hand-quern bill: 40 raw oats -> 40 milled oats at 720 work.

Role and balance:
- The bill scales the existing 180 work exactly fourfold and keeps the same
  Crafting labor, effect, sound, and learning factor.
- The original single-batch milling bill and all existing oat-food stats remain
  unchanged.

Compatibility:
- Requires RimWorld 1.6 Core; no DLC or other mod is required.
- Existing saves can add this content without custom migration.

Full release notes:
https://github.com/PatrickMee/emerald-isle/blob/main/docs/release/v0.6.3.md
```

## Verification

After publication, record the public Steam manifest, update time, byte total,
and independent subscriber verification against the exact v0.6.3 GitHub
artifact here or on the merged release PR.
