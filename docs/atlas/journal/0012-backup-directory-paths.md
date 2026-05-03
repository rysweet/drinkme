# Journal 0012: backup directory path characterization

## Loop 11 target

The next project-persistence seam was `ProjectFileUtilities.backupDirectory(...)`. Atlas review had flagged nearby backup-directory code as worth checking, especially around directory creation and backup-file path handling.

The initial suspicion around `copyDefaultBackupDirectory()` being a file-vs-directory bug was downgraded: the public path calls `backupDirectory(file, false)` first, which creates the named `.bak` directory before `createNewFile()` runs. The line is still ugly, but not the sharpest confirmed failure.

The sharper edge was parentless backup files. `backupDirectory(saved, true)` called `saved.getParentFile().toPath()` unconditionally, which can throw before callers get the existing `null`-means-skip behavior used elsewhere in the backup flow.

## Alice implementation commit

Commit in `alice3-modernization`:

- `0ddc38dbbb Characterize backup directory paths`

Changes:

- Added `core/ide/src/test/java/org/alice/ide/ProjectFileUtilitiesTest.java`.
- Characterized:
  - saved `.a3p` files use sibling `<base>.bak` directories;
  - non-project files use `<full-name>.bak`;
  - backup files use their parent directory;
  - parentless backup files return `null`.
- Hardened `ProjectFileUtilities.backupDirectory(saved, true)` to return `null` when a backup file has no parent instead of throwing `NullPointerException`.

## Review and validation

Crusty review:

- Approved the slice as a small path-policy hardening, not a broad persistence rewrite.
- Confirmed the tests use temp files and avoid UI, `StageIDE`, renderer, Sims, and asset dependencies.
- Confirmed the production change preserves the surrounding backup flow: callers already treat a `null` backup directory as “do not write a backup.”
- Confirmed `copyDefaultBackupDirectory()` should remain on the watch list, but direct testing needs a cleaner seam than constructing a full `StageIDE`.

Local validation passed:

```bash
mvn -DincludeSims=false -Dinstall4j.skip -pl core/ide -am test
mvn -DincludeSims=false -Dinstall4j.skip clean test
mvn checkstyle:check -Dcheckstyle.config.location=checkstyle.xml
```

Standalone CI passed for commit `0ddc38dbbb`:

- Alice Test CI: success, run `25271410262`
- Alice Checkstyle CI: success, run `25271410266`

## Next useful slices

1. Characterize NetBeans project-template archive contents and metadata renaming.
2. Add a narrow seam around `copyDefaultBackupDirectory()` only if it can be tested without launching `StageIDE`.
3. Continue `ModelResourceInfo` edge characterization for explicit child false overrides and missing texture names.
4. Add fixture-backed Alice-to-Java source-generation checks once safe fixture provenance is clear.
