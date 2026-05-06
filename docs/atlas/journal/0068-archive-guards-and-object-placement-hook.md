# 0068 - Archive guards and object-placement hook contract

## Purpose

This journal records the wave after the Xvfb launcher proof. The work tightened
old-file failure behavior in RabbitHole and moved eatme's first-lesson object
placement check from "the missing affordance has a name" to "Alice can satisfy a
specific proof contract when the hook exists."

The wave improved four areas:

1. old project/player archive boundaries;
2. model resource joint-tree bad-parent handling;
3. generated launcher preconditions;
4. first-lesson object-placement proof requirements.

## Integrated source changes

| Pull request | Merge commit | Evidence |
| --- | --- | --- |
| `rysweet/RabbitHole#140` | `466e1c7c2f630bf158eb8c10d9758884fb4201f8` | Adds an old-archive boundary for unresolved legacy parent types, keeping unsupported data explicit instead of pretending the file is fully decoded. |
| `rysweet/RabbitHole#141` | `b012a03b7f965855fd90fac2e4aaeee12d5d9da3` | Makes model resource joint-tree ordering fail with a bounded `IllegalArgumentException` for missing or cyclic parents instead of hanging forever. |
| `rysweet/RabbitHole#142` | `b5b8139e326bf69214f656189b09746b01ff1ac8` | Guards generated launchers so `Program.main` does not run when a direct call supplies a null JavaFX `Stage`. This does not prove visible window or rendering behavior. |
| `rysweet/eatme#68` | `bd71bba7cac934bfc5f380b4cfe636590aecc29c` | Adds an Alice-side `tools/eatme-place-object` hook contract. Object placement only passes when the hook returns the expected schema, object id, a non-empty placement artifact, and a non-empty scene or project diff artifact. |

## Review findings that changed the work

The RabbitHole launcher work initially claimed too much. A direct
`start(null)` call proves the generated launcher's null-`Stage` guard, not the
full JavaFX lifecycle or a user-visible display. The PR title, test name, error
message, and marker text were narrowed before merge.

The final generated message is:

> Generated launcher requires a non-null primary Stage before Program.main can
> run.

The eatme object-placement contract was accepted because it does not count a
hook as proof unless both required artifacts exist and are non-empty. Missing
hooks remain blocked, not silently successful.

## Atlas implications

| Area | Updated understanding |
| --- | --- |
| Project/player reads | Unresolved parent data is now a named old-archive boundary. That improves safety, but does not complete methods, constructors, or complex value decoding. |
| Model resource export | Missing or cyclic joint parents now produce a bounded error instead of an infinite loop. This is reliability work first, cleanup second. |
| NetBeans/export behavior | The generated launcher has a clearer precondition around JavaFX `Stage` handoff. It still does not prove visible rendering or packaged launcher behavior. |
| eatme first-lesson execution | The next Alice-side step is concrete: provide `tools/eatme-place-object` or an equivalent UI hook that returns proof artifacts. |

## What this still does not prove

- A user-visible Alice IDE window opens and renders correctly.
- OpenGL scene rendering works in the exported launcher.
- Packaged installers or deployed classroom launchers work.
- eatme can actually place an object without the Alice-side hook.
- eatme can edit code, run a world, save a project, grade work, or complete a
  full teacher/student lesson.
- RabbitHole supports full method/constructor decoding, complex values, or
  unresolved parent types.

## Next evidence targets

1. Implement the Alice-side object-placement hook or a stable UI proof path that
   satisfies the eatme contract.
2. Add exported launcher evidence beyond `Program.main`, such as visible window,
   scene setup, or clean runtime handoff.
3. Keep adding LFS-independent old-project fixtures around `.a3p`, `.a3c`, and
   `.a3w` formats.
4. Continue large-class cleanup only behind behavior tests.
