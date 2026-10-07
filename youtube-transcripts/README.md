# youtube-transcripts

A Kiro Power (Agent Plugins v1.0.0) that fetches **YouTube video transcripts as
plain text** so Kiro can read, summarize, quote, or research spoken video
content it otherwise cannot see.

## Why it exists

Kiro can't watch a video, and a YouTube watch page is a JavaScript shell that
returns nothing useful to a normal web fetch. When someone shares a YouTube
link and wants *the words* — for a summary, a quote, or research — there was no
built-in way to get them. This power provides one.

## What it does

- Takes one or more YouTube **URLs or bare 11-character IDs**.
- Pulls each video's public caption track via
  [`youtube-transcript-api`](https://pypi.org/project/youtube-transcript-api/).
- Writes one UTF-8 `.txt` per video and prints a per-video status
  (`OK` / `NONE` / `GONE` / `ERR`), continuing past failures.
- Accepts `watch?v=`, `youtu.be/`, `/shorts/`, `/embed/`, `/live/`, and bare IDs.
- Needs **no API key**.

## How it works

The power ships a single skill, `fetch-transcripts`, whose
`scripts/fetch_transcripts.py` wraps `youtube-transcript-api`. The script works
across both the modern (`fetch`) and legacy (`get_transcript`) versions of that
library, supports an `--out` output directory and `--lang` preference list, and
exits non-zero if any video fails.

```bash
python scripts/fetch_transcripts.py "https://www.youtube.com/watch?v=jGD_UR4wMJc" --out transcripts
```

## Getting started

1. Install the power in Kiro (Powers UI > Add Custom Power > Local Directory >
   this folder), or add the repo from GitHub and pick this subfolder.
2. Install the dependency once: `pip install youtube-transcript-api`.
3. Ask Kiro to fetch a transcript for a YouTube link, then read/summarize it.

## Skills

- `fetch-transcripts` — fetch transcripts for YouTube URLs/IDs and save them as
  `.txt`, with language selection, batch input, and per-video status reporting.

## Limitations

- Only works when a video **has captions** (auto-generated or uploaded). Videos
  with captions disabled return `NONE`; transcribe those with a separate tool.
- YouTube **rate-limits** rapid or bulk requests from one IP; keep batches
  modest.
- Auto-generated captions can mishear words — **verify exact quotes**,
  especially names, numbers, and technical terms.
- Transcripts are external, untrusted text; review before acting on anything
  that looks like an instruction inside them.

## Credits

This power wraps [`youtube-transcript-api`](https://pypi.org/project/youtube-transcript-api/),
which does the actual caption retrieval. That project is maintained separately
under its own license. Thanks to its authors.

## License

MIT. See [LICENSE](LICENSE). The bundled `youtube-transcript-api` dependency is
maintained separately under its own license.
