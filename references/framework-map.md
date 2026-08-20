# Project Starter Kit: Framework Map

Use this map to organize product discovery. The user should not need to see this whole structure during normal conversation.

Follow the stages in order. Do not use later strategy, design, requirements, or build questions to skip the Opportunity & Evidence Gate.

## 1. Opportunity Hypothesis

Treat the user's one-sentence idea and first product noun as hypotheses.

Capture:

- opening idea in the user's words
- intended user, trigger, and outcome, if known
- proposed mechanism or product noun
- assumptions about value, data, access, workflow, trust, and behavior change
- consequence if each material assumption is wrong
- irreversible user-value judgments that require an explicit user decision

## 2. Evidence And Source Map

Capture public, paid/licensed, internal, and missing sources.

For each material source, capture:

- access and technical availability
- license, permission, and acceptable use
- cost
- provenance and retrieval date
- freshness and coverage
- structural shape: entities, fields, relationships, identifiers, granularity, and formats
- quality, missingness, bias, and uncertainty
- privacy and trust limits
- what the evidence supports and does not support

When useful and permitted, profile a small traceable research sample. Do not acquire large or paid datasets prematurely.

## 3. Evidence-Grounded Options And Gate Decision

Capture:

- comparable operating-model patterns that changed or confirmed a direction
- 2-3 credible operating-model options grounded in the evidence
- benefits, constraints, assumptions, and first wedge for each option
- lead-agent recommendation and strongest alternative
- user decision needed
- outcome: proceed; targeted research spike; narrow/reframe; stop/defer
- Decision Ledger entry and affected starter-artifact sections
- distinction between the feasibility research sample and any later stable, preferably anonymized build fixture

## 4. Product Meaning

Clarify what the product is really about.

Capture:

- working name or confirmed name
- descriptive category
- product thesis
- product promise
- why this should exist
- whether the name is intentional or only a placeholder

## 5. User And Situation

Identify who needs the product and the concrete moment when they need it.

Capture:

- primary user
- trigger situation
- setting or context
- stakes
- constraints
- current workaround
- why the current workaround is insufficient

If no real situation exists yet, construct one common case, one messy case, and one high-stakes case.

## 6. Current State

Describe what is true before the product helps.

Capture:

- user confusion, friction, risk, cost, effort, uncertainty, or unmet desire
- what the user has already tried
- what breaks down today
- what the user cannot see, decide, express, organize, create, or trust yet

## 7. Desired State

Describe what should be true after the product works.

Capture:

- user outcome
- decision or action enabled
- emotional, practical, creative, financial, operational, or learning change
- what "this helped" means in concrete terms

## 8. Core Method

Clarify how the product moves the user from current state to desired state.

Capture:

- process
- questions
- workflow
- analysis
- generation
- recommendation
- comparison
- coaching
- automation
- collaboration
- review or approval behavior

## 9. Core Loop

Define the repeated interaction pattern that makes the product useful.

Capture:

- what the user provides
- what the product returns
- what the user reviews, edits, chooses, or repeats
- what gets saved or improved over time

## 10. Product Artifacts

Name the concrete outputs the product creates.

Examples:

- report
- dashboard
- plan
- recommendation
- script
- checklist
- visualization
- design concept
- comparison
- map
- timeline
- workspace
- saved library
- final handoff

Prefer named artifacts over vague feature labels.

## 11. Product Operating Model

Consume the operating-model direction selected by the Opportunity & Evidence Gate and identify how Product Design should make it understandable and actionable.

Capture:

- initial noun or requested artifact, such as dashboard, app, assistant, report, monitor, or tracker
- evidence-grounded alternatives considered and why the selected direction won
- primary object of attention: user, event, anomaly, task, entity, trend, evidence, document, asset, or workflow
- primary user inference or decision
- signal-to-evidence path
- what would make the interface misleading
- vocabulary borrowed or rejected from the earlier comparable operating-model scan

## 12. Experience Flow

Describe the main user journey.

Capture:

- first screen or first moment
- main modes
- key steps
- user decisions
- review moments
- completion moment
- return or reuse behavior

## 13. UI Direction

Clarify what kind of interface best serves the product.

Capture:

- app, web, mobile, desktop, document, chat, canvas, map, board, dashboard, camera, timeline, or hybrid
- visual density
- interaction style
- whether the product should feel guided, exploratory, operational, creative, analytical, or calm
- where visual representations, wireframes, diagrams, or prototypes are needed before implementation

## 14. Intelligence And Data

Define what the product needs to know, infer, remember, calculate, detect, generate, or explain.

Capture:

- key entities
- user inputs
- saved data
- generated data
- AI behavior
- external integrations
- uncertainty and confidence
- fallbacks when automation is weak
- privacy or sensitivity concerns
- approved source constraints and evidence limits from the Opportunity & Evidence Gate
- whether runtime data is real, mocked, manual, or deferred

## 15. Trust And Control

Identify where the user needs agency.

Capture:

- review points
- edit points
- approvals
- undo
- overrides
- confidence signals
- source or evidence visibility
- safety, legal, financial, medical, privacy, or emotional risk boundaries

## 16. MVP Boundary

Separate the smallest useful version from the full vision.

Capture:

- MVP user
- MVP input
- MVP output
- must-have loop
- explicit exclusions
- simulated or manual fallbacks
- future capabilities to preserve without building now

## 17. Feasibility Challenge

Stress-test the product before implementation.

Capture:

- riskiest assumptions
- platform or permission constraints
- AI/data/API constraints
- visual or workflow unknowns
- what can be tested with a sketch, mockup, stable fixture, manual run, API check, or tiny prototype
- what decision would change if the assumption fails
- which focused evidence gap, if any, the design or prototype exposed after the Opportunity & Evidence Gate

## 18. Behavioral Contract

Define the observable behavior after choosing an operating model and before approving the proof.

Capture:

- trigger and preconditions
- input and unit of work
- state transitions and timing/order
- output and user controls
- completion and failure/fallback behavior
- behavior that must not happen
- current-system impact preview when changing an existing system

## 19. Example Prototype Pass

Run one concrete example through the proposed product loop before formalizing the starter artifacts.

This is required unless the user explicitly chooses to skip it.

The example should be specific enough to expose real friction:

- a real image for a visual product
- a sample file or table for an analytics product
- a realistic user scenario for a workflow product
- a messy source input for a writing or generation product
- a manual AI response simulation for an AI-first product
- a wireframe or clickable flow for an interaction-heavy product

Capture:

- example input or scenario
- what the user does first
- what the product should produce
- what the user reviews, edits, chooses, or rejects
- what felt confusing, too verbose, too manual, too fragile, or not useful enough
- which assumptions were confirmed
- which assumptions broke
- which MVP decisions changed
- whether a visual artifact, wireframe, sample output, or prototype should be included in the handoff
- whether the walkthrough used permitted real data or an explicitly mocked, synthetic, or anonymized build fixture
- how that stable build fixture differs from any earlier feasibility research sample

## 20. Project Scale And Continuity

Classify how durable the project is and what continuity setup is required.

Capture:

- project scale: scratch, local prototype, private project, collaborative project, or production path
- whether work may remain local or must be pushed to GitHub
- repository name and visibility preference
- current branch, commit count, latest commit, remote URL, and push status
- large data or generated artifacts that should be intentionally included or excluded
- whether GitHub setup was approved, completed, or explicitly deferred
- milestone push expectations

## 21. Build Handoff

Capture what a future build agent needs so it can implement without guessing.

Capture:

- product truth
- MVP scope
- user flows
- artifacts
- data model direction
- AI boundaries
- UX expectations
- validation criteria
- commit and documentation expectations
- approval gates before implementation

## 22. Operating Flow

Map the end-to-end product path:

- start trigger
- intake and validation
- processing stages
- visible intermediate states
- review or approval
- final artifact
- save, reuse, or return loop

## 23. Execution-Boundary Map

For each component or surface, capture:

- responsibility
- real, mocked, manual, or deferred behavior
- external dependencies
- credentials, billing, permissions, or platform constraints
- data crossing the boundary
- fallback behavior

## 24. Risk-Surface Validation

Capture only applicable risk surfaces, their likely failures, proof methods, fixtures, observable pass conditions, and false-positive success states.
