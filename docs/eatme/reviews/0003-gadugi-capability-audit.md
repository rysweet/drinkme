# Eatme review 0003: gadugi-agentic-test capability audit

## Summary

No gadugi changes were made. Missing desktop/Swing support is real but not a trivial isolated fix.

`gadugi-agentic-test` is useful for the `eatme` workstream, but Alice should not be forced into the existing Electron/TUI abstractions. The right move is an Alice-specific scenario schema in `eatme`, with an adapter to gadugi where current capabilities fit, and a later upstream proposal for a true desktop agent.

## Current gadugi capabilities

- TypeScript package: `@gadugi/agentic-test`.
- Exported agents include `ElectronUIAgent`, `CLIAgent`, `TUIAgent`, `APIAgent`, `WebSocketAgent`, `SystemAgent`, `ComprehensionAgent`, `PriorityAgent`, and `IssueReporter`.
- Orchestrator routes `CLI`, `TUI`, `GUI`, `API`, and `MIXED`.
- `GUI` currently means Electron through Playwright `_electron`.
- Evidence support already includes screenshots, screenshot diffs, state snapshots, command output buffers, TUI buffers, console logs, performance samples, websocket events, and result JSON.
- The comprehension agent can generate scenarios from docs, but that is currently pipeline-oriented.

## Gaps for Alice Swing/Java desktop

- No `DESKTOP` or `SWING` test interface.
- No DesktopAgent.
- Playwright cannot inspect Swing DOM/components.
- No Xvfb lifecycle support.
- No `DISPLAY` allocation.
- No root-window screenshot lifecycle.
- TUI support is not desktop support.
- `node-pty-prebuilt-multiarch` is missing locally, causing targeted TUI test import failure.
- Scenario adapter currently drops or weakens useful YAML fields.
- WebSocket agent is exported but not represented in `TestInterface` routing.
- GitHub failure reporting is incomplete.

## Recommended Alice scenario schema

Use an Alice-specific schema in `eatme`, then compile or adapt to gadugi where possible:

```yaml
id: alice-instructor-create-first-world
role: instructor
app: alice3
goal: "Create a world, add one object, run it, and verify the scene changes."
environment:
  aliceRepo: /home/azureuser/src/alice3-modernization
  buildCommand: "mvn -DincludeSims=false -Dinstall4j.skip package"
  launchCommand: "..."
  display:
    provider: xvfb
    size: "1920x1080x24"
    windowManager: openbox
agents:
  - id: desktop
    type: swing-desktop
    observation:
      screenshot: true
      accessibilityTree: optional
      componentTreeProbe: optional-internal-testing
      ocr: optional
  - id: comprehension
    type: alice-comprehension
steps:
  - intent: "Launch Alice"
    action: launch
    expect:
      visual_contains: ["Alice"]
      window_title_matches: "Alice.*"
evidence:
  required:
    - before_after_screenshots
    - action_log
    - process_log
    - final_observation_summary
```

## Evidence model

Each step should emit:

- timestamp
- scenario id
- role
- step id
- intent
- input event
- before/after screenshots with hashes
- window geometry and `DISPLAY`
- optional OCR text
- optional accessibility tree
- optional Swing component tree
- process PID/stdout/stderr/logs
- assertion result, confidence, and failure reason
- produced artifacts such as `.a3p` files, recordings, and diff images

Store each run as:

```text
runs/<scenario>/<timestamp>/manifest.json
```

## First implementation tasks

1. Initialize `eatme` as the Alice outside-in test harness repo.
2. Add an Alice scenario YAML schema and validator.
3. Implement `DesktopSession`: Xvfb startup, display export, window-manager startup, Java process lifecycle.
4. Implement `DesktopObserver`: root screenshot, window title/geometry, process logs, optional OCR/accessibility.
5. Implement `DesktopActor`: click, type, key chords, wait-for-visual-change.
6. Add one smoke scenario: launch Alice under Xvfb and capture evidence.
7. Add one instructor scenario and one student scenario.
8. Later propose gadugi `TestInterface.DESKTOP` and `DesktopAgent`.

## Files inspected

The audit inspected gadugi package metadata, scenario parsing, orchestrator routing, agent exports, Electron/TUI implementations, screenshot utilities, smart runners, docs, sample scenarios, and the Alice modernization README/pom/AGENTS files.
