# Journal 0021: NetBeans resource-backed source compile smoke

## Loop 20 target

Extend the generated-source compile smoke to resource-backed Alice projects. Loop 19 proved that `Program.java` and `AliceJavaFXLauncher.java` compile for a realistic synthetic program. Loop 20 adds generated `Resources.java` to the compile set.

## Alice implementation commit

Commit in `alice3-modernization`:

- `dfab918616 Compile generated resource sources`

Changes:

- Extended `ProjectCodeGeneratorTest`.
- Generates source from a synthetic Alice project containing `note.txt`.
- Compiles:
  - `Program.java`;
  - `AliceJavaFXLauncher.java`;
  - `Resources.java`.
- Uses the same JDK compiler helper introduced in Loop 19.

## Review

Crusty verdict:

- This is a useful next rung: generated resource code now has to parse and type-check, not merely exist.
- It still uses the Maven test classpath, so it is not a full exported-project build.
- It does not run the generated code or verify classpath resource loading at runtime.
- The synthetic resource is enough for this layer because the goal is code-generation compatibility, not gallery asset behavior.

## Validation

Local validation passed:

```bash
mvn -DincludeSims=false -Dinstall4j.skip -pl netbeans -am test
mvn -DincludeSims=false -Dinstall4j.skip clean test
mvn checkstyle:check -Dcheckstyle.config.location=checkstyle.xml
```

Standalone CI passed for commit `dfab918616`:

- Alice Checkstyle CI: success, run `25272595234`
- Alice Test CI: success, run `25272595237`

## Limits

- The generated Java project is not built as a separate NetBeans/Ant project yet.
- The generated launcher is not executed.
- Runtime resource lookup from generated classes is not tested.
- Formatting still uses the headless seam and is not validated in this unit test.

## Next useful slices

1. Add a synthetic user method or scene method so generated source contains a non-empty body.
2. Map and test the standalone exported project classpath/build.
3. Add runtime resource-loading checks if they can be done without invoking JavaFX windows.
