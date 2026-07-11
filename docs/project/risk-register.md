# Project Risk Register

| ID | Risk | Likelihood | Impact | Response | Trigger | Owner | Status |
|---|---|---|---|---|---|---|---|
| R-001 | Single-maintainer bus factor | H | H | Add backup maintainer and release access before 1.0 | Maintainer unavailable | Founder | Open |
| R-002 | Project/asset licensing ambiguity | L | H | MIT code license and separate creative-asset policy adopted | License scope changes | Founder | Closed |
| R-003 | Unsupported game/DLC assumptions | L | H | RimWorld 1.6 Core and supported-DLC policy adopted | Game/DLC update | Tech lead | Controlled |
| R-004 | Cultural flattening or stereotype | M | H | Source-specific research and qualified review | Sensitive feature proposal | Research lead | Open |
| R-005 | Scope expansion across roadmap | H | H | Milestone gates and smallest coherent slice | Feature imports later scope | Product lead | Controlled |
| R-006 | Save incompatibility from public IDs/state | M | H | Freeze `EI_Plant_Oats` and `EI_RawOats`; validate save/load and removal before release | First persistent feature | Tech lead | Active |
| R-007 | Mod conflicts from broad patches | M | H | Defensive patches and compatibility matrix | First external patch | Tech lead | Deferred |
| R-008 | Performance degradation in large colonies | M | H | Performance budgets and representative profiling | First runtime system | Gameplay lead | Deferred |
| R-009 | AI-generated false claims or scope drift | M | H | Source verification, bounded tasks, human gates | AI-authored change | Maintainer | Controlled |
| R-010 | Documentation becomes contradictory | M | M | Authority order, ownership, milestone audits | Duplicate rule found | Docs lead | Controlled |
| R-011 | Generated Oats art fails vanilla readability or asset acceptance | M | M | Preserve provenance; test all required states beside vanilla crops; require human art acceptance | FS-001 in-game art review | Art owner | Closed 2026-07-07 |

Review at milestone start, monthly during active development, and before release.
Closed risks remain in history with closure evidence.
