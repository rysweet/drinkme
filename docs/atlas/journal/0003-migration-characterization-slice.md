# Journal 0003: project migration characterization slice

## Loop 2 audit inputs

The second modernization loop used structural quality audit, code-atlas bug hunting, QA/spec review, and crusty-old-engineer review before implementation.

Findings that shaped the slice:

- The repo is still sparsely tested: roughly 4,336 tracked production Java files and 16 Java test files before this slice.
- High-risk uncharacterized areas include project migration/load, model/resource export, IDE command journeys, and NetBeans Java-transition behavior.
- `ProjectMigrationManager` is a major oversized file, but it should not be split before its current behavior is characterized.
- Playwright is not a good fit for the Swing/JavaFX IDE at this stage. Headless/unit characterization should come first.
- Gherkin/TLA+ may be useful later for real lifecycle/state-machine seams, but they would be ceremony for this slice.

Crusty-old-engineer recommendation:

- Do not chase 70% coverage or `<500 line classes` mechanically yet.
- Next high-value seam: project version/migration behavior.
- Add conservative characterization tests before touching production migration code.

## Alice implementation commit

Commit in `alice3-modernization`:

- `79d3941e58 Characterize project migration versions`

Changes:

- Extended `core/ast/src/test/java/org/lgna/project/VersionTest.java` with historical Alice version round-trip and comparison behavior.
- Added `core/story-api-migration/src/test/java/org/lgna/project/migration/ProjectMigrationManagerTest.java`.
- Characterized migration table invariants:
  - text migration result versions are valid, round-trippable, and increasing;
  - AST migration result versions are valid, round-trippable, and increasing;
  - migration applicability is true only before the migration result-version threshold;
  - representative legacy story/resource strings are rewritten through the current cumulative migration chain.
- No production code changed.

## Notable behavior captured

- `Version("3.3.0.0.0")` compares equal to `Version("3.3.0.0")` because missing trailing segments are treated like zeroes.
- Prerelease versions compare before matching releases.
- Metadata does not affect version ordering.
- A legacy dresser class migration is cumulative: it does not stop at the first replacement; it reaches `org.lgna.story.resources.prop.DresserResource`.

## Review and validation

Crusty diff review:

- Approved.
- No blockers.
- Confirmed the tests characterize current behavior rather than desired behavior.

Local validation passed:

```bash
mvn -DincludeSims=false -Dinstall4j.skip -pl core/ast,core/story-api-migration -am test
mvn -DincludeSims=false -Dinstall4j.skip clean test
```

Standalone CI started for commit `79d3941e58`:

- Alice Checkstyle CI: `25269757370`
- Alice Test CI: `25269757378`

## Next useful slices

1. Add tiny historical `.a3p` fixture migration tests with explicit provenance and no Sims/nonfree assets.
2. Characterize `FileProjectLoader` load-failure behavior; the atlas bug hunt found an empty `handleLoadException()` path.
3. Replace the commented `ModelExportTest` with a minimal no-Sims model/resource export test.
4. Add NetBeans generated-project characterization tests for the Alice-to-Java bridge.
