# Research Approach: Verifying Interview Questions

How we verify that interview questions in `interview/questions.md` come from real interview experiences, not just AI-generated content.

## Problem

Many "interview question" articles (especially on Medium) may be AI-generated or speculative. We need to verify questions against real first-person accounts — people who actually sat in interviews or conducted them.

## Tools

### 1. Arctic-Shift API (Reddit data, free)

**Script:** `scripts/fetch_reddit.py`

Fetches Reddit posts + comments without authentication. We use this to get full text of interview discussion threads.

```bash
# Single post
uv run python scripts/fetch_reddit.py 'https://www.reddit.com/r/ExperiencedDevs/comments/1r78ipa/...'

# Batch mode
uv run python scripts/fetch_reddit.py --batch _work-in-progress/reddit-urls-to-fetch.txt
```

- API: `https://arctic-shift.photon-reddit.com/api`
- No auth needed, free
- Max 100 comments per request
- Saves both `.md` (readable) and `.json` (raw data) to `_work-in-progress/reddit-posts/`

### 2. x.ai Grok API with search tools (paid)

**Script:** `scripts/xai_search.py`

Uses Grok (`grok-4-1-fast-reasoning`) with built-in `web_search` and `x_search` tools to find and analyze sources across the web.

```bash
uv run python scripts/xai_search.py \
  'Your natural language research prompt here. Be specific about what you need.
   Tell it which sources to check: Reddit, HN, Twitter/X, Medium, blogs.
   Ask for exact quotes, URLs, and whether sources are first-person accounts.' \
  --tools web_search,x_search \
  --system 'System prompt defining the research assistant role and quality criteria' \
  --label 'descriptive-name-for-filing'
```

**Key usage notes:**
- Write a **natural language prompt**, not search-engine keywords. This is an AI agent, not a search engine.
- Explicitly tell it **which sources** to check (Reddit, HN, X/Twitter, Medium, specific subreddits)
- Tell it what **quality bar** you need (first-person accounts only, not tutorials)
- Ask it to be **honest** when it can't find something
- The `--label` flag names the output file in `_work-in-progress/grok-responses/`
- Full JSON response (with all tool calls, citations, timestamps) is always saved
- Cost is shown in stderr (typically $500-1000 per query with search tools)

**Example — good prompt:**
```
I am researching real AI engineer interview questions asked in 2025-2026.
I need to find first-person accounts where someone was asked about [TOPIC].

Search Reddit (r/ExperiencedDevs, r/MachineLearning, r/LangChain),
Hacker News, Twitter/X, Medium, and engineering blogs.

For each finding, tell me:
- Is it a real interview experience or just a discussion/tutorial?
- What company/role?
- Exact quote or context
- URL

Be honest if nothing matches.
```

**Example — bad prompt (search-engine style, don't do this):**
```
AI engineer interview "how do agents decide task is done" OR "termination" site:reddit.com
```

### 3. Manual verification

For links found by other AI agents (ChatGPT, Grok research), we verify each one:
- Fetch the URL directly or via Arctic-Shift
- Check if content matches the claimed description
- Flag fabricated/hallucinated links (common with AI research assistants)

Results tracked in `_work-in-progress/link-summaries/agent-questions-research.md`.

## Process

1. **Identify single-sourced questions** — find questions in `questions.md` with only one citation, especially from sources that may be AI-generated (e.g., `[^techeon]`)

2. **Search for corroboration** — use Grok + Arctic-Shift to find real interview experiences discussing the same topics

3. **Map corroboration** — document which questions have second sources in `_work-in-progress/link-summaries/techeon-corroboration-map.md`

4. **Add references** — update `questions.md` with new source citations using footnote format `[^source-name]`

5. **Discover new questions** — when fetching Reddit threads, look for interview questions not yet in our collection and add them

## File structure

```
_work-in-progress/
├── reddit-posts/              # Fetched Reddit threads (.md + .json)
├── reddit-urls-to-fetch.txt   # Batch URLs for fetch_reddit.py
├── grok-responses/            # Full Grok API responses with timestamps
├── link-summaries/
│   ├── agent-questions-research.md    # Link verification status
│   └── techeon-corroboration-map.md   # Question-to-evidence mapping
scripts/
├── fetch_reddit.py            # Arctic-Shift Reddit fetcher
└── xai_search.py              # Grok API search with web/x tools
```

## Citation format

In `questions.md`, each question has footnote citations:
```markdown
- How do you sandbox tool execution safely? [^techeon] [^reddit-expdevs-agentic]
```

Footnotes defined at the bottom:
```markdown
[^reddit-expdevs-agentic]: [Reddit - Agentic AI System Design Interview](https://reddit.com/...) (r/ExperiencedDevs, Feb 2026)
```
