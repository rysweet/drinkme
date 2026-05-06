# 0069 - Object-placement hook implementation

This entry records the first backend object-placement implementation wave.

## What changed

- [RabbitHole PR #143](https://github.com/rysweet/RabbitHole/pull/143) added
  `tools/eatme-place-object`.
- The hook loads a starter `.a3p`, finds the scene, adds a Bunny-backed
  `SBiped` field, writes `placed-project.a3p`, and emits the JSON schema that
  eatme expects.
- The hook was kept headless by building the AST directly instead of using
  gallery UI classes.
- Review found real hardening issues. The final version escapes JSON control
  characters, validates fixed artifact names, and bounds generated field-name
  suffixes.
- [eatme PR #69](https://github.com/rysweet/eatme/pull/69) consumes valid hook
  proof. When placement is proven, eatme moves from
  `ui_action_automation_unimplemented` to
  `ui_action_remaining_steps_unimplemented`.

## What this proves

- RabbitHole can perform one deterministic backend first-lesson object change
  for `alice-gallery://animals/bunny`.
- eatme can distinguish "object placement is missing" from "object placement is
  proven but editing, running, and saving are still missing."
- The proof artifacts are machine-readable and non-empty.

## What this does not prove

- It does not click through Alice's object gallery.
- It does not edit a procedure or code block.
- It does not run the world.
- It does not save from the desktop UI.
- It does not grade projects, assess creativity, or complete a teacher/student
  lesson.

## Gate notes

- RabbitHole local focused hook tests passed.
- RabbitHole package and packaged-hook smoke passed after initializing
  `tweedle-lang` and skipping network license downloads.
- RabbitHole focused review was clean after hardening fixes.
- RabbitHole GitHub checks were green before merge.
- eatme full quality gates, asset validation, generated adapter freshness, and
  focused review were clean before merge.
