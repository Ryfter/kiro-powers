# matt-pocock-skills

> **This is 100% the work of Matt Pocock.** Every skill in this power was
> written by Matt Pocock and lives at
> [github.com/mattpocock/skills](https://github.com/mattpocock/skills).
> This power does **not** add, rewrite, or improve any of that work — it only
> **repackages it, unchanged, so it can be installed as a Kiro power.**
> All credit goes to Matt Pocock. If you find these skills valuable, follow and
> support the original author.

A Kiro Power that vendors Matt Pocock's engineering and productivity agent
skills so Kiro can use them. The skill files are copied verbatim from upstream;
attribution and license are preserved.

## Attribution

- **Author:** Matt Pocock — <https://github.com/mattpocock>
- **Source repo:** <https://github.com/mattpocock/skills>
- **License:** MIT (see [UPSTREAM-LICENSE](UPSTREAM-LICENSE))
- **Synced commit:** recorded in [UPSTREAM.txt](UPSTREAM.txt)

## What is synced

The polished, advertised skill sets from upstream:

- **Engineering** (`skills/engineering/`): `ask-matt`, `code-review`,
  `codebase-design`, `diagnosing-bugs`, `domain-modeling`, `grill-with-docs`,
  `implement`, `improve-codebase-architecture`, `prototype`, `research`,
  `resolving-merge-conflicts`, `setup-matt-pocock-skills`, `tdd`, `to-spec`,
  `to-tickets`, `triage`, `wayfinder`, `wizard`
- **Productivity** (`skills/productivity/`): `grill-me`, `grilling`, `handoff`,
  `teach`, `to-questionnaire`, `wait-what`, `writing-for-agents`

Upstream nests these under category folders (`skills/engineering/…`,
`skills/productivity/…`). The Agent Plugins spec only recognizes skills one
level below `skills/`, so this power **flattens** them to `skills/<name>/`.
That is the only structural change; file contents are untouched.

## What is NOT synced (and why)

- **`skills/in-progress/`** — Matt marks these as unfinished/experimental and
  does not advertise them in the upstream README. They change frequently, so
  syncing them would churn the weekly update PR and could ship half-baked
  behavior. Excluded until they graduate upstream.
- **`skills/misc/`** — These are Claude-Code-specific setup helpers
  (`git-guardrails-claude-code`, `setup-pre-commit`, `migrate-to-shoehorn`,
  `scaffold-exercises`) that target Claude Code's environment rather than Kiro,
  so they would not work as-is here.
- **Repo scaffolding** — `.claude-plugin/`, `package.json`, changelog, and
  other Claude-Code marketplace machinery are not skills and are not needed to
  run the skills in Kiro.

If you want any excluded skill, take it directly from
[the upstream repo](https://github.com/mattpocock/skills).

## Some skills expect a setup step

Several engineering skills reference `/setup-matt-pocock-skills` (issue tracker,
triage labels, docs location). That skill is included here. Run it once per repo
before leaning on the issue-tracker-aware skills. Some skills also reference a
project `CONTEXT.md` (a shared-language doc) — optional but recommended.

## Overlap with the `superpowers` power

This power and the sibling `superpowers` power share a methodology backbone
(align → plan → TDD → review → debug). They are kept separate for clean
per-author attribution. See the repo root
[README](../README.md#overlap-between-matt-pocock-skills-and-superpowers) for a
guide on which to reach for.

## Updating

Skills are refreshed from upstream by a weekly GitHub Actions workflow
([`.github/workflows/sync-upstream-skills.yml`](../.github/workflows/sync-upstream-skills.yml)),
which opens a pull request when upstream changes. You can also run
[`scripts/sync-upstream.sh`](../scripts/sync-upstream.sh) locally.

## License

The skills are MIT-licensed by Matt Pocock; see [UPSTREAM-LICENSE](UPSTREAM-LICENSE)
and [NOTICE](NOTICE). The packaging around them (this README, `plugin.json`) is
provided under the repository's MIT license.
