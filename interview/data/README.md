# Interview Data

All data used to compile `interview/questions.md` and other interview guides. Every question is traceable back to a real source.

## Structure

```
data/
├── sources/                  # Organized inventory of all source links
│   ├── interview-stories.md       # First-person interview experiences (Medium, dev.to, blogs)
│   ├── discussion-threads.md      # 58 Reddit + 46 HN interview discussion threads
│   ├── blogs-and-guides.md        # Interview prep articles and guides
│   ├── github-repos.md            # 65+ take-home assignments from GitHub
│   ├── interview-prep-repos.md    # GitHub interview prep repositories
│   ├── community-links.md         # Community forums and subreddits
│   ├── all-links.md               # Complete link inventory (every URL we found)
│   ├── github-search-methodology.md  # How we searched GitHub for assignments
│   └── research-approach.md       # How we use our research tools (Arctic-Shift, Grok)
├── fetched/                  # Actually downloaded source content
│   ├── reddit-posts/              # 10 Reddit threads fetched via Arctic-Shift (.md + .json)
│   └── grok-responses/            # 8 Grok API search results with full citations (.json)
├── link-summaries/           # Verification and corroboration results
│   ├── techeon-corroboration-map.md   # 27 questions mapped to evidence (20 corroborated)
│   ├── agent-questions-research.md    # Link verification from other AI agents
│   ├── APPROACHES.md                  # How to fetch from each platform
│   ├── reddit-*.md, hn-*.md, etc.     # Platform-specific fetch results
│   └── blind-*.md, x-*.md             # TeamBlind and X/Twitter summaries
├── job-descriptions/         # 51 YAML job postings (AI engineer roles)
└── research-exports/         # Raw AI research session exports (ChatGPT, Gemini, Grok)
```

## Key source files

| File | What it contains |
|------|-----------------|
| `sources/discussion-threads.md` | 104 Reddit + HN threads with direct interview experiences. URL, score, one-line description each. |
| `sources/interview-stories.md` | First-person blog posts from engineers who got hired (Medium, dev.to). Summaries + links. |
| `sources/github-repos.md` | 65+ real take-home assignments from GitHub. Company name, date, description, link. |
| `sources/blogs-and-guides.md` | Interview prep articles, RAG guides, industry analysis. Tables with links. |
| `link-summaries/techeon-corroboration-map.md` | Maps 27 agentic AI questions to corroborating Reddit evidence. 20 corroborated, 6 single-sourced. |

## How to reproduce

### Fetch Reddit threads (free, no auth)

Uses Arctic-Shift API. Run from `interview/_internal/`:

```bash
cd interview/_internal

# Single thread
uv run python fetch_reddit.py 'https://www.reddit.com/r/ExperiencedDevs/comments/1r78ipa/...'

# Batch
uv run python fetch_reddit.py --batch ../data/reddit-urls-to-fetch.txt
```

Output: `.md` + `.json` saved to `data/fetched/reddit-posts/`.

### Search with Grok (paid, needs x.ai API key)

```bash
cd interview/_internal

uv run python xai_search.py \
  'Natural language prompt. Tell it which sources to check (Reddit, HN, X, Medium).
   Ask for URLs, exact quotes. Tell it to be honest when nothing is found.' \
  --tools web_search,x_search \
  --system 'Research assistant role and quality criteria' \
  --label 'descriptive-name'
```

Output: full JSON saved to `data/fetched/grok-responses/`.

### Web pages behind firewalls

1. Jina Reader: `https://r.jina.ai/<URL>`
2. Google Cache: `https://webcache.googleusercontent.com/search?q=cache:<URL>`
3. Wayback Machine: `https://web.archive.org/web/<URL>`

### Hacker News

Direct JSON API: `https://hacker-news.firebaseio.com/v0/item/<ID>.json`

## All footnote sources

Defined at the bottom of `interview/questions.md` — 50+ sources including YouTube, Medium, Reddit, HN, interview prep sites, GitHub repos, and datainterview.com.
