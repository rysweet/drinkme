# 0094 - RabbitHole source and CI status wave

## Summary

RabbitHole PRs #185, #187, #188, #190, and #191 have merged. This wave added more real source tests and fixed a CI problem that had delayed several PRs.

This is useful progress, but it is not a finished Alice modernization. It does not prove full Alice UI automation, visible rendering correctness, desktop save-menu completion, grading, creative assessment, learner-world grading, first-lesson completion, a deployed sharing platform, procedure UI invocation, or full Tweedle decode support.

## What changed in RabbitHole

- [RabbitHole PR #185](https://github.com/rysweet/RabbitHole/pull/185) merged at `713758374d0b6e937ec3f1471a78d7c95f69a35a`. It adds real characterization tests for model resource array grouping, skip behavior, and duplicate index rejection. The 70 percent aggregate coverage target is still unproven, and the oversized-file count remains high: 51 or 52 files over 500 lines depending on the measurement point.
- [RabbitHole PR #187](https://github.com/rysweet/RabbitHole/pull/187) merged at `7bc8f2991ddc45708203682bd5edeb7a2d990c40`. It is a narrow Tweedle null slice: `TextString label <- null` now parses and decodes to `NullLiteral`, while `WholeNumber <- null` still fails. Review caught over-broad primitive null support, and that was fixed before merge. Broader null support, method and constructor body decode, complete player decode, and full Tweedle decode support remain unproven.
- [RabbitHole PR #188](https://github.com/rysweet/RabbitHole/pull/188) merged at `39085aaed5cb042ad5260adfcc6d4c4e1dcda9d7`. It adds `ProcedureTabSelection`, tests, and a reference doc with next steps and limits. This is a UI automation design and test boundary, not live procedure invocation. Live procedure invocation, desktop edit command, Save-menu completion, dialogs, first-lesson completion, grading, and rendering remain unproven.
- [RabbitHole PR #190](https://github.com/rysweet/RabbitHole/pull/190) merged at `fd71bfb96fe9c82aa4cdd3de8f967f7c410af629`. It adds `IssueReportWorker` non-retryable failure tests. It was delayed by transient `jogamp.org` network failures until CI was rerun. The 70 percent aggregate coverage target is still not claimable; a fresh hotspot count reported by an agent found 52 Java files over 500 lines.
- [RabbitHole PR #191](https://github.com/rysweet/RabbitHole/pull/191) merged at `aac8fa55b96c32cd797c98c016c0ae4e598ffc3a`. It restores the Maven cache fallback in CI. That fixed the stuck coverage path; post-merge coverage run `25492250204` completed successfully, and develop checks after PR #190 all completed successfully at `fd71bfb96fe9c82aa4cdd3de8f967f7c410af629`.

## Operational issue recorded plainly

PR #187, PR #188, and PR #190 were delayed by stuck coverage behavior and network dependency failures. PR #191 fixed the Maven cache fallback path that was part of the stuck coverage problem. The network failures were transient, but they still slowed the work and should stay visible in status notes.

## What remains unproven

- Full Alice UI automation remains unproven.
- Visible rendering correctness remains unproven.
- Desktop save-menu completion remains unproven.
- Procedure UI invocation and the desktop edit command remain unproven.
- Dialog handling remains unproven.
- Grading and learner-world grading remain unproven.
- Creative assessment remains unproven.
- First-lesson completion remains unproven.
- A deployed sharing platform remains unproven.
- Full Tweedle decode support remains unproven, including broader null support, method and constructor body decode, and complete player decode.
- The 70 percent aggregate coverage target remains unproven.
- The oversized Java-file count remains high: 52 files over 500 lines in the latest reported count, with 51 or 52 remaining depending on the earlier measurement point.

## Traceability

- [drinkme status](../../../README.md)
- [root investigation plan](../../plan.md)
- [current modernization plan](../../modernization/current-state-and-next-steps.md)
- [eatme implementation plan](../../eatme/implementation-plan.md)
