# Project Starter Kit: Triggered Tools Protocol

## Purpose

Use project tools as triggered challenge, discipline, and learning aids.

Triggered does not mean mandatory for every project. It means that when a trigger
condition appears, the agent must use the corresponding tool, use the corresponding
review lens, or clearly explain why it was skipped.

These tools must not change the approved product name, product promise, MVP boundary, or
core UX direction without user approval.

## Core Rule

Do not wait for the user to name a tool when the project shows a tool trigger.

If the environment has no callable tool installed, apply the review lens manually and
report it honestly, for example: `GStack-style review lens used; no callable GStack tool
was available`.

Do not use tools just to add ceremony. Use them when they can reveal risk, improve
quality, or capture a reusable decision.

## Required Visual Prototype Trigger

For visual, spatial, creative, AI-output, design-heavy, or interaction-heavy products,
run a fast visual/output prototype before implementation planning unless the user
explicitly skips it.

Prototype options:

- chat-generated image exploration
- wireframe
- UI block diagram
- workflow diagram
- sample output artifact
- annotated image
- clickable low-fidelity flow
- manual AI response simulation

The prototype pass must answer:

- What concrete input or scenario was used?
- What did the user expect to see or do?
- What artifact did the user review?
- What assumption changed?
- What MVP behavior changed?
- What must be tested in the real runtime path later?

## Reality Path Trigger

Before implementation, identify the real runtime path for every AI, vision, generation,
upload, device, auth, or integration capability.

Answer:

- Will this run in chat, local app, backend API, browser-only code, or mobile device?
- What credentials, billing, permissions, or platform access are required?
- Can one real user-provided input be tested before building the full UI?
- What fallback appears if the runtime path fails?

This prevents confusing chat-only capability with application/API capability.

## GStack

Repository:

- https://github.com/garrytan/gstack

Use for:

- product challenge
- design challenge
- engineering challenge
- QA challenge
- visual usability review
- low-friction UX review

Triggers:

- the product depends on visual trust, visual comparison, or spatial layout
- the user is reacting to UI confusion, clutter, unclear controls, or unclear workflow
- a screen/card/overlay/button exists but its value is unclear
- the output is visual but the implementation substitutes text, metadata, or placeholder UI
- the user says something like "what is this doing?", "why is this here?", "this is not useful", or "this looks cluttered"
- before approving visual or workflow-heavy product direction
- before declaring a UI or feature flow complete

Expected output:

- what screen, flow, or product promise was challenged
- what was removed or simplified
- what user expectation changed
- what should be prototyped visually before implementation continues

## Specialist Or Multi-Agent Review

Use specialist or multi-agent review only when separate viewpoints can run in parallel
without creating coordination drag.

Good use:

- a visual product needs a focused UI/UX review while implementation continues elsewhere
- the project has separate product, design, technical feasibility, and QA risks
- one agent is looping through too many roles and missing obvious issues
- a feature is expensive to implement and needs a quick challenge before code
- multiple independent artifacts can be reviewed at the same time

Poor use:

- the question is small enough for the main agent to answer directly
- the product direction is still too vague to brief a specialist
- the specialist would need the full conversation history instead of a tight brief
- coordinating agents would take longer than doing the work

Recommended specialist briefs:

- Product challenge: "Find unclear product promises, MVP drift, and missing user value."
- UI/UX challenge: "Review the screen or flow for clutter, unclear controls, missing
  visual proof, and low-friction user action."
- Feasibility challenge: "Check whether the proposed capability can run in the real
  runtime path with available credentials, billing, permissions, and APIs."
- QA challenge: "Identify untested visible UI actions, broken flows, stale data, and
  misleading success states."

Expected output:

- specialist role used
- exact artifact, screen, flow, or assumption reviewed
- top findings
- what changed because of the findings
- whether the finding should update `project-brief.md`, `prototype-pass.md`,
  `build-brief.md`, Spec Kit artifacts, tasks, or `docs/solutions/`

## Superpowers

Repository:

- https://github.com/obra/superpowers

Use for:

- disciplined implementation behavior
- branch or worktree discipline
- TDD where practical
- code review habits
- branch finishing

Triggers:

- implementation starts
- a meaningful feature begins
- visible behavior changes
- tests are missing or unclear
- the branch is ready to finish
- the user has a stated commit or merge preference

Expected output:

- branch/worktree status
- tests or verification run
- commit strategy used
- review or finish behavior applied

Do not duplicate baseline commit rules. Use Superpowers as an aid to enforce or review
the baseline expectations already defined in the Spec Kit start protocol.

## Compound Engineering

Repository:

- https://github.com/EveryInc/compound-engineering-plugin

Use for:

- simplifying meaningful features
- reviewing implementation decisions
- capturing reusable learnings
- documenting solution patterns

Triggers:

- a product assumption changes
- a feature is simplified after user feedback
- a runtime/platform constraint changes the implementation path
- a reusable UX, product, data, or engineering lesson appears
- a meaningful feature is completed
- before branch or milestone wrap-up

Expected output:

- short note in `docs/solutions/` when useful
- what was learned
- what decision changed
- what future agents should reuse or avoid

Examples of reusable learnings:

- visual products need real visual output, not explanatory placeholder UI
- do not claim an inventory item is used unless it appears in the generated image
- stale demo assets must not masquerade as results for a newly uploaded user input
- detection overlays should show only actionable objects
- chat-generated capability and local/API runtime capability must be checked separately
- every pause should state the next requirement or what is waiting on the user

## Reporting Requirement

If any triggered tool or framework is used, include the tool summary required by the
top-level Status Rule in `SKILL.md`.

For each tool or framework used, report:

- name of the tool or framework
- specific feature, mode, practice, or review used
- trigger condition
- why it was used
- artifact, file, or output produced
- decision changed, if any
- commit or file result, if applicable

If a trigger condition appeared and no tool or review lens was used, briefly explain why
it was skipped.
