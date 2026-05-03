# Journal 0034: NetBeans exported build-property contract

## Loop 33 target

Start mapping the full exported NetBeans/Ant project build path after the generated-source compile smokes. The immediate finding: the generated project template is not standalone by itself. It depends on a NetBeans library named `Alice3Library` for compile classpath and Alice root-directory runtime wiring.

Rather than fake an external Ant build, this loop locks the template contract and fixes CI so the no-Sims gate does not depend on Git LFS asset availability.

## Alice implementation commits

Commits in `alice3-modernization`:

- `cbb2c9217f Characterize exported project build properties`
- `9624b81198 Skip LFS for no-Sims test CI`

Changes:

- Added `projectTemplateBuildPropertiesDeclareAliceLibraryContract()` to `Alice3ProjectTemplateWizardIteratorTest`.
- Characterized `nbproject/project.properties` expectations in `ProjectTemplate.zip`:
  - `javac.release = 21`;
  - `javac.classpath` uses `${libs.Alice3Library.classpath}`;
  - `main.class = AliceJavaFXLauncher`;
  - `run.jvmargs` sets `-Dorg.alice.ide.rootDirectory="${libs.Alice3Library.src}_root"`;
  - JavaFX application module opens are present.
- Updated `.github/workflows/alice-test-ci.yml` to use `lfs: false`.

## CI incident

The first CI run for `cbb2c9217f` had a test-workflow checkout failure before Maven ran:

```text
This repository exceeded its LFS budget.
```

That was not a code failure. The no-Sims test baseline does not need LFS assets, so the workflow now skips LFS checkout. The corrective commit `9624b81198` produced a clean rerun.

## Review and validation

Crusty verdict:

- Correct call: do not pretend the exported project is standalone when the template clearly depends on a NetBeans global library.
- Also correct: no-Sims CI should not fetch LFS blobs. If a future Sims/assets job needs LFS, make it explicit and separate.
- Next step should be mapping how `Alice3Library` is created/configured, then deciding whether a portable exported-project build test is possible.

Local validation passed:

```bash
mvn -DincludeSims=false -Dinstall4j.skip -pl netbeans -am test
mvn -DincludeSims=false -Dinstall4j.skip clean test
mvn checkstyle:check -Dcheckstyle.config.location=checkstyle.xml
```

Standalone CI:

- Commit `cbb2c9217f`:
  - Alice Checkstyle CI: success, run `25274389136`
  - Alice Test CI: failed at checkout due LFS budget, run `25274389139`
- Commit `9624b81198`:
  - Alice Checkstyle CI: success, run `25274493700`
  - Alice Test CI: success, run `25274493704`

## Next useful slices

1. Locate and characterize `Alice3Library` registration/configuration for exported projects.
2. Decide whether to synthesize a portable Ant build classpath for a generated project test.
3. Keep source-generator construct characterization moving only where it closes clear export/build/runtime gaps.
