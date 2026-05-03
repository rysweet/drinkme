# Characterization test plan

Goal: create a complete enough test suite that the current Alice 3 code passes it before any major refactor or rewrite. The first suite should model current behavior, not idealized behavior.

## Current test inventory

| Module | Active coverage |
| --- | --- |
| `core/util` | math and immutable geometry tests |
| `core/tweedle` | Tweedle parser, literals, statements, lambdas, manifest encoding |
| `core/ast` | version parsing/compatibility; resource wrapper field mapping |
| `core/model-loading` | test file exists, but meaningful model export test is commented out |
| `core/story-api` | model resource XML metadata parsing, variant selection, manifest generation, model-only/placement edge cases, and subresource tag isolation |
| `core/story-api-migration` | migration table ordering, applicability thresholds, representative text rewrite chains, synthetic project IO round-trip, and synthetic resource IO round-trip |
| `core/ide` | corrupt project-load IO failure delegation, backup recovery policy seams, backup-directory path handling, and VR project-loader save-path behavior |
| `alice-ide` | launch argument parsing |
| `netbeans` | generated Alice-to-Java launcher, project template archive contents, main-class alignment, generated project metadata renaming, exported build-property contract, `Alice3Library` registration, library packaging source, synthetic Alice project source generation, generated resource export foothold, generated-source compile smokes, generated resource runtime loading, resource filename mismatch coverage, duplicate resource filename coverage, blank resource filename fallback, unsafe resource filename sanitization, non-empty generated user method source, local declaration source, user parameter source, user-method invocation source, invocation-argument source, conditional source, and count-loop source |

Frameworks are mixed JUnit 4 and JUnit 5. The root POM configures Surefire with `surefire-junit47`; `core/util` adds JUnit Jupiter; `core/tweedle` has its own Surefire `argLine` for Java module opens.

CI now runs both checkstyle and a no-Sims clean Maven test gate in the standalone modernization repo.

## Phase 1 progress

Completed characterization slices:

- Alice IDE launch arguments: locale flag handling, project path, window geometry defaults/fallbacks, and legacy quirks.
- Version parsing and comparison: historical version round trips, trailing-zero comparison behavior, prerelease ordering, and metadata ordering behavior.
- Project migration tables: text/AST migration result versions are valid and increasing; migration applicability is threshold-based; representative legacy story/resource strings are rewritten to current forms.
- Project-load failure seam: corrupt `.a3p` IO failures return `null` and delegate to the load-exception hook so `ProjectApplication` can drive backup recovery UI.
- File project loader VR save-path: temp-file tests cover non-VR URI/save state, make-VR-ready renamed URI, and existing/missing VR-copy `shouldBeSaved()` behavior.
- Backup selection policy: headless tests cover the next-backup decision for corrupted main projects, unloadable backups, recent-backup probes, missing timestamps, and exhausted candidates.
- Project-load failure plan: headless tests cover the current dialog/load branch choice for manually loaded corrupt backups, corrupt main projects, corrupt backups during recovery, default unsaved backups, exhausted saved-project backups, and failed recent-backup probes.
- Model resource metadata: synthetic no-Sims XML covers metadata defaults, malformed optional fields, subresource tag inheritance, texture-specific subresource lookup, model-only fallback, manifest variant/resource/texture-set generation, and structure/texture-set de-duplication.
- NetBeans launcher generation: generated `AliceJavaFXLauncher.java` is written by the generator and remains aligned with the template `main.class` used by exported Java projects.
- Resource wrapper code-generation seam: generated `Resources` fields now map back to their `Resource` instances, including duplicate fixed-name handling.
- Backup-directory path handling: temp-file tests cover saved-project `.bak` sibling directories, non-project file naming, backup-file parent reuse, and parentless backup-file null handling.
- NetBeans project-template metadata: archive tests cover required template entries without a root-prefix directory, and property-renaming tests cover generated `application.title`/`dist.jar` values while preserving the launcher `main.class`.
- Model resource manifest edges: synthetic XML tests cover explicit subresource `placeOnGround=false` overriding a true parent, missing subresource placement inheriting from the parent, and model-only resources producing manifest names without `_null`.
- Model resource tag parsing: synthetic XML tests cover grouped subresource tags and confirm nested unrelated `Tag`, `GroupTag`, and `ThemeTag` descendants do not leak into variant metadata.
- Project IO foothold: synthetic in-memory project tests write a temporary `.a3p`, read it back, verify the program type and default camera metadata, and verify core zip entries without checking in binary fixtures.
- Resource IO foothold: a test-only `Resource` class implements Alice's `valueOf(String)` reflection contract; tests verify resource UUID, names, content type, bytes, `resources.xml`, and resource zip entry survive the `.a3p` round trip.
- NetBeans source generation foothold: a synthetic `.a3p` generates `Program.java` and `AliceJavaFXLauncher.java` in a headless test, while the public IDE path still performs NetBeans editor formatting.
- NetBeans resource generation foothold: a synthetic resource generates `resources/note.txt` and `Resources.java`, requiring both `valueOf(String)` and public `(Class, String, String)` constructors on generated resource classes.
- NetBeans generated-source compile smoke: a synthetic program with static `main(String[] args)` compiles generated `Program.java` and `AliceJavaFXLauncher.java` with the JDK compiler and test classpath.
- NetBeans resource-backed compile smoke: a synthetic resource project compiles generated `Program.java`, `AliceJavaFXLauncher.java`, and `Resources.java` together.
- NetBeans generated-resource runtime smoke: compiled `Resources.java` loads copied `resources/note.txt` bytes from the classpath through its generated static field.
- NetBeans resource filename mismatch: generated exports copy resource bytes by `originalFileName`, matching `Resources.java`, even when the user-visible resource name differs.
- NetBeans duplicate resource filenames: generated exports assign unique `resources`, `resources2`, ... paths when multiple resources share an `originalFileName`, and runtime loading preserves both byte payloads.
- NetBeans blank resource filenames: generated exports fall back to the fixed resource display name when `originalFileName` is blank, and runtime loading still preserves bytes.
- NetBeans unsafe resource filenames: generated exports sanitize slash/backslash path separators and bare parent-directory names so copied resource files stay inside the generated resources layout.
- NetBeans non-empty generated user method source: a synthetic `sayHello()` method with a comment body generates Java source and compiles with the exported program/launcher smoke test.
- NetBeans local declaration source: a synthetic `sayHello()` method generates and compiles a final `String` local initialized from a string literal.
- NetBeans user parameter source: a synthetic `remember(String message)` method generates and compiles a parameter access through a final local declaration.
- NetBeans user-method invocation source: a synthetic `callSayHello()` method generates and compiles a `this.sayHello();` invocation of another generated user method.
- NetBeans invocation argument source: a synthetic `callRemember()` method generates and compiles `this.remember("hello alice");`, with the callee consuming the parameter through a final local declaration.
- NetBeans conditional source: a synthetic `choose()` method generates and compiles a minimal `if(true)` branch with an `else` body.
- NetBeans count-loop source: a synthetic `repeat()` method generates and compiles a minimal count loop with deterministic `indexA` naming.
- NetBeans exported build-property contract: project template properties lock Java 21, `AliceJavaFXLauncher`, `libs.Alice3Library.classpath`, Alice root-directory runtime property, and JavaFX module opens.
- NetBeans `Alice3Library` registration: the NetBeans layer registers `Alice3Library.xml`, and the library declares classpath, source, and javadoc volumes including Alice jars, JavaFX graphics, `aliceSource.jar`, and `aliceDocs.zip`.
- NetBeans library packaging source: the module POM is characterized for javadoc, story source, and final NBM assembly descriptors that back `Alice3Library` support artifacts.
- CI no-Sims test gate: checkout no longer fetches Git LFS objects, because the no-Sims test baseline should not fail when the repository LFS budget is exhausted.
- CI no-Sims NetBeans package gate: GitHub Actions now runs `mvn -DincludeSims=false -Dinstall4j.skip -pl netbeans -am package -DskipTests` on `develop` pushes and pull requests, proving the package phase still creates the NBM/support artifact set without Sims/LFS assets.
- CI package artifact assertions: the NetBeans package workflow now verifies a single top-level NBM, the NetBeans module jar, `aliceSource.jar`, `aliceDocs.zip`, `Alice3Library.xml`, `layer.xml`, `SProgram.java`, and the javadoc overview entry.
- NetBeans generated launcher runtime handoff: a headless test compiles the generated `AliceJavaFXLauncher` with test-only JavaFX stubs and verifies `AliceJavaFXLauncher.main(args)` passes the exact args array to `Program.main(args)`.

Known limits:

- Historical `.a3p` fixture migration is not yet covered. Add only tiny fixtures with explicit provenance and no Sims/nonfree assets.
- The synthetic project/resource IO tests are intentionally minimal. They do not cover real StageIDE-generated projects, manifests supplied by `ProjectFileUtilities`, thumbnails, gallery resource subclasses, or historical fixtures.
- Model export remains mostly untested because the existing test body is commented and tied to gallery resources; current model-resource coverage is still XML/manifest-only.
- Resource wrapper tests cover the mapping seam only; full Java source generation from Alice project fixtures still belongs in the NetBeans/export phase.
- Backup recovery dialogs and recursive load side effects themselves are not yet tested headlessly; current coverage locks the lower-level loader contract, backup candidate selection policy, and branch-planning decision only.
- `copyDefaultBackupDirectory()` is not yet directly covered because it depends on `StageIDE.getActiveInstance()` for the default projects directory. The earlier file-vs-directory concern appears lower risk because `backupDirectory(file, false)` creates the named directory before `createNewFile()` is called.
- The `ModelResourceExporter` binary/model export path is still not covered; Loop 4 intentionally stopped at pure metadata parsing to avoid asset/license and rendering dependencies.
- The NetBeans slices cover launcher generation, generated launcher argument handoff, template archive shape, generated project metadata, exported build-property assumptions, `Alice3Library` registration, library packaging sources, package-phase CI with artifact smoke assertions, minimal Alice-project-to-Java source generation, a synthetic generated-resource path, compilation of generated program/launcher/resource source, runtime loading of generated resource bytes, display-name/original-filename mismatch behavior, duplicate original-filename behavior, blank original-filename fallback, unsafe filename sanitization, a comment-only non-empty user method, a final string local declaration, a simple string parameter access, a user-method invocation, a string literal invocation argument, a minimal conditional, and a minimal count loop. They do not yet cover meaningful story API calls, real scenes/events, complex parameters, while loops, foreach loops, full wizard execution, real JavaFX launcher startup, formatted output, palette/completion behavior, deep NBM manifest/module install semantics, or an actual standalone Ant build with a populated `Alice3Library` definition.

## Phase 1: lock down pure logic and formats

These tests should be fast, deterministic, and run on every PR.

- Version parsing and round-trip compatibility.
- Tweedle literal parsing: null, booleans, strings, escapes, integers, decimals, negative values.
- Tweedle statements: `countUpTo`, conditionals, blocks, variable declaration/assignment.
- Tweedle lambdas inside method calls.
- Manifest JSON encoding/decoding shape, including metadata, provenance, root joints, texture sets, model lists, and date formats.
- Math/geometry invariants: matrices, quaternions, Euler angles, transforms, epsilon equality.

## Phase 2: project, model, and resource persistence

These tests should establish behavioral confidence around Alice artifacts.

- Project load/save round trips using small fixture worlds.
- Project version migration and compatibility checks.
- Model manifest export/import and resource ID stability.
- Gallery resource lookup with `includeSims=false`.
- Re-enabled equivalent of `ModelExportTest`, using minimal fixtures that can be committed safely.
- Localization resource lookup and fallback behavior.

## Phase 3: IDE command and user-journey characterization

These tests can use headless-friendly seams where possible, with a small number of UI smoke tests.

- Launch argument parsing: locale, project path, window coordinates.
- Startup classinfo loading.
- Crash detector open/close behavior.
- StageIDE initialization side effects, especially gallery directory setup.
- Project open flow from command-line argument.
- Command availability for scene editing, adding objects, run/stop story, save/export.
- License prompt gating and accepted-preference behavior.

## Phase 4: rendering-adjacent behavior

Avoid brittle pixel tests at first. Start with structural and invariant tests.

- Scenegraph construction from story/model resources.
- Renderer native library loader selection logic.
- Platform-native resource path resolution.
- Transform hierarchy invariants.
- Visual/resource wiring for simple model fixtures.

## Phase 5: NetBeans plugin and Java transition

These tests model the website promise that Alice can bridge to Java.

- Project template generation.
- Generated Java source shape from Alice project fixtures.
- Completion/palette registration smoke tests.
- NBM package build smoke.
- Alice-to-Java tutorial fixtures as executable regression tests.

## CI plan

1. Keep the Maven test workflow running `mvn -DincludeSims=false -Dinstall4j.skip clean test`.
2. Keep checkstyle as a separate fast signal.
3. Split slow or UI-heavy tests into profiles after the characterization suite grows.
4. Require every refactor PR to preserve all current characterization tests.

## Test data policy

- Prefer tiny synthetic fixtures.
- Keep Sims/nonfree assets out of public test fixtures unless their license explicitly allows the use.
- Preserve fixture provenance and license notes.
- Store large/generated fixture inventories as metadata, not copied binaries.
