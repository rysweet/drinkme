# Alice modernization current state and next steps

## Repository state

The current silver-thread journey is: launch Alice -> build or change a starter
world/program -> run and observe it -> save and reopen it -> report
instructor/student readiness.

- Source capability work happens in `rysweet/RabbitHole`.
- Scenario coverage and readiness reporting happen in `rysweet/eatme`.
- Investigation artifacts, status, diagrams, and evidence links are journaled in
  `drinkme`.
- TypeScript prototype lives in `rysweet/alice-web-prototype`.
- Latest status is summarized by capability below, not as pull request
  chronology.
- The linked status docs describe the same exact remaining gap list and workstream
  mapping.
- Automation scenarios cover the full lesson path from launch through save.
- The remaining gaps are listed below with workstream ownership.

### What works now

- **90+ PRs merged**: RabbitHole 68+, eatme 28+, drinkme 12, amplihack-rs 4.
- **12 large files refactored under 500 lines**:
  - PMM: 5702→117, TweedleEncoder: 959→499, NCT: 1842→476
  - MRE: 1358→486, SSE: 1259→493, VM(ast): 1193→480
  - IK Enforcer: 1328→372, ASG: 1241→114
  - EatmeDesktopRunEvidence: 1103→415, SaveOperationEvidence: 1009→429
  - Graphics2D: 1225→493, DragAdapter: 1039→682
- **7 remaining large files under active default-workflow refactoring**:
  - JointedModelColladaExporter: 1181 (Step 8 - Implementation)
  - AbstractComposite: 1113 (Step 5 - Design)
  - AbstractTransformableImp: 977 (Step 2c)
  - JointedModelImp: 955 (Step 5b)
  - VirtualMachine: 938 (Step 2b)
  - AliceResourceUtilities: 916 (Step 2b)
  - JsonProjectIo: 798 (Step 2c)
- **46 eatme scenarios** covering all 21 alice.org curriculum lessons.
- **47 orchestration adapters** generated and validated.
- **Real Alice desktop test**: 6/6 assertions pass (fork + upstream).
- **TypeScript prototype** (alice-web-prototype):
  - .a3p parser, Three.js scene builder, Express API, evidence writer
  - CLI hooks matching Java Alice tools/ interface (place/edit/run/save)
  - 31 tests pass
  - All 4 lesson steps produce correct evidence artifacts
- **618-line web migration feasibility analysis** in drinkme.
- **CI optimized**: non-Java PRs finish in under 30 seconds.

### What is partly working

- Desktop Run and Save-path evidence provide useful signals, but not full Alice
  UI automation.
- Tweedle decoder covers arithmetic, logic, loops, constructors, optional params
  but missing method calls, full constructor bodies, resource initializers.
- TS prototype produces eatme-compatible evidence but has not been run through
  the full eatme validation pipeline end-to-end yet.

### What is still missing

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
- Each default-workflow refactoring takes 1-2 hours through the 22-step pipeline.
- Current coverage is below the 70% aggregate coverage target (~10.35%).
- @SuppressWarnings has RetentionPolicy.SOURCE — invisible to runtime reflection.
- Parallel worktrees consume ~1.5GB each; disk must be monitored.

## Strategic direction

The safest modernization path remains incremental:

1. characterize behavior;
2. fix correctness bugs exposed by characterization;
3. split oversized or tangled tests/classes where safe;
4. refactor production code behind characterization checks;
5. TypeScript prototype validates the same eatme scenarios as Java Alice;
6. web migration feasibility analysis guides long-term architecture.

Core Alice remains Java. The TypeScript prototype is a parallel validation
target, not a replacement.
