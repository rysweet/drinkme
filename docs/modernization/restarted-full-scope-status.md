# Restarted full-scope Alice modernization status

Last updated: 2026-05-08

## Campaign state

- Loop 64 recovery/integration is **closed**.
- The recovered source and support-tool work that passed review was integrated.
- Artifact-only work tracks were preserved in `drinkme`; they are not Alice runtime/source changes.
- The original full-scope Alice modernization remains **open**. Do not treat Loop 64 recovery closure or the latest status-doc integration as modernization completion.

## Active workstreams

| Workstream | Owner repo | Status |
| --- | --- | --- |
| Alice source modernization | Modernized Alice source tree | Open: continue characterization-first source work behind local checks and CI. |
| Automation scenarios | Scenario comparison repository | Open: continue lesson, classroom, desktop, export/share, and accessibility-style coverage against real Alice evidence. |
| Supporting-tool readiness | Related tooling | Open as needed: fix harness/tool defects only when they block evidence-producing Alice or scenario work. |
| Code-atlas / formal-spec / review inputs | `rysweet/drinkme` | Open read-only inputs: use recovered findings to choose and review high-value seams. |
| Drinkme status and artifact reconciliation | `rysweet/drinkme` | Open: keep linked status docs current as each work round changes state. |

## Current status by capability

| Capability area | Plain status |
| --- | --- |
| Linked status docs | Updated: README, current-state, restarted-status, and atlas now summarize automation-scenario status without using PR chronology as the user-facing view. |
| Automation scenarios | Partly working: scenarios cover more desktop, classroom, lesson, export/share, accessibility, Save-path, and readiness paths, but they are not full Alice UI automation. |
| Source characterization | Partly working: selected project IO, generated Story API, model export, NetBeans export, scenegraph, Croquet layout, and Tweedle decode slices have evidence. |
| Runtime/user behavior | Open: visible rendering, full world execution, first-lesson completion, grading, creative assessment, desktop Save menu-to-written-project completion, and full Tweedle/player decode remain incomplete. |
| Evidence history | Detailed journal entries remain the evidence source; this tracker uses them to summarize current capability status. |

## What changed in the integrated automation-scenario wave

- Documentation/status integration is complete for the linked entry points: README, current-state, restarted-status, and atlas now describe the same current gaps.
- Automation scenarios now cover a wider set of desktop and classroom-style paths, including launch/readiness evidence, desktop Run status reporting, Save-path evidence, project load/save and export boundaries, generated Story API compile/runtime slices, model export attribution evidence, and instructor/student lesson inventories.
- The user-facing status changed from a PR-by-PR merge log to a capability summary: what is covered, what is partial, and what still needs runtime evidence.
- Model export attribution and headless generated Story API runtime-state evidence improved the source characterization map, but they do not change the open status of visible rendering, JavaFX launch, animation playback, full world execution, grading, full UI automation, full lesson completion, or full Tweedle/player decode.

## Latest integrated evidence

- Coverage tooling exists through a reporting-only JaCoCo profile and CI artifact baseline.
- Project IO/load-save has archive fixture, backup, save-to-backup, cancellation, and JSON/XML manifest fallback characterization.
- Desktop automation scenarios cover open/load/save, package/install checks, wizard/palette/completion contracts, readiness reporting, and blocked next actions at the scenario level.
- NetBeans export coverage uses a populated `Alice3Library` classpath contract with JavaFX artifacts and install/package checks.
- Generated Story API Java coverage includes loop, foreach, iterable, local, method, parameter, conditional, story API call compile characterization, and a headless generated runtime-state slice.
- Starter project `.a3p` archives have XML fallback readability coverage using committed fixtures.
- Croquet palette layout and scenegraph model behavior have headless characterization tests; scenegraph `Joint` bounds/scale bugs exposed by tests were fixed.
- Public no-Sims builds guard against nonfree library leakage, and includeSims builds explicitly overwrite the no-Sims `Alice3Library.xml` when authorized.
- Instructor/student scenario assets and readiness reports now cover more classroom and lesson paths, with implementation status separated from completion claims.
- Model export attribution has targeted evidence; it does not change the open status of visible rendering, JavaFX launch, animation playback, full world execution, grading, full UI automation, full lesson completion, or full Tweedle/player decode.

## Remaining gaps

Do not mark the Alice modernization complete while any of these remain true:

1. active workstreams above are still open;
2. characterization coverage is still below the modernization target;
3. real UI/story/export/load-save journeys remain incomplete;
4. local checks or GitHub Actions have not passed for the integrated source state;
5. `drinkme` has not recorded the evidence, limits, and next work.

Open product/runtime gaps remain:

- full Alice UI automation;
- visible rendering correctness;
- desktop Save menu-to-written-project completion from a real rendered click path;
- first-lesson completion;
- grading and creative assessment;
- deployed sharing/platform behavior;
- full Tweedle/player decode;
- the 70 percent aggregate coverage target.

Closure requires direct evidence, not a recovered artifact count, a single successful loop, or completed status documentation.

## Evidence references

- [Current state and next steps](current-state-and-next-steps.md) is the shortest current status narrative.
- [Atlas index](../atlas/index.md) is the overview of diagrams and evidence history.
- [Latest evidence boundary status](../atlas/journal/0130-rabbithole-306-308-evidence-status.md) records the detailed source-evidence boundary for the latest merged evidence.
- [Merged metadata journal](../atlas/journal/0129-four-pr-merged-metadata-status.md) keeps the verified merge metadata out of this tracker.
- [Save-path evidence history](../atlas/journal/0100-rabbithole-pr235-through-pr259-status.md) and [desktop Run execution evidence](../atlas/journal/0085-desktop-run-execution-evidence.md) remain detailed historical sources.
