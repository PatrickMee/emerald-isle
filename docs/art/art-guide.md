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
