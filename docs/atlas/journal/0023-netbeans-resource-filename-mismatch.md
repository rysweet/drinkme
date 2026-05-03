# Journal 0023: NetBeans resource filename mismatch

## Loop 22 target

Run a code-atlas consistency check over the generated resource path after proving runtime loading:

```text
ProjectCodeGenerator copies bytes -> generated resources/ path
ResourcesTypeWrapper emits constructor -> runtime classpath resource path
```

The two sides were not using the same `Resource` property.

## Bug found

`ProjectCodeGenerator` copied resource bytes using:

```java
resource.getName()
```

`ResourcesTypeWrapper` generated `Resources.java` constructor calls using:

```java
"resources/" + resource.getOriginalFileName()
```

If Alice changed a resource display name while preserving its original file name, export would copy bytes to one path and generated Java would load from another. The previous tests missed this because `name == originalFileName`.

## Alice implementation commit

Commit in `alice3-modernization`:

- `4a44541510 Fix generated resource filename mismatch`

Changes:

- `ProjectCodeGenerator` now copies generated resource bytes using `resource.getOriginalFileName()`.
- Added a regression where `TestResource` has:
  - original file name: `note.txt`;
  - display name: `friendly note`.
- Verified export writes `resources/note.txt`, does not write `resources/friendly note`, and compiled generated `Resources.java` loads the original bytes.
- Refactored the resource runtime-load assertion into a helper to keep the NetBeans test readable.

## Review and validation

Crusty verdict:

- Good fix: it aligns copy-side and generated-code-side contracts instead of adding fallback magic.
- Compatibility risk is low because generated `Resources.java` already required `originalFileName`; copying by display name was the inconsistent side.
- Remaining edge: resources with missing or duplicate original filenames still need characterization before touching behavior.

Local validation passed:

```bash
mvn -DincludeSims=false -Dinstall4j.skip -pl netbeans -am test
mvn -DincludeSims=false -Dinstall4j.skip clean test
mvn checkstyle:check -Dcheckstyle.config.location=checkstyle.xml
```

Standalone CI passed for commit `4a44541510`:

- Alice Test CI: success, run `25272880288`
- Alice Checkstyle CI: success, run `25272880190`

## Next useful slices

1. Characterize duplicate original filenames in exported resources.
2. Characterize missing/blank original filenames if production resources can reach that state.
3. Continue exported Java path coverage toward a full generated Ant/NetBeans project build.
