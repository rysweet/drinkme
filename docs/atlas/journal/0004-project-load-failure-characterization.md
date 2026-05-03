# Journal 0004: project-load IO failure characterization

## Loop 3 target

The code-atlas bug hunt flagged `FileProjectLoader.handleLoadException()` as empty. Initial instinct was to treat that as silent failure and make it show a dialog.

Crusty review caught the important context: the empty hook was introduced with the backup recovery system. `AbstractFileProjectLoader.load()` returns `null` after an `IOException`, then `ProjectApplication.projectLoaded()` routes the null project to `handleProjectLoadError()`, which drives backup-recovery dialogs and fallback loading.

## Decision

Do not add a dialog inside `FileProjectLoader.handleLoadException()`.

Why:

- Adding a dialog there causes duplicate user-facing dialogs before the backup recovery flow has a chance to run.
- `ProjectApplication.handleProjectLoadError()` already owns the recovery UX for corrupt existing project files.
- The right slice is to characterize and document the delegation contract, not to change behavior.

## Alice implementation commit

Commit in `alice3-modernization`:

- `d278d6f9a7 Characterize project load IO failure hook`

Changes:

- Added an explicit JUnit test dependency to `core/ide/pom.xml`.
- Added `core/ide/src/test/java/org/alice/ide/uricontent/FileProjectLoaderTest.java`.
- Characterized that an existing corrupt `.a3p` file:
  - causes `AbstractFileProjectLoader.load()` to return `null`;
  - delegates the `IOException` to `handleLoadException()`;
  - does not require Swing dialog interaction in the unit test.
- Added a short comment in `FileProjectLoader.handleLoadException()` documenting that `ProjectApplication` handles null project loads with backup recovery UI.

## Review and validation

Crusty review loop:

1. Rejected the first version because it added an error dialog and would cause double-dialog behavior with backup recovery.
2. Rejected the second version until the IDE module declared its JUnit dependency explicitly.
3. Approved the final characterization-only version.

Local validation passed:

```bash
mvn -DincludeSims=false -Dinstall4j.skip -pl core/ide -am test
mvn -DincludeSims=false -Dinstall4j.skip clean test
```

Standalone CI passed for commit `d278d6f9a7`:

- Alice Checkstyle CI: success, run `25270074065`
- Alice Test CI: success, run `25270074067`

## Next useful slices

1. Add headless characterization around `ProjectApplication.handleProjectLoadError()` using a small extracted decision object if needed.
2. Add tiny `.a3p` fixture migration/load round-trip tests with explicit provenance and no Sims/nonfree assets.
3. Replace the commented `ModelExportTest` with a minimal no-Sims resource/export characterization.
4. Add NetBeans generated-project characterization tests for the Alice-to-Java bridge.
