# Alice 3 build baseline

Source checkout: `/home/azureuser/src/alice3`  
Public fork: `https://github.com/rysweet/alice3`  
Upstream: `https://github.com/TheAliceProject/alice3`  
Baseline commit: `0e2f80df62 Merge pull request #550 from jennej/eventListeners`

## Repository separation

`drinkme` is a private artifact repository. It must contain investigation notes, plans, maps, diagrams, and generated documentation only. Alice source code remains in the public fork.

## Required build tools

The upstream README requires:

| Tool | Required | Local status |
| --- | --- | --- |
| Java | 21 | OpenJDK 21.0.10 installed |
| Maven | 3.9.9+ | Maven 3.9.11 installed |
| git | yes | installed |
| git-lfs | yes | git-lfs 3.6.1 installed |
| Install4J | installer builds only | not installed; skipped for baseline |

Ant and Gradle are not part of the documented main build path.

## Baseline command

```bash
cd /home/azureuser/src/alice3
git submodule update --init --recursive
git lfs pull
mvn -DincludeSims=false -Dinstall4j.skip -DskipTests=false test
```

## Baseline result

The baseline Maven test run passed.

| Metric | Value |
| --- | --- |
| Maven result | `BUILD SUCCESS` |
| Total time | `05:13 min` |
| Test summary | 218 reported test cases, 0 failures, 0 errors |
| Java production files | 4,528 |
| Java test files | 15 |
| Resource files | 2,372 |
| POM files | 29 |

Active tests are concentrated in `core/util`, `core/tweedle`, and `core/ast`. `core/model-loading` has a test file, but the relevant model export test body is commented out.

## Reactor modules from the root POM

- `core`
- `core/ast`
- `core/croquet`
- `core/i18n`
- `core/ide`
- `core/image-editor`
- `core/issue-reporting`
- `core/resources`
- `core/scenegraph`
- `core/glrender`
- `core/story-api-migration`
- `core/story-api`
- `core/util`
- `core/model-loading`
- `core/tweedle`
- `core/models`
- `external`
- `external/collada`
- `external/collada-schema-1-4-1`
- `external/wrapped-flow-layout`
- `alice-ide`
- `netbeans`

## CI baseline

The only workflow found is `.github/workflows/alice-checkstyle-ci.yml`; it runs `mvn checkstyle:check -Dcheckstyle.config.location=checkstyle.xml` on push. It does not run Maven tests.

