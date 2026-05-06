# 0077 - Project-save proof hook

This entry records the first bounded project-save proof in the first-lesson
harness.

## Source changes

- RabbitHole PR: [#147](https://github.com/rysweet/RabbitHole/pull/147)
- RabbitHole squash merge commit: `7c9918257e6b99ad01a8d7da73250a98466bf2ce`
- RabbitHole branch head before merge: `dcc0d9f57ebca6a27e2503b0762d6b3fa23d20fc`
- eatme PR: [#76](https://github.com/rysweet/eatme/pull/76)
- eatme squash merge commit: `b10240ad01cc7962c433d2750b62836bcd563d3a`
- eatme branch head before merge: `16109e9a7c005695b2b5360108de92d8a1e6fff6`

## What changed

RabbitHole now exposes `tools/eatme-save-project`. The hook takes the edited
first-lesson project, requires the exact selector
`scene.eatmeFirstLessonStep`, writes `saved-project.a3p`, reads that saved
project back, and writes a save proof artifact.

eatme now consumes that proof after run-world proof passes. It accepts the
save-project action only when the hook returns the expected schema, status,
selector, saved project artifact, and save evidence artifact.

The overall UI contract still stays blocked. That is intentional. Backend save
proof is not desktop menu automation and not full lesson completion.

## Real run evidence

The integrated run `project-save-proof-20260506105110` compared original Alice
with RabbitHole after the save hook was available.

- Original Alice passed window detection and focus, then stopped at object
  placement because the backend proof hook does not exist there.
- RabbitHole passed window detection, focus, object placement, procedure edit,
  bounded run-world proof, and bounded project-save proof.
- The run still reports `blocked_until_ui_automation` because the harness does
  not yet drive the real desktop controls for the complete teacher/student path.

## Why this matters

The selected first-lesson backend path now reaches the end of the current proof
chain: place an object, edit a method, run the method body, and save/read back
the edited project.

That closes one narrow seam. It does not close the modernization project.

## What this proves

- RabbitHole can persist the edited first-lesson project through a bounded
  backend hook.
- eatme can reject weak save evidence and accept only the expected proof shape.
- The first-lesson readiness path can advance through object placement,
  procedure edit, run-world proof, and project-save proof for RabbitHole.

## What this does not prove

- It does not click Alice's desktop save menu.
- It does not click Alice's desktop run button.
- It does not prove visible world rendering.
- It does not grade student work or assess creativity.
- It does not complete a teacher/student lesson.
- It does not prove that original Alice has these backend hooks.

## Next boundary

The next useful boundary is not another backend proof with a new name. The
harness should either replace one backend seam with a real desktop control or
expand the first-lesson comparison into a fuller teacher/student path while
keeping the same evidence discipline.
