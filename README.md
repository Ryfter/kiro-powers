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
