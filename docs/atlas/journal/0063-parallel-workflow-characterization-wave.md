# 0063 - Parallel workflow characterization wave

## Slice

Ran another workflow-aware parallel implementation wave using isolated branches/worktrees, then integrated the successful branches sequentially behind local gates and CI.

## Source repo

- Repo: `rysweet/alice3-modernization`
- Branch: `develop`
- Integrated commits:
  - `38ca0324b4 Characterize NetBeans Alice library classpath`
  - `eb73ae08c1 Extract project load failure dispatch plan`
  - `3ba86b66ad Add explicit manifest decode errors`
  - `6bc25da7f0 Characterize JSON type archive version handling`
  - `5bd75d8c83 Isolate XML resource identity on read`
  - `4fc78d7c88 Add JsonModelIo export format seam test`
  - `67fd047b72 Characterize URI project loader path classification`
  - `73ca278621 Handle empty default backup copy`

## Parallel structure

The wave used implementation lanes for:

1. XML resource identity.
2. Manifest decoder error semantics.
3. Project-load failure dispatch planning.
4. NetBeans `Alice3Library` classpath/package structure.
5. JSON `.a3c` version behavior.
6. `JsonModelIo` export format seams.
7. URI project-loader path classification.
8. Default-backup copy behavior.

It also used guardrail/scout lanes for crusty proxy review, QA/outside-in testing perspective, code-atlas seam mapping, merge sequencing, CI/package risk, and test-gap review. The original FileProjectLoader seam lane was closed as no-go because existing tests already covered the requested lower-level behavior.

## What changed

### NetBeans library classpath

`Alice3Library.xml` now uses `story-api.jar` without a trailing slash. Tests parse the packaged XML and verify uniqueness and required Alice/OpenJFX classpath entries.

### Recovery failure dispatch

`ProjectLoadFailureDispatchPlan` extracts the post-dialog load/new-project decision from `ProjectApplication`. The Swing dialogs and recursive load side effects remain in the application class.

### Manifest decode errors

`ManifestEncoderDecoder.fromJson()` preserves legacy log-and-null compatibility. New opt-in `fromJsonOrThrow()` lets IO dispatch fail explicitly for corrupt present manifests.

### JSON `.a3c` version behavior

JSON type archive readers now characterize future, missing, and corrupt `version.txt` behavior through the same `ProjectReader` seam used by player archives.

### XML resource identity

XML reads now create fresh `Resource` instances by UUID constructor rather than reusing static `valueOf` maps. AST `ResourceExpression`s are rebound by UUID to the decoded project resources, preserving in-project identity.

### JsonModelIo export formats

Asset-free tests cover export format selection for Collada, glTF, and Alice type archive paths.

### URI project-loader classification

`FileProjectLoaderTest` now covers normal `.a3p` files, named backup directories, `.defaultbak` backup directories, and new-project loader classification.

### Default-backup copy

Default backup copy now no-ops when `.defaultbak` is missing or empty, and copy failures propagate through the existing `saveProjectTo(File) throws IOException` path instead of being logged and hidden.

## Validation

Each lane ran focused local gates before integration. Branches were rebased onto the evolving `develop` stack and merged one at a time.

CI passed for all integrated commits through `67fd047b72`:

- `38ca0324b4`: Alice Checkstyle CI `25288634327`, Alice Test CI `25288634332`, Alice NetBeans Package CI `25288634325`
- `eb73ae08c1`: Alice Checkstyle CI `25288852010`, Alice Test CI `25288852014`, Alice NetBeans Package CI `25288852021`
- `3ba86b66ad`: Alice Checkstyle CI `25288931791`, Alice Test CI `25288931792`, Alice NetBeans Package CI `25288931798`
- `6bc25da7f0`: Alice Checkstyle CI `25289014724`, Alice Test CI `25289014720`, Alice NetBeans Package CI `25289014730`
- `5bd75d8c83`: Alice Checkstyle CI `25289107936`, Alice Test CI `25289107845`, Alice NetBeans Package CI `25289107871`
- `4fc78d7c88`: Alice Checkstyle CI `25289195814`, Alice Test CI `25289195822`, Alice NetBeans Package CI `25289195823`
- `67fd047b72`: Alice Checkstyle CI `25289274571`, Alice Test CI `25289274574`, Alice NetBeans Package CI `25289274578`
- `73ca278621`: Alice Checkstyle CI `25289363439`, Alice Test CI `25289363445`, Alice NetBeans Package CI `25289363430`

## Submodule note

Several worktrees needed `git submodule update --init tweedle-lang` before broad Maven validation. Missing `tweedle-lang/Grammar` causes `core/tweedle` generated parser failures that look like Java compile regressions but are really checkout setup failures.

## Crusty proxy note

The lesson remains: parallelize discovery and implementation, not final integration. The branches were independent enough to build concurrently, but shared tests and IO semantics required serialized rebase, focused validation, root checkstyle, and CI gates.

## QA/outside-in note

The useful outside-in surfaces for this wave were public file/load/save seams:

- manifest-declared archive readers;
- `IoUtilities.writeProject/readProject/checkForFutureVersion`;
- `ProjectApplication` pure planning seams;
- `ProjectFileUtilities` save/copy behavior;
- `UriProjectLoader` path classification;
- NetBeans packaged library XML.

Full desktop UI automation remains deferred until a stable Xvfb/Swing/JavaFX harness exists.

## Next seams

- Add a real exported Ant/NetBeans build harness using populated `Alice3Library`.
- Continue project save/load user journey characterization above the pure planning seams.
- Add XML resource entry-name sanitization/dedup parity with JSON exports.
- Decode Tweedle type/program data only after resource-only JSON boundaries remain stable.
