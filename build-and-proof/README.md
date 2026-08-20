# Build & Proof

Build & Proof helps Codex implement an already-approved behavior and show convincing evidence that it works. It is deliberately narrower than a full product lifecycle: it owns execution and proof, not product discovery.

## When to use it

Use this skill when you want Codex to:

- build, change, fix, or finish an approved feature
- execute tasks from a specification or implementation plan
- write behavior-driven acceptance scenarios
- verify that a new test fails for the intended reason before fixing it
- choose tests based on the feature's real risks
- prove a UI, queue, upload, integration, retry loop, or deployed workflow—not only an isolated component

## How it works

1. Read the approved Project Starter Kit artifacts, specification, plan, and tasks.
2. Map each approved behavior and critical risk to implementation and verification work.
3. Start with a user-visible Given/When/Then scenario that drives representative input through a full run or flow and asserts the outside-observable result.
4. Run it before production implementation and confirm it is red because the behavior is missing or wrong, not because the test, fixture, environment, or setup is broken.
5. Treat an already-green new test as invalid intended-red evidence; strengthen it until it detects the missing behavior.
6. Implement from the outside in using mechanistic red/verified-red/green slices until the scenario becomes green.
7. Run proof that matches the risk surface, including the real operating layer when needed.
8. Record the scenario-red evidence, mechanistic sequence, final scenario-green evidence, broader checks, and current delivery state.

Red before green is mandatory for every new or changed observable behavior. If the representative scenario cannot run, implementation is blocked rather than allowed to proceed on unit tests or inspection alone.

## What's in this folder

- `SKILL.md` — the instructions Codex follows when the skill is active.
- `agents/openai.yaml` — the display name, description, and default prompt shown by Codex.
- `references/risk-surface-validation.md` — guidance for matching proof to behavioral, timing, state, data, integration, UI, safety, and delivery risks.
- `templates/build-proof-trace.md` — a reusable trace from approved behavior or risk to task, test, operating-layer proof, and evidence.

## Main output

The main artifact is a compact Build & Proof trace. It answers:

- What approved behavior changed?
- Which risks mattered?
- Did the acceptance test fail for the right reason before the fix?
- What component and operating-layer proof ran?
- What evidence exists, and what remains unproved?

### Evidence you should expect from every behavioral dev run

- scenario test ID/path and the representative fixture or input
- outside-observable outcome asserted by the scenario
- exact scenario-red command and concise failure excerpt
- confirmation that the fixture/environment was valid and the behavior—not the test harness—was missing or wrong
- evidence that production implementation started only after valid scenario red
- each mechanistic test's red command, verified failure reason, smallest implementation slice, and green result
- final scenario-green command and observable result
- operating-layer and broader regression proof

A final green test count without the preceding red evidence is insufficient.

### Who consumes the outputs

| Producer | Artifact or output | Next consumer | Why they need it |
| --- | --- | --- | --- |
| Project Starter Kit or specification phase | Approved behavioral contract, risk plan, spec, and tasks | Implementation agent using Build & Proof | Implement the agreed behavior without reopening product scope. |
| Implementation agent | Code change and Build & Proof trace | Independent verifier or reviewer | Check that the evidence detects the real failure modes and is not merely a passing component suite. |
| Independent verifier or reviewer | Verification findings and remaining gaps | Human decision-maker | Decide whether to approve, revise, merge, deploy, or accept a known limitation. |
| Build & Proof | Proven behavior, evidence links, and delivery state | Continuity & Handoff or the next agent | Preserve exact proof, unproved claims, and the first safe next action. |
| Human decision-maker | Approval or requested changes | Downstream review, release, or operations phase | Continue only with the accepted behavior and evidence threshold. |

```text
Project Starter Kit/specification
  -> approved behavior and risks
  -> implementation agent + Build & Proof trace
  -> independent verifier/reviewer
  -> human decision-maker
  -> Continuity & Handoff / downstream release phase
```

## Small example

**Before:** A transcript parser unit test passes, so the team says transcript replay works.

**After:** Build & Proof also runs a timestamped replay fixture through the real queue and state path. It proves that later transcript facts do not leak into earlier guidance, retries do not duplicate segments, and the UI shows complete chronological coverage.

## How it connects

Project Starter Kit shapes and approves the product, behavioral contract, operating flow, boundaries, and risk plan. Build & Proof consumes those artifacts and implements them.

Continuity & Handoff then preserves the result across agents, threads, milestones, and delivery stages. It carries forward the Build & Proof evidence without turning this skill into a project-management workflow.
