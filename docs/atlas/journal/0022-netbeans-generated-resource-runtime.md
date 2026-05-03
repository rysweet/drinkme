# Journal 0022: NetBeans generated resource runtime smoke

## Loop 21 target

Close the next gap in the generated resource path. Previous loops proved generated resource source exists and compiles. Loop 21 verifies the generated `Resources` class can actually load copied resource bytes from the classpath at runtime.

## Alice implementation commit

Commit in `alice3-modernization`:

- `62ca83ba4d Load generated resource bytes`

Changes:

- Extended `ProjectCodeGeneratorTest`.
- Generates source from a synthetic Alice project containing `note.txt`.
- Compiles `Program.java`, `AliceJavaFXLauncher.java`, and `Resources.java`.
- Copies generated `resources/note.txt` into the compiled classes directory.
- Loads generated `Resources` through a `URLClassLoader`.
- Reflects the generated static resource field.
- Verifies:
  - content type is `text/plain`;
  - generated resource bytes equal the original synthetic bytes.

## Code-atlas bug-hunt check

The graph path is now covered through these edges:

```text
.a3p resource -> ProjectCodeGenerator -> resources/note.txt
              -> ResourcesTypeWrapper -> Resources.java
              -> javac output -> URLClassLoader -> Resource.getData()
```

The relevant production contract is `ResourcesTypeWrapper` generating constructor calls with `"resources/" + resource.getOriginalFileName()`. `Resource(Class, String, String)` then loads that path relative to the generated `Resources` class. The test copies the generated `resources/` directory into the class output to model the expected exported classpath layout.

## Review and validation

Local validation passed:

```bash
mvn -DincludeSims=false -Dinstall4j.skip -pl netbeans -am test
mvn -DincludeSims=false -Dinstall4j.skip clean test
mvn checkstyle:check -Dcheckstyle.config.location=checkstyle.xml
```

Standalone CI passed for commit `62ca83ba4d`:

- Alice Checkstyle CI: success, run `25272738786`
- Alice Test CI: success, run `25272738796`

## Limits

- Still not a full exported NetBeans/Ant project build.
- Still does not launch the generated JavaFX application.
- Uses synthetic text bytes, not production media/model resource subclasses.
- Reflective field access is necessary because generated `Resources` is in the default package and package-private.

## Next useful slices

1. Add a non-empty synthetic user method or scene method and compile it.
2. Map the exported Ant project classpath and build the generated project outside Maven tests.
3. Add a headless runtime smoke for a generated class that does not open JavaFX windows.
