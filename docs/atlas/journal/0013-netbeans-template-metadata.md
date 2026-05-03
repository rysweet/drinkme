# Journal 0013: NetBeans project-template metadata

## Loop 12 target

The next headless Java-transition seam was the NetBeans project template used by “Java Project from Existing Alice Project.” Earlier coverage locked generated launcher source and `main.class`; this loop checked the packaged template archive and generated project metadata.

Atlas review found a real mismatch:

- `Alice3ProjectTemplateWizardIterator` rewrote `nbproject/project.xml` to the chosen project directory name;
- `nbproject/project.properties` kept `application.title = Alice3JavaApplication`;
- `dist.jar` also kept `Alice3JavaApplication.jar`.

That left exported NetBeans projects with user-visible project metadata that did not match the imported project name.

## Alice implementation commit

Commit in `alice3-modernization`:

- `16c795ac12 Fix NetBeans template project metadata`

Changes:

- Added a small `project.properties` rewrite path next to the existing `project.xml` rewrite in `Alice3ProjectTemplateWizardIterator`.
- Renamed:
  - `application.title` to the generated project name;
  - `dist.jar` to `${dist.dir}/<project-name>.jar`.
- Preserved `main.class = AliceJavaFXLauncher`.
- Added `Alice3ProjectTemplateWizardIteratorTest` covering:
  - required entries in the generated `ProjectTemplate.zip`;
  - absence of an unwanted root `ProjectTemplate/` prefix in the archive;
  - project-property renaming behavior.

## Review and validation

Crusty review:

- Approved because this protects a user-facing exported-project contract without trying to rewrite the NetBeans plugin.
- Confirmed the archive test is not just “does a file exist”; it verifies the packaged shape NetBeans will consume.
- Confirmed the property rewrite stays limited to two metadata keys and avoids changing launcher generation.

Local validation passed:

```bash
mvn -DincludeSims=false -Dinstall4j.skip -pl netbeans -am test
mvn -DincludeSims=false -Dinstall4j.skip clean test
mvn checkstyle:check -Dcheckstyle.config.location=checkstyle.xml
```

Standalone CI passed for commit `16c795ac12`:

- Alice Checkstyle CI: success, run `25271555980`
- Alice Test CI: success, run `25271555857`

## Next useful slices

1. Continue NetBeans export characterization with a tiny Alice project fixture only if provenance is clean.
2. Characterize `ModelResourceInfo` edge behavior for explicit child false overrides and missing texture-name manifest output.
3. Add a clean seam for `copyDefaultBackupDirectory()` if backup copying remains a priority.
4. Revisit project persistence fixtures after identifying tiny safe `.a3p` samples.
