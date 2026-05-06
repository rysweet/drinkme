# 0083 - Run shortcut focus delivery

## What changed

- eatme [PR #82](https://github.com/rysweet/eatme/pull/82) changes only the
  gated Run shortcut dispatch path.
- Before sending Ctrl+F5, eatme now uses `xdotool windowfocus --sync` on the
  already detected Alice window.
- The existing Ctrl+S save-shortcut dispatch still uses the previous direct
  `xdotool key --window ...` path.
- eatme also reports the exact attempted command when `xdotool` fails to start
  or cannot be executed.

## Evidence

The first refocus experiment used `xdotool windowactivate --sync`, but that was
the wrong primitive for the current bare-Xvfb environment:

```text
Your windowmanager claims not to support _NET_ACTIVE_WINDOW, so the attempt to activate the window was aborted.
```

The merged version uses `windowfocus --sync` instead.

Real run `run-window-refocus-20260506150631-focus` used both
`EATME_REAL_ALICE=1` and `EATME_ACCEPT_ALICE_LICENSES_FOR_TESTS=1`.

| Target | What passed | Where it stopped |
| --- | --- | --- |
| Original Alice | Window detection, window activation, and Ctrl+S input dispatch. | Object placement, because original Alice does not expose the eatme proof hooks. |
| RabbitHole | Window detection, activation, Ctrl+S input dispatch, focused Ctrl+F5 Run shortcut dispatch, object placement, procedure edit, bounded run-world proof, and backend project-save proof. | No Alice Run window was observed after Ctrl+F5. |

The overall readiness report passed with
`readiness_status=blocked_until_ui_automation`. That means the comparison
sequence is internally consistent, not that the desktop Run action completed.

## What this does not prove

- It does not prove that Ctrl+F5 opens the desktop Run window.
- It does not prove desktop world execution from the shortcut.
- It does not prove visible rendering or deployed launcher success.
- It does not prove desktop save completion.
- It does not prove grading, creative assessment, or full teacher/student lesson
  completion.

## Why it matters

This removes a bad assumption. Bare Xvfb does not necessarily provide the
window-manager behavior needed by `windowactivate`. The focus step can now run
without depending on `_NET_ACTIVE_WINDOW`, and the remaining result is clearer:
the shortcut can be delivered, but the Run window still is not observed.

## Next boundary

Investigate Alice's actual desktop Run action path rather than adding another
label around Ctrl+F5. Good candidates are a bounded menu/action probe, a better
window observation target, or a precise machine-readable no-go reason if the Run
action is unavailable in this state.
