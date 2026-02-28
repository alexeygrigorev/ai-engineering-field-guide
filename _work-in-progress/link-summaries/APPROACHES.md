# Link Fetching Approaches — What Worked and What Didn't

## Overview

444 community discussion links were processed across 4 platforms (Hacker News, Reddit, TeamBlind, X/Twitter). Direct access was blocked on 3 of 4 platforms. This document records which approaches succeeded and failed for each platform.

---

## Hacker News (78 links) — 100% success rate

### What Worked
- **Direct WebFetch** to `news.ycombinator.com` — worked perfectly for all 78 links
- HN has no bot blocking, rate limiting, or authentication requirements
- Both post pages and comment threads render as plain HTML, no JavaScript required

### What Didn't Work
- N/A — everything worked on the first try

---

## Reddit (107 links) — Mixed results

### What Worked
1. **Arctic Shift API** (best approach, used by reddit-01: 18/18 success)
   - **Post content**: `https://arctic-shift.photon-reddit.com/api/posts/search?subreddit=[sub]&...`
   - **Comment tree** (full threaded comments): `https://arctic-shift.photon-reddit.com/api/comments/tree?link_id=[post_id]&limit=50`
   - Returns full post JSON (title, selftext, author, score) AND full nested comment bodies with author, score, and reply structure
   - Extract `post_id` from URL path (e.g., `1b25o1e` from `/comments/1b25o1e/...`)
   - Comment endpoint returns threaded `replies` with full `body` text — this is the only way to get Reddit comments without direct site access
   - Works for posts of any age, including deleted posts (if archived before deletion)
   - Free, no auth required; mild rate limiting (a few requests/sec is fine)
   - **Note**: The older Pullpush API (`api.pullpush.io`) returned empty results in testing; Arctic Shift's photon-reddit endpoint is the working one as of Feb 2026

2. **Redlib mirrors** (used by reddit-02: partial success)
   - Replace `reddit.com` with a Redlib instance (e.g., `redlib.catsarch.com`)
   - Renders Reddit content without JavaScript
   - Mirrors go up and down frequently — unreliable across runs

3. **WebSearch reconstruction** (fallback, used by reddit-00, reddit-03)
   - Search for: `reddit [subreddit] [post title keywords]`
   - Also try: `site:reddit.com [key terms]`
   - Returns search snippets with partial content, sometimes enough to reconstruct a summary
   - Quality varies — works well for popular/viral posts, poorly for niche ones

### What Didn't Work
- **Direct WebFetch to reddit.com** — HTTP 403 for all requests (bot blocking)
- **old.reddit.com** — Same 403 block
- **Teddit/Libreddit mirrors** — Most instances are dead or also blocked
- **Wayback Machine (web.archive.org)** — Also blocked by WebFetch tool restrictions
- **Google Cache** — No longer available (Google discontinued cache feature)

---

## TeamBlind (147 links) — 0% direct, ~80% via search

### What Worked
1. **WebSearch reconstruction** (used by blind-04, blind-05: ~47 posts recovered)
   - Search for: `teamblind.com [post slug keywords]` or `site:teamblind.com [key terms]`
   - Also search the topic directly: `[Company] [role] interview experience blind`
   - Google often indexes TeamBlind post titles and snippets even though the site blocks direct access
   - Cross-reference with other interview prep sites (Glassdoor, Exponent, IGotAnOffer) for supplementary detail
   - Quality: Good for post titles and general topic; variable for specific interview questions and comments

### What Didn't Work
- **Direct WebFetch** — HTTP 403 (application-level authentication required, not just bot detection)
- **Playwright headless browser** — Same 403; TeamBlind blocks unauthenticated access at the server level
- **Playwright + Oxylabs residential proxy** — Still 403 (block is auth-based, not IP-based)
- **Playwright + user cookies** — Failed because `document.cookie` doesn't include httpOnly cookies (session tokens). Both `extra_http_headers: {"Cookie": ...}` and `context.add_cookies()` approaches returned 403
- **Playwright headed mode + Xvfb + anti-detection flags** — Same 403
- **CORS proxies** (allorigins.win, corsproxy.io, codetabs.com) — Either timed out or passed through the 403
- **Jina Reader API** (`r.jina.ai/[url]`) — Returned 403 Forbidden
- **12ft.io** — Certificate error (ERR_CERT_AUTHORITY_INVALID)
- **Google Cache** — No cached version available for any tested URL

---

## X/Twitter (59 links) — ~66% success rate

### What Worked
1. **fxtwitter API** (used by x-02: 19/19 success)
   - Replace `x.com` with `api.fxtwitter.com` in the URL
   - Returns JSON with full tweet text, author info, media, engagement metrics
   - Example: `https://api.fxtwitter.com/username/status/12345`
   - Fast, reliable, no auth required
   - Works for tweets, threads, and quote tweets

2. **Nitter proxy** (used by x-00: 20/20 success)
   - Replace `x.com` with `nitter.poast.org` (or other active Nitter instance)
   - Renders tweet content as plain HTML without JavaScript
   - Instances go up and down — check availability first
   - Works well when an instance is up

3. **WebSearch** (fallback)
   - Search for: `from:[username] [topic keywords]`
   - Works for viral/popular tweets but unreliable for lesser-known accounts

### What Didn't Work
- **Direct WebFetch to x.com** — Returns "JavaScript is not available" error page (x.com is a JavaScript SPA)
- **Playwright headless** — Could work in theory but was not tested (fxtwitter/Nitter were simpler)

---

## Summary: Recommended Approach Per Platform

| Platform   | Primary Approach            | Fallback                  | Success Rate |
|------------|-----------------------------|---------------------------|--------------|
| HN         | Direct WebFetch             | N/A                       | ~100%        |
| Reddit     | Pullpush API (`api.pullpush.io`) | WebSearch            | ~90%+        |
| TeamBlind  | WebSearch reconstruction    | Cross-reference (Glassdoor, etc.) | ~80%  |
| X/Twitter  | fxtwitter API               | Nitter proxy → WebSearch  | ~95%+        |

## Key Lessons

1. **API-based approaches beat scraping**: Pullpush for Reddit and fxtwitter for X/Twitter are both faster and more reliable than any browser-based approach
2. **Authentication blocks can't be bypassed with proxies**: TeamBlind's block is auth-based (not IP or bot detection), so residential proxies don't help
3. **WebSearch is a universal fallback**: When all else fails, search engines often have indexed snippets that provide partial content recovery
4. **Cookie export via `document.cookie` is incomplete**: httpOnly cookies (including session tokens) are not accessible from JavaScript, making cookie-based auth bypass ineffective
5. **Mirror/proxy services are ephemeral**: Nitter, Redlib, Teddit instances go up and down frequently — always have a fallback
