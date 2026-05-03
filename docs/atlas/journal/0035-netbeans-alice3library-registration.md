# Journal 0035: NetBeans Alice3Library registration

## Loop 34 target

Follow the exported build-property contract to the next source of truth: where `libs.Alice3Library.*` comes from.

The answer is not Java code. The NetBeans module registers `Alice3Library.xml` through `layer.xml` under `org-netbeans-api-project-libraries/Libraries`, and exported projects refer to that named library.

## Alice implementation commit

Commit in `alice3-modernization`:

- `4d15310d70 Characterize Alice3Library registration`

Changes:

- Added `Alice3LibraryRegistrationTest`.
- Characterized layer registration:
  - `target/classes/org/alice/netbeans/layer.xml`;
  - `org-netbeans-api-project-libraries/Libraries`;
  - `Alice3Library.xml` registration.
- Characterized the library declaration:
  - library name `Alice3Library`;
  - type `j2se`;
  - classpath volume with Alice jars and JavaFX graphics;
  - source volume `nbinst:/src/aliceSource.jar`;
  - javadoc volume `nbinst:/doc/aliceDocs.zip`.

## Review and validation

Crusty verdict:

- Good map point: exported projects depend on NetBeans module installation state, not just files generated into the project directory.
- Important caveat: this still does not prove every referenced `nbinst:` jar exists in the packaged NBM, and it does not run an exported Ant build.
- There is a suspicious historical detail worth tracking, not changing blindly: the `story-api.jar/` classpath resource has a trailing slash. Leave it characterized until a packaged-project build test proves whether it matters.

Local validation passed:

```bash
mvn -DincludeSims=false -Dinstall4j.skip -pl netbeans -am test
mvn -DincludeSims=false -Dinstall4j.skip clean test
mvn checkstyle:check -Dcheckstyle.config.location=checkstyle.xml
```

Standalone CI passed for commit `4d15310d70`:

- Alice Checkstyle CI: success, run `25274621665`
- Alice Test CI: success, run `25274621670`

## Next useful slices

1. Characterize packaged NBM/ext contents against `Alice3Library.xml`.
2. Decide whether to build a synthetic standalone Ant project by materializing `Alice3Library` classpath.
3. Continue generated-source branch coverage only after export packaging assumptions are locked.
