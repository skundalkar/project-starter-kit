---
name: build-and-proof
description: Implement approved product or system behavior and prove it works with risk-matched evidence. Use when Codex is asked to build, change, fix, or complete an approved feature; execute Spec Kit tasks; apply behavior-driven development; design acceptance tests; diagnose a false-green test suite; verify an orchestrated workflow or external boundary; or produce a trace from approved behaviors and risks to tasks, tests, and evidence.
---

# Build & Proof

Implement the smallest approved behavior and produce evidence that matches how it can fail. Keep this skill focused on execution and proof; use Project Starter Kit or the active specification to shape product intent first.

## Inputs

Read the most specific available sources in this order:

1. `project-index.md`, when present
2. `project-brief.md`, `prototype-pass.md`, and `build-brief.md`
3. active spec, plan, tasks, and approved addenda
4. current code, tests, runtime configuration, and delivery state

Extract the approved behavioral contract, operating flow, execution boundaries, critical risk surfaces, and must-not-happen cases. If the requested behavior changes an existing system and its impact is unclear, require a current-behavior impact preview before implementation.

## Workflow

### 1. Establish Traceability

Create or update a compact trace using `templates/build-proof-trace.md`.

Map each approved behavior and critical risk to:

- source decision or requirement
- implementation task
- user-visible acceptance scenario
- component or unit checks
- operating-layer or boundary proof, when applicable
- resulting evidence

Do not let tasks exist without an approved behavior or risk, and do not let critical behaviors or risks remain unmapped.

### 2. Select Proof By Risk Surface

Read `references/risk-surface-validation.md` when choosing validation.

Use only applicable surfaces. Prefer the smallest proof that would fail if the required behavior were wrong. Record false-positive success states, such as a page rendering while its controls fail, a command succeeding while orchestration is broken, or a full file being covered with incorrect timing/state behavior.

### 3. Work Outside To Inside

For each behavior:

1. Write a user-visible Given/When/Then scenario from a concrete fixture.
2. Run it before implementation and observe red.
3. Verify red occurred for the intended missing or wrong behavior, not setup, syntax, dependency, fixture, permission, or environment failure.
4. Define the service/component contracts needed to satisfy the scenario.
5. Add focused unit checks for important internal decisions.
6. Implement the smallest coherent change.
7. Rerun the focused scenario, then relevant component checks, then the broader gate.

If a new test passes before the change, show why it is still meaningful or strengthen it until it detects the missing behavior.

### 4. Prove The Operating Layer

Distinguish:

- component proof: a parser, function, service, query, or command works in isolation
- operating-layer proof: the real UI, queue, orchestrator, upload path, retry loop, external service, deployment, or end-to-end state transition works

When behavior depends on sequencing, retries, idempotency, permissions, auth, billing, runtime mode, persistence, or deployment, test that boundary directly. Do not substitute a manual underlying command for proof of the workflow that is supposed to own it.

### 5. Capture Evidence

For each mapped item, record:

- command, scenario, or inspection run
- expected result
- observed result
- environment or delivery plane
- artifact, log, screenshot, trace, or test identifier
- limitations or unproved claims

Keep evidence concise and reproducible. Never report a local commit as pushed, a pushed change as deployed, or a deployed change as user-verified.

### 6. Finish Honestly

Before completion:

- confirm all approved behaviors and critical risks are mapped
- confirm intended-red evidence exists for new behavior tests when practical
- run relevant regression and quality gates
- inspect user-visible behavior when the change has a UI or workflow
- report what is proven, what remains unproven, and the exact next action

Hand continuity or cross-thread transfer to Continuity & Handoff rather than expanding this skill into a lifecycle manager.

## Output

Report:

- behavior implemented
- risk surfaces selected
- intended-red result
- focused and broader validation results
- operating-layer proof, if required
- trace/evidence location
- delivery state and remaining gaps

Do not claim success from test count alone.
