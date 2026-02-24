#!/usr/bin/env python3
import re
from pathlib import Path
import html

# More permissive pattern
URL_PATTERN = r'https?://(?:www\.)?(?:reddit\.com/r/\w+/[\w-]+|x\.com/[\w-]+|twitter\.com/[\w-]+|github\.com/[\w-]+/[\w-]+|medium\.com/[@\w-]+/[\w-]+|dev\.to/[\w-]+/[\w-]+|scribd\.com/document/[\w-]+)'

def clean_url(url):
    url = re.sub(r':~:text[^"\'<>]*', '', url)
    url = re.sub(r'&amp;', '&', url)
    url = re.sub(r'&lt;', '<', url)
    url = re.sub(r'&gt;', '>', url)
    url = url.strip('\'"<>.,')
    return url

def strip_html_entities(text):
    """Decode HTML entities"""
    text = html.unescape(text)
    text = re.sub(r'<[^>]+>', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def extract_links_with_context(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    results = []
    seen = set()

    # Find URLs in raw HTML
    for match in re.finditer(URL_PATTERN, content, re.IGNORECASE):
        url = clean_url(match.group(0))

        if url in seen or any(x in url for x in ['google.com', 'gstatic.com', 'favicon', 'clients6.google.com']):
            continue
        seen.add(url)

        # Get context around the URL
        start = max(0, match.start() - 300)
        end = min(len(content), match.end() + 300)
        context_raw = content[start:end]

        # Clean context
        context = strip_html_entities(context_raw)
        if len(context) > 400:
            context = context[:400] + '...'

        results.append((url, context))

    return results

def main():
    html_dir = Path('research_html')
    all_results = {}

    for html_file in sorted(html_dir.glob('*.html')):
        print(f"Processing {html_file.name}...")
        results = extract_links_with_context(html_file)

        for url, context in results:
            if url not in all_results:
                all_results[url] = context

    # Categorize
    categories = {
        'Reddit': [],
        'X/Twitter': [],
        'GitHub': [],
        'Medium': [],
        'Dev.to': [],
        'Scribd': [],
        'LinkedIn': [],
    }

    for url, context in sorted(all_results.items()):
        if 'reddit.com' in url:
            categories['Reddit'].append((url, context))
        elif 'x.com' in url or 'twitter.com' in url:
            categories['X/Twitter'].append((url, context))
        elif 'github.com' in url:
            categories['GitHub'].append((url, context))
        elif 'medium.com' in url:
            categories['Medium'].append((url, context))
        elif 'dev.to' in url:
            categories['Dev.to'].append((url, context))
        elif 'scribd.com' in url:
            categories['Scribd'].append((url, context))
        elif 'linkedin.com' in url:
            categories['LinkedIn'].append((url, context))

    # Write to file
    with open('research/sources.md', 'w', encoding='utf-8') as f:
        f.write('# Research Sources\n\nExtracted from research_html files with context.\n\n')

        for category, items in categories.items():
            if items:
                f.write(f'## {category} ({len(items)} links)\n\n')
                for url, context in items:
                    f.write(f'{url}\n\n{context}\n\n')
                f.write('\n')

    print(f"\nTotal unique links: {len(all_results)}")
    print("Written to research/sources.md")

if __name__ == '__main__':
    main()
