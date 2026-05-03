# Eatme implementation plan

The canonical implementation plan is maintained in the private `eatme` repo at:

```text
/home/azureuser/src/eatme/docs/implementation-plan.md
```

This `drinkme` copy records the current planning direction and links the plan to the Alice modernization documentation corpus.

## Current direction

The plan has been constrained by first-pass reviews:

- Build the first thin, real, repeatable vertical slice before expanding the agentic classroom crew.
- Use Rust for orchestration, asset validation, memory adapters, reporting, and process control.
- Keep Alice itself Java/Maven.
- Use Xvfb and screenshot/log/process evidence for the real Alice desktop app.
- Use Playwright for Alice.org web resources only, not for the Swing/Croquet IDE.
- Treat true desktop/Swing support as an `eatme` harness first, then consider upstreaming a gadugi `DESKTOP` agent later.
- Keep personas, prompts, rubrics, lessons, and scenarios as editable YAML/Markdown.

## First vertical slice

Given one editable lesson asset:

1. Package real Alice from `/home/azureuser/src/alice3-modernization`.
2. Start Xvfb with isolated user state.
3. Launch Alice via direct Java using `org.alice.stageide.EntryPoint`.
4. Load a known starter project.
5. Capture process status, Alice logs, and screenshot evidence.
6. Produce a deterministic pass/fail verdict.
7. Store artifacts under `runs/<scenario>/<timestamp>/`.

## Review artifacts

- `docs/eatme/reviews/0001-crusty-old-engineer.md`
- `docs/eatme/reviews/0002-rust-memory-architecture.md`
- `docs/eatme/reviews/0003-gadugi-capability-audit.md`
- `docs/eatme/reviews/0004-real-alice-harness-design.md`
- `docs/eatme/research/0001-alice-org-resource-map.raw.md`
