# Journal 0024: NetBeans duplicate generated resource filenames

## Loop 23 target

Continue the generated resource code-atlas pass after fixing display-name/original-filename mismatch. The next edge was duplicate `Resource.originalFileName` values.

XML project IO already handles this by writing duplicate resources to:

```text
resources/<filename>
resources2/<filename>
resources3/<filename>
...
```

NetBeans generated Java export did not have the same uniqueness strategy.

## Bug found

Before this loop:

- `ResourcesTypeWrapper` emitted every duplicate original filename as `resources/<filename>`.
- `ProjectCodeGenerator` copied resource bytes to the same path.
- Two generated static resource fields could therefore load the same final byte payload instead of their distinct resources.

This is reachable because XML project IO can read/write duplicate original filenames by using distinct zip entry paths while preserving each resource's `originalFileName` attribute.

## Alice implementation commit

Commit in `alice3-modernization`:

- `8308e5ece9 Handle duplicate generated resource filenames`

Changes:

- `ResourcesTypeWrapper` now owns a resource-to-generated-path map.
- Generated paths mirror XML project IO's strategy:
  - first duplicate: `resources/<filename>`;
  - second duplicate: `resources2/<filename>`;
  - third duplicate: `resources3/<filename>`;
  - and so on.
- `Resources.java` constructor strings and `ProjectCodeGenerator` copied files now use the same wrapper-owned generated path.
- Added AST-level coverage for duplicate original filename path mapping.
- Added NetBeans runtime coverage proving two resources with original filename `note.txt` and different bytes load back as distinct generated resources.

## Review and validation

Crusty verdict:

- This is the right owner for the mapping: `ResourcesTypeWrapper` generates the source reference, so the copy path must ask it for the same path.
- The fix avoids fallback guessing and aligns generated export behavior with existing XML project IO uniqueness.
- Remaining edge: missing or blank original filenames should be characterized separately before changing behavior.

Local validation passed:

```bash
mvn -DincludeSims=false -Dinstall4j.skip -pl netbeans -am test
mvn -DincludeSims=false -Dinstall4j.skip clean test
mvn checkstyle:check -Dcheckstyle.config.location=checkstyle.xml
```

Standalone CI passed for commit `8308e5ece9`:

- Alice Checkstyle CI: success, run `25273033519`
- Alice Test CI: success, run `25273033517`

## Next useful slices

1. Characterize missing/blank original filenames in project IO and NetBeans export.
2. Map the exported Ant project build path now that generated source/resource paths are stronger.
3. Add a non-empty synthetic method/scene source generation test.
