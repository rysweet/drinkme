# Alice website and reference map

Primary site: `https://www.alice.org/`  
Sitemap index: `https://www.alice.org/sitemap.xml`

The root page returned HTTP 500 during one fetch attempt, so this map relies on the sitemap, targeted public pages, and cross-checks against repository documentation.

## Sitemap categories

The WordPress sitemap exposes these categories:

- posts
- pages
- downloads
- featured projects
- lessons
- eap
- textbooks
- how-to
- curriculum
- workshop
- research
- taxonomies: category, post tag, resource type

## Notable product and download pages

- `https://www.alice.org/get-alice/`
- `https://www.alice.org/get-alice/alice-3/`
- `https://www.alice.org/get-alice/alice-3-with-netbeans/`
- `https://www.alice.org/get-alice/alice-3-player/`
- `https://www.alice.org/get-alice/alice-3-beta-vr/`
- `https://www.alice.org/get-alice/alice-2/`
- `https://www.alice.org/downloads/alice-3-windows-32-bit/`
- `https://www.alice.org/downloads/alice-3-windows-64-bit/`
- `https://www.alice.org/downloads/alice-3-linux/`
- `https://www.alice.org/downloads/alice-3-mac/`
- `https://www.alice.org/downloads/alice-3-download-instructions/`
- `https://www.alice.org/downloads/mediated-transfer-alice-3-to-java-pdf/`

## Teaching and reference collections

- Lessons: `https://www.alice.org/resources/alice-3-lessons/`
- How-tos: `https://www.alice.org/resources/alice-3-how-tos/`
- Curriculum: `https://www.alice.org/resources/alice-3-curriculums/`
- Workshops: `https://www.alice.org/workshops/`
- Textbooks: `https://www.alice.org/resources/alice-3-textbooks/`
- Research: `https://www.alice.org/research/`
- Java transition: `https://www.alice.org/alice-and-the-transition-to-java/`
- Mediated transfer research: `https://www.alice.org/research/mediated-transfer-alice-3-to-java/`

## Key product claims to preserve as behavior/spec targets

- Alice is a free CMU educational programming environment.
- Alice 3 is the newest Alice programming environment and emphasizes object-oriented concepts.
- Alice 3 supports animations, interactive narratives, and simple 3D games.
- Alice 3 includes a rich gallery of models and is intended to help students transition to Java.
- The Alice 3 NetBeans plugin supports moving Alice worlds into a Java development environment.
- The site positions Alice 2 as a simpler/older first environment and Alice 3 as the current object-oriented pathway.

## Licensing and resource constraints

From the source license and open-source announcement:

- Source and binary redistribution are allowed with required notices.
- Derivative products may not be called "Alice" or include "Alice" in their name without CMU permission.
- Advertising materials must acknowledge CMU-developed software.
- EA/Sims art assets are restricted to personal, non-commercial, academic use.
- Any derivative work using Sims 2 assets must preserve the relevant art-gallery license terms.
- Practical modernization implication: separate code refactoring from asset redistribution decisions, and keep a no-Sims build/test path healthy.

## References to convert into tests or traceability specs

| Reference area | Example URLs | Test/spec direction |
| --- | --- | --- |
| Product launch and download | `get-alice/alice-3`, platform download pages | installer smoke checks, launch checks, version metadata |
| Scene editor basics | scene editor quick references and how-tos | UI journey characterization, command availability |
| Adding objects/models | adding-object resources and gallery pages | model/resource loading and scenegraph construction |
| Alice 3 to Java | transition pages and PDF | NetBeans plugin, generated Java/project structure, mediated-transfer workflows |
| Lessons/curriculum | Alice 3 lessons/curriculums | behavior examples that should become executable fixtures |
| Research | mediated-transfer research pages | rationale for preserving block-to-Java mental model |

