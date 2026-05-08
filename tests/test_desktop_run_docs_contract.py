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
ENTRY_0105 = ROOT / "docs/atlas/journal/0105-eatme-pr125-ecosystem-balance-loop-status.md"
ENTRY_0106 = ROOT / "docs/atlas/journal/0106-eatme-pr126-rabbithole-pr269-status.md"
ENTRY_0107 = ROOT / "docs/atlas/journal/0107-eatme-pr127-mars-rover-proximity-mission-status.md"
ENTRY_0108 = ROOT / "docs/atlas/journal/0108-rabbithole-pr270-identifier-rhs-status.md"
ENTRY_0109 = ROOT / "docs/atlas/journal/0109-rabbithole-pr271-eatme-pr129-status.md"
ENTRY_0110 = ROOT / "docs/atlas/journal/0110-rabbithole-pr272-pr273-eatme-pr131-status.md"
ENTRY_0111 = ROOT / "docs/atlas/journal/0111-rabbithole-pr274-arithmetic-binary-status.md"
ENTRY_0112 = ROOT / "docs/atlas/journal/0112-rabbithole-pr276-save-menu-doclick-status.md"
ENTRY_0113 = ROOT / "docs/atlas/journal/0113-rabbithole-pr277-tweedle-string-concat-status.md"
ENTRY_0114 = ROOT / "docs/atlas/journal/0114-rabbithole-pr278-select-project-atapi-status.md"
ENTRY_0115 = ROOT / "docs/atlas/journal/0115-eatme-pr132-accessibility-rescue-camera-captions-status.md"
ENTRY_0116 = ROOT / "docs/atlas/journal/0116-rabbithole-pr281-save-proof-flag-fix-status.md"
ENTRY_0117 = ROOT / "docs/atlas/journal/0117-eatme-pr133-design-process-story-or-game-status.md"
ENTRY_0118 = ROOT / "docs/atlas/journal/0118-rabbithole-pr282-relational-comparison-status.md"
ENTRY_0119 = ROOT / "docs/atlas/journal/0119-rabbithole-pr284-save-proof-ordering-fix-status.md"
ENTRY_0120 = ROOT / "docs/atlas/journal/0120-rabbithole-pr285-atapi-main-window-post-project-open-status.md"
ENTRY_0121 = ROOT / "docs/atlas/journal/0121-eatme-pr134-setup-preflight-ready-to-create-status.md"
ENTRY_0122 = ROOT / "docs/atlas/journal/0122-eatme-pr135-audio-camera-and-export-sharecase-status.md"
ENTRY_0123 = ROOT / "docs/atlas/journal/0123-rabbithole-pr287-pr289-logical-expression-decode-status.md"
ENTRY_0124 = ROOT / "docs/atlas/journal/0124-rabbithole-pr290-scg-char-tests-status.md"
ENTRY_0125 = ROOT / "docs/atlas/journal/0125-eatme-pr136-next-missing-hook-path-status.md"
ENTRY_0126 = ROOT / "docs/atlas/journal/0126-rabbithole-pr291-conditional-statement-decode-status.md"
ENTRY_0127 = ROOT / "docs/atlas/journal/0127-rabbithole-pr292-file-menu-save-navigation-proof-status.md"
ENTRY_0128 = ROOT / "docs/atlas/journal/0128-rabbithole-pr293-while-loop-decode-status.md"
ENTRY_0129 = ROOT / "docs/atlas/journal/0129-four-pr-merged-metadata-status.md"
ENTRY_0130 = ROOT / "docs/atlas/journal/0130-rabbithole-306-308-evidence-status.md"
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
    "atlas entry 0105": ENTRY_0105,
    "atlas entry 0106": ENTRY_0106,
    "atlas entry 0107": ENTRY_0107,
    "atlas entry 0108": ENTRY_0108,
    "atlas entry 0109": ENTRY_0109,
    "atlas entry 0110": ENTRY_0110,
    "atlas entry 0111": ENTRY_0111,
    "atlas entry 0112": ENTRY_0112,
    "atlas entry 0113": ENTRY_0113,
    "atlas entry 0114": ENTRY_0114,
    "atlas entry 0115": ENTRY_0115,
    "atlas entry 0116": ENTRY_0116,
    "atlas entry 0117": ENTRY_0117,
    "atlas entry 0118": ENTRY_0118,
    "atlas entry 0119": ENTRY_0119,
    "atlas entry 0120": ENTRY_0120,
    "atlas entry 0121": ENTRY_0121,
    "atlas entry 0122": ENTRY_0122,
    "atlas entry 0123": ENTRY_0123,
    "atlas entry 0124": ENTRY_0124,
    "atlas entry 0125": ENTRY_0125,
    "atlas entry 0126": ENTRY_0126,
    "atlas entry 0127": ENTRY_0127,
    "atlas entry 0128": ENTRY_0128,
    "atlas entry 0129": ENTRY_0129,
    "atlas entry 0130": ENTRY_0130,
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
    "[atlas journal entry 0105](docs/atlas/journal/0105-eatme-pr125-ecosystem-balance-loop-status.md)",
    "[atlas journal entry 0106](docs/atlas/journal/0106-eatme-pr126-rabbithole-pr269-status.md)",
    "[atlas journal entry 0107](docs/atlas/journal/0107-eatme-pr127-mars-rover-proximity-mission-status.md)",
    "[atlas journal entry 0108](docs/atlas/journal/0108-rabbithole-pr270-identifier-rhs-status.md)",
    "[atlas journal entry 0109](docs/atlas/journal/0109-rabbithole-pr271-eatme-pr129-status.md)",
    "[atlas journal entry 0110](docs/atlas/journal/0110-rabbithole-pr272-pr273-eatme-pr131-status.md)",
    "[atlas journal entry 0111](docs/atlas/journal/0111-rabbithole-pr274-arithmetic-binary-status.md)",
    "[atlas journal entry 0112](docs/atlas/journal/0112-rabbithole-pr276-save-menu-doclick-status.md)",
    "[atlas journal entry 0113](docs/atlas/journal/0113-rabbithole-pr277-tweedle-string-concat-status.md)",
    "[atlas journal entry 0114](docs/atlas/journal/0114-rabbithole-pr278-select-project-atapi-status.md)",
    "[atlas journal entry 0115](docs/atlas/journal/0115-eatme-pr132-accessibility-rescue-camera-captions-status.md)",
    "[atlas journal entry 0116](docs/atlas/journal/0116-rabbithole-pr281-save-proof-flag-fix-status.md)",
    "[atlas journal entry 0117](docs/atlas/journal/0117-eatme-pr133-design-process-story-or-game-status.md)",
    "[atlas journal entry 0118](docs/atlas/journal/0118-rabbithole-pr282-relational-comparison-status.md)",
    "[atlas journal entry 0119](docs/atlas/journal/0119-rabbithole-pr284-save-proof-ordering-fix-status.md)",
    "[atlas journal entry 0120](docs/atlas/journal/0120-rabbithole-pr285-atapi-main-window-post-project-open-status.md)",
    "[atlas journal entry 0121](docs/atlas/journal/0121-eatme-pr134-setup-preflight-ready-to-create-status.md)",
    "[atlas journal entry 0122](docs/atlas/journal/0122-eatme-pr135-audio-camera-and-export-sharecase-status.md)",
    "[atlas journal entry 0123](docs/atlas/journal/0123-rabbithole-pr287-pr289-logical-expression-decode-status.md)",
    "[atlas journal entry 0124](docs/atlas/journal/0124-rabbithole-pr290-scg-char-tests-status.md)",
    "[atlas journal entry 0125](docs/atlas/journal/0125-eatme-pr136-next-missing-hook-path-status.md)",
    "[atlas journal entry 0126](docs/atlas/journal/0126-rabbithole-pr291-conditional-statement-decode-status.md)",
    "[atlas journal entry 0127](docs/atlas/journal/0127-rabbithole-pr292-file-menu-save-navigation-proof-status.md)",
    "[atlas journal entry 0128](docs/atlas/journal/0128-rabbithole-pr293-while-loop-decode-status.md)",
    "[atlas journal entry 0129](docs/atlas/journal/0129-four-pr-merged-metadata-status.md)",
    "[atlas journal entry 0130](docs/atlas/journal/0130-rabbithole-306-308-evidence-status.md)",
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

EATME_PR125_WAVE_PR_LINKS = [
    "https://github.com/rysweet/eatme/pull/125",
]

RABBITHOLE_PR269_EATME_PR126_WAVE_PR_LINKS = [
    "https://github.com/rysweet/RabbitHole/pull/269",
    "https://github.com/rysweet/eatme/pull/126",
]

EATME_PR127_WAVE_PR_LINKS = [
    "https://github.com/rysweet/eatme/pull/127",
]

RABBITHOLE_PR270_WAVE_PR_LINKS = [
    "https://github.com/rysweet/RabbitHole/pull/270",
]

RABBITHOLE_PR271_EATME_PR129_WAVE_PR_LINKS = [
    "https://github.com/rysweet/RabbitHole/pull/271",
    "https://github.com/rysweet/eatme/pull/129",
]

RABBITHOLE_PR272_PR273_EATME_PR131_WAVE_PR_LINKS = [
    "https://github.com/rysweet/RabbitHole/pull/272",
    "https://github.com/rysweet/RabbitHole/pull/273",
    "https://github.com/rysweet/eatme/pull/131",
]

RABBITHOLE_PR274_WAVE_PR_LINKS = [
    "https://github.com/rysweet/RabbitHole/pull/274",
]

RABBITHOLE_PR276_WAVE_PR_LINKS = [
    "https://github.com/rysweet/RabbitHole/pull/276",
]

RABBITHOLE_PR277_WAVE_PR_LINKS = [
    "https://github.com/rysweet/RabbitHole/pull/277",
]

RABBITHOLE_PR278_WAVE_PR_LINKS = [
    "https://github.com/rysweet/RabbitHole/pull/278",
]

EATME_PR132_WAVE_PR_LINKS = [
    "https://github.com/rysweet/eatme/pull/132",
]

RABBITHOLE_PR281_WAVE_PR_LINKS = [
    "https://github.com/rysweet/RabbitHole/pull/281",
]

EATME_PR133_WAVE_PR_LINKS = [
    "https://github.com/rysweet/eatme/pull/133",
]

RABBITHOLE_PR282_WAVE_PR_LINKS = [
    "https://github.com/rysweet/RabbitHole/pull/282",
]

RABBITHOLE_PR284_WAVE_PR_LINKS = [
    "https://github.com/rysweet/RabbitHole/pull/284",
]

RABBITHOLE_PR285_WAVE_PR_LINKS = [
    "https://github.com/rysweet/RabbitHole/pull/285",
]

EATME_PR134_WAVE_PR_LINKS = [
    "https://github.com/rysweet/eatme/pull/134",
]

EATME_PR135_WAVE_PR_LINKS = [
    "https://github.com/rysweet/eatme/pull/135",
]

RABBITHOLE_PR287_PR289_WAVE_PR_LINKS = [
    "https://github.com/rysweet/RabbitHole/pull/287",
    "https://github.com/rysweet/RabbitHole/pull/289",
]

RABBITHOLE_PR290_WAVE_PR_LINKS = [
    "https://github.com/rysweet/RabbitHole/pull/290",
]

EATME_PR136_WAVE_PR_LINKS = [
    "https://github.com/rysweet/eatme/pull/136",
]

RABBITHOLE_PR291_WAVE_PR_LINKS = [
    "https://github.com/rysweet/RabbitHole/pull/291",
]

RABBITHOLE_PR292_WAVE_PR_LINKS = [
    "https://github.com/rysweet/RabbitHole/pull/292",
]

RABBITHOLE_PR293_WAVE_PR_LINKS = [
    "https://github.com/rysweet/RabbitHole/pull/293",
]

FOUR_PR_MERGED_METADATA_LINKS = [
    "https://github.com/rysweet/RabbitHole/pull/297",
    "https://github.com/rysweet/RabbitHole/pull/298",
    "https://github.com/rysweet/eatme/pull/138",
    "https://github.com/rysweet/amplihack-rs/pull/571",
]

RABBITHOLE_PR306_PR308_EVIDENCE_LINKS = [
    "https://github.com/rysweet/RabbitHole/pull/306",
    "https://github.com/rysweet/RabbitHole/pull/308",
]

RABBITHOLE_PR307_BOUNDED_LINKS = [
    "https://github.com/rysweet/RabbitHole/pull/307",
]

ACTIVE_FOLLOWUP_LINKS = [
    "https://github.com/rysweet/amplihack-rs/pull/575",
]

RABBITHOLE_306_308_EVIDENCE_TERMS = [
    "RabbitHole PR #306",
    "narrow ModelResourceExporter attribution evidence",
    "RabbitHole PR #308",
    "narrow headless generated Story API runtime-state evidence",
]

RABBITHOLE_306_308_APPROVED_WORDING = [
    "PR #306 is narrow ModelResourceExporter attribution evidence only.",
    "PR #308 is narrow headless generated Story API runtime-state evidence only.",
]

ACTIVE_FOLLOWUP_TERMS = [
    "amplihack-rs PR #575",
    "active follow-up work",
]

RABBITHOLE_PR307_BOUNDED_TERMS = [
    "RabbitHole PR #307",
    "PR #307 is merged bounded Project I/O recovery evidence only.",
]

ACTIVE_FOLLOWUP_STATUS_SENTENCE = (
    "amplihack-rs PR #575 remains active follow-up work."
)

PLANNED_BUILD_BOUNDARY_TERMS = [
    "RabbitHole PR #307 has landed as bounded evidence only",
    "amplihack-rs PR #575 is the supporting recipe pre-commit reliability work",
    "still to land",
]

CAPABILITY_BOUNDARY_SENTENCE = (
    "PR #306 and PR #308 do not prove visible rendering, JavaFX launch, "
    "animation playback, full world execution, grading, full UI automation, "
    "full lesson completion, or full Tweedle/player decode."
)

CAPABILITY_BOUNDARY_TERMS = [
    "do not prove visible rendering",
    "JavaFX launch",
    "animation playback",
    "full world execution",
    "grading",
    "full UI automation",
    "full lesson completion",
    "full Tweedle/player decode",
]

RABBITHOLE_306_308_CAPABILITIES = [
    "visible rendering",
    "JavaFX launch",
    "animation playback",
    "full world execution",
    "grading",
    "full UI automation",
    "full lesson completion",
    "full Tweedle/player decode",
]

RABBITHOLE_306_308_OVERCLAIM_VERBS = [
    "proves",
    "shows",
    "demonstrates",
    "confirms",
    "launches",
    "renders",
    "plays",
    "executes",
    "grades",
    "automates",
    "completes",
    "decodes",
]

RABBITHOLE_306_308_FORBIDDEN_OVERCLAIMS = [
    *(f"{capability} is proven" for capability in RABBITHOLE_306_308_CAPABILITIES),
    "full Tweedle/player decode support is complete",
    *(
        f"PR #{number} {verb} {capability}"
        for number in ("306", "308")
        for verb in RABBITHOLE_306_308_OVERCLAIM_VERBS
        for capability in RABBITHOLE_306_308_CAPABILITIES
    ),
]

RABBITHOLE_306_308_FORBIDDEN_OVERCLAIMS_NORMALIZED = [
    (claim, claim.lower()) for claim in RABBITHOLE_306_308_FORBIDDEN_OVERCLAIMS
]

FOUR_PR_MERGED_METADATA_TABLE_LINES = [
    "| Repository | PR | Status | Merged at | Merged by | Merge commit SHA | Head SHA |",
    "| --- | --- | --- | --- | --- | --- | --- |",
    "| `rysweet/RabbitHole` | [#297](https://github.com/rysweet/RabbitHole/pull/297) | `MERGED` | `2026-05-08T04:39:11Z` | `rysweet` | `527011aa8337222cddd05d23766edcac908a699b` | `59272ae077e3e614f3ef30a4b6b37140c8eb80f8` |",
    "| `rysweet/RabbitHole` | [#298](https://github.com/rysweet/RabbitHole/pull/298) | `MERGED` | `2026-05-08T02:32:51Z` | `rysweet` | `fb9da28c2dcaf426b87699ffceebaba7093d994a` | `6bd52537504d0f88cd0fe6c1919e5a4134eca2a8` |",
    "| `rysweet/eatme` | [#138](https://github.com/rysweet/eatme/pull/138) | `MERGED` | `2026-05-08T02:13:51Z` | `rysweet` | `b412458d6abf4d235dc03f4efb3debabd54e79d1` | `8cacd14cc51fc09cae20ee421f4bc4a8e285b751` |",
    "| `rysweet/amplihack-rs` | [#571](https://github.com/rysweet/amplihack-rs/pull/571) | `MERGED` | `2026-05-08T04:55:47Z` | `rysweet` | `0af6f12824778fbff94627dae5da92b57beb6fc9` | `33582d27e8cac3f00cbd7e702a5304c34768d41a` |",
]

RABBITHOLE_PR278_EATME_PR132_WAVE_PR_LINKS = (
    RABBITHOLE_PR278_WAVE_PR_LINKS + EATME_PR132_WAVE_PR_LINKS
)

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
    + EATME_PR125_WAVE_PR_LINKS
    + RABBITHOLE_PR269_EATME_PR126_WAVE_PR_LINKS
    + EATME_PR127_WAVE_PR_LINKS
    + RABBITHOLE_PR270_WAVE_PR_LINKS
    + RABBITHOLE_PR271_EATME_PR129_WAVE_PR_LINKS
    + RABBITHOLE_PR272_PR273_EATME_PR131_WAVE_PR_LINKS
    + RABBITHOLE_PR274_WAVE_PR_LINKS
    + RABBITHOLE_PR276_WAVE_PR_LINKS
    + RABBITHOLE_PR277_WAVE_PR_LINKS
    + RABBITHOLE_PR278_EATME_PR132_WAVE_PR_LINKS
    + RABBITHOLE_PR281_WAVE_PR_LINKS
    + EATME_PR133_WAVE_PR_LINKS
    + RABBITHOLE_PR282_WAVE_PR_LINKS
    + RABBITHOLE_PR284_WAVE_PR_LINKS
    + RABBITHOLE_PR285_WAVE_PR_LINKS
    + EATME_PR134_WAVE_PR_LINKS
    + EATME_PR135_WAVE_PR_LINKS
    + RABBITHOLE_PR287_PR289_WAVE_PR_LINKS
    + RABBITHOLE_PR290_WAVE_PR_LINKS
    + EATME_PR136_WAVE_PR_LINKS
    + RABBITHOLE_PR291_WAVE_PR_LINKS
    + RABBITHOLE_PR292_WAVE_PR_LINKS
    + RABBITHOLE_PR293_WAVE_PR_LINKS
    + FOUR_PR_MERGED_METADATA_LINKS
    + RABBITHOLE_PR306_PR308_EVIDENCE_LINKS
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
    "eatme PR #125": [
        "eatme PR #125",
        "Merged",
        "847c09d20be16435595e1368f8f96c495fc6e4f5",
        "ecosystem-balance-loop-simulation",
        "75 to 77",
        "grading",
        "creative assessment",
    ],
    "RabbitHole PR #269": [
        "RabbitHole PR #269",
        "Merged",
        "ce31df5c04401f7ddb759c9d6640ca2881f82c4f",
        "optional",
        "UserParameter",
        "full Tweedle",
    ],
    "eatme PR #126": [
        "eatme PR #126",
        "Merged",
        "72731e2e7dd092292f982408faad5a2e98d7e74a",
        "time-travel-recipe-sequencing",
        "77 to 79",
        "grading",
        "creative assessment",
    ],
    "eatme PR #127": [
        "eatme PR #127",
        "Merged",
        "e0c090f265f0dfb2f0b662616aac8b6cb078dae6",
        "mars-rover-proximity-mission",
        "79 to 81",
        "grading",
        "creative assessment",
    ],
    "RabbitHole PR #270": [
        "RabbitHole PR #270",
        "Merged",
        "b887a14e85a514b5bf7504eeffd3fbeff490e0a2",
        "IdentifierReference",
        "ParameterAccess",
        "Full Tweedle",
    ],
    "RabbitHole PR #271": [
        "RabbitHole PR #271",
        "Merged",
        "b49b898ddfd2c19a27ce88d265f2c723499b1454",
        "local variable declarations",
        "IdentifierReference",
        "LocalAccess",
        "Full Tweedle",
    ],
    "eatme PR #129": [
        "eatme PR #129",
        "Merged",
        "b72afe499c9b7a3826012b7d10c69b5ae6b6c0a1",
        "creature-choreography-loop-lab",
        "81 to 83",
        "grading",
        "creative assessment",
    ],
    "RabbitHole PR #272": [
        "RabbitHole PR #272",
        "Merged",
        "458bed0f4b409d207a2610b8ccfa8e8dfbbce6c9",
        "AT-SPI",
        "exec:exec",
        "tab labels",
    ],
    "RabbitHole PR #273": [
        "RabbitHole PR #273",
        "Merged",
        "c86e8c4747b73921e8c432709c8cf7a741848855",
        "SaveProjectOperation",
        "JFileChooser",
        ".a3p",
    ],
    "eatme PR #131": [
        "eatme PR #131",
        "Merged",
        "973b65f",
        "neighborhood-data-story",
        "83 to 85",
        "grading",
        "creative assessment",
    ],
    "RabbitHole PR #274": [
        "RabbitHole PR #274",
        "Merged",
        "5571894e5152482c9fb26ba31fc3d633d372e88e",
        "arithmetic",
        "binary",
    ],
    "RabbitHole PR #276": [
        "RabbitHole PR #276",
        "Merged",
        "66b38f87090f633f44a403737778c3c01a01c52b",
        "doClick",
        "JFileChooser",
        ".a3p",
    ],
    "RabbitHole PR #277": [
        "RabbitHole PR #277",
        "Merged",
        "8c1a3fd32c2c1d19aac7ea265909f0d19276273e",
        "string concatenation",
        "..",
    ],
    "RabbitHole PR #278": [
        "RabbitHole PR #278",
        "Merged",
        "e130dac3a6f6431895f72f71733a042f1bb92cb3",
        "AT-SPI",
        "toggle button",
        "projectOpenObserved",
    ],
    "eatme PR #132": [
        "eatme PR #132",
        "Merged",
        "ebaf93e85a502f4778aaa194f4cd61ae8ae4cdda",
        "accessibility-rescue-camera-captions",
        "87",
    ],
    "RabbitHole PR #281": [
        "RabbitHole PR #281",
        "Merged",
        "daaceb0a9648d18e890c5b106327d2ddbe489149",
        "approvedSelection",
        "approveSelection",
    ],
    "eatme PR #133": [
        "eatme PR #133",
        "Merged",
        "7d0d05726b970dc9a616ed8aa633e090ceebf88b",
        "design-process-story-or-game",
        "89",
    ],
    "RabbitHole PR #282": [
        "RabbitHole PR #282",
        "Merged",
        "81db4122fc3270e2a16a02c46c4a1d7f254717e3",
        "RelationalInfixExpression",
        "relational",
    ],
    "RabbitHole PR #284": [
        "RabbitHole PR #284",
        "Merged",
        "eca3fb920e3d2b13f5de7117ccc96308378a10f6",
        "approvedSelection",
        "SaveFileDialogShowControlProofTest",
    ],
    "RabbitHole PR #285": [
        "RabbitHole PR #285",
        "Merged",
        "8eaa066f98ab173bfa6d0d08f804b5e4eb47a7be",
        "projectOpenObserved",
        "post-project-open-probe",
    ],
    "eatme PR #134": [
        "eatme PR #134",
        "Merged",
        "294ca3319863098c11e3abd712dc661b44a6278e",
        "setup-preflight-ready-to-create",
        "91",
    ],
    "eatme PR #135": [
        "eatme PR #135",
        "Merged",
        "8f82d682aef4d22c3ca4e7bdc4344cae660b13bd",
        "audio-camera-and-export-sharecase",
        "93",
    ],
    "RabbitHole PR #287": [
        "RabbitHole PR #287",
        "Merged",
        "198b482733f3fcb9ae7ecfc5479027393f21cf71",
        "ConditionalInfixExpression",
        "LogicalComplement",
    ],
    "RabbitHole PR #289": [
        "RabbitHole PR #289",
        "Merged",
        "cc119baebb4dd5ad775ac497c9f2318b9f8d2add",
        "non-Boolean",
    ],
    "RabbitHole PR #290": [
        "RabbitHole PR #290",
        "Merged",
        "65c11f6",
        "SourceCodeGenerator",
        "while loop",
        "null literal",
        "array access",
        "array length",
    ],
    "eatme PR #136": [
        "eatme PR #136",
        "Merged",
        "next_missing_real_desktop_proof",
        "place-object",
        "edit-procedure-or-code-block",
        "run-world",
        "save-project",
    ],
    "RabbitHole PR #291": [
        "RabbitHole PR #291",
        "Merged",
        "0f00c088f20e489b5b3c43bdbdc29e078dfb6b9b",
        "ConditionalStatement",
        "BooleanExpressionBodyPair",
        "if",
        "void method bodies",
        "Local declarations",
    ],
    "RabbitHole PR #292": [
        "RabbitHole PR #292",
        "Merged",
        "17e82091",
        "FileMenuSaveNavigationProofTest",
        "FileMenuModel",
        "AliceMenuBar",
        "SaveProjectOperation",
        "menu_item_dispatched",
        "ActionEventTrigger",
    ],
    "RabbitHole PR #293": [
        "RabbitHole PR #293",
        "Merged",
        "3696670873c6a409046ac6e648e828d95956aa8b",
        "WhileLoop",
        "void method bodies",
    ],
    "RabbitHole PR #297": [
        "RabbitHole PR #297",
        "rysweet/RabbitHole",
        "MERGED",
        "2026-05-08T04:39:11Z",
        "527011aa8337222cddd05d23766edcac908a699b",
        "59272ae077e3e614f3ef30a4b6b37140c8eb80f8",
    ],
    "RabbitHole PR #298": [
        "RabbitHole PR #298",
        "rysweet/RabbitHole",
        "MERGED",
        "2026-05-08T02:32:51Z",
        "fb9da28c2dcaf426b87699ffceebaba7093d994a",
        "6bd52537504d0f88cd0fe6c1919e5a4134eca2a8",
    ],
    "RabbitHole PR #306": [
        "RabbitHole PR #306",
        "Merged",
        "2026-05-08T09:31:58Z",
        "narrow ModelResourceExporter attribution evidence",
        "do not prove visible rendering",
        "JavaFX launch",
        "animation playback",
        "full world execution",
        "full UI automation",
        "full lesson completion",
        "full Tweedle/player decode",
    ],
    "RabbitHole PR #308": [
        "RabbitHole PR #308",
        "Merged",
        "2026-05-08T09:15:55Z",
        "narrow headless generated Story API runtime-state evidence",
        "do not prove visible rendering",
        "JavaFX launch",
        "animation playback",
        "full world execution",
        "full UI automation",
        "full lesson completion",
        "full Tweedle/player decode",
    ],
    "eatme PR #138": [
        "eatme PR #138",
        "rysweet/eatme",
        "MERGED",
        "2026-05-08T02:13:51Z",
        "b412458d6abf4d235dc03f4efb3debabd54e79d1",
        "8cacd14cc51fc09cae20ee421f4bc4a8e285b751",
    ],
    "amplihack-rs PR #571": [
        "amplihack-rs PR #571",
        "rysweet/amplihack-rs",
        "MERGED",
        "2026-05-08T04:55:47Z",
        "0af6f12824778fbff94627dae5da92b57beb6fc9",
        "33582d27e8cac3f00cbd7e702a5304c34768d41a",
    ],
}

FOUR_PR_MERGED_METADATA_REQUIREMENTS = {
    "RabbitHole PR #297": MERGED_CURRENT_PR_REQUIREMENTS["RabbitHole PR #297"],
    "RabbitHole PR #298": MERGED_CURRENT_PR_REQUIREMENTS["RabbitHole PR #298"],
    "eatme PR #138": MERGED_CURRENT_PR_REQUIREMENTS["eatme PR #138"],
    "amplihack-rs PR #571": MERGED_CURRENT_PR_REQUIREMENTS["amplihack-rs PR #571"],
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
    r"PR\s*#?125[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?125",
    r"PR\s*#?272[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?272",
    r"PR\s*#?273[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?273",
    r"PR\s*#?131[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?131",
    r"PR\s*#?281[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?281",
    r"PR\s*#?133[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?133",
    r"PR\s*#?290[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?290",
    r"PR\s*#?136[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?136",
    r"PR\s*#?291[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?291",
    r"PR\s*#?297[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?297",
    r"PR\s*#?298[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?298",
    r"PR\s*#?306[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?306",
    r"PR\s*#?308[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?308",
    r"PR\s*#?138[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?138",
    r"PR\s*#?571[^.\n|]*(?:pending|waiting|under review|blocked on review|still needs review)",
    r"(?:pending|waiting|under review|blocked on review|still needs review)[^.\n|]*PR\s*#?571",
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


PLAIN_WHITESPACE_RE = re.compile(r"\s+")
MARKDOWN_LINK_RE = re.compile(r"\[(?P<label>[^\]]+)\]\([^)]+\)")


def plain(text):
    return PLAIN_WHITESPACE_RE.sub(" ", text.replace("**", " "))


def without_markdown_link_targets(text):
    def keep_label(match):
        return match.group("label")

    return MARKDOWN_LINK_RE.sub(keep_label, text)


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
        cls.plain_docs = {name: plain(text) for name, text in cls.docs.items()}
        cls.lower_plain_docs = {name: text.lower() for name, text in cls.plain_docs.items()}

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
        ordered_latest_entries = [
            "[atlas journal entry 0124](docs/atlas/journal/0124-rabbithole-pr290-scg-char-tests-status.md)",
            "[atlas journal entry 0125](docs/atlas/journal/0125-eatme-pr136-next-missing-hook-path-status.md)",
            "[atlas journal entry 0126](docs/atlas/journal/0126-rabbithole-pr291-conditional-statement-decode-status.md)",
            "[atlas journal entry 0127](docs/atlas/journal/0127-rabbithole-pr292-file-menu-save-navigation-proof-status.md)",
            "[atlas journal entry 0128](docs/atlas/journal/0128-rabbithole-pr293-while-loop-decode-status.md)",
            "[atlas journal entry 0129](docs/atlas/journal/0129-four-pr-merged-metadata-status.md)",
            "[atlas journal entry 0130](docs/atlas/journal/0130-rabbithole-306-308-evidence-status.md)",
        ]
        ordered_positions = [plan_summary.index(entry) for entry in ordered_latest_entries]
        self.assertEqual(sorted(ordered_positions), ordered_positions)

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
        entry_0105_link = "journal/0105-eatme-pr125-ecosystem-balance-loop-status.md"
        self.assertEqual(1, text.count(entry_0105_link))
        self.assertIn("ecosystem-balance-loop-simulation", text)
        self.assertIn("75 to 77", text)
        entry_0106_link = "journal/0106-eatme-pr126-rabbithole-pr269-status.md"
        self.assertEqual(1, text.count(entry_0106_link))
        self.assertIn("time-travel-recipe-sequencing", text)
        self.assertIn("77 to 79", text)
        entry_0107_link = "journal/0107-eatme-pr127-mars-rover-proximity-mission-status.md"
        self.assertEqual(1, text.count(entry_0107_link))
        self.assertIn("mars-rover-proximity-mission", text)
        self.assertIn("79 to 81", text)
        entry_0108_link = "journal/0108-rabbithole-pr270-identifier-rhs-status.md"
        self.assertEqual(1, text.count(entry_0108_link))
        self.assertIn("IdentifierReference", text)
        self.assertIn("ParameterAccess", text)
        entry_0109_link = "journal/0109-rabbithole-pr271-eatme-pr129-status.md"
        self.assertEqual(1, text.count(entry_0109_link))
        self.assertIn("creature-choreography-loop-lab", text)
        entry_0110_link = "journal/0110-rabbithole-pr272-pr273-eatme-pr131-status.md"
        self.assertEqual(1, text.count(entry_0110_link))
        self.assertIn("neighborhood-data-story", text)
        entry_0111_link = "journal/0111-rabbithole-pr274-arithmetic-binary-status.md"
        self.assertEqual(1, text.count(entry_0111_link))
        self.assertIn("arithmetic", text)
        entry_0112_link = "journal/0112-rabbithole-pr276-save-menu-doclick-status.md"
        self.assertEqual(1, text.count(entry_0112_link))
        self.assertIn("doClick", text)
        entry_0113_link = "journal/0113-rabbithole-pr277-tweedle-string-concat-status.md"
        self.assertEqual(1, text.count(entry_0113_link))
        self.assertIn("string concatenation", text)
        entry_0114_link = "journal/0114-rabbithole-pr278-select-project-atapi-status.md"
        self.assertEqual(1, text.count(entry_0114_link))
        self.assertIn("projectOpenObserved", text)
        entry_0115_link = "journal/0115-eatme-pr132-accessibility-rescue-camera-captions-status.md"
        self.assertEqual(1, text.count(entry_0115_link))
        self.assertIn("accessibility-rescue-camera-captions", text)
        entry_0116_link = "journal/0116-rabbithole-pr281-save-proof-flag-fix-status.md"
        self.assertEqual(1, text.count(entry_0116_link))
        self.assertIn("approvedSelection", text)
        entry_0117_link = "journal/0117-eatme-pr133-design-process-story-or-game-status.md"
        self.assertEqual(1, text.count(entry_0117_link))
        self.assertIn("design-process-story-or-game", text)
        self.assertIn("87 to 89", text)
        entry_0118_link = "journal/0118-rabbithole-pr282-relational-comparison-status.md"
        self.assertEqual(1, text.count(entry_0118_link))
        self.assertIn("RelationalInfixExpression", text)
        entry_0119_link = "journal/0119-rabbithole-pr284-save-proof-ordering-fix-status.md"
        self.assertEqual(1, text.count(entry_0119_link))
        entry_0120_link = "journal/0120-rabbithole-pr285-atapi-main-window-post-project-open-status.md"
        self.assertEqual(1, text.count(entry_0120_link))
        self.assertIn("post-project-open-probe", text)
        entry_0121_link = "journal/0121-eatme-pr134-setup-preflight-ready-to-create-status.md"
        self.assertEqual(1, text.count(entry_0121_link))
        self.assertIn("setup-preflight-ready-to-create", text)
        self.assertIn("89 to 91", text)
        entry_0122_link = "journal/0122-eatme-pr135-audio-camera-and-export-sharecase-status.md"
        self.assertEqual(1, text.count(entry_0122_link))
        self.assertIn("audio-camera-and-export-sharecase", text)
        self.assertIn("91 to 93", text)
        entry_0123_link = "journal/0123-rabbithole-pr287-pr289-logical-expression-decode-status.md"
        self.assertEqual(1, text.count(entry_0123_link))
        self.assertIn("ConditionalInfixExpression", text)
        self.assertIn("LogicalComplement", text)
        entry_0124_link = "journal/0124-rabbithole-pr290-scg-char-tests-status.md"
        self.assertEqual(1, text.count(entry_0124_link))
        self.assertIn("SourceCodeGenerator", text)
        entry_0125_link = "journal/0125-eatme-pr136-next-missing-hook-path-status.md"
        self.assertEqual(1, text.count(entry_0125_link))
        self.assertIn("next_missing_real_desktop_proof", text)
        entry_0126_link = "journal/0126-rabbithole-pr291-conditional-statement-decode-status.md"
        self.assertEqual(1, text.count(entry_0126_link))
        self.assertIn("ConditionalStatement", text)
        entry_0127_link = "journal/0127-rabbithole-pr292-file-menu-save-navigation-proof-status.md"
        self.assertEqual(1, text.count(entry_0127_link))
        self.assertIn("FileMenuSaveNavigationProofTest", text)
        self.assertIn("FileMenuModel", text)
        self.assertIn("menu_item_dispatched", text)
        entry_0128_link = "journal/0128-rabbithole-pr293-while-loop-decode-status.md"
        self.assertEqual(1, text.count(entry_0128_link))
        self.assertIn("WhileLoop", text)
        entry_0129_link = "journal/0129-four-pr-merged-metadata-status.md"
        self.assertEqual(1, text.count(entry_0129_link))
        self.assertIn("Four-PR merged metadata status", text)
        self.assertIn("RabbitHole PR #297", text)
        self.assertIn("RabbitHole PR #298", text)
        self.assertIn("eatme PR #138", text)
        self.assertIn("amplihack-rs PR #571", text)
        self.assertIn("merge commit SHA", text)
        entry_0130_link = "journal/0130-rabbithole-306-308-evidence-status.md"
        self.assertEqual(1, text.count(entry_0130_link))
        plain_text = plain(text)
        self.assert_contains_all(plain_text, RABBITHOLE_306_308_EVIDENCE_TERMS, "atlas index")
        self.assert_contains_all(plain_text, ACTIVE_FOLLOWUP_TERMS, "atlas index")
        self.assert_contains_all(plain_text, CAPABILITY_BOUNDARY_TERMS, "atlas index")

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

    def test_0105_current_merge_status_and_boundaries_are_explicit(self):
        text = self.docs["atlas entry 0105"]

        requirements = {
            key: MERGED_CURRENT_PR_REQUIREMENTS[key]
            for key in [
                "eatme PR #125",
            ]
        }
        self.assert_contains_all(text, EATME_PR125_WAVE_PR_LINKS, "atlas entry 0105")
        self.assert_contains_all(text, ENTRY_TRACEABILITY_LINKS, "atlas entry 0105")
        self.assert_current_merge_status_is_plain(text, "atlas entry 0105", requirements)
        self.assert_current_unproven_behaviors_are_explicit(text, "atlas entry 0105")
        self.assertIn("847c09d20be16435595e1368f8f96c495fc6e4f5", text)
        self.assertIn("ecosystem-balance-loop-simulation", text)
        self.assertIn("75 to 77", text)
        self.assertIn("grading", text)
        self.assertIn("creative assessment", text)

    def test_0106_current_merge_status_and_boundaries_are_explicit(self):
        text = self.docs["atlas entry 0106"]

        requirements = {
            key: MERGED_CURRENT_PR_REQUIREMENTS[key]
            for key in [
                "RabbitHole PR #269",
                "eatme PR #126",
            ]
        }
        self.assert_contains_all(text, RABBITHOLE_PR269_EATME_PR126_WAVE_PR_LINKS, "atlas entry 0106")
        self.assert_contains_all(text, ENTRY_TRACEABILITY_LINKS, "atlas entry 0106")
        self.assert_current_merge_status_is_plain(text, "atlas entry 0106", requirements)
        self.assert_current_unproven_behaviors_are_explicit(text, "atlas entry 0106")
        self.assertIn("ce31df5c04401f7ddb759c9d6640ca2881f82c4f", text)
        self.assertIn("72731e2e7dd092292f982408faad5a2e98d7e74a", text)
        self.assertIn("time-travel-recipe-sequencing", text)
        self.assertIn("77 to 79", text)
        self.assertIn("UserParameter", text)
        self.assertIn("grading", text)
        self.assertIn("creative assessment", text)

    def test_0107_current_merge_status_and_boundaries_are_explicit(self):
        text = self.docs["atlas entry 0107"]

        requirements = {
            key: MERGED_CURRENT_PR_REQUIREMENTS[key]
            for key in [
                "eatme PR #127",
            ]
        }
        self.assert_contains_all(text, EATME_PR127_WAVE_PR_LINKS, "atlas entry 0107")
        self.assert_contains_all(text, ENTRY_TRACEABILITY_LINKS, "atlas entry 0107")
        self.assert_current_merge_status_is_plain(text, "atlas entry 0107", requirements)
        self.assert_current_unproven_behaviors_are_explicit(text, "atlas entry 0107")
        self.assertIn("e0c090f265f0dfb2f0b662616aac8b6cb078dae6", text)
        self.assertIn("mars-rover-proximity-mission", text)
        self.assertIn("79 to 81", text)
        self.assertIn("grading", text)
        self.assertIn("creative assessment", text)

    def test_0108_current_merge_status_and_boundaries_are_explicit(self):
        text = self.docs["atlas entry 0108"]

        requirements = {
            key: MERGED_CURRENT_PR_REQUIREMENTS[key]
            for key in [
                "RabbitHole PR #270",
            ]
        }
        self.assert_contains_all(text, RABBITHOLE_PR270_WAVE_PR_LINKS, "atlas entry 0108")
        self.assert_contains_all(text, ENTRY_TRACEABILITY_LINKS, "atlas entry 0108")
        self.assert_current_merge_status_is_plain(text, "atlas entry 0108", requirements)
        self.assert_current_unproven_behaviors_are_explicit(text, "atlas entry 0108")
        self.assertIn("b887a14e85a514b5bf7504eeffd3fbeff490e0a2", text)
        self.assertIn("IdentifierReference", text)
        self.assertIn("ParameterAccess", text)
        self.assertIn("Full Tweedle", text)

    def test_0109_current_merge_status_and_boundaries_are_explicit(self):
        text = self.docs["atlas entry 0109"]

        requirements = {
            key: MERGED_CURRENT_PR_REQUIREMENTS[key]
            for key in [
                "RabbitHole PR #271",
                "eatme PR #129",
            ]
        }
        self.assert_contains_all(text, RABBITHOLE_PR271_EATME_PR129_WAVE_PR_LINKS, "atlas entry 0109")
        self.assert_contains_all(text, ENTRY_TRACEABILITY_LINKS, "atlas entry 0109")
        self.assert_current_merge_status_is_plain(text, "atlas entry 0109", requirements)
        self.assert_current_unproven_behaviors_are_explicit(text, "atlas entry 0109")
        self.assertIn("b49b898ddfd2c19a27ce88d265f2c723499b1454", text)
        self.assertIn("b72afe499c9b7a3826012b7d10c69b5ae6b6c0a1", text)
        self.assertIn("local variable declarations", text)
        self.assertIn("creature-choreography-loop-lab", text)
        self.assertIn("81 to 83", text)

    def test_0110_current_merge_status_and_boundaries_are_explicit(self):
        text = self.docs["atlas entry 0110"]

        requirements = {
            key: MERGED_CURRENT_PR_REQUIREMENTS[key]
            for key in [
                "RabbitHole PR #272",
                "RabbitHole PR #273",
                "eatme PR #131",
            ]
        }
        self.assert_contains_all(text, RABBITHOLE_PR272_PR273_EATME_PR131_WAVE_PR_LINKS, "atlas entry 0110")
        self.assert_contains_all(text, ENTRY_TRACEABILITY_LINKS, "atlas entry 0110")
        self.assert_current_merge_status_is_plain(text, "atlas entry 0110", requirements)
        self.assert_current_unproven_behaviors_are_explicit(text, "atlas entry 0110")
        self.assertIn("458bed0f4b409d207a2610b8ccfa8e8dfbbce6c9", text)
        self.assertIn("c86e8c4747b73921e8c432709c8cf7a741848855", text)
        self.assertIn("973b65f", text)
        self.assertIn("AT-SPI", text)
        self.assertIn("SaveProjectOperation", text)
        self.assertIn("neighborhood-data-story", text)
        self.assertIn("83 to 85", text)
        self.assertIn("tab labels", text)


        for name in CURRENT_MERGE_STATUS_DOCS:
            with self.subTest(document=name):
                text = self.docs[name]
                self.assert_contains_all(text, CURRENT_MERGED_PR_LINKS, name)
                self.assert_current_merge_status_is_plain(text, name)
                self.assert_current_unproven_behaviors_are_explicit(text, name)
                self.assert_no_stale_status_for_current_prs(text, name)

    def test_0111_current_merge_status_and_boundaries_are_explicit(self):
        text = self.docs["atlas entry 0111"]

        requirements = {
            key: MERGED_CURRENT_PR_REQUIREMENTS[key]
            for key in [
                "RabbitHole PR #274",
            ]
        }
        self.assert_contains_all(text, RABBITHOLE_PR274_WAVE_PR_LINKS, "atlas entry 0111")
        self.assert_contains_all(text, ENTRY_TRACEABILITY_LINKS, "atlas entry 0111")
        self.assert_current_merge_status_is_plain(text, "atlas entry 0111", requirements)
        self.assert_current_unproven_behaviors_are_explicit(text, "atlas entry 0111")
        self.assertIn("5571894e5152482c9fb26ba31fc3d633d372e88e", text)
        self.assertIn("arithmetic", text)
        self.assertIn("binary", text)

    def test_0112_current_merge_status_and_boundaries_are_explicit(self):
        text = self.docs["atlas entry 0112"]

        requirements = {
            key: MERGED_CURRENT_PR_REQUIREMENTS[key]
            for key in [
                "RabbitHole PR #276",
            ]
        }
        self.assert_contains_all(text, RABBITHOLE_PR276_WAVE_PR_LINKS, "atlas entry 0112")
        self.assert_contains_all(text, ENTRY_TRACEABILITY_LINKS, "atlas entry 0112")
        self.assert_current_merge_status_is_plain(text, "atlas entry 0112", requirements)
        self.assert_current_unproven_behaviors_are_explicit(text, "atlas entry 0112")
        self.assertIn("66b38f87090f633f44a403737778c3c01a01c52b", text)
        self.assertIn("doClick", text)
        self.assertIn("JFileChooser", text)
        self.assertIn(".a3p", text)

    def test_0113_current_merge_status_and_boundaries_are_explicit(self):
        text = self.docs["atlas entry 0113"]

        requirements = {
            key: MERGED_CURRENT_PR_REQUIREMENTS[key]
            for key in [
                "RabbitHole PR #277",
            ]
        }
        self.assert_contains_all(text, RABBITHOLE_PR277_WAVE_PR_LINKS, "atlas entry 0113")
        self.assert_contains_all(text, ENTRY_TRACEABILITY_LINKS, "atlas entry 0113")
        self.assert_current_merge_status_is_plain(text, "atlas entry 0113", requirements)
        self.assert_current_unproven_behaviors_are_explicit(text, "atlas entry 0113")
        self.assertIn("8c1a3fd32c2c1d19aac7ea265909f0d19276273e", text)
        self.assertIn("string concatenation", text)
        self.assertIn("..", text)

    def test_0114_current_merge_status_and_boundaries_are_explicit(self):
        text = self.docs["atlas entry 0114"]

        requirements = {
            key: MERGED_CURRENT_PR_REQUIREMENTS[key]
            for key in [
                "RabbitHole PR #278",
            ]
        }
        self.assert_contains_all(text, RABBITHOLE_PR278_WAVE_PR_LINKS, "atlas entry 0114")
        self.assert_contains_all(text, ENTRY_TRACEABILITY_LINKS, "atlas entry 0114")
        self.assert_current_merge_status_is_plain(text, "atlas entry 0114", requirements)
        self.assert_current_unproven_behaviors_are_explicit(text, "atlas entry 0114")
        self.assertIn("e130dac3a6f6431895f72f71733a042f1bb92cb3", text)
        self.assertIn("AT-SPI", text)
        self.assertIn("projectOpenObserved", text)

    def test_0115_current_merge_status_and_boundaries_are_explicit(self):
        text = self.docs["atlas entry 0115"]

        requirements = {
            key: MERGED_CURRENT_PR_REQUIREMENTS[key]
            for key in [
                "eatme PR #132",
            ]
        }
        self.assert_contains_all(text, EATME_PR132_WAVE_PR_LINKS, "atlas entry 0115")
        self.assert_contains_all(text, ENTRY_TRACEABILITY_LINKS, "atlas entry 0115")
        self.assert_current_merge_status_is_plain(text, "atlas entry 0115", requirements)
        self.assert_current_unproven_behaviors_are_explicit(text, "atlas entry 0115")
        self.assertIn("ebaf93e85a502f4778aaa194f4cd61ae8ae4cdda", text)
        self.assertIn("accessibility-rescue-camera-captions", text)
        self.assertIn("87", text)
        for name, text in self.docs.items():
            with self.subTest(document=name):
                prose = without_markdown_link_targets(text)
                for term in PLAIN_LANGUAGE_JARGON:
                    self.assertIsNone(
                        re.search(rf"\b{re.escape(term)}\b", prose, re.IGNORECASE),
                        f"{name} uses project jargon without plain-language explanation: {term}",
                    )

    def test_0116_current_merge_status_and_boundaries_are_explicit(self):
        text = self.docs["atlas entry 0116"]

        requirements = {
            key: MERGED_CURRENT_PR_REQUIREMENTS[key]
            for key in [
                "RabbitHole PR #281",
            ]
        }
        self.assert_contains_all(text, RABBITHOLE_PR281_WAVE_PR_LINKS, "atlas entry 0116")
        self.assert_contains_all(text, ENTRY_TRACEABILITY_LINKS, "atlas entry 0116")
        self.assert_current_merge_status_is_plain(text, "atlas entry 0116", requirements)
        self.assert_current_unproven_behaviors_are_explicit(text, "atlas entry 0116")
        self.assertIn("daaceb0a9648d18e890c5b106327d2ddbe489149", text)
        self.assertIn("approvedSelection", text)
        self.assertIn("approveSelection", text)

    def test_0117_current_merge_status_and_boundaries_are_explicit(self):
        text = self.docs["atlas entry 0117"]

        requirements = {
            key: MERGED_CURRENT_PR_REQUIREMENTS[key]
            for key in [
                "eatme PR #133",
            ]
        }
        self.assert_contains_all(text, EATME_PR133_WAVE_PR_LINKS, "atlas entry 0117")
        self.assert_contains_all(text, ENTRY_TRACEABILITY_LINKS, "atlas entry 0117")
        self.assert_current_merge_status_is_plain(text, "atlas entry 0117", requirements)
        self.assert_current_unproven_behaviors_are_explicit(text, "atlas entry 0117")
        self.assertIn("7d0d05726b970dc9a616ed8aa633e090ceebf88b", text)
        self.assertIn("design-process-story-or-game", text)
        self.assertIn("89", text)

    def test_0118_current_merge_status_and_boundaries_are_explicit(self):
        text = self.docs["atlas entry 0118"]

        requirements = {
            key: MERGED_CURRENT_PR_REQUIREMENTS[key]
            for key in [
                "RabbitHole PR #282",
            ]
        }
        self.assert_contains_all(text, RABBITHOLE_PR282_WAVE_PR_LINKS, "atlas entry 0118")
        self.assert_contains_all(text, ENTRY_TRACEABILITY_LINKS, "atlas entry 0118")
        self.assert_current_merge_status_is_plain(text, "atlas entry 0118", requirements)
        self.assert_current_unproven_behaviors_are_explicit(text, "atlas entry 0118")
        self.assertIn("81db4122fc3270e2a16a02c46c4a1d7f254717e3", text)
        self.assertIn("RelationalInfixExpression", text)
        self.assertIn("relational", text)

    def test_0119_current_merge_status_and_boundaries_are_explicit(self):
        text = self.docs["atlas entry 0119"]

        requirements = {
            key: MERGED_CURRENT_PR_REQUIREMENTS[key]
            for key in [
                "RabbitHole PR #284",
            ]
        }
        self.assert_contains_all(text, RABBITHOLE_PR284_WAVE_PR_LINKS, "atlas entry 0119")
        self.assert_contains_all(text, ENTRY_TRACEABILITY_LINKS, "atlas entry 0119")
        self.assert_current_merge_status_is_plain(text, "atlas entry 0119", requirements)
        self.assert_current_unproven_behaviors_are_explicit(text, "atlas entry 0119")
        self.assertIn("eca3fb920e3d2b13f5de7117ccc96308378a10f6", text)
        self.assertIn("approvedSelection", text)
        self.assertIn("SaveFileDialogShowControlProofTest", text)

    def test_0120_current_merge_status_and_boundaries_are_explicit(self):
        text = self.docs["atlas entry 0120"]

        requirements = {
            key: MERGED_CURRENT_PR_REQUIREMENTS[key]
            for key in [
                "RabbitHole PR #285",
            ]
        }
        self.assert_contains_all(text, RABBITHOLE_PR285_WAVE_PR_LINKS, "atlas entry 0120")
        self.assert_contains_all(text, ENTRY_TRACEABILITY_LINKS, "atlas entry 0120")
        self.assert_current_merge_status_is_plain(text, "atlas entry 0120", requirements)
        self.assert_current_unproven_behaviors_are_explicit(text, "atlas entry 0120")
        self.assertIn("8eaa066f98ab173bfa6d0d08f804b5e4eb47a7be", text)
        self.assertIn("projectOpenObserved", text)
        self.assertIn("post-project-open-probe", text)

    def test_0121_current_merge_status_and_boundaries_are_explicit(self):
        text = self.docs["atlas entry 0121"]

        requirements = {
            key: MERGED_CURRENT_PR_REQUIREMENTS[key]
            for key in [
                "eatme PR #134",
            ]
        }
        self.assert_contains_all(text, EATME_PR134_WAVE_PR_LINKS, "atlas entry 0121")
        self.assert_contains_all(text, ENTRY_TRACEABILITY_LINKS, "atlas entry 0121")
        self.assert_current_merge_status_is_plain(text, "atlas entry 0121", requirements)
        self.assert_current_unproven_behaviors_are_explicit(text, "atlas entry 0121")
        self.assertIn("294ca3319863098c11e3abd712dc661b44a6278e", text)
        self.assertIn("setup-preflight-ready-to-create", text)
        self.assertIn("91", text)

    def test_0122_current_merge_status_and_boundaries_are_explicit(self):
        text = self.docs["atlas entry 0122"]

        requirements = {
            key: MERGED_CURRENT_PR_REQUIREMENTS[key]
            for key in [
                "eatme PR #135",
            ]
        }
        self.assert_contains_all(text, EATME_PR135_WAVE_PR_LINKS, "atlas entry 0122")
        self.assert_contains_all(text, ENTRY_TRACEABILITY_LINKS, "atlas entry 0122")
        self.assert_current_merge_status_is_plain(text, "atlas entry 0122", requirements)
        self.assert_current_unproven_behaviors_are_explicit(text, "atlas entry 0122")
        self.assertIn("8f82d682aef4d22c3ca4e7bdc4344cae660b13bd", text)
        self.assertIn("audio-camera-and-export-sharecase", text)
        self.assertIn("93", text)

    def test_0123_current_merge_status_and_boundaries_are_explicit(self):
        text = self.docs["atlas entry 0123"]

        requirements = {
            key: MERGED_CURRENT_PR_REQUIREMENTS[key]
            for key in [
                "RabbitHole PR #287",
                "RabbitHole PR #289",
            ]
        }
        self.assert_contains_all(text, RABBITHOLE_PR287_PR289_WAVE_PR_LINKS, "atlas entry 0123")
        self.assert_contains_all(text, ENTRY_TRACEABILITY_LINKS, "atlas entry 0123")
        self.assert_current_merge_status_is_plain(text, "atlas entry 0123", requirements)
        self.assert_current_unproven_behaviors_are_explicit(text, "atlas entry 0123")
        self.assertIn("198b482733f3fcb9ae7ecfc5479027393f21cf71", text)
        self.assertIn("cc119baebb4dd5ad775ac497c9f2318b9f8d2add", text)
        self.assertIn("ConditionalInfixExpression", text)
        self.assertIn("LogicalComplement", text)
        self.assertIn("non-Boolean", text)

    def test_0124_current_merge_status_and_boundaries_are_explicit(self):
        text = self.docs["atlas entry 0124"]

        requirements = {
            key: MERGED_CURRENT_PR_REQUIREMENTS[key]
            for key in [
                "RabbitHole PR #290",
            ]
        }
        self.assert_contains_all(text, RABBITHOLE_PR290_WAVE_PR_LINKS, "atlas entry 0124")
        self.assert_contains_all(text, ENTRY_TRACEABILITY_LINKS, "atlas entry 0124")
        self.assert_current_merge_status_is_plain(text, "atlas entry 0124", requirements)
        self.assert_current_unproven_behaviors_are_explicit(text, "atlas entry 0124")
        self.assertIn("65c11f6", text)
        self.assertIn("SourceCodeGenerator", text)
        self.assertIn("while loop", text)
        self.assertIn("null literal", text)
        self.assertIn("array access", text)
        self.assertIn("array length", text)

    def test_0125_current_merge_status_and_boundaries_are_explicit(self):
        text = self.docs["atlas entry 0125"]

        requirements = {
            key: MERGED_CURRENT_PR_REQUIREMENTS[key]
            for key in [
                "eatme PR #136",
            ]
        }
        self.assert_contains_all(text, EATME_PR136_WAVE_PR_LINKS, "atlas entry 0125")
        self.assert_contains_all(text, ENTRY_TRACEABILITY_LINKS, "atlas entry 0125")
        self.assert_current_merge_status_is_plain(text, "atlas entry 0125", requirements)
        self.assert_current_unproven_behaviors_are_explicit(text, "atlas entry 0125")
        self.assertIn("next_missing_real_desktop_proof", text)
        self.assertIn("place-object", text)
        self.assertIn("edit-procedure-or-code-block", text)
        self.assertIn("run-world", text)
        self.assertIn("save-project", text)
        self.assertIn("203", text)

    def test_0126_current_merge_status_and_boundaries_are_explicit(self):
        text = self.docs["atlas entry 0126"]

        requirements = {
            key: MERGED_CURRENT_PR_REQUIREMENTS[key]
            for key in [
                "RabbitHole PR #291",
            ]
        }
        self.assert_contains_all(text, RABBITHOLE_PR291_WAVE_PR_LINKS, "atlas entry 0126")
        self.assert_contains_all(text, ENTRY_TRACEABILITY_LINKS, "atlas entry 0126")
        self.assert_current_merge_status_is_plain(text, "atlas entry 0126", requirements)
        self.assert_current_unproven_behaviors_are_explicit(text, "atlas entry 0126")
        self.assertIn("0f00c088f20e489b5b3c43bdbdc29e078dfb6b9b", text)
        self.assertIn("ConditionalStatement", text)
        self.assertIn("BooleanExpressionBodyPair", text)
        self.assertIn("void method bodies", text)
        self.assertIn("Local declarations", text)

    def test_0127_current_merge_status_and_boundaries_are_explicit(self):
        text = self.docs["atlas entry 0127"]

        requirements = {
            key: MERGED_CURRENT_PR_REQUIREMENTS[key]
            for key in [
                "RabbitHole PR #292",
            ]
        }
        self.assert_contains_all(text, RABBITHOLE_PR292_WAVE_PR_LINKS, "atlas entry 0127")
        self.assert_contains_all(text, ENTRY_TRACEABILITY_LINKS, "atlas entry 0127")
        self.assert_current_merge_status_is_plain(text, "atlas entry 0127", requirements)
        self.assert_current_unproven_behaviors_are_explicit(text, "atlas entry 0127")
        self.assertIn("17e82091", text)
        self.assertIn("FileMenuSaveNavigationProofTest", text)
        self.assertIn("FileMenuModel", text)
        self.assertIn("AliceMenuBar", text)
        self.assertIn("SaveProjectOperation", text)
        self.assertIn("menu_item_dispatched", text)
        self.assertIn("ActionEventTrigger", text)

    def test_0128_current_merge_status_and_boundaries_are_explicit(self):
        text = self.docs["atlas entry 0128"]

        requirements = {
            key: MERGED_CURRENT_PR_REQUIREMENTS[key]
            for key in [
                "RabbitHole PR #293",
            ]
        }
        self.assert_contains_all(text, RABBITHOLE_PR293_WAVE_PR_LINKS, "atlas entry 0128")
        self.assert_contains_all(text, ENTRY_TRACEABILITY_LINKS, "atlas entry 0128")
        self.assert_current_merge_status_is_plain(text, "atlas entry 0128", requirements)
        self.assert_current_unproven_behaviors_are_explicit(text, "atlas entry 0128")
        self.assertIn("3696670873c6a409046ac6e648e828d95956aa8b", text)
        self.assertIn("WhileLoop", text)
        self.assertIn("void method bodies", text)
        self.assertIn("BlockStatement", text)
        self.assertIn("UnsupportedTweedleDecodeException", text)
        self.assertIn("109", text)


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

    def test_0129_current_merge_metadata_is_explicit(self):
        text = self.docs["atlas entry 0129"]

        self.assert_contains_all(text, FOUR_PR_MERGED_METADATA_LINKS, "atlas entry 0129")
        self.assert_contains_all(text, ENTRY_TRACEABILITY_LINKS, "atlas entry 0129")
        self.assert_current_merge_status_is_plain(
            text,
            "atlas entry 0129",
            FOUR_PR_MERGED_METADATA_REQUIREMENTS,
        )
        self.assert_no_stale_status_for_current_prs(text, "atlas entry 0129")
        self.assertIn("Repository", text)
        self.assertIn("PR number", text)
        self.assertIn("merged timestamp", text)
        self.assertIn("merged-by user", text)
        self.assertIn("Repository values come from the fixed GitHub", text)
        self.assertIn("repository inputs and returned PR URLs", text)
        self.assertIn("`number`", text)
        self.assertIn("`state`", text)
        self.assertIn("`mergedAt`", text)
        self.assertIn("`mergedBy.login`", text)
        self.assertIn("merge commit SHA", text)
        self.assertIn("`mergeCommit.oid`", text)
        self.assertIn("head SHA", text)
        self.assertIn("`headRefOid`", text)
        self.assertIn("does not describe implementation impact", text)
        self.assertIn("runtime behavior", text)

    def test_0129_metadata_table_has_only_verified_columns_and_rows(self):
        text = self.docs["atlas entry 0129"]
        metadata_section = section(text, "Verified merged metadata")
        table_lines = [
            line
            for line in metadata_section.splitlines()
            if line.startswith("|") and line.endswith("|")
        ]

        self.assertEqual(
            FOUR_PR_MERGED_METADATA_TABLE_LINES,
            table_lines,
        )

    def test_0129_metadata_table_omits_unverified_placeholder_values(self):
        text = self.docs["atlas entry 0129"]
        metadata_section = section(text, "Verified merged metadata")
        table_lines = [
            line
            for line in metadata_section.splitlines()
            if line.startswith("|") and line.endswith("|")
        ][2:]

        for row in table_lines:
            with self.subTest(row=row):
                cells = [cell.strip().strip("`").lower() for cell in row.strip("|").split("|")]
                self.assertNotIn("", cells)
                self.assertTrue(all(cell not in {"null", "none", "unknown", "tbd", "n/a"} for cell in cells))

    def test_0129_status_entry_avoids_four_pr_overclaims(self):
        text = plain(self.docs["atlas entry 0129"]).lower()
        forbidden_claims = [
            "implementation impact is",
            "implementation impact:",
            "rollout is",
            "rollout:",
            "business value is",
            "business value:",
            "downstream effects are",
            "downstream effects:",
            "runtime behavior is",
            "runtime behavior:",
            "proves runtime",
            "proven runtime",
        ]

        for claim in forbidden_claims:
            with self.subTest(claim=claim):
                self.assertNotIn(claim, text)

    def test_0130_rabbithole_306_308_evidence_status_is_bounded(self):
        docs_to_check = {
            name: self.docs[name]
            for name in [
                "README",
                "root plan",
                "current modernization plan",
                "restarted full-scope status",
                "eatme implementation plan",
                "atlas index",
                "atlas entry 0130",
            ]
        }

        for name, text in docs_to_check.items():
            with self.subTest(document=name):
                self.assert_contains_all(text, RABBITHOLE_PR306_PR308_EVIDENCE_LINKS, name)
                self.assert_contains_all(text, RABBITHOLE_PR307_BOUNDED_LINKS, name)
                self.assert_contains_all(text, ACTIVE_FOLLOWUP_LINKS, name)
                plain_text = plain(without_markdown_link_targets(text))
                self.assert_contains_all(
                    plain_text,
                    RABBITHOLE_306_308_APPROVED_WORDING,
                    name,
                )
                self.assert_contains_all(plain_text, RABBITHOLE_PR307_BOUNDED_TERMS, name)
                self.assertIn(ACTIVE_FOLLOWUP_STATUS_SENTENCE, plain_text)
                self.assertNotIn(
                    "RabbitHole PR #307 and amplihack-rs PR #575 remain active follow-up work.",
                    plain_text,
                )
                self.assertNotIn(
                    "RabbitHole PR #307 is the Project I/O recovery shard still to land",
                    plain_text,
                )
                self.assertIn(CAPABILITY_BOUNDARY_SENTENCE, plain_text)
                self.assert_contains_all(plain_text, RABBITHOLE_306_308_EVIDENCE_TERMS, name)
                self.assert_contains_all(plain_text, ACTIVE_FOLLOWUP_TERMS, name)
                self.assert_contains_all(plain_text, PLANNED_BUILD_BOUNDARY_TERMS, name)
                self.assert_contains_all(plain_text, CAPABILITY_BOUNDARY_TERMS, name)

    def test_0130_rabbithole_306_308_evidence_avoids_overclaims(self):
        for name, text in self.lower_plain_docs.items():
            found_claims = [
                claim
                for claim, normalized in RABBITHOLE_306_308_FORBIDDEN_OVERCLAIMS_NORMALIZED
                if normalized in text
            ]
            with self.subTest(document=name):
                self.assertEqual([], found_claims, f"{name} contains forbidden overclaims")

    def test_0130_atlas_entry_links_previous_status_and_active_followups(self):
        text = self.docs["atlas entry 0130"]

        self.assert_contains_all(text, ENTRY_TRACEABILITY_LINKS, "atlas entry 0130")
        self.assert_contains_all(text, ACTIVE_FOLLOWUP_LINKS, "atlas entry 0130")
        self.assertIn("Previous entry: [0129 - Four-PR merged metadata status]", text)


if __name__ == "__main__":
    unittest.main()
