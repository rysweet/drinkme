# 0128 - RabbitHole PR #293 WhileLoop decode status

## Summary

RabbitHole PR #293 has merged. This entry records what that change adds and what
still needs proof.

This is a status update only. drinkme records links and evidence summaries. It
does not copy RabbitHole, eatme, or Alice source.

## What changed in RabbitHole

- [RabbitHole PR #293](https://github.com/rysweet/RabbitHole/pull/293) merged at
  head `3696670873c6a409046ac6e648e828d95956aa8b`. Decodes Tweedle
  `while (condition) { ... }` to Alice `WhileLoop` in void method bodies.

  **What this proves:** A Tweedle `while` loop in a void method body decodes to
  an Alice `WhileLoop` with a Boolean condition and a `BlockStatement` body.
  Boolean conditions supported: literal, parameter access, relational infix,
  and logical infix/not. Body statements supported: assignment statements only
  (same restriction as `if`/`else` branches), including empty bodies. 6 new
  tests bring the total to 109; all five RabbitHole CI checks passed; focused
  review returned CLEAN.

  **What this does not prove:** Non-Boolean while conditions are rejected with
  `UnsupportedTweedleDecodeException`. Non-assignment statements in while bodies
  (local declaration, nested while, nested if) are rejected. While loops in
  non-void methods are rejected with an explicit error. Method-call expression
  support in conditions or bodies is not added. For-each and count-up loops are
  not supported. Non-this member assignment targets are not supported. Resource
  field initializers are not decoded. Constructor body while loops are not
  decoded. Full player decode and full Tweedle decode remain unproven.

## Done vs. remaining

### Proven in this change

- Tweedle `while (condition) { ... }` in a void method body decodes to Alice
  `WhileLoop` with a Boolean conditional and `BlockStatement` body
  (RabbitHole PR #293).
- Supported Boolean conditions: literal, parameter access, relational infix,
  logical infix/not (RabbitHole PR #293).
- Supported body: assignment-only statements; empty body also accepted
  (RabbitHole PR #293).
- 6 new tests added; 109 total; 0 failures; all five RabbitHole CI checks
  passed; focused review returned CLEAN (RabbitHole PR #293).

### Still not proven

- While loops in non-void methods are not decoded (rejected with explicit
  error).
- Non-Boolean while conditions are not decoded (rejected with explicit error).
- Non-assignment statements in while bodies are not decoded (rejected with
  explicit error).
- Method-call expressions in conditions or bodies are not supported.
- For-each and count-up loops are not supported.
- Non-this member assignment targets are not supported.
- Constructor body while loops are not decoded.
- Resource field initializers are not decoded.
- Full Tweedle decode is not complete.
- Full player decode is not proven.
- Desktop save-menu completion from a rendered menu bar click is not proven.
- Visible rendering is not proven.
- Grading, learner-world grading, and automated creative assessment remain
  unproven.
- Full Alice UI automation remains unproven.
- First-lesson completion remains unproven.

## Default-workflow attempt and process defect

`amplihack recipe run default-workflow --step-timeout 0 -c task_description="Document RabbitHole PR 293" -c repo_path=.`
was run first in this drinkme worktree; it completed (exit code 0) with no
output and no edits to tracked files. Docs changes were made manually through
equivalent disciplined steps.

**Process defect (plain):** The source stream for RabbitHole PR #293 itself
recorded that a prior default-workflow attempt timed out after approximately
two minutes with no output, after which work continued manually. Manual
continuation after a timeout is non-compliant under the no-timeout policy.
The defect is recorded here for traceability; it does not affect the correctness
of the merge or the test results.

## Traceability

- [drinkme status](../../../README.md)
- [root investigation plan](../../plan.md)
- [current modernization plan](../../modernization/current-state-and-next-steps.md)
- [eatme implementation plan](../../eatme/implementation-plan.md)
- Previous entry: [0127 - RabbitHole PR #292 File menu save navigation proof status](0127-rabbithole-pr292-file-menu-save-navigation-proof-status.md)
