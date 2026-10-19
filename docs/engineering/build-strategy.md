# Build Strategy

## Milestones 0 and 0.5

No runtime build exists. Validation covers Markdown links/structure, JSON/YAML,
shell syntax, policy gates, and prohibited gameplay artifacts.

## Version 0.1 Build Contract

Before code begins, adopt an ADR specifying supported operating systems, RimWorld
version, .NET target compatible with that game build, compiler/SDK pin, test
framework, analyzer set, package layout, and CI environment.

The intended pipeline is:

1. validate documentation, XML, references, IDs, localization keys, and assets
2. restore pinned build dependencies
3. compile with warnings treated as errors under the adopted policy
4. run unit and integration-capable tests
5. stage a clean mod directory from declared inputs
6. exclude source, editor, test, and local files
7. generate checksums/manifest and archive deterministically where practical
8. install the staged package into an isolated RimWorld test location
9. run documented in-game smoke and release checks

## Dependency Rules

Do not commit RimWorld, Unity, DLC, Workshop, or other proprietary binaries.
Resolve game references from a documented local environment variable or CI secret
location. Do not redistribute decompiled source. Pin third-party build packages and
review transitive licenses. Runtime dependencies require Design Bible and ADR review.

## Reproducibility

One documented command must create the release candidate from a clean checkout.
The build must not depend on a developer's Workshop folder or mutate source files.
Generated outputs are reproducible, ignored, and rebuilt in CI. Release testing
uses the exact staged archive, not loose developer files.

`python3 tools/build-release.py vX.Y.Z --candidate` creates the review artifact;
the same command without `--candidate` requires clean, synchronized `main` and an
annotated tag identifying `HEAD`. Archives have sorted entries, normalized
timestamps and permissions, and an embedded `About/BuildInfo.txt` containing the
release version, package ID, and Workshop item ID. Excluding a Git commit from
the embedded file lets the approved candidate and tagged-main rebuild remain
byte-identical; the annotated tag and release record retain source provenance.

Steam uploads are staged by `tools/stage-workshop-release.py` from the published
GitHub ZIP. `tools/verify-workshop-release.py` independently compares the public
Steam package and a subscriber cache to that ZIP. CI runs the cumulative runtime
contract validator so a feature branch cannot silently drop previously released
balance values or definitions.

## Hearth Social Prototype Assembly

[ADR 0007](../adr/0007-first-gameplay-assembly-for-hearth-social-relaxation.md)
records the first gameplay assembly decision. For the local prototype, set
`RIMWORLD_MANAGED_DIR` to the installed RimWorld 1.6.4871 rev597 `Managed`
directory and run `./tools/stage-mod.sh`. Staging invokes
`tools/build-assembly.sh`, which verifies the exact game DLL and pinned Mono
Roslyn compiler, then compiles the current `Source/EmeraldIsle` files into the
staged `Assemblies/EmeraldIsle.dll`. No generated DLL belongs in Git or the
source `Assemblies` directory. A missing or changed game reference stops staging
before the previous package is replaced. A public CI runner without licensed
RimWorld references cannot claim a complete package build; the prototype's full
build and game-load evidence must be recorded from a configured local or private
runner.

### Licensed manual CI

Patrick authorized a manually triggered local GitHub runner on 2026-10-18.
`validate-package.yml` separates automatic **source-validation** on GitHub's
Ubuntu machines from **licensed-package-validation** on the Mac. A source-only
success is not package-build evidence. The licensed job runs the complete staging,
compiled-assembly tests, runtime contracts, release safety, developer staging,
texture checks, and release-tool checks. Its successful run for the exact reviewed
commit is required evidence in the implementation/release PR before merge.

The licensed job accepts only a manual dispatch by `PatrickMee` whose
`reviewed_commit` equals the selected ref's exact SHA. Never register a persistent
runner or start a runner with default labels for this public repository. The
operator reviews the workflow and source, registers an ephemeral runner with a
fresh unpredictable label and `--no-default-labels`, dispatches that exact SHA
with the label, checks the queued job, and starts the runner for that one job.
The runner exits and deregisters after the job. No service is installed. Do not
reuse its label. Checkout credentials are not persisted and job permissions are
read-only. Game references stay on the Mac and are never uploaded as artifacts.

Before starting the runner, verify no other job targets its fresh label. Record
the completed run URL and SHA in the PR. Remove an unused offline registration
if dispatch fails. Bootstrap a new workflow dispatch only after GitHub recognizes
the workflow on its default branch; do not merge unreviewed code to work around
that platform requirement. A blocked bootstrap remains a review condition.

This limits exposure; an ephemeral runner is not a sandbox. Only reviewed code
may execute on the maintainer's Mac. Follow GitHub's
[self-hosted runner security guidance](https://docs.github.com/en/actions/reference/security/secure-use).

## Developer Testing Framework

Developer-only test assets live under `Dev/` and are staged only by
`tools/stage-dev-mod.sh` into a separate companion package with packageId
`patrickmee.emeraldisle.devtools`. The public package is always staged by
`tools/stage-mod.sh`.

Release staging runs `tools/validate-release-safety.sh` before publishing the
staged package. The guard fails if developer-only paths, package IDs, or
identifiers appear in the production package. CI validates both the public package
and the developer companion package, but only the public package is a release
candidate.
