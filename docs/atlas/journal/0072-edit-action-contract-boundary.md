# 0072 - Edit action contract boundary

This entry records the eatme follow-up after first-lesson readiness could pass
object placement and reach the remaining edit/run/save blockers.

## What changed

- [eatme PR #72](https://github.com/rysweet/eatme/pull/72) adds a
  machine-readable no-go probe for the next first-lesson action:
  `edit-procedure-or-code-block`.
- The probe is recorded only after object placement proof exists.
- The new missing affordance is named:
  `deterministic-alice-procedure-edit-affordance`.
- `ui-action-contract.json` now names the expected future contract:
  - candidate backend: `tools/eatme-edit-procedure`;
  - inputs: project after object placement, procedure selector, edit spec, and
    evidence directory;
  - outputs: edited project artifact and procedure or code diff.
- eatme validation now rejects a first-lesson readiness contract that claims the
  edit no-go state without also proving the object-placement precondition.
- Small helper modules were split out so the first-lesson action code stays
  under the repository's module-size gate.

## What this proves

- The harness has moved from a vague "edit/run/save are still missing" message
  to a specific, testable edit contract boundary.
- RabbitHole now has a concrete next hook target after object placement.
- eatme can keep the target blocked while still reporting the exact missing
  action contract.

## What this does not prove

- It does not edit an Alice procedure or code block.
- It does not run the world.
- It does not save the project.
- It does not automate Alice gallery UI clicks.
- It does not grade work, assess creativity, or complete a teacher/student
  lesson.

## Gate notes

- `cargo test -q -p eatme-alice` passed.
- Asset validation passed.
- Generated Gadugi adapters were fresh.
- `scripts/quality-gates.sh` passed locally and in GitHub Actions.
- Focused review found two contract issues before merge: a stale evidence name
  and incomplete edit-precondition validation. Both were fixed before PR #72 was
  merged.
