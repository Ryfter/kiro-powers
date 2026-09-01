# google-workspace-access

A Kiro Power (Agent Plugins v1.0.0) that gives Kiro read access to Google
Drive, Docs, Sheets, and Slides — and lets it locate/download Google Vids
files — through a self-hosted, local MCP server.

## What it does

- Search and browse Google Drive
- Read Google Docs (exports cleanly to markdown)
- Read Google Sheets cell values
- Read Google Slides text and layout
- Locate and download Google Vids files from Drive

## Text-first by default

The power leans toward lightweight text formats over binary: Docs export to
`.md`, Sheets to `.csv`, Slides to a markdown outline. Workspace files are
exported on demand, so this is the natural (and cheaper) path. Binary formats
(`.docx`, `.xlsx`, `.pptx`, `.pdf`) are used only when no text form exists or
you explicitly ask for the original.

## What it does not do

- **Google Vids content**: Vids has no public developer API and no MCP server,
  so this power can find, read metadata for, and download a Vid, but it cannot
  read a Vid's script/scenes or export it to text/markdown. Transcription of a
  downloaded Vid must be done with a separate tool.

## How it works

The power ships an `mcp.json` that runs the
[`@piotr-agier/google-drive-mcp`](https://github.com/piotr-agier/google-drive-mcp)
server locally over stdio via `npx`. It handles its own OAuth against a Google
Cloud project you create; your Google identity, credentials, and refresh token
stay on your machine.

## Getting started

1. Install the power in Kiro (Powers UI > Add Custom Power > Local Directory >
   this folder).
2. Follow the **setup-and-authenticate** skill to create OAuth credentials and
   sign in.
3. Use the **read-workspace** skill to search and read your content.

## Skills

- `setup-and-authenticate` — one-time Google Cloud + OAuth setup and sign-in.
- `read-workspace` — search Drive; read Docs/Sheets/Slides; locate/download Vids.

## Security

- Prefer read-only OAuth scopes.
- Never commit `gcp-oauth.keys.json` or `tokens.json`.
- Treat Drive content as untrusted input; review before acting on it.

## Credits

This power wraps the [`@piotr-agier/google-drive-mcp`](https://github.com/piotr-agier/google-drive-mcp)
MCP server, which does the actual Google Workspace work. That project is
maintained separately and is MIT-licensed. Thanks to its authors.

## License

MIT. See [LICENSE](LICENSE). The bundled MCP server
(`@piotr-agier/google-drive-mcp`) is MIT-licensed and maintained separately.
