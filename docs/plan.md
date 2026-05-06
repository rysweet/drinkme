# Alice modernization investigation plan

## Problem

Alice 3 is a valuable educational programming environment with strong public teaching/reference material, but the source code is large, sparsely tested, and hard to maintain. Before refactoring or rewriting, we need a characterization test suite and a durable map of the current system.

## Repository model

- Modernized Alice implementation repo: `https://github.com/rysweet/RabbitHole`
- Public source fork/reference: `https://github.com/rysweet/alice3`
- Upstream source: `https://github.com/TheAliceProject/alice3`
- Private artifact repo: `https://github.com/rysweet/drinkme`

`drinkme` stores only investigation outputs: plans, notes, maps, diagrams, journals, and generated documentation. It must not vendor the Alice source tree.

The active implementation repo is `rysweet/RabbitHole`, not the upstream fork
network. Do not open issues or pull requests against
`TheAliceProject/alice3`; use the RabbitHole repo namespace only.

## Current findings

- Alice 3 is a Java 21/Maven desktop IDE with a NetBeans plugin.
- The documented non-installer build path works locally.
- Baseline command passed: `mvn -DincludeSims=false -Dinstall4j.skip -DskipTests=false test`.
- The RabbitHole modernization repo now has CI running `mvn -DincludeSims=false -Dinstall4j.skip clean test` and a no-Sims NetBeans package gate.
- Current test coverage is still small relative to the codebase, but the characterization suite now covers key IO, recovery, and NetBeans generation seams after the first sixty-two modernization slices.
- Desktop Run execution is partly proven for RabbitHole only: eatme can use a
  geometry-checked toolbar fallback, read RabbitHole's Run-frame and VM listener
  artifacts, and show that the desktop Run path reached VM statement execution.
  This does not yet prove original Alice equivalence, visible rendering, desktop
  save-menu completion, grading, or full lesson automation.
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
- Forty-second implementation slice split generated-source export tests into `ProjectCodeGeneratorGeneratedSourceTest`, reducing `ProjectCodeGeneratorTest` from 788 lines to 430 and keeping the new focused class at 399 lines.
- Forty-third implementation slice replaced the dormant model export test body with active no-Sims characterization for `ModelResourceExporter` XML serialization and generated resource Java compilation.
- Forty-fourth implementation slice added a standalone-style exported project smoke: a synthetic Alice project is generated into a `src` layout, compiled with JavaFX stubs, and the generated launcher is invoked through a child-first classloader.
- Forty-fifth implementation slice characterized named foreach item generation: named item locals emit readable Java (`item`) while unnamed helper-created loops still emit the current `COUNT__` fallback.
- Forty-sixth implementation slice characterized iterable foreach generation: a synthetic `ForEachInIterableLoop` over `Arrays.asList("red","blue")` emits compilable Java, imports `java.util.Arrays`, and preserves the explicit loop item name.
- Forty-seventh implementation slice added a template-shaped exported project smoke: the real NetBeans project template is extracted, generated Alice Java sources are placed in `src`, the `Alice3Library` classpath contract is checked, and the source tree compiles with the test classpath as the library surrogate.
- Forty-eighth implementation slice characterized the first realistic story API generated-source call: a synthetic program emits and compiles `this.setSimulationSpeedFactor(1.5);` in a new focused NetBeans test class rather than bloating the existing 481-line generated-source test.
- Forty-ninth implementation slice characterized the user-visible player export artifact: `ProjectFileUtilities.exportCopyOfProjectTo` now has a headless smoke proving the exported archive contains `version.txt`, `manifest.json`, `thumbnail.png`, and `src/Program.twe` with manifest metadata for the program and thumbnail.
- Fiftieth implementation slice characterized editor save-copy roundtrip: `ProjectFileUtilities.saveCopyOfProjectTo` writes a readable `.a3p` with manifest, thumbnail, program XML, and resource bytes, then `IoUtilities.readProject` preserves the program, camera type, resource identity, name, content type, and data.
- Fifty-first implementation slice characterized backup recovery candidate skipping: recent-backup probes now cover a newer unloadable backup being skipped, with the next candidate selected only when its timestamp is newer than the main project and rejected when older.
- Fifty-second implementation slice characterized `ProjectFileUtilities` save/export source selection and default-backup migration: export uses the forced up-to-date snapshot, save-copy uses the normal up-to-date snapshot, and default auto-backups move into the saved project's named backup directory.
- Fifty-third implementation slice added a headless backup recovery IO path: a corrupt main project and unloadable newest backup lead to the next backup being selected, planned as a backup-load prompt, and loaded through `FileProjectLoader` with resource metadata and bytes intact.
- Fifty-fourth implementation slice extracted and characterized the `ProjectApplication.saveProjectTo` target decision into `ProjectSaveTargetPlan`, preserving current new-project/default-backup/backup-save behavior while making the save orchestration seam testable without constructing the Swing-heavy IDE frame.
- Fifty-fifth implementation slice characterized the resource-bearing player export boundary: a referenced image resource is written into the player/Tweedle archive with manifest metadata, but the current editor XML reader cannot reopen that player export.
- Fifty-sixth implementation slice characterized editor save-copy roundtrip for an AST-referenced `ImageResource`: the XML editor archive writes `resources/picture.png` and reopens with program, camera, image resource identity, names, content type, and bytes intact.
- Fifty-seventh implementation slice added manifest-based reader dispatch for player exports and minimal JSON IO resource reads: exported `.a3w`/Tweedle archives now route to `JsonProjectIo` and restore manifest-listed image resources while leaving program-type Tweedle decoding explicitly unimplemented.
- Fifty-eighth implementation slice made JSON/player archives report future `version.txt` values through `ProjectReader.checkForFutureVersion()`, matching the XML reader warning path used by file loaders.
- Fifty-ninth implementation slice made JSON/player export resource entries duplicate-safe and path-safe: duplicate resource filenames use `resources2/...`, and slash/backslash path-like filenames are flattened before zip entry creation while resource bytes still round-trip.
- Sixtieth implementation slice characterized JSON/player export and readback for an AST-referenced `AudioResource`, using synthetic bytes and preserving the current resource-only player reader boundary.
- Sixty-first implementation wave used six isolated workflow-aware implementation branches plus fifteen scout/review lanes. It fixed JSON/player resource read identity isolation, hardened corrupt-manifest dispatch, characterized model/generated type references in player archives, added JSON `.a3c` resource-only type reads, strengthened the NetBeans template compiler surrogate, and extracted the project-load success decision seam.
- Sixty-second implementation wave used eight workflow-aware implementation lanes plus guardrails. It fixed NetBeans `Alice3Library` classpath shape, extracted project-load failure dispatch planning, added explicit manifest decode errors, characterized JSON `.a3c` version behavior, isolated XML resource identity on read, characterized `JsonModelIo` export format selection, characterized URI project-loader path classification, and hardened default-backup copy behavior.
- Added a dedicated submodule working guide for `tweedle-lang`, worktree initialization, `core/tweedle` ANTLR generation, and the common missing-submodule parser failure mode.
- Going forward, every coding lane and subagent must explicitly follow `DEFAULT_WORKFLOW`. Parallel implementation should use isolated worktrees/branches for independent modules; never parallel-edit the same working tree.
- The highest-risk uncharacterized areas are project load/save, model/resource handling, IDE journeys, NetBeans Java-transition workflows, and rendering-adjacent scenegraph behavior.
- Keep the core application Java for now; consider Rust first for optional external tooling, not core runtime.

## Work plan

1. Establish and preserve the two-repo split.
2. Maintain a reproducible build baseline from the public fork.
3. Build a website/reference traceability map.
4. Expand the code atlas from initial diagrams into all major architectural layers.
5. Convert website lessons, how-tos, and reference material into behavior-spec candidates.
6. Build characterization tests in phases, starting with pure logic and project formats.
7. Keep CI test execution active in the RabbitHole modernization repo.
8. Refactor incrementally behind tests; defer any rewrite decision until behavior is documented and protected.
9. Use crusty-old-engineer as a standing proxy review lane and qa-team as a standing outside-in testing lane, not as occasional afterthoughts.
10. For the desktop Run path, replace coordinate toolbar clicks with a stable UI
    or accessibility affordance, capture visible rendering after VM execution,
    prove desktop save-menu completion, and define how original Alice can be
    fairly proven without RabbitHole-only hooks.

## Success criteria

- Alice current code passes the characterization suite.
- The atlas lets a new contributor navigate startup, project persistence, Tweedle, resources, rendering, and NetBeans workflows without reading the whole source tree.
- Refactor proposals are tied to measured pain points and protected by tests.
- License-sensitive assets and no-Sims workflows stay explicit.
- Any Rust or non-Java work is isolated, optional, and justified by clear tooling or performance value.
