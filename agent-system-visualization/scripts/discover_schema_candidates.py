#!/usr/bin/env python3
"""Discover exact schema vocabulary as reviewable candidates, never runtime facts."""

from __future__ import annotations

import ast
import json
import re
import sys
from pathlib import Path


SKIP_DIRS = {".git", "node_modules", "dist", "build", "coverage", ".next", ".venv", "venv"}
TEXT_EXTENSIONS = {".ts", ".tsx", ".js", ".jsx", ".py", ".json"}
SKIP_FILES = {"package-lock.json", "npm-shrinkwrap.json", "composer.lock"}


def candidate(path: Path, root: Path, symbol: str, value: str, extractor: str, line: int | None = None) -> dict:
    return {
        "source_path": str(path.relative_to(root)),
        "symbol": symbol,
        "source_name": value,
        "candidate_kind": "unclassified_vocabulary",
        "suggested_claim_scope": "declared_vocabulary",
        "extractor": extractor,
        "line": line,
        "review_status": "unreviewed",
        "note": "Classify semantically and verify in source before promotion; this does not prove runtime occurrence.",
    }


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def scan_js(path: Path, root: Path, text: str) -> list[dict]:
    found: list[dict] = []
    union = re.compile(r"(?:export\s+)?type\s+(\w+)\s*=\s*((?:['\"][^'\"]+['\"]\s*\|?\s*)+);", re.S)
    for match in union.finditer(text):
        for value in re.findall(r"['\"]([^'\"]+)['\"]", match.group(2)):
            found.append(candidate(path, root, match.group(1), value, "ts_literal_union", line_number(text, match.start())))
    enum = re.compile(r"(?:export\s+)?enum\s+(\w+)\s*\{(.*?)\}", re.S)
    for match in enum.finditer(text):
        for value in re.findall(r"(?:\w+)\s*=\s*['\"]([^'\"]+)['\"]", match.group(2)):
            found.append(candidate(path, root, match.group(1), value, "ts_enum", line_number(text, match.start())))
    zenum = re.compile(r"(?:const|let|var)\s+(\w+)\s*=.*?z\.enum\s*\(\s*\[(.*?)\]", re.S)
    for match in zenum.finditer(text):
        for value in re.findall(r"['\"]([^'\"]+)['\"]", match.group(2)):
            found.append(candidate(path, root, match.group(1), value, "zod_enum", line_number(text, match.start())))
    property_union = re.compile(r"\b(\w+)\s*:\s*((?:['\"][^'\"]+['\"]\s*\|\s*)+['\"][^'\"]+['\"])")
    for match in property_union.finditer(text):
        for value in re.findall(r"['\"]([^'\"]+)['\"]", match.group(2)):
            found.append(candidate(path, root, match.group(1), value, "ts_property_literal_union", line_number(text, match.start())))
    object_literal = re.compile(r"\btype\s*:\s*['\"]([^'\"]+)['\"]")
    for match in object_literal.finditer(text):
        prefix = text[:match.start()]
        owners = list(re.finditer(r"(?:export\s+)?type\s+(\w+)\s*=", prefix))
        symbol = f"{owners[-1].group(1)}.type" if owners else "type"
        found.append(candidate(path, root, symbol, match.group(1), "ts_discriminant_literal", line_number(text, match.start())))
    return found


def scan_python(path: Path, root: Path, text: str) -> list[dict]:
    found: list[dict] = []
    try:
        tree = ast.parse(text)
    except SyntaxError:
        return found
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef) and any(getattr(base, "id", "") in {"Enum", "StrEnum"} for base in node.bases):
            for item in node.body:
                if isinstance(item, (ast.Assign, ast.AnnAssign)):
                    value_node = item.value
                    if isinstance(value_node, ast.Constant) and isinstance(value_node.value, str):
                        found.append(candidate(path, root, node.name, value_node.value, "python_enum", item.lineno))
        if isinstance(node, ast.AnnAssign) and isinstance(node.annotation, ast.Subscript) and getattr(node.annotation.value, "id", "") == "Literal":
            symbol = getattr(node.target, "id", "Literal")
            values = node.annotation.slice.elts if isinstance(node.annotation.slice, ast.Tuple) else [node.annotation.slice]
            for value_node in values:
                if isinstance(value_node, ast.Constant) and isinstance(value_node.value, str):
                    found.append(candidate(path, root, symbol, value_node.value, "python_literal", node.lineno))
    return found


def scan_json(path: Path, root: Path, text: str) -> list[dict]:
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        return []
    found: list[dict] = []

    def walk(value: object, pointer: str = "#") -> None:
        if isinstance(value, dict):
            if isinstance(value.get("enum"), list):
                for item in value["enum"]:
                    if isinstance(item, (str, int, float, bool)):
                        found.append(candidate(path, root, pointer, str(item), "json_schema_enum"))
            for key, child in value.items():
                walk(child, f"{pointer}/{key}")
        elif isinstance(value, list):
            for index, child in enumerate(value):
                walk(child, f"{pointer}/{index}")

    walk(data)
    return found


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: discover_schema_candidates.py PROJECT_ROOT OUTPUT.json", file=sys.stderr)
        return 2
    root, output = Path(sys.argv[1]).resolve(), Path(sys.argv[2])
    if not root.is_dir():
        print(f"ERROR: not a directory: {root}", file=sys.stderr)
        return 1
    found: list[dict] = []
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.name in SKIP_FILES or path.suffix.lower() not in TEXT_EXTENSIONS or any(part in SKIP_DIRS for part in path.parts):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        if path.suffix.lower() == ".py":
            found.extend(scan_python(path, root, text))
        elif path.suffix.lower() == ".json":
            found.extend(scan_json(path, root, text))
        else:
            found.extend(scan_js(path, root, text))
    unique = {(item["source_path"], item["symbol"], item["source_name"], item["extractor"]): item for item in found}
    payload = {
        "project_root": str(root),
        "disclaimer": "Candidates prove declared vocabulary only. Audit and classify before adding them to a canonical model.",
        "candidates": sorted(unique.values(), key=lambda item: (item["source_path"], item.get("line") or 0, item["symbol"], item["source_name"])),
    }
    output.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"DISCOVERED: {len(payload['candidates'])} candidates -> {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
