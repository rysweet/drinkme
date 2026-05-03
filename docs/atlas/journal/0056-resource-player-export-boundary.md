# 0056 - Resource player export boundary

## Slice

Added headless characterization for a resource-bearing player export through `ProjectFileUtilities.exportCopyOfProjectTo(...)`.

## Source change

- Repo: `rysweet/alice3-modernization`
- Branch: `develop`
- Commit: `e12e1b4348 Characterize resource player export boundary`
- File: `core/ide/src/test/java/org/alice/ide/ProjectFileUtilitiesTest.java`

No production code changed in this slice.

## Test behavior

The new test:

1. Creates a synthetic program that references an `ImageResource` through an AST `ResourceExpression`.
2. Exports the project through `ProjectFileUtilities.exportCopyOfProjectTo(...)`.
3. Verifies the player archive contains:
   - `version.txt`
   - `manifest.json`
   - `src/Program.twe`
   - `resources/picture.png`
4. Verifies the exported resource bytes match the original image resource.
5. Verifies the manifest references `resources/picture.png`.
6. Verifies the current editor reader path, `IoUtilities.readProject(...)`, rejects the player/Tweedle archive with `IllegalArgumentException`.

## Why this slice

Crusty and QA both pointed at export reloadability for resource-bearing projects. The actual code has two different formats: editor save-copy uses XML (`programType.xml`, `resources.xml`) and is readable by `IoUtilities.readProject(...)`; player export uses JSON/Tweedle (`manifest.json`, `src/*.twe`) and the current reader selection still routes through `XmlProjectIo`. This slice pins that boundary instead of pretending the two archive formats are interchangeable.

## Findings

- Referenced `ImageResource` values are included in the player export archive.
- Plain project-resource membership is not enough for player export; resources are discovered by crawling AST `ResourceExpression` values.
- Player exports are not currently editor-readable through `IoUtilities.readProject(...)`.
- `JsonProjectIo.reader(...)` exists but is not selected by `IoUtilities.projectReader(...)`; the code still has a TODO to read the manifest and identify file type.
- `ProjectFileUtilitiesTest` remains under the 500-line target at 297 lines.

## Validation

Local gates:

```bash
mvn -DincludeSims=false -Dinstall4j.skip -pl core/ide -am test -Dtest=ProjectFileUtilitiesTest -Dsurefire.failIfNoSpecifiedTests=false -DfailIfNoTests=false
mvn -DincludeSims=false -Dinstall4j.skip clean test
mvn checkstyle:check -Dcheckstyle.config.location=checkstyle.xml
mvn -DincludeSims=false -Dinstall4j.skip -pl netbeans -am package -DskipTests
```

All local gates passed before push.

CI for `e12e1b4348` passed:

- Alice Test CI: `25285746094`
- Alice Checkstyle CI: `25285746088`
- Alice NetBeans Package CI: `25285746095`

## Crusty proxy note

This is a useful boundary test, not a happy reload story. If product intent says exported player archives should reopen in the editor, that is currently not true. Do not “fix” it casually: the reader-selection TODO, incomplete `JsonProjectIo.reader(...)`, and player/editor format split need a deliberate compatibility decision.

## Next seam

Decide whether to keep characterizing player export format details, implement/characterize JSON reader selection, or move to QA's model-resource codegen recommendation.
