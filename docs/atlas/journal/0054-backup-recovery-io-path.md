# 0054 - Backup recovery IO path

## Slice

Added a headless recovery-path characterization that connects real corrupt files, backup selection, failure planning, and backup project loading.

## Source change

- Repo: `rysweet/alice3-modernization`
- Branch: `develop`
- Commit: `bf20204906 Characterize backup recovery IO path`
- File: `core/ide/src/test/java/org/alice/ide/ProjectBackupRecoveryIoTest.java`

No production code changed in this slice.

## Test behavior

The new test:

1. Creates a corrupt main `world.a3p`.
2. Creates a sibling `world.bak` directory.
3. Adds a corrupt newest backup file.
4. Writes a valid older backup project archive with a test resource.
5. Verifies the corrupt main file returns `null` through `FileProjectLoader`.
6. Uses `ProjectBackupSelector` to skip the known-unloadable newest backup.
7. Uses `ProjectLoadFailurePlan` to choose `PROMPT_LOAD_BACKUP`.
8. Loads the selected backup through `FileProjectLoader`.
9. Verifies the recovered project name, resource class, UUID, original file name, content type, and bytes survive.

## Why this slice

QA and crusty both pushed toward the backup recovery journey. Direct `ProjectApplication` tests are still brittle because construction builds a large IDE/Swing frame, so this slice exercises the highest-value non-GUI boundary: real files, actual loader behavior, selector decision, failure plan, and resource fidelity.

## Findings

- Corrupt main project files are loadable enough to return `null` without crashing the test path.
- For a corrupted main project, backup selection does not compare backup timestamps; it skips known-unloadable backup names and selects the next candidate.
- A selected backup archive written through `IoUtilities.writeProject(...)` remains readable through `FileProjectLoader`.
- `ProjectBackupRecoveryIoTest` is 102 lines, well under the 500-line target.

## Validation

Local gates:

```bash
mvn -DincludeSims=false -Dinstall4j.skip -pl core/ide -am test -Dtest=ProjectBackupRecoveryIoTest -Dsurefire.failIfNoSpecifiedTests=false -DfailIfNoTests=false
mvn -DincludeSims=false -Dinstall4j.skip clean test
mvn checkstyle:check -Dcheckstyle.config.location=checkstyle.xml
mvn -DincludeSims=false -Dinstall4j.skip -pl netbeans -am package -DskipTests
```

All local gates passed before push.

CI for `bf20204906` passed:

- Alice Test CI: `25285183639`
- Alice Checkstyle CI: `25285183637`
- Alice NetBeans Package CI: `25285183650`

## Crusty proxy note

This is better than another pure decision-table test. It still does not instantiate `ProjectApplication`, click dialogs, or prove the menu/action journey. That remains risky work and should only be attempted through a narrow seam, not by dragging the whole IDE into a unit test.

## Next seam

Either extract and test the remaining `ProjectApplication` recovery orchestration as a narrow package-private collaborator, or move to the next user-visible seam: generated/exported Java behavior with a real scene/model API call.
