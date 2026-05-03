# 0038 - NetBeans package artifact assertions

## Scope

Loop 37 tightened the NetBeans package CI workflow so package success is not just a Maven exit code. The workflow now checks that the expected package artifacts exist and contain representative entries required by exported Alice Java projects.

## Source change

- Repository: `rysweet/alice3-modernization`
- Branch: `develop`
- Commit: `ce9f40ce98 Verify NetBeans package artifacts in CI`
- Modified workflow: `.github/workflows/alice-netbeans-package-ci.yml`

The workflow still runs:

```bash
mvn -DincludeSims=false -Dinstall4j.skip -pl netbeans -am package -DskipTests
```

It now also verifies:

- exactly one top-level `netbeans/target/netbeans-*.nbm`;
- `netbeans/target/nbm/clusters/extra/modules/org-alice-netbeans.jar`;
- `netbeans/target/nbm/clusters/extra/src/aliceSource.jar`;
- `netbeans/target/nbm/clusters/extra/doc/aliceDocs.zip`;
- `org/alice/netbeans/Alice3Library.xml` in the module jar;
- `org/alice/netbeans/layer.xml` in the module jar;
- `SProgram.java` in `aliceSource.jar`;
- `overview-summary.html` in `aliceDocs.zip`.

## Local validation

Ran in `/home/azureuser/src/alice3-modernization`:

```bash
mvn -DincludeSims=false -Dinstall4j.skip -pl netbeans -am package -DskipTests
# artifact/content assertions equivalent to the CI workflow
mvn -DincludeSims=false -Dinstall4j.skip clean test
mvn checkstyle:check -Dcheckstyle.config.location=checkstyle.xml
```

Result: all local gates passed. The local assertion output confirmed `Alice3Library.xml`, `layer.xml`, `SProgram.java`, and `overview-summary.html`.

## CI validation

All workflows passed for source commit `ce9f40ce982db06aad39932a5ffe8851a50b7364`:

| Workflow | Run ID | Result |
| --- | ---: | --- |
| Alice Checkstyle CI | 25275134734 | success |
| Alice NetBeans Package CI | 25275134736 | success |
| Alice Test CI | 25275134876 | success |

## What this proves

- The package phase produces the expected NBM support files in CI.
- The packaged NetBeans module still carries the library registration resources.
- The source and javadoc volumes referenced by `Alice3Library.xml` are represented by actual packaged archives.

## What this does not prove yet

- It does not install the NBM into NetBeans.
- It does not parse NBM manifests or update tracking metadata deeply.
- It does not compile or run an exported Ant project against the packaged `Alice3Library`.

## Crusty proxy note

This is the right kind of ratchet: cheap, deterministic, and aimed at a real integration seam. It is not a substitute for exported-project execution. The next serious export slice should prove the generated launcher or standalone Ant project path, not add more paper coverage.
