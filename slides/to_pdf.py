"""Convert reveal.js slides to PDF using Playwright."""

import sys
import asyncio
from pathlib import Path

from playwright.async_api import async_playwright


async def convert(html_path: str, pdf_path: str | None = None):
    html_file = Path(html_path).resolve()
    if not html_file.exists():
        print(f"File not found: {html_file}")
        sys.exit(1)

    if pdf_path is None:
        pdf_path = str(html_file.with_suffix(".pdf"))

    url = f"file://{html_file}?print-pdf"

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        await page.goto(url, wait_until="networkidle")
        await page.wait_for_timeout(2000)

        await page.pdf(
            path=pdf_path,
            width="1200px",
            height="700px",
            print_background=True,
            prefer_css_page_size=True,
        )

        await browser.close()

    print(f"Saved to {pdf_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python to_pdf.py <slides.html> [output.pdf]")
        sys.exit(1)

    html = sys.argv[1]
    pdf = sys.argv[2] if len(sys.argv) > 2 else None
    asyncio.run(convert(html, pdf))
