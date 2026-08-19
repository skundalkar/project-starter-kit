# Continuity & Handoff

Continuity & Handoff keeps work understandable and executable when it moves between agents, threads, chats, processes, milestones, or human approvals. It preserves the smallest reliable state needed to continue without reconstructing the project from history.

## When to use it

Use this skill when:

- another agent, thread, or process will continue the work
- a long pause or context compaction could lose important state
- the project crosses shaping, specification, implementation, review, release, or incident boundaries
- progress depends on approval, credentials, deployment, or another external action
- the human asks what is done, pushed, deployed, verified, blocked, or next

## How it works

1. Read the Project Starter Kit Pyramid Index and source artifacts when present.
2. Maintain a compact working contract: purpose, inputs and assumptions, current state, expected outputs and evidence, and stop or escalation conditions.
3. Keep a delivery ledger that separates local work, commits, remote state, CI/review, deployment, runtime health, and human verification.
4. Detect meaningful boundaries and create an executable handoff.
5. Give the next owner an exact read order, approved constraints, evidence, blockers, and ordered next actions.
6. Tell the human what was done, what changed, what is happening now, what comes next, and what is waiting.

## What's in this folder

- `SKILL.md` — the continuity and handoff instructions Codex follows.
- `agents/openai.yaml` — the skill's display metadata and default prompt.
- `references/handoff-protocol.md` — the boundary checklist, handoff quality test, and contradiction-handling guidance.
- `templates/continuity-handoff.md` — a reusable working contract, delivery ledger, handoff, and human status format.

## Main outputs

Depending on the boundary, the skill produces either:

- a compact current-state update, or
- an executable handoff containing source-of-truth read order, approved decisions, evidence, delivery state, blockers, next actions, and escalation rules.

## Small example

**Before:** A new thread hears, “The feature is done,” but cannot tell whether changes are only local, committed, pushed, deployed, or tested by the user.

**After:** The handoff states that the code is committed and pushed, CI is green, staging is deployed and healthy, production is untouched, and user verification is still pending. It links the exact artifacts and names the first next action.

## How it connects

Project Starter Kit establishes the approved product direction and creates the project-package entry point. Continuity & Handoff keeps that package current and usable across boundaries without replacing its source artifacts.

Build & Proof supplies implementation and validation evidence. Continuity & Handoff records the delivery plane, carries that evidence forward, and makes the next step executable.
