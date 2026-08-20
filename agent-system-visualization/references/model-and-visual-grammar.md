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
- “How does work begin, pause, branch, and end?” → lifecycle/state view.
- “Where did this output come from?” → artifact/provenance flow.
- “Why did the system choose or block this action?” → decision/control map.
- “What happened in this particular run?” → ordered run walkthrough, only with event evidence.

Use separate views when combining them would blur classes. A run walkthrough is optional and never substitutes for the canonical model.

## Diagram grammar

- subsystem: strong rectangular block
- state/visit: rounded block with explicit state label
- decision: diamond or clearly labeled gate
- artifact: document shape or labeled artifact node
- actor/human event: person/event label distinct from automation
- external system: bounded or double-outline node outside the system boundary
- terminal outcome: terminal/capsule shape
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
