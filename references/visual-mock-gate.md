# Project Starter Kit: Visual Mock Gate

## Purpose

Use this gate before implementation when the product's first user experience cannot be judged from text, requirements, or a low-fidelity walkthrough alone.

The gate does not require final design polish. It requires enough visual structure to expose scan path, density, hierarchy, trust, and action clarity before code starts.

## Trigger Conditions

- UI-heavy, visual, spatial, workflow-heavy, decision-support, AI-output, or consumer-facing product.
- A text wireframe exists but card density, layout, labels, controls, or navigation remain uncertain.
- The user will need to inspect, compare, approve, edit, or trust visual output.
- Visual artifact review found confusion, clutter, misleading labels, or unclear next action.
- Implementation is about to start and the first screen is not visually understood.

## Acceptable Artifacts

- annotated wireframe
- higher-fidelity static mock
- clickable low-fidelity flow
- representative output card or report
- visual state diagram
- generated bitmap mockup
- screenshot-style HTML prototype

## Required Review

Record in `prototype-pass.md` or `build-brief.md`:

```text
Visual artifact:
First screen:
Primary user inference:
Primary action:
Secondary actions:
Information hierarchy:
What is immediately clear:
What is confusing or crowded:
What should be removed:
What must be visible before implementation:
Visual approval status:
```

## Pass Criteria

The gate passes when:

- the first screen or primary output is visible as a concrete artifact
- the main user inference is clear within 10 seconds
- primary and secondary actions are distinguishable
- text and controls are not overloaded
- trust/evidence/uncertainty cues are visible when needed
- unresolved visual risks are recorded in the build brief

If the gate does not pass, continue design or prototype before implementation.
