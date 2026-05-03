# 0064 - Parallel workflow lane plan

## Purpose

Loop 64 continues Alice characterization after Loop 63, but it touches two fragile areas:

1. project persistence/recovery;
2. NetBeans export/runtime.

This loop uses parallel implementation worktrees for discovery and branch creation, but integration must be serialized, fast-forward only, and CI-gated after each meaningful merge.

## Source and artifact repositories

- Source implementation: `rysweet/alice3-modernization`, branch `develop`
- Private artifacts: `rysweet/drinkme`, branch `main`
- Running status issue: `rysweet/drinkme#1`

No upstream issues, upstream pull requests, or upstream pushes are allowed.

## Workflow requirements

Every coding lane must:

1. follow `DEFAULT_WORKFLOW`;
2. work in an isolated worktree/branch under `/home/azureuser/src/alice3-modernization-worktrees`;
3. initialize `tweedle-lang` before broad Maven validation;
4. run focused tests and root checkstyle where feasible;
5. push only the lane branch to `rysweet/alice3-modernization`;
6. return branch, commit, files changed, validation evidence, risks, and no-go notes.

The main integration lane must:

1. rebase each branch onto current `origin/develop`;
2. inspect the diff;
3. rerun focused local validation;
4. fast-forward merge only;
5. push `develop`;
6. wait for Alice Checkstyle CI, Alice Test CI, and Alice NetBeans Package CI to go green before the next risky merge.

## Implementation lanes

| Lane | Branch | Purpose | Expected touched areas |
| --- | --- | --- | --- |
| Submodule setup check | `loop64-submodule-check` | Make missing `tweedle-lang` diagnostics clearer without heavy automation. | `README.md`, `AGENTS.md`, `core/tweedle/pom.xml` if justified |
| Save failure surfacing | `loop64-save-failure-surface` | Characterize save/copy failure propagation and filesystem state after failure. | `core/ide`, `ProjectFileUtilities*` |
| Backup directory collision | `loop64-backup-dir-collision` | Characterize named backup path collisions and partial default-backup move risk. | `core/ide`, `ProjectFileUtilities*` |
| Project load planning seam | `loop64-project-load-plan` | Extract the next pure planning seam only if it avoids UI construction and preserves behavior. | `ProjectApplication`, pure plan classes/tests |
| JSON type manifest errors | `loop64-type-manifest-errors` | Characterize `.a3c` missing/corrupt manifest behavior after explicit decoder changes. | `IoUtilitiesTest`, manifest/IO dispatch |
| JSON missing resource entry | `loop64-json-missing-resource` | Characterize behavior when manifest-listed image/audio entries are missing from the archive. | `JsonProjectIo`, `IoUtilitiesTest` |
| JSON unknown resource reference | `loop64-json-unknown-resource` | Characterize unsupported JSON manifest references as metadata, not binary resources. | `IoUtilitiesTest` |
| XML resource entry safety | `loop64-xml-entry-safety` | Characterize duplicate/path/blank XML resource entry names and fix only if unsafe. | `XmlProjectIo`, `IoUtilitiesTest` |
| NetBeans library artifact existence | `loop64-netbeans-library-exists` | Verify `Alice3Library.xml` entries against packaged/resolvable artifacts where feasible. | `netbeans` tests/resources |
| Launcher runtime edge | `loop64-launcher-runtime` | Add a narrow headless generated-launcher runtime handoff edge using test stubs. | NetBeans codegen tests |
| Generated story API call | `loop64-generated-story-call` | Add one focused generated Java source compile smoke for a real story API call. | NetBeans generated-source tests |
| NetBeans Ant build smoke | `loop64-netbeans-ant-smoke` | Attempt real exported Ant build smoke; no-go if CI/tooling makes it brittle. | NetBeans template/export tests |

## Guardrails completed so far

| Guardrail | Key finding |
| --- | --- |
| QA outside-in | Highest user value: NetBeans Ant smoke, save failure, project-load planning, backup collision, JSON missing/unknown behavior, XML entry safety, generated story call, launcher runtime. |
| UI harness | Keep headless seam tests in normal CI. First real desktop smoke should be opt-in Xvfb + Swing/AWT Robot; TestFX is not the first fit. |
| Coverage/class-size | No JaCoCo/Cobertura artifacts, so `>70%` cannot yet be proven. Risks: `ProjectApplication` 760 lines, `JsonModelIo` 534, `IDE` 539, `IoUtilitiesTest` 633. |
| Code atlas | Risks: XML resource entry naming, XML writer mutating project resources, JSON reads are resource-only, backup creation/thumbnail/autosave edges, NetBeans import/library fragility. |
| Merge sequencing | Use serialized FF-only integration. No-go weak evidence or missing focused tests/root checkstyle/CI. |
| IO risk | Priorities: atomic save/data loss, default-backup migration loss, missing resource entries, corrupt XML manifest fallback, duplicate UUID/name in one archive, duplicate zip entries. |
| CI risk | Use `-DincludeSims=false -Dinstall4j.skip`; watch LFS, missing `tweedle-lang`, and no Ant in CI. |
| NetBeans scout | P0 real exported Ant build/run, P1 library resolution parity including JavaFX classifier jars, P2 generated API breadth, P3 install semantics. |
| Resource/model scout | Preserve cross-read UUID isolation; characterize same-archive duplicate UUIDs; account for `Resource(UUID)` constructor requirements; keep model resources as manifest references. |
| Crusty proxy | No source merge until this lane plan exists. Treat Loop 64 as a serialized integration queue, not a parallel merge party. |

## Recommended merge order

1. `loop64-submodule-check`
2. `loop64-save-failure-surface`
3. `loop64-backup-dir-collision`
4. `loop64-project-load-plan`
5. `loop64-type-manifest-errors`
6. `loop64-json-missing-resource`
7. `loop64-json-unknown-resource`
8. `loop64-xml-entry-safety`
9. `loop64-netbeans-library-exists`
10. `loop64-launcher-runtime`
11. `loop64-generated-story-call`
12. `loop64-netbeans-ant-smoke`

This order favors setup and data-loss-adjacent save behavior before archive semantics, and leaves broad/flaky NetBeans runtime work until library assumptions are characterized.

## No-go criteria

No-go any lane if:

- the worktree is dirty at integration time;
- branch evidence lacks focused tests;
- branch evidence lacks root checkstyle or an explicit justified exception;
- branch cannot be rebased cleanly onto current `origin/develop`;
- behavior changes are documented only in `drinkme`, not in source tests/docs where users need them;
- a save/load change cannot prove filesystem state after failure;
- a resource/archive test accepts silent data loss as "no crash";
- a NetBeans lane claims runtime/build coverage while using only test-classpath surrogates or JavaFX stubs.

## Validation command families

Common:

```bash
git status --short --branch
git diff --check origin/develop...HEAD
mvn checkstyle:check -Dcheckstyle.config.location=checkstyle.xml
```

IO lanes:

```bash
mvn -q -DincludeSims=false -Dinstall4j.skip -pl core/story-api-migration -am test -Dtest=IoUtilitiesTest
```

IDE save/load lanes:

```bash
mvn -q -DincludeSims=false -Dinstall4j.skip -pl core/ide -am test -Dtest=ProjectFileUtilitiesTest
```

Project planning seams:

```bash
mvn -q -DincludeSims=false -Dinstall4j.skip -pl core/ide -am test -Dtest=ProjectLoadSuccessPlanTest,ProjectLoadFailurePlanTest,ProjectLoadFailureDispatchPlanTest,ProjectSaveTargetPlanTest
```

NetBeans lanes:

```bash
mvn -q -DincludeSims=false -Dinstall4j.skip -pl netbeans -am test
mvn -DincludeSims=false -Dinstall4j.skip -pl netbeans -am package -DskipTests
```

Submodule lane:

```bash
git submodule status --recursive
test -d tweedle-lang/Grammar
mvn -q -DincludeSims=false -Dinstall4j.skip -pl core/tweedle test -Dtest=ManifestEncoderTest
```
