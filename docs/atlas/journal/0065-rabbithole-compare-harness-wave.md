# 0065 - RabbitHole comparison harness wave

## Purpose

This journal records the integrated RabbitHole and eatme comparison-harness wave after the
repository rename to `rysweet/RabbitHole`.

The work improved four modernization fronts:

1. exported project Ant behavior;
2. generated-source timer-handler seam behavior;
3. primitive Tweedle initializer decoding for JSON project and class reads;
4. eatme baseline-vs-modernized comparison evidence.

## Integrated source changes

| Pull request | Merge commit | Evidence |
| --- | --- | --- |
| `rysweet/eatme#57` | `1c488255064b51ecab7294cc392a10ea39cbd2f2` | Added comparison scorecard/timing fields. This is instrumentation, not performance proof by itself. |
| `rysweet/RabbitHole#124` | `5292f58b284e1e4e6dfc8b34fe7a8440d40e1224` | Proved exported NetBeans project Ant `run-test-with-main` behavior without Sims assets. |
| `rysweet/RabbitHole#126` | `247fcf811c7029feda0d847b4e05e17552fbb364` | Decoded primitive Tweedle field initializers for integer, decimal, text, and Boolean values while preserving unsupported boundaries. |
| `rysweet/RabbitHole#125` | `44bd1b533865d47afae526553dd422fabeaa53ee` | Characterized generated time-listener dispatch through the timer-handler seam after correcting an overstated automatic-display claim. |

## Review findings that changed the work

The first PR #125 review rejected the original wording because the test used a private
timer-handler update seam and did not exercise the full automatic display tick path. The
branch was corrected before merge:

- the test name now says it covers the timer-handler seam;
- the assertion now says the generated listener runs when the timer-handler seam updates;
- the pull request body explicitly says the automatic display tick path remains unprotected.

This matters because generated-source tests are useful only when the claim matches the
execution path. A reflection-based seam test is acceptable as a protected boundary, but it is
not full runtime UI coverage.

## eatme execute comparison evidence

The first real execute comparison ran:

- baseline target: `/home/azureuser/src/alice3` at
  `0e2f80df62e64f16a5416792164d2c3c9d9da99c`;
- modernized target: clean RabbitHole worktree at
  `247fcf811c7029feda0d847b4e05e17552fbb364`;
- scenario: `real-alice-launch-smoke`;
- run id: `baseline-0e2f80d-vs-rabbithole-247fcf8-20260505194437`.

Result:

- baseline passed launch smoke;
- modernized failed package preflight with `alice_package_failed`;
- no timing comparison was valid because both targets did not pass.

The modernized failure was not an Alice runtime failure. It was a target-preparation failure:
the clean RabbitHole worktree did not have the `tweedle-lang` grammar submodule initialized.
Maven failed the `require-tweedle-lang-submodule` enforcer rule before packaging could reach
runtime launch.

The second execute comparison initialized `tweedle-lang` and reran:

- run id: `baseline-0e2f80d-vs-rabbithole-247fcf8-submodule-20260505194834`;
- baseline result: passed launch smoke in 90026 ms;
- modernized result: passed launch smoke in 122293 ms;
- timing scorecard: baseline faster by 32267 ms for this one same-machine sample.

This is real execute evidence, but it is not yet a stable speed claim. Repeated same-machine
runs are required before treating the timing delta as representative.

The scorecard still reported functionality as `different` because assertion details included
volatile X display identifiers (`:99` vs `:100`) even though both `display_responsive`
assertions passed. That is a harness normalization issue, not evidence of functional
behavior divergence.

Session artifacts:

- first comparison manifest:
  `/home/azureuser/.copilot/session-state/0d7fa6b6-9ef5-4278-a6c8-5672d3328455/files/eatme-execute-comparison-runs/comparisons/real-alice-launch-smoke/baseline-0e2f80d-vs-rabbithole-247fcf8-20260505194437/comparison-manifest.json`
- first reduced summary:
  `/home/azureuser/.copilot/session-state/0d7fa6b6-9ef5-4278-a6c8-5672d3328455/files/eatme-execute-comparison-summary.json`
- second comparison manifest:
  `/home/azureuser/.copilot/session-state/0d7fa6b6-9ef5-4278-a6c8-5672d3328455/files/eatme-execute-comparison-runs/comparisons/real-alice-launch-smoke/baseline-0e2f80d-vs-rabbithole-247fcf8-submodule-20260505194834/comparison-manifest.json`
- second reduced summary:
  `/home/azureuser/.copilot/session-state/0d7fa6b6-9ef5-4278-a6c8-5672d3328455/files/eatme-execute-comparison-submodule-summary.json`

## Atlas implications

| Area | Updated understanding |
| --- | --- |
| Project IO/player reads | Primitive Tweedle field initializers now move from unsupported to supported for JSON `.a3w` and `.a3c` reads. Methods, constructors, complex initializer expressions, and unresolved supertypes remain boundaries. |
| NetBeans/export behavior | The Ant `run-test-with-main` target has stronger evidence. Full graphical launcher behavior and full StageIDE export UI behavior remain unproven. |
| Runtime behavior | Time-listener generated source has a protected timer-handler seam. The automatic display tick path still needs a public-path characterization. |
| eatme comparison harness | The harness can execute both configured targets and emit scorecards. It needs assertion normalization and repeated runs before speed claims. |
| Operational setup | Clean RabbitHole comparison targets must initialize `tweedle-lang`; otherwise packaging fails before launch. This setup requirement belongs in future eatme target preparation guidance. |

## Next evidence targets

1. Normalize volatile assertion details in eatme comparison diffs so equivalent passing
   assertions do not imply functionality differences.
2. Repeat same-machine baseline-vs-RabbitHole execute comparisons before making speed claims.
3. Add eatme target-preflight guidance or automation for required RabbitHole submodules.
4. Add a public-path automatic display tick characterization for generated time listeners.
5. Continue broadening Tweedle/player support without erasing unsupported-boundary tests.
