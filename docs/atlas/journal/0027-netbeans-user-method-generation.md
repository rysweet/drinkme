# Journal 0027: NetBeans user method source generation

## Loop 26 target

Move the NetBeans generated-source characterization beyond empty synthetic program scaffolding by proving that a non-empty user method body is emitted into Java source and still compiles with the generated launcher.

The test remains deliberately small: it uses a synthetic `sayHello()` method with a comment body rather than pulling in StageIDE scenes, story API calls, or rendering-adjacent dependencies.

## Alice implementation commit

Commit in `alice3-modernization`:

- `c0c6d4175b Characterize generated user method source`

Changes:

- Added `generatedSyntheticUserMethodSourceCompiles()` to `ProjectCodeGeneratorTest`.
- Built a minimal synthetic Alice program containing:
  - static `main(String[] args)`, still required by `AliceJavaFXLauncher`;
  - non-static `sayHello()` with a `Comment("hello alice")` body.
- Generated `Program.java` and `AliceJavaFXLauncher.java` from the synthetic `.a3p`.
- Verified generated source contains the expected comment text.
- Compiled the generated program and launcher with the JDK compiler using the test classpath and `-proc:none`.

## Review and validation

Crusty verdict:

- Useful foothold: it proves the source generator is traversing method bodies, not just writing class shells.
- Do not oversell it. A comment statement is the lowest-risk non-empty body; it does not characterize story API calls, scene setup, events, parameters, control flow, or launcher runtime behavior.
- Keep the next slice focused on one richer generated construct rather than refactoring generator internals prematurely.

Local validation passed:

```bash
mvn -DincludeSims=false -Dinstall4j.skip -pl netbeans -am test
mvn -DincludeSims=false -Dinstall4j.skip clean test
mvn checkstyle:check -Dcheckstyle.config.location=checkstyle.xml
```

Standalone CI passed for commit `c0c6d4175b`:

- Alice Checkstyle CI: success, run `25273424710`
- Alice Test CI: success, run `25273424715`

## Next useful slices

1. Add generated-source coverage for a simple real statement/expression beyond comments.
2. Map and smoke-test the standalone exported Ant project build path.
3. Add launcher execution coverage once generated classpath and headless JavaFX constraints are understood.
