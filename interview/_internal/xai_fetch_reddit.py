#!/usr/bin/env python3
"""Fetch Reddit posts with all comments via x.ai Grok API (which can access Reddit)."""

import json
import os
import sys
from pathlib import Path

import httpx
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent.parent.parent / ".env")

API_KEY = os.environ["XAI_API_KEY"]
API_URL = "https://api.x.ai/v1/responses"
MODEL = "grok-4-1-fast-reasoning"


def fetch_reddit_post(url: str) -> dict:
    """Fetch a Reddit post with all comments via Grok web_search."""
    payload = {
        "model": MODEL,
        "input": [
            {
                "role": "user",
                "content": (
                    f"Go to this Reddit page and return the COMPLETE content:\n\n{url}\n\n"
                    "Return the following in EXACTLY this format:\n\n"
                    "TITLE: [exact post title]\n"
                    "AUTHOR: [username]\n"
                    "SUBREDDIT: [subreddit name]\n"
                    "DATE: [post date]\n"
                    "SCORE: [upvotes if visible]\n"
                    "URL: [the url]\n\n"
                    "POST BODY:\n[the full original post text, preserving formatting]\n\n"
                    "COMMENTS:\n"
                    "[For each comment, format as:]\n"
                    "---\n"
                    "u/[username] | [score if visible] | [date if visible]\n"
                    "[full comment text]\n"
                    "[if there are replies, indent them with > and include them]\n\n"
                    "Include ALL comments and replies, not just top-level ones. "
                    "Do not summarize or skip any comments. "
                    "Do not add any analysis or commentary of your own."
                ),
            }
        ],
        "tools": [{"type": "web_search"}],
        "temperature": 0,
    }

    resp = httpx.post(
        API_URL,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}",
        },
        json=payload,
        timeout=120,
    )
    resp.raise_for_status()
    return resp.json()


def extract_text(response: dict) -> str:
    """Extract text content from Grok response."""
    parts = []
    for item in response.get("output", []):
        if item.get("type") == "message":
            for content in item.get("content", []):
                if content.get("type") == "output_text":
                    parts.append(content["text"])
    return "\n".join(parts)


def extract_urls_visited(response: dict) -> list[str]:
    """Extract URLs from web_search_call open_page actions."""
    urls = []
    for item in response.get("output", []):
        if item.get("type") == "web_search_call":
            action = item.get("action", {})
            if action.get("type") == "open_page" and action.get("url"):
                urls.append(action["url"])
    return urls


def extract_citations(response: dict) -> list[dict]:
    """Extract url_citation annotations from output_text blocks."""
    citations = []
    seen = set()
    for item in response.get("output", []):
        if item.get("type") == "message":
            for content in item.get("content", []):
                if content.get("type") == "output_text":
                    for ann in content.get("annotations", []):
                        if ann.get("type") == "url_citation" and ann.get("url"):
                            url = ann["url"]
                            if url not in seen:
                                seen.add(url)
                                citations.append({"url": url, "title": ann.get("title", "")})
    return citations


def url_to_filename(url: str) -> str:
    """Convert Reddit URL to a safe filename."""
    # Extract subreddit and post ID from URL
    parts = url.rstrip("/").split("/")
    # Find 'comments' index
    try:
        idx = parts.index("comments")
        post_id = parts[idx + 1]
        slug = parts[idx + 2] if idx + 2 < len(parts) else "post"
    except (ValueError, IndexError):
        post_id = "unknown"
        slug = "post"
    # Find subreddit
    try:
        r_idx = parts.index("r")
        subreddit = parts[r_idx + 1]
    except (ValueError, IndexError):
        subreddit = "unknown"
    return f"{subreddit}_{post_id}_{slug}.md"


def main():
    if len(sys.argv) < 2:
        print("Usage: python xai_fetch_reddit.py <reddit_url> [output_dir]")
        print("       python xai_fetch_reddit.py --batch <file_with_urls> [output_dir]")
        sys.exit(1)

    output_dir = Path("_work-in-progress/reddit-posts")

    if sys.argv[1] == "--batch":
        if len(sys.argv) < 3:
            print("Usage: python xai_fetch_reddit.py --batch <file_with_urls> [output_dir]")
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

    for url in urls:
        filename = url_to_filename(url)
        outpath = output_dir / filename
        print(f"Fetching: {url}")
        print(f"  -> {outpath}")

        try:
            response = fetch_reddit_post(url)
            text = extract_text(response)

            # Save the extracted text
            outpath.write_text(text)

            # Save trimmed JSON response
            json_path = output_dir / filename.replace(".md", ".json")
            trimmed = {
                "url": url,
                "text": text,
                "urls_visited": extract_urls_visited(response),
                "citations": extract_citations(response),
                "usage": response.get("usage", {}),
            }
            json_path.write_text(json.dumps(trimmed, indent=2))

            usage = response.get("usage", {})
            cost = usage.get("cost_in_usd_ticks", 0) / 1_000_000
            tools = usage.get("num_server_side_tools_used", 0)
            print(f"  Done. Tools used: {tools}, Cost: ${cost:.4f}")
        except Exception as e:
            print(f"  ERROR: {e}")

        print()


if __name__ == "__main__":
    main()
