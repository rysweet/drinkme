# 0111 - RabbitHole PR #274 arithmetic binary expression status

## Summary

RabbitHole PR #274 has merged. This entry records what that change adds and
what still needs proof.

This is a status update only. drinkme records links and evidence summaries. It
does not copy RabbitHole, eatme, or Alice source.

## What changed in RabbitHole

- [RabbitHole PR #274](https://github.com/rysweet/RabbitHole/pull/274) merged at
  `5571894e5152482c9fb26ba31fc3d633d372e88e`. Tweedle assignment right-hand-side
  values and local variable initializer values that are arithmetic binary
  expressions (`+`, `-`, `*`, `/`) now decode to AST binary nodes.

  **What this proves:** arithmetic binary expressions (`+`, `-`, `*`, `/`) are
  decoded as Tweedle assignment right-hand-side values and as local variable
  initializer values.

  **What this does not prove:** string concatenation expressions are not decoded.
  Logical and comparison expressions are not decoded. Method call expressions
  are not decoded. Non-`this` member assignment targets are not supported.
  Loops, conditional statements, and procedure/method calls in Tweedle bodies
  are not decoded. Resource field initializers are not decoded. Full
  player/Tweedle decode is not proven.

## Done vs. remaining

### Proven in this change

- Arithmetic binary expressions (`+`, `-`, `*`, `/`) decode as Tweedle
  assignment right-hand-side values (RabbitHole PR #274).
- Arithmetic binary expressions (`+`, `-`, `*`, `/`) decode as Tweedle local
  variable initializer values (RabbitHole PR #274).

### Still not proven

- String concatenation expressions are not decoded.
- Logical and comparison expressions are not decoded.
- Method call expressions are not decoded.
- Non-`this` member assignment targets are not supported.
- Loops, conditional statements, and procedure/method calls in Tweedle bodies
  are not decoded.
- Resource field initializers are not decoded.
- Full Tweedle/player decode support is not proven.
- AT-SPI tab labels are not visible or enumerable.
- Project selection and opening are not proven.
- Full UI widget tree accessibility remains unproven.
- The native `java.awt.FileDialog` path is not proven on Linux.
- A complete Save menu item `doClick`-to-written-file journey in one path is
  not proven.
- Desktop save-menu completion from a menu-click to a written file remains
  unproven.
- Visible rendering is not proven.
- Grading, learner-world grading, and automated creative assessment remain
  unproven.
- Full Alice UI automation remains unproven.
- First-lesson completion remains unproven.

### Remaining scenario gaps

The following scenario files are still missing from eatme after eatme PR #131:

- accessibility-rescue-camera-captions
- design-process-story-or-game
- audio-camera-and-export-sharecase
- setup-preflight-ready-to-create

### Active work not yet merged

- RabbitHole PR #276: Save menu item doClick — not yet merged; do not count
  as done.
- eatme PR #132: accessibility scenario — not yet merged; do not count as done.
- Select Project follow-up — not yet merged; do not count as done.
- Next Tweedle decoder after PR #274 — not yet merged; do not count as done.

## Default-workflow attempt

`amplihack recipe run default-workflow -c task_description="Update plain Alice
modernization status after RabbitHole PR 274" -c repo_path=/home/azureuser/src/drinkme`
was attempted first; timed out (exit 124) before producing any edits. Log:
`default-workflow-attempt-rh274-20260507232036.log` (empty).
Continued manually through equivalent phases.

## Traceability

- [drinkme status](../../../README.md)
- [root investigation plan](../../plan.md)
- [current modernization plan](../../modernization/current-state-and-next-steps.md)
- [eatme implementation plan](../../eatme/implementation-plan.md)
- Previous entry: [0110 - RabbitHole PR #272, PR #273, and eatme PR #131 status](0110-rabbithole-pr272-pr273-eatme-pr131-status.md)
