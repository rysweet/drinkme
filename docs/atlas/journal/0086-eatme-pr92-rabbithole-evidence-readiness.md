# 0086 - eatme PR #92 RabbitHole evidence readiness

## What changed

- [RabbitHole PR #154](https://github.com/rysweet/RabbitHole/pull/154)
  merged. It records that Alice put the Run panel into the Run window area.
- [RabbitHole PR #155](https://github.com/rysweet/RabbitHole/pull/155)
  merged. It records launcher steps and no-go messages, but does not prove
  rendering.
- [RabbitHole PR #156](https://github.com/rysweet/RabbitHole/pull/156)
  merged. It keeps old image recovery while safely rejecting unsupported old
  code.
- [eatme PR #89](https://github.com/rysweet/eatme/pull/89) merged. It improves
  instructor and student readiness reports, but does not grade work or prove full
  lesson completion.
- [eatme PR #92](https://github.com/rysweet/eatme/pull/92) merged at
  `cfe1f9e364d0015a3f97e237a9de5af670ae3bd6`.
- eatme now documents the RabbitHole evidence needed before first-lesson
  readiness can be marked ready.
- This drinkme entry records the status meaning. It does not add RabbitHole
  runtime artifacts or raw eatme run output.

## Traceability

This status update is reflected in the top-level [drinkme status](../../../README.md),
[root investigation plan](../../plan.md), the
[current modernization plan](../../modernization/current-state-and-next-steps.md),
the [restarted full-scope status](../../modernization/restarted-full-scope-status.md),
and the [eatme implementation plan](../../eatme/implementation-plan.md).

## Required RabbitHole evidence

Before first-lesson readiness can be marked ready, eatme expects RabbitHole
evidence covering:

1. launch evidence;
2. Run-window evidence;
3. desktop execution evidence;
4. screenshot/log/window artifacts;
5. `ui-action-contract.json`.

## What this means

The PR #92 merge means eatme has documented the evidence RabbitHole must provide
before first-lesson readiness can be marked ready. It does not mean drinkme or
eatme contains that runtime proof.

## What this does not prove

- This does not prove full Alice UI automation.
- This does not prove creative assessment.
- This does not prove learner-world grading.
- This does not prove visible rendering correctness.
- This does not prove first-lesson completion.

The older desktop Run status remains a narrow Run window attachment signal:
RabbitHole PR #154 records only that Alice put the Run panel into the Run window
area. It does not prove pixels were drawn, does not prove the lesson finished,
does not prove desktop save-menu completion, and is not grading.

## Next useful work

- Use eatme PR #92 as documentation of required RabbitHole evidence, not as
  runtime proof.
- Add separate proof before claiming pixel drawing, lesson completion, desktop
  save-menu completion, or grading.
