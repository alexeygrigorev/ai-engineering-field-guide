#!/usr/bin/env python3
"""Query x.ai Grok API with web_search and x_search tools for research."""

import json
import os
import sys
from datetime import datetime
from pathlib import Path

import httpx
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent.parent.parent / ".env")

API_KEY = os.environ["XAI_API_KEY"]
API_URL = "https://api.x.ai/v1/responses"
MODEL = "grok-4-1-fast-reasoning"

OUTPUT_DIR = Path("_work-in-progress/grok-responses")


def search(query: str, tools: list[str] | None = None, system: str | None = None) -> dict:
    """Run a query with Grok search tools."""
    if tools is None:
        tools = ["web_search", "x_search"]

    tool_defs = [{"type": t} for t in tools]

    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": query})

    payload = {
        "model": MODEL,
        "input": messages,
        "tools": tool_defs,
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
    """Extract text content from a Grok response."""
    parts = []
    for item in response.get("output", []):
        if item.get("type") == "message":
            for content in item.get("content", []):
                if content.get("type") == "output_text":
                    parts.append(content["text"])
    return "\n".join(parts)


def extract_citations(response: dict) -> list[dict]:
    """Extract citations from a Grok response."""
    citations = []
    for item in response.get("output", []):
        if item.get("type") == "message":
            for content in item.get("content", []):
                if content.get("type") == "output_text":
                    for cite in content.get("annotations", []):
                        if cite.get("type") == "url_citation":
                            citations.append({
                                "title": cite.get("title", ""),
                                "url": cite.get("url", ""),
                            })
    return citations


def save_response(query: str, response: dict, label: str | None = None):
    """Save the full response with timestamp."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    slug = label or query[:50].replace(" ", "_").replace("/", "_")
    slug = "".join(c for c in slug if c.isalnum() or c in "_-")

    path = OUTPUT_DIR / f"{ts}_{slug}.json"
    payload = {
        "query": query,
        "timestamp": ts,
        "response": response,
    }
    path.write_text(json.dumps(payload, indent=2))
    return path


def main():
    if len(sys.argv) < 2:
        print("Usage: python xai_search.py '<query>' [--tools web_search,x_search] [--system 'prompt'] [--raw] [--label 'name']")
        sys.exit(1)

    query = sys.argv[1]
    tools = None
    system = None
    raw = False
    label = None

    i = 2
    while i < len(sys.argv):
        if sys.argv[i] == "--tools" and i + 1 < len(sys.argv):
            tools = sys.argv[i + 1].split(",")
            i += 2
        elif sys.argv[i] == "--system" and i + 1 < len(sys.argv):
            system = sys.argv[i + 1]
            i += 2
        elif sys.argv[i] == "--label" and i + 1 < len(sys.argv):
            label = sys.argv[i + 1]
            i += 2
        elif sys.argv[i] == "--raw":
            raw = True
            i += 1
        else:
            i += 1

    response = search(query, tools=tools, system=system)

    # Always save full response
    saved_path = save_response(query, response, label=label)
    print(f"[Saved to {saved_path}]", file=sys.stderr)

    usage = response.get("usage", {})
    cost = usage.get("cost_in_usd_ticks", 0) / 1_000_000
    tools_used = usage.get("num_server_side_tools_used", 0)
    print(f"[Tools: {tools_used}, Cost: ${cost:.4f}]", file=sys.stderr)

    if raw:
        print(json.dumps(response, indent=2))
    else:
        text = extract_text(response)
        citations = extract_citations(response)

        print(text)
        if citations:
            seen = set()
            print("\n--- Sources ---")
            for c in citations:
                url = c["url"]
                if url not in seen:
                    seen.add(url)
                    title = c["title"] or url
                    print(f"- [{title}]({url})")


if __name__ == "__main__":
    main()
