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
ENTRY_0096 = ROOT / "docs/atlas/journal/0096-rabbithole-pr209-pr210-pr211-source-wave-status.md"
ENTRY_0097 = ROOT / "docs/atlas/journal/0097-rabbithole-pr212-eatme-pr118-save-diagnostics-status.md"
ENTRY_0098 = ROOT / "docs/atlas/journal/0098-rabbithole-pr214-pr215-pr216-pr218-eatme-pr120-pr121-status.md"
ENTRY_0099 = ROOT / "docs/atlas/journal/0099-rabbithole-pr219-pr222-pr224-pr225-pr229-pr230-pr231-pr234-status.md"
ENTRY_0100 = ROOT / "docs/atlas/journal/0100-rabbithole-pr235-through-pr259-status.md"
ENTRY_0101 = ROOT / "docs/atlas/journal/0101-rabbithole-pr260-pr261-pr262-eatme-pr122-status.md"
ENTRY_0102 = ROOT / "docs/atlas/journal/0102-eatme-pr123-weather-wizard-status.md"
ENTRY_0103 = ROOT / "docs/atlas/journal/0103-rabbithole-pr264-eatme-pr124-status.md"
ENTRY_0104 = ROOT / "docs/atlas/journal/0104-rabbithole-pr265-pr266-pr267-status.md"
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
    "atlas entry 0096": ENTRY_0096,
    "atlas entry 0097": ENTRY_0097,
    "atlas entry 0098": ENTRY_0098,
    "atlas entry 0099": ENTRY_0099,
    "atlas entry 0100": ENTRY_0100,
    "atlas entry 0101": ENTRY_0101,
    "atlas entry 0102": ENTRY_0102,
    "atlas entry 0103": ENTRY_0103,
    "atlas entry 0104": ENTRY_0104,
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
    "[atlas journal entry 0096](docs/atlas/journal/0096-rabbithole-pr209-pr210-pr211-source-wave-status.md)",
    "[atlas journal entry 0097](docs/atlas/journal/0097-rabbithole-pr212-eatme-pr118-save-diagnostics-status.md)",
    "[atlas journal entry 0098](docs/atlas/journal/0098-rabbithole-pr214-pr215-pr216-pr218-eatme-pr120-pr121-status.md)",
    "[atlas journal entry 0099](docs/atlas/journal/0099-rabbithole-pr219-pr222-pr224-pr225-pr229-pr230-pr231-pr234-status.md)",
    "[atlas journal entry 0100](docs/atlas/journal/0100-rabbithole-pr235-through-pr259-status.md)",
    "[atlas journal entry 0101](docs/atlas/journal/0101-rabbithole-pr260-pr261-pr262-eatme-pr122-status.md)",
    "[atlas journal entry 0102](docs/atlas/journal/0102-eatme-pr123-weather-wizard-status.md)",
    "[atlas journal entry 0103](docs/atlas/journal/0103-rabbithole-pr264-eatme-pr124-status.md)",
    "[atlas journal entry 0104](docs/atlas/journal/0104-rabbithole-pr265-pr266-pr267-status.md)",
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

LATEST_SOURCE_WAVE_PR_LINKS = [
    "https://github.com/rysweet/RabbitHole/pull/209",
    "https://github.com/rysweet/RabbitHole/pull/210",
    "https://github.com/rysweet/RabbitHole/pull/211",
]

SAVE_DIAGNOSTICS_WAVE_PR_LINKS = [
    "https://github.com/rysweet/RabbitHole/pull/212",
    "https://github.com/rysweet/eatme/pull/118",
]

LATEST_PROOF_REPORTING_WAVE_PR_LINKS = [
    "https://github.com/rysweet/RabbitHole/pull/214",
    "https://github.com/rysweet/RabbitHole/pull/215",
    "https://github.com/rysweet/RabbitHole/pull/216",
    "https://github.com/rysweet/RabbitHole/pull/218",
    "https://github.com/rysweet/eatme/pull/120",
    "https://github.com/rysweet/eatme/pull/121",
]

RABBITHOLE_COMPLETED_SOURCE_WAVE_PR_LINKS = [
    "https://github.com/rysweet/RabbitHole/pull/219",
    "https://github.com/rysweet/RabbitHole/pull/222",
    "https://github.com/rysweet/RabbitHole/pull/224",
    "https://github.com/rysweet/RabbitHole/pull/225",
    "https://github.com/rysweet/RabbitHole/pull/229",
    "https://github.com/rysweet/RabbitHole/pull/230",
    "https://github.com/rysweet/RabbitHole/pull/231",
    "https://github.com/rysweet/RabbitHole/pull/234",
]

RABBITHOLE_NEW_SOURCE_WAVE_PR_LINKS = [
    "https://github.com/rysweet/RabbitHole/pull/235",
    "https://github.com/rysweet/RabbitHole/pull/237",
    "https://github.com/rysweet/RabbitHole/pull/238",
    "https://github.com/rysweet/RabbitHole/pull/240",
    "https://github.com/rysweet/RabbitHole/pull/241",
    "https://github.com/rysweet/RabbitHole/pull/245",
    "https://github.com/rysweet/RabbitHole/pull/246",
    "https://github.com/rysweet/RabbitHole/pull/247",
    "https://github.com/rysweet/RabbitHole/pull/250",
    "https://github.com/rysweet/RabbitHole/pull/253",
    "https://github.com/rysweet/RabbitHole/pull/254",
    "https://github.com/rysweet/RabbitHole/pull/255",
    "https://github.com/rysweet/RabbitHole/pull/259",
]

RABBITHOLE_LATEST_WAVE_PR_LINKS = [
    "https://github.com/rysweet/RabbitHole/pull/260",
    "https://github.com/rysweet/RabbitHole/pull/261",
    "https://github.com/rysweet/RabbitHole/pull/262",
    "https://github.com/rysweet/eatme/pull/122",
]

EATME_PR123_WAVE_PR_LINKS = [
    "https://github.com/rysweet/eatme/pull/123",
]

RABBITHOLE_PR264_EATME_PR124_WAVE_PR_LINKS = [
    "https://github.com/rysweet/RabbitHole/pull/264",
    "https://github.com/rysweet/eatme/pull/124",
]

RABBITHOLE_PR265_PR266_PR267_WAVE_PR_LINKS = [
    "https://github.com/rysweet/RabbitHole/pull/265",
    "https://github.com/rysweet/RabbitHole/pull/266",
    "https://github.com/rysweet/RabbitHole/pull/267",
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
    + LATEST_SOURCE_WAVE_PR_LINKS
    + SAVE_DIAGNOSTICS_WAVE_PR_LINKS
    + LATEST_PROOF_REPORTING_WAVE_PR_LINKS
    + RABBITHOLE_COMPLETED_SOURCE_WAVE_PR_LINKS
    + RABBITHOLE_NEW_SOURCE_WAVE_PR_LINKS
    + RABBITHOLE_LATEST_WAVE_PR_LINKS
    + EATME_PR123_WAVE_PR_LINKS
    + RABBITHOLE_PR264_EATME_PR124_WAVE_PR_LINKS
    + RABBITHOLE_PR265_PR266_PR267_WAVE_PR_LINKS
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
    "RabbitHole PR #209": [
        "RabbitHole PR #209",
        "Merged",
        "02e50a00078e8ff348aa33b8c8635483f9b817bf",
        "new WholeNumber[2]",
        "non-literal sizes still fail clearly",
        "broader array expressions",
        "method and constructor bodies",
        "non-null resource initializers",
        "full Tweedle decode remain unproven",
    ],
    "RabbitHole PR #210": [
        "RabbitHole PR #210",
        "Merged",
        "d2cba4ba3e349c704765129511de5a062210ec08",
        "launcher/runtime proof",
        "Program.main",
        "null-Stage guard",
        "visible rendering",
        "deployed installer success",
        "full world execution",
    ],
    "RabbitHole PR #211": [
        "RabbitHole PR #211",
        "Merged",
        "9b509aa3e60e6cf60b5e870a3ee03a0a80363f89",
        "story-api keyboard event",
        "4.55%",
        "6.21%",
        "260 covered lines",
        "70 percent aggregate coverage target",
        "manual QA gaps",
        "smoke checks that still need manual approval",
    ],

    "RabbitHole PR #212": [
        "RabbitHole PR #212",
        "Merged",
        "db72e0cfef8912cd0a92243f1889ae4cd2180535",
        "a84346582aef22c51d3afa33a05df26b62e370c7",
        "Save dialog/control target evidence",
        "focused Save tests",
        "focused review",
        "package-netbeans",
        "GitGuardian",
        "live desktop Save menu invocation",
        "actual Save dialog discovery/control",
    ],
    "eatme PR #118": [
        "eatme PR #118",
        "Merged",
        "2c760511eeff8c554b17ee550e779e7c51444591",
        "b70048d78f0b5f8669dc7e725cdac6b1ff3566f5",
        "Alice window action diagnostics",
        "CI passed",
        "manual real Alice smoke check was skipped",
        "real desktop environment still needs proving",
        "later procedure edit, run, and save automation remains incomplete",
    ],

    "RabbitHole PR #214": [
        "RabbitHole PR #214",
        "Merged",
        "2155904f38e55323b00d732b7f64e957db4406f5",
        "launcher drawing surface readiness",
        "Stage.show()",
        "isShowing()",
        "render-target-unavailable",
        "visible pixels",
        "deployed installer success",
        "full world execution",
    ],
    "RabbitHole PR #215": [
        "RabbitHole PR #215",
        "Merged",
        "c727d97c3d71a0f045925a691a080a42d36fbe9d",
        "empty `void` Tweedle methods",
        "AST `UserMethod`",
        "parameters",
        "method bodies",
        "non-void methods",
        "constructors still fail clearly",
    ],
    "RabbitHole PR #216": [
        "RabbitHole PR #216",
        "Merged",
        "c84bdf826723284e84b4872ce2e6c791dee0c8a6",
        "Save dialog discovery target evidence",
        "live Save menu click",
        "actual dialog display/control",
        "selected path automation",
    ],
    "RabbitHole PR #218": [
        "RabbitHole PR #218",
        "Merged",
        "a568bae3c3960c60792351cfa423450fea51b067",
        "launcher render observation proof",
        "visible pixels remain unobserved",
        "deployed installer success",
        "full world execution",
    ],
    "eatme PR #120": [
        "eatme PR #120",
        "Merged",
        "f526544014ee8d368a623359f6bf97cce6588f7d",
        "next first-lesson action reporting/proof slice",
        "real desktop proof",
        "procedure edit/run/save UI automation",
        "manual real Alice smoke",
    ],
    "eatme PR #121": [
        "eatme PR #121",
        "Merged",
        "4ade2a5d6def4d7ad7be7691b9349a3f5c9ff61e",
        "real desktop proof reporting/status",
        "actual real desktop proof/manual Alice smoke",
        "project save",
        "full first-lesson completion",
    ],
    "RabbitHole PR #219": [
        "RabbitHole PR #219",
        "Merged",
        "144081e1067cd8795666e5ee8802f47fbfefe671",
        "empty no-argument Tweedle constructors",
        "AST `NamedUserConstructor`",
        "constructor parameters",
        "constructor bodies still failed clearly",
    ],
    "RabbitHole PR #222": [
        "RabbitHole PR #222",
        "Merged",
        "f749ed7cc92f7df4678e96bbb29bcbd0b09913b8",
        "SaveProjectOperation.fire(UserActivity)",
        "AbstractSaveOperation.perform",
        "StageIDE.getActiveInstance()",
    ],
    "RabbitHole PR #224": [
        "RabbitHole PR #224",
        "Merged",
        "1a3eae6937a7109f3608112a7fb40519e1a4f8d7",
        "JavaFX cannot open `DISPLAY` locally",
        "visible rendering correctness remains unproven",
    ],
    "RabbitHole PR #225": [
        "RabbitHole PR #225",
        "Merged",
        "db44c10bd017a5b7cc8eddc1cc82b1d1b90c8fb8",
        "required Tweedle constructor parameters",
        "AST `UserParameter`",
        "optional constructor parameters still fail clearly",
    ],
    "RabbitHole PR #229": [
        "RabbitHole PR #229",
        "Merged",
        "7953c8348272298e9cb85f2319fba6520ba51a32",
        "required parameters for empty `void` Tweedle methods",
        "AST `UserParameter`",
        "optional method parameters still fail clearly",
    ],
    "RabbitHole PR #230": [
        "RabbitHole PR #230",
        "Merged",
        "31d506f6af59ef736ccefad9aa7b793b3add6a3d",
        "status=action_invoked",
        "StageIDE=true",
        "ProjectDocumentFrame=true",
        "menu click",
        "completed save remains unproven",
    ],
    "RabbitHole PR #231": [
        "RabbitHole PR #231",
        "Merged",
        "622748401fe8ff00d81d3a2851faac153585b76c",
        "generated launcher Xvfb marker pixels",
        "real Alice desktop pixels were not observed",
        "org.alice.stageide.EntryPoint",
        "ClassNotFoundException",
    ],
    "RabbitHole PR #234": [
        "RabbitHole PR #234",
        "Merged",
        "45d937fbe1e9ddee74e7c2b89af31841fb38a202",
        "single primitive-literal Tweedle `return` method bodies",
        "AST `ReturnStatement`",
        "full method decode",
        "full Tweedle/player decode support remains unproven",
    ],
    "RabbitHole PR #235": [
        "RabbitHole PR #235",
        "Merged",
        "a6ebc43a0e09",
        "Save menu item dispatch",
        "Save action path",
        "Save dialog display",
        "Save dialog control",
    ],
    "RabbitHole PR #237": [
        "RabbitHole PR #237",
        "Merged",
        "70deb2e15967",
        "alice-ide",
        "org.alice.stageide.EntryPoint",
        "Maven exec classpath",
        "visible rendering",
    ],
    "RabbitHole PR #238": [
        "RabbitHole PR #238",
        "Merged",
        "f9c832b8a86e",
        "required method parameter identifier",
        "ParameterAccess",
        "full method body",
        "complete Tweedle decode support",
    ],
    "RabbitHole PR #240": [
        "RabbitHole PR #240",
        "Merged",
        "ae3d8de57aec",
        "x-window-inventory.json",
        "alice-window-not-found",
        "classpath",
    ],
    "RabbitHole PR #241": [
        "RabbitHole PR #241",
        "Merged",
        "d2ab990dffa8",
        "FileDialogUtilities.showSaveFileDialog",
        "selected-path automation",
        "symlink",
        "Save dialog display",
    ],
    "RabbitHole PR #245": [
        "RabbitHole PR #245",
        "Merged",
        "9cc5893d8b67",
        "application-root-error.json",
        "Application Root Error",
        "org.alice.ide.rootDirectory",
    ],
    "RabbitHole PR #246": [
        "RabbitHole PR #246",
        "Merged",
        "2fe47f4ebaea",
        "ProjectDocumentFrame.showSaveFileDialog",
        "FileDialogUtilities",
        "displayable",
        "JFrame",
        "Save dialog display",
    ],
    "RabbitHole PR #247": [
        "RabbitHole PR #247",
        "Merged",
        "0a75eb7a21f5",
        "constructor",
        "primitive-literal local variable declarations",
        "LocalDeclaration",
        "full Tweedle constructor",
    ],
    "RabbitHole PR #250": [
        "RabbitHole PR #250",
        "Merged",
        "c640c3fbd9ef",
        "rootDirectory",
        "org.alice.ide.rootDirectory",
        "core/resources/target/distribution",
        "Application Root Error",
    ],
    "RabbitHole PR #253": [
        "RabbitHole PR #253",
        "Merged",
        "39635ffd1010",
        "declared Tweedle fields",
        "FieldAccess",
        "field return",
        "player decode",
    ],
    "RabbitHole PR #254": [
        "RabbitHole PR #254",
        "Merged",
        "88e8cffffa7c",
        "License Agreement",
        "java.util.prefs",
        "license",
        "pixel",
    ],
    "RabbitHole PR #255": [
        "RabbitHole PR #255",
        "Merged",
        "c8d52a9a8865",
        "SaveOperationFlow",
        "saved_file_exists",
        "saved_file_size_bytes",
        "Save dialog",
        "desktop save-menu completion",
    ],
    "RabbitHole PR #259": [
        "RabbitHole PR #259",
        "Merged",
        "e5b0ac5fce21b4eee1e13ea5861d2e9cee538ca8",
        "this.field",
        "AST `FieldAccess`",
        "full Tweedle/player decode",
    ],
    "RabbitHole PR #260": [
        "RabbitHole PR #260",
        "Merged",
        "b553677c1225d704d1d951a59653fb0f66096139",
        "JFileChooser",
        "Xvfb",
        "java.awt.FileDialog",
        "StageIDE Save-menu-to-real-chooser",
    ],
    "RabbitHole PR #261": [
        "RabbitHole PR #261",
        "Merged",
        "97c1ae707544bd0ca89e711df92e7e45e6d377ac",
        "Select Project",
        "title",
        "class",
        "geometry",
        "selecting or opening a project",
    ],
    "RabbitHole PR #262": [
        "RabbitHole PR #262",
        "Merged",
        "9ef09e05402b2e0af9c07803eee92aa5db29b325",
        "primitive literal field assignments",
        "Tweedle method bodies",
        "unsupported-form",
        "full Tweedle/player decode",
    ],
    "eatme PR #122": [
        "eatme PR #122",
        "Merged",
        "41142db",
        "lost-robot-debug-museum",
        "reflective-debugger",
        "grading",
        "creative assessment",
    ],
    "eatme PR #123": [
        "eatme PR #123",
        "Merged",
        "773fb3df7a6ec234c5f317eefdfea82916ecd7bc",
        "weather-wizard-conditional-theater",
        "creative_new",
        "grading",
        "creative assessment",
    ],
    "RabbitHole PR #264": [
        "RabbitHole PR #264",
        "Merged",
        "a4386130d66b97feecdbcb5ab1b6bc765392deb3",
        "primitive literal field assignments",
        "Tweedle constructor bodies",
        "unsupported constructor assignment forms",
        "full Tweedle/player decode",
    ],
    "eatme PR #124": [
        "eatme PR #124",
        "Merged",
        "d3bb687145b6c9e38601703c691aa7f6bcbb4862",
        "alien-linguist-parameter-dialogue",
        "73 to 75",
        "grading",
        "creative assessment",
    ],
    "RabbitHole PR #265": [
        "RabbitHole PR #265",
        "Merged",
        "ead3a465a6c794f552edc32699f011242fc303d7",
        "DocumentFrame.showSaveFileDialog",
        "JFileChooser",
        "SwingFileDialog",
        "Save-menu-to-written-project",
    ],
    "RabbitHole PR #266": [
        "RabbitHole PR #266",
        "Merged",
        "2fe0ba4ef5d9",
        "AT-SPI",
        "libatk-wrapper",
        "exec:java",
        "Select Project",
    ],
    "RabbitHole PR #267": [
        "RabbitHole PR #267",
        "Merged",
        "2ca7aa1062ee",
        "local variable reassignment",
        "Tweedle method",
        "constructor bodies",
        "Tweedle/player decode support",
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
    r"PR\s*#?212[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?212",
    r"PR\s*#?118[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?118",
    r"PR\s*#?219[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"PR\s*#?222[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"PR\s*#?224[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"PR\s*#?225[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"PR\s*#?229[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"PR\s*#?230[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"PR\s*#?231[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"PR\s*#?234[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?219",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?222",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?224",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?225",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?229",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?230",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?231",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?234",
    r"PR\s*#?235[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"PR\s*#?237[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"PR\s*#?238[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"PR\s*#?240[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"PR\s*#?241[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"PR\s*#?245[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"PR\s*#?246[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"PR\s*#?247[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"PR\s*#?250[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"PR\s*#?253[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"PR\s*#?254[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"PR\s*#?255[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"PR\s*#?259[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?235",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?237",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?238",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?240",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?241",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?245",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?246",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?247",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?250",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?253",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?254",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?255",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?259",
    r"PR\s*#?260[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"PR\s*#?261[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"PR\s*#?262[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"PR\s*#?264[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?260",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?261",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?262",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?264",
    r"PR\s*#?265[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"PR\s*#?266[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"PR\s*#?267[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?265",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?266",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?267",
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
        entry_0096_link = "journal/0096-rabbithole-pr209-pr210-pr211-source-wave-status.md"
        entry_0097_link = "journal/0097-rabbithole-pr212-eatme-pr118-save-diagnostics-status.md"
        entry_0098_link = "journal/0098-rabbithole-pr214-pr215-pr216-pr218-eatme-pr120-pr121-status.md"
        entry_0099_link = "journal/0099-rabbithole-pr219-pr222-pr224-pr225-pr229-pr230-pr231-pr234-status.md"
        entry_0100_link = "journal/0100-rabbithole-pr235-through-pr259-status.md"
        entry_0101_link = "journal/0101-rabbithole-pr260-pr261-pr262-eatme-pr122-status.md"

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
        self.assertEqual(1, text.count(entry_0096_link))
        self.assertIn("RabbitHole PR #209/#210/#211 source wave status", text)
        self.assertIn("4.55% to 6.21%", text)
        self.assertIn("260 more covered lines", text)
        self.assertEqual(1, text.count(entry_0097_link))
        self.assertIn("RabbitHole PR #212 and eatme PR #118 Save diagnostics status", text)
        self.assertIn("Save dialog/control target evidence", text)
        self.assertIn("skipped manual real Alice smoke", plain(text))
        self.assertEqual(1, text.count(entry_0098_link))
        self.assertIn("RabbitHole PR #214/#215/#216/#218 and eatme PR #120/#121 status", text)
        self.assertIn("launcher drawing surface readiness", text)
        self.assertIn("empty `void` Tweedle method decoding", text)
        self.assertIn("visible pixels still", text)
        self.assertEqual(1, text.count(entry_0099_link))
        self.assertIn("RabbitHole PR #219/#222/#224/#225/#229/#230/#231/#234 status", text)
        self.assertIn("empty no-argument constructor decode", text)
        self.assertIn("Xvfb Save action proof", text)
        self.assertIn("real Alice desktop classpath blocker", text)
        self.assertEqual(1, text.count(entry_0100_link))
        self.assertIn("RabbitHole PR #235 through PR #259 status", text)
        self.assertIn("Save menu item dispatch proof", text)
        self.assertIn("Alice launch classpath fix", text)
        self.assertIn("completed Save-flow file write", text)
        self.assertEqual(1, text.count(entry_0101_link))
        self.assertIn("RabbitHole PR #260", text)
        self.assertIn("JFileChooser", text)
        self.assertIn("Select Project", text)
        self.assertIn("lost-robot-debug-museum", text)
        entry_0102_link = "journal/0102-eatme-pr123-weather-wizard-status.md"
        entry_0103_link = "journal/0103-rabbithole-pr264-eatme-pr124-status.md"
        self.assertEqual(1, text.count(entry_0102_link))
        self.assertIn("weather-wizard-conditional-theater", text)
        self.assertEqual(1, text.count(entry_0103_link))
        self.assertIn("alien-linguist-parameter-dialogue", text)
        self.assertIn("Tweedle constructor bodies", text)
        entry_0104_link = "journal/0104-rabbithole-pr265-pr266-pr267-status.md"
        self.assertEqual(1, text.count(entry_0104_link))
        self.assertIn("DocumentFrame.showSaveFileDialog", text)
        self.assertIn("AT-SPI", text)
        self.assertIn("local variable reassignment", text)

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


    def test_0096_current_merge_status_and_boundaries_are_explicit(self):
        text = self.docs["atlas entry 0096"]

        requirements = {
            key: MERGED_CURRENT_PR_REQUIREMENTS[key]
            for key in ["RabbitHole PR #209", "RabbitHole PR #210", "RabbitHole PR #211"]
        }
        self.assert_contains_all(text, LATEST_SOURCE_WAVE_PR_LINKS, "atlas entry 0096")
        self.assert_contains_all(text, ENTRY_TRACEABILITY_LINKS, "atlas entry 0096")
        self.assert_current_merge_status_is_plain(text, "atlas entry 0096", requirements)
        self.assert_current_unproven_behaviors_are_explicit(text, "atlas entry 0096")
        self.assert_no_stale_status_for_current_prs(text, "atlas entry 0096")
        self.assertIn("new WholeNumber[2]", text)
        self.assertIn("non-literal sizes still fail clearly", text)
        self.assertIn("launcher/runtime proof", text)
        self.assertIn("null-Stage guard", text)
        self.assertIn("story-api keyboard event", text)
        self.assertIn("4.55% to 6.21%", text)
        self.assertIn("260 covered lines", text)
        self.assertIn("smoke checks that still need manual approval", text)

    def test_0097_current_merge_status_and_boundaries_are_explicit(self):
        text = self.docs["atlas entry 0097"]

        requirements = {
            key: MERGED_CURRENT_PR_REQUIREMENTS[key]
            for key in ["RabbitHole PR #212", "eatme PR #118"]
        }
        self.assert_contains_all(text, SAVE_DIAGNOSTICS_WAVE_PR_LINKS, "atlas entry 0097")
        self.assert_contains_all(text, ENTRY_TRACEABILITY_LINKS, "atlas entry 0097")
        self.assert_current_merge_status_is_plain(text, "atlas entry 0097", requirements)
        self.assert_current_unproven_behaviors_are_explicit(text, "atlas entry 0097")
        self.assert_no_stale_status_for_current_prs(text, "atlas entry 0097")
        self.assertIn("Save dialog/control target evidence", text)
        self.assertIn("focused Save tests", text)
        self.assertIn("focused review", text)
        self.assertIn("manual real Alice smoke check was skipped", text)
        self.assertIn("Actual Save dialog discovery/control remains unproven", text)


    def test_0098_current_merge_status_and_boundaries_are_explicit(self):
        text = self.docs["atlas entry 0098"]

        requirements = {
            key: MERGED_CURRENT_PR_REQUIREMENTS[key]
            for key in [
                "RabbitHole PR #214",
                "RabbitHole PR #215",
                "RabbitHole PR #216",
                "RabbitHole PR #218",
                "eatme PR #120",
                "eatme PR #121",
            ]
        }
        self.assert_contains_all(text, LATEST_PROOF_REPORTING_WAVE_PR_LINKS, "atlas entry 0098")
        self.assert_contains_all(text, ENTRY_TRACEABILITY_LINKS, "atlas entry 0098")
        self.assert_current_merge_status_is_plain(text, "atlas entry 0098", requirements)
        self.assert_current_unproven_behaviors_are_explicit(text, "atlas entry 0098")
        self.assert_no_stale_status_for_current_prs(text, "atlas entry 0098")
        self.assertIn("Stage.show()", text)
        self.assertIn("isShowing()", text)
        self.assertIn("render-target-unavailable", text)
        self.assertIn("AST `UserMethod`", text)
        self.assertIn("Save dialog discovery target evidence", text)
        self.assertIn("visible pixels remain unobserved", text)
        self.assertIn("manual real Alice smoke check was skipped", text)
        self.assertIn("project save", text)

    def test_0099_current_merge_status_and_boundaries_are_explicit(self):
        text = self.docs["atlas entry 0099"]

        requirements = {
            key: MERGED_CURRENT_PR_REQUIREMENTS[key]
            for key in [
                "RabbitHole PR #219",
                "RabbitHole PR #222",
                "RabbitHole PR #224",
                "RabbitHole PR #225",
                "RabbitHole PR #229",
                "RabbitHole PR #230",
                "RabbitHole PR #231",
                "RabbitHole PR #234",
            ]
        }
        self.assert_contains_all(text, RABBITHOLE_COMPLETED_SOURCE_WAVE_PR_LINKS, "atlas entry 0099")
        self.assert_contains_all(text, ENTRY_TRACEABILITY_LINKS, "atlas entry 0099")
        self.assert_current_merge_status_is_plain(text, "atlas entry 0099", requirements)
        self.assert_current_unproven_behaviors_are_explicit(text, "atlas entry 0099")
        self.assert_no_stale_status_for_current_prs(text, "atlas entry 0099")
        self.assertIn("NamedUserConstructor", text)
        self.assertIn("SaveProjectOperation.fire(UserActivity)", text)
        self.assertIn("StageIDE.getActiveInstance()", text)
        self.assertIn("JavaFX cannot open `DISPLAY` locally", text)
        self.assertIn("status=action_invoked", text)
        self.assertIn("ProjectDocumentFrame=true", text)
        self.assertIn("ClassNotFoundException", text)
        self.assertIn("AST `ReturnStatement`", text)

    def test_0100_current_merge_status_and_boundaries_are_explicit(self):
        text = self.docs["atlas entry 0100"]

        requirements = {
            key: MERGED_CURRENT_PR_REQUIREMENTS[key]
            for key in [
                "RabbitHole PR #235",
                "RabbitHole PR #237",
                "RabbitHole PR #238",
                "RabbitHole PR #240",
                "RabbitHole PR #241",
                "RabbitHole PR #245",
                "RabbitHole PR #246",
                "RabbitHole PR #247",
                "RabbitHole PR #250",
                "RabbitHole PR #253",
                "RabbitHole PR #254",
                "RabbitHole PR #255",
                "RabbitHole PR #259",
            ]
        }
        self.assert_contains_all(text, RABBITHOLE_NEW_SOURCE_WAVE_PR_LINKS, "atlas entry 0100")
        self.assert_contains_all(text, ENTRY_TRACEABILITY_LINKS, "atlas entry 0100")
        self.assert_current_merge_status_is_plain(text, "atlas entry 0100", requirements)
        self.assert_current_unproven_behaviors_are_explicit(text, "atlas entry 0100")
        self.assert_no_stale_status_for_current_prs(text, "atlas entry 0100")
        self.assertIn("Save menu item dispatch", text)
        self.assertIn("org.alice.stageide.EntryPoint", text)
        self.assertIn("ParameterAccess", text)
        self.assertIn("x-window-inventory.json", text)
        self.assertIn("FileDialogUtilities.showSaveFileDialog", text)
        self.assertIn("application-root-error.json", text)
        self.assertIn("ProjectDocumentFrame.showSaveFileDialog", text)
        self.assertIn("LocalDeclaration", text)
        self.assertIn("org.alice.ide.rootDirectory", text)
        self.assertIn("AST `FieldAccess`", text)
        self.assertIn("saved_file_exists", text)
        self.assertIn("this.field", text)
        self.assertIn("e5b0ac5fce21b4eee1e13ea5861d2e9cee538ca8", text)


        for name in CONTROL_DOCS:
            with self.subTest(document=name):
                self.assert_contains_all(plain(self.docs[name]), PROOF_BOUNDARY_TERMS, name)

    def test_0101_current_merge_status_and_boundaries_are_explicit(self):
        text = self.docs["atlas entry 0101"]

        requirements = {
            key: MERGED_CURRENT_PR_REQUIREMENTS[key]
            for key in [
                "RabbitHole PR #260",
                "RabbitHole PR #261",
                "RabbitHole PR #262",
                "eatme PR #122",
            ]
        }
        self.assert_contains_all(text, RABBITHOLE_LATEST_WAVE_PR_LINKS, "atlas entry 0101")
        self.assert_contains_all(text, ENTRY_TRACEABILITY_LINKS, "atlas entry 0101")
        self.assert_current_merge_status_is_plain(text, "atlas entry 0101", requirements)
        self.assert_current_unproven_behaviors_are_explicit(text, "atlas entry 0101")
        self.assert_no_stale_status_for_current_prs(text, "atlas entry 0101")
        self.assertIn("JFileChooser", text)
        self.assertIn("java.awt.FileDialog", text)
        self.assertIn("Select Project", text)
        self.assertIn("b553677c1225d704d1d951a59653fb0f66096139", text)
        self.assertIn("97c1ae707544bd0ca89e711df92e7e45e6d377ac", text)
        self.assertIn("9ef09e05402b2e0af9c07803eee92aa5db29b325", text)
        self.assertIn("lost-robot-debug-museum", text)
        self.assertIn("Primitive literal field assignments", text)
        self.assertIn("Full Tweedle/player decode", text)


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

    def test_0102_current_merge_status_and_boundaries_are_explicit(self):
        text = self.docs["atlas entry 0102"]

        requirements = {
            key: MERGED_CURRENT_PR_REQUIREMENTS[key]
            for key in [
                "eatme PR #123",
            ]
        }
        self.assert_contains_all(text, EATME_PR123_WAVE_PR_LINKS, "atlas entry 0102")
        self.assert_contains_all(text, ENTRY_TRACEABILITY_LINKS, "atlas entry 0102")
        self.assert_current_merge_status_is_plain(text, "atlas entry 0102", requirements)
        self.assert_current_unproven_behaviors_are_explicit(text, "atlas entry 0102")
        self.assertIn("weather-wizard-conditional-theater", text)
        self.assertIn("773fb3df7a6ec234c5f317eefdfea82916ecd7bc", text)
        self.assertIn("creative_new", text)
        self.assertIn("grading", text)
        self.assertIn("creative assessment", text)

    def test_0103_current_merge_status_and_boundaries_are_explicit(self):
        text = self.docs["atlas entry 0103"]

        requirements = {
            key: MERGED_CURRENT_PR_REQUIREMENTS[key]
            for key in [
                "RabbitHole PR #264",
                "eatme PR #124",
            ]
        }
        self.assert_contains_all(text, RABBITHOLE_PR264_EATME_PR124_WAVE_PR_LINKS, "atlas entry 0103")
        self.assert_contains_all(text, ENTRY_TRACEABILITY_LINKS, "atlas entry 0103")
        self.assert_current_merge_status_is_plain(text, "atlas entry 0103", requirements)
        self.assert_current_unproven_behaviors_are_explicit(text, "atlas entry 0103")
        self.assertIn("a4386130d66b97feecdbcb5ab1b6bc765392deb3", text)
        self.assertIn("d3bb687145b6c9e38601703c691aa7f6bcbb4862", text)
        self.assertIn("Tweedle constructor bodies", text)
        self.assertIn("alien-linguist-parameter-dialogue", text)
        self.assertIn("73 to 75", text)
        self.assertIn("grading", text)
        self.assertIn("creative assessment", text)

    def test_0104_current_merge_status_and_boundaries_are_explicit(self):
        text = self.docs["atlas entry 0104"]

        requirements = {
            key: MERGED_CURRENT_PR_REQUIREMENTS[key]
            for key in [
                "RabbitHole PR #265",
                "RabbitHole PR #266",
                "RabbitHole PR #267",
            ]
        }
        self.assert_contains_all(text, RABBITHOLE_PR265_PR266_PR267_WAVE_PR_LINKS, "atlas entry 0104")
        self.assert_contains_all(text, ENTRY_TRACEABILITY_LINKS, "atlas entry 0104")
        self.assert_current_merge_status_is_plain(text, "atlas entry 0104", requirements)
        self.assert_current_unproven_behaviors_are_explicit(text, "atlas entry 0104")
        self.assertIn("ead3a465a6c794f552edc32699f011242fc303d7", text)
        self.assertIn("DocumentFrame.showSaveFileDialog", text)
        self.assertIn("JFileChooser", text)
        self.assertIn("SwingFileDialog", text)
        self.assertIn("AT-SPI", text)
        self.assertIn("local variable reassignment", text)
        self.assertIn("Tweedle/player decode support", text)
        self.assertIn("first-lesson completion", text)

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
