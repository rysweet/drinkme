# 0039 - NetBeans launcher runtime handoff

## Scope

Loop 38 moved generated launcher coverage from source-shape/compile-only toward runtime behavior. The new test verifies that `AliceJavaFXLauncher.main(args)` preserves the startup arguments and hands them to `Program.main(args)`.

## Source change

- Repository: `rysweet/alice3-modernization`
- Branch: `develop`
- Commit: `57ca03ed15 Characterize generated launcher argument handoff`
- Modified test: `netbeans/src/test/java/org/alice/netbeans/project/ProjectCodeGeneratorTest.java`
- New test: `generatedLauncherPassesStartingArgsToProgramMain()`

## Test design

The test stays headless and does not start real JavaFX:

1. Generate `AliceJavaFXLauncher.java` through `ProjectCodeGenerator.generateLauncher(...)`.
2. Write a synthetic `Program` class whose `main(String[] args)` records the received args.
3. Write test-only `javafx.application.Application` and `javafx.stage.Stage` stubs.
4. Compile generated launcher, synthetic program, and stubs into an isolated class directory.
5. Load them with a `URLClassLoader` whose parent is the platform classloader, so the test stubs provide JavaFX.
6. Invoke `AliceJavaFXLauncher.main(new String[] {"alpha", "beta"})`.
7. Wait for the generated background thread and assert the same args array reaches `Program.main(...)`.

## Local validation

Ran in `/home/azureuser/src/alice3-modernization`:

```bash
mvn -DincludeSims=false -Dinstall4j.skip -pl netbeans -am test \
  -Dtest=ProjectCodeGeneratorTest \
  -Dsurefire.failIfNoSpecifiedTests=false \
  -DfailIfNoTests=false
mvn -DincludeSims=false -Dinstall4j.skip clean test
mvn checkstyle:check -Dcheckstyle.config.location=checkstyle.xml
```

Result: all local gates passed. `ProjectCodeGeneratorTest` now reports 18 tests.

## CI validation

All workflows passed for source commit `57ca03ed15e308213beec839ed31b39b9e19dc85`:

| Workflow | Run ID | Result |
| --- | ---: | --- |
| Alice Checkstyle CI | 25275286174 | success |
| Alice Test CI | 25275286178 | success |
| Alice NetBeans Package CI | 25275286173 | success |

## What this proves

- The generated launcher stores startup args before launch.
- The generated launcher calls `Program.main(startingArgs)` from `start(...)`.
- The handoff works when the launcher is invoked through its real `main(String[] args)` entry point.

## What this does not prove yet

- It does not start the real JavaFX runtime.
- It does not render a stage or execute Alice scene behavior.
- It does not prove exported Ant project execution with the packaged `Alice3Library`.

## Crusty proxy note

Good. This is not UI testing theater; it locks an actual generated-code contract without depending on a display server. Next export work should either prove standalone exported project build/execution or expand generated-source coverage to constructs students actually use.
