# Journal 0025: NetBeans blank generated resource filenames

## Loop 24 target

Finish the immediate generated-resource filename edge pass by checking blank `Resource.originalFileName` values.

Previous loops aligned normal, renamed, and duplicate original filenames. Blank original filenames still produced bad generated paths such as `resources/`, which cannot be copied and loaded as a concrete classpath resource.

## Alice implementation commit

Commit in `alice3-modernization`:

- `64c288c92a Handle blank generated resource filenames`

Changes:

- `ResourcesTypeWrapper` now resolves a generated resource filename with this order:
  1. nonblank `resource.getOriginalFileName()`;
  2. fixed resource display name from `resource.getName()`.
- The same wrapper-owned generated path is still used by both:
  - generated `Resources.java` constructor calls;
  - `ProjectCodeGenerator` copied resource bytes.
- Added AST-level coverage for blank original filename path mapping.
- Added NetBeans runtime coverage proving a resource with blank original filename and display name `friendly note` exports as `resources/friendly_note` and loads its bytes through compiled `Resources.java`.

## Review and validation

Crusty verdict:

- Fallback is narrow and compatibility-safe: normal nonblank original filenames are unchanged.
- It fixes a concrete generated-export dead path instead of adding broad runtime fallback magic.
- It still does not sanitize path separators or model every hostile filename; those should be separate slices.

Local validation passed:

```bash
mvn -DincludeSims=false -Dinstall4j.skip -pl netbeans -am test
mvn -DincludeSims=false -Dinstall4j.skip clean test
mvn checkstyle:check -Dcheckstyle.config.location=checkstyle.xml
```

Standalone CI passed for commit `64c288c92a`:

- Alice Checkstyle CI: success, run `25273170558`
- Alice Test CI: success, run `25273170556`

## Next useful slices

1. Characterize path separators or traversal-like original filenames in generated resources.
2. Map the exported Ant project build path now that resource path handling is stronger.
3. Add a non-empty synthetic method/scene source generation test.
