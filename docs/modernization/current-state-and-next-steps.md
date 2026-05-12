# Alice modernization current state and next steps

## Repository state

The current silver-thread journey is: launch Alice -> build or change a starter
world/program -> run and observe it -> save and reopen it -> report
instructor/student readiness.

- Source capability work happens in `rysweet/RabbitHole`.
- Scenario coverage and readiness reporting happen in `rysweet/eatme`.
- Investigation artifacts, status, diagrams, and evidence links are journaled in
  `drinkme`.
- Latest status is summarized by capability below, not as pull request
  chronology.
- The linked status docs describe the same exact remaining gap list and workstream
  mapping.

### What works now

- **74 PRs merged**: RabbitHole 46, eatme 24, amplihack-rs 4.
- **ProjectMigrationManager decomposed**: 5702→117 lines. Migration data lives
  in 5 TextMigrationRegistry files. All 188 tests pass.
- **TweedleEncoder decomposed**: 959→499 lines with 4 delegates:
  StatementEncoder (46), ResourceEncoder (240), TweedleEncoderData (213),
  FormattingEncoder (122).
- **8 silver-thread e2e tests** on develop covering: launch/build/run, Save
  round-trip, edit/Save/readback, Tweedle decoder round-trip, VM execution,
  student program save/reopen, codegen, and event dispatch.
- **85 boundary tests** for decoder delegates and IoUtilities.
- **87 VM execution characterization tests**.
- **Run-window detection** proves Alice Run window is observable under Xvfb.
- **EatmeEditProcedure** accepts any `scene.*` selector (not just hardcoded
  `eatmeFirstLessonStep`), so starter projects like `africa.a3p` work.
- **Mac compatibility**: platform-tolerant render assertions, headless save
  guards, disabled screen menu bar for Robot tests.
- **CI optimized**: non-Java PRs finish in under 30 seconds.
- **44/46 eatme scenarios pass** (7/7) against both the fork and upstream Alice.
- **5 eatme-side integration bugs found and fixed**: selector, optional field,
  schema version, status value, validation logic.
- **4 lesson e2e tests** with per-step grading: Building a Scene, Code Editor
  First Run, Loops and Conditionals, Events and Collision.
- **Creative assessment**, **sharing/platform**, and **grading** reports added.
- Documentation checks, Markdown link checks, and status-doc contracts run from
  this repository.

### What is partly working

- **2 eatme scenarios** score 18/23 instead of 7/7. The 5 remaining assertion
  failures are in the edit→run→save chain.
- **NonCachingTextRenderer extraction** started: 1842→1318 lines with 3 inner
  classes extracted, but 3 test compilation failures remain.
- Desktop Run and Save-path evidence provide useful signals, but not full Alice
  UI automation.
- Tweedle and player decoding cover many small cases, but full decoder support
  remains open.
- Automation scenarios describe launch, lesson, classroom, export/share, and
  accessibility-style paths, but they do not grade student work or complete a
  full lesson.

### What is still missing

The remaining gaps are listed below with workstream ownership.

| Remaining coverage gap | Next workstream |
| --- | --- |
| Full Alice UI automation | RabbitHole |
| Visible rendering correctness | RabbitHole |
| Desktop Save menu-to-written-project completion from a real rendered click path | RabbitHole + eatme |
| First-lesson completion | eatme |
| Grading | eatme |
| Creative assessment | eatme |
| Deployed sharing/platform behavior | eatme |
| Full Tweedle/player decode | RabbitHole |
| 70 percent aggregate coverage target | RabbitHole + eatme |

## Build and CI state

The no-Sims local and CI path is healthy. Current important source-side checks:

```bash
mvn -DincludeSims=false -Dinstall4j.skip -pl netbeans -am test
mvn -DincludeSims=false -Dinstall4j.skip clean test
mvn checkstyle:check -Dcheckstyle.config.location=checkstyle.xml
mvn -DincludeSims=false -Dinstall4j.skip -pl netbeans -am package -DskipTests
```

The drinkme documentation contract:

```bash
python3 -m unittest discover -s tests -v
```

## Important findings

- 5 integration bugs between eatme and Alice were all on the eatme side, not
  Alice bugs. This validates that the upstream project behavior is correct.
- The eatme scenarios are portable: verified working against both
  rysweet/RabbitHole and upstream TheAliceProject/alice3 with same results.
- TweedleEncoder extraction proved that decomposing large classes is safe when
  backed by comprehensive characterization tests first.
- Alice's Run window renders in-place (no separate window), which means
  screenshot comparison is needed instead of new-window polling.
- Current coverage is below the 70% aggregate coverage target (~10.35%).

## Immediate next steps

1. Fix NCT extraction test failures and continue reducing from 1318 lines.
2. Fix 2 remaining eatme scenario failures in edit→run→save chain.
3. Characterize and reduce ModelResourceExporter (1358 lines).
4. Characterize and reduce StorytellingSceneEditor (1259 lines).
5. Continue Tweedle/player decoder slices with negative tests.
6. Expand real-Alice UI journey coverage.
7. Keep drinkme current after each meaningful wave.

## Strategic direction

The safest modernization path remains incremental:

1. characterize behavior;
2. fix correctness bugs exposed by characterization;
3. split oversized or tangled tests/classes where safe;
4. refactor production code behind characterization checks;
5. only consider rewrite or non-Java components after enough evidence exists.

Core Alice should remain Java for now.
