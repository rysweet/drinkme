# Journal 0029: NetBeans user parameter source generation

## Loop 28 target

Continue widening generated-source characterization by proving that a user method parameter is emitted in generated Java and can be referenced from a generated statement.

The slice builds directly on the local-declaration foothold: `remember(String message)` assigns the parameter into a final local variable. This exercises `UserParameter` plus `ParameterAccess` without introducing story runtime, scenes, or UI dependencies.

## Alice implementation commit

Commit in `alice3-modernization`:

- `cbdbff9b36 Characterize generated method parameters`

Changes:

- Added `generatedSyntheticUserMethodParameterSourceCompiles()` to `ProjectCodeGeneratorTest`.
- Built a minimal synthetic Alice program containing:
  - static `main(String[] args)`, still required by `AliceJavaFXLauncher`;
  - non-static `remember(String message)`;
  - final local declaration `copy` initialized from `message`.
- Verified the generated `Program.java` includes the parameterized method and parameter-backed local declaration.
- Compiled the generated program and launcher with the JDK compiler using the test classpath and `-proc:none`.

## Review and validation

Crusty verdict:

- Useful incremental coverage: this now exercises method parameter emission and identifier use, not just literals.
- Still small and synthetic. It does not prove multi-parameter ordering, callbacks, control flow, story API invocation, or runtime execution.
- Keep accumulating these seams until the generator has enough behavioral net to justify cleanup.

Local validation passed:

```bash
mvn -DincludeSims=false -Dinstall4j.skip -pl netbeans -am test
mvn -DincludeSims=false -Dinstall4j.skip clean test
mvn checkstyle:check -Dcheckstyle.config.location=checkstyle.xml
```

Standalone CI passed for commit `cbdbff9b36`:

- Alice Checkstyle CI: success, run `25273733470`
- Alice Test CI: success, run `25273733465`

## Next useful slices

1. Add generated-source coverage for a method invocation, ideally a user-method call before story API calls.
2. Add simple control-flow characterization if the AST constructors stay headless-friendly.
3. Map the exported Ant/NetBeans project build path outside the unit-test compiler helper.
