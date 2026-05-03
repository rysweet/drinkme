# Eatme review 0004: real Alice harness design

## Target

- Alice repo: `/home/azureuser/src/alice3-modernization`
- Real app entrypoint: `org.alice.stageide.EntryPoint` in `alice-ide`
- GUI stack: Java 21, Maven, Swing/Croquet main UI, JavaFX startup, JOGL/OpenGL rendering

## Key finding

Alice cannot be meaningfully exercised in pure CLI/headless mode.

`EntryPoint` extends `javafx.application.Application`; even with `-Djava.awt.headless=true`, JavaFX requires an X display:

```text
Caused by: java.lang.UnsupportedOperationException: Unable to open DISPLAY
```

`eatme` needs an X server, preferably `Xvfb`, plus screenshot and process/log observation tooling.

## Build commands

Fresh/full build path:

```bash
cd /home/azureuser/src/alice3-modernization
git submodule update --init tweedle-lang
git lfs pull
mvn -DincludeSims=false -Dinstall4j.skip -DskipTests -pl alice-ide -am package
```

Cached/offline path that worked during investigation:

```bash
cd /home/azureuser/src/alice3-modernization
mvn -o -DskipTests -DincludeSims=false -Dinstall4j.skip -pl alice-ide -am package
```

Observed artifacts after packaging:

```text
alice-ide/target/alice-ide-9.1.0-SNAPSHOT.jar
alice-ide/target/lib/
core/resources/target/distribution/application/starter-projects/*.a3p
```

The README launch command remains:

```bash
cd /home/azureuser/src/alice3-modernization/alice-ide
mvn exec:java -Dalice-ide
```

For harnessing, direct `java` after packaging is more deterministic because it avoids Maven dependency resolution during UI tests.

## Required system dependencies

The current machine was missing key GUI harness tools during investigation:

```text
Xvfb=missing
xvfb-run=missing
imagemagick/import=missing
scrot=missing
xdotool=missing
wmctrl=missing
```

Recommended Linux host setup:

```bash
sudo apt-get update
sudo apt-get install -y \
  xvfb xauth x11-utils x11-apps \
  imagemagick scrot xdotool wmctrl \
  mesa-utils libgl1-mesa-dri libglx-mesa0 libgtk-3-0 fonts-dejavu
```

Optional recording/debugging:

```bash
sudo apt-get install -y ffmpeg
```

## Direct launch under Xvfb

Prefer long-lived Xvfb so the harness can capture screenshots while Alice runs:

```bash
cd /home/azureuser/src/alice3-modernization

mkdir -p target/eatme-run/home target/eatme-run/prefs target/eatme-run/screens

Xvfb :99 -screen 0 1280x900x24 +extension GLX +render -noreset &
XVFB_PID=$!
export DISPLAY=:99
export LIBGL_ALWAYS_SOFTWARE=1

xdpyinfo >/dev/null
```

Then launch Alice:

```bash
FXMP="alice-ide/target/lib/javafx-base-21.0.7-linux.jar:alice-ide/target/lib/javafx-graphics-21.0.7-linux.jar:alice-ide/target/lib/javafx-media-21.0.7-linux.jar"

java \
  -ea \
  -Xmx1024m \
  -Dswing.aatext=true \
  -Dorg.alice.ide.rootDirectory=./core/resources/target/distribution \
  -Dcom.apple.mrj.application.apple.menu.about.name=Alice3 \
  -Dedu.cmu.cs.dennisc.java.util.logging.Logger.Level=WARNING \
  -Dorg.alice.ide.internalTesting=true \
  -Dorg.lgna.croquet.Element.isIdCheckDesired=true \
  -Djogamp.gluegen.UseTempJarCache=false \
  -Dorg.alice.stageide.isCrashDetectionDesired=false \
  -Dsun.java2d.cmm=sun.java2d.cmm.kcms.KcmsServiceProvider \
  -Duser.home=./target/eatme-run/home \
  -Djava.util.prefs.userRoot=./target/eatme-run/prefs \
  --add-opens=java.base/java.io=ALL-UNNAMED \
  --add-opens=java.desktop/sun.awt=ALL-UNNAMED \
  --add-opens=java.base/java.time=ALL-UNNAMED \
  --module-path "$FXMP" \
  --add-modules javafx.graphics,javafx.media \
  -cp "alice-ide/target/alice-ide-9.1.0-SNAPSHOT.jar:alice-ide/target/lib/*" \
  org.alice.stageide.EntryPoint \
  core/resources/target/distribution/application/starter-projects/africa.a3p \
  0 0 1000 740 \
  > target/eatme-run/alice.log 2>&1 &

ALICE_PID=$!
```

Direct Java needs `--module-path`; classpath-only launch fails with:

```text
Error: JavaFX runtime components are missing, and are required to run this application
```

## Smoke probes

```bash
sleep 20

jps -l | grep org.alice.stageide.EntryPoint || ps -p "$ALICE_PID"

grep -E "version:|Exception|SEVERE|Unable to open DISPLAY" target/eatme-run/alice.log | tail -80

wmctrl -lx
xdotool search --name Alice
```

Screenshot options:

```bash
import -window root target/eatme-run/screens/startup.png
scrot target/eatme-run/screens/startup.png
xwd -root -silent -out target/eatme-run/screens/startup.xwd
```

Clean shutdown:

```bash
wmctrl -c Alice || kill "$ALICE_PID"
kill "$XVFB_PID"
```

Use isolated `user.home` and `java.util.prefs.userRoot` so first-run/crash/prefs state does not pollute the real user profile.

## Minimal first real test

**Goal:** prove `gadugi-agentic-test` can launch and observe real Alice.

1. Build/package Alice.
2. Start Xvfb.
3. Launch Alice with `core/resources/target/distribution/application/starter-projects/africa.a3p`.
4. Wait up to 60 seconds.
5. Capture screenshot.
6. Agentic observer judges:
   - Alice main window is visible.
   - No crash dialog or Java exception dominates the screen.
   - A project or Alice start surface is visible.
   - Log contains `version:` and no fatal DISPLAY/OpenGL failure.

Do not start by asserting exact buttons, Swing component names, or coordinates.

## Gadugi invocation model

Recommended shape:

```yaml
scenario_under_test: real-alice-launch-smoke
harness:
  repo: /home/azureuser/src/alice3-modernization
  build:
    - mvn -o -DskipTests -DincludeSims=false -Dinstall4j.skip -pl alice-ide -am package
  display:
    server: Xvfb
    display: ":99"
    screen: "1280x900x24"
  launch:
    main_class: org.alice.stageide.EntryPoint
    starter_project: core/resources/target/distribution/application/starter-projects/africa.a3p
  observe:
    - process_alive
    - alice_log_tail
    - root_screenshot
    - optional_window_list
agentic_observer:
  mode: screenshot-plus-log
  instruction: >
    Judge the visible Alice user experience like a teacher/student would.
    Prefer robust visual evidence and recovery steps over brittle selectors.
```

Interaction model:

- Harness owns process, X display, screenshots, and logs.
- Agent observes screenshots/logs.
- Agent may request high-level actions like "click the visible Run button" or "press Escape if a modal is blocking."
- Executor translates those into `xdotool` clicks/keys from current screenshot evidence, not hard-coded selectors.
- Store screenshots/logs as test artifacts.

## Playwright relevance

Playwright is not the right tool for Alice itself. Alice is a desktop Swing/Croquet/JavaFX application, not a browser DOM.

Use Playwright only for Alice web docs/resource pages if a scenario explicitly tests documentation discovery. For the real IDE, use Xvfb plus screenshot/log/process observation.

## Risks

- Xvfb is currently absent on this machine.
- OpenGL/JOGL may need Mesa software rendering and GLX enabled.
- Fresh Maven builds may need network; online package attempt hit repeated `www.gnu.org` network failures.
- `mvn exec:java` from only `alice-ide` can fail unless reactor/local artifacts are installed; direct Java after package is more deterministic.
- First-run/crash dialogs can block tests.
- Swing-internal automation would be brittle. Prefer screenshot-based agentic observation.

## Validations tried

Succeeded:

```bash
java -version
mvn -version
git submodule status
mvn -o -DskipTests -DincludeSims=false -Dinstall4j.skip -pl alice-ide -am package
mvn -q -o -pl alice-ide -am -Dtest=LaunchConfigurationTest -Dsurefire.failIfNoSpecifiedTests=false test
```

Confirmed constraints:

```bash
# classpath-only direct Java
# => JavaFX runtime components are missing

# direct Java with JavaFX module path but no DISPLAY
# => Unable to open DISPLAY

# same with -Djava.awt.headless=true
# => Unable to open DISPLAY
```

Final Alice source status stayed clean during investigation.
