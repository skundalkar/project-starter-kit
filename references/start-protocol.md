# Project Starter Kit: Start Protocol

## Purpose

Project Starter Kit helps a user turn a rough project idea into a clear, build-ready product direction.

When invoked, do not build the product yet. Do not create a repository during initial discovery. Do not generate a formal specification yet. Repository setup is handled by the Repo & Continuity Gate once starter artifacts exist or implementation is about to begin.

First, help the user discover what they are actually trying to build. Treat the user's first product noun as a hypothesis until the operating model is clear.

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

## Framework Source

Use `framework-map.md` as the organizing model for discovery.

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

## Readiness Check

When enough information exists, say:

"I think we have enough to draft the first product brief. Before I do that, here is the current product shape."

Then summarize the readiness checklist from `readiness-check.md`.

Ask for approval before generating formal artifacts.

## Product Design Gate

Before the example prototype pass, or during it as soon as product/design uncertainty appears, use `product-design-gate.md` when the initial product shape may be wrong.

Trigger this gate when:

- the user asks for a dashboard, monitor, tracker, assistant, report, workflow, or app but the decision job is unclear
- metrics, scores, categories, thresholds, labels, or evidence may be hard to interpret
- the product is visual, analytics-heavy, workflow-heavy, AI-output-heavy, trust/safety-sensitive, or interaction-heavy
- the user expresses confusion about what a number, chart, screen, or output is supposed to mean
- outside examples or mature product patterns could change the vocabulary or operating model

During this gate:

- challenge the initial noun with 3-5 alternative operating models
- ask what the user should infer, trust, compare, review, or do next
- run a lightweight market/pattern scan when current public examples could improve the model
- create or request 2-3 competing visual or structural concepts for visual/decision-support products
- map signal -> driver -> evidence -> interpretation
- record the chosen operating model and user critique in `prototype-pass.md`

Do not proceed to final starter artifacts until the Product Design Gate has passed or the user explicitly skips it.

## Required Example Prototype Pass

Before generating final starter artifacts, run an example prototype pass.

The prototype pass must use one concrete input, scenario, file, sample data set, sketch, or workflow that represents the product's first real use.

Do not treat this as implementation. Treat it as a fast reality check before formalizing the product.

Ask the user for or help create the example:

- For a visual product, use a real image, mockup, wireframe, or visual walkthrough.
- For an analytics product, use a sample table, CSV, chart, or question.
- For a writing product, use a messy source note and draft the expected output.
- For a workflow product, walk through one realistic case step by step.
- For an AI product, manually simulate the AI response before assuming automation.

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

Do not proceed to `project-brief.md`, `prototype-pass.md`, or `build-brief.md` until the example prototype pass has either been completed or the user explicitly chooses to skip it.

If product/design uncertainty appears during the pass, run or rerun `product-design-gate.md`; also follow `triggered-tools-protocol.md` when tool or review triggers apply before formalizing the build brief.

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
