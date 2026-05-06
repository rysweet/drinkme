# 0085 - Desktop Run execution evidence

## What changed

- [RabbitHole PR #149](https://github.com/rysweet/RabbitHole/pull/149) adds an
  opt-in desktop Run VM listener evidence hook.
- [eatme PR #84](https://github.com/rysweet/eatme/pull/84) consumes that
  evidence after the geometry-checked toolbar Run-frame proof.
- [drinkme PR #35](https://github.com/rysweet/drinkme/pull/35) added the strict
  Done / Partial / Not proven ledger that this entry updates.

## Traceability

This evidence updates the top-level [drinkme status](../../../README.md), the
[root investigation plan](../../plan.md), the
[current modernization plan](../../modernization/current-state-and-next-steps.md),
and the [eatme implementation plan](../../eatme/implementation-plan.md). Those
plans now carry the same RabbitHole-only proof boundary and next feature seams.

## Evidence recorded

The real run `desktop-run-execution-20260506182000` passed its evidence checks,
while overall readiness remained
`readiness_status=blocked_until_ui_automation`.

For RabbitHole, the run recorded:

- toolbar Run dispatch passed;
- Run-frame observation passed through `run-window-created.json`;
- desktop Run execution observation passed through `desktop-run-execution.json`;
- `desktop-run-execution.json` used schema
  `eatme.alice-desktop-run-execution/v1`;
- status was `statement_execution_observed`;
- `active_scene_invoke_started` was `true`;
- `executing_statement_count` was `260`;
- `desktop-run-runtime.log`, `run-window-created.json`,
  `ui-action-contract.json`, and the Run-frame screenshot were non-empty.

Original Alice remains uninstrumented for this proof path, so the run does not
establish original Alice equivalence for object placement or the Run-frame path.

## What this proves

RabbitHole can now prove that the desktop Run path reached VM statement
execution after the toolbar Run-frame proof.

## What this does not prove

- Ctrl+F5 still does not open the Run window in the current Xvfb run.
- This does not prove original Alice equivalence.
- This does not prove visible rendering correctness.
- This does not prove world completion.
- This does not prove desktop save-menu completion.
- This does not prove grading, creative assessment, or full lesson automation.

## Next useful work

- Replace the coordinate-based toolbar click with a stable UI or accessibility
  affordance.
- Add visible rendering evidence after VM statement execution before claiming
  world playback.
- Add desktop save-menu completion evidence before counting the save step as
  fully done.
- Define the acceptable proof strategy for original Alice where RabbitHole-only
  hooks cannot exist.
