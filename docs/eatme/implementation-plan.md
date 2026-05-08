# Eatme implementation plan

The canonical implementation plan is maintained in the private `eatme` repo at:

```text
/home/azureuser/src/eatme/docs/implementation-plan.md
```

This `drinkme` copy records the current planning direction and links the plan to the Alice modernization documentation corpus.

## Current direction

Second-pass review tightened the plan:

- Milestone 0 is a deterministic real-Alice launch smoke only.
- No personas, gadugi dependency, lesson evaluation, or parallel GUI runs in Milestone 0.
- `eatme` owns desktop execution: Alice packaging, Xvfb, display allocation, window/process lifecycle, screenshots, logs, and manifests.
- Gadugi initially treats `eatme` as a CLI/system harness and asserts against `manifest.json`.
- Pass/fail initially comes from deterministic evidence, not agentic judgment.
- Alice.org curriculum scenarios begin after the launch smoke.
- [eatme PR #89](https://github.com/rysweet/eatme/pull/89)
  merged. It improves instructor and student readiness reports, but does not grade
  work or prove full lesson completion.
- [eatme PR #92](https://github.com/rysweet/eatme/pull/92)
  merged at `cfe1f9e364d0015a3f97e237a9de5af670ae3bd6`. It documents the
  RabbitHole evidence needed before first-lesson readiness can be marked ready:
  launch evidence, Run-window evidence, desktop execution evidence,
  screenshot/log/window artifacts, and `ui-action-contract.json`.
- [eatme PR #93](https://github.com/rysweet/eatme/pull/93) merged at
  `f5c08aea14c679124afc680fc9bc9e155da237dd`. It makes first-lesson readiness
  reports list concrete RabbitHole readiness evidence categories; it does not
  create new runtime proof or prove grading, creative assessment, or
  first-lesson completion.
- eatme depends on the merged RabbitHole source PRs:
  [RabbitHole PR #154](https://github.com/rysweet/RabbitHole/pull/154)
  merged. It records that Alice put the Run panel into the Run window area.
  [RabbitHole PR #155](https://github.com/rysweet/RabbitHole/pull/155)
  merged. It records launcher steps and no-go messages, but does not prove
  rendering.
  [RabbitHole PR #156](https://github.com/rysweet/RabbitHole/pull/156)
  merged. It keeps old image recovery while safely rejecting unsupported old
  code.
  [RabbitHole PR #159](https://github.com/rysweet/RabbitHole/pull/159) merged
  at `9dbf0266ad7d61439f5dd74121e744dbbd365462`. It adds a generated archive
  test where a missing Tweedle source entry fails clearly; it does not add broad
  Tweedle decode support.
   [RabbitHole PR #160](https://github.com/rysweet/RabbitHole/pull/160) merged
   at `18c533efdacc7bdefa971c82ac655d5127bc743e`. It adds
   `desktop-run-pixel-boundary.json` with `status: "not_observed"`; it does not
   prove pixels, screenshots, visible rendering, or grading.
  [RabbitHole PR #163](https://github.com/rysweet/RabbitHole/pull/163) merged
  at `4f225f2795c79f84c367874cd7995dc6dcded22f`. It rejects unsupported
  manifest-declared Tweedle type names with a clear error instead of silently
  dropping a type; it does not add full Tweedle decode support.
  [RabbitHole PR #164](https://github.com/rysweet/RabbitHole/pull/164) merged
  at `fb3e419b81c55b0e055711c9b57d3143f4f69f10`. It adds the matching generated
  archive test for a constructor-bearing sibling Tweedle type; it does not add
  full Tweedle decode support.
  [RabbitHole PR #166](https://github.com/rysweet/RabbitHole/pull/166) merged
  at `bb617171524fa11d59b71b77a0d29d1b645e2507`. It adds a generated archive
  test for a sibling Tweedle type with an unsupported complex field initializer;
  it does not add full Tweedle decode support.
  [RabbitHole PR #167](https://github.com/rysweet/RabbitHole/pull/167) merged
  at `4c5e2f21b2674f07176df40f90ded35e5738bde3`. It adds
  `desktop-run-pixel-observation.json` so a run records a screenshot and center
  pixel when possible, or a blocker code and component state when not; it does
  not prove visible rendering or first-lesson completion.
  [RabbitHole PR #168](https://github.com/rysweet/RabbitHole/pull/168) merged
  at `da0fb851fd974721a630811873f0d583a853eb5e`. It adds a generated archive
  test for a sibling Tweedle type with an unresolved parent; it does not add full
  Tweedle decode support.
  [RabbitHole PR #169](https://github.com/rysweet/RabbitHole/pull/169) merged
  at `0a0d182c139aeaf5bc7c2c45213a0392cf8f245c`. It adds machine-readable
  blocker details to `desktop-run-pixel-observation.json`; it does not prove
  visible rendering or first-lesson completion.
  [RabbitHole PR #170](https://github.com/rysweet/RabbitHole/pull/170) merged
  at `7e58f46b5b1d9624dd54bf1d2367243349ce8a28`. It improves pixel observation
  fallback to the attached Run panel for pixel sampling; it does not prove
  visible rendering correctness.
  [RabbitHole PR #171](https://github.com/rysweet/RabbitHole/pull/171) merged
  at `34a48d0b24ebf933925ad6237afaa4ca7518fd99`. It rejects resource-typed
  Tweedle field initializers instead of accepting them as strings; it does not
  add full Tweedle decode support.
  [RabbitHole PR #172](https://github.com/rysweet/RabbitHole/pull/172) merged
  at `e0c199ab88d10f635d4f3e9e5d67553fb1fd3f4f`. It adds
  `desktop-first-lesson-next-action.json`, naming missing deterministic
  Save-menu and code/procedure action targets; it does not complete those
  actions.
  [RabbitHole PR #209](https://github.com/rysweet/RabbitHole/pull/209) merged
  at `02e50a00078e8ff348aa33b8c8635483f9b817bf`. It supports literal sized
  Tweedle array field initializers such as `new WholeNumber[2]`; non-literal
  sizes still fail clearly, and broader array expressions, method and constructor
  bodies, non-literal initializers, non-null resource initializers, complete
  player decode, and full Tweedle decode remain unproven.
  [RabbitHole PR #210](https://github.com/rysweet/RabbitHole/pull/210) merged
  at `d2cba4ba3e349c704765129511de5a062210ec08`. It adds launcher/runtime proof
  beyond the earlier `Program.main` null-Stage guard; visible rendering, deployed
  installer success, and full world execution remain unproven.
  [RabbitHole PR #211](https://github.com/rysweet/RabbitHole/pull/211) merged
  at `9b509aa3e60e6cf60b5e870a3ee03a0a80363f89`. It adds story-api keyboard event
  characterization tests; `core/story-api` coverage was reported from 4.55% to
  6.21%, adding 260 covered lines. The 70 percent aggregate coverage target,
  manual QA gaps, and smoke checks that still need manual approval remain
  unproven.
  [RabbitHole PR #212](https://github.com/rysweet/RabbitHole/pull/212) merged at
  `db72e0cfef8912cd0a92243f1889ae4cd2180535` from head `a84346582aef22c51d3afa33a05df26b62e370c7`. It adds Save
  dialog/control target evidence. The focused Save tests, focused review, and
  GitHub build, coverage, test, package-netbeans, and GitGuardian checks
  passed. Live desktop Save menu invocation and actual Save dialog
  discovery/control remain unproven.
  [RabbitHole PR #214](https://github.com/rysweet/RabbitHole/pull/214) merged at
  `2155904f38e55323b00d732b7f64e957db4406f5`. It proves launcher drawing
  surface readiness through `Stage.show()` and `isShowing()` and adds a
  `render-target-unavailable` no-go path; visible pixels, deployed installer
  success, and full world execution remain unproven.
  [RabbitHole PR #215](https://github.com/rysweet/RabbitHole/pull/215) merged at
  `c727d97c3d71a0f045925a691a080a42d36fbe9d`. It decodes empty `void` Tweedle
  methods to AST `UserMethod`; parameters, method bodies, non-void methods, and
  constructors still fail clearly.
  [RabbitHole PR #216](https://github.com/rysweet/RabbitHole/pull/216) merged at
  `c84bdf826723284e84b4872ce2e6c791dee0c8a6`. It adds Save dialog discovery
  target evidence; live Save menu click, actual dialog display/control, selected
  path automation, full lesson completion, rendering, and grading remain
  unproven.
  [RabbitHole PR #218](https://github.com/rysweet/RabbitHole/pull/218) merged at
  `a568bae3c3960c60792351cfa423450fea51b067`. It adds launcher render
  observation proof, but visible pixels remain unobserved. Deployed installer
  success and full world execution remain unproven.
  [RabbitHole PR #219](https://github.com/rysweet/RabbitHole/pull/219) merged at
  `144081e1067cd8795666e5ee8802f47fbfefe671`. Empty no-argument Tweedle
  constructors decode to AST `NamedUserConstructor`; constructor parameters and
  constructor bodies still failed clearly at that point.
  [RabbitHole PR #222](https://github.com/rysweet/RabbitHole/pull/222) merged at
  `f749ed7cc92f7df4678e96bbb29bcbd0b09913b8`. It proves
  `SaveProjectOperation.fire(UserActivity)` reaches
  `AbstractSaveOperation.perform`, but the non-desktop proof lacks
  `StageIDE.getActiveInstance()`.
  [RabbitHole PR #224](https://github.com/rysweet/RabbitHole/pull/224) merged at
  `1a3eae6937a7109f3608112a7fb40519e1a4f8d7`. A real pixel attempt proved
  JavaFX cannot open `DISPLAY` locally; visible rendering correctness remains
  unproven.
  [RabbitHole PR #225](https://github.com/rysweet/RabbitHole/pull/225) merged at
  `db44c10bd017a5b7cc8eddc1cc82b1d1b90c8fb8`. Required Tweedle constructor
  parameters decode to AST `UserParameter`; optional constructor parameters still
  fail clearly.
  [RabbitHole PR #229](https://github.com/rysweet/RabbitHole/pull/229) merged at
  `7953c8348272298e9cb85f2319fba6520ba51a32`. Required parameters for empty
  `void` Tweedle methods decode to AST `UserParameter`; optional method
  parameters still fail clearly.
  [RabbitHole PR #230](https://github.com/rysweet/RabbitHole/pull/230) merged at
  `31d506f6af59ef736ccefad9aa7b793b3add6a3d`. Under Xvfb, Save action
  invocation is proven with `status=action_invoked`, `StageIDE=true`, and
  `ProjectDocumentFrame=true`; menu click, dialog display/control, selected path
  automation remain unproven, and completed save remains unproven.
  [RabbitHole PR #231](https://github.com/rysweet/RabbitHole/pull/231) merged at
  `622748401fe8ff00d81d3a2851faac153585b76c`. Generated launcher Xvfb marker
  pixels were observed; real Alice desktop pixels were not observed because
  `mvn exec:java -Dalice-ide` fails with `org.alice.stageide.EntryPoint`
  `ClassNotFoundException`.
  [RabbitHole PR #234](https://github.com/rysweet/RabbitHole/pull/234) merged at
  `45d937fbe1e9ddee74e7c2b89af31841fb38a202`. Single primitive-literal Tweedle
  `return` method bodies decode to AST `ReturnStatement`; full method decode,
  full player decode, and full Tweedle decode support remain unproven.
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
  `ae3d8de57aec10d2f9c3b7e1a5c6d8f4e2b1c9a3` and adds `x-window-inventory.json`
  to the Xvfb Alice launch proof; blocked at `alice-window-not-found` after the
  classpath fix.
  [RabbitHole PR #241](https://github.com/rysweet/RabbitHole/pull/241) merged at
  `d2ab990dffa8c7e5b9a3d1f6c4e2b8d7a5c0f1e9` and adds an opt-in selected-path
  automation seam at `FileDialogUtilities.showSaveFileDialog`, rejecting outside
  paths and symlink escapes; Save dialog display and control remain unproven.
  [RabbitHole PR #245](https://github.com/rysweet/RabbitHole/pull/245) merged at
  `9cc5893d8b67e4d1b8a3c7f2e5d6c9b4a1e8f3d2` and adds `application-root-error.json`
  probe mapping the `Application Root Error` window to the
  `org.alice.ide.rootDirectory` condition.
  [RabbitHole PR #246](https://github.com/rysweet/RabbitHole/pull/246) merged at
  `2fe47f4ebaea9d7c3b5a1e8f4d6c2b9a7e5d3c8f` and proves
  `ProjectDocumentFrame.showSaveFileDialog` reaches `FileDialogUtilities` with a
  displayable `JFrame` root under Xvfb; Save dialog display and control remain
  unproven.
  [RabbitHole PR #247](https://github.com/rysweet/RabbitHole/pull/247) merged at
  `0a75eb7a21f5d3c9b7e2a4d6f1c8b5e9d2a7c3f6` and decodes narrow Tweedle
  constructor bodies with primitive-literal local variable declarations to AST
  `LocalDeclaration`; full Tweedle constructor, method, player, and resource
  decode remain unproven.
  [RabbitHole PR #250](https://github.com/rysweet/RabbitHole/pull/250) merged at
  `c640c3fbd9ef5a7d1c8b2e4f6a9d3c7b5e1a8f2d` and adds a `rootDirectory` prep
  helper verifying `alice-ide` configures `org.alice.ide.rootDirectory` and
  prepares `core/resources/target/distribution` before Xvfb launch.
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
  `11c8c58a33b2c6c7ec93e1b4a057c375e0dbb70f`. It shows first-lesson readiness
  progress and every required evidence item in plain text output. It does not
  add new runtime proof.
- [eatme PR #99](https://github.com/rysweet/eatme/pull/99) merged at
  `5e8ba4b8c970d04b410060e90c22a613430e202b`. It reports
  `desktop-run-pixel-observation.json` beside readiness progress, including
  observed screenshot/sample data or blocked component state and blocker codes.
  It does not add new runtime proof.
- [eatme PR #101](https://github.com/rysweet/eatme/pull/101) merged at
  `546dfc7c2cdbc5ca6c4526fe3e90bb9f717999ed`. It shows explicit next-action
  evidence in first-lesson plain output; it does not add new runtime proof.
- [eatme PR #102](https://github.com/rysweet/eatme/pull/102) merged at
  `3e183407e247944831a6f7ff44870c71169302f4`. It adds the
  `media-audio-cue-storyboard` student scenario for `media-audio-creator` and
  generated adapter; it does not grade student work or prove lesson completion.
- [eatme PR #118](https://github.com/rysweet/eatme/pull/118) merged at
  `2c760511eeff8c554b17ee550e779e7c51444591` from head `b70048d78f0b5f8669dc7e725cdac6b1ff3566f5`. It improves
  Alice window action diagnostics. CI passed, and the manual real Alice smoke
  check was skipped. A real desktop environment still needs proving, and
  later procedure edit, run, and save automation remains incomplete.
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
- [eatme PR #124](https://github.com/rysweet/eatme/pull/124) merged at
  `d3bb687145b6c9e38601703c691aa7f6bcbb4862`. Adds the
  `alien-linguist-parameter-dialogue` instructor/student scenario; scenario
  assets grew from 73 to 75 with all adapters fresh. Grading, automated
  creative assessment, real Alice UI automation, and full lesson delivery remain
  unproven.
- [RabbitHole PR #264](https://github.com/rysweet/RabbitHole/pull/264) merged at
  `a4386130d66b97feecdbcb5ab1b6bc765392deb3`. Primitive literal field assignments
  in Tweedle constructor bodies now decode, with clear failures for unsupported
  constructor assignment forms; full Tweedle/player decode remains unproven.
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
  grew from 77 to 79 with all adapters fresh. This does not prove grading,
  automated creative assessment, real Alice UI automation, or full lesson
  delivery.
- [eatme PR #127](https://github.com/rysweet/eatme/pull/127) merged at
  `e0c090f265f0dfb2f0b662616aac8b6cb078dae6`. Adds the
  `mars-rover-proximity-mission` instructor/student scenario; scenario assets
  grew from 79 to 81 with all 40 generated gadugi adapters fresh. This does not
  prove grading, automated creative assessment, real Alice UI automation, or full
  lesson delivery.
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
  grew from 81 to 83 with all Gadugi adapters fresh. This does not prove grading,
  automated creative assessment, real Alice UI automation, or full lesson delivery.
- [RabbitHole PR #272](https://github.com/rysweet/RabbitHole/pull/272) merged at
  `458bed0f4b409d207a2610b8ccfa8e8dfbbce6c9`. Proves AT-SPI reaches the Alice
  Java process via `exec:exec` and `NO_AT_BRIDGE=1`; top-level Swing widgets are
  observable. Tab labels are not visible or enumerable. Project selection and
  opening are not proven.
- [RabbitHole PR #273](https://github.com/rysweet/RabbitHole/pull/273) merged at
  `c86e8c4747b73921e8c432709c8cf7a741848855`. Proves `SaveProjectOperation.fire()`
  reaches a live `JFileChooser`, a background probe approves it, and a non-empty
  `.a3p` is written. Visible rendering, grading, desktop save-menu completion, and
  a full Save menu item `doClick`-to-written-file journey remain unproven.
- [eatme PR #131](https://github.com/rysweet/eatme/pull/131) merged at
  `973b65f`. Adds the `neighborhood-data-story` instructor/student scenario;
  scenario assets grew from 83 to 85 with all Gadugi adapters fresh. This does
  not prove grading, automated creative assessment, real Alice UI automation, or
  full lesson delivery.
- [RabbitHole PR #274](https://github.com/rysweet/RabbitHole/pull/274) merged at
  `5571894e5152482c9fb26ba31fc3d633d372e88e`. Arithmetic binary expressions
  (`+`, `-`, `*`, `/`) now decode as Tweedle assignment right-hand-side values
  and as local variable initializer values. String concatenation, logical and
  comparison expressions, method calls, non-`this` member assignment targets,
  loops, conditionals, resource field initializers, and full Tweedle/player decode
  remain unproven.
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
  `17e82091232131de7f1b2169638a2ea1a48fedfd`. Adds `FileMenuSaveNavigationProofTest`:
  starts `StageIDE`, finds `FileMenuModel` in the real `AliceMenuBar`, calls
  `fileMenuModel.createMenu()` to build the actual `JMenu`, locates the `JMenuItem`
  backed by the same `Action` instance as `SaveProjectOperation`, calls `doClick()`,
  and checks that evidence shows `status=menu_item_dispatched`,
  `menu_item_dispatch=true`, and `trigger_class=ActionEventTrigger`. All five CI
  checks passed; focused review returned CLEAN. The user physically clicking the
  on-screen File menu, desktop save-menu completion from a real rendered click path,
  full live FileDialog interaction with a confirmed file write, visible rendering
  correctness, grading, and first-lesson completion remain unproven.
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
- RabbitHole PRs #159, #160, #163, #164, #166, #167, #168, #169, #170, #172, #185, #187, #188, #190, #191, #207, #208, #209, #210, #211, #212, #214, #215, #216, #218, #219, #222, #224, #225, #229, #230, #231, #234, #235, #237, #238, #240, #241, #245, #246, #247, #250, #253, #254, #255, #259, #260, #261, #262, #264, #265, #266, #267, #269, #270, #271, #272, #273, #274, #276, #277, #278, #281, #282, #284, #285, #287, #289, #290, #291, #292, and #293
  and eatme PRs #93, #95, #96, #98, #99, #101, #102, #118, #120, #121, #122, #123, #124, #125, #126, #127, #129, #131, #132, #133, #134, #135, and #136 have merged, but they do
  not prove full Alice UI automation, visible rendering, desktop save-menu
  completion, native FileDialog peer control, project selection or opening,
  grading, creative assessment, learner-world grading, first-lesson
  completion, real desktop proof, project save, deployed installer success, full
  world execution, procedure UI invocation, or complete player/full Tweedle decode support.
- The proof boundary remains a narrow Run window attachment signal: Alice put
  the Run panel into the Run window area. This evidence does not prove pixels
  were drawn, does not prove the lesson finished, and is not grading.
- The PR #92 evidence list does not prove full Alice UI automation, creative
  assessment, learner-world grading, visible rendering correctness, or
  first-lesson completion. It describes what RabbitHole evidence must exist and
  be documented before readiness can be marked ready.


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
  `IssueReportWorker` non-retryable failure tests, with 52 Java files over 500 lines reported by the latest hotspot count. [RabbitHole PR #191](https://github.com/rysweet/RabbitHole/pull/191) restored the Maven
  cache fallback, fixed the stuck coverage path, and left coverage run
  `25492250204` plus develop checks after PR #190 successful. PR #187, PR #188,
  and PR #190 were delayed by stuck coverage behavior and transient `jogamp.org`
  network failures.
- Latest RabbitHole source evidence is tracked in
  `docs/atlas/journal/0095-rabbithole-pr207-pr208-source-evidence.md`.
  [RabbitHole PR #207](https://github.com/rysweet/RabbitHole/pull/207) merged Numeric and Boolean Tweedle `null` field initializer
  decoding to AST `NullLiteral` while still rejecting primitive statement
  contexts such as `if(null)` and `while(null)`. [RabbitHole PR #208](https://github.com/rysweet/RabbitHole/pull/208) records Save
  operation completion evidence; its head before merge was
  `153f4e4ce77415d42e6f1047abcc2074671ae4c8`, all GitHub checks passed, and it
  merged at `8799854787655ca61b6fad9378377b19d41aa7b1`. The 70 percent aggregate
  coverage target, live procedure invocation, desktop edit command, desktop
  save-menu completion, dialogs, grading, rendering, first-lesson completion,
  deployed sharing, and full Tweedle/player decode support remain unproven.

### Latest eatme local audit

| Area checked | Done for now | What remains outside eatme local docs/harness work |
| --- | ---: | --- |
| Canonical scenario inventory | 34 of 34 | Runtime proof still depends on RabbitHole evidence. |
| Gadugi scenario inventory | 35 of 35 | One is a hand-authored validation regression; broader lesson proof remains separate. |
| Persona inventory | 24 of 24 | Persona coverage is documentation coverage, not grading. |
| Student/instructor persona links | 33 of 33 scenarios | These links do not prove learner-world behavior. |
| Docs navigation | 18 of 18 pages | Published sharing and full classroom workflow proof remain unproven. |

Plainly: eatme local instructor/student persona coverage, student docs, Gadugi
adapters, and plain readiness output are complete for now. The remaining blockers
depend on RabbitHole first-lesson evidence and broader behavior proof.

## Milestone 0

Milestone 0 proves:

1. Host dependencies are detected.
2. RabbitHole packages from `/home/azureuser/src/RabbitHole`.
3. Long-lived Xvfb starts with GLX enabled.
4. Alice launches via direct Java and `org.alice.stageide.EntryPoint`.
5. The run uses isolated user home, prefs root, and temp/cache directories.
6. The harness captures process status, logs, window/display data, screenshot, command log, and `manifest.json`.
7. The deterministic assertions pass.

## Required manifest contract

The manifest must include:

- scenario id and run id
- Alice repo path and commit
- eatme commit
- Java/Maven versions
- dependency checks
- build command and exit status
- launch command
- `DISPLAY`
- Xvfb PID and Alice PID
- timeout values
- screenshot path, size, and hash
- log path, size, and hash
- fatal log scan
- assertion results
- failure category

## Post-launch scenario path

After Milestone 0:

1. `building-a-scene-first-world`
2. `code-editor-first-run`
3. `control-structures-visible-change`
4. `introduction-to-events-first-binding`
5. `design-process-thin-slice`

Export/player, collision/proximity games, and broader creative scenarios come later.

## Desktop Run proof path

The next desktop Run work should preserve the current strict boundary:

1. Treat merged RabbitHole PR #154 as limited to the Run window attachment
   signal.
2. Treat merged RabbitHole PR #155 as recorded launcher steps and no-go
   messages, not proof that rendering happened.
3. Treat merged RabbitHole PR #156 as old image recovery support plus safe
   rejection of unsupported old code.
4. Treat merged eatme PR #89 as improved instructor and student readiness reports,
   not grading and not proof of full lesson completion.
5. Treat merged eatme PR #92 as the documentation of required RabbitHole
   evidence categories, not proof that those categories have passed in drinkme.
6. Treat merged eatme PR #93 as a report-output improvement that lists required
   readiness evidence, not grading, creative assessment, or first-lesson
   completion.
7. Treat merged RabbitHole PR #159 as one clear archive failure test, not broad
   Tweedle decode support.
8. Treat merged RabbitHole PR #160 as a pixel-proof boundary record, not proof
   of pixels, screenshots, visible rendering, or desktop save-menu completion.
9. Treat merged RabbitHole PR #163 as a clear rejection for unsupported
   manifest-declared Tweedle type names, not full Tweedle decode support.
10. Treat merged RabbitHole PR #164 as constructor-bearing sibling archive
    coverage for the same clear-failure behavior, not full Tweedle decode support.
11. Treat merged eatme PR #95 as explicit pixel-boundary status reporting, not
    proof of pixels, visible rendering, grading, or first-lesson completion.
12. Treat merged eatme PR #96 as a countable progress summary, not new runtime
    proof.
13. Treat merged RabbitHole PR #166 as complex-initializer sibling archive
    coverage for the same clear-failure behavior, not full Tweedle decode support.
14. Treat merged RabbitHole PR #167 as a pixel observation file that records an
    observation when possible and a clear blocker when not, not visible rendering
    proof.
15. Treat merged eatme PR #98 as plain readiness output, not new runtime proof.
16. Treat merged RabbitHole PR #168 as unresolved-parent sibling archive coverage
    for the same clear-failure behavior, not full Tweedle decode support.
17. Treat merged RabbitHole PR #169 as blocker details for the pixel observation
    file, not visible rendering proof.
18. Treat merged eatme PR #99 as pixel observation reporting, not new runtime
    proof.
19. Treat merged RabbitHole PR #170 as improved pixel observation fallback, not
    visible rendering proof.
20. Treat merged RabbitHole PR #172 as a next-action no-go file, not desktop
    Save-menu or code/procedure automation completion.
21. Treat merged eatme PR #101 as next-action reporting, not runtime proof.
22. Treat merged eatme PR #102 as one student scenario increment, not grading or
    lesson completion.
23. Treat merged RabbitHole PR #207 as Numeric and Boolean `null` field
    initializer support only, not full Tweedle/player decode support.
24. Treat merged RabbitHole PR #208 as Save operation completion evidence only,
    not proof that the full desktop Save-menu path is complete.
25. Add separate proof before eatme claims pixels were drawn, the lesson
    finished, or grading happened.

## Governance boundaries

- Supporting tool repos such as `amplihack-rs`, `gadugi-agentic-test`, `amplihack-recipe-runner`, and `amplihack-memory-lib` are in scope for bug fixes or feature work when needed.
- Any supporting-tool repo change must follow the default workflow, and subagents doing that work must follow the default workflow too.
- No silent repo mutation.

## Review artifacts

- `docs/eatme/reviews/0001-crusty-old-engineer.md`
- `docs/eatme/reviews/0002-rust-memory-architecture.md`
- `docs/eatme/reviews/0003-gadugi-capability-audit.md`
- `docs/eatme/reviews/0004-real-alice-harness-design.md`
- `docs/eatme/reviews/0005-second-pass-harness-review.md`
- `docs/eatme/reviews/0006-second-pass-crusty-review.md`
- `docs/eatme/reviews/0007-second-pass-curriculum-review.md`
- `docs/eatme/reviews/0008-second-pass-gadugi-review.md`
- `docs/eatme/research/0001-alice-org-resource-map.raw.md`


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
