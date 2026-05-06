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
