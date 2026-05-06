# 0067 - Xvfb launcher and object-placement contract

## Purpose

This journal records the wave that followed the first JavaFX display-boundary
work. It moved one exported-project test from "real JavaFX modules reach a
headless boundary" to "real JavaFX reaches `Program.main` on an Xvfb-backed
display." It also made the next missing eatme affordance explicit.

The wave improved four areas:

1. generated launcher startup through real OpenJFX on Xvfb;
2. JSON player rejection for complex program field initializers;
3. model resource joint-tree cleanup protected by direct tests;
4. eatme's first-lesson object-placement contract.

## Integrated source changes

| Pull request | Merge commit | Evidence |
| --- | --- | --- |
| `rysweet/RabbitHole#137` | `88923a86c9fa54bedc8e3d3df209fb5c1d94e209` | Extracts model resource joint-tree ordering/root handling from `ModelResourceExporter` into a package-private helper with direct helper tests and an exporter-level generated-code ordering check. |
| `rysweet/RabbitHole#138` | `80487be3de2975b58a466d8b6bbf6db67e589941` | Runs the generated `AliceJavaFXLauncher` with real OpenJFX modules under `xvfb-run` and proves `Program.main` receives the expected launch arguments. |
| `rysweet/RabbitHole#139` | `479f6bf7cbbd76d749bfa1891644d8fe121d599d` | Adds generated JSON player archive evidence that a complex program field initializer is rejected at project load without partial program decode. |
| `rysweet/eatme#67` | `9c7c4ae4383954cd0be5b70c25f13254051dc010` | Adds `missing_affordance.id = deterministic-alice-object-gallery-placement-affordance` to the first-lesson `place-object` no-go probe. |

## Review findings that changed the work

PR #138 initially received a false-positive review finding that
`ProjectTemplate.zip` was a Git LFS dependency. The follow-up check showed:

- `.gitattributes` marks `*.zip` as `binary`, not `filter=lfs`;
- the committed `ProjectTemplate.zip` source is a zero-byte placeholder;
- Maven's `project-template` assembly builds the real
  `target/classes/org/alice/netbeans/ProjectTemplate.zip` during
  `process-resources`;
- CI ran the NetBeans tests successfully.

The final review accepted the test as real JavaFX/Xvfb evidence, not LFS-backed
fixture evidence.

## Atlas implications

| Area | Updated understanding |
| --- | --- |
| NetBeans/export behavior | The exported launcher now has an Xvfb-backed proof that real OpenJFX startup reaches generated `Program.main`. This is a stronger runtime seam than the prior headless-boundary test. |
| Project/player reads | Complex program field initializers are now an explicit generated-archive boundary. The project reader rejects the archive because the program type is missing after unsupported decode is skipped. |
| Model resource export | Joint-tree ordering and root-promotion logic is now isolated behind direct tests. Review also noted a pre-existing missing-parent infinite-loop risk; it was not introduced by this extraction. |
| eatme first-lesson execution | The object-placement blocker now names the missing affordance precisely instead of saying only that no backend exists. |

## What this still does not prove

- A user-visible Alice IDE window opens and renders correctly.
- OpenGL scene rendering works in the exported launcher.
- Packaged installers or deployed classroom launchers work.
- eatme can place an object, edit code, run a world, save a project, grade work,
  or complete a full lesson.
- RabbitHole supports complex initializers, methods, constructors, resource
  expressions, or unresolved parent types.

## Next evidence targets

1. Turn `deterministic-alice-object-gallery-placement-affordance` into a real
   backend command, accessibility target, stable menu action, or scene/project
   verification hook.
2. Add an exported launcher test that proves more than `Program.main`: a visible
   window, scene setup, or clean runtime handoff.
3. Add or file a protected test for the pre-existing joint-tree missing-parent
   infinite-loop risk before changing that behavior.
4. Keep adding LFS-independent archive fixtures around old project/player
   formats.
