# Restarted full-scope Alice modernization status

Last updated: 2026-05-07

## Campaign state

- Loop 64 recovery/integration is **closed**.
- The recovered source and support-tool work that passed review was integrated.
- The restarted modernization wave integrated Alice PRs #35, #36, #37, #38, #39, #40, #42, #43, #44, #45, and #46; drinkme PR #4; and eatme PR #6.
- Artifact-only work tracks were preserved in `drinkme`; they are not Alice runtime/source changes.
- The original full-scope Alice modernization remains **open**. Do not treat Loop 64 recovery closure as modernization completion.

## Active workstreams

| Workstream | Owner repo | Status |
| --- | --- | --- |
| Alice source modernization | `rysweet/RabbitHole` | Open: continue characterization-first source work behind local checks and CI. |
| Eatme real-Alice user QA | `rysweet/eatme` | Open: continue lesson/persona/scenario smoke coverage against real Alice evidence. |
| Supporting-tool readiness | `gadugi-agentic-test` and related tooling | Open as needed: fix harness/tool defects only when they block evidence-producing Alice or eatme work. |
| Code-atlas / formal-spec / crusty review inputs | `rysweet/drinkme` | Open read-only inputs: use recovered findings to choose and review high-value seams. |
| Drinkme status and artifact reconciliation | `rysweet/drinkme` | Open: keep issue/status artifacts current as each work round changes state. |

## Current PR status

| Work item | Plain status |
| --- | --- |
| [RabbitHole PR #154](https://github.com/rysweet/RabbitHole/pull/154) | Merged. Records that Alice put the Run panel into the Run window area. |
| [RabbitHole PR #155](https://github.com/rysweet/RabbitHole/pull/155) | Merged. Records launcher steps and no-go messages, but does not prove rendering. |
| [RabbitHole PR #156](https://github.com/rysweet/RabbitHole/pull/156) | Merged. Keeps old image recovery while safely rejecting unsupported old code. |
| [RabbitHole PR #159](https://github.com/rysweet/RabbitHole/pull/159) | Merged at `9dbf0266ad7d61439f5dd74121e744dbbd365462`. Adds a generated archive test where a missing Tweedle source entry fails clearly; it does not add broad Tweedle decode support. |
| [RabbitHole PR #160](https://github.com/rysweet/RabbitHole/pull/160) | Merged at `18c533efdacc7bdefa971c82ac655d5127bc743e`. Adds `desktop-run-pixel-boundary.json` with `status: "not_observed"`; it does not prove pixels, screenshots, visible rendering, or grading. |
| [RabbitHole PR #163](https://github.com/rysweet/RabbitHole/pull/163) | Merged at `4f225f2795c79f84c367874cd7995dc6dcded22f`. Rejects unsupported manifest-declared Tweedle type names with a clear error instead of silently dropping a type; it does not add full Tweedle decode support. |
| [RabbitHole PR #164](https://github.com/rysweet/RabbitHole/pull/164) | Merged at `fb3e419b81c55b0e055711c9b57d3143f4f69f10`. Adds a generated archive test for constructor-bearing sibling Tweedle type rejection; it does not add full Tweedle decode support. |
| [RabbitHole PR #166](https://github.com/rysweet/RabbitHole/pull/166) | Merged at `bb617171524fa11d59b71b77a0d29d1b645e2507`. Adds a generated archive test for a sibling Tweedle type with an unsupported complex field initializer; it does not add full Tweedle decode support. |
| [RabbitHole PR #167](https://github.com/rysweet/RabbitHole/pull/167) | Merged at `4c5e2f21b2674f07176df40f90ded35e5738bde3`. Adds `desktop-run-pixel-observation.json` so a run records a screenshot and center pixel when possible, or records a blocker code and component state when not; it does not prove visible rendering, desktop save-menu completion, grading, creative assessment, or first-lesson completion. |
| [RabbitHole PR #168](https://github.com/rysweet/RabbitHole/pull/168) | Merged at `da0fb851fd974721a630811873f0d583a853eb5e`. Adds a generated archive test for a sibling Tweedle type with an unresolved parent; it does not add full Tweedle decode support. |
| [RabbitHole PR #169](https://github.com/rysweet/RabbitHole/pull/169) | Merged at `0a0d182c139aeaf5bc7c2c45213a0392cf8f245c`. Adds machine-readable blocker details to `desktop-run-pixel-observation.json`; it does not prove visible rendering, desktop save-menu completion, grading, creative assessment, or first-lesson completion. |
| [RabbitHole PR #170](https://github.com/rysweet/RabbitHole/pull/170) | Merged at `7e58f46b5b1d9624dd54bf1d2367243349ce8a28`. Falls back from the raw Run display target to the attached Run panel for pixel sampling while preserving exact blockers; it does not prove visible rendering correctness. |
| [RabbitHole PR #171](https://github.com/rysweet/RabbitHole/pull/171) | Merged at `34a48d0b24ebf933925ad6237afaa4ca7518fd99`. Rejects resource-typed Tweedle field initializers instead of accepting them as plain strings; it does not add full Tweedle decode support. |
| [RabbitHole PR #172](https://github.com/rysweet/RabbitHole/pull/172) | Merged at `e0c199ab88d10f635d4f3e9e5d67553fb1fd3f4f`. Adds `desktop-first-lesson-next-action.json` naming the missing Save-menu and code/procedure action targets; it does not prove full Alice UI automation, visible rendering correctness, desktop save-menu completion, grading, creative assessment, or first-lesson completion. |
| [eatme PR #89](https://github.com/rysweet/eatme/pull/89) | Merged. Improves instructor and student readiness reports, but does not grade work or prove full lesson completion. |
| [eatme PR #92](https://github.com/rysweet/eatme/pull/92) | Merged at `cfe1f9e364d0015a3f97e237a9de5af670ae3bd6`. Documents the RabbitHole evidence needed before first-lesson readiness can be marked ready. |
| [eatme PR #93](https://github.com/rysweet/eatme/pull/93) | Merged at `f5c08aea14c679124afc680fc9bc9e155da237dd`. Lists the concrete readiness evidence categories in the report; it does not create new runtime proof. |
| [eatme PR #95](https://github.com/rysweet/eatme/pull/95) | Merged at `d29e3d80112dbd6d2f820ceb8989c61c5e7de7b9`. Reports `desktop-run-pixel-boundary.json` as missing, invalid, or `not_observed`; it does not prove pixels, visible rendering, grading, or first-lesson completion. |
| [eatme PR #96](https://github.com/rysweet/eatme/pull/96) | Merged at `9d765fec2d8f9f3a029b5222d48b3de23b461d5b`. Adds an `evidence_progress` summary that counts required first-lesson evidence as present, missing, invalid, not observed, or blocked; it summarizes existing evidence only. |
| [eatme PR #98](https://github.com/rysweet/eatme/pull/98) | Merged at `11c8c58a33b2c6c7ec93e1b4a057c375e0dbb70f`. Shows first-lesson readiness progress and each required evidence item in plain text output; it does not create new runtime proof or prove first-lesson completion. |
| [eatme PR #99](https://github.com/rysweet/eatme/pull/99) | Merged at `5e8ba4b8c970d04b410060e90c22a613430e202b`. Reports `desktop-run-pixel-observation.json` beside readiness progress, including observed screenshot/sample data or blocked component state and blocker codes; it does not prove visible rendering or first-lesson completion. |
| [eatme PR #101](https://github.com/rysweet/eatme/pull/101) | Merged at `546dfc7c2cdbc5ca6c4526fe3e90bb9f717999ed`. Shows explicit next-action evidence in first-lesson plain output; it does not add new runtime proof. |
| [eatme PR #102](https://github.com/rysweet/eatme/pull/102) | Merged at `3e183407e247944831a6f7ff44870c71169302f4`. Adds the `media-audio-cue-storyboard` student scenario for `media-audio-creator` and generated adapter; it does not grade student work or prove lesson completion. |
| [eatme PR #118](https://github.com/rysweet/eatme/pull/118) | Merged at `2c760511eeff8c554b17ee550e779e7c51444591` from head `b70048d78f0b5f8669dc7e725cdac6b1ff3566f5`. Improves Alice window action diagnostics. CI passed, and the manual real Alice smoke check was skipped. A real desktop environment still needs proving, and later procedure edit, run, and save automation remains incomplete. |
| [eatme PR #120](https://github.com/rysweet/eatme/pull/120) | Merged at `f526544014ee8d368a623359f6bf97cce6588f7d`. Adds the next first-lesson action reporting/proof slice. Real desktop proof is still needed; procedure edit/run/save UI automation is incomplete; manual real Alice smoke was skipped. |
| [eatme PR #121](https://github.com/rysweet/eatme/pull/121) | Merged at `4ade2a5d6def4d7ad7be7691b9349a3f5c9ff61e`. Improves real desktop proof reporting/status, but actual real desktop proof/manual Alice smoke, procedure edit/run/save UI automation, project save, and full first-lesson completion remain incomplete. |
| [RabbitHole PR #219](https://github.com/rysweet/RabbitHole/pull/219) | Merged at `144081e1067cd8795666e5ee8802f47fbfefe671`. Decodes empty no-argument Tweedle constructors to AST `NamedUserConstructor`; constructor parameters and constructor bodies still failed clearly at that point. |
| [RabbitHole PR #222](https://github.com/rysweet/RabbitHole/pull/222) | Merged at `f749ed7cc92f7df4678e96bbb29bcbd0b09913b8`. Proves `SaveProjectOperation.fire(UserActivity)` reaches `AbstractSaveOperation.perform`, but the non-desktop proof lacks `StageIDE.getActiveInstance()`. |
| [RabbitHole PR #224](https://github.com/rysweet/RabbitHole/pull/224) | Merged at `1a3eae6937a7109f3608112a7fb40519e1a4f8d7`. Proves JavaFX cannot open `DISPLAY` locally; visible rendering correctness remains unproven. |
| [RabbitHole PR #225](https://github.com/rysweet/RabbitHole/pull/225) | Merged at `db44c10bd017a5b7cc8eddc1cc82b1d1b90c8fb8`. Decodes required Tweedle constructor parameters to AST `UserParameter`; optional constructor parameters still fail clearly. |
| [RabbitHole PR #229](https://github.com/rysweet/RabbitHole/pull/229) | Merged at `7953c8348272298e9cb85f2319fba6520ba51a32`. Decodes required parameters for empty `void` Tweedle methods to AST `UserParameter`; optional method parameters still fail clearly. |
| [RabbitHole PR #230](https://github.com/rysweet/RabbitHole/pull/230) | Merged at `31d506f6af59ef736ccefad9aa7b793b3add6a3d`. Proves Save action invocation under Xvfb with `status=action_invoked`, `StageIDE=true`, and `ProjectDocumentFrame=true`; menu click, dialog display/control, selected path automation remain unproven, and completed save remains unproven. |
| [RabbitHole PR #231](https://github.com/rysweet/RabbitHole/pull/231) | Merged at `622748401fe8ff00d81d3a2851faac153585b76c`. Observes generated launcher Xvfb marker pixels; real Alice desktop pixels were not observed because `mvn exec:java -Dalice-ide` fails with `org.alice.stageide.EntryPoint` `ClassNotFoundException`. |
| [RabbitHole PR #234](https://github.com/rysweet/RabbitHole/pull/234) | Merged at `45d937fbe1e9ddee74e7c2b89af31841fb38a202`. Decodes single primitive-literal Tweedle `return` method bodies to AST `ReturnStatement`; full method decode and full Tweedle/player decode support remain unproven. |

The proof boundary remains a narrow Run window attachment signal: Alice put the
Run panel into the Run window area. This evidence does not prove pixels were
drawn, does not prove the lesson finished, and is not grading.

RabbitHole PR #212 adds Save dialog/control target evidence and passed focused
Save tests, focused review, and GitHub build, coverage, test, package-netbeans,
and GitGuardian checks. RabbitHole PR #214 proves launcher drawing surface
readiness through `Stage.show()` and `isShowing()` and adds a
`render-target-unavailable` no-go path. RabbitHole PR #215 decodes empty `void`
Tweedle methods to AST `UserMethod`. RabbitHole PR #216 adds Save dialog
discovery target evidence. RabbitHole PR #218 adds launcher render observation
proof, but visible pixels remain unobserved. eatme PR #118 improves Alice window
action diagnostics; CI passed, and the manual real Alice smoke check was skipped.
eatme PR #120 adds the next first-lesson action reporting/proof slice, and eatme
PR #121 improves real desktop proof reporting/status. These changes do not prove
live desktop Save menu click, actual Save dialog display/control, selected path
automation, full Alice UI automation, visible rendering correctness, desktop
save-menu completion, grading, creative assessment, learner-world grading,
first-lesson completion, procedure UI invocation, real desktop proof, project
save, deployed installer success, full world execution, or complete player/full
Tweedle decode support. A real desktop environment still needs proving for eatme,
and procedure edit, run, and save automation remains incomplete.

RabbitHole PR #219 decodes empty no-argument Tweedle constructors to AST
`NamedUserConstructor`. PR #222 proves `SaveProjectOperation.fire(UserActivity)`
reaches `AbstractSaveOperation.perform`, but lacks `StageIDE.getActiveInstance()`.
PR #224 proves JavaFX cannot open `DISPLAY` locally. PR #225 decodes required
constructor parameters to AST `UserParameter`. PR #229 decodes required
parameters for empty `void` Tweedle methods to AST `UserParameter`. PR #230
proves Save action invocation under Xvfb with `status=action_invoked`,
`StageIDE=true`, and `ProjectDocumentFrame=true`. PR #231 observes generated
launcher Xvfb marker pixels, while real Alice desktop pixels are blocked by
`org.alice.stageide.EntryPoint` `ClassNotFoundException`. PR #234 decodes single
primitive-literal Tweedle `return` method bodies to AST `ReturnStatement`. These
changes do not prove full Alice UI automation, visible rendering correctness,
desktop save-menu completion, grading, creative assessment, learner-world
grading, first-lesson completion, procedure UI invocation, completed save, real
Alice desktop pixels, or full Tweedle/player decode support.

eatme PR #92 now documents the RabbitHole evidence needed before first-lesson
readiness can be marked ready: launch evidence, Run-window evidence, desktop
execution evidence, screenshot/log/window artifacts, and
`ui-action-contract.json`. This does not prove full Alice UI automation,
creative assessment, learner-world grading, visible rendering correctness, or
first-lesson completion.

RabbitHole PR #159 adds a generated archive failure test for a missing Tweedle
source entry. RabbitHole PR #160 records a pixel-proof boundary with
`status: "not_observed"`. eatme PR #93 lists the readiness evidence categories
in the output. These changes do not prove full Alice UI automation, visible
rendering, desktop save-menu completion, grading, creative assessment, or
first-lesson completion.

RabbitHole PR #163 rejects unsupported manifest-declared Tweedle type names with
a clear error instead of silently dropping a type. eatme PR #95 reports
`desktop-run-pixel-boundary.json` as missing, invalid, or `not_observed`. These
changes do not prove full Alice UI automation, visible rendering, desktop
save-menu completion, grading, creative assessment, or first-lesson completion.

RabbitHole PR #164 adds the matching generated archive test for a
constructor-bearing sibling Tweedle type. eatme PR #96 adds a compact
first-lesson progress summary. These changes make remaining work easier to see;
they do not prove full Alice UI automation, visible rendering, desktop
save-menu completion, grading, creative assessment, or first-lesson completion.

RabbitHole PR #166 adds a generated archive test for a sibling Tweedle type with
an unsupported complex field initializer. RabbitHole PR #167 adds
`desktop-run-pixel-observation.json`, which records a screenshot and center pixel
when possible, or a blocker code and component state when not. eatme PR #98 shows
first-lesson readiness progress in plain text output. These changes make
evidence easier to inspect; they do not prove full Alice UI automation, visible
rendering, desktop save-menu completion, grading, creative assessment, or
first-lesson completion.

RabbitHole PR #168 adds a generated archive test for a sibling Tweedle type with
an unresolved parent. RabbitHole PR #169 adds machine-readable blocker details to
`desktop-run-pixel-observation.json`. eatme PR #99 reports that pixel
observation file beside readiness progress. These changes make the current
blocker easier to inspect; they do not prove full Alice UI automation, visible
rendering, desktop save-menu completion, grading, creative assessment, or
first-lesson completion.

RabbitHole PR #170 improves pixel observation fallback to the attached Run panel.
RabbitHole PR #171 rejects resource-typed Tweedle field initializers instead of
accepting them as strings. RabbitHole PR #172 adds a no-go next-action file that
names the missing Save-menu and code/procedure action targets. eatme PR #101
shows explicit next-action evidence, and eatme PR #102 adds a media/audio student
scenario. These changes make the next work clearer; they do not prove full Alice
UI automation, visible rendering, desktop save-menu completion, grading,
creative assessment, or first-lesson completion.


- Latest source/eatme/CI wave status is tracked in
  `docs/atlas/journal/0093-source-eatme-ci-wave-status.md`.
  RabbitHole PRs #173 through #184 merged: procedure UI and Save-menu missing
  action records are clearer, desktop Run status summary reporting is clearer,
  several Tweedle/archive edge cases fail with better paths, and RabbitHole CI
  timing notes record Checkstyle 0:53, GitGuardian 0:01, NetBeans 6:01, tests
  7:13, and coverage 11:54 with coverage longest. eatme PRs #105, #106, and
  #108 through #116 merged: student artifact sharing, classroom gallery walk,
  teacher community sharing, curriculum sequence remix, persona inventory,
  instructor/student mission inventory, plain readiness wording, and docs-only CI
  handling are now recorded. The eatme audit at
  `b79ff7b96961bfdf9082a1609c8f86194f7429eb` found 34 canonical scenarios, 35
  Gadugi scenarios, 69 total scenario YAML files, 24 personas, 33 scenarios with
  both instructor and student personas, baseline-only `real-alice-launch-smoke`,
  and 18 docs pages in MkDocs navigation. This completes eatme local
  instructor/student persona coverage, student docs, Gadugi adapters, and plain
  readiness output for now, but it does not prove full Alice UI automation,
  visible rendering correctness, desktop save-menu completion, grading, creative
  assessment, learner-world grading, first-lesson completion, a deployed sharing
  platform, or full Tweedle decode support.
- Previous RabbitHole source/CI wave status is tracked in
  `docs/atlas/journal/0094-rabbithole-source-ci-wave-status.md`.
  RabbitHole PR #185 merged model resource array grouping, skip behavior, and
  duplicate index rejection tests. PR #187 merged narrow `TextString label <- null`
  parsing and decoding to `NullLiteral`. PR #188 merged `ProcedureTabSelection`,
  tests, and a reference doc as a design and test boundary, not live procedure
  invocation. PR #190 merged `IssueReportWorker` non-retryable failure tests.
  PR #191 restored the Maven cache fallback, fixed the stuck coverage path, and
  left coverage run `25492250204` plus develop checks after PR #190 successful.
  PR #187, PR #188, and PR #190 were delayed by stuck coverage behavior and
  transient `jogamp.org` network failures.
- Latest RabbitHole source evidence is tracked in
  `docs/atlas/journal/0095-rabbithole-pr207-pr208-source-evidence.md`.
  RabbitHole PR #207 merged Numeric and Boolean Tweedle `null` field initializer
  decoding to AST `NullLiteral` while still rejecting primitive statement
  contexts such as `if(null)` and `while(null)`. RabbitHole PR #208 records Save
  operation completion evidence; its head before merge was
  `153f4e4ce77415d42e6f1047abcc2074671ae4c8`, all GitHub checks passed, and it
  merged at `8799854787655ca61b6fad9378377b19d41aa7b1`. The 70 percent aggregate
  coverage target, live procedure invocation, desktop edit command, desktop
  save-menu completion, dialogs, grading, rendering, first-lesson completion,
  deployed sharing, and full Tweedle/player decode support remain unproven.
- Latest RabbitHole source wave status is tracked in
  `docs/atlas/journal/0096-rabbithole-pr209-pr210-pr211-source-wave-status.md`.
  RabbitHole PR #209 merged literal sized Tweedle array field initializer support
  such as `new WholeNumber[2]`; non-literal sizes still fail clearly, and broader
  array expressions, method and constructor bodies, non-literal initializers,
  non-null resource initializers, complete player decode, and full Tweedle decode
  remain unproven. RabbitHole PR #210 adds a launcher/runtime proof beyond the
  earlier `Program.main` null-Stage guard; visible rendering, deployed installer
  success, and full world execution remain unproven. RabbitHole PR #211 adds
  focused story-api keyboard event characterization tests; reported
  `core/story-api` coverage moved from 4.55% to 6.21%, adding 260 covered lines.
  The 70 percent aggregate coverage target, manual QA gaps, and smoke checks that
  still need manual approval remain unproven.

## Latest integrated evidence

- Coverage tooling now exists through a reporting-only JaCoCo profile and CI artifact baseline.
- Project IO/load-save has new archive fixture, backup, save-to-backup, cancellation, and JSON/XML manifest fallback characterization.
- Outside-in Alice desktop QA scenarios now cover open/load/save, package/install smoke, and wizard/palette/completion contracts at the scenario level.
- NetBeans export coverage now uses a populated `Alice3Library` classpath contract with JavaFX artifacts and install/package smoke assertions.
- Generated Story API Java coverage now includes loop, foreach, iterable, local, method, parameter, conditional, and story API call compile characterization; stale cached `COUNT__` foreach item names are repaired while explicit item names are preserved.
- Starter project `.a3p` archives now have XML fallback readability coverage using committed fixtures.
- Croquet palette layout and scenegraph model behavior have new headless characterization tests; scenegraph `Joint` bounds/scale bugs exposed by tests were fixed.
- Public no-Sims builds now guard against nonfree library leakage, and includeSims builds explicitly overwrite the no-Sims `Alice3Library.xml` when authorized.
- Eatme now has expanded instructor/student prompt assets, Alice.org-grounded lesson smoke scenarios, gadugi adapters, and split validation modules below the 500-line target.
- Formal high-risk data-loss Gherkin scenarios are recorded in drinkme as specified behavior, with implementation status separated from completion claims.
- The merged source PRs above keep the proof boundary narrow: RabbitHole PR
  #154 records only the Run window attachment signal; RabbitHole PR #155
  records launcher steps and no-go messages, but does not prove rendering; and
  eatme PR #89 does not grade work or prove full lesson completion.
- The merged eatme PR #92 records the evidence categories RabbitHole must supply
  before first-lesson readiness can be marked ready. It documents the
  requirement; it is not the runtime proof.
- The merged RabbitHole PR #159 records one clear archive failure boundary, not
  broad Tweedle decode support.
- The merged RabbitHole PR #160 records that pixel and screenshot proof were not
  observed by the Run-window attachment signal.
- The merged eatme PR #93 makes required readiness evidence visible in output;
  it does not create new runtime evidence.
- The merged RabbitHole PR #163 turns one silent archive loss case into a clear
  error for unsupported manifest-declared Tweedle type names.
- The merged eatme PR #95 reports the pixel-boundary file state explicitly as
  missing, invalid, or `not_observed`; it does not add pixel proof.
- The merged RabbitHole PR #164 adds constructor-bearing sibling archive coverage
  for the same clear-failure behavior.
- The merged eatme PR #96 makes readiness progress countable without adding new
  runtime proof.
- The merged RabbitHole PR #166 adds complex-initializer sibling archive coverage
  for the same clear-failure behavior.
- The merged RabbitHole PR #167 adds a pixel observation file that records an
  observation when possible and a clear blocker when not.
- The merged eatme PR #98 shows readiness progress in plain text without adding
  new runtime proof.
- The merged RabbitHole PR #168 adds unresolved-parent sibling archive coverage
  for the same clear-failure behavior.
- The merged RabbitHole PR #169 adds blocker details to the pixel observation
  file without proving visible rendering.
- The merged eatme PR #99 reports the pixel observation file without adding new
  runtime proof.
- The merged RabbitHole PR #170 improves pixel observation fallback without
  proving visible rendering correctness.
- The merged RabbitHole PR #171 adds resource-initializer clear-failure coverage,
  not full Tweedle decode support.
- The merged RabbitHole PR #172 records the next blocked UI action targets.
- The merged eatme PR #101 shows next-action evidence in plain output without
  adding runtime proof.
- The merged eatme PR #102 adds one media/audio student scenario without grading
  student work.
- The merged RabbitHole PR #185 adds model resource array grouping, skip behavior,
  and duplicate index rejection tests without proving 70 percent aggregate coverage.
- The merged RabbitHole PR #187 adds narrow `TextString label <- null` support and
  keeps broader null/player/Tweedle decode work open.
- The merged RabbitHole PR #188 adds `ProcedureTabSelection` as a design and test
  boundary, not live procedure invocation.
- The merged RabbitHole PR #190 adds `IssueReportWorker` non-retryable failure tests;
  transient `jogamp.org` failures delayed CI until rerun.
- The merged RabbitHole PR #191 restores the Maven cache fallback and fixes the stuck
  coverage path; coverage run `25492250204` completed successfully.
- The merged RabbitHole PR #209 supports literal sized Tweedle array field initializers
  such as `new WholeNumber[2]`, while non-literal sizes still fail clearly.
- The merged RabbitHole PR #210 adds launcher/runtime proof beyond the earlier
  `Program.main` null-Stage guard without proving rendering, installer success, or
  full world execution.
- The merged RabbitHole PR #211 adds story-api keyboard event characterization tests;
  reported `core/story-api` coverage moved from 4.55% to 6.21% with 260 more
  covered lines, while the 70 percent aggregate coverage target and manual QA gaps remain.

## No-premature-completion rule

Do not mark the Alice modernization complete while any of these remain true:

1. active workstreams above are still open;
2. characterization coverage is still below the modernization target;
3. real UI/story/export/load-save journeys remain unproven;
4. local checks or GitHub Actions have not passed for the integrated source state;
5. `drinkme` has not recorded the evidence, limits, and next work.

Closure requires evidence, not a recovered artifact count or a single successful loop.


### Latest merged source/eatme wave links

- https://github.com/rysweet/RabbitHole/pull/173
- https://github.com/rysweet/RabbitHole/pull/174
- https://github.com/rysweet/RabbitHole/pull/175
- https://github.com/rysweet/RabbitHole/pull/176
- https://github.com/rysweet/RabbitHole/pull/177
- https://github.com/rysweet/RabbitHole/pull/178
- https://github.com/rysweet/RabbitHole/pull/179
- https://github.com/rysweet/RabbitHole/pull/180
- https://github.com/rysweet/RabbitHole/pull/181
- https://github.com/rysweet/RabbitHole/pull/182
- https://github.com/rysweet/RabbitHole/pull/183
- https://github.com/rysweet/RabbitHole/pull/184
- https://github.com/rysweet/eatme/pull/105
- https://github.com/rysweet/eatme/pull/106
- https://github.com/rysweet/eatme/pull/108
- https://github.com/rysweet/eatme/pull/109
- https://github.com/rysweet/eatme/pull/110
- https://github.com/rysweet/eatme/pull/111
- https://github.com/rysweet/eatme/pull/112
- https://github.com/rysweet/eatme/pull/113
- https://github.com/rysweet/eatme/pull/114
- https://github.com/rysweet/eatme/pull/115
- https://github.com/rysweet/eatme/pull/116

### Latest RabbitHole source/CI wave links

- https://github.com/rysweet/RabbitHole/pull/185
- https://github.com/rysweet/RabbitHole/pull/187
- https://github.com/rysweet/RabbitHole/pull/188
- https://github.com/rysweet/RabbitHole/pull/190
- https://github.com/rysweet/RabbitHole/pull/191

## Latest RabbitHole source/CI wave details

| Work item | Plain status |
| --- | --- |
| [RabbitHole PR #185](https://github.com/rysweet/RabbitHole/pull/185) | Merged at `713758374d0b6e937ec3f1471a78d7c95f69a35a`. Adds model resource array grouping, skip behavior, and duplicate index rejection tests; 70 percent aggregate coverage and the oversized-file goal remain open. |
| [RabbitHole PR #187](https://github.com/rysweet/RabbitHole/pull/187) | Merged at `7bc8f2991ddc45708203682bd5edeb7a2d990c40`. Adds narrow `TextString label <- null` support to `NullLiteral`; broader null/player/Tweedle decode work remains open. |
| [RabbitHole PR #188](https://github.com/rysweet/RabbitHole/pull/188) | Merged at `39085aaed5cb042ad5260adfcc6d4c4e1dcda9d7`. Adds `ProcedureTabSelection`, tests, and a reference doc; live procedure invocation and desktop edit flow remain open. |
| [RabbitHole PR #190](https://github.com/rysweet/RabbitHole/pull/190) | Merged at `fd71bfb96fe9c82aa4cdd3de8f967f7c410af629`. Adds `IssueReportWorker` non-retryable failure tests; transient `jogamp.org` failures delayed CI until rerun, and 52 Java files over 500 lines were reported by the latest hotspot count. |
| [RabbitHole PR #191](https://github.com/rysweet/RabbitHole/pull/191) | Merged at `aac8fa55b96c32cd797c98c016c0ae4e598ffc3a`. Restores the Maven cache fallback and fixes the stuck coverage path; coverage run `25492250204` and develop checks after PR #190 completed successfully. |

## Latest merged source/eatme wave details

| Work item | Plain status |
| --- | --- |
| [RabbitHole PR #173](https://github.com/rysweet/RabbitHole/pull/173) | Merged at `e20d4eb411c8afb3c326ee585807afd1b3ab29e9`. Records a procedure UI action no-go artifact and names the missing desktop code/procedure UI target; no desktop UI invocation is proven. |
| [RabbitHole PR #174](https://github.com/rysweet/RabbitHole/pull/174) | Merged at `fc0d941fa22686c216e973ea535db6869bc48835`. Records Save-menu action target no-go evidence; save-menu completion remains unproven. |
| [RabbitHole PR #175](https://github.com/rysweet/RabbitHole/pull/175) | Merged at `2642e9139fb73cfd6d00585d285d03e671c2bbf7`. Adds desktop Run status summary evidence; visible rendering correctness and full UI automation remain unproven. |
| [RabbitHole PR #176](https://github.com/rysweet/RabbitHole/pull/176) | Merged at `c0c2ef5d6a30237d5a8a7e3c0a23a42f16c480f8`. Makes a missing sibling Tweedle entry fail clearly. |
| [RabbitHole PR #177](https://github.com/rysweet/RabbitHole/pull/177) | Merged at `54d021e3457e6f9250547ec8693f7e491e4b8507`. Clarifies desktop Run evidence status summary wording. |
| [RabbitHole PR #178](https://github.com/rysweet/RabbitHole/pull/178) | Merged at `5123f03640d7166e30b6160c107e92c78c0f9728`. Makes unnamed unsupported manifest Tweedle sibling types fail clearly using the archive path. |
| [RabbitHole PR #179](https://github.com/rysweet/RabbitHole/pull/179) | Merged at `0a25c2f17849f944cf5e14f10c26d3be48524d1a`. Documents RabbitHole CI timing notes only: Checkstyle 0:53, GitGuardian 0:01, NetBeans 6:01, tests 7:13, coverage 11:54; coverage was longest. |
| [RabbitHole PR #180](https://github.com/rysweet/RabbitHole/pull/180) | Merged at `17c0c593baea0046d502c97f20f0f6a19fef2c09`. Clarifies first-lesson desktop evidence reporting. |
| [RabbitHole PR #181](https://github.com/rysweet/RabbitHole/pull/181) | Merged at `2dbd3881c096291c529f491173610e5567f1883a`. Characterizes a JSON archive with a resource-typed field initializer on the manifest program type; no behavior change. |
| [RabbitHole PR #182](https://github.com/rysweet/RabbitHole/pull/182) | Merged at `d436b7a9cd2084b3409017cff8cc3605f43ee2d0`. `desktop-run-status-summary.json` lists the pixel boundary artifact and machine-readable missing procedure UI and `SaveProjectOperation` evidence. |
| [RabbitHole PR #183](https://github.com/rysweet/RabbitHole/pull/183) | Merged at `82527ca0ed04315dd40808a80ca7946a2cd029b4`. Characterizes typed-null Tweedle field initializers; malformed Tweedle and JSON `.a3c` failures include the archive entry path. |
| [RabbitHole PR #184](https://github.com/rysweet/RabbitHole/pull/184) | Merged at `4eb21803bd76bb13bdc75ce53c6f590e3d3597a7`. Documents project-IO and Tweedle covered boundaries and the larger decode gaps that remain. |
| [RabbitHole PR #185](https://github.com/rysweet/RabbitHole/pull/185) | Merged at `713758374d0b6e937ec3f1471a78d7c95f69a35a`. Adds model resource array grouping, skip behavior, and duplicate index rejection tests; 70 percent aggregate coverage remains unproven, and 51 or 52 oversized files remain depending on the measurement point. |
| [RabbitHole PR #187](https://github.com/rysweet/RabbitHole/pull/187) | Merged at `7bc8f2991ddc45708203682bd5edeb7a2d990c40`. Adds narrow Tweedle null support: `TextString label <- null` parses and decodes to `NullLiteral`; `WholeNumber <- null` still fails, and full Tweedle decode support remains unproven. |
| [RabbitHole PR #188](https://github.com/rysweet/RabbitHole/pull/188) | Merged at `39085aaed5cb042ad5260adfcc6d4c4e1dcda9d7`. Adds `ProcedureTabSelection`, tests, and a reference doc; this is not live procedure invocation, desktop edit command completion, Save-menu completion, dialogs, grading, rendering, or first-lesson completion. |
| [RabbitHole PR #190](https://github.com/rysweet/RabbitHole/pull/190) | Merged at `fd71bfb96fe9c82aa4cdd3de8f967f7c410af629`. Adds `IssueReportWorker` non-retryable failure tests; transient `jogamp.org` network failures delayed CI until rerun, 70 percent aggregate coverage is still not claimable, and the latest reported hotspot count is 52 Java files over 500 lines. |
| [RabbitHole PR #191](https://github.com/rysweet/RabbitHole/pull/191) | Merged at `aac8fa55b96c32cd797c98c016c0ae4e598ffc3a`. Restores the Maven cache fallback, fixes the stuck coverage path, and leaves post-merge coverage run `25492250204` plus develop checks after PR #190 successful. |
| [RabbitHole PR #207](https://github.com/rysweet/RabbitHole/pull/207) | Merged at `6d744747a831824378c053713fef4e8a136c25c5`. Adds Numeric and Boolean Tweedle `null` field initializer decoding to AST `NullLiteral`; primitive statement contexts such as `if(null)` and `while(null)` still fail. Full Tweedle/player decode support remains unproven. |
| [RabbitHole PR #208](https://github.com/rysweet/RabbitHole/pull/208) | Merged at `8799854787655ca61b6fad9378377b19d41aa7b1` from head `153f4e4ce77415d42e6f1047abcc2074671ae4c8` after all GitHub checks passed. Records Save operation completion evidence; desktop save-menu completion remains unproven. |
| [RabbitHole PR #209](https://github.com/rysweet/RabbitHole/pull/209) | Merged at `02e50a00078e8ff348aa33b8c8635483f9b817bf`. Supports literal sized Tweedle array field initializers such as `new WholeNumber[2]`; non-literal sizes still fail clearly, and broader array expressions, method and constructor bodies, non-literal initializers, non-null resource initializers, complete player decode, and full Tweedle decode remain unproven. |
| [RabbitHole PR #210](https://github.com/rysweet/RabbitHole/pull/210) | Merged at `d2cba4ba3e349c704765129511de5a062210ec08`. Adds launcher/runtime proof beyond the earlier `Program.main` null-Stage guard; visible rendering, deployed installer success, and full world execution remain unproven. |
| [RabbitHole PR #211](https://github.com/rysweet/RabbitHole/pull/211) | Merged at `9b509aa3e60e6cf60b5e870a3ee03a0a80363f89`. Adds story-api keyboard event characterization tests; `core/story-api` coverage was reported from 4.55% to 6.21%, adding 260 covered lines. The 70 percent aggregate coverage target, manual QA gaps, and smoke checks that still need manual approval remain unproven. |
| [RabbitHole PR #212](https://github.com/rysweet/RabbitHole/pull/212) | Merged at `db72e0cfef8912cd0a92243f1889ae4cd2180535` from head `a84346582aef22c51d3afa33a05df26b62e370c7`. Adds Save dialog/control target evidence. focused Save tests, focused review, and GitHub build, coverage, test, package-netbeans, and GitGuardian checks passed. Live desktop Save menu invocation and actual Save dialog discovery/control remain unproven. |
| [RabbitHole PR #214](https://github.com/rysweet/RabbitHole/pull/214) | Merged at `2155904f38e55323b00d732b7f64e957db4406f5`. Proves launcher drawing surface readiness through `Stage.show()` and `isShowing()` and adds a `render-target-unavailable` no-go path; visible pixels, deployed installer success, and full world execution remain unproven. |
| [RabbitHole PR #215](https://github.com/rysweet/RabbitHole/pull/215) | Merged at `c727d97c3d71a0f045925a691a080a42d36fbe9d`. Decodes empty `void` Tweedle methods to AST `UserMethod`; parameters, method bodies, non-void methods, and constructors still fail clearly. |
| [RabbitHole PR #216](https://github.com/rysweet/RabbitHole/pull/216) | Merged at `c84bdf826723284e84b4872ce2e6c791dee0c8a6`. Adds Save dialog discovery target evidence; live Save menu click, actual dialog display/control, selected path automation, full lesson completion, rendering, and grading remain unproven. |
| [RabbitHole PR #218](https://github.com/rysweet/RabbitHole/pull/218) | Merged at `a568bae3c3960c60792351cfa423450fea51b067`. Adds launcher render observation proof, but visible pixels remain unobserved; deployed installer success and full world execution remain unproven. |
| [eatme PR #105](https://github.com/rysweet/eatme/pull/105) | Merged at `b88afdf60c2dd81a2849878706903f76ab8c2344`. Adds the student artifact sharing mission doc entry. |
| [eatme PR #106](https://github.com/rysweet/eatme/pull/106) | Merged at `320f3c56cd65ec949e9cea0137f72a3dd0200f09`. Consumes RabbitHole desktop-first-lesson next-action evidence in readiness reporting. |
| [eatme PR #108](https://github.com/rysweet/eatme/pull/108) | Merged at `5640df08832cb5a74c8051ec19ff769d6484710b`. Adds the classroom gallery walk QA scenario. |
| [eatme PR #109](https://github.com/rysweet/eatme/pull/109) | Merged at `2c56018f378221748a457b3414a96374d7675185`. Maps teacher community sharing. |
| [eatme PR #110](https://github.com/rysweet/eatme/pull/110) | Merged at `3a6fdf35c69f8e96e4a58ea452446a4e40ca4958`. Makes the readiness heading say evidence files are not proof of full UI automation. |
| [eatme PR #111](https://github.com/rysweet/eatme/pull/111) | Merged at `13458167399bc60ca763fe82d3407ded4418b6e1`. Cancels stale PR-only runs in CI. |
| [eatme PR #112](https://github.com/rysweet/eatme/pull/112) | Merged at `1f137014d7fd2d5fff1706a861cedb0a6d94d323`. Adds the `curriculum-sequence-remix-pack` scenario and generated Gadugi adapter. |
| [eatme PR #113](https://github.com/rysweet/eatme/pull/113) | Merged at `a0dd075d7e5c8e21394836de0e5aa01a15643e41`. Aligns the persona asset docs inventory. |
| [eatme PR #114](https://github.com/rysweet/eatme/pull/114) | Merged at `5f74845722c284eb60bece43e0880a7de23cd888`. Completes the instructor mission inventory: 34 canonical scenarios, 35 Gadugi adapters, 24 personas, and 18 docs pages. |
| [eatme PR #115](https://github.com/rysweet/eatme/pull/115) | Merged at `b79ff7b96961bfdf9082a1609c8f86194f7429eb`. Completes the student mission inventory; docs reference all 33 scenarios with student personas. |
| [eatme PR #116](https://github.com/rysweet/eatme/pull/116) | Merged at `0aa0155d63ee4aa16edba72459e9f3cac47bee27`. Docs/docs-site-only CI skips Rust checks safely; exact time saved awaits a future docs-only PR. |
