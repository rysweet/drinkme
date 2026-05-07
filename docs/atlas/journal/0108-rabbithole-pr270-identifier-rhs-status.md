# 0108 - RabbitHole PR #270 status

## Summary

RabbitHole PR #270 has merged. This entry records what that change adds and what
still needs proof.

This is a status update only. drinkme records links and evidence summaries. It
does not copy RabbitHole, eatme, or Alice source.

## What changed in RabbitHole

- [RabbitHole PR #270](https://github.com/rysweet/RabbitHole/pull/270) merged at
  `b887a14e85a514b5bf7504eeffd3fbeff490e0a2`. Continues the Tweedle decoder
  stream after PR #269 (optional parameter support).

  **Identifier-reference RHS in assignment statements:** previously both method
  and constructor assignment statement decoders only accepted primitive literal
  values on the right-hand side of an assignment. This PR adds a
  `decodeAssignmentRhs` helper that resolves `IdentifierReference` values to
  `ParameterAccess`, `LocalAccess`, or `FieldAccess` depending on what the
  identifier name matches in scope, and throws a clear error for unknown
  identifiers.

  To allow parameter lookup inside constructor assignment bodies,
  `UserParameter[]` is now passed through `decodeConstructor` →
  `decodeConstructorBody` → `decodeConstructorAssignmentStatement`. The method
  path already had `allParameters` available but was not forwarding it to
  `decodeMethodAssignmentStatement`; that gap is also closed.

  Primitive literal RHS continues to work exactly as before.

  **Test count:** 58 → 62 decoder tests (84 total in the `ast` module). Four new
  positive tests cover parameter-as-RHS in method assignment, local-as-RHS in
  method assignment, parameter-as-RHS in constructor assignment, and
  parameter-as-RHS in constructor `this`-field assignment. Two existing
  error-message assertions were updated to match the new wording.

## Done vs. remaining

### Proven in this change

- Assignment statements in Tweedle method and constructor bodies can now decode
  an `IdentifierReference` RHS to `ParameterAccess`, `LocalAccess`, or
  `FieldAccess` (RabbitHole PR #270).
- Constructor assignment bodies now receive `UserParameter[]`, so constructor
  setter patterns can resolve parameter RHS (RabbitHole PR #270).
- Four positive decoder tests and two updated error-message tests pass
  (RabbitHole PR #270).

### Still not proven

- Non-`this` member assignment targets are not supported.
- Non-literal, non-identifier RHS (binary expressions, method calls, etc.) are
  not supported in assignment statements.
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
- Default values for optional Tweedle parameters are not represented (Alice AST
  has no optional-parameter concept; `TweedleOptionalParameter` has no default
  accessor).

### Remaining scenario gaps (unchanged from entry 0107)

- creature-choreography-loop-lab
- neighborhood-data-story
- accessibility-rescue-camera-captions
- design-process-story-or-game
- audio-camera-and-export-sharecase
- setup-preflight-ready-to-create

## Default-workflow attempt

`amplihack recipe run default-workflow -c task_description="Update plain Alice
modernization status after RabbitHole PR 270" -c repo_path=.`
was attempted first; timed out (exit 124) before producing any edits. Log:
`default-workflow-attempt-rh270-20260507223551.log` (empty). Continued manually
through equivalent phases.

## Traceability

- [drinkme status](../../../README.md)
- [root investigation plan](../../plan.md)
- [current modernization plan](../../modernization/current-state-and-next-steps.md)
- [restarted full-scope status](../../modernization/restarted-full-scope-status.md)
- [eatme implementation plan](../../eatme/implementation-plan.md)
- Previous entry: [0107 - eatme PR #127 mars-rover-proximity-mission](0107-eatme-pr127-mars-rover-proximity-mission-status.md)
