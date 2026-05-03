# 0058 - Player export JSON resource read

## Slice

Added manifest-based reader dispatch for Alice player/export archives and a minimal JSON IO reader path for manifest-listed image/audio resources.

## Source change

- Repo: `rysweet/alice3-modernization`
- Branch: `develop`
- Commit: `c1243a39e7 Read player export resources through JSON IO`
- Files:
  - `core/story-api-migration/src/main/java/org/lgna/project/io/IoUtilities.java`
  - `core/story-api-migration/src/main/java/org/lgna/project/io/JsonProjectIo.java`
  - `core/story-api-migration/src/test/java/org/lgna/project/io/IoUtilitiesTest.java`
  - `core/ide/src/test/java/org/alice/ide/ProjectFileUtilitiesTest.java`

## Test behavior

The new and updated tests:

1. Export a synthetic project whose AST references an `ImageResource`.
2. Verify the player archive still contains `version.txt`, `manifest.json`, `src/Program.twe`, and `resources/picture.png`.
3. Reopen the player archive through `IoUtilities.readProject(...)`.
4. Verify `IoUtilities` dispatches the manifest-declared `.a3w` archive to `JsonProjectIo`.
5. Verify the manifest-listed image resource reopens with class, UUID, name, original file name, content type, and bytes intact.
6. Explicitly assert the program type is still `null` because Tweedle decoding remains unimplemented.

## Why this slice

Crusty and code-atlas both identified the reader split as the next high-value seam after Loop 57:

- editor saves use XML archives and were already readable;
- player exports use JSON/Tweedle archives;
- `IoUtilities` previously always routed reads to `XmlProjectIo`, causing player archives to fail as if they were malformed editor archives.

The implementation deliberately stops at resource restoration. A full player export read would require a real Tweedle decoder, and `org.alice.serialization.tweedle.Decoder` is still a stub.

## Findings

- The manifest's `metadata.fileType` is the correct dispatch signal for `.a3w` player archives.
- Deserializing the manifest as `ProjectManifest`, not base `Manifest`, preserves the export metadata needed by the current shape.
- `JsonProjectIo` can restore `ImageResource` and `AudioResource` payloads from manifest references using the existing resource `valueOf(String)` identity map.
- Player export program restoration remains blocked on Tweedle decoding, not on zip/manifest dispatch.

## Validation

Local gates:

```bash
mvn -DincludeSims=false -Dinstall4j.skip -pl core/story-api-migration,core/ide -am test -Dtest=IoUtilitiesTest,ProjectFileUtilitiesTest -Dsurefire.failIfNoSpecifiedTests=false -DfailIfNoTests=false
mvn -DincludeSims=false -Dinstall4j.skip clean test
mvn checkstyle:check -Dcheckstyle.config.location=checkstyle.xml
mvn -DincludeSims=false -Dinstall4j.skip -pl netbeans -am package -DskipTests
```

All local gates passed before push.

CI for `c1243a39e7` passed:

- Alice Test CI: `25286267720`
- Alice Checkstyle CI: `25286267703`
- Alice NetBeans Package CI: `25286267935`

## Crusty proxy note

This is not a full player import feature. It removes the bogus XML-reader failure and preserves exported resources through the shared IO entry point. The harder work is still the program/type reader. Do not pretend otherwise.

## Next seam

QA's next candidate remains model-resource save/open/export characterization. The adjacent IO seam is full Tweedle program-type decoding for player archives, but that is a larger feature than this loop.
