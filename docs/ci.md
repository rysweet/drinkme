# Docs CI lane

The `drinkme` repository has a small GitHub Actions CI lane for documentation and status artifacts. It validates repository hygiene only; it does not run application unit tests, build an application, publish docs, or install project dependencies.

The workflow lives at [`.github/workflows/ci.yml`](../.github/workflows/ci.yml) and runs the `Repository validation` job on `ubuntu-latest`.

## When CI runs

CI runs automatically for:

- every pull request targeting the repository; and
- every push to `main`.

The workflow uses read-only repository permissions (`contents: read`) and checks only tracked files. Untracked local files, editor scratch files, and session artifacts do not affect CI.

## What CI validates

### Repository shape

The repository is treated as a docs/status repository. CI requires:

- `README.md` at the repository root;
- a `docs/` directory; and
- Markdown files only in `README.md` or under `docs/`.

Put new documentation under `docs/` unless it is the root README.

### JSON syntax

Every tracked `*.json` file must parse as valid JSON with the Python standard library. JSON Lines files are not included because they use the `*.jsonl` extension.

### YAML syntax

Every tracked `*.yml` and `*.yaml` file must parse as valid YAML. This includes the CI workflow itself.

### Internal Markdown links

CI checks local relative links and image references in tracked Markdown files. A link fails CI when it:

- points to a missing file or directory;
- resolves outside the repository root; or
- uses a malformed local file path.

CI intentionally skips:

- external URLs such as `https://...`;
- non-file schemes such as `mailto:` and `ssh:`;
- pure same-page anchors such as `#artifact-map`; and
- network availability checks.

The link check focuses on local file existence. It does not validate that a GitHub heading anchor exists inside a target Markdown file.

## Local usage

Before opening a pull request, run checks that match the CI intent with standard shell tools. The YAML command requires Ruby; the GitHub Actions runner provides it.

```bash
test -f README.md
test -d docs
git ls-files '*.md' | awk '$0 != "README.md" && $0 !~ /^docs\// { print }'
git ls-files '*.json' | xargs -r -n1 python3 -m json.tool >/dev/null
ruby -e 'require "yaml"; ARGV.each { |file| YAML.load_file(file) }' -- $(git ls-files '*.yml' '*.yaml')
```

For Markdown links, use the pull request CI result as the source of truth. The workflow performs path normalization, URL decoding, fragment/query stripping, repository-boundary checks, and missing-target reporting.

## Adding documentation safely

1. Create or edit Markdown under `docs/`.
2. Use relative links for repository-local references, for example `[CI lane](ci.md)` from another file in `docs/`.
3. Use root-relative repository paths only in prose or code spans, not as Markdown links.
4. Keep generated artifacts tracked only when they are intended repository artifacts.
5. Open a pull request and wait for the `Repository validation` check to pass.

## Configuration

The CI lane has no project-specific dependency configuration. It relies on tools available on `ubuntu-latest`: Bash, Git, Python 3, and Ruby.

Change the workflow only when the repository contract changes. Examples of valid workflow changes include allowing another documentation directory, adding another syntax-only file validator, or tightening local link validation. Do not add fake unit tests or package-manager setup unless the repository gains real code or real package tooling.

## API surface

This feature has no runtime API. Its public interface is the GitHub Actions workflow result on pull requests and pushes to `main`.
