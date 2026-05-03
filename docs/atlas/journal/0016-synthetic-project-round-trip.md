# Journal 0016: synthetic project round trip

## Loop 15 target

The next project-persistence goal was to get a fixture-safe `.a3p` read/write foothold without committing opaque or license-sensitive binary project files.

Instead of adding a checked-in fixture, this loop builds a minimal `Project` in memory, writes it to a temporary `.a3p`, and reads it back through the same `IoUtilities` APIs used by Alice project persistence.

## Alice implementation commit

Commit in `alice3-modernization`:

- `8d1b6a0657 Characterize synthetic project round trip`

Changes:

- Added `core/story-api-migration/src/test/java/org/lgna/project/io/IoUtilitiesTest.java`.
- Created a minimal `NamedUserType` named `Program` with `SProgram` as its supertype.
- Wrote a temporary `.a3p` with `IoUtilities.writeProject(...)`.
- Read it back with `IoUtilities.readProject(...)`.
- Verified:
  - program type name survives the round trip;
  - default window-camera metadata is preserved when creating a save manifest from the read project;
  - no resources are introduced;
  - the zip contains `version.txt` and `programType.xml`;
  - no `resources.xml` is written for an empty-resource project.

## Review and validation

Crusty review:

- Approved as a foothold, not a claim of full project persistence coverage.
- Confirmed it avoids binary fixtures and asset provenance problems.
- Confirmed it belongs before historical `.a3p` fixtures because it proves the test harness can exercise project IO in-memory.
- Noted that real IDE-generated project round trips, resources, thumbnails, and manifests supplied by `ProjectFileUtilities` remain future work.

Local validation passed:

```bash
mvn -DincludeSims=false -Dinstall4j.skip -pl core/story-api-migration -am test
mvn -DincludeSims=false -Dinstall4j.skip clean test
mvn checkstyle:check -Dcheckstyle.config.location=checkstyle.xml
```

Standalone CI passed for commit `8d1b6a0657`:

- Alice Checkstyle CI: success, run `25271921473`
- Alice Test CI: success, run `25271921453`

## Next useful slices

1. Extend synthetic project IO with a tiny generated resource only if the resource type can be constructed without file/assets.
2. Add `ProjectFileUtilities` manifest/thumbnail data-source characterization if it can be tested without a full `ProjectApplication`.
3. Use this synthetic `.a3p` path as groundwork for NetBeans generated-source tests.
4. Continue searching for provenance-clean historical `.a3p` samples.
