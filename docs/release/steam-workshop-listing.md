# Steam Workshop Listing

**Status:** Version 0.3 candidate fields prepared; Steam upload and public
verification pending<br>
**Workshop item:** [Emerald Isle 3763433723](https://steamcommunity.com/sharedfiles/filedetails/?id=3763433723)<br>
**Current release:** `v0.2.0` - The Hearth and Household<br>
**Prepared update:** `v0.3.0` - The Brat Cloak<br>
**Publication owner:** Patrick Mee

Steam listing text is managed separately from `About/About.xml`. The code blocks
below are the exact prepared inputs for the Workshop description and Version 0.3
change note. Apply them with the public package, then confirm
the public Workshop page matches this record.

## Description

```text
Emerald Isle is a lore-friendly RimWorld expansion inspired by Irish history, archaeology, material culture, language, and mythology.

[h1]Version 0.3 - The Brat Cloak[/h1]

Version 0.3 adds a practical brat cloak to the household clothing path. It pairs with the linen tunic as a cheap cold-weather outer layer while remaining less protective than dusters, parkas, and armor. The mod remains vanilla-friendly, XML-only, and focused on practical choices rather than strict upgrades.

[h1]Current content[/h1]

[list]
[*][b]Oats[/b] - A medium-cycle grain crop with a hand-quern processing chain for milled oats, oat porridge, and oat flatbread.
[*][b]Dry-stone wall[/b] - A material-efficient linked stone wall with original artwork.
[*][b]Flax and linen[/b] - Ground-grown flax is harvested as raw flax and processed into linen at vanilla work locations. Linen is a general Fabric with a warm-weather niche and lower durability than cloth.
[*][b]Linen tunic[/b] - A linen-only everyday garment with original ground and worn artwork.
[*][b]Brat cloak[/b] - A Fabric-stuffable shell-layer cloak with a wool-optimal cold-weather niche, low armor, and original art for all supported body types and directions.
[*][b]Central hearth[/b] - A stone-stuffable, continuously fueled household hearth providing heat, light, gathering-spot behavior, campfire-grade cooking, and Emerald Isle oat-food bills.
[/list]

[h1]Compatibility[/h1]

[b]Requires RimWorld 1.6 Core.[/b] No DLC is required. Royalty, Ideology, Biotech, Anomaly, and Odyssey are supported but add no Version 0.3-specific behavior.

Existing Version 0.2 saves can add the brat cloak without custom migration or serialized state. Back up important saves before changing any mod list.

[url=https://github.com/PatrickMee/emerald-isle/releases/tag/v0.3.0]Version 0.3 release notes and manual download[/url]
```

## Version 0.3 Change Note

```text
Version 0.3.0 - The Brat Cloak

Added:
- A practical shell-layer brat cloak craftable from vanilla Fabric textiles at the Crafting Spot and tailoring benches.
- Original ground and worn artwork for Male, Female, Thin, Hulk, and Fat body types in every required direction.

Balance:
- Cheaper and quicker to make than the duster and parka.
- Warmer than the duster but less warm than the parka.
- Less protective than both, with no hot-weather advantage.
- Wool provides stronger cold insulation than cloth.

Compatibility:
- Requires RimWorld 1.6 Core; no DLC or other mod is required.
- Existing Version 0.2 saves can add the brat cloak without custom migration.

Full release notes:
https://github.com/PatrickMee/emerald-isle/releases/tag/v0.3.0
```

## Verification

After applying both fields in Steam, verify through the public Workshop page or
Steam published-file API that:

- the description contains `Version 0.3 - The Brat Cloak`;
- the description names the brat cloak and its wool-optimal cold-weather niche;
- the Version 0.3 change note is visible;
- the preview reads `VERSION 0.3` and `THE BRAT CLOAK` and depicts the practical
  dark brat over the linen underlayer in the established household scene;
- the item still resolves to Workshop ID `3763433723`.

The replacement `About/Preview.png` is recorded in the
[Version 0.3 preview asset record](../art/assets/workshop-preview-v0.3.md). It
remains a candidate until maintainer visual acceptance and the public Workshop
page both confirm the replacement.
