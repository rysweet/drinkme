# 0119 - RabbitHole PR #284 Save proof ordering fix status

## Summary

RabbitHole PR #284 has merged. This entry records what that change adds and
what still needs proof.

This is a status update only. drinkme records links and evidence summaries. It
does not copy RabbitHole, eatme, or Alice source.

## What changed in RabbitHole

- [RabbitHole PR #284](https://github.com/rysweet/RabbitHole/pull/284) merged at
  `eca3fb920e3d2b13f5de7117ccc96308378a10f6`. Fixes the `approvedSelection`
  ordering in two older Save proof tests (`StageIdeSaveMenuE2EWriteProofTest`
  and `SaveFileDialogShowControlProofTest`) so all Save proof tests now set the
  proof flag before the approval call. This is proof bookkeeping only.

  **What this proves:** all Save proof tests in the test suite now set the proof
  flag before the approval step. The ordering fix removes a potential race where
  a probe could read an unset flag after the chooser closed.

  **What this does not prove:** this change does not expand the Save proof scope
  beyond what RabbitHole PR #276 established. Real rendered desktop menu bar
  navigation, the native `java.awt.FileDialog` path on Linux, visible rendering,
  grading, and first-lesson completion remain unproven.

## Done vs. remaining

### Proven in this change

- All Save proof tests (`StageIdeSaveMenuE2EWriteProofTest`,
  `SaveFileDialogShowControlProofTest`) set the proof flag before the approval
  call (RabbitHole PR #284).

### Still not proven

- Real rendered desktop menu bar navigation and click are not proven.
- The native `java.awt.FileDialog` path on Linux is not proven.
- Desktop save-menu completion from a rendered menu bar click is not proven.
- Visible rendering is not proven.
- Grading, learner-world grading, and automated creative assessment remain
  unproven.
- Full Alice UI automation remains unproven.
- First-lesson completion remains unproven.

## Default-workflow attempt

`amplihack recipe run default-workflow -c task_description="Update plain Alice
modernization status after RabbitHole PRs 282 284 285 and eatme PR 134"
-c repo_path=/home/azureuser/src/drinkme` was attempted first; timed out
(exit 124) before producing any edits. Continued manually through equivalent
phases.

## Traceability

- [drinkme status](../../../README.md)
- [root investigation plan](../../plan.md)
- [current modernization plan](../../modernization/current-state-and-next-steps.md)
- [eatme implementation plan](../../eatme/implementation-plan.md)
- Previous entry: [0118 - RabbitHole PR #282 relational comparison decode status](0118-rabbithole-pr282-relational-comparison-status.md)
- Next entry: [0120 - RabbitHole PR #285 AT-SPI main-window state after Select Project dismissal](0120-rabbithole-pr285-atapi-main-window-post-project-open-status.md)
