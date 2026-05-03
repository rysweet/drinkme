# Journal 0017: synthetic resource round trip

## Loop 16 target

After the synthetic project round-trip foothold, the next safe project-IO slice was resource persistence without committing gallery assets or binary fixtures.

Alice project IO writes each resource to `resources/<originalFileName>` and records resource metadata in `resources.xml`. On read, it reconstructs the resource class through a public static `valueOf(String)` method, then calls `decodeAttributes(...)` with the stored bytes.

## Alice implementation commit

Commit in `alice3-modernization`:

- `ed03c0db72 Characterize synthetic resource round trip`

Changes:

- Extended `IoUtilitiesTest` with a test-only `TestResource`.
- `TestResource` implements the production reflection contract:
  - extends `org.lgna.common.Resource`;
  - exposes `public static TestResource valueOf(String uuidText)`;
  - lets `decodeAttributes(...)` populate name, original filename, content type, and bytes.
- Wrote a temporary `.a3p` with one synthetic text resource.
- Read it back through `IoUtilities.readProject(...)`.
- Verified:
  - resource class;
  - UUID;
  - original filename;
  - display name;
  - content type;
  - byte content;
  - `resources.xml`;
  - `resources/note.txt` archive entry.

## Review and validation

Crusty review:

- Approved because it exercises the real project-IO resource contract without asset dependencies.
- Confirmed the resource class is test-only and does not alter production code.
- Confirmed this still does not claim coverage for gallery resource subclasses, model export, thumbnails, or real StageIDE project saves.

Local validation passed:

```bash
mvn -DincludeSims=false -Dinstall4j.skip -pl core/story-api-migration -am test
mvn -DincludeSims=false -Dinstall4j.skip clean test
mvn checkstyle:check -Dcheckstyle.config.location=checkstyle.xml
```

Standalone CI passed for commit `ed03c0db72`:

- Alice Checkstyle CI: success, run `25272030076`
- Alice Test CI: success, run `25272030080`

## Next useful slices

1. Use the synthetic `.a3p` path to drive a first NetBeans generated-source test.
2. Characterize `ProjectFileUtilities` data-source behavior if it can be separated from `ProjectApplication`.
3. Search for provenance-clean real `.a3p` fixtures or generate them from source-only builders.
4. Continue code-atlas passes over project IO now that synthetic round trips exist.
