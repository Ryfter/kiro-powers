# Ryfter Kiro Powers

A collection of [Kiro](https://kiro.dev) powers. Each power adds specialized
context and tools to the Kiro agent on demand.

Each top-level folder is a self-contained power (a `plugin.json` manifest, one
or more skills, and an optional `mcp.json`). Install a power by pointing Kiro at
its subfolder.

## Available powers

### google-workspace-access
Read and search Google Drive, and read Google Docs, Sheets, and Slides directly
from Kiro. Leans toward lightweight text formats (Docs → markdown, Sheets → CSV,
Slides → outline) over binary. Can also locate and download Google Vids files.
Runs a self-hosted Google Workspace MCP server locally; your Google identity and
tokens stay on your machine.

- Folder: [`google-workspace-access/`](google-workspace-access/)
- MCP server: [`@piotr-agier/google-drive-mcp`](https://github.com/piotr-agier/google-drive-mcp) (stdio, local)
- Setup and sharing: see the power's [README](google-workspace-access/README.md)
  and [SHARING.md](google-workspace-access/SHARING.md)

### matt-pocock-skills
Matt Pocock's engineering and productivity agent skills, **repackaged unchanged**
for Kiro. Alignment/"grilling", TDD, code review, debugging, codebase design,
domain modeling, specs, and tickets. This power is **100% Matt Pocock's work**;
Ryfter only brings it into Kiro.

- Folder: [`matt-pocock-skills/`](matt-pocock-skills/)
- Source: [github.com/mattpocock/skills](https://github.com/mattpocock/skills) (MIT)
- What is / is not synced: see the power's [README](matt-pocock-skills/README.md)

### superpowers
Jesse Vincent's Superpowers agent skills, **repackaged unchanged** for Kiro. A
complete development methodology: brainstorming, writing/executing plans, TDD,
systematic debugging, code review, git worktrees, subagent-driven development.
This power is **100% the Superpowers authors' work**; Ryfter only brings it into
Kiro.

- Folder: [`superpowers/`](superpowers/)
- Source: [github.com/obra/superpowers](https://github.com/obra/superpowers) (MIT)
- What is / is not synced: see the power's [README](superpowers/README.md)

## Overlap between matt-pocock-skills and superpowers

Both skill collections are built on the same engineering philosophy — align
before coding, test-first (red-green-refactor), small steps, systematic over
ad-hoc. So they overlap heavily in the **core loop** and are kept as **separate
powers** for clean per-author attribution. You can install one or both.

**The shared backbone (roughly the same job in each):**

| Concern | matt-pocock-skills | superpowers |
|---|---|---|
| Align before building | `grill-me`, `grilling`, `grill-with-docs` | `brainstorming` |
| Turn intent into a plan/spec | `to-spec`, `to-tickets`, `wayfinder` | `writing-plans` |
| Execute the plan | `implement` | `executing-plans`, `subagent-driven-development` |
| Test-driven development | `tdd` | `test-driven-development` |
| Debugging discipline | `diagnosing-bugs` | `systematic-debugging` |
| Code review | `code-review` | `requesting-code-review`, `receiving-code-review` |
| Writing skills/docs for agents | `writing-for-agents` | `writing-skills` |

Even where names match, the **instructions differ**. For example, Matt's `tdd`
is a reference for the whole loop (what a good test is, mocking, anti-patterns),
while Superpowers' `test-driven-development` is a strict "watch it fail first"
gate. Matt's `code-review` runs two parallel sub-agents (standards vs. spec);
Superpowers' `requesting-code-review` dispatches a reviewer at mandatory
checkpoints. Keeping both gives you two takes on the same discipline.

**Where each is distinctive:**

- **matt-pocock-skills** goes deeper on **software design quality**
  (`codebase-design`, `domain-modeling`, `improve-codebase-architecture`) and
  adds **productivity/meta** tools (`prototype`, `research`, `wizard`, `triage`,
  `handoff`, `teach`, `to-questionnaire`, `wait-what`). It is a composable
  toolkit.
- **superpowers** is a tighter, more **prescriptive end-to-end methodology**,
  stronger on **git/branch lifecycle** (`using-git-worktrees`,
  `finishing-a-development-branch`) and **subagent orchestration**
  (`dispatching-parallel-agents`, `subagent-driven-development`).

**Which to reach for:** want a full, opinionated pipeline? Start with
**superpowers**. Want composable pieces plus design-quality and productivity
tooling? Start with **matt-pocock-skills**. Installing both is fine — just be
aware the core loop is covered twice, so pick your preferred version of TDD,
review, and alignment.

## Keeping the skills current

`matt-pocock-skills` and `superpowers` are **vendored** (copied) from their
upstream repos, not forked. A weekly GitHub Actions workflow
([`.github/workflows/sync-upstream-skills.yml`](.github/workflows/sync-upstream-skills.yml))
re-runs [`scripts/sync-upstream.sh`](scripts/sync-upstream.sh) and opens a pull
request whenever upstream changes, so upstream updates are reviewed before going
live. Each power's `UPSTREAM.txt` records the exact synced commit.

## Installing a power

**From GitHub (recommended):**
1. In Kiro, open the **Powers** UI.
2. Choose **Add Custom Power > GitHub / URL**.
3. Paste `https://github.com/Ryfter/kiro-powers`.
4. Select the power's subfolder if prompted, then **Add**.

**From a local clone:**
```bash
git clone https://github.com/Ryfter/kiro-powers.git
```
Then in Kiro: **Add Custom Power > Local Directory** and point at the power's
subfolder (for example `kiro-powers/google-workspace-access`).

## License

MIT — see [LICENSE](LICENSE). Individual powers may bundle or reference
third-party MCP servers under their own licenses; see each power's README.
