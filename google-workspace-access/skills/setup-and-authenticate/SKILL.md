---
name: "setup-and-authenticate"
description: "Set up Google Cloud OAuth credentials and authenticate the Google Workspace MCP server so Kiro can read Drive, Docs, Sheets, and Slides. Use when first installing this power, when tool calls fail with authentication or permission errors, or when switching Google accounts."
license: "MIT"
compatibility: "Requires Node.js 18+ and npx. Works with Kiro on Windows, macOS, and Linux."
metadata:
  author: "krank"
  version: "1.0.0"
---

# Set Up and Authenticate Google Workspace Access

## Overview

This power connects Kiro to Google Drive, Docs, Sheets, and Slides through a
self-hosted MCP server ([`@piotr-agier/google-drive-mcp`](https://github.com/piotr-agier/google-drive-mcp)).
The server runs locally over stdio and holds its own OAuth credentials and
token, so nothing is sent to a third party — your Google identity and refresh
token stay on your machine.

This skill covers the one-time setup: creating a Google Cloud project, enabling
the APIs, creating an OAuth client, and completing the browser consent flow.
Once done, the read skill (`read-workspace`) can search and read your content.

## Prerequisites Checklist

- [ ] Node.js 18 or newer installed (`node --version`)
- [ ] `npx` available (ships with Node.js)
- [ ] A Google account with access to the Drive/Docs/Sheets/Slides you want to read
- [ ] Ability to create a project in the [Google Cloud Console](https://console.cloud.google.com/)

## Step-by-Step Guide

### 1. Create a Google Cloud project

1. Open the [Google Cloud Console](https://console.cloud.google.com/).
2. Click the project selector at the top, then **New Project**.
3. Name it something like `kiro-workspace-access` and click **Create**.
4. Make sure the new project is selected before continuing.

### 2. Enable the required APIs

In your project, enable these APIs (search each by name in the console, or use
the links):

- [Google Drive API](https://console.cloud.google.com/apis/library/drive.googleapis.com)
- [Google Docs API](https://console.cloud.google.com/apis/library/docs.googleapis.com)
- [Google Sheets API](https://console.cloud.google.com/apis/library/sheets.googleapis.com)
- [Google Slides API](https://console.cloud.google.com/apis/library/slides.googleapis.com)

Reading Google Docs, Sheets, and Slides all still require the Drive API too,
so enable all four.

### 3. Configure the OAuth consent screen

1. Go to **APIs & Services > OAuth consent screen** (or **Google Auth Platform > Branding**).
2. If prompted to get started, set:
   - **App name**: `Kiro Workspace Access`
   - **User support email**: your email
   - **Audience / User type**: choose **Internal** if available; otherwise **External**.
3. If you chose **External**, add your own Google account under **Test users**.
   While the app is in "testing," only listed test users can authenticate.

#### Scopes (read-only recommended)

Under **Data Access > Add or Remove Scopes**, add the read scopes you need.
For read-only access to everything this power targets, add:

```
https://www.googleapis.com/auth/drive.readonly
https://www.googleapis.com/auth/documents.readonly
https://www.googleapis.com/auth/spreadsheets.readonly
https://www.googleapis.com/auth/presentations.readonly
```

Use the narrowest scopes that cover your use. Add write scopes (for example
`documents`, `spreadsheets`, `presentations`, `drive.file`) only if you intend
to edit content, not just read it.

### 4. Create the OAuth client (Desktop app)

1. Go to **APIs & Services > Credentials > Create Credentials > OAuth client ID**.
2. Application type: **Desktop app**.
3. Name it (for example `kiro-desktop`) and click **Create**.
4. Click **Download JSON** and save the file. The MCP server looks for it at:

   - **macOS / Linux**: `~/.config/google-drive-mcp/gcp-oauth.keys.json`
   - **Windows**: `%USERPROFILE%\.config\google-drive-mcp\gcp-oauth.keys.json`
     (in PowerShell: `$env:USERPROFILE\.config\google-drive-mcp\gcp-oauth.keys.json`)

Create the `google-drive-mcp` folder if it does not exist. Save the downloaded
file there with the exact name `gcp-oauth.keys.json`.

### 5. Run the authentication flow

In a terminal, run the server's auth command. This opens a browser for Google
consent and caches a token locally.

```bash
npx -y @piotr-agier/google-drive-mcp auth
```

1. Sign in with the Google account whose files you want to read.
2. Grant the requested scopes.
3. On success, a token is stored at `~/.config/google-drive-mcp/tokens.json`
   (`%USERPROFILE%\.config\google-drive-mcp\tokens.json` on Windows).

You only do this once. The refresh token is reused on future runs.

### 6. Confirm the power is active in Kiro

The MCP server is already declared in this power's `mcp.json`. After installing
the power and reconnecting/restarting Kiro:

1. Ask Kiro: **"Run authGetStatus and tell me which Google account is active."**
2. A correct response naming your account confirms authentication worked.

If tools are not visible, reconnect the MCP server from Kiro's MCP Server view
or restart Kiro.

## Common Workflows

### Workflow: Switch to a different Google account

**Goal:** Authenticate as a different identity.

1. Delete or rename the cached token: `~/.config/google-drive-mcp/tokens.json`.
2. Re-run `npx -y @piotr-agier/google-drive-mcp auth`.
3. Sign in with the other account.

### Workflow: Grant write access later

**Goal:** Move from read-only to editing.

1. Add the write scopes in **OAuth consent screen > Data Access**.
2. Delete `tokens.json` to force re-consent.
3. Re-run the `auth` command and approve the new scopes.

## Troubleshooting

### Error: "gcp-oauth.keys.json not found"
**Cause:** The OAuth client JSON is missing or in the wrong location.
**Solution:**
1. Confirm the file is at `~/.config/google-drive-mcp/gcp-oauth.keys.json`
   (`%USERPROFILE%\.config\google-drive-mcp\` on Windows).
2. Confirm the filename is exactly `gcp-oauth.keys.json`.
3. Re-download it from **Credentials** if needed.

### Error: "access_denied" or "app is blocked" during consent
**Cause:** External app in testing with your account not listed as a test user.
**Solution:**
1. Go to **OAuth consent screen > Test users** and add your Google account.
2. Retry the auth command.

### Error: "insufficient permission" / 403 on a read call
**Cause:** The token was granted narrower scopes than the tool needs.
**Solution:**
1. Add the missing read scope in **Data Access**.
2. Delete `tokens.json` and re-run `auth` to re-consent.

### Tools do not appear in Kiro
**Cause:** MCP server not connected after install.
**Solution:**
1. Open Kiro's MCP Server view and reconnect `google-drive`.
2. If still missing, restart Kiro and confirm `npx` runs (`npx --version`).

## Best Practices

- Prefer read-only scopes unless you specifically need to edit content.
- Never commit `gcp-oauth.keys.json` or `tokens.json` to source control.
- Keep the token file private; it grants access to your Google content.
- Re-run `auth` after changing scopes so the token reflects the new grant.
