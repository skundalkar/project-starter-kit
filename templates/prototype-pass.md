# Prototype Pass

## Approval Status

- Status: Draft
- Approved by:
- Date:

## Purpose

This artifact records how Product Design consumed the approved Opportunity & Evidence direction, the Behavioral Contract, and the concrete example walkthrough used to challenge the product before formal implementation planning.

## Opportunity & Evidence Gate Inputs

- Approved user/job/outcome and first wedge:
- Chosen operating model and evidence basis:
- Rejected alternatives and why:
- Approved source, access, license, cost, privacy, and trust constraints:
- Research-sample limitations:
- Accepted or deferred evidence gaps:

### Research Sample Record

- Source and retrieval date:
- Access/use terms and sampling method:
- Entities, fields, relationships, identifiers, granularity, and formats:
- Freshness, coverage, missingness, quality, bias, and uncertainty:
- What the sample supports:
- What it does not support:

The research sample decides feasibility or direction. It is not automatically a build fixture.

## Product Design Gate

### Approved Strategy Check

- First user/job/outcome:
- Strategic wedge:
- First-session value:
- Intentional non-goals:

### Approved Operating-Model Direction

Describe the operating model chosen by the Opportunity & Evidence Gate and the initial noun or framing it replaced.

### Visual Or Structural Concepts Considered

List 2-3 competing interaction models or information hierarchies tested within the approved direction.

-

### Chosen Concept And Interaction Model

Name the selected concept, interaction/operating flow, and why it fits the user's job.

### Primary User Inference

State what the user should understand, decide, compare, trust, or do after using the product.

### Signal-To-Evidence Path

Describe the path from first signal to supporting evidence.

```text
signal
-> driver
-> evidence
-> interpretation
-> optional next action
```

### Entity And Time Context

List the main entities and time contexts that must remain visible or explainable.

### Metric And Label Semantics

Define important scores, labels, categories, thresholds, or statuses. Remove or rename any that remain unclear.

### Misinterpretation Risks

List what the user could wrongly infer and how the product should prevent that.

### Focused Evidence Reopened During Design

- Concrete design decision blocked:
- Newly exposed evidence gap:
- Smallest permitted source or sample used:
- Access, cost, privacy, and stop limits:
- Finding and concept decision changed:
- Opportunity & Evidence section and Decision Ledger updated:

### Concepts Tested And User Critique

List visual or structural concepts tested, what confused the user, and what changed because of critique.

## Behavioral Contract

- Trigger:
- Preconditions:
- Input and unit of work:
- State transitions and timing/order:
- Output:
- User controls:
- Completion behavior:
- Failure/fallback:
- Must not happen:

## Behavioral Delta Review

Complete when changing an existing system. Summarize the current-system impact preview from `references/behavioral-delta-review.md`.

| Dimension | Current behavior | Likely behavior after requested change | Intended behavior | Decision needed |
| --- | --- | --- | --- | --- |

## Operating Flow

```text
Start trigger -> intake -> validation -> processing stages -> visible intermediate states -> review/approval -> final artifact -> save/reuse
```

## Execution-Boundary Map

| Component or surface | Responsibility | Real/mocked/manual/deferred | External dependency | Auth/billing/permission | Data crossing boundary | Fallback |
| --- | --- | --- | --- | --- | --- | --- |

## Example Input Or Scenario

Describe the real image, sample file, user scenario, messy source input, workflow, sketch, or manual AI simulation used.

## Assumptions Tested

List the assumptions being tested before the walkthrough.

-

## Expected Product Loop

1. User starts by:
2. Product should respond with:
3. User reviews/edits/chooses:
4. Product should produce:

## Prototype Or Walkthrough Output

Describe or link to the visualization, sketch, diagram, sample output, mockup, image, and concrete operating walkthrough result.

## Proof Data Boundary

- Real data used with permission:
- Explicitly mocked, synthetic, or anonymized build fixture:
- Fixture version/schema and stable location:
- Expected outcomes and edge states:
- How this fixture differs from the research sample:
- What the proof supports and does not support:

## What Worked

-

## What Broke Or Became Doubtful

-

## Decisions Changed

List product, UX, MVP, platform, data, AI, or feasibility decisions changed because of this pass.

## Decision Ledger

| Decision | Status | Evidence or reason | Affected sections | Approval owner |
| --- | --- | --- | --- | --- |

## MVP Changes Required

List the specific MVP scope, UX, platform, data, AI, or validation changes required by this pass.

## Validation Plan

- Target users:
- Riskiest assumption:
- Validation question:
- Test method:
- Script:
- Success threshold:
- Invalidation signal:
- What changes if validation fails:

## Project Scale Notes

- Current project scale:
- Does the prototype suggest this should remain scratch/local, become a private project, become collaborative, or move toward production?
- Repository or continuity implication:


-

## Visual Approval Notes

If this is a visual, spatial, workflow-heavy, or interaction-heavy product, include what visual artifact was used or what visual artifact is still needed.

## Visual Mock Gate

- Visual artifact:
- First screen:
- Primary user inference:
- Primary action:
- Secondary actions:
- Information hierarchy:
- What is immediately clear:
- What is confusing or crowded:
- What should be removed:
- What must be visible before implementation:
- Visual approval status:

## Remaining Feasibility Risks

-

## Prototype Status

Choose one:

- Proceed
- Re-run prototype pass
- Blocked until more information is available

Reason:
