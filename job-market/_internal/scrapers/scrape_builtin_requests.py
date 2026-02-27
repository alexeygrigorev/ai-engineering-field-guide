#!/usr/bin/env python3
"""
Built In job listing scraper using requests + Oxylabs proxy.
No Playwright/browser automation needed.

Scrapes all 5 Built In locations, saves per-location JSONs with date stamp,
then combines into a single CSV.
"""
import os
import sys
import csv
import json
import time
import random
import argparse
from datetime import date
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

if sys.stdout.encoding != "utf-8":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

load_dotenv()

OXYLABS_ENDPOINT = os.getenv("OXYLABS_ENDPOINT", "pr.oxylabs.io:7777")
OXYLABS_USER = os.getenv("OXYLABS_USER")
OXYLABS_PASSWORD = os.getenv("OXYLABS_PASSWORD")

SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent  # _internal/
JSON_DIR = PROJECT_ROOT / "jobs" / "builtin"
JSON_DIR.mkdir(parents=True, exist_ok=True)

BUILTIN_SITES = {
    "la": {
        "name": "LA, USA (Global)",
        "url": "https://www.builtinla.com/jobs?search=AI+engineer&allLocations=true",
    },
    "berlin": {
        "name": "Berlin, Germany",
        "url": "https://builtin.com/jobs?search=AI+Engineer&city=Berlin&state=Berlin&country=DEU&allLocations=true",
    },
    "london": {
        "name": "London, UK",
        "url": "https://builtin.com/jobs?search=AI+Engineer&city=London&state=England&country=GBR&allLocations=true",
    },
    "amsterdam": {
        "name": "Amsterdam, Netherlands",
        "url": "https://builtin.com/jobs?search=AI+Engineer&city=Amsterdam&state=Noord-Holland&country=NLD&allLocations=true",
    },
    "newyork": {
        "name": "New York, USA",
        "url": "https://builtin.com/jobs?search=AI+Engineer&city=New+York&state=New+York&country=USA&allLocations=true",
    },
    "india": {
        "name": "India",
        "url": "https://builtin.com/jobs/remote/hybrid/office?search=AI+Engineer&country=IND",
    },
}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

CSV_FIELDS = ["title", "company", "location", "work_type", "level", "compensation", "link", "id", "scraped_date"]


def get_proxy():
    return {
        "http": f"http://customer-{OXYLABS_USER}:{OXYLABS_PASSWORD}@{OXYLABS_ENDPOINT}",
        "https": f"http://customer-{OXYLABS_USER}:{OXYLABS_PASSWORD}@{OXYLABS_ENDPOINT}",
    }


def fetch_page(url, retries=3):
    """Fetch a page with retries."""
    for attempt in range(retries):
        try:
            resp = requests.get(url, proxies=get_proxy(), headers=HEADERS, timeout=60)
            resp.raise_for_status()
            return resp.text
        except Exception as e:
            if attempt < retries - 1:
                wait = 5 * (attempt + 1) + random.uniform(0, 2)
                print(f"    Retry {attempt + 1}: {e}")
                time.sleep(wait)
            else:
                print(f"    Failed after {retries} attempts: {e}")
                return None


def extract_jobs_from_html(html_content, base_domain):
    """Extract job cards from listing page HTML."""
    soup = BeautifulSoup(html_content, "html.parser")
    jobs = []

    # Find all job title links (same selector as Playwright version)
    title_links = soup.select('h2 a[href*="/job/"]')

    for link_el in title_links:
        job = {}

        # Title and link
        job["title"] = link_el.get_text(strip=True)
        href = link_el.get("href", "")
        if href.startswith("/"):
            job["link"] = f"https://{base_domain}{href}"
        else:
            job["link"] = href

        # Extract job ID from link
        job["id"] = href.rstrip("/").rsplit("/", 1)[-1]

        # Find the card container (walk up from the link)
        card = link_el.find_parent("div", id=lambda x: x and x.startswith("job-card-"))
        if not card:
            card = link_el.find_parent("div", class_=lambda x: x and "job" in x.lower()) if link_el.parent else None
        if not card:
            # Walk up a few levels
            card = link_el.parent
            for _ in range(5):
                if card and card.parent:
                    card = card.parent
                else:
                    break

        # Company - from company link img alt or span
        job["company"] = ""
        if card:
            company_link = card.find("a", href=lambda x: x and "/company/" in x)
            if company_link:
                img = company_link.find("img")
                if img and img.get("alt"):
                    job["company"] = img["alt"].replace(" Logo", "").replace(" logo", "").strip()
                else:
                    span = company_link.find("span")
                    if span:
                        job["company"] = span.get_text(strip=True)
                    else:
                        job["company"] = company_link.get_text(strip=True)

        # Icon-based fields
        job["location"] = ""
        job["work_type"] = ""
        job["compensation"] = ""
        job["level"] = ""

        if card:
            # Location: fa-location-dot
            loc_icon = card.find("i", class_=lambda c: c and "fa-location-dot" in c)
            if loc_icon:
                parent = loc_icon.parent
                if parent:
                    job["location"] = parent.get_text(strip=True)

            # Work type: fa-house-building
            wt_icon = card.find("i", class_=lambda c: c and "fa-house-building" in c)
            if wt_icon:
                parent = wt_icon.parent
                if parent:
                    job["work_type"] = parent.get_text(strip=True)

            # Compensation: fa-sack-dollar
            comp_icon = card.find("i", class_=lambda c: c and "fa-sack-dollar" in c)
            if comp_icon:
                parent = comp_icon.parent
                if parent:
                    job["compensation"] = parent.get_text(strip=True)

            # Level: fa-trophy
            level_icon = card.find("i", class_=lambda c: c and "fa-trophy" in c)
            if level_icon:
                parent = level_icon.parent
                if parent:
                    job["level"] = parent.get_text(strip=True)

        # Only add if we have title and link
        if job["title"] and job["link"]:
            jobs.append(job)

    return jobs


def scrape_site(site_id, site_config, scraped_date):
    """Scrape all pages for a Built In site."""
    print(f"\n{'='*60}")
    print(f"Scraping: {site_config['name']}")
    print(f"URL: {site_config['url']}")
    print(f"{'='*60}")

    # Extract base domain from URL
    from urllib.parse import urlparse
    parsed = urlparse(site_config["url"])
    base_domain = parsed.netloc

    all_jobs = []
    seen_ids = set()
    page_num = 1

    while True:
        url = site_config["url"]
        if page_num > 1:
            separator = "&" if "?" in url else "?"
            url = f"{url}{separator}page={page_num}"

        print(f"  Page {page_num}: {url}")

        html = fetch_page(url)
        if not html:
            print(f"    Failed to fetch page {page_num}, stopping")
            break

        page_jobs = extract_jobs_from_html(html, base_domain)

        # Filter duplicates
        new_jobs = []
        for job in page_jobs:
            if job["id"] not in seen_ids:
                seen_ids.add(job["id"])
                job["scraped_date"] = scraped_date
                new_jobs.append(job)

        if not page_jobs:
            print(f"    No jobs found on page {page_num}, stopping")
            break

        all_jobs.extend(new_jobs)
        print(f"    Got {len(page_jobs)} jobs ({len(new_jobs)} new)")

        # Show first few
        for job in page_jobs[:3]:
            print(f"      - {job.get('company', '?')}: {job['title'][:50]}...")

        # Check if likely last page
        if len(page_jobs) < 15:
            print(f"    Only {len(page_jobs)} jobs, likely last page")
            break

        page_num += 1
        time.sleep(2 + random.uniform(0, 2))

    return all_jobs


def main():
    parser = argparse.ArgumentParser(description="Scrape Built In job listings (requests-based)")
    parser.add_argument("sites", nargs="*", help="Sites to scrape (default: all)")
    parser.add_argument("--date", default=date.today().isoformat(), help="Date label (default: today)")
    args = parser.parse_args()

    scraped_date = args.date
    date_stamp = scraped_date.replace("-", "")
    sites = args.sites if args.sites else list(BUILTIN_SITES.keys())

    print("=" * 60)
    print("Built In Job Scraper (requests-based)")
    print(f"Date: {scraped_date}")
    print(f"Sites: {', '.join(sites)}")
    print("=" * 60)

    all_jobs = []

    for site_id in sites:
        if site_id not in BUILTIN_SITES:
            print(f"Unknown site: {site_id}")
            print(f"Available: {', '.join(BUILTIN_SITES.keys())}")
            continue

        site_jobs = scrape_site(site_id, BUILTIN_SITES[site_id], scraped_date)

        # Save per-site JSON (date-stamped)
        if site_jobs:
            json_file = JSON_DIR / f"{site_id}_{date_stamp}.json"
            with open(json_file, "w", encoding="utf-8") as f:
                json.dump(site_jobs, f, indent=2, ensure_ascii=False)
            print(f"\n  Saved {len(site_jobs)} jobs -> {json_file.name}")

        all_jobs.extend(site_jobs)

    # Combine into CSV
    if all_jobs:
        csv_file = PROJECT_ROOT / f"all_jobs_{date_stamp}.csv"
        with open(csv_file, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=CSV_FIELDS)
            writer.writeheader()
            for job in all_jobs:
                writer.writerow({field: job.get(field, "") for field in CSV_FIELDS})
        print(f"\nCombined CSV: {csv_file.name} ({len(all_jobs)} jobs)")

    print(f"\n{'='*60}")
    print(f"COMPLETE - {len(all_jobs)} total jobs across {len(sites)} sites")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
