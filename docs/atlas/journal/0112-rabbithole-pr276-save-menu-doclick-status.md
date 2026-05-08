# 0112 - RabbitHole PR #276 Save menu item doClick proof status

## Summary

RabbitHole PR #276 has merged. This entry records what that change adds and
what still needs proof.

This is a status update only. drinkme records links and evidence summaries. It
does not copy RabbitHole, eatme, or Alice source.

## What changed in RabbitHole

- [RabbitHole PR #276](https://github.com/rysweet/RabbitHole/pull/276) merged at
  `66b38f87090f633f44a403737778c3c01a01c52b`. A programmatically-created real
  Save menu item has `doClick()` called on it, which dispatches through Croquet,
  reaches a live `JFileChooser`, the dialog is approved by a background probe,
  and a non-empty `.a3p` file is written to disk.

  **What this proves:** Save menu item `doClick()` on a programmatically-created
  real Save menu item, through Croquet dispatch, to a live `JFileChooser`
  approval, produces a non-empty `.a3p` file on disk.

  **What this does not prove:** real rendered desktop menu bar navigation and
  click are not proven. Desktop save-menu completion from a rendered menu bar
  click is not proven. The native `java.awt.FileDialog` path on Linux is not
  proven. Visible rendering is not proven. Grading, learner-world grading, and
  automated creative assessment remain unproven. Full Alice UI automation remains
  unproven. First-lesson completion remains unproven.

  **Active follow-up:** RabbitHole PR #281 merged at
  `daaceb0a9648d18e890c5b106327d2ddbe489149` and fixed the proof-flag ordering;
  see journal entry 0116.

## Done vs. remaining

### Proven in this change

- Save menu item `doClick()` on a programmatically-created real Save menu item
  dispatches through Croquet and reaches a live `JFileChooser` (RabbitHole PR
  #276).
- The `JFileChooser` is approved by a background probe and a non-empty `.a3p`
  file is written to disk (RabbitHole PR #276).

### Still not proven

- Real rendered desktop menu bar navigation and click are not proven.
- Desktop save-menu completion from a rendered menu bar click is not proven.
- The native `java.awt.FileDialog` path on Linux is not proven.
- Visible rendering is not proven.
- Grading, learner-world grading, and automated creative assessment remain
  unproven.
- Full Alice UI automation remains unproven.
- First-lesson completion remains unproven.
- AT-SPI Select Project tab navigation to a real project open remains a separate
  concern; it was addressed independently in RabbitHole PR #278.
- RabbitHole PR #281 (proof-flag ordering fix) merged at
  `daaceb0a9648d18e890c5b106327d2ddbe489149`; see journal entry 0116.

### Remaining scenario gaps

The following scenario files are still missing from eatme after eatme PR #132:

- design-process-story-or-game
- audio-camera-and-export-sharecase
- setup-preflight-ready-to-create

## Default-workflow attempt

`amplihack recipe run default-workflow -c task_description="Update plain Alice
modernization status after RabbitHole PRs 276 277 278 and eatme PR 132"
-c repo_path=/home/azureuser/src/drinkme` was attempted first; timed out
(exit 124) before producing any edits. Log:
`default-workflow-attempt-rh276-rh277-rh278-eatme132-20260507234028.log`
(empty). Continued manually through equivalent phases.

## Traceability

- [drinkme status](../../../README.md)
- [root investigation plan](../../plan.md)
- [current modernization plan](../../modernization/current-state-and-next-steps.md)
- [eatme implementation plan](../../eatme/implementation-plan.md)
- Previous entry: [0111 - RabbitHole PR #274 arithmetic binary expression status](0111-rabbithole-pr274-arithmetic-binary-status.md)
- Next entry: [0113 - RabbitHole PR #277 Tweedle string concatenation decode status](0113-rabbithole-pr277-tweedle-string-concat-status.md)
