# Journal 0028: NetBeans local declaration source generation

## Loop 27 target

Add one richer generated-code characterization after the comment-only user-method foothold: a synthetic user method that declares a final local `String` initialized from a string literal.

This keeps the test headless and provenance-clean while forcing the generator through a real statement plus expression path: `LocalDeclarationStatement`, `UserLocal`, and `StringLiteral`.

## Alice implementation commit

Commit in `alice3-modernization`:

- `b77acb6bf6 Characterize generated local declarations`

Changes:

- Added `generatedSyntheticUserMethodLocalDeclarationSourceCompiles()` to `ProjectCodeGeneratorTest`.
- Built a minimal synthetic Alice program containing:
  - static `main(String[] args)`, still required by `AliceJavaFXLauncher`;
  - non-static `sayHello()` containing `final String greeting="hello alice";`.
- Verified the generated `Program.java` includes the user method and local declaration.
- Compiled the generated program and launcher with the JDK compiler using the test classpath and `-proc:none`.

## Review and validation

Crusty verdict:

- Better than the comment-only slice: this exercises statement generation, local variable typing, final-ness, and escaped string literal output.
- Still modest: it does not prove story API calls, scene fields, parameters, control flow, or runtime behavior.
- Keep the pressure on characterization before refactoring; source-generator internals still do not deserve cleanup until more generated constructs are locked down.

Local validation passed:

```bash
mvn -DincludeSims=false -Dinstall4j.skip -pl netbeans -am test
mvn -DincludeSims=false -Dinstall4j.skip clean test
mvn checkstyle:check -Dcheckstyle.config.location=checkstyle.xml
```

Standalone CI passed for commit `b77acb6bf6`:

- Alice Checkstyle CI: success, run `25273609568`
- Alice Test CI: success, run `25273609558`

## Next useful slices

1. Add generated-source coverage for user-method parameters or a simple method invocation.
2. Map the exported Ant/NetBeans project build path and compile it outside the unit-test helper.
3. Continue project/resource IO characterization outside the NetBeans export seam.
