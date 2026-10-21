---
name: poteto-help
description: 說明 pstack 的技能與適用情境，依你的目標推薦流程並提供可直接使用的提示。
compatibility: opencode
metadata:
  opencode/slash: "true"
  opencode/autoinvoke: "false"
---

Read [the OpenCode runtime contract](../poteto-mode/references/opencode-runtime.md) before executing this skill.

# Pstack help

Read the routing table in ../poteto-mode/SKILL.md. Identify the user's intended result, available artifacts, and cheapest useful next step. Explain only the relevant workflow, its evidence, and any missing capability. Give a ready-to-use `/poteto-mode ...` or specific `/skill-name ...` prompt. Do not execute that prompt unless the user also requested the work. Describe this package's actual capabilities, not upstream platform integrations.
