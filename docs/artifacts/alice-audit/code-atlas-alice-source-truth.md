# Alice source-truth code atlas bug hunt

Generated: 2026-05-03T22:21Z  
Repository: `rysweet/alice3-modernization`  
Scope: checked-out Alice source tree under `alice-ide`, `core`, `core-nonfree`, `external`, `installer`, `netbeans`, root build files, `README.md`, and `AGENTS.md`.

This artifact is source-derived documentation. It stores architecture summaries, metrics, and findings only; it does not copy Alice source into `drinkme`.

## Source truth method

The atlas was derived from:

- Maven module declarations in `pom.xml:101-126`, profile modules in `pom.xml:681-696` and `pom.xml:765-776`.
- Module POM dependencies in `alice-ide/pom.xml`, `core/*/pom.xml`, `core-nonfree/*/pom.xml`, `external/*/pom.xml`, `netbeans/pom.xml`, and `installer/pom.xml`.
- Java source inventory under module `src/main/java` and `src/test/java`, excluding `target`.
- Targeted grep checks for entry points, root-directory integration, stale docs, optional Sims paths, TODO/deprecated markers, and NetBeans packaging settings.

Companion diagrams:

- Mermaid: `drinkme/code-atlas-alice-module-graph.mmd`
- Graphviz DOT: `drinkme/code-atlas-alice-module-graph.dot`

Verdict vocabulary:

- **CONFIRMED / FAIL**: source-backed contradiction or stale artifact with direct file/path evidence.
- **NEEDS_ATTENTION**: source-backed risk that requires a targeted build, packaging job, or characterization test before changing behavior.
- **PASS**: no validated issue found for the category during this pass.

## Architecture summary

Alice is a Java 21 / Maven 3.9.9 multi-module application. The root reactor always includes core, external wrappers, `alice-ide`, and `netbeans`; optional profiles add Sims/nonfree assets and installers.

| Layer | Source truth | Role |
| --- | --- | --- |
| Root build | `pom.xml:101-126` | Main reactor: core modules, external modules, `alice-ide`, `netbeans`. |
| Optional Sims/nonfree | `pom.xml:681-696`, `alice-ide/pom.xml:120-136`, `netbeans/pom.xml:293-312` | Adds `core-nonfree/*` modules and dependencies when `includeSims` is not false. |
| Installer | `pom.xml:765-776`, `installer/pom.xml:53-84` | Profile-gated Install4J packaging that depends on `alice-ide`. |
| Runtime launcher | `alice-ide/pom.xml:161-181`, `alice-ide/src/main/java/org/alice/stageide/EntryPoint.java:70-150` | Maven exec entrypoint, FlatLaf setup, JOGL native init, Swing/JavaFX startup, `StageIDE` creation. |
| Application root | `core/util/src/main/java/edu/cmu/cs/dennisc/app/ApplicationRoot.java:53-87` | Requires `org.alice.ide.rootDirectory` and exits if absent or invalid. |
| Story/model stack | `core/story-api`, `core/models`, `core/model-loading`, `core/story-api-migration` POMs | Public story API, gallery resources, model loading/export, and project migration. |
| IDE stack | `core/ide`, `core/croquet`, `core/image-editor`, `core/issue-reporting` POMs | Stage IDE UI, Croquet UI framework, image editor, issue reporting. |
| NetBeans integration | `netbeans/pom.xml:54-56`, `netbeans/pom.xml:430-442` | NBM packaging against NetBeans `RELEASE180`; includes legacy Pack200 installer setting. |

## Module dependency map

High-level internal Maven edges:

- `alice-ide -> ide`
- `ide -> story-api, story-api-migration, models, scenegraph, glrender, ast, croquet, resources, i18n, image-editor, issue-reporting, util`
- `story-api -> ast, scenegraph, glrender, tweedle, util, collada-schema-1-4-1`
- `story-api-migration -> ast, story-api, model-loading, models, tweedle`
- `model-loading -> story-api, scenegraph, glrender, ast, util, collada, collada-schema-1-4-1`
- `netbeans -> story-api, story-api-migration, models, scenegraph, glrender, ast, tweedle, util`
- `installer -> alice-ide`
- `ide-nonfree -> ide, story-api-nonfree, resources-nonfree`
- `story-api-nonfree -> story-api, models-nonfree`
- `models-nonfree -> story-api, util`

See the Mermaid/DOT files for a renderable graph.

## Size and hotspot inventory

Java files and line counts exclude `target` generated output.

| Module | Java files | Approx. LOC | Notes |
| --- | ---: | ---: | --- |
| `core/ide` | 1545 | 168490 | Largest module; UI/editor integration hotspot. |
| `core/story-api` | 505 | 60436 | Public API and implementation surface. |
| `core/croquet` | 408 | 46705 | UI framework dependency for IDE modules. |
| `core-nonfree/story-api-nonfree` | 748 | 42245 | Large generated/resource-style nonfree API surface. |
| `core/util` | 410 | 41392 | Shared utility base used broadly. |
| `core/ast` | 208 | 24981 | AST and VM foundations. |
| `core/models` | 343 | 24437 | Resource/model catalog. |
| `core/glrender` | 121 | 19138 | Rendering bridge to JOGL. |
| `core/scenegraph` | 174 | 16512 | Scenegraph primitives. |
| `core/story-api-migration` | 37 | 10967 | Small file count but migration monolith hotspot. |

Largest non-target Java sources observed:

| LOC | File |
| ---: | --- |
| 5915 | `core/story-api-migration/src/main/java/org/lgna/project/migration/ProjectMigrationManager.java` |
| 1843 | `core/glrender/src/main/java/edu/cmu/cs/dennisc/render/joglrenderer/NonCachingTextRenderer.java` |
| 1767 | `core/model-loading/src/main/java/org/lgna/story/resourceutilities/ModelResourceExporter.java` |
| 1329 | `core/story-api/src/main/java/org/lgna/ik/core/enforcer/TightPositionalIkEnforcer.java` |
| 1260 | `core/ide/src/main/java/org/alice/stageide/sceneeditor/StorytellingSceneEditor.java` |
| 1242 | `core/scenegraph/src/main/java/edu/cmu/cs/dennisc/scenegraph/io/ASG.java` |
| 1226 | `core/glrender/src/main/java/edu/cmu/cs/dennisc/render/gl/imp/Graphics2D.java` |
| 1203 | `core/model-loading/src/main/java/org/lgna/story/resourceutilities/JointedModelColladaExporter.java` |
| 1194 | `core/ast/src/main/java/org/lgna/project/virtualmachine/VirtualMachine.java` |
| 1114 | `core/croquet/src/main/java/org/lgna/croquet/AbstractComposite.java` |

## Bug-hunt verdict summary

| Category | Verdict | Status | Evidence anchor |
| --- | --- | --- | --- |
| Structural bug | FAIL | CONFIRMED | Optional NetBeans nonfree classpath mappings point to module directories that do not exist. |
| Stale documentation | FAIL | CONFIRMED | README clone sequence conflicts with later `${alice3}` checkout-root commands. |
| Dead code path | FAIL | CONFIRMED | `MODULE_OUTPUTS` paths for optional nonfree artifacts are unreachable under current module names. |
| Size hotspot | NEEDS_ATTENTION | RISK | Migration manager is 5915 LOC and string-pattern-heavy. |
| Refactor risk | NEEDS_ATTENTION | RISK | Startup path combines crash detection, FlatLaf, JOGL, Swing, JavaFX, root-directory, and heap monitoring. |
| Packaged integration | NEEDS_ATTENTION | RISK | NetBeans NBM configuration still enables Pack200 under the Java 21 baseline. |

## Validated findings

### 1. Structural bug / dead path: NetBeans optional nonfree classpath lookup points at missing module directories

Verdict: **FAIL**  
Status: **CONFIRMED**

Evidence:

- `netbeans/src/test/java/org/alice/netbeans/Alice3ProjectTemplateAntSmokeTest.java:36` defines `models-nonfree` and `story-api-nonfree` as optional library artifacts.
- `netbeans/src/test/java/org/alice/netbeans/Alice3ProjectTemplateAntSmokeTest.java:119-148` resolves each artifact by checking `MODULE_OUTPUTS` first and then falling back to jars on the test classpath; optional artifacts are not added to the missing list.
- `netbeans/src/test/java/org/alice/netbeans/Alice3ProjectTemplateAntSmokeTest.java:222-223` maps:
  - `models-nonfree` to `../core-nonfree/models/target/classes`
  - `story-api-nonfree` to `../core-nonfree/story-api/target/classes`
- Actual source modules are `core-nonfree/models-nonfree` and `core-nonfree/story-api-nonfree`, declared in `pom.xml:691-695`; the POM dependencies also use `models-nonfree` and `story-api-nonfree` in `netbeans/pom.xml:303-310`.
- Filesystem validation: `core-nonfree/models` and `core-nonfree/story-api` are missing; `core-nonfree/models-nonfree` and `core-nonfree/story-api-nonfree` exist.

Impact:

The smoke test can silently skip optional nonfree classpath entries because they are optional and the direct module-output paths are dead. This can mask NetBeans library packaging drift for Sims-enabled builds.

Recommended fix path:

Update the two test path mappings to `../core-nonfree/models-nonfree/target/classes` and `../core-nonfree/story-api-nonfree/target/classes`, then run the NetBeans test slice with and without `-DincludeSims=false`.

### 2. Stale documentation: README clone instructions use `${alice3}` as both destination and working directory

Verdict: **FAIL**  
Status: **CONFIRMED**

Evidence:

- `README.md:21` says to clone the repository into local directory `${alice3}`.
- `README.md:23-24` then shows `cd ${alice3}` followed by `git clone --recurse-submodules https://github.com/rysweet/alice3-modernization.git`.
- Later commands treat `${alice3}` as the repository root, for example `README.md:49-51`, `README.md:70-71`, and `README.md:132-137`.

Impact:

Following the clone sequence literally creates a nested `alice3-modernization` checkout below `${alice3}`, but later commands assume `${alice3}` is the checkout root. This is documentation drift, not source behavior.

Recommended fix path:

Clarify whether `${alice3}` is the parent directory or the checkout directory, and make the clone command consistent with subsequent `cd ${alice3}` examples.

### 3. Dead/legacy integration path risk: NetBeans NBM packaging still enables Pack200

Verdict: **NEEDS_ATTENTION**  
Status: **RISK**

Evidence:

- `pom.xml:90` pins NetBeans to `RELEASE180`.
- `netbeans/pom.xml:430-442` configures `org.apache.netbeans.utilities:nbm-maven-plugin:14.2`.
- `netbeans/pom.xml:440` sets `<installerPack200Enable>true</installerPack200Enable>`.

Impact:

Pack200 was removed from modern JDKs, while this repository builds with Java 21 per `pom.xml:74-99` and `README.md:11-17`. If the NBM plugin path still attempts Pack200 work under Java 21, NetBeans packaging can fail or depend on plugin compatibility behavior. This is an integration risk; it should be validated in the NetBeans packaging job before changing behavior.

Recommended fix path:

Run the NetBeans packaging target under Java 21 and decide whether the Pack200 flag is still needed for `nbm-maven-plugin` 14.2.

### 4. Size hotspot: project migration logic is a high-risk monolith

Verdict: **NEEDS_ATTENTION**  
Status: **RISK**

Evidence:

- `core/story-api-migration/src/main/java/org/lgna/project/migration/ProjectMigrationManager.java` is approximately 5915 LOC.
- The file imports migration AST helpers and story/model resource types near `ProjectMigrationManager.java:45-53`.
- It builds XML/string migration patterns directly near `ProjectMigrationManager.java:58-120`.

Impact:

Project migration is behavior-critical for opening old Alice projects. Large, string-heavy migration logic is a refactor risk because small edits can alter compatibility with historical project files. Any change here should be preceded by characterization tests over representative project versions.

Recommended fix path:

Add characterization coverage before extracting helpers. Prefer table-driven or data-backed migration steps only after preserving current migration outputs.

### 5. Refactor risk: startup crosses Swing, JavaFX, native rendering, crash detection, and root-directory configuration

Verdict: **NEEDS_ATTENTION**  
Status: **RISK**

Evidence:

- `alice-ide/src/main/java/org/alice/stageide/EntryPoint.java:75-150` handles crash detection, FlatLaf, JOGL native initialization, Swing event queue setup, `StageIDE`, heap monitoring, and JavaFX launch.
- `alice-ide/pom.xml:172-181` wires `org.alice.stageide.EntryPoint` and sets `org.alice.ide.rootDirectory` for Maven exec.
- `core/util/src/main/java/edu/cmu/cs/dennisc/app/ApplicationRoot.java:53-87` treats missing or invalid `org.alice.ide.rootDirectory` as fatal via `System.exit(-1)`.
- `README.md:102-119` documents the same root-directory and module-open options for IntelliJ runs.

Impact:

Startup behavior depends on build packaging, IDE configuration, root-directory layout, native libraries, Swing threading, and JavaFX initialization. Refactors that separate launcher concerns or adjust runtime layout can break local dev and packaged runs unless both entrypoint and documented launch configurations are updated together.

Recommended fix path:

Keep launcher changes small and test both `mvn exec:java -Dalice-ide` and documented IDE launch settings. Consider characterization tests around `LaunchConfiguration` and root-directory resolution before changing fatal startup behavior.

## Observations without immediate source action

- TODO/deprecated markers are concentrated in `core`; a targeted grep counted hundreds of TODO/FIXME/HACK/deprecated hits under Java/POM/README files, but most are maintenance debt rather than validated bugs.
- `core-nonfree/resources-nonfree`, `core/resources`, `core/i18n`, and `external/collada-schema-1-4-1` have little or no checked-in Java source outside generated/build/resource content. Treat LOC metrics for those modules separately from resource payload size.
- Broad Maven validation should initialize `tweedle-lang` first. The required grammar files were present during this scan: `tweedle-lang/Grammar/TweedleLexer.g4` and `tweedle-lang/Grammar/TweedleParser.g4`.

## Likely files to modify in follow-up work

No source files were modified for this atlas. If the findings are acted on later, likely touch points are:

- `netbeans/src/test/java/org/alice/netbeans/Alice3ProjectTemplateAntSmokeTest.java` for the optional nonfree module-output paths.
- `README.md` for the clone command wording.
- `netbeans/pom.xml` only after validating whether Pack200 is still active or harmful under Java 21.
- `core/story-api-migration/src/main/java/org/lgna/project/migration/ProjectMigrationManager.java` only behind characterization tests.
- `alice-ide/src/main/java/org/alice/stageide/EntryPoint.java`, `core/util/src/main/java/edu/cmu/cs/dennisc/app/ApplicationRoot.java`, and launch docs only if startup/root-directory behavior is intentionally changed.

## Guardrail notes

- No upstream issue or pull request activity was performed.
- No upstream issue database was used.
- No source files were copied into `drinkme`.
- No application/source code was changed.
