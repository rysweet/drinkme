from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]

README = ROOT / "README.md"
CURRENT_STATE = ROOT / "docs/modernization/current-state-and-next-steps.md"
RESTARTED_STATUS = ROOT / "docs/modernization/restarted-full-scope-status.md"
ATLAS_INDEX = ROOT / "docs/atlas/index.md"
ENTRY_0130 = ROOT / "docs/atlas/journal/0130-rabbithole-306-308-evidence-status.md"

LINKED_DOCS = {
    "README": README,
    "current state": CURRENT_STATE,
    "restarted status": RESTARTED_STATUS,
    "atlas index": ATLAS_INDEX,
    "latest evidence journal": ENTRY_0130,
}

USER_FACING_DOCS = {
    "README": README,
    "current state": CURRENT_STATE,
    "restarted status": RESTARTED_STATUS,
    "atlas index": ATLAS_INDEX,
}

README_REQUIRED_HEADINGS = [
    "# drinkme",
    "## Plan summary",
    "## How the work runs",
    "## Current verdict",
    "## One-page project map",
    "## What works now",
    "## What is partly working",
    "## What is still missing",
    "## Current focus",
    "## Progress at a glance",
    "## Useful links",
    "## Where to go next",
]

README_REQUIRED_LINK_TARGETS = [
    "docs/plan.md",
    "docs/modernization/current-state-and-next-steps.md",
    "docs/modernization/restarted-full-scope-status.md",
    "docs/eatme/implementation-plan.md",
    "docs/atlas/index.md",
    "docs/atlas/diagrams/repo-surface-mermaid.svg",
    "docs/atlas/diagrams/repo-surface.mmd",
    "docs/atlas/diagrams/startup-flow-mermaid.svg",
    "docs/atlas/diagrams/startup-flow.mmd",
    "docs/atlas/diagrams/testing-roadmap-mermaid.svg",
    "docs/atlas/diagrams/testing-roadmap.mmd",
]

SYNTHESIZED_STATUS_TERMS = [
    "automation scenarios",
    "linked status docs",
    "remaining gaps",
    "full Alice UI automation",
    "visible rendering",
    "desktop Save menu-to-written-project completion",
    "first-lesson completion",
    "grading",
    "creative assessment",
    "full Tweedle/player decode",
]

REMAINING_GAPS = [
    "full Alice UI automation",
    "visible rendering",
    "desktop Save menu-to-written-project completion",
    "first-lesson completion",
    "grading",
    "creative assessment",
    "full Tweedle/player decode",
]

FORBIDDEN_READER_JARGON = [
    "Gadugi",
    "smoke",
    "RabbitHole/eatme wave",
    "automation-scenario",
]

FORBIDDEN_OVERCLAIMS = [
    "Alice UI automation is complete",
    "visible rendering correctness is proven",
    "desktop Save completion is done",
    "grading works",
    "creative assessment works",
    "first-lesson completion is complete",
    "full Tweedle/player decode is complete",
    "70% aggregate coverage is complete",
    "70 percent aggregate coverage is complete",
]

MARKDOWN_LINK_RE = re.compile(r"!?\[[^\]]+\]\((?P<target>[^)#]+)(?:#[^)]+)?\)")
PLAIN_WHITESPACE_RE = re.compile(r"\s+")
MARKDOWN_LINK_TARGET_RE = re.compile(r"\[(?P<label>[^\]]+)\]\([^)]+\)")


def plain(text):
    return PLAIN_WHITESPACE_RE.sub(" ", text.replace("**", " "))


def without_markdown_link_targets(text):
    return MARKDOWN_LINK_TARGET_RE.sub(lambda match: match.group("label"), text)


def section(text, heading):
    pattern = re.compile(
        rf"^## {re.escape(heading)}\n(?P<body>.*?)(?=^## |\Z)",
        re.MULTILINE | re.DOTALL,
    )
    match = pattern.search(text)
    if not match:
        raise AssertionError(f"Missing section: {heading}")
    return match.group("body")


class DesktopRunDocsContractTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.docs = {
            name: path.read_text(encoding="utf-8")
            for name, path in LINKED_DOCS.items()
        }

    def assert_contains_all(self, text, expected, source):
        missing = [term for term in expected if term not in text]
        self.assertEqual([], missing, f"{source} is missing expected terms")

    def assert_no_pr_dump(self, text, source, max_pr_mentions):
        pr_mentions = re.findall(r"\bPR\s*#\d+", without_markdown_link_targets(text))
        self.assertLessEqual(
            len(pr_mentions),
            max_pr_mentions,
            f"{source} should summarize status instead of listing PR chronology",
        )

        pr_table_rows = [
            row
            for row in text.splitlines()
            if row.strip().startswith("|") and re.search(r"\bPR\s*#?\d+|\bpull/\d+", row)
        ]
        self.assertEqual([], pr_table_rows, f"{source} should not contain PR table rows")

    def assert_user_facing_status_is_plain(self, text, source):
        prose = without_markdown_link_targets(text)
        for term in FORBIDDEN_READER_JARGON:
            self.assertNotRegex(
                prose,
                rf"(?i)\b{re.escape(term)}\b",
                f"{source} uses avoidable internal or test jargon: {term}",
            )
        for claim in FORBIDDEN_OVERCLAIMS:
            self.assertNotIn(claim.lower(), plain(prose).lower())
        self.assertNotRegex(
            prose,
            r"(?i)\bunproven\b|\bproven\b",
            f"{source} should not use Proven/proven as user-facing status wording",
        )

    def test_user_facing_docs_use_plain_status_language(self):
        for name, path in USER_FACING_DOCS.items():
            with self.subTest(document=name):
                self.assert_user_facing_status_is_plain(
                    path.read_text(encoding="utf-8"),
                    name,
                )

    def test_readme_is_concise_linked_and_diagram_preserving(self):
        readme = self.docs["README"]
        prose = without_markdown_link_targets(readme)

        self.assert_contains_all(readme, README_REQUIRED_HEADINGS, "README")
        self.assert_contains_all(readme, README_REQUIRED_LINK_TARGETS, "README links")
        self.assertIn("This README is a project overview, not a changelog.", readme)
        self.assertIn("automation scenario coverage", readme)
        self.assertIn("Use drinkme as a map and status index.", readme)
        self.assertIn("python3 -m unittest discover -s tests -v", readme)
        self.assertGreaterEqual(readme.count("```mermaid"), 3)
        self.assertLessEqual(len(readme.splitlines()), 170)
        self.assert_no_pr_dump(readme, "README", max_pr_mentions=0)
        self.assertNotIn("RabbitHole", prose)
        self.assertNotIn("eatme", prose)
        self.assert_user_facing_status_is_plain(readme, "README")

    def test_current_state_summarizes_automation_status_not_pr_chronology(self):
        text = self.docs["current state"]
        opening_status = section(text, "Repository state")

        self.assert_contains_all(
            plain(opening_status).lower(),
            [term.lower() for term in SYNTHESIZED_STATUS_TERMS],
            "current state",
        )
        self.assertIn("### What works now", text)
        self.assertIn("### What is partly working", text)
        self.assertIn("### What is still missing", text)
        self.assert_contains_all(
            plain(text).lower(),
            [term.lower() for term in REMAINING_GAPS],
            "current state remaining gaps",
        )
        self.assert_no_pr_dump(opening_status, "current state opening status", max_pr_mentions=0)
        self.assert_user_facing_status_is_plain(opening_status, "current state opening status")

    def test_restarted_status_tracks_capabilities_not_release_log(self):
        text = self.docs["restarted status"]
        prose = without_markdown_link_targets(text)

        self.assertIn("## Current status by capability", text)
        self.assertIn("## What changed after automation scenarios were integrated", text)
        self.assertIn("## Latest integrated evidence", text)
        self.assertIn("## Remaining gaps", text)
        self.assert_contains_all(
            plain(text).lower(),
            [term.lower() for term in SYNTHESIZED_STATUS_TERMS],
            "restarted status",
        )
        self.assert_contains_all(plain(section(text, "Remaining gaps")), REMAINING_GAPS, "restarted gaps")
        self.assert_no_pr_dump(text, "restarted status", max_pr_mentions=0)
        self.assertNotIn("Latest merged source/eatme wave links", text)
        self.assertNotIn("Latest RabbitHole source/CI wave details", text)
        self.assertNotIn("Evidence detail ledger", text)
        self.assert_user_facing_status_is_plain(prose, "restarted status")

    def test_atlas_index_is_overview_with_bounded_journal_links(self):
        text = self.docs["atlas index"]

        self.assertIn("## Current diagrams", text)
        self.assertIn("## Current status summary", text)
        self.assertIn("## Evidence history", text)
        self.assertGreaterEqual(text.count("![Repo surface"), 2)
        self.assertGreaterEqual(text.count("![Startup flow"), 2)
        self.assertGreaterEqual(text.count("![Testing roadmap"), 2)
        self.assert_contains_all(
            plain(text).lower(),
            [term.lower() for term in SYNTHESIZED_STATUS_TERMS],
            "atlas index",
        )
        self.assertLessEqual(text.count("journal/"), 8)
        self.assert_no_pr_dump(text, "atlas index", max_pr_mentions=0)
        self.assert_user_facing_status_is_plain(text, "atlas index")

    def test_latest_evidence_journal_remains_bounded_history(self):
        text = self.docs["latest evidence journal"]
        plain_text = plain(text)

        self.assertIn("model export attribution evidence", plain_text)
        self.assertIn("generated story runtime-state evidence", plain_text)
        self.assertIn("Runtime-state evidence collected without opening the desktop UI only", text)
        self.assertIn(
            "does not prove visible rendering, JavaFX launch, animation playback, "
            "full world execution, grading, full UI automation, full lesson "
            "completion, or full Tweedle/player decode",
            plain_text,
        )
        self.assert_no_pr_dump(text, "latest evidence journal", max_pr_mentions=0)
        self.assertNotRegex(plain_text, r"(?i)\bproven\b")

    def test_linked_docs_keep_internal_markdown_links_valid(self):
        for name, path in LINKED_DOCS.items():
            text = self.docs[name]
            for match in MARKDOWN_LINK_RE.finditer(text):
                target = match.group("target")
                if re.match(r"^[a-z][a-z0-9+.-]*:", target) or target.startswith("#"):
                    continue
                with self.subTest(document=name, target=target):
                    self.assertTrue((path.parent / target).resolve().exists())


if __name__ == "__main__":
    unittest.main()
