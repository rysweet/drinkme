# 0080 - Run-window observation

## What changed

- eatme [PR #79](https://github.com/rysweet/eatme/pull/79) adds a bounded
  observation probe after the desktop Run shortcut dispatch.
- The probe records `observe-run-window-after-shortcut` in
  `ui-action-contract.json`.
- The readiness manifest records `run_world_desktop_window_observed`.
- A visible Alice Run window passes that assertion. If Ctrl+F5 was dispatched
  but no Run window appears, eatme records the failed observation as the current
  blocker instead of pretending the step passed.

## Evidence

Real run `run-window-observation-accepted-20260506131119-offline` compared
original Alice `0e2f80df62` with RabbitHole `dcc0d9f57e`.

| Target | What passed | What was observed |
| --- | --- | --- |
| Original Alice | Window detection, window activation, and Ctrl+S input dispatch. | It stopped at object placement because original Alice does not expose the eatme proof hooks. |
| RabbitHole | Window detection, activation, Ctrl+S input dispatch, gated Ctrl+F5 Run shortcut dispatch, object placement, procedure edit, bounded run-world proof, and backend project-save proof. | `run_world_desktop_window_observed` was recorded as failed: Ctrl+F5 dispatch succeeded, but no Alice Run window was observed. |

The overall readiness report still passed with
`readiness_status=blocked_until_ui_automation`. That is intentional. eatme
now records the desktop-result gap clearly instead of converting a known
unproven UI result into an incomplete evidence contract.

## What this does not prove

- It does not prove that Ctrl+F5 opened the desktop Run window.
- It does not prove desktop world execution.
- It does not replace the bounded backend run-world proof.
- It does not prove desktop gallery placement, editor interaction, desktop save
  completion, visible rendering, grading, creative assessment, or full
  teacher/student lesson completion.

## Why it matters

The previous loop proved bounded desktop input dispatch. This loop checked for a
visible result and found a real stop point: no Run window was observed after the
shortcut in the current Xvfb run. That is less satisfying than a pass, but more
useful than a green label. It tells the next desktop-control loop exactly where
the evidence runs out.

## Next boundary

The next useful desktop work is to explain or remove the Run-window blocker:
handle any modal interference, find a stable Run-window affordance, or switch to
another deterministic first-lesson desktop result that can be observed without
overstating what Alice did.
