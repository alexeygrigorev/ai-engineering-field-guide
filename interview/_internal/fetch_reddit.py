#!/usr/bin/env python3
"""Fetch Reddit posts with all comments via Arctic-Shift API (free, no auth required)."""

import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import httpx

ARCTIC_SHIFT_BASE = "https://arctic-shift.photon-reddit.com/api"


def parse_reddit_url(url: str) -> tuple[str, str, str]:
    """Extract subreddit, post_id, slug from a Reddit URL."""
    parts = url.rstrip("/").split("/")
    try:
        idx = parts.index("comments")
        post_id = parts[idx + 1]
        slug = parts[idx + 2] if idx + 2 < len(parts) else "post"
    except (ValueError, IndexError):
        post_id = "unknown"
        slug = "post"
    try:
        r_idx = parts.index("r")
        subreddit = parts[r_idx + 1]
    except (ValueError, IndexError):
        subreddit = "unknown"
    return subreddit, post_id, slug


def fetch_post_by_title(subreddit: str, slug: str) -> dict | None:
    """Search for a post by subreddit and title keywords from the URL slug."""
    title_query = slug.replace("_", " ")
    resp = httpx.get(
        f"{ARCTIC_SHIFT_BASE}/posts/search",
        params={"subreddit": subreddit, "title": title_query, "limit": 1},
        timeout=30,
    )
    resp.raise_for_status()
    data = resp.json().get("data", [])
    return data[0] if data else None


def fetch_comments(post_id: str) -> list[dict]:
    """Fetch all comments for a post from Arctic-Shift."""
    resp = httpx.get(
        f"{ARCTIC_SHIFT_BASE}/comments/search",
        params={"link_id": post_id, "limit": 100},
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json().get("data", [])


def format_post(post: dict, comments: list[dict], url: str) -> str:
    """Format post and comments as readable markdown."""
    created = datetime.fromtimestamp(post.get("created_utc", 0), tz=timezone.utc)

    lines = [
        f"# {post.get('title', 'Untitled')}",
        "",
        f"- **Subreddit**: r/{post.get('subreddit', '?')}",
        f"- **Author**: u/{post.get('author', '?')}",
        f"- **Date**: {created.strftime('%Y-%m-%d %H:%M UTC')}",
        f"- **Score**: {post.get('score', '?')}",
        f"- **Comments**: {post.get('num_comments', '?')}",
        f"- **URL**: {url}",
        f"- **Post ID**: {post.get('id', '?')}",
        "",
        "## Post Body",
        "",
        post.get("selftext", "*[no text]*") or "*[no text]*",
        "",
    ]

    # Filter out AutoModerator
    real_comments = [c for c in comments if c.get("author") != "AutoModerator"]

    if real_comments:
        lines.append("## Comments")
        lines.append("")

        # Build parent lookup for threading
        by_id = {c["id"]: c for c in real_comments}
        top_level = []
        replies: dict[str, list[dict]] = {}
        for c in real_comments:
            parent = c.get("parent_id", "")
            if parent.startswith("t3_"):
                top_level.append(c)
            else:
                parent_id = parent.replace("t1_", "")
                replies.setdefault(parent_id, []).append(c)

        def render_comment(comment: dict, depth: int = 0):
            prefix = "> " * depth
            score = comment.get("score", "?")
            author = comment.get("author", "?")
            body = comment.get("body", "").strip()
            lines.append(f"{prefix}**u/{author}** (score: {score})")
            lines.append(f"{prefix}")
            for line in body.split("\n"):
                lines.append(f"{prefix}{line}")
            lines.append("")
            for reply in replies.get(comment["id"], []):
                render_comment(reply, depth + 1)

        for c in top_level:
            render_comment(c)
            lines.append("---")
            lines.append("")

    return "\n".join(lines)


def main():
    if len(sys.argv) < 2:
        print("Usage: python fetch_reddit.py <reddit_url> [output_dir]")
        print("       python fetch_reddit.py --batch <file_with_urls> [output_dir]")
        sys.exit(1)

    output_dir = Path("_work-in-progress/reddit-posts")

    if sys.argv[1] == "--batch":
        if len(sys.argv) < 3:
            print("Usage: python fetch_reddit.py --batch <file_with_urls> [output_dir]")
            sys.exit(1)
        urls_file = sys.argv[2]
        if len(sys.argv) > 3:
            output_dir = Path(sys.argv[3])
        with open(urls_file) as f:
            urls = [line.strip() for line in f if line.strip() and not line.startswith("#")]
    else:
        urls = [sys.argv[1]]
        if len(sys.argv) > 2:
            output_dir = Path(sys.argv[2])

    output_dir.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")

    for url in urls:
        subreddit, post_id, slug = parse_reddit_url(url)
        filename = f"{subreddit}_{post_id}_{slug}"
        print(f"Fetching: {url}")

        try:
            post = fetch_post_by_title(subreddit, slug)
            if not post:
                print(f"  NOT FOUND in Arctic-Shift")
                outpath = output_dir / f"{filename}_{ts}.md"
                outpath.write_text(
                    f"# NOT FOUND\n\nURL: {url}\nFetched: {ts}\n"
                    f"Subreddit `{subreddit}` / slug `{slug}` not found in Arctic-Shift.\n"
                )
                print(f"  -> {outpath}")
                time.sleep(1)
                continue

            # Verify we got the right post
            if post["id"] != post_id:
                print(f"  WARNING: Found post {post['id']} but expected {post_id}")
                print(f"  Title: {post['title']}")

            time.sleep(1)  # rate limit
            comments = fetch_comments(post["id"])

            # Save formatted markdown
            md_path = output_dir / f"{filename}_{ts}.md"
            md_path.write_text(format_post(post, comments, url))
            print(f"  -> {md_path}")

            # Save raw JSON
            json_path = output_dir / f"{filename}_{ts}.json"
            json_path.write_text(json.dumps({"post": post, "comments": comments}, indent=2))

            real_comments = [c for c in comments if c.get("author") != "AutoModerator"]
            print(f"  Score: {post.get('score')}, Comments: {len(real_comments)}")

        except Exception as e:
            print(f"  ERROR: {e}")

        time.sleep(1)  # rate limit between requests
        print()


if __name__ == "__main__":
    main()
