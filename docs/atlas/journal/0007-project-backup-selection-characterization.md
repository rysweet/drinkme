# Journal 0007: project backup selection characterization

## Loop 6 target

Loop 3 proved that corrupt `.a3p` load failures intentionally return `null` so `ProjectApplication` can drive the backup recovery flow. The next safe step was to separate one headless policy from that UI method: which backup candidate Alice should attempt next.

This is deliberately not a Swing dialog test. The dialogs, activity cancellation, and recursive `loadProject(...)` calls remain in `ProjectApplication`.

## Alice implementation commit

Commit in `alice3-modernization`:

- `ec46aee3a7 Characterize project backup selection`

Changes:

- Added package-private `org.alice.ide.ProjectBackupSelector`.
- Changed `ProjectApplication.getNextBackup(...)` to sort/filter backup files as before, then delegate the candidate selection policy to `ProjectBackupSelector`.
- Added `core/ide/src/test/java/org/alice/ide/ProjectBackupSelectorTest.java`.
- Characterized current behavior:
  - corrupted main projects use the latest non-unloadable backup without checking backup timestamps;
  - known unloadable backups are skipped;
  - recent-backup probes only choose a backup newer than the main project;
  - if the latest remaining candidate is not newer than the main project, Alice stops rather than searching older backups;
  - `LocalDateTime.MIN` is treated as a missing main-project timestamp and uses the latest candidate;
  - no remaining candidates returns `null`.

## Review and validation

Crusty review:

- Approved the narrow extraction.
- Confirmed it removes policy from a large UI class without changing the dialog/recovery choreography.
- Noted that the `LocalDateTime.MIN` identity check is a legacy quirk intentionally preserved for now, not improved under characterization work.

Local validation passed:

```bash
mvn -DincludeSims=false -Dinstall4j.skip -pl core/ide -am test
mvn -DincludeSims=false -Dinstall4j.skip clean test
mvn checkstyle:check -Dcheckstyle.config.location=checkstyle.xml
```

Standalone CI passed for commit `ec46aee3a7`:

- Alice Test CI: success, run `25270766984`
- Alice Checkstyle CI: success, run `25270767103`

## Next useful slices

1. Characterize the remaining backup recovery action decisions behind a headless result object, without showing Swing dialogs.
2. Add tiny historical `.a3p` project load/migration fixtures with explicit provenance.
3. Add NetBeans project-template archive content tests.
4. Add a minimal no-Sims model export fixture only after licensing and asset provenance are clear.
