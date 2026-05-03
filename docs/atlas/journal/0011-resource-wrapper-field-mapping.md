# Journal 0011: resource wrapper field mapping fix

## Loop 10 target

Code-atlas bug hunting found a structural contradiction in the Alice-to-Java/resource export path:

- `ResourcesTypeWrapper` created generated `Resources` fields for exported resources;
- `JavaCodeGenerator.processResourceExpression(...)` expected `ResourcesTypeWrapper.getFieldForResource(resource)` to resolve those fields;
- the wrapper initialized `mapResourceToField` after creating the fields and never populated the map.

That meant generated code could fall back to brittle fixed-name resource lookups instead of using the generated field associated with the actual resource instance.

## Alice implementation commit

Commit in `alice3-modernization`:

- `2876037628 Fix resource wrapper field mapping`

Changes:

- Initialized `mapResourceToField` before resource fields are generated.
- Added each generated field to the map as its `Resource` is processed.
- Added `core/ast/src/test/java/org/lgna/project/resource/ResourcesTypeWrapperTest.java`.
- Covered normal resource mapping and duplicate fixed-name resources mapping to their distinct generated fields.

## Review and validation

Crusty review:

- Approved as a real bug fix rather than speculative cleanup.
- Confirmed the production change is the smallest useful fix: one map initialization move and one map population line.
- Confirmed the test resource uses the public `(Class, String, String)` constructor contract required by generated code.
- Confirmed duplicate-resource ordering is deterministic via `LinkedHashSet`, not `Set.of(...)`.

Local validation passed:

```bash
mvn -DincludeSims=false -Dinstall4j.skip -pl core/ast -am test
mvn -DincludeSims=false -Dinstall4j.skip clean test
mvn checkstyle:check -Dcheckstyle.config.location=checkstyle.xml
```

Standalone CI passed for commit `2876037628`:

- Alice Checkstyle CI: success, run `25271282049`
- Alice Test CI: success, run `25271282050`

## Next useful slices

1. Characterize `ProjectFileUtilities.copyDefaultBackupDirectory()` around the suspected file-vs-directory backup copy behavior.
2. Characterize parentless saved-project backup-directory handling before changing any null-parent behavior.
3. Characterize NetBeans project-template archive contents and metadata renaming without launching NetBeans.
4. Continue pure `ModelResourceInfo` edge coverage for explicit child `placeOnGround=false` and missing texture-name manifest output.
