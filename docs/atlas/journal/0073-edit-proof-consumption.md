# 0073 - Edit proof consumption

This entry records the first move from an edit-action no-go contract to backend
edit proof that eatme can consume.

## What changed

- [RabbitHole PR #145](https://github.com/rysweet/RabbitHole/pull/145) adds
  `tools/eatme-edit-procedure`.
- The hook loads the project produced after object placement, edits a fixed
  scene procedure selector, writes `edited-project.a3p`, writes
  `procedure.diff.json`, and emits JSON-only proof.
- [eatme PR #73](https://github.com/rysweet/eatme/pull/73) runs that hook after
  object placement proof exists.
- eatme accepts edit proof only when the hook returns:
  - schema `eatme.alice-procedure-edit-result/v1`;
  - status `edited`;
  - exact selector `scene.eatmeFirstLessonStep`;
  - a non-empty edited project artifact;
  - a non-empty procedure/code diff artifact.
- The first-lesson status still records run-world and save-project as blocked.

## What this proves

- RabbitHole has a deterministic backend proof path for one procedure edit after
  object placement.
- eatme can move the first-lesson action report past object placement and edit
  proof when the RabbitHole hooks are present.
- The comparison harness is now closer to a real lesson path while still
  separating proven backend changes from unproven desktop actions.

## What this does not prove

- It does not click the Alice desktop code editor.
- It does not run the world.
- It does not save the project through the desktop interface.
- It does not grade work, assess creativity, or complete a teacher/student
  lesson.
- It does not prove original Alice has the same backend hook.

## Gate notes

- RabbitHole PR #145 passed focused local tests, package build, smoke use after
  object placement, focused review, and GitHub checks before merge.
- eatme PR #73 passed full workspace tests, asset validation, generated adapter
  freshness checks, quality gates, diff checks, focused review, and GitHub
  checks before merge.
- Focused review caught that eatme readiness validation initially accepted any
  `scene.*` selector. The final branch requires the exact first-lesson selector
  that the hook proves.
