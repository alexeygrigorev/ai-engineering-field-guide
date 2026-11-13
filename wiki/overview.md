# Overview

This is an LLM-maintained knowledge wiki for AI engineering, following the [LLM wiki pattern](concepts/llm-wiki-pattern.md). The human curates sources and asks questions; the LLM writes and maintains every page here per the schema in [CLAUDE.md](CLAUDE.md). Start at [index.md](index.md) to see everything the wiki contains.

The wiki's first corpus is the repo itself: the [AI Engineering Field Guide](../README.md), ingested 2026-09-09. Every authored repo file is summarized in [summaries/](summaries/) and mapped in [answers/repo-content-map.md](answers/repo-content-map.md).

## Main threads

- Defining the AI engineer role - the data-driven answer: an integrator role (RAG, agents, orchestration via provider APIs), 68.9% AI-First, full-stack, applied; fine-tuning niche; five role archetypes; the integrator-vs-trainer shift is the strongest trend. See [AI engineer role](concepts/ai-engineer-role.md) and the [role summary](summaries/role.md)
- Getting hired - a non-standardized interview process converging on consistent signals: evaluation thinking, ownership narratives, production awareness; take-homes as the de facto practical exam; a domain-first portfolio method. See [interview process](concepts/interview-process.md), [take-home assignments](concepts/take-home-assignments.md), [portfolio projects](concepts/portfolio-projects.md)
- Evaluation as the differentiator - the claim every section of the repo makes independently; collected in one page: [evaluation as the differentiator](concepts/evaluation-differentiator.md)
- Transitions - the role is entered from adjacent roles (ML engineer easiest, then backend, data engineer, data scientist, frontend), all converging on the same shortlist: LLM APIs, RAG, agents, evaluation. See [learning paths](summaries/learning-paths.md)
- The measurement engine - the job-market scraping and LLM-extraction pipeline, its eval discipline, and its known caveats (unreliable `is_management`/`company_stage` fields). See [job-market](summaries/job-market.md)
- The market data itself - a generated wiki that aggregates the raw postings directly (skills, use cases, industries, companies, seniority, month-over-month trends) into pages, SVG charts, and a dashboard; it moved to the AISL wiki repo ([AI-Shipping-Labs/wiki](https://github.com/AI-Shipping-Labs/wiki), `market-wiki/`) on 2026-09-16 and is regenerated there whenever a new scrape lands
- The LLM wiki pattern itself - the wiki's operating system, seeded from Karpathy's April 2026 gist: [LLM wiki pattern](concepts/llm-wiki-pattern.md)

## Current synthesis

The repo's sections agree on a single picture of the 2026 market: AI engineering has consolidated into a software-engineering specialization - build reliable systems on top of pre-trained models for enterprise automation use cases. Hiring (interviews, take-homes, portfolios) selects for the ability to measure and operate such systems, not to train models. The demand data (61.8% of AI-First roles requiring evaluation skills; junior postings pinned near 1%) says the role is a second specialization layered on engineering experience, and the learning paths are built exactly for that reader.

## Open questions

- Which [awesome.md](summaries/awesome.md) sources to ingest into `raw/` first - the list is the wiki's reading queue and ingesting it is the main growth path
- The gap between job descriptions and day-to-day work rests on thin qualitative data (one viral tweet plus discussion threads) - more first-person candidate/engineer accounts would strengthen [reality vs postings](summaries/role.md)
- Junior share (~1%) and the Staff+ decline - is this measurement (titles unbundling) or a real closed entry ladder? Worth a dedicated query against the dataset
- `is_management` and `company_stage` in `data_structured/` are unreliable in both extractions pending re-extraction - do not quote until then ([job-market](summaries/job-market.md))
- At what scale the index stops being enough and a search tool (e.g. qmd) becomes worth adding
