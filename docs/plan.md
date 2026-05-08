# Alice modernization investigation plan

## Problem

Alice 3 is a valuable educational programming environment with strong public teaching/reference material, but the source code is large, sparsely tested, and hard to maintain. Before refactoring or rewriting, we need a characterization test suite and a durable map of the current system.

## Repository model

- Modernized Alice implementation repo: `https://github.com/rysweet/RabbitHole`
- Public source fork/reference: `https://github.com/rysweet/alice3`
- Upstream source: `https://github.com/TheAliceProject/alice3`
- Private artifact repo: `https://github.com/rysweet/drinkme`

`drinkme` stores only investigation outputs: plans, notes, maps, diagrams, journals, and generated documentation. It must not vendor the Alice source tree.

The active implementation repo is `rysweet/RabbitHole`, not the upstream fork
network. Do not open issues or pull requests against
`TheAliceProject/alice3`; use the RabbitHole repo namespace only.

## Current findings

- Alice 3 is a Java 21/Maven desktop IDE with a NetBeans plugin.
- The documented non-installer build path works locally.
- Baseline command passed: `mvn -DincludeSims=false -Dinstall4j.skip -DskipTests=false test`.
- The RabbitHole modernization repo now has CI running `mvn -DincludeSims=false -Dinstall4j.skip clean test` and a no-Sims NetBeans package check.
- Current test coverage is still small relative to the codebase, but the characterization suite now covers key IO, recovery, and NetBeans generation seams after the first sixty-two modernization slices.
- [RabbitHole PR #154](https://github.com/rysweet/RabbitHole/pull/154)
  records a narrow Run window attachment signal. It proves Alice put the Run
  panel into the Run window area. It does not prove pixels were drawn, does not
  prove the lesson finished, and is not grading.
- [eatme PR #92](https://github.com/rysweet/eatme/pull/92) merged at
  `cfe1f9e364d0015a3f97e237a9de5af670ae3bd6`. eatme now documents the
  RabbitHole evidence needed before first-lesson readiness can be marked ready:
  launch evidence, Run-window evidence, desktop execution evidence,
  screenshot/log/window artifacts, and `ui-action-contract.json`.
- RabbitHole PR #159 merged at
  `9dbf0266ad7d61439f5dd74121e744dbbd365462`. It adds a generated archive test
  where a missing manifest-declared Tweedle source entry fails clearly; it does
  not add broad Tweedle decode support.
- RabbitHole PR #160 merged at
  `18c533efdacc7bdefa971c82ac655d5127bc743e`. It adds
  `desktop-run-pixel-boundary.json` with `status: "not_observed"`; it does not
  prove pixels, screenshots, visible rendering, or grading.
- [RabbitHole PR #163](https://github.com/rysweet/RabbitHole/pull/163) merged at
  `4f225f2795c79f84c367874cd7995dc6dcded22f`. It rejects unsupported
  manifest-declared Tweedle type names with a clear error instead of silently
  dropping a type; it does not add full Tweedle method, constructor,
  complex-value, or missing-parent decode support.
- [RabbitHole PR #164](https://github.com/rysweet/RabbitHole/pull/164) merged at
  `fb3e419b81c55b0e055711c9b57d3143f4f69f10`. It adds the matching generated
  archive test for a constructor-bearing sibling Tweedle type so that case also
  fails clearly; it does not add full Tweedle decode support.
- [RabbitHole PR #166](https://github.com/rysweet/RabbitHole/pull/166) merged at
  `bb617171524fa11d59b71b77a0d29d1b645e2507`. It adds a generated archive test
  for a sibling Tweedle type with an unsupported complex field initializer; it
  does not add full Tweedle method, constructor, complex-value,
  resource-expression, or missing-parent decode support.
- [RabbitHole PR #167](https://github.com/rysweet/RabbitHole/pull/167) merged at
  `4c5e2f21b2674f07176df40f90ded35e5738bde3`. It adds
  `desktop-run-pixel-observation.json` so a run records a screenshot and center
  pixel when possible, or a blocker code and component state when not; it does
  not prove visible rendering, desktop save-menu completion, grading, creative
  assessment, or first-lesson completion.
- [RabbitHole PR #168](https://github.com/rysweet/RabbitHole/pull/168) merged at
  `da0fb851fd974721a630811873f0d583a853eb5e`. It adds a generated archive test
  for a sibling Tweedle type with an unresolved parent; it does not add full
  Tweedle decode support.
- [RabbitHole PR #169](https://github.com/rysweet/RabbitHole/pull/169) merged at
  `0a0d182c139aeaf5bc7c2c45213a0392cf8f245c`. It adds machine-readable blocker
  details to `desktop-run-pixel-observation.json`; it does not prove visible
  rendering, desktop save-menu completion, grading, creative assessment, or
  first-lesson completion.
- [RabbitHole PR #170](https://github.com/rysweet/RabbitHole/pull/170) merged at
  `7e58f46b5b1d9624dd54bf1d2367243349ce8a28`. It falls back from the raw Run
  display target to the attached Run panel for pixel sampling while preserving
  exact blockers; it does not prove visible rendering correctness.
- [RabbitHole PR #171](https://github.com/rysweet/RabbitHole/pull/171) merged at
  `34a48d0b24ebf933925ad6237afaa4ca7518fd99`. It rejects resource-typed Tweedle
  field initializers instead of accepting them as plain strings; it does not add
  full Tweedle decode support.
- [RabbitHole PR #172](https://github.com/rysweet/RabbitHole/pull/172) merged at
  `e0c199ab88d10f635d4f3e9e5d67553fb1fd3f4f`. It adds
  `desktop-first-lesson-next-action.json`, naming the missing deterministic
  Save-menu and code/procedure action targets. It does not prove full Alice UI
  automation, visible rendering correctness, desktop save-menu completion,
  grading, creative assessment, or first-lesson completion.
- eatme PR #93 merged at `f5c08aea14c679124afc680fc9bc9e155da237dd`. It makes
  readiness reports list concrete RabbitHole readiness evidence categories; it
  does not create new runtime proof or prove first-lesson completion.
- [eatme PR #95](https://github.com/rysweet/eatme/pull/95) merged at
  `d29e3d80112dbd6d2f820ceb8989c61c5e7de7b9`. It reports
  `desktop-run-pixel-boundary.json` as missing, invalid, or `not_observed`; it
  does not prove pixels, visible rendering, grading, or first-lesson completion.
- [eatme PR #96](https://github.com/rysweet/eatme/pull/96) merged at
  `9d765fec2d8f9f3a029b5222d48b3de23b461d5b`. It adds an
  `evidence_progress` summary that counts required first-lesson evidence as
  present, missing, invalid, not observed, or blocked. It summarizes existing
  evidence only.
- [eatme PR #98](https://github.com/rysweet/eatme/pull/98) merged at
  `11c8c58a33b2c6c7ec93e1b4a057c375e0dbb70f`. It shows the first-lesson
  readiness progress summary and every required evidence item in plain text
  output. It does not add new runtime proof.
- [eatme PR #99](https://github.com/rysweet/eatme/pull/99) merged at
  `5e8ba4b8c970d04b410060e90c22a613430e202b`. It reports
  `desktop-run-pixel-observation.json` beside readiness progress, including
  observed screenshot/sample data or blocked component state and blocker codes.
  It does not add new runtime proof.
- [eatme PR #101](https://github.com/rysweet/eatme/pull/101) merged at
  `546dfc7c2cdbc5ca6c4526fe3e90bb9f717999ed`. It shows explicit
  `next_action` next-action evidence in first-lesson plain output as
  `fix next: ...`. It does not add new runtime proof.
- [eatme PR #102](https://github.com/rysweet/eatme/pull/102) merged at
  `3e183407e247944831a6f7ff44870c71169302f4`. It adds the
  `media-audio-cue-storyboard` student scenario for `media-audio-creator` and
  its generated adapter. It does not grade student work or prove lesson
  completion.

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
- Previous RabbitHole source evidence is tracked in
  `docs/atlas/journal/0095-rabbithole-pr207-pr208-source-evidence.md`.
  RabbitHole PR #207 merged Numeric and Boolean Tweedle `null` field initializer
  decoding to AST `NullLiteral` while still rejecting primitive statement
  contexts such as `if(null)` and `while(null)`. RabbitHole PR #208 records Save
  operation completion evidence; its head before merge was
  `153f4e4ce77415d42e6f1047abcc2074671ae4c8`, all GitHub checks passed, and it
  merged at `8799854787655ca61b6fad9378377b19d41aa7b1`. The 70 percent aggregate
  coverage target, live procedure invocation, desktop edit command, full desktop
  Save menu completion, dialogs, grading, rendering, first-lesson completion,
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
- [RabbitHole PR #212](https://github.com/rysweet/RabbitHole/pull/212) merged at
  `db72e0cfef8912cd0a92243f1889ae4cd2180535` from head `a84346582aef22c51d3afa33a05df26b62e370c7`. It adds Save
  dialog/control target evidence. The focused Save tests, focused review, and
  GitHub build, coverage, test, package-netbeans, and GitGuardian checks
  passed. Live desktop Save menu invocation and actual Save dialog
  discovery/control remain unproven.
- [eatme PR #118](https://github.com/rysweet/eatme/pull/118) merged at
  `2c760511eeff8c554b17ee550e779e7c51444591` from head `b70048d78f0b5f8669dc7e725cdac6b1ff3566f5`. It improves
  Alice window action diagnostics. CI passed, and the manual real Alice smoke
  check was skipped. A real desktop environment still needs proving, and
  later procedure edit, run, and save automation remains incomplete.
- [RabbitHole PR #214](https://github.com/rysweet/RabbitHole/pull/214) merged at
  `2155904f38e55323b00d732b7f64e957db4406f5`. It proves launcher drawing
  surface readiness through `Stage.show()` and `isShowing()` and adds a
  `render-target-unavailable` no-go path. It does not prove visible pixels,
  deployed installer success, or full world execution.
- [RabbitHole PR #215](https://github.com/rysweet/RabbitHole/pull/215) merged at
  `c727d97c3d71a0f045925a691a080a42d36fbe9d`. It decodes empty `void` Tweedle
  methods to AST `UserMethod`. Parameters, method bodies, non-void methods, and
  constructors still fail clearly.
- [RabbitHole PR #216](https://github.com/rysweet/RabbitHole/pull/216) merged at
  `c84bdf826723284e84b4872ce2e6c791dee0c8a6`. It adds Save dialog discovery
  target evidence. Live Save menu click, actual dialog display/control, selected
  path automation, full lesson completion, rendering, and grading remain
  unproven.
- [RabbitHole PR #218](https://github.com/rysweet/RabbitHole/pull/218) merged at
  `a568bae3c3960c60792351cfa423450fea51b067`. It adds launcher render
  observation proof, but visible pixels remain unobserved. Deployed installer
  success and full world execution remain unproven.
- [eatme PR #120](https://github.com/rysweet/eatme/pull/120) merged at
  `f526544014ee8d368a623359f6bf97cce6588f7d`. It adds the next first-lesson
  action reporting/proof slice. Real desktop proof is still needed; procedure
  edit/run/save UI automation is incomplete; the manual real Alice smoke check
  was skipped.
- [eatme PR #121](https://github.com/rysweet/eatme/pull/121) merged at
  `4ade2a5d6def4d7ad7be7691b9349a3f5c9ff61e`. It improves real desktop proof
  reporting/status, but actual real desktop proof/manual Alice smoke, procedure
  edit/run/save UI automation, project save, and full first-lesson completion
  remain incomplete.
- [RabbitHole PR #219](https://github.com/rysweet/RabbitHole/pull/219) merged at
  `144081e1067cd8795666e5ee8802f47fbfefe671`. Empty no-argument Tweedle
  constructors decode to AST `NamedUserConstructor`; constructor parameters and
  constructor bodies still failed clearly at that point.
- [RabbitHole PR #222](https://github.com/rysweet/RabbitHole/pull/222) merged at
  `f749ed7cc92f7df4678e96bbb29bcbd0b09913b8`. It proves
  `SaveProjectOperation.fire(UserActivity)` reaches
  `AbstractSaveOperation.perform`, but the non-desktop proof lacks
  `StageIDE.getActiveInstance()`.
- [RabbitHole PR #224](https://github.com/rysweet/RabbitHole/pull/224) merged at
  `1a3eae6937a7109f3608112a7fb40519e1a4f8d7`. A real pixel attempt proved
  JavaFX cannot open `DISPLAY` locally; visible rendering correctness remains
  unproven.
- [RabbitHole PR #225](https://github.com/rysweet/RabbitHole/pull/225) merged at
  `db44c10bd017a5b7cc8eddc1cc82b1d1b90c8fb8`. Required Tweedle constructor
  parameters decode to AST `UserParameter`; optional constructor parameters still
  fail clearly.
- [RabbitHole PR #229](https://github.com/rysweet/RabbitHole/pull/229) merged at
  `7953c8348272298e9cb85f2319fba6520ba51a32`. Required parameters for empty
  `void` Tweedle methods decode to AST `UserParameter`; optional method
  parameters still fail clearly.
- [RabbitHole PR #230](https://github.com/rysweet/RabbitHole/pull/230) merged at
  `31d506f6af59ef736ccefad9aa7b793b3add6a3d`. Under Xvfb, Save action
  invocation is proven with `status=action_invoked`, `StageIDE=true`, and
  `ProjectDocumentFrame=true`; menu click, dialog display/control, selected path
  automation remain unproven, and completed save remains unproven.
- [RabbitHole PR #231](https://github.com/rysweet/RabbitHole/pull/231) merged at
  `622748401fe8ff00d81d3a2851faac153585b76c`. Generated launcher Xvfb marker
  pixels were observed; real Alice desktop pixels were not observed because
  `mvn exec:java -Dalice-ide` fails with `org.alice.stageide.EntryPoint`
  `ClassNotFoundException`.
- [RabbitHole PR #234](https://github.com/rysweet/RabbitHole/pull/234) merged at
  `45d937fbe1e9ddee74e7c2b89af31841fb38a202`. Single primitive-literal Tweedle
  `return` method bodies decode to AST `ReturnStatement`; full method decode,
  full player decode, and full Tweedle decode support remain unproven.
- [RabbitHole PR #235](https://github.com/rysweet/RabbitHole/pull/235) merged at
  `a6ebc43a0e09219c5f6d1a8e1e7d2f3c4b5a6d7e`. Save menu item dispatch into the
  Save action path is proven under Xvfb; Save dialog display and Save dialog control
  remain unproven.
- [RabbitHole PR #237](https://github.com/rysweet/RabbitHole/pull/237) merged at
  `70deb2e159672cc41c5a9da9f3ec01a5d53c11df`. Fixes the Alice launch classpath
  so `org.alice.stageide.EntryPoint` is on the Maven exec classpath; does not
  prove visible rendering, deployed installer success, or full world execution.
- [RabbitHole PR #238](https://github.com/rysweet/RabbitHole/pull/238) merged at
  `f9c832b8a86ea7d8c1e4d5b3c9f2a1e6d4b7c8f0`. Decodes the narrow case of a
  single Tweedle `return` of a required method parameter identifier to AST
  `ParameterAccess`; full method body, constructor body, player, and complete
  Tweedle decode support remain unproven.
- [RabbitHole PR #240](https://github.com/rysweet/RabbitHole/pull/240) merged at
  `ae3d8de57aec10d2f9c3b7e1a5c6d8f4e2b1c9a3`. Adds an `x-window-inventory.json`
  to the Xvfb Alice launch proof, recording visible X window title, class,
  process, and geometry; blocked at `alice-window-not-found` after the classpath
  fix.
- [RabbitHole PR #241](https://github.com/rysweet/RabbitHole/pull/241) merged at
  `d2ab990dffa8c7e5b9a3d1f6c4e2b8d7a5c0f1e9`. Adds an opt-in selected-path
  automation seam at `FileDialogUtilities.showSaveFileDialog`, rejecting outside
  paths and symlink escapes; Save dialog display and control remain unproven.
- [RabbitHole PR #245](https://github.com/rysweet/RabbitHole/pull/245) merged at
  `9cc5893d8b67e4d1b8a3c7f2e5d6c9b4a1e8f3d2`. Adds an `application-root-error.json`
  probe that maps the `Application Root Error` window to the
  `org.alice.ide.rootDirectory` condition and next invocation change needed.
- [RabbitHole PR #246](https://github.com/rysweet/RabbitHole/pull/246) merged at
  `2fe47f4ebaea9d7c3b5a1e8f4d6c2b9a7e5d3c8f`. Proves
  `ProjectDocumentFrame.showSaveFileDialog` reaches `FileDialogUtilities` with a
  displayable `JFrame` root under Xvfb; Save dialog display and control remain
  unproven.
- [RabbitHole PR #247](https://github.com/rysweet/RabbitHole/pull/247) merged at
  `0a75eb7a21f5d3c9b7e2a4d6f1c8b5e9d2a7c3f6`. Decodes narrow Tweedle constructor
  bodies with primitive-literal local variable declarations to AST
  `LocalDeclaration`; full Tweedle constructor, method, player, and resource
  decode remain unproven.
- [RabbitHole PR #250](https://github.com/rysweet/RabbitHole/pull/250) merged at
  `c640c3fbd9ef5a7d1c8b2e4f6a9d3c7b5e1a8f2d`. Adds a `rootDirectory` prep helper
  that verifies `alice-ide` configures `org.alice.ide.rootDirectory` and prepares
  `core/resources/target/distribution` before the Xvfb launch, recording the
  precise `Application Root Error` blocker artifacts.
- [RabbitHole PR #253](https://github.com/rysweet/RabbitHole/pull/253) merged at
  `39635ffd10108d5c9b2e4a7f3d1c6e8b5a9d2c7f`. Decodes method return identifiers
  that refer to declared Tweedle fields as AST `FieldAccess` expressions; field
  return type-mismatch cases are rejected clearly; full method, assignment,
  member-expression, and player decode remain unproven.
- [RabbitHole PR #254](https://github.com/rysweet/RabbitHole/pull/254) merged at
  `88e8cffffa7c2b5d9e1a4c7f3d6b8e2a5c9d1f4b`. Adds a first-run license QA bypass:
  a focused License Agreement dialog probe and explicit test-only Java Preferences
  acceptance using isolated `java.util.prefs.userRoot` state, with license
  acceptance and dialog artifacts recorded in Xvfb launch evidence.
- [RabbitHole PR #255](https://github.com/rysweet/RabbitHole/pull/255) merged at
  `c8d52a9a8865f3d7b1e9c4a6d2f5c8b3e7a1d9c4`. Adds a `SaveOperationFlow` Xvfb-safe
  proof that writes a real `.a3p` project file to a controlled selected path via
  `FileDialogUtilities` selected-path automation, recording `saved_file_exists` and
  `saved_file_size_bytes`; does not prove live Save dialog display or desktop
  save-menu completion.
- [RabbitHole PR #259](https://github.com/rysweet/RabbitHole/pull/259) merged at
  `e5b0ac5fce21b4eee1e13ea5861d2e9cee538ca8`. Decodes Tweedle method returns of
  `this.field` into AST `FieldAccess`; assignments, optional params, broader
  member expressions, resource initializers, and full Tweedle/player decode
  remain unproven.
- [RabbitHole PR #260](https://github.com/rysweet/RabbitHole/pull/260) merged at
  `b553677c1225d704d1d951a59653fb0f66096139`. A Swing `JFileChooser` dialog was
  observed under Xvfb and approved through the chooser's controls; native
  `java.awt.FileDialog` peer control and the full StageIDE Save-menu-to-real-chooser
  journey remain unproven.
- [RabbitHole PR #261](https://github.com/rysweet/RabbitHole/pull/261) merged at
  `97c1ae707544bd0ca89e711df92e7e45e6d377ac`. The Select Project Java window was
  observed under Xvfb with title, class, process, and geometry; selecting or
  opening a project, world execution, and installer success remain unproven.
- [RabbitHole PR #262](https://github.com/rysweet/RabbitHole/pull/262) merged at
  `9ef09e05402b2e0af9c07803eee92aa5db29b325`. Primitive literal field assignments
  in Tweedle method bodies now decode, with clear unsupported-form failures; full
  Tweedle/player decode remains unproven.
- [eatme PR #122](https://github.com/rysweet/eatme/pull/122) merged at `41142db`.
  Adds the `lost-robot-debug-museum` instructor/student scenario for the
  reflective-debugger/debug-coach use case; grading, creative assessment, real
  Alice UI automation, and full lesson delivery remain unproven.
- [eatme PR #123](https://github.com/rysweet/eatme/pull/123) merged at
  `773fb3df7a6ec234c5f317eefdfea82916ecd7bc`. Adds the
  `weather-wizard-conditional-theater` instructor/student scenario, the next
  `creative_new` teaching/learning gap fill; scenario assets grew from 71 to 73.
  Grading, automated creative assessment, real Alice UI automation, and full
  lesson delivery remain unproven.
- [RabbitHole PR #264](https://github.com/rysweet/RabbitHole/pull/264) merged at
  `a4386130d66b97feecdbcb5ab1b6bc765392deb3`. Primitive literal field assignments
  in Tweedle constructor bodies now decode, with clear failures for unsupported
  constructor assignment forms; full Tweedle/player decode remains unproven.
- [eatme PR #124](https://github.com/rysweet/eatme/pull/124) merged at
  `d3bb687145b6c9e38601703c691aa7f6bcbb4862`. Adds the
  `alien-linguist-parameter-dialogue` instructor/student scenario; scenario
  assets grew from 73 to 75 with all adapters fresh. Grading, automated
  creative assessment, real Alice UI automation, and full lesson delivery remain
  unproven.
- [RabbitHole PR #265](https://github.com/rysweet/RabbitHole/pull/265) merged at
  `ead3a465a6c794f552edc32699f011242fc303d7`. `DocumentFrame.showSaveFileDialog`
  reaches a live `JFileChooser` under Xvfb via a running StageIDE instance;
  `FileDialogUtilities.createFileDialog()` returns `SwingFileDialog` on Linux so
  native `java.awt.FileDialog` is not used. Full Save-menu-to-written-project
  journey remains unproven.
- [RabbitHole PR #266](https://github.com/rysweet/RabbitHole/pull/266) merged at
  `2fe0ba4ef5d94e5516e9975f00fea9c23ff79ac9`. AT-SPI bus is reachable and
  Alice's Java process registers via `libatk-wrapper.so`; Swing components are
  not accessible in the `exec:java` context; exact remediation path documented.
  Select Project widget enumeration and project opening remain unproven.
- [RabbitHole PR #267](https://github.com/rysweet/RabbitHole/pull/267) merged at
  `2ca7aa1062ee94b4e10eb8a13cdad8a4f4cfabc6`. Primitive literal local variable
  reassignment in Tweedle method and constructor bodies now decodes; full
  Tweedle/player decode remains unproven.
- [eatme PR #125](https://github.com/rysweet/eatme/pull/125) merged at
  `847c09d20be16435595e1368f8f96c495fc6e4f5`. Adds the
  `ecosystem-balance-loop-simulation` instructor/student scenario; scenario
  assets grew from 75 to 77 with all 38 Gadugi adapters fresh. Grading,
  automated creative assessment, real Alice UI automation, and full lesson
  delivery remain unproven.
- [RabbitHole PR #269](https://github.com/rysweet/RabbitHole/pull/269) merged at
  `ce31df5c04401f7ddb759c9d6640ca2881f82c4f`. Tweedle optional method and
  constructor parameters now decode as Alice `UserParameter` entries. Default
  values are not represented because the Alice AST has no optional-parameter
  concept and `TweedleOptionalParameter` exposes no default accessor. Full
  Tweedle/player decode remains unproven.
- [eatme PR #126](https://github.com/rysweet/eatme/pull/126) merged at
  `72731e2e7dd092292f982408faad5a2e98d7e74a`. Adds the
  `time-travel-recipe-sequencing` instructor/student scenario; scenario assets
  grew from 77 to 79 with all adapters fresh. Grading, automated creative
  assessment, real Alice UI automation, and full lesson delivery remain unproven.
- [eatme PR #127](https://github.com/rysweet/eatme/pull/127) merged at
  `e0c090f265f0dfb2f0b662616aac8b6cb078dae6`. Adds the
  `mars-rover-proximity-mission` instructor/student scenario; scenario assets
  grew from 79 to 81 with all 40 generated gadugi adapters fresh. Grading,
  automated creative assessment, real Alice UI automation, and full lesson
  delivery remain unproven.
- [RabbitHole PR #270](https://github.com/rysweet/RabbitHole/pull/270) merged at
  `b887a14e85a514b5bf7504eeffd3fbeff490e0a2`. Assignment statements in Tweedle
  method and constructor bodies now decode an `IdentifierReference` RHS to
  `ParameterAccess`, `LocalAccess`, or `FieldAccess`. Constructor assignment
  bodies now receive `UserParameter[]` so constructor setter patterns resolve
  parameter RHS. Full Tweedle/player decode remains unproven.
- [RabbitHole PR #271](https://github.com/rysweet/RabbitHole/pull/271) merged at
  `b49b898ddfd2c19a27ce88d265f2c723499b1454`. Local variable declarations in
  Tweedle method and constructor bodies now decode an `IdentifierReference`
  initializer to `LocalAccess`, `ParameterAccess`, or `FieldAccess`. Full
  Tweedle/player decode remains unproven.
- [eatme PR #129](https://github.com/rysweet/eatme/pull/129) merged at
  `b72afe499c9b7a3826012b7d10c69b5ae6b6c0a1`. Adds the
  `creature-choreography-loop-lab` instructor/student scenario; scenario assets
  grew from 81 to 83 with all Gadugi adapters fresh. Grading, automated creative
  assessment, real Alice UI automation, and full lesson delivery remain unproven.
- [RabbitHole PR #272](https://github.com/rysweet/RabbitHole/pull/272) merged at
  `458bed0f4b409d207a2610b8ccfa8e8dfbbce6c9`. Proves AT-SPI reaches the Alice
  Java process via `exec:exec` and `NO_AT_BRIDGE=1`; top-level Swing widgets are
  observable. Tab labels are not visible or enumerable. Project selection and
  opening are not proven.
- [RabbitHole PR #273](https://github.com/rysweet/RabbitHole/pull/273) merged at
  `c86e8c4747b73921e8c432709c8cf7a741848855`. Proves `SaveProjectOperation.fire()`
  reaches a live `JFileChooser`, a background probe approves it, and a non-empty
  `.a3p` is written. Visible rendering, grading, the native FileDialog path, and a
  full Save menu item `doClick`-to-written-file journey in one path remain unproven.
- [eatme PR #131](https://github.com/rysweet/eatme/pull/131) merged at
  `973b65f`. Adds the `neighborhood-data-story` instructor/student scenario;
  scenario assets grew from 83 to 85 with all Gadugi adapters fresh. Remaining
  missing scenario files: accessibility-rescue-camera-captions,
  design-process-story-or-game, audio-camera-and-export-sharecase,
  setup-preflight-ready-to-create. Grading, automated creative assessment, real
  Alice UI automation, and full lesson delivery remain unproven.
- [RabbitHole PR #274](https://github.com/rysweet/RabbitHole/pull/274) merged at
  `5571894e5152482c9fb26ba31fc3d633d372e88e`. Arithmetic binary expressions
  (`+`, `-`, `*`, `/`) now decode as Tweedle assignment right-hand-side values
  and as local variable initializer values. String concatenation, logical and
  comparison expressions, method calls, non-`this` member assignment targets,
  loops, conditionals, resource field initializers, and full Tweedle/player
  decode remain unproven.
- [RabbitHole PR #276](https://github.com/rysweet/RabbitHole/pull/276) merged at
  `66b38f87090f633f44a403737778c3c01a01c52b`. A programmatically-created real
  Save menu item has `doClick()` called on it; this dispatches through Croquet,
  reaches a live `JFileChooser`, the dialog is approved by a background probe,
  and a non-empty `.a3p` file is written. Real rendered desktop menu bar
  navigation, native FileDialog, visible rendering, grading, and full lesson
  completion remain unproven.
- [RabbitHole PR #277](https://github.com/rysweet/RabbitHole/pull/277) merged at
  `8c1a3fd32c2c1d19aac7ea265909f0d19276273e`. Tweedle string concatenation (`..`)
  now decodes in assignment right-hand-side values, local variable initializers,
  and method return expressions. Logical and comparison expressions, method calls,
  non-`this` member assignment targets, loops, conditionals, resource field
  initializers, and full Tweedle/player decode remain unproven.
- [RabbitHole PR #278](https://github.com/rysweet/RabbitHole/pull/278) merged at
  `e130dac3a6f6431895f72f71733a042f1bb92cb3`. Select Project tab labels are
  accessible as AT-SPI toggle buttons at depth 11; all five tabs can be clicked
  programmatically; Starters -> Africa Full -> OK causes `projectOpenObserved: true`
  and the Select Project frame disappears. Real rendered desktop menu bar
  navigation, native FileDialog, visible rendering, grading, and full lesson
  completion remain unproven.
- [eatme PR #132](https://github.com/rysweet/eatme/pull/132) merged at
  `ebaf93e85a502f4778aaa194f4cd61ae8ae4cdda`. Adds the
  `accessibility-rescue-camera-captions` instructor/student scenario and Gadugi
  adapter; scenario asset count grew to 87. Remaining missing scenario files:
  design-process-story-or-game, audio-camera-and-export-sharecase,
  setup-preflight-ready-to-create. Grading, automated creative assessment, real
  Alice UI automation, and full lesson delivery remain unproven.
- [RabbitHole PR #281](https://github.com/rysweet/RabbitHole/pull/281) merged at
  `daaceb0a9648d18e890c5b106327d2ddbe489149`. Fixes the Save menu doClick test
  proof bookkeeping: `approvedSelection` is now set before `approveSelection()`
  is called so the probe cannot falsely report unsupported after a successful
  write. Does not expand Save proof scope beyond PR #276. Real rendered desktop
  menu bar navigation, native FileDialog, visible rendering, grading, and full
  lesson completion remain unproven.
- [eatme PR #133](https://github.com/rysweet/eatme/pull/133) merged at
  `7d0d05726b970dc9a616ed8aa633e090ceebf88b`. Adds the
  `design-process-story-or-game` instructor/student scenario and Gadugi adapter;
  scenario asset count grew from 87 to 89. Remaining missing scenario files:
  audio-camera-and-export-sharecase, setup-preflight-ready-to-create. Grading,
  automated creative assessment, real Alice UI automation, and full lesson
  delivery remain unproven.
- [RabbitHole PR #282](https://github.com/rysweet/RabbitHole/pull/282) merged at
  `81db4122fc3270e2a16a02c46c4a1d7f254717e3`. Decodes Tweedle relational
  comparison expressions (`==`, `!=`, `<`, `<=`, `>`, `>=`) to
  `RelationalInfixExpression` in local initializers, assignment right-hand sides,
  and method returns. Logical expressions, method calls, non-`this` member
  targets, loops, conditionals, resource initializers, and full Tweedle/player
  decode remain unproven.
- [RabbitHole PR #284](https://github.com/rysweet/RabbitHole/pull/284) merged at
  `eca3fb920e3d2b13f5de7117ccc96308378a10f6`. Fixes `approvedSelection` ordering
  in `StageIdeSaveMenuE2EWriteProofTest` and `SaveFileDialogShowControlProofTest`
  so all Save proof tests set the proof flag before the approval call. Proof
  bookkeeping only; does not expand Save proof scope beyond PR #276.
- [RabbitHole PR #285](https://github.com/rysweet/RabbitHole/pull/285) merged at
  `8eaa066f98ab173bfa6d0d08f804b5e4eb47a7be`. Proves Alice 3 main-window AT-SPI
  state after Select Project dismissal via `post-project-open-probe.py`. Requires
  `projectOpenObserved=true`, waits five seconds, enumerates top-level frames,
  and records blockers. Full scene load, visible rendering, UI correctness,
  grading, and lesson completion remain unproven.
- [eatme PR #134](https://github.com/rysweet/eatme/pull/134) merged at
  `294ca3319863098c11e3abd712dc661b44a6278e`. Adds the
  `setup-preflight-ready-to-create` instructor/student scenario and Gadugi
  adapter; scenario asset count grew from 89 to 91. Remaining missing scenario
  file: audio-camera-and-export-sharecase. Grading, automated creative
  assessment, real Alice UI automation, and full lesson delivery remain unproven.
- [eatme PR #135](https://github.com/rysweet/eatme/pull/135) merged at
  `8f82d682aef4d22c3ca4e7bdc4344cae660b13bd`. Adds the
  `audio-camera-and-export-sharecase` instructor/student scenario and Gadugi
  adapter; scenario asset count grew from 91 to 93. No remaining scenario gaps
  from the list in `docs/persona-assets.md` and
  `assets/personas/alice-user-crew.yaml`. Grading, automated creative
  assessment, real Alice UI automation, and full lesson delivery remain unproven.
- [RabbitHole PR #287](https://github.com/rysweet/RabbitHole/pull/287) merged at
  `198b482733f3fcb9ae7ecfc5479027393f21cf71`. Decodes Tweedle logical expressions:
  `&&` and `||` to `ConditionalInfixExpression`; `!` to `LogicalComplement`.
  Covers local variable initializers, assignment right-hand-side positions, and
  method return expressions. Full Tweedle/player decode, method calls, loops,
  conditionals, resource initializers, visible rendering, grading, and
  first-lesson completion remain unproven.
- [RabbitHole PR #289](https://github.com/rysweet/RabbitHole/pull/289) merged at
  `cc119baebb4dd5ad775ac497c9f2318b9f8d2add`. Adds tests that logical `&&`, `||`,
  and `!` method returns fail clearly when the method declares a non-Boolean return
  type. Test-only; does not expand decode behavior. Full Tweedle/player decode,
  visible rendering, grading, and first-lesson completion remain unproven.
- [RabbitHole PR #290](https://github.com/rysweet/RabbitHole/pull/290) merged at
  `65c11f6`. Adds seven `SourceCodeGenerator` behavior characterization tests:
  while loop, null literal, logical complement, arithmetic infix, relational infix,
  array access, and array length. All five RabbitHole checks passed; focused review
  returned CLEAN. Full Alice UI automation, visible rendering, grading, full
  Tweedle/player decode, and first-lesson completion remain unproven.
- [eatme PR #136](https://github.com/rysweet/eatme/pull/136) merged. Improves
  `next_missing_real_desktop_proof` so after the pixel chain users see the first
  missing RabbitHole hook path in order: `place-object` /
  `tools/eatme-place-object`, `edit-procedure-or-code-block` /
  `tools/eatme-edit-procedure`, `run-world` / `tools/eatme-run-world`,
  `save-project` / `tools/eatme-save-project`. 203 tests passed; CI is green.
  These hook messages do not prove full UI automation. Full Alice UI automation,
  visible rendering, grading, and first-lesson completion remain unproven.
- [RabbitHole PR #291](https://github.com/rysweet/RabbitHole/pull/291) merged at
  head `0f00c088f20e489b5b3c43bdbdc29e078dfb6b9b`. Decodes Tweedle `if`/`else`
  statements in void method bodies into Alice `ConditionalStatement` with a
  `BooleanExpressionBodyPair` and else body. Adds 5 tests; CI all green; focused
  review CLEAN. Local declarations inside `if`/`else` bodies, nested `if`/`else`,
  loops, method calls, constructors, resource fields, full player decode, and full
  Tweedle decode remain unproven. Visible rendering, grading, and first-lesson
  completion remain unproven.
- [RabbitHole PR #292](https://github.com/rysweet/RabbitHole/pull/292) merged at
  `17e82091232131de7f1b2169638a2ea1a48fedfd`. Adds
  `FileMenuSaveNavigationProofTest`: starts `StageIDE`, finds `FileMenuModel` in
  the real `AliceMenuBar`, calls `fileMenuModel.createMenu()` to build the actual
  `JMenu`, locates the `JMenuItem` backed by the same `Action` instance as
  `SaveProjectOperation`, calls `doClick()`, and checks that evidence shows
  `status=menu_item_dispatched`, `menu_item_dispatch=true`, and
  `trigger_class=ActionEventTrigger`. All five CI checks passed; focused review
  returned CLEAN. The user physically clicking the on-screen File menu, desktop
  save-menu completion from a real rendered click path, full live FileDialog
  interaction with a confirmed file write, visible rendering correctness, grading,
  and first-lesson completion remain unproven.
- [RabbitHole PR #293](https://github.com/rysweet/RabbitHole/pull/293) merged at
  head `3696670873c6a409046ac6e648e828d95956aa8b`. Decodes Tweedle
  `while (condition) { ... }` to Alice `WhileLoop` in void method bodies.
  Supported Boolean conditions: literal, parameter access, relational infix,
  logical infix/not. Supported body: assignment-only statements; empty body
  accepted. 6 new tests; 109 total; 0 failures; all five CI checks passed;
  focused review returned CLEAN. Non-void method while loops, non-Boolean
  conditions, non-assignment body statements, method calls, for-each/count-up
  loops, constructor body while loops, resource field initializers, full player
  decode, and full Tweedle decode remain unproven. Visible rendering, grading,
  and first-lesson completion remain unproven.
- [RabbitHole PR #297](https://github.com/rysweet/RabbitHole/pull/297):
  repository `rysweet/RabbitHole`; status `MERGED`; merged at
  `2026-05-08T04:39:11Z`; merged by `rysweet`; merge commit SHA
  `527011aa8337222cddd05d23766edcac908a699b`; head SHA
  `59272ae077e3e614f3ef30a4b6b37140c8eb80f8`.
- [RabbitHole PR #298](https://github.com/rysweet/RabbitHole/pull/298):
  repository `rysweet/RabbitHole`; status `MERGED`; merged at
  `2026-05-08T02:32:51Z`; merged by `rysweet`; merge commit SHA
  `fb9da28c2dcaf426b87699ffceebaba7093d994a`; head SHA
  `6bd52537504d0f88cd0fe6c1919e5a4134eca2a8`.
- [RabbitHole PR #306](https://github.com/rysweet/RabbitHole/pull/306)
  merged at `2026-05-08T09:31:58Z`. PR #306 is narrow
  ModelResourceExporter attribution evidence only.
- [RabbitHole PR #308](https://github.com/rysweet/RabbitHole/pull/308)
  merged at `2026-05-08T09:15:55Z`. PR #308 is narrow headless generated
  Story API runtime-state evidence only.
- [RabbitHole PR #307](https://github.com/rysweet/RabbitHole/pull/307)
  and [amplihack-rs PR #575](https://github.com/rysweet/amplihack-rs/pull/575)
  remain active follow-up work outside this PR #306/#308 evidence entry.
- PR #307 is bounded Project I/O recovery follow-up.
- [amplihack-rs PR #575](https://github.com/rysweet/amplihack-rs/pull/575)
  is supporting recipe pre-commit reliability follow-up.
- PR #306 and PR #308 do not prove visible rendering, JavaFX launch, animation
  playback, full world execution, grading, full UI automation, full lesson
  completion, or full Tweedle/player decode.
- [eatme PR #138](https://github.com/rysweet/eatme/pull/138): repository
  `rysweet/eatme`; status `MERGED`; merged at `2026-05-08T02:13:51Z`;
  merged by `rysweet`; merge commit SHA
  `b412458d6abf4d235dc03f4efb3debabd54e79d1`; head SHA
  `8cacd14cc51fc09cae20ee421f4bc4a8e285b751`.
- [amplihack-rs PR #571](https://github.com/rysweet/amplihack-rs/pull/571):
  repository `rysweet/amplihack-rs`; status `MERGED`; merged at
  `2026-05-08T04:55:47Z`; merged by `rysweet`; merge commit SHA
  `0af6f12824778fbff94627dae5da92b57beb6fc9`; head SHA
  `33582d27e8cac3f00cbd7e702a5304c34768d41a`.
- Existing tests mostly cover Tweedle parsing, manifest encoding, version parsing, and math utilities.
- First implementation slice added launch-argument characterization tests and extracted a tested `LaunchConfiguration` seam.
- Second implementation slice added project migration/version characterization tests without production code changes.
- Third implementation slice characterized corrupt project-load IO failure delegation and documented why `FileProjectLoader` does not show its own error dialog.
- Fourth implementation slice added no-Sims `ModelResourceInfo` XML metadata and manifest characterization tests.
- Fifth implementation slice added NetBeans Alice-to-Java launcher generation characterization and locked the generated `AliceJavaFXLauncher` against the project template `main.class`.
- Sixth implementation slice extracted and characterized project backup candidate selection, keeping dialogs and recursive loading in `ProjectApplication`.
- Seventh implementation slice extracted and characterized the project-load failure branch plan, keeping Swing dialogs and recursive loading in `ProjectApplication`.
- Eighth implementation slice characterized `FileProjectLoader` VR save-path and `shouldBeSaved()` behavior with temp files.
- Ninth implementation slice characterized `ModelResourceInfo` texture-specific subresource lookup, model-only fallback, and manifest de-duplication.
- Tenth implementation slice fixed and characterized `ResourcesTypeWrapper` resource-to-field mapping, a code-atlas bug-hunt finding that broke exported-resource code generation by leaving generated fields unmapped.
- Eleventh implementation slice characterized backup-directory path derivation and hardened parentless backup-file handling so callers can skip backup work instead of crashing on a null parent.
- Twelfth implementation slice characterized the NetBeans project-template archive and fixed generated project metadata so `application.title` and `dist.jar` are renamed with the imported project.
- Thirteenth implementation slice fixed `ModelResourceInfo` edge cases: explicit child `placeOnGround=false` now overrides a true parent, omitted child values still inherit, and model-only manifest entries no longer use `*_null` names.
- Fourteenth implementation slice fixed `ModelResourceInfo` subresource tag parsing so nested unrelated XML tags are not collected while preserving direct and grouped tag formats.
- Fifteenth implementation slice added a provenance-clean synthetic `.a3p` round-trip test: a minimal in-memory project is written, read back, and checked for core archive entries without committing binary fixtures.
- Sixteenth implementation slice extended the synthetic `.a3p` round-trip to include a test-only resource that follows Alice's `valueOf(String)` reflection contract, verifying resource metadata and bytes survive project IO.
- Seventeenth implementation slice used the synthetic `.a3p` foothold to characterize NetBeans Java source generation: a minimal Alice project now generates `Program.java` plus `AliceJavaFXLauncher.java` in a headless test, with a package-private seam that skips only NetBeans editor formatting.
- Eighteenth implementation slice extended NetBeans source-generation characterization to resources: a synthetic resource now generates copied resource bytes plus `Resources.java`, preserving the resource constructor/reflection contracts needed by exported code.
- Nineteenth implementation slice added a JavaCompiler smoke test for generated `Program.java` and `AliceJavaFXLauncher.java`, and documented that even synthetic exported projects need the static `main(String[] args)` entry point expected by the launcher.
- Twentieth implementation slice extended generated-source compilation to resource-backed exports: `Program.java`, `AliceJavaFXLauncher.java`, and `Resources.java` now compile together for a synthetic resource project.
- Twenty-first implementation slice added a runtime smoke for generated resources: compiled `Resources.java` can load copied `resources/note.txt` bytes from the classpath through the generated static resource field.
- Twenty-second implementation slice fixed a generated-resource filename mismatch: NetBeans export now copies resource bytes by `originalFileName`, matching the path emitted in `Resources.java`, so display-name changes no longer break runtime resource loading.
- Twenty-third implementation slice fixed duplicate generated-resource filenames: exported `Resources.java` now assigns unique `resources`, `resources2`, ... paths and NetBeans copies bytes to those same paths, so duplicate original filenames do not collapse to one runtime resource.
- Twenty-fourth implementation slice fixed blank generated-resource filenames: when `originalFileName` is blank, export falls back to the fixed resource display name so `Resources.java` and copied bytes still use a loadable path.
- Twenty-fifth implementation slice hardened generated-resource filenames with separators or parent-directory names: export now sanitizes slash/backslash filename segments and falls back for bare `.`/`..`, keeping generated resource files inside the expected resources layout.
- Twenty-sixth implementation slice added non-empty generated user method coverage: a synthetic `sayHello()` method with a comment body is generated and compiled, expanding NetBeans source-generation characterization beyond empty program/resource scaffolding.
- Twenty-seventh implementation slice added local-declaration generated-source coverage: a synthetic user method now emits and compiles a final `String` local initialized from a string literal.
- Twenty-eighth implementation slice added user-parameter generated-source coverage: a synthetic method parameter is emitted in Java and accessed through a generated local declaration.
- Twenty-ninth implementation slice added user-method invocation generated-source coverage: a synthetic method emits and compiles a `this.sayHello();` call to another generated user method.
- Thirtieth implementation slice added user-method invocation argument coverage: a synthetic method emits and compiles `this.remember("hello alice");`, exercising generated arguments alongside parameter access.
- Thirty-first implementation slice added conditional generated-source coverage: a synthetic method emits and compiles a minimal `if(true) ... else ...` body.
- Thirty-second implementation slice added count-loop generated-source coverage: a synthetic method emits and compiles a minimal `for(Integer indexA=0;indexA<3;indexA++)` body.
- Thirty-third implementation slice characterized exported NetBeans project build properties: the template targets Java 21, `AliceJavaFXLauncher`, the `Alice3Library` NetBeans library, Alice root-directory runtime property, and JavaFX module opens; no-Sims CI now skips LFS checkout because the LFS budget can block tests that do not need assets.
- Thirty-fourth implementation slice characterized `Alice3Library` registration: the NetBeans layer registers `Alice3Library.xml`, and the library declares classpath, source, and javadoc volumes used by exported projects.
- Thirty-fifth implementation slice characterized NetBeans library packaging sources: the module POM packages javadoc, story source, and renamed NBM artifacts that back `Alice3Library` source/javadoc volumes.
- Thirty-sixth implementation slice added no-Sims NetBeans package CI so NBM/support artifact generation is checked on every `develop` push without relying on Git LFS assets.
- Thirty-seventh implementation slice tightened NetBeans package CI with explicit assertions for the NBM, module jar, source jar, javadoc zip, library registration resources, story source, and javadoc overview.
- Thirty-eighth implementation slice characterized generated launcher runtime handoff: a headless test invokes `AliceJavaFXLauncher.main(...)` against test-only JavaFX stubs and verifies the original args reach `Program.main(...)`.
- Thirty-ninth implementation slice added while-loop generated-source coverage: a synthetic method emits and compiles a minimal `while (true)` body without executing it.
- Fortieth implementation slice added foreach-array generated-source coverage: a synthetic method emits and compiles `for(String COUNT__ : new String[]{"red", "blue"})`, exposing a suspicious current loop-variable name for future cleanup.
- Forty-first implementation slice characterized foreach loop-item access: the same `COUNT__` variable is used coherently when the loop body reads the item, so this is readability debt rather than an immediate compile bug.
- Forty-second implementation slice split generated-source export tests into `ProjectCodeGeneratorGeneratedSourceTest`, reducing `ProjectCodeGeneratorTest` from 788 lines to 430 and keeping the new focused class at 399 lines.
- Forty-third implementation slice replaced the dormant model export test body with active no-Sims characterization for `ModelResourceExporter` XML serialization and generated resource Java compilation.
- Forty-fourth implementation slice added a standalone-style exported project smoke: a synthetic Alice project is generated into a `src` layout, compiled with JavaFX stubs, and the generated launcher is invoked through a child-first classloader.
- Forty-fifth implementation slice characterized named foreach item generation: named item locals emit readable Java (`item`) while unnamed helper-created loops still emit the current `COUNT__` fallback.
- Forty-sixth implementation slice characterized iterable foreach generation: a synthetic `ForEachInIterableLoop` over `Arrays.asList("red","blue")` emits compilable Java, imports `java.util.Arrays`, and preserves the explicit loop item name.
- Forty-seventh implementation slice added a template-shaped exported project smoke: the real NetBeans project template is extracted, generated Alice Java sources are placed in `src`, the `Alice3Library` classpath contract is checked, and the source tree compiles with the test classpath as the library surrogate.
- Forty-eighth implementation slice characterized the first realistic story API generated-source call: a synthetic program emits and compiles `this.setSimulationSpeedFactor(1.5);` in a new focused NetBeans test class rather than bloating the existing 481-line generated-source test.
- Forty-ninth implementation slice characterized the user-visible player export artifact: `ProjectFileUtilities.exportCopyOfProjectTo` now has a headless smoke proving the exported archive contains `version.txt`, `manifest.json`, `thumbnail.png`, and `src/Program.twe` with manifest metadata for the program and thumbnail.
- Fiftieth implementation slice characterized editor save-copy roundtrip: `ProjectFileUtilities.saveCopyOfProjectTo` writes a readable `.a3p` with manifest, thumbnail, program XML, and resource bytes, then `IoUtilities.readProject` preserves the program, camera type, resource identity, name, content type, and data.
- Fifty-first implementation slice characterized backup recovery candidate skipping: recent-backup probes now cover a newer unloadable backup being skipped, with the next candidate selected only when its timestamp is newer than the main project and rejected when older.
- Fifty-second implementation slice characterized `ProjectFileUtilities` save/export source selection and default-backup migration: export uses the forced up-to-date snapshot, save-copy uses the normal up-to-date snapshot, and default auto-backups move into the saved project's named backup directory.
- Fifty-third implementation slice added a headless backup recovery IO path: a corrupt main project and unloadable newest backup lead to the next backup being selected, planned as a backup-load prompt, and loaded through `FileProjectLoader` with resource metadata and bytes intact.
- Fifty-fourth implementation slice extracted and characterized the `ProjectApplication.saveProjectTo` target decision into `ProjectSaveTargetPlan`, preserving current new-project/default-backup/backup-save behavior while making the save orchestration seam testable without constructing the Swing-heavy IDE frame.
- Fifty-fifth implementation slice characterized the resource-bearing player export boundary: a referenced image resource is written into the player/Tweedle archive with manifest metadata, but the current editor XML reader cannot reopen that player export.
- Fifty-sixth implementation slice characterized editor save-copy roundtrip for an AST-referenced `ImageResource`: the XML editor archive writes `resources/picture.png` and reopens with program, camera, image resource identity, names, content type, and bytes intact.
- Fifty-seventh implementation slice added manifest-based reader dispatch for player exports and minimal JSON IO resource reads: exported `.a3w`/Tweedle archives now route to `JsonProjectIo` and restore manifest-listed image resources while leaving program-type Tweedle decoding explicitly unimplemented.
- Fifty-eighth implementation slice made JSON/player archives report future `version.txt` values through `ProjectReader.checkForFutureVersion()`, matching the XML reader warning path used by file loaders.
- Fifty-ninth implementation slice made JSON/player export resource entries duplicate-safe and path-safe: duplicate resource filenames use `resources2/...`, and slash/backslash path-like filenames are flattened before zip entry creation while resource bytes still round-trip.
- Sixtieth implementation slice characterized JSON/player export and readback for an AST-referenced `AudioResource`, using synthetic bytes and preserving the current resource-only player reader boundary.
- Sixty-first implementation wave used six isolated workflow-aware implementation branches plus fifteen scout/review tracks. It fixed JSON/player resource read identity isolation, hardened corrupt-manifest dispatch, characterized model/generated type references in player archives, added JSON `.a3c` resource-only type reads, strengthened the NetBeans template compiler surrogate, and extracted the project-load success decision seam.
- Sixty-second implementation wave used eight workflow-aware implementation tracks plus guardrails. It fixed NetBeans `Alice3Library` classpath shape, extracted project-load failure dispatch planning, added explicit manifest decode errors, characterized JSON `.a3c` version behavior, isolated XML resource identity on read, characterized `JsonModelIo` export format selection, characterized URI project-loader path classification, and hardened default-backup copy behavior.
- Added a dedicated submodule working guide for `tweedle-lang`, worktree initialization, `core/tweedle` ANTLR generation, and the common missing-submodule parser failure mode.
- Going forward, every coding track and subagent must explicitly follow `DEFAULT_WORKFLOW`. Parallel implementation should use isolated worktrees/branches for independent modules; never parallel-edit the same working tree.

Merged source PR status:

| Work item | Plain status |
| --- | --- |
| [RabbitHole PR #154](https://github.com/rysweet/RabbitHole/pull/154) | Merged. Records that Alice put the Run panel into the Run window area. |
| [RabbitHole PR #155](https://github.com/rysweet/RabbitHole/pull/155) | Merged. Records launcher steps and no-go messages, but does not prove rendering. |
| [RabbitHole PR #156](https://github.com/rysweet/RabbitHole/pull/156) | Merged. Keeps old image recovery while safely rejecting unsupported old code. |
| [RabbitHole PR #159](https://github.com/rysweet/RabbitHole/pull/159) | Merged. This repo records only that the PR landed. |
| [RabbitHole PR #160](https://github.com/rysweet/RabbitHole/pull/160) | Merged. This repo records only that the PR landed. |
| [eatme PR #89](https://github.com/rysweet/eatme/pull/89) | Merged. Improves instructor and student readiness reports, but does not grade work or prove full lesson completion. |
| [eatme PR #92](https://github.com/rysweet/eatme/pull/92) | Merged at `cfe1f9e364d0015a3f97e237a9de5af670ae3bd6`. Documents the RabbitHole evidence needed before first-lesson readiness can be marked ready; does not prove full Alice UI automation. |
| [eatme PR #93](https://github.com/rysweet/eatme/pull/93) | Merged. This repo records only that the PR landed. |
- The highest-risk uncharacterized areas are project load/save, model/resource handling, IDE journeys, NetBeans Java-transition workflows, and rendering-adjacent scenegraph behavior.
- Keep the core application Java for now; consider Rust first for optional external tooling, not core runtime.

## Work plan

1. Establish and preserve the two-repo split.
2. Maintain a reproducible build baseline from the public fork.
3. Build a website/reference traceability map.
4. Expand the code atlas from initial diagrams into all major architectural layers.
5. Convert website lessons, how-tos, and reference material into behavior-spec candidates.
6. Build characterization tests in phases, starting with pure logic and project formats.
7. Keep CI test execution active in the RabbitHole modernization repo.
8. Refactor incrementally behind tests; defer any rewrite decision until behavior is documented and protected.
9. Use crusty-old-engineer as a standing proxy review track and qa-team as a standing outside-in testing track, not as occasional afterthoughts.
10. For the desktop Run path, keep the PR #154 boundary narrow until separate
    evidence exists: it proves only that Alice put the Run panel into the Run
    window area, not that pixels were drawn, the lesson finished, or grading
    happened.
11. Treat eatme PR #92 as documentation of the RabbitHole evidence needed before
    first-lesson readiness can be marked ready, not as proof of full Alice UI
    automation, creative assessment, learner-world grading, visible rendering
    correctness, or first-lesson completion.
12. Treat merged RabbitHole PRs #159 and #160 and merged eatme PR #93 as proof
    only that those PRs landed. Do not treat them as proof of full Alice UI
    automation, visible rendering, desktop save-menu completion, grading,
    creative assessment, or first-lesson completion.

## Success criteria

- Alice current code passes the characterization suite.
- The atlas lets a new contributor navigate startup, project persistence, Tweedle, resources, rendering, and NetBeans workflows without reading the whole source tree.
- Refactor proposals are tied to measured pain points and protected by tests.
- License-sensitive assets and no-Sims workflows stay explicit.
- Any Rust or non-Java work is isolated, optional, and justified by clear tooling or performance value.


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

### Latest RabbitHole PR #209/#210/#211 links

- https://github.com/rysweet/RabbitHole/pull/209
- https://github.com/rysweet/RabbitHole/pull/210
- https://github.com/rysweet/RabbitHole/pull/211

### Previous RabbitHole PR #207/#208 links

- https://github.com/rysweet/RabbitHole/pull/207
- https://github.com/rysweet/RabbitHole/pull/208

## Latest RabbitHole PR #209/#210/#211 details

| Work item | Plain status |
| --- | --- |
| [RabbitHole PR #209](https://github.com/rysweet/RabbitHole/pull/209) | Merged at `02e50a00078e8ff348aa33b8c8635483f9b817bf`. Supports literal sized Tweedle array field initializers such as `new WholeNumber[2]`; non-literal sizes still fail clearly, and broader array expressions, method and constructor bodies, non-literal initializers, non-null resource initializers, complete player decode, and full Tweedle decode remain unproven. |
| [RabbitHole PR #210](https://github.com/rysweet/RabbitHole/pull/210) | Merged at `d2cba4ba3e349c704765129511de5a062210ec08`. Adds launcher/runtime proof beyond the earlier `Program.main` null-Stage guard; visible rendering, deployed installer success, and full world execution remain unproven. |
| [RabbitHole PR #211](https://github.com/rysweet/RabbitHole/pull/211) | Merged at `9b509aa3e60e6cf60b5e870a3ee03a0a80363f89`. Adds story-api keyboard event characterization tests; `core/story-api` coverage was reported from 4.55% to 6.21%, adding 260 covered lines. The 70 percent aggregate coverage target, manual QA gaps, and smoke checks that still need manual approval remain unproven. |

## Previous RabbitHole PR #207/#208 details

| Work item | Plain status |
| --- | --- |
| [RabbitHole PR #207](https://github.com/rysweet/RabbitHole/pull/207) | Merged at `6d744747a831824378c053713fef4e8a136c25c5`. Adds Numeric and Boolean Tweedle `null` field initializer decoding to AST `NullLiteral`; primitive statement contexts such as `if(null)` and `while(null)` still fail. Full Tweedle/player decode support remains unproven. |
| [RabbitHole PR #208](https://github.com/rysweet/RabbitHole/pull/208) | Merged at `8799854787655ca61b6fad9378377b19d41aa7b1` from head `153f4e4ce77415d42e6f1047abcc2074671ae4c8` after all GitHub checks passed. Records Save operation completion evidence; desktop save-menu completion remains unproven. |

## Previous RabbitHole source/CI wave details

| Work item | Plain status |
| --- | --- |
| [RabbitHole PR #185](https://github.com/rysweet/RabbitHole/pull/185) | Merged at `713758374d0b6e937ec3f1471a78d7c95f69a35a`. Adds model resource array grouping, skip behavior, and duplicate index rejection tests; 70 percent aggregate coverage and the oversized-file goal remain open. |
| [RabbitHole PR #187](https://github.com/rysweet/RabbitHole/pull/187) | Merged at `7bc8f2991ddc45708203682bd5edeb7a2d990c40`. Adds narrow `TextString label <- null` support to `NullLiteral`; `WholeNumber <- null` still fails, and broader null/player/Tweedle decode work remains open. |
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
| [RabbitHole PR #272](https://github.com/rysweet/RabbitHole/pull/272) | Merged at `458bed0f4b409d207a2610b8ccfa8e8dfbbce6c9`. Proves AT-SPI reaches the Alice Java process via `exec:exec` and `NO_AT_BRIDGE=1`; top-level Swing widgets are observable. Tab labels are still not visible or enumerable. Project selection and opening are not proven. |
| [RabbitHole PR #273](https://github.com/rysweet/RabbitHole/pull/273) | Merged at `c86e8c4747b73921e8c432709c8cf7a741848855`. Proves `SaveProjectOperation.fire()` reaches a live `JFileChooser`, a background probe approves it, and a non-empty `.a3p` is written. Visible rendering, grading, the native FileDialog path, and a full Save menu item `doClick`-to-written-file journey remain unproven. |
| [eatme PR #131](https://github.com/rysweet/eatme/pull/131) | Merged at `973b65f`. Adds the `neighborhood-data-story` instructor/student scenario; scenario assets grew from 83 to 85, all Gadugi adapters fresh. Remaining missing scenario files: accessibility-rescue-camera-captions, design-process-story-or-game, audio-camera-and-export-sharecase, setup-preflight-ready-to-create. Grading, automated creative assessment, real Alice UI automation, and full lesson delivery remain unproven. |
