# Refactoring Teaching Record

This tutorial keeps a running record of RabbitHole refactors that are useful for
teaching good software engineering. It is not a changelog. It is a set of
repeatable lessons: what problem was found, what engineering habit fixed it, and
how to recognize the same problem elsewhere.

## How to use this record

For each example:

1. Start with the failure mode, not the implementation.
2. Add a characterization test or executable proof before changing behavior.
3. Move one boundary at a time.
4. Keep the old user-visible behavior unless the change is explicit and tested.
5. Merge only after review and the repository checks are green.

The point is not to admire the refactor. The point is to teach how not to make a
legacy system worse while improving it.

## Example 1: Move process termination to entry points

**Source example:** RabbitHole PR #883, "Restrict process termination to entry
points".

**Failure mode:** reusable code and exception handlers called `System.exit`
directly. That makes tests brittle and lets library code terminate Maven, CI, or
embedding tools.

**Engineering lesson:** process termination is an application boundary. Library
code should report intent with a typed result or exception. A real entry point
decides whether to show UI and exit.

**Teaching exercise:**

1. Search for direct `System.exit` calls.
2. Classify each call as entry-point, tool launcher, or reusable code.
3. Add an allowlist test for the calls that are still permitted.
4. Replace reusable-code exits with a narrow termination-intent API.
5. Keep the visible error message and exit code stable at the entry point.

**Why it matters:** hidden exits are operational traps. They make a codebase hard
to embed, hard to test, and easy to break from a harmless-looking code path.

## Example 2: Keep GUI behavior out of library code

**Source examples:** RabbitHole PR #846, PR #880, PR #892.

**Failure mode:** utility and resource code displayed modal Swing dialogs or
started GUI behavior in non-interactive contexts. CI then hung or failed under
Xvfb.

**Engineering lesson:** UI prompts belong behind a UI boundary. Core libraries
should return data, return `null` with an explicit log where that is the
established contract, or throw typed exceptions. They should not block on a
dialog.

**Teaching exercise:**

1. Search for `JOptionPane.show*` and dialog-opening methods outside UI adapter
   code.
2. Decide whether each call is application UI or library logic.
3. For library logic, add a test for the non-interactive behavior first.
4. Move prompting into an explicit application-level method or entry-point
   adapter.
5. Keep CI/headless/Xvfb behavior deterministic.

**Why it matters:** a modal dialog in the wrong layer is not a user experience.
It is a build deadlock wearing a button.

## Example 3: Turn reflection sweeps into smoke alarms, not specifications

**Source examples:** RabbitHole PR #889, PR #892.

**Failure mode:** class-loading and coverage sweeps invoked broad method sets by
reflection. Some methods opened dialogs, changed visibility, disposed windows, or
started launch paths.

**Engineering lesson:** reflection sweeps are coarse smoke tests. They should
prove "this surface does not explode when loaded," not "call every method and
hope." Important behavior needs explicit tests.

**Teaching exercise:**

1. Identify reflection-based exercisers.
2. Add filters for method families that perform UI, lifecycle, launch, print, or
   disposal behavior.
3. Add focused tests for the filter itself.
4. Write explicit tests for behavior that actually matters.
5. Keep the sweep small enough that a failure points to a class of problem, not
   a random side effect.

**Why it matters:** broad reflection is easy coverage and poor evidence. It finds
some crashes. It also creates crashes.

## Example 4: Make GUI CI prove one thing

**Source examples:** RabbitHole PR #880, PR #885.

**Failure mode:** headed GUI validation was mixed with full test execution,
workflow-local Xvfb setup, launcher process cleanup, and display-specific
failures. The result was a CI lane that was hard to reason about.

**Engineering lesson:** a GUI CI lane should prove a narrow contract. In this
case: can the documented no-Sims Alice GUI path build, start under Xvfb, and
avoid hanging?

**Teaching exercise:**

1. Put Xvfb setup in one reusable action or script.
2. Use the same resilient flags everywhere:
   `--auto-servernum -s "-screen 0 1024x768x24 -ac"`.
3. Bound GUI startup with a timeout and a process-tree cleanup path.
4. Keep headless full tests in the headless lane.
5. Treat Xvfb as proof of startup/display integration, not as a second copy of
   every unit test.

**Why it matters:** mixing too many contracts into one CI job makes failures
ambiguous. Ambiguous CI gets ignored.

## Example 5: Data-driven migration with parity checks

**Source examples:** RabbitHole PR #881, PR #882, PR #884.

**Failure mode:** text migrations were historically encoded in large Java
registries. Moving them to JSON made them easier to inspect, but it also created
risk: order, null replacement semantics, and generated data drift could change
old project behavior.

**Engineering lesson:** data-driven does not mean "trust the data." Parity tests
must compare the old registry, generated representation, committed resource, and
runtime loader.

**Teaching exercise:**

1. Extract canonical migration data from the legacy source.
2. Compare it to the generated JSON.
3. Compare generated JSON to the committed resource.
4. Add runtime loader tests for edge cases such as `null` replacement entries.
5. Do not manually edit generated migration data.

**Why it matters:** migrations are compatibility code. If they are wrong, old
projects fail later and far from the change that broke them.

## Example 6: Avoid filesystem fallbacks that scan the world

**Source example:** RabbitHole PR #892.

**Failure mode:** a missing resource directory fell back to the user's home
directory. Downstream code then recursively scanned for JSON, causing long hangs
and unpredictable behavior.

**Engineering lesson:** fallback paths need blast-radius limits. If a resource
root is missing, fail clearly or return an explicit empty result. Do not guess a
large filesystem root.

**Teaching exercise:**

1. Find fallback-to-home or fallback-to-current-directory behavior.
2. Add a test that proves the fallback does not scan outside the intended root.
3. Return `null`, an empty collection, or a typed error according to the existing
   contract.
4. Log enough context to diagnose the missing resource root.
5. Keep recursive scans behind an explicit root, never a convenience fallback.

**Why it matters:** accidental filesystem breadth is a performance bug and a
reliability bug. It also makes local machines lie to you.

## Candidate lessons still worth extracting

These are not yet as clean as the examples above, but they are good teaching
targets.

| Candidate | Lesson to teach | First safe move |
| --- | --- | --- |
| Static clipboard/DnD operation maps | Global mutable state leaks across tests and sessions | Add scoped registry characterization before replacing static maps |
| NetBeans generated-source tests | Packaging and generated-source correctness are different contracts | Move pure generated-source assertions out of packaging-heavy tests |
| Time-based waits in tests | Sleeps are not synchronization | Replace with latches, polling conditions, or test hooks |
| Story/resource model loading | Discovery needs bounded roots and explicit missing-resource behavior | Add root-boundary tests before refactoring discovery |

## Review checklist for future entries

Before adding a refactor to this tutorial, answer these questions:

1. What concrete failure mode did it remove?
2. What characterization test would have failed before the fix?
3. What boundary became cleaner?
4. What behavior was intentionally preserved?
5. What future mistake should this example prevent?

If those answers are vague, it is not a teaching example yet. It is just a pull
request.
