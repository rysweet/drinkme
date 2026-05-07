# 0114 - RabbitHole PR #278 Select Project AT-SPI proof status

## Summary

RabbitHole PR #278 has merged. This entry records what that change adds and
what still needs proof.

This is a status update only. drinkme records links and evidence summaries. It
does not copy RabbitHole, eatme, or Alice source.

## What changed in RabbitHole

- [RabbitHole PR #278](https://github.com/rysweet/RabbitHole/pull/278) merged at
  `e130dac3a6f6431895f72f71733a042f1bb92cb3`. Select Project dialog tab labels
  are accessible as AT-SPI toggle buttons at depth 11 in the accessibility tree.
  All five tabs can be clicked programmatically. Clicking Starters, then Africa
  Full, then OK causes `projectOpenObserved: true` and the Select Project frame
  disappears.

  **What this proves:** Select Project tab labels are accessible as AT-SPI
  toggle buttons at depth 11. All five tabs can be clicked. The Starters ->
  Africa Full -> OK path causes `projectOpenObserved: true` and the Select
  Project frame closes.

  **What this does not prove:** real rendered desktop menu bar navigation and
  click are not proven. Desktop save-menu completion from a rendered menu bar
  click is not proven. The native `java.awt.FileDialog` path on Linux is not
  proven. Visible rendering is not proven. Grading, learner-world grading, and
  automated creative assessment remain unproven. Full Alice UI automation remains
  unproven. First-lesson completion remains unproven.

## Done vs. remaining

### Proven in this change

- Select Project tab labels are accessible as AT-SPI toggle buttons at depth 11
  (RabbitHole PR #278).
- All five Select Project tabs can be clicked programmatically via AT-SPI
  (RabbitHole PR #278).
- The Starters -> Africa Full -> OK path causes `projectOpenObserved: true`
  (RabbitHole PR #278).
- The Select Project frame disappears after OK is clicked on the Africa Full
  selection (RabbitHole PR #278).

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

The following scenario files are still missing from eatme after eatme PR #132:

- design-process-story-or-game
- audio-camera-and-export-sharecase
- setup-preflight-ready-to-create

## Default-workflow attempt

`amplihack recipe run default-workflow -c task_description="Update plain Alice
modernization status after RabbitHole PRs 276 277 278 and eatme PR 132"
-c repo_path=/home/azureuser/src/drinkme` was attempted first; timed out
(exit 124) before producing any edits. Continued manually through equivalent
phases.

## Traceability

- [drinkme status](../../../README.md)
- [root investigation plan](../../plan.md)
- [current modernization plan](../../modernization/current-state-and-next-steps.md)
- [eatme implementation plan](../../eatme/implementation-plan.md)
- Previous entry: [0113 - RabbitHole PR #277 Tweedle string concatenation decode status](0113-rabbithole-pr277-tweedle-string-concat-status.md)
- Next entry: [0115 - eatme PR #132 accessibility-rescue-camera-captions scenario status](0115-eatme-pr132-accessibility-rescue-camera-captions-status.md)
