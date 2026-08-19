---
name: continuity-and-handoff
description: Preserve compact, executable continuity across Codex agents, threads, chats, compactions, long-running processes, milestones, and external waits. Use when work must be resumed, delegated, transferred, summarized for another task, paused safely, handed to a human or agent, or reported across local/commit/remote/CI/deployment states; also use by default at meaningful boundaries in multi-stage work.
---

# Continuity & Handoff

Maintain the smallest reliable working state that lets a human or next agent continue without reconstructing the project. This skill coordinates continuity; it does not replace product shaping, specifications, implementation, or validation.

## Inputs

When present, read `project-index.md` first, then its stated read order. Reuse approved Project Starter Kit artifacts, active specs/plans/tasks, current repository status, recent evidence, and explicit user decisions.

Separate:

- approved facts and decisions
- observed current state
- assumptions or inferences
- open questions
- external actions requiring approval

## Maintain The Working Contract

Keep a compact contract using `templates/continuity-handoff.md` or the same fields in the active project record:

- purpose
- inputs and assumptions
- current state
- outputs and evidence
- stop and escalation conditions

Update it after a scope decision, behavioral change, milestone, blocker, delivery transition, or handoff boundary. Do not turn it into a transcript or document dump.

## Maintain The Delivery Ledger

Track delivery planes separately:

1. working tree or generated artifact
2. local commit
3. remote branch and PR, when any
4. CI/review result
5. deployed environment and version
6. health/runtime verification
7. human-visible or user-verified behavior

Record `not applicable`, `not started`, `in progress`, `passed`, `failed`, or `unknown` rather than inferring later planes from earlier ones.

Never describe committed work as pushed, pushed work as deployed, or deployed work as user-verified.

## Detect Boundaries

Produce an executable handoff when:

- work moves to another agent, thread, chat, or process
- context compaction or a long pause risks losing state
- the project crosses shaping, specification, implementation, review, release, or incident boundaries
- progress depends on external approval, credentials, deployment, or human action
- a milestone completes and the next owner or action changes

Read `references/handoff-protocol.md` for the boundary checklist.

## Produce The Handoff

Lead with the useful state, not history. Include:

- one-sentence purpose and current outcome
- exact artifact/read order with resolvable paths or links
- approved behavior, scope, and must-not-drift decisions
- completed work and evidence
- delivery ledger
- current blockers, assumptions, and unresolved decisions
- exact next actions in order
- stop/escalation conditions and required authority

Make commands or next steps specific enough to execute, but do not include secrets. Name the environment, branch, version, fixture, or external system when material.

## Communicate To The Human

Every substantive boundary update should answer:

- What was just done?
- What decision or state changed?
- What is happening now?
- What comes next?
- What is waiting on the user or an external system?
- What evidence supports the status?

If work is continuing, say so. If paused, name the pause reason and restart condition. If blocked, distinguish a real authority/external dependency from work that can still proceed safely.

## Keep Continuity Compact

- Link to sources of truth; do not duplicate them.
- Preserve user-stated decisions verbatim when wording is behaviorally important.
- Use a Pyramid Index when one exists.
- Carry forward only evidence needed to make the next decision or action.
- Update stale status rather than appending conflicting status reports.
- Record contradictions explicitly and identify which source wins or who must decide.

## Output

Provide either a compact status update or executable handoff. State the current delivery plane and next action even when no file is created.
