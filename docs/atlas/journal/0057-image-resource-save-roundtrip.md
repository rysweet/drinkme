# 0057 - Image resource save roundtrip

## Slice

Added headless editor save-copy characterization for an AST-referenced `ImageResource`.

## Source change

- Repo: `rysweet/alice3-modernization`
- Branch: `develop`
- Commit: `259a3d02b6 Characterize image resource save roundtrip`
- File: `core/ide/src/test/java/org/alice/ide/ProjectFileUtilitiesTest.java`

No production code changed in this slice.

## Test behavior

The new test:

1. Creates a synthetic program that references an `ImageResource` through an AST `ResourceExpression`.
2. Adds the same image resource to the project resource set.
3. Saves through `ProjectFileUtilities.saveCopyOfProjectTo(...)`.
4. Verifies the editor archive contains:
   - `programType.xml`
   - `resources.xml`
   - `resources/picture.png`
5. Verifies saved image bytes match the original.
6. Reopens through `IoUtilities.readProject(...)`.
7. Verifies program name, camera type, resource class, UUID, original file name, display name, content type, and bytes survive.

## Why this slice

QA recommended pinning the editor save/open behavior for a real image resource after Loop 56 proved the player export boundary. This gives both sides of the resource archive split:

- editor save-copy: XML archive, image resource reopens successfully;
- player export: Tweedle/manifest archive, image bytes are written but the current editor reader rejects it.

## Findings

- Editor save-copy preserves AST-referenced `ImageResource` data and metadata.
- The saved editor archive remains readable through the current XML reader.
- This contrasts with player export, where `IoUtilities.readProject(...)` still routes through `XmlProjectIo` and cannot reopen the Tweedle archive.
- `ProjectFileUtilitiesTest` is 334 lines, still under the 500-line target.

## Validation

Local gates:

```bash
mvn -DincludeSims=false -Dinstall4j.skip -pl core/ide -am test -Dtest=ProjectFileUtilitiesTest -Dsurefire.failIfNoSpecifiedTests=false -DfailIfNoTests=false
mvn -DincludeSims=false -Dinstall4j.skip clean test
mvn checkstyle:check -Dcheckstyle.config.location=checkstyle.xml
mvn -DincludeSims=false -Dinstall4j.skip -pl netbeans -am package -DskipTests
```

All local gates passed before push.

CI for `259a3d02b6` passed:

- Alice Test CI: `25285987722`
- Alice Checkstyle CI: `25285987723`
- Alice NetBeans Package CI: `25285987725`

## Crusty proxy note

This was the safe prerequisite. It confirms the editor archive path is sound for a real image resource. It does not fix player archive reader dispatch, and it does not prove model resources or real gallery assets.

## Next seam

Return to the reader-dispatch mismatch: `IoUtilities.projectReader(...)` still always selects `XmlProjectIo`, while player exports are written by `JsonProjectIo`.
