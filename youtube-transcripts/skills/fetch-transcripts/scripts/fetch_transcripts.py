"""Fetch YouTube transcripts for a list of video URLs/IDs and save them as text.

Usage:
    python fetch_transcripts.py <url_or_id> [<url_or_id> ...] [--out DIR] [--lang CODE ...]

Options:
    --out DIR        Directory to write transcripts into (default: ./transcripts)
    --lang CODE ...  Preferred transcript language codes, most-preferred first
                     (e.g. --lang en en-US). Falls back to any available track.

Behavior:
    - Accepts full watch URLs, youtu.be links, /shorts/ and /embed/ forms,
      and bare 11-character video IDs.
    - Writes one UTF-8 <video_id>.txt per video.
    - Reports OK / NONE (no captions) / GONE (unavailable) / ERR per video,
      and continues past failures.
    - Exit code is 0 if every video succeeded, 1 if any failed/skipped.

Dependency:
    pip install youtube-transcript-api
"""
import argparse
import re
import sys
from pathlib import Path

try:
    from youtube_transcript_api import YouTubeTranscriptApi
    from youtube_transcript_api._errors import (
        TranscriptsDisabled,
        NoTranscriptFound,
        VideoUnavailable,
    )
except ImportError:
    sys.exit(
        "Missing dependency 'youtube-transcript-api'.\n"
        "Install it with: pip install youtube-transcript-api"
    )

_ID_RE = re.compile(r"[A-Za-z0-9_-]{11}")
_URL_RE = re.compile(r"(?:v=|youtu\.be/|/shorts/|/embed/|/live/)([A-Za-z0-9_-]{11})")


def extract_id(url_or_id: str) -> str:
    """Return the 11-char video ID from a URL or bare ID, or raise ValueError."""
    s = url_or_id.strip()
    if _ID_RE.fullmatch(s):
        return s
    m = _URL_RE.search(s)
    if m:
        return m.group(1)
    raise ValueError(f"could not extract a video ID from: {url_or_id!r}")


def _snippets_to_text(snippets) -> str:
    lines = []
    for s in snippets:
        text = s.text if hasattr(s, "text") else s["text"]
        lines.append(text)
    return "\n".join(lines)


def fetch_one(video_id: str, languages=None) -> str:
    """Return transcript text for one video ID.

    Works across the modern (>=1.0, instance.fetch) and legacy
    (classmethod get_transcript) youtube-transcript-api interfaces.
    """
    api = YouTubeTranscriptApi()
    if hasattr(api, "fetch"):  # modern API
        if languages:
            fetched = api.fetch(video_id, languages=languages)
        else:
            fetched = api.fetch(video_id)
        snippets = getattr(fetched, "snippets", fetched)
        return _snippets_to_text(snippets)

    # legacy API
    if languages:
        data = YouTubeTranscriptApi.get_transcript(video_id, languages=languages)
    else:
        data = YouTubeTranscriptApi.get_transcript(video_id)
    return "\n".join(chunk["text"] for chunk in data)


def main(argv) -> int:
    parser = argparse.ArgumentParser(
        description="Fetch YouTube transcripts and save them as .txt files.",
    )
    parser.add_argument("videos", nargs="+", help="YouTube URLs or 11-char video IDs")
    parser.add_argument(
        "--out",
        default="transcripts",
        help="output directory (default: ./transcripts)",
    )
    parser.add_argument(
        "--lang",
        nargs="+",
        default=None,
        metavar="CODE",
        help="preferred language codes, most-preferred first (e.g. --lang en en-US)",
    )
    args = parser.parse_args(argv)

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    had_failure = False

    for raw in args.videos:
        try:
            vid = extract_id(raw)
        except ValueError as e:
            print(f"SKIP  {raw}: {e}")
            had_failure = True
            continue

        try:
            text = fetch_one(vid, languages=args.lang)
        except (TranscriptsDisabled, NoTranscriptFound):
            print(f"NONE  {vid}: no transcript/captions available")
            had_failure = True
            continue
        except VideoUnavailable:
            print(f"GONE  {vid}: video unavailable")
            had_failure = True
            continue
        except Exception as e:  # noqa: BLE001 - report and keep going
            print(f"ERR   {vid}: {type(e).__name__}: {e}")
            had_failure = True
            continue

        out_file = out_dir / f"{vid}.txt"
        out_file.write_text(text, encoding="utf-8")
        words = len(text.split())
        print(f"OK    {vid}: {words} words -> {out_file}")

    return 1 if had_failure else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
