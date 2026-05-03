# 0050 - Project export artifact

## Slice

Added a headless smoke test for the user-visible player export artifact created through `ProjectFileUtilities.exportCopyOfProjectTo`.

## Source change

- Repo: `rysweet/alice3-modernization`
- Branch: `develop`
- Commit: `fa0054eb9d Characterize project export artifact`
- Files:
  - `core/ide/src/main/java/org/alice/ide/ProjectFileUtilities.java`
  - `core/ide/src/test/java/org/alice/ide/ProjectFileUtilitiesTest.java`

The production change is a small package-private seam:

- `getForcedUpToDateProject()`
- `getUpToDateProject()`
- `createThumbnail()`

The default implementation still delegates to `ProjectApplication`. The test overrides only the project and thumbnail providers so it can exercise export without constructing the full IDE frame.

## Test behavior

The new test:

1. Creates a synthetic `Project` with `Program extends SProgram`.
2. Supplies a deterministic 1x1 thumbnail.
3. Calls `ProjectFileUtilities.exportCopyOfProjectTo(...)`.
4. Opens the resulting `.a3p` as a zip archive.
5. Verifies entries:
   - `version.txt`
   - `manifest.json`
   - `thumbnail.png`
   - `src/Program.twe`
6. Verifies manifest text includes:
   - `"name":"Program"`
   - `"icon":"thumbnail.png"`

## Findings

- Player export uses the JSON/Tweedle writer path and emits `src/Program.twe`, not the older XML project entry shape.
- `exportCopyOfProjectTo` passes thumbnail data sources only; the player writer creates the export manifest itself.
- The manifest writer emits compact JSON without spaces. The test locks the current compact form only for two targeted metadata strings.
- `ProjectFileUtilities` remains under the 500-line target at 286 lines; `ProjectFileUtilitiesTest` is 105 lines.

## Validation

Local gates:

```bash
mvn -DincludeSims=false -Dinstall4j.skip -pl core/ide -am test -Dtest=ProjectFileUtilitiesTest -Dsurefire.failIfNoSpecifiedTests=false -DfailIfNoTests=false
mvn -DincludeSims=false -Dinstall4j.skip clean test
mvn checkstyle:check -Dcheckstyle.config.location=checkstyle.xml
mvn -DincludeSims=false -Dinstall4j.skip -pl netbeans -am package -DskipTests
```

All local gates passed before push.

CI for `fa0054eb9d` passed:

- Alice Test CI: `25284181445`
- Alice Checkstyle CI: `25284181422`
- Alice NetBeans Package CI: `25284181420`

## Crusty proxy note

This finally protects a real exported artifact shape. Still do not pretend it is a full user journey. It uses a synthetic project and thumbnail. It does not launch StageIDE, click export, include real gallery assets, or execute the exported world.

## Next seam

Project IO save/reload with resource and manifest survival is now the next adjacent data-loss seam, unless a new crusty/QA/code-atlas pass reprioritizes.
