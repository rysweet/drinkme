# 0048 - Template project export smoke

## Slice

Added a project-shaped NetBeans export smoke so generated Alice Java is tested inside the packaged project template, not just a loose `src` directory.

## Source change

- Repo: `rysweet/alice3-modernization`
- Branch: `develop`
- Commit: `a9ecf4bd56 Add template project export smoke`
- File: `netbeans/src/test/java/org/alice/netbeans/project/ProjectCodeGeneratorStandaloneProjectTest.java`

The new test:

1. Writes a tiny synthetic `.a3p`.
2. Extracts `target/classes/org/alice/netbeans/ProjectTemplate.zip` into a temporary project directory.
3. Generates `Program.java` and `AliceJavaFXLauncher.java` into the template `src` directory.
4. Writes test-only JavaFX stubs.
5. Loads `nbproject/project.properties` and asserts:
   - `src.dir = src`
   - `main.class = AliceJavaFXLauncher`
   - `javac.classpath = ${libs.Alice3Library.classpath}`
6. Compiles all project sources into `build/classes`.
7. Verifies `Program.class` and `AliceJavaFXLauncher.class` exist.

## Parallel lane rationale

- **Crusty proxy:** warned that the work was drifting toward toy AST coverage and recommended a more artifact-shaped exported project/classpath smoke before more snippets.
- **QA lane:** independently recommended a user-observable export artifact smoke.
- **Code-atlas lane:** recommended story API call generation next, but also noted the existing generated-source test class is already 481 lines and should not be bloated.

This slice follows crusty and QA first while keeping the atlas recommendation as the next generated-source target in a new focused test class.

## Findings

- The packaged project template can be extracted in test and combined with generated Alice Java sources.
- The template still declares `AliceJavaFXLauncher` as `main.class` and uses `${libs.Alice3Library.classpath}` as the compile classpath contract.
- The generated template-shaped project compiles under a JDK compiler when the test classpath stands in for the NetBeans `Alice3Library` and JavaFX is stubbed.
- This is a better artifact smoke than a loose source directory, but it is still not a real Ant/NetBeans build.
- `ProjectCodeGeneratorStandaloneProjectTest` remains under the 500-line target at 248 lines.

## Validation

Local gates:

```bash
mvn -DincludeSims=false -Dinstall4j.skip -pl netbeans -am test -Dtest=ProjectCodeGeneratorStandaloneProjectTest -Dsurefire.failIfNoSpecifiedTests=false -DfailIfNoTests=false
mvn -DincludeSims=false -Dinstall4j.skip clean test
mvn checkstyle:check -Dcheckstyle.config.location=checkstyle.xml
mvn -DincludeSims=false -Dinstall4j.skip -pl netbeans -am package -DskipTests
```

All local gates passed before push.

CI for `a9ecf4bd56` passed:

- Alice Test CI: `25283669456`
- Alice Checkstyle CI: `25283669460`
- Alice NetBeans Package CI: `25283669454`

## Crusty proxy note

Do not oversell this. It proves the template-shaped source tree compiles with a surrogate classpath. It does not prove Ant, NetBeans project loading, a populated `Alice3Library`, or real JavaFX execution.

## Next seam

The next generated-source slice should be a new focused class for one realistic story API call compile smoke, not another addition to the 481-line `ProjectCodeGeneratorGeneratedSourceTest`.
