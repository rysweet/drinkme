# 0040 - NetBeans while-loop generation

## Scope

Loop 39 added generated-source characterization for Alice while loops in the NetBeans Java export path.

## Source change

- Repository: `rysweet/alice3-modernization`
- Branch: `develop`
- Commit: `531902f03a Characterize generated while loops`
- Modified test: `netbeans/src/test/java/org/alice/netbeans/project/ProjectCodeGeneratorTest.java`
- New test: `generatedSyntheticUserMethodWhileLoopSourceCompiles()`

## Test design

The test creates a synthetic Alice `Program` type with a user method:

```java
void spin() {
  while (true) {
    // loop body
  }
}
```

The generated source is compile-only; the loop is intentionally not executed. Assertions lock the current emitted method and `while (true)` spelling, then compile `Program.java` with `AliceJavaFXLauncher.java`.

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

Initial expected spelling `while(true)` was wrong; the generator currently emits `while (true)`. The assertion was updated to match behavior.

Result: all local gates passed. `ProjectCodeGeneratorTest` now reports 19 tests.

## CI validation

All workflows passed for source commit `531902f03a49903c8a2ade73c7650f9c5c931423`:

| Workflow | Run ID | Result |
| --- | ---: | --- |
| Alice Test CI | 25275427595 | success |
| Alice Checkstyle CI | 25275427593 | success |
| Alice NetBeans Package CI | 25275427596 | success |

## What this proves

- The Java export path emits syntactically valid while-loop source for a synthetic user method.
- The generated while-loop method compiles with the generated launcher.
- Current generator formatting uses `while (true)` for while loops.

## What this does not prove yet

- Runtime execution of while loops.
- Complex conditions or condition mutation.
- `foreach` loops and other richer Alice control-flow constructs.

## Crusty proxy note

Small, boring, and useful. Keep walking the high-value source generation branches, but do not confuse compile-only loop coverage with behavioral VM or scene execution coverage.
