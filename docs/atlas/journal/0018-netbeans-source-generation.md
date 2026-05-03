# Journal 0018: NetBeans source generation foothold

## Loop 17 target

Use the synthetic `.a3p` project-IO foothold to characterize the first real NetBeans source-generation path without committing binary fixtures or invoking the full IDE wizard.

The useful path is `ProjectCodeGenerator.generateCode(...)`: it reads an Alice project, converts named user types to Java source, writes resources if present, generates `AliceJavaFXLauncher.java`, and returns files the wizard should open.

## Alice implementation commit

Commit in `alice3-modernization`:

- `56d2e080f7 Characterize NetBeans source generation`

Changes:

- Extended `ProjectCodeGeneratorTest`.
- Creates a temporary synthetic `.a3p` with a minimal `Program` type extending `SProgram`.
- Runs `ProjectCodeGenerator.generateCode(...)` into a temporary source directory.
- Verifies:
  - `Program.java` is created;
  - `AliceJavaFXLauncher.java` is created;
  - the launcher is returned in the files-to-open collection;
  - generated program source contains `class Program extends SProgram`.
- Added a package-private overload of `generateCode(...)` that can skip the NetBeans editor formatting step in headless tests.
- Preserved the public `generateCode(File, File, ProgressHandle)` behavior: it still formats generated files through NetBeans editor infrastructure.

## Bug-hunt finding

The first test attempt exposed a headless seam rather than a generation bug:

- file creation succeeded far enough to reach the formatting phase;
- `DataObject`/`EditorCookie.openDocument()` reached NetBeans `ProjectManager`;
- the Maven unit-test runtime has no `ProjectManagerImplementation` in global lookup;
- result: `ExceptionInInitializerError` from NetBeans project API.

Crusty verdict: do not fake a NetBeans runtime in a unit test. Keep the IDE path intact and add the smallest seam that lets tests exercise source generation while skipping editor formatting.

## Review and validation

Local validation passed:

```bash
mvn -DincludeSims=false -Dinstall4j.skip -pl netbeans -am test
mvn -DincludeSims=false -Dinstall4j.skip clean test
mvn checkstyle:check -Dcheckstyle.config.location=checkstyle.xml
```

Standalone CI passed for commit `56d2e080f7`:

- Alice Checkstyle CI: success, run `25272190438`
- Alice Test CI: success, run `25272190440`

## Limits

- The test does not run the full NetBeans import wizard.
- The test does not validate NetBeans editor formatting.
- The generated Java project is not compiled outside the Maven/Alice test runtime.
- The synthetic project contains no methods, scenes, procedures, fields, or resources.

## Next useful slices

1. Add generated-source assertions for a synthetic user method or scene type.
2. Add a generated resource source test using the synthetic resource round-trip contract.
3. Eventually compile generated source as an external Java project, once the minimal classpath is understood.
