# Journal 0008: project-load failure plan characterization

## Audit input

After Loop 6, a quality-audit pass looked for the next useful modernization seam without opening upstream issues or using any upstream issue database.

Validated candidates included:

- continuing the `ProjectApplication` backup recovery split;
- `FileProjectLoader` VR-save-path behavior;
- `ModelResourceInfo` subresource precedence and manifest de-duplication;
- NetBeans template/codegen resource handling;
- future `ProjectMigrationManager` table extraction.

The selected slice was the remaining headless part of project-load failure recovery: choosing which dialog/load branch to run after a project or backup fails to load. This directly follows the previous backup selector extraction and avoids Swing UI tests.

## Alice implementation commit

Commit in `alice3-modernization`:

- `cd48511929 Characterize project load failure plan`

Changes:

- Added package-private `org.alice.ide.ProjectLoadFailurePlan`.
- Changed `ProjectApplication.handleProjectLoadError(...)` to compute a plan and then execute the same dialog/load side effects as before.
- Added `core/ide/src/test/java/org/alice/ide/ProjectLoadFailurePlanTest.java`.
- Characterized current behavior:
  - manually loaded corrupt backup shows the backup-load error and ignores any available next backup;
  - corrupt main project with a backup prompts to load that backup;
  - corrupt backup during recovery prompts to load the next backup and passes the failed backup name;
  - corrupt default/unsaved project with no more backups shows the unsaved-backups error;
  - corrupt saved project with no more backups shows the project-and-all-backups error;
  - failed recent-backup probe prompts to load the main project.

## Review and validation

Crusty review:

- Approved the extraction as a branch table, not a redesign.
- Confirmed dialogs, activity cancellation, and recursive `loadProject(...)` calls remain in `ProjectApplication`.
- Confirmed this reduces conditional complexity while preserving legacy behavior.

Local validation passed:

```bash
mvn -DincludeSims=false -Dinstall4j.skip -pl core/ide -am test
mvn -DincludeSims=false -Dinstall4j.skip clean test
mvn checkstyle:check -Dcheckstyle.config.location=checkstyle.xml
```

Standalone CI passed for commit `cd48511929`:

- Alice Test CI: success, run `25270925622`
- Alice Checkstyle CI: success, run `25270925633`

## Next useful slices

1. Characterize `FileProjectLoader` VR-save-path and `shouldBeSaved()` behavior with temp files.
2. Characterize `ModelResourceInfo.getSubResource(modelName, textureName)` precedence and manifest de-duplication.
3. Characterize NetBeans project-template archive contents without launching the NetBeans IDE.
4. Add tiny historical `.a3p` project load/migration fixtures only with explicit provenance.
