# Project Starter Kit

Project Starter Kit is a Codex skill for starting new product ideas cleanly before implementation begins.

Use it when you have a rough idea but do not yet have a clear product brief, MVP boundary, prototype challenge, or build-ready handoff.

## What It Helps You Do

Project Starter Kit guides you from:

```text
I have an idea, but it is still fuzzy.
```

to:

```text
I know what this product is, who it is for, what the MVP should include, what assumptions were tested, and what a build agent should make next.
```

It is designed to happen before repository setup, Spec Kit, technical planning, tasks, or application code.

## How To Start

In a new project conversation or folder, say:

```text
Use Project Starter Kit. Start.
```

Then describe your idea in a messy way. A sentence, paragraph, rough problem, or half-formed product thought is enough.

The skill will interview you lightly, one or two questions at a time. It will help clarify:

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

`project-brief.md` captures the product truth: user, promise, situation, transformation, product rules, MVP boundary, and future vision.

`prototype-pass.md` captures a concrete example walkthrough used to test assumptions before formal planning.

`build-brief.md` is the implementation handoff. It explains what to build, what not to invent, expected user flow, data direction, AI or automation expectations, acceptance criteria, and validation expectations.

## Prototype Pass

Before formalizing the build brief, the skill asks for or helps create one concrete example.

Examples:

- a real image for a visual product
- a sample CSV for an analytics product
- a messy note for a writing product
- a realistic scenario for a workflow product
- a manual AI response simulation for an AI-first product
- a wireframe or block diagram for an interaction-heavy product

The goal is to catch weak assumptions early, before code is written.

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

## After The Starter Artifacts

After the three artifacts exist, the skill asks whether you want to create a Git repo and start the Spec Kit handoff.

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
