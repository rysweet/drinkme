# 0044 - Model resource export output characterization

## Scope

Loop 43 followed the crusty proxy review: model export had weaker protection than the NetBeans generated-source area. The existing `ModelExportTest` was mostly commented-out gallery-asset work and did not run meaningful assertions.

## Source change

- Repository: `rysweet/alice3-modernization`
- Branch: `develop`
- Commit: `eb34ad9c6a Characterize model resource export output`
- Modified:
  - `core/model-loading/src/main/java/org/lgna/story/resourceutilities/ModelResourceExporter.java`
  - `core/model-loading/src/test/java/org/lgna/story/resourceutilities/ModelExportTest.java`

## What changed

- Replaced dormant/commented model export tests with active no-Sims JUnit 4 tests.
- Added XML serialization characterization for a synthetic prop resource:
  - root `AliceModel` attributes;
  - creator/year metadata;
  - `placeOnGround="TRUE"`;
  - class tags/group tags/theme tags;
  - default resource entry;
  - current texture-name enum behavior: `Default` is serialized as `DEFAULT`.
- Added generated Java characterization:
  - `ModelResourceExporter.createJavaCode()` emits `TestPropResource`;
  - generated enum implements `PropResource`;
  - generated source compiles with the JDK compiler and current test classpath.
- Made `ModelResourceExporter.createXMLString()` package-visible so the test can exercise serialization without reflection.

## Validation

Local validation in `/home/azureuser/src/alice3-modernization`:

```bash
mvn -DincludeSims=false -Dinstall4j.skip -pl core/model-loading -am test \
  -Dtest=ModelExportTest \
  -Dsurefire.failIfNoSpecifiedTests=false \
  -DfailIfNoTests=false
mvn -DincludeSims=false -Dinstall4j.skip clean test
mvn checkstyle:check -Dcheckstyle.config.location=checkstyle.xml
```

Result: all local gates passed.

CI validation for source commit `eb34ad9c6a16976abff2673e2a2b8eec7cd43d1a`:

| Workflow | Run ID | Result |
| --- | ---: | --- |
| Alice Test CI | 25282678925 | success |
| Alice Checkstyle CI | 25282678929 | success |
| Alice NetBeans Package CI | 25282678928 | success |

## Crusty proxy note

This is a real risk-reduction slice: one dead test file became executable characterization over a compatibility-sensitive exporter. Do not oversell it. It does not prove Collada/glTF output, thumbnails, real gallery assets, or full model package semantics.

## QA note

This is still mostly inside-out, but it is closer to user-observable output than string-only internals: XML and generated Java are durable exported artifacts. The next QA lane should keep pushing toward full exported-project/package smoke tests.

