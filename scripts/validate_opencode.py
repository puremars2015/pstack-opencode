"""Validate OpenCode metadata and optionally compare installed skill contents."""
import argparse
import hashlib
import json
from pathlib import Path
import sys

import yaml

from validate import validate


parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--installed", type=Path)
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
result = validate(root)
errors = result["errors"]
explicit = 0
for entry in (root / "skills").glob("*/SKILL.md"):
    meta = yaml.safe_load(entry.read_text(encoding="utf-8").split("---", 2)[1])
    metadata = meta.get("metadata", {})
    if metadata.get("opencode/slash") != "true":
        errors.append(f"Missing slash exposure: {entry.parent.name}")
    if meta.get("compatibility") != "opencode":
        errors.append(f"Wrong compatibility: {entry.parent.name}")
    policy = yaml.safe_load((entry.parent / "agents/openai.yaml").read_text(encoding="utf-8"))
    if policy.get("policy", {}).get("allow_implicit_invocation") is False:
        explicit += 1
        if metadata.get("opencode/autoinvoke") != "false":
            errors.append(f"Lost explicit invocation policy: {entry.parent.name}")
    elif "opencode/autoinvoke" in metadata:
        errors.append(f"Unexpected invocation override: {entry.parent.name}")
    if not 1 <= len(meta.get("description", "")) <= 1024:
        errors.append(f"Invalid description length: {entry.parent.name}")
for path in (root / "skills").rglob("*.md"):
    text = path.read_text(encoding="utf-8")
    if any(token in text for token in ("Codex", "$CODEX_HOME", "$pstack-codex:", "collaboration.spawn_agent", "codex-runtime.md")):
        errors.append(f"Unadapted runtime reference: {path.relative_to(root)}")
if (result["skills"], result["playbooks"], explicit) != (55, 23, 54):
    errors.append("Expected 55 skills, 23 playbooks, and 54 explicit-only skills")
if args.installed:
    for skill in (root / "skills").iterdir():
        if not skill.is_dir():
            continue
        installed = args.installed.expanduser().resolve() / skill.name
        expected_files = {p.relative_to(skill) for p in skill.rglob("*") if p.is_file()}
        actual_files = {p.relative_to(installed) for p in installed.rglob("*") if p.is_file()}
        if expected_files != actual_files:
            errors.append(f"Installed file set differs: {skill.name}")
        for relative in expected_files & actual_files:
            expected = hashlib.sha256((skill / relative).read_bytes()).digest()
            actual = hashlib.sha256((installed / relative).read_bytes()).digest()
            if expected != actual:
                errors.append(f"Installed content differs: {skill.name}/{relative}")
result["explicit_only"] = explicit
print(json.dumps(result, ensure_ascii=False, indent=2))
sys.exit(bool(errors))
