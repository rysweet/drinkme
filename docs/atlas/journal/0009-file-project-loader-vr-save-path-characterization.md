# Journal 0009: FileProjectLoader VR save-path characterization

## Loop 8 target

The quality-audit pass identified `FileProjectLoader` VR-save-path behavior as a small, high-value loader seam. The production logic rewrites a loaded world path from `name.a3p` to `name VR.a3p` when `makeVrReady` is true, so converted VR worlds do not overwrite the original project.

This slice used temp files only. No project fixture, gallery asset, Sims/nonfree asset, or desktop UI was needed.

## Alice implementation commit

Commit in `alice3-modernization`:

- `6dea78abd0 Characterize VR project loader save path`

Changes:

- Extended `core/ide/src/test/java/org/alice/ide/uricontent/FileProjectLoaderTest.java`.
- Characterized current behavior:
  - non-VR loader uses the original project URI;
  - non-VR existing project does not require save;
  - make-VR-ready loader uses the suffixed ` VR.a3p` URI;
  - make-VR-ready loader requires save when the VR copy does not exist;
  - make-VR-ready loader does not require save when the VR copy already exists.

## Review and validation

Crusty review:

- Approved after tightening the expected VR path helper to mirror the production suffix rule exactly.
- Confirmed the slice is characterization only and does not change loader behavior.

Local validation passed:

```bash
mvn -DincludeSims=false -Dinstall4j.skip -pl core/ide -am test
mvn -DincludeSims=false -Dinstall4j.skip clean test
mvn checkstyle:check -Dcheckstyle.config.location=checkstyle.xml
```

Standalone CI passed for commit `6dea78abd0`:

- Alice Test CI: success, run `25271052148`
- Alice Checkstyle CI: success, run `25271052144`

## Next useful slices

1. Characterize `ModelResourceInfo.getSubResource(modelName, textureName)` precedence and manifest de-duplication.
2. Characterize NetBeans project-template archive contents without launching the NetBeans IDE.
3. Add tiny historical `.a3p` project load/migration fixtures only with explicit provenance.
4. Begin a cautious `ProjectMigrationManager` extraction only after more representative migration samples are protected.
