# Java, Rust, and language-boundary assessment

Recommendation: keep Alice 3 predominantly Java. Introduce Rust only at optional, isolated edges after characterization tests exist.

## What should remain Java

| Area | Reason |
| --- | --- |
| Desktop IDE and UI | `alice-ide`, `core/ide`, and `StageIDE` are Java desktop/Swing/JavaFX/FlatLaf code with deep lifecycle coupling. |
| NetBeans plugin | The plugin is packaged as `nbm` and depends heavily on NetBeans Java APIs. |
| Rendering integration | `core/glrender` is already integrated with JOGL/GlueGen and Java scenegraph objects. |
| Scenegraph/story API/AST | These object models are deeply Java-shaped and central to current behavior. |
| Tweedle compiler/parser pipeline | Current ANTLR/Jackson/Maven integration is Java-native and already tested in part. |
| Maven/Install4J packaging | The build and installer pipeline is Java-toolchain centered. |

## Where Rust might help later

Rust can be useful if it stays outside the IDE runtime at first:

- standalone asset validation CLI,
- batch model linting,
- project/archive inspection tools,
- fast log/index scanning,
- optional geometry or mesh processing after profiling proves a bottleneck,
- deterministic test-fixture generators.

The safest pattern is a separate CLI/tool crate that reads Alice artifacts and emits reports. Do not put it on the critical IDE startup path initially.

## What not to rewrite now

- NetBeans plugin.
- Swing/desktop workflows.
- JOGL/OpenGL rendering stack.
- Tweedle/AST/story API core.
- Installer packaging.

These areas have high regression risk and low near-term rewrite payoff.

## Migration risks

- JNI/JNA object marshaling across large scene/model graphs.
- Cross-platform native binary packaging.
- Harder debugging for teachers/contributors familiar with Java.
- License and asset-distribution complexity.
- Fragmented build pipeline.
- Reimplementation drift before current behavior is characterized.

## Practical modernization path

1. Build characterization tests around current Java behavior.
2. Refactor Java modules behind clearer package boundaries.
3. Extract pure Java services where possible before considering language changes.
4. Pilot Rust only as optional external tooling.
5. Promote Rust into runtime only with profiling evidence, stable FFI contracts, and cross-platform packaging tests.

