# Canonical model and visual grammar

## Evidence precedence

Use the strongest available source for each claim:

1. runtime traces or persisted records from the relevant version;
2. executable tests and code paths;
3. schemas, contracts, and configuration;
4. current operational documentation;
5. plans, proposals, mockups, and retrospective narrative.

Lower-ranked sources can explain intent but cannot override observed behavior. Record contradictions and the evidence cutoff.

## Entity kinds

- `actor`: human or system authority that initiates or approves work
- `subsystem`: component with a stable responsibility
- `state`: durable or meaningful lifecycle condition
- `visit`: one observed entry into a state or phase during a run
- `trigger`: condition or event that starts processing
- `decision`: branch, gate, classification, or approval point
- `artifact`: named output that can be stored, passed, or inspected
- `store`: persistence or recovery boundary
- `external_system`: dependency outside the modeled boundary
- `human_event`: intervention, correction, approval, or cancellation
- `system_event`: retry, wait, timeout, compaction, recovery, or boundary event
- `terminal_outcome`: completion, failure, cancellation, release, or escalation

## Relationship classes

Every edge must use exactly one primary class:

| Class | Meaning | Formal edge? |
|---|---|---:|
| `trigger` | An event or condition starts a transition or activity | yes |
| `state_transition` | The system can move between states under a named condition | yes |
| `route_decision` | A decision selects a next state, action, or outcome | yes |
| `artifact_production` | A source creates or materially updates an artifact | yes |
| `formal_artifact_input` | A target actually consumes the named artifact | yes |
| `dependency` | A component requires another capability or service | yes |
| `control` | An actor, gate, or policy authorizes or blocks action | yes |
| `human_event` | A human action changes system state or evidence | yes |
| `system_event` | A retry, wait, timeout, recovery, or similar event affects processing | yes |
| `external_boundary` | Data or control crosses the modeled system boundary | yes |
| `terminal_transition` | A condition ends the modeled lifecycle | yes |
| `continuity_context` | Prior-run or restart context informs interpretation but is not a consumed formal input | no |
| `explanatory_association` | Narrative relationship useful for explanation without verified causality | no |

If one fact carries two semantics, create two separately evidenced relationships. Do not use a vague `flow` class.

## Verification states

- `observed`: directly supported by the cited source.
- `inferred`: a bounded interpretation from cited evidence; render as contextual and state the inference.
- `unknown`: evidence is absent or conflicting; usually record as uncertainty rather than an edge.

Formal edges must be `observed` and cite evidence. Inferred chronology does not establish causality. Mere coexistence in a state object does not establish artifact consumption.

## View selection

Choose views by decision question, not by a default timeline:

- “What exists and who owns what?” → architecture/subsystem map.
- “Which participant sends what, in what order?” → flow/sequence diagram.
- “How does work begin, pause, branch, and end?” → lifecycle/state view.
- “Where did this output come from?” → artifact/provenance flow.
- “Why did the system choose or block this action?” → decision/control map.
- “What happened in this particular session/run?” → run inspector, only with ordered event evidence.
- “When did each state visit occur, what did it consume, and what crossed to the next visit?” → time-scaled run dashboard when start/end evidence exists.
- “What context survived a handoff or restart, and was compaction recorded?” → continuity/session view.

Use separate views when combining them would blur classes. A run walkthrough is optional and never substitutes for the canonical model.

Architecture, sequence, and state views are different visual grammars:

- Architecture groups components inside explicit system/deployment boundaries and places external actors or services outside them. It must not imply execution order.
- Sequence uses named participant lanes and an ordered message/event ledger. Every message that implies a handoff must cite a registered relationship; adjacency alone is not an edge.
- State uses durable state nodes and registered state/terminal transitions. Do not put processing components into a state diagram merely because they run during a state.
- Provenance follows named artifact records through production, persistence, transformation, and formal consumption.
- Run inspection separates sessions, repeated visits, human events, system events, artifacts, decisions, and terminal outcomes. Repeated visits remain distinct records even when they enter the same state or subsystem.

If runtime evidence is unavailable, a code-derived ordered path may be shown as an **implemented execution recipe**. It must not have observed timestamps, session IDs, or run claims.

### Time-scaled run dashboard

Use `run_dashboard` when evidence contains visit start/end times plus named artifacts or events. This is the reusable grammar proven by the GraphRun visualization—not a GraphRun-specific phase list.

- Put one state-family lane per recurring phase and preserve each visit (`V1`, `V2`, …) as its own time-width block.
- Add explicit human, system/compaction, external-boundary, and terminal lanes. Never infer compaction or event time; if exact time is absent, say so rather than placing an apparently exact marker.
- Put artifacts in compact rows below the visit timeline. Position a produced artifact at its evidenced creation/end point and connect it only to visits that formally consume it.
- Give all ordinary formal artifact handoffs one subdued base style. Use a distinct dashed style only for terminal/non-consumption routes. Offset fan-out curves so overdraw does not imply extra importance.
- Let the chart use the browser width with horizontal scrolling as fallback. Keep phase blocks stronger than handoff ribbons.
- Provide a detail inspector for visits, artifacts, events, and handoffs. A visit detail must answer why it started, why it stopped, its inputs/outputs, route, evidence, and what the next participant knew.
- For multiple runs, allow combined and per-run inspection. Compress inactive gaps only when they are marked as compressed; never draw restart context as a formal cross-run artifact edge.

If visit timing is absent but ordered events exist, use `run_walkthrough`. If neither exists, use a lifecycle/recipe view and state that no observed run record is preserved.

## Artifact and run records

Use an artifact record when an implementation names a concrete inspectable object. Record its form (`file`, `folder`, `database_entity`, `api_payload`, `queue_record`, `state_field`, `in_memory`, or `conceptual`), exact or patterned location, persistence behavior, evidence, and uncertainty. “Conceptual” and “in memory only” are valid, useful answers.

For an observed run, record persistent sessions and repeated visits separately, assigning each to a stable lane. Record ordered events with stable IDs, session/visit identity, actor/system involvement, state before/after, input/output artifact references, confidence, and source. Keep compactions, retries, waits, recoveries, human actions, and external-boundary calls as explicit events. Do not infer causality from timestamp proximity. A run inspector should show lanes/visits plus the event ledger when both are available.

For every project, explicitly answer: were execution sessions/threads/runs recorded; is compaction evidenced; and how was context passed? If the repository has no such records, say so in the continuity view and distinguish the code/design execution recipe from an observed run. Never infer compaction. Treat these separately:

- formal artifact: named, evidenced producer/consumer handoff;
- persisted state: durable recovery input, not automatically a message between agents;
- queue/task record: scheduled work with its own durability semantics;
- handoff summary: explicit continuity artifact when named and consumed;
- narrative/restart context: explanatory context, never a formal data-flow edge without consumption evidence.

## Diagram grammar

- subsystem: strong rectangular block
- state/visit: rounded block with explicit state label
- decision: diamond or clearly labeled gate
- artifact: document shape or labeled artifact node
- actor/human event: person/event label distinct from automation
- external system: bounded or double-outline node outside the system boundary
- terminal outcome: terminal/capsule shape
- sequence participant: named lane with a visible lifeline
- event/visit: numbered marker with type and verification label
- verified formal/control edge: solid, directional, class label
- contextual or inferred relationship: dashed, directional only if direction is evidenced
- uncertainty: warning marker or explicit “unknown,” not a faint pseudo-edge

Keep line weight subordinate to nodes. Maintain readable contrast in light and dark contexts. Do not encode meaning with color alone.

## Entity detail contract

For interactive artifacts, selecting any major entity must expose:

- responsibility or meaning;
- start reason and stop reason;
- formal inputs and outputs;
- decision or control exercised;
- cited evidence and verification status;
- meaningful handoff, or “none evidenced”;
- relevant uncertainty.

## Final audit

Before delivery, ask:

1. Does every rendered edge exist in the relationship register?
2. Does every formal artifact-input edge prove consumption rather than context?
3. Are human events, system events, state visits, decisions, artifacts, and story visually distinguishable?
4. Are external boundaries and terminal outcomes explicit?
5. Are uncertainties visible without being promoted into facts?
6. Does each view begin with its meaning and takeaway?
7. Can a color-blind reader distinguish all important categories?
8. Are architecture, sequence, and state views genuinely different diagrams rather than filters over one layout?
9. Does every concrete artifact reference say whether it is persisted, in memory, a payload, or conceptual?
