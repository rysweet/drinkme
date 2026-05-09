# Eatme implementation plan

This `drinkme` copy records the current scenario and readiness direction for the
Alice modernization documentation corpus. It is part of the linked status docs
and keeps the remaining gaps visible for readiness planning. The canonical
implementation plan is maintained in the private `eatme` repo at
`docs/implementation-plan.md`.

## Current direction

The current silver-thread journey is: launch Alice -> build or change a starter
world/program -> run and observe it -> save and reopen it -> report
instructor/student readiness.

eatme owns the scenario coverage, reporting, grading/readiness workflows, and
platform-facing automation that make that journey readable for instructors and
students. RabbitHole owns the Alice-side capability work that the scenarios
exercise: launch, richer UI behavior, visible rendering, Save/Open, and
Tweedle/player behavior.

## Scenario model

Automation scenarios should answer plain user questions:

| Scenario question | Readiness signal |
| --- | --- |
| Can Alice launch in the expected environment? | Instructor and student setup can start. |
| Can a starter world/program be built or changed? | The first lesson can move beyond setup into creation. |
| Can the changed world/program run and be observed? | The learner can see whether the program behaves as intended. |
| Can the project be saved and reopened? | Student work can survive a session and be reviewed later. |
| Can reports explain readiness and gaps? | Instructors know what is ready, partial, or blocked. |

Use "automation scenarios" or "scenarios" in user-facing copy. Avoid exposing
internal mechanics unless a link or artifact contract requires them.

## Current scenario coverage

| Journey step | Current coverage |
| --- | --- |
| Launch Alice | Covered by current scenarios as setup/readiness evidence, but not full UI automation. |
| Build or change a starter world/program | Partly covered by lesson and starter-world scenario inventories. First-lesson completion remains open. |
| Run and observe | Partly covered by desktop Run status and rendering-adjacent evidence. Visible rendering correctness remains open. |
| Save and reopen | Partly covered by Save-path evidence and project IO slices. The real rendered menu path to a written and reopened project remains open. |
| Report instructor/student readiness | Partly covered by readiness reports and scenario inventories. Grading, creative assessment, and deployed sharing/platform behavior remain open. |

## Remaining coverage gaps

| Remaining coverage gap | Next workstream | eatme responsibility |
| --- | --- | --- |
| Full Alice UI automation | RabbitHole | Consume RabbitHole UI evidence in scenarios; do not claim this until RabbitHole capability exists. |
| Visible rendering correctness | RabbitHole | Report RabbitHole rendering evidence and blockers in scenario readiness. |
| Desktop Save menu-to-written-project completion from a real rendered click path | RabbitHole + eatme | Cover and report the scenario after RabbitHole closes the UI/write capability. |
| First-lesson completion | eatme | Own the scenario coverage and readiness report. |
| Grading | eatme | Own grading workflow coverage and report language. |
| Creative assessment | eatme | Own creative-assessment workflow coverage and report language. |
| Deployed sharing/platform behavior | eatme | Own platform-facing automation scenarios and report language. |
| Full Tweedle/player decode | RabbitHole | Report RabbitHole decoder readiness when scenarios depend on player or Tweedle behavior. |
| 70 percent aggregate coverage target | RabbitHole + eatme | Combine source coverage and scenario coverage reporting. |

## Scenario priorities

1. Setup/readiness scenario: verify the environment can start Alice and explain
   any blocking setup issue in instructor/student language.
2. Starter-world scenario: create or change a simple world/program that maps to a
   first-lesson activity.
3. Run-and-observe scenario: run the world/program and report what was visible,
   blocked, or not yet checked.
4. Save-and-reopen scenario: save through the desktop path once RabbitHole
   capability is available, reopen the project, and report whether the work
   survived.
5. Readiness scenario: combine setup, creation, run, save/reopen, grading,
   creative assessment, and sharing/platform signals into one instructor/student
   report.

## Reporting language

Readiness reports should say what is ready, partial, or still missing. Use:

- "covered by current scenarios" when the scenario exists and has evidence;
- "partially covered" when the scenario exercises only a slice of the journey;
- "remaining gap" when the journey step is not yet covered end to end;
- "blocked by RabbitHole capability" when the scenario waits on Alice-side UI,
  rendering, Save/Open, or decoder behavior.

Do not use confidence language that sounds stronger than the evidence. Readiness
reporting is not grading unless the grading scenario and workflow are present.
Readiness reporting is not creative assessment unless the creative-assessment
scenario and workflow are present.

## Review artifacts

These older review artifacts remain useful background, but the current
user-facing plan above is the source of truth for scenario direction:

- [0001 crusty-old-engineer review](reviews/0001-crusty-old-engineer.md)
- [0002 rust memory architecture review](reviews/0002-rust-memory-architecture.md)
- [0003 capability audit](reviews/0003-gadugi-capability-audit.md)
- [0004 real Alice automation design](reviews/0004-real-alice-harness-design.md)
- [0005 second-pass automation review](reviews/0005-second-pass-harness-review.md)
- [0006 second-pass crusty review](reviews/0006-second-pass-crusty-review.md)
- [0007 second-pass curriculum review](reviews/0007-second-pass-curriculum-review.md)
- [0008 second-pass capability review](reviews/0008-second-pass-gadugi-review.md)
- [Alice.org resource map](research/0001-alice-org-resource-map.raw.md)

## Related status

- [Investigation plan](../plan.md)
- [Current state and next steps](../modernization/current-state-and-next-steps.md)
- [Restarted full-scope status](../modernization/restarted-full-scope-status.md)
- [Atlas index](../atlas/index.md)
