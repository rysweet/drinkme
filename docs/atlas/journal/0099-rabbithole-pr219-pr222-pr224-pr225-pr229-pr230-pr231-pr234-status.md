# 0099 - RabbitHole PR #219/#222/#224/#225/#229/#230/#231/#234 status

## Summary

RabbitHole PR #219, PR #222, PR #224, PR #225, PR #229, PR #230, PR #231, and PR #234 have merged. This entry records what those source changes prove and what still needs proof.

This is a status update only. drinkme records links and evidence summaries. It does not copy RabbitHole, eatme, or Alice source.

## What changed in RabbitHole

- [RabbitHole PR #219](https://github.com/rysweet/RabbitHole/pull/219) merged at `144081e1067cd8795666e5ee8802f47fbfefe671`. Empty no-argument Tweedle constructors now decode to AST `NamedUserConstructor`. Constructor parameters and constructor bodies still failed clearly at that point.
- [RabbitHole PR #222](https://github.com/rysweet/RabbitHole/pull/222) merged at `f749ed7cc92f7df4678e96bbb29bcbd0b09913b8`. It proves the non-desktop Save blocker: `SaveProjectOperation.fire(UserActivity)` reaches `AbstractSaveOperation.perform`, but that proof lacks `StageIDE.getActiveInstance()`.
- [RabbitHole PR #224](https://github.com/rysweet/RabbitHole/pull/224) merged at `1a3eae6937a7109f3608112a7fb40519e1a4f8d7`. A real pixel attempt proved JavaFX cannot open `DISPLAY` locally. It does not prove visible rendering correctness, and visible rendering correctness remains unproven.
- [RabbitHole PR #225](https://github.com/rysweet/RabbitHole/pull/225) merged at `db44c10bd017a5b7cc8eddc1cc82b1d1b90c8fb8`. Required Tweedle constructor parameters decode to AST `UserParameter`. Optional constructor parameters still fail clearly.
- [RabbitHole PR #229](https://github.com/rysweet/RabbitHole/pull/229) merged at `7953c8348272298e9cb85f2319fba6520ba51a32`. Required parameters for empty `void` Tweedle methods decode to AST `UserParameter`. Optional method parameters still fail clearly.
- [RabbitHole PR #230](https://github.com/rysweet/RabbitHole/pull/230) merged at `31d506f6af59ef736ccefad9aa7b793b3add6a3d`. Under Xvfb, Save action invocation is proven with `status=action_invoked`, `StageIDE=true`, and `ProjectDocumentFrame=true`. It does not prove a menu click, dialog display/control, selected path automation, or completed save; completed save remains unproven.
- [RabbitHole PR #231](https://github.com/rysweet/RabbitHole/pull/231) merged at `622748401fe8ff00d81d3a2851faac153585b76c`. Generated launcher Xvfb marker pixels were observed. Real Alice desktop pixels were not observed because `mvn exec:java -Dalice-ide` fails with `org.alice.stageide.EntryPoint` `ClassNotFoundException`.
- [RabbitHole PR #234](https://github.com/rysweet/RabbitHole/pull/234) merged at `45d937fbe1e9ddee74e7c2b89af31841fb38a202`. Single primitive-literal Tweedle `return` method bodies decode to AST `ReturnStatement`. This is not full method decode, full player decode, or full Tweedle decode support; full Tweedle/player decode support remains unproven.

## What remains unproven

- Full Alice UI automation remains unproven.
- Visible rendering correctness and real Alice desktop pixels remain unproven.
- Desktop Save-menu completion remains unproven.
- Save menu click, actual Save dialog display/control, selected path automation, and completed desktop Save remain unproven.
- Grading, learner-world grading, and creative assessment remain unproven.
- First-lesson completion and full first-lesson completion remain unproven.
- Procedure UI invocation remains unproven.
- Full Tweedle/player decode support remains unproven.
- The Save dialog/control follow-up after PR #230 is still active, so this entry does not mark it complete.
- The desktop classpath/render proof follow-up after PR #231 is still active, so this entry does not mark it complete.
- The decoder follow-up after PR #234 is still active, so this entry does not mark it complete.

## Traceability

- [drinkme status](../../../README.md)
- [root investigation plan](../../plan.md)
- [current modernization plan](../../modernization/current-state-and-next-steps.md)
- [restarted full-scope status](../../modernization/restarted-full-scope-status.md)
- [eatme implementation plan](../../eatme/implementation-plan.md)
