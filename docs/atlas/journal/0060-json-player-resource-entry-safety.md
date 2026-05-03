# 0060 - JSON player resource entry safety

## Slice

Made JSON/player export resource zip entries duplicate-safe and path-safe.

## Source change

- Repo: `rysweet/alice3-modernization`
- Branch: `develop`
- Commit: `42b7c673b3 Make JSON player resource entries path safe`
- Files:
  - `core/story-api-migration/src/main/java/org/lgna/project/io/JsonProjectIo.java`
  - `core/story-api-migration/src/test/java/org/lgna/project/io/IoUtilitiesTest.java`

## Test behavior

The new test:

1. Creates three AST-referenced image resources:
   - two with the same original filename, `image.png`;
   - one with a path-like original filename, `../folder/picture.png`.
2. Exports the project through `IoUtilities.exportProject(...)`.
3. Verifies the archive contains:
   - `resources/image.png`;
   - `resources2/image.png`;
   - `resources/.._folder_picture.png`.
4. Verifies the unsafe path entry `resources/../folder/picture.png` is not present.
5. Reopens the player archive through `IoUtilities.readProject(...)`.
6. Verifies all three image resources preserve their byte payloads by UUID.

## Why this slice

The wide scout fan-out found that `JsonProjectIo` handled duplicate resource filenames by moving later entries into `resources2`, `resources3`, and so on, but still used raw `originalFileName` text for zip entries. That allowed path-like filenames to become nested or traversal-shaped archive paths.

This loop aligns JSON/player export with the already-characterized NetBeans resource path behavior: slash and backslash characters are flattened before zip entry creation, and duplicates remain deterministic.

## Findings

- `JsonProjectIo.generateEntryName(...)` now sanitizes `originalFileName` before composing zip entry names.
- Empty, `.`, and `..` filenames fall back through the resource display name path.
- Duplicate filenames still receive distinct resource directories.
- Existing JSON/player resource readback preserves bytes for all entries after sanitization.

## Validation

Local gates:

```bash
mvn -DincludeSims=false -Dinstall4j.skip -pl core/story-api-migration -am test -Dtest=IoUtilitiesTest -Dsurefire.failIfNoSpecifiedTests=false -DfailIfNoTests=false
mvn -DincludeSims=false -Dinstall4j.skip clean test
mvn checkstyle:check -Dcheckstyle.config.location=checkstyle.xml
mvn -DincludeSims=false -Dinstall4j.skip -pl netbeans -am package -DskipTests
```

All local gates passed before push.

CI for `42b7c673b3` passed:

- Alice Test CI: `25286788778`
- Alice Checkstyle CI: `25286788791`
- Alice NetBeans Package CI: `25286788786`

## Crusty proxy note

This is a boring fix. Good. Zip paths should not be exciting. The remaining resource work is model/dynamic resource export and full program/type readback, not more filename tricks unless new evidence appears.

## Next seam

The strongest remaining candidates are:

- JSON `.a3c` type-read behavior;
- model-resource export/read boundaries;
- `ProjectApplication` recovery orchestration seam extraction;
- minimal Tweedle decode scaffolding, but only after a small grammar/parser plan is explicit.
