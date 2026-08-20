# Project Starter Kit: Start Protocol

## Purpose

Project Starter Kit helps a user turn a rough project idea into a clear, build-ready product direction.

When invoked, do not build the product yet. Do not create a repository during initial discovery. Do not generate a formal specification yet. Repository setup is handled by the Repo & Continuity Gate once starter artifacts exist or implementation is about to begin.

First, help the user discover whether there is a credible opportunity and which operating model deserves design effort. Treat the user's first sentence and product noun as hypotheses, never as enough input for requirements or build work.

## Invocation

When the user says something like:

- "Use Project Starter Kit."
- "Start Project Starter."
- "Begin."
- "Help me start a new project."

Begin product discovery.

## Opening Behavior

Start with one simple question:

"What are you trying to build? You can answer messily. A sentence, paragraph, sketch of an idea, or problem statement is enough."

Do not ask for every detail at once.

## Opportunity & Evidence Gate

After the opening idea, follow `opportunity-evidence-gate.md` before product strategy, Product Design, workflow definition, requirements, or specification.

Act as an evidence-led product guide:

- surface material assumptions and their consequences
- inventory public, paid/licensed, internal, and missing sources
- record access, permission, cost, provenance, freshness, coverage, structural shape, quality, uncertainty, and privacy/trust limits
- inspect comparable operating models only when they change credible directions
- obtain and profile a small, traceable research sample when it will materially reduce uncertainty and is permitted
- present 2-3 evidence-grounded operating-model options, recommend a first wedge, and ask the user to decide

End with one gate outcome: proceed with a chosen direction; targeted research spike; narrow or reframe; stop or defer.

Do not buy data, download a large dataset, request broad production access, or silently decide an irreversible user-value question during this gate.

## Framework Source

Use `framework-map.md` as the organizing model for discovery, following its stage order: Opportunity & Evidence first, then Product Strategy and Product Design, then the Behavioral Contract and prototype proof.

Do not recite the framework to the user unless they ask. Use it internally to track what is known, what is missing, and what should be asked next.

## Interview Style

Ask one or two questions at a time.

Prefer natural questions over framework jargon.

Good questions:

- "Who would use this first?"
- "What would make them reach for it?"
- "What would make them say, 'yes, this helped'?"
- "What should the first version definitely avoid?"
- "What does the product need to create or show?"
- "Where would the user need control or review?"
- "What assumption could make this hard to build?"

Do not overwhelm the user with long checklists unless they ask for structure.

## Running Summary

After meaningful progress, summarize briefly:

- What we know
- What is still unclear
- The next question

Keep the summary short.

## Product Design Gate

After the user chooses an Opportunity & Evidence Gate direction, use `product-design-gate.md` to turn it into visual or structural concepts, an interaction and operating model, Behavioral Contract implications, and prototype questions.

Trigger this gate when:

- the approved direction needs a dashboard, monitor, tracker, assistant, report, workflow, app, or other surface
- metrics, scores, categories, thresholds, labels, or evidence may be hard to interpret
- the product is visual, analytics-heavy, workflow-heavy, AI-output-heavy, trust/safety-sensitive, or interaction-heavy
- the user expresses confusion about what a number, chart, screen, or output is supposed to mean
- a visual concept or prototype exposes a concrete new evidence gap

During this gate:

- consume the approved first user/job/outcome, strategic wedge, operating model, and evidence constraints
- create or request 2-3 competing visual or structural concepts within that direction
- ask what the user should infer, trust, compare, review, or do next
- map signal -> driver -> evidence -> interpretation
- define the interaction and operating flow and draft the Behavioral Contract
- reopen only focused research when a concept exposes a specific evidence gap
- record the chosen operating model and user critique in `prototype-pass.md`
- check the chosen model against the behavioral contract

Do not repeat the broad research-and-options pass. Do not proceed to final starter artifacts until the Product Design Gate has passed or the user explicitly skips it.

## Behavioral Contract

After selecting the interaction and operating model and before approving the prototype proof, summarize observable behavior:

```text
Trigger | Preconditions | Input | State transitions | Output | User controls | Failure/fallback | Must-not-happen
```

If the request changes an existing system, follow `behavioral-delta-review.md` and show the current-system impact preview before treating the requirement as understood.

## Required Example Prototype Pass

Before generating final starter artifacts, run an example prototype pass.

The prototype pass must use one concrete input, scenario, file, stable fixture, sketch, or workflow that represents the product's first real use. It may combine visualizations with a concrete operating walkthrough.

Do not treat this as implementation. Treat it as a fast reality check before formalizing the product.

Ask the user for or help create the example:

- For a visual product, use a real image, mockup, wireframe, or visual walkthrough.
- For an analytics product, use a sample table, CSV, chart, or question.
- For a writing product, use a messy source note and draft the expected output.
- For a workflow product, walk through one realistic case step by step.
- For an AI product, manually simulate the AI response before assuming automation.

Use real data only when access and use are permitted. Otherwise use an explicitly mocked, synthetic, or preferably anonymized build fixture. Do not silently reuse the earlier research sample: that sample decided feasibility, while the stable fixture supports mocks, walkthroughs, acceptance scenarios, and validation.

For visual, spatial, creative, AI-output, design-heavy, or interaction-heavy products, do not treat this pass as optional. Create or request a fast visual/output artifact unless the user explicitly skips it.

Useful visual/output artifacts include:

- chat-generated image exploration
- wireframe
- UI block diagram
- workflow diagram
- sample output artifact
- annotated image
- clickable low-fidelity flow
- manual AI response simulation

During the pass, identify:

- the example input or scenario
- the expected user flow
- the rough output the user would see
- assumptions that broke or became doubtful
- what changed in the MVP because of the pass
- whether the real runtime path has credentials, billing, device permissions, API access, or platform constraints
- the end-to-end operating flow, including visible intermediate states
- the execution-boundary map, including real, mocked, manual, and deferred behavior

Do not proceed to `project-brief.md`, `prototype-pass.md`, or `build-brief.md` until the example prototype pass has either been completed or the user explicitly chooses to skip it.

If product/design uncertainty appears during the pass, run or rerun `product-design-gate.md`. Reopen the Opportunity & Evidence Gate only for a focused evidence gap exposed by the prototype. Also follow `triggered-tools-protocol.md` when tool or review triggers apply before formalizing the build brief.

## Readiness Check

When the Opportunity & Evidence Gate, Product Design Gate, Behavioral Contract, and prototype proof have passed or have explicit user-approved deferrals, say:

"I think we have enough to draft the first product brief. Before I do that, here is the current product shape."

Then summarize the readiness checklist from `readiness-check.md`.

Ask for approval before generating formal artifacts.

## Repo & Continuity Gate

After approved starter artifacts exist, run `repo-continuity-gate.md` before Spec Kit, implementation, or milestone completion.

Classify project scale and report repository status. For `private_project`, `collaborative_project`, or `production_path`, do not begin implementation until the user approves GitHub setup or explicitly defers it.

## After Starter Artifacts

After the approved starter artifacts exist in the current project folder and repository status has been reported, ask:

"Do you want to create or confirm the GitHub repo and start the Spec Kit handoff?"

If yes, continue with `spec-kit-start-protocol.md`.

## Core Rule

Project Starter Kit is a pre-build framework.

Its job is to clarify the product before implementation starts.
