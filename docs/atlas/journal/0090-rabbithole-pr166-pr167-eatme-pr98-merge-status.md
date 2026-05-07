# 0090 - RabbitHole PR #166/#167 and eatme PR #98 merge status

## Summary

RabbitHole PR #166, RabbitHole PR #167, and eatme PR #98 have merged.
RabbitHole now has a generated archive test for a sibling Tweedle type with an
unsupported complex field initializer. RabbitHole also writes
`desktop-run-pixel-observation.json` so a desktop run can record a screenshot and
center pixel when possible, or a clear blocker code when the current desktop
state cannot support that observation. eatme now shows first-lesson readiness
progress in plain text output, including each required evidence item and its
state.

These changes make the evidence easier to inspect. They do not prove full Alice
UI automation, visible rendering, desktop save-menu completion, grading,
creative assessment, or first-lesson completion.

## What changed

- [RabbitHole PR #166](https://github.com/rysweet/RabbitHole/pull/166) merged at
  `bb617171524fa11d59b71b77a0d29d1b645e2507`. It adds a generated archive test
  proving a sibling Tweedle type with an unsupported complex field initializer
  fails clearly instead of being silently dropped.
- [RabbitHole PR #167](https://github.com/rysweet/RabbitHole/pull/167) merged at
  `4c5e2f21b2674f07176df40f90ded35e5738bde3`. It adds
  `desktop-run-pixel-observation.json`, which records a screenshot and center
  pixel when possible, or records blocker codes and component state when not.
- [eatme PR #98](https://github.com/rysweet/eatme/pull/98) merged at
  `11c8c58a33b2c6c7ec93e1b4a057c375e0dbb70f`. It adds plain-language
  first-lesson readiness output for the countable `evidence_progress` summary
  and every required evidence item.
- This `drinkme` status update records those merge states in the public status
  page and control docs.

## What this proves

- Complex-initializer sibling Tweedle types now have clear-failure regression
  coverage instead of relying on silent omission.
- A desktop run now has a machine-readable place to record whether pixel
  observation happened, and if not, why not.
- eatme can show readiness progress without requiring JSON output.
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
- PR #166 does not add full Tweedle decode support, including method,
  constructor, complex-value, resource-expression, or missing-parent behavior.
- PR #167 does not prove that pixels were drawn correctly; it records an
  observation when possible and a clear blocker when not.
- PR #98 changes reporting only; it does not add new runtime proof.

## Follow-up work

- Use the new pixel observation file in the next comparison run before claiming
  any visible rendering result.
- Keep future status updates separate from older evidence entries so historical
  records stay intact.
