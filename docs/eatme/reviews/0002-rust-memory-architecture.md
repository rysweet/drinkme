# Eatme review 0002: Rust and memory architecture

## Findings

- `/home/azureuser/src/eatme` is a new empty private repo.
- The real Alice modernization source tree is `/home/azureuser/src/alice3-modernization` (`rysweet/alice3-modernization`, branch `develop`).
- `/home/azureuser/src/alice` is not the active Alice source tree.
- `amplihack-memory-lib` exists locally at `/home/azureuser/src/amplihack-fix/amplihack-memory-lib`.
- A Rust memory crate exists at `/home/azureuser/src/amplihack-rs/crates/amplihack-memory`.
- `gadugi-agentic-test` exists locally at `/home/azureuser/src/gadugi-agentic-test`; the built CLI is `dist/cli.js`.

## Recommended Rust workspace

```text
eatme/
├── Cargo.toml
├── crates/
│   ├── eatme-cli/          # clap CLI only
│   ├── eatme-core/         # shared types, errors, config, process traits
│   ├── eatme-assets/       # load/validate personas/prompts/scenarios
│   ├── eatme-personas/     # persona + prompt rendering
│   ├── eatme-alice/        # real Alice fork discovery/build/test wrappers
│   ├── eatme-gadugi/       # gadugi-agentic-test adapter
│   ├── eatme-memory/       # memory trait + adapters
│   ├── eatme-report/       # junit/json/markdown summaries
│   └── eatme-test-support/ # fake process runner, fixtures
├── assets/
├── tests/
└── scripts/
```

## Rules

- No Rust source file over 500 lines.
- `lib.rs` files should only re-export modules.
- All shell, Maven, and gadugi execution goes through an injectable `CommandRunner` trait so tests can use deterministic fakes.
- Alice remains Java/Maven. Moving Alice itself to Rust is not justified by current evidence.
- Rust should orchestrate, validate, index artifacts, bind memory, and report.

## Editable asset layout

```text
assets/
├── personas/
├── prompts/
├── scenarios/
│   ├── gadugi/
│   └── eatme/
├── rubrics/
└── alice/
```

Rust validates these assets. It must not hard-code persona text, prompts, scenario steps, or Alice paths.

## Memory binding strategy

Start with a small Rust trait:

```rust
trait MemoryStore {
    fn remember(&self, event: MemoryEvent) -> Result<MemoryId>;
    fn recall(&self, query: MemoryQuery) -> Result<Vec<MemoryHit>>;
}
```

Adapters:

1. `NoopMemoryStore` for deterministic tests.
2. `JsonlMemoryStore` under `.eatme/memory/events.jsonl`.
3. Optional `AmplihackRustMemoryStore` using `/home/azureuser/src/amplihack-rs/crates/amplihack-memory`.
4. Optional Python sidecar only if the richer Python/Kuzu graph model is needed.

Memory should store scenario outcomes, Alice failures, successful fixes, persona effectiveness, recurring diagnostics, and resource coverage.

## Test and coverage approach

The 70% coverage target applies to the Rust workspace, not to Alice itself.

Recommended commands:

```bash
cargo fmt --check
cargo clippy --workspace --all-targets --all-features -- -D warnings
cargo test --workspace --all-features
cargo llvm-cov --workspace --all-features --fail-under-lines 70
```

Real Alice tests should be gated:

```bash
EATME_REAL_ALICE=1 ALICE_HOME=/home/azureuser/src/alice3-modernization cargo test --test real_alice
```

Line guard:

```bash
find crates -name '*.rs' -not -path '*/target/*' -exec wc -l {} + \
  | awk '$1 > 500 { print; bad=1 } END { exit bad }'
```

## Initial CLI surface

```bash
eatme assets validate
eatme personas render --persona alice-teacher --prompt analyze-alice-build
eatme alice discover --alice-home /home/azureuser/src/alice3-modernization
eatme alice verify --alice-home /home/azureuser/src/alice3-modernization --no-sims
eatme gadugi validate --dir assets/scenarios/gadugi
eatme gadugi run --scenario alice-no-sims-smoke
eatme memory recall "netbeans compile failure"
eatme report summarize --format markdown
```

## Keep as YAML/Markdown

- Personas
- Prompt templates
- Gadugi scenarios
- Alice fork/profile definitions
- Evaluation rubrics
- User journeys
- Memory retention policy
- Report wording/templates
