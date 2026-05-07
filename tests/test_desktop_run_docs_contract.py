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
ENTRY_0091 = ROOT / "docs/atlas/journal/0091-rabbithole-pr168-pr169-eatme-pr99-merge-status.md"
ENTRY_0092 = ROOT / "docs/atlas/journal/0092-rabbithole-pr170-pr171-pr172-eatme-pr101-pr102-merge-status.md"
ENTRY_0093 = ROOT / "docs/atlas/journal/0093-source-eatme-ci-wave-status.md"
ENTRY_0094 = ROOT / "docs/atlas/journal/0094-rabbithole-source-ci-wave-status.md"
ENTRY_0095 = ROOT / "docs/atlas/journal/0095-rabbithole-pr207-pr208-source-evidence.md"
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
    "atlas entry 0091": ENTRY_0091,
    "atlas entry 0092": ENTRY_0092,
    "atlas entry 0093": ENTRY_0093,
    "atlas entry 0094": ENTRY_0094,
    "atlas entry 0095": ENTRY_0095,
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
    "[atlas journal entry 0091](docs/atlas/journal/0091-rabbithole-pr168-pr169-eatme-pr99-merge-status.md)",
    "[atlas journal entry 0092](docs/atlas/journal/0092-rabbithole-pr170-pr171-pr172-eatme-pr101-pr102-merge-status.md)",
    "[atlas journal entry 0093](docs/atlas/journal/0093-source-eatme-ci-wave-status.md)",
    "[atlas journal entry 0094](docs/atlas/journal/0094-rabbithole-source-ci-wave-status.md)",
    "[atlas journal entry 0095](docs/atlas/journal/0095-rabbithole-pr207-pr208-source-evidence.md)",
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

OBSERVATION_WAVE_PR_LINKS = [
    "https://github.com/rysweet/RabbitHole/pull/168",
    "https://github.com/rysweet/RabbitHole/pull/169",
    "https://github.com/rysweet/eatme/pull/99",
]


SOURCE_EATME_CI_WAVE_PR_LINKS = [
    "https://github.com/rysweet/RabbitHole/pull/173",
    "https://github.com/rysweet/RabbitHole/pull/174",
    "https://github.com/rysweet/RabbitHole/pull/175",
    "https://github.com/rysweet/RabbitHole/pull/176",
    "https://github.com/rysweet/RabbitHole/pull/177",
    "https://github.com/rysweet/RabbitHole/pull/178",
    "https://github.com/rysweet/RabbitHole/pull/179",
    "https://github.com/rysweet/RabbitHole/pull/180",
    "https://github.com/rysweet/RabbitHole/pull/181",
    "https://github.com/rysweet/RabbitHole/pull/182",
    "https://github.com/rysweet/RabbitHole/pull/183",
    "https://github.com/rysweet/RabbitHole/pull/184",
    "https://github.com/rysweet/eatme/pull/105",
    "https://github.com/rysweet/eatme/pull/106",
    "https://github.com/rysweet/eatme/pull/108",
    "https://github.com/rysweet/eatme/pull/109",
    "https://github.com/rysweet/eatme/pull/110",
    "https://github.com/rysweet/eatme/pull/111",
    "https://github.com/rysweet/eatme/pull/112",
    "https://github.com/rysweet/eatme/pull/113",
    "https://github.com/rysweet/eatme/pull/114",
    "https://github.com/rysweet/eatme/pull/115",
    "https://github.com/rysweet/eatme/pull/116",
]

NEXT_ACTION_WAVE_PR_LINKS = [
    "https://github.com/rysweet/RabbitHole/pull/170",
    "https://github.com/rysweet/RabbitHole/pull/171",
    "https://github.com/rysweet/RabbitHole/pull/172",
    "https://github.com/rysweet/eatme/pull/101",
    "https://github.com/rysweet/eatme/pull/102",
]

SOURCE_CI_FIX_WAVE_PR_LINKS = [
    "https://github.com/rysweet/RabbitHole/pull/185",
    "https://github.com/rysweet/RabbitHole/pull/187",
    "https://github.com/rysweet/RabbitHole/pull/188",
    "https://github.com/rysweet/RabbitHole/pull/190",
    "https://github.com/rysweet/RabbitHole/pull/191",
]

SOURCE_EVIDENCE_WAVE_PR_LINKS = [
    "https://github.com/rysweet/RabbitHole/pull/207",
    "https://github.com/rysweet/RabbitHole/pull/208",
]

CURRENT_MERGED_PR_LINKS = (
    PREVIOUS_MERGED_PR_LINKS
    + LATEST_MERGED_PR_LINKS
    + NEWEST_MERGED_PR_LINKS
    + CURRENT_WAVE_PR_LINKS
    + OBSERVATION_WAVE_PR_LINKS
    + NEXT_ACTION_WAVE_PR_LINKS
    + SOURCE_EATME_CI_WAVE_PR_LINKS
    + SOURCE_CI_FIX_WAVE_PR_LINKS
    + SOURCE_EVIDENCE_WAVE_PR_LINKS
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
    "RabbitHole PR #168": [
        "RabbitHole PR #168",
        "Merged",
        "unresolved parent",
        "full Tweedle decode support",
    ],
    "RabbitHole PR #169": [
        "RabbitHole PR #169",
        "Merged",
        "machine-readable blocker details",
        "desktop-run-pixel-observation.json",
        "visible rendering",
    ],
    "eatme PR #99": [
        "eatme PR #99",
        "Merged",
        "desktop-run-pixel-observation.json",
        "observed screenshot/sample data",
        "blocked component state",
        "runtime proof",
    ],
    "RabbitHole PR #170": [
        "RabbitHole PR #170",
        "Merged",
        "attached Run panel",
        "pixel sampling",
        "visible rendering correctness",
    ],
    "RabbitHole PR #171": [
        "RabbitHole PR #171",
        "Merged",
        "resource-typed Tweedle field initializer",
        "full Tweedle decode support",
    ],
    "RabbitHole PR #172": [
        "RabbitHole PR #172",
        "Merged",
        "desktop-first-lesson-next-action.json",
        "Save-menu",
        "code/procedure action",
        "full Alice UI automation",
    ],
    "eatme PR #101": [
        "eatme PR #101",
        "Merged",
        "next-action evidence",
        "first-lesson plain output",
        "runtime proof",
    ],
    "eatme PR #102": [
        "eatme PR #102",
        "Merged",
        "media-audio-cue-storyboard",
        "media-audio-creator",
        "grade student work",
    ],

    "RabbitHole PR #173": ["RabbitHole PR #173", "Merged", "procedure UI action", "no desktop UI invocation is proven"],
    "RabbitHole PR #174": ["RabbitHole PR #174", "Merged", "Save-menu action target", "save-menu completion remains unproven"],
    "RabbitHole PR #175": ["RabbitHole PR #175", "Merged", "desktop Run status summary", "visible rendering correctness"],
    "RabbitHole PR #176": ["RabbitHole PR #176", "Merged", "missing sibling Tweedle entry", "fail clearly"],
    "RabbitHole PR #177": ["RabbitHole PR #177", "Merged", "desktop Run evidence status summary"],
    "RabbitHole PR #178": ["RabbitHole PR #178", "Merged", "unnamed unsupported manifest Tweedle sibling types", "archive path"],
    "RabbitHole PR #179": ["RabbitHole PR #179", "Merged", "Checkstyle 0:53", "coverage 11:54"],
    "RabbitHole PR #180": ["RabbitHole PR #180", "Merged", "first-lesson desktop evidence reporting"],
    "RabbitHole PR #181": ["RabbitHole PR #181", "Merged", "resource-typed field initializer", "no behavior change"],
    "RabbitHole PR #182": ["RabbitHole PR #182", "Merged", "desktop-run-status-summary.json", "SaveProjectOperation"],
    "RabbitHole PR #183": ["RabbitHole PR #183", "Merged", "typed-null Tweedle field initializer", "archive entry path"],
    "RabbitHole PR #184": ["RabbitHole PR #184", "Merged", "project-IO", "larger decode gaps"],
    "eatme PR #105": ["eatme PR #105", "Merged", "student artifact sharing"],
    "eatme PR #106": ["eatme PR #106", "Merged", "next-action evidence", "readiness reporting"],
    "eatme PR #108": ["eatme PR #108", "Merged", "classroom gallery walk"],
    "eatme PR #109": ["eatme PR #109", "Merged", "teacher community sharing"],
    "eatme PR #110": ["eatme PR #110", "Merged", "not proof of full UI automation"],
    "eatme PR #111": ["eatme PR #111", "Merged", "stale PR-only runs", "CI"],
    "eatme PR #112": ["eatme PR #112", "Merged", "curriculum-sequence-remix-pack", "Gadugi adapter"],
    "eatme PR #113": ["eatme PR #113", "Merged", "persona asset docs inventory"],
    "eatme PR #114": ["eatme PR #114", "Merged", "instructor mission inventory", "34 canonical scenarios"],
    "eatme PR #115": ["eatme PR #115", "Merged", "student mission inventory", "33 scenarios"],
    "eatme PR #116": ["eatme PR #116", "Merged", "docs/docs-site-only CI", "Rust checks"],

    "RabbitHole PR #185": [
        "RabbitHole PR #185",
        "Merged",
        "model resource array grouping",
        "duplicate index rejection",
        "70 percent aggregate coverage",
    ],
    "RabbitHole PR #187": [
        "RabbitHole PR #187",
        "Merged",
        "TextString label <- null",
        "NullLiteral",
        "full Tweedle decode support",
    ],
    "RabbitHole PR #188": [
        "RabbitHole PR #188",
        "Merged",
        "ProcedureTabSelection",
        "not live procedure invocation",
        "Save-menu completion",
    ],
    "RabbitHole PR #190": [
        "RabbitHole PR #190",
        "Merged",
        "IssueReportWorker",
        "jogamp.org",
        "52 Java files over 500 lines",
    ],
    "RabbitHole PR #191": [
        "RabbitHole PR #191",
        "Merged",
        "Maven cache fallback",
        "stuck coverage path",
        "25492250204",
    ],
    "RabbitHole PR #207": [
        "RabbitHole PR #207",
        "Merged",
        "Numeric and Boolean",
        "null",
        "AST `NullLiteral`",
        "if(null)",
        "while(null)",
        "Full Tweedle/player decode support remains unproven",
    ],
    "RabbitHole PR #208": [
        "RabbitHole PR #208",
        "Merged",
        "8799854787655ca61b6fad9378377b19d41aa7b1",
        "153f4e4ce77415d42e6f1047abcc2074671ae4c8",
        "all GitHub checks passed",
        "Save operation completion evidence",
        "desktop save-menu completion remains unproven",
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
    r"PR\s*#?168[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"PR\s*#?169[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"PR\s*#?99[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"PR\s*#?170[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"PR\s*#?171[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"PR\s*#?172[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"PR\s*#?101[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"PR\s*#?102[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
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
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?168",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?169",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?99",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?170",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?171",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?172",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?101",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?102",
    r"PR\s*#?173[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"PR\s*#?174[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"PR\s*#?175[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"PR\s*#?176[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"PR\s*#?177[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"PR\s*#?178[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"PR\s*#?179[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"PR\s*#?180[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"PR\s*#?181[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"PR\s*#?182[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"PR\s*#?183[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"PR\s*#?184[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"PR\s*#?105[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"PR\s*#?106[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"PR\s*#?108[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"PR\s*#?109[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"PR\s*#?110[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"PR\s*#?111[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"PR\s*#?112[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"PR\s*#?113[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"PR\s*#?114[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"PR\s*#?115[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"PR\s*#?116[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?173",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?174",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?175",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?176",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?177",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?178",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?179",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?180",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?181",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?182",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?183",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?184",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?105",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?106",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?108",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?109",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?110",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?111",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?112",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?113",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?114",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?115",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?116",
    r"PR\s*#?185[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"PR\s*#?187[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"PR\s*#?188[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"PR\s*#?190[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"PR\s*#?191[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?185",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?187",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?188",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?190",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?191",
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
        entry_0091_link = "journal/0091-rabbithole-pr168-pr169-eatme-pr99-merge-status.md"
        entry_0092_link = "journal/0092-rabbithole-pr170-pr171-pr172-eatme-pr101-pr102-merge-status.md"
        entry_0093_link = "journal/0093-source-eatme-ci-wave-status.md"
        entry_0094_link = "journal/0094-rabbithole-source-ci-wave-status.md"
        entry_0095_link = "journal/0095-rabbithole-pr207-pr208-source-evidence.md"

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
        self.assertEqual(1, text.count(entry_0091_link))
        self.assertIn("RabbitHole PR #168/#169 and eatme PR #99 merge status", text)
        self.assertEqual(1, text.count(entry_0092_link))
        self.assertIn("RabbitHole PR #170/#171/#172 and eatme PR #101/#102 merge status", text)
        self.assertEqual(1, text.count(entry_0093_link))
        self.assertIn("Source, eatme, and CI status wave", text)
        self.assertEqual(1, text.count(entry_0094_link))
        self.assertIn("RabbitHole source and CI status wave", text)
        self.assertIn("Maven cache fallback", text)
        self.assertEqual(1, text.count(entry_0095_link))
        self.assertIn("RabbitHole PR #207/#208 source evidence update", text)
        self.assertIn("Save operation completion evidence", text)

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

    def test_0091_current_merge_status_and_boundaries_are_explicit(self):
        text = self.docs["atlas entry 0091"]

        requirements = {
            key: MERGED_CURRENT_PR_REQUIREMENTS[key]
            for key in ["RabbitHole PR #168", "RabbitHole PR #169", "eatme PR #99"]
        }
        self.assert_contains_all(text, OBSERVATION_WAVE_PR_LINKS, "atlas entry 0091")
        self.assert_current_merge_status_is_plain(text, "atlas entry 0091", requirements)
        self.assert_current_unproven_behaviors_are_explicit(text, "atlas entry 0091")
        self.assert_no_stale_status_for_current_prs(text, "atlas entry 0091")
        self.assertIn("unresolved parent", text)
        self.assertIn("machine-readable blocker details", text)
        self.assertIn("observed screenshot/sample data", text)

    def test_0092_current_merge_status_and_boundaries_are_explicit(self):
        text = self.docs["atlas entry 0092"]

        requirements = {
            key: MERGED_CURRENT_PR_REQUIREMENTS[key]
            for key in [
                "RabbitHole PR #170",
                "RabbitHole PR #171",
                "RabbitHole PR #172",
                "eatme PR #101",
                "eatme PR #102",
            ]
        }
        self.assert_contains_all(text, NEXT_ACTION_WAVE_PR_LINKS, "atlas entry 0092")
        self.assert_current_merge_status_is_plain(text, "atlas entry 0092", requirements)
        self.assert_current_unproven_behaviors_are_explicit(text, "atlas entry 0092")
        self.assert_no_stale_status_for_current_prs(text, "atlas entry 0092")
        self.assertIn("attached Run panel", text)
        self.assertIn("resource-typed Tweedle field initializer", text)
        self.assertIn("desktop-first-lesson-next-action.json", text)
        self.assertIn("media-audio-cue-storyboard", text)


    def test_0093_current_merge_status_and_boundaries_are_explicit(self):
        text = self.docs["atlas entry 0093"]

        requirements = {
            key: MERGED_CURRENT_PR_REQUIREMENTS[key]
            for key in [
                "RabbitHole PR #173",
                "RabbitHole PR #174",
                "RabbitHole PR #175",
                "RabbitHole PR #176",
                "RabbitHole PR #177",
                "RabbitHole PR #178",
                "RabbitHole PR #179",
                "RabbitHole PR #180",
                "RabbitHole PR #181",
                "RabbitHole PR #182",
                "RabbitHole PR #183",
                "RabbitHole PR #184",
                "eatme PR #105",
                "eatme PR #106",
                "eatme PR #108",
                "eatme PR #109",
                "eatme PR #110",
                "eatme PR #111",
                "eatme PR #112",
                "eatme PR #113",
                "eatme PR #114",
                "eatme PR #115",
                "eatme PR #116",
            ]
        }
        self.assert_contains_all(text, SOURCE_EATME_CI_WAVE_PR_LINKS, "atlas entry 0093")
        self.assert_current_merge_status_is_plain(text, "atlas entry 0093", requirements)
        self.assert_current_unproven_behaviors_are_explicit(text, "atlas entry 0093")
        self.assert_no_stale_status_for_current_prs(text, "atlas entry 0093")
        self.assertIn("34 canonical scenarios", text)
        self.assertIn("35 Gadugi scenarios", text)
        self.assertIn("coverage 11:54", text)
        self.assertIn("deployed sharing platform remains unproven", text)
        self.assertIn("full Tweedle decode support remains unproven", text)


    def test_0094_current_merge_status_and_boundaries_are_explicit(self):
        text = self.docs["atlas entry 0094"]

        requirements = {
            key: MERGED_CURRENT_PR_REQUIREMENTS[key]
            for key in [
                "RabbitHole PR #185",
                "RabbitHole PR #187",
                "RabbitHole PR #188",
                "RabbitHole PR #190",
                "RabbitHole PR #191",
            ]
        }
        self.assert_contains_all(text, SOURCE_CI_FIX_WAVE_PR_LINKS, "atlas entry 0094")
        self.assert_contains_all(text, ENTRY_TRACEABILITY_LINKS, "atlas entry 0094")
        self.assert_current_merge_status_is_plain(text, "atlas entry 0094", requirements)
        self.assert_current_unproven_behaviors_are_explicit(text, "atlas entry 0094")
        self.assert_no_stale_status_for_current_prs(text, "atlas entry 0094")
        self.assertIn("TextString label <- null", text)
        self.assertIn("WholeNumber <- null", text)
        self.assertIn("25492250204", text)
        self.assertIn("jogamp.org", text)
        self.assertIn("52 Java files over 500 lines", text)

    def test_0095_current_merge_status_and_boundaries_are_explicit(self):
        text = self.docs["atlas entry 0095"]

        requirements = {
            key: MERGED_CURRENT_PR_REQUIREMENTS[key]
            for key in ["RabbitHole PR #207", "RabbitHole PR #208"]
        }
        self.assert_contains_all(text, SOURCE_EVIDENCE_WAVE_PR_LINKS, "atlas entry 0095")
        self.assert_contains_all(text, ENTRY_TRACEABILITY_LINKS, "atlas entry 0095")
        self.assert_current_merge_status_is_plain(text, "atlas entry 0095", requirements)
        self.assert_current_unproven_behaviors_are_explicit(text, "atlas entry 0095")
        self.assert_no_stale_status_for_current_prs(text, "atlas entry 0095")
        self.assertIn("Numeric and Boolean", text)
        self.assertIn("AST `NullLiteral`", text)
        self.assertIn("if(null)", text)
        self.assertIn("while(null)", text)
        self.assertIn("all GitHub checks passed", text)
        self.assertIn("Save operation completion evidence", text)

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
