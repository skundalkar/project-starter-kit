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

For every new or changed observable behavior, enforce this sequence:

1. Write one or more user-visible Given/When/Then scenario tests that drive representative inputs through a full run or operating flow and assert the observable outcome at the outside boundary.
2. Run the scenario tests before writing or changing production implementation code. They must be red.
3. Read the failure output and verify that each scenario is red because the approved behavior is missing or wrong, not because of setup, syntax, dependencies, fixtures, permissions, assertions, or an unavailable environment.
4. If a scenario is already green or fails for the wrong reason, stop. Correct or strengthen the test and fixture until it produces valid red evidence. An already-green test is regression coverage, not proof of a new behavior.
5. Derive the next service or component contract and write the smallest mechanistic test needed for that slice.
6. Run the mechanistic test, observe red, and verify its failure reason before changing production code for that slice.
7. Implement the smallest change that makes the mechanistic test green.
8. Repeat the mechanistic red/verified-red/green loop until the outside-in scenario test becomes green.
9. Rerun the scenario tests, relevant component checks, operating-layer proof, and broader regression gate.

Red before green is mandatory. Do not start production implementation without valid scenario-red evidence. Do not start a mechanistic implementation slice without valid mechanistic-red evidence. If the required scenario cannot run in the real test environment, report the work as blocked; do not substitute isolated unit tests or implementation by inspection.

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
- confirm valid scenario-red evidence predates production implementation for every new or changed observable behavior
- confirm each mechanistic implementation slice has red/verified-red/green evidence and the final outside-in scenario is green
- run relevant regression and quality gates
- inspect user-visible behavior when the change has a UI or workflow
- report what is proven, what remains unproven, and the exact next action

Hand continuity or cross-thread transfer to Continuity & Handoff rather than expanding this skill into a lifecycle manager.

## Output

Report:

- behavior implemented
- risk surfaces selected
- representative scenario, outside-observable assertion, and scenario-red command/failure/reason
- mechanistic red/verified-red/green sequence and final scenario-green result
- focused and broader validation results
- operating-layer proof, if required
- trace/evidence location
- delivery state and remaining gaps

Do not claim success from test count alone.
