# Eatme review 0001: crusty-old-engineer

## Framing

This is not one workstream. It is five hard problems taped together.

The work is still worth doing, but the first proof must be a thin, real, repeatable slice. Do not start by building a general "agentic instructor/student QA crew." That risks producing a demo instead of a validation system.

## Sharp edges

- Alice is a desktop 3D Java app. Headless GUI testing is annoying; headless 3D/OpenGL testing is worse. Xvfb may boot windows but fail rendering or behave differently.
- Agentic QA is nondeterministic. If the test oracle is also an agent, failures become arguments. Keep deterministic assertions around artifacts: project file exists, screenshot captured, lesson step completed, expected UI state visible.
- Maximum parallelism can hurt early. GUI tests, virtual displays, TTY sessions, browser sessions, and model calls compete for ports, displays, CPU, GPU/software rendering, file locks, and rate limits. Parallelize after isolation is proven.
- Rust is fine for the harness. It is probably bad as the first language for every integration. Playwright, desktop automation, YAML scenario runners, and agent tooling are richer elsewhere. Use Rust for orchestration, process control, artifact indexing, and typed lesson validation.
- Editable non-code assets need schemas now. If lessons/prompts/scenarios are loose Markdown only, they will rot.
- Private repo plus agent crew creates governance risk. Agents touching real code, curriculum, and Alice assets need clear read/write boundaries, audit logs, and no silent mutation.
- Multiple review layers can become theater. Reviewer agents are useful only if they check different things: deterministic test reviewer, curriculum reviewer, code reviewer.

## Sequencing constraints

1. Prove `alice3-modernization` can build and run reproducibly.
2. Prove one real Alice GUI session can run under virtual display with artifact capture.
3. Prove one outside-in scenario with deterministic pass/fail.
4. Add one student agent.
5. Add one instructor agent.
6. Add reviewers only after there is something stable to review.

Do not invert this. If the crew comes before the harness, we will debug personalities instead of software.

## Do not overbuild first

- General multi-agent classroom simulator.
- Full Alice.org curriculum ingestion.
- Custom GUI automation framework.
- Visual AI grading for arbitrary 3D scenes.
- Self-improving agents.
- Distributed parallel runner.
- Rich asset editor.
- Full Rust-native replacement for tools that already work.

## Recommended first vertical slice

Build one boring proof:

**Goal:** Given one editable lesson asset, run real Alice, perform one small student task, collect evidence, and produce a deterministic QA verdict.

Example slice:

1. `lesson.yaml`
   - title
   - objective
   - Alice version/source commit
   - required starting project/sample
   - 3-5 student-visible steps
   - deterministic success criteria

2. Rust runner:
   - allocates isolated workspace
   - starts virtual display
   - launches Alice from `alice3-modernization`
   - invokes `gadugi-agentic-test` scenario
   - captures logs, screenshots, project output, timing

3. Gadugi scenario:
   - open Alice
   - create/open one project
   - add or inspect one object
   - run/play scene
   - assert visible evidence or saved artifact

4. Student agent:
   - only reads lesson
   - only interacts outside-in
   - cannot edit repo code

5. Reviewer:
   - checks artifacts against deterministic criteria
   - reports pass/fail with links to screenshots/logs

If that works twice in CI and once locally, then the project has a foundation. Before that, it has a diagram.

## References

- Google SRE, Simplicity: https://sre.google/sre-book/simplicity/
- Martin Fowler, Test Pyramid: https://martinfowler.com/bliki/TestPyramid.html
- Xvfb manual: https://man7.org/linux/man-pages/man1/Xvfb.1.html
- Mesa docs: https://docs.mesa3d.org/
- Gadugi Agentic Test: https://github.com/rysweet/gadugi-agentic-test
- Alice resources: https://www.alice.org/resources/
