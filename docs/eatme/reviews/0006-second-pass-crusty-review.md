# Eatme review 0006: second-pass crusty review

## Framing

The adapted plan is much better than the first version. It is real Alice, real X display, and real artifacts.

It still tries to build too much harness before proving the harness deserves to exist.

## Required changes

1. Split Phase 1 into a smaller Milestone 0:
   - `eatme-cli`
   - `eatme-core`
   - `eatme-alice`
   - `eatme-test-support`

2. Make the first vertical slice dumber:
   - detect dependencies
   - package Alice
   - launch under Xvfb
   - isolate user state
   - capture logs, screenshot, manifest
   - emit deterministic pass/fail

3. Define deterministic evidence as the test oracle. Required manifest fields:
   - Alice repo path and git commit
   - eatme git commit
   - Java/Maven versions
   - build command and exit status
   - launch command
   - `DISPLAY`
   - Xvfb PID and Alice PID
   - timeout values
   - screenshot path and hash
   - log path and hash
   - dependency detection results
   - failure category

4. Demote agentic judgment:
   - agents may annotate the run
   - agents must not decide pass/fail in the first slice
   - pass/fail comes from process, X server, window/log/screenshot evidence

5. Add parallelism rules:
   - default serial execution
   - no parallel GUI runs until display allocation, workspace isolation, locking, and cleanup are tested
   - later parallel runs need unique `DISPLAY`, workspace, user home, prefs root, and cleanup guard

6. Add governance boundaries:
   - agents may read lessons/scenarios/artifacts
   - agents may not modify Alice source
   - agents may not modify `eatme` source during test execution
   - all commands must be logged
   - memory writes stay under `.eatme/memory` or `alice.eatme`
   - no silent repo mutation

7. Clarify CI expectations:
   - do not assume GPU availability
   - require Mesa software rendering/GLX checks
   - real Alice tests stay gated behind `EATME_REAL_ALICE=1`

## Acceptable sequencing

1. Dependency audit command.
2. Offline/package command wrapper.
3. Xvfb lifecycle wrapper.
4. Direct Java launcher.
5. Artifact capture.
6. Deterministic smoke verdict.
7. One editable YAML scenario.
8. Gadugi adapter.
9. Student persona.
10. Instructor persona.
11. More scenarios.
12. Parallel execution.

## Verdict

No-go for implementing the earlier broad plan.

Go for implementation only if the first implementation is the deterministic real-Alice launch smoke harness.
