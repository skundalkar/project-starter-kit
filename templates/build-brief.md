# Build Brief

## Approval Status

- Status: Draft
- Approved by:
- Date:

## Build Readiness Gate

- Readiness status:
- Blocking issues:
- Deferred issues:
- Required before implementation:
- Who must approve:

## How To Use This Brief

Use this file as the implementation handoff after reading `project-brief.md` and `prototype-pass.md`.

The product direction and MVP boundary come from `project-brief.md`.

The approved Opportunity & Evidence direction comes from `project-brief.md`. The Product Design Gate decisions, focused evidence findings, Behavioral Contract, and prototype learnings come from `prototype-pass.md`.

Do not change the approved product name, promise, MVP boundary, or core UX direction without asking the user.

## Build Goal

Describe the MVP to build in one paragraph.

## Source Artifacts

- `project-brief.md`
- `prototype-pass.md`

## MVP Scope

## Must Build

- 

## Must Not Build Yet

- 

## Do Not Invent

List things the implementation agent must not add unless the user explicitly approves them.

- 


## Repository And Continuity Gate

Before implementation starts, report:

- Project scale:
- Local Git repo:
- Current branch:
- Commit count:
- Latest commit:
- GitHub remote:
- Pushed to remote:
- Repo URL:
- Deferred repository decision, if any:

For private, collaborative, or production-path projects, do not begin implementation until GitHub setup is completed or explicitly deferred by the user.

## Implementation Priority

Build in this order unless there is a clear technical reason to adjust:

1. 
2. 
3. 

## Product Operating Model

State the operating model approved by the Opportunity & Evidence Gate and the visual/interaction concept selected by Product Design.

## Approved Evidence And Source Constraints

- Gate outcome and approved first wedge:
- Permitted public, paid/licensed, and internal sources:
- Missing sources or unsupported claims:
- Access, license/permission, cost, provenance, freshness, and coverage constraints:
- Structural shape/entities/fields available:
- Quality, uncertainty, privacy, and trust limits:
- Focused research spike still open, if any:

## User Flow

Describe the user journey the MVP must support.

## Approved Behavioral Contract

Carry forward the approved trigger, preconditions, input/unit of work, state transitions, timing/order, output, controls, completion/failure, and must-not-happen behavior.

## Operating Flow

Describe the end-to-end path from trigger through visible intermediate states, review, final artifact, and reuse.

## Execution-Boundary Map

| Component or surface | Responsibility | Real/mocked/manual/deferred | External dependency | Auth/billing/permission | Data crossing boundary | Fallback |
| --- | --- | --- | --- | --- | --- | --- |

## Screens Or Surfaces

List the expected screens, views, modes, or surfaces.

## Product Artifacts

List the concrete outputs the implemented product must create, show, save, compare, or export.

## Data Model Direction

List the core entities, fields, relationships, persistence needs, and generated outputs.

Keep feasibility research samples separate from stable build fixtures. Do not use licensed, sensitive, or messy sample data in mocks or tests unless permission, privacy treatment, stability, and representativeness are explicit.

## AI, Automation, Or Integration Direction

Describe what should be real, mocked, deterministic, manual, or deferred.

## Trust, Review, And Control

Describe how the user can review, edit, approve, undo, override, or understand uncertainty.

## Safety, Claims, And Privacy

- Sensitive context:
- Allowed claim types:
- Forbidden claim types:
- Safer wording rules:
- Data minimization:
- Deletion/reset requirements:
- Uncertainty language:
- Review required before launch:

## Visual / UX Expectations

Describe the visual quality, interaction behavior, wireframes, diagrams, Product Design Gate concepts, critique decisions, or prototype outputs that should guide implementation.

## Visual Mock Readiness

- Visual artifact required before implementation:
- First screen or primary output:
- Main user inference:
- Main action:
- Visual risks:
- Approval status:

## Acceptance Criteria

- 

Write behavior-first scenarios from the outside in. Start with a user-visible fixture and outcome, then identify service/component contracts and internal unit coverage needed to prove it.

## Required BDD Sequence

For every new or changed observable behavior, implementation must follow this order:

```text
representative full-flow scenario
-> scenario red for the intended missing behavior
-> verify the red failure message and environment
-> mechanistic red / verified-red / green slices
-> scenario green
-> broader regression and operating-layer proof
```

- Scenario red before implementation: Required
- Representative input or fixture:
- Outside-observable outcome:
- Expected missing-behavior failure:
- Red command and evidence location:
- Mechanistic red/green evidence location:
- Final scenario-green command and evidence location:

An already-green test is regression coverage, not intended-red evidence. If the scenario cannot run or is red for the wrong reason, implementation is blocked.

## Risk-Surface Validation Plan

| Risk surface | Likely failure | Proof method | Fixture/scenario | Observable pass | False-positive success to prevent | Owner/stage |
| --- | --- | --- | --- | --- | --- | --- |

Use only applicable surfaces: behavioral semantics, temporal/order, data/source honesty, external boundary, auth/billing/permissions, retries/idempotency, UI interpretation/accessibility, safety/privacy, and deployment/delivery state.

## Behavior And Risk Traceability

| Approved behavior or critical risk | Spec/plan location | Task | Verification task or check |
| --- | --- | --- | --- |

## Testable Decisions Appendix

### Primary Fixture

- Input:
- Sample data:
- Provenance: Real / mocked / synthetic / anonymized
- Version and stable location:
- Permission and privacy treatment:
- Difference from the Opportunity & Evidence research sample:
- Expected output:
- Required explanation:
- Required caution or edge behavior:

### Edge States

- 

### Privacy/Data Tests

- 

## Validation Expectations

- Run the product locally when there is a UI.
- Provide a localhost link before asking the user to verify UI behavior.
- Test functionality behind interactive UI elements.
- Verify key flows before committing final implementation changes.

## User Verification Path

Describe the exact local path or sequence the user should try to verify the MVP.

1. 
2. 
3. 

## Spec Kit Handoff

After this build brief is approved, run the Repo & Continuity Gate, then ask whether to create or confirm the GitHub repo and start the Spec Kit handoff.

If yes, follow `references/spec-kit-start-protocol.md`.

## Spec Kit Input Summary

Use these as source material for Spec Kit specification generation:

- Product truth: `project-brief.md`
- Product Design Gate and prototype decisions: `prototype-pass.md`
- Implementation handoff: `build-brief.md`

Spec Kit must not change approved product scope without user approval.
