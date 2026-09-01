# Installing this power

This power connects Kiro to Google Drive, Docs, Sheets, and Slides (and can
locate/download Google Vids files). It runs a local MCP server and uses your
own Google identity — no credentials are shared or stored in this repo.

## Prerequisites

- **Kiro** with Powers support.
- **Node.js 18+** and `npx` (check: `node --version`). The MCP server runs via `npx`.
- A **Google account** with access to the files you want to read.

## Install in Kiro

### Option A — from GitHub (recommended)

1. In Kiro, open the **Powers** UI.
2. Choose **Add Custom Power**.
3. Select **GitHub / URL** and paste the repo URL:
   `https://github.com/Ryfter/kiro-powers`
   This power lives in the `google-workspace-access/` subfolder of that repo.
4. Click **Add**, then reconnect or restart Kiro if prompted.

### Option B — from a local clone

1. Clone the repo:
   ```bash
   git clone https://github.com/Ryfter/kiro-powers.git
   ```
2. In Kiro, open the **Powers** UI.
3. Choose **Add Custom Power > Local Directory**.
4. Point it at `kiro-powers/google-workspace-access` and click **Add**.

## One-time Google setup (each person does this once)

Every user authenticates with their **own** Google identity. Nothing is shared.

1. Follow the **setup-and-authenticate** skill in this power. In short:
   - Create (or reuse) a Google Cloud project.
   - Enable the Drive, Docs, Sheets, and Slides APIs.
   - Configure the OAuth consent screen with **read-only** scopes.
   - Create a **Desktop app** OAuth client and download the JSON.
   - Save it as `~/.config/google-drive-mcp/gcp-oauth.keys.json`
     (`%USERPROFILE%\.config\google-drive-mcp\gcp-oauth.keys.json` on Windows).
2. Authenticate:
   ```bash
   npx -y @piotr-agier/google-drive-mcp auth
   ```
3. In Kiro, confirm it works:
   > Run `authGetStatus` and tell me which Google account is active.

### Sharing one Google Cloud project (optional)

To avoid each colleague creating a project, one person can create a single
Google Cloud project and add the others as **test users** on the OAuth consent
screen. Each colleague still creates their own OAuth client (or you share the
Desktop-app client JSON) and runs the `auth` step to sign in as themselves.
The token is per-user and stays on each machine.

## What is safe to share

- **Safe (in this repo):** `plugin.json`, `mcp.json`, skills, README, this file.
  None contain secrets.
- **Never share / never commit:** `gcp-oauth.keys.json` and `tokens.json`.
  These live under `~/.config/google-drive-mcp/` on each machine, not in this repo.

## Updating

- **GitHub install:** in the Powers UI, use **Check for Updates** then
  **Update Power**.
- **Local clone:** `git pull`, then **Check for Updates > Update Power** in Kiro.

## Troubleshooting

See the **setup-and-authenticate** skill for auth/scope errors and the
**read-workspace** skill for read/export issues.
