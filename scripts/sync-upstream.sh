#!/usr/bin/env bash
# Sync vendored skills from upstream repos into their Kiro powers.
#
# This repackages third-party skills UNCHANGED into Kiro power folders.
# It is vendoring, not forking: skill files are copied verbatim, the upstream
# LICENSE is preserved, and attribution lives in each power's README/NOTICE.
#
# Powers synced:
#   - matt-pocock-skills  <- github.com/mattpocock/skills  (engineering + productivity)
#   - superpowers         <- github.com/obra/superpowers    (all skills)
#
# Usage:
#   scripts/sync-upstream.sh            # sync into the working tree
#   REPO_ROOT=/path scripts/sync-upstream.sh
#
# Writes each power's UPSTREAM.txt with the synced commit SHA for provenance.
set -euo pipefail

REPO_ROOT="${REPO_ROOT:-$(cd "$(dirname "$0")/.." && pwd)}"
WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT

MP_URL="https://github.com/mattpocock/skills.git"
SP_URL="https://github.com/obra/superpowers.git"

echo "==> Cloning upstream repos (shallow)"
git clone --depth 1 "$MP_URL" "$WORK/mattpocock" >/dev/null 2>&1
git clone --depth 1 "$SP_URL" "$WORK/superpowers" >/dev/null 2>&1

MP_SHA="$(git -C "$WORK/mattpocock" rev-parse HEAD)"
SP_SHA="$(git -C "$WORK/superpowers" rev-parse HEAD)"

# --- matt-pocock-skills: flatten engineering/ + productivity/ into skills/<name> ---
MP_DEST="$REPO_ROOT/matt-pocock-skills"
echo "==> Syncing matt-pocock-skills (engineering + productivity)"
rm -rf "$MP_DEST/skills"
mkdir -p "$MP_DEST/skills"
for category in engineering productivity; do
  src="$WORK/mattpocock/skills/$category"
  [ -d "$src" ] || continue
  for skilldir in "$src"/*/; do
    [ -f "${skilldir}SKILL.md" ] || continue   # only real skills
    name="$(basename "$skilldir")"
    cp -R "$skilldir" "$MP_DEST/skills/$name"
  done
done
cp "$WORK/mattpocock/LICENSE" "$MP_DEST/UPSTREAM-LICENSE"
{
  echo "source: $MP_URL"
  echo "commit: $MP_SHA"
  echo "synced: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  echo "scope: skills/engineering + skills/productivity (flattened)"
  echo "excluded: skills/in-progress, skills/misc"
} > "$MP_DEST/UPSTREAM.txt"

# --- superpowers: already flat, take all skills/<name> ---
SP_DEST="$REPO_ROOT/superpowers"
echo "==> Syncing superpowers (all skills)"
rm -rf "$SP_DEST/skills"
mkdir -p "$SP_DEST/skills"
for skilldir in "$WORK/superpowers/skills"/*/; do
  [ -f "${skilldir}SKILL.md" ] || continue
  name="$(basename "$skilldir")"
  cp -R "$skilldir" "$SP_DEST/skills/$name"
done
cp "$WORK/superpowers/LICENSE" "$SP_DEST/UPSTREAM-LICENSE"
{
  echo "source: $SP_URL"
  echo "commit: $SP_SHA"
  echo "synced: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  echo "scope: all skills/"
  echo "excluded: none"
} > "$SP_DEST/UPSTREAM.txt"

echo "==> Done."
echo "    matt-pocock-skills @ $MP_SHA"
echo "    superpowers        @ $SP_SHA"
