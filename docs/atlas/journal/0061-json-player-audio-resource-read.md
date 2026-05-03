# 0061 - JSON player audio resource read

## Slice

Added headless characterization for JSON/player export and readback of an AST-referenced `AudioResource`.

## Source change

- Repo: `rysweet/alice3-modernization`
- Branch: `develop`
- Commit: `7a64e1c70e Characterize JSON player audio resource read`
- File:
  - `core/story-api-migration/src/test/java/org/lgna/project/io/IoUtilitiesTest.java`

No production code changed in this slice.

## Test behavior

The new test:

1. Creates a synthetic temporary `sound.wav` file with four bytes.
2. Constructs an `AudioResource` from that file.
3. Builds a synthetic project whose AST references the audio resource through a `ResourceExpression`.
4. Exports the project through `IoUtilities.exportProject(...)`.
5. Reopens the player archive through `IoUtilities.readProject(...)`.
6. Verifies the current resource-only player reader boundary:
   - `programType` remains `null` because Tweedle decoding is still unimplemented;
   - resource class is `AudioResource`;
   - UUID, original file name, display name, content type, byte payload, and normalized duration survive.

## Workflow correction

During this loop the user correctly called out that coding work and subagents must use the amplihack `DEFAULT_WORKFLOW`, not just ad hoc validation. The active loop was retrofitted into explicit Step 0-22 tracking:

- Step 0 workflow preparation was completed by reading `DEFAULT_WORKFLOW.md`.
- Steps blocked by explicit user constraints were marked skipped, not ignored:
  - no upstream issues/PRs/issue DB;
  - no PR creation/merge in this autonomous branch flow.
- Workflow-aware parallel lanes were launched for review, security, QA/outside-in, and philosophy review.
- Future parallel coding should use isolated worktrees/branches per implementation lane; the main working tree remains serialized for integration.

## Review lanes

Workflow-aware review lanes found no blockers:

- Code review: clean test-only characterization, no stubs/TODOs/swallowed exceptions.
- Security: synthetic bytes and temp file are safe; no new archive/path risk.
- QA/outside-in: public `IoUtilities` export/read path is adequate for this headless slice.
- Philosophy: focused, simple, no false claim of full player import support.

## Validation

Local gates:

```bash
mvn -DincludeSims=false -Dinstall4j.skip -pl core/story-api-migration -am test -Dtest=IoUtilitiesTest -Dsurefire.failIfNoSpecifiedTests=false -DfailIfNoTests=false
mvn -DincludeSims=false -Dinstall4j.skip clean test
mvn checkstyle:check -Dcheckstyle.config.location=checkstyle.xml
mvn -DincludeSims=false -Dinstall4j.skip -pl netbeans -am package -DskipTests
```

All local gates passed before push.

CI for `7a64e1c70e` passed:

- Alice Test CI: `25287120566`
- Alice Checkstyle CI: `25287120569`
- Alice NetBeans Package CI: `25287120560`

## Crusty proxy note

This is a useful characterization because the JSON reader claims image/audio support. Now both are pinned. It still does not make player archives fully importable. The program/type reader remains blocked by Tweedle decoding.

## Next seam

Use isolated worktrees for parallel implementation lanes. Strong candidates:

- JSON `.a3c` type-read behavior;
- model-resource export/read boundaries;
- `ProjectApplication` recovery orchestration seam extraction;
- minimal Tweedle decode scaffolding after a narrow grammar plan.
