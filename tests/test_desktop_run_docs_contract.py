from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]

README = ROOT / "README.md"
ATLAS_INDEX = ROOT / "docs/atlas/index.md"
ENTRY_0085 = ROOT / "docs/atlas/journal/0085-desktop-run-execution-evidence.md"
ROOT_PLAN = ROOT / "docs/plan.md"
CURRENT_STATE = ROOT / "docs/modernization/current-state-and-next-steps.md"
RESTARTED_STATUS = ROOT / "docs/modernization/restarted-full-scope-status.md"
EATME_PLAN = ROOT / "docs/eatme/implementation-plan.md"

CONTROL_DOCS = {
    "README": README,
    "root plan": ROOT_PLAN,
    "current modernization plan": CURRENT_STATE,
    "restarted full-scope status": RESTARTED_STATUS,
    "eatme implementation plan": EATME_PLAN,
    "atlas entry 0085": ENTRY_0085,
}

DOCS = {
    **CONTROL_DOCS,
    "atlas index": ATLAS_INDEX,
}

README_PLAN_LINKS = [
    "[root investigation plan](docs/plan.md)",
    "[current modernization plan](docs/modernization/current-state-and-next-steps.md)",
    "[restarted full-scope status](docs/modernization/restarted-full-scope-status.md)",
    "[eatme implementation plan](docs/eatme/implementation-plan.md)",
    "[atlas journal entry 0085](docs/atlas/journal/0085-desktop-run-execution-evidence.md)",
]

ENTRY_TRACEABILITY_LINKS = [
    "[drinkme status](../../../README.md)",
    "[root investigation plan](../../plan.md)",
    "[current modernization plan](../../modernization/current-state-and-next-steps.md)",
    "[eatme implementation plan](../../eatme/implementation-plan.md)",
]

REQUIRED_PR_LINKS = [
    "https://github.com/rysweet/RabbitHole/pull/154",
    "https://github.com/rysweet/RabbitHole/pull/155",
    "https://github.com/rysweet/RabbitHole/pull/156",
    "https://github.com/rysweet/eatme/pull/89",
]

PROOF_BOUNDARY_TERMS = [
    "narrow Run window attachment signal",
    "Alice put the Run panel into the Run window area",
    "does not prove pixels were drawn",
    "does not prove the lesson finished",
    "is not grading",
]

MERGED_SOURCE_PR_REQUIREMENTS = {
    "RabbitHole PR #154": [
        "RabbitHole PR #154",
        "Merged.",
        "Records that Alice put the Run panel into the Run window area.",
    ],
    "RabbitHole PR #155": [
        "RabbitHole PR #155",
        "Merged.",
        "Records launcher steps and no-go messages",
        "does not prove rendering",
    ],
    "RabbitHole PR #156": [
        "RabbitHole PR #156",
        "Merged.",
        "Keeps old image recovery while safely rejecting unsupported old code.",
    ],
    "eatme PR #89": [
        "eatme PR #89",
        "Merged.",
        "Improves instructor and student readiness reports",
        "does not grade work or prove full lesson completion",
    ],
}

STALE_STATUS_TERMS = [
    "review is still running",
    "waiting on coverage",
    "under review",
    "pending review",
    "still pending",
    "blocked on review",
    "marked review-running",
]

STALE_README_TABLE_STATUS_TERMS = [
    "review is still running",
    "waiting",
    "under review",
    "finish review",
    "add coverage for pr #156",
]

PLAIN_LANGUAGE_JARGON = ["gate", "lane", "affordance", "render target"]

EVIDENCE_TERMS = [
    "desktop-run-execution-20260506182000",
    "readiness_status=blocked_until_ui_automation",
    "desktop-run-execution.json",
    "eatme.alice-desktop-run-execution/v1",
    "statement_execution_observed",
    "active_scene_invoke_started",
    "executing_statement_count",
    "260",
    "desktop-run-runtime.log",
    "run-window-created.json",
    "ui-action-contract.json",
]


def plain(text):
    return re.sub(r"\s+", " ", text.replace("**", " "))


def without_markdown_link_targets(text):
    def keep_label(match):
        return match.group("label")

    return re.sub(r"\[(?P<label>[^\]]+)\]\([^)]+\)", keep_label, text)


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
        cls.docs = {name: path.read_text(encoding="utf-8") for name, path in DOCS.items()}

    def assert_contains_all(self, text, expected, source):
        missing = [term for term in expected if term not in text]
        self.assertEqual([], missing, f"{source} is missing expected terms")

    def assert_merged_source_status_is_plain(self, text, source):
        normalized = plain(text).lower()
        missing = {}
        for work_item, terms in MERGED_SOURCE_PR_REQUIREMENTS.items():
            missing_terms = [term for term in terms if term.lower() not in normalized]
            if missing_terms:
                missing[work_item] = missing_terms

        self.assertEqual({}, missing, f"{source} is missing merged source PR status")

    def assert_no_stale_status_near_source_prs(self, text, source):
        normalized = plain(text).lower()
        for pr_name in MERGED_SOURCE_PR_REQUIREMENTS:
            index = normalized.find(pr_name.lower())
            self.assertNotEqual(-1, index, f"{source} is missing {pr_name}")
            nearby = normalized[index : index + 350]
            for term in STALE_STATUS_TERMS:
                self.assertNotIn(
                    term,
                    nearby,
                    f"{source} uses stale status near {pr_name}: {term}",
                )

    def assert_no_stale_readme_table_status(self, text):
        source_pr_rows = [
            row
            for row in text.splitlines()
            if row.strip().startswith("|")
            and any(link in row for link in REQUIRED_PR_LINKS)
        ]

        self.assertGreaterEqual(
            len(source_pr_rows),
            len(MERGED_SOURCE_PR_REQUIREMENTS),
            "README is missing source PR table rows",
        )

        table_text = plain("\n".join(source_pr_rows)).lower()
        for term in STALE_README_TABLE_STATUS_TERMS:
            self.assertNotIn(term, table_text, f"README source PR table uses stale status: {term}")

    def test_readme_plan_summary_links_to_controlling_docs_and_latest_evidence(self):
        plan_summary = section(self.docs["README"], "Plan summary")

        self.assert_contains_all(plan_summary, README_PLAN_LINKS, "README plan summary")
        self.assert_contains_all(plan_summary, REQUIRED_PR_LINKS, "README plan summary")
        self.assert_contains_all(plain(plan_summary), PROOF_BOUNDARY_TERMS, "README plan summary")
        self.assert_merged_source_status_is_plain(plan_summary, "README plan summary")
        self.assert_no_stale_status_near_source_prs(plan_summary, "README plan summary")
        self.assert_no_stale_readme_table_status(self.docs["README"])

    def test_atlas_index_lists_0085_once_with_a_bounded_summary(self):
        text = self.docs["atlas index"]
        entry_link = "journal/0085-desktop-run-execution-evidence.md"

        self.assertEqual(1, text.count(entry_link))
        self.assertIn("RabbitHole PR #154 Run window attachment signal", text)
        self.assertIn("limits", text)

    def test_0085_traceability_and_evidence_contract_are_explicit(self):
        text = self.docs["atlas entry 0085"]

        self.assert_contains_all(text, ENTRY_TRACEABILITY_LINKS, "atlas entry 0085")
        self.assert_contains_all(text, EVIDENCE_TERMS, "atlas entry 0085")
        self.assert_contains_all(text, REQUIRED_PR_LINKS, "atlas entry 0085")
        self.assert_contains_all(plain(text), PROOF_BOUNDARY_TERMS, "atlas entry 0085")
        self.assert_merged_source_status_is_plain(text, "atlas entry 0085")
        self.assert_no_stale_status_near_source_prs(text, "atlas entry 0085")

    def test_all_controlling_docs_share_the_same_proof_boundary(self):
        for name in CONTROL_DOCS:
            with self.subTest(document=name):
                self.assert_contains_all(plain(self.docs[name]), PROOF_BOUNDARY_TERMS, name)

    def test_status_docs_list_merged_source_prs_plainly(self):
        status_docs = [
            "README",
            "root plan",
            "current modernization plan",
            "restarted full-scope status",
            "eatme implementation plan",
            "atlas entry 0085",
        ]

        for name in status_docs:
            with self.subTest(document=name):
                self.assert_contains_all(self.docs[name], REQUIRED_PR_LINKS, name)
                self.assert_merged_source_status_is_plain(self.docs[name], name)
                self.assert_no_stale_status_near_source_prs(self.docs[name], name)

    def test_controlling_docs_avoid_unexplained_project_jargon(self):
        for name, text in self.docs.items():
            with self.subTest(document=name):
                prose = without_markdown_link_targets(text)
                for term in PLAIN_LANGUAGE_JARGON:
                    self.assertIsNone(
                        re.search(rf"\b{re.escape(term)}\b", prose, re.IGNORECASE),
                        f"{name} uses project jargon without plain-language explanation: {term}",
                    )

    def test_no_doc_uses_stale_repo_or_overclaim_language(self):
        forbidden_terms = [
            "alice3-modernization",
            "visible rendering is proven",
            "pixels were drawn is proven",
            "desktop save-menu completion is proven",
            "original Alice is proven equivalent",
            "full lesson automation is complete",
            "VM statement execution",
            "VM statement-execution proof",
        ]

        for name in CONTROL_DOCS:
            with self.subTest(document=name):
                text = self.docs[name]
                for term in forbidden_terms:
                    self.assertNotIn(term, text)


if __name__ == "__main__":
    unittest.main()
