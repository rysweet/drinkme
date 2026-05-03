# Operating model for the Alice modernization loop

## Blunt assessment

The recent work was too serial. That was safe for code mutation, but it left useful lanes idle.

The right model is not "parallel everything." That is how shared repositories get trashed. The right model is one serialized mutation lane plus parallel non-mutating lanes that feed it.

## Standing lanes

| Lane | Parallel? | Mutates source? | Purpose |
| --- | --- | --- | --- |
| Implementation | No | Yes | Make one coherent source change at a time in `rysweet/alice3-modernization`. |
| Local/CI validation | Partly | No | Run package/test/style gates; do not overlap conflicting source mutations. |
| Crusty proxy review | Yes | No | Skeptical review of scope, risks, sequencing, and "are we fooling ourselves?" questions. |
| QA outside-in design | Yes | No | Define user-observable scenarios before or alongside implementation. |
| Code-atlas bug hunt | Yes | No, unless explicitly converting a finding into a source fix | Map seams and identify contradictions; journal findings in `drinkme`, not issues. |
| Documentation/journal | Yes after source facts are known | Artifacts only | Keep `drinkme` current. |

## Crusty-old-engineer usage

`crusty-old-engineer` is a standing proxy for this effort, not an occasional style pass.

Use it at these points:

1. Before choosing the next modernization slice.
2. After a characterization test exposes surprising behavior.
3. Before refactoring production code.
4. Before claiming a slice is "done."
5. When deciding between incremental refactor, rewrite, or language/tool boundary changes.

Expected output:

- what assumption is probably wrong;
- what failure mode is likely;
- what evidence would make the next step defensible;
- whether the current change is actual progress or just motion.

## QA-team outside-in usage

`qa-team` is the standing outside-in testing lane.

For Alice, not every QA scenario maps cleanly to Playwright because Alice is a Java desktop application, not a web app. Use the right user-observable harness:

| User-facing path | Outside-in strategy |
| --- | --- |
| Maven build/test/package | CLI scenario around commands, exit codes, and artifacts. |
| NetBeans export/package | CLI/package scenario plus artifact checks. |
| Exported Java project | Generate/export project, compile it, then run launcher or inspect observable output. |
| Desktop UI startup | Headless smoke first; later Xvfb/Jemmy/FEST/AssertJ-Swing-style UI automation if practical. |
| Website/reference behavior | Playwright is appropriate for web reference/documentation checks, not Swing internals. |
| Future rewrite parity | A/B scenarios comparing current Alice behavior to candidate implementation. |

Immediate QA backlog:

1. Exported project outside-in smoke: synthetic Alice project -> generated Java project -> compile -> launcher handoff/run evidence.
2. NetBeans package outside-in smoke: package command -> expected NBM/support artifacts -> representative archive contents.
3. Project IO outside-in smoke: create synthetic project -> save -> reload -> observable project metadata/resource survival.
4. Failure path outside-in smoke: corrupt project input -> user-observable failure handling path without crashing.
5. Future UI smoke: launch application in controlled display environment and verify a stable first-window or startup signal.

## Parallelism rules

Do in parallel:

- code-atlas seam analysis;
- QA scenario drafting;
- crusty review;
- doc/reference audits;
- independent read-only investigations;
- CI monitoring while preparing artifact docs.

Do not do in parallel:

- two source edits in the same files;
- refactor plus behavior change;
- artifact docs that claim CI success before CI finishes;
- source push while another mutation lane is unvalidated;
- anything that opens upstream issues or PRs.

## Current correction

The process should now treat parallel review/design lanes as mandatory for substantial slices:

1. Choose next slice.
2. In parallel, run crusty risk review, QA outside-in scenario design, and code-atlas/seam review where useful.
3. Implement the smallest protected change.
4. Run local gates.
5. Push and verify CI.
6. Journal evidence and limitations.
7. Repeat.

This is slower than pretending. It is faster than debugging fantasy.

