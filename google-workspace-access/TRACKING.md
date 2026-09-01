# Tracking: revisit the official Google Workspace MCP server

## The decision (why stdio for now)

This power uses a **local stdio** MCP server
([`@piotr-agier/google-drive-mcp`](https://github.com/piotr-agier/google-drive-mcp))
instead of Google's **official remote** Workspace MCP servers
(`https://drivemcp.googleapis.com/mcp/v1` and the docs/sheets/slides
equivalents).

Reason: the official servers authenticate with an OAuth 2.0 authorization-code
flow where the **MCP host** performs a browser callback against a host-specific
redirect URI (for example Antigravity's `https://antigravity.google/oauth-callback`
or Claude's `https://claude.ai/api/mcp/auth_callback`). As of the last review,
**Kiro does not run that interactive remote-OAuth flow**, and the agent-plugins
`mcp.json` remote-server config allows only fixed headers with no secret
expansion — so there is no way to supply a live OAuth token. The stdio server
sidesteps this by doing its own OAuth once and caching the token locally, which
Kiro supports natively.

When Kiro gains support for remote OAuth MCP, prefer the official Google servers:
one server per product, maintained by Google, same permission model.

## The automated re-check

A scheduled GitHub Actions workflow
([`.github/workflows/check-kiro-mcp-oauth.yml`](../.github/workflows/check-kiro-mcp-oauth.yml))
runs **monthly** (and on demand) to nudge a human to re-evaluate this decision.

What it does each run:

- Fetches Kiro's MCP documentation and scans for OAuth-related mentions that
  might indicate remote-OAuth MCP support has landed.
- Reports the latest published version of the upstream stdio server package.
- Opens or updates a tracking **GitHub Issue** titled
  "Re-check: Kiro remote-OAuth MCP support" with the findings.

Important: the docs scan is a **heuristic hint, not a definitive answer**. There
is no official signal that says "Kiro now supports remote OAuth MCP." A human
reviews the issue and decides whether to switch this power to the official
endpoints.

### When the answer becomes "yes"

If Kiro supports remote OAuth MCP:

1. Add an alternative `mcp.json` (or document the swap) pointing at the official
   endpoints:
   - `https://drivemcp.googleapis.com/mcp/v1`
   - `https://docsmcp.googleapis.com/mcp/v1`
   - `https://sheetsmcp.googleapis.com/mcp/v1`
   - `https://slidesmcp.googleapis.com/mcp/v1`
2. Update `setup-and-authenticate` for the host-driven OAuth flow (Web-app OAuth
   client + redirect URI) instead of the local `npx ... auth` step.
3. Keep the stdio option documented as a fallback for hosts without remote OAuth.
4. Close the tracking issue with a note linking the change.

## Manual re-check

Run the workflow anytime from the repo's **Actions** tab
("Check Kiro remote-OAuth MCP support" > **Run workflow**), or review:

- Kiro MCP docs: https://kiro.dev/docs/mcp/
- Google Drive MCP setup: https://developers.google.com/workspace/drive/api/guides/configure-mcp-server
