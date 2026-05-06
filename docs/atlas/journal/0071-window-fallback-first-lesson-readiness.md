# 0071 - Window fallback first-lesson readiness

This entry records the follow-up eatme window-targeting fix after the
object-placement hook became consumable.

## What changed

- [eatme PR #71](https://github.com/rysweet/eatme/pull/71) handles bare-Xvfb
  runs where `wmctrl -lx` cannot list windows because there is no window-manager
  client list.
- eatme now falls back to `xwininfo -root -tree` for Alice window discovery.
- eatme now falls back to `xdotool windowfocus` when `wmctrl -ia` cannot focus
  the detected Alice window.
- The Alice window matcher was tightened so the license dialog is not mistaken
  for the main Alice window.
- `glxinfo` is now treated as diagnostic-only, matching the docs and scenario
  assets.

## What the real run showed

The executed first-lesson readiness sequence now reaches the expected bounded
state:

- Overall readiness report: `passed=true`.
- Readiness status: `blocked_until_ui_automation`.
- Original Alice target: `ui_action_automation_unimplemented` because it does
  not expose the object-placement hook.
- RabbitHole target: `ui_action_remaining_steps_unimplemented`.
- RabbitHole action evidence:
  - Alice main window detected.
  - Alice main window focused.
  - `place_object_ui_action` passed.
  - `edit_procedure_ui_action` remained blocked.
  - `run_world_ui_action` remained blocked.
  - `save_project_ui_action` remained blocked.

## What this proves

- eatme can now run the first-lesson readiness sequence far enough to compare
  original Alice and RabbitHole at the object-placement boundary.
- RabbitHole has advanced past object-placement proof in this harness.
- The next missing actions are now explicit and narrower: edit a procedure or
  code block, run the world, and save the project.

## What this does not prove

- It does not automate Alice gallery UI clicks.
- It does not edit a procedure or code block.
- It does not run the world.
- It does not save from the desktop UI.
- It does not grade projects, assess creativity, or complete a teacher/student
  lesson.
- It does not prove broad Alice compatibility beyond this selected scenario.

## Gate notes

- eatme focused window-fallback tests passed.
- Full `eatme-alice` tests passed.
- Asset validation passed.
- Generated Gadugi adapters were fresh.
- eatme quality gates passed locally and in GitHub Actions.
- The manual real-Alice GitHub job remains intentionally skipped by workflow
  rules; the real run was executed locally with explicit `EATME_REAL_ALICE=1`.
