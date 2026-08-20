# Project Starter Kit

Project Starter Kit is a Codex skill for starting new product ideas cleanly before implementation begins.

Use it when you have a rough idea but do not yet have evidence for a credible operating model, a clear product brief, an MVP boundary, a prototype challenge, or a build-ready handoff.

## Contents

- [How to start](#how-to-start)
- [End-to-end flow](#end-to-end-flow)
- [Expected outputs](#expected-outputs)
- [Gate catalog](#gate-catalog)
- [Opportunity & Evidence Gate](#opportunity--evidence-gate)
- [Prototype pass](#prototype-pass)
- [Triggered review tools](#triggered-review-tools)
- [Repo & Continuity Gate](#repo--continuity-gate)
- [After the starter artifacts](#after-the-starter-artifacts)

## What It Helps You Do

Project Starter Kit guides you from:

```text
I have an idea, but it is still fuzzy.
```

to:

```text
I know which opportunity direction the evidence supports, who this product is for, what the MVP should include, what assumptions were tested, and what a build agent should make next.
```

It is designed to clarify the product before Spec Kit, technical planning, tasks, or application code. Repository setup is handled by an explicit Repo & Continuity Gate once starter artifacts exist or implementation is about to begin.

## How To Start

In a new project conversation or folder, say:

```text
Use Project Starter Kit. Start.
```

Then describe your idea in a messy way. A sentence, paragraph, rough problem, or half-formed product thought is enough.

The skill will interview you lightly, one or two questions at a time. It will help clarify:

- which assumptions are hidden in the idea
- which public, paid/licensed, internal, or missing evidence sources matter
- which 2-3 operating models are credible and which first wedge is recommended
- what the product is
- who it is for
- the first real-use situation
- the current problem or unmet need
- the desired outcome
- the MVP loop
- what the product should create or show
- what should not be built yet
- what assumptions need to be tested before implementation

## End-To-End Flow

The gates are ordered so research and user-value decisions happen before design, and design decisions happen before requirements or build planning.

```text
Rough idea
-> Opportunity & Evidence Gate
   -> proceed with a chosen direction
   -> targeted research spike
   -> narrow or reframe
   -> stop or defer
-> Product Design Gate
-> Behavioral Contract
-> Example Prototype Pass
-> Readiness Check
-> project-brief.md + prototype-pass.md + build-brief.md
-> Build Continuation Track
   -> Validation Gate
   -> Business And Acquisition Gate, when triggered
   -> Visual Mock Gate, when triggered
   -> Health-Adjacent Safety Gate, when triggered and not already complete
   -> Build Readiness Gate
   -> Repo & Continuity Gate
-> project-index.md for durable projects
-> Spec Kit handoff
   -> specification approval
   -> technical-plan approval
   -> Intermediate Specialist Review Quality Gate, when triggered
   -> behavior/risk-to-task mapping
   -> tasks
   -> implementation
```

Some reviews are cross-cutting rather than fixed serial steps:

- Run the **Behavioral Delta Review** during discovery when changing an existing system.
- Run the **Health-Adjacent Safety Gate** before finalizing claims or scope whenever high-trust or sensitive domains appear.
- Run the **Product Artifact Review Gate** whenever a mock, report, chart, prototype, or implemented artifact exposes confusion or a new assumption.
- Run the **Async Orchestration Gate** when independent review, data, documentation, or verification work can safely proceed in parallel.
- Follow the **Triggered Tools Protocol** whenever a project-specific tool or review condition appears.

## Expected Outputs

By default, Project Starter Kit creates three starter artifacts:

```text
project-brief.md
prototype-pass.md
build-brief.md
```

`project-brief.md` captures the Opportunity & Evidence Gate decision and product truth: evidence basis, user, promise, situation, transformation, product rules, MVP boundary, and future vision.

`prototype-pass.md` captures how Product Design consumed that direction, the Behavioral Contract, a stable data/fixture boundary, and a concrete example walkthrough used to test assumptions before formal planning.

`build-brief.md` is the implementation handoff. It explains what to build, what not to invent, approved source constraints, stable build fixtures, expected user flow, data direction, AI or automation expectations, acceptance criteria, and validation expectations.

For `private_project`, `collaborative_project`, and `production_path`, the skill also creates `project-index.md` after shaping approval. The index is a read-order entry point to the three artifacts, not a fourth source of product truth.

## Gate Catalog

| Gate or checkpoint | When it runs | What it decides or produces | Detailed reference |
| --- | --- | --- | --- |
| Opportunity & Evidence Gate | Immediately after the rough idea, before strategy, Product Design, requirements, or specification | Evidence source map, research-sample limits, 2-3 credible operating-model options, recommendation, user decision, and one of four gate outcomes | [`opportunity-evidence-gate.md`](references/opportunity-evidence-gate.md) |
| Product Design Gate | After an opportunity direction is approved | Visual or structural concepts, interaction/operating flow, signal-to-evidence path, Behavioral Contract implications, and prototype questions | [`product-design-gate.md`](references/product-design-gate.md) |
| Behavioral Delta Review | When changing an existing system | Current-versus-intended behavior, affected surfaces, unchanged behavior, migration/compatibility concerns, and decisions needed | [`behavioral-delta-review.md`](references/behavioral-delta-review.md) |
| Health-Adjacent Safety Gate | When health, wellness, body, accessibility, safety, legal, financial, privacy, or other high-trust risk appears | Claim boundaries, safer wording, evidence needs, privacy controls, uncertainty language, and launch review requirements | [`health-adjacent-safety-gate.md`](references/health-adjacent-safety-gate.md) |
| Product Artifact Review Gate | After a concrete artifact exposes confusion, misleading semantics, source gaps, or product-form drift | Artifact-driven findings and required updates to product decisions, specs, tasks, or the next prototype | [`product-artifact-review-gate.md`](references/product-artifact-review-gate.md) |
| Async Orchestration Gate | When independent work can safely run beside the critical path | Main-agent critical path, bounded sidecar roles, allowed files, outputs, integration points, and stop conditions | [`async-orchestration-gate.md`](references/async-orchestration-gate.md) |
| Validation Gate | Before build handoff when value, behavior, trust, onboarding, safety, or retention assumptions remain unproven | Risk-surface validation plan, success thresholds, invalidation signals, fixtures, observable passes, and false-positive states | [`validation-gate.md`](references/validation-gate.md) |
| Business And Acquisition Gate | For consumer, paid, marketplace, community, education, productivity, health/wellness, or distribution-dependent products | Acquisition, activation, retention, monetization, buyer, trust, and pre-build validation hypotheses | [`business-acquisition-gate.md`](references/business-acquisition-gate.md) |
| Visual Mock Gate | Before implementation when text or a low-fidelity walkthrough cannot prove the first experience | Reviewable visual artifact, hierarchy, actions, states, trust signals, confusion findings, and visual approval status | [`visual-mock-gate.md`](references/visual-mock-gate.md) |
| Build Readiness Gate | Before Spec Kit handoff or implementation | Readiness status, blockers, deferred issues, required next action, approval owner, fixture completeness, and evidence boundaries | [`build-readiness-gate.md`](references/build-readiness-gate.md) |
| Repo & Continuity Gate | After starter artifacts and before Spec Kit, implementation, or milestone completion | Project scale, local/remote repository status, branch/commit/push state, artifact handling, and approved deferrals | [`repo-continuity-gate.md`](references/repo-continuity-gate.md) |
| Intermediate Specialist Review Quality Gate | After Spec Kit plan approval and before task generation, when specialist review is triggered | Bounded specialist findings, main-agent adjudication, approved plan changes, and behavior/risk-to-task coverage | [`spec-kit-start-protocol.md`](references/spec-kit-start-protocol.md#intermediate-specialist-review-quality-gate) |

Required non-gate checkpoints complete the flow:

| Checkpoint | Purpose | Detailed reference |
| --- | --- | --- |
| Behavioral Contract | Defines trigger, preconditions, input, state transitions, output, user controls, fallback, and must-not-happen behavior | [`start-protocol.md`](references/start-protocol.md#behavioral-contract) |
| Example Prototype Pass | Tests the contract with a concrete walkthrough and permitted real data or an explicit stable fixture | [`start-protocol.md`](references/start-protocol.md#required-example-prototype-pass) |
| Readiness Check | Confirms enough evidence, direction, behavior, scope, and continuity detail exists to draft formal artifacts | [`readiness-check.md`](references/readiness-check.md) |
| Triggered Tools Protocol | Applies available project/design/engineering review tools when their conditions appear and reports skipped triggers honestly | [`triggered-tools-protocol.md`](references/triggered-tools-protocol.md) |
| Spec Kit Start Protocol | Turns approved starter artifacts into specification, plan, reviewed tasks, and implementation without changing product truth silently | [`spec-kit-start-protocol.md`](references/spec-kit-start-protocol.md) |

## Opportunity & Evidence Gate

The first sentence is treated as a hypothesis, not as requirements. Before strategy or Product Design, the skill:

- surfaces assumptions and their consequences
- maps public, paid/licensed, internal, and missing evidence sources
- profiles a small, traceable research sample when useful and permitted
- inspects comparable operating models only when they change credible directions
- presents 2-3 evidence-grounded options, recommends a first wedge, and asks the user to decide

The outcome is to proceed, run a targeted research spike, narrow or reframe, or stop/defer. Evidence and decisions stay in the three starter artifacts and their Decision Ledger; the gate does not create another source of truth.

Research samples decide feasibility. Later stable, preferably anonymized build fixtures support mocks, walkthroughs, acceptance scenarios, and validation.

## Prototype Pass

After the Opportunity & Evidence direction and Product Design concept are chosen and the Behavioral Contract is explicit, the skill asks for or helps create one concrete example.

Examples:

- a real image for a visual product
- a sample CSV for an analytics product
- a messy note for a writing product
- a realistic scenario for a workflow product
- a manual AI response simulation for an AI-first product
- a wireframe or block diagram for an interaction-heavy product

The goal is to catch weak assumptions early, before code is written. The proof can combine visualizations with a concrete operating walkthrough and must use permitted real data or an explicitly mocked/fixture data set.

For visual, spatial, creative, AI-output, or interaction-heavy products, this prototype
pass is expected, not merely nice to have. The skill should help create a quick visual or
output artifact so the user can react to something concrete before implementation.

## Triggered Review Tools

Some tools are situational rather than always-on. In this kit, that means they are
triggered by the project shape or risk, not ignored until someone asks for them.

Examples:

- Use a GStack-style product/design challenge when the UI feels cluttered, unclear, or
  visually untrustworthy.
- Use Superpowers-style discipline when implementation starts, tests matter, or a branch
  is ready to finish.
- Use Compound Engineering-style notes when a reusable product, UX, or engineering lesson
  appears.
- Use a bounded specialist or multi-agent review when product, UI, feasibility, and QA
  questions can be challenged in parallel without slowing the main thread down.

If a tool is not installed, the skill should still apply the review lens manually and
say that no callable tool was available.


## Repo & Continuity Gate

After starter artifacts exist, the skill classifies project scale and reports repository status before Spec Kit or implementation.

Project scale options:

- `scratch`: throwaway exploration; Git optional
- `local_prototype`: useful local artifact; local Git required before implementation
- `private_project`: continuing project; private GitHub remote required before implementation unless explicitly deferred
- `collaborative_project`: multiple agents/users/reviewers; GitHub remote required before Spec Kit tasks or implementation
- `production_path`: deployable or long-lived work; GitHub remote, commit discipline, and milestone push checks required

The gate reports local Git status, branch, commit count, latest commit, GitHub remote, push status, repo URL, and any deferred decision.

## After The Starter Artifacts

After the three artifacts exist, the skill does not jump directly to implementation. When the user asks to continue toward a real build, it runs the Build Continuation Track in this order:

1. Validation Gate
2. Business And Acquisition Gate, when triggered
3. Visual Mock Gate, when triggered
4. Health-Adjacent Safety Gate, when triggered and not already complete
5. Build Readiness Gate
6. Repo & Continuity Gate

The skill reports blockers, deferred issues, and the exact next action rather than stopping at "not build ready." After readiness and repository state are explicit, it asks whether you want to create or confirm a GitHub repo and start the Spec Kit handoff.

If you say yes, the Spec Kit handoff protocol guides the next phase:

```text
Project Starter Kit artifacts
-> Spec Kit specification
-> technical plan
-> tasks
-> implementation
```

The skill expects approval gates before moving from specification to plan, and from plan to tasks/implementation.

## Useful When

Use Project Starter Kit when:

- you have an idea but not a clear MVP
- you want Codex to help discover the product before coding
- you want to avoid jumping straight into features
- you want a build agent to understand the product without guessing
- you want to test assumptions with a quick example before implementation
- you plan to hand the project into Spec Kit later

## Core Principle

Do not build first.

First clarify what should be built, why it matters, what the first version must prove, and what assumptions need to be challenged.
