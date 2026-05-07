# 0101 - RabbitHole PR #260, PR #261, PR #262 and eatme PR #122 status

## Summary

RabbitHole PR #260, PR #261, and PR #262 have merged, along with eatme PR #122.
This entry records what those changes prove and what still needs proof.

This is a status update only. drinkme records links and evidence summaries. It
does not copy RabbitHole, eatme, or Alice source.

## What changed in RabbitHole

- [RabbitHole PR #260](https://github.com/rysweet/RabbitHole/pull/260) merged at
  `b553677c1225d704d1d951a59653fb0f66096139`. A Swing `JFileChooser` dialog was
  observed under Xvfb and approved through the chooser's controls. This proves
  the `JFileChooser` dialog appears and responds to programmatic input in the
  test environment. It does not prove native `java.awt.FileDialog` peer control
  or the full StageIDE Save-menu-to-real-chooser journey.
- [RabbitHole PR #261](https://github.com/rysweet/RabbitHole/pull/261) merged at
  `97c1ae707544bd0ca89e711df92e7e45e6d377ac`. The Select Project Java window was
  observed under Xvfb with its title, Java class, process, and geometry
  recorded. This proves the Select Project window appears in the test
  environment. It does not prove selecting or opening a project, world
  execution, or installer success.
- [RabbitHole PR #262](https://github.com/rysweet/RabbitHole/pull/262) merged at
  `9ef09e05402b2e0af9c07803eee92aa5db29b325`. Primitive literal field
  assignments in Tweedle method bodies now decode, with clear unsupported-form
  failures for other cases. This is one narrow decoder slice. It does not prove
  full Tweedle method body decode, full constructor decode, player decode, or
  complete Tweedle/player decode support.

## What changed in eatme

- [eatme PR #122](https://github.com/rysweet/eatme/pull/122) merged at
  `41142db`. Adds the `lost-robot-debug-museum` instructor/student scenario for
  the reflective-debugger/debug-coach use case. This adds a new scenario to the
  eatme scenario library. It does not prove grading, creative assessment, real
  Alice UI automation, or full lesson delivery.

## Done vs. remaining

### Proven in this wave

- Swing `JFileChooser` dialog appears under Xvfb and responds to chooser
  controls (PR #260).
- Select Project Java window appears under Xvfb with title, class, process, and
  geometry recorded (PR #261).
- Primitive literal field assignments in Tweedle method bodies decode, with
  clear unsupported-form failures (PR #262).
- `lost-robot-debug-museum` instructor/student scenario added to eatme scenario
  library (eatme PR #122).

### Still not proven

- Native `java.awt.FileDialog` peer control remains unproven.
- Full StageIDE Save-menu-to-real-chooser journey remains unproven.
- Selecting or opening a project remains unproven.
- World execution remains unproven.
- Deployed installer success remains unproven.
- Full Tweedle method body decode remains unproven.
- Full Tweedle constructor, player, and complete decode support remain unproven.
- Grading, learner-world grading, and creative assessment remain unproven.
- First-lesson completion and full first-lesson completion remain unproven.
- Full Alice UI automation remains unproven.
- Visible rendering correctness remains unproven.
- Desktop save-menu completion remains unproven.

## What remains unproven (summary)

- Full Alice UI automation remains unproven.
- Visible rendering correctness remains unproven.
- Desktop save-menu completion remains unproven.
- Native `java.awt.FileDialog` peer control remains unproven.
- Full StageIDE Save-menu-to-real-chooser journey remains unproven.
- Project selection and opening remain unproven.
- Grading, creative assessment, first-lesson completion remain unproven.
- Full Tweedle/player decode support remains unproven.

## Traceability

- [drinkme status](../../../README.md)
- [root investigation plan](../../plan.md)
- [current modernization plan](../../modernization/current-state-and-next-steps.md)
- [restarted full-scope status](../../modernization/restarted-full-scope-status.md)
- [eatme implementation plan](../../eatme/implementation-plan.md)
