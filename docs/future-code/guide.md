# Envisioned future code guide

The target is not novelty. The target is a codebase that a new contributor, teacher, or student-facing tool builder can understand, test, and safely extend.

## Guiding principles

- Preserve current behavior first; improve structure second.
- Treat educational workflows as product contracts.
- Separate source code from restricted/nonfree assets.
- Prefer Java for the application core until tests and profiling justify a boundary.
- Make every major subsystem independently testable without launching the full IDE.

## Proposed architecture direction

### Application shell

Keep a Java desktop shell, but isolate startup decisions:

- argument parsing,
- locale selection,
- crash detection,
- look-and-feel setup,
- native renderer initialization,
- project-to-open selection.

These should become testable services called by `EntryPoint`, not embedded directly in UI startup code.

### Domain core

Clarify and document stable contracts around:

- AST/project model,
- Tweedle parsing and serialization,
- story API,
- project persistence,
- model/resource metadata,
- scenegraph construction.

### Resource and asset boundary

Create explicit packages or modules for:

- open/free resources,
- nonfree Sims/EA overlays,
- platform-native render resources,
- gallery indexing and lookup.

Every build and test profile should make the asset choice visible.

### Testing boundary

Aim for these layers:

1. pure unit tests for math/parser/version/format logic,
2. fixture-based persistence tests,
3. headless service tests for IDE-adjacent behavior,
4. minimal UI smoke tests,
5. platform/package smoke tests.

### Tooling boundary

External tooling may evolve separately from the Java IDE:

- report generators,
- code atlas generation,
- asset validators,
- fixture builders,
- migration analyzers.

Rust is a good candidate here because these tools can be optional and independently shipped.

## Rewrite vs refactor recommendation

Start with targeted incremental refactoring, not wholesale rewrite.

Reasons:

- The current Maven build passes.
- The project has a large Java/Swing/JOGL/NetBeans surface.
- The highest risk is unknown behavior, not a known impossible architecture.
- Existing website/reference material can seed characterization tests.
- A rewrite before tests would likely lose educational workflows and asset edge cases.

Revisit a rewrite only after:

- current behavior is covered by characterization tests,
- subsystem boundaries are documented,
- hard-to-maintain hotspots are measured,
- a prototype proves a simpler architecture for a bounded slice.

