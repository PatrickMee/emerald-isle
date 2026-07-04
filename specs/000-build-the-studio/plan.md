# Implementation Plan: Build the Studio

**Branch:** `main` | **Date:** 2026-07-04 | **Spec:** [spec.md](spec.md)

## Summary

Establish a documentation-first studio operating system around Spec Kit, replacing
generic software defaults with RimWorld-specific, cross-disciplinary quality gates.

## Constitution Check

- Gameplay content excluded: pass
- Milestone scope bounded: pass
- Research and cultural transformation encoded: pass
- Vanilla comparison and tradeoff rules encoded: pass
- XML-first and compatibility rules encoded: pass
- Whole-system verification and release evidence encoded: pass

## Structure Decision

Keep governance in `.specify/memory`, active work in `specs`, reusable working
artifacts in `templates`, and durable handbooks in discipline-oriented `docs`
directories. Document future mod package paths without creating empty gameplay
scaffolding.

## Delivery Slices

1. Governance, vision, roadmap, and repository boundary
2. Design, research, engineering, art, QA, release, and contribution handbooks
3. Workflow, Git/versioning, AI policy, ADR process, and reusable templates
4. Spec Kit template adaptation and validation

## Verification

Scan all files, links, placeholders, source extensions, and requested deliverable
terms. Review authority and cross-document consistency. No runtime test applies
because this milestone intentionally contains no runtime content.
