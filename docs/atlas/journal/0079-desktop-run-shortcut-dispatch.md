# 0079 - Desktop Run shortcut dispatch

## What changed

- eatme [PR #78](https://github.com/rysweet/eatme/pull/78) adds a bounded
  desktop-control probe for Alice's documented Run shortcut.
- Alice declares the Run operation shortcut as `RunComposite.accelerator =
  VK_F5,PLATFORM_ACCELERATOR_MASK`, so the Xvfb/Linux harness dispatches
  `Ctrl+F5` with `xdotool`.
- eatme only sends that shortcut after both preconditions are true:
  - the Alice main window was detected and activated;
  - procedure/code-block edit proof already exists.
- The manifest assertion is `run_world_desktop_shortcut_dispatch`. The
  ui-action contract probe id is `dispatch-run-world-shortcut`.

## Evidence

Real run `desktop-run-dispatch-20260506120727` compared original Alice
`0e2f80df62` with RabbitHole `dcc0d9f57e`.

| Target | What passed | Where it stopped |
| --- | --- | --- |
| Original Alice | Window detection, window activation, and Ctrl+S input dispatch. | Object placement. Because edit proof was unavailable, eatme did not claim Ctrl+F5 Run shortcut dispatch. |
| RabbitHole | Window detection, activation, Ctrl+S input dispatch, gated Ctrl+F5 Run shortcut dispatch, object placement, procedure edit, bounded run-world proof, and backend project-save proof. | Overall status remains blocked until fuller desktop lesson automation exists. |

## What this does not prove

- It does not prove that the desktop Run window completed world execution.
- It does not replace the backend run-world proof from RabbitHole
  [PR #146](https://github.com/rysweet/RabbitHole/pull/146) and eatme
  [PR #75](https://github.com/rysweet/eatme/pull/75).
- It does not prove desktop gallery placement, editor interaction, desktop save
  completion, visible rendering, grading, creative assessment, or full
  teacher/student lesson completion.

## Why it matters

This is a better desktop probe than sending another shortcut at startup. It is
gated behind the lesson state that makes the Run action meaningful. That keeps
original Alice from receiving a false run-dispatch claim when it has not reached
object placement or edit proof.

## Next boundary

The remaining useful work is harder: prove a real desktop action result, not
just input dispatch. The likely candidates are a deterministic desktop object
placement affordance, a desktop editor target, a Run-window observation, or a
fuller teacher/student lesson path with the same explicit proof gates.
