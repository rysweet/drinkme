# 0089 - RabbitHole PR #164 and eatme PR #96 merge status

## Summary

RabbitHole PR #164 and eatme PR #96 have merged. RabbitHole now has a generated
archive test for a constructor-bearing sibling Tweedle type, matching the
clear-failure behavior added for method-bearing sibling types. eatme now reports
a compact `evidence_progress` summary that counts required first-lesson evidence
as present, missing, invalid, not observed, or blocked.

These changes make progress easier to read. They do not prove full Alice UI
automation, visible rendering, desktop save-menu completion, grading, creative
assessment, or first-lesson completion.

## What changed

- [RabbitHole PR #164](https://github.com/rysweet/RabbitHole/pull/164) merged at
  `fb3e419b81c55b0e055711c9b57d3143f4f69f10`. It adds a generated archive test
  proving a constructor-bearing sibling Tweedle type fails clearly instead of
  being silently dropped; it does not add full Tweedle decode support.
- [eatme PR #96](https://github.com/rysweet/eatme/pull/96) merged at
  `9d765fec2d8f9f3a029b5222d48b3de23b461d5b`. It adds `evidence_progress` to
  first-lesson readiness reports so the output can say how many required
  evidence items are present, missing, invalid, not observed, or blocked.
- This `drinkme` status update records those merge states in the public status
  page and control docs.

## What this proves

- Constructor-bearing sibling Tweedle types now have the same clear-failure
  regression coverage as method-bearing sibling Tweedle types.
- eatme can now show countable first-lesson readiness progress instead of only a
  list of required evidence.
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
- PR #164 does not add full Tweedle method, constructor, complex-value, or
  missing-parent decode support.
- PR #96 summarizes existing evidence only; it does not add new runtime proof.

## Follow-up work

- Add separate repo evidence before claiming any of the unproven product
  behaviors above.
- Keep future status updates separate from older evidence entries so historical
  records stay intact.
