# Alice modernization investigation plan

## Problem

Alice 3 is a valuable educational programming environment with strong public teaching/reference material, but the source code is large, sparsely tested, and hard to maintain. Before refactoring or rewriting, we need a characterization test suite and a durable map of the current system.

## Repository model

- Standalone modernization repo: `https://github.com/rysweet/alice3-modernization`
- Public source fork/reference: `https://github.com/rysweet/alice3`
- Upstream source: `https://github.com/TheAliceProject/alice3`
- Private artifact repo: `https://github.com/rysweet/drinkme`

`drinkme` stores only investigation outputs: plans, notes, maps, diagrams, journals, and generated documentation. It must not vendor the Alice source tree.

The active implementation repo is `rysweet/alice3-modernization`, not the upstream fork network. Do not open issues or pull requests against `TheAliceProject/alice3`; use the standalone repo namespace only.

## Current findings

- Alice 3 is a Java 21/Maven desktop IDE with a NetBeans plugin.
- The documented non-installer build path works locally.
- Baseline command passed: `mvn -DincludeSims=false -Dinstall4j.skip -DskipTests=false test`.
- The standalone modernization repo now has CI running `mvn -DincludeSims=false -Dinstall4j.skip clean test` and a no-Sims NetBeans package gate.
- Current test coverage is very small relative to the codebase: thousands of tracked production Java files and 27 Java test files after the first forty-one modernization slices.
- Existing tests mostly cover Tweedle parsing, manifest encoding, version parsing, and math utilities.
- First implementation slice added launch-argument characterization tests and extracted a tested `LaunchConfiguration` seam.
- Second implementation slice added project migration/version characterization tests without production code changes.
- Third implementation slice characterized corrupt project-load IO failure delegation and documented why `FileProjectLoader` does not show its own error dialog.
- Fourth implementation slice added no-Sims `ModelResourceInfo` XML metadata and manifest characterization tests.
- Fifth implementation slice added NetBeans Alice-to-Java launcher generation characterization and locked the generated `AliceJavaFXLauncher` against the project template `main.class`.
- Sixth implementation slice extracted and characterized project backup candidate selection, keeping dialogs and recursive loading in `ProjectApplication`.
- Seventh implementation slice extracted and characterized the project-load failure branch plan, keeping Swing dialogs and recursive loading in `ProjectApplication`.
- Eighth implementation slice characterized `FileProjectLoader` VR save-path and `shouldBeSaved()` behavior with temp files.
- Ninth implementation slice characterized `ModelResourceInfo` texture-specific subresource lookup, model-only fallback, and manifest de-duplication.
- Tenth implementation slice fixed and characterized `ResourcesTypeWrapper` resource-to-field mapping, a code-atlas bug-hunt finding that broke exported-resource code generation by leaving generated fields unmapped.
- Eleventh implementation slice characterized backup-directory path derivation and hardened parentless backup-file handling so callers can skip backup work instead of crashing on a null parent.
- Twelfth implementation slice characterized the NetBeans project-template archive and fixed generated project metadata so `application.title` and `dist.jar` are renamed with the imported project.
- Thirteenth implementation slice fixed `ModelResourceInfo` edge cases: explicit child `placeOnGround=false` now overrides a true parent, omitted child values still inherit, and model-only manifest entries no longer use `*_null` names.
- Fourteenth implementation slice fixed `ModelResourceInfo` subresource tag parsing so nested unrelated XML tags are not collected while preserving direct and grouped tag formats.
- Fifteenth implementation slice added a provenance-clean synthetic `.a3p` round-trip test: a minimal in-memory project is written, read back, and checked for core archive entries without committing binary fixtures.
- Sixteenth implementation slice extended the synthetic `.a3p` round-trip to include a test-only resource that follows Alice's `valueOf(String)` reflection contract, verifying resource metadata and bytes survive project IO.
- Seventeenth implementation slice used the synthetic `.a3p` foothold to characterize NetBeans Java source generation: a minimal Alice project now generates `Program.java` plus `AliceJavaFXLauncher.java` in a headless test, with a package-private seam that skips only NetBeans editor formatting.
- Eighteenth implementation slice extended NetBeans source-generation characterization to resources: a synthetic resource now generates copied resource bytes plus `Resources.java`, preserving the resource constructor/reflection contracts needed by exported code.
- Nineteenth implementation slice added a JavaCompiler smoke test for generated `Program.java` and `AliceJavaFXLauncher.java`, and documented that even synthetic exported projects need the static `main(String[] args)` entry point expected by the launcher.
- Twentieth implementation slice extended generated-source compilation to resource-backed exports: `Program.java`, `AliceJavaFXLauncher.java`, and `Resources.java` now compile together for a synthetic resource project.
- Twenty-first implementation slice added a runtime smoke for generated resources: compiled `Resources.java` can load copied `resources/note.txt` bytes from the classpath through the generated static resource field.
- Twenty-second implementation slice fixed a generated-resource filename mismatch: NetBeans export now copies resource bytes by `originalFileName`, matching the path emitted in `Resources.java`, so display-name changes no longer break runtime resource loading.
- Twenty-third implementation slice fixed duplicate generated-resource filenames: exported `Resources.java` now assigns unique `resources`, `resources2`, ... paths and NetBeans copies bytes to those same paths, so duplicate original filenames do not collapse to one runtime resource.
- Twenty-fourth implementation slice fixed blank generated-resource filenames: when `originalFileName` is blank, export falls back to the fixed resource display name so `Resources.java` and copied bytes still use a loadable path.
- Twenty-fifth implementation slice hardened generated-resource filenames with separators or parent-directory names: export now sanitizes slash/backslash filename segments and falls back for bare `.`/`..`, keeping generated resource files inside the expected resources layout.
- Twenty-sixth implementation slice added non-empty generated user method coverage: a synthetic `sayHello()` method with a comment body is generated and compiled, expanding NetBeans source-generation characterization beyond empty program/resource scaffolding.
- Twenty-seventh implementation slice added local-declaration generated-source coverage: a synthetic user method now emits and compiles a final `String` local initialized from a string literal.
- Twenty-eighth implementation slice added user-parameter generated-source coverage: a synthetic method parameter is emitted in Java and accessed through a generated local declaration.
- Twenty-ninth implementation slice added user-method invocation generated-source coverage: a synthetic method emits and compiles a `this.sayHello();` call to another generated user method.
- Thirtieth implementation slice added user-method invocation argument coverage: a synthetic method emits and compiles `this.remember("hello alice");`, exercising generated arguments alongside parameter access.
- Thirty-first implementation slice added conditional generated-source coverage: a synthetic method emits and compiles a minimal `if(true) ... else ...` body.
- Thirty-second implementation slice added count-loop generated-source coverage: a synthetic method emits and compiles a minimal `for(Integer indexA=0;indexA<3;indexA++)` body.
- Thirty-third implementation slice characterized exported NetBeans project build properties: the template targets Java 21, `AliceJavaFXLauncher`, the `Alice3Library` NetBeans library, Alice root-directory runtime property, and JavaFX module opens; no-Sims CI now skips LFS checkout because the LFS budget can block tests that do not need assets.
- Thirty-fourth implementation slice characterized `Alice3Library` registration: the NetBeans layer registers `Alice3Library.xml`, and the library declares classpath, source, and javadoc volumes used by exported projects.
- Thirty-fifth implementation slice characterized NetBeans library packaging sources: the module POM packages javadoc, story source, and renamed NBM artifacts that back `Alice3Library` source/javadoc volumes.
- Thirty-sixth implementation slice added no-Sims NetBeans package CI so NBM/support artifact generation is checked on every `develop` push without relying on Git LFS assets.
- Thirty-seventh implementation slice tightened NetBeans package CI with explicit assertions for the NBM, module jar, source jar, javadoc zip, library registration resources, story source, and javadoc overview.
- Thirty-eighth implementation slice characterized generated launcher runtime handoff: a headless test invokes `AliceJavaFXLauncher.main(...)` against test-only JavaFX stubs and verifies the original args reach `Program.main(...)`.
- Thirty-ninth implementation slice added while-loop generated-source coverage: a synthetic method emits and compiles a minimal `while (true)` body without executing it.
- Fortieth implementation slice added foreach-array generated-source coverage: a synthetic method emits and compiles `for(String COUNT__ : new String[]{"red", "blue"})`, exposing a suspicious current loop-variable name for future cleanup.
- Forty-first implementation slice characterized foreach loop-item access: the same `COUNT__` variable is used coherently when the loop body reads the item, so this is readability debt rather than an immediate compile bug.
- The highest-risk uncharacterized areas are project load/save, model/resource handling, IDE journeys, NetBeans Java-transition workflows, and rendering-adjacent scenegraph behavior.
- Keep the core application Java for now; consider Rust first for optional external tooling, not core runtime.

## Work plan

1. Establish and preserve the two-repo split.
2. Maintain a reproducible build baseline from the public fork.
3. Build a website/reference traceability map.
4. Expand the code atlas from initial diagrams into all major architectural layers.
5. Convert website lessons, how-tos, and reference material into behavior-spec candidates.
6. Build characterization tests in phases, starting with pure logic and project formats.
7. Keep CI test execution active in the standalone modernization repo.
8. Refactor incrementally behind tests; defer any rewrite decision until behavior is documented and protected.

## Success criteria

- Alice current code passes the characterization suite.
- The atlas lets a new contributor navigate startup, project persistence, Tweedle, resources, rendering, and NetBeans workflows without reading the whole source tree.
- Refactor proposals are tied to measured pain points and protected by tests.
- License-sensitive assets and no-Sims workflows stay explicit.
- Any Rust or non-Java work is isolated, optional, and justified by clear tooling or performance value.
