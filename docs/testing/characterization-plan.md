# Characterization test plan

Goal: create a complete enough test suite that the current Alice 3 code passes it before any major refactor or rewrite. The first suite should model current behavior, not idealized behavior.

## Current test inventory

| Module | Active coverage |
| --- | --- |
| `core/util` | math and immutable geometry tests |
| `core/tweedle` | Tweedle parser, literals, statements, lambdas, manifest encoding |
| `core/ast` | version parsing/compatibility |
| `core/model-loading` | test file exists, but meaningful model export test is commented out |
| `core/story-api` | model resource XML metadata parsing and manifest generation |
| `core/story-api-migration` | migration table ordering, applicability thresholds, and representative text rewrite chains |
| `core/ide` | corrupt project-load IO failure delegation and backup candidate selection policy |
| `alice-ide` | launch argument parsing |
| `netbeans` | generated Alice-to-Java launcher and project template main-class alignment |

Frameworks are mixed JUnit 4 and JUnit 5. The root POM configures Surefire with `surefire-junit47`; `core/util` adds JUnit Jupiter; `core/tweedle` has its own Surefire `argLine` for Java module opens.

CI now runs both checkstyle and a no-Sims clean Maven test gate in the standalone modernization repo.

## Phase 1 progress

Completed characterization slices:

- Alice IDE launch arguments: locale flag handling, project path, window geometry defaults/fallbacks, and legacy quirks.
- Version parsing and comparison: historical version round trips, trailing-zero comparison behavior, prerelease ordering, and metadata ordering behavior.
- Project migration tables: text/AST migration result versions are valid and increasing; migration applicability is threshold-based; representative legacy story/resource strings are rewritten to current forms.
- Project-load failure seam: corrupt `.a3p` IO failures return `null` and delegate to the load-exception hook so `ProjectApplication` can drive backup recovery UI.
- Backup selection policy: headless tests cover the next-backup decision for corrupted main projects, unloadable backups, recent-backup probes, missing timestamps, and exhausted candidates.
- Model resource metadata: synthetic no-Sims XML covers metadata defaults, malformed optional fields, subresource tag inheritance, and manifest variant/resource/texture-set generation.
- NetBeans launcher generation: generated `AliceJavaFXLauncher.java` is written by the generator and remains aligned with the template `main.class` used by exported Java projects.

Known limits:

- Historical `.a3p` fixture migration is not yet covered. Add only tiny fixtures with explicit provenance and no Sims/nonfree assets.
- Model export remains mostly untested because the existing test body is commented and tied to gallery resources.
- Backup recovery dialogs and recursive load actions themselves are not yet tested headlessly; current coverage locks the lower-level loader contract and backup candidate selection policy only.
- The `ModelResourceExporter` binary/model export path is still not covered; Loop 4 intentionally stopped at pure metadata parsing to avoid asset/license and rendering dependencies.
- The NetBeans slice covers launcher generation only. It does not yet cover full Alice-project-to-Java source generation, palette/completion behavior, or NBM package behavior.

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
