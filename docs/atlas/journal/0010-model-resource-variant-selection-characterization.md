# Journal 0010: model resource variant selection characterization

## Loop 9 target

The next pure model-resource seam was `ModelResourceInfo` variant lookup and manifest de-duplication. These behaviors affect which model/texture variants Alice selects and how exported model manifests avoid duplicate structures and texture sets.

The slice used synthetic XML only. No gallery binaries, Sims/nonfree assets, renderer, or desktop UI were involved.

## Alice implementation commit

Commit in `alice3-modernization`:

- `666bb5eb1f Characterize model resource variant selection`

Changes:

- Extended `core/story-api/src/test/java/org/lgna/story/resourceutilities/ModelResourceInfoTest.java`.
- Characterized current behavior:
  - `getSubResource(modelName, textureName)` prefers exact model+texture matches before model-only fallback;
  - model-only fallback is used when the requested texture has no exact match;
  - unmatched model names return `null`;
  - `createModelManifest()` de-duplicates shared structures and texture sets while preserving separate model variants.

## Review and validation

Crusty review:

- Approved as a pure characterization slice.
- Confirmed the tests pin behavior that would be easy to break during later model exporter/resource refactors.
- Confirmed there is no asset provenance risk.

Local validation passed:

```bash
mvn -DincludeSims=false -Dinstall4j.skip -pl core/story-api -am test
mvn -DincludeSims=false -Dinstall4j.skip clean test
mvn checkstyle:check -Dcheckstyle.config.location=checkstyle.xml
```

Standalone CI passed for commit `666bb5eb1f`:

- Alice Test CI: success, run `25271161096`
- Alice Checkstyle CI: success, run `25271161107`

## Next useful slices

1. Characterize NetBeans project-template archive contents without launching the NetBeans IDE.
2. Add tiny historical `.a3p` project load/migration fixtures only with explicit provenance.
3. Add no-Sims model export coverage only after safe fixture provenance is resolved.
4. Begin a cautious `ProjectMigrationManager` extraction only after more representative migration samples are protected.
