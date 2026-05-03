# 0042 - NetBeans foreach item access

## Scope

Loop 41 checked whether the suspicious `COUNT__` foreach item name found in Loop 40 is merely ugly or breaks generated source when the loop item is used.

## Source change

- Repository: `rysweet/alice3-modernization`
- Branch: `develop`
- Commit: `761d4da5e2 Characterize generated foreach item access`
- Modified test: `netbeans/src/test/java/org/alice/netbeans/project/ProjectCodeGeneratorTest.java`
- New test: `generatedSyntheticForEachLoopItemAccessSourceCompiles()`

## Test design

The test creates a synthetic Alice `Program` type with a user method equivalent to:

```java
void copyEach() {
  for (String item : new String[] {"red", "blue"}) {
    final String copy = item;
  }
}
```

Current generated output is characterized as:

```java
for(String COUNT__ : new String[]{"red", "blue"}) {
  final String copy=COUNT__;
}
```

The generated source compiles, so `COUNT__` is used consistently in the declaration and body reference.

## Local validation

Ran in `/home/azureuser/src/alice3-modernization`:

```bash
mvn -DincludeSims=false -Dinstall4j.skip -pl netbeans -am test \
  -Dtest=ProjectCodeGeneratorTest \
  -Dsurefire.failIfNoSpecifiedTests=false \
  -DfailIfNoTests=false
mvn -DincludeSims=false -Dinstall4j.skip clean test
mvn checkstyle:check -Dcheckstyle.config.location=checkstyle.xml
```

Result: all local gates passed. `ProjectCodeGeneratorTest` now reports 21 tests.

## CI validation

All workflows passed for source commit `761d4da5e26219fc1d5a5f30f1421a7862573b78`:

| Workflow | Run ID | Result |
| --- | ---: | --- |
| Alice Test CI | 25275734042 | success |
| Alice NetBeans Package CI | 25275734038 | success |
| Alice Checkstyle CI | 25275734035 | success |

## What this proves

- The Java export path emits foreach-array source that compiles even when the loop item is referenced in the body.
- The generated loop item name `COUNT__` is internally coherent.

## What this does not prove yet

- Runtime execution of foreach loops.
- Iterable foreach loops.
- Whether generated variable naming is acceptable for teaching/readability.

## Crusty proxy note

This downgrades `COUNT__` from “maybe correctness bug” to “readability debt.” That still matters for Alice, because exported Java is part of the teaching story, but it should be fixed after stronger characterization around named locals and student-visible generated source.
