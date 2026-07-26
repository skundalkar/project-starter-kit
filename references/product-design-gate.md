# Project Starter Kit: Product Design Gate

## Purpose

Use this gate when the product form, interface, or operating model could be wrong even if the user's first noun sounds clear.

The gate is not a documentation step. It is an adversarial clarification step before implementation framing hardens.

## Core Behavior

Treat the user's first product noun as a hypothesis, not a requirement.

If the user asks for a dashboard, app, assistant, tracker, report, monitor, workflow, or tool, challenge what job that surface is meant to do.

Do not ask, "Do you want a dashboard?" Ask what decision, inference, comparison, review, or action the product should make easier.

## Required Reframing

Generate 3-5 possible operating models when the product shape is ambiguous.

Examples:

- dashboard
- monitor
- anomaly detector
- triage queue
- investigation console
- command center
- alerting surface
- report
- decision-support surface
- workflow tool
- search or exploration interface
- evidence review tool

For each plausible model, identify:

- primary object of attention
- primary user inference
- first signal that makes the user care
- evidence needed to trust the signal
- what the user does next, if anything
- what would make the interface misleading

## Cross-Questioning

Ask one or two sharp questions at a time. Prefer questions that challenge the frame.

Useful questions:

- "What should the user infer from this screen in 10 seconds?"
- "What would the user do differently after seeing it?"
- "What would make this screen useless or misleading?"
- "Is the main object a user, event, anomaly, task, entity, trend, or piece of evidence?"
- "Is this for monitoring, diagnosis, comparison, prioritization, review, or action?"
- "If the main number is high, what should explain why?"
- "What evidence would make the user trust the signal?"
- "What time context matters: item age, user/account age, incident duration, trend duration, or current-window activity?"
- "Which labels or scores are unclear without definitions?"
- "What can be removed because the visual already communicates it?"

## Market And Pattern Scan

When the product form is ambiguous, high-stakes, or common-sounding, perform a lightweight market/pattern scan before settling the model.

Use current public sources when product patterns, platform constraints, or competitor behavior may have changed. Prefer official product pages, public docs, credible case studies, and mature comparable tools.

Look for:

- vocabulary used by mature products
- workflow patterns
- alerting, triage, monitoring, or investigation models
- metric semantics and threshold language
- evidence and drilldown patterns
- escalation or review patterns
- what users are expected to infer

Then report what changed in the product framing. Do not copy competitor features blindly.

## Visual Concept Requirement

For visual, dashboard, analytics, monitoring, workflow, AI-output, or interaction-heavy products, create or request 2-3 competing visual or structural concepts before approving the product direction unless the user explicitly skips this gate.

Each concept should test a different operating model or information hierarchy, not merely a different color treatment.

For each concept, ask:

- what is immediately clear
- what is confusing
- what metric lacks meaning
- what drilldown or evidence is missing
- what entity hierarchy is hidden
- what time context is missing
- what should be removed

## Signal-To-Evidence Map

Before the gate passes, define the path from signal to evidence:

```text
signal
-> primary driver
-> supporting evidence
-> user interpretation
-> optional next action
```

For analytics and monitoring products, also define:

- baseline or comparison source
- current-window signal
- historical/context signal
- driver attribution
- evidence examples
- confidence or uncertainty language

## Output

Record Product Design Gate decisions inside `prototype-pass.md` and carry the chosen model into `project-brief.md` and `build-brief.md`.

Do not create a separate artifact by default unless the gate was substantial enough that a standalone design decision report would prevent confusion.

Required recorded decisions:

1. challenged initial noun
2. alternative operating models considered
3. chosen operating model
4. primary user inference
5. main object of attention
6. signal-to-evidence path
7. entity hierarchy
8. time-context requirements
9. metric or label definitions
10. misinterpretation risks
11. visual concepts tested
12. user critique and resulting changes

## Pass Criteria

Pass the gate only when:

- the primary user inference is clear
- the main object of attention is clear
- the signal-to-evidence path is clear
- important time/context assumptions are clear
- confusing metrics or labels have been renamed, defined, or removed
- the user has reacted to competing concepts when the product is visual or interaction-heavy
- the chosen operating model is reflected in the starter artifacts

If these are not true, continue product design discovery or rerun the prototype pass before Spec Kit handoff.
