# 0084 - Run-window toolbar proof

## What changed

- RabbitHole [PR #148](https://github.com/rysweet/RabbitHole/pull/148) adds an
  opt-in Run-window evidence hook.
- When the harness sets `org.alice.eatme.runWindowEvidenceDir`, Alice writes
  `run-window-created.json` after it prepares the desktop Run frame.
- The hook is off by default. If the proof file cannot be written, Alice logs the
  failure but does not break the normal Run action.
- eatme [PR #83](https://github.com/rysweet/eatme/pull/83) passes that property
  into RabbitHole, keeps Ctrl+F5 and toolbar-click evidence separate, checks the
  fixed 1000x740 Alice launch geometry before clicking the toolbar Run button,
  and captures a screenshot after the Run frame is observed.
- eatme also split its quality gate into parallel static, test, and coverage jobs
  with separate Cargo cache keys. The aggregate required job name stayed the
  same.

## Real-run evidence

Real run `run-window-geometry-license-20260506170700` used:

- original Alice from `/home/azureuser/src/alice3`;
- RabbitHole after PR #148's source changes;
- `EATME_REAL_ALICE=1`;
- `EATME_ACCEPT_ALICE_LICENSES_FOR_TESTS=1`.

The run passed with `readiness_status=blocked_until_ui_automation`. That status
is intentional: the harness proved the next boundary but still stops before full
desktop lesson automation.

| Probe | Result | Meaning |
| --- | --- | --- |
| `dispatch-run-world-shortcut` | passed | eatme delivered Ctrl+F5 to the Alice window. |
| `observe-run-window-after-shortcut` | failed | Ctrl+F5 still did not open an observed Run window in this Xvfb run. |
| `dispatch-run-toolbar-button` | passed | eatme verified the Alice window was 1000x740, then clicked the configured toolbar Run coordinate `(344,47)`. |
| `observe-run-window-after-toolbar-button` | passed | RabbitHole wrote `run-window-created.json`, and eatme captured `screenshots/run-window-after-dispatch.png`. |

The important shift is that the harness can now tell the difference between
"a keypress was sent" and "Alice actually prepared the Run frame."

## What this still does not prove

- Ctrl+F5 opening the Run window.
- Desktop world execution after the Run frame opens.
- Visible scene rendering correctness.
- Desktop save-menu completion.
- Grading or creative assessment.
- A full teacher/student lesson creation and consumption flow.

## Why it matters

The previous loop only proved that eatme could deliver Ctrl+F5 after focusing
Alice. This loop proves a stronger desktop boundary: RabbitHole can open the Run
frame when eatme uses a bounded toolbar click, and the proof is a file written by
Alice itself rather than a guess from window text alone.

The coordinate click is still not a great long-term interface. It is bounded by
the fixed launch geometry and backed by the Alice-side sentinel, so it is useful
evidence now. It should eventually be replaced by a stable UI action seam or
accessibility path.

## Next evidence targets

1. Replace the toolbar coordinate with a stronger Run action affordance.
2. Prove desktop world execution and visible rendering after the Run frame opens.
3. Prove desktop save completion, not just backend save-hook output or Ctrl+S
   input dispatch.
4. Continue keeping drinkme status aligned after each source loop.
