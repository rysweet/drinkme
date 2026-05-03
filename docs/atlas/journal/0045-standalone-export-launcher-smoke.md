# 0045 - Standalone-style export launcher smoke

## Scope

Loop 44 applied the QA-team outside-in lane. The goal was to move beyond AST-shaped generated-source assertions toward a user-observable exported-project smoke while staying deterministic in no-Sims CI.

## Source change

- Repository: `rysweet/alice3-modernization`
- Branch: `develop`
- Commit: `09072e5743 Add standalone export launcher smoke`
- Added:
  - `netbeans/src/test/java/org/alice/netbeans/project/ProjectCodeGeneratorStandaloneProjectTest.java`

## What changed

Added a focused 191-line NetBeans test class that:

1. creates a synthetic `.a3p` project;
2. generates Java export output into a standalone-style `src` tree;
3. writes test-only JavaFX stubs into that same source tree;
4. compiles all Java sources under `src` into `build/classes`;
5. loads generated classes through a child-first classloader for generated and JavaFX classes;
6. invokes `AliceJavaFXLauncher.main(args)`;
7. verifies the generated launcher passes the startup args to `Application.launch(args)` and invokes `start(...)`.

## Why this matters

This is closer to a user-facing export smoke than the earlier generated-source unit tests. It treats the generated project layout and launcher as the artifact under test, not just individual snippets.

It still avoids real JavaFX startup and real NetBeans/Ant execution because those are heavier and less deterministic in the current no-Sims CI environment.

## Validation

Local validation in `/home/azureuser/src/alice3-modernization`:

```bash
mvn -DincludeSims=false -Dinstall4j.skip -pl netbeans -am test \
  -Dtest=ProjectCodeGeneratorStandaloneProjectTest \
  -Dsurefire.failIfNoSpecifiedTests=false \
  -DfailIfNoTests=false
mvn -DincludeSims=false -Dinstall4j.skip clean test
mvn checkstyle:check -Dcheckstyle.config.location=checkstyle.xml
mvn -DincludeSims=false -Dinstall4j.skip -pl netbeans -am package -DskipTests
```

Result: all local gates passed.

CI validation for source commit `09072e57435c1e331318b3f9686e6f77d50eb76b`:

| Workflow | Run ID | Result |
| --- | ---: | --- |
| Alice Test CI | 25282906915 | success |
| Alice Checkstyle CI | 25282906912 | success |
| Alice NetBeans Package CI | 25282906923 | success |

## Crusty proxy note

This is useful, but don't kid yourself: it is not a real NetBeans Ant build and not a real JavaFX application launch. It proves a generated project-shaped source tree compiles and the generated launcher is invokable with controlled JavaFX stubs.

## QA note

This is the right direction for outside-in testing in a Java desktop project: executable artifact smoke first, real UI automation later when the display/runtime harness is stable enough to be worth trusting.

