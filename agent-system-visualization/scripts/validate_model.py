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
VIEW_TYPES = {"architecture", "lifecycle", "provenance", "decision_control", "run_walkthrough"}
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

    for view in model.get("views", []):
        view_id = view.get("id", "<missing>")
        require(view.get("type") in VIEW_TYPES, f"view {view_id}: invalid type", errors)
        require(bool(view.get("question")), f"view {view_id}: missing decision question", errors)
        for entity_id in view.get("entities", []):
            require(entity_id in entity_ids, f"view {view_id}: unknown entity {entity_id}", errors)
        for rel_id in view.get("relationships", []):
            require(rel_id in relationship_ids, f"view {view_id}: unknown relationship {rel_id}", errors)

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
