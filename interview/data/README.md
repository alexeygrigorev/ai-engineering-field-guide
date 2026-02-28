# Interview Data

All data used to compile `interview/questions.md` and other interview guides.

## Structure

```
data/
├── job-descriptions/     # YAML job postings for AI engineer roles
├── reddit-posts/         # Fetched Reddit threads (.md readable + .json raw)
├── grok-responses/       # x.ai Grok API search results (full JSON)
├── link-summaries/       # Corroboration maps, link verification
├── raw/                  # Master link lists and scraped content
│   ├── all-links.md          # All links from every source file
│   ├── interview-threads.md  # 58 Reddit + 46 HN + Blind + X threads
│   └── community-links.md    # Community/forum links
├── research/             # Research session exports (Gemini, ChatGPT, Grok)
├── interviews/           # Interview trends analysis, take-home assignments
├── challenges/           # Interview stories, methodology notes
└── research-approach.md  # How we use our research tools
```

## Key link inventories

- **`raw/interview-threads.md`** — 58 Reddit + 46 HN threads with direct interview experiences. Each has URL, score, and one-line description.
- **`raw/all-links.md`** — Every link extracted from all research files, organized by source.
- **`link-summaries/techeon-corroboration-map.md`** — Maps 27 TechEon questions to corroborating Reddit evidence.
- **`link-summaries/agent-questions-research.md`** — Verification status of links from other AI agents.

## How to reproduce data fetching

### Reddit posts (free, no auth)

Uses Arctic-Shift API. Run from `interview/_internal/`:

```bash
cd interview/_internal

# Fetch a single thread
uv run python fetch_reddit.py 'https://www.reddit.com/r/ExperiencedDevs/comments/1r78ipa/...'

# Batch fetch from URL list
uv run python fetch_reddit.py --batch ../data/reddit-urls-to-fetch.txt
```

Output: `.md` (readable) + `.json` (raw) saved to `data/reddit-posts/`.

### Grok search (paid, needs x.ai API key)

Uses x.ai API with `web_search` + `x_search` tools. Set `XAI_API_KEY` in `.env` at repo root.

```bash
cd interview/_internal

uv run python xai_search.py \
  'Natural language research prompt. Tell it which sources to check
   (Reddit, HN, X/Twitter, Medium). Ask for URLs and exact quotes.
   Tell it to be honest when nothing is found.' \
  --tools web_search,x_search \
  --system 'Role description and quality criteria' \
  --label 'descriptive-name'
```

Output: full JSON response saved to `data/grok-responses/` with timestamp.

### Web pages

For pages that block direct access, try in order:
1. Jina Reader: `https://r.jina.ai/<URL>`
2. Google Cache: `https://webcache.googleusercontent.com/search?q=cache:<URL>`
3. Wayback Machine: `https://web.archive.org/web/<URL>`

### Hacker News

Direct JSON API (no auth): `https://hacker-news.firebaseio.com/v0/item/<ID>.json`

## Sources used in questions.md

All footnote sources are defined at the bottom of `interview/questions.md`. Currently 50+ sources including:
- YouTube interviews and mock sessions
- Medium/Substack blog posts (first-person experiences)
- Reddit threads (interview discussions and prep)
- Interview prep sites (igotanoffer, designgurus, interviewnode, etc.)
- GitHub repos (question banks, take-home assignments)
- Hacker News discussions
- datainterview.com (prep guides based on candidate reports)
