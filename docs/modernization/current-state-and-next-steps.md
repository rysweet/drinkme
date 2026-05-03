# Alice modernization current state and next steps

## Repository state

- Source work is in `rysweet/alice3-modernization` on branch `develop`.
- Private investigation artifacts are in `rysweet/drinkme` on branch `main`.
- Upstream issue/PR usage is prohibited. Findings are journaled in `drinkme`.
- The active source repo has guardrails in `AGENTS.md`.
- Latest source work at the time of this summary included:
  - `c57606b81f Report future versions for JSON player archives`
  - `c1243a39e7 Read player export resources through JSON IO`
  - `259a3d02b6 Characterize image resource save roundtrip`
  - `e12e1b4348 Characterize resource player export boundary`
  - `54b74d2476 Extract project save target plan`

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
- future-version detection for JSON/player archives through the shared `ProjectReader` seam;
- headless editor save-copy archive shape and reload fidelity through `ProjectFileUtilities`;
- AST-referenced image resource editor save-copy and reopen fidelity;
- project save/export snapshot source selection and default auto-backup migration;
- project save target planning for new/default-backup/backup saves;
- NetBeans generated launcher shape and launcher argument handoff;
- NetBeans project-template archive and generated metadata;
- exported build-property contract;
- `Alice3Library` registration and packaging source;
- NetBeans package-phase CI and artifact assertions;
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
- Generated source now includes one actual story API call smoke, `this.setSimulationSpeedFactor(1.5);`, in a new focused test class.
- `ProjectFileUtilities.exportCopyOfProjectTo` now has a headless player artifact smoke for version, manifest, thumbnail, and program Tweedle entries.
- Resource-bearing player export now proves referenced image bytes and manifest metadata are written. `IoUtilities.readProject(...)` now routes manifest-declared `.a3w` archives to `JsonProjectIo` and can restore manifest-listed image resources, but Tweedle program-type decoding is still not implemented.
- JSON/player archives now report future `version.txt` values through `JsonProjectIo.checkForFutureVersion()`, so loader warning behavior is no longer XML-only at that seam.
- `ProjectFileUtilities.saveCopyOfProjectTo` now has a headless editor-save roundtrip smoke for manifest, thumbnail, program XML, resource XML/bytes, and reload fidelity.
- Editor save-copy now has a real `ImageResource` roundtrip: an AST-referenced image resource is written to `resources/picture.png` and reopens with identity and bytes intact.
- `ProjectFileUtilities` now has source-selection tests proving export forces a fresh project snapshot while save-copy uses the normal up-to-date snapshot, plus default backup migration coverage for auto backups.
- `ProjectApplication.saveProjectTo` now delegates its target decision to `ProjectSaveTargetPlan`, giving the oversized application class a characterized save-orchestration seam without changing save order or UI behavior.
- Recent-backup recovery now covers the case where the newest candidate is known unloadable: the next candidate is considered, but still must be newer than the main project to be selected.
- Backup recovery now has a real-file headless path covering corrupt main file, skipped unloadable backup, selected valid backup, failure-plan action, and `FileProjectLoader` resource fidelity.
- The generated foreach loop currently emits `COUNT__` as the item variable when the AST item local has no explicit name.
  - This is internally coherent and compiles when referenced.
  - It remains readability debt for teaching-facing generated Java.
- Explicitly named foreach item locals do emit readable Java names and are now characterized separately from the unnamed fallback.
- Iterable foreach loops over a generated `Arrays.asList(...)` expression compile and import `java.util.Arrays`; the current characterization preserves explicit item local naming.
- Headless tests can cover important exported-code behavior without launching real JavaFX.
- Real JavaFX/UI behavior, story execution, and rendering-adjacent behavior remain mostly unprotected.
- Git LFS budget exhaustion can break CI checkout if no-Sims workflows fetch LFS objects; no-Sims CI should avoid LFS unless a job explicitly needs it.

## Known limits

- Historical `.a3p` migration fixtures are not yet covered.
- Real StageIDE-generated projects, thumbnails, gallery resources, and provenance-sensitive assets remain mostly uncovered.
- The player export artifact smoke uses a synthetic project and 1x1 thumbnail; it does not prove the full StageIDE export UI journey.
- The editor save-copy roundtrip also uses a synthetic project and test resource; it does not prove the full StageIDE save UI journey.
- Model binary export, thumbnails, real gallery resources, and full model package output remain mostly untested.
- Backup recovery dialogs and recursive UI side effects are not directly tested.
- Full wizard execution is not covered.
- Real JavaFX launcher startup is not covered.
- Palette/completion behavior is not covered.
- Deep NBM install semantics are not covered.
- A standalone exported Ant project build/run against a populated `Alice3Library` is not yet proven; current coverage uses a JDK compiler, JavaFX stubs, and a test-classpath surrogate for the NetBeans library.
- Scene/model story API calls, events, and rendering behavior are not yet characterized.
- Player export JSON reads are currently resource-only; the program type is still `null` because the Tweedle decoder remains a stub.
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
5. Use code-atlas bug hunting on the next high-value seam:
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
