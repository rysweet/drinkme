# Refactor vs rewrite recommendation

## Recommendation

Start with a targeted incremental refactor. Do not begin with a wholesale rewrite.

## Why

- The current build passes with Java 21 and Maven.
- Existing educational behavior is broad and under-tested.
- The codebase has deep Java desktop, Swing, JOGL, NetBeans, Maven, and Install4J coupling.
- The website and teaching materials define many implicit product contracts that are not encoded as tests.
- A rewrite now would risk losing behavior that teachers and students rely on.

## Refactor strategy

1. Add characterization tests around current behavior.
2. Extract testable startup/configuration services from `EntryPoint`.
3. Clarify project persistence, model loading, resource lookup, and Tweedle boundaries.
4. Separate restricted asset overlays from open-code behavior in tests and documentation.
5. Add CI that runs tests, not only checkstyle.
6. Use small, module-scoped refactors with atlas updates.

## Rewrite decision gate

Only reconsider a rewrite after:

- project load/save and core teaching journeys are covered,
- NetBeans Java-transition workflow is covered,
- model/resource behavior is covered without restricted fixtures,
- package-level atlas shows which modules are genuinely unsalvageable,
- a prototype demonstrates a simpler replacement for a bounded slice.

