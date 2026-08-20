# Project Starter Kit: Product Design Gate

## Contents

- Purpose and approved inputs
- Core behavior
- Visual and structural concepts
- Interaction and operating model
- Signal-to-evidence map
- Focused evidence reopen rule
- Prototype proof, output, and pass criteria

## Purpose

Run this gate after the Opportunity & Evidence Gate has produced an approved direction or an explicitly accepted uncertainty.

Turn the chosen operating model into visual or structural concepts, an interaction and operating flow, behavioral-contract implications, and a concrete prototype pass. Challenge how the direction works without repeating the earlier opportunity research.

## Approved Inputs

Begin by restating:

- selected user, job, outcome, and first wedge
- chosen operating model and rejected alternatives
- evidence supporting the direction
- source, access, trust, and privacy constraints
- research-sample limitations
- focused evidence gaps accepted or deferred

If these inputs do not exist, return to `opportunity-evidence-gate.md`. Do not invent product strategy to fill the gap.

## Core Behavior

Treat the approved operating model as a direction to test, not a finished interface.

Ask what decision, inference, comparison, review, or action each surface should make easier. Preserve the approved wedge unless user critique or focused new evidence justifies a Decision Ledger update.

Do not ask only, "Do you want a dashboard?" Ask what the user should understand or do, what evidence they need, and what would make the concept misleading.

## Visual And Structural Concepts

For visual, dashboard, analytics, monitoring, workflow, AI-output, or interaction-heavy products, create or request 2-3 competing concepts unless the user explicitly skips the gate.

Each concept must test a different interaction model, information hierarchy, or division of human and system responsibility within the approved direction. Do not vary only color or styling.

For each concept, identify:

- primary object of attention
- primary user inference or decision
- first signal that creates relevance
- evidence needed to trust the signal
- main action and next state
- review, edit, approval, undo, or override controls
- what would make the concept misleading
- what is immediately clear, confusing, crowded, missing, or removable
- behavioral-contract implications

Useful challenge questions:

- "What should the user infer from this in 10 seconds?"
- "What would the user do differently after seeing it?"
- "What evidence would make the signal trustworthy?"
- "What is the main object: user, event, anomaly, task, entity, trend, or evidence?"
- "What time context matters?"
- "Which score, label, threshold, or state is unclear without a definition?"
- "Where must the user be able to inspect, correct, or stop the system?"

## Interaction And Operating Model

For the leading concept, define:

- entry trigger and preconditions
- first screen, artifact, or moment
- main entities and hierarchy
- key steps and visible intermediate states
- user and system responsibilities
- review or approval points
- completion state
- failure, fallback, and return/reuse paths
- real, mocked, manual, and deferred boundaries

Use this to draft the Behavioral Contract before approving the prototype proof.

## Signal-To-Evidence Map

For analytics, monitoring, AI, workflow, or decision-support products, define:

```text
signal
-> primary driver
-> supporting evidence
-> user interpretation
-> optional next action
```

Also define when applicable:

- baseline or comparison source
- current-window signal
- historical or contextual signal
- driver attribution
- evidence examples
- confidence or uncertainty language

## Focused Evidence Reopen Rule

Review the approved Opportunity & Evidence Gate record; do not rerun its broad source inventory or comparable-product scan.

Reopen research only when a visual concept or prototype exposes a concrete evidence gap, such as an unavailable field, unreliable label, missing workflow permission, unsupported user inference, or unclear trust boundary.

For a focused spike, record:

- design decision blocked
- precise evidence needed
- smallest permitted source or sample
- access, cost, privacy, and stop limits
- what result would change the concept

Update the existing Opportunity & Evidence section and Decision Ledger with the result. Do not create a second research report.

## Prototype Proof

Use the smallest useful proof that can test the concept and Behavioral Contract. It may combine visualizations with one concrete operating walkthrough.

Connect the proof to:

- real data that is permitted and proportionate, or
- an explicitly mocked, synthetic, or anonymized build fixture

Do not silently reuse a messy or license-limited research sample as the build fixture. Label every data boundary and state what the proof supports and does not support.

## Output

Record Product Design Gate decisions inside `prototype-pass.md` and carry the approved operating model into `project-brief.md` and `build-brief.md`.

Required recorded decisions:

1. approved opportunity direction and evidence constraints consumed
2. visual or structural concepts considered
3. chosen concept and interaction/operating model
4. primary user inference and main object of attention
5. signal-to-evidence path
6. entity hierarchy and time context
7. metric or label definitions
8. misinterpretation risks and user controls
9. user critique and resulting changes
10. behavioral-contract implications
11. concrete walkthrough and data/fixture boundary
12. focused research reopened, if any, and the decision it resolved

## Pass Criteria

Pass only when:

- the selected concept preserves or explicitly updates the approved first user/job/outcome and wedge
- the primary user inference and main object of attention are clear
- the interaction and operating flow are clear
- the signal-to-evidence path is clear when applicable
- important time, context, metric, label, and user-control assumptions are clear
- the user has reacted to competing concepts when the product is visual or interaction-heavy
- the Behavioral Contract covers trigger, preconditions, input, state, output, controls, fallback, and must-not-happen behavior
- a concrete walkthrough uses real or explicitly mocked/fixture data
- any reopened research was focused on a newly exposed evidence gap
- the chosen concept is reflected in the starter artifacts

If these are not true, continue product design discovery or rerun the prototype pass before Spec Kit handoff.
