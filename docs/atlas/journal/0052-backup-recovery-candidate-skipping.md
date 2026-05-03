# 0052 - Backup recovery candidate skipping

## Slice

Added focused backup-selection characterization for recent-backup recovery when the newest candidate is already known unloadable.

## Source change

- Repo: `rysweet/alice3-modernization`
- Branch: `develop`
- Commit: `f43e35cf2b Characterize backup recovery candidate skipping`
- File: `core/ide/src/test/java/org/alice/ide/ProjectBackupSelectorTest.java`

No production code changed in this slice.

## Test behavior

The new tests cover two adjacent cases:

1. A newer backup is marked unloadable, the next candidate is newer than the main project, and the selector chooses that next candidate.
2. A newer backup is marked unloadable, the next candidate is older than the main project, and the selector returns `null`.

This locks the current recent-backup probe policy: known bad candidates are skipped, but the replacement candidate still has to pass the freshness check unless the main project is corrupted or has no usable modified timestamp.

## Why this slice

Code-atlas flagged the backup recovery path around `ProjectBackupSelector` and `ProjectLoadFailurePlan`. Existing tests covered corrupted-main fallback, unloadable backup skipping, and recent-backup freshness separately. They did not pin the combined case where the newest recent-backup candidate is unloadable and the selector must evaluate the next candidate without accidentally accepting stale backup data.

## Findings

- The selector evaluates the first loadable candidate after skipping names in the unloadable set.
- For non-corrupt main projects with a valid modified timestamp, the freshness check still applies to that replacement candidate.
- This protects a data-loss-adjacent seam without invoking Swing dialogs or recursive project loading.
- `ProjectBackupSelectorTest` remains under the 500-line target at 130 lines.

## Validation

Local gates:

```bash
mvn -DincludeSims=false -Dinstall4j.skip -pl core/ide -am test -Dtest=ProjectBackupSelectorTest,ProjectLoadFailurePlanTest -Dsurefire.failIfNoSpecifiedTests=false -DfailIfNoTests=false
mvn -DincludeSims=false -Dinstall4j.skip clean test
mvn checkstyle:check -Dcheckstyle.config.location=checkstyle.xml
mvn -DincludeSims=false -Dinstall4j.skip -pl netbeans -am package -DskipTests
```

All local gates passed before push.

CI for `f43e35cf2b` passed:

- Alice Test CI: `25284653504`
- Alice Checkstyle CI: `25284653530`
- Alice NetBeans Package CI: `25284653514`

## Crusty proxy note

This is a useful lock on the recovery policy. It is not a user-journey test. It does not prove the dialog path, backup file copying, recursive load attempt, or save-as behavior. Those are still the next places where data loss can hide.

## Next seam

Stay on project IO/data-loss behavior: characterize backup/save-as handling with real temporary files, then add higher-level recovery journey coverage only after the headless seams are stable.
