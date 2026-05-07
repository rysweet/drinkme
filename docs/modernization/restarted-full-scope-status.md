# Restarted full-scope Alice modernization status

Last updated: 2026-05-06

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
| [eatme PR #89](https://github.com/rysweet/eatme/pull/89) | Merged. Improves instructor and student readiness reports, but does not grade work or prove full lesson completion. |
| [eatme PR #92](https://github.com/rysweet/eatme/pull/92) | Merged at `cfe1f9e364d0015a3f97e237a9de5af670ae3bd6`. Documents the RabbitHole evidence needed before first-lesson readiness can be marked ready. |
| [eatme PR #93](https://github.com/rysweet/eatme/pull/93) | Merged at `f5c08aea14c679124afc680fc9bc9e155da237dd`. Lists the concrete readiness evidence categories in the report; it does not create new runtime proof. |

The proof boundary remains a narrow Run window attachment signal: Alice put the
Run panel into the Run window area. This evidence does not prove pixels were
drawn, does not prove the lesson finished, and is not grading.

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

## No-premature-completion rule

Do not mark the Alice modernization complete while any of these remain true:

1. active workstreams above are still open;
2. characterization coverage is still below the modernization target;
3. real UI/story/export/load-save journeys remain unproven;
4. local checks or GitHub Actions have not passed for the integrated source state;
5. `drinkme` has not recorded the evidence, limits, and next work.

Closure requires evidence, not a recovered artifact count or a single successful loop.
