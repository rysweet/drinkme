# 0075 - Run-world contract boundary

This entry records the eatme change that names the next first-lesson stop point
after RabbitHole proves object placement and one backend procedure edit.

## Source change

- eatme PR: [#74](https://github.com/rysweet/eatme/pull/74)
- Squash merge commit: `3450ba905b3a8cf5e9859b8777e487a148ab051a`
- Branch head before merge: `854b339eab72a80a35a3c0b7a21dbb309fd7757b`

## What changed

eatme now records a machine-readable `run-world` no-go contract after procedure
edit proof passes. In plain terms: the harness knows the next action should be
"run the world", but it also records that the proof needed to do that safely
does not exist yet.

The new boundary names:

- missing affordance: `deterministic-alice-world-run-affordance`
- future backend target: `tools/eatme-run-world`
- expected future inputs: edited project, run selector, evidence directory
- expected future outputs: run artifact plus runtime or log evidence

## Why this matters

The previous readiness run proved that RabbitHole can pass window focus, object
placement, and one backend procedure edit before stopping. This change prevents
the next stop from being vague. If edit proof is present, readiness validation
now expects a clear run-world no-go probe instead of silently accepting a generic
"not implemented" state.

## What this proves

- eatme can distinguish "procedure edit passed" from "world run is still the
  next missing action."
- The future run-world hook contract has named inputs and outputs.
- The first-lesson comparison path remains honest about where it stops.

## What this does not prove

- It does not run the Alice world.
- It does not save the project.
- It does not click the desktop run button.
- It does not grade student work or assess creativity.
- It does not complete a teacher/student lesson.

## Next boundary

RabbitHole needs to implement or expose `tools/eatme-run-world`, or an
equivalent stable proof path. eatme should then consume that proof and keep
project save blocked until there is real save evidence.
