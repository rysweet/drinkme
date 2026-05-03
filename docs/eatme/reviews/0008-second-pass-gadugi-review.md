# Eatme review 0008: second-pass gadugi review

## Verdict

The plan is directionally right, but the gadugi boundary must be sharper. Current gadugi should orchestrate `eatme` as a CLI/system harness, not own Swing/Xvfb/Desktop behavior.

## Required changes

1. Define the boundary explicitly:
   - `eatme` owns Alice packaging, Xvfb/display allocation, window manager, Java process lifecycle, screenshots, logs, run manifests, rubrics, persona assets, and memory namespace.
   - `gadugi` owns running `eatme` CLI commands, collecting stdout/stderr/result JSON, and evaluating manifest-level evidence.
   - `eatme-gadugi` owns compiling/adapting `eatme` scenarios into gadugi-compatible CLI/MIXED scenarios.

2. Do not put Swing desktop automation into gadugi integration yet:
   - no `DESKTOP`
   - no `SWING`
   - no Playwright GUI
   - no component trees
   - no OCR
   - no direct UI actions

3. Keep canonical editable scenarios in `assets/scenarios/eatme/`. Generate or validate gadugi-compatible scenarios under `assets/scenarios/gadugi/`.

4. Add deterministic CLI flags:
   - `--run-id`
   - `--runs-dir`
   - `--json`
   - `--timeout`
   - `--no-memory`

5. Manifest is the integration contract. Required fields:
   - `scenario_id`
   - `run_id`
   - `alice_home`
   - `display`
   - command status
   - process status
   - screenshot artifact path/size/hash
   - log artifact path/size/hash
   - assertion results
   - fatal error scan result

6. Add schema fields:
   - `schema_version`
   - `capabilities.required`
   - `capabilities.optional`
   - `adapter.targets`
   - `steps[].id`
   - `timeouts`
   - `artifacts`
   - `unsupported_policy`

7. Replace weak visual assertions. `visual_contains: ["Alice"]` is not deterministic unless OCR is explicitly available. First slice should use:
   - process alive
   - X display responsive
   - window title if `wmctrl` can see it
   - screenshot exists, non-empty, hash recorded
   - no fatal log patterns

## First gadugi-compatible scenario

Use gadugi as a CLI runner around `eatme`:

```yaml
schema_version: gadugi-agentic-test/v1
id: eatme-real-alice-launch-smoke
name: Eatme real Alice launch smoke
interface: CLI
working_directory: /home/azureuser/src/eatme
timeout_ms: 900000
environment:
  EATME_REAL_ALICE: "1"
  ALICE_HOME: /home/azureuser/src/alice3-modernization
steps:
  - id: validate-assets
    run: cargo run -q -p eatme-cli -- assets validate
  - id: discover-alice
    run: cargo run -q -p eatme-cli -- alice discover --alice-home "$ALICE_HOME" --json
  - id: launch-smoke
    run: >
      cargo run -q -p eatme-cli -- alice launch-smoke
      --alice-home "$ALICE_HOME"
      --run-id gadugi-real-alice-launch-smoke
      --runs-dir runs
      --json
      --timeout 120
  - id: verify-evidence
    run: >
      python3 -c 'import json, pathlib;
      p=pathlib.Path("runs/real-alice-launch-smoke/gadugi-real-alice-launch-smoke/manifest.json");
      m=json.loads(p.read_text());
      assert m["scenario_id"]=="real-alice-launch-smoke";
      assert m["assertions"]["process_started"]["passed"];
      assert m["assertions"]["display_responsive"]["passed"];
      assert m["assertions"]["startup_screenshot"]["passed"];
      assert m["assertions"]["no_fatal_logs"]["passed"]'
```

This keeps all desktop/Swing complexity inside `eatme`.
