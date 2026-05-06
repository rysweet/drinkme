# 0078 - Desktop save shortcut dispatch

## What changed

- eatme [PR #77](https://github.com/rysweet/eatme/pull/77) adds a bounded
  desktop-control probe for the first-lesson readiness path.
- After eatme finds and activates the Alice main window, it sends `Ctrl+S` to
  that exact window with `xdotool`.
- The result is recorded as `save_project_desktop_shortcut_dispatch` in launch
  manifests and as `dispatch-save-project-shortcut` in
  `ui-action-contract.json`.

## Evidence

Real run `desktop-save-dispatch-20260506113637` compared original Alice
`0e2f80df62` with RabbitHole `dcc0d9f57e`.

| Target | What passed | Where it stopped |
| --- | --- | --- |
| Original Alice | Window detection, window activation, and Ctrl+S input dispatch. | Object placement, because original Alice does not expose the eatme proof hooks. |
| RabbitHole | Window detection, window activation, Ctrl+S input dispatch, object placement, procedure edit, bounded run-world proof, and backend project-save proof. | Overall status remains blocked until fuller desktop lesson automation exists. |

## What this does not prove

- It does not prove that Alice's desktop save menu completed a save.
- It does not prove saved project contents.
- It does not replace the backend project-save proof from RabbitHole
  [PR #147](https://github.com/rysweet/RabbitHole/pull/147) and eatme
  [PR #76](https://github.com/rysweet/eatme/pull/76).
- It does not prove desktop object placement, editor interaction, run-button
  use, visible rendering, grading, creative assessment, or full teacher/student
  lesson completion.

## Why it matters

The previous loop said not to add another backend-only proof just to move a
status line. This change is the first small replacement of a backend-only seam
with a real desktop input action while keeping the evidence label narrow enough
to be true.

## Next boundary

The useful next step is not more naming. It is either a deterministic desktop
object/edit/run action or a fuller teacher/student lesson path that still keeps
proof gates explicit.
