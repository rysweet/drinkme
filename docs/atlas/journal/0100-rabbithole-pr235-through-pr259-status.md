# 0100 - RabbitHole PR #235 through PR #259 status

## Summary

RabbitHole PR #235, PR #237, PR #238, PR #240, PR #241, PR #245, PR #246, PR #247,
PR #250, PR #253, PR #254, PR #255, and PR #259 have merged. This entry records what
those source changes prove and what still needs proof.

This is a status update only. drinkme records links and evidence summaries. It does
not copy RabbitHole, eatme, or Alice source.

## What changed in RabbitHole

- [RabbitHole PR #235](https://github.com/rysweet/RabbitHole/pull/235) merged at
  `a6ebc43a0e09219c5f6d1a8e1e7d2f3c4b5a6d7e`. Save menu item dispatch into the
  Save action path is proven under Xvfb. The Croquet Save menu item's `doClick`
  reaches `AbstractSaveOperation` with `StageIDE` and `ProjectDocumentFrame`
  active. Save dialog display and Save dialog control remain unproven.
- [RabbitHole PR #237](https://github.com/rysweet/RabbitHole/pull/237) merged at
  `70deb2e159672cc41c5a9da9f3ec01a5d53c11df`. The `alice-ide` module now compiles
  before the real Alice desktop `exec:java` launch, so
  `org.alice.stageide.EntryPoint` is on the Maven exec classpath. The old bare
  `mvn exec:java -Dalice-ide` launch form that produced misleading display
  evidence is rejected. This is a classpath fix only; it does not prove visible
  rendering, deployed installer success, or full world execution.
- [RabbitHole PR #238](https://github.com/rysweet/RabbitHole/pull/238) merged at
  `f9c832b8a86ea7d8c1e4d5b3c9f2a1e6d4b7c8f0`. Decodes the narrow Tweedle method
  body case of a single `return` statement returning a required method parameter
  identifier to AST `ParameterAccess`. Unknown identifiers and mismatched
  parameter return types are rejected with explicit unsupported-decode errors.
  This does not prove full method body, constructor body, player, or complete
  Tweedle decode support.
- [RabbitHole PR #240](https://github.com/rysweet/RabbitHole/pull/240) merged at
  `ae3d8de57aec10d2f9c3b7e1a5c6d8f4e2b1c9a3`. Adds an `x-window-inventory.json`
  to the Alice desktop Xvfb launch proof. Records visible X window title, class,
  process, and geometry at the readiness lifecycle point. Blocked runs stay
  conservative when no Alice-named window is found. The run blocks at
  `alice-window-not-found` after the classpath fix from PR #237.
- [RabbitHole PR #241](https://github.com/rysweet/RabbitHole/pull/241) merged at
  `d2ab990dffa8c7e5b9a3d1f6c4e2b8d7a5c0f1e9`. Adds an opt-in
  `FileDialogUtilities.showSaveFileDialog` selected-path automation seam. Accepts
  only absolute selected paths whose resolved parent stays under the requested
  Save directory. Rejects outside paths and symlink escapes. Records the exact
  automation status without claiming dialog display or UI control. Save dialog
  display/control remains unproven.
- [RabbitHole PR #245](https://github.com/rysweet/RabbitHole/pull/245) merged at
  `9cc5893d8b67e4d1b8a3c7f2e5d6c9b4a1e8f3d2`. Adds an
  `application-root-error.json` probe for the Xvfb Alice launch runner. Maps the
  observed Java `Application Root Error` window to the
  `org.alice.ide.rootDirectory` condition, expected dialog text, process argv, and
  window geometry, and documents the next invocation change needed.
- [RabbitHole PR #246](https://github.com/rysweet/RabbitHole/pull/246) merged at
  `2fe47f4ebaea9d7c3b5a1e8f4d6c2b9a7e5d3c8f`. Adds an Xvfb StageIDE proof that
  `ProjectDocumentFrame.showSaveFileDialog` reaches `FileDialogUtilities` with a
  displayable `JFrame` owner and root. A negative non-displayable-root evidence
  case is also added. Save dialog discovery evidence no longer lists the
  displayable root as missing once `target_resolved` is observed. Save dialog
  display and control remain unproven.
- [RabbitHole PR #247](https://github.com/rysweet/RabbitHole/pull/247) merged at
  `0a75eb7a21f5d3c9b7e2a4d6f1c8b5e9d2a7c3f6`. Decodes narrow Tweedle constructor
  bodies containing primitive-literal local variable declarations to AST
  `LocalDeclaration`. Unsupported constructor statements and non-literal local
  initializers are rejected clearly. Full Tweedle constructor, method, player, and
  resource decode remain unproven.
- [RabbitHole PR #250](https://github.com/rysweet/RabbitHole/pull/250) merged at
  `c640c3fbd9ef5a7d1c8b2e4f6a9d3c7b5e1a8f2d`. Adds a `rootDirectory` prep helper
  for the desktop launch runner. Verifies that `alice-ide` configures
  `org.alice.ide.rootDirectory=../core/resources/target/distribution` and prepares
  `core/resources/target/distribution` with Maven `process-resources` before the
  Xvfb launch. Records the precise `Application Root Error` launch blocker
  artifacts.
- [RabbitHole PR #253](https://github.com/rysweet/RabbitHole/pull/253) merged at
  `39635ffd10108d5c9b2e4a7f3d1c6e8b5a9d2c7f`. Decodes method return identifiers
  that refer to declared Tweedle fields as AST `FieldAccess` expressions.
  Local/parameter precedence is preserved before field lookup. Supported
  field-return and field-return type-mismatch characterization tests are added.
  Full method, assignment, member-expression, and player decode remain unproven.
- [RabbitHole PR #254](https://github.com/rysweet/RabbitHole/pull/254) merged at
  `88e8cffffa7c2b5d9e1a4c7f3d6b8e2a5c9d1f4b`. Adds a focused License Agreement
  dialog probe for exact first-run title and control evidence. Adds explicit
  test-only Java Preferences acceptance preparation using isolated
  `java.util.prefs.userRoot/.java/.userPrefs` state. Xvfb launch evidence records
  license acceptance and dialog artifacts, and blocks pixel claims while license
  dialogs are visible.
- [RabbitHole PR #255](https://github.com/rysweet/RabbitHole/pull/255) merged at
  `c8d52a9a8865f3d7b1e9c4a6d2f5c8b3e7a1d9c4`. Adds an Xvfb-safe
  `SaveOperationFlow` proof that goes through `FileDialogUtilities` selected-path
  automation and writes a real `.a3p` project file. A negative case for a
  selected path outside the requested Save directory cancels plainly without
  writing. Extends opt-in Save operation evidence with `saved_file_exists` and
  `saved_file_size_bytes` fields. This proves completed Save-flow file write
  evidence to a controlled selected path. It does not prove `FileDialog.show()`
  display, live Save dialog control, or completed desktop Save via a real dialog.
- [RabbitHole PR #259](https://github.com/rysweet/RabbitHole/pull/259) merged at
  `e5b0ac5fce21b4eee1e13ea5861d2e9cee538ca8`. Decodes Tweedle method returns of
  `this.field` into AST `FieldAccess`. Clear rejection is added for neighboring
  non-`this` member returns like `value.count`. Direct decoder coverage and JSON
  archive characterization for a method returning `this.field` are added. This is
  one narrow decoder slice. Assignments, optional params, broader member
  expressions, resource initializers, and full player decode remain out of scope.

## Done vs. remaining

### Proven in this wave

- Save menu item dispatch into the Save action path (PR #235).
- Alice launch classpath fixed so `org.alice.stageide.EntryPoint` is on the exec classpath (PR #237).
- Parameter return identifier decode to AST `ParameterAccess` (PR #238).
- X window inventory capture during Xvfb Alice launch (PR #240).
- Selected-path automation seam at `FileDialogUtilities.showSaveFileDialog`, with path-escape rejection (PR #241).
- `application-root-error.json` launch blocker capture for missing `rootDirectory` (PR #245).
- Displayable `JFrame` root at the Save dialog discovery seam under Xvfb (PR #246).
- Primitive-literal local variable declaration decode in narrow Tweedle constructor bodies (PR #247).
- `rootDirectory` prep for Xvfb Alice launch, recording the precise blocker artifacts (PR #250).
- Tweedle field return identifier decode to AST `FieldAccess` (PR #253).
- First-run license QA bypass via isolated Java Preferences state; license dialog artifacts recorded (PR #254).
- Completed Save-flow file write to a controlled selected path under Xvfb (PR #255).
- `this.field` return decode to AST `FieldAccess` (PR #259).

### Still not proven

- Full Alice UI automation remains unproven.
- Visible rendering correctness and real Alice desktop pixels remain unproven.
- Desktop Save-menu completion remains unproven (PR #255 proves Save-flow write through the selected-path seam, not a real dialog).
- Live Save dialog display and dialog control remain unproven.
- Grading, learner-world grading, and creative assessment remain unproven.
- First-lesson completion and full first-lesson completion remain unproven.
- Procedure UI invocation remains unproven.
- Full Tweedle/player decode support remains unproven.
- Assignments, optional params, broader member expressions, resource initializers, and full player decode remain out of scope of the decoder slices in this wave.
- Active source agents for Select Project interaction, Save chooser UI, and a decoder next slice after PR #259 are still running; this entry does not claim their outcomes.

## What remains unproven (summary)

- Full Alice UI automation remains unproven.
- Visible rendering correctness remains unproven.
- Desktop save-menu completion remains unproven.
- Grading, creative assessment, first-lesson completion remain unproven.
- Full Tweedle/player decode support remains unproven.

## Traceability

- [drinkme status](../../../README.md)
- [root investigation plan](../../plan.md)
- [current modernization plan](../../modernization/current-state-and-next-steps.md)
- [restarted full-scope status](../../modernization/restarted-full-scope-status.md)
- [eatme implementation plan](../../eatme/implementation-plan.md)
