# 0110 - RabbitHole PR #272, PR #273, and eatme PR #131 status

## Summary

RabbitHole PR #272, PR #273, and eatme PR #131 have merged. This entry records
what those changes add and what still needs proof.

This is a status update only. drinkme records links and evidence summaries. It
does not copy RabbitHole, eatme, or Alice source.

## What changed in RabbitHole

- [RabbitHole PR #272](https://github.com/rysweet/RabbitHole/pull/272) merged at
  `458bed0f4b409d207a2610b8ccfa8e8dfbbce6c9`. Proves the Select Project Java
  process and Swing widgets can be observed through AT-SPI using `exec:exec`
  and `NO_AT_BRIDGE=1`.

  **What this proves:** the AT-SPI bridge reaches the Alice Java process when
  launched via `exec:exec` with `NO_AT_BRIDGE=1` unset; top-level Swing widgets
  (frame, panel) are visible and enumerable through AT-SPI in this launch mode.

  **What this does not prove:** tab labels are still not visible or enumerable
  through AT-SPI. Project opening is not proven. Full UI widget tree
  accessibility and project selection completion remain unproven.

- [RabbitHole PR #273](https://github.com/rysweet/RabbitHole/pull/273) merged at
  `c86e8c4747b73921e8c432709c8cf7a741848855`. Proves `SaveProjectOperation.fire()`
  reaches a live `JFileChooser`, that a background probe approves it, and that a
  non-empty `.a3p` file is written.

  **What this proves:** `SaveProjectOperation.fire()` reaches a live
  `JFileChooser`; a background probe observes and approves the dialog; a
  non-empty `.a3p` archive is written to the target path.

  **What this does not prove:** visible rendering, grading, full lesson
  completion, the native `java.awt.FileDialog` path, or a full Save menu item
  `doClick`-to-written-file journey in one path.

## What changed in eatme

- [eatme PR #131](https://github.com/rysweet/eatme/pull/131) merged at
  `973b65f`. Adds the `neighborhood-data-story` instructor/student scenario.

  Scenario asset count is now 85 (42 eatme assets + 43 gadugi assets). All
  generated Gadugi adapters are fresh.

## Done vs. remaining

### Proven in this change

- AT-SPI reaches the Alice Java process via `exec:exec` and `NO_AT_BRIDGE=1`;
  top-level Swing widgets are observable (RabbitHole PR #272).
- `SaveProjectOperation.fire()` reaches a live `JFileChooser`; a background
  probe approves it; a non-empty `.a3p` is written (RabbitHole PR #273).
- eatme now includes the `neighborhood-data-story` scenario; scenario assets
  grew from 83 to 85 (eatme PR #131).

### Still not proven

- AT-SPI tab labels are not visible or enumerable.
- Project selection and opening are not proven.
- Full UI widget tree accessibility remains unproven.
- The native `java.awt.FileDialog` path is not proven on Linux.
- A complete Save menu item `doClick`-to-written-file journey in one path is not proven.
- Desktop save-menu completion from a menu-click to a written file remains unproven.
- Visible rendering is not proven.
- Grading, learner-world grading, and automated creative assessment remain
  unproven.
- Full Alice UI automation remains unproven.
- Full StageIDE Save-menu-to-written-project journey remains unproven.
- First-lesson completion remains unproven.
- Full Tweedle/player decode support remains unproven.
- Non-`this` member assignment targets are not supported.
- Non-literal, non-identifier RHS and initializers (binary expressions, method
  calls, etc.) are not decoded.
- Loops, conditional statements, and procedure/method calls in Tweedle bodies
  are not decoded.

### Remaining scenario gaps

The following scenario files are still missing from eatme after eatme PR #131:

- accessibility-rescue-camera-captions
- design-process-story-or-game
- audio-camera-and-export-sharecase
- setup-preflight-ready-to-create

### Active work not yet merged

- RabbitHole PR #274: binary numeric expression decoding — not yet merged; do
  not count as done.

## Default-workflow attempt

`amplihack recipe run default-workflow -c task_description="Update plain Alice
modernization status after RabbitHole PRs 272 and 273 and eatme PR 131" -c
repo_path=/home/azureuser/src/drinkme`
was attempted first; timed out (exit 124) before producing any edits. Log:
`default-workflow-attempt-rh272-rh273-eatme131-20260507230811.log` (empty).
Continued manually through equivalent phases.

## Traceability

- [drinkme status](../../../README.md)
- [root investigation plan](../../plan.md)
- [current modernization plan](../../modernization/current-state-and-next-steps.md)
- [eatme implementation plan](../../eatme/implementation-plan.md)
- Previous entry: [0109 - RabbitHole PR #271 and eatme PR #129 status](0109-rabbithole-pr271-eatme-pr129-status.md)
