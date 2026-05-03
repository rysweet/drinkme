# Journal 0030: NetBeans user-method invocation source generation

## Loop 29 target

Continue the generated-source characterization ladder by proving that one generated user method can call another generated user method.

The slice uses a minimal synthetic program with `sayHello()` and `callSayHello()`, where `callSayHello()` emits `this.sayHello();`. This exercises `AstUtilities.createMethodInvocationStatement`, `ThisExpression`, and `MethodInvocation` without crossing into story API, scenes, JavaFX runtime, or UI wizard behavior.

## Alice implementation commit

Commit in `alice3-modernization`:

- `370c483629 Characterize generated method invocations`

Changes:

- Added `generatedSyntheticUserMethodInvocationSourceCompiles()` to `ProjectCodeGeneratorTest`.
- Built a minimal synthetic Alice program containing:
  - static `main(String[] args)`, still required by `AliceJavaFXLauncher`;
  - non-static `sayHello()` with a comment body;
  - non-static `callSayHello()` invoking `this.sayHello();`.
- Verified the generated `Program.java` includes both methods and the generated invocation.
- Compiled the generated program and launcher with the JDK compiler using the test classpath and `-proc:none`.

## Review and validation

Crusty verdict:

- Good incremental net: generated methods are no longer isolated bodies; this covers a simple intra-program call edge.
- Still a small foothold. It does not prove story API invocation, overloaded methods, arguments, control flow, event wiring, or runtime launch.
- Keep characterization moving outward from synthetic AST constructs toward exported project build/runtime behavior.

Local validation passed:

```bash
mvn -DincludeSims=false -Dinstall4j.skip -pl netbeans -am test
mvn -DincludeSims=false -Dinstall4j.skip clean test
mvn checkstyle:check -Dcheckstyle.config.location=checkstyle.xml
```

Standalone CI passed for commit `370c483629`:

- Alice Checkstyle CI: success, run `25273875820`
- Alice Test CI: success, run `25273875817`

## Next useful slices

1. Add method invocation with an argument, reusing the parameter/local declaration footholds.
2. Map the exported Ant/NetBeans project build path outside the unit-test compiler helper.
3. Start a code-atlas pass over generated-source constructs to identify the next missing branch before refactoring.
