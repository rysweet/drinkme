# 0091 - RabbitHole PR #168/#169 and eatme PR #99 merge status

## Summary

RabbitHole PR #168, RabbitHole PR #169, and eatme PR #99 have merged.
RabbitHole now has a generated archive test for a sibling Tweedle type with an
unresolved parent. RabbitHole also adds machine-readable blocker details to
`desktop-run-pixel-observation.json` when pixel capture is blocked. eatme now
reads `desktop-run-pixel-observation.json` beside the existing readiness
evidence and reports observed screenshot/sample data or blocked component state
and blocker codes.

These changes make the next blocker easier to see. They do not prove full Alice
UI automation, visible rendering, desktop save-menu completion, grading,
creative assessment, or first-lesson completion.

## What changed

- [RabbitHole PR #168](https://github.com/rysweet/RabbitHole/pull/168) merged at
  `da0fb851fd974721a630811873f0d583a853eb5e`. It adds a generated archive test
  proving a sibling Tweedle type with an unresolved parent fails clearly instead
  of returning a partial project that omits the unsupported sibling.
- [RabbitHole PR #169](https://github.com/rysweet/RabbitHole/pull/169) merged at
  `0a0d182c139aeaf5bc7c2c45213a0392cf8f245c`. It adds machine-readable blocker
  details to `desktop-run-pixel-observation.json` while keeping the existing
  blocker codes and no-proof limits.
- [eatme PR #99](https://github.com/rysweet/eatme/pull/99) merged at
  `5e8ba4b8c970d04b410060e90c22a613430e202b`. It reports
  `desktop-run-pixel-observation.json` alongside readiness progress, including
  observed screenshot/sample data or blocked component state and blocker codes.
- This `drinkme` status update records those merge states in the public status
  page and control docs.

## What this proves

- Unresolved-parent sibling Tweedle types now have clear-failure regression
  coverage instead of relying on silent omission.
- A blocked pixel observation now records enough component and environment detail
  to explain why the screenshot/sample path could not prove pixels.
- eatme can show the pixel observation result or blocker in the same first-lesson
  readiness reporting path.
- Older atlas entries remain historical evidence. This entry is the current
  status for these PRs and should not be read as older work still needing a
  merge.

## What remains unproven

- Full Alice UI automation remains unproven.
- Visible rendering remains unproven.
- Desktop save-menu completion remains unproven.
- Grading remains unproven.
- Creative assessment remains unproven.
- First-lesson completion remains unproven.
- PR #168 does not add full Tweedle decode support, including method,
  constructor, complex-value, resource-expression, or missing-parent behavior.
- PR #169 does not prove that pixels were drawn correctly; it records blocker
  details when pixel capture is blocked.
- PR #99 reports existing pixel observation evidence; it does not add new runtime
  proof.

## Follow-up work

- Run the comparison path that produces a non-blocked pixel observation before
  claiming any visible rendering result.
- Keep future status updates separate from older evidence entries so historical
  records stay intact.
