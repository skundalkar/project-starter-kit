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
2. Inspect authoritative code, contracts, tests, schemas, runtime traces, and current docs. Record conflicts and unknowns; do not silently resolve them. When the project exposes typed models or schemas, run `python3 scripts/discover_schema_candidates.py <project-root> <candidates.json>` and audit its candidate inventory against the source.
3. Inventory entities: subsystems, actors, states or visits, triggers, decisions, artifacts, data stores, external systems, human events, system events, and terminal outcomes. Promote useful schema candidates into `declarations`, then link canonical records with `declaration_ids`; preserve the exact source name separately from the human-facing label.
4. Register every relationship with a class, verification status, evidence citation, and plain-language meaning. Treat chronology and causality as separate claims.
5. Mark each statement `observed`, `inferred`, or `unknown`. For schema-derived declarations, also classify claim scope: a schema may prove `declared_vocabulary` or `allowed_structure`; code/tests may prove `implemented_behavior`; only a trace or persisted run record proves `observed_occurrence`. Formal artifact-flow edges require observed evidence that the target actually consumes the named artifact.
6. Normalize repository-specific evidence into the stable schema. Do not teach the renderer project vocabulary. For run/session views, populate the renderer-complete `projection` contract described in the reference; use `python3 scripts/build_dashboard_projection.py <model.json> <output.json>` as a deterministic starting point, then audit every generated handoff.
7. Validate the model with `python3 scripts/validate_model.py <model.json>`. Validation must fail when a dashboard lacks lanes/visits, references missing records, or presents an unobserved relationship as formal. For a compact standalone explainer, run `python3 scripts/render_model.py <model.json> <output.html>`.
8. Select only the views that answer the user's questions. Treat each as a first-class diagram grammar, not the same node grid with a different filter:
   - architecture/system diagram for components, ownership, deployment boundaries, stores, and external systems;
   - flow/sequence diagram for ordered messages, artifact handoffs, and human/system involvement across named participants;
   - lifecycle/state diagram for legal states, triggers, waits, retries, recovery, and terminal outcomes;
   - artifact/provenance flow for formal production and consumption;
   - decision/control map for route choices, gates, uncertainty, and operator authority;
   - session/run inspector only when ordered event evidence exists. Separate a real observed run from a code-derived execution recipe. When visit start/end evidence exists, prefer the `run_dashboard` grammar: a horizontal time axis, one lane per state family, repeated visit blocks whose widths encode duration, separate artifact rows, explicit human/system/terminal lanes, and only classified handoff ribbons.
   - continuity/session view for persisted state, handoff summaries, queue/task records, restart context, session identity, and explicit compaction evidence—or an explicit statement that the project does not preserve them.
9. Draw separate visual layers for state visits, artifact provenance, route decisions, human/system events, and explanatory context. A view may combine layers only when edge classes remain explicit.
10. Lead with “what this shows” and the decision-relevant takeaway. Explain every major diagram in plain language.
11. Verify labels, contrast, narrow-width layout, keyboard interaction, view navigation, and every edge against the canonical register. Report open uncertainties beside the visual.

## Visual and interaction rules

- Prefer semantic accuracy over polish. Make subsystem or state blocks visually stronger than handoff lines.
- Label edges by relationship class or use a legend with unmistakable line styles. Do not rely on similar colors; pair color with labels, shapes, stroke styles, or icons.
- Show external boundaries explicitly. Distinguish human actions from system events and terminal outcomes from ordinary states.
- Use solid lines for verified formal/control relationships, dashed lines for contextual or inferred relationships, and never let styling upgrade an uncertain claim.
- Keep detail available for each selected entity, event, visit, or artifact: responsibility, start/stop reasons, inputs, outputs, decision, evidence, provenance, and meaningful handoff. Display “none evidenced” or “unknown” instead of inventing content.
- In flow and run views, identify concrete payloads, records, files, folders, database entities, queues, and storage paths when evidence names them. Label conceptual or in-memory artifacts explicitly.
- Never infer compaction from long duration, context limits, or multi-step work. Show compaction only from an explicit transcript/event record. Keep formal artifacts, persisted state, queue/task records, handoff summaries, and narrative/restart context as different provenance classes.
- Keep diagrams compact. Prefer multiple focused views over one universal graph.
- Do not reduce a richly evidenced run to cards. For GraphRun-like ledgers—or any system with timed visits, durable artifacts, and event records—make the session dashboard a first-class view beside architecture, sequence, and lifecycle. Provide run selection and timeline/artifact focus controls when they materially help.
- Treat `projection` as a lossless visual index over canonical IDs, not a second narrative model. It may choose lane order, artifact rows, and anchors; it must not introduce facts, rename uncertainty into certainty, or contain an edge that is absent from the classified evidence register.
- Derive visual grammar from normalized semantics, never identifier spelling: entity kind and semantic role choose shapes/lanes; relationship class chooses line grammar; actor/boundary role chooses placement; artifact form/persistence chooses provenance rows; event order/time chooses sequence or duration; verification and claim scope choose certainty treatment. Project names remain labels and inspector evidence.
- Treat automated schema discovery as candidate generation, not truth promotion. It improves exact naming, completeness, and drift detection but does not prove that a state occurred, an event fired, an artifact persisted, or one component consumed another's output.

## Output contract

Deliver:

- a canonical model (JSON, YAML, or equivalently structured tables) with evidence citations and uncertainties;
- the smallest useful visual artifact containing an architecture view plus at least one lifecycle/state, provenance, or decision/control view;
- a short decision-first explanation of each view and its limits;
- validation evidence, including unresolved model warnings.

When schemas are available, also deliver a brief coverage statement: which declared states/events/artifacts were mapped, intentionally omitted, or left unresolved. Do not force unused declarations into diagrams.

For an implementation-grounded artifact, cite repository-relative paths and symbols or line ranges when stable. Do not claim runtime behavior from a proposal document alone. Do not imply a single execution order from unordered architecture evidence.
