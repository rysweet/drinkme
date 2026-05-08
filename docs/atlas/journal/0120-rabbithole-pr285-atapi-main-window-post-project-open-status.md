# 0120 - RabbitHole PR #285 AT-SPI main-window state after Select Project dismissal

## Summary

RabbitHole PR #285 has merged. This entry records what that change adds and
what still needs proof.

This is a status update only. drinkme records links and evidence summaries. It
does not copy RabbitHole, eatme, or Alice source.

## What changed in RabbitHole

- [RabbitHole PR #285](https://github.com/rysweet/RabbitHole/pull/285) merged at
  `8eaa066f98ab173bfa6d0d08f804b5e4eb47a7be`. Proves Alice 3 main-window AT-SPI
  state after Select Project dismissal via `post-project-open-probe.py`. The
  probe requires `projectOpenObserved=true`, waits five seconds, enumerates
  top-level frames, and records blockers.

  **What this proves:** the Alice 3 main window is observable via AT-SPI after
  Select Project dismissal when `projectOpenObserved=true`. Top-level frame
  enumeration and blocker recording are present.

  **What this does not prove:** full scene load, visible rendering, UI
  correctness, grading, or lesson completion are not proven. The probe records
  AT-SPI frame state only; it does not confirm scene objects were rendered or
  that any lesson action succeeded.

## Done vs. remaining

### Proven in this change

- AT-SPI main-window state is observable after Select Project dismissal when
  `projectOpenObserved=true` (RabbitHole PR #285).
- `post-project-open-probe.py` enumerates top-level frames and records blockers.

### Still not proven

- Full scene load is not proven.
- Desktop save-menu completion from a rendered menu bar click is not proven.
- Visible rendering is not proven.
- UI correctness after project open is not proven.
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
- Previous entry: [0119 - RabbitHole PR #284 Save proof ordering fix status](0119-rabbithole-pr284-save-proof-ordering-fix-status.md)
- Next entry: [0121 - eatme PR #134 setup-preflight-ready-to-create scenario status](0121-eatme-pr134-setup-preflight-ready-to-create-status.md)
