# superpowers

> **This is 100% the work of Jesse Vincent (and the team at Prime Radiant).**
> Every skill in this power was written by the Superpowers authors and lives at
> [github.com/obra/superpowers](https://github.com/obra/superpowers).
> This power does **not** add, rewrite, or improve any of that work — it only
> **repackages it, unchanged, so it can be installed as a Kiro power.**
> All credit goes to the original authors. If you find these skills valuable,
> follow and support them.

A Kiro Power that vendors the Superpowers agent skills so Kiro can use them. The
skill files are copied verbatim from upstream; attribution and license are
preserved.

## Attribution

- **Author:** Jesse Vincent / Prime Radiant — <https://github.com/obra>
- **Source repo:** <https://github.com/obra/superpowers>
- **License:** MIT (see [UPSTREAM-LICENSE](UPSTREAM-LICENSE))
- **Synced commit:** recorded in [UPSTREAM.txt](UPSTREAM.txt)

## What is synced

**All skills** from upstream `skills/` (they are polished and already laid out
one level below `skills/`, so they map directly with no restructuring):

`brainstorming`, `dispatching-parallel-agents`, `executing-plans`,
`finishing-a-development-branch`, `receiving-code-review`,
`requesting-code-review`, `subagent-driven-development`, `systematic-debugging`,
`test-driven-development`, `using-git-worktrees`, `using-superpowers`,
`verification-before-completion`, `writing-plans`, `writing-skills`

Each skill's supporting files (references, examples, scripts) are included as-is.

## What is NOT synced (and why)

- **Harness plugin scaffolding** — `.claude-plugin/`, `.codex-plugin/`,
  `.cursor-plugin/`, `.devin-plugin/`, `.hermes-plugin/`, `.kimi-plugin/`,
  `.opencode/`, `.pi/`, `gemini-extension.json`, etc. These wire Superpowers
  into specific coding agents (Claude Code, Codex, Cursor, …). Kiro loads skills
  from the `skills/` folder directly, so this machinery is not needed here.
- **`hooks/`** — Superpowers ships session-start hooks that auto-inject its
  bootstrap in supported harnesses. Kiro handles power/skill activation its own
  way, so these upstream hooks are not synced. (Kiro-native hooks, if desired,
  can be added separately.)
- **Evals / tests / release tooling** — `tests/`, `evals` harness references,
  `RELEASE-NOTES.md`, `package.json`, and version-bump config are development
  infrastructure for the upstream project, not runnable skills.
- **Telemetry** — The upstream `brainstorming` visual companion can load a
  remote logo for anonymous version telemetry. It is optional upstream and can
  be disabled with `SUPERPOWERS_DISABLE_TELEMETRY`. Review the skill if this
  matters to you.

If you want any excluded component, take it directly from
[the upstream repo](https://github.com/obra/superpowers).

## Note on the methodology

Superpowers is designed as an auto-triggering, end-to-end methodology in
harnesses that support its hooks. In Kiro, the **skills** are available on
demand, but the upstream session-start auto-activation is not part of this
power (see "What is NOT synced"). You reach for the skills as needed.

## Overlap with the `matt-pocock-skills` power

This power and the sibling `matt-pocock-skills` power share a methodology
backbone (align → plan → TDD → review → debug). They are kept separate for clean
per-author attribution. See the repo root
[README](../README.md#overlap-between-matt-pocock-skills-and-superpowers) for a
guide on which to reach for.

## Updating

Skills are refreshed from upstream by a weekly GitHub Actions workflow
([`.github/workflows/sync-upstream-skills.yml`](../.github/workflows/sync-upstream-skills.yml)),
which opens a pull request when upstream changes. You can also run
[`scripts/sync-upstream.sh`](../scripts/sync-upstream.sh) locally.

## License

The skills are MIT-licensed by their authors; see [UPSTREAM-LICENSE](UPSTREAM-LICENSE)
and [NOTICE](NOTICE). The packaging around them (this README, `plugin.json`) is
provided under the repository's MIT license.
