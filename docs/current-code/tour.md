# Current Alice 3 code tour

This tour is derived from the public fork at `/home/azureuser/src/alice3`.

## 1. Repository and Maven topology

Alice 3 is a Java 21, Maven reactor desktop application. The root POM defines the core reactor, external/vendor modules, `alice-ide`, and `netbeans`.

Primary module groups:

- `core/*`: language, AST, IDE core, scenegraph, rendering, resources, story API, model loading.
- `external/*`: vendored or wrapped external libraries.
- `alice-ide`: runnable Alice desktop IDE jar.
- `netbeans`: NetBeans plugin packaged as `nbm`.
- `core-nonfree/*`: nonfree overlays for Sims/gallery resources; not in the root default module list.
- `tweedle-lang`: git submodule containing Tweedle grammar and language assets.

## 2. Application startup

Main entry: `alice-ide/src/main/java/org/alice/stageide/EntryPoint.java`

Startup flow:

1. Create/open `CrashDetector`.
2. Print current project version.
3. Register FlatLaf theme defaults and set Swing look-and-feel.
4. Initialize renderer native libraries before Swing/JavaFX startup.
5. Initialize Swing on the event dispatch thread.
6. Parse command-line arguments for locale, project file, and window geometry.
7. Load `classinfos.json` into `ClassInfoManager`.
8. Construct `StageIDE`.
9. Optionally set a project file to open.
10. Initialize the IDE and show the document frame.
11. Launch JavaFX to satisfy JavaFX initialization.

Important files:

- `alice-ide/pom.xml`: defines `org.alice.stageide.EntryPoint` as the Maven exec main class.
- `core/ide/src/main/java/org/alice/ide/IDE.java`: base IDE shell and document-frame initialization.
- `core/ide/src/main/java/org/alice/stageide/StageIDE.java`: Alice 3 stage-specific IDE behavior.

## 3. IDE shell and stage customization

`IDE` extends `ProjectApplication` and owns:

- default exception handling,
- active locale initialization,
- project document frame initialization,
- perspective changes,
- field accessor/mutator display policy,
- abstract hooks for scene editor and declaration filters.

`StageIDE` adds Alice 3 story/stage behavior:

- connects `StoryApiConfigurationManager`,
- updates the user gallery directory,
- provides `StorytellingSceneEditor`,
- filters generated setup methods,
- registers virtual-machine adapters for scene execution,
- prompts for license acceptance.

## 4. Tweedle language integration

Tweedle is the internal representation of Alice code.

Key files:

- `tweedle-lang/Grammar/TweedleLexer.g4`
- `tweedle-lang/Grammar/TweedleParser.g4`
- `core/tweedle/pom.xml`
- `core/tweedle/src/main/java/org/alice/tweedle/unlinked/TweedleUnlinkedParser.java`
- `core/tweedle/src/main/java/org/alice/tweedle/TweedleLibrary.java`

The `core/tweedle` Maven module runs ANTLR against the grammar submodule and generates Java parser sources under `target/generated-sources/antlr4`.

## 5. Resource and model handling

The runtime expects resources from `core/resources/target/distribution`.

`core/resources/pom.xml` builds a distribution layout:

- copies application resources,
- unpacks JOGL and GlueGen platform natives,
- creates platform-specific resource directories.

Model and resource-related modules:

- `core/models`: gallery model module.
- `core/model-loading`: AST/story API, scenegraph, GL, Collada, glTF, and JAXB integration.
- `core/resources`: application and platform resource distribution.
- `core-nonfree/models-nonfree` and `core-nonfree/resources-nonfree`: restricted gallery/resource overlays.

## 6. Rendering and scenegraph

Rendering is Java-side JOGL/OpenGL integration:

- `core/scenegraph`: scene representation.
- `core/glrender`: rendering implementation and JOGL/GlueGen dependencies.
- `core/resources`: native JOGL/GlueGen unpacking for supported platforms.

This is tightly coupled to Java desktop runtime and native packaging.

## 7. NetBeans plugin

The `netbeans` module packages an Alice plugin as `nbm`.

It depends on NetBeans APIs plus Alice modules including:

- `util`
- `scenegraph`
- `glrender`
- `story-api`
- `ast`
- `story-api-migration`
- `tweedle`
- `models`

Main plugin concerns include:

- project template generation,
- code completion,
- palette integration,
- options/preferences,
- Alice-to-Java transition support.

## 8. Current test layout

Only four modules contain Java test source files:

- `core/util`: math tests, mostly JUnit 5.
- `core/tweedle`: parser/manifest tests, JUnit 4.
- `core/ast`: version tests, JUnit 4.
- `core/model-loading`: active no-Sims model exporter tests for XML serialization and generated resource Java compilation.

The current test suite is useful but not representative of the full application behavior.
