# 0109 - RabbitHole PR #271 and eatme PR #129 status

## Summary

RabbitHole PR #271 and eatme PR #129 have merged. This entry records what those
changes add and what still needs proof.

This is a status update only. drinkme records links and evidence summaries. It
does not copy RabbitHole, eatme, or Alice source.

## What changed in RabbitHole

- [RabbitHole PR #271](https://github.com/rysweet/RabbitHole/pull/271) merged at
  `b49b898ddfd2c19a27ce88d265f2c723499b1454`. Continues the Tweedle decoder
  stream after PR #270 (identifier-reference RHS in assignment statements).

  **Identifier-reference initializers in local variable declarations:** previously
  local variable declarations in Tweedle method and constructor bodies only accepted
  primitive literal initial values. This PR extends the local-variable decoder so
  that an `IdentifierReference` initializer resolves to `LocalAccess`,
  `ParameterAccess`, or `FieldAccess` depending on what the identifier name matches
  in scope at the point of the declaration.

  This applies in both method bodies and constructor bodies. The change follows the
  same scoping rules introduced in PR #270 for assignment RHS values.

## What changed in eatme

- [eatme PR #129](https://github.com/rysweet/eatme/pull/129) merged at
  `b72afe499c9b7a3826012b7d10c69b5ae6b6c0a1`. Adds the
  `creature-choreography-loop-lab` instructor/student scenario, a loop-focused
  context where students choreograph creature movements using loops instead of
  repeated individual calls.

  Scenario assets grew from 81 to 83 with all generated Gadugi adapters fresh.

## Done vs. remaining

### Proven in this change

- Local variable declarations in Tweedle method and constructor bodies can now
  decode an `IdentifierReference` initializer to `LocalAccess`, `ParameterAccess`,
  or `FieldAccess` (RabbitHole PR #271).
- eatme now includes the `creature-choreography-loop-lab` scenario; scenario
  assets grew from 81 to 83 (eatme PR #129).

### Still not proven

- Non-`this` member assignment targets are not supported.
- Non-literal, non-identifier RHS and initializers (binary expressions, method
  calls, etc.) are not decoded.
- Loops, conditional statements, and procedure/method calls in Tweedle bodies
  are not decoded.
- Resource initializers in Tweedle fields are not supported.
- Full Tweedle/player decode support remains unproven.
- Grading, learner-world grading, and automated creative assessment remain
  unproven.
- Full Alice UI automation remains unproven.
- Visible rendering correctness remains unproven.
- Desktop save-menu completion remains unproven.
- Full StageIDE Save-menu-to-written-project journey remains unproven.
- Project selection and opening remain unproven.
- First-lesson completion remains unproven.

### Remaining scenario gaps

The following scenario files are still missing from eatme (unchanged from entry 0108,
minus `creature-choreography-loop-lab` which is now done):

- neighborhood-data-story
- accessibility-rescue-camera-captions
- design-process-story-or-game
- audio-camera-and-export-sharecase
- setup-preflight-ready-to-create

### Active work not yet merged

- RabbitHole PR #272: Select Project AT-SPI widget observation fix — not yet
  merged; do not count as done.
- RabbitHole PR #273: SaveProjectOperation-to-JFileChooser-to-written-a3p proof
  — not yet merged; do not count as done.

## Default-workflow attempt

`amplihack recipe run default-workflow -c task_description="Update plain Alice
modernization status after RabbitHole PR 271 and eatme PR 129" -c repo_path=.`
was attempted first; timed out (exit 124) before producing any edits. Log:
`default-workflow-attempt-rh271-eatme129-20260507225059.log` (empty). Continued
manually through equivalent phases.

## Traceability

- [drinkme status](../../../README.md)
- [root investigation plan](../../plan.md)
- [current modernization plan](../../modernization/current-state-and-next-steps.md)
- [restarted full-scope status](../../modernization/restarted-full-scope-status.md)
- [eatme implementation plan](../../eatme/implementation-plan.md)
- Previous entry: [0108 - RabbitHole PR #270 status](0108-rabbithole-pr270-identifier-rhs-status.md)
