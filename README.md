# drinkme

drinkme is the front door for the Alice 3 modernization work. It keeps the
plan, current status, project map, diagrams, and next-step links in one place so
readers can understand the work without reading pull request history.

This README is a project overview, not a changelog. Detailed status and evidence
live in the linked docs.

## Plan summary

The silver-thread journey is: launch Alice -> build or change a starter
world/program -> run and observe it -> save and reopen it -> report
instructor/student readiness.

The modernization loop is simple: protect current Alice behavior with focused
checks, use the evidence to refactor the source in small steps, compare
automation scenario outcomes and gaps, and keep drinkme as the status and
evidence index.

## How the work runs

Source work improves Alice capability, scenario work compares Alice outcomes,
and drinkme tracks plan, status, and evidence.

### Source behavior-test-before-refactor loop
```mermaid
flowchart LR
  Check["Behavior check"] --> Evidence["Capture evidence"] --> Refactor["Refactor one source slice"] --> Repeat["Run the check again"]
  Repeat -->|new evidence| Check
```

### Automation scenario comparison loop
```mermaid
flowchart LR
  Scenarios["Define automation scenarios"] --> Compare["Compare Alice outcomes"] --> Gaps["Record remaining gaps"] --> Next["Choose next scenario"]
  Next -->|next gap| Scenarios
```

### drinkme plan/status/evidence tracking loop
```mermaid
flowchart LR
  Plan["Summarize plan"] --> Status["Show current status"] --> Evidence["Link evidence"] --> Decisions["Guide decisions"]
  Decisions -->|updated plan| Plan
```

## Current verdict

The modernization is active and useful, but unfinished. Over 200 pull requests
are merged. Forty-seven refactoring PRs have decomposed large production classes.
Only 41 production Java files remain over 500 lines (down from 100+). Eight
silver-thread end-to-end tests cover the full student journey. All 37 automation
scenarios validate. All 8 Alice.org curriculum lessons have grading coverage.
A TypeScript prototype runs the silver thread journey against a web API.
The repository has automation scenario coverage, readiness reports, and diagrams.

Use drinkme as a map and status index. Do not read it as a claim that Alice
modernization, classroom assessment, UI automation, rendering, or coverage goals
are complete.

## One-page project map

```mermaid
flowchart TD
  Reader["Reader"] --> README["drinkme README"]
  README --> Plan["Plan and priorities"]
  README --> Status["Current status"]
  README --> Atlas["Atlas and diagrams"]
  README --> Links["Repositories and tools"]

  Plan --> Source["Modernized Alice source tree"]
  Plan --> Scenarios["Automation scenarios"]
  Status --> Works["What works now"]
  Status --> Partial["What is partly working"]
  Status --> Missing["What is still missing"]
  Atlas --> RepoMap["Repository surface"]
  Atlas --> Startup["Startup flow"]
  Atlas --> Testing["Testing roadmap"]
  Scenarios --> Reports["Readiness reports"]
```

| Area | Purpose | Start here |
| --- | --- | --- |
| Plan | Shows the modernization path and priority order. | [Investigation plan](docs/plan.md) |
| Current status | Summarizes what is complete, partial, and still open. | [Current state and next steps](docs/modernization/current-state-and-next-steps.md) |
| Full-scope status | Keeps the broader modernization boundary explicit. | [Restarted full-scope status](docs/modernization/restarted-full-scope-status.md) |
| Atlas | Maps repository structure, startup flow, and test roadmap. | [Atlas index](docs/atlas/index.md) |
| Scenarios | Tracks planned user and classroom-style checks. | [Scenario implementation plan](docs/eatme/implementation-plan.md) |

## What works now

- Over 200 pull requests merged across source and scenario repositories.
- 47 refactoring PRs decomposing large classes. 41 files remain over 500 lines.
- Eight silver-thread end-to-end tests, all 37 automation scenarios validate.
- All 8 Alice.org curriculum lessons have automation grading coverage (650 tests).
- TypeScript prototype runs the silver thread journey against web API (39 tests).
- The drinkme documentation contract is reproducible with `python3 -m unittest discover -s tests -v`.

## What is partly working

- NonCachingTextRenderer reduced from 1842 to 476 lines.
- Save-path work has component-level evidence, but full desktop Save completion is missing.
- Rendering work has surface and blocker records, but not visible correctness.
- Tweedle and player decoding covers many cases, but full decode is still missing.
- Agentic test composability work is in progress.

## What is still missing

Still missing: full Alice UI automation, visible rendering correctness, full desktop Save
completion, full Tweedle/player decode, and the 70 percent coverage target; see
the [investigation plan](docs/plan.md) for the authoritative remaining gap list.

## Current focus

Close the largest evidence gaps: real UI actions, visible rendering, desktop Save completion, decoder coverage, and the TypeScript/.a3p prototype.

## Progress at a glance

```mermaid
flowchart LR
  Works["Works now<br/>200+ PRs, 40 refactors, 37 scenarios"] --> Partial["Partly working<br/>Save path, rendering, decoder, lesson grading"]
  Partial --> Missing["Still missing examples<br/>full UI, visible rendering, grading, first lesson, 70 percent coverage"]
```

| Area | Status | Reader takeaway |
| --- | --- | --- |
| Documentation checks | Works now | Run the unittest command above for the drinkme docs contract. |
| Project map and diagrams | Works now | Start with the atlas and diagram links below. |
| Automation scenarios | Works now | All 37 scenarios validate. |
| Desktop Save | Partly working | Component-level evidence exists, but full desktop Save completion is missing. |
| Lesson grading | Works now | All 8 curriculum lessons graded; TS prototype tested. |
| Rendering | Missing | Do not treat current evidence as visible correctness. |
| Tweedle/player decode | Partly working | Many slices are characterized; full decode is missing. |
| Coverage target | Missing | 70 percent aggregate coverage is still a target, not a result. |

## Useful links

### Repositories and tools

- [Original Alice 3 project](https://github.com/TheAliceProject/alice3)
- [Modernized Alice source tree](https://github.com/rysweet/RabbitHole)
- [Automation scenario repository](https://github.com/rysweet/eatme)
- [drinkme repository](https://github.com/rysweet/drinkme)
- [TypeScript .a3p prototype](https://github.com/rysweet/alice-web-prototype)
- [Agentic test framework](https://github.com/rysweet/gadugi-agentic-test)

### Plans, status, and diagrams

- [Investigation plan](docs/plan.md)
- [Current state and next steps](docs/modernization/current-state-and-next-steps.md)
- [Restarted full-scope status](docs/modernization/restarted-full-scope-status.md)
- [Scenario implementation plan](docs/eatme/implementation-plan.md)
- [Atlas index](docs/atlas/index.md)
- [Repository surface diagram](docs/atlas/diagrams/repo-surface-mermaid.svg) and
  [source](docs/atlas/diagrams/repo-surface.mmd)
- [Startup flow diagram](docs/atlas/diagrams/startup-flow-mermaid.svg) and
  [source](docs/atlas/diagrams/startup-flow.mmd)
- [Testing roadmap diagram](docs/atlas/diagrams/testing-roadmap-mermaid.svg) and
  [source](docs/atlas/diagrams/testing-roadmap.mmd)

## Where to go next

For the shortest status read, open
[current state and next steps](docs/modernization/current-state-and-next-steps.md).
For the overall work order, read the [investigation plan](docs/plan.md). For
structure and diagrams, use the [atlas index](docs/atlas/index.md). For the
automation scenario side, read the
[scenario implementation plan](docs/eatme/implementation-plan.md).
