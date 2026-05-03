# Alice submodule working guide

## Purpose

Alice 3 currently uses a required git submodule for the Tweedle language grammar. Every source checkout and every isolated worktree used for implementation lanes must initialize that submodule before broad Maven builds or any module path that reaches `core/tweedle`.

## Active submodule

| Path | Purpose | Required by |
| --- | --- | --- |
| `tweedle-lang` | Tweedle grammar and language assets | `core/tweedle` parser generation |

The important grammar inputs are:

- `tweedle-lang/Grammar/TweedleLexer.g4`
- `tweedle-lang/Grammar/TweedleParser.g4`

`core/tweedle/pom.xml` points the ANTLR Maven plugin at `../../tweedle-lang/Grammar` and generates Java parser sources under:

```text
core/tweedle/target/generated-sources/antlr4/org/alice/tweedle
```

## Required setup

For a fresh clone:

```bash
git clone --recurse-submodules https://github.com/rysweet/alice3-modernization.git
```

For an existing checkout or worktree:

```bash
cd /path/to/alice3-modernization
git submodule update --init --recursive
```

For an isolated worktree lane, run the same command in that worktree before broad validation:

```bash
cd /home/azureuser/src/alice3-modernization-worktrees/<lane>
git submodule update --init tweedle-lang
```

## Failure mode

If `tweedle-lang` is not initialized, Maven builds that reach `core/tweedle` can fail with missing generated parser classes such as:

```text
cannot find symbol: class TweedleParser
cannot find symbol: class TweedleParserBaseVisitor
```

This is usually not a source-code regression. First check:

```bash
git submodule status
test -d tweedle-lang/Grammar && echo "grammar present"
```

If the grammar is missing, initialize the submodule and rerun the validation command.

## Working-tree rule

Do not assume submodules initialized in the main checkout are present in a separate worktree. Each worktree has its own working directory and may need:

```bash
git submodule update --init tweedle-lang
```

This was confirmed during Loop 63: a recovery branch initially looked broken because `core/tweedle` generated parser classes were missing, but validation passed after initializing `tweedle-lang` in that worktree.
