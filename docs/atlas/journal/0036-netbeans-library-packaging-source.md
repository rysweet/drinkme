# Journal 0036: NetBeans library packaging source

## Loop 35 target

Follow `Alice3Library` registration toward packaging. A true NBM content test cannot live in the normal unit-test phase because the `.nbm` artifact is produced by `package`, not `test`.

This loop therefore characterizes the packaging source of truth in the NetBeans module POM: the assembly steps that create support artifacts for `Alice3Library` source and javadoc volumes and the renamed NBM.

## Alice implementation commit

Commit in `alice3-modernization`:

- `e663ac0b3f Characterize NetBeans library packaging`

Changes:

- Extended `Alice3LibraryRegistrationTest`.
- Added `pomPackagesAliceLibrarySourceAndJavadocVolumes()`.
- Characterized POM assembly configuration:
  - javadoc assembly via `src/main/resources/assemblies/rename-javadoc.xml`;
  - story source assembly via `src/main/resources/assemblies/story-src.xml`;
  - `nbm/clusters/extra/src/aliceSource` final name;
  - final NBM rename assembly via `src/main/resources/assemblies/rename-nbm.xml`.

## Package probe

As an investigation step, ran:

```bash
mvn -DincludeSims=false -Dinstall4j.skip -pl netbeans -am package -DskipTests
```

That produced:

- `netbeans/target/netbeans-9.1.0-SNAPSHOT.nbm`;
- `netbeans/target/nbm/clusters/extra/modules/org-alice-netbeans.jar`;
- `netbeans/target/nbm/clusters/extra/src/aliceSource.jar`;
- `netbeans/target/nbm/clusters/extra/doc/aliceDocs.zip`.

The package probe is useful evidence, but the committed test stays in the normal test phase and locks the POM source contract rather than depending on a package-phase artifact.

## Review and validation

Crusty verdict:

- Correct boundary: do not make unit tests depend on artifacts not produced by the unit-test lifecycle.
- Good next target: a dedicated package-phase smoke or CI job could assert actual NBM contents, but that should be explicit.
- The exported project is still not proven buildable outside NetBeans; it is only better mapped.

Local validation passed:

```bash
mvn -DincludeSims=false -Dinstall4j.skip -pl netbeans -am test
mvn -DincludeSims=false -Dinstall4j.skip clean test
mvn checkstyle:check -Dcheckstyle.config.location=checkstyle.xml
```

Standalone CI passed for commit `e663ac0b3f`:

- Alice Checkstyle CI: success, run `25274783388`
- Alice Test CI: success, run `25274783371`

## Next useful slices

1. Add an explicit package-phase CI/job or integration test for NBM contents if package time is acceptable.
2. Materialize `Alice3Library` classpath into a generated Ant project smoke test.
3. Continue characterizing exported-project runtime only after classpath/package assumptions are executable.
