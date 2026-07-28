# Project Starter Kit: Async Orchestration Gate

## Purpose

Use this gate to decide whether a project step should run with sidecar specialist work instead of one long serial conversation.

The goal is not "more agents." The goal is to keep the critical path moving while independent review, data, documentation, or verification work happens in parallel.

## Trigger Conditions

Run this gate when:

- the user asks to spin up agents, use async work, or run work in parallel
- artifact review reveals multiple independent questions
- a data job may take time while product/design work can continue
- specialist review would improve quality without blocking the main step
- documentation capture can happen while implementation or analysis continues
- verification can run in parallel with non-overlapping work

## Critical Path First

Before delegating, define:

```text
Critical path:
Sidecar candidates:
What the main agent will do now:
What results are needed later:
```

Do not delegate the immediate blocker. If the next local action depends on a result, the main agent should usually do that work locally.

## Sidecar Roles

Use only the roles that match the work:

| Role | Use For | Typical Output |
| --- | --- | --- |
| Product Intent Reviewer | Product fit, MVP boundary, user inference | Alignment findings and next questions |
| UI Interpretation Reviewer | Visual clarity, scan path, misleading layout | UI findings with smallest changes |
| Metric Semantics Reviewer | Scores, percentages, counts, windows, baselines | Reconciliation table and label fixes |
| Data Honesty Reviewer | Source completeness, filtered/sampled data, blockers | Coverage findings and supported claims |
| Actionability Reviewer | What user should do after a signal | Action ladder and evidence needed |
| Documentation Capture Agent | Manuals, schema examples, durable decisions | Doc draft and spec/task updates |
| Data Worker | Fixture generation, corpus scan, report creation | Generated files, commands, blockers |
| Verification Reviewer | Build/test/UI inspection | Verification report and failures |

## Delegation Contract

Every sidecar prompt must include:

- role and expertise lens
- exact question
- repo or artifact scope
- files it may inspect
- files it may edit, if any
- files it must not edit
- whether to commit
- output format
- when the main agent should wait or continue

For code-editing sidecars, assign disjoint write scopes. Avoid having two agents edit the same file.

## Wait Policy

- Continue main-path work after launching sidecars.
- Wait only when the result is needed for the next critical-path action.
- If a sidecar stalls, close it and recover the work locally or restart with a narrower prompt.
- Do not keep broad stalled agents open indefinitely.

## Integration Policy

When sidecar results return:

1. Summarize findings.
2. Identify contradictions.
3. Decide accepted vs deferred findings.
4. Update spec/tasks/docs for accepted changes.
5. Apply implementation only after the source of truth is updated.
6. Report which sidecars were used and what changed.

## No Duplication Rule

Project Starter Kit remains the orchestrator.

Do not create overlapping gates for the same concern. Use this ownership model:

```text
Product Design Gate:
  Challenges product form before or during prototype.

Product Artifact Review Gate:
  Reviews concrete artifacts after user reaction.

Async Orchestration Gate:
  Decides what work can run in parallel.

Repo & Continuity Gate:
  Handles Git/GitHub/project preservation.

Spec Kit Protocol:
  Handles spec/plan/tasks/implementation sequencing.
```

## Output Format

```text
Async orchestration decision:
- Critical path:
- Sidecars launched:
- Sidecars skipped:
- Reason:
- Main agent next action:
- Integration point:
```
