import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
WORKFLOW_PATH = REPO_ROOT / ".github" / "workflows" / "ci.yml"
WORKFLOW_TEXT = WORKFLOW_PATH.read_text(encoding="utf-8")
WORKFLOW_LINES = WORKFLOW_TEXT.splitlines()


class WorkflowContractTests(unittest.TestCase):
    def test_workflow_runs_on_pull_requests_and_pushes_to_main(self):
        self.assertIn("on:\n  pull_request:\n  push:\n    branches:\n      - main", WORKFLOW_TEXT)

    def test_workflow_uses_read_only_permissions(self):
        self.assertIn("permissions:\n  contents: read", WORKFLOW_TEXT)

    def test_repository_validation_job_uses_ubuntu_latest(self):
        self.assertIn("repository-validation:", WORKFLOW_TEXT)
        self.assertIn("name: Repository validation", WORKFLOW_TEXT)
        self.assertIn("runs-on: ubuntu-latest", WORKFLOW_TEXT)

    def test_workflow_checks_out_repository_with_current_checkout_action(self):
        self.assertIn("uses: actions/checkout@v4", WORKFLOW_TEXT)

    def test_workflow_runs_this_test_suite_before_validation_gates(self):
        self.assertIn("name: Run CI workflow tests", WORKFLOW_TEXT)
        self.assertIn("python3 -m unittest discover -s tests -v", WORKFLOW_TEXT)
        self.assertLess(
            WORKFLOW_TEXT.index("name: Run CI workflow tests"),
            WORKFLOW_TEXT.index("name: Validate repository artifacts"),
        )


class WorkflowScriptTests(unittest.TestCase):
    def test_repository_shape_accepts_docs_repository(self):
        with tracked_repo(
            {
                "README.md": "# Example\n",
                "docs/index.md": "# Docs\n",
            }
        ) as repo:
            result = run_step("Validate repository artifacts", repo)

        self.assertEqual(result.returncode, 0, result.stderr)

    def test_repository_shape_rejects_markdown_outside_readme_or_docs(self):
        with tracked_repo(
            {
                "README.md": "# Example\n",
                "NOTES.md": "# Wrong place\n",
                "docs/index.md": "# Docs\n",
            }
        ) as repo:
            result = run_step("Validate repository artifacts", repo)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Markdown files must live in README.md or docs/", result.stderr)
        self.assertIn("NOTES.md", result.stderr)

    def test_repository_shape_handles_newlines_in_tracked_markdown_paths(self):
        with tracked_repo(
            {
                "README.md": "# Example\n",
                "docs/index.md": "# Docs\n",
                "docs/linked\nfile.md": "# Odd path\n",
            }
        ) as repo:
            result = run_step("Validate repository artifacts", repo)

        self.assertEqual(result.returncode, 0, result.stderr)

    def test_json_validation_accepts_json_and_ignores_json_lines(self):
        with tracked_repo(
            {
                "README.md": "# Example\n",
                "docs/index.md": "# Docs\n",
                "docs/valid.json": '{"ok": true}\n',
                "docs/events.jsonl": '{"ok": true}\nnot-json\n',
            }
        ) as repo:
            result = run_step("Validate repository artifacts", repo)

        self.assertEqual(result.returncode, 0, result.stderr)

    def test_json_validation_rejects_invalid_tracked_json(self):
        with tracked_repo(
            {
                "README.md": "# Example\n",
                "docs/index.md": "# Docs\n",
                "docs/broken.json": '{"missing": }\n',
            }
        ) as repo:
            result = run_step("Validate repository artifacts", repo)

        self.assertNotEqual(result.returncode, 0)

    @unittest.skipUnless(shutil.which("ruby"), "Ruby is required for workflow YAML validation")
    def test_yaml_validation_accepts_valid_yaml(self):
        with tracked_repo(
            {
                "README.md": "# Example\n",
                "docs/index.md": "# Docs\n",
                ".github/workflows/example.yml": "name: Example\non:\n  push:\n",
            }
        ) as repo:
            result = run_step("Validate YAML syntax", repo)

        self.assertEqual(result.returncode, 0, result.stderr)

    @unittest.skipUnless(shutil.which("ruby"), "Ruby is required for workflow YAML validation")
    def test_yaml_validation_rejects_invalid_yaml(self):
        with tracked_repo(
            {
                "README.md": "# Example\n",
                "docs/index.md": "# Docs\n",
                ".github/workflows/broken.yml": "name: Broken\ninvalid: [\n",
            }
        ) as repo:
            result = run_step("Validate YAML syntax", repo)

        self.assertNotEqual(result.returncode, 0)

    def test_markdown_link_validation_accepts_existing_local_targets(self):
        with tracked_repo(
            {
                "README.md": "[Docs](docs/index.md)\n",
                "docs/index.md": (
                    "[Guide](guide.md)\n"
                    "[Extensionless](guide)\n"
                    "[Directory](assets)\n"
                    "![Image](assets/logo.svg)\n"
                    "[Reference]: guide.md\n"
                ),
                "docs/guide.md": "# Guide\n",
                "docs/assets/logo.svg": "<svg />\n",
            }
        ) as repo:
            result = run_step("Validate repository artifacts", repo)

        self.assertEqual(result.returncode, 0, result.stderr)

    def test_markdown_link_validation_ignores_untracked_local_targets(self):
        with tracked_repo(
            {
                "README.md": "[Untracked](docs/untracked.md)\n",
                "docs/index.md": "# Docs\n",
            },
            untracked_files={
                "docs/untracked.md": "# Local only\n",
            },
        ) as repo:
            result = run_step("Validate repository artifacts", repo)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("missing target", result.stderr)
        self.assertIn("docs/untracked.md", result.stderr)

    def test_markdown_link_validation_rejects_missing_targets(self):
        with tracked_repo(
            {
                "README.md": "[Missing](docs/missing.md)\n",
                "docs/index.md": "# Docs\n",
            }
        ) as repo:
            result = run_step("Validate repository artifacts", repo)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Repository validation failed", result.stderr)
        self.assertIn("missing target", result.stderr)
        self.assertIn("docs/missing.md", result.stderr)

    def test_markdown_link_validation_rejects_repository_escape(self):
        with tracked_repo(
            {
                "README.md": "[Escape](../outside.md)\n",
                "docs/index.md": "# Docs\n",
            }
        ) as repo:
            result = run_step("Validate repository artifacts", repo)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("link escapes repository", result.stderr)

    def test_markdown_link_validation_skips_external_links_and_pure_anchors(self):
        with tracked_repo(
            {
                "README.md": (
                    "[Web](https://example.test/missing.md)\n"
                    "[Mail](mailto:person@example.test)\n"
                    "[Network](//example.test/missing.md)\n"
                    "[Anchor](#local-heading)\n"
                ),
                "docs/index.md": "# Docs\n",
            }
        ) as repo:
            result = run_step("Validate repository artifacts", repo)

        self.assertEqual(result.returncode, 0, result.stderr)

    def test_markdown_link_validation_url_decodes_paths_and_ignores_fragments(self):
        with tracked_repo(
            {
                "README.md": "[Spaced](docs/spaced%20name.md#section)\n",
                "docs/index.md": "# Docs\n",
                "docs/spaced name.md": "# Spaced\n",
            }
        ) as repo:
            result = run_step("Validate repository artifacts", repo)

        self.assertEqual(result.returncode, 0, result.stderr)

    def test_markdown_link_validation_checks_angle_wrapped_paths_with_spaces(self):
        with tracked_repo(
            {
                "README.md": "[Missing](<docs/missing file.md>)\n",
                "docs/index.md": "# Docs\n",
            }
        ) as repo:
            result = run_step("Validate repository artifacts", repo)

        self.assertNotEqual(result.returncode, 0)
        self.assertIn("missing target", result.stderr)
        self.assertIn("docs/missing file.md", result.stderr)

    def test_markdown_link_validation_handles_newlines_in_tracked_markdown_paths(self):
        with tracked_repo(
            {
                "README.md": "[Odd path](docs/linked%0Afile.md)\n",
                "docs/index.md": "# Docs\n",
                "docs/linked\nfile.md": "# Odd path\n",
            }
        ) as repo:
            result = run_step("Validate repository artifacts", repo)

        self.assertEqual(result.returncode, 0, result.stderr)


def workflow_step_script(step_name):
    marker = f"      - name: {step_name}"

    try:
        step_start = WORKFLOW_LINES.index(marker)
    except ValueError as exc:
        raise AssertionError(f"Missing workflow step: {step_name}") from exc

    try:
        run_line = next(
            index
            for index in range(step_start + 1, len(WORKFLOW_LINES))
            if WORKFLOW_LINES[index] == "        run: |"
        )
    except StopIteration as exc:
        raise AssertionError(f"Workflow step has no run block: {step_name}") from exc

    script_lines = []
    for line in WORKFLOW_LINES[run_line + 1 :]:
        if line.startswith("      - name: "):
            break
        if line.startswith("          "):
            script_lines.append(line[10:])
        elif line == "":
            script_lines.append("")
        else:
            break

    return "\n".join(script_lines).rstrip() + "\n"


def run_step(step_name, cwd):
    script = workflow_step_script(step_name)
    return subprocess.run(
        ["bash", "-c", script],
        cwd=cwd,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


class tracked_repo:
    def __init__(self, files, untracked_files=None):
        self.files = files
        self.untracked_files = untracked_files or {}
        self._temporary_directory = tempfile.TemporaryDirectory()
        self.path = Path(self._temporary_directory.name)

    def __enter__(self):
        subprocess.run(["git", "init", "--quiet"], cwd=self.path, check=True)
        for relative_path, content in self.files.items():
            file_path = self.path / relative_path
            file_path.parent.mkdir(parents=True, exist_ok=True)
            file_path.write_text(content, encoding="utf-8")
        subprocess.run(["git", "add", "."], cwd=self.path, check=True)
        for relative_path, content in self.untracked_files.items():
            file_path = self.path / relative_path
            file_path.parent.mkdir(parents=True, exist_ok=True)
            file_path.write_text(content, encoding="utf-8")
        return self.path

    def __exit__(self, exc_type, exc_value, traceback):
        self._temporary_directory.cleanup()


if __name__ == "__main__":
    unittest.main()
