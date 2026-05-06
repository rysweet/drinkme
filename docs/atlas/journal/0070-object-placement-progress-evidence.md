# 0070 - Object-placement progress evidence

This entry records the follow-up evidence from running eatme against a
RabbitHole checkout with the backend object-placement hook.

## What changed

- [RabbitHole PR #144](https://github.com/rysweet/RabbitHole/pull/144) keeps
  `tools/eatme-place-object` stdout parseable as the hook result JSON. Alice
  project migration code can print progress text through `System.out`; the hook
  now suppresses that incidental output while it loads and rewrites the project.
- [eatme PR #70](https://github.com/rysweet/eatme/pull/70) adds action-level
  progress to the first-lesson readiness report. A target can still fail for an
  earlier reason, such as missing Alice window detection, while the report shows
  that object placement itself passed.

## What the real run showed

The executed first-lesson readiness run reached the RabbitHole hook and produced
real object-placement proof:

- `place_object_candidate_hook_probe` passed for the modernized target.
- `place_object_ui_action` passed for the modernized target.
- The hook returned one JSON line on stdout and empty stderr.
- `placed-project.a3p`, `placement.json`, and `scene.diff.json` were non-empty.

The run still did not pass first-lesson readiness because both targets failed
earlier at Alice window detection:

- `specific_alice_window_detected` failed.
- `activate_alice_window_ui_action` failed.
- The target failure category remained `alice_window_not_detected`, which is the
  honest result for this environment.

## What this proves

- RabbitHole's backend object-placement hook can be consumed by eatme in a real
  first-lesson readiness run.
- eatme can show partial first-lesson action progress without pretending the
  whole target is ready.
- The next blocker is clearer: real window targeting must be fixed before the
  readiness sequence can advance to the normal `ui_action_remaining_steps_unimplemented`
  state.

## What this does not prove

- It does not prove Alice gallery UI clicks.
- It does not prove reliable Alice window detection in the current environment.
- It does not edit a procedure or code block.
- It does not run the world.
- It does not save from the desktop UI.
- It does not grade projects, assess creativity, or complete a teacher/student
  lesson.

## Gate notes

- RabbitHole focused hook tests passed.
- RabbitHole package build and migrated-starter hook smoke passed.
- RabbitHole GitHub checks were green before merge.
- eatme focused tests, full `eatme-alice` tests, quality gates, and asset
  validation passed.
- eatme GitHub checks were green before merge; Pages deploy and manual real
  Alice launch smoke were skipped by workflow rules.
