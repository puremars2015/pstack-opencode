# Pstack for OpenCode

OpenCode adaptation of puremars2015/pstack-codex (0.1.2), retaining 55 skills,
24 engineering principles, and 23 playbooks. This is a native skills package,
not an executable JavaScript plugin or MCP server. No API key is required by
the package. Model calls use your existing OpenCode account and settings.

## Installation

Download this repository:

```sh
git clone https://github.com/puremars2015/pstack-opencode.git
cd pstack-opencode
python scripts/install_opencode.py
```

From this directory, run `python scripts/install_opencode.py` to install all
skills into `~/.config/opencode/skills/`. The installer refuses existing names
instead of overwriting unrelated skills. It does not modify opencode.json,
providers, permissions, or model settings. Quit and restart OpenCode afterward.

For project scope, replace `<project>` with the project path:

```sh
python scripts/install_opencode.py --destination "<project>/.opencode/skills"
```

Keep the entire skill tree, including references, playbooks, and scripts.

Requires an OpenCode release supporting `metadata["opencode/slash"]` and
`metadata["opencode/autoinvoke"]`. Verified locally with OpenCode 1.18.23.
The 54 originally explicit-only skills remain explicit-only; setup-pstack
retains its original automatic-discovery behavior. All 55 expose slash commands.

## Usage

```text
/poteto-help
/poteto-mode Fix this bug and verify the regression
/how Explain this module without modifying files
/interrogate Review the implementation for correctness risks
/tdd Implement this change with a regression test
/setup-pstack
```

You can also ask OpenCode to load a skill by its exact name. The router loads
only the playbooks and principles relevant to the task. Slash commands execute
in the current chat; this package does not force a separate agent or model.

## Preferences and Limits

Optional workflow preferences use project `.agents/pstack.json` first, otherwise
`~/.config/opencode/pstack/config.json`. They are not merged. No preferences
file is required or created at installation. Defaults inherit the current model
and compare two candidates. Model overrides do not register OpenCode agents.

Delegation uses available Task agents; absent delegation falls back to disclosed
sequential passes. Browser verification, GitHub operations, and formal proof
require actual host tools. No background scheduler, automatic publication,
external model service, or bundled skill-creator is provided.

## Validation

```text
python -m pip install -r scripts/requirements-dev.txt
python scripts/validate_opencode.py
opencode debug skill
```

The authoring validator requires `scripts/requirements-dev.txt`; normal skill
usage and the installer have no third-party Python dependencies. Structural
validation is not a behavioral test of all workflows or models.

## Provenance

See OPENCODE.json for the source revision and adaptation details. The original
Codex README is retained as README.codex.md, and original Codex manifests and
sidecars are inert archival metadata. Do not add plugin.json to OpenCode's
`plugin` list. MIT license and upstream copyright are preserved in LICENSE.
This adaptation does not imply upstream authorship or endorsement.
