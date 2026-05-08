# 0129 - Four-PR merged metadata status

## Summary

RabbitHole PR #297, RabbitHole PR #298, eatme PR #138, and amplihack-rs PR #571
have merged. This entry records only GitHub-verified merged metadata.

This is a status update only. drinkme records links and merged metadata. It
does not copy RabbitHole, eatme, amplihack-rs, or Alice source.

## Verified merged metadata

Fields recorded: repository, PR number, status, merged timestamp, merged-by user,
merge commit SHA, and head SHA. Repository values come from the fixed GitHub
repository inputs and returned PR URLs. The other metadata values come from the
GitHub CLI JSON fields listed below.

GitHub field mapping:

- merged-by user = `mergedBy.login`
- merge commit SHA = `mergeCommit.oid`
- head SHA = `headRefOid`

| Repository | PR | Status | Merged at | Merged by | Merge commit SHA | Head SHA |
| --- | --- | --- | --- | --- | --- | --- |
| `rysweet/RabbitHole` | [#297](https://github.com/rysweet/RabbitHole/pull/297) | `MERGED` | `2026-05-08T04:39:11Z` | `rysweet` | `527011aa8337222cddd05d23766edcac908a699b` | `59272ae077e3e614f3ef30a4b6b37140c8eb80f8` |
| `rysweet/RabbitHole` | [#298](https://github.com/rysweet/RabbitHole/pull/298) | `MERGED` | `2026-05-08T02:32:51Z` | `rysweet` | `fb9da28c2dcaf426b87699ffceebaba7093d994a` | `6bd52537504d0f88cd0fe6c1919e5a4134eca2a8` |
| `rysweet/eatme` | [#138](https://github.com/rysweet/eatme/pull/138) | `MERGED` | `2026-05-08T02:13:51Z` | `rysweet` | `b412458d6abf4d235dc03f4efb3debabd54e79d1` | `8cacd14cc51fc09cae20ee421f4bc4a8e285b751` |
| `rysweet/amplihack-rs` | [#571](https://github.com/rysweet/amplihack-rs/pull/571) | `MERGED` | `2026-05-08T04:55:47Z` | `rysweet` | `0af6f12824778fbff94627dae5da92b57beb6fc9` | `33582d27e8cac3f00cbd7e702a5304c34768d41a` |

## Metadata boundary

The table does not describe implementation impact, rollout, business value,
downstream effects, or runtime behavior.

No value is listed for any field outside the fixed repository inputs, returned
PR URLs, or returned non-null metadata fields.

## Traceability

- [drinkme status](../../../README.md)
- [root investigation plan](../../plan.md)
- [current modernization plan](../../modernization/current-state-and-next-steps.md)
- [eatme implementation plan](../../eatme/implementation-plan.md)
- Previous entry: [0128 - RabbitHole PR #293 WhileLoop decode status](0128-rabbithole-pr293-while-loop-decode-status.md)
