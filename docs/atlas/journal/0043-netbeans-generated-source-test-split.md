# 0043 - NetBeans generated-source test split

## Scope

Loop 42 addressed test-suite maintainability. `ProjectCodeGeneratorTest` had grown to 788 lines while accumulating generated-source characterization. That violated the modernization goal of keeping classes under 500 lines.

## Source change

- Repository: `rysweet/alice3-modernization`
- Branch: `develop`
- Commit: `643467e751 Split generated source export tests`
- Added: `netbeans/src/test/java/org/alice/netbeans/project/ProjectCodeGeneratorGeneratedSourceTest.java`
- Modified: `netbeans/src/test/java/org/alice/netbeans/project/ProjectCodeGeneratorTest.java`

## What changed

Moved generated user-method/control-flow export tests into a focused class:

- non-empty user method;
- local declaration;
- method parameter access;
- user-method invocation;
- invocation with argument;
- conditional;
- count loop;
- while loop;
- foreach-array loop;
- foreach item access.

Line counts after split:

| File | Lines |
| --- | ---: |
| `ProjectCodeGeneratorTest.java` | 430 |
| `ProjectCodeGeneratorGeneratedSourceTest.java` | 399 |

## Local validation

Ran in `/home/azureuser/src/alice3-modernization`:

```bash
mvn -DincludeSims=false -Dinstall4j.skip -pl netbeans -am test \
  -Dtest=ProjectCodeGeneratorTest,ProjectCodeGeneratorGeneratedSourceTest \
  -Dsurefire.failIfNoSpecifiedTests=false \
  -DfailIfNoTests=false
mvn -DincludeSims=false -Dinstall4j.skip clean test
mvn checkstyle:check -Dcheckstyle.config.location=checkstyle.xml
```

Result: all local gates passed.

## CI validation

All workflows passed for source commit `643467e75151136616211e92c72cd7cf7eab3402`:

| Workflow | Run ID | Result |
| --- | ---: | --- |
| Alice NetBeans Package CI | 25282370657 | success |
| Alice Test CI | 25282370656 | success |
| Alice Checkstyle CI | 25282370662 | success |

## Crusty proxy note

This is the kind of refactor that is allowed before broad production refactoring: narrow, protected, and measurable. It reduced a test class below the stated size target without changing production behavior. Do more of this when the safety net itself starts becoming mud.

## QA note

This was not outside-in user testing. It was maintainability work on the characterization suite. The next testing lane should add user-observable scenarios around exported project/package behavior rather than only more AST-shaped compile tests.

