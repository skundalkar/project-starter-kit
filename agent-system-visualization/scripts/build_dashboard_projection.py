#!/usr/bin/env python3
"""Build renderer-complete run-dashboard projections from canonical records.

The script does not discover implementation facts. It indexes existing sessions,
events, artifacts, relationships, and evidence into a stable visual contract.
Generated handoffs are limited to artifact inputs attached to an observed formal
relationship; everything else remains visible as a record without a causal edge.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


def slug(value: str) -> str:
    text = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return text or "lane"


def build(model: dict, view: dict) -> dict:
    run_id = view["run_id"]
    sessions = [s for s in model.get("sessions", []) if s.get("run_id") == run_id and s.get("visit") is not None]
    events = sorted((e for e in model.get("events", []) if e.get("run_id") == run_id), key=lambda e: e["order"])
    relationships = {r["id"]: r for r in model.get("relationships", [])}
    artifacts = {a["id"]: a for a in model.get("artifact_records", [])}
    evidence = {item["id"] for item in model.get("evidence_sources", [])}

    observed_time = bool(sessions) and all(s.get("start") and s.get("end") and "not recorded" not in str(s.get("start")) for s in sessions)
    lanes: list[dict] = []
    lane_seen: set[str] = set()

    def add_lane(label: str, kind: str = "state") -> str:
        base, candidate, suffix = slug(label), slug(label), 2
        while candidate in lane_seen and next((x for x in lanes if x["id"] == candidate and x["label"] == label), None) is None:
            candidate, suffix = f"{base}-{suffix}", suffix + 1
        if candidate not in lane_seen:
            lane_seen.add(candidate)
            lanes.append({"id": candidate, "label": label, "kind": kind, "order": len(lanes) + 1})
        return candidate

    visits: list[dict] = []
    session_to_visit: dict[str, str] = {}
    event_to_visit: dict[str, str] = {}
    if sessions:
        for order, session in enumerate(sorted(sessions, key=lambda s: s["start"]), 1):
            lane_id = add_lane(session["lane"].replace("-", " "))
            visit_id = f"visit-{slug(session['id'])}"
            session_to_visit[session["id"]] = visit_id
            visits.append({"id": visit_id, "record_type": "session", "record_id": session["id"], "lane_id": lane_id,
                           "label": session["label"], "order": order, "start": session["start"], "end": session["end"]})
        system_lane = add_lane("System / human / boundary", "system")
    else:
        for event in events:
            kind = "human" if event["event_type"] == "human" else "external" if event["event_type"] == "external_boundary" else "terminal" if event["event_type"] == "terminal" else "state"
            lane_id = add_lane(event["actor"], kind)
            visit_id = f"step-{slug(event['id'])}"
            event_to_visit[event["id"]] = visit_id
            visits.append({"id": visit_id, "record_type": "event", "record_id": event["id"], "lane_id": lane_id,
                           "label": event["label"], "order": event["order"]})
        system_lane = add_lane("System / human / boundary", "system")
    add_lane("Terminal outcome", "terminal")

    produced_by: dict[str, tuple[str, int]] = {}
    for event in events:
        anchor = session_to_visit.get(event.get("session_id")) or event_to_visit.get(event["id"])
        for artifact_id in event.get("output_refs", []):
            if anchor and artifact_id not in produced_by:
                produced_by[artifact_id] = (anchor, event["order"])
    if sessions:
        for session in sessions:
            source = str(session.get("source", "")).rstrip("/")
            if not source:
                continue
            for artifact_id, artifact in artifacts.items():
                if str(artifact.get("location", "")).startswith(source + "/") and artifact_id not in produced_by:
                    produced_by[artifact_id] = (session_to_visit[session["id"]], next(v["order"] for v in visits if v["id"] == session_to_visit[session["id"]]))

    referenced = []
    for event in events:
        for artifact_id in [*event.get("input_refs", []), *event.get("output_refs", [])]:
            if artifact_id in artifacts and artifact_id not in referenced:
                referenced.append(artifact_id)
    rows = [
        {"id": "source-inputs", "label": "Source / external inputs", "order": 1},
        {"id": "persisted-outputs", "label": "Persisted outputs", "order": 2},
        {"id": "transient-context", "label": "Transient / in-memory context", "order": 3},
    ]
    projected_artifacts = []
    for artifact_id in referenced:
        artifact = artifacts[artifact_id]
        producer = produced_by.get(artifact_id)
        transient = artifact.get("form") in {"in_memory", "conceptual"} or "not durable" in artifact.get("persistence", "").lower()
        row_id = "transient-context" if transient else "persisted-outputs" if producer else "source-inputs"
        projected_artifacts.append({"artifact_id": artifact_id, "row_id": row_id,
                                    "anchor_visit_id": producer[0] if producer else None,
                                    "anchor": "end", "order": producer[1] if producer else 0})

    handoffs = []
    for event in events:
        target = session_to_visit.get(event.get("session_id")) or event_to_visit.get(event["id"])
        if not target:
            continue
        formal_rels = [relationships[rid] for rid in event.get("relationship_ids", [])
                       if rid in relationships and relationships[rid].get("formal") and relationships[rid].get("verification") == "observed"]
        for artifact_id in event.get("input_refs", []):
            if artifact_id not in artifacts or (not formal_rels and event.get("verification") != "observed"):
                continue
            rel = next((r for r in formal_rels if r.get("class") == "formal_artifact_input"), formal_rels[0] if formal_rels else None)
            handoffs.append({"id": f"handoff-{slug(event['id'])}-{slug(artifact_id)}", "artifact_id": artifact_id,
                             "target_visit_id": target, "class": rel["class"] if rel else "formal_artifact_input", "formal": True, "verification": "observed",
                             "label": f"{artifacts[artifact_id]['label']} → {event['label']}",
                             "meaning": rel["meaning"] if rel else "The observed canonical event names this artifact in input_refs.",
                             "evidence": [x for x in (rel["evidence"] if rel else event["evidence"]) if x in evidence]})

    event_marks = []
    if sessions:
        for event in events:
            if event["event_type"] == "visit":
                continue
            item = {"event_id": event["id"], "lane_id": system_lane, "order": event["order"]}
            if event.get("time"):
                item["time"] = event["time"]
            event_marks.append(item)

    terminals = []
    terminal_events = [e for e in events if e["event_type"] == "terminal"]
    if terminal_events:
        for event in terminal_events:
            source = event_to_visit.get(event["id"]) or session_to_visit.get(event.get("session_id"))
            if source:
                terminals.append({"id": f"terminal-{slug(event['id'])}", "from_visit_id": source, "label": event["label"],
                                  "class": "terminal_transition", "verification": event["verification"], "evidence": event["evidence"]})
    elif visits:
        run = next((r for r in model.get("runs", []) if r["id"] == run_id), None)
        if run:
            terminals.append({"id": f"terminal-{slug(run_id)}", "from_visit_id": visits[-1]["id"],
                              "label": "; ".join(run.get("terminal_outcomes", [])) or "Terminal outcome",
                              "class": "terminal_transition", "verification": run["verification"], "evidence": run["evidence"]})

    return {"time_mode": "observed_time" if observed_time else "ordinal_recipe", "lanes": lanes, "visits": visits,
            "artifact_rows": rows, "artifacts": projected_artifacts, "handoffs": handoffs,
            "event_marks": event_marks, "terminals": terminals}


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: build_dashboard_projection.py MODEL.json OUTPUT.json", file=sys.stderr)
        return 2
    source, output = map(Path, sys.argv[1:])
    model = json.loads(source.read_text(encoding="utf-8"))
    dashboard_runs = {view.get("run_id") for view in model.get("views", []) if view.get("type") == "run_dashboard"}
    additions = []
    for run in model.get("runs", []):
        run_id = run["id"]
        if run_id in dashboard_runs:
            continue
        run_events = [e for e in model.get("events", []) if e.get("run_id") == run_id]
        run_sessions = [s for s in model.get("sessions", []) if s.get("run_id") == run_id]
        if not run_events and not run_sessions:
            continue
        artifact_ids = []
        for event in run_events:
            for artifact_id in [*event.get("input_refs", []), *event.get("output_refs", [])]:
                if artifact_id not in artifact_ids:
                    artifact_ids.append(artifact_id)
        observed = run.get("kind") == "observed_run" and bool(run_sessions)
        additions.append({"id": f"dashboard-{slug(run_id)}", "type": "run_dashboard", "label": run["label"],
                          "question": "What happened in this run or implemented recipe, step by step?",
                          "meaning": "A normalized visit, artifact, event, handoff, and terminal projection derived from canonical records.",
                          "takeaway": "Widths encode observed duration." if observed else "This is a code/design-derived ordinal recipe; it does not claim a recorded runtime session or elapsed duration.",
                          "entities": [], "relationships": [], "run_id": run_id,
                          "sessions": [s["id"] for s in run_sessions], "events": [e["id"] for e in run_events],
                          "artifact_records": artifact_ids})
    if additions:
        insert_at = next((i for i, view in enumerate(model.get("views", [])) if view.get("type") == "continuity"), len(model.get("views", [])))
        model["views"][insert_at:insert_at] = additions
    for view in model.get("views", []):
        if view.get("type") == "run_dashboard":
            view["projection"] = build(model, view)
    output.write_text(json.dumps(model, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"PROJECTED: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
