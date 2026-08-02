# Art Guide

**Status:** Stable baseline at v0.0.0. Material changes normally require an ADR.

## Direction

Art must combine readable RimWorld silhouettes and material language with
Irish-inspired form, craft, landscape, and ornament. Inspiration should be
structural, not a layer of generic Celtic knots or green paint.

## Priorities

1. Gameplay readability at normal zoom and lighting
2. Consistency with vanilla scale, perspective, outlines, and visual density
3. Clear material and state communication
4. Distinctive but restrained cultural character
5. Efficient reuse without obvious repetition

## Feature Art Brief

Every asset request records gameplay function, camera context, dimensions,
states and damage variants, palette/material references, cultural sources,
animation or shader needs, file names, texture paths, and acceptance screenshots.

When several assets represent construction by the same in-world culture, their
briefs also identify the shared material and construction language plus any
intentional functional deviation. Stone assets follow the Design Bible's
[Stone Construction Language](../design/design-bible.md#stone-construction-language).

## Pawn and Animal Sprites

Treat the supported installed RimWorld build as the visual baseline. Before
production, compare the proposed subject with at least two functionally or
physically similar vanilla pawns at normal gameplay zoom.

Animal sprites use compact top-down token anatomy, not standing side-elevation
illustration. The torso remains the dominant silhouette; heads and identifying
features stay readable; legs, feet, and other small anatomy are simplified,
foreshortened, occluded, or integrated into the body edge as the vanilla
comparison requires. A realistic subject does not justify photographic anatomy,
texture density, or perspective.

Approve one representative direction at runtime size before producing the full
directional and state set. It must remain readable when previewed at 64×64,
without depending on fine internal detail. Generation briefs must describe the
required silhouette, projection, and anatomical occlusion explicitly; phrases
such as “RimWorld-style” are not sufficient art direction.

## Pipeline

Keep editable sources outside game-ready exports. Review silhouette and grayscale
readability before detail. Validate exports in-game, including selection overlays,
snow, rain, darkness, damage, rotation, stacking, and adjacent vanilla objects.

AI-generated or externally sourced art requires explicit provenance, license
compatibility, human review, and substantial art-direction control. It must not
imitate a living artist or ingest unlicensed project assets.

## Naming and Organization

Use `EI_<Domain>_<Asset>_<State>` for source and exported names where RimWorld
conventions allow. Texture paths mirror feature domains. Never encode temporary
version numbers into public paths; use source-control history.
