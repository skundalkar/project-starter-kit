# Prototype Pass

## Approval Status

- Status: Draft
- Approved by:
- Date:

## Purpose

This artifact records the concrete example walkthrough and Product Design Gate decisions used to challenge the product before formal implementation planning.

## Product Design Gate

### Strategy Check

- First user/job/outcome:
- Strategic wedge:
- First-session value:
- Intentional non-goals:

### Initial Product Noun Or Framing

Describe the user's starting noun or framing, such as dashboard, monitor, assistant, tracker, report, app, or workflow.

### Alternative Operating Models Considered

List competing product models considered before selecting the direction.

-

### Chosen Operating Model

Name the selected model and why it fits the user's job.

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

### Market Or Pattern Scan

Summarize any outside product patterns, public research, comparable tools, or vocabulary that changed the direction.

### Competitive / Comparable Products Lens

- Comparable products:
- Comparison dimensions:
- What to borrow:
- What to avoid:
- Differentiation implication:
- Feature decisions changed:

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

Describe or link to the sketch, diagram, sample output, mockup, image, or manual walkthrough result.

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
