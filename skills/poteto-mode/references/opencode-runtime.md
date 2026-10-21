# OpenCode runtime contract

This is a skills-only adaptation. Read this contract before executing a bundled workflow. User instructions, repository instructions, and host permissions take precedence. A skill does not grant permission to message people, commit, publish, merge, delete data, or change unrelated configuration. Preserve user changes and complete authorized, reversible work without unnecessary confirmation.

## Tools and models

Use tools actually exposed in this session. Prefer Glob and Grep for discovery, Read for content, and apply_patch for edits when available. Use the host todo tool for substantial work. Use installed browser/computer tools for real UI verification. If a capability is absent, report the gap and use an honest narrower check; never claim simulated checks as real execution.

Delegate with OpenCode's Task tool only when allowed, using an available agent type. Give workers a complete task, exact source revision, owned files or isolated output directory, acceptance checks, and required evidence. Workers can share files; writable alternatives need isolated directories or managed worktrees. Respect concurrency limits, use the tool's completion/resume mechanism, and inspect artifacts yourself. Do not create user chats as workers. If delegation is unavailable, execute sequentially and disclose that independent review was unavailable. Parallelize independent tool calls only through the host's supported interface.

Inherit the current chat model. Do not invent model identifiers, launch external model CLIs, or change the default model. Per-role overrides require explicit user selection and an actually configured OpenCode agent/model that the delegation tool can select. Workflow JSON alone does not configure agents. Same-model review is not a different-model panel. Effort/variant controls must match the exposed tool schema.

## Optional configuration

Use `<repository>/.agents/pstack.json` if present; otherwise use `~/.config/opencode/pstack/config.json`. Do not merge the two. Missing configuration means inherited model, host effort, two comparison candidates, and no background scheduling. See [config.schema.json](config.schema.json). These are workflow preferences, NOT native opencode.json settings. Only setup-pstack writes them on a setup request. Do not edit global instructions, permissions, providers, or default models.

## Boundaries and evidence

Run on the actual platform. On Windows, use PowerShell syntax and do not assume bash, /tmp, Bun, Linux profilers, or macOS tools. Prefer Python for bundled scripts. Use the host-approved temporary directory or an established project scratch location. Never delete a checkout with user changes as incidental cleanup.

Changes invalidate affected verification. Record exact revisions for reviews and identify uncommitted edits. A green build does not prove behavior or authorize publishing. Use authenticated GitHub tools when available; disclose missing access. Commit, PR creation, merge, deployment, notifications, and recurring jobs require applicable user authorization. No skill silently schedules itself. Stop when done, blocked by required input, explicitly stopped, or at agreed cost/time limits. Report remaining work honestly.

## Skill resolution

Users invoke `/poteto-mode <task>`, `/poteto-help`, or another `/skill-name` command. Load bundled skills using the native skill tool by exact name, such as `skill({ name: "how" })`. Skills marked explicit-only are deliberately absent from automatic selection guidance but remain loadable by exact name when requested or needed by an explicitly selected workflow. Read only relevant principles and playbooks.

From this reference, sibling entrypoints are `../../<skill-name>/SKILL.md`; from a skill entrypoint they are `../<skill-name>/SKILL.md`. Resolve all references relative to the installed skill, not the working directory. Former-host sidecars and manifests are archival metadata, not OpenCode registration. Change the source distribution and reinstall rather than silently editing installed copies. Use setup-pstack for preferences and poteto-help for workflow selection.
