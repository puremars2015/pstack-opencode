---
name: setup-pstack
description: 設定 OpenCode 版 pstack 的工作流程偏好與角色選項，保留目前聊天的預設模型。
compatibility: opencode
metadata:
  opencode/slash: "true"
---

Read [the OpenCode runtime contract](../poteto-mode/references/opencode-runtime.md) before executing this skill.

# Setup pstack

Read the runtime contract for configuration precedence. Detect the current host's actual model choices and tool capabilities; do not infer entitlement from model marketing names. If no preferences were requested, write the defaults below. Do not ask for a budget just to complete initial setup. An optional user-selected role override must match an exposed model and effort and comply with the host's override rules.

Use `~/.config/opencode/pstack/config.json` for a personal setup, or `.agents/pstack.json` when the user asks for project scope. Preserve existing recognized preferences and report invalid entries before replacing them. Validate the result against `../poteto-mode/references/config.schema.json`. If jsonschema is available, use it; otherwise explicitly report manual schema checking. Do not claim validation that was not performed. Never modify the default OpenCode model or global instructions.

```json
{"version": 1, "model": "inherit-parent", "candidate_count": 2, "roles": {}}
```

Report the actual path and settings. This file guides these skills; it does not alter the host or make new models available. Verification scaffolding and formal verification remain separate optional tasks.
