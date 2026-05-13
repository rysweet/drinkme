# Alice 3 Web Migration: Technical Feasibility Analysis

**Date:** July 2025
**Repository:** `rysweet/RabbitHole` (fork of `TheAliceProject/alice3`)
**Methodology:** Static analysis of the actual codebase, dependency mapping, and research of comparable migration projects.

---

## Executive Summary

Alice 3 is a ~474K-line Java codebase (164K lines of handwritten Java across ~5,200 source files, plus ~310K lines of generated model resource code in `target/`) with deep coupling to Java Swing for the IDE and JOGL for 3D rendering. A full web migration is a multi-year, high-risk undertaking. No comparable project (Greenfoot, Processing, Alice itself at CMU) has successfully migrated a Java 3D educational environment to the web — every successful web educational environment (Scratch 3.0, p5.js web editor) was a ground-up rebuild.

The recommended approach is **Option C: Gradual migration** — build a new TypeScript/React/Three.js web frontend for a narrowly scoped "player" experience first, reading existing `.a3p`/`.a3w` project files, while the Java IDE continues to serve as the authoring tool.

---

## 1. Current Architecture Assessment

### 1.1 Module Map and Size

The codebase is organized as a Maven multi-module project with 22 modules:

| Module | Java Files | Lines | Role |
|--------|-----------|-------|------|
| `core/ide` | 1,624 | 187,629 | IDE framework, editors, operations, gallery browser |
| `core/story-api` | 509 | 60,322 | Runtime API for Alice programs (`SThing`, `SScene`, `SModel`) |
| `core/croquet` | 409 | 46,404 | Custom MVC/UI framework (Croquet) |
| `core/util` | 418 | 42,044 | Math, property system, general utilities |
| `core/ast` | ~350 | 34,420 | Legacy AST representation (pre-Tweedle) |
| `core/models` | ~200 | 24,094 | Generated model resource classes (gallery metadata) |
| `core/glrender` | ~100 | 21,176 | JOGL OpenGL rendering backend |
| `core/story-api-migration` | ~150 | 17,258 | Project I/O, format migration (XML ↔ JSON) |
| `core/scenegraph` | ~120 | 16,671 | Platform-independent scene graph abstraction |
| `core/model-loading` | ~50 | 8,219 | Collada/glTF import, model export |
| `core/tweedle` | ~60 | 5,944 | Tweedle parser (ANTLR), AST, VM |
| `external/collada` | ~40 | 5,899 | Collada XML parser |
| `core/image-editor` | 12 | 2,089 | Image editing composites |
| `core/issue-reporting` | 12 | 1,258 | Bug report UI |
| `alice-ide` | 7 | 827 | Application entry point, launcher |
| **Total** | **~5,200** | **~474K** | |

### 1.2 Subsystem Dependency Graph

```
alice-ide (EntryPoint)
  └─ core/ide (187K lines — the biggest module by far)
       ├─ core/croquet (custom MVC framework)
       │    └─ javax.swing.* (deeply embedded)
       ├─ core/story-api (runtime objects: SThing, SScene, SModel, SCamera)
       │    ├─ core/scenegraph (platform-independent scene graph)
       │    ├─ core/glrender (JOGL rendering — GLJPanel, GLEventListener)
       │    │    └─ com.jogamp.opengl.* (native OpenGL)
       │    ├─ core/tweedle (Tweedle language)
       │    │    └─ tweedle-lang/Grammar/*.g4 (ANTLR grammars)
       │    └─ core/ast (legacy AST)
       ├─ core/model-loading (Collada/glTF import)
       │    └─ external/collada (Collada parser)
       └─ core/story-api-migration (project I/O — .a3p/.a3w)
            └─ core/tweedle (manifest, resource refs)
```

### 1.3 Platform Coupling Analysis

#### Tightly Coupled to Java/Swing/JOGL (cannot be extracted without rewrite)

| Subsystem | Lines | Coupling Severity | Details |
|-----------|-------|-------------------|---------|
| **core/ide** | 187K | **Critical** | 2,952 files across the repo import `javax.swing.*` or `java.awt.*`; `core/ide` is the densest concentration. Every UI component is a Swing `JPanel`/`JComponent`. The Croquet framework is a Swing MVC layer. Drag-and-drop uses `java.awt.dnd.Transferable`. |
| **core/croquet** | 46K | **Critical** | Custom UI framework built entirely on Swing. `Composite<V extends JComponent>`, `Operation` fires Swing `ActionEvent`, views are `JPanel` subclasses. |
| **core/glrender** | 21K | **Critical** | Directly wraps JOGL. `GlrOnscreenRenderTarget` extends `GLJPanel`. `RenderTargetImp` attaches `GLEventListener`. Every class imports `com.jogamp.opengl.*`. |
| **core/image-editor** | 2K | **High** | Swing-based image editing UI. |

#### Partially Coupled (mixed platform-specific and portable logic)

| Subsystem | Lines | Portable Fraction | Details |
|-----------|-------|-------------------|---------|
| **core/story-api** | 60K | ~40% | `SThing`/`SScene`/`SModel` are thin wrappers; the public API could be re-exposed. Implementation classes (`*Imp`) call into `scenegraph` and `glrender`. |
| **core/util** | 42K | ~60% | Math (`AffineMatrix4x4`, vectors, quaternions), property system, string utils are portable. Some utilities use `java.awt.Image`/`BufferedImage`. |

#### Platform-Independent (extractable or directly translatable)

| Subsystem | Lines | Portability | Details |
|-----------|-------|-------------|---------|
| **core/scenegraph** | 17K | **High** | Abstract scene graph: `Scene`, `Component`, `Composite`, `Visual`, `Geometry`, `Mesh`, `Joint`, `Camera`, `Light`. Depends only on `core/util`. No Swing/JOGL imports. **This is the key abstraction layer.** |
| **core/tweedle** | 6K | **High** | ANTLR grammar (489 lines), AST nodes, `VirtualMachine`. Grammar is language-agnostic. Parser uses standard ANTLR visitor pattern. |
| **core/story-api-migration** | 17K | **High** | Project I/O reads/writes zip archives with XML/JSON. Uses standard `java.util.zip`, Jackson JSON, DOM XML. Logic is algorithmic, not UI-bound. |
| **core/model-loading** | 8K | **Medium** | Collada/glTF import logic is algorithmic but outputs `scenegraph` objects that expect `glrender`. |
| **core/models** | 24K | **Medium** | Generated resource metadata classes. Structure is data, not behavior. |
| **tweedle-lang** | 7K `.twe` | **High** | 154 Tweedle library files defining the standard library (`SThing`, `SScene`, shapes, events, tweens). Pure source text. |

### 1.4 Key Architectural Observations

1. **The scenegraph is already abstracted from the renderer.** `core/scenegraph` defines platform-neutral nodes (`Scene`, `Visual`, `Mesh`, `Joint`). `core/glrender` implements `RenderFactory`/`RenderTarget` against JOGL. A Three.js backend could implement the same `RenderFactory` interface.

2. **The Tweedle language is small and well-defined.** The grammar is 489 lines of ANTLR (175 lexer + 315 parser rules). It's a Java-like language with Alice-specific constructs (`doInOrder`, `doTogether`, `eachTogether`, `countUpTo`). The AST has ~30 node types. The VM is a simple tree-walking interpreter.

3. **Project I/O is a zip-based format.** `.a3p` files are ZIP archives containing `manifest.json`, `programType.xml` (or `.twe` source), `resources.xml`, and binary resource entries. The `.a3w` player export uses the same format with Tweedle source under `src/`. Both are readable with standard zip libraries in any language.

4. **The IDE is the hard part.** `core/ide` alone is 187K lines — more than the rest of the codebase combined. It implements: scene editor with 3D manipulation handles, code editor with drag-and-drop block programming, gallery browser with model search/preview, property editors, type hierarchy browsers, and a complex undo/redo system built on Croquet's `AbstractEdit` framework.

5. **The gallery is a separate asset problem.** 3D models are in Collada format (imported via `JointedModelColladaImporter`) and a custom binary format. The gallery metadata is generated into Java classes (`core/models`). The gallery itself is ~10GB+ of assets not stored in this repository — it's a distribution/CDN problem independent of the code migration.

---

## 2. Web Migration Options

### Option A: Full Rewrite in TypeScript/React + Three.js

**Approach:** Build a new web application from scratch, reimplementing the IDE, renderer, language runtime, and project I/O in TypeScript.

| Criterion | Assessment |
|-----------|-----------|
| **Feasibility** | **3/5** — Technically possible but enormous scope. The Scratch 3.0 rewrite took 3+ years with a team at MIT + Google partnership. Alice is more complex (3D vs 2D, custom language vs blocks). |
| **Effort** | **36–60 person-months** (3–5 engineers × 12 months) |
| **Risk** | **High** — Feature parity is a moving target. The existing Java codebase has 20+ years of edge cases, accessibility fixes, and curriculum-specific behaviors. Reimplementing `core/ide` (187K lines) alone is a year+ effort. |

**What translates well:**
- Tweedle grammar → ANTLR TypeScript target (`antlr4ng`) — direct port of `.g4` files
- Scenegraph → Three.js `Object3D` hierarchy — close conceptual mapping
- Project I/O → JSZip + DOM parser — straightforward
- Standard library `.twe` files — unchanged, just loaded by the TS parser

**What must be reimplemented:**
- Entire IDE UI (187K lines of Swing → React components)
- Croquet MVC framework (46K lines → React state management + hooks)
- Drag-and-drop code editor → custom React DnD or Blockly integration
- 3D scene editor with manipulation handles → Three.js + `@react-three/drei` TransformControls
- Undo/redo → Immer patches or custom command pattern
- Gallery browser → new React component + asset CDN

**What would break:**
- Pixel-perfect UI compatibility (Swing layout ≠ CSS layout)
- Any curriculum that depends on specific IDE UI workflows
- Platform-specific behaviors (file dialogs, drag from OS, print)

### Option B: Electron Wrapper Around Existing Java App

**Approach:** Package the Java application inside Electron, possibly using a local HTTP bridge between the Node.js process and a headless JVM.

| Criterion | Assessment |
|-----------|-----------|
| **Feasibility** | **2/5** — This doesn't actually solve the web deployment problem. You'd still need a JVM. It adds complexity (two runtimes) without enabling browser-based access. |
| **Effort** | **6–12 person-months** |
| **Risk** | **Medium** — Fragile integration layer. JOGL rendering inside Electron would require native OpenGL context sharing, which is unsupported. |

**What works:**
- Native file system access (Electron can shell out to `java -jar`)
- Could wrap the existing app as an Electron "window" if rendered server-side

**What doesn't work:**
- JOGL cannot render into an Electron-managed window directly
- No path to browser-based deployment
- Two runtime environments to install and update
- Doesn't reduce the Java dependency

**Verdict:** This is not a migration — it's wrapping duct tape around the existing architecture. Only useful as a distribution mechanism if the goal is "desktop app with auto-update", not "web accessible".

### Option C: Gradual Migration — Web Frontend + Java Backend API

**Approach:** Build a new web frontend (React/Three.js) that talks to the Java backend via HTTP/WebSocket API. The Java side handles project I/O, Tweedle compilation, and heavy lifting. The web side handles rendering and UI.

| Criterion | Assessment |
|-----------|-----------|
| **Feasibility** | **4/5** — The most pragmatic option. Each piece can be built and validated incrementally. The scenegraph abstraction already separates rendering from the object model. |
| **Effort** | **12–24 person-months** for a useful first milestone |
| **Risk** | **Medium** — Network latency between frontend and backend. Need to define a clean API boundary. Risk of "two codebase" maintenance burden. |

**Phase 1 (3–6 months): Player/Viewer**
- Web app that opens `.a3p`/`.a3w` files and renders the 3D scene
- TypeScript Tweedle parser (port the ANTLR grammar)
- Three.js renderer consuming the scenegraph data
- No editing, no IDE — just "play" a project

**Phase 2 (6–12 months): Editing**
- Scene editor with Three.js TransformControls
- Property panels in React
- Project save/load (client-side zip handling)
- Java backend for model gallery serving

**Phase 3 (12–24 months): Full IDE**
- Code editor (drag-and-drop or Monaco-based)
- Gallery browser
- Undo/redo
- Migrate Java backend logic to TypeScript (eliminate server dependency)

**What would break:**
- IDE workflows change (different UI)
- Some file format edge cases during transition
- Gallery serving requires either a server or CDN migration

### Option D: CheerpJ / WebSwing — Run Java in Browser

**Approach:** Use CheerpJ (WebAssembly JVM) or WebSwing (server-side rendering) to run the existing Java app in a browser.

| Criterion | Assessment |
|-----------|-----------|
| **Feasibility** | **1/5** — Both technologies explicitly do not support JOGL or hardware-accelerated 3D. This is a hard blocker, not a limitation to work around. |
| **Effort** | **2–4 person-months** to attempt, then discover it doesn't work |
| **Risk** | **Critical** — JOGL is architecturally incompatible with both platforms. The 3D rendering that is the core educational value of Alice would not function. |

**CheerpJ specifics:**
- Runs Java bytecode in browser via WebAssembly JIT
- Supports Swing/AWT (renders to HTML5 Canvas)
- **Does NOT support JOGL** — no JNI, no native OpenGL
- Performance: 5–20x overhead vs native JVM for Swing apps
- Initial load: 40–80MB runtime download
- Free for personal use; commercial license required

**WebSwing specifics:**
- Runs JVM server-side, streams rendered frames to browser via WebSocket
- **"3D hardware-accelerated content is not supported"** — their own docs
- Requires server infrastructure (200–500MB RAM per concurrent user)
- Network latency makes 60fps 3D rendering impossible
- Fine for form-based enterprise apps; unsuitable for real-time 3D

**What would break:**
- All 3D rendering (the core of Alice)
- Performance would be unacceptable for educational use
- CheerpJ: any native library dependency (JOGL, audio codecs)
- WebSwing: requires always-on server infrastructure

**Verdict:** Dead on arrival for Alice. These tools are designed for enterprise Swing form applications, not 3D educational environments.

---

## 3. Key Technical Challenges

### 3.1 3D Rendering: JOGL → Three.js/WebGL

**Complexity: HIGH (but tractable)**

The good news is that Alice's scenegraph (`core/scenegraph`, 17K lines) is already abstracted from the renderer. The key mapping:

| Alice Scenegraph | Three.js Equivalent |
|-----------------|---------------------|
| `Scene extends Composite` | `THREE.Scene` |
| `Component` (abstract node) | `THREE.Object3D` |
| `AbstractTransformable` | `THREE.Object3D` (has `.position`, `.rotation`, `.scale`) |
| `Visual extends Leaf` | `THREE.Mesh` |
| `Geometry` / `Mesh` / `WeightedMesh` | `THREE.BufferGeometry` |
| `Joint` | `THREE.Bone` / `THREE.SkinnedMesh` |
| `Camera` variants | `THREE.PerspectiveCamera` / `THREE.OrthographicCamera` |
| `Light` variants | `THREE.PointLight` / `THREE.DirectionalLight` |
| `Background` | `scene.background` |
| `RenderFactory` → `GlrRenderFactory` | `THREE.WebGLRenderer` |
| `AffineMatrix4x4` | `THREE.Matrix4` |

The hard parts:
- **Skinned mesh / joint animation** — Alice uses `WeightedMesh` with custom vertex skinning in JOGL shaders. Three.js has `SkinnedMesh` but the vertex weight format must be translated.
- **Custom shaders** — `RenderTargetImp` (500+ lines) implements multi-pass rendering, picking (ray casting for mouse interaction), and silhouette rendering. Each must be reimplemented.
- **Model format conversion** — Alice's internal model format is Collada-based but stored in a custom binary layout. The `JointedModelColladaImporter` (in `core/model-loading`) would need a TypeScript equivalent, or models could be pre-converted to glTF.

**Estimated effort:** 4–8 person-months for a functional renderer. 8–12 to reach full feature parity with the JOGL renderer.

### 3.2 Tweedle Language: AST/Compiler/VM

**Complexity: MEDIUM (well-bounded)**

Tweedle is a small language:
- **Grammar:** 489 lines of ANTLR (175 lexer tokens, 315 parser rules)
- **AST:** ~42 node types (`TweedleExpression`, `TweedleStatement`, `DoInOrder`, `DoTogether`, `ForEachLoop`, `CountUpLoop`, `ConditionalStatement`, `ReturnStatement`, etc.)
- **VM:** Tree-walking interpreter with `Frame`-based scope (`VirtualMachine.java`, ~200 active lines)
- **Standard library:** 154 `.twe` files, 6,920 lines (type definitions for `SThing`, `SScene`, shapes, events, tweens)

**Migration path:**
1. Use ANTLR's TypeScript target to generate a TS parser from the existing `.g4` grammars. The `antlr4ng` runtime is the best choice — it's a complete TypeScript rewrite with best-in-class performance.
2. Port the ~42 AST node classes to TypeScript interfaces/classes.
3. Port the tree-walking interpreter (`VirtualMachine`) to TypeScript.
4. The `.twe` standard library files are loaded unchanged — they're source text, not compiled artifacts.

**Key Alice-specific constructs to handle:**
- `doInOrder { ... }` — sequential statement execution (default in most languages, but explicit in Alice)
- `doTogether { ... }` — concurrent execution of child statements (requires coroutine/promise-based scheduling)
- `eachTogether (Type item in collection) { ... }` — parallel iteration
- `countUpTo (i < N) { ... }` — counting loop
- `<-` assignment operator (instead of `=`)
- `@PrimeTime` / `@TuckedAway` / `@CompletelyHidden` visibility annotations

**The `doTogether` construct is the hardest part.** In the Java VM, concurrent execution uses Java threads. In a browser, this must use `Promise.all()`, `requestAnimationFrame` scheduling, or a cooperative coroutine system. Getting the timing semantics right (all concurrent statements should progress at the same animation rate) requires careful design.

**Estimated effort:** 3–5 person-months.

### 3.3 File Format Compatibility (.a3p, .a3w)

**Complexity: MEDIUM**

`.a3p` (editor project) and `.a3w` (player export) are ZIP archives with a well-documented structure:

```
my-project.a3p
├── version.txt              # Archive format version
├── manifest.json            # Project metadata (Jackson-serialized)
├── programType.xml          # Legacy: XML-encoded AST
│   — OR —
├── src/Program.twe          # Modern: Tweedle source
├── resources.xml            # Legacy: resource metadata
├── resources/               # Binary resources (images, audio)
│   ├── image-uuid-1.png
│   └── audio-uuid-2.mp3
└── thumbnail.png            # Optional project thumbnail
```

**Migration path:**
- ZIP handling: `JSZip` library (browser) or Node.js `yauzl`
- JSON manifest: `JSON.parse()` — trivially portable
- XML program type: `DOMParser` (browser-native) for the legacy format. The XML schema is documented in `XmlProjectIo.java` (567 lines).
- Tweedle source: parsed by the TypeScript ANTLR parser
- Resources: binary blobs, no conversion needed

**Risk:** The XML format (`programType.xml`) has evolved through multiple versions. `XmlProjectIo.java` contains migration logic for older formats. A TypeScript reader would need to handle the same version variations or only support modern (JSON/Tweedle) project files.

**Estimated effort:** 2–4 person-months (modern format only: 1–2 months; full legacy support: 3–4 months).

### 3.4 Model Gallery (10GB+ of 3D Assets)

**Complexity: HIGH (infrastructure, not code)**

The gallery contains 3D character models (bipeds, animals, vehicles, props) contributed by Electronic Arts (Sims 2 assets) and CMU. Key issues:

1. **Format:** Models are in Collada format, imported via `JointedModelColladaImporter`. The web standard is glTF/GLB. A batch conversion pipeline (Collada → glTF) is needed.

2. **Size:** The full gallery is 10GB+. This cannot be bundled with a web app. Options:
   - CDN-hosted asset library with on-demand loading
   - Compressed glTF (Draco/meshopt compression can reduce 10:1)
   - Progressive loading (thumbnails first, full model on demand)

3. **Licensing:** The EA/Sims 2 assets have restrictive licensing ("personal, non-commercial, and academic use only"). Web distribution may require legal review.

4. **Metadata:** Model gallery metadata is generated into Java classes (`core/models`, 24K lines). This needs to be exported as a JSON catalog for the web gallery browser.

**Estimated effort:** 3–5 person-months (conversion pipeline + CDN + gallery browser UI).

### 3.5 Drag-and-Drop Visual Programming

**Complexity: HIGH**

Alice's code editor is not a text editor — it's a visual drag-and-drop programming interface where:
- Method bodies are composed by dragging statement tiles into a vertical stack
- Expressions are dragged into slots within statements
- The gallery panel lets you drag objects into the scene
- Parameter values are selected from popup menus, not typed

This is implemented in `core/ide` using Java's `java.awt.dnd.*` API, custom `Transferable` types, and Croquet's composite system.

**Web alternatives:**
- **Blockly (Google):** Used by Scratch 3.0. Block-based programming in the browser. Could represent Tweedle programs as blocks. However, Alice's visual style (statement tiles, not interlocking blocks) is different from Blockly's jigsaw metaphor.
- **Custom React DnD:** Using `react-dnd` or `@dnd-kit/core` to build a custom drag-and-drop code editor that matches Alice's visual style. Higher effort but more faithful.
- **Monaco Editor with custom rendering:** Use Monaco as the code editor engine but add a custom visual rendering layer on top. Good for text representation but doesn't match Alice's tile-based approach.

**Estimated effort:** 6–10 person-months for a faithful recreation. 3–5 months if the UI paradigm is simplified (e.g., Blockly-based).

### 3.6 Undo/Redo System

**Complexity: MEDIUM**

Alice's undo/redo is built on Croquet's `AbstractEdit` framework — each operation creates an `Edit` object that knows how to undo/redo itself. The edit history is managed by a Croquet `UndoManager`.

**Web equivalent:** This pattern maps cleanly to:
- **Command pattern** with explicit undo/redo operations
- **Immer** + patch-based history (record structural changes as patches)
- **Zustand** or **Redux** with middleware for action replay

**Estimated effort:** 2–3 person-months (integrated with the larger IDE effort).

### 3.7 Project Persistence

**Complexity: LOW–MEDIUM**

Web options for project storage:
- **Client-side:** `File System Access API` (Chrome/Edge), `IndexedDB` for auto-save, download-as-file for explicit save
- **Server-side:** Cloud storage (S3/Azure Blob), user accounts with project lists
- **Hybrid:** Local-first with optional cloud sync

The `.a3p` zip format can be read/written entirely client-side using `JSZip`. The `File System Access API` provides native save-file dialogs in Chromium browsers.

**Estimated effort:** 1–2 person-months.

---

## 4. Prototype Scope

### The Smallest Useful Demo: "Hello World Player"

**Goal:** Open an existing `.a3p` or `.a3w` file in a browser, render the 3D scene, and execute the program.

**Target lesson:** The Alice tutorial "Hello World" — a scene with one character that says "Hello World" via a speech bubble and performs a simple animation (wave, turn).

#### Minimum Requirements

| Component | Minimum Viable Implementation |
|-----------|------------------------------|
| **File loading** | `<input type="file">` → JSZip → parse `manifest.json` + Tweedle source |
| **Tweedle parser** | ANTLR TypeScript parser from existing `.g4` grammars |
| **Tweedle VM** | Execute `myFirstMethod()` — sequential statement execution, `say()`, `move()`, `turn()` |
| **Scene graph** | Load scene description → Three.js `Object3D` tree |
| **3D rendering** | Three.js with placeholder geometries (boxes/cylinders for characters). Full model loading is NOT required for the prototype. |
| **Animations** | `move()`, `turn()`, `say()` — basic tween interpolation via Three.js or `gsap` |
| **UI** | Play/pause button. No editing. |

#### What the Prototype Proves

1. **Tweedle → TypeScript works:** The ANTLR grammar generates a working TS parser.
2. **Project files are readable:** The `.a3p` zip format can be parsed client-side.
3. **Three.js can render Alice scenes:** The scenegraph mapping is viable.
4. **The `doTogether` / animation scheduling model works in JS.**

#### What the Prototype Does NOT Prove

- IDE editing feasibility
- Drag-and-drop code editing
- Full model gallery loading
- Performance at scale (complex scenes with many actors)
- Desktop parity (offline, file associations)

#### Estimated Effort for Prototype

| Task | Person-Weeks |
|------|-------------|
| ANTLR TypeScript parser generation + validation | 2 |
| Tweedle AST + minimal VM (sequential execution, method calls) | 3 |
| `.a3p` file reader (JSZip + manifest parser) | 1 |
| Three.js scene renderer (placeholder geometries) | 2 |
| Animation system (`move`, `turn`, `say`, `doTogether`) | 2 |
| Integration + "Hello World" demo | 1 |
| **Total** | **~11 person-weeks (2.5–3 months for one engineer)** |

### Could It Load an Existing `.a3p` File?

**Yes, with limitations.** The prototype can parse the ZIP, read `manifest.json`, and extract Tweedle source. It can execute the program logic. The limitation is 3D model rendering — existing `.a3p` files reference models by resource class name (e.g., `AliceResource`, `MarchHareResource`), and the prototype would need either:
- A mapping from resource names to pre-converted glTF files (manual for the prototype), or
- Placeholder geometries (colored boxes with labels)

The second option is sufficient for proof-of-concept and avoids the model conversion pipeline entirely.

---

## 5. Pros and Cons Summary

| Approach | Pros | Cons |
|----------|------|------|
| **A. Full Rewrite** | Clean architecture. Modern stack. Best long-term outcome. No Java dependency. | Enormous effort (36–60 PM). Feature parity takes years. Risk of "second system syndrome". Curriculum disruption during transition. |
| **B. Electron Wrapper** | Quick to prototype. Reuses existing code. | Doesn't enable web access. Still requires JVM. JOGL incompatible with Electron rendering. Adds complexity without solving the core problem. |
| **C. Gradual Migration** | Incremental value delivery. Java backend handles hard parts initially. Web frontend can be user-tested early. Risk is bounded per phase. | Two codebases to maintain during transition. API design is critical and hard to change later. Network latency for server-backed features. |
| **D. CheerpJ/WebSwing** | Minimal code changes. | **JOGL not supported by either platform.** 3D rendering (the core of Alice) would not function. Dead on arrival. |

### Decision Matrix

| Criterion (weight) | A: Full Rewrite | B: Electron | C: Gradual | D: CheerpJ/WebSwing |
|---------------------|:-:|:-:|:-:|:-:|
| Browser deployment (30%) | ★★★★★ | ★☆☆☆☆ | ★★★★☆ | ★☆☆☆☆ |
| 3D rendering works (25%) | ★★★★★ | ★★☆☆☆ | ★★★★☆ | ☆☆☆☆☆ |
| Time to first value (20%) | ★☆☆☆☆ | ★★★☆☆ | ★★★★★ | ★★☆☆☆ |
| Maintenance burden (15%) | ★★★★★ | ★★☆☆☆ | ★★☆☆☆ | ★★★★☆ |
| Feature parity risk (10%) | ★★☆☆☆ | ★★★★★ | ★★★☆☆ | ★☆☆☆☆ |
| **Weighted Score** | **3.4** | **2.2** | **3.8** | **0.8** |

---

## 6. Recommendation

### Recommended Approach: Option C — Gradual Migration (Web Player First)

Given the educational mission, the 20-year investment in the Java codebase, and the research showing that no comparable project has successfully ported (as opposed to rewritten) a Java 3D educational environment, we recommend:

#### Phase 0: Prototype (3 months, 1 engineer)
Build the "Hello World Player" prototype described in Section 4. This validates:
- Tweedle grammar → TypeScript parser
- `.a3p` file reading in the browser
- Three.js rendering of Alice scenes
- Animation scheduling (`doTogether` semantics)

**Exit criterion:** Open the Alice "Hello World" tutorial `.a3p` file in a browser and watch it execute.

#### Phase 1: Web Player (6 months, 2 engineers)
- Full Tweedle VM execution
- Model loading (Collada → glTF conversion pipeline for the gallery)
- Scene rendering with actual 3D models
- Sound/audio playback
- Shareable URLs ("view this project in your browser")

**Exit criterion:** Students can share Alice projects as web links. Teachers can embed projects in course pages.

#### Phase 2: Web Scene Editor (12 months, 3 engineers)
- Three.js scene editor with object manipulation
- Property panels
- Gallery browser (CDN-hosted models)
- Project save/load (client-side)
- The Java IDE remains the primary authoring tool; the web editor handles simple edits

**Exit criterion:** Simple scene composition and modification in the browser.

#### Phase 3: Full Web IDE (18–24 months, 3–4 engineers)
- Code editor (drag-and-drop or hybrid)
- Full gallery integration
- Undo/redo
- Account system, cloud projects
- Deprecate Java IDE for new users

**Exit criterion:** New students can complete the standard Alice curriculum entirely in the browser.

### Why Not a Full Rewrite?

The Scratch 3.0 rewrite succeeded because:
1. MIT had Google's partnership and engineering resources
2. Scratch's 2D Canvas rendering is much simpler than 3D JOGL
3. Flash was literally being killed by browsers (existential threat)
4. The Blockly block editor existed as leverage

Alice lacks all four of these conditions. A full rewrite is the right long-term architecture but the wrong starting point. The gradual approach delivers value (shareable project links) in months, not years, and each phase validates the next.

### Critical Path Risks

1. **`doTogether` semantics in JavaScript** — The concurrent execution model must be proven in the prototype. If it can't faithfully reproduce Alice's animation timing, the entire migration is at risk.
2. **3D model conversion at scale** — The 10GB+ gallery must be converted from Collada to glTF. Batch conversion may reveal model-specific issues (rigging, UV mapping, textures).
3. **EA/Sims 2 licensing for web distribution** — The gallery's restrictive license may prohibit CDN hosting. Legal review needed before Phase 1.
4. **Two-codebase maintenance** — During the gradual migration, bugs must be fixed in both Java and TypeScript. This is the primary cost of the gradual approach.

### Technology Stack Recommendation

| Layer | Technology | Rationale |
|-------|-----------|-----------|
| **UI Framework** | React 19+ | Ecosystem, tooling, hiring pool |
| **3D Rendering** | Three.js via `@react-three/fiber` | Declarative scene graph matches Alice's model |
| **Tweedle Parser** | `antlr4ng` (ANTLR TypeScript runtime) | Direct port of existing `.g4` grammars; best TS perf |
| **State Management** | Zustand or Jotai | Lightweight, React-friendly, supports undo/redo middleware |
| **Project I/O** | JSZip + File System Access API | Client-side zip handling, native save dialogs |
| **Build Tool** | Vite | Fast dev server, good TypeScript support |
| **Desktop (future)** | Electron or Tauri | Same web codebase, offline support |
| **Model Format** | glTF/GLB | Web standard; Draco compression for CDN |
| **Asset CDN** | Azure Blob / CloudFront | Gallery hosting with geographic distribution |

---

## Appendix A: Comparable Migration Outcomes

| Project | Original | Web Version | Approach | Timeline | Outcome |
|---------|----------|-------------|----------|----------|---------|
| **Scratch** | Flash/ActionScript | React/JS/Canvas | Full rewrite | 3+ years (2016–2019) | Success. 100M+ users. |
| **Processing** | Java Swing/JOGL | p5.js (JS/WebGL) | Parallel new project | Ongoing since 2013 | Success. Both coexist. Java IDE never migrated. |
| **Greenfoot** | Java Swing | N/A | No migration | — | Still desktop-only (2024). |
| **Eclipse** | Java SWT | Theia (TS/Monaco) | Full rewrite (different project) | 5+ years | Success, but Theia is not Eclipse. |
| **Alice 3** | Java Swing/JOGL | N/A | No migration | — | Still desktop-only (2024). |

**Pattern:** Every successful migration was either a full rewrite by a well-resourced team or a parallel new project that didn't try to be the old one.

## Appendix B: Tweedle Grammar Quick Reference

The Tweedle language (489 lines of ANTLR grammar) supports:

```
// Class and enum declarations
class MyClass extends SBiped {
    // Fields with left-arrow assignment
    Number speed <- 1.0;
    
    // Methods with visibility annotations
    @PrimeTime void myFirstMethod() {
        // Sequential by default
        doInOrder {
            this.say(text: "Hello!");
            this.move(direction: MoveDirection.FORWARD, amount: 1.0);
        }
        
        // Concurrent execution
        doTogether {
            this.turn(direction: TurnDirection.LEFT, amount: 0.5);
            this.say(text: "Turning!");
        }
        
        // Iteration
        forEach (SThing thing in this.scene.getThings()) {
            thing.setOpacity(opacity: 0.5);
        }
        
        // Counting loop
        countUpTo (i < 5) {
            this.move(direction: MoveDirection.UP, amount: 0.1);
        }
    }
}
```

Key types: `Boolean`, `Number`, `DecimalNumber`, `WholeNumber`, `TextString`
Keywords unique to Alice: `doInOrder`, `doTogether`, `eachTogether`, `countUpTo`, `models`, `constant`, `<-` (assignment)
Visibility: `@CompletelyHidden`, `@TuckedAway`, `@PrimeTime`

## Appendix C: `.a3p` Archive Structure

```
my-project.a3p (ZIP)
│
├── version.txt                    # "38.0" (format version)
├── manifest.json                  # ProjectManifest (Jackson)
│   {
│     "description": { "name": "MyProject", "icon": "thumbnail.png" },
│     "metadata": { "fileType": "a3p", "formatVersion": "..." },
│     "provenance": { "aliceVersion": "3.9.0" },
│     "resources": [
│       { "type": "image", "name": "background.png", "file": "resources/img-uuid.png" },
│       { "type": "audio", "name": "music.mp3", "file": "resources/aud-uuid.mp3" }
│     ],
│     "prerequisites": { ... }
│   }
│
├── programType.xml                # Legacy XML AST (XmlProjectIo)
│   — OR —
├── src/Program.twe                # Modern Tweedle source (JsonProjectIo)
│
├── resources.xml                  # Legacy resource metadata
├── resources/                     # Binary resource entries
│   ├── img-uuid-1.png
│   └── aud-uuid-2.mp3
└── thumbnail.png                  # Project thumbnail (optional)
```

The `JsonProjectIo` path (modern) uses `manifest.json` + `.twe` files.
The `XmlProjectIo` path (legacy) uses `programType.xml` + `resources.xml`.
Both are readable from the same ZIP archive. A web reader should support both.
