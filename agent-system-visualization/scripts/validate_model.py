#!/usr/bin/env python3
"""Validate an agent-system canonical model using only the Python standard library."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ENTITY_KINDS = {
    "actor", "subsystem", "state", "visit", "trigger", "decision", "artifact",
    "store", "external_system", "human_event", "system_event", "terminal_outcome",
}
RELATIONSHIP_CLASSES = {
    "trigger", "state_transition", "route_decision", "artifact_production",
    "formal_artifact_input", "dependency", "control", "human_event", "system_event",
    "external_boundary", "terminal_transition", "continuity_context",
    "explanatory_association",
}
NON_FORMAL_CLASSES = {"continuity_context", "explanatory_association"}
VIEW_TYPES = {"architecture", "sequence", "state", "lifecycle", "provenance", "decision_control", "run_walkthrough", "run_dashboard", "continuity"}
VERIFICATION = {"observed", "inferred", "unknown"}


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def validate(model: dict) -> list[str]:
    errors: list[str] = []
    for key in ("version", "system", "takeaway", "evidence_sources", "entities", "relationships", "views", "uncertainties"):
        require(key in model, f"missing top-level field: {key}", errors)

    evidence_ids = {item.get("id") for item in model.get("evidence_sources", [])}
    require(None not in evidence_ids, "every evidence source needs an id", errors)

    entities = model.get("entities", [])
    entity_ids = [item.get("id") for item in entities]
    require(None not in entity_ids, "every entity needs an id", errors)
    require(len(entity_ids) == len(set(entity_ids)), "entity ids must be unique", errors)

    for entity in entities:
        entity_id = entity.get("id", "<missing>")
        require(entity.get("kind") in ENTITY_KINDS, f"entity {entity_id}: invalid kind", errors)
        require(entity.get("verification") in VERIFICATION, f"entity {entity_id}: invalid verification", errors)
        for field in ("label", "responsibility", "start_reason", "stop_reason", "inputs", "outputs", "decision", "handoff", "evidence", "uncertainty"):
            require(field in entity, f"entity {entity_id}: missing {field}", errors)
        for evidence_id in entity.get("evidence", []):
            require(evidence_id in evidence_ids, f"entity {entity_id}: unknown evidence {evidence_id}", errors)

    relationship_ids: list[str | None] = []
    for rel in model.get("relationships", []):
        rel_id = rel.get("id", "<missing>")
        relationship_ids.append(rel.get("id"))
        require(rel.get("from") in entity_ids, f"relationship {rel_id}: unknown from endpoint", errors)
        require(rel.get("to") in entity_ids, f"relationship {rel_id}: unknown to endpoint", errors)
        require(rel.get("class") in RELATIONSHIP_CLASSES, f"relationship {rel_id}: invalid or missing class", errors)
        require(rel.get("verification") in VERIFICATION, f"relationship {rel_id}: invalid verification", errors)
        require(isinstance(rel.get("formal"), bool), f"relationship {rel_id}: formal must be boolean", errors)
        for field in ("label", "meaning", "evidence"):
            require(field in rel, f"relationship {rel_id}: missing {field}", errors)
        for evidence_id in rel.get("evidence", []):
            require(evidence_id in evidence_ids, f"relationship {rel_id}: unknown evidence {evidence_id}", errors)
        if rel.get("class") in NON_FORMAL_CLASSES:
            require(rel.get("formal") is False, f"relationship {rel_id}: narrative/context class cannot be formal", errors)
        if rel.get("formal") is True:
            require(rel.get("verification") == "observed", f"relationship {rel_id}: formal edge must be observed", errors)
            require(bool(rel.get("evidence")), f"relationship {rel_id}: formal edge needs evidence", errors)

    require(None not in relationship_ids, "every relationship needs an id", errors)
    require(len(relationship_ids) == len(set(relationship_ids)), "relationship ids must be unique", errors)

    artifact_ids: list[str | None] = []
    for artifact in model.get("artifact_records", []):
        artifact_id = artifact.get("id", "<missing>")
        artifact_ids.append(artifact.get("id"))
        for field in ("label", "form", "location", "persistence", "verification", "evidence", "uncertainty"):
            require(field in artifact, f"artifact {artifact_id}: missing {field}", errors)
        require(artifact.get("verification") in VERIFICATION, f"artifact {artifact_id}: invalid verification", errors)
        for evidence_id in artifact.get("evidence", []):
            require(evidence_id in evidence_ids, f"artifact {artifact_id}: unknown evidence {evidence_id}", errors)
    require(None not in artifact_ids, "every artifact record needs an id", errors)
    require(len(artifact_ids) == len(set(artifact_ids)), "artifact record ids must be unique", errors)

    run_ids = [run.get("id") for run in model.get("runs", [])]
    require(None not in run_ids, "every run needs an id", errors)
    require(len(run_ids) == len(set(run_ids)), "run ids must be unique", errors)
    session_ids: list[str | None] = []
    for session in model.get("sessions", []):
        session_id = session.get("id", "<missing>")
        session_ids.append(session.get("id"))
        require(session.get("run_id") in run_ids, f"session {session_id}: unknown run", errors)
        require(session.get("verification") in VERIFICATION, f"session {session_id}: invalid verification", errors)
        for field in ("label", "role", "lane", "visit", "start", "end", "source", "detail", "evidence"):
            require(field in session, f"session {session_id}: missing {field}", errors)
        for evidence_id in session.get("evidence", []):
            require(evidence_id in evidence_ids, f"session {session_id}: unknown evidence {evidence_id}", errors)
    require(None not in session_ids, "every session needs an id", errors)
    require(len(session_ids) == len(set(session_ids)), "session ids must be unique", errors)
    event_ids: list[str | None] = []
    for event in model.get("events", []):
        event_id = event.get("id", "<missing>")
        event_ids.append(event.get("id"))
        require(event.get("run_id") in run_ids, f"event {event_id}: unknown run", errors)
        if event.get("session_id") is not None:
            require(event.get("session_id") in session_ids, f"event {event_id}: unknown session", errors)
        require(isinstance(event.get("order"), int), f"event {event_id}: order must be integer", errors)
        require(event.get("verification") in VERIFICATION, f"event {event_id}: invalid verification", errors)
        for field in ("label", "event_type", "actor", "state_before", "state_after", "input_refs", "output_refs", "evidence", "note"):
            require(field in event, f"event {event_id}: missing {field}", errors)
        for ref in [*event.get("input_refs", []), *event.get("output_refs", [])]:
            require(ref in artifact_ids, f"event {event_id}: unknown artifact ref {ref}", errors)
        for rel_id in event.get("relationship_ids", []):
            require(rel_id in relationship_ids, f"event {event_id}: unknown relationship {rel_id}", errors)
        for evidence_id in event.get("evidence", []):
            require(evidence_id in evidence_ids, f"event {event_id}: unknown evidence {evidence_id}", errors)
    require(None not in event_ids, "every event needs an id", errors)
    require(len(event_ids) == len(set(event_ids)), "event ids must be unique", errors)

    for view in model.get("views", []):
        view_id = view.get("id", "<missing>")
        require(view.get("type") in VIEW_TYPES, f"view {view_id}: invalid type", errors)
        require(bool(view.get("question")), f"view {view_id}: missing decision question", errors)
        for entity_id in view.get("entities", []):
            require(entity_id in entity_ids, f"view {view_id}: unknown entity {entity_id}", errors)
        for rel_id in view.get("relationships", []):
            require(rel_id in relationship_ids, f"view {view_id}: unknown relationship {rel_id}", errors)
        for artifact_id in view.get("artifact_records", []):
            require(artifact_id in artifact_ids, f"view {view_id}: unknown artifact record {artifact_id}", errors)
        for event_id in view.get("events", []):
            require(event_id in event_ids, f"view {view_id}: unknown event {event_id}", errors)
        for session_id in view.get("sessions", []):
            require(session_id in session_ids, f"view {view_id}: unknown session {session_id}", errors)
        for step in view.get("steps", []):
            require(step.get("relationship_id") in relationship_ids, f"view {view_id}: step has unknown relationship", errors)
        if view.get("type") == "run_dashboard":
            projection = view.get("projection")
            require(isinstance(projection, dict), f"view {view_id}: run_dashboard needs a renderer-complete projection", errors)
            if isinstance(projection, dict):
                require(projection.get("time_mode") in {"observed_time", "ordinal_recipe"}, f"view {view_id}: invalid projection time_mode", errors)
                lane_ids = [item.get("id") for item in projection.get("lanes", [])]
                visit_ids = [item.get("id") for item in projection.get("visits", [])]
                row_ids = [item.get("id") for item in projection.get("artifact_rows", [])]
                require(bool(lane_ids), f"view {view_id}: projection needs lanes", errors)
                require(bool(visit_ids), f"view {view_id}: projection needs visits", errors)
                require(None not in lane_ids and len(lane_ids) == len(set(lane_ids)), f"view {view_id}: projection lane ids must be present and unique", errors)
                require(None not in visit_ids and len(visit_ids) == len(set(visit_ids)), f"view {view_id}: projection visit ids must be present and unique", errors)
                for visit in projection.get("visits", []):
                    require(visit.get("lane_id") in lane_ids, f"view {view_id}: visit {visit.get('id')} has unknown lane", errors)
                    record_type, record_id = visit.get("record_type"), visit.get("record_id")
                    require(record_type in {"session", "event"}, f"view {view_id}: visit {visit.get('id')} has invalid record_type", errors)
                    require(record_id in (session_ids if record_type == "session" else event_ids), f"view {view_id}: visit {visit.get('id')} has unknown canonical record", errors)
                    if projection.get("time_mode") == "observed_time":
                        require(bool(visit.get("start")) and bool(visit.get("end")), f"view {view_id}: timed visit {visit.get('id')} needs start/end", errors)
                for item in projection.get("artifacts", []):
                    require(item.get("artifact_id") in artifact_ids, f"view {view_id}: projected artifact is unknown", errors)
                    require(item.get("row_id") in row_ids, f"view {view_id}: projected artifact has unknown row", errors)
                    if item.get("anchor_visit_id") is not None:
                        require(item.get("anchor_visit_id") in visit_ids, f"view {view_id}: projected artifact has unknown anchor visit", errors)
                for handoff in projection.get("handoffs", []):
                    require(handoff.get("artifact_id") in artifact_ids, f"view {view_id}: handoff {handoff.get('id')} has unknown artifact", errors)
                    require(handoff.get("target_visit_id") in visit_ids, f"view {view_id}: handoff {handoff.get('id')} has unknown target visit", errors)
                    require(handoff.get("class") in RELATIONSHIP_CLASSES, f"view {view_id}: handoff {handoff.get('id')} has invalid class", errors)
                    require(handoff.get("verification") in VERIFICATION, f"view {view_id}: handoff {handoff.get('id')} has invalid verification", errors)
                    require(isinstance(handoff.get("formal"), bool), f"view {view_id}: handoff {handoff.get('id')} formal must be boolean", errors)
                    if handoff.get("formal"):
                        require(handoff.get("verification") == "observed", f"view {view_id}: formal handoff {handoff.get('id')} must be observed", errors)
                        require(bool(handoff.get("evidence")), f"view {view_id}: formal handoff {handoff.get('id')} needs evidence", errors)
                    if handoff.get("class") in NON_FORMAL_CLASSES:
                        require(handoff.get("formal") is False, f"view {view_id}: contextual handoff {handoff.get('id')} cannot be formal", errors)
                for mark in projection.get("event_marks", []):
                    require(mark.get("event_id") in event_ids, f"view {view_id}: event mark has unknown event", errors)
                    require(mark.get("lane_id") in lane_ids, f"view {view_id}: event mark has unknown lane", errors)
                for terminal in projection.get("terminals", []):
                    require(terminal.get("from_visit_id") in visit_ids, f"view {view_id}: terminal {terminal.get('id')} has unknown source visit", errors)

    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: validate_model.py MODEL.json", file=sys.stderr)
        return 2
    path = Path(sys.argv[1])
    try:
        model = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"INVALID: {exc}", file=sys.stderr)
        return 1
    errors = validate(model)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"VALID: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
