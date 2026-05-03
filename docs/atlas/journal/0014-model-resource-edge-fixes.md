# Journal 0014: model resource edge fixes

## Loop 13 target

This loop stayed on the pure XML/manifest seam in `ModelResourceInfo`, avoiding renderer, gallery, Sims, and binary asset dependencies.

Two atlas-followup edge cases were confirmed:

- `getPlaceOnGround()` treated `false` as “missing,” so a subresource with `placeOnGround="false"` inherited a true parent value instead of overriding it.
- `getTextureReferenceName()` generated names like `ChairModel_null` for model-only resources that omit `textureName`.

## Alice implementation commit

Commit in `alice3-modernization`:

- `cf1e22ef35 Fix model resource manifest edge cases`

Changes:

- Kept the public `ModelResourceInfo(..., boolean placeOnGround)` constructor intact for source compatibility.
- Internally represented XML-derived `placeOnGround` as nullable so “missing” can inherit while explicit false remains false.
- Changed model-only texture reference naming to use just the model name when texture is missing or blank.
- Added synthetic XML tests for:
  - explicit child `placeOnGround=false` overriding a true parent;
  - missing child `placeOnGround` inheriting from parent;
  - manifest structure/texture-set names for model-only resources avoiding `_null`.

## Review and validation

Crusty review:

- Approved after preserving the public constructor signature; nullable state remains internal.
- Confirmed the tests document real edge behavior and are not asset-dependent.
- Confirmed the model-only manifest naming fix is preferable to preserving `*_null`, which is generated-artifact leakage rather than intentional compatibility.

Local validation passed:

```bash
mvn -DincludeSims=false -Dinstall4j.skip -pl core/story-api -am test
mvn -DincludeSims=false -Dinstall4j.skip clean test
mvn checkstyle:check -Dcheckstyle.config.location=checkstyle.xml
```

Standalone CI passed for commit `cf1e22ef35`:

- Alice Checkstyle CI: success, run `25271688838`
- Alice Test CI: success, run `25271688845`

## Next useful slices

1. Continue no-Sims model/resource work only where synthetic XML or tiny safe fixtures are enough.
2. Look for a safe project persistence fixture path for load/save round trips.
3. Expand NetBeans Java export coverage once tiny `.a3p` fixture provenance is resolved.
4. Re-run atlas bug-hunt passes after the next few structural fixes.
