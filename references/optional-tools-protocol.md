# Project Starter Kit: Optional Tools Protocol

## Purpose

Use optional project tools as challenge, discipline, and learning aids.

These tools may improve the product and implementation process, but they must not change the approved product name, product promise, MVP boundary, or core UX direction without user approval.

## When To Consider Optional Tools

Consider optional tools at these points:

- during the example prototype pass
- before approving visual or workflow-heavy product direction
- after Spec Kit creates the specification, plan, or tasks
- during implementation of meaningful features
- before declaring a UI or feature flow complete
- after a product or technical decision changes
- before branch or milestone wrap-up

Do not use optional tools just to add ceremony. Use them when they can reveal risk, improve quality, or capture a reusable decision.

## gstack

Repository:

- https://github.com/garrytan/gstack

Use for:

- product challenge
- design challenge
- engineering challenge
- QA challenge
- visual usability review
- low-friction UX review

Best fit:

- prototype pass before Spec Kit
- first-screen review
- visual/workflow approval
- UI flow review during implementation
- feature-complete UX review

Expected value:

- identify unnecessary UI
- expose unclear workflows
- reduce text-heavy approval burden
- improve visual usability
- challenge whether the product output is actually useful

## Superpowers

Repository:

- https://github.com/obra/superpowers

Use for:

- disciplined implementation behavior
- branch or worktree discipline
- TDD where practical
- code review habits
- branch finishing

Best fit:

- implementation start
- before or during meaningful feature work
- before commit
- before merge or branch finish
- when the work risks becoming messy or under-tested

Expected value:

- cleaner implementation flow
- fewer accidental changes
- stronger test behavior
- better review before finishing
- better branch hygiene

Do not duplicate baseline commit rules. Use Superpowers as an optional aid to enforce or review the baseline expectations already defined in the Spec Kit start protocol.

## Compound Engineering

Repository:

- https://github.com/EveryInc/compound-engineering-plugin

Use for:

- simplifying meaningful features
- reviewing implementation decisions
- capturing reusable learnings
- documenting solution patterns

Best fit:

- after a meaningful feature
- after a product or technical pivot
- after solving a reusable implementation problem
- before branch or milestone wrap-up

Expected value:

- simpler implementation
- clearer rationale
- reusable notes for future agents
- solution records in `docs/solutions/` when useful

## Reporting Requirement

If any optional tool or framework is used, include the tool summary required by the top-level Status Rule in `SKILL.md`.

For each tool or framework used, report:

- name of the tool or framework
- specific feature, mode, practice, or review used
- why it was used
- artifact, file, or output produced
- decision changed, if any
- commit or file result, if applicable

If no optional tools or frameworks were used, no tool summary is required unless the user asks.
