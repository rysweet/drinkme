# 0049 - Story API generated source

## Slice

Added the first generated-source compile smoke for a real Alice story API call.

## Source change

- Repo: `rysweet/alice3-modernization`
- Branch: `develop`
- Commit: `b48ab476ff Characterize story API generated source`
- File: `netbeans/src/test/java/org/alice/netbeans/project/ProjectCodeGeneratorStoryApiGeneratedSourceTest.java`

The new focused test class builds a synthetic `Program` type with a `configureStory()` method that invokes:

```java
this.setSimulationSpeedFactor(1.5);
```

The method is constructed through the AST using `AstUtilities.lookupMethod(SProgram.class, "setSimulationSpeedFactor", Number.class)` and a `DoubleLiteral(1.5)`. The test generates `Program.java`, asserts the expected source text, and compiles `Program.java` plus `AliceJavaFXLauncher.java` with the existing JDK compiler harness.

## Why this slice

The previous parallel lanes converged on two near-term needs:

- Crusty wanted fewer toy AST snippets and more export/user-artifact proof.
- Code-atlas identified story API method emission as the next generated-source gap, but warned not to bloat the 481-line generated-source test class.

Loop 48 handled the artifact-shaped project smoke. This loop handles the story API generated-source gap in a new 128-line class.

## Findings

- A generated `Program extends SProgram` can emit and compile a direct call to an actual inherited story API method.
- `Number` parameters are handled correctly for this basic `DoubleLiteral` case.
- The new class keeps test organization healthier than adding more cases to `ProjectCodeGeneratorGeneratedSourceTest`.

## Validation

Local gates:

```bash
mvn -DincludeSims=false -Dinstall4j.skip -pl netbeans -am test -Dtest=ProjectCodeGeneratorStoryApiGeneratedSourceTest -Dsurefire.failIfNoSpecifiedTests=false -DfailIfNoTests=false
mvn -DincludeSims=false -Dinstall4j.skip clean test
mvn checkstyle:check -Dcheckstyle.config.location=checkstyle.xml
mvn -DincludeSims=false -Dinstall4j.skip -pl netbeans -am package -DskipTests
```

All local gates passed before push.

CI for `b48ab476ff` passed:

- Alice Test CI: `25283917095`
- Alice Checkstyle CI: `25283917094`
- Alice NetBeans Package CI: `25283917103`

## Crusty proxy note

This is a toe in the water, not a real story coverage suite. It proves one inherited `SProgram` method call. It does not cover scene/model calls, events, resources, rendering, or actual story execution.

## Next seam

Either move outward to project IO save/export artifact behavior, as QA suggested, or add one scene/model story API call only after building the minimal fixture needed to avoid more synthetic nonsense.
