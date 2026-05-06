# 0066 - JavaFX, archive, and first-lesson action boundaries

## Purpose

This journal records the modernization wave that followed the plain-language
README update. The work improved evidence in four places, but it did not finish
the project.

The useful change in this wave is that several vague gaps became executable
checks:

1. exported Java projects now run with real OpenJFX modules until either
   `Program.main` is reached or the headless display boundary stops them;
2. JSON player archives now have an explicit method-decode boundary test;
3. model resource array cleanup is protected by direct helper tests;
4. eatme now records why object placement cannot safely run yet.

## Integrated source changes

| Pull request | Merge commit | Evidence |
| --- | --- | --- |
| `rysweet/RabbitHole#134` | `47c38c1db0c8b4c66a0a19b4f2dcf9468ffcf0cc` | Runs the exported launcher jar with real OpenJFX modules. On headless machines it requires the specific `Unable to open DISPLAY` boundary before `Program.main`; on display-capable machines the generated program marker must receive the expected arguments. |
| `rysweet/RabbitHole#135` | `7f887ce47e5e1ffdf953d3c567b3005e088eced4` | Extracts model resource array helper logic from `ModelResourceExporter`, reducing the class by 94 lines while preserving the public facade and directly testing the extracted helper. |
| `rysweet/RabbitHole#136` | `35c88c573502aee4a7219f4bce598bb560d01cd7` | Adds generated-archive evidence for the JSON player method-decode boundary. Scene type decoding succeeds; unsupported program method decoding is still rejected. |
| `rysweet/eatme#66` | `9965c38954b499a6f5ec57a2bfdffc793466b8d9` | Adds a first-lesson `place-object` precondition probe with a machine-readable `no_go` decision after Alice window activation. |
| `rysweet/drinkme#15` | `cd03fb5bb7889c5008f60092c742836127e847af` | Updates the README status tables and charts with the latest evidence while keeping remaining limits explicit. |

## Review findings that changed the work

Two review findings prevented weak evidence from merging:

- PR #134 originally accepted broad error text such as `DISPLAY`, `Glass`, or
  `gtk`. That could have passed for unrelated toolkit failures. The final test
  requires the specific OpenJFX message `Unable to open DISPLAY`.
- PR #135 originally named the new test after the extracted helper but called
  the old `ModelResourceExporter` facade. The final test calls
  `ModelResourceArrayUtilities` directly, so it protects the extracted code.

That is the point of this process. A green test is not enough when the test does
not prove the thing its name claims.

## Atlas implications

| Area | Updated understanding |
| --- | --- |
| NetBeans/export behavior | The generated launcher has moved beyond stub-only evidence. It now proves real OpenJFX modules can be placed on the forked JVM module path and that the launcher reaches the next honest boundary. It still does not prove a visible JavaFX window, rendering, or a deployed classroom runtime. |
| Project/player reads | JSON player method decoding is now an explicit unsupported boundary rather than an untested gap. This keeps future method/constructor support honest. |
| Model resource export | Array naming, grouping, sorting, and suppression logic is now a smaller helper with direct tests. That makes later resource-export cleanup safer, but does not by itself expand behavior. |
| eatme first-lesson execution | eatme can now distinguish "we activated the Alice window" from "we can place an object." The next action is blocked with a recorded reason instead of hidden behind a vague failure. |

## What this still does not prove

- A teacher or student can complete a full Alice lesson in automation.
- eatme can place an object, edit code, run a world, save a project, grade work,
  or judge creative quality.
- RabbitHole can run a user-visible JavaFX launcher end to end in a deployed
  environment.
- RabbitHole can decode all Tweedle methods, constructors, complex initial
  values, or unresolved parent types.
- The modernization work has reached the long-term coverage target.

## Next evidence targets

1. Turn the eatme place-object `no_go` record into either a deterministic real
   first-lesson action or a smaller UI contract that makes the missing backend
   obvious.
2. Add a real JavaFX/display success path for the exported launcher in an
   environment that can show a window, without relying on stubs.
3. Add more LFS-independent historical archive fixtures that cover old project
   and player formats.
4. Continue reducing large classes only where behavior is already protected or
   a characterization test is added first.
