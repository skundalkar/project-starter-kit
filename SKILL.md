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
4. Run the required example prototype pass unless the user explicitly skips it.
5. If triggered project-tool conditions appear, follow `references/triggered-tools-protocol.md`.
6. Generate the three starter artifacts using:
   - `templates/project-brief.md`
   - `templates/prototype-pass.md`
   - `templates/build-brief.md`
7. After starter artifacts exist, ask whether to create the Git repo and start the Spec Kit handoff.
8. If yes, follow `references/spec-kit-start-protocol.md`.

## Invocation Behavior

For "Use Project Starter Kit. Start." or similar:

- Begin with one simple question: "What are you trying to build? You can answer messily."
- Do not ask for repo details, implementation choices, or Spec Kit setup yet.
- Interview lightly, one or two questions at a time.
- Track what is known and missing using the framework map.
- Give short running summaries.
- Always clearly state the next question, next requirement, or what is waiting on the user.
- Treat visual, workflow, AI-output, or feasibility uncertainty as a trigger for a
  prototype pass or tool/lens review; do not wait for the user to explicitly request it.

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
