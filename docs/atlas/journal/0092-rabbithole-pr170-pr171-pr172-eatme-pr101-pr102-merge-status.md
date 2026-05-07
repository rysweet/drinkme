# 0092 - RabbitHole PR #170/#171/#172 and eatme PR #101/#102 merge status

## Summary

RabbitHole PR #170, RabbitHole PR #171, RabbitHole PR #172, eatme PR #101, and
eatme PR #102 have merged. RabbitHole pixel observation now falls back from the
raw Run display target to the attached Run panel while preserving exact blockers.
RabbitHole archive reading now rejects resource-typed Tweedle field initializers
instead of accepting them as plain strings. RabbitHole also writes
`desktop-first-lesson-next-action.json`, a conservative no-go file that names the
missing desktop Save-menu and code/procedure action targets. eatme now shows
explicit next-action evidence in first-lesson output and adds the
`media-audio-cue-storyboard` student scenario for `media-audio-creator`.

These changes make the next work clearer. They do not prove full Alice UI
automation, visible rendering, desktop save-menu completion, grading, creative
assessment, or first-lesson completion.

## What changed

- [RabbitHole PR #170](https://github.com/rysweet/RabbitHole/pull/170) merged at
  `7e58f46b5b1d9624dd54bf1d2367243349ce8a28`. It falls back from the raw Run
  display target to the attached Run panel for pixel sampling while preserving
  exact blockers.
- [RabbitHole PR #171](https://github.com/rysweet/RabbitHole/pull/171) merged at
  `34a48d0b24ebf933925ad6237afaa4ca7518fd99`. It rejects resource-typed Tweedle
  field initializers instead of accepting them as plain string literals.
- [RabbitHole PR #172](https://github.com/rysweet/RabbitHole/pull/172) merged at
  `e0c199ab88d10f635d4f3e9e5d67553fb1fd3f4f`. It adds
  `desktop-first-lesson-next-action.json`, which names the missing deterministic
  desktop Save-menu action and code editor/procedure action targets.
- [eatme PR #101](https://github.com/rysweet/eatme/pull/101) merged at
  `546dfc7c2cdbc5ca6c4526fe3e90bb9f717999ed`. It shows explicit
  `next_action`/`nextAction` evidence in first-lesson plain output as
  `fix next: ...`.
- [eatme PR #102](https://github.com/rysweet/eatme/pull/102) merged at
  `3e183407e247944831a6f7ff44870c71169302f4`. It adds the
  `media-audio-cue-storyboard` student scenario for `media-audio-creator`,
  including the generated adapter and documentation updates.
- This `drinkme` status update records those merge states in the public status
  page and control docs.

## What this proves

- Pixel observation has a better chance to produce useful evidence because it can
  use the attached Run panel when the raw target is not showing yet.
- Resource-typed Tweedle field initializers now fail clearly instead of being
  treated as plain strings.
- The next first-lesson no-go file names the missing deterministic Save-menu and
  code/procedure action targets.
- eatme can show explicit next-action evidence in plain first-lesson output.
- The instructor/student corpus now includes a media/audio student scenario.
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
- PR #170 does not prove visible rendering correctness; observed pixel evidence
  only means a desktop screenshot was captured and sampled.
- PR #171 does not add full Tweedle decode support.
- PR #172 records a blocked/no-go next-action file; it does not complete desktop
  Save-menu automation or code/procedure editing.
- PR #101 changes reporting only; it does not add new runtime proof.
- PR #102 adds scenario coverage; it does not grade student work or prove lesson
  completion.

## Follow-up work

- Use the next-action no-go file to implement one deterministic Save-menu or
  code/procedure action proof.
- Keep future status updates separate from older evidence entries so historical
  records stay intact.
