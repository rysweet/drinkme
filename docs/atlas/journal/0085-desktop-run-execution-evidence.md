# 0085 - Desktop Run execution evidence

## What changed

- [RabbitHole PR #149](https://github.com/rysweet/RabbitHole/pull/149) adds an
  opt-in desktop Run VM listener evidence hook.
- [eatme PR #84](https://github.com/rysweet/eatme/pull/84) consumes that
  evidence after the geometry-checked toolbar Run-frame proof.
- [drinkme PR #35](https://github.com/rysweet/drinkme/pull/35) added the strict
  Done / Partial / Not proven ledger that this entry updates.

## Evidence recorded

The real run `desktop-run-execution-20260506182000` passed with
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

For original Alice, the same run still did not prove object placement or the
Run-frame path because original Alice does not expose the RabbitHole proof
hooks.

## What this proves

RabbitHole can now prove that the desktop Run path reached VM statement
execution after the toolbar Run-frame proof.

## What this does not prove

- Ctrl+F5 still does not open the Run window in the current Xvfb run.
- This does not prove visible rendering correctness.
- This does not prove world completion.
- This does not prove desktop save-menu completion.
- This does not prove grading, creative assessment, or full teacher/student
  lesson completion.

## Next useful work

- Replace the coordinate-based toolbar click with a stronger UI affordance or
  accessibility path.
- Add visible rendering evidence before claiming world playback.
- Add desktop save-menu completion evidence before counting the save step as
  fully done.
