# 0127 - RabbitHole PR #292 File menu save navigation proof status

## Summary

RabbitHole PR #292 has merged. This entry records what that change adds and what
still needs proof.

This is a status update only. drinkme records links and evidence summaries. It
does not copy RabbitHole, eatme, or Alice source.

## What changed in RabbitHole

- [RabbitHole PR #292](https://github.com/rysweet/RabbitHole/pull/292) merged at
  `17e82091232131de7f1b2169638a2ea1a48fedfd`. Adds
  `FileMenuSaveNavigationProofTest`.

  **What this proves:** The test starts `StageIDE` on the event dispatch thread,
  finds `FileMenuModel` inside the real `AliceMenuBar` by walking
  `getCodePerspective().getMenuBarComposite().getChildren()`, calls
  `fileMenuModel.createMenu()` to build the actual `JMenu` from the live model,
  locates the `JMenuItem` whose `Action` instance is the same object as
  `SaveProjectOperation.getInstance().getImp().getSwingModel().getAction()`, then
  calls `doClick()` and checks that the written evidence shows
  `status=menu_item_dispatched`, `menu_item_dispatch=true`, and
  `trigger_class=ActionEventTrigger`. This closes the navigation gap between the
  two existing narrower proofs: one that showed `FileMenuModel` is in
  `AliceMenuBar`, and one that dispatched through a programmatically-created menu
  item built outside the real menu path.

  **What this does not prove:** The user physically navigating the rendered menu
  bar — clicking the on-screen File label to open the dropdown and then clicking
  Save — is not proven. That requires real AWT robot input or a person at the
  screen. Desktop save-menu completion from a real rendered click path is not
  proven. Full live `FileDialog` interaction with a confirmed file write at the
  end of one rendered path is not proven. Visible rendering correctness is not
  proven. Grading, automated creative assessment, and full first-lesson completion
  remain unproven.

## Done vs. remaining

### Proven in this change

- `StageIDE` starts and `AliceMenuBar` is reachable from the live IDE instance
  (RabbitHole PR #292).
- `FileMenuModel.createMenu()` builds a `JMenu` containing a `JMenuItem` backed
  by the same `Action` instance as `SaveProjectOperation` (RabbitHole PR #292).
- `doClick()` on that `JMenuItem` dispatches into the save action and writes
  evidence with `status=menu_item_dispatched`, `menu_item_dispatch=true`, and
  `trigger_class=ActionEventTrigger` (RabbitHole PR #292).
- All five RabbitHole CI checks passed; focused review returned CLEAN.

### Still not proven

- The user physically clicking the on-screen File menu label to open the dropdown
  is not proven.
- Selecting Save from that visible dropdown by mouse or keyboard is not proven.
- Desktop save-menu completion from a real rendered click path is not proven.
- Full live `FileDialog` interaction with a confirmed file write completing in one
  rendered path is not proven.
- Visible rendering correctness is not proven.
- Grading, learner-world grading, and automated creative assessment remain
  unproven.
- Full Alice UI automation remains unproven.
- First-lesson completion remains unproven.

## Default-workflow attempt

`amplihack recipe run default-workflow -c task_description="Update plain Alice
modernization status after RabbitHole PR 292 FileMenuSaveNavigationProofTest"
-c repo_path=/home/azureuser/src/drinkme-worktrees/feat/status-rh292-20260508013031`
was attempted first; timed out (exit 124) before producing any edits. Continued
manually through equivalent phases.

## Traceability

- [drinkme status](../../../README.md)
- [root investigation plan](../../plan.md)
- [current modernization plan](../../modernization/current-state-and-next-steps.md)
- [eatme implementation plan](../../eatme/implementation-plan.md)
- Previous entry: [0126 - RabbitHole PR #291 conditional statement decode status](0126-rabbithole-pr291-conditional-statement-decode-status.md)
