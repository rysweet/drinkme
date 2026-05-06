# 0074 - Edit proof readiness run

This entry records the first executed first-lesson readiness run after
RabbitHole added `tools/eatme-edit-procedure` and eatme learned to consume its
proof.

## Run

- Run id: `edit-proof-20260506075255`
- eatme commit: `f2ef1ad73b736d25e931504039f8108dab5eb84e`
- RabbitHole commit: `897a37693088a8f8be3a8ebce62ce74c57be7570`
- Baseline Alice checkout: `0e2f80df62`
- Command shape:
  `EATME_REAL_ALICE=1 eatme-cli alice run-first-lesson-readiness --execute`

## Result

- Overall readiness report: `passed=true`
- Readiness status: `blocked_until_ui_automation`
- Baseline target: failed at `ui_action_automation_unimplemented`
- RabbitHole target: failed at `ui_action_remaining_steps_unimplemented`

## Action evidence

| Action | Original Alice | RabbitHole |
| --- | --- | --- |
| Find Alice window | passed | passed |
| Focus Alice window | passed | passed |
| Place object | failed: no `tools/eatme-place-object` hook | passed |
| Edit procedure/code block | failed: object placement proof was missing | passed |
| Run world | blocked | blocked |
| Save project | blocked | blocked |

RabbitHole now returns non-empty object-placement evidence and non-empty
procedure-edit evidence for the first-lesson backend path.

## What this proves

- The harness can distinguish original Alice lacking the backend hooks from
  RabbitHole proving object placement and one procedure edit.
- The first-lesson path has advanced from "edit contract named" to "edit proof
  consumed."
- eatme still stops honestly at the next missing actions.

## What this does not prove

- It does not click the Alice gallery or code editor.
- It does not run the world.
- It does not save the project.
- It does not grade work, assess creativity, or complete a teacher/student
  lesson.
- It does not prove broad Alice compatibility beyond this selected path.

## Next boundary

The next useful contract is run-world or project-save proof. It should be as
specific as the object-placement and edit hooks: named inputs, named artifacts,
strict validation, and no success claim until evidence exists.
