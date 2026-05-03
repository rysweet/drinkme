# Eatme review 0005: second-pass harness review

## Verdict

The first slice is not implementable as written in the initial implementation plan alone. It is feasible if the detailed direct-Java launch contract from review 0004 is promoted into the plan.

## Required changes

1. Add exact direct-Java launch requirements:
   - JavaFX `--module-path`
   - `--add-modules javafx.graphics,javafx.media`
   - Alice classpath containing `alice-ide` jar and `target/lib/*`
   - `org.alice.stageide.EntryPoint`
   - starter project path
   - `org.alice.ide.rootDirectory`

2. Add Xvfb contract:
   - long-lived Xvfb, not one-shot `xvfb-run`
   - GLX enabled: `+extension GLX +render -noreset`
   - validate with `xdpyinfo`
   - allocate display dynamically or lock `:99`

3. Add OpenGL/JOGL requirements:
   - install Mesa/GLX packages
   - set `LIBGL_ALWAYS_SOFTWARE=1`
   - detect fatal OpenGL/JOGL failures in logs
   - set `-Djogamp.gluegen.UseTempJarCache=false`
   - use per-run `java.io.tmpdir`

4. Strengthen process isolation:
   - per-run `user.home`
   - per-run `java.util.prefs.userRoot`
   - per-run temp/cache dirs
   - killable process groups
   - cleanup on timeout/failure

5. Define screenshots/logs as hard pass/fail artifacts:
   - screenshot exists and is non-empty
   - `alice.log` exists
   - manifest records command, environment, cwd, PIDs, exit status, dependency versions
   - capture `wmctrl -lx` or equivalent window list when available

6. First slice should be:
   - package Alice
   - start Xvfb
   - launch `africa.a3p`
   - wait up to 60 seconds
   - capture screenshot/log/window/process evidence
   - judge only that Alice visibly launched without fatal DISPLAY/OpenGL/crash failure

## No-go risks

- No Xvfb/X tooling installed.
- JavaFX without `DISPLAY`.
- Direct Java without JavaFX module path.
- JOGL/OpenGL without Mesa/GLX/software rendering.
- Offline Maven without cached dependencies.
- First-run/crash dialogs blocking visual success.
- Hardcoded `:99` under parallel runs or stale Xvfb.

## Decision

Implementable only after the detailed launch contract is promoted into Milestone 0.
