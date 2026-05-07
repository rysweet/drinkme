# 0096 - RabbitHole PR #209/#210/#211 source wave status

## Summary

RabbitHole PR #209, PR #210, and PR #211 have merged. This entry records the new source evidence and the work that still is not proven.

This is a RabbitHole source update. drinkme only records the status and links. It does not copy RabbitHole or Alice source.

## What changed in RabbitHole

- [RabbitHole PR #209](https://github.com/rysweet/RabbitHole/pull/209) merged at `02e50a00078e8ff348aa33b8c8635483f9b817bf`. It supports literal sized Tweedle array field initializers such as `new WholeNumber[2]`; non-literal sizes still fail clearly. Broader array expressions, method and constructor bodies, non-literal initializers, non-null resource initializers, complete player decode, and full Tweedle decode remain unproven.
- [RabbitHole PR #210](https://github.com/rysweet/RabbitHole/pull/210) merged at `d2cba4ba3e349c704765129511de5a062210ec08`. It adds a launcher/runtime proof beyond the earlier `Program.main` null-Stage guard. Visible rendering, deployed installer success, and full world execution remain unproven.
- [RabbitHole PR #211](https://github.com/rysweet/RabbitHole/pull/211) merged at `9b509aa3e60e6cf60b5e870a3ee03a0a80363f89`. It adds focused story-api keyboard event characterization tests. The workstream reported `core/story-api` coverage moving from 4.55% to 6.21%, adding 260 covered lines. The 70 percent aggregate coverage target, manual QA gaps, and smoke checks that still need manual approval remain unproven.

## What remains unproven

- Full Alice UI automation remains unproven.
- Visible rendering correctness remains unproven.
- Desktop save-menu completion remains unproven.
- Grading and learner-world grading remain unproven.
- Creative assessment remains unproven.
- First-lesson completion remains unproven.
- Procedure UI invocation remains unproven.
- Deployed installer success remains unproven.
- Full world execution remains unproven.
- Complete player/full Tweedle decode support remains unproven, including broader array expressions, method and constructor bodies, non-literal initializers, and non-null resource initializers.
- The 70 percent aggregate coverage target remains unproven.

## Traceability

- [drinkme status](../../../README.md)
- [root investigation plan](../../plan.md)
- [current modernization plan](../../modernization/current-state-and-next-steps.md)
- [restarted full-scope status](../../modernization/restarted-full-scope-status.md)
- [eatme implementation plan](../../eatme/implementation-plan.md)
