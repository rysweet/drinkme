# 0037 - NetBeans package CI

## Scope

Loop 36 added a GitHub Actions gate for the NetBeans package phase in the standalone modernization repository. This closes the gap between the previous local package probe and continuous validation.

## Source change

- Repository: `rysweet/alice3-modernization`
- Branch: `develop`
- Commit: `521602d0b9 Add NetBeans package CI`
- Added workflow: `.github/workflows/alice-netbeans-package-ci.yml`
- Workflow command:
  - `mvn -DincludeSims=false -Dinstall4j.skip -pl netbeans -am package -DskipTests`

The workflow intentionally checks out with `lfs: false`, matching the no-Sims test gate. The package phase should remain independent of Sims/Git LFS assets.

## Local validation

Ran in `/home/azureuser/src/alice3-modernization`:

```bash
mvn -DincludeSims=false -Dinstall4j.skip -pl netbeans -am package -DskipTests
mvn -DincludeSims=false -Dinstall4j.skip clean test
mvn checkstyle:check -Dcheckstyle.config.location=checkstyle.xml
```

Result: all local gates passed.

## CI validation

All workflows passed for source commit `521602d0b941d4667dc74cef0b81678ecd7721f4`:

| Workflow | Run ID | Result |
| --- | ---: | --- |
| Alice Checkstyle CI | 25274923435 | success |
| Alice Test CI | 25274923442 | success |
| Alice NetBeans Package CI | 25274923443 | success |

## What this proves

- The no-Sims package phase can run in GitHub Actions without fetching Git LFS assets.
- The NetBeans module still packages from the reactor after the generated-source/resource/export characterization changes.
- NBM/support artifact generation is now continuously checked rather than relying on a one-off local probe.

## What this does not prove yet

- The workflow does not inspect the packaged NBM archive contents beyond Maven package success.
- It does not install the NBM into NetBeans.
- It does not run an exported Ant project against a populated `Alice3Library`.
- It skips tests in the package job; behavioral coverage remains in `Alice Test CI`.

## Crusty proxy note

This is a useful ratchet, not a modernization endpoint. Package success is necessary but not sufficient. Next high-value work remains exported-project smoke coverage, generated launcher execution, and broader generated-source characterization for real Alice constructs.
