# 0087 - RabbitHole PR #159/#160 and eatme PR #93 merge status

## Summary

RabbitHole PRs #159 and #160 and eatme PR #93 have merged. PR #159 adds a
generated archive test for a missing Tweedle source entry. PR #160 records that
pixel and screenshot proof were not observed by the Run-window attachment
signal. eatme PR #93 lists the readiness evidence categories in the report.
These changes are useful, but they do not prove full Alice UI automation,
visible rendering, desktop save-menu completion, grading, creative assessment,
or first-lesson completion.

## What changed

- [RabbitHole PR #159](https://github.com/rysweet/RabbitHole/pull/159) merged
  at `9dbf0266ad7d61439f5dd74121e744dbbd365462`. It adds a generated
  LFS-independent archive test where a manifest-declared Tweedle source entry is
  missing and must fail clearly.
- [RabbitHole PR #160](https://github.com/rysweet/RabbitHole/pull/160) merged
  at `18c533efdacc7bdefa971c82ac655d5127bc743e`. It adds
  `desktop-run-pixel-boundary.json` with `status: "not_observed"` and says
  pixel and screenshot proof need separate evidence.
- [eatme PR #93](https://github.com/rysweet/eatme/pull/93) merged at
  `f5c08aea14c679124afc680fc9bc9e155da237dd`. It makes first-lesson readiness
  reports list the concrete evidence categories eatme expects from RabbitHole.
- This `drinkme` status update records those merge states in the public status
  page and control docs.

## What this proves

- Missing manifest-declared Tweedle source entries now have a checked failure
  test.
- The desktop Run-window attachment evidence now has a machine-readable file
  saying pixel proof was not observed.
- eatme readiness reports now show the evidence categories they require instead
  of hiding them in prose.
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
- PR #159 does not add broad Tweedle decode support, including full method,
  constructor, complex value, or missing-parent decoding.
- PR #160 does not prove pixels, screenshots, visible rendering, or grading.
- PR #93 does not create new runtime evidence; it lists required evidence in the
  readiness output.

## Follow-up work

- Add separate repo evidence before claiming any of the unproven product
  behaviors above.
- Keep future status updates separate from older evidence entries so historical
  records stay intact.
