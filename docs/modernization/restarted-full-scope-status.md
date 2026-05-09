# Restarted full-scope Alice modernization status

Last updated: 2026-05-09

## Campaign state

The broad Alice modernization remains open. The current silver-thread journey
is: launch Alice -> build or change a starter world/program -> run and observe
it -> save and reopen it -> report instructor/student readiness.

Loop 64 recovery/integration is closed, and recovered source or support-tool
work that passed review was integrated. Artifact-only work tracks were
preserved in `drinkme`; they are not Alice runtime/source changes. Do not treat
recovery closure, status-doc integration, or scenario inventory completion as
modernization completion.

## Active workstreams

| Workstream | Owner repo | Status |
| --- | --- | --- |
| Alice source modernization | RabbitHole | Open: continue characterization-first source work behind local checks and CI. |
| Automation scenarios and readiness | eatme | Open: continue lesson, classroom, desktop, export/share, grading, creative-assessment, and platform-facing coverage. |
| Code atlas and evidence index | drinkme | Open read-only inputs: keep diagrams, journals, and status pages linked. |
| Drinkme status and artifact reconciliation | drinkme | Open: keep linked status docs current as each work round changes state. |

## Current status by capability

| Capability area | Plain status |
| --- | --- |
| Linked status docs | Updated: README, plan, current-state, restarted-status, eatme plan, and atlas now summarize the silver-thread journey without using pull request chronology as the user-facing view. |
| Automation scenarios | Partly working: scenarios cover more desktop, classroom, lesson, export/share, accessibility, Save-path, and readiness paths, but they are not full Alice UI automation. |
| Source characterization | Partly working: selected project IO, generated Story API, model export, NetBeans export, scenegraph, Croquet layout, and Tweedle decode slices have evidence. |
| Runtime/user behavior | Open: visible rendering, full world execution, first-lesson completion, grading, creative assessment, desktop Save menu-to-written-project completion, deployed sharing/platform behavior, and full Tweedle/player decode remain incomplete. |
| Coverage target | Open: the 70 percent aggregate coverage target remains a target, not a result. |

## What changed after automation scenarios were integrated

- Documentation/status integration is complete for the linked entry points:
  README, plan, current-state, restarted-status, eatme plan, and atlas now
  describe the same product journey and remaining gaps.
- Automation scenarios now cover a wider set of desktop and classroom-style
  paths, including launch/readiness evidence, desktop Run status reporting,
  Save-path evidence, project load/save and export boundaries, generated Story
  API compile/runtime slices, model export attribution evidence, and
  instructor/student lesson inventories.
- The user-facing status changed from a merge log to a capability summary: what
  works now, what is partial, and what still needs runtime or readiness evidence.
- Model export attribution and generated story-code runtime-state evidence
  improved the source characterization map, but they do not close visible
  rendering, animation playback, full world execution, grading, full UI
  automation, full lesson completion, or full Tweedle/player decode.

## Latest integrated evidence

- Coverage tooling exists through a reporting-only JaCoCo profile and CI artifact
  baseline.
- Project IO/load-save has archive fixture, backup, save-to-backup,
  cancellation, and JSON/XML manifest fallback characterization.
- Desktop automation scenarios cover open/load/save, package/install checks,
  wizard/palette/completion contracts, readiness reporting, and blocked next
  actions at the scenario level.
- NetBeans export coverage uses a populated `Alice3Library` classpath contract
  with JavaFX artifacts and install/package checks.
- Generated story-code Java coverage includes loop, foreach, iterable, local,
  method, parameter, conditional, story API call compile characterization, and a
  generated runtime-state slice collected without opening the desktop UI.
- Starter project `.a3p` archives have XML fallback readability coverage using
  committed fixtures.
- Croquet palette layout and scenegraph model behavior have headless
  characterization tests.
- Instructor/student scenario assets and readiness reports now cover more
  classroom and lesson paths, with implementation status separated from
  completion claims.

## Remaining gaps

This is the same exact remaining gap list and workstream mapping used by the
plan and current-state docs.

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

Closure requires direct product and readiness evidence, not a recovered artifact
count, a single successful loop, or completed status documentation.

## Evidence references

- [Current state and next steps](current-state-and-next-steps.md) is the shortest current status narrative.
- [Atlas index](../atlas/index.md) is the overview of diagrams and evidence history.
- [Latest evidence boundary status](../atlas/journal/0130-rabbithole-306-308-evidence-status.md) records the detailed source-evidence boundary for the latest merged evidence.
- [Merged metadata journal](../atlas/journal/0129-four-pr-merged-metadata-status.md) keeps verified merge metadata out of this tracker.
- [Save-path evidence history](../atlas/journal/0100-rabbithole-pr235-through-pr259-status.md) and [desktop Run execution evidence](../atlas/journal/0085-desktop-run-execution-evidence.md) remain detailed historical sources.
