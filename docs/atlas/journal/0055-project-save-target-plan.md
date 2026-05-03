# 0055 - Project save target plan

## Slice

Extracted and characterized the `ProjectApplication.saveProjectTo(...)` target decision into a small package-private `ProjectSaveTargetPlan`.

## Source change

- Repo: `rysweet/alice3-modernization`
- Branch: `develop`
- Commit: `54b74d2476 Extract project save target plan`
- Files:
  - `core/ide/src/main/java/org/alice/ide/ProjectApplication.java`
  - `core/ide/src/main/java/org/alice/ide/ProjectSaveTargetPlan.java`
  - `core/ide/src/test/java/org/alice/ide/ProjectSaveTargetPlanTest.java`

## Test behavior

The new tests characterize the current save-target decisions:

1. Saving a new project to a normal `.a3p` copies default backups and is not a backup save.
2. Saving a project opened from `.defaultbak` to a normal `.a3p` copies default backups.
3. Saving from `.defaultbak` back into `.defaultbak` does not copy default backups and is a backup save.
4. Saving an existing project to a sibling `.bak` file is treated as a backup save.

## Why this slice

Crusty and code-atlas both identified `ProjectApplication.saveProjectTo(...)` as the next stateful data-loss seam. Directly constructing `ProjectApplication` in a unit test still drags in a large Swing/IDE frame, so this slice extracts the target decision into a testable collaborator while preserving the current save order and side effects.

## Findings

- The previous inline logic is now expressed as `ProjectSaveTargetPlan.choose(...)`.
- `ProjectApplication.saveProjectTo(...)` still copies default backups before swapping `uriProjectLoader`, still swaps the loader before saving, and still updates the interface only when default backups were copied.
- The extracted class is 35 lines; the test is 85 lines.
- This is a small refactor behind characterization, not a policy change.

## Validation

Local gates:

```bash
mvn -DincludeSims=false -Dinstall4j.skip -pl core/ide -am test -Dtest=ProjectSaveTargetPlanTest -Dsurefire.failIfNoSpecifiedTests=false -DfailIfNoTests=false
mvn -DincludeSims=false -Dinstall4j.skip clean test
mvn checkstyle:check -Dcheckstyle.config.location=checkstyle.xml
mvn -DincludeSims=false -Dinstall4j.skip -pl netbeans -am package -DskipTests
```

All local gates passed before push.

CI for `54b74d2476` passed:

- Alice Test CI: `25285447577`
- Alice Checkstyle CI: `25285447568`
- Alice NetBeans Package CI: `25285447569`

## Crusty proxy note

This isolates a decision seam. It does not prove the full menu/action save journey, and it deliberately does not fix the existing ordering where `uriProjectLoader` is swapped before the save write completes. That ordering is now easier to reason about, but still needs a separate characterization/fix if we decide it is wrong.

## Next seam

Either continue extracting the remaining `ProjectApplication` recovery orchestration decisions, or take QA's lower-risk outside-in recommendation: export a resource-bearing project and prove the exported artifact can be reopened with resource fidelity where applicable.
