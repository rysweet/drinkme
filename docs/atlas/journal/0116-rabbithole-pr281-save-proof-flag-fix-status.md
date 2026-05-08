# 0116 - RabbitHole PR #281 Save proof approval flag ordering fix status

## Summary

RabbitHole PR #281 has merged. This entry records what that change adds and
what still needs proof.

This is a status update only. drinkme records links and evidence summaries. It
does not copy RabbitHole, eatme, or Alice source.

## What changed in RabbitHole

- [RabbitHole PR #281](https://github.com/rysweet/RabbitHole/pull/281) merged at
  `daaceb0a9648d18e890c5b106327d2ddbe489149`. Fixes the Save menu doClick test
  proof bookkeeping: `approvedSelection` is now set before `approveSelection()`
  is called, so the background probe cannot falsely report the result as
  unsupported after the chooser closes and the file write succeeds.

  **What this proves:** the Save menu doClick test now reports the correct
  approved outcome. The proof bookkeeping fix removes a false-negative race
  where evidence could show unsupported even after a successful `.a3p` write.

  **What this does not prove:** this change does not expand the Save proof
  scope beyond what RabbitHole PR #276 established. Real rendered desktop menu
  bar navigation and click are not proven. Desktop save-menu completion from a
  rendered menu bar click is not proven. The native `java.awt.FileDialog` path
  on Linux is not proven. Visible rendering is not proven. Grading, learner-world
  grading, and automated creative assessment remain unproven. Full Alice UI
  automation remains unproven. First-lesson completion remains unproven.

## Done vs. remaining

### Proven in this change

- Save menu doClick test approval flag is set before the probe callback, so
  evidence cannot falsely report unsupported after a successful write
  (RabbitHole PR #281).

### Still not proven

- Real rendered desktop menu bar navigation and click are not proven.
- Desktop save-menu completion from a rendered menu bar click is not proven.
- The native `java.awt.FileDialog` path on Linux is not proven.
- Visible rendering is not proven.
- Grading, learner-world grading, and automated creative assessment remain
  unproven.
- Full Alice UI automation remains unproven.
- First-lesson completion remains unproven.

### Remaining scenario gaps

The following scenario files are still missing from eatme after eatme PR #133:

- audio-camera-and-export-sharecase
- setup-preflight-ready-to-create

## Default-workflow attempt

`amplihack recipe run default-workflow -c task_description="Update plain Alice
modernization status after RabbitHole PR 281 and eatme PR 133"
-c repo_path=/home/azureuser/src/drinkme` was attempted first; timed out
(exit 124) before producing any edits. Continued manually through equivalent
phases.

## Traceability

- [drinkme status](../../../README.md)
- [root investigation plan](../../plan.md)
- [current modernization plan](../../modernization/current-state-and-next-steps.md)
- [eatme implementation plan](../../eatme/implementation-plan.md)
- Previous entry: [0115 - eatme PR #132 accessibility-rescue-camera-captions scenario status](0115-eatme-pr132-accessibility-rescue-camera-captions-status.md)
- Next entry: [0117 - eatme PR #133 design-process-story-or-game scenario status](0117-eatme-pr133-design-process-story-or-game-status.md)
