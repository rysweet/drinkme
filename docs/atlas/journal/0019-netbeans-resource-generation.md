# Journal 0019: NetBeans resource generation foothold

## Loop 18 target

Extend the NetBeans generated-source foothold from a resource-free synthetic project to a synthetic project containing one resource.

This closes the loop between:

- project IO resource persistence;
- `ProjectCodeGenerator.generateCode(...)`;
- copied resource bytes under generated `resources/`;
- generated `Resources.java` source;
- the `ResourcesTypeWrapper` reflection contract fixed earlier.

## Alice implementation commit

Commit in `alice3-modernization`:

- `352dea5ff5 Characterize NetBeans resource generation`

Changes:

- Extended `ProjectCodeGeneratorTest` with a synthetic resource project.
- Added a test-only `TestResource` class that implements both resource contracts:
  - `public static valueOf(String)` for `.a3p` readback;
  - `public (Class<?>, String, String)` constructor for generated `Resources.java`.
- Wrote a temporary `.a3p` containing `note.txt`.
- Generated Java source/resources through `ProjectCodeGenerator.generateCode(...)` with editor formatting skipped by the Loop 17 headless seam.
- Verified:
  - generated `resources/note.txt` exists and preserves bytes;
  - generated `Resources.java` exists;
  - generated source contains `class Resources`;
  - generated source references `note.txt`.

## Bug-hunt finding

The first Loop 18 run failed because the test-only resource had `valueOf(String)` but not the public `(Class, String, String)` constructor.

That failure was useful: it confirmed two different Alice resource contracts are in play:

1. `.a3p` project readback reconstructs resource instances via `valueOf(String)`.
2. Exported/generated Java source reconstructs resources via constructor reflection.

Crusty verdict: keep both contracts explicit in tests. Otherwise a future cleanup could "simplify" one constructor away and break exported Java projects.

## Review and validation

Local validation passed:

```bash
mvn -DincludeSims=false -Dinstall4j.skip -pl netbeans -am test
mvn -DincludeSims=false -Dinstall4j.skip clean test
mvn checkstyle:check -Dcheckstyle.config.location=checkstyle.xml
```

Standalone CI passed for commit `352dea5ff5`:

- Alice Checkstyle CI: success, run `25272328258`
- Alice Test CI: success, run `25272328256`

## Limits

- The generated Java project is still not compiled outside the Alice Maven test runtime.
- The test uses a synthetic resource, not production image/audio/model/gallery resource subclasses.
- The test does not validate formatted output because that path requires NetBeans editor/project runtime services.

## Next useful slices

1. Generate a synthetic method body or scene type and assert more meaningful Java source shape.
2. Compile the generated Java sources once the minimal classpath for exported projects is mapped.
3. Investigate whether a real production resource subclass can be used without asset/license coupling.
