# Journal 0002: standalone modernization repo and first implementation slice

## Hard routing decision

The modernization work moved to a standalone repository:

- Source modernization repo: `https://github.com/rysweet/alice3-modernization`
- Private artifact repo: `https://github.com/rysweet/drinkme`
- Upstream source reference: `https://github.com/TheAliceProject/alice3`

`rysweet/alice3-modernization` is not a GitHub fork. It preserves Alice history but has its own issue and pull request namespace. This avoids accidental use of the upstream issue database.

Local remote policy:

- `origin` points to `https://github.com/rysweet/alice3-modernization.git`
- `upstream-source` fetches from `https://github.com/TheAliceProject/alice3.git`
- `upstream-source` push URL is disabled

All agents and automation must follow: do not open upstream issues or pull requests.

## First implementation slice

Commit in `alice3-modernization`:

- `78e33abd12 Characterize Alice IDE launch arguments`

Changes:

- Added `AGENTS.md` with no-upstream guardrails.
- Extracted Alice IDE launch argument parsing from `EntryPoint` into package-private immutable `LaunchConfiguration`.
- Added 8 JUnit 4 characterization tests for current launch argument behavior.
- Left behavior compatible with current Alice 3, including quirky legacy parsing behavior and silent geometry fallback.

Crusty review result:

- No blockers.
- Review accepted the slice as behavior-preserving and adequately characterized for this seam.

## CI gate

Commit in `alice3-modernization`:

- `7c3892349f Add no-Sims Maven test CI`

Added standalone GitHub Actions workflow:

```bash
mvn -DincludeSims=false -Dinstall4j.skip clean test
```

CI results:

- Alice Test CI: success, run `25269201552`
- Alice Checkstyle CI: success, run `25269201551`

## Local validation

Passed:

```bash
mvn -DincludeSims=false -Dinstall4j.skip -pl alice-ide -am test
mvn -DincludeSims=false -Dinstall4j.skip clean test
```

The full non-clean run exposed stale/incremental target fragility in `core/tweedle` class files. A clean build passes. Treat clean test as the reliable baseline gate until incremental build behavior is separately characterized.

## Crusty assessment

This is the correct size of first cut. It does not pretend to solve 70% coverage. It adds one protected seam, proves the repo can build in CI, and reduces risk before touching more important code.

Next useful slices:

1. Add project/version and manifest snapshot characterization where fixtures are already small.
2. Re-enable or replace the commented `ModelExportTest` with minimal no-Sims fixtures.
3. Add coverage reporting after the suite has enough meaningful tests; raw percentage before useful tests is vanity accounting.
4. Continue extracting small testable services from startup and project-loading paths.

