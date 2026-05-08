# drinkme

drinkme is the documentation and evidence tracker for modernizing Alice 3.

## What this project is

- **RabbitHole** is the modernized Alice source tree where runtime, project, UI,
  and decoder changes are made.
- **eatme** is the headless browser and runtime side that checks Alice lesson
  material outside the old desktop-only path.
- **drinkme** keeps the plan, evidence map, diagrams, and history so the work
  stays clear about what is proven and what is still missing.

## Plan

- Keep Alice lessons loadable outside the legacy desktop path.
- Prove content parsing, project loading, and basic lesson flow in small steps.
- Keep browser and desktop work honest with repeatable checks.
- Move detailed status history into atlas docs instead of the README.

## Proven progress

- A browser smoke path exists for checking lesson material outside the old
  desktop-only flow.
- Documentation CI checks repository shape, JSON, YAML, and internal Markdown
  links.
- Atlas and journal docs capture detailed evidence history.
- Some Alice project/package evidence has been captured, including project
  loading, Save-path probes, and limited Tweedle decode slices.

## Currently in progress

- More browser and desktop coverage for Alice lesson paths.
- More Alice lesson evidence gathering.
- Save/load and player decode investigation.
- Documentation cleanup that keeps the README short and moves history into the
  atlas.

## Still unproven

- Full Alice UI automation.
- Visible rendering correctness.
- Desktop Save completion.
- Grading.
- Creative assessment.
- First-lesson completion.
- Full Tweedle/player decode.
- 70 percent aggregate coverage.

## Detailed history

Use the [atlas index](docs/atlas/index.md) for the current map and the
[atlas journal](docs/atlas/journal/) for chronological evidence records.
