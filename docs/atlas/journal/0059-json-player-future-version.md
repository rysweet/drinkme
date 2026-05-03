# 0059 - JSON player future-version detection

## Slice

Added future-version detection for JSON/player archives by making `JsonProjectIo.checkForFutureVersion()` read `version.txt`.

## Source change

- Repo: `rysweet/alice3-modernization`
- Branch: `develop`
- Commit: `c57606b81f Report future versions for JSON player archives`
- Files:
  - `core/story-api-migration/src/main/java/org/lgna/project/io/JsonProjectIo.java`
  - `core/story-api-migration/src/test/java/org/lgna/project/io/IoUtilitiesTest.java`

## Test behavior

The new test:

1. Creates a tiny player-style archive with `manifest.json` declaring `.a3w` and `version.txt` set to `999.0.0.0`.
2. Gets the reader through the public `IoUtilities.projectReader(...)` seam.
3. Calls `checkForFutureVersion()`.
4. Verifies the future version is returned.

## Why this slice

The parallel scout lanes found that `JsonProjectIo.checkForFutureVersion()` was still a stub returning `null`, while `XmlProjectIo` already reports future `version.txt` values. That means loader warning behavior could silently miss newer Alice player/export archives even after Loop 58 added JSON reader dispatch.

This is a small compatibility fix adjacent to the new JSON reader path. It does not attempt full Tweedle program decoding.

## Findings

- `JsonProjectIo` can use the same `version.txt` convention as `XmlProjectIo`.
- The shared `ProjectReader.checkForFutureVersion()` seam is enough to test the behavior without constructing IDE loaders.
- Full program/type restoration remains blocked by the stubbed Tweedle decoder.

## Validation

Local gates:

```bash
mvn -DincludeSims=false -Dinstall4j.skip -pl core/story-api-migration -am test -Dtest=IoUtilitiesTest -Dsurefire.failIfNoSpecifiedTests=false -DfailIfNoTests=false
mvn -DincludeSims=false -Dinstall4j.skip clean test
mvn checkstyle:check -Dcheckstyle.config.location=checkstyle.xml
mvn -DincludeSims=false -Dinstall4j.skip -pl netbeans -am package -DskipTests
```

All local gates passed before push.

CI for `c57606b81f` passed:

- Alice Test CI: `25286552384`
- Alice Checkstyle CI: `25286552358`
- Alice NetBeans Package CI: `25286552345`

## Crusty proxy note

This is the right size of fix: one stubbed compatibility hook, one test, no fake parser work. The real decoder remains a larger job. Do not confuse this with player import support.

## Next seam

The strongest remaining candidates from the wide scout fan-out are:

- player export duplicate/path-like resource entry handling;
- JSON type read behavior for `.a3c`/Tweedle archives;
- model-resource export/read boundaries;
- `ProjectApplication` recovery orchestration seam extraction.
