# Journal 0001: initial Alice 3 investigation

## Repository correction

The desired repository model is two repos:

- Public source fork: `https://github.com/rysweet/alice3`
- Private artifact repo: `https://github.com/rysweet/drinkme`

`drinkme` must not contain Alice source. It holds only investigation artifacts.

## Build discoveries

- Alice 3 builds with Java 21 and Maven 3.9.9+.
- `git-lfs` and the `tweedle-lang` submodule are required.
- Install4J is needed only for installer builds.
- Non-Sims baseline test command passed:

```bash
mvn -DincludeSims=false -Dinstall4j.skip -DskipTests=false test
```

## Codebase scale

- 4,528 Java production files.
- 15 Java test files.
- 2,372 resource files.
- 29 POM files.
- Root reactor has 22 listed modules.

## Important architecture observations

- Alice 3 is a Java desktop IDE, not a web app or service.
- The startup path is concentrated in `EntryPoint`, `IDE`, and `StageIDE`.
- Tweedle is the internal representation of Alice code and is generated from ANTLR grammar in the `tweedle-lang` submodule.
- Resource/model loading is central and license-sensitive.
- NetBeans plugin support is first-class and tied to the Alice-to-Java teaching pathway.
- Existing tests mostly cover math, Tweedle parsing, manifest encoding, and version parsing.

## Early modernization conclusion

Do not start with a wholesale rewrite. Build characterization tests first, then refactor incrementally. Keep the application core Java. Consider Rust later for optional CLI/tooling around asset validation, fixture generation, and analysis.

