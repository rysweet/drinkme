# 0051 - Project save-copy roundtrip

## Slice

Added a headless editor-save compatibility smoke for `ProjectFileUtilities.saveCopyOfProjectTo`.

## Source change

- Repo: `rysweet/alice3-modernization`
- Branch: `develop`
- Commit: `a15d6a49e3 Characterize project save copy roundtrip`
- File: `core/ide/src/test/java/org/alice/ide/ProjectFileUtilitiesTest.java`

This builds on the package-private provider seam added in Loop 50. No production code changed in this slice.

## Test behavior

The new test:

1. Creates a synthetic `Project` with `Program extends SProgram`, `WindowCamera`, and one test `Resource`.
2. Supplies a deterministic 1x1 thumbnail.
3. Calls `ProjectFileUtilities.saveCopyOfProjectTo(...)`.
4. Opens the saved `.a3p` as a zip archive.
5. Verifies entries:
   - `version.txt`
   - `manifest.json`
   - `thumbnail.png`
   - `programType.xml`
   - `resources.xml`
   - `resources/note.txt`
6. Verifies manifest text includes:
   - `"name":"Program"`
   - `"icon":"thumbnail.png"`
7. Reopens with `IoUtilities.readProject(...)`.
8. Verifies the program type, `WindowCamera`, resource class, UUID, original file name, display name, content type, and bytes survive.

## Why this slice

QA recommended save/reopen roundtrip with resources, camera, and archive shape. Crusty ranked project save/reload resource survival as the next protected slice after Loop 50. The existing lower-level `IoUtilitiesTest` already covered raw `IoUtilities.writeProject(...)`, so this slice deliberately exercises the higher-level IDE save-copy path instead of duplicating the lower-level test.

## Findings

- Editor save-copy uses the XML project archive shape (`programType.xml`, `resources.xml`, `resources/...`) plus manifest and thumbnail data sources supplied by `ProjectFileUtilities`.
- The saved editor archive remains readable through `IoUtilities.readProject(...)`.
- Synthetic resource reflection still depends on the Alice `valueOf(String)` resource contract.
- `ProjectFileUtilitiesTest` remains under the 500-line target at 170 lines.

## Validation

Local gates:

```bash
mvn -DincludeSims=false -Dinstall4j.skip -pl core/ide -am test -Dtest=ProjectFileUtilitiesTest -Dsurefire.failIfNoSpecifiedTests=false -DfailIfNoTests=false
mvn -DincludeSims=false -Dinstall4j.skip clean test
mvn checkstyle:check -Dcheckstyle.config.location=checkstyle.xml
mvn -DincludeSims=false -Dinstall4j.skip -pl netbeans -am package -DskipTests
```

All local gates passed before push.

CI for `a15d6a49e3` passed:

- Alice Test CI: `25284444032`
- Alice Checkstyle CI: `25284444024`
- Alice NetBeans Package CI: `25284444021`

## Crusty proxy note

This protects an important data-loss seam. It is still synthetic. It does not click Save in StageIDE, it does not cover real gallery resources, and it does not cover historical project fixtures.

## Next seam

The next adjacent target is backup/save-as data-loss behavior or the backup recovery branch that code-atlas flagged around `ProjectApplication.getNextBackup(...)` and `ProjectBackupSelector`.
