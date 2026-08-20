---
name: agent-system-visualization
description: Model and visualize the verified inner workings of an agentic system. Use when Codex needs to explain an agent, multi-agent workflow, AI copilot, automation, decision-support system, or orchestration runtime through architecture, lifecycle/state, artifact provenance, decision/control, event, boundary, or run-walkthrough views grounded in code, docs, traces, tests, and other source artifacts.
---

# Agent System Visualization

Build the model before drawing. Optimize for a human deciding what the system does, why it moves, what it produces, and where evidence stops.

## Non-negotiable rule

Create one canonical source-of-truth model and classify every relationship before rendering any diagram. Never draw narrative, restart context, temporal adjacency, or a plausible association as a formal data-flow, dependency, or causal edge.

Use `assets/canonical-model.template.json` for machine-checkable work. Read `references/model-and-visual-grammar.md` before creating or reviewing a model.

## Workflow

1. Establish scope, audience, decision, system boundary, and evidence cutoff.
2. Inspect authoritative code, contracts, tests, schemas, runtime traces, and current docs. Record conflicts and unknowns; do not silently resolve them.
3. Inventory entities: subsystems, actors, states or visits, triggers, decisions, artifacts, data stores, external systems, human events, system events, and terminal outcomes.
4. Register every relationship with a class, verification status, evidence citation, and plain-language meaning. Treat chronology and causality as separate claims.
5. Mark each statement `observed`, `inferred`, or `unknown`. Formal artifact-flow edges require observed evidence that the target actually consumes the named artifact.
6. Validate the model with `python3 scripts/validate_model.py <model.json>`. For a compact standalone explainer, run `python3 scripts/render_model.py <model.json> <output.html>`.
7. Select only the views that answer the user's questions:
   - architecture/subsystem map for ownership, responsibilities, and boundaries;
   - lifecycle/state view for triggers, state changes, waits, retries, and outcomes;
   - artifact/provenance flow for formal production and consumption;
   - decision/control map for route choices, gates, uncertainty, and operator authority;
   - run walkthrough only when ordered event evidence exists.
8. Draw separate visual layers for state visits, artifact provenance, route decisions, human/system events, and explanatory context. A view may combine layers only when edge classes remain explicit.
9. Lead with “what this shows” and the decision-relevant takeaway. Explain every major diagram in plain language.
10. Verify labels, contrast, narrow-width layout, keyboard interaction, and every edge against the canonical register. Report open uncertainties beside the visual.

## Visual and interaction rules

- Prefer semantic accuracy over polish. Make subsystem or state blocks visually stronger than handoff lines.
- Label edges by relationship class or use a legend with unmistakable line styles. Do not rely on similar colors; pair color with labels, shapes, stroke styles, or icons.
- Show external boundaries explicitly. Distinguish human actions from system events and terminal outcomes from ordinary states.
- Use solid lines for verified formal/control relationships, dashed lines for contextual or inferred relationships, and never let styling upgrade an uncertain claim.
- Keep detail available for each selected entity: responsibility, start/stop reasons, inputs, outputs, decision, evidence, and meaningful handoff. Display “none evidenced” or “unknown” instead of inventing content.
- Keep diagrams compact. Prefer multiple focused views over one universal graph.

## Output contract

Deliver:

- a canonical model (JSON, YAML, or equivalently structured tables) with evidence citations and uncertainties;
- the smallest useful visual artifact containing an architecture view plus at least one lifecycle/state, provenance, or decision/control view;
- a short decision-first explanation of each view and its limits;
- validation evidence, including unresolved model warnings.

For an implementation-grounded artifact, cite repository-relative paths and symbols or line ranges when stable. Do not claim runtime behavior from a proposal document alone. Do not imply a single execution order from unordered architecture evidence.
