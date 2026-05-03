# Journal 0026: NetBeans unsafe generated resource filenames

## Loop 25 target

Continue the generated-resource filename hardening pass by checking original filenames that contain path separators or parent-directory names.

Before this loop, generated export paths were built from the original filename after only blank handling. That left room for names like:

```text
../folder\note.txt
..
```

to produce nested or traversal-like generated resource paths.

## Alice implementation commit

Commit in `alice3-modernization`:

- `3e8a17cd47 Sanitize generated resource filenames`

Changes:

- `ResourcesTypeWrapper` sanitizes generated resource filename segments:
  - `/` becomes `_`;
  - `\` becomes `_`;
  - bare `.` and `..` fall back to the fixed display name.
- Normal nonblank filenames are otherwise preserved.
- The wrapper-owned generated path remains the single source of truth for both `Resources.java` and copied resource bytes.
- Added AST-level coverage for:
  - mixed slash/backslash original filenames;
  - bare parent-directory filename fallback.
- Added NetBeans runtime coverage proving a traversal-like synthetic original filename exports as a single file under `resources/` and still loads bytes through compiled `Resources.java`.

## Review and validation

Crusty verdict:

- Good boundary: fix only generated export filenames, do not rewrite project IO history.
- This is not a broad sanitizer for every possible hostile filename, but it closes the practical path-separator/traversal class.
- Normal resource filenames and previous duplicate/blank behavior remain covered.

Local validation passed:

```bash
mvn -DincludeSims=false -Dinstall4j.skip -pl netbeans -am test
mvn -DincludeSims=false -Dinstall4j.skip clean test
mvn checkstyle:check -Dcheckstyle.config.location=checkstyle.xml
```

Standalone CI passed for commit `3e8a17cd47`:

- Alice Checkstyle CI: success, run `25273289296`
- Alice Test CI: success, run `25273289294`

## Next useful slices

1. Map the exported Ant project build path now that generated source/resource paths are stronger.
2. Add a non-empty synthetic method/scene source generation test.
3. Continue broader project IO/resource migration characterization outside NetBeans export.
