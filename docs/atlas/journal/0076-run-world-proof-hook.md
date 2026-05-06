# 0076 - Run-world proof hook

This entry records the first bounded proof that the first-lesson harness can
move past "run-world is missing" when RabbitHole provides a stable backend hook.

## Source changes

- RabbitHole PR: [#146](https://github.com/rysweet/RabbitHole/pull/146)
- RabbitHole squash merge commit: `c041e44099051e1ebd975882e255a55789387d52`
- RabbitHole branch head before merge: `b3feb24dd696db683c809df9373b659777d9e639`
- eatme PR: [#75](https://github.com/rysweet/eatme/pull/75)
- eatme squash merge commit: `ad5a9aa6987f8e857eae46f0a6a7cce0335a2a4c`
- eatme branch head before merge: `a02629e0170ad21bfc371181eb60a4c5bd4cbb31`

## What changed

RabbitHole now exposes `tools/eatme-run-world`. The hook takes the edited
first-lesson project, requires the exact selector
`scene.eatmeFirstLessonStep`, runs that scene method body through Alice's
headless virtual-machine path, and writes proof artifacts.

eatme now consumes that proof after procedure-edit proof passes. It accepts the
run-world action only when the hook returns the expected schema, status,
selector, and non-empty run/runtime evidence. Project save remains blocked.

## Real run evidence

The integrated run `run-world-proof-20260506091921` compared original Alice
with RabbitHole after the hook was available.

- Original Alice passed window detection and focus, then stopped at object
  placement because the backend proof hook does not exist there.
- RabbitHole passed window detection, focus, object placement, procedure edit,
  and bounded run-world proof.
- RabbitHole then stopped at project save, which is still intentionally
  unimplemented in the harness.

## Why this matters

This is the first evidence that the selected first-lesson path can run a changed
world method after object placement and code edit proof. The harness now reports
a later, more precise stop point: save is missing.

That is progress. It is not a victory lap.

## What this proves

- RabbitHole can run the fixed first-lesson scene method body through a bounded
  backend hook.
- eatme can reject weak run-world evidence and accept only the expected proof
  shape.
- The first-lesson readiness path can advance through object placement,
  procedure edit, and run-world proof for RabbitHole.

## What this does not prove

- It does not click Alice's desktop run button.
- It does not prove visible world rendering.
- It does not save the project.
- It does not grade student work or assess creativity.
- It does not complete a teacher/student lesson.
- It does not prove that original Alice has these backend hooks.

## Next boundary

RabbitHole and eatme should define or implement the next deterministic
project-save proof. Until then, save remains the honest stop point.
