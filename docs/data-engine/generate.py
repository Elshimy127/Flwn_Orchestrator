"""Build the orchestrator-facing API files from the data engine's live OpenAPI spec.

Outputs (in the target folder):
  data-engine-openapi.json   domain routes only + the schemas they reference
  API_REFERENCE.md           every endpoint (grouped by tag) + every schema's fields
"""
import copy
import json
import re
import sys

src, out_dir = sys.argv[1], sys.argv[2]
spec = json.load(open(src))

MEMORY = lambda p: p.startswith("/workspaces/{workspace_id}") or p in ("/healthz", "/readyz", "/auth/tokens")
paths = {p: v for p, v in spec["paths"].items() if not MEMORY(p)}

# --- collect referenced schemas (transitively) ---
schemas = spec["components"]["schemas"]
needed, stack = set(), []


def refs(node):
    if isinstance(node, dict):
        for k, v in node.items():
            if k == "$ref":
                yield v.split("/")[-1]
            else:
                yield from refs(v)
    elif isinstance(node, list):
        for v in node:
            yield from refs(v)


stack = list(refs(paths))
while stack:
    name = stack.pop()
    if name in needed:
        continue
    needed.add(name)
    stack.extend(refs(schemas[name]))

domain_spec = {
    "openapi": spec["openapi"],
    "info": {
        "title": "Flwn Data Engine: Domain API",
        "version": spec["info"].get("version", "0.1.0"),
        "description": "Domain CRUD routes of flwn-data-engine (memory/MCP routes excluded). "
        "Generated from the running code on branch feature/schema-and-basic-cruds.",
    },
    "paths": paths,
    "components": {"schemas": {k: schemas[k] for k in sorted(needed)}},
}
json.dump(domain_spec, open(f"{out_dir}/data-engine-openapi.json", "w"), indent=2)


# --- markdown reference ---
def type_of(s):
    if "$ref" in s:
        return s["$ref"].split("/")[-1]
    if "anyOf" in s:
        parts = [type_of(x) for x in s["anyOf"]]
        return " \\| ".join(parts)
    if "allOf" in s:
        return " & ".join(type_of(x) for x in s["allOf"])
    t = s.get("type", "any")
    if t == "array":
        return f"array<{type_of(s.get('items', {}))}>"
    fmt = s.get("format")
    if "enum" in s:
        return " \\| ".join(f"`{e}`" for e in s["enum"])
    return f"{t}({fmt})" if fmt else t


def constraints(s):
    bits = []
    for src in [s] + s.get("anyOf", []):
        for key, label in (("minLength", "min"), ("maxLength", "max"), ("minimum", "≥"),
                           ("maximum", "≤"), ("pattern", "pattern")):
            if key in src:
                val = src[key]
                bits.append(f"{label} `{val}`" if key == "pattern" else f"{label} {val}")
    return ", ".join(dict.fromkeys(bits))


def org_source(path, op):
    params = [p["name"] for p in op.get("parameters", [])]
    if path.startswith("/organizations/{orgId}"):
        return "path `orgId`"
    if "X-Organization-Id" in params:
        return "header"
    return "none (global)"


METHOD_ORDER = {"post": 0, "get": 1, "patch": 2, "put": 3, "delete": 4}
by_tag = {}
for path, item in paths.items():
    for method, op in item.items():
        if method not in METHOD_ORDER:
            continue
        tag = (op.get("tags") or ["other"])[0]
        by_tag.setdefault(tag, []).append((path, method, op))

lines = [
    "# Data Engine: API reference (domain CRUD)",
    "",
    "> **Generated** from the data engine's OpenAPI spec (`data-engine-openapi.json`, same folder).",
    "> Don't edit by hand; regenerate it when the data engine changes. For conventions, errors and",
    "> usage, read `DATA_ENGINE_GUIDE.md` first.",
    "",
    "Every route needs `X-Data-API-Key`. The **Org** column says where the organization comes from.",
    "",
    "## Endpoints",
    "",
]
TAG_ORDER = ["users", "organizations", "members", "workspaces", "teams", "projects",
             "work items", "work-items", "sprints", "tasks"]
for tag in sorted(by_tag, key=lambda t: (TAG_ORDER.index(t) if t in TAG_ORDER else 99, t)):
    lines += [f"### {tag.capitalize()}", "",
              "| Method | Path | Summary | Org | Body | Success | Errors | Query params |",
              "|---|---|---|---|---|---|---|---|"]
    for path, method, op in sorted(by_tag[tag], key=lambda x: (x[0], METHOD_ORDER[x[1]])):
        body = "—"
        rb = op.get("requestBody", {}).get("content", {}).get("application/json", {}).get("schema")
        if rb:
            body = f"`{type_of(rb)}`"
        ok = [c for c in op["responses"] if c.startswith("2")]
        succ = []
        for c in ok:
            sch = op["responses"][c].get("content", {}).get("application/json", {}).get("schema")
            succ.append(f"{c} `{type_of(sch)}`" if sch else c)
        errs = ", ".join(c for c in op["responses"] if not c.startswith("2"))
        q = [p for p in op.get("parameters", []) if p["in"] == "query"]
        qs = ", ".join(f"`{p['name']}`" + ("*" if p.get("required") else "") for p in q) or "—"
        lines.append(f"| `{method.upper()}` | `{path}` | {op.get('summary','')} | {org_source(path, op)} "
                     f"| {body} | {' / '.join(succ)} | {errs} | {qs} |")
    lines.append("")
lines += ["`*` = required query parameter. Every list route also takes `limit` (1–200, default 50) "
          "and `offset` (≥ 0, default 0).", "", "## Schemas", ""]

ENUMS = [n for n in sorted(needed) if "enum" in schemas[n]]
lines += ["### Enums", "", "| Enum | Values |", "|---|---|"]
for n in ENUMS:
    lines.append(f"| `{n}` | " + ", ".join(f"`{v}`" for v in schemas[n]["enum"]) + " |")
lines.append("")

for n in sorted(needed):
    s = schemas[n]
    if "enum" in s or "properties" not in s:
        continue
    req = set(s.get("required", []))
    lines += [f"### `{n}`", ""]
    if s.get("description"):
        lines += [s["description"].strip(), ""]
    lines += ["| Field | Type | Required | Default | Constraints |", "|---|---|---|---|---|"]
    for f, fs in s["properties"].items():
        default = fs.get("default", "")
        default = "—" if default == "" else f"`{json.dumps(default)}`"
        lines.append(f"| `{f}` | {type_of(fs)} | {'yes' if f in req else 'no'} | {default} | {constraints(fs) or '—'} |")
    lines.append("")

open(f"{out_dir}/API_REFERENCE.md", "w").write("\n".join(lines))
ops = sum(len(v) for v in by_tag.values())
print(f"{len(paths)} paths, {ops} operations, {len(needed)} schemas")
