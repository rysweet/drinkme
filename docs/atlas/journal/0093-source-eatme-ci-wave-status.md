# 0093 - Source, eatme, and CI status wave

## Summary

RabbitHole PRs #173 through #184 and eatme PRs #105, #106, and #108
through #116 have merged. The source work added clearer records for the next
missing desktop actions, clearer failures for several Tweedle/archive edge cases,
and plain notes about RabbitHole CI timing. The eatme work completed the current
local instructor/student documentation, persona, scenario, adapter, and plain
readiness-reporting pass.

This is progress, but it is not a finished Alice modernization. It does not prove
full Alice UI automation, visible rendering correctness, desktop save-menu
completion, grading, creative assessment, learner-world grading, first-lesson
completion, a deployed sharing platform, or full Tweedle decode support.

## What changed in RabbitHole

- [RabbitHole PR #173](https://github.com/rysweet/RabbitHole/pull/173) merged at
  `e20d4eb411c8afb3c326ee585807afd1b3ab29e9`. It records a procedure UI action
  no-go artifact and names the missing desktop code/procedure UI target; no
  desktop UI invocation is proven.
- [RabbitHole PR #174](https://github.com/rysweet/RabbitHole/pull/174) merged at
  `fc0d941fa22686c216e973ea535db6869bc48835`. It records Save-menu action target
  no-go evidence; save-menu completion remains unproven.
- [RabbitHole PR #175](https://github.com/rysweet/RabbitHole/pull/175) merged at
  `2642e9139fb73cfd6d00585d285d03e671c2bbf7`. It adds desktop Run status
  summary evidence; visible rendering correctness and full UI automation remain
  unproven.
- [RabbitHole PR #176](https://github.com/rysweet/RabbitHole/pull/176) merged at
  `c0c2ef5d6a30237d5a8a7e3c0a23a42f16c480f8`. It makes a missing sibling
  Tweedle entry fail clearly.
- [RabbitHole PR #177](https://github.com/rysweet/RabbitHole/pull/177) merged at
  `54d021e3457e6f9250547ec8693f7e491e4b8507`. It clarifies desktop Run evidence
  status summary wording.
- [RabbitHole PR #178](https://github.com/rysweet/RabbitHole/pull/178) merged at
  `5123f03640d7166e30b6160c107e92c78c0f9728`. It makes unnamed unsupported
  manifest Tweedle sibling types fail clearly using the archive path.
- [RabbitHole PR #179](https://github.com/rysweet/RabbitHole/pull/179) merged at
  `0a25c2f17849f944cf5e14f10c26d3be48524d1a`. It documents RabbitHole CI
  timing notes only: Checkstyle 0:53, GitGuardian 0:01, NetBeans 6:01, tests
  7:13, and coverage 11:54. Coverage was the longest observed check.
- [RabbitHole PR #180](https://github.com/rysweet/RabbitHole/pull/180) merged at
  `17c0c593baea0046d502c97f20f0f6a19fef2c09`. It clarifies first-lesson desktop
  evidence reporting.
- [RabbitHole PR #181](https://github.com/rysweet/RabbitHole/pull/181) merged at
  `2dbd3881c096291c529f491173610e5567f1883a`. It characterizes a JSON archive
  with a resource-typed field initializer on the manifest program type; no
  behavior change.
- [RabbitHole PR #182](https://github.com/rysweet/RabbitHole/pull/182) merged at
  `d436b7a9cd2084b3409017cff8cc3605f43ee2d0`. It makes
  `desktop-run-status-summary.json` list the pixel boundary artifact and
  machine-readable missing procedure UI and `SaveProjectOperation` evidence.
- [RabbitHole PR #183](https://github.com/rysweet/RabbitHole/pull/183) merged at
  `82527ca0ed04315dd40808a80ca7946a2cd029b4`. It characterizes typed-null
  Tweedle field initializers; AST decode reports malformed Tweedle, and JSON
  `.a3c` read failures include the archive entry path.
- [RabbitHole PR #184](https://github.com/rysweet/RabbitHole/pull/184) merged at
  `4eb21803bd76bb13bdc75ce53c6f590e3d3597a7`. It documents project-IO and
  Tweedle status by listing covered boundaries and the larger decode gaps that
  remain.

## What changed in eatme

- [eatme PR #105](https://github.com/rysweet/eatme/pull/105) merged at
  `b88afdf60c2dd81a2849878706903f76ab8c2344`. It adds the student artifact
  sharing mission doc entry.
- [eatme PR #106](https://github.com/rysweet/eatme/pull/106) merged at
  `320f3c56cd65ec949e9cea0137f72a3dd0200f09`. It consumes RabbitHole
  desktop-first-lesson next-action evidence in readiness reporting.
- [eatme PR #108](https://github.com/rysweet/eatme/pull/108) merged at
  `5640df08832cb5a74c8051ec19ff769d6484710b`. It adds the classroom gallery
  walk QA scenario.
- [eatme PR #109](https://github.com/rysweet/eatme/pull/109) merged at
  `2c56018f378221748a457b3414a96374d7675185`. It maps teacher community sharing.
- [eatme PR #110](https://github.com/rysweet/eatme/pull/110) merged at
  `3a6fdf35c69f8e96e4a58ea452446a4e40ca4958`. It makes the readiness heading say
  evidence files are not proof of full UI automation.
- [eatme PR #111](https://github.com/rysweet/eatme/pull/111) merged at
  `13458167399bc60ca763fe82d3407ded4418b6e1`. It cancels stale PR-only runs in
  CI.
- [eatme PR #112](https://github.com/rysweet/eatme/pull/112) merged at
  `1f137014d7fd2d5fff1706a861cedb0a6d94d323`. It adds the
  `curriculum-sequence-remix-pack` scenario and generated Gadugi adapter.
- [eatme PR #113](https://github.com/rysweet/eatme/pull/113) merged at
  `a0dd075d7e5c8e21394836de0e5aa01a15643e41`. It aligns the persona asset docs
  inventory.
- [eatme PR #114](https://github.com/rysweet/eatme/pull/114) merged at
  `5f74845722c284eb60bece43e0880a7de23cd888`. It completes the instructor
  mission inventory. The counts then were 34 canonical scenarios, 35 Gadugi
  adapters, 24 personas, and 18 docs pages.
- [eatme PR #115](https://github.com/rysweet/eatme/pull/115) merged at
  `b79ff7b96961bfdf9082a1609c8f86194f7429eb`. It completes the student mission
  inventory; docs reference all 33 scenarios with student personas.
- [eatme PR #116](https://github.com/rysweet/eatme/pull/116) merged at
  `0aa0155d63ee4aa16edba72459e9f3cac47bee27`. Docs/docs-site-only CI now skips
  Rust checks safely; exact time saved awaits a future docs-only PR.

## Eatme audit result

An audit-only check at eatme head `b79ff7b96961bfdf9082a1609c8f86194f7429eb`
before PR #116 found 34 canonical scenarios, 35 Gadugi scenarios (34 generated
and 1 hand-authored validation regression), 69 total scenario YAML files, 24
personas (11 instructor and 13 student), 33 scenarios naming both instructor and
student personas, `real-alice-launch-smoke` as baseline-only, and 18 docs pages
all present in MkDocs navigation. Validation passed.

Plainly: eatme local instructor/student persona coverage, student docs, Gadugi
adapters, and plain readiness output are complete for now. Remaining eatme
blockers depend on RabbitHole first-lesson evidence and broader proof.

## What remains unproven

- Full Alice UI automation remains unproven.
- Visible rendering correctness remains unproven.
- Desktop save-menu completion remains unproven.
- Grading and learner-world grading remain unproven.
- Creative assessment remains unproven.
- First-lesson completion remains unproven.
- A deployed sharing platform remains unproven.
- full Tweedle decode support remains unproven.
- Procedure UI invocation and `SaveProjectOperation` desktop completion remain
  named missing pieces, not completed actions.

## Follow-up work

- Use the new missing-action records to build one deterministic desktop action
  proof at a time.
- Keep RabbitHole CI timing notes current as checks change.
- Keep eatme local inventory counts separate from RabbitHole behavior proof.
