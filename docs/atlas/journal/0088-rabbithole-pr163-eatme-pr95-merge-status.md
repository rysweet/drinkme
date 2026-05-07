# 0088 - RabbitHole PR #163 and eatme PR #95 merge status

## Summary

RabbitHole PR #163 and eatme PR #95 have merged. RabbitHole now rejects a project
or type archive when a manifest-declared Tweedle type cannot be decoded, instead
of silently dropping that type. eatme now reads RabbitHole's
`desktop-run-pixel-boundary.json` file and reports whether it is missing,
invalid, or `not_observed`.

These changes make failure states clearer. They do not prove full Alice UI
automation, visible rendering, desktop save-menu completion, grading, creative
assessment, or first-lesson completion.

## What changed

- [RabbitHole PR #163](https://github.com/rysweet/RabbitHole/pull/163) merged at
  `4f225f2795c79f84c367874cd7995dc6dcded22f`. It rejects unsupported
  manifest-declared Tweedle type names with a clear error instead of silently
  dropping a type from the loaded project or type archive.
- [eatme PR #95](https://github.com/rysweet/eatme/pull/95) merged at
  `d29e3d80112dbd6d2f820ceb8989c61c5e7de7b9`. It reports
  `desktop-run-pixel-boundary.json` as missing, invalid, or `not_observed` in
  first-lesson readiness output.
- This `drinkme` status update records those merge states in the public status
  page and control docs.

## What this proves

- One previously silent archive-loss case now fails clearly when a
  manifest-declared Tweedle type cannot be decoded.
- eatme can now show whether the RabbitHole pixel-boundary file is present and
  what status it contains.
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
- PR #163 does not add full Tweedle method, constructor, complex-value, or
  missing-parent decode support.
- PR #95 does not prove pixels, screenshots, visible rendering, desktop save
  completion, grading, creative assessment, or first-lesson completion.

## Follow-up work

- Add separate repo evidence before claiming any of the unproven product
  behaviors above.
- Keep future status updates separate from older evidence entries so historical
  records stay intact.
