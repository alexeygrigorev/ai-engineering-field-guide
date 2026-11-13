# Log

Append-only record of wiki operations. Each entry starts with `## [YYYY-MM-DD] <operation> | <subject>` so the history is greppable: `grep "^## \[" log.md | tail -5`.

## [2026-09-09] ingest | LLM Wiki (Karpathy, April 2026)

- First wiki operation: initialized the wiki structure per the pattern and ingested the pattern's own source document
- Fetched the gist into [raw/2026-04-karpathy-llm-wiki.md](raw/2026-04-karpathy-llm-wiki.md)
- Wrote [summaries/2026-04-karpathy-llm-wiki.md](summaries/2026-04-karpathy-llm-wiki.md) and [concepts/llm-wiki-pattern.md](concepts/llm-wiki-pattern.md)
- Created the schema ([CLAUDE.md](CLAUDE.md)), [overview.md](overview.md), [index.md](index.md), and this log

## [2026-09-09] ingest | repo corpus (the AI Engineering Field Guide itself)

- Goal: build the wiki out from the repo's own files. Read all authored content end to end: root docs, `role/` (9), `interview/` (13 including `questions/`), `portfolio/` (8), `learning-paths/` (6), `webinars/` (6 + slides), `job-market/` docs (4), `awesome.md`
- Co-evolved the schema: repo documents are sources in place (relative paths are source links; git provides immutability); data/code directories are raw material; dataset numbers carry the Feb 4 - Aug 25, 2026 scrape window
- Wrote 8 summary pages: [role](summaries/role.md), [interview](summaries/interview.md), [portfolio](summaries/portfolio.md), [learning-paths](summaries/learning-paths.md), [webinars](summaries/webinars.md), [job-market](summaries/job-market.md), [awesome](summaries/awesome.md), [field-guide-readme](summaries/field-guide-readme.md)
- Wrote 5 concept syntheses: [ai-engineer-role](concepts/ai-engineer-role.md), [interview-process](concepts/interview-process.md), [take-home-assignments](concepts/take-home-assignments.md), [portfolio-projects](concepts/portfolio-projects.md), [evaluation-differentiator](concepts/evaluation-differentiator.md)
- Wrote 1 entity page: [alexey-grigorev](entities/alexey-grigorev.md)
- Filed the verification artifact: [answers/repo-content-map.md](answers/repo-content-map.md) mapping every authored file to its wiki coverage
- Rewrote [overview.md](overview.md) (six main threads, current synthesis, five open questions) and [index.md](index.md)
- Deliberately not summarized page-by-page (raw material per the schema): `job-market/data_*`, `job-market/_internal` scripts, `interview/data/`, `portfolio/_internal/`, `webinars/slides/` (presentation artifacts), `_work-in-progress/`, `.tmp/`

## [2026-09-09] create | sibling market-wiki over the job-description dataset

- Built [../market-wiki/](../market-wiki/README.md): a generated data view of the 6,964 postings in `data_structured/` - skills, use-case themes, industries, companies, locations, seniority, and month-over-month trends, as markdown pages plus 9 SVG charts and an HTML dashboard
- The generator (`market-wiki/generate.py`, deterministic, no LLM calls) is the update path: rerun after each new scrape and it rebuilds every page and chart; its log records each run
- Cross-checked its output against this wiki's analysis: AI-First 70.0%, MCP 9.9% to 17.6%, LangGraph rising, PyTorch falling - all match [role](summaries/role.md)
- Industries and use-case themes there are keyword classifiers (the dataset has no industry field), flagged as approximations on the pages; numbers quoted in this wiki still come from the repo's own analysis
- Linked from the [overview](overview.md) main threads; this wiki remains the synthesis layer, market-wiki the data layer

## [2026-09-16] move | market-wiki relocated to AI-Shipping-Labs/wiki

- The generated market wiki moved out of this repo into the AISL wiki repo ([AI-Shipping-Labs/wiki](https://github.com/AI-Shipping-Labs/wiki), `market-wiki/`) so all member-facing wiki material sits in one place
- This repo keeps the dataset (`job-market/data_structured/`) and the synthesis (`wiki/`); the generator now runs from the wiki repo (`uv run python market-wiki/generate.py`) against this repo's dataset
- Removed `market-wiki/` and updated the live references in [overview](overview.md), [index](index.md), [repo-content-map](answers/repo-content-map.md), and `serve_wiki.py`; the 2026-09-09 create entry above stays as history

## [2026-11-13] update | refresh analyses from 9,760-job corpus (through 2026-11-06)

- Re-ran `job-market/analysis.ipynb`, `charts.py`, `trends.py`, `deep_trends.py`, `deep_trends2.py`, `extract_responsibilities.py`, `extract_use_cases.py`, and supporting analysis scripts across all 10 scrapes (Feb 4 - Nov 6, 2026, 9,760 postings)
- Updated `README.md`, `job-market/README.md`, `role/README.md`, `role/02-skills.md`, `role/03-responsibilities.md`, `role/04-use-cases.md`, `role/05-reality-vs-postings.md`, `role/06-fde.md`, `role/07-trends.md`, `role/08-trends-appendix.md`, and regenerated `job-market/images/*.png`
- Synced wiki pages ([overview](overview.md), [index](index.md), [AGENTS.md](AGENTS.md), [summaries/role](summaries/role.md), [summaries/job-market](summaries/job-market.md), [summaries/field-guide-readme](summaries/field-guide-readme.md), [concepts/ai-engineer-role](concepts/ai-engineer-role.md), [concepts/evaluation-differentiator](concepts/evaluation-differentiator.md), [entities/alexey-grigorev](entities/alexey-grigorev.md))

## [2026-11-13] lint | complete 9,760-job refresh across remaining role, learning-paths, portfolio, and wiki pages

- Completed the remaining category, domain, and word-count updates in `role/03-responsibilities.md` (all 17 responsibility categories, Key Insights, and top words) and `role/04-use-cases.md` (remaining 8 use-case categories, 7 domains served, Key Insights, and top words)
- Restored the 8-bullet FDE responsibility breakdown for the 277 unique FDE roles in `role/06-fde.md` and documented the 277 vs 287 pattern difference with `role/07-trends.md` / `role/08-trends-appendix.md`
- Updated stale 895-job and 4,894-job figures in `role/01-my-vision.md`, `role/05-reality-vs-postings.md`, `learning-paths/README.md`, `portfolio/01-types-of-projects.md`, `portfolio/02-how-to-pick-a-project.md`, [concepts/portfolio-projects](concepts/portfolio-projects.md), and [summaries/portfolio](summaries/portfolio.md)
