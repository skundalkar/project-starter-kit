# Project Starter Kit

Project Starter Kit is a Codex skill for starting new product ideas cleanly before implementation begins.

Use it when you have a rough idea but do not yet have evidence for a credible operating model, a clear product brief, an MVP boundary, a prototype challenge, or a build-ready handoff.

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

After the three artifacts exist, the skill runs the Repo & Continuity Gate, then asks whether you want to create or confirm a GitHub repo and start the Spec Kit handoff.

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
