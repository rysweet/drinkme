from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]

README = ROOT / "README.md"
ATLAS_INDEX = ROOT / "docs/atlas/index.md"
ENTRY_0085 = ROOT / "docs/atlas/journal/0085-desktop-run-execution-evidence.md"
ROOT_PLAN = ROOT / "docs/plan.md"
CURRENT_STATE = ROOT / "docs/modernization/current-state-and-next-steps.md"
EATME_PLAN = ROOT / "docs/eatme/implementation-plan.md"

CONTROL_DOCS = {
    "README": README,
    "root plan": ROOT_PLAN,
    "current modernization plan": CURRENT_STATE,
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

BOUNDARY_TERMS = [
    "RabbitHole",
    "VM statement execution",
    "geometry-checked toolbar",
    "original Alice equivalence",
    "visible rendering",
    "desktop save-menu completion",
    "grading",
    "full lesson automation",
]

NEXT_FEATURE_SEAMS = [
    "stable UI or accessibility",
    "visible rendering evidence",
    "desktop save-menu completion",
    "original Alice",
]

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

    def test_readme_plan_summary_links_to_controlling_docs_and_latest_evidence(self):
        plan_summary = section(self.docs["README"], "Plan summary")

        self.assert_contains_all(plan_summary, README_PLAN_LINKS, "README plan summary")
        self.assert_contains_all(plan_summary, BOUNDARY_TERMS, "README plan summary")
        self.assert_contains_all(plan_summary, NEXT_FEATURE_SEAMS, "README plan summary")

    def test_atlas_index_lists_0085_once_with_a_bounded_summary(self):
        text = self.docs["atlas index"]
        entry_link = "journal/0085-desktop-run-execution-evidence.md"

        self.assertEqual(1, text.count(entry_link))
        self.assertIn("RabbitHole VM statement-execution proof", text)
        self.assertIn("remaining limits", text)

    def test_0085_traceability_and_evidence_contract_are_explicit(self):
        text = self.docs["atlas entry 0085"]

        self.assert_contains_all(text, ENTRY_TRACEABILITY_LINKS, "atlas entry 0085")
        self.assert_contains_all(text, EVIDENCE_TERMS, "atlas entry 0085")
        self.assert_contains_all(text, BOUNDARY_TERMS, "atlas entry 0085")
        self.assert_contains_all(text, NEXT_FEATURE_SEAMS, "atlas entry 0085")

    def test_all_controlling_docs_share_the_same_proof_boundary(self):
        for name in CONTROL_DOCS:
            with self.subTest(document=name):
                self.assert_contains_all(self.docs[name], BOUNDARY_TERMS, name)

    def test_no_doc_uses_stale_repo_or_overclaim_language(self):
        forbidden_terms = [
            "alice3-modernization",
            "visible rendering is proven",
            "desktop save-menu completion is proven",
            "original Alice is proven equivalent",
            "full lesson automation is complete",
        ]

        for name in CONTROL_DOCS:
            with self.subTest(document=name):
                text = self.docs[name]
                for term in forbidden_terms:
                    self.assertNotIn(term, text)


if __name__ == "__main__":
    unittest.main()
