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
  instructor/student readiness is green, but review is still running.
- eatme depends on the narrower
  [RabbitHole PR #154](https://github.com/rysweet/RabbitHole/pull/154)
  boundary. PR #154 records a narrow Run window attachment signal. It proves
  Alice put the Run panel into the Run window area. It does not prove pixels
  were drawn, does not prove the lesson finished, and is not grading.

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

1. Keep PR #154 limited to the Run window attachment signal.
2. Treat [RabbitHole PR #155](https://github.com/rysweet/RabbitHole/pull/155)
   as green on launcher evidence checks while review is still running.
3. Treat [RabbitHole PR #156](https://github.com/rysweet/RabbitHole/pull/156)
   old archive/image recovery checks as still waiting on coverage.
4. Add separate proof before eatme claims pixels were drawn, the lesson
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
