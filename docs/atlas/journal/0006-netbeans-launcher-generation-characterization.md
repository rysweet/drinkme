# Journal 0006: NetBeans launcher generation characterization

## Loop 5 target

The next atlas item was the Alice-to-Java bridge in the NetBeans plugin. This is part of Alice's teaching story: students can move from Alice projects toward Java source.

The safe first slice was not a full NetBeans UI or generated-project journey. That would need project fixtures and more runtime setup. The narrow seam was the generated `AliceJavaFXLauncher.java` file and the project template's `main.class` setting.

## Alice implementation commit

Commit in `alice3-modernization`:

- `245f910b9e Characterize NetBeans launcher generation`

Changes:

- Added an explicit JUnit test dependency to `netbeans/pom.xml`.
- Added `netbeans/src/test/java/org/alice/netbeans/project/ProjectCodeGeneratorTest.java`.
- Made `ProjectCodeGenerator.generateLauncher(File)` package-visible so the package-level test exercises the actual launcher write path instead of only inspecting private constants.
- Characterized that:
  - the generated file is `AliceJavaFXLauncher.java`;
  - the generated class name is `AliceJavaFXLauncher`;
  - `ProjectTemplate/nbproject/project.properties` uses the same `main.class`;
  - the launcher extends `javafx.application.Application`;
  - the launcher passes startup arguments through `Program.main(startingArgs)`;
  - the launcher enters JavaFX via `launch(args)`.

## Review and validation

Crusty review:

- Rejected the first version as too constant-focused.
- Approved the revised version because it exercises the actual generator write path and still avoids a broad NetBeans runtime test.
- Noted that this is a toe-hold, not a complete Alice-to-Java characterization.

Local validation passed:

```bash
mvn -DincludeSims=false -Dinstall4j.skip -pl netbeans -am test
mvn -DincludeSims=false -Dinstall4j.skip clean test
mvn checkstyle:check -Dcheckstyle.config.location=checkstyle.xml
```

Standalone CI passed for commit `245f910b9e`:

- Alice Test CI: success, run `25270530245`
- Alice Checkstyle CI: success, run `25270530251`

## Next useful slices

1. Add a minimal generated-source test from a tiny no-Sims Alice project fixture once fixture provenance is explicit.
2. Characterize project template archive contents without requiring a full NetBeans IDE launch.
3. Characterize backup recovery decision logic in `ProjectApplication` behind a headless decision object.
4. Add a minimal no-Sims model export fixture only after licensing and asset provenance are clear.
