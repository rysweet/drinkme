from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]

README = ROOT / "README.md"
ATLAS_INDEX = ROOT / "docs/atlas/index.md"
ENTRY_0085 = ROOT / "docs/atlas/journal/0085-desktop-run-execution-evidence.md"
ENTRY_0086 = ROOT / "docs/atlas/journal/0086-eatme-pr92-rabbithole-evidence-readiness.md"
ENTRY_0087 = ROOT / "docs/atlas/journal/0087-rabbithole-pr159-pr160-eatme-pr93-merge-status.md"
ENTRY_0088 = ROOT / "docs/atlas/journal/0088-rabbithole-pr163-eatme-pr95-merge-status.md"
ENTRY_0089 = ROOT / "docs/atlas/journal/0089-rabbithole-pr164-eatme-pr96-merge-status.md"
ENTRY_0090 = ROOT / "docs/atlas/journal/0090-rabbithole-pr166-pr167-eatme-pr98-merge-status.md"
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
    "atlas entry 0086": ENTRY_0086,
}

CURRENT_MERGE_STATUS_DOCS = {
    "README": README,
    "root plan": ROOT_PLAN,
    "current modernization plan": CURRENT_STATE,
    "restarted full-scope status": RESTARTED_STATUS,
    "eatme implementation plan": EATME_PLAN,
}

DOCS = {
    **CONTROL_DOCS,
    **CURRENT_MERGE_STATUS_DOCS,
    "atlas index": ATLAS_INDEX,
    "atlas entry 0087": ENTRY_0087,
    "atlas entry 0088": ENTRY_0088,
    "atlas entry 0089": ENTRY_0089,
    "atlas entry 0090": ENTRY_0090,
}

README_PLAN_LINKS = [
    "[root investigation plan](docs/plan.md)",
    "[current modernization plan](docs/modernization/current-state-and-next-steps.md)",
    "[restarted full-scope status](docs/modernization/restarted-full-scope-status.md)",
    "[eatme implementation plan](docs/eatme/implementation-plan.md)",
    "[atlas journal entry 0085](docs/atlas/journal/0085-desktop-run-execution-evidence.md)",
    "[atlas journal entry 0086](docs/atlas/journal/0086-eatme-pr92-rabbithole-evidence-readiness.md)",
    "[atlas journal entry 0087](docs/atlas/journal/0087-rabbithole-pr159-pr160-eatme-pr93-merge-status.md)",
    "[atlas journal entry 0088](docs/atlas/journal/0088-rabbithole-pr163-eatme-pr95-merge-status.md)",
    "[atlas journal entry 0089](docs/atlas/journal/0089-rabbithole-pr164-eatme-pr96-merge-status.md)",
    "[atlas journal entry 0090](docs/atlas/journal/0090-rabbithole-pr166-pr167-eatme-pr98-merge-status.md)",
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
    "https://github.com/rysweet/eatme/pull/92",
]

PREVIOUS_MERGED_PR_LINKS = [
    "https://github.com/rysweet/RabbitHole/pull/159",
    "https://github.com/rysweet/RabbitHole/pull/160",
    "https://github.com/rysweet/eatme/pull/93",
]

LATEST_MERGED_PR_LINKS = [
    "https://github.com/rysweet/RabbitHole/pull/163",
    "https://github.com/rysweet/eatme/pull/95",
]

NEWEST_MERGED_PR_LINKS = [
    "https://github.com/rysweet/RabbitHole/pull/164",
    "https://github.com/rysweet/eatme/pull/96",
]

CURRENT_WAVE_PR_LINKS = [
    "https://github.com/rysweet/RabbitHole/pull/166",
    "https://github.com/rysweet/RabbitHole/pull/167",
    "https://github.com/rysweet/eatme/pull/98",
]

CURRENT_MERGED_PR_LINKS = (
    PREVIOUS_MERGED_PR_LINKS
    + LATEST_MERGED_PR_LINKS
    + NEWEST_MERGED_PR_LINKS
    + CURRENT_WAVE_PR_LINKS
)

PROOF_BOUNDARY_TERMS = [
    "narrow Run window attachment signal",
    "Alice put the Run panel into the Run window area",
    "does not prove pixels were drawn",
    "does not prove the lesson finished",
    "is not grading",
]

CURRENT_UNPROVEN_BEHAVIORS = [
    "full Alice UI automation",
    "visible rendering",
    "desktop save-menu completion",
    "grading",
    "creative assessment",
    "first-lesson completion",
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
    "eatme PR #92": [
        "eatme PR #92",
        "Merged",
        "Documents the RabbitHole evidence needed before first-lesson readiness can be marked ready",
        "full Alice UI automation",
    ],
}

MERGED_CURRENT_PR_REQUIREMENTS = {
    "RabbitHole PR #159": [
        "RabbitHole PR #159",
        "Merged",
        "Tweedle source entry",
        "clear",
    ],
    "RabbitHole PR #160": [
        "RabbitHole PR #160",
        "Merged",
        "desktop-run-pixel-boundary.json",
        'status: "not_observed"',
        "pixel",
    ],
    "RabbitHole PR #163": [
        "RabbitHole PR #163",
        "Merged",
        "unsupported manifest-declared Tweedle type",
        "clear error",
        "silently dropping",
    ],
    "RabbitHole PR #164": [
        "RabbitHole PR #164",
        "Merged",
        "constructor-bearing sibling",
        "fails clearly",
        "full Tweedle decode support",
    ],
    "eatme PR #93": [
        "eatme PR #93",
        "Merged",
        "readiness evidence categories",
        "runtime",
    ],
    "eatme PR #95": [
        "eatme PR #95",
        "Merged",
        "desktop-run-pixel-boundary.json",
        "missing",
        "invalid",
        "not_observed",
    ],
    "eatme PR #96": [
        "eatme PR #96",
        "Merged",
        "evidence_progress",
        "present",
        "missing",
        "blocked",
    ],
    "RabbitHole PR #166": [
        "RabbitHole PR #166",
        "Merged",
        "complex field initializer",
        "full Tweedle decode support",
    ],
    "RabbitHole PR #167": [
        "RabbitHole PR #167",
        "Merged",
        "desktop-run-pixel-observation.json",
        "screenshot",
        "center pixel",
        "blocker code",
    ],
    "eatme PR #98": [
        "eatme PR #98",
        "Merged",
        "first-lesson readiness progress",
        "plain text output",
        "runtime proof",
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

STALE_CURRENT_PR_PATTERNS = [
    r"PR\s*#?159[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"PR\s*#?160[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"PR\s*#?93[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"PR\s*#?163[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"PR\s*#?95[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"PR\s*#?164[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"PR\s*#?96[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"PR\s*#?166[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"PR\s*#?167[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"PR\s*#?98[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?159",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?160",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?93",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?163",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?95",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?164",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?96",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?166",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?167",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?98",
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

    def assert_current_merge_status_is_plain(self, text, source, requirements=None):
        if requirements is None:
            requirements = MERGED_CURRENT_PR_REQUIREMENTS
        normalized = plain(text).lower()
        missing = {}
        for work_item, terms in requirements.items():
            missing_terms = [term for term in terms if term.lower() not in normalized]
            if missing_terms:
                missing[work_item] = missing_terms

        self.assertEqual({}, missing, f"{source} is missing current merged PR status")

    def assert_current_unproven_behaviors_are_explicit(self, text, source):
        normalized = plain(text).lower()
        missing = [term for term in CURRENT_UNPROVEN_BEHAVIORS if term.lower() not in normalized]
        self.assertEqual([], missing, f"{source} is missing current unproven behavior terms")
        self.assertTrue(
            "does not prove" in normalized or "unproven" in normalized,
            f"{source} must separate merged PR status from product behavior proof",
        )

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

    def assert_no_stale_status_for_current_prs(self, text, source):
        normalized = plain(text).lower()
        for pattern in STALE_CURRENT_PR_PATTERNS:
            self.assertIsNone(
                re.search(pattern, normalized, re.IGNORECASE),
                f"{source} uses stale pending/review wording for a merged current PR",
            )

    def assert_no_stale_readme_table_status(self, text):
        all_pr_links = REQUIRED_PR_LINKS + CURRENT_MERGED_PR_LINKS
        source_pr_rows = [
            row
            for row in text.splitlines()
            if row.strip().startswith("|")
            and any(link in row for link in all_pr_links)
        ]

        self.assertGreaterEqual(
            len(source_pr_rows),
            len(MERGED_SOURCE_PR_REQUIREMENTS) + len(MERGED_CURRENT_PR_REQUIREMENTS),
            "README is missing source PR table rows",
        )

        self.assert_contains_all("\n".join(source_pr_rows), CURRENT_MERGED_PR_LINKS, "README source PR table")

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

    def test_atlas_index_lists_recent_entries_once_with_bounded_summaries(self):
        text = self.docs["atlas index"]
        entry_link = "journal/0085-desktop-run-execution-evidence.md"
        entry_0086_link = "journal/0086-eatme-pr92-rabbithole-evidence-readiness.md"
        entry_0087_link = "journal/0087-rabbithole-pr159-pr160-eatme-pr93-merge-status.md"
        entry_0088_link = "journal/0088-rabbithole-pr163-eatme-pr95-merge-status.md"
        entry_0089_link = "journal/0089-rabbithole-pr164-eatme-pr96-merge-status.md"
        entry_0090_link = "journal/0090-rabbithole-pr166-pr167-eatme-pr98-merge-status.md"

        self.assertEqual(1, text.count(entry_link))
        self.assertIn("RabbitHole PR #154 Run window attachment signal", text)
        self.assertIn("limits", text)
        self.assertEqual(1, text.count(entry_0086_link))
        self.assertIn("eatme PR #92 documentation update", text)
        self.assertEqual(1, text.count(entry_0087_link))
        self.assertIn("RabbitHole PR #159/#160 and eatme PR #93 merge status", text)
        self.assertEqual(1, text.count(entry_0088_link))
        self.assertIn("RabbitHole PR #163 and eatme PR #95 merge status", text)
        self.assertEqual(1, text.count(entry_0089_link))
        self.assertIn("RabbitHole PR #164 and eatme PR #96 merge status", text)
        self.assertEqual(1, text.count(entry_0090_link))
        self.assertIn("RabbitHole PR #166/#167 and eatme PR #98 merge status", text)

    def test_0085_traceability_and_evidence_contract_are_explicit(self):
        text = self.docs["atlas entry 0085"]

        self.assert_contains_all(text, ENTRY_TRACEABILITY_LINKS, "atlas entry 0085")
        self.assert_contains_all(text, EVIDENCE_TERMS, "atlas entry 0085")
        self.assert_contains_all(text, REQUIRED_PR_LINKS, "atlas entry 0085")
        self.assert_contains_all(plain(text), PROOF_BOUNDARY_TERMS, "atlas entry 0085")
        self.assert_merged_source_status_is_plain(text, "atlas entry 0085")
        self.assert_no_stale_status_near_source_prs(text, "atlas entry 0085")

    def test_0086_traceability_and_boundaries_are_explicit(self):
        text = self.docs["atlas entry 0086"]

        self.assert_contains_all(text, ENTRY_TRACEABILITY_LINKS, "atlas entry 0086")
        self.assert_contains_all(text, ["eatme PR #92", "cfe1f9e364d0015a3f97e237a9de5af670ae3bd6"], "atlas entry 0086")
        self.assert_contains_all(plain(text), PROOF_BOUNDARY_TERMS, "atlas entry 0086")
        self.assert_merged_source_status_is_plain(text, "atlas entry 0086")
        self.assert_no_stale_status_near_source_prs(text, "atlas entry 0086")

    def test_0087_current_merge_status_and_boundaries_are_explicit(self):
        text = self.docs["atlas entry 0087"]

        requirements = {
            key: MERGED_CURRENT_PR_REQUIREMENTS[key]
            for key in ["RabbitHole PR #159", "RabbitHole PR #160", "eatme PR #93"]
        }
        self.assert_contains_all(text, PREVIOUS_MERGED_PR_LINKS, "atlas entry 0087")
        self.assert_current_merge_status_is_plain(text, "atlas entry 0087", requirements)
        self.assert_current_unproven_behaviors_are_explicit(text, "atlas entry 0087")
        self.assert_no_stale_status_for_current_prs(text, "atlas entry 0087")
        self.assertIn("Older atlas entries remain historical evidence", text)
        self.assertIn("pixel and screenshot proof were not observed", text)
        self.assertIn("broad Tweedle decode support", text)

    def test_0088_current_merge_status_and_boundaries_are_explicit(self):
        text = self.docs["atlas entry 0088"]

        requirements = {
            key: MERGED_CURRENT_PR_REQUIREMENTS[key]
            for key in ["RabbitHole PR #163", "eatme PR #95"]
        }
        self.assert_contains_all(text, LATEST_MERGED_PR_LINKS, "atlas entry 0088")
        self.assert_current_merge_status_is_plain(text, "atlas entry 0088", requirements)
        self.assert_current_unproven_behaviors_are_explicit(text, "atlas entry 0088")
        self.assert_no_stale_status_for_current_prs(text, "atlas entry 0088")
        self.assertIn("silently dropping that type", text)
        self.assertIn("missing, invalid, or `not_observed`", text)
        self.assertIn("does not add full Tweedle", text)

    def test_0089_current_merge_status_and_boundaries_are_explicit(self):
        text = self.docs["atlas entry 0089"]

        requirements = {
            key: MERGED_CURRENT_PR_REQUIREMENTS[key]
            for key in ["RabbitHole PR #164", "eatme PR #96"]
        }
        self.assert_contains_all(text, NEWEST_MERGED_PR_LINKS, "atlas entry 0089")
        self.assert_current_merge_status_is_plain(text, "atlas entry 0089", requirements)
        self.assert_current_unproven_behaviors_are_explicit(text, "atlas entry 0089")
        self.assert_no_stale_status_for_current_prs(text, "atlas entry 0089")
        self.assertIn("constructor-bearing sibling Tweedle type", text)
        self.assertIn("evidence_progress", text)
        self.assertIn("summarizes existing evidence only", text)

    def test_0090_current_merge_status_and_boundaries_are_explicit(self):
        text = self.docs["atlas entry 0090"]

        requirements = {
            key: MERGED_CURRENT_PR_REQUIREMENTS[key]
            for key in ["RabbitHole PR #166", "RabbitHole PR #167", "eatme PR #98"]
        }
        self.assert_contains_all(text, CURRENT_WAVE_PR_LINKS, "atlas entry 0090")
        self.assert_current_merge_status_is_plain(text, "atlas entry 0090", requirements)
        self.assert_current_unproven_behaviors_are_explicit(text, "atlas entry 0090")
        self.assert_no_stale_status_for_current_prs(text, "atlas entry 0090")
        self.assertIn("complex field initializer", text)
        self.assertIn("desktop-run-pixel-observation.json", text)
        self.assertIn("plain text output", text)

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

    def test_current_status_docs_list_new_merged_prs_plainly(self):
        for name in CURRENT_MERGE_STATUS_DOCS:
            with self.subTest(document=name):
                text = self.docs[name]
                self.assert_contains_all(text, CURRENT_MERGED_PR_LINKS, name)
                self.assert_current_merge_status_is_plain(text, name)
                self.assert_current_unproven_behaviors_are_explicit(text, name)
                self.assert_no_stale_status_for_current_prs(text, name)

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

        for name in DOCS:
            with self.subTest(document=name):
                text = self.docs[name]
                for term in forbidden_terms:
                    self.assertNotIn(term, text)


if __name__ == "__main__":
    unittest.main()
