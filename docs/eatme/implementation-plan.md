# Eatme implementation plan

The canonical implementation plan is maintained in the private `eatme` repo at:

```text
/home/azureuser/src/eatme/docs/implementation-plan.md
```

This `drinkme` copy records the current planning direction and links the plan to the Alice modernization documentation corpus.

## Current direction

Second-pass review tightened the plan:

- Milestone 0 is a deterministic real-Alice launch smoke only.
- No personas, gadugi dependency, lesson evaluation, or parallel GUI runs in Milestone 0.
- `eatme` owns desktop execution: Alice packaging, Xvfb, display allocation, window/process lifecycle, screenshots, logs, and manifests.
- Gadugi initially treats `eatme` as a CLI/system harness and asserts against `manifest.json`.
- Pass/fail initially comes from deterministic evidence, not agentic judgment.
- Alice.org curriculum scenarios begin after the launch smoke.
- [eatme PR #89](https://github.com/rysweet/eatme/pull/89)
  merged. It improves instructor and student readiness reports, but does not grade
  work or prove full lesson completion.
- [eatme PR #92](https://github.com/rysweet/eatme/pull/92)
  merged at `cfe1f9e364d0015a3f97e237a9de5af670ae3bd6`. It documents the
  RabbitHole evidence needed before first-lesson readiness can be marked ready:
  launch evidence, Run-window evidence, desktop execution evidence,
  screenshot/log/window artifacts, and `ui-action-contract.json`.
- [eatme PR #93](https://github.com/rysweet/eatme/pull/93) merged at
  `f5c08aea14c679124afc680fc9bc9e155da237dd`. It makes first-lesson readiness
  reports list concrete RabbitHole readiness evidence categories; it does not
  create new runtime proof or prove grading, creative assessment, or
  first-lesson completion.
- eatme depends on the merged RabbitHole source PRs:
  [RabbitHole PR #154](https://github.com/rysweet/RabbitHole/pull/154)
  merged. It records that Alice put the Run panel into the Run window area.
  [RabbitHole PR #155](https://github.com/rysweet/RabbitHole/pull/155)
  merged. It records launcher steps and no-go messages, but does not prove
  rendering.
  [RabbitHole PR #156](https://github.com/rysweet/RabbitHole/pull/156)
  merged. It keeps old image recovery while safely rejecting unsupported old
  code.
  [RabbitHole PR #159](https://github.com/rysweet/RabbitHole/pull/159) merged
  at `9dbf0266ad7d61439f5dd74121e744dbbd365462`. It adds a generated archive
  test where a missing Tweedle source entry fails clearly; it does not add broad
  Tweedle decode support.
   [RabbitHole PR #160](https://github.com/rysweet/RabbitHole/pull/160) merged
   at `18c533efdacc7bdefa971c82ac655d5127bc743e`. It adds
   `desktop-run-pixel-boundary.json` with `status: "not_observed"`; it does not
   prove pixels, screenshots, visible rendering, or grading.
  [RabbitHole PR #163](https://github.com/rysweet/RabbitHole/pull/163) merged
  at `4f225f2795c79f84c367874cd7995dc6dcded22f`. It rejects unsupported
  manifest-declared Tweedle type names with a clear error instead of silently
  dropping a type; it does not add full Tweedle decode support.
  [RabbitHole PR #164](https://github.com/rysweet/RabbitHole/pull/164) merged
  at `fb3e419b81c55b0e055711c9b57d3143f4f69f10`. It adds the matching generated
  archive test for a constructor-bearing sibling Tweedle type; it does not add
  full Tweedle decode support.
  [RabbitHole PR #166](https://github.com/rysweet/RabbitHole/pull/166) merged
  at `bb617171524fa11d59b71b77a0d29d1b645e2507`. It adds a generated archive
  test for a sibling Tweedle type with an unsupported complex field initializer;
  it does not add full Tweedle decode support.
  [RabbitHole PR #167](https://github.com/rysweet/RabbitHole/pull/167) merged
  at `4c5e2f21b2674f07176df40f90ded35e5738bde3`. It adds
  `desktop-run-pixel-observation.json` so a run records a screenshot and center
  pixel when possible, or a blocker code and component state when not; it does
  not prove visible rendering or first-lesson completion.
  [RabbitHole PR #168](https://github.com/rysweet/RabbitHole/pull/168) merged
  at `da0fb851fd974721a630811873f0d583a853eb5e`. It adds a generated archive
  test for a sibling Tweedle type with an unresolved parent; it does not add full
  Tweedle decode support.
  [RabbitHole PR #169](https://github.com/rysweet/RabbitHole/pull/169) merged
  at `0a0d182c139aeaf5bc7c2c45213a0392cf8f245c`. It adds machine-readable
  blocker details to `desktop-run-pixel-observation.json`; it does not prove
  visible rendering or first-lesson completion.
- [eatme PR #95](https://github.com/rysweet/eatme/pull/95) merged at
  `d29e3d80112dbd6d2f820ceb8989c61c5e7de7b9`. It reports
  `desktop-run-pixel-boundary.json` as missing, invalid, or `not_observed`; it
  does not prove pixels, visible rendering, grading, or first-lesson completion.
- [eatme PR #96](https://github.com/rysweet/eatme/pull/96) merged at
  `9d765fec2d8f9f3a029b5222d48b3de23b461d5b`. It adds an
  `evidence_progress` summary that counts required first-lesson evidence as
  present, missing, invalid, not observed, or blocked. It summarizes existing
  evidence only.
- [eatme PR #98](https://github.com/rysweet/eatme/pull/98) merged at
  `11c8c58a33b2c6c7ec93e1b4a057c375e0dbb70f`. It shows first-lesson readiness
  progress and every required evidence item in plain text output. It does not
  add new runtime proof.
- [eatme PR #99](https://github.com/rysweet/eatme/pull/99) merged at
  `5e8ba4b8c970d04b410060e90c22a613430e202b`. It reports
  `desktop-run-pixel-observation.json` beside readiness progress, including
  observed screenshot/sample data or blocked component state and blocker codes.
  It does not add new runtime proof.
- RabbitHole PRs #159, #160, #163, #164, #166, #167, #168, and #169 and eatme
  PRs #93, #95, #96, #98, and #99 have merged, but they do not prove full Alice
  UI automation, visible rendering, desktop save-menu completion, grading,
  creative assessment, or first-lesson completion.
- The proof boundary remains a narrow Run window attachment signal: Alice put
  the Run panel into the Run window area. This evidence does not prove pixels
  were drawn, does not prove the lesson finished, and is not grading.
- The PR #92 evidence list does not prove full Alice UI automation, creative
  assessment, learner-world grading, visible rendering correctness, or
  first-lesson completion. It describes what RabbitHole evidence must exist and
  be documented before readiness can be marked ready.

## Milestone 0

Milestone 0 proves:

1. Host dependencies are detected.
2. RabbitHole packages from `/home/azureuser/src/RabbitHole`.
3. Long-lived Xvfb starts with GLX enabled.
4. Alice launches via direct Java and `org.alice.stageide.EntryPoint`.
5. The run uses isolated user home, prefs root, and temp/cache directories.
6. The harness captures process status, logs, window/display data, screenshot, command log, and `manifest.json`.
7. The deterministic assertions pass.

## Required manifest contract

The manifest must include:

- scenario id and run id
- Alice repo path and commit
- eatme commit
- Java/Maven versions
- dependency checks
- build command and exit status
- launch command
- `DISPLAY`
- Xvfb PID and Alice PID
- timeout values
- screenshot path, size, and hash
- log path, size, and hash
- fatal log scan
- assertion results
- failure category

## Post-launch scenario path

After Milestone 0:

1. `building-a-scene-first-world`
2. `code-editor-first-run`
3. `control-structures-visible-change`
4. `introduction-to-events-first-binding`
5. `design-process-thin-slice`

Export/player, collision/proximity games, and broader creative scenarios come later.

## Desktop Run proof path

The next desktop Run work should preserve the current strict boundary:

1. Treat merged RabbitHole PR #154 as limited to the Run window attachment
   signal.
2. Treat merged RabbitHole PR #155 as recorded launcher steps and no-go
   messages, not proof that rendering happened.
3. Treat merged RabbitHole PR #156 as old image recovery support plus safe
   rejection of unsupported old code.
4. Treat merged eatme PR #89 as improved instructor and student readiness reports,
   not grading and not proof of full lesson completion.
5. Treat merged eatme PR #92 as the documentation of required RabbitHole
   evidence categories, not proof that those categories have passed in drinkme.
6. Treat merged eatme PR #93 as a report-output improvement that lists required
   readiness evidence, not grading, creative assessment, or first-lesson
   completion.
7. Treat merged RabbitHole PR #159 as one clear archive failure test, not broad
   Tweedle decode support.
8. Treat merged RabbitHole PR #160 as a pixel-proof boundary record, not proof
   of pixels, screenshots, visible rendering, or desktop save-menu completion.
9. Treat merged RabbitHole PR #163 as a clear rejection for unsupported
   manifest-declared Tweedle type names, not full Tweedle decode support.
10. Treat merged RabbitHole PR #164 as constructor-bearing sibling archive
    coverage for the same clear-failure behavior, not full Tweedle decode support.
11. Treat merged eatme PR #95 as explicit pixel-boundary status reporting, not
    proof of pixels, visible rendering, grading, or first-lesson completion.
12. Treat merged eatme PR #96 as a countable progress summary, not new runtime
    proof.
13. Treat merged RabbitHole PR #166 as complex-initializer sibling archive
    coverage for the same clear-failure behavior, not full Tweedle decode support.
14. Treat merged RabbitHole PR #167 as a pixel observation file that records an
    observation when possible and a clear blocker when not, not visible rendering
    proof.
15. Treat merged eatme PR #98 as plain readiness output, not new runtime proof.
16. Treat merged RabbitHole PR #168 as unresolved-parent sibling archive coverage
    for the same clear-failure behavior, not full Tweedle decode support.
17. Treat merged RabbitHole PR #169 as blocker details for the pixel observation
    file, not visible rendering proof.
18. Treat merged eatme PR #99 as pixel observation reporting, not new runtime
    proof.
19. Add separate proof before eatme claims pixels were drawn, the lesson
    finished, or grading happened.

## Governance boundaries

- Supporting tool repos such as `amplihack-rs`, `gadugi-agentic-test`, `amplihack-recipe-runner`, and `amplihack-memory-lib` are in scope for bug fixes or feature work when needed.
- Any supporting-tool repo change must follow the default workflow, and subagents doing that work must follow the default workflow too.
- No silent repo mutation.

## Review artifacts

- `docs/eatme/reviews/0001-crusty-old-engineer.md`
- `docs/eatme/reviews/0002-rust-memory-architecture.md`
- `docs/eatme/reviews/0003-gadugi-capability-audit.md`
- `docs/eatme/reviews/0004-real-alice-harness-design.md`
- `docs/eatme/reviews/0005-second-pass-harness-review.md`
- `docs/eatme/reviews/0006-second-pass-crusty-review.md`
- `docs/eatme/reviews/0007-second-pass-curriculum-review.md`
- `docs/eatme/reviews/0008-second-pass-gadugi-review.md`
- `docs/eatme/research/0001-alice-org-resource-map.raw.md`
