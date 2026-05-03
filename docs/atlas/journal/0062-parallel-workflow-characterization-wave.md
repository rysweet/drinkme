# 0062 - Parallel workflow characterization wave

## Slice

Ran a workflow-aware parallel implementation wave using isolated branches/worktrees, then integrated the branches sequentially behind local gates and CI.

## Source repo

- Repo: `rysweet/alice3-modernization`
- Branch: `develop`
- Integrated commits:
  - `4f1509f1a3 Isolate JSON player resource reads by UUID`
  - `85589b3888 Surface corrupt manifest IO errors`
  - `89e771d339 Characterize model resource player archive read`
  - `da7b191089 Characterize JSON type archive resource reads`
  - `4218bc9aaa Characterize NetBeans template compiler structure`
  - `e2f08d89b4 Extract project load success plan`

## Parallel structure

The wave used six implementation lanes:

1. JSON/player resource identity isolation.
2. IO corrupt-manifest and missing-version behavior.
3. JSON/player model and generated type manifest references.
4. JSON `.a3c` type archive resource-only reads.
5. NetBeans template compiler surrogate structure.
6. Project-load success decision planning.

It also used read-only guardrail lanes for crusty proxy review, QA/outside-in scenario design, code-atlas seam mapping, CI/package risk, class-size/coverage scanning, merge sequencing, UI harness feasibility, and lane-specific scouts.

## What changed

### JSON/player resource identity

JSON player reads now construct fresh `ImageResource` and `AudioResource` instances from manifest UUIDs instead of reusing mutable static UUID-map instances. This preserves UUID identity while preventing a later archive read from mutating an earlier read's resource data.

### IO error behavior

Corrupt `manifest.json` in reader dispatch now fails explicitly with `IOException`. Missing manifests can still behave as legacy XML archives, but present-and-corrupt manifests no longer silently fall back to the XML reader.

### Model/generated type boundaries

JSON/player archives with `ModelReference` and generated `TypeReference` manifest entries are characterized. Current behavior is intentionally resource-only: those manifest entries remain archive metadata and are not returned as binary `Resource`s while Tweedle/model decoding is unimplemented.

### JSON `.a3c` type archives

JSON type archives now write `metadata.fileType = "a3c"` and route through `JsonProjectIo` when read by `IoUtilities.readType(...)`. Manifest-listed resources are restored, while the Tweedle type remains `null`.

### NetBeans template compiler surrogate

The standalone generated-project compiler surrogate now verifies template build/classpath properties and resolves its output classes directory from the template instead of hardcoding `build/classes`.

### Project-load success planning

`ProjectLoadSuccessPlan` extracts a pure decision seam from `ProjectApplication` for successful project-load branching. The Swing/UI side effects remain in `ProjectApplication`.

## Validation

Each lane ran focused local gates before integration. Branches were then rebased onto the evolving `develop` stack and merged one at a time.

CI passed for the first five integrated commits:

- `4f1509f1a3`: Alice Test CI `25287596182`, Alice Checkstyle CI `25287596205`, Alice NetBeans Package CI `25287596210`
- `85589b3888`: Alice Test CI `25287714577`, Alice Checkstyle CI `25287714585`, Alice NetBeans Package CI `25287714574`
- `89e771d339`: Alice Test CI `25287806516`, Alice Checkstyle CI `25287806503`, Alice NetBeans Package CI `25287806508`
- `da7b191089`: Alice Test CI `25287897588`, Alice Checkstyle CI `25287897593`, Alice NetBeans Package CI `25287897591`
- `4218bc9aaa`: Alice Test CI `25288030879`, Alice Checkstyle CI `25288030881`, Alice NetBeans Package CI `25288030877`

CI passed for the final integrated commit:

- Alice Test CI: `25288119314`
- Alice Checkstyle CI: `25288119322`
- Alice NetBeans Package CI: `25288119319`

## Crusty proxy note

The important lesson is that "parallel" does not mean "independent." Resource identity, reader dispatch, type reads, and recovery all touch the same file-format semantics. The safe pattern was parallel branch work followed by serialized rebasing, local validation, and CI-gated integration.

## QA/outside-in note

The useful outside-in surface remains headless public APIs:

- `IoUtilities.writeProject/readProject/readType/exportProject`
- `ProjectFileUtilities.saveCopyOfProjectTo/exportCopyOfProjectTo`
- NetBeans generated-source compiler surrogates
- pure recovery planning seams

Full desktop UI automation should remain deferred until an Xvfb/Swing/JavaFX harness exists.

## Next seams

- Decode Tweedle type/program data only after the resource-only JSON boundaries remain stable.
- Characterize XML project read identity before changing any static UUID-map semantics outside JSON IO.
- Extract the next recovery seam around error-dialog/load command dispatch.
- Replace NetBeans classpath surrogates with a real `Alice3Library`/Ant build harness when feasible.
