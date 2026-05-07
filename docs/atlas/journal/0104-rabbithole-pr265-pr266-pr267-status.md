# 0104 - RabbitHole PR #265, PR #266, and PR #267 status

## Summary

RabbitHole PR #265, PR #266, and PR #267 have merged. This entry records what
those changes prove and what still needs proof.

This is a status update only. drinkme records links and evidence summaries. It
does not copy RabbitHole, eatme, or Alice source.

## What changed in RabbitHole

- [RabbitHole PR #265](https://github.com/rysweet/RabbitHole/pull/265) merged at
  `ead3a465a6c794f552edc32699f011242fc303d7`. The `StageIDE`
  `DocumentFrame.showSaveFileDialog` seam was called while StageIDE was fully
  running under Xvfb, and a live Swing `JFileChooser` was observed in
  `Window.getWindows()` and then cancelled. This proves the exact seam reached
  by `AbstractSaveOperation.perform` leads to a real `JFileChooser` dialog when
  a live StageIDE instance is used. A separate test records that on Linux
  `FileDialogUtilities.createFileDialog()` returns `SwingFileDialog` (not a
  native `java.awt.FileDialog`), so `XFileDialogPeer` is never instantiated on
  this path. This does not prove that the Save menu item was clicked from the
  desktop, that a file was written, or that the full Save-menu-to-written-project
  journey works end-to-end.

- [RabbitHole PR #266](https://github.com/rysweet/RabbitHole/pull/266) merged at
  `2fe0ba4ef5d94e5516e9975f00fea9c23ff79ac9`. A live AT-SPI probe ran against
  Alice under Xvfb, connected to the AT-SPI bus, confirmed Alice's Java process
  is registered via the `libatk-wrapper.so` JNI bridge in OpenJDK 21, and
  recorded that the Java ATK wrapper class is not bridging Swing components to
  AT-SPI nodes in the `exec:java` context. A machine-readable
  `select-project-not-accessible` blocker document names the exact remediation
  (run Alice via `exec:exec` with the ATK wrapper jar on CLASSPATH). This proves
  the AT-SPI bus is reachable and Alice is registered with it. It does not prove
  that Select Project AT-SPI widget enumeration works, that a project can be
  opened, or that the Select Project flow completes end-to-end.

- [RabbitHole PR #267](https://github.com/rysweet/RabbitHole/pull/267) merged at
  `2ca7aa1062ee94b4e10eb8a13cdad8a4f4cfabc6`. Primitive literal local variable
  reassignment (`x <- 5;`) in Tweedle method bodies and constructor bodies now
  decodes, with clear failures for type mismatches and unknown assignment targets.
  Four new decoder tests pass alongside the 55 existing tests (59 total in
  `TweedleEncoderDecoderTest`). This is one narrow reassignment slice on top of
  PR #262 (field assignment) and PR #264 (constructor field assignment). It does
  not prove full Tweedle method or constructor body decode, full player decode,
  non-literal RHS, loops, conditionals, calls, resource initializers, or complete
  Tweedle/player decode support.

## Done vs. remaining

### Proven in this wave

- `DocumentFrame.showSaveFileDialog` reaches a live `JFileChooser` under Xvfb
  when called through a running StageIDE instance (RabbitHole PR #265).
- Linux does not instantiate native `java.awt.FileDialog`/`XFileDialogPeer` on
  the `showSaveFileDialog` path because `FileDialogUtilities.createFileDialog()`
  returns `SwingFileDialog` on Linux (RabbitHole PR #265).
- AT-SPI bus is reachable, Alice's Java process registers with it via
  `libatk-wrapper.so`, and the blocker for full Swing widget introspection is
  identified as the `exec:java` classloader context (RabbitHole PR #266).
- Primitive literal local variable reassignment in Tweedle method and constructor
  bodies decodes, with clear type-mismatch and unknown-target failures
  (RabbitHole PR #267).

### Still not proven

- Full Save-menu-to-written-project desktop journey remains unproven. Separate
  Save stream work is active.
- Project selection and opening remain unproven. AT-SPI widget enumeration is
  blocked on the `exec:java` classloader gap (remediation path documented).
- Full Tweedle method and constructor body decode remains unproven (non-literal
  RHS, loops, calls, conditionals, resource initializers all unproven).
- Full Tweedle/player decode support remains unproven.
- Grading, learner-world grading, and automated creative assessment remain
  unproven.
- Full Alice UI automation remains unproven.
- Visible rendering correctness remains unproven.
- Desktop save-menu completion remains unproven. Separate
  Save stream work is active.
- Native `java.awt.FileDialog`/`XFileDialogPeer` control remains not applicable
  on Linux (not blocked, just not the path used).
- First-lesson completion remains unproven; grading, creative assessment, and
  first-lesson completion have no new evidence in this wave.

## Default-workflow attempt

`amplihack recipe run default-workflow -c task_description="Update plain Alice
modernization status after RabbitHole PR 265" -c repo_path=.`
was attempted first; the process timed out (exit 124) before edits were needed.
Log: `default-workflow-attempt-rh265.log` (empty). Continued manually through
equivalent phases.

## Traceability

- [drinkme status](../../../README.md)
- [root investigation plan](../../plan.md)
- [current modernization plan](../../modernization/current-state-and-next-steps.md)
- [restarted full-scope status](../../modernization/restarted-full-scope-status.md)
- [eatme implementation plan](../../eatme/implementation-plan.md)
- Previous entry: [0103 - RabbitHole PR #264 and eatme PR #124](0103-rabbithole-pr264-eatme-pr124-status.md)
