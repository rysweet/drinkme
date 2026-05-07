# 0098 - RabbitHole PR #214/#215/#216/#218 and eatme PR #120/#121 status

## Summary

RabbitHole PR #214, PR #215, PR #216, and PR #218 have merged. eatme PR #120 and PR #121 have merged. This entry records what those changes prove and what still needs proof.

This is a status update only. drinkme records links and evidence summaries. It does not copy RabbitHole, eatme, or Alice source.

## What changed in RabbitHole

- [RabbitHole PR #214](https://github.com/rysweet/RabbitHole/pull/214) merged at `2155904f38e55323b00d732b7f64e957db4406f5`. It proves launcher drawing surface readiness through `Stage.show()` and `isShowing()`, and it adds a `render-target-unavailable` no-go path. It does not prove visible pixels, deployed installer success, or full world execution.
- [RabbitHole PR #215](https://github.com/rysweet/RabbitHole/pull/215) merged at `c727d97c3d71a0f045925a691a080a42d36fbe9d`. It decodes empty `void` Tweedle methods to AST `UserMethod`. Parameters, method bodies, non-void methods, and constructors still fail clearly.
- [RabbitHole PR #216](https://github.com/rysweet/RabbitHole/pull/216) merged at `c84bdf826723284e84b4872ce2e6c791dee0c8a6`. It adds Save dialog discovery target evidence. Live Save menu click, actual dialog display/control, selected path automation, full lesson completion, rendering, and grading remain unproven.
- [RabbitHole PR #218](https://github.com/rysweet/RabbitHole/pull/218) merged at `a568bae3c3960c60792351cfa423450fea51b067`. It adds launcher render observation proof, but visible pixels remain unobserved. Visible pixels, deployed installer success, and full world execution remain unproven.

## What changed in eatme

- [eatme PR #120](https://github.com/rysweet/eatme/pull/120) merged at `f526544014ee8d368a623359f6bf97cce6588f7d`. It adds the next first-lesson action reporting/proof slice. Real desktop proof is still needed; procedure edit/run/save UI automation is incomplete; the manual real Alice smoke check was skipped.
- [eatme PR #121](https://github.com/rysweet/eatme/pull/121) merged at `4ade2a5d6def4d7ad7be7691b9349a3f5c9ff61e`. It improves real desktop proof reporting/status. Actual real desktop proof/manual Alice smoke, procedure edit/run/save UI automation, project save, and full first-lesson completion remain incomplete.

## What remains unproven

- Full Alice UI automation remains unproven.
- Visible pixels and visible rendering correctness remain unproven.
- Deployed installer success remains unproven.
- Full world execution remains unproven.
- Live desktop Save menu click and desktop save-menu completion remain unproven.
- Actual Save dialog display/control and selected path automation remain unproven.
- Real desktop proof and the manual real Alice smoke check remain incomplete for eatme.
- Procedure edit/run/save UI automation and procedure UI invocation remain incomplete.
- Project save remains incomplete for eatme.
- Grading, learner-world grading, and creative assessment remain unproven.
- First-lesson completion and full first-lesson completion remain unproven.
- Complete player/full Tweedle decode support remains unproven.

## Traceability

- [drinkme status](../../../README.md)
- [root investigation plan](../../plan.md)
- [current modernization plan](../../modernization/current-state-and-next-steps.md)
- [restarted full-scope status](../../modernization/restarted-full-scope-status.md)
- [eatme implementation plan](../../eatme/implementation-plan.md)
