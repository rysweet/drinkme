# 0053 - Project save/export snapshots

## Slice

Added headless `ProjectFileUtilities` characterization for save/export snapshot source selection and default-backup migration.

## Source change

- Repo: `rysweet/alice3-modernization`
- Branch: `develop`
- Commit: `5cbfc03f0d Characterize project save export snapshots`
- File: `core/ide/src/test/java/org/alice/ide/ProjectFileUtilitiesTest.java`

No production code changed in this slice.

## Test behavior

The new tests cover three user-visible data-loss seams:

1. `exportCopyOfProjectTo(...)` uses `getForcedUpToDateProject()` and writes the forced snapshot into the player archive.
2. `saveCopyOfProjectTo(...)` uses `getUpToDateProject()` and writes a readable editor archive from that snapshot.
3. `copyDefaultBackupDirectory(...)` moves `auto*.a3p` files from `.defaultbak` into the saved project's named `.bak` directory while leaving non-auto and non-project files in place.

## Why this slice

Crusty recommended pinning the save/export source-selection split before any IO refactor. Code-atlas pointed at the default-backup save-as path as a likely data-loss seam. This slice covers both without constructing the full Swing `ProjectApplication` stack.

## Findings

- Player export and editor save-copy intentionally use different snapshot providers.
- Default-backup migration moves only auto project backups, not saved backups or non-project files.
- The test remains headless and synthetic; it does not prove the full `ProjectApplication.saveProjectTo(...)` orchestration branch.
- `ProjectFileUtilitiesTest` remains under the 500-line target at 247 lines.

## Validation

Local gates:

```bash
mvn -DincludeSims=false -Dinstall4j.skip -pl core/ide -am test -Dtest=ProjectFileUtilitiesTest -Dsurefire.failIfNoSpecifiedTests=false -DfailIfNoTests=false
mvn -DincludeSims=false -Dinstall4j.skip clean test
mvn checkstyle:check -Dcheckstyle.config.location=checkstyle.xml
mvn -DincludeSims=false -Dinstall4j.skip -pl netbeans -am package -DskipTests
```

All local gates passed before push.

CI for `5cbfc03f0d` passed:

- Alice Test CI: `25284915572`
- Alice Checkstyle CI: `25284915576`
- Alice NetBeans Package CI: `25284915581`

## Crusty proxy note

This is useful, but still not the whole save-as story. It proves the lower-level utility behavior. It does not prove that `ProjectApplication.saveProjectTo(...)` calls the migration branch at the right time, nor does it exercise the actual menu/action path.

## Next seam

Either add a narrow orchestration test around `ProjectApplication.saveProjectTo(...)` if a clean seam can be introduced without GUI drag, or return to generated/exported project behavior with a real scene/model API call.
