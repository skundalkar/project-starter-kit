#!/usr/bin/env python3
"""Render a validated canonical model as a self-contained interactive HTML explainer."""

from __future__ import annotations

import html
import json
import sys
from pathlib import Path


def render(model: dict) -> str:
    title = html.escape(model["system"]["name"])
    data = json.dumps(model, ensure_ascii=False).replace("</", "<\\/")
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} — agent system visualization</title>
<style>
:root{{--ink:#18232b;--muted:#5d6b73;--paper:#f7f5ef;--panel:#fff;--line:#a9b4b8;--accent:#116a72;--accent2:#9c4f24;--soft:#e7f2f1;--warn:#fff1d6;--shadow:0 10px 30px rgba(24,35,43,.08)}}
*{{box-sizing:border-box}} body{{margin:0;background:var(--paper);color:var(--ink);font:15px/1.45 ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}} button{{font:inherit}} .shell{{max-width:1180px;margin:auto;padding:28px 20px 44px}} .kicker{{font-size:.78rem;letter-spacing:.11em;text-transform:uppercase;color:var(--accent);font-weight:700}} h1{{font-size:clamp(1.8rem,4vw,3rem);line-height:1.05;margin:.35rem 0 .75rem}} h2{{font-size:1.25rem;margin:0 0 .35rem}} h3{{font-size:1rem;margin:0}} p{{margin:.3rem 0}} .lead{{max-width:900px;font-size:1.05rem}} .takeaway{{margin:20px 0;padding:16px 18px;border-left:5px solid var(--accent);background:var(--soft)}} .takeaway strong{{display:block;margin-bottom:4px}} .meta{{display:flex;flex-wrap:wrap;gap:8px;margin-top:14px}} .chip,.kind{{display:inline-flex;align-items:center;border:1px solid var(--line);border-radius:999px;padding:3px 8px;font-size:.76rem;background:var(--panel)}} .tabs{{display:flex;flex-wrap:wrap;gap:8px;margin:24px 0 14px}} .tabs button{{border:1px solid var(--line);background:var(--panel);color:var(--ink);padding:9px 13px;border-radius:8px;cursor:pointer}} .tabs button[aria-selected="true"]{{background:var(--ink);color:var(--paper);border-color:var(--ink)}} .view-head{{display:grid;grid-template-columns:minmax(0,1fr) minmax(220px,.45fr);gap:18px;align-items:start;margin-bottom:14px}} .view-note{{color:var(--muted)}} .view-takeaway{{font-weight:650;border-left:3px solid var(--accent2);padding-left:12px}} .canvas{{display:grid;grid-template-columns:minmax(0,1.6fr) minmax(280px,.8fr);gap:18px;align-items:start}} .map{{min-width:0}} .nodes{{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:10px;margin-bottom:18px}} .node{{min-height:112px;text-align:left;padding:13px;border:2px solid var(--ink);border-radius:8px;background:var(--panel);color:var(--ink);cursor:pointer;box-shadow:var(--shadow)}} .node:hover,.node:focus-visible{{outline:3px solid #f0b75d;outline-offset:2px}} .node[aria-pressed="true"]{{background:var(--soft);border-color:var(--accent)}} .node .kind{{margin-bottom:8px;border-style:dashed}} .node .responsibility{{display:block;color:var(--muted);margin-top:5px}} .node[data-kind="decision"]{{border-radius:22px;border-color:var(--accent2)}} .node[data-kind="artifact"],.node[data-kind="store"]{{border-left:8px solid var(--accent)}} .node[data-kind="external_system"]{{border-style:dashed}} .node[data-kind="human_event"],.node[data-kind="actor"]{{border-left:8px solid var(--accent2)}} .node[data-kind="terminal_outcome"]{{border-radius:999px}} .relations{{display:grid;gap:8px}} .relation{{display:grid;grid-template-columns:minmax(120px,1fr) minmax(150px,.9fr) minmax(120px,1fr);align-items:center;gap:8px;padding:10px 0;border-top:1px solid var(--line)}} .endpoint{{font-weight:650}} .edge{{position:relative;text-align:center;color:var(--accent);font-size:.78rem;padding:5px 18px;border-top:3px solid currentColor}} .edge:after{{content:"";position:absolute;right:0;top:-6px;border-left:8px solid currentColor;border-top:5px solid transparent;border-bottom:5px solid transparent}} .edge.nonformal,.edge.inferred{{border-top-style:dashed;color:var(--accent2)}} .edge small{{display:block;color:var(--muted)}} .detail{{position:sticky;top:12px;background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:16px;box-shadow:var(--shadow)}} .detail dl{{margin:12px 0 0;display:grid;gap:10px}} .detail dt{{font-size:.72rem;text-transform:uppercase;letter-spacing:.08em;color:var(--muted)}} .detail dd{{margin:2px 0 0}} .detail ul{{margin:4px 0 0;padding-left:18px}} .uncertainty{{margin-top:24px;padding:16px;background:var(--warn);border:1px solid #d99a38;border-radius:8px}} .sources{{margin-top:24px}} .sources details{{background:var(--panel);border-top:1px solid var(--line);padding:10px}} .legend{{display:flex;flex-wrap:wrap;gap:12px;margin:12px 0;color:var(--muted);font-size:.8rem}} .legend span:before{{content:"";display:inline-block;width:26px;border-top:3px solid var(--accent);vertical-align:middle;margin-right:6px}} .legend .context:before{{border-top-style:dashed;border-color:var(--accent2)}} .sr-only{{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}}
@media (max-width:780px){{.view-head,.canvas{{grid-template-columns:1fr}} .detail{{position:static}} .relation{{grid-template-columns:1fr}} .edge{{text-align:left;margin:2px 0}} .edge:after{{right:0}}}}
@media (prefers-color-scheme:dark){{:root{{--ink:#e8eeee;--muted:#aab7ba;--paper:#101719;--panel:#182225;--line:#526064;--accent:#70c7c8;--accent2:#f0ad76;--soft:#173638;--warn:#3a2d16;--shadow:none}}}}
</style>
</head>
<body>
<main class="shell" id="app"><div class="kicker">Canonical agent-system model</div><h1>{title}</h1><p class="lead" id="boundary"></p><div class="takeaway"><strong>What this shows</strong><span id="takeaway"></span></div><div class="meta" id="meta"></div><nav class="tabs" id="tabs" aria-label="Diagram views"></nav><section id="view"></section><section class="uncertainty"><h2>Uncertainties and boundaries</h2><ul id="uncertainties"></ul></section><section class="sources"><h2>Evidence register</h2><div id="sources"></div></section></main>
<script>
const MODEL={data};
const byId=new Map(MODEL.entities.map(e=>[e.id,e]));
const relById=new Map(MODEL.relationships.map(r=>[r.id,r]));
const $=id=>document.getElementById(id);
const text=(tag,value,cls)=>{{const el=document.createElement(tag);if(cls)el.className=cls;el.textContent=value;return el}};
$("boundary").textContent=MODEL.system.boundary;
$("takeaway").textContent=MODEL.takeaway;
for(const value of [`Audience: ${{MODEL.system.audience}}`,`Decision: ${{MODEL.system.decision}}`,`Evidence cutoff: ${{MODEL.system.evidence_cutoff}}`]) $("meta").append(text("span",value,"chip"));
MODEL.uncertainties.forEach(item=>$("uncertainties").append(text("li",item)));
MODEL.evidence_sources.forEach(source=>{{const d=document.createElement("details");const s=text("summary",`${{source.id}} · ${{source.path}}`);d.append(s,text("p",`${{source.kind}} — ${{source.note}}`));$("sources").append(d)}});
function detail(entity){{const box=document.createElement("aside");box.className="detail";box.setAttribute("aria-live","polite");box.append(text("div",entity.kind.replaceAll("_"," "),"kicker"),text("h2",entity.label),text("p",entity.responsibility));const dl=document.createElement("dl");const fields=[["Start reason",entity.start_reason],["Stop reason",entity.stop_reason],["Inputs",entity.inputs],["Outputs",entity.outputs],["Decision / control",entity.decision],["Meaningful handoff",entity.handoff],["Verification",entity.verification],["Evidence",entity.evidence],["Uncertainty",entity.uncertainty]];for(const [label,value] of fields){{const wrap=document.createElement("div");wrap.append(text("dt",label));const dd=document.createElement("dd");if(Array.isArray(value)){{const ul=document.createElement("ul");value.forEach(v=>ul.append(text("li",v)));dd.append(ul)}}else dd.textContent=value;wrap.append(dd);dl.append(wrap)}}box.append(dl);return box}}
function render(view){{document.querySelectorAll("#tabs button").forEach(b=>b.setAttribute("aria-selected",String(b.dataset.id===view.id)));const section=$("view");section.replaceChildren();const head=document.createElement("div");head.className="view-head";const left=document.createElement("div");left.append(text("div",view.type.replaceAll("_"," "),"kicker"),text("h2",view.question),text("p",view.meaning||"This view is derived from the canonical entity and relationship register.","view-note"));head.append(left,text("p",view.takeaway||MODEL.takeaway,"view-takeaway"));section.append(head);const legend=document.createElement("div");legend.className="legend";legend.append(text("span","verified formal/control relationship"),text("span","context or inference","context"));section.append(legend);const canvas=document.createElement("div");canvas.className="canvas";const map=document.createElement("div");map.className="map";const nodes=document.createElement("div");nodes.className="nodes";const entities=view.entities.map(id=>byId.get(id)).filter(Boolean);let selected=entities[0];const detailSlot=document.createElement("div");function select(entity,button){{selected=entity;nodes.querySelectorAll("button").forEach(b=>b.setAttribute("aria-pressed",String(b===button)));detailSlot.replaceChildren(detail(entity))}}entities.forEach(entity=>{{const button=document.createElement("button");button.className="node";button.dataset.kind=entity.kind;button.setAttribute("aria-pressed","false");button.append(text("span",entity.kind.replaceAll("_"," "),"kind"),text("h3",entity.label),text("span",entity.responsibility,"responsibility"));button.addEventListener("click",()=>select(entity,button));nodes.append(button)}});map.append(nodes);const relations=document.createElement("div");relations.className="relations";relations.setAttribute("aria-label","Classified relationships");view.relationships.map(id=>relById.get(id)).filter(Boolean).forEach(rel=>{{const row=document.createElement("div");row.className="relation";const edge=document.createElement("div");edge.className=`edge ${{rel.formal?"formal":"nonformal"}} ${{rel.verification==="inferred"?"inferred":""}}`;edge.append(text("span",rel.class.replaceAll("_"," ")),text("small",`${{rel.label}} · ${{rel.id}}`));row.append(text("div",byId.get(rel.from)?.label||rel.from,"endpoint"),edge,text("div",byId.get(rel.to)?.label||rel.to,"endpoint"));relations.append(row)}});map.append(relations);canvas.append(map,detailSlot);section.append(canvas);const first=nodes.querySelector("button");if(first)select(selected,first)}}
MODEL.views.forEach((view,index)=>{{const button=text("button",view.label||view.type.replaceAll("_"," "));button.type="button";button.dataset.id=view.id;button.setAttribute("aria-selected",String(index===0));button.addEventListener("click",()=>render(view));$("tabs").append(button)}});
render(MODEL.views[0]);
</script>
</body>
</html>
"""


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: render_model.py MODEL.json OUTPUT.html", file=sys.stderr)
        return 2
    model_path, output_path = map(Path, sys.argv[1:])
    model = json.loads(model_path.read_text(encoding="utf-8"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(render(model), encoding="utf-8")
    print(f"RENDERED: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
