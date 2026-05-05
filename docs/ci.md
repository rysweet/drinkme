# Docs CI lane

The `drinkme` repository has a small GitHub Actions CI lane for documentation and status artifacts. It validates repository hygiene only; it does not run application unit tests, build an application, publish docs, or install project dependencies.

The workflow lives at [`.github/workflows/ci.yml`](../.github/workflows/ci.yml) and runs on every pull request plus every push to `main`.

## What CI validates

- `README.md` exists at the repository root.
- `docs/` exists, and tracked Markdown files live only in `README.md` or under `docs/`.
- Every tracked `*.json` file parses as JSON with the Python standard library.
- Every tracked `*.yml` and `*.yaml` file parses as YAML with Ruby Psych.
- Common internal Markdown links resolve to tracked files or directories without escaping the repository.

The link check intentionally skips external URLs, URL schemes such as `https` and `mailto`, network locations, same-page anchors, and heading-anchor validation inside Markdown files. It does not make network requests.

## Local usage

The workflow uses only tools available on `ubuntu-latest`: Bash, Git, Python 3, and Ruby. Use the pull request check as the source of truth when local tool versions differ.
