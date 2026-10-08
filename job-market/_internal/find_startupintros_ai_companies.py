"""Find stable AI companies from Startup Intros.

The script discovers candidates via Startup Intros' public search API, enriches
them from organization pages, and writes dated Markdown/CSV/JSON shortlists.
"""
from __future__ import annotations

import argparse
import csv
import html
import json
import math
import os
import re
import shutil
import sys
import time
from dataclasses import asdict, dataclass, field
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

try:
    from pipeline_paths import INTERNAL_ROOT, JOB_MARKET_ROOT, PIPELINE_DATA_DIR
except ImportError:
    INTERNAL_ROOT = Path(__file__).resolve().parent
    JOB_MARKET_ROOT = INTERNAL_ROOT.parent
    PIPELINE_DATA_DIR = INTERNAL_ROOT / "data"

load_dotenv(JOB_MARKET_ROOT / ".env")


BASE_URL = "https://startupintros.com"
SEARCH_URL = f"{BASE_URL}/api/search"
FIRECRAWL_SCRAPE_URL = "https://api.firecrawl.dev/v2/scrape"
OUTPUT_ROOT = PIPELINE_DATA_DIR / "startupintros"

DEFAULT_QUERIES = [
    "ai engineer",
    "artificial intelligence",
    "generative ai",
    "llm",
    "agents",
    "agentic",
    "developer tools ai",
    "ai infrastructure",
    "machine learning",
    "computer vision",
    "automation ai",
    "rag",
    "voice ai",
]

AI_KEYWORDS = [
    "ai[- ]powered",
    "artificial intelligence",
    "machine learning",
    "generative ai",
    "large language model",
    "llm",
    "llmops",
    "foundation model",
    "agentic",
    "ai agent",
    "autonomous agent",
    "computer vision",
    "natural language",
    "nlp",
    "deep learning",
    "inference",
    "rag",
    "retrieval augmented",
    "model deployment",
    "model evaluation",
    "mlops",
    "speech recognition",
    "voice ai",
]
AI_REGEXES = [
    re.compile(rf"(?<![a-z0-9]){keyword}(?![a-z0-9])", re.IGNORECASE)
    for keyword in AI_KEYWORDS
]

TRACTION_PATTERNS = [
    r"\b\d[\d,.]*\s*(?:k|m|b|million|billion)?\s+(?:users|customers|clients|enterprises|developers|teams|employees|creators|brands|clinics|stores|locations|agencies|downloads|members|repositories|repos|questions|claims|transactions|deployments|installations)\b",
    r"\b(?:serves|serving|used by|utilized by|deployed by|adopted by|trusted by)\b",
    r"\b(?:fortune\s+\d+|enterprise customer|paying customer|annual recurring revenue|arr|revenue run-rate|revenue)\b",
    r"\b(?:github stars|discord members|monthly active|daily active|active users|download volume)\b",
    r"\b(?:including|customers include|clients include)\s+[A-Z][A-Za-z0-9&.\- ]+",
]

NEWNESS_RISK_PATTERNS = [
    r"\bwithin months\b",
    r"\brecently launched\b",
    r"\binitial public launch\b",
    r"\bstealth\b",
    r"\btwo employees\b",
    r"\bcore team of two\b",
]

ROUND_RE = re.compile(
    r"(?:most recently,\s*)?(?:it|the company|the organization|the firm)?\s*"
    r"(?:has\s+)?(?:raised|secured|closed)\s+"
    r"(?P<amount>[$\u20ac\u00a3]\s?[\d,.]+(?:\s*(?:million|billion)|[mb])?|\d[\d,.]*(?:\s+(?:million|billion)|[mb])\b)"
    r"(?:\s+in\s+)?(?P<round>(?:pre[- ]?seed|seed|series\s+[a-z]|growth|venture|strategic|debt|equity)[^.,;]*)?",
    re.IGNORECASE,
)
TOTAL_FUNDING_RE = re.compile(
    r"(?:raised|secured|funding(?: raised)?(?: to date)?(?: of)?|total venture funding(?: of)?)"
    r".{0,80}?"
    r"(?P<amount>[$\u20ac\u00a3]\s?[\d,.]+(?:\s*(?:million|billion)|[mb])?|\d[\d,.]*(?:\s+(?:million|billion)|[mb])\b)",
    re.IGNORECASE,
)
YEAR_RE = re.compile(r"\b(19\d{2}|20\d{2})\b")


@dataclass
class CompanyRecord:
    name: str
    slug: str
    url: str
    website_url: str = ""
    location: str = ""
    year_founded: int | None = None
    company_size: str = ""
    company_type: str = ""
    company_role: str = ""
    operating_status: str = ""
    description: str = ""
    about: str = ""
    funding_musd: float | None = None
    funding_text: str = ""
    funding_rounds: int | None = None
    latest_round: str = ""
    traction_evidence: list[str] = field(default_factory=list)
    ai_evidence: list[str] = field(default_factory=list)
    risk_flags: list[str] = field(default_factory=list)
    sources: list[str] = field(default_factory=list)
    score: float = 0.0
    decision: str = "review"
    reasons: list[str] = field(default_factory=list)


def clean_text(value: str | None) -> str:
    if not value:
        return ""
    value = html.unescape(value)
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def split_sentences(text: str) -> list[str]:
    text = clean_text(text)
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9])", text)
    return [part.strip() for part in parts if len(part.strip()) > 20]


def parse_money_to_musd(text: str) -> float | None:
    value = clean_text(text).lower().replace(",", "")
    currency_multiplier = 1.0
    has_currency = value.startswith(("$", "\u20ac", "\u00a3"))
    if value.startswith("\u20ac"):
        currency_multiplier = 1.09
    elif value.startswith("\u00a3"):
        currency_multiplier = 1.27

    value = value.lstrip("$\u20ac\u00a3").strip()
    match = re.search(r"(\d+(?:\.\d+)?)", value)
    if not match:
        return None

    has_scale = bool(re.search(r"(?:million|billion|[mb])\b", value))
    if has_currency and not has_scale:
        return None

    amount = float(match.group(1))
    if "billion" in value or re.search(r"b\b", value):
        amount *= 1000
    elif "million" in value or re.search(r"m\b", value):
        amount *= 1
    else:
        # Startup Intros mostly uses abbreviated funding amounts. Treat bare
        # dollar amounts as millions when they are written in funding context.
        amount *= 1

    return round(amount * currency_multiplier, 2)


def find_funding(text: str) -> tuple[float | None, str, str]:
    candidates: list[tuple[float, str, str]] = []
    for regex in (TOTAL_FUNDING_RE, ROUND_RE):
        for match in regex.finditer(text):
            amount_text = match.group("amount")
            amount = parse_money_to_musd(amount_text)
            if amount is None:
                continue
            context = clean_text(text[max(0, match.start() - 90) : match.end() + 120])
            local_context = clean_text(text[max(0, match.start() - 45) : match.end() + 45])
            after_amount = clean_text(text[match.end() : match.end() + 60])
            if re.search(r"\b(undisclosed|not available|no significant|remain undisclosed)\b", context, re.IGNORECASE):
                continue
            if re.search(r"\b(valuation|post-money|post money)\b", local_context, re.IGNORECASE):
                continue
            revenue_after_match = re.search(r"\b(revenue|run-rate|run rate)\b", after_amount, re.IGNORECASE)
            if revenue_after_match:
                before_revenue = after_amount[: revenue_after_match.start()]
                if not re.search(r"\b(funding|capital|round)\b", before_revenue, re.IGNORECASE):
                    continue
            local_has_funding_word = re.search(r"\b(funding|raised|secured|capital|round)\b", local_context, re.IGNORECASE)
            if re.search(r"\b(revenue|run-rate|run rate)\b", local_context, re.IGNORECASE) and not local_has_funding_word:
                continue
            round_text = clean_text(match.groupdict().get("round") or "")
            candidates.append((amount, context, round_text))

    if not candidates:
        return None, "", ""

    amount, context, round_text = max(candidates, key=lambda item: item[0])
    return amount, context, round_text


def find_funding_rounds(text: str) -> int | None:
    match = re.search(r"across\s+(\d+)\s+funding rounds?", text, re.IGNORECASE)
    return int(match.group(1)) if match else None


def extract_json_ld(soup: BeautifulSoup) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for script in soup.find_all("script", attrs={"type": "application/ld+json"}):
        raw = script.string or script.get_text("")
        if not raw.strip():
            continue
        try:
            parsed = json.loads(raw)
        except json.JSONDecodeError:
            continue
        if isinstance(parsed, list):
            records.extend(item for item in parsed if isinstance(item, dict))
        elif isinstance(parsed, dict):
            records.append(parsed)
    return records


def extract_sources(soup: BeautifulSoup) -> list[str]:
    sources: list[str] = []
    for link in soup.find_all("a", href=True):
        href = link["href"].strip()
        if href.startswith("/"):
            continue
        if "startupintros.com" in href:
            continue
        if href.startswith(("http://", "https://")) and href not in sources:
            sources.append(href)
    return sources[:12]


def extract_page_text(soup: BeautifulSoup) -> str:
    for element in soup.find_all(["script", "style", "noscript", "svg"]):
        element.decompose()
    main = soup.find("main")
    return clean_text((main or soup).get_text(" "))


def ai_evidence_from_text(text: str) -> list[str]:
    sentences = split_sentences(text)
    evidence: list[str] = []
    for sentence in sentences:
        if any(regex.search(sentence) for regex in AI_REGEXES):
            evidence.append(sentence)
        if len(evidence) >= 3:
            break
    return evidence


def traction_from_text(text: str) -> list[str]:
    sentences = split_sentences(text)
    evidence: list[str] = []
    for sentence in sentences:
        if any(re.search(pattern, sentence, re.IGNORECASE) for pattern in TRACTION_PATTERNS):
            if sentence not in evidence:
                evidence.append(sentence)
        if len(evidence) >= 4:
            break
    return evidence


def risk_flags_from_text(text: str, *, current_year: int, year_founded: int | None) -> list[str]:
    flags: list[str] = []
    if year_founded and current_year - year_founded < 2:
        flags.append(f"founded {year_founded}, less than 2 years old")
    lower = text.lower()
    for pattern in NEWNESS_RISK_PATTERNS:
        if re.search(pattern, lower):
            label = pattern.replace(r"\b", "").replace("\\", "")
            flags.append(f"newness signal: {label}")
    if re.search(
        r"\b(?:was|were|got|been|being)\s+acquired\s+by\b|\bprior to its acquisition\b|\bfollowing (?:the|its) acquisition\b",
        lower,
    ):
        flags.append("company acquisition mentioned")
    return sorted(set(flags))


def score_record(record: CompanyRecord, *, min_funding_musd: float, min_age_years: int, current_year: int) -> CompanyRecord:
    reasons: list[str] = []
    score = 0.0

    if record.operating_status and record.operating_status.lower() not in {"active", "operating"}:
        reasons.append(f"status is {record.operating_status}")
    if record.company_role and record.company_role.lower() not in {"startup", "company"}:
        reasons.append(f"not an operating startup/company: {record.company_role}")
    if re.search(r"\b(ventures|venture capital|capital partners|capital management|fund|vc)\b", record.name, re.IGNORECASE):
        reasons.append("appears to be an investor or fund, not an application target")

    if not record.ai_evidence:
        reasons.append("no strong AI product evidence")
    else:
        score += 20 + min(10, len(record.ai_evidence) * 3)

    if record.funding_musd is None:
        reasons.append("funding unknown")
    elif record.funding_musd < min_funding_musd:
        reasons.append(f"funding ${record.funding_musd:.1f}M is below ${min_funding_musd:.1f}M")
    else:
        score += 20 + min(20, math.log10(max(record.funding_musd, 1)) * 12)

    if record.year_founded is None:
        reasons.append("founding year unknown")
    elif current_year - record.year_founded < min_age_years:
        reasons.append(f"founded {record.year_founded}, too new for {min_age_years}+ year filter")
    else:
        score += min(15, (current_year - record.year_founded) * 2)

    if not record.traction_evidence:
        reasons.append("no concrete traction evidence")
    else:
        score += 15 + min(15, len(record.traction_evidence) * 4)

    if record.funding_rounds and record.funding_rounds >= 2:
        score += 5
    if record.latest_round and re.search(r"series\s+[ab]|growth", record.latest_round, re.IGNORECASE):
        score += 5
    if any("company acquisition mentioned" == flag for flag in record.risk_flags):
        reasons.append("company acquisition mentioned")
        score -= 8

    record.score = round(score, 1)
    record.reasons = reasons
    record.decision = "apply" if not reasons else "skip"
    return record


class StartupIntrosClient:
    def __init__(
        self,
        *,
        delay_seconds: float = 0.2,
        timeout_seconds: float = 30.0,
        use_firecrawl: bool = False,
        firecrawl_api_key: str = "",
        firecrawl_clean_content: bool = True,
    ) -> None:
        self.delay_seconds = delay_seconds
        self.timeout_seconds = timeout_seconds
        self.use_firecrawl = use_firecrawl
        self.firecrawl_api_key = firecrawl_api_key
        self.firecrawl_clean_content = firecrawl_clean_content
        self.session = requests.Session()
        self.session.headers.update(
            {
                "User-Agent": "Mozilla/5.0 (compatible; ai-engineering-job-market-research/1.0)",
                "Accept": "application/json,text/html;q=0.9,*/*;q=0.8",
            }
        )

    def search(self, query: str) -> list[dict[str, Any]]:
        response = self.session.get(SEARCH_URL, params={"q": query}, timeout=self.timeout_seconds)
        response.raise_for_status()
        data = response.json()
        time.sleep(self.delay_seconds)
        return data.get("companies") or []

    def fetch_org_page(self, slug: str) -> str:
        response = self.session.get(urljoin(BASE_URL, f"/orgs/{slug}"), timeout=self.timeout_seconds)
        response.raise_for_status()
        time.sleep(self.delay_seconds)
        return response.text

    def fetch_org_markdown(self, url: str) -> str:
        if not self.use_firecrawl:
            return ""
        if not self.firecrawl_api_key:
            raise RuntimeError("FIRECRAWL_API_KEY is required when --use-firecrawl is set")

        payload = {
            "url": url,
            "formats": ["markdown"],
            "onlyMainContent": True,
            "onlyCleanContent": self.firecrawl_clean_content,
            "removeBase64Images": True,
            "blockAds": True,
            "timeout": int(self.timeout_seconds * 1000),
        }
        response = self.session.post(
            FIRECRAWL_SCRAPE_URL,
            headers={
                "Authorization": f"Bearer {self.firecrawl_api_key}",
                "Content-Type": "application/json",
            },
            json=payload,
            timeout=max(self.timeout_seconds + 5, 60),
        )
        response.raise_for_status()
        data = response.json()
        if not data.get("success", True):
            raise RuntimeError(str(data.get("error") or "Firecrawl scrape failed"))
        time.sleep(self.delay_seconds)
        return clean_text((data.get("data") or {}).get("markdown") or "")


def year_from_value(value: Any) -> int | None:
    if value is None:
        return None
    match = YEAR_RE.search(str(value))
    if not match:
        return None
    year = int(match.group(1))
    return year if 1900 <= year <= date.today().year + 1 else None


def record_from_search_result(item: dict[str, Any]) -> CompanyRecord:
    slug = str(item.get("slug") or "").strip()
    name = str(item.get("name") or slug).strip()
    return CompanyRecord(
        name=name,
        slug=slug,
        url=urljoin(BASE_URL, f"/orgs/{slug}"),
        website_url=str(item.get("website_url") or "").strip(),
        location=str(item.get("headquarters_location") or "").strip(),
        year_founded=year_from_value(item.get("year_founded")),
        company_size=str(item.get("company_size") or "").strip(),
        company_type=str(item.get("company_type") or "").strip(),
        company_role=str(item.get("company_role") or "").strip(),
        operating_status=str(item.get("operating_status") or "").strip(),
        description=clean_text(item.get("meta_description")),
        about=clean_text(item.get("about")),
    )


def enrich_record(
    record: CompanyRecord,
    page_html: str,
    *,
    current_year: int,
    page_markdown: str = "",
) -> CompanyRecord:
    soup = BeautifulSoup(page_html, "html5lib")
    page_title = clean_text(soup.title.get_text(" ") if soup.title else "")
    visible_text = "" if "Organization Not Found" in page_title else extract_page_text(soup)
    combined_text = clean_text(" ".join([record.description, record.about, visible_text, page_markdown]))

    for json_ld in extract_json_ld(soup):
        if json_ld.get("@type") != "Organization":
            continue
        record.website_url = record.website_url or str(json_ld.get("url") or "")
        record.description = record.description or clean_text(json_ld.get("description"))
        record.year_founded = record.year_founded or year_from_value(json_ld.get("foundingDate"))
        address = json_ld.get("address")
        if not record.location and isinstance(address, dict):
            record.location = clean_text(address.get("name"))
        employees = json_ld.get("numberOfEmployees")
        if not record.company_size and isinstance(employees, dict):
            min_value = employees.get("minValue")
            max_value = employees.get("maxValue")
            if min_value and max_value:
                record.company_size = f"{min_value}-{max_value}"

    record.funding_musd, record.funding_text, round_text = find_funding(combined_text)
    record.latest_round = round_text
    record.funding_rounds = find_funding_rounds(combined_text)
    record.ai_evidence = ai_evidence_from_text(" ".join([record.description, record.about]))
    if not record.ai_evidence:
        record.ai_evidence = ai_evidence_from_text(combined_text)
    record.traction_evidence = traction_from_text(combined_text)
    record.risk_flags = risk_flags_from_text(combined_text, current_year=current_year, year_founded=record.year_founded)
    record.sources = extract_sources(soup)
    return record


def discover_candidates(client: StartupIntrosClient, queries: list[str], *, max_candidates: int | None) -> list[CompanyRecord]:
    records_by_slug: dict[str, CompanyRecord] = {}
    for query in queries:
        try:
            results = client.search(query)
        except Exception as exc:
            print(f"warning: search failed for {query!r}: {exc}", file=sys.stderr)
            continue
        for item in results:
            slug = str(item.get("slug") or "").strip()
            if not slug or slug in records_by_slug:
                continue
            records_by_slug[slug] = record_from_search_result(item)
            if max_candidates and len(records_by_slug) >= max_candidates:
                return list(records_by_slug.values())
    return list(records_by_slug.values())


def analyze(
    *,
    queries: list[str],
    min_funding_musd: float,
    min_age_years: int,
    max_candidates: int | None,
    delay_seconds: float,
    timeout_seconds: float,
    use_firecrawl: bool,
    firecrawl_api_key: str,
    firecrawl_clean_content: bool,
) -> list[CompanyRecord]:
    current_year = date.today().year
    client = StartupIntrosClient(
        delay_seconds=delay_seconds,
        timeout_seconds=timeout_seconds,
        use_firecrawl=use_firecrawl,
        firecrawl_api_key=firecrawl_api_key,
        firecrawl_clean_content=firecrawl_clean_content,
    )
    records = discover_candidates(client, queries, max_candidates=max_candidates)

    analyzed: list[CompanyRecord] = []
    for index, record in enumerate(records, start=1):
        if not record.slug:
            continue
        try:
            page_html = client.fetch_org_page(record.slug)
            page_markdown = ""
            if use_firecrawl:
                try:
                    page_markdown = client.fetch_org_markdown(record.url)
                except Exception as exc:
                    print(f"warning: Firecrawl failed for {record.slug}: {exc}", file=sys.stderr)
            record = enrich_record(record, page_html, current_year=current_year, page_markdown=page_markdown)
        except Exception as exc:
            record.reasons.append(f"profile fetch failed: {exc}")
        record = score_record(
            record,
            min_funding_musd=min_funding_musd,
            min_age_years=min_age_years,
            current_year=current_year,
        )
        analyzed.append(record)
        print(f"{index:03d}/{len(records):03d} {record.decision:5s} {record.name}", file=sys.stderr)

    return sorted(analyzed, key=lambda item: (item.decision != "apply", -item.score, item.name.lower()))


def markdown_escape(value: str) -> str:
    return clean_text(value).replace("|", "\\|")


def markdown_cell(value: str, *, max_length: int = 260) -> str:
    value = markdown_escape(value)
    if len(value) <= max_length:
        return value
    return value[: max_length - 3].rstrip() + "..."


def write_markdown(
    records: list[CompanyRecord],
    path: Path,
    *,
    min_funding_musd: float,
    min_age_years: int,
    queries: list[str],
) -> None:
    apply_records = [record for record in records if record.decision == "apply"]
    skipped_records = [record for record in records if record.decision != "apply"]
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    lines: list[str] = [
        "# Startup Intros AI Company Shortlist",
        "",
        f"Generated: {now}",
        "",
        "Filters:",
        f"- Funding: at least ${min_funding_musd:.1f}M disclosed or strongly stated",
        f"- Maturity: founded at least {min_age_years} years ago",
        "- Product: AI must be part of the core product, not only a name match",
        "- Traction: concrete users, customers, revenue, deployments, GitHub/community, or named customer evidence",
        "",
        f"Queries: {', '.join(queries)}",
        "",
        f"Recommended: {len(apply_records)}",
        "",
        "| Rank | Company | Funding | Founded | Traction | Why apply | Cautions | Links |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]

    for rank, record in enumerate(apply_records, start=1):
        traction = record.traction_evidence[0] if record.traction_evidence else ""
        why = record.ai_evidence[0] if record.ai_evidence else record.description
        funding = f"${record.funding_musd:.1f}M" if record.funding_musd is not None else "unknown"
        cautions = "; ".join(record.risk_flags[:2])
        links = f"[Startup Intros]({record.url})"
        if record.website_url:
            links += f", [website]({record.website_url})"
        lines.append(
            "| "
            + " | ".join(
                [
                    str(rank),
                    markdown_cell(record.name),
                    markdown_cell(funding),
                    markdown_cell(str(record.year_founded or "")),
                    markdown_cell(traction),
                    markdown_cell(why),
                    markdown_cell(cautions),
                    links,
                ]
            )
            + " |"
        )

    lines.extend(["", "## Skipped Or Needs Manual Review", ""])
    lines.extend(["| Company | Reason | Funding | Founded | Link |", "| --- | --- | --- | --- | --- |"])
    for record in skipped_records[:80]:
        funding = f"${record.funding_musd:.1f}M" if record.funding_musd is not None else "unknown"
        lines.append(
            "| "
            + " | ".join(
                [
                    markdown_cell(record.name),
                    markdown_cell("; ".join(record.reasons[:3])),
                    markdown_cell(funding),
                    markdown_cell(str(record.year_founded or "")),
                    f"[Startup Intros]({record.url})",
                ]
            )
            + " |"
        )

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_csv(records: list[CompanyRecord], path: Path) -> None:
    fields = [
        "decision",
        "score",
        "name",
        "slug",
        "url",
        "website_url",
        "location",
        "year_founded",
        "company_size",
        "company_type",
        "company_role",
        "operating_status",
        "funding_musd",
        "funding_text",
        "funding_rounds",
        "latest_round",
        "traction_evidence",
        "ai_evidence",
        "risk_flags",
        "reasons",
        "sources",
    ]
    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        for record in records:
            row = asdict(record)
            row["traction_evidence"] = " | ".join(record.traction_evidence)
            row["ai_evidence"] = " | ".join(record.ai_evidence)
            row["risk_flags"] = " | ".join(record.risk_flags)
            row["reasons"] = " | ".join(record.reasons)
            row["sources"] = " | ".join(record.sources)
            writer.writerow({field_name: row.get(field_name, "") for field_name in fields})


def write_outputs(
    records: list[CompanyRecord],
    *,
    output_date: str,
    min_funding_musd: float,
    min_age_years: int,
    queries: list[str],
) -> dict[str, Path]:
    out_dir = OUTPUT_ROOT / output_date
    out_dir.mkdir(parents=True, exist_ok=True)

    json_path = out_dir / "startupintros_ai_companies.json"
    csv_path = out_dir / "startupintros_ai_companies.csv"
    md_path = out_dir / "startupintros_ai_companies.md"

    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "filters": {
            "min_funding_musd": min_funding_musd,
            "min_age_years": min_age_years,
            "queries": queries,
        },
        "records": [asdict(record) for record in records],
    }
    json_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    write_csv(records, csv_path)
    write_markdown(
        records,
        md_path,
        min_funding_musd=min_funding_musd,
        min_age_years=min_age_years,
        queries=queries,
    )

    latest_dir = OUTPUT_ROOT / "latest"
    latest_dir.mkdir(parents=True, exist_ok=True)
    latest_json = latest_dir / json_path.name
    latest_csv = latest_dir / csv_path.name
    latest_md = latest_dir / md_path.name
    shutil.copyfile(json_path, latest_json)
    shutil.copyfile(csv_path, latest_csv)
    shutil.copyfile(md_path, latest_md)

    return {"json": json_path, "csv": csv_path, "markdown": md_path, "latest_markdown": latest_md}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--query", action="append", dest="queries", help="Search query to send to Startup Intros. Can be repeated.")
    parser.add_argument("--min-funding", type=float, default=8.0, help="Minimum disclosed funding in USD millions. Default: 8.")
    parser.add_argument("--min-age-years", type=int, default=2, help="Minimum company age in years. Default: 2.")
    parser.add_argument("--max-candidates", type=int, default=None, help="Stop after discovering this many unique company slugs.")
    parser.add_argument("--delay", type=float, default=0.25, help="Delay between HTTP requests in seconds. Default: 0.25.")
    parser.add_argument("--timeout", type=float, default=30.0, help="HTTP timeout in seconds. Default: 30.")
    parser.add_argument("--use-firecrawl", action="store_true", help="Use Firecrawl scrape markdown for company profile enrichment.")
    parser.add_argument(
        "--firecrawl-raw-content",
        action="store_true",
        help="Disable Firecrawl's LLM clean-content pass and use only main-content markdown.",
    )
    parser.add_argument("--date", default=date.today().isoformat(), help="Output date folder. Default: today.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    queries = args.queries or DEFAULT_QUERIES
    firecrawl_api_key = os.environ.get("FIRECRAWL_API_KEY", "")
    if args.use_firecrawl and not firecrawl_api_key:
        print("error: FIRECRAWL_API_KEY must be set when --use-firecrawl is used", file=sys.stderr)
        return 2

    records = analyze(
        queries=queries,
        min_funding_musd=args.min_funding,
        min_age_years=args.min_age_years,
        max_candidates=args.max_candidates,
        delay_seconds=args.delay,
        timeout_seconds=args.timeout,
        use_firecrawl=args.use_firecrawl,
        firecrawl_api_key=firecrawl_api_key,
        firecrawl_clean_content=not args.firecrawl_raw_content,
    )
    paths = write_outputs(
        records,
        output_date=args.date,
        min_funding_musd=args.min_funding,
        min_age_years=args.min_age_years,
        queries=queries,
    )
    apply_count = sum(1 for record in records if record.decision == "apply")
    print(f"Wrote {len(records)} analyzed companies, {apply_count} recommended.")
    for label, path in paths.items():
        print(f"{label}: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
