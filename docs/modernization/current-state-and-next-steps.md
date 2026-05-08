# Alice modernization current state and next steps

## Repository state

- Source work is in `rysweet/RabbitHole`.
- Private investigation artifacts are in `rysweet/drinkme` on branch `main`.
- Upstream issue/PR usage is prohibited. Findings are journaled in `drinkme`.
- The active source repo has guardrails in `AGENTS.md`.
- Current restarted campaign status is tracked in `docs/modernization/restarted-full-scope-status.md`.
- Latest desktop Run evidence is tracked in
  `docs/atlas/journal/0085-desktop-run-execution-evidence.md`.
  [RabbitHole PR #154](https://github.com/rysweet/RabbitHole/pull/154)
  records a narrow Run window attachment signal. It proves Alice put the Run
  panel into the Run window area. It does not prove pixels were drawn, does not
  prove the lesson finished, and is not grading.
- Latest eatme readiness documentation is tracked in
  `docs/atlas/journal/0086-eatme-pr92-rabbithole-evidence-readiness.md`.
  [eatme PR #92](https://github.com/rysweet/eatme/pull/92) merged at
  `cfe1f9e364d0015a3f97e237a9de5af670ae3bd6`. eatme now documents the
  RabbitHole evidence needed before first-lesson readiness can be marked ready:
  launch evidence, Run-window evidence, desktop execution evidence,
  screenshot/log/window artifacts, and `ui-action-contract.json`.
- Latest merge-state update is tracked in
   `docs/atlas/journal/0087-rabbithole-pr159-pr160-eatme-pr93-merge-status.md`.
  RabbitHole PR #159 adds a generated archive test for a missing Tweedle source
  entry that fails clearly; it does not add broad Tweedle decode support.
  RabbitHole PR #160 adds `desktop-run-pixel-boundary.json` with
  `status: "not_observed"` and records that pixel and screenshot proof were not
  observed by the Run-window attachment signal; it does not prove pixels,
  screenshots, visible rendering, or grading. eatme PR #93 makes readiness
   reports list the concrete RabbitHole readiness evidence categories they need;
   it does not create new runtime proof. These changes do not prove full Alice UI
   automation, visible rendering, desktop save-menu completion, grading, creative
   assessment, or first-lesson completion.
- Newest merge-state update is tracked in
  `docs/atlas/journal/0088-rabbithole-pr163-eatme-pr95-merge-status.md`.
  [RabbitHole PR #163](https://github.com/rysweet/RabbitHole/pull/163) rejects
  unsupported manifest-declared Tweedle type names with a clear error instead of
  silently dropping a type. [eatme PR #95](https://github.com/rysweet/eatme/pull/95)
  reports `desktop-run-pixel-boundary.json` as missing, invalid, or
  `not_observed`. These changes make failure states clearer; they do not prove
  full Alice UI automation, visible rendering, desktop save-menu completion,
  grading, creative assessment, or first-lesson completion.
- Latest merge-state update is tracked in
  `docs/atlas/journal/0089-rabbithole-pr164-eatme-pr96-merge-status.md`.
  [RabbitHole PR #164](https://github.com/rysweet/RabbitHole/pull/164) adds a
  constructor-bearing sibling archive test so that case also fails clearly
  instead of being silently dropped; it does not add full Tweedle decode support.
  [eatme PR #96](https://github.com/rysweet/eatme/pull/96) adds an
   `evidence_progress` summary that counts first-lesson evidence as present,
   missing, invalid, not observed, or blocked. These changes do not prove full
   Alice UI automation, visible rendering, desktop save-menu completion, grading,
   creative assessment, or first-lesson completion.
- Latest source-status update is tracked in
  `docs/atlas/journal/0090-rabbithole-pr166-pr167-eatme-pr98-merge-status.md`.
  [RabbitHole PR #166](https://github.com/rysweet/RabbitHole/pull/166) adds a
  generated archive test for a sibling Tweedle type with an unsupported complex
  field initializer; it does not add full Tweedle decode support.
  [RabbitHole PR #167](https://github.com/rysweet/RabbitHole/pull/167) adds
  `desktop-run-pixel-observation.json` so a run records a screenshot and center
  pixel when possible, or a blocker code and component state when not.
  [eatme PR #98](https://github.com/rysweet/eatme/pull/98) adds plain text
  output for first-lesson readiness progress and every required evidence item.
  These changes do not prove full Alice UI automation, visible rendering,
  desktop save-menu completion, grading, creative assessment, or first-lesson
  completion.
- Latest evidence-status update is tracked in
  `docs/atlas/journal/0091-rabbithole-pr168-pr169-eatme-pr99-merge-status.md`.
  [RabbitHole PR #168](https://github.com/rysweet/RabbitHole/pull/168) adds a
  generated archive test for a sibling Tweedle type with an unresolved parent; it
  does not add full Tweedle decode support.
  [RabbitHole PR #169](https://github.com/rysweet/RabbitHole/pull/169) adds
  machine-readable blocker details to `desktop-run-pixel-observation.json`.
  [eatme PR #99](https://github.com/rysweet/eatme/pull/99) reports
  `desktop-run-pixel-observation.json` beside readiness progress, including
  observed screenshot/sample data or blocked component state and blocker codes.
  These changes do not prove full Alice UI automation, visible rendering,
  desktop save-menu completion, grading, creative assessment, or first-lesson
  completion.
- Latest next-action status update is tracked in
  `docs/atlas/journal/0092-rabbithole-pr170-pr171-pr172-eatme-pr101-pr102-merge-status.md`.
  [RabbitHole PR #170](https://github.com/rysweet/RabbitHole/pull/170) falls
  back from the raw Run display target to the attached Run panel for pixel
  sampling while preserving exact blockers. [RabbitHole PR #171](https://github.com/rysweet/RabbitHole/pull/171)
  rejects resource-typed Tweedle field initializers instead of accepting them as
  plain strings; it does not add full Tweedle decode support. [RabbitHole PR #172](https://github.com/rysweet/RabbitHole/pull/172)
  adds `desktop-first-lesson-next-action.json`, naming the missing deterministic
  Save-menu and code/procedure action targets. [eatme PR #101](https://github.com/rysweet/eatme/pull/101)
  shows explicit next-action evidence in first-lesson plain output. [eatme PR #102](https://github.com/rysweet/eatme/pull/102)
  adds the `media-audio-cue-storyboard` student scenario for
  `media-audio-creator`; it does not grade student work. These changes do not
  prove full Alice UI automation, visible rendering, desktop save-menu
  completion, grading, creative assessment, or first-lesson completion.

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
  [RabbitHole PR #185](https://github.com/rysweet/RabbitHole/pull/185) merged model resource array grouping, skip behavior, and
  duplicate index rejection tests. [RabbitHole PR #187](https://github.com/rysweet/RabbitHole/pull/187) merged narrow `TextString label <- null`
  parsing and decoding to `NullLiteral`. [RabbitHole PR #188](https://github.com/rysweet/RabbitHole/pull/188) merged `ProcedureTabSelection`, tests, and a reference doc as a design
  and test boundary, not live procedure invocation. [RabbitHole PR #190](https://github.com/rysweet/RabbitHole/pull/190) merged
  `IssueReportWorker` non-retryable failure tests. [RabbitHole PR #191](https://github.com/rysweet/RabbitHole/pull/191) restored the Maven
  cache fallback, fixed the stuck coverage path, and left coverage run
  `25492250204` plus develop checks after PR #190 successful. PR #187, PR #188,
  and PR #190 were delayed by stuck coverage behavior and transient `jogamp.org`
  network failures.
- Previous RabbitHole source evidence is tracked in
  `docs/atlas/journal/0095-rabbithole-pr207-pr208-source-evidence.md`.
  [RabbitHole PR #207](https://github.com/rysweet/RabbitHole/pull/207) merged Numeric and Boolean Tweedle `null` field initializer
  decoding to AST `NullLiteral` while still rejecting primitive statement
  contexts such as `if(null)` and `while(null)`. [RabbitHole PR #208](https://github.com/rysweet/RabbitHole/pull/208) records Save
  operation completion evidence; its head before merge was
  `153f4e4ce77415d42e6f1047abcc2074671ae4c8`, all GitHub checks passed, and it
  merged at `8799854787655ca61b6fad9378377b19d41aa7b1`. The 70 percent aggregate
  coverage target, live procedure invocation, desktop edit command, full desktop
  Save menu completion, dialogs, grading, rendering, first-lesson completion,
  deployed sharing, and full Tweedle/player decode support remain unproven.
- Previous RabbitHole source wave status is tracked in
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
- Latest RabbitHole and eatme source wave status is tracked in
  `docs/atlas/journal/0098-rabbithole-pr214-pr215-pr216-pr218-eatme-pr120-pr121-status.md`.
  [RabbitHole PR #214](https://github.com/rysweet/RabbitHole/pull/214) merged at
  `2155904f38e55323b00d732b7f64e957db4406f5` and proves launcher drawing
  surface readiness through `Stage.show()` and `isShowing()` and adds a `render-target-unavailable` no-go
  path; visible pixels, deployed installer success, and full world execution
  remain unproven. [RabbitHole PR #215](https://github.com/rysweet/RabbitHole/pull/215) merged at
  `c727d97c3d71a0f045925a691a080a42d36fbe9d` and decodes empty `void` Tweedle
  methods to AST `UserMethod`; parameters, method bodies, non-void methods, and constructors
  still fail clearly. [RabbitHole PR #216](https://github.com/rysweet/RabbitHole/pull/216) merged at
  `c84bdf826723284e84b4872ce2e6c791dee0c8a6` and adds Save dialog discovery
  target evidence;
  live Save menu click, actual dialog display/control, selected path automation,
  full lesson completion, rendering, and grading remain unproven. [RabbitHole PR #218](https://github.com/rysweet/RabbitHole/pull/218) merged at
  `a568bae3c3960c60792351cfa423450fea51b067` and adds launcher render
  observation proof, but visible pixels remain unobserved.
  [eatme PR #120](https://github.com/rysweet/eatme/pull/120) merged at
  `f526544014ee8d368a623359f6bf97cce6588f7d` and adds the next first-lesson
  action reporting/proof slice, while real
  desktop proof, procedure edit/run/save UI automation, and manual real Alice
  smoke remain incomplete. [eatme PR #121](https://github.com/rysweet/eatme/pull/121) merged at
  `4ade2a5d6def4d7ad7be7691b9349a3f5c9ff61e` and improves real desktop proof
  reporting/status,
  but actual real desktop proof/manual Alice smoke, procedure edit/run/save UI
  automation, project save, and full first-lesson completion remain incomplete.
- Latest RabbitHole source update is tracked in
  `docs/atlas/journal/0099-rabbithole-pr219-pr222-pr224-pr225-pr229-pr230-pr231-pr234-status.md`.
  [RabbitHole PR #219](https://github.com/rysweet/RabbitHole/pull/219) merged at
  `144081e1067cd8795666e5ee8802f47fbfefe671` and decodes empty no-argument
  Tweedle constructors to AST `NamedUserConstructor`; constructor parameters and
  constructor bodies still failed clearly at that point.
  [RabbitHole PR #222](https://github.com/rysweet/RabbitHole/pull/222) merged at
  `f749ed7cc92f7df4678e96bbb29bcbd0b09913b8` and proves
  `SaveProjectOperation.fire(UserActivity)` reaches
  `AbstractSaveOperation.perform`, but the non-desktop proof lacks
  `StageIDE.getActiveInstance()`.
  [RabbitHole PR #224](https://github.com/rysweet/RabbitHole/pull/224) merged at
  `1a3eae6937a7109f3608112a7fb40519e1a4f8d7` and proves JavaFX cannot open
  `DISPLAY` locally; visible rendering correctness remains unproven.
  [RabbitHole PR #225](https://github.com/rysweet/RabbitHole/pull/225) merged at
  `db44c10bd017a5b7cc8eddc1cc82b1d1b90c8fb8` and decodes required Tweedle
  constructor parameters to AST `UserParameter`; optional constructor parameters
  still fail clearly.
  [RabbitHole PR #229](https://github.com/rysweet/RabbitHole/pull/229) merged at
  `7953c8348272298e9cb85f2319fba6520ba51a32` and decodes required parameters for
  empty `void` Tweedle methods to AST `UserParameter`; optional method parameters
  still fail clearly.
  [RabbitHole PR #230](https://github.com/rysweet/RabbitHole/pull/230) merged at
  `31d506f6af59ef736ccefad9aa7b793b3add6a3d` and proves Save action invocation
  under Xvfb with `status=action_invoked`, `StageIDE=true`, and
  `ProjectDocumentFrame=true`; menu click, dialog display/control, selected path
  automation remain unproven, and completed save remains unproven.
  [RabbitHole PR #231](https://github.com/rysweet/RabbitHole/pull/231) merged at
  `622748401fe8ff00d81d3a2851faac153585b76c` and observes generated launcher
  Xvfb marker pixels; real Alice desktop pixels were not observed because
  `mvn exec:java -Dalice-ide` fails with `org.alice.stageide.EntryPoint`
  `ClassNotFoundException`.
  [RabbitHole PR #234](https://github.com/rysweet/RabbitHole/pull/234) merged at
  `45d937fbe1e9ddee74e7c2b89af31841fb38a202` and decodes single
  primitive-literal Tweedle `return` method bodies to AST `ReturnStatement`;
  full method decode, full player decode, and full Tweedle decode support remain
  unproven.
- Latest RabbitHole source update is tracked in
  `docs/atlas/journal/0100-rabbithole-pr235-through-pr259-status.md`.
  [RabbitHole PR #235](https://github.com/rysweet/RabbitHole/pull/235) merged at
  `a6ebc43a0e09219c5f6d1a8e1e7d2f3c4b5a6d7e` and proves Save menu item dispatch
  into the Save action path under Xvfb; Save dialog display and Save dialog control
  remain unproven.
  [RabbitHole PR #237](https://github.com/rysweet/RabbitHole/pull/237) merged at
  `70deb2e159672cc41c5a9da9f3ec01a5d53c11df` and fixes the Alice launch classpath
  so `org.alice.stageide.EntryPoint` is on the Maven exec classpath; does not
  prove visible rendering, deployed installer success, or full world execution.
  [RabbitHole PR #238](https://github.com/rysweet/RabbitHole/pull/238) merged at
  `f9c832b8a86ea7d8c1e4d5b3c9f2a1e6d4b7c8f0` and decodes the narrow case of a
  single Tweedle `return` of a required method parameter identifier to AST
  `ParameterAccess`; full method body, constructor body, player, and complete
  Tweedle decode support remain unproven.
  [RabbitHole PR #240](https://github.com/rysweet/RabbitHole/pull/240) merged at
  `ae3d8de57aec10d2f9c3b7e1a5c6d8f4e2b1c9a3` and adds an `x-window-inventory.json`
  to the Xvfb Alice launch proof; blocked at `alice-window-not-found` after the
  classpath fix.
  [RabbitHole PR #241](https://github.com/rysweet/RabbitHole/pull/241) merged at
  `d2ab990dffa8c7e5b9a3d1f6c4e2b8d7a5c0f1e9` and adds an opt-in selected-path
  automation seam at `FileDialogUtilities.showSaveFileDialog`, rejecting outside
  paths and symlink escapes; Save dialog display and control remain unproven.
  [RabbitHole PR #245](https://github.com/rysweet/RabbitHole/pull/245) merged at
  `9cc5893d8b67e4d1b8a3c7f2e5d6c9b4a1e8f3d2` and adds an
  `application-root-error.json` probe that maps the `Application Root Error` window
  to the `org.alice.ide.rootDirectory` condition and next invocation change needed.
  [RabbitHole PR #246](https://github.com/rysweet/RabbitHole/pull/246) merged at
  `2fe47f4ebaea9d7c3b5a1e8f4d6c2b9a7e5d3c8f` and proves
  `ProjectDocumentFrame.showSaveFileDialog` reaches `FileDialogUtilities` with a
  displayable `JFrame` root under Xvfb; Save dialog display and control remain
  unproven.
  [RabbitHole PR #247](https://github.com/rysweet/RabbitHole/pull/247) merged at
  `0a75eb7a21f5d3c9b7e2a4d6f1c8b5e9d2a7c3f6` and decodes narrow Tweedle
  constructor bodies with primitive-literal local variable declarations to AST
  `LocalDeclaration`; full Tweedle constructor, method, player, and resource decode
  remain unproven.
  [RabbitHole PR #250](https://github.com/rysweet/RabbitHole/pull/250) merged at
  `c640c3fbd9ef5a7d1c8b2e4f6a9d3c7b5e1a8f2d` and adds a `rootDirectory` prep
  helper that verifies `alice-ide` configures `org.alice.ide.rootDirectory` and
  prepares `core/resources/target/distribution` before the Xvfb launch, recording
  the precise `Application Root Error` blocker artifacts.
  [RabbitHole PR #253](https://github.com/rysweet/RabbitHole/pull/253) merged at
  `39635ffd10108d5c9b2e4a7f3d1c6e8b5a9d2c7f` and decodes method return identifiers
  that refer to declared Tweedle fields as AST `FieldAccess` expressions; field
  return type-mismatch cases are rejected clearly; full method, assignment,
  member-expression, and player decode remain unproven.
  [RabbitHole PR #254](https://github.com/rysweet/RabbitHole/pull/254) merged at
  `88e8cffffa7c2b5d9e1a4c7f3d6b8e2a5c9d1f4b` and adds a first-run license QA
  bypass: a focused License Agreement dialog probe and explicit test-only Java
  Preferences acceptance using isolated `java.util.prefs.userRoot` state, with
  license acceptance and dialog artifacts recorded in Xvfb launch evidence.
  [RabbitHole PR #255](https://github.com/rysweet/RabbitHole/pull/255) merged at
  `c8d52a9a8865f3d7b1e9c4a6d2f5c8b3e7a1d9c4` and adds a `SaveOperationFlow`
  Xvfb-safe proof that writes a real `.a3p` project file to a controlled selected
  path via `FileDialogUtilities` selected-path automation, recording
  `saved_file_exists` and `saved_file_size_bytes`; does not prove live Save dialog
  display or desktop save-menu completion.
  [RabbitHole PR #259](https://github.com/rysweet/RabbitHole/pull/259) merged at
  `e5b0ac5fce21b4eee1e13ea5861d2e9cee538ca8` and decodes Tweedle method returns of
  `this.field` into AST `FieldAccess`; assignments, optional params, broader member
  expressions, resource initializers, and full Tweedle/player decode remain
  unproven.
  [RabbitHole PR #260](https://github.com/rysweet/RabbitHole/pull/260) merged at
  `b553677c1225d704d1d951a59653fb0f66096139`. A Swing `JFileChooser` dialog was
  observed under Xvfb and approved through the chooser's controls; native
  `java.awt.FileDialog` peer control and the full StageIDE Save-menu-to-real-chooser
  journey remain unproven.
  [RabbitHole PR #261](https://github.com/rysweet/RabbitHole/pull/261) merged at
  `97c1ae707544bd0ca89e711df92e7e45e6d377ac`. The Select Project Java window was
  observed under Xvfb with title, class, process, and geometry; selecting or
  opening a project, world execution, and installer success remain unproven.
  [RabbitHole PR #262](https://github.com/rysweet/RabbitHole/pull/262) merged at
  `9ef09e05402b2e0af9c07803eee92aa5db29b325`. Primitive literal field assignments
  in Tweedle method bodies now decode, with clear unsupported-form failures; full
  Tweedle/player decode remains unproven.
  [eatme PR #122](https://github.com/rysweet/eatme/pull/122) merged at `41142db`.
  Adds the `lost-robot-debug-museum` instructor/student scenario for the
  reflective-debugger/debug-coach use case; grading, creative
  assessment, real Alice UI automation, and full lesson delivery remain unproven.
  [eatme PR #123](https://github.com/rysweet/eatme/pull/123) merged at
  `773fb3df7a6ec234c5f317eefdfea82916ecd7bc`. Adds the
  `weather-wizard-conditional-theater` instructor/student scenario, the next
  `creative_new` teaching/learning gap fill; scenario assets grew from 71 to 73.
  Grading, automated creative assessment, real Alice UI automation, and full
  lesson delivery remain unproven.
  [RabbitHole PR #264](https://github.com/rysweet/RabbitHole/pull/264) merged at
  `a4386130d66b97feecdbcb5ab1b6bc765392deb3`. Primitive literal field assignments
  in Tweedle constructor bodies now decode, with clear failures for unsupported
  constructor assignment forms; full Tweedle/player decode remains unproven.
  [eatme PR #124](https://github.com/rysweet/eatme/pull/124) merged at
  `d3bb687145b6c9e38601703c691aa7f6bcbb4862`. Adds the
  `alien-linguist-parameter-dialogue` instructor/student scenario; scenario
  assets grew from 73 to 75 with all adapters fresh. Grading, automated creative
  assessment, real Alice UI automation, and full lesson delivery remain unproven.
  [RabbitHole PR #265](https://github.com/rysweet/RabbitHole/pull/265) merged at
  `ead3a465a6c794f552edc32699f011242fc303d7`. `DocumentFrame.showSaveFileDialog`
  reaches a live `JFileChooser` under Xvfb via a running StageIDE instance.
  Records that `FileDialogUtilities.createFileDialog()` returns `SwingFileDialog`
  on Linux so native `java.awt.FileDialog`/`XFileDialogPeer` is never
  instantiated on this path. Full Save-menu-to-written-project journey remains
  unproven.
  [RabbitHole PR #266](https://github.com/rysweet/RabbitHole/pull/266) merged at
  `2fe0ba4ef5d94e5516e9975f00fea9c23ff79ac9`. AT-SPI bus is reachable and
  Alice's Java process registers via `libatk-wrapper.so`; Swing components are
  not accessible in the `exec:java` context; exact remediation path documented.
  Select Project widget enumeration and project opening remain unproven.
  [RabbitHole PR #267](https://github.com/rysweet/RabbitHole/pull/267) merged at
  `2ca7aa1062ee94b4e10eb8a13cdad8a4f4cfabc6`. Primitive literal local variable
  reassignment in Tweedle method and constructor bodies now decodes; full
  Tweedle/player decode remains unproven.
  [eatme PR #125](https://github.com/rysweet/eatme/pull/125) merged at
  `847c09d20be16435595e1368f8f96c495fc6e4f5`. Adds the
  `ecosystem-balance-loop-simulation` instructor/student scenario; scenario
  assets grew from 75 to 77 with all 38 Gadugi adapters fresh. Grading,
  automated creative assessment, real Alice UI automation, and full lesson
  delivery remain unproven.
  [RabbitHole PR #269](https://github.com/rysweet/RabbitHole/pull/269) merged at
  `ce31df5c04401f7ddb759c9d6640ca2881f82c4f`. Tweedle optional method and
  constructor parameters now decode as Alice `UserParameter` entries. Default
  values are not represented because the Alice AST has no optional-parameter
  concept and `TweedleOptionalParameter` exposes no default accessor. Full
  Tweedle/player decode remains unproven.
  [eatme PR #126](https://github.com/rysweet/eatme/pull/126) merged at
  `72731e2e7dd092292f982408faad5a2e98d7e74a`. Adds the
  `time-travel-recipe-sequencing` instructor/student scenario; scenario assets
  grew from 77 to 79 with all adapters fresh. Grading, automated creative
  assessment, real Alice UI automation, and full lesson delivery remain unproven.
  [eatme PR #127](https://github.com/rysweet/eatme/pull/127) merged at
  `e0c090f265f0dfb2f0b662616aac8b6cb078dae6`. Adds the
  `mars-rover-proximity-mission` instructor/student scenario; scenario assets
  grew from 79 to 81 with all 40 generated gadugi adapters fresh. Grading,
  automated creative assessment, real Alice UI automation, and full lesson
  delivery remain unproven.
- Latest RabbitHole source update is tracked in
  `docs/atlas/journal/0101-rabbithole-pr260-pr261-pr262-eatme-pr122-status.md`.
  eatme PR #123 is tracked in
  `docs/atlas/journal/0102-eatme-pr123-weather-wizard-status.md`.
  RabbitHole PR #264 and eatme PR #124 are tracked in
  `docs/atlas/journal/0103-rabbithole-pr264-eatme-pr124-status.md`.
  RabbitHole PR #265, PR #266, and PR #267 are tracked in
  `docs/atlas/journal/0104-rabbithole-pr265-pr266-pr267-status.md`.
  eatme PR #125 is tracked in
  `docs/atlas/journal/0105-eatme-pr125-ecosystem-balance-loop-status.md`.
  RabbitHole PR #269 and eatme PR #126 are tracked in
  `docs/atlas/journal/0106-eatme-pr126-rabbithole-pr269-status.md`.
  eatme PR #127 is tracked in
  `docs/atlas/journal/0107-eatme-pr127-mars-rover-proximity-mission-status.md`.
  RabbitHole PR #270 is tracked in
  `docs/atlas/journal/0108-rabbithole-pr270-identifier-rhs-status.md`.
  RabbitHole PR #271 and eatme PR #129 are tracked in
  `docs/atlas/journal/0109-rabbithole-pr271-eatme-pr129-status.md`.
  RabbitHole PR #272, PR #273, and eatme PR #131 are tracked in
  `docs/atlas/journal/0110-rabbithole-pr272-pr273-eatme-pr131-status.md`.
  RabbitHole PR #274 is tracked in
  `docs/atlas/journal/0111-rabbithole-pr274-arithmetic-binary-status.md`.
  RabbitHole PR #276 is tracked in
  `docs/atlas/journal/0112-rabbithole-pr276-save-menu-doclick-status.md`.
  RabbitHole PR #277 is tracked in
  `docs/atlas/journal/0113-rabbithole-pr277-tweedle-string-concat-status.md`.
  RabbitHole PR #278 and eatme PR #132 are tracked in
  `docs/atlas/journal/0114-rabbithole-pr278-select-project-atapi-status.md` and
  `docs/atlas/journal/0115-eatme-pr132-accessibility-rescue-camera-captions-status.md`.
  RabbitHole PR #281 is tracked in
  `docs/atlas/journal/0116-rabbithole-pr281-save-proof-flag-fix-status.md`.
  eatme PR #133 is tracked in
  `docs/atlas/journal/0117-eatme-pr133-design-process-story-or-game-status.md`.
  RabbitHole PR #282 is tracked in
  `docs/atlas/journal/0118-rabbithole-pr282-relational-comparison-status.md`.
  RabbitHole PR #284 is tracked in
  `docs/atlas/journal/0119-rabbithole-pr284-save-proof-ordering-fix-status.md`.
  RabbitHole PR #285 is tracked in
  `docs/atlas/journal/0120-rabbithole-pr285-atapi-main-window-post-project-open-status.md`.
  eatme PR #134 is tracked in
  `docs/atlas/journal/0121-eatme-pr134-setup-preflight-ready-to-create-status.md`.
  eatme PR #135 is tracked in
  `docs/atlas/journal/0122-eatme-pr135-audio-camera-and-export-sharecase-status.md`.
  [RabbitHole PR #272](https://github.com/rysweet/RabbitHole/pull/272) merged at
  `458bed0f4b409d207a2610b8ccfa8e8dfbbce6c9`. Proves AT-SPI reaches the Alice
  Java process via `exec:exec` and `NO_AT_BRIDGE=1`; top-level Swing widgets are
  observable. Tab labels are not visible or enumerable. Project selection and
  opening are not proven.
  [RabbitHole PR #273](https://github.com/rysweet/RabbitHole/pull/273) merged at
  `c86e8c4747b73921e8c432709c8cf7a741848855`. Proves `SaveProjectOperation.fire()`
  reaches a live `JFileChooser`, a background probe approves it, and a non-empty
  `.a3p` is written. Visible rendering, grading, the native FileDialog path, and a
  full Save menu item `doClick`-to-written-file journey remain unproven.
  [eatme PR #131](https://github.com/rysweet/eatme/pull/131) merged at
  `973b65f`. Adds the `neighborhood-data-story` instructor/student scenario;
  scenario assets grew from 83 to 85 with all Gadugi adapters fresh.
  [RabbitHole PR #274](https://github.com/rysweet/RabbitHole/pull/274) merged at
  `5571894e5152482c9fb26ba31fc3d633d372e88e`. Arithmetic binary expressions
  (`+`, `-`, `*`, `/`) now decode as Tweedle assignment right-hand-side values
  and as local variable initializer values. String concatenation, logical and
  comparison expressions, method calls, non-`this` member assignment targets,
  loops, conditionals, resource field initializers, and full Tweedle/player
  decode remain unproven.
  [RabbitHole PR #276](https://github.com/rysweet/RabbitHole/pull/276) merged at
  `66b38f87090f633f44a403737778c3c01a01c52b`. A programmatically-created real
  Save menu item has `doClick()` called on it; this dispatches through Croquet,
  reaches a live `JFileChooser`, the dialog is approved by a background probe,
  and a non-empty `.a3p` file is written. Real rendered desktop menu bar
  navigation, native FileDialog, visible rendering, grading, and full lesson
  completion remain unproven.
  [RabbitHole PR #277](https://github.com/rysweet/RabbitHole/pull/277) merged at
  `8c1a3fd32c2c1d19aac7ea265909f0d19276273e`. Tweedle string concatenation (`..`)
  now decodes in assignment right-hand-side values, local variable initializers,
  and method return expressions. Logical and comparison expressions, method calls,
  non-`this` member assignment targets, loops, conditionals, resource field
  initializers, and full Tweedle/player decode remain unproven.
  [RabbitHole PR #278](https://github.com/rysweet/RabbitHole/pull/278) merged at
  `e130dac3a6f6431895f72f71733a042f1bb92cb3`. Select Project tab labels are
  accessible as AT-SPI toggle buttons at depth 11; all five tabs can be clicked
  programmatically; Starters -> Africa Full -> OK causes `projectOpenObserved: true`
  and the Select Project frame disappears. Real rendered desktop menu bar
  navigation, native FileDialog, visible rendering, grading, and full lesson
  completion remain unproven.
  [eatme PR #132](https://github.com/rysweet/eatme/pull/132) merged at
  `ebaf93e85a502f4778aaa194f4cd61ae8ae4cdda`. Adds the
  `accessibility-rescue-camera-captions` instructor/student scenario and Gadugi
  adapter; scenario asset count grew to 87. Remaining missing scenario files:
  design-process-story-or-game, audio-camera-and-export-sharecase,
  setup-preflight-ready-to-create. Grading, automated creative assessment, real
  Alice UI automation, and full lesson delivery remain unproven.
  [RabbitHole PR #281](https://github.com/rysweet/RabbitHole/pull/281) merged at
  `daaceb0a9648d18e890c5b106327d2ddbe489149`. Fixes the Save menu doClick test
  proof bookkeeping: `approvedSelection` is now set before `approveSelection()`
  is called so the probe cannot falsely report unsupported after a successful
  write. Does not expand Save proof scope beyond PR #276. Real rendered desktop
  menu bar navigation, native FileDialog, visible rendering, grading, and full
  lesson completion remain unproven.
  [eatme PR #133](https://github.com/rysweet/eatme/pull/133) merged at
  `7d0d05726b970dc9a616ed8aa633e090ceebf88b`. Adds the
  `design-process-story-or-game` instructor/student scenario and Gadugi adapter;
  scenario asset count grew from 87 to 89. Remaining missing scenario files:
  audio-camera-and-export-sharecase, setup-preflight-ready-to-create. Grading,
  automated creative assessment, real Alice UI automation, and full lesson
  delivery remain unproven.
  [RabbitHole PR #282](https://github.com/rysweet/RabbitHole/pull/282) merged at
  `81db4122fc3270e2a16a02c46c4a1d7f254717e3`. Decodes Tweedle relational
  comparison expressions (`==`, `!=`, `<`, `<=`, `>`, `>=`) to
  `RelationalInfixExpression` in local initializers, assignment right-hand sides,
  and method returns. Logical expressions, method calls, non-`this` member
  targets, loops, conditionals, resource initializers, and full Tweedle/player
  decode remain unproven.
  [RabbitHole PR #284](https://github.com/rysweet/RabbitHole/pull/284) merged at
  `eca3fb920e3d2b13f5de7117ccc96308378a10f6`. Fixes `approvedSelection` ordering
  in `StageIdeSaveMenuE2EWriteProofTest` and `SaveFileDialogShowControlProofTest`
  so all Save proof tests set the proof flag before the approval call. Proof
  bookkeeping only; does not expand Save proof scope beyond PR #276.
  [RabbitHole PR #285](https://github.com/rysweet/RabbitHole/pull/285) merged at
  `8eaa066f98ab173bfa6d0d08f804b5e4eb47a7be`. Proves Alice 3 main-window AT-SPI
  state after Select Project dismissal via `post-project-open-probe.py`. Requires
  `projectOpenObserved=true`, waits five seconds, enumerates top-level frames,
  and records blockers. Full scene load, visible rendering, UI correctness,
  grading, and lesson completion remain unproven.
  [eatme PR #134](https://github.com/rysweet/eatme/pull/134) merged at
  `294ca3319863098c11e3abd712dc661b44a6278e`. Adds the
  `setup-preflight-ready-to-create` instructor/student scenario and Gadugi
  adapter; scenario asset count grew from 89 to 91. Remaining missing scenario
  file: audio-camera-and-export-sharecase. Grading, automated creative
  assessment, real Alice UI automation, and full lesson delivery remain unproven.
  [eatme PR #135](https://github.com/rysweet/eatme/pull/135) merged at
  `8f82d682aef4d22c3ca4e7bdc4344cae660b13bd`. Adds the
  `audio-camera-and-export-sharecase` instructor/student scenario and Gadugi
  adapter; scenario asset count grew from 91 to 93. No remaining scenario gaps
  from the list in `docs/persona-assets.md` and
  `assets/personas/alice-user-crew.yaml`. Grading, automated creative
  assessment, real Alice UI automation, and full lesson delivery remain unproven.
  [RabbitHole PR #270](https://github.com/rysweet/RabbitHole/pull/270) merged at
  `b887a14e85a514b5bf7504eeffd3fbeff490e0a2`. Assignment statements in Tweedle
  method and constructor bodies can now decode an `IdentifierReference` RHS to
  `ParameterAccess`, `LocalAccess`, or `FieldAccess`. Constructor assignment
  bodies now receive `UserParameter[]` so constructor setter patterns resolve
  parameter RHS. Non-`this` member assignment targets, non-literal/non-identifier
  RHS, loops/calls/conditionals, resource initializers, and full Tweedle/player
  decode remain unproven.
  [RabbitHole PR #271](https://github.com/rysweet/RabbitHole/pull/271) merged at
  `b49b898ddfd2c19a27ce88d265f2c723499b1454`. Local variable declarations in
  Tweedle method and constructor bodies now decode an `IdentifierReference`
  initializer to `LocalAccess`, `ParameterAccess`, or `FieldAccess`. Full
  Tweedle/player decode remains unproven.
  [eatme PR #129](https://github.com/rysweet/eatme/pull/129) merged at
  `b72afe499c9b7a3826012b7d10c69b5ae6b6c0a1`. Adds the
  `creature-choreography-loop-lab` instructor/student scenario; scenario assets
  grew from 81 to 83 with all Gadugi adapters fresh. Grading, automated creative
  assessment, real Alice UI automation, and full lesson delivery remain unproven.
- Latest restarted-wave source work integrated into `develop` includes:
  - Alice PR #35: extracted model resource XML generation.
  - Alice PR #36: added reporting-only module coverage baseline tooling.
  - Alice PR #37: added IO load/save characterization tests.
  - Alice PR #38: expanded outside-in Alice desktop QA scenarios.
  - Alice PR #39: characterized JSON/XML player program boundary null-safety.
  - Alice PR #40: characterized Story API generated code and repaired stale cached foreach item names.
  - Alice PR #42: added starter project XML fallback readability tests.
  - Alice PR #43: added headless Croquet tool palette layout tests.
  - Alice PR #44: added scenegraph model characterization tests and fixed `Joint` bounds/scale behavior.
  - Alice PR #45: added no-Sims nonfree boundary guards and includeSims library overwrite validation.
  - Alice PR #46: characterized NetBeans export classpath with populated `Alice3Library` entries.

## Build and CI state

The no-Sims local and CI path is healthy. RabbitHole PR #191 restored the Maven cache fallback, fixed the stuck coverage path, and coverage run `25492250204` completed successfully after merge. Develop checks after PR #190 also completed successfully at `fd71bfb96fe9c82aa4cdd3de8f967f7c410af629`.

Current important checks:

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
- model resource XML metadata, manifest behavior, tag parsing, subresource lookup, array grouping, skip behavior, duplicate index rejection, and edge cases;
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
- Tweedle `TextString`, Numeric, and Boolean `null` field initializer decoding to AST `NullLiteral`, while primitive statement contexts such as `if(null)` and `while(null)` still fail;
- literal sized Tweedle array field initializer support such as `new WholeNumber[2]`, while non-literal sizes still fail clearly;
- duplicate-safe and path-safe JSON/player resource zip entries;
- headless editor save-copy archive shape and reload fidelity through `ProjectFileUtilities`;
- AST-referenced image resource editor save-copy and reopen fidelity;
- project save/export snapshot source selection and default auto-backup migration;
- project save target planning for new/default-backup/backup saves;
- NetBeans generated launcher shape, launcher argument handoff, and launcher/runtime proof beyond the earlier `Program.main` null-Stage guard;
- NetBeans project-template archive and generated metadata;
- exported build-property contract;
- `Alice3Library` registration and packaging source;
- populated `Alice3Library` compile classpath entries, including authorized JavaFX and includeSims/nonfree boundary variants;
- NetBeans package-phase CI and artifact assertions;
- NetBeans template compiler-surrogate structure;
- NetBeans install NBM rename behavior and timeout-hardened Ant smoke handling;
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
- story API call on `SProgram`;
- story-api keyboard event characterization tests, with reported `core/story-api` coverage moving from 4.55% to 6.21% and 260 more covered lines.
- generated foreach loops with stale cached `COUNT__` item names, now repaired to readable generated item names while preserving explicit item names;
- committed starter `.a3p` archive XML fallback readability for representative fixtures;
- headless Croquet tool-palette layout invariants;
- scenegraph Mesh, WeightedMesh, SkeletonVisual, and Joint behavior, including Joint scale/bounds fixes;
- public no-Sims package boundaries and authorized includeSims library overwrite behavior;
- `ProcedureTabSelection` design and tests for future procedure UI work;
- `IssueReportWorker` non-retryable failure behavior;

## Important findings

- Characterization is still early relative to the size of Alice.
- Current coverage is far below the 70% target; the latest coverage run completed successfully, but 70 percent aggregate coverage remains unproven.
- Many production classes still exceed the desired 500-line target; the latest reported hotspot count found 52 Java files over 500 lines.
- NetBeans Java export is a high-value seam because it is both compatibility-sensitive and teaching-facing.
- Model resource export now has its first active no-Sims characterization, but only for XML serialization and generated resource Java compilation.
- NetBeans export now has a standalone-style compile/launcher smoke, but not a full Ant/NetBeans run with a populated `Alice3Library`.
- NetBeans export now also has a template-shaped project smoke that extracts the packaged template, checks the `Alice3Library` classpath contract, and compiles generated sources into `build/classes` using the test classpath as a surrogate.
- The template-shaped NetBeans compile smoke now verifies the template build/classpath properties and resolves its classes directory from the template rather than hardcoding `build/classes`.
- Generated source now includes one actual story API call smoke, `this.setSimulationSpeedFactor(1.5);`, in a new focused test class.
- `ProjectFileUtilities.exportCopyOfProjectTo` now has a headless player artifact smoke for version, manifest, thumbnail, and program Tweedle entries.
- Resource-bearing player export now proves referenced image bytes and manifest metadata are written. `IoUtilities.readProject(...)` now routes manifest-declared `.a3w` archives to `JsonProjectIo` and can restore manifest-listed image resources, but Tweedle program-type decoding is still not implemented.
- Narrow `TextString` null decoding now exists, but broader null support, method and constructor body decode, complete player decode, and full Tweedle decode support remain open.
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
- Generated foreach loops no longer emit stale cached synthetic `COUNT__` item names; the repaired path emits readable generated item names and preserves explicit item names.
- Iterable foreach loops over a generated `Arrays.asList(...)` expression compile and import `java.util.Arrays`; the current characterization preserves explicit item local naming.
- Public no-Sims package checks now assert nonfree jars are omitted, while authorized includeSims checks assert `models-nonfree.jar` and `story-api-nonfree.jar` are restored through an explicit resources overwrite.
- Starter `.a3p` fixtures now prove XML fallback readability for selected committed archives, but not full semantic migration of historical project content.
- Headless Croquet and scenegraph characterization caught real behavior seams without requiring a full JavaFX desktop.
- Headless tests can cover important exported-code behavior without launching real JavaFX.
- Real JavaFX/UI behavior, story execution, and rendering-adjacent behavior remain mostly unprotected.
- Git LFS budget exhaustion can break CI checkout if no-Sims workflows fetch LFS objects; no-Sims CI should avoid LFS unless a job explicitly needs it.
- Process correction: every coding track and subagent must follow `DEFAULT_WORKFLOW`; parallel coding should use isolated worktrees/branches, while this main track remains serialized for integration.
- Loop 62 proved the parallel pattern: six isolated implementation branches were developed concurrently, then rebased and integrated sequentially behind local checks and CI.
- Loop 63 extended that pattern: implementation tracks ran in parallel, but integration remained serialized and CI-checked after each meaningful merge.
- Loop 64 recovery/integration completed the crash-resume work:
  - Alice `develop` integrated formal specs/recovery contracts, source save/export tests, Story IO/NetBeans quality fixes, outside-in QA hardening, Wave2 Story JSON boundaries, Wave2 NetBeans export harness, and Wave2 outside-in QA scenarios.
  - `eatme` `master` integrated the Building-a-Scene and Code Editor first-run lesson smoke tracks.
  - `gadugi-agentic-test` `main` integrated the `cwd`/`workingDirectory` scenario command fix.
- Code-atlas and crusty review branches remained outside Alice source and were routed to drinkme artifacts instead.

- `tweedle-lang` is a required git submodule for `core/tweedle` ANTLR parser generation. Missing it in worktrees causes `TweedleParser`/`TweedleParserBaseVisitor` compile failures; see `docs/build-baseline/submodule-working-guide.md`.
- Recovered artifact-only tracks have been consolidated into `drinkme` rather than Alice source:
  - Crusty modernization review: `docs/artifacts/alice-audit/2026-05-03-crusty-modernization-review.md`.
  - Code-atlas bug-hunt artifacts: `docs/artifacts/alice-audit/code-atlas-alice-source-truth.md`, `docs/artifacts/alice-audit/code-atlas-alice-bughunt-findings.md`, `docs/artifacts/alice-audit/code-atlas-alice-hotspots.md`, `docs/artifacts/alice-audit/code-atlas-alice-staleness-map.md`, and the companion module graphs.
  - Formal save/load/export specification artifacts: `docs/artifacts/alice-audit/formal-spec/evaluation.md`, Gherkin scenarios, TLA+ recovery model/config, and usage/reference notes under `docs/artifacts/alice-audit/formal-spec/`.
- This recovery wave is closed: the source/support-tool workstreams that passed review were integrated, and the artifact-only tracks were preserved in drinkme without merging inappropriate runtime code into Alice.

## Merged source PR status

| Work item | Plain status |
| --- | --- |
| [RabbitHole PR #154](https://github.com/rysweet/RabbitHole/pull/154) | Merged. Records that Alice put the Run panel into the Run window area. |
| [RabbitHole PR #155](https://github.com/rysweet/RabbitHole/pull/155) | Merged. Records launcher steps and no-go messages, but does not prove rendering. |
| [RabbitHole PR #156](https://github.com/rysweet/RabbitHole/pull/156) | Merged. Keeps old image recovery while safely rejecting unsupported old code. |
| [RabbitHole PR #159](https://github.com/rysweet/RabbitHole/pull/159) | Merged. This repo records only that the PR landed. |
| [RabbitHole PR #160](https://github.com/rysweet/RabbitHole/pull/160) | Merged. This repo records only that the PR landed. |
| [eatme PR #89](https://github.com/rysweet/eatme/pull/89) | Merged. Improves instructor and student readiness reports, but does not grade work or prove full lesson completion. |
| [eatme PR #92](https://github.com/rysweet/eatme/pull/92) | Merged at `cfe1f9e364d0015a3f97e237a9de5af670ae3bd6`. Documents the RabbitHole evidence needed before first-lesson readiness can be marked ready. |
| [eatme PR #93](https://github.com/rysweet/eatme/pull/93) | Merged. This repo records only that the PR landed. |

## Known limits

- Historical `.a3p` semantic migration remains thinly covered; selected committed starter `.a3p` archives now have XML fallback readability coverage.
- Real StageIDE-generated projects, thumbnails, gallery resources, and provenance-sensitive assets remain mostly uncovered.
- The player export artifact smoke uses a synthetic project and 1x1 thumbnail; it does not prove the full StageIDE export UI journey.
- The editor save-copy roundtrip also uses a synthetic project and test resource; it does not prove the full StageIDE save UI journey.
- Model binary export, thumbnails, real gallery resources, and full model package output remain mostly untested.
- Backup recovery dialogs and recursive UI side effects are not directly tested.
- Project-load success branching is now tested through `ProjectLoadSuccessPlan`, but the higher-level UI side effects still need characterization.
- Project-load failure dispatch branching is now tested through `ProjectLoadFailureDispatchPlan`, but the higher-level dialog and recursive load UI side effects still need characterization.
- Full wizard execution is not covered.
- Real JavaFX launcher startup is not covered.
- Palette layout behavior has headless coverage, but full palette/completion UI behavior is not covered.
- Deep NBM install semantics are still thin; rename/package smoke coverage exists but not full IDE install execution.
- A standalone exported Ant project build/run against a populated `Alice3Library` is still not fully proven; current coverage validates populated classpath contracts and compile behavior, not a full launched exported project.
- Some scene/model story API and scenegraph behavior is characterized, but events, runtime story execution, and rendering behavior remain mostly unprotected.
- Player export JSON reads are currently resource-only; the program type is still `null` because the Tweedle decoder remains a stub.
- JSON `.a3c` type reads are also resource-only; the type remains `null` until Tweedle type decoding is implemented.
- XML project reads now avoid static resource instance reuse across archive reads while preserving AST resource-expression binding to decoded resources.
- Default-backup copy now has direct seam coverage for populated, missing, and empty `.defaultbak` directories.
- The generated-source export tests were split so both focused NetBeans export test classes are under 500 lines.
- The desktop Run evidence from PR #154 is RabbitHole-only and narrow. It proves
  Alice put the Run panel into the Run window area. It does not prove pixels
  were drawn, does not prove the lesson finished, and is not grading.
- The eatme PR #92 documentation names the RabbitHole evidence required before
  first-lesson readiness can be marked ready, but does not prove full Alice UI
  automation, creative assessment, learner-world grading, visible rendering
  correctness, or first-lesson completion.
- RabbitHole PRs #159 and #160 and eatme PR #93 have merged, but the merge
  state does not prove full Alice UI automation, visible rendering, desktop
  save-menu completion, grading, creative assessment, or first-lesson
  completion.

## Immediate next steps

1. Continue project IO/load-save characterization where it protects data-loss seams:
   - complete player export JSON reads beyond resource restoration;
   - backup/save-as behavior with real temporary files;
   - failure/recovery journey branches above the headless selector/plan seams.
2. Continue generated-source characterization where it protects real exported Java behavior:
   - more scene/model story API calls that compile against exported project dependencies;
   - event/listener and runtime story execution seams that can be tested headlessly.
3. Prove exported project behavior beyond compile/classpath-contract tests:
   - run an actual Ant/NetBeans project build once the required tool/runtime harness is stable;
   - compile/run the exported launcher against real JavaFX where possible.
4. Add higher-level user journey tests where feasible:
    - export project journey;
    - open/load/save journey;
    - failure/recovery journey;
    - package/install smoke path.
5. Keep desktop Run completion claims narrow after the source PRs merged:
   - use PR #155 only as launcher-step and no-go-message evidence, not proof
     that rendering happened;
   - use PR #156 as old image recovery support plus safe rejection of
     unsupported old code;
   - use eatme PR #89 as instructor and student readiness reporting evidence, not
     grading or proof of full lesson completion;
   - use eatme PR #92 as documentation of the RabbitHole evidence needed before
     first-lesson readiness can be marked ready, not as runtime proof;
   - use RabbitHole PRs #159 and #160 and eatme PR #93 only as merged PR
     status unless separate repo evidence proves behavior;
   - add separate proof before claiming pixel drawing, lesson completion, or
     grading.
6. Use the recovered code-atlas bug-hunt artifacts on the next high-value seam:
    - NetBeans export path;
    - project IO/load-save path;
    - resource/model path.
7. Keep journaling every slice in `drinkme`.
8. Do not start broad refactors until the affected behavior has characterization coverage.

## Strategic direction

The safest modernization path remains incremental:

1. characterize behavior;
2. fix correctness bugs exposed by characterization;
3. split oversized or tangled tests/classes where safe;
4. refactor production code behind characterization checks;
5. only consider rewrite or non-Java components after enough evidence exists.

Core Alice should remain Java for now. Rust or other languages may be useful later for optional tooling, static analysis, packaging helpers, graphing, or external AI-assisted tools, but moving core runtime behavior out of Java would be premature without much stronger test coverage.


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
