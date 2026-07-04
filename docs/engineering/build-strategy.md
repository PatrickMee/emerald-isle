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
