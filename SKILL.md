---
name: project-starter-kit
description: Start and structure a new product/project idea before implementation. Use when the user wants to begin a new project, shape a rough idea, create a product brief, run a feasibility/prototype challenge, generate a build-ready brief, or hand the result to Spec Kit for specification, planning, tasks, and implementation.
---

# Project Starter Kit

Project Starter Kit is a pre-build skill. It helps the user turn a rough idea into clear starter artifacts before any repository, Spec Kit specification, plan, tasks, or implementation work begins.

## Core Workflow

1. If the user says to start a new project, follow `references/start-protocol.md`.
2. Use `references/framework-map.md` to organize discovery internally.
3. Use `references/readiness-check.md` before producing formal artifacts.
4. Run `references/product-design-gate.md` before or during the prototype pass when the product form, UI, operating model, metrics, evidence, or user inference is ambiguous.
5. Run `references/product-artifact-review-gate.md` after meaningful product artifacts, visual mocks, dashboards, reports, charts, generated documents, or UI prototypes create user questions, metric confusion, source-coverage concerns, or product-form uncertainty.
6. Use `references/async-orchestration-gate.md` before major implementation, review, data, or documentation work to split critical-path work from safe parallel sidecar work.
7. Run the required example prototype pass unless the user explicitly skips it.
8. If triggered project-tool conditions appear, follow `references/triggered-tools-protocol.md`.
9. Generate the three starter artifacts using:
   - `templates/project-brief.md`
   - `templates/prototype-pass.md`
   - `templates/build-brief.md`
10. Run `references/validation-gate.md` when the user wants to continue toward implementation or the product has customer, safety, trust, onboarding, behavior-change, or retention risk.
11. Run `references/business-acquisition-gate.md` for consumer products, paid products, community-led products, marketplaces, healthcare/wellness products, education products, productivity products, or products that need distribution.
12. Run `references/build-readiness-gate.md` before Spec Kit handoff or implementation.
13. Run `references/repo-continuity-gate.md` after starter artifacts exist and before Spec Kit, implementation, or a major milestone.
14. After build readiness and repository status are explicit, ask whether to initialize/confirm local Git, create/confirm a private GitHub repo, and start the Spec Kit handoff.
15. If yes, follow `references/spec-kit-start-protocol.md`, including the Repo & Continuity Gate and the Intermediate Specialist Review Quality Gate when triggered after plan approval and before task generation.
16. Implementation happens through Spec Kit or the appropriate build workflow, not directly inside Project Starter Kit, unless the user explicitly asks for a local prototype and repo readiness has passed or been explicitly deferred.

## Invocation Behavior

For "Use Project Starter Kit. Start." or similar:

- Begin with one simple question: "What are you trying to build? You can answer messily."
- Do not ask for repo details, implementation choices, or Spec Kit setup yet.
- Interview lightly, one or two questions at a time.
- Track what is known and missing using the framework map.
- Give short running summaries.
- Always clearly state the next question, next requirement, or what is waiting on the user.
- Treat visual, workflow, AI-output, operating-model, metric-semantics, evidence, or feasibility uncertainty as a trigger for the Product Design Gate, prototype pass, or tool/lens review; do not wait for the user to explicitly request it.
- Do not accept the user's first artifact noun, such as dashboard, app, tracker, assistant, monitor, or report, as the final product model without testing what job it must do.
- After the user sees an artifact and starts asking what numbers mean, what to infer, what action to take, whether source data is complete, or why the output feels wrong, run the Product Artifact Review Gate before continuing implementation.
- When multiple independent questions appear, use the Async Orchestration Gate to decide whether specialist review, data generation, documentation capture, or verification should run in parallel.
- Treat project scale as a first-class decision. If the project is more than scratch exploration, run the Repo & Continuity Gate before implementation and make local-vs-GitHub status explicit.
- If the user asks to continue into a real build, do not stop at "not build ready." Run the Validation Gate, Business & Acquisition Gate when triggered, Build Readiness Gate, and Repo & Continuity Gate, then state the exact next action that moves the project toward Spec Kit or implementation.

For "Use Project Starter Kit. Start Spec Kit handoff." or similar:

- Confirm `project-brief.md`, `prototype-pass.md`, and `build-brief.md` exist in the current project folder.
- If they do not exist, return to starter artifact generation.
- If they exist, follow the Spec Kit start protocol.

## Output Rule

Generate only the three core starter artifacts by default:

- `project-brief.md`
- `prototype-pass.md`
- `build-brief.md`

Do not create a separate `start-here.md`, `given-prompt.md`, or `AGENTS.md` by default.

## Repo & Continuity Gate Rule

Use `references/repo-continuity-gate.md` after starter artifacts exist, before Spec Kit handoff, before implementation, and before milestone completion.

Classify project scale as `scratch`, `local_prototype`, `private_project`, `collaborative_project`, or `production_path`.

For `private_project`, `collaborative_project`, or `production_path`, do not begin implementation until the repository status has been reported and the user has either approved GitHub setup or explicitly deferred it.

Default to a private GitHub repository when creating a remote, unless the user asks for public.

Every milestone final response should include repository status when the gate has been triggered:

- project scale
- local Git repo
- branch
- commit count
- latest commit
- GitHub remote
- pushed status
- repo URL

## Build Continuation Track

Use the Build Continuation Track after starter artifacts exist when the user asks to build, implement, create a repo, push to GitHub, start Spec Kit, or continue toward a real product.

Run the track in this order:

1. `references/validation-gate.md`
2. `references/business-acquisition-gate.md`, when triggered
3. `references/build-readiness-gate.md`
4. `references/repo-continuity-gate.md`
5. Spec Kit handoff or implementation workflow after required approvals

Do not treat "not build ready" as a terminal answer. Report the readiness status, blockers, deferred issues, and the exact next action. Local Git may be initialized when the user asks to proceed into build and the workspace is not already a repo. Creating a GitHub remote creates external state and requires explicit user approval; default to private unless the user asks for public.

## Product Design Gate Rule

When the user asks for a dashboard, monitor, analytics surface, workflow, AI assistant, report, or other common product noun, treat that noun as a hypothesis.

Use `references/product-design-gate.md` when the real operating model could be one of several alternatives, such as anomaly detector, triage queue, investigation console, command center, evidence review tool, report, or workflow tool.

For ambiguous visual or decision-support products, compare 2-3 competing product framings or UI concepts before formalizing the build brief unless the user explicitly skips this gate.

Record Product Design Gate decisions in `prototype-pass.md` and carry the chosen operating model into `project-brief.md` and `build-brief.md`.

## Visual Prototype Rule

For visual, spatial, workflow-heavy, AI-output-heavy, or interaction-heavy products, do not rely only on long markdown for approval.

Before finalizing starter artifacts, produce or request a visual artifact. This is required unless the user explicitly skips it:

- wireframe
- block diagram
- workflow diagram
- sample output
- annotated image
- quick mockup
- manual prototype walkthrough

Use the visual artifact to challenge assumptions before formalizing the build brief. For visual products, sample output can expose product truth faster than implementation.

## Product Artifact Review Gate Rule

Use `references/product-artifact-review-gate.md` after a meaningful artifact exists and the user's reaction reveals confusion, new questions, metric ambiguity, data/source uncertainty, action uncertainty, or product-form drift.

This gate reviews the artifact as evidence, not as a finished deliverable. It should identify what became clearer, what became more confusing, which assumptions were exposed, and what must update spec/tasks/docs before more coding.

Do not duplicate the Product Design Gate. Product Design Gate challenges the product form before or during prototyping; Product Artifact Review Gate interrogates a concrete artifact after the user has seen it.

## Async Orchestration Gate Rule

Use `references/async-orchestration-gate.md` when a project step contains independent review, data, documentation, verification, or implementation work that can safely run in parallel.

Project Starter Kit remains the orchestrator. Specialized review agents are sidecars, not new sources of truth. The main agent must define each sidecar's role, scope, allowed files, output, and integration point.

## Status Rule

Every substantive response should make the current state clear:

- what was just done
- what decision changed, if any
- what comes next
- what is waiting on the user, if anything

Avoid leaving the user guessing whether the process is paused, waiting for approval, or continuing.

If triggered project tools or frameworks were used during the step, include an explicit tool summary in the same status or final response.

For tool definitions and usage guidance, follow `references/triggered-tools-protocol.md`.

For each tool or framework used, report:

- name of the tool or framework
- specific feature, mode, practice, or review used
- why it was used
- artifact, file, or output produced
- decision changed, if any
- commit or file result, if applicable

If a trigger condition appeared and no tool or review lens was used, say why it was skipped.
