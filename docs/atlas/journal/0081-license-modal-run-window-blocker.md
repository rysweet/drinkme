# 0081 - License modal Run-window blocker

## What changed

- eatme [PR #80](https://github.com/rysweet/eatme/pull/80) sharpens the
  Run-window observation result from PR #79.
- If the window tree shows Alice's license agreement after Ctrl+F5 dispatch,
  eatme now records `observe-run-window-after-shortcut` as blocked with a plain
  message: the license window must be cleared before Run-window observation can
  prove anything.
- eatme also cleans stale X display socket and lock files left by crashed Xvfb
  runs when the socket is not accepting connections and the lock PID is gone.
  This prevents old crashed runs from making every display in `:90` through
  `:129` look busy forever.

## Evidence

Real run `run-window-license-blocker-20260506135409-cleanup` compared original
Alice `0e2f80df62` with RabbitHole `dcc0d9f57e`.

| Target | What passed | Where it stopped |
| --- | --- | --- |
| Original Alice | Window detection, window activation, and Ctrl+S input dispatch. | Object placement, because original Alice does not expose the eatme proof hooks. |
| RabbitHole | Window detection, activation, Ctrl+S input dispatch, gated Ctrl+F5 Run shortcut dispatch, object placement, procedure edit, bounded run-world proof, and backend project-save proof. | Run-window observation is blocked because the Alice license agreement window is still visible after Ctrl+F5. |

The readiness report still passed with
`readiness_status=blocked_until_ui_automation`. That is the right outcome. The
run records a sharper blocker without claiming desktop Run success.

## What this does not prove

- It does not prove the license agreement can be cleared safely.
- It does not prove that Ctrl+F5 opens the desktop Run window after the license
  agreement is cleared.
- It does not prove desktop world execution, desktop save completion, visible
  rendering, grading, creative assessment, or full teacher/student lesson
  completion.

## Why it matters

This is not glamorous. It is useful. eatme now survives stale display files from
crashed runs and names the modal that blocks the next desktop proof. The next
loop can target a real blocker instead of guessing why Run-window observation is
negative.

## Next boundary

Find a safe way to start Alice in a first-run-ready state or clear the license
agreement explicitly, then rerun the same first-lesson path. Do not claim
desktop Run-window success until the window is actually observed.
