# 0085 - Desktop Run execution evidence

## What changed

- [RabbitHole PR #154](https://github.com/rysweet/RabbitHole/pull/154)
  is now the current source of truth for desktop Run evidence. It records a
  narrow Run window attachment signal. It proves Alice put the Run panel into
  the Run window area. It does not prove pixels were drawn, does not prove the
  lesson finished, and is not grading.
- [RabbitHole PR #149](https://github.com/rysweet/RabbitHole/pull/149) adds an
  older opt-in desktop Run listener evidence hook.
- [eatme PR #84](https://github.com/rysweet/eatme/pull/84) consumes that
  older evidence after the previous Run-window check.
- [drinkme PR #35](https://github.com/rysweet/drinkme/pull/35) added the strict
  Done / Partial / Not proven ledger that this entry updates.

## Traceability

This evidence updates the top-level [drinkme status](../../../README.md), the
[root investigation plan](../../plan.md), the
[current modernization plan](../../modernization/current-state-and-next-steps.md),
and the [eatme implementation plan](../../eatme/implementation-plan.md). Those
plans now carry the same RabbitHole-only proof boundary and next work.

## Evidence recorded

The real run `desktop-run-execution-20260506182000` passed its evidence checks,
while overall readiness remained
`readiness_status=blocked_until_ui_automation`.

For RabbitHole, the older run recorded:

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

RabbitHole PR #154 proves only that Alice put the Run panel into the Run window
area.

## What this does not prove

- Ctrl+F5 still does not open the Run window in the current Xvfb run.
- This does not prove original Alice equivalence.
- This does not prove pixels were drawn.
- This does not prove the lesson finished.
- This does not prove desktop save-menu completion.
- This is not grading.

## Next useful work

- Finish review on [RabbitHole PR #155](https://github.com/rysweet/RabbitHole/pull/155)
  after green launcher evidence checks.
- Add coverage for [RabbitHole PR #156](https://github.com/rysweet/RabbitHole/pull/156)
  old archive/image recovery checks.
- Keep [eatme PR #89](https://github.com/rysweet/eatme/pull/89)
  marked review-running after green instructor/student readiness checks.
- Add separate evidence before claiming pixel drawing, lesson completion, or
  grading.
