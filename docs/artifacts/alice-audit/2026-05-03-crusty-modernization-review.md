# Crusty-old-engineer modernization review

Date: 2026-05-03

Scope: independent proxy review of current Alice modernization workstreams, test/refactor strategy, class-size/coverage targets, risks, and likely overreach. This is a decision-support artifact, not merge approval.

## Bottom line

The current direction is useful but too easy to overrun its guardrails. The strongest work is the narrow characterization-first stream around project IO, resource archive handling, Tweedle submodule diagnostics, and NetBeans packaging smoke tests. The weak spot is measurement discipline: this checkout has 455,429 tracked `src/main/java` lines, only 37 tracked Java test files, no visible coverage gate in the Maven/CI surfaces I inspected, and a pile of branch/worktree noise that can make "parallel progress" look more mature than it is.

Do not broaden into large-scale refactors, class-size crusades, or coverage percentage promises yet. Keep the lane boring: one behavior seam, one characterization test, one small extraction, one focused validation, then stop.

## Evidence

### Repository/build facts

- `README.md:11-18` requires Java 21, Maven 3.9.9+, git, git-lfs, and Install4J only for installers.
- `README.md:26-43` documents the `tweedle-lang` submodule and the required `tweedle-lang/Grammar/TweedleLexer.g4` and `TweedleParser.g4` files.
- `README.md:49-72` says normal build/test entry points are `mvn compile install` and `mvn test`.
- `README.md:124-140` describes `-DincludeSims=false` as useful but still experimental.
- `AGENTS.md:7-18` forbids using upstream issue tracking/pushing, requires baseline compatibility, requires characterization tests before refactoring, and requires initializing `tweedle-lang` before broad Maven validation.
- Root `pom.xml:74-99` sets Java 21 and core dependency versions; `pom.xml:101-126` defines a multi-module Maven reactor spanning `core`, `external`, `alice-ide`, and `netbeans`.
- Root `pom.xml:510-519` configures Surefire/JUnit 4.7 support; `pom.xml:562-585` wires Checkstyle into `validate`; `pom.xml:530-547` includes OpenRewrite static analysis configuration.
- `core/tweedle/pom.xml:61-73` has an explicit Maven enforcer rule for the Tweedle grammar files; `core/tweedle/pom.xml:89-107` generates ANTLR sources from `../../tweedle-lang/Grammar`.

### CI/test facts

- `.github/workflows/alice-test-ci.yml:13-33` checks out submodules recursively and runs `mvn -DincludeSims=false -Dinstall4j.skip clean test`.
- `.github/workflows/alice-netbeans-package-ci.yml:32-52` builds only the NetBeans package with `-DskipTests`, then verifies package artifacts by file/jar contents.
- `.github/workflows/alice-checkstyle-ci.yml:9-27` runs Checkstyle on push, but uses `actions/checkout@v2` without an explicit submodule setting.
- `hooks/pre-push:1-19` runs git-lfs pre-push and Maven Checkstyle.
- Targeted search of root `pom.xml`, `.github`, `hooks`, `README.md`, and `AGENTS.md` found no `jacoco`, `coverage`, `cobertura`, or `pitest` references. So coverage targets are currently aspirational unless an untracked/external lane owns them.

### Size/test metrics from this checkout

Metric method:

Tracked `git ls-files '*.java'` entries were classified by `/src/main/java/` and `/src/test/java/`, excluding `target`.

Observed metrics:

- Java files: 5,003 total.
- Main source Java files: 4,342.
- Test Java files: 37.
- Other tracked Java files outside standard main/test source layout: 624.
- Main source LOC: 455,429.
- Source files over 500 LOC: 52.
- Source files over 1,000 LOC: 12.
- Largest source file: `core/story-api-migration/src/main/java/org/lgna/project/migration/ProjectMigrationManager.java` at 5,914 lines.
- Other >1,000 LOC hot spots include `NonCachingTextRenderer.java` 1,842, `ModelResourceExporter.java` 1,766, `TightPositionalIkEnforcer.java` 1,328, `StorytellingSceneEditor.java` 1,259, `ASG.java` 1,241, `Graphics2D.java` 1,225, `JointedModelColladaExporter.java` 1,202, `VirtualMachine.java` 1,193, `AbstractComposite.java` 1,113, `Jama/Matrix.java` 1,055, and `DragAdapter.java` 1,039.
- Test distribution by module/package is concentrated in `core/util`, `core/tweedle`, `core/ide`, `core/story-api-migration`, `core/ast`, `core/story-api`, `core/model-loading`, `alice-ide`, and `netbeans`. Large areas still have no visible test coverage.

### Current workstream signals

Branch refs and recent commit subjects show many narrow lanes, but the local branch tips are mostly historical or stale relative to `develop` in this checkout:

- `loop62-*`: IO errors, JSON A3C/resource reads, model resource reads, NetBeans compiler structure, project recovery, resource identity.
- `loop63-*`: default backup copy, file/URI project loader, JSON model IO, JSON type version, manifest decoder errors, NetBeans library surrogate, recovery error plan, XML resource identity.
- `loop64-*`: backup directory collision, generated story call, missing/unknown JSON resources, launcher runtime, NetBeans Ant smoke, NetBeans library artifacts, project load plan, save failure surface, submodule diagnostics, type manifest errors, XML entry safety.
- `develop` currently points at `cb8973df0f Add NetBeans project Ant smoke test`, with the recent history dominated by characterization and seam-extraction commits.
- `git worktree list --porcelain` currently shows only the main `develop` checkout and `worktrees/feat/alice-code-atlas-bughunt`; the loop62/63/64 lanes are branch refs, not active local worktrees.
- `git rev-list --left-right --count develop...<branch>` reports the local loop62/63 branch tips and most local loop64 branch tips as behind `develop` and ahead by `0`. A few `origin/loop64-*` refs still show one commit ahead while also behind `develop`, so those need explicit reconciliation before anyone treats them as fresh merge candidates.

Worktree hygiene matters:

- Current `git status --short` groups as 4 `drinkme` artifacts, 2 `.claude/runtime` files, 68 `runs/real-alice-launch-smoke/...` runtime/cache/prefs files, plus 3 other non-review paths.
- The current `drinkme` artifact set contains this review and code-atlas investigation artifacts. That is the right place for durable review evidence; it is not a reason to merge raw runtime state.
- `git submodule status tweedle-lang` reported `f6fc9e5ac116fc42924f46bf6de76a6bc037fa98 tweedle-lang (0.11-46-gf6fc9e5)`, and `tweedle-lang/Grammar` exists in this checkout.

## Findings

### 1. Parallel workstreams are productive, but the local refs are now stale-looking bookkeeping

The branch names look nicely sliced, but the local loop branches are behind `develop` and ahead by `0`. That means they are either already integrated, superseded, or stale. Treating them as active merge candidates would be cargo-cult process. Treating them as irrelevant would also be lazy, because their topics still describe the seams being modernized.

The real risk is not "can these branches merge?" The real risk is losing the validation story behind a sequence of related project IO/resource/archive/NetBeans changes.

Recommendation: treat loop62/63/64 lanes as historical workstream records unless a human explicitly reopens one. Before more work proceeds on the same seam, require a short lane note that says whether the old branch was merged, superseded, or abandoned, and which tests now protect the behavior on `develop`.

### 2. Characterization-first is the right strategy; refactor-first would be reckless

The recent history is full of commits like "Characterize ...", "Extract ... plan", and "Add ... smoke test." That matches `AGENTS.md:11-12`: preserve current baseline behavior and add characterization tests before refactoring. Good. Keep doing that.

The skeptical bit: characterization tests can become a fig leaf if they are too narrow or assert implementation trivia. A test that only proves a seam exists is not enough to justify changing archive IO, project loading, generated code, or backup behavior.

Recommendation: every refactor touching project persistence, resource archives, generated code, or loader classification needs at least one behavior-level before/after characterization test and one negative/error-path test if the branch claims error handling.

### 3. Class-size targets should be used as triage, not as a scorecard

There are 52 source files over 500 LOC and 12 over 1,000 LOC. Chasing "reduce all classes below N lines" would be busywork and a regression factory. Some large files are math/rendering/vendor-ish or central framework types; shrinking them for aesthetics is overreach.

The one obvious outlier is `ProjectMigrationManager.java` at 5,914 LOC. It is not automatically wrong because it is large, but it is too large to modify casually. Any modernization there needs characterization around real migration inputs, not "split file until the metric is green."

Recommendation: use class size only as a risk multiplier. A class-size target is acceptable only when tied to a behavior seam, a defect, or a testability bottleneck. Otherwise pause.

### 4. Coverage targets are currently not operational

I found Surefire and Checkstyle, but no visible Jacoco/coverage tooling in the inspected Maven/CI/docs surfaces. With 4,342 main source Java files and 37 test files, a percentage target would be theater unless instrumentation and baselines exist.

Recommendation: do not promise repository-wide coverage percentages yet. First establish module-level coverage measurement for the lanes under active modernization, then gate changed seams on meaningful characterization breadth.

### 5. The no-Sims path is useful but not a complete confidence signal

CI uses `-DincludeSims=false`, and README explicitly calls the no-Sims path experimental. That is pragmatic for speed and licensing/assets. It is not full Alice behavior validation.

Recommendation: no-Sims Maven test/package is a baseline gate, not a release-quality gate. Anything touching resource loading, model export/import, gallery assets, or runtime launch should have a second validation story that explains whether Sims/nonfree assets are intentionally excluded.

### 6. Worktree/runtime artifacts are a governance risk

The staged `runs/real-alice-launch-smoke/...` cache/prefs files are evidence that real launch smoke work happened, but they should not be confused with durable review artifacts or source changes. Runtime caches in branch state make review noisy and can accidentally fossilize machine-local state.

Recommendation: keep real-launch evidence summarized under `drinkme` or another agreed investigation-artifact path, not as raw cache trees. Do not merge runtime cache/prefs blobs without explicit maintainer approval.

## Risks and overreach

| Risk | Evidence | Skeptical assessment | Gate |
|---|---|---|---|
| Stale branch/worktree confusion | `git worktree list --porcelain` shows only `develop` and `feat/alice-code-atlas-bughunt` worktrees, while many loop62/63/64 branch refs remain behind `develop` and ahead by `0` | "Parallel" is now partly an illusion; stale refs can trigger duplicate or contradictory work | Reopen a lane only after documenting whether the old branch was merged, superseded, abandoned, or still has a remote-only delta |
| Refactor without behavior lock | `AGENTS.md` requires characterization tests before refactor; current tests are sparse relative to code size | Easy to accidentally codify implementation detail while missing user-visible behavior | Require behavior-level characterization plus negative-path test for changed persistence/loader/archive code |
| Class-size metric gaming | 52 main source files >500 LOC, 12 >1,000 LOC, one 5,914 LOC outlier; `checkstyleSuppression.xml:7-12` suppresses the two biggest FileLength offenders | Cutting files by line count alone will create worse architecture | Only allow class-size work when tied to a named seam, defect, or testability blocker |
| Coverage theater | No visible coverage tooling; 37 test files for 4,342 main source files | Repository-wide percentages would be fake precision | First add measurement/baseline for active modules; gate changed code by tests that fail before fix/refactor |
| False confidence from no-Sims CI | CI runs `-DincludeSims=false`; README calls no-Sims experimental | Good fast gate, incomplete product gate | Use no-Sims for baseline; require explicit nonfree/Sims risk statement for model/resource/gallery changes |
| Tweedle submodule fragility | README and `core/tweedle/pom.xml` both call out grammar dependency | Broad Maven validation fails for bad checkout state, not necessarily code quality | Check `git submodule status tweedle-lang` and grammar presence before broad Maven conclusions |
| Runtime artifact pollution | 68 staged `runs/...` files, mostly caches/prefs | Reviewers may miss real source changes or merge machine-local state | Block merge while runtime/cache files are staged unless explicitly approved as artifacts |

## Actionable gating criteria

Use these as proceed/pause/re-scope checks.

### Repository hygiene gate

Proceed only if:

- `git status --short --untracked-files=no` contains no staged or modified files outside the intended source/test/docs/artifact set.
- Runtime caches, local prefs, `.claude/runtime`, and raw `runs/...` blobs are absent from merge candidates unless the maintainer explicitly approves them as artifacts.
- No branch pushes to `upstream-source` and no planning references upstream Alice issues for modernization tracking.

Pause if dirty state obscures which files are part of the lane.

### Submodule/build gate

Proceed only if:

- `git submodule status tweedle-lang` reports an initialized commit.
- `test -d tweedle-lang/Grammar` passes.
- The branch records whether validation used full Maven, no-Sims Maven, or targeted module tests.

Pause if Maven failures mention missing Tweedle generated/parser classes before blaming branch logic.

### Characterization/refactor gate

Proceed only if:

- Every behavior-changing refactor has a characterization test that would have failed or protected the previous behavior boundary.
- Persistence/archive/loader/error-handling lanes include at least one negative-path test when they claim safer failures.
- Tests are in the module owning the behavior, not only in a downstream smoke test.

Re-scope if the branch changes behavior and the only validation is compile/checkstyle.

### Parallel workstream reopen/merge gate

Proceed only if each lane has:

- A named owner/scope.
- A base commit and current rebase target.
- A state: merged into `develop`, superseded by another lane, abandoned, or actively reopened.
- A list of dependent loop branches or "none, verified by diff/history."
- Commands run after rebasing.
- A short "what behavior can regress?" note.

Pause if two lanes touch the same project IO/resource/archive/generated-code seam without an integration plan, or if a stale worktree is used as fresh evidence.

### Class-size gate

Proceed with class-size reduction only if:

- The target file is over 500 LOC and is actively blocking testability, comprehension of a current seam, or safe defect repair.
- The branch states the behavior seam being isolated.
- The diff preserves public API/serialization/project compatibility unless the behavior change is explicitly documented and tested.

Re-scope if the goal is "make the class smaller" rather than "make this behavior safer to test/change."

### Coverage gate

Proceed only if:

- The branch avoids repository-wide coverage claims until coverage tooling/baselines are added.
- For touched modules, the maintainer can name the important behaviors now covered and the remaining blind spots.
- Any future percentage target is module-scoped, measured by CI, and tied to changed seams.

Pause if coverage is discussed only as a percentage with no tooling, no baseline, or no behavior map.

### Product confidence gate

Proceed from CI-green to merge-candidate only if:

- No-Sims CI is green for normal lanes.
- NetBeans/package lanes also run the package verification path.
- Resource/model/gallery/launch lanes state whether full-assets or real-launch validation was run, skipped, or blocked.

Re-scope if a lane changes asset/resource handling but only validates a pure unit seam.

## Recommended next high-value targets

Priority is based on risk reduction per unit of work, not architectural elegance.

1. **Clean and formalize workstream artifacts**

   Create a lightweight `drinkme` index for loop62/63/64 lanes: branch name, scope, base, dependent lanes, validation commands, and state (`merged`, `superseded`, `abandoned`, `reopened`, or `remote-only delta`). This is boring governance, which is exactly why it matters. Evidence: many loop branch refs still exist, most local tips are behind `develop`/ahead by `0`, a few remote loop64 refs still show one ahead commit, and the topics share IO/resource/NetBeans seams.

2. **Add module-scoped coverage measurement before setting coverage targets**

   Start with active modules: `core/story-api-migration`, `core/model-loading`, `core/ide`, `core/tweedle`, and `netbeans`. Do not gate on percentages yet; first produce baselines and identify blind seams. Evidence: no visible Jacoco/coverage tooling in inspected build/CI docs, 37 test files versus 4,342 main source files.

3. **Stabilize project IO/resource archive negative-path tests**

   Consolidate the existing JSON/XML/resource identity/error branches around a shared test matrix: missing entry, unknown resource, future version, corrupt manifest, path traversal/unsafe entry, and UUID identity. Evidence: loop62/63/64 branches repeatedly touch JSON/XML resource identity, missing/unknown resources, manifest errors, and archive entry safety.

4. **Turn project load/save/recovery plans into explicit seam contracts**

   The "Extract ... plan" commits are promising. The next target is not more extraction; it is contract clarity: input state, output decision, failure surface, and user-visible consequence. Evidence: project recovery/load/save branches span backup adoption, load success/failure dispatch, save target plan, save failure propagation, URI loader classification, and backup directory collisions.

5. **Put guardrails around `ProjectMigrationManager.java` before touching it**

   At 5,914 LOC, this file is a high-risk modernization target. First target should be fixture inventory and characterization around representative migration paths. Do not split it yet. Evidence: it is the largest source file by a wide margin and sits in `core/story-api-migration`, an active modernization area with existing tests.

6. **Separate real-launch smoke evidence from raw runtime state**

   Preserve launch-smoke findings as a concise artifact, not as cache/prefs blobs. Evidence: current tracked/staged state includes 68 `runs/real-alice-launch-smoke/...` runtime files, including Mesa/OpenJFX caches and Java prefs.

7. **Fix CI asymmetry deliberately**

   Decide whether Checkstyle CI should use submodules like test/package CI does, or document why it intentionally does not need them. Evidence: test and NetBeans workflows use recursive submodules; Checkstyle workflow uses checkout v2 without explicit submodules.

## Codebase context summary

1. **Relevant existing code and patterns**

   This is a Java 21, Maven 3.9.9 multi-module application. The core modernization pattern currently visible is characterization-first work around project IO, resource archive identity/error handling, launcher configuration, Tweedle grammar/submodule handling, and NetBeans project/package smoke tests. That is the right bias for a legacy educational IDE. The bad version would be broad cleanup without behavior locks.

2. **Files that will likely need modification**

   For this review task, only `drinkme/2026-05-03-crusty-modernization-review.md` should change. Future work should mostly modify module tests first: `core/story-api-migration/src/test/java/**`, `core/model-loading/src/test/java/**`, `core/ide/src/test/java/**`, `core/tweedle/src/test/java/**`, `alice-ide/src/test/java/**`, and `netbeans/src/test/java/**`. Source files should only follow after the characterization/refactor gate passes, especially around `ProjectMigrationManager.java`, resource exporters/loaders, project load/save/recovery seams, launcher configuration, and NetBeans library/template packaging.

3. **Dependencies and integration points**

   The main integration points are Maven reactor profiles (`includeSims`, `buildInstaller`), Tweedle ANTLR generation from `tweedle-lang/Grammar`, Surefire/JUnit test execution, Checkstyle validation, NetBeans NBM/package generation, JavaFX/JOGL/FlatLaf runtime launch, and optional Sims/nonfree modules. No-Sims CI is useful. It is not full product confidence for resource/model/gallery behavior.

4. **Potential conflicts or considerations**

   The biggest conflict is stale branch state masquerading as active parallel work. The next biggest is measurement overreach: class-size and coverage targets are not useful until tied to tested seams and CI-measured baselines. Runtime launch evidence currently appears as raw `runs/...` cache/prefs files; that should remain blocked from merge unless explicitly approved as an artifact. Checkstyle has a `FileLength` rule, but existing suppressions for large files mean class-size governance is already exception-based, not a clean enforceable target.

## Likely files that should change next

For this review task, only this artifact under `drinkme` should be modified.

For future modernization lanes, likely modification surfaces are:

- `drinkme/**` for workstream manifests, review notes, and validation summaries.
- `.github/workflows/**` only if adding measurable gates or fixing CI asymmetry.
- Module tests under `core/*/src/test/java/**`, `alice-ide/src/test/java/**`, and `netbeans/src/test/java/**` for characterization.
- Source files only after the characterization/refactor gate passes, especially around `core/story-api-migration`, `core/model-loading`, `core/ide`, `core/tweedle`, and `netbeans`.

## Non-approval statement

This review does not approve merging any branch. It argues for preserving the current characterization-first momentum while tightening gates around merge order, validation evidence, runtime artifact hygiene, and measurement claims.
