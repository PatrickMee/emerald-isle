# Hearth Social Relaxation Prototype

**Status:** Approved for local prototype; human in-game acceptance pending  
**Milestone:** Version 1.0 cohesion  
**Risk:** High-Risk — first gameplay assembly, native job extension, save-visible defs  
**Owner and approval:** Patrick Mee directly approved this bounded design on 2026-10-18 in the project-owner task; the implementation instruction was delegated to this task. This record preserves that human approval and does not create a new agent approval.

## Player value and comparison

The existing central hearth becomes a useful household gathering choice in a mature colony. Its new hearth-specific seated social option gains Social recreation at 120% of ordinary social relaxation while the fire burns. Native social relaxation can still select the hearth at its ordinary rate; this prototype does not change that global job. An ordinary table remains available without the bonus. The hearth still costs stone, space, cooking speed, and continuous wood fuel, reduced by this prototype from 6 to 3 wood/day. The player chooses whether that combined utility is worth its placement and fuel work; no forced event or passive aura is added.

This extends the released FS-007 building under new maintainer approval. FS-007's original no-C# exclusion defined the earlier shipped slice and is not retroactive authority over this extension.

## Approved boundary

- Keep `EI_CentralHearth`, its work-giver, recipes, output, localization keys, texture paths, package ID, and existing save data stable.
- Set the hearth's `CompRefuelable.fuelConsumptionRate` to 3.0 wood/day.
- Use RimWorld's existing Social joy kind, need, tolerance, boredom, timetable, seating, and gathering toggle. The 1.2 gain factor applies only while a valid seated social job targets an active, fueled, operational Emerald Isle hearth; it stops when fuel runs out or the gather spot is disabled.
- Keep the cooking interaction cell unreserved and available to cooks during social relaxation. Preserve normal Core behavior with or without supported DLC.
- Do not add Harmony, a global social patch, a new joy kind, mood aura, ritual, forced gathering, new fuel, or a serialized component.

## Implementation and compatibility decision

XML carries the fuel value and new job/joy-giver definitions. The small C# assembly uses native `JoyGiver_SocialRelax` selection and `JobDriver_SocialRelax` toils, replacing only the selected hearth job's joy tick because native social relaxation passes no joy source and XML `JoyGainFactor` cannot affect it. The first-assembly build contract is [ADR 0007](../adr/0007-first-gameplay-assembly-for-hearth-social-relaxation.md). New `EI_` job/joy-giver defs are additive; existing saves retain the same hearth and gather-spot state. Removing this prototype from a save leaves RimWorld to abandon its transient custom jobs, while the released building remains defined; this needs a disposable-save check before a release claim.

## Acceptance and evidence still needed

1. Verify the hearth-specific option with an eligible chair near an active, fueled hearth yields a seated Social relaxation job with 1.2 gain; ordinary table relaxation retains its normal rate. No chair, disabled gathering, or no fuel yields no bonus. Fuel loss during a job stops the bonus immediately. Native SocialRelax may still use the hearth at 1.0; judge whether the option is discoverable and useful enough without changing that vanilla path.
2. Verify a cook can use the hearth while a pawn relaxes nearby, with the cooking interaction cell clear.
3. Build from verified RimWorld 1.6 references, stage a clean package with exactly one current assembly, and load Core plus the all-supported-DLC configuration without errors.
4. Have Patrick test the new behavior in a copied colony, save/reload, and accept or reject the prototype. Automated startup and static checks alone do not mark this feature Done or Released.

## Release integration

Patrick authorized a manually triggered licensed local runner on 2026-10-18. The workflow now distinguishes automatic public source validation from the complete manually dispatched assembly/package build on the Mac. The exact reviewed commit must have a successful licensed package run before merge/release; a green source-only job is insufficient. See [Build Strategy](../engineering/build-strategy.md#licensed-manual-ci). Never redistribute proprietary references or route unreviewed PR code to the Mac.

## Local prototype verification — 2026-10-18

- Implementation commit: `25fe554c6d45d45f6d677346095e502dfa1ff1ed`. Local build, all 24 regression checks, runtime contracts, texture references, developer-package staging, release-tool syntax, and release-safety validation passed. The assembly checks inspect compiled wiring; they do not simulate a seated pawn.
- Two separate builds produced the same DLL SHA-256: `5571046eed53ac829e0f5056e56a5f40448c4a0fdb39e0a9f1de25b0d5028928`. The installed local package exactly matched all 122 staged files. Its manifest SHA-256 is `fdddb09e7e3929bf5f96d06574a0fc66e7d4165a4eb2e3ed6669fb1ca99e771c`.
- The exact installed package reached new-game initialization in isolated batch-mode Core-only and Core-plus-all-five-DLC runs, each observed for 95 seconds. Logs had no mod-load/type/XML exceptions. Direct-launch Steam initialization and zero-resolution batch-mode notices also occur in the unchanged baseline; these checks do not establish Steam-launch or visible-UI behavior.
- Prior local readiness package (119 files) was backed up and verified before replacement. The released v0.7.1 rollback ZIP remains unchanged. Ignored local manifests, startup logs, build identity, and backup are under `build/hearth-social-test/`; normal save/configuration folders were not used.
- Review tightened multi-cell seat exclusion to keep every possible assigned sitting cell off the cooking position and preserved native optional-drink finalization. Human recreation-rate, cooking-concurrency, fuel/toggle, and save/reload acceptance remain pending. Nothing was pushed, merged, tagged, or published.
