# Alice modernization current state and next steps

## Repository state

- Source work is in `rysweet/alice3-modernization` on branch `develop`.
- Private investigation artifacts are in `rysweet/drinkme` on branch `main`.
- Upstream issue/PR usage is prohibited. Findings are journaled in `drinkme`.
- The active source repo has guardrails in `AGENTS.md`.
- Latest source work at the time of this summary included:
  - `73ca278621 Handle empty default backup copy`
  - `67fd047b72 Characterize URI project loader path classification`
  - `4fc78d7c88 Add JsonModelIo export format seam test`
  - `5bd75d8c83 Isolate XML resource identity on read`
  - `6bc25da7f0 Characterize JSON type archive version handling`
  - `3ba86b66ad Add explicit manifest decode errors`
  - `eb73ae08c1 Extract project load failure dispatch plan`
  - `38ca0324b4 Characterize NetBeans Alice library classpath`

## Build and CI state

The no-Sims local and CI path is healthy.

Current important gates:

```bash
mvn -DincludeSims=false -Dinstall4j.skip -pl netbeans -am test
mvn -DincludeSims=false -Dinstall4j.skip clean test
mvn checkstyle:check -Dcheckstyle.config.location=checkstyle.xml
mvn -DincludeSims=false -Dinstall4j.skip -pl netbeans -am package -DskipTests
```

GitHub Actions now includes:

- Alice Test CI: no-Sims clean test.
- Alice Checkstyle CI.
- Alice NetBeans Package CI.

The NetBeans package workflow intentionally avoids Git LFS checkout and verifies representative package artifacts:

- one top-level `netbeans-*.nbm`;
- `org-alice-netbeans.jar`;
- `aliceSource.jar`;
- `aliceDocs.zip`;
- `Alice3Library.xml`;
- `layer.xml`;
- `SProgram.java`;
- javadoc overview entry.

## Characterization progress

The work has focused on building a compatibility safety net before broad refactoring.

Covered areas include:

- launch argument parsing;
- project migration/version behavior;
- corrupt project-load failure delegation;
- project backup candidate selection and branch planning;
- backup recovery candidate skipping when a newer backup is known unloadable;
- backup recovery IO path from corrupt files to valid backup load;
- VR project-loader save-path behavior;
- model resource XML metadata, manifest behavior, tag parsing, subresource lookup, and edge cases;
- synthetic `.a3p` project IO round trips;
- synthetic resource IO round trips;
- headless player export archive shape through `ProjectFileUtilities`;
- resource-bearing player export archive boundary and current editor-reader rejection;
- manifest-based JSON reader dispatch and image-resource restoration for player exports;
- JSON/player audio resource restoration through the same resource-only reader boundary;
- future-version detection for JSON/player archives through the shared `ProjectReader` seam;
- explicit corrupt-manifest IO dispatch errors instead of silent XML fallback;
- JSON/player image/audio resource identity isolation when separate archive reads reuse UUIDs;
- JSON/player model/generated type manifest-reference boundaries;
- JSON `.a3c` resource-only type archive reads;
- duplicate-safe and path-safe JSON/player resource zip entries;
- headless editor save-copy archive shape and reload fidelity through `ProjectFileUtilities`;
- AST-referenced image resource editor save-copy and reopen fidelity;
- project save/export snapshot source selection and default auto-backup migration;
- project save target planning for new/default-backup/backup saves;
- NetBeans generated launcher shape and launcher argument handoff;
- NetBeans project-template archive and generated metadata;
- exported build-property contract;
- `Alice3Library` registration and packaging source;
- NetBeans package-phase CI and artifact assertions;
- NetBeans template compiler-surrogate structure;
- generated resource export/runtime loading;
- generated resource filename mismatch, duplicate name, blank name, and unsafe path behavior;
- generated Java source compilation for:
  - empty/minimal program;
  - resource-backed program;
  - non-empty user method;
  - local declaration;
  - method parameter access;
  - user-method invocation;
  - invocation with argument;
  - conditional;
  - count loop;
  - while loop;
  - foreach-array loop;
  - foreach item access;
  - named foreach item access;
  - iterable foreach loop;
  - story API call on `SProgram`.

## Important findings

- Characterization is still early relative to the size of Alice.
- Current coverage is far below the 70% target.
- Many production classes still exceed the desired 500-line target.
- NetBeans Java export is a high-value seam because it is both compatibility-sensitive and teaching-facing.
- Model resource export now has its first active no-Sims characterization, but only for XML serialization and generated resource Java compilation.
- NetBeans export now has a standalone-style compile/launcher smoke, but not a full Ant/NetBeans run with a populated `Alice3Library`.
- NetBeans export now also has a template-shaped project smoke that extracts the packaged template, checks the `Alice3Library` classpath contract, and compiles generated sources into `build/classes` using the test classpath as a surrogate.
- The template-shaped NetBeans compile smoke now verifies the template build/classpath properties and resolves its classes directory from the template rather than hardcoding `build/classes`.
- Generated source now includes one actual story API call smoke, `this.setSimulationSpeedFactor(1.5);`, in a new focused test class.
- `ProjectFileUtilities.exportCopyOfProjectTo` now has a headless player artifact smoke for version, manifest, thumbnail, and program Tweedle entries.
- Resource-bearing player export now proves referenced image bytes and manifest metadata are written. `IoUtilities.readProject(...)` now routes manifest-declared `.a3w` archives to `JsonProjectIo` and can restore manifest-listed image resources, but Tweedle program-type decoding is still not implemented.
- JSON/player export/readback now also covers AST-referenced `AudioResource` with synthetic bytes, preserving UUID, names, content type, byte payload, and normalized duration.
- JSON/player archives now report future `version.txt` values through `JsonProjectIo.checkForFutureVersion()`, so loader warning behavior is no longer XML-only at that seam.
- Corrupt `manifest.json` in IO dispatch now surfaces an `IOException` instead of being treated like an absent manifest and falling through to XML.
- JSON/player resource reads no longer reuse mutable static UUID-map instances for image/audio resources, preventing one archive read from mutating an earlier read with the same UUID.
- JSON/player archives with model and generated type manifest references are characterized as manifest entries, not binary `Resource`s, until Tweedle/model decoding is implemented.
- JSON `.a3c` archives now route to JSON IO, restore manifest-listed resources, and still return `null` type while Tweedle decoding is unimplemented.
- JSON/player export now flattens path-like image resource filenames and allocates distinct `resources`, `resources2`, ... entry directories for duplicate filenames while preserving resource bytes on reopen.
- `ProjectFileUtilities.saveCopyOfProjectTo` now has a headless editor-save roundtrip smoke for manifest, thumbnail, program XML, resource XML/bytes, and reload fidelity.
- Editor save-copy now has a real `ImageResource` roundtrip: an AST-referenced image resource is written to `resources/picture.png` and reopens with identity and bytes intact.
- `ProjectFileUtilities` now has source-selection tests proving export forces a fresh project snapshot while save-copy uses the normal up-to-date snapshot, plus default backup migration coverage for auto backups.
- `ProjectApplication.saveProjectTo` now delegates its target decision to `ProjectSaveTargetPlan`, giving the oversized application class a characterized save-orchestration seam without changing save order or UI behavior.
- Recent-backup recovery now covers the case where the newest candidate is known unloadable: the next candidate is considered, but still must be newer than the main project to be selected.
- Backup recovery now has a real-file headless path covering corrupt main file, skipped unloadable backup, selected valid backup, failure-plan action, and `FileProjectLoader` resource fidelity.
- Project-load success planning now has a pure seam for backup-prompt/open-loader decisions, while UI dialogs and application state mutations remain in `ProjectApplication`.
- The generated foreach loop currently emits `COUNT__` as the item variable when the AST item local has no explicit name.
  - This is internally coherent and compiles when referenced.
  - It remains readability debt for teaching-facing generated Java.
- Explicitly named foreach item locals do emit readable Java names and are now characterized separately from the unnamed fallback.
- Iterable foreach loops over a generated `Arrays.asList(...)` expression compile and import `java.util.Arrays`; the current characterization preserves explicit item local naming.
- Headless tests can cover important exported-code behavior without launching real JavaFX.
- Real JavaFX/UI behavior, story execution, and rendering-adjacent behavior remain mostly unprotected.
- Git LFS budget exhaustion can break CI checkout if no-Sims workflows fetch LFS objects; no-Sims CI should avoid LFS unless a job explicitly needs it.
- Process correction: every coding lane and subagent must follow `DEFAULT_WORKFLOW`; parallel coding should use isolated worktrees/branches, while this main lane remains serialized for integration.
- Loop 62 proved the parallel pattern: six isolated implementation branches were developed concurrently, then rebased and integrated sequentially behind local gates and CI.
- Loop 63 extended that pattern: implementation lanes ran in parallel, but integration remained serialized and CI-gated after each meaningful merge.
- `tweedle-lang` is a required git submodule for `core/tweedle` ANTLR parser generation. Missing it in worktrees causes `TweedleParser`/`TweedleParserBaseVisitor` compile failures; see `docs/build-baseline/submodule-working-guide.md`.
- Recovered artifact-only lanes have been consolidated into `drinkme` rather than Alice source:
  - Crusty modernization review: `docs/artifacts/alice-audit/2026-05-03-crusty-modernization-review.md`.
  - Code-atlas bug-hunt artifacts: `docs/artifacts/alice-audit/code-atlas-alice-source-truth.md`, `docs/artifacts/alice-audit/code-atlas-alice-bughunt-findings.md`, `docs/artifacts/alice-audit/code-atlas-alice-hotspots.md`, `docs/artifacts/alice-audit/code-atlas-alice-staleness-map.md`, and the companion module graphs.
  - Formal save/load/export specification artifacts: `docs/artifacts/alice-audit/formal-spec/evaluation.md`, Gherkin scenarios, TLA+ recovery model/config, and usage/reference notes under `docs/artifacts/alice-audit/formal-spec/`.
- This recovery is a planning/artifact wave only. It preserves evidence for the next parallel modernization wave; it does not claim the Alice modernization mission or source implementation work is complete.

## Known limits

- Historical `.a3p` migration fixtures are not yet covered.
- Real StageIDE-generated projects, thumbnails, gallery resources, and provenance-sensitive assets remain mostly uncovered.
- The player export artifact smoke uses a synthetic project and 1x1 thumbnail; it does not prove the full StageIDE export UI journey.
- The editor save-copy roundtrip also uses a synthetic project and test resource; it does not prove the full StageIDE save UI journey.
- Model binary export, thumbnails, real gallery resources, and full model package output remain mostly untested.
- Backup recovery dialogs and recursive UI side effects are not directly tested.
- Project-load success branching is now tested through `ProjectLoadSuccessPlan`, but the higher-level UI side effects still need characterization.
- Project-load failure dispatch branching is now tested through `ProjectLoadFailureDispatchPlan`, but the higher-level dialog and recursive load UI side effects still need characterization.
- Full wizard execution is not covered.
- Real JavaFX launcher startup is not covered.
- Palette/completion behavior is not covered.
- Deep NBM install semantics are not covered.
- A standalone exported Ant project build/run against a populated `Alice3Library` is not yet proven; current coverage uses a JDK compiler, JavaFX stubs, and a test-classpath surrogate for the NetBeans library.
- Scene/model story API calls, events, and rendering behavior are not yet characterized.
- Player export JSON reads are currently resource-only; the program type is still `null` because the Tweedle decoder remains a stub.
- JSON `.a3c` type reads are also resource-only; the type remains `null` until Tweedle type decoding is implemented.
- XML project reads now avoid static resource instance reuse across archive reads while preserving AST resource-expression binding to decoded resources.
- Default-backup copy now has direct seam coverage for populated, missing, and empty `.defaultbak` directories.
- The generated-source export tests were split so both focused NetBeans export test classes are under 500 lines.

## Immediate next steps

1. Continue project IO/load-save characterization where it protects data-loss seams:
   - complete player export JSON reads beyond resource restoration;
   - backup/save-as behavior with real temporary files;
   - failure/recovery journey branches above the headless selector/plan seams.
2. Continue generated-source characterization where it protects real exported Java behavior:
   - scene/model story API calls that compile against exported project dependencies.
3. Prove exported project behavior beyond compile-only tests:
   - run an actual Ant/NetBeans project build once the required tool/runtime harness is stable;
   - replace the classpath surrogate with a populated `Alice3Library` definition;
   - compile/run the exported launcher against real JavaFX where possible.
4. Add higher-level user journey tests where feasible:
   - export project journey;
   - open/load/save journey;
   - failure/recovery journey;
   - package/install smoke path.
5. Use the recovered code-atlas bug-hunt artifacts on the next high-value seam:
   - NetBeans export path;
   - project IO/load-save path;
   - resource/model path.
6. Keep journaling every slice in `drinkme`.
7. Do not start broad refactors until the affected behavior has characterization coverage.

## Strategic direction

The safest modernization path remains incremental:

1. characterize behavior;
2. fix correctness bugs exposed by characterization;
3. split oversized or tangled tests/classes where safe;
4. refactor production code behind characterization gates;
5. only consider rewrite or non-Java components after enough evidence exists.

Core Alice should remain Java for now. Rust or other languages may be useful later for optional tooling, static analysis, packaging helpers, graphing, or external AI-assisted tools, but moving core runtime behavior out of Java would be premature without much stronger test coverage.
