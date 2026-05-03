# 0046 - NetBeans named foreach generation

## Scope

Loop 45 followed the generated-source readability debt exposed by earlier foreach tests. Prior characterization showed helper-created foreach loops with unnamed item locals emit `COUNT__`, and that the generated body references `COUNT__` coherently. This slice checked whether explicit item names are preserved.

## Source change

- Repository: `rysweet/alice3-modernization`
- Branch: `develop`
- Commit: `e4dd96408f Characterize named foreach generation`
- Modified:
  - `netbeans/src/test/java/org/alice/netbeans/project/ProjectCodeGeneratorGeneratedSourceTest.java`

## What changed

Added `generatedSyntheticNamedForEachLoopItemAccessSourceCompiles()`:

- builds a synthetic `copyNamedItem()` method;
- constructs a `ForEachInArrayLoop` with `new UserLocal("item", String.class, true)`;
- reads the loop item into `final String copy=item;`;
- asserts generated Java contains:
  - `for(String item : new String[]{"red", "blue"})`;
  - `final String copy=item;`;
- compiles the generated `Program.java` and `AliceJavaFXLauncher.java`.

The generated-source test class remains under the 500-line target at 434 lines.

## Validation

Local validation in `/home/azureuser/src/alice3-modernization`:

```bash
mvn -DincludeSims=false -Dinstall4j.skip -pl netbeans -am test \
  -Dtest=ProjectCodeGeneratorGeneratedSourceTest \
  -Dsurefire.failIfNoSpecifiedTests=false \
  -DfailIfNoTests=false
mvn -DincludeSims=false -Dinstall4j.skip clean test
mvn checkstyle:check -Dcheckstyle.config.location=checkstyle.xml
```

Result: all local gates passed.

CI validation for source commit `e4dd96408f7465a2c4b9c4e07100fb1ab378b4d1`:

| Workflow | Run ID | Result |
| --- | ---: | --- |
| Alice Test CI | 25283083628 | success |
| Alice Checkstyle CI | 25283083616 | success |
| Alice NetBeans Package CI | 25283083619 | success |

## Crusty proxy note

Good, but don't confuse this with a fix. The ugly `COUNT__` path is still current behavior for unnamed helper-created loop items. This slice narrows the problem: explicit item names are preserved, so the debt is in unnamed/default naming, not all foreach generation.

## QA note

This is still generated-source characterization, not a user journey. It is useful because it protects a teaching-facing output: students and instructors reading exported Java should see readable names when Alice has an explicit item local.

