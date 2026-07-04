# Performance Budget

Performance is a feature constraint. Budgets apply to representative late-game
colonies and worst relevant feature scale, not empty developer maps.

## Hard Structural Budgets

- Zero recurring errors or warnings caused by Emerald Isle.
- Zero unbounded whole-map/world scans in normal recurring paths.
- Zero per-tick polling unless an approved plan proves event-driven or lower-rate
  alternatives cannot meet the requirement.
- Every cache has an owner, upper bound, invalidation rule, and save/load behavior.
- Every collection or saved record has a growth bound or cleanup strategy.
- Optional integrations add no recurring work when their target is absent.

## Provisional Runtime Budgets

Until Version 0.1 establishes benchmark hardware and saves:

- A feature should add no more than 2% median simulation-frame time in its typical
  active case and no more than 5% in its documented worst representative case.
- Idle feature systems should allocate no steady-state managed memory per frame
  after warm-up.
- Load-time and memory deltas must be measured and justified against player value;
  numerical release limits are adopted with the Version 0.1 benchmark ADR.

These are investigation triggers, not permission to consume the full budget.

## Measurement

Record game/mod build, hardware, map and pawn scale, speed, DLC/mod list, warm-up,
sample duration, baseline, feature result, profiler/tool, variance, and trace. Test
typical, peak, idle, save, load, and cleanup paths. Optimize only after identifying
the measured hot path, then preserve a regression benchmark when practical.
