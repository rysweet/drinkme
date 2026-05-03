# Journal 0020: NetBeans generated-source compile smoke

## Loop 19 target

Move from "generated files exist" to "minimal generated files compile." This is the first user-like Alice-to-Java bridge check that invokes `javac` against generated source.

Scope stayed deliberately small:

- synthetic `.a3p`;
- generated `Program.java`;
- generated `AliceJavaFXLauncher.java`;
- JDK compiler using the Maven test classpath;
- no external project build, runtime launch, or IDE wizard.

## Alice implementation commit

Commit in `alice3-modernization`:

- `8ecb1769e6 Compile generated NetBeans sources`

Changes:

- Extended `ProjectCodeGeneratorTest`.
- Added `generatedSyntheticAliceProjectSourcesCompile()`.
- Generates source from a synthetic Alice project.
- Compiles `Program.java` and `AliceJavaFXLauncher.java` into a temporary classes directory using `javax.tools.JavaCompiler`.
- Adds `-proc:none` so unrelated annotation processors on the test classpath do not affect the smoke test.

## Bug-hunt finding

The first compile attempt failed:

```text
AliceJavaFXLauncher.java: cannot find symbol
  Program.main(String[])
```

Cause:

- the earlier synthetic `Program` type was too minimal;
- real exported Alice programs include a static `main(String[] args)` entry point;
- the generated launcher always calls `Program.main(startingArgs)`.

Fix in test fixture:

- add a synthetic static `main(String[] args)` `UserMethod`;
- keep it empty because the smoke test only validates source compatibility, not runtime behavior.

Crusty verdict: good catch. A test fixture that is too fake can report false breakage. The corrected fixture is closer to Alice's real bootstrap contract while still staying source-only and deterministic.

## Review and validation

Local validation passed:

```bash
mvn -DincludeSims=false -Dinstall4j.skip -pl netbeans -am test
mvn -DincludeSims=false -Dinstall4j.skip clean test
mvn checkstyle:check -Dcheckstyle.config.location=checkstyle.xml
```

Standalone CI passed for commit `8ecb1769e6`:

- Alice Checkstyle CI: success, run `25272478890`
- Alice Test CI: success, run `25272478880`

## Limits

- The generated source is compiled with the Maven test classpath, not an independently exported NetBeans project classpath.
- The test does not run the generated launcher.
- The test does not compile generated `Resources.java` yet.
- The synthetic main method is empty; it verifies the launcher contract, not story execution.

## Next useful slices

1. Compile generated source that includes `Resources.java`.
2. Add a synthetic scene or simple user method so generated source has meaningful behavior beyond an empty entry point.
3. Map the standalone exported-project classpath instead of leaning on the Maven test classpath.
