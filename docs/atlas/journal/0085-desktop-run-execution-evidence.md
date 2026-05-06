# 0085 - Desktop Run execution evidence

## What changed

- [RabbitHole PR #154](https://github.com/rysweet/RabbitHole/pull/154)
  merged. It records that Alice put the Run panel into the Run window area. In
  plain terms, this is a narrow Run window attachment signal.
- [RabbitHole PR #155](https://github.com/rysweet/RabbitHole/pull/155)
  merged. It records launcher steps and no-go messages, but does not prove
  rendering.
- [RabbitHole PR #156](https://github.com/rysweet/RabbitHole/pull/156)
  merged. It keeps old image recovery while safely rejecting unsupported old
  code.
- [eatme PR #89](https://github.com/rysweet/eatme/pull/89) merged. It improves
  instructor and student readiness reports, but does not grade work or prove full
  lesson completion.
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
plans now carry the same merged-source status and proof boundary.

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
area. RabbitHole PR #155 records launcher steps and no-go messages, but those
records are not proof that rendering happened.

## What this does not prove

- Ctrl+F5 still does not open the Run window in the current Xvfb run.
- This does not prove original Alice equivalence.
- This does not prove pixels were drawn.
- This does not prove lesson completion. It does not prove the lesson finished.
- This does not prove desktop save-menu completion.
- This is not grading.

## Next useful work

- Use the merged [RabbitHole PR #155](https://github.com/rysweet/RabbitHole/pull/155)
  launcher and no-go records as trace evidence, not rendering proof.
- Use the merged [RabbitHole PR #156](https://github.com/rysweet/RabbitHole/pull/156)
  old image recovery checks as recovery evidence, not a broad compatibility
  claim.
- Use the merged [eatme PR #89](https://github.com/rysweet/eatme/pull/89)
  readiness reports as instructor/student reporting evidence, not grading or
  full lesson completion proof.
- Add separate evidence before claiming pixel drawing, lesson completion, or
  grading.
