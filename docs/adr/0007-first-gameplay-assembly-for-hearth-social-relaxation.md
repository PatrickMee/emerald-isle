# ADR 0007: Compile a Small Core Assembly for Hearth Social Relaxation

**Status:** Accepted<br>
**Date:** 2026-10-18  
**Decision owner:** Patrick Mee<br>
**Accepted by/date:** Patrick Mee, 2026-10-18, explicitly selected “Approve the ADR 0007 design” after reviewing the small native-social assembly and local build approach in the implementation chat. This records human approval, not agent self-approval.<br>
**Related:** [Hearth prototype record](../specifications/hearth-social-relaxation.md), [ADR 0002](0002-version-0.1-package-build-contract.md)

## Context and decision

The released hearth is a native `CompGatherSpot`. RimWorld 1.6.4871 rev597's `JobDriver_SocialRelax` calls `JoyUtility.JoyTickCheckEnd` with a null joy source and factor 1.0. Setting a building joy stat in XML therefore cannot produce the approved 1.2 seated-hearth rate. A generic building-interaction job would reserve the worktable and risk blocking cooks. Harmony would modify global behavior and is outside approval.

Add one `EmeraldIsle.dll` core assembly containing only the hearth-specific joy giver and job driver. The joy giver delegates candidate-seat and optional-drink selection to native social relaxation and accepts only active, fueled `EI_CentralHearth` jobs with a real seat outside the cooking interaction cell. The driver keeps native social toils, seat reservations, ingestion, comfort, facing, and social mode, replacing only the recreation tick with the native `JoyUtility` call at factor 1.2 while eligibility remains true. It never reserves the hearth itself. There is no Harmony dependency, global patch, or custom serialized state.

The separate native SocialRelax giver remains available and can still choose the hearth at its ordinary rate. The prototype therefore adds a 1.2 hearthside option without claiming that every social job at the hearth is boosted. Native gathering-area callers use ordinary SocialRelax; the custom giver returns no job for that entry point.

The verified installed 1.6 assembly has one `SuperActive`/`Delay`/`joyDuration` social toil with a recreation tick. Its reservations cover the sitting cell and optional drink, not target A (the hearth). The original tick uses `JoyTickFullJoyAction.GoToNextToil`, which reaches optional drink finalization; the custom tick preserves that action. `CompRefuelable.HasFuel` gates the hearth's fire overlay and glower and accounts for its vacuum setting; the prototype also honors `FlickUtility.WantsToBeOn`. These seams were checked against the DLL hash and MVID above.

## Build contract

- Target the installed RimWorld 1.6.4871 rev597 `Assembly-CSharp.dll`, verified by SHA-256 `6d06b881d59cb54d05b674e8631fa2e8b1629dc8b8dd294a5bcc928f1e5d2148` and MVID `967DDB80-5594-49F0-A776-DAFA26A855D1`. Use only the game's Core, Unity Core, and bundled `netstandard.dll` assemblies as game compile references; never commit or package those references.
- Pin the local compiler to Mono Roslyn `csc` 3.9.0-6.21124.20, target the .NET Framework 4.7.2 reference API, use C# 7.3 or older syntax, and treat compiler warnings as errors. The source has no NuGet/runtime dependency or analyzer package; focused package-contract tests and in-game smoke cover this prototype.
- `tools/build-assembly.sh` requires an explicit `RIMWORLD_MANAGED_DIR` pointing to the installed game's managed assembly directory. Public staging compiles from source into an ignored temporary build directory and copies only the new DLL into `Assemblies/`; it fails before replacing the destination if references, compiler, or output are missing or stale. Generated DLLs remain ignored and are never edited or committed.
- CI provides the same verified game references through a licensed runner before it can compile the full package. Patrick authorized the manual local-runner setup on 2026-10-18. The integration separates automatic public source checks from the complete manually dispatched package job on a one-job, uniquely labeled local runner, as described in [Build Strategy](../engineering/build-strategy.md#licensed-manual-ci). A public GitHub runner must not claim the assembly was built or staged. A successful licensed-package run for the exact reviewed source and exact-artifact verification remain required release evidence.

## Consequences and revisit

This creates the first save-visible C# class names and an assembly build dependency. Preserve the `EmeraldIsle` namespace/class names after public release or perform migration review. Revalidate the exact RimWorld API and compiler when the supported game build changes. Remove the custom job/joy-giver cleanly if the prototype fails Patrick's seated-use or cooking-concurrency playtest. No released artifact follows from this ADR alone.
