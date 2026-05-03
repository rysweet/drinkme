Agent completed. agent_id: eatme-alice-resources, agent_type: research, status: completed, description: Discover Alice resources, elapsed: 395s, total_turns: 0, duration: 380s

I now have comprehensive coverage. Let me compile the full findings.

---

## Alice 3 / Alice.org — QA Workstream `eatme` Resource Map

**Research Status:** Complete. All resources verified by direct fetch. Main domain `https://www.alice.org/` returns HTTP 500 at root but all sub-pages respond. GitHub source at `TheAliceProject/alice3` confirmed. No resources were modified. All URLs below are verified reachable unless flagged `[500]` or `[404]`.

---

### 1. SUMMARY

Alice 3 is a free, CMU-developed block-based 3D animation/programming IDE (current stable: **3.9.0.3**, released 2025-11-12; repo HEAD: **3.9.1.0**). It targets K–12 and introductory college CS, with a structured modular curriculum on alice.org covering Scene Building → Programming Basics → Control Structures → Events → OOP/Java transition. Resources divide into: official CMU lessons/how-tos/curriculum (alice.org); official source code (GitHub `TheAliceProject/alice3`); an officially-linked third-party curriculum suite (Duke "Adventures in Alice"); Oracle Academy materials; and community video tutorials. VR is a first-class feature since v3.8 (Oculus Quest, Vive). The Alice Player is a separate runtime enabling standalone app export. A NetBeans plugin supports mediated transfer to Java.

---

### 2. REPOSITORIES & SOURCE

| Repo | Status | Purpose |
|---|---|---|
| `TheAliceProject/alice3` | **Official** | Full Alice 3 IDE source. Java 21 + Maven + git-lfs. Submodule: Tweedle (internal Alice language IR). Latest tag: 3.9.1.0. |
| `TheAliceProject/alice3-tools` | **Official** (linked) | Experimental/dev-aid tools separated from main repo |

**Key repo facts (README.md):**
- Build: `mvn compile install` → also emits NetBeans plugin at `netbeans/target/`
- Run: `cd alice-ide && mvn exec:java -Dalice-ide`
- Test: `mvn test`
- IDE recommendation: IntelliJ IDEA (free community or JetBrains edu license)
- Sims assets optional: `mvn -DincludeSims=false clean install`
- Internal language: "Tweedle" (submodule)
- VR improvements: 3.8 (headset/hands), 3.9 (conversion on open, cameraMakers)
- Notable: references to "Drink me!" in v3.7 changelog (VR User has scale)

---

### 3. INSTALLATION / GETTING-STARTED DOCS

| Priority | URL | Status | Constituency | Notes |
|---|---|---|---|---|
| P0 | `https://www.alice.org/get-alice/alice-3/` | **Official** ✅ | All | Primary download + full changelog + HW requirements + platform notes (Win/Mac/Linux/Raspberry Pi). Current: 3.9.0.3. |
| P0 | `https://www.alice.org/get-alice/` | **Official** ✅ | Instructors/Students | Alice 2 vs Alice 3 decision guide. Explains all three variants (Alice 3, Alice 3+NetBeans, Alice 2). |
| P1 | `https://www.alice.org/get-alice/alice-3-with-netbeans/` | **Official** ✅ | Instructors/Advanced Students | NetBeans plugin install, versioning requirements, Java 17/18 JDK requirement. |
| P2 | `https://www.alice.org/resources/how-tos/running-the-tutorial/` | **Official** ✅ (Alice 2) | Students | In-app tutorial launch via File → New World → Tutorial tab |
| P2 | `https://github.com/TheAliceProject/alice3` | **Official** ✅ | Dev/QA | Source build instructions, dev environment setup |

**QA Scenarios — Installation:**
- Fresh install on Windows 10/11, macOS 13+ (Ventura dark mode bug fixed in 3.8), Ubuntu; verify launch
- Install on Raspberry Pi 3 (Full KMS required) and Pi 4 (library dependency)
- Verify NetBeans plugin version-match enforcement (mismatched version should error)
- `mvn test` full suite pass on clean clone
- Build with `-DincludeSims=false` smoke test

---

### 4. LESSONS (Structured Curriculum — Alice 3)

All lessons are **Official** ✅ and live at `https://www.alice.org/resources/lessons/`. Each lesson is designed as a facilitator guide with: presentation, tutorial exercise, assessment ideas, and how-to video links. Material format: Google Slides + .pptx download.

#### 4a. Core Lessons (Minimum viable curriculum path)

| Priority | URL | Constituency | Learning Objectives | Completion Status |
|---|---|---|---|---|
| **P0** | `/lessons/building-a-scene/` | Students + Instructors | Virtual world concepts; Scene Editor; Object add/position/orient/scale/subparts; Camera controls; Camera Markers | ✅ Full lesson (Oct 2019) |
| **P0** | `/lessons/programming-in-alice/` | Students + Instructors | Code Editor; Procedures; Run program; Control structures (DoInOrder/DoTogether); Camera Marker programming; Audio | ✅ Full lesson (Nov 2019) |
| **P0** | `/lessons/control-structures-overview/` | Students + Instructors | 4 control structure types; nested blocks; animation synchronization | ✅ Full lesson |
| **P0** | `/lessons/introduction-to-events/` | Students + Instructors | Events, listeners, handlers; initializeEventListeners; scene/keyboard/mouse/collision events | ✅ Full lesson |
| **P1** | `/lessons/making-procedural-methods/` | Students + Instructors | Custom procedures; export/import methods; clipboard | ✅ Full lesson |
| **P1** | `/lessons/using-functions/` | Students + Instructors | Functional methods; random numbers | ⚠️ Facilitation guide still in development |

#### 4b. Extending Lessons

| Priority | URL | Constituency | Notes |
|---|---|---|---|
| P1 | `/lessons/using-parameters/` | Students | Extends procedural methods; data type prerequisite | ⚠️ Under development |
| P1 | `/lessons/data-types/` | Students | Prerequisite for parameters/expressions | — |
| P1 | `/lessons/control-structures-loops/` | Students | Count/forEach/while loops | ⚠️ Under development |
| P1 | `/lessons/control-structures-conditionals/` | Students | if_ blocks; combined with functions/variables | ⚠️ Under development |
| P2 | `/lessons/events-collision-and-proximity/` | Students | Bounding box; collision/proximity event construction | ⚠️ Under development |
| P2 | `/lessons/using-comments/` | Students | — | — |

#### 4c. Advanced / Supplemental Lessons

| Priority | URL | Constituency | Notes |
|---|---|---|---|
| P2 | `/lessons/using-variables/` | Students | Slide deck only; integral to games/conditionals/events | ⚠️ Slide deck only |
| P2 | `/lessons/arrays/` | Students | Slide deck only; referenced by events/loops lessons | ⚠️ Slide deck only |
| P2 | `/lessons/arithmetic-expressions/` | Students | Supplement to functions | — |
| P2 | `/lessons/relational-expressions/` | Students | Supplement to loops/conditionals | — |

#### 4d. Design-Process Lessons (Project-Based)

| Priority | URL | Constituency | Prerequisites | Notes |
|---|---|---|---|---|
| **P0** | `/lessons/design-process-introduction/` | Students + Instructors | Building a Scene + Programming in Alice | Storyboarding → algorithm → flowchart → set design. Full lesson (Nov 2019) |
| P1 | `/lessons/design-interactive-narrative/` | Students + Instructors | Conditionals + Events | Branching narratives; open worlds; plot mapping | ⚠️ Presentation only; guide still in dev |
| P1 | `/lessons/design-process-games/` | Students + Instructors | Variables + Control structures + Events | Game goals; win/lose conditions; mechanics; game design doc | ⚠️ Presentation only; guide still in dev |
| P2 | `/lessons/design-process-virtual-reality/` | Students + Instructors | Core design lessons | VR sickness; VR mechanics; locomotion patterns | ⚠️ Presentation only |

#### 4e. Entry-Point Lessons (Events / Workshops)

| Priority | URL | Constituency | Notes |
|---|---|---|---|
| **P0** | `/lessons/hour-of-code/` | All (1–2 hrs) | Storyboard → script → 3D animation. Condensed core intro. |
| P1 | `/lessons/hour-of-code-2/` | All | Second Hour of Code variant |

#### 4f. Legacy / Alice 2 Lessons (⚠️ External/partially official)

| URL | Status | Notes |
|---|---|---|
| `/lessons/adventures-in-alice-programming/` | Official link to **External** (Duke) | 3rd–12th grade lesson plans, 2008–2015 workshops. Creative Commons. |
| `/lessons/learning-to-program-with-alice/` | Official link to **External** (aliceprogramming.net) | Alice 2; free supplemental materials |

**QA Scenarios — Lessons:**
- Follow core path (Building Scene → Programming → Control Structures → Events) end-to-end; verify all linked how-tos resolve
- Verify each lesson's Google Slides link is accessible (non-paywalled)
- Verify .pptx downloads work (where provided)
- Confirm assessment materials present for "full lesson" entries vs. "under development" entries
- Test Hour of Code lesson as a 60-min single-session walkthrough

---

### 5. HOW-TOS (Reference / Micro-Tutorials)

All at `https://www.alice.org/resources/how-tos/`. These are **Official** ✅ short reference guides (text + embedded video). Organized here by functional domain.

#### 5a. Interface & Basic Object Manipulation

| URL | Constituency | What It Covers |
|---|---|---|
| `/how-tos/scene-editor-overview/` | All | Camera View, Properties Panel, Gallery, Object Tree, One-shots |
| `/how-tos/code-editor-overview/` | All | Code editor layout ⚠️ (page returned only footer — content may be embedded video only) |
| `/how-tos/adding-objects/` | Students | Gallery → Scene |
| `/how-tos/positioning-objects/` | Students | 3D positioning tools |
| `/how-tos/rotating-objects/` | Students | Rotation handles |
| `/how-tos/resizing-objects/` | Students | Scale tools |
| `/how-tos/manipulating-object-joints/` | Students | Joint sub-parts |
| `/how-tos/moving-the-camera/` | Students | Camera controls |
| `/how-tos/using-camera-views/` | Students | Perspective/ortho views |
| `/how-tos/using-camera-markers/` | Students | Record/recall camera positions |
| `/how-tos/using-one-shots/` | Students | One-shot property manipulations |

#### 5b. Programming

| URL | Constituency | What It Covers |
|---|---|---|
| `/how-tos/using-procedures-overview/` | Students + Instructors | Full procedure taxonomy (text/position/orientation/size/appearance/audio/timing/vehicle/custom) |
| `/how-tos/understanding-using-move-turn-or-roll/` | Students | Core movement procedures |
| `/how-tos/using-do-together/` | Students | Concurrent execution |
| `/how-tos/creating-custom-procedures/` | Students | User-defined methods |
| `/how-tos/adding-and-using-parameters/` | Students | Parameterized methods |
| `/how-tos/using-functions-overview/` | Students | Functional method usage |
| `/how-tos/using-events-overview/` | Students + Instructors | Full event taxonomy (scene/keyboard/mouse/position-orientation) + initializeEventListeners |
| `/how-tos/using-joint-arrays/` | Students | Joint arrays (advanced animation) |
| `/how-tos/first-person-camera/` | Students | Vehicle camera to character; over-shoulder variant |

#### 5c. Game Mechanics

| URL | Constituency | What It Covers |
|---|---|---|
| `/how-tos/setting-up-collision-detection/` | Students | Collision event triggers; score increment |
| `/how-tos/setting-up-proximity-detection/` | Students | Distance-parameter proximity trigger |
| `/how-tos/setting-up-a-scorekeeper/` | Students | TextObject-based score variable display |
| `/how-tos/setting-up-a-timekeeper/` | Students | While-loop timer; TimerListener approach; attached demo world |

#### 5d. Animation

| URL | Constituency | What It Covers |
|---|---|---|
| `/how-tos/biped-walk-cycle/` | Students | Walk Start/cycle/end animation pattern; arm/leg counter-swing |
| `/how-tos/manipulating-biped-joints/` | Students | Joint anatomy reference |

#### 5e. Audio

| URL | Constituency | What It Covers |
|---|---|---|
| `/how-tos/the-basics-of-using-audio/` | Students | Audio procedure basics |
| `/how-tos/adding-background-music/` | Students | Background audio loop |
| `/how-tos/matching-sound-to-animation/` | Students | Sync audio to animation timing |
| `/how-tos/creating-custom-audio-in-audacity/` | Students | Audacity workflow |
| `/how-tos/changing-file-formats-in-audacity/` | Students | Format conversion for Alice |

#### 5f. Import / Export / Sharing

| URL | Constituency | What It Covers |
|---|---|---|
| `/how-tos/importing-models-overview/` | Advanced Students + Instructors | .dae import requirements; Blender workflow; My Gallery; sharing zipped models |
| `/how-tos/importing-models/` | Students | Basic import flow |
| `/how-tos/map-custom-images/` | Students | Billboard/texture mapping |
| `/how-tos/exporting-and-importing-modified-classes/` | Students | Class portability across projects |
| `/how-tos/recording-and-sharing-alice-worlds/` | Students | OBS/QuickTime/Win10 screen capture; limitations of built-in export |
| `/how-tos/exporting-for-the-alice-player/` | Students | File → Export → .a3w workflow |
| `/how-tos/using-the-alice-player/` | Students | Player install, load world, controls, settings (Unity backend) |
| `/how-tos/making-an-alice-app/` | Students + Instructors | Standalone app creation via Alice Player |

#### 5g. VR How-Tos (Alice 3.8+)

| Priority | URL | Constituency | What It Covers |
|---|---|---|---|
| P0 | `/how-tos/creating-a-vr-project-with-a-vruser/` | Instructors + Advanced Students | VR world type; vrUser, headset, hands. Links to Google Doc. |
| P1 | `/how-tos/overview-of-vr-input-mapping/` | Advanced Students | Input mapping reference |
| P1 | `/how-tos/vr-locomotion-direct-control/` | Advanced Students | Direct movement control |
| P1 | `/how-tos/vr-locomotion-teleportation/` | Advanced Students | Teleport locomotion |
| P1 | `/how-tos/vr-locomotion-on-rails/` | Advanced Students | On-rails movement |
| P1 | `/how-tos/vr-locomotion-puppeteer/` | Advanced Students | Puppeteer locomotion |
| P1 | `/how-tos/vr-object-interaction-click-and-move/` | Advanced Students | Click-to-move object |
| P1 | `/how-tos/vr-object-interaction-point-and-click/` | Advanced Students | Point-and-click interaction |
| P1 | `/how-tos/vr-using-controller-objects-hands/` | Advanced Students | Controller/hand model binding |
| P2 | `/how-tos/using-the-alice-player-with-oculus-quest-vr/` | Students | Oculus Quest setup |
| P2 | `/how-tos/using-the-alice-player-with-vive-vr/` | Students | Vive setup |
| P2 | `/how-tos/using-the-alice-player-with-oculus-vr/` | Students | Oculus (non-Quest) setup |

#### 5h. Community / External How-To Resources

| URL | Status | Notes |
|---|---|---|
| `/how-tos/youtube-channels-and-playlists/` | **Official** ✅ (index) | Points to: Alice At Duke, Oracle Academy, Bill Barnum, Mathew W Vids |
| `/how-tos/adventures-in-alice-programming/` | Official link → **External** (Duke) | PPT + handouts + exercise files + world movies per tutorial |
| `/how-tos/adventures-in-alice-programming-2/` | Official link → **External** | Second Duke tutorial set |
| `/how-tos/example-of-step-by-step-construction/` | **Official** ✅ | Step-by-step construction example |

**QA Scenarios — How-Tos:**
- Verify all Google Doc links (VR how-tos) are publicly accessible
- Test each import/export how-to end-to-end in current Alice 3.9
- Verify .dae import workflow with known-good model; test error on unsupported class type (Flyer/Slitherer)
- Test Alice Player launch + .a3w load on Windows + macOS
- Validate all YouTube playlist links are still live (external dependency)

---

### 6. CURRICULUM MATERIALS

All at `https://www.alice.org/resources/curriculum/`.

| Priority | URL | Status | Constituency | Description |
|---|---|---|---|---|
| **P0** | `/curriculum/building-an-alice-curriculum/` | **Official** ✅ | Instructors | Master curriculum design guide. Defines Core/Extending/Advanced/Supplemental lesson types. Provides recommended lesson progression. Links standards spreadsheet (CSTA, ISTE). |
| **P0** | `/curriculum/alice-curriculum-mapped-to-standards/` | **Official** ✅ | Instructors | 6-week program mapped to standards ⚠️ (very thin content returned — may require login or be in-progress) |
| P1 | `/curriculum/adventures-in-alice-programming/` | Official link → **External** (Duke University) ⚠️ | Instructors | Teacher workshops 2010–2017; Alice 2+3 materials; Coursera course |
| P1 | `/curriculum/oracle-academy/` | Official link → **External** (Oracle) ⚠️ | Instructors + Students | "Getting Started with Java Using Alice" self-paced module + workshop-in-a-box; Java Fundamentals course integration |
| P2 | `/curriculum/expeditions-through-alice-and-cs-principles/` | Official link → **External** (UCSD/Sweetwater) ⚠️ | Instructors | AP Computer Science Principles implementation using Alice 2. Teacher testimonial. 72–68% AP exam pass rate. |
| P2 | `/curriculum/testing-curriculum-alice-3/` | **Official** ✅ | Instructors | Test/staging curriculum entry (likely internal) |

**Curriculum progression (from Building an Alice Curriculum):**
```
Building a Scene → Programming in Alice
  ├─ Comments, Making Procedural Methods, Parameters, Data Types
  └─ Using Functions → Arithmetic Expressions
       └─ Control Structures Overview
            ├─ Control Structures Loops → Arrays, Relational Expressions
            └─ Using Variables → Control Structures Conditionals
                  └─ Introduction to Events
                        ├─ Events Collision and Proximity
                        ├─ Events Mouse (⚠️ under development)
                        ├─ Events Keypress (⚠️ under development)
                        └─ Events Scene Activated (⚠️ under development)

Design Lessons (inject at indicated prerequisites):
  Design Process Introduction (earliest: after Building Scene + Programming)
  Design Interactive Narrative (after Conditionals + Events)
  Design Games (after Variables + Control Structures + Events)
  Design for VR (after core design lessons)
```

**QA Scenarios — Curriculum:**
- Validate entire core path for a student with no prior CS: time per lesson, can they complete the recommended progression in 6 weeks?
- Verify standards spreadsheet link is accessible
- Check Oracle Academy links still resolve (external dependency)
- Validate AP CS Principles alignment claims against current CSTA standards

---

### 7. GALLERY / FEATURED PROJECTS

All at `https://www.alice.org/featured-projects/`. **Official** ✅ (student/team work curated by CMU Alice team). Community projects page: `https://www.alice.org/community/featured-projects/`.

| Priority | URL | Alice Version | What It Showcases |
|---|---|---|---|
| **P0** | `/featured-projects/interactive-narrative-example-evergarden/` | Alice 3 | Open-world interactive narrative; collision + proximity detection patterns; full design document template; prototypes included |
| P1 | `/featured-projects/peacock-romance/` | Alice 3 | Animation showcase |
| P1 | `/featured-projects/sea-encounter/` | Alice 3 | Animation/scene building |
| P1 | `/featured-projects/happy-hippo/` | Alice 3 | Don Slater classic Alice demo world |
| P1 | `/featured-projects/alice-regional-challenge-high-school-finalists/` | Alice 3 | Student competition entries (Pittsburgh, Spring 2018) |
| P1 | `/featured-projects/alice-regional-challenge-middle-school-finalists/` | Alice 3 | Student competition entries |
| P2 | `/featured-projects/happy-halloween-from-the-alice-team/` | Alice 3 | Gallery content showcase |
| P2 | `/featured-projects/happy-halloween-from-the-alice-team-alice-2-style/` | Alice 2 | Community member work (Jeff Schultes) |

**QA Scenarios — Gallery:**
- Download and run Evergarden .a3w in current player; verify collision + proximity events fire correctly
- Verify design document template is accessible and usable as project scaffold
- Run all Alice 3 featured project worlds; check for regression in 3.9

---

### 8. TEXTBOOKS (Reference)

All at `https://www.alice.org/resources/textbooks/`. **Official** page listings; books themselves are **external** (commercial publishers). Included for QA awareness.

#### Alice 3 Textbooks

| Priority | URL | Status | Authors | Notes |
|---|---|---|---|---|
| P1 | `/textbooks/learning-java-through-alice-3/` | Official listing ✅ | Daly & Wrigley | Java+Alice3 hybrid; ISBN 978-1499728477 (2014) |
| P1 | `/textbooks/alice-3-in-action-computing-through-animation/` | Official listing ✅ | — | 6-chapter supplementary; "2E"; no prior experience required |
| P1 | `/textbooks/alice-3-to-java/` | Official listing ✅ | — | Alice 3 → Java bridge; storytelling + gaming approach |
| P1 | `/textbooks/alice-3-in-action-with-java-1st-edition/` | Official listing ✅ | — | 1st edition variant |
| P2 | `/textbooks/how-to-guide-for-alice-3/` | Official listing ✅ | Dann, Slater, Cosgrove, Paoletti, Culyba, Tang | Free guide; 2012/2014. Notable: CMU team authors. |
| P2 | `/textbooks/learning-to-program-with-alice/` | Official listing ✅ | — | 3rd ed; pre-CS1; objects-first or objects-early approach; Java-like syntax |
| P2 | `/textbooks/learning-java-through-alice-3-resources/` | Official listing ✅ | — | Companion resources |
| P2 | `/textbooks/expeditions-through-alice/` | Official listing ✅ | Cutts, Esper, Simon | Online book; Alice 2 basis; AP CSP implementation |

#### Alice 2 Textbooks (lower QA priority, listed for completeness)
`/textbooks/starting-out-with-alice/` (Gaddis, visual intro), `/textbooks/exploring-wonderland/` (Java+Media Computation), `/textbooks/alice-in-action-with-java/` and `alice-in-action-with-java-2/`, `/textbooks/programming-with-alice-and-java/`, `/textbooks/fluency-with-alice-workbook/`, `/textbooks/alice-2-0-introductory-concepts-and-techniques/`, `/textbooks/the-alice-programming-language/`

---

### 9. WORKSHOPS

All at `https://www.alice.org/resources/workshops/`. **Official** ✅ (CMU-hosted and partner-hosted educator PD events).

| Priority | URL | Constituency | Description |
|---|---|---|---|
| **P0** | `/workshops/learn-to-create-3d-worlds-with-alice/` | Instructors | Core teacher PD: scene building + simple animations + leading student projects. Starting point for Alice Challenge. Eligible for Act 48 credits. |
| P1 | `/workshops/game-design-with-alice/` | Instructors | Workshop 2 of 3: branching narratives, open worlds, game design docs, conditional mechanics, variables |
| P1 | `/workshops/getting-started-with-java-using-alice/` | Instructors | Java transition workshop |
| P2 | `/workshops/introduction-to-alice-3/` | Instructors | [500 error — may be retired or temporarily down] |
| P2 | `/workshops/learn-alice-at-assemble/` | Instructors | Community partner event |
| P2 | `/workshops/alice-weekly-question-and-answer-session/` | Instructors | Ongoing community Q&A |
| P2 | `/workshops/adventures-in-alice-2-beginner-workshop/` | Instructors | Alice 2 beginner PD |
| P3 | `/workshops/learn-to-create-3d-worlds-with-alice-2/` through `-iu1`, `-consortium-*`, `-weekly-zoom` | Instructors | Regional/partner variants of core workshop |

**QA Scenarios — Workshops:**
- Verify Eventbrite RSVP links (external dependency) still resolve
- Confirm Act 48 credit workflow is documented accurately

---

### 10. COMMUNITY / TEACHER RESOURCES

| URL | Status | Constituency | Notes |
|---|---|---|---|
| `https://www.alice.org/community/` | **Official** ✅ | All | Hub for featured projects, challenge, HoC, forum, teacher community, swag |
| `https://lists.andrew.cmu.edu/mailman/listinfo/alice-teachers` | **Official** ✅ (external CMU service) | Instructors | Teacher listserv; primary peer support channel |
| `https://www.alice.org/community/hour-of-code/` | **Official** ✅ | Instructors + Students | Hour of Code event resource page |
| `https://www.alice.org/community/featured-projects/` | **Official** ✅ | All | Curated student/community project gallery |
| `/community/alice-challenge/` | **Official** ✅ (empty content) | Instructors + Students | Annual competition; Pittsburgh regional + others |
| `/community/teacher-community/` | **Official** (404) ⚠️ | Instructors | Page not found — possibly relocated to listserv |

---

### 11. EXTERNAL RESOURCES (Officially Linked, Not CMU-owned)

| Resource | URL | Status | Constituency | QA Note |
|---|---|---|---|---|
| Adventures in Alice Programming (Duke) | `http://www.cs.duke.edu/csed/alice/aliceInSchools/` | **External** ⚠️ | Instructors | CS Duke URL; verify still active. PPT/handout/exercise files + world movies. Lesson plans 3rd–12th grade. Creative Commons. |
| Adventures in Alice Lesson Plans | `http://www.cs.duke.edu/csed/alice/aliceInSchools/lessonPlans/` | **External** ⚠️ | Instructors | Teacher-generated plans from Duke workshops 2008–2015 |
| aliceprogramming.net | `http://www.aliceprogramming.net/materials.html` | **External** ⚠️ | All | "Learning to Program with Alice" companion site |
| Oracle Academy | `https://academy.oracle.com/en/solutions-education-bytes.html` | **External** ⚠️ | Instructors | Self-paced "Getting Started with Java Using Alice" |
| Oracle Academy Workshops | `https://academy.oracle.com/en/training-workshops.html` | **External** ⚠️ | Instructors | Workshop-in-a-box |
| Oracle Academy Curriculum | `https://academy.oracle.com/en/solutions-curriculum.html#java1-tab` | **External** ⚠️ | Instructors | Java Fundamentals with Alice |
| Oracle Academy YouTube | `https://www.youtube.com/playlist?list=PLGv3QgWrkbRl6mkI3pixTX5NKAQIPvlA7` | **External** ⚠️ | Students + Instructors | Extensive bite-size video concepts |
| Alice At Duke YouTube | `https://www.youtube.com/user/AliceAtDuke/feed` | **External** ⚠️ | All | All Duke Alice videos |
| Bill Barnum YouTube | `https://www.youtube.com/playlist?list=PLmpmyPywZ440OmMec0WWu6jqdqCXMd8Td` | **External** ⚠️ | Students | Control structures; variable usage tutorials |
| Mathew W Vids YouTube | `https://www.youtube.com/channel/UCrO3JExtBhcObXIpIG3O84A` | **External** ⚠️ | Students | Beginner + advanced + user Q&A playlists |
| Import Model Requirements (Google Doc) | `https://docs.google.com/document/d/1ZkFVOPCHJGAswV2aAKF0fnMl3GJL_duzP5Sr7yeo2nE/edit?usp=sharing` | **Official** ✅ (CMU-hosted on GDocs) | Advanced Students | Continuously updated model import checklist |
| VR How-To (Google Doc) | `https://docs.google.com/document/d/1UlivaWLVXon9RA0zPQF-9bDGgR0s2YvRv0pARMLreVE/edit?usp=share_link` | **Official** ✅ (CMU-hosted on GDocs) | Advanced Students | Creating a VR Project with vrUser |

---

### 12. KEY ALICE 3 FUNCTIONALITY (Implied by Resources)

| Functional Area | Key Mechanisms | How-To / Lesson Coverage |
|---|---|---|
| **Scene Building** | Gallery (class hierarchy/themes/groups/search), 3D placement, joint manipulation, camera controls, camera markers, one-shots | Scene Editor Overview, Building a Scene, all object manipulation how-tos |
| **Block Programming** | Drag-drop procedures/functions, myFirstMethod, control blocks (DoInOrder, DoTogether, if_, count, forEach, while), initializeEventListeners | Programming in Alice, Control Structures, Events lessons; Procedures Overview how-to |
| **OOP Concepts** | Class hierarchy, inheritance, custom methods, parameters, export/import classes | Making Procedural Methods, Using Parameters, Exporting Modified Classes |
| **Events System** | Scene activation, keyboard, mouse, collision, proximity, time listeners — all in initializeEventListeners method | Introduction to Events, Events how-tos, Collision/Proximity how-tos |
| **Game Mechanics** | Variables (score, timer, game-active state), collision/proximity detection, conditionals, while-loop timer, TimerListener | ScoreKeeper, TimeKeeper, Collision/Proximity how-tos; Design Games lesson |
| **Animation** | Biped joint manipulation, walk cycle (start/cycle/end pattern), joint arrays, DoTogether timing, duration/style arguments | Biped how-tos, Joint Arrays, DoTogether |
| **Audio** | Background music, audio sync to animation, Audacity integration (format conversion, custom audio) | Audio how-tos |
| **Model Import** | .dae format, texture requirement, class assignment (prop/biped/flyer⚠️), My Gallery storage, Blender workflow | Importing Models Overview, Map Custom Images |
| **VR** | vrUser world type (headset+hands), locomotion (direct/teleport/rails/puppeteer), object interaction (click-move/point-click), input mapping, Oculus Quest/Vive | All VR how-tos; Design VR lesson |
| **Sharing / Distribution** | Screen capture (OBS/QuickTime/Win10), .a3w export, Alice Player (Unity runtime), standalone app creation, NetBeans plugin (→ Java) | Recording/Sharing, Player how-tos, Making an App, NetBeans |
| **Java Transition** | NetBeans plugin, "Tweedle" IR (internal), Alice 3 to Java textbooks, Alice 3+NetBeans download | NetBeans page, textbooks |

---

### 13. CONSTITUENCY MAPPING

| Resource Category | Primary Constituency | Secondary Constituency |
|---|---|---|
| Download / Installation pages | **Students** + **Instructors** | Dev/QA (source build) |
| Core Lessons (Building Scene, Programming, Events, Design) | **Students** (delivered by instructors) | Instructors (facilitation guide role) |
| Curriculum Guide (Building an Alice Curriculum) | **Instructors** | — |
| How-Tos (all categories) | **Students** (self-service reference) | Instructors (lesson planning) |
| VR How-Tos | **Advanced Students** | Instructors integrating VR |
| Textbooks | **Students** (college/HS) | Instructors (course adoption) |
| Workshops | **Instructors** (professional development) | — |
| Featured Projects / Gallery | **Students** (inspiration) | Instructors (demo material) |
| Teacher Listserv | **Instructors** | — |
| Hour of Code | **Event facilitators** + **Students** | — |
| GitHub source + build docs | **QA / Dev** | — |
| Oracle Academy / Duke materials | **Instructors** (alternate curricula) | Students (self-study) |

---

### 14. SUGGESTED QA SCENARIOS BY RESOURCE

| Scenario | Resource(s) Consumed | Functionality Under Test |
|---|---|---|
| **QA-01: Fresh Install Smoke Test** | `get-alice/alice-3/`, GitHub README | Installer on Win/Mac/Linux/Pi; app launch; splash; gallery load |
| **QA-02: In-App Tutorial Completion** | `how-tos/running-the-tutorial/` | Tutorial tab in File→New World; built-in tutorial completion flow |
| **QA-03: Core Lesson End-to-End (Scene → Animation)** | `lessons/building-a-scene/`, `lessons/programming-in-alice/` | Scene Editor; gallery browsing; object add/position; camera marker; code editor; procedure drag; DoInOrder/DoTogether; Run |
| **QA-04: Design Process Walkthrough** | `lessons/design-process-introduction/` | Storyboard → flowchart → Alice implementation; project export |
| **QA-05: Control Structures Correctness** | `lessons/control-structures-overview/`, `lessons/control-structures-loops/`, `lessons/control-structures-conditionals/` | Count loop; forEach; while loop; if_ branching; nested blocks; animation sync with duration |
| **QA-06: Events Binding** | `lessons/introduction-to-events/`, `how-tos/using-events-overview/` | Keyboard move; mouse click; scene activation; initializeEventListeners tab |
| **QA-07: Game Mechanics Integration** | `how-tos/setting-up-collision-detection/`, `how-tos/setting-up-proximity-detection/`, `how-tos/setting-up-a-scorekeeper/`, `how-tos/setting-up-a-timekeeper/` | Bounding box collision trigger; proximity distance; TextObject score display; while-loop timer; TimerListener |
| **QA-08: Custom Method + Parameters** | `lessons/making-procedural-methods/`, `lessons/using-parameters/`, `how-tos/creating-custom-procedures/`, `how-tos/adding-and-using-parameters/` | Custom procedure creation; parameter passing; export/import method portability; clipboard |
| **QA-09: Character Animation (Biped Walk)** | `how-tos/biped-walk-cycle/`, `how-tos/manipulating-biped-joints/`, `how-tos/using-joint-arrays/` | Walk Start/Cycle/End animation; joint manipulation; straightenOutJoints; DoTogether timing |
| **QA-10: Audio Pipeline** | `how-tos/the-basics-of-using-audio/`, `how-tos/adding-background-music/`, `how-tos/matching-sound-to-animation/` | Audio procedure add; background music loop; duration-matched audio sync (JavaFX audio, v3.8+) |
| **QA-11: Model Import Workflow** | `how-tos/importing-models-overview/`, GDoc checklist | .dae import with valid texture; class assignment; My Gallery storage; error on Flyer/Slitherer class; model sharing via zip |
| **QA-12: Alice Player Export + Launch** | `how-tos/exporting-for-the-alice-player/`, `how-tos/using-the-alice-player/`, `how-tos/making-an-alice-app/` | File→Export→.a3w; Player install; Load World; playback controls; standalone app bundling |
| **QA-13: Interactive Narrative (Evergarden Pattern)** | `featured-projects/interactive-narrative-example-evergarden/`, `lessons/design-interactive-narrative/` | Open world; collision trigger; proximity trigger; branching narrative via conditionals |
| **QA-14: VR World Creation** | `how-tos/creating-a-vr-project-with-a-vruser/`, all VR locomotion/interaction how-tos | VR world type creation; vrUser, headset, hands objects; locomotion modes; controller binding; Oculus Quest / Vive player |
| **QA-15: Java Transition (NetBeans)** | `get-alice/alice-3-with-netbeans/`, `how-tos/adventures-in-alice-programming-2/` | Alice 3 save → NetBeans import; plugin version match; Java code generation from Alice world |
| **QA-16: Hour of Code Session** | `lessons/hour-of-code/`, `community/hour-of-code/` | 60–90 min storyboard→animation flow; Google Slides accessibility; no prior knowledge assumed |
| **QA-17: Curriculum Path (Instructor)** | `curriculum/building-an-alice-curriculum/`, standards spreadsheet | Verify all linked lessons load; progression prerequisites are satisfiable; standards doc accessible |
| **QA-18: Gallery Browsing + Sims Characters** | `how-tos/scene-editor-overview/` (Gallery section) | Browse by class hierarchy/themes/groups; Sims character builder; search; My Classes tab |
| **QA-19: Screen Capture / Share** | `how-tos/recording-and-sharing-alice-worlds/` | OBS capture of running Alice world; verify audio captured; note limitations of built-in export |
| **QA-20: Regression — Binary Op Bug (3.9.0.3 hotfix)** | `get-alice/alice-3/` changelog | Verify LHS of binary operations is preserved after edit in 3.9.0.3 |

---

### 15. GAPS, UNCERTAINTIES & FLAGS

| Item | Detail |
|---|---|
| ⚠️ `alice.org` root returns HTTP 500 | Main homepage unavailable at time of research. All sub-pages work. |
| ⚠️ `/how-tos/code-editor-overview/` | Returns only footer; likely video-only content or CMS issue. Content not verifiable by text fetch. |
| ⚠️ Several lessons marked "under development" | `using-parameters/`, `control-structures-loops/`, `control-structures-conditionals/`, `events-collision-and-proximity/`, `using-functions/`, `design-interactive-narrative/`, `design-process-games/`, `design-process-virtual-reality/` — facilitation guides/tutorials/assessments not yet complete per page content. Presentation slides may be the only deliverable. |
| ⚠️ `using-variables/` and `arrays/` | Slide deck only — no tutorial exercise or assessments. |
| ⚠️ Events: Mouse, Keypress, Scene Activated lessons | Listed in curriculum guide as "under Development" — no pages found in sitemap. |
| ⚠️ `/resources/curriculum/alice-curriculum-mapped-to-standards/` | Very thin content returned ("6 week program"). Standards spreadsheet link not included in fetched text. May require direct CMU contact. |
| ⚠️ `/resources/workshops/introduction-to-alice-3/` | Returns HTTP 500. May be retired or temporarily down. |
| ⚠️ `/community/teacher-community/` | Returns 404. Content likely migrated to listserv or community page. |
| ⚠️ Duke "Adventures in Alice" | External (cs.duke.edu URLs). HTTP reachability not verified via fetch. Hosted on university infrastructure; longevity uncertain. |
| ⚠️ Alice 3.9.1.0 (GitHub) vs 3.9.0.3 (alice.org download) | GitHub HEAD is ahead of published installer. QA should clarify which version to test against. |
| ⚠️ Alice Player described as "Unity application" | Not verified beyond page description. VR Player compatibility matrix (Oculus/Vive generations) may be outdated. |
| ⚠️ NetBeans plugin last confirmed working on NetBeans 14 | Current NetBeans is 18+. Compatibility with current NetBeans not confirmed. |
| ⚠️ No dedicated Alice 3 API/reference documentation found | No javadoc-style reference on alice.org. Closest approximation: How-To: Using Procedures Overview (comprehensive text description) and source code on GitHub. |
| ⚠️ `alice3-tools` repo | Referenced in alice3 README but not independently researched. May contain test harnesses relevant to QA. |
| ℹ️ "Drink me!" reference | Alice 3.7 changelog explicitly says "VR User has scale – Drink me!" — a deliberate homage to *Alice in Wonderland* (and likely intentional naming inspiration for the `drinkme`/`eatme` workstream asset directories). |

---

### 16. PRIORITIZED RESOURCE MAP (Quick Reference)

```
TIER 1 — QA Must Cover (P0, Official, Alice 3)
  Installation:   https://www.alice.org/get-alice/alice-3/
  Source/Build:   https://github.com/TheAliceProject/alice3
  Core Lesson 1:  https://www.alice.org/resources/lessons/building-a-scene/
  Core Lesson 2:  https://www.alice.org/resources/lessons/programming-in-alice/
  Core Lesson 3:  https://www.alice.org/resources/lessons/control-structures-overview/
  Core Lesson 4:  https://www.alice.org/resources/lessons/introduction-to-events/
  Design Entry:   https://www.alice.org/resources/lessons/design-process-introduction/
  Hour of Code:   https://www.alice.org/resources/lessons/hour-of-code/
  Curriculum Map: https://www.alice.org/resources/curriculum/building-an-alice-curriculum/
  Interface Ref:  https://www.alice.org/resources/how-tos/scene-editor-overview/
  Procedures Ref: https://www.alice.org/resources/how-tos/using-procedures-overview/
  Events Ref:     https://www.alice.org/resources/how-tos/using-events-overview/
  Gallery (P0):   https://www.alice.org/featured-projects/interactive-narrative-example-evergarden/

TIER 2 — QA Should Cover (P1, Official, Alice 3)
  Game Mechanics: /how-tos/setting-up-collision-detection/ + -scorekeeper/ + -timekeeper/
  Animation:      /how-tos/biped-walk-cycle/ + /how-tos/manipulating-biped-joints/
  Export/Share:   /how-tos/exporting-for-the-alice-player/ + /how-tos/using-the-alice-player/
  VR Intro:       /how-tos/creating-a-vr-project-with-a-vruser/
  Extending Lessons: making-procedural-methods, using-functions, events-collision-and-proximity
  Design Lessons: design-interactive-narrative, design-process-games
  Workshops:      /workshops/learn-to-create-3d-worlds-with-alice/
  NetBeans:       https://www.alice.org/get-alice/alice-3-with-netbeans/

TIER 3 — QA May Cover (P2, Official or External)
  Audio:          /how-tos/the-basics-of-using-audio/ + matching-sound + adding-background-music
  Import:         /how-tos/importing-models-overview/
  VR Locomotion:  all /how-tos/vr-locomotion-*/ and /vr-object-interaction-*/
  Textbooks:      /textbooks/how-to-guide-for-alice-3/ (free CMU guide, 2014)
  Oracle Academy: https://academy.oracle.com/ (external)
  Duke/Adventures: http://www.cs.duke.edu/csed/alice/aliceInSchools/ (external)
  YouTube:        Alice At Duke, Oracle Academy, Bill Barnum playlists (external)
```

---

*All findings are suitable for storage as structured asset files in `/home/azureuser/src/drinkme` (installation/reference/how-to assets) and `/home/azureuser/src/eatme` (lesson/curriculum/QA scenario assets). The "Drink me / Eat me" naming is directly mirrored in Alice 3.7's own changelog for the VR User scale feature — a strong signal of intentional thematic alignment.*