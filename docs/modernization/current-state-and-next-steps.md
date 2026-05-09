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
- Detailed evidence remains available in the atlas journal, especially
  [0085 desktop Run evidence](../atlas/journal/0085-desktop-run-execution-evidence.md),
  [0086 readiness evidence requirements](../atlas/journal/0086-eatme-pr92-rabbithole-evidence-readiness.md),
  [0100 Save-path and source status](../atlas/journal/0100-rabbithole-pr235-through-pr259-status.md),
  [0128 Tweedle while-loop decode status](../atlas/journal/0128-rabbithole-pr293-while-loop-decode-status.md),
  [0129 merged metadata](../atlas/journal/0129-four-pr-merged-metadata-status.md),
  and [0130 latest evidence boundary status](../atlas/journal/0130-rabbithole-306-308-evidence-status.md).

Automation scenarios now cover a broader set of classroom and desktop paths:
launch/readiness evidence, desktop Run status reporting, Save-path evidence,
project load/save and export boundaries, generated Story API compile/runtime
slices, model export attribution evidence, and instructor/student lesson
scenario inventories. The linked status docs describe the same remaining gaps.

### What works now

- Documentation checks, Markdown link checks, and status-doc contracts run from
  this repository.
- Scenario inventories and readiness reports organize known Alice automation
  paths and the evidence each path still needs.
- Source characterization covers selected project IO, generated Story API, model
  export, NetBeans export, scenegraph, Croquet layout, and Tweedle decode slices.
- Current scenarios provide useful signals for launch, Run, Save-path, lesson,
  classroom, export/share, and accessibility-style paths.

### What is partly working

- Desktop Run and Save-path evidence provide useful signals, but not full Alice
  UI automation.
- Rendering-adjacent checks document surfaces, windows, blockers, and status
  files, but not visible rendering correctness.
- Save-path checks cover selected-path, menu-dispatch, chooser, and file-write
  slices, but not desktop Save menu-to-written-project completion from a real
  rendered click path.
- Automation scenarios describe launch, lesson, classroom, export/share, and
  accessibility-style paths, but they do not grade student work or complete a
  full lesson.
- Tweedle and player decoding cover many small cases, but full decoder support
  remains open.

### What is still missing

The linked status docs use this same exact remaining gap list and workstream
mapping.

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

The no-Sims local and CI path is healthy enough to keep characterization-first
work moving. Current important source-side checks remain:

```bash
mvn -DincludeSims=false -Dinstall4j.skip -pl netbeans -am test
mvn -DincludeSims=false -Dinstall4j.skip clean test
mvn checkstyle:check -Dcheckstyle.config.location=checkstyle.xml
mvn -DincludeSims=false -Dinstall4j.skip -pl netbeans -am package -DskipTests
```

The drinkme documentation contract remains:

```bash
python3 -m unittest discover -s tests -v
```

## Important findings

- Characterization is still early relative to the size of Alice.
- Current coverage is below the 70 percent aggregate coverage target.
- Headless tests cover important exported-code and persistence behavior without
  launching the desktop UI.
- Real JavaFX/UI behavior, story execution, visible rendering, and complete
  classroom assessment remain the highest-risk user-facing gaps.
- Merge state alone is not product behavior evidence; keep claims tied to the
  capability evidence summarized above.

## Immediate next steps

1. RabbitHole: close the launch, rendered UI action, visible rendering, Save/Open,
   and Tweedle/player behavior gaps that block the silver-thread journey.
2. eatme: expand automation scenarios and readiness reporting so instructor and
   student outcomes are readable, including first-lesson completion, grading,
   creative assessment, and deployed sharing/platform behavior.
3. RabbitHole + eatme: complete the desktop Save menu-to-written-project path
   from a real rendered click, then reopen the saved project and report it.
4. RabbitHole + eatme: keep expanding source and scenario coverage toward the
   70 percent aggregate coverage target.

## Strategic direction

The safest modernization path remains incremental:

1. characterize behavior;
2. fix correctness bugs exposed by characterization;
3. split oversized or tangled tests/classes where safe;
4. refactor production code behind characterization checks;
5. only consider rewrite or non-Java components after enough evidence exists.

Core Alice should remain Java for now. Other languages may be useful later for
optional tooling, static analysis, packaging helpers, graphing, or external
AI-assisted tools, but moving core runtime behavior out of Java would be
premature without much stronger test coverage.
