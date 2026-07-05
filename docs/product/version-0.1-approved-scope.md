# Version 0.1 – The First Holding

## Overall Scope

Approved.

Version 0.1 remains intentionally small.

Primary goals:

- Establish the identity of an early medieval Irish holding.
- Prove the Emerald Isle development process.
- Prefer XML-only implementations.
- Avoid unnecessary complexity.

Version 0.1 will not introduce:

- New gameplay systems
- Harmony patches
- Custom C#
- New stone resource families
- Large-scale settlement generation

unless future approved research demonstrates they are genuinely necessary.

---

## Approved Feature 1 – Oats

Status

Approved.

Research DoR: Passed.

ADR-0001: Accepted.

Approved design:

- Authentic early medieval Irish crop.
- Medium-cycle grain.
- XML-only implementation.
- Uses RimWorld's existing agriculture systems.
- Processed into milled oats using a conditional hand quern.
- Produces one or two oat-based foods.
- Must never become a superior "hardy crop" that replaces vanilla grains.

Gameplay intent:

Provide a processing grain that rewards additional work without replacing existing vanilla crops.

---

## Approved Feature 2 – Dry-Stone Wall

Status

Approved.

Research RSC-003: Approved.

Approved design:

- One wall variant only.
- XML-only.
- Uses vanilla stone blocks.
- Inspired by early medieval cashel enclosure walls.
- Represents the perimeter of a holding rather than later Irish field-wall networks.
- Player-facing name is "Dry-Stone Wall."
- Documentation may describe the inspiration as "cashel-inspired."
- No gates.
- No wall family.
- No new stone resources.
- No curved walls.
- No procedural ringfort generation.

Approved gameplay niche:

Material-efficient perimeter wall.

It must trade off against vanilla walls through one or more of:

- Lower durability
- Increased construction work
- Reduced structural capability

It must never become a strictly superior replacement for vanilla walls.

---

## Historical Direction

Emerald Isle Version 0.1 is firmly grounded in:

- Early medieval Ireland (approximately AD 400–1100)
- Ordinary farmsteads and holdings
- Domestic life
- Archaeological evidence

The project should avoid romantic reconstruction and nineteenth-century Irish imagery unless explicitly introduced in a future version.

---

## Architectural Philosophy

Version 0.1 represents one small Irish holding rather than Ireland as a whole.

Its visual identity centers on:

- Oats
- Cashel-inspired dry-stone perimeter walls
- Local stone
- Simple vernacular construction

It does not attempt to recreate monumental sites such as Grianán of Aileach or the later extensive dry-stone landscapes of places like The Burren.

---

## Research Status

Complete.

The following research briefs are approved and have passed Research Definition of Ready:

- RSC-002 — Oats
- RSC-003 — Dry-Stone Wall
- RSC-004 — Hand Quern
- RSC-005 — Milled Oats
- RSC-006 — Oat Foods

The Version 0.1 Readiness Review was approved on 2026-07-05. The project is
authorized to create one feature specification at a time in the approved order.
Implementation remains unauthorized until the later acceptance, architecture,
planning, Definition of Ready, and maintainer gates pass.

---

## Scope Control

This document is now the canonical scope for Version 0.1.

Any additions, removals, or significant changes require explicit approval and, where appropriate, a new ADR.
