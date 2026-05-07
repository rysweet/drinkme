# Alice 3 code atlas

This is the first-pass atlas for the Alice 3 investigation. It is intentionally stored in `drinkme`, not in the Alice source fork.

## Current diagrams

### Repository surface

![Repo surface Mermaid](diagrams/repo-surface-mermaid.svg)

![Repo surface Graphviz](diagrams/repo-surface-dot.svg)

### Startup flow

![Startup flow Mermaid](diagrams/startup-flow-mermaid.svg)

![Startup flow Graphviz](diagrams/startup-flow-dot.svg)

### Testing roadmap

![Testing roadmap Mermaid](diagrams/testing-roadmap-mermaid.svg)

![Testing roadmap Graphviz](diagrams/testing-roadmap-dot.svg)

## Atlas layers started

| Layer | Status | Notes |
| --- | --- | --- |
| repo-surface | started | Maven reactor and major module groups mapped. |
| ast-lsp-bindings | not started | Needs Java LSP or static symbol pass. |
| compile-deps | started | Initial module dependency map only; needs full POM extraction. |
| runtime-topology | not applicable/service-light | Desktop app, not a service topology; still needs runtime component map. |
| api-contracts | not applicable/http-light | No HTTP API found in first pass; plugin and Java APIs need contract docs. |
| data-flow | started | Startup flow mapped; project/model persistence flows still needed. |
| service-components | started | Major Java modules mapped; package-level diagrams still needed. |
| user-journeys | started | Testing roadmap identifies journey candidates; executable journeys still needed. |

## Next atlas expansion

1. Generate POM dependency graph directly from Maven metadata.
2. Add package-level diagrams for `core/ide`, `core/tweedle`, `core/model-loading`, `core/resources`, `core/glrender`, and `netbeans`.
3. Trace project load/save and model import/export data flows.
4. Trace Alice-to-Java NetBeans workflow.
5. Add static symbol and entry-point inventory.
6. Add staleness triggers keyed to Maven modules and source/resource folders.

## Recent journal entries

- [0096 - RabbitHole PR #209/#210/#211 source wave status](journal/0096-rabbithole-pr209-pr210-pr211-source-wave-status.md)
  records literal sized Tweedle array initializer support, launcher/runtime proof,
  story-api keyboard event characterization tests, reported `core/story-api`
  coverage movement from 4.55% to 6.21% with 260 more covered lines, and the
  decode, rendering, installer, full-world, manual QA, smoke-check, and 70 percent
  coverage limits that remain.
- [0095 - RabbitHole PR #207/#208 source evidence update](journal/0095-rabbithole-pr207-pr208-source-evidence.md)
  records Numeric and Boolean Tweedle `null` field initializer decoding to AST
  `NullLiteral`, Save operation completion evidence, the all-passing PR #208
  checks, and the limits that remain for UI automation, rendering, full desktop
  Save menu completion, grading, first-lesson completion, procedure UI invocation,
  and full Tweedle/player decode support.
- [0094 - RabbitHole source and CI status wave](journal/0094-rabbithole-source-ci-wave-status.md)
  records RabbitHole PR #185, #187, #188, #190, and #191: model resource array
  tests, narrow `TextString` null support, `ProcedureTabSelection`,
  `IssueReportWorker` non-retryable failure tests, and the Maven cache fallback
  fix that cleared stuck coverage behavior, while keeping coverage, oversized
  files, live procedure invocation, rendering, grading, first-lesson completion,
  and full Tweedle decode support unproven.
- [0093 - Source, eatme, and CI status wave](journal/0093-source-eatme-ci-wave-status.md)
  records RabbitHole PRs #173 through #184, eatme PRs #105/#106/#108 through
  #116, the eatme local audit counts, and RabbitHole CI timing notes, while
  keeping UI automation, visible rendering correctness, save-menu completion,
  grading, first-lesson completion, deployed sharing, and full Tweedle decode
  support unproven.
- [0092 - RabbitHole PR #170/#171/#172 and eatme PR #101/#102 merge status](journal/0092-rabbithole-pr170-pr171-pr172-eatme-pr101-pr102-merge-status.md)
  records the Run-panel pixel-observation fallback, resource-initializer archive
  rejection, next-action no-go file, explicit next-action output, and
  media/audio student scenario, while keeping rendering, grading, and
  first-lesson completion unproven.
- [0091 - RabbitHole PR #168/#169 and eatme PR #99 merge status](journal/0091-rabbithole-pr168-pr169-eatme-pr99-merge-status.md)
  records the unresolved-parent archive rejection test, pixel-observation blocker
  details, and eatme pixel-observation reporting, while keeping rendering,
  grading, and first-lesson completion unproven.
- [0090 - RabbitHole PR #166/#167 and eatme PR #98 merge status](journal/0090-rabbithole-pr166-pr167-eatme-pr98-merge-status.md)
  records the complex-initializer archive rejection test, the desktop pixel
  observation evidence file, and plain first-lesson readiness output, while
  keeping rendering, grading, and first-lesson completion unproven.
- [0089 - RabbitHole PR #164 and eatme PR #96 merge status](journal/0089-rabbithole-pr164-eatme-pr96-merge-status.md)
  records the constructor-bearing sibling archive test and the first-lesson
  evidence progress summary, while keeping pixels, rendering, grading, and
  first-lesson completion unproven.
- [0088 - RabbitHole PR #163 and eatme PR #95 merge status](journal/0088-rabbithole-pr163-eatme-pr95-merge-status.md)
  records the clear unsupported-Tweedle-type rejection and the eatme
  pixel-boundary status reporting update, while keeping pixels, rendering,
  grading, and first-lesson completion unproven.
- [0087 - RabbitHole PR #159/#160 and eatme PR #93 merge status](journal/0087-rabbithole-pr159-pr160-eatme-pr93-merge-status.md)
  records the missing Tweedle source-entry test, the pixel-proof boundary file,
  and the readiness evidence list, while keeping product behavior unproven until
  separate evidence exists.
- [0086 - eatme PR #92 RabbitHole evidence readiness](journal/0086-eatme-pr92-rabbithole-evidence-readiness.md)
  records the eatme PR #92 documentation update and its limits.
- [0085 - Desktop Run execution evidence](journal/0085-desktop-run-execution-evidence.md)
  records the RabbitHole PR #154 Run window attachment signal and its limits.
- [0084 - Run-window toolbar proof](journal/0084-run-window-toolbar-proof.md)
- [0083 - Run shortcut focus delivery](journal/0083-run-shortcut-focus-delivery.md)
- [0082 - License-preseeded Run-window check](journal/0082-license-preseeded-run-window-check.md)
- [0081 - License modal Run-window blocker](journal/0081-license-modal-run-window-blocker.md)
- [0080 - Run-window observation](journal/0080-run-window-observation.md)
- [0079 - Desktop Run shortcut dispatch](journal/0079-desktop-run-shortcut-dispatch.md)
- [0078 - Desktop save shortcut dispatch](journal/0078-desktop-save-shortcut-dispatch.md)
- [0077 - Project-save proof hook](journal/0077-project-save-proof-hook.md)
- [0076 - Run-world proof hook](journal/0076-run-world-proof-hook.md)
- [0075 - Run-world contract boundary](journal/0075-run-world-contract-boundary.md)
- [0074 - Edit proof readiness run](journal/0074-edit-proof-readiness-run.md)
- [0073 - Edit proof consumption](journal/0073-edit-proof-consumption.md)
- [0072 - Edit action contract boundary](journal/0072-edit-action-contract-boundary.md)
- [0071 - Window fallback first-lesson readiness](journal/0071-window-fallback-first-lesson-readiness.md)
- [0070 - Object-placement progress evidence](journal/0070-object-placement-progress-evidence.md)
- [0069 - Object-placement hook implementation](journal/0069-object-placement-hook-implementation.md)
- [0068 - Archive guards and object-placement hook contract](journal/0068-archive-guards-and-object-placement-hook.md)
- [0067 - Xvfb launcher and object-placement contract](journal/0067-xvfb-launcher-and-affordance-contract.md)
- [0066 - JavaFX, archive, and first-lesson action boundaries](journal/0066-javafx-archive-ui-action-boundaries.md)
- [0065 - RabbitHole comparison harness wave](journal/0065-rabbithole-compare-harness-wave.md)
