---
name: "google-workspace-access"
description: "Read and search your Google Workspace directly from Kiro through a self-hosted, local MCP server. Search and browse Google Drive, read Google Docs (exported cleanly to markdown), pull Google Sheets cell values, and read Google Slides text and layout. It leans toward lightweight text formats over binary: Docs become .md, Sheets become .csv, Slides become a markdown outline, so you spend fewer tokens and get diff-friendly output; binary is used only when no text form exists or you ask for the original. Can also locate and download Google Vids files (Vids has no content API, so deeper Vid contents are not extractable). Runs the @piotr-agier/google-drive-mcp server locally over stdio; your Google identity, OAuth credentials, and token stay on your machine. Prefers read-only scopes by default."
keywords: google-drive, google-docs, google-sheets, google-slides, workspace, mcp, markdown-export
---

# google-workspace-access

Read and search Google Drive, Docs, Sheets, and Slides directly from Kiro
through a self-hosted, local Google Workspace MCP server. Leans toward
text-first output (Docs → markdown, Sheets → CSV, Slides → outline) and can
locate/download Google Vids files.

- **MCP server:** [`@piotr-agier/google-drive-mcp`](https://github.com/piotr-agier/google-drive-mcp) (stdio, local)
- **Setup & sharing:** see [README.md](README.md), [SHARING.md](SHARING.md), and the [setup-and-authenticate](skills/setup-and-authenticate/SKILL.md) skill
- **License:** MIT

Your Google identity, OAuth credentials, and token stay on your machine.
