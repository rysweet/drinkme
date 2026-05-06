# 0082 - License-preseeded Run-window check

## What changed

- eatme [PR #81](https://github.com/rysweet/eatme/pull/81) adds an explicit
  test-only switch: `EATME_ACCEPT_ALICE_LICENSES_FOR_TESTS=1`.
- When the switch is set, eatme seeds Alice's isolated per-run Java Preferences
  before launch so the Alice and Sims license prompts do not appear.
- When the switch is not set, eatme does nothing. The default behavior still
  shows the license prompt when Alice asks for it.
- The launch manifest records `alice_license_preferences_seeded` when the
  opt-in path is used.

## Evidence

Real run `run-window-license-seeded-clean-20260506143829` compared original
Alice `0e2f80df62` with RabbitHole `dcc0d9f57e`.

The command used both `EATME_REAL_ALICE=1` and
`EATME_ACCEPT_ALICE_LICENSES_FOR_TESTS=1`.

| Target | What passed | Where it stopped |
| --- | --- | --- |
| Original Alice | Window detection, window activation, and Ctrl+S input dispatch. | Object placement, because original Alice does not expose the eatme proof hooks. |
| RabbitHole | Window detection, activation, Ctrl+S input dispatch, gated Ctrl+F5 Run shortcut dispatch, object placement, procedure edit, bounded run-world proof, and backend project-save proof. | No Alice Run window was observed after Ctrl+F5, even though the license window was gone. |

The overall readiness report still passed with
`readiness_status=blocked_until_ui_automation`. The result is narrower now:
license prompting is no longer the blocker under explicit opt-in, but desktop
Run-window success is still unproven.

## What this does not prove

- It does not claim user consent outside the explicit test switch.
- It does not prove that Ctrl+F5 opens the desktop Run window.
- It does not prove desktop world execution, desktop save completion, visible
  rendering, grading, creative assessment, or full teacher/student lesson
  completion.

## Why it matters

This removes one source of ambiguity. The license modal was real, but it was not
the whole Run-window problem. With a first-run-ready test profile, the same
shortcut still does not produce an observed Run window. The next loop can focus
on shortcut delivery, focus, accelerator behavior, or finding a different stable
desktop Run affordance.

## Next boundary

Investigate why Ctrl+F5 does not open an observed Run window after license
preseeding. Do not claim desktop Run success until the Run window is actually
visible in the captured window tree.
