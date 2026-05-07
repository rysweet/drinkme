# 0095 - RabbitHole PR #207/#208 source evidence update

## Summary

RabbitHole PR #207 and PR #208 have merged. This update records what those two source changes prove and what they do not prove.

At the start of this drinkme update, GitHub showed no open pull requests in RabbitHole, eatme, or drinkme. Other work may open new pull requests later.

## What changed in RabbitHole

- [RabbitHole PR #207](https://github.com/rysweet/RabbitHole/pull/207) merged at `6d744747a831824378c053713fef4e8a136c25c5`. It adds Numeric and Boolean Tweedle field initializer decoding for `null`, producing AST `NullLiteral`. It still rejects primitive statement contexts such as `if(null)` and `while(null)`. This is more null-field support, not full Tweedle or player decode support.
- [RabbitHole PR #208](https://github.com/rysweet/RabbitHole/pull/208) merged at `8799854787655ca61b6fad9378377b19d41aa7b1`. Its head before merge was `153f4e4ce77415d42e6f1047abcc2074671ae4c8`, and all GitHub checks passed before merge. It records Save operation completion evidence. That is not proof that the full desktop Save-menu path is complete.

## What remains unproven

- Full Alice UI automation remains unproven.
- Visible rendering correctness remains unproven.
- Desktop save-menu completion remains unproven.
- Grading and learner-world grading remain unproven.
- Creative assessment remains unproven.
- First-lesson completion remains unproven.
- Procedure UI invocation remains unproven.
- Full Tweedle/player decode support remains unproven, including method body decode, constructor body decode, and complete player decode.

## Traceability

- [drinkme status](../../../README.md)
- [root investigation plan](../../plan.md)
- [current modernization plan](../../modernization/current-state-and-next-steps.md)
- [eatme implementation plan](../../eatme/implementation-plan.md)
