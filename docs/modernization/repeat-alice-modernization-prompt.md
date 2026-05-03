# Repeat prompt: Alice modernization investigation and implementation

Use this prompt to repeat the Alice modernization exercise in a fresh agent session.

```text
We are going to work on and improve the Alice programming environment and tools:
https://www.alice.org/

Primary objective:
Establish a complete, trustworthy characterization and modernization path for Alice 3. The current Alice code is well documented through references, examples, and website material, but has few tests and is poorly organized. The goal is to make the codebase easier to learn, maintain, teach, evolve, and extend for future generations, including future AI-assisted experiences.

Repository and artifact requirements:
1. Use two separate repositories:
   - A public source repository/fork for Alice code work.
   - A private repository named `drinkme` for investigation artifacts, plans, journals, code atlases, graphs, prompts, summaries, and documentation.
2. Keep source code changes out of `drinkme`.
3. Keep investigation/planning artifacts out of the source repository unless they are directly required by the codebase.
4. Do not open upstream issues or pull requests.
5. Do not use the upstream issue database.
6. Make sure every subagent, helper, and workflow receives the same no-upstream/no-issues/no-PRs instruction.
7. If necessary, use a standalone repo that preserves history but prevents accidental upstream issue/PR usage.

Initial investigation requirements:
1. Make a detailed map of the Alice website and reference material.
2. Memorize and preserve important aspects of the website, references, examples, tutorials, build docs, and teaching material in `drinkme`.
3. Make or use the appropriate public Alice source fork/repo.
4. Install all dependencies required to build, test, package, and run Alice as a user would.
5. Deep dive into the code using code mapping, graphing, code-atlas, subagents, and other investigation techniques.
6. Keep a journal of key things learned at each stage.
7. Cross-check findings rather than assuming.
8. Store analysis, plans, code atlas outputs, graphs, and related artifacts in the private `drinkme` repo.
9. Include a complete documentation tour of the existing code and a documentation guide to the envisioned future code.

Testing and characterization requirements:
1. Build a comprehensive characterization test suite for current Alice behavior.
2. The current code must pass the characterization suite.
3. Continue expanding tests until functionality is modeled thoroughly.
4. Strive for test coverage above 70%.
5. Use multiple levels of quality audit.
6. Use code-atlas as a bug-hunting technique, but record findings in `drinkme`; do not file upstream issues.
7. Use QA-team style testing.
8. Build and test things like a user would, including UI/end-to-end approaches such as Playwright where appropriate.
9. Consider Gherkin and TLA+ where they help define behavior or prove correctness.
10. Prefer small, deterministic, provenance-clean fixtures. Avoid committing nonfree or unclear-origin binary assets.

Modernization and refactoring requirements:
1. Do not refactor blindly. Characterize behavior first.
2. After characterization, proceed with clean refactoring of the most important targets.
3. Preserve full compatibility with the current Alice version.
4. Strive for all classes to be under 500 lines.
5. Improve organization, maintainability, learnability, and teachability.
6. Decide between wholesale rewrite and targeted incremental refactor based on evidence.
7. Investigate whether Alice should remain all Java or whether portions would benefit from Rust or other languages.
8. For now, keep core runtime/application behavior in Java unless evidence strongly supports otherwise; consider Rust or other languages first for optional tooling, analysis, packaging, or external helpers.
9. Keep a current plan and journal after every slice of work.

Proxy/review requirements:
1. Use the crusty-old-engineer skill/persona as my proxy.
2. Iterate in a loop until the crusty-old-engineer proxy is satisfied with the work.
3. Each time you think the task is complete, re-check whether tests cover everything and whether all refactoring/modernization goals are actually met.
4. Do not claim completion prematurely.
5. The modernization task is not complete until all tests, modernization, quality, compatibility, documentation, and refactoring work are complete.

Execution loop:
1. Work autonomously and independently.
2. Pick the highest-value unprotected behavior or maintainability issue.
3. Add or strengthen characterization tests.
4. Fix correctness bugs only when the tests expose or protect the behavior.
5. Refactor only when protected by tests.
6. Run the relevant local gates.
7. Push source changes to the Alice modernization source repo.
8. Verify CI.
9. Update `drinkme` with the journal, plan changes, evidence, known limits, and next steps.
10. Repeat.

Current preferred gates:
1. `mvn -DincludeSims=false -Dinstall4j.skip -pl netbeans -am test`
2. `mvn -DincludeSims=false -Dinstall4j.skip clean test`
3. `mvn checkstyle:check -Dcheckstyle.config.location=checkstyle.xml`
4. NetBeans package gate:
   `mvn -DincludeSims=false -Dinstall4j.skip -pl netbeans -am package -DskipTests`

Important behavioral constraints:
1. Never push to upstream.
2. Never open upstream issues or PRs.
3. Never use the upstream issue database.
4. Preserve compatibility with current Alice behavior.
5. Treat generated Java export behavior as teaching-facing and compatibility-sensitive.
6. Prefer evidence over assumptions.
7. Keep source and artifact repos clean and pushed after each completed slice.
```

