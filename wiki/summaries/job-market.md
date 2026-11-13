# Job Market Data Project (repo: job-market/)

- Sources: [job-market/README.md](../../job-market/README.md), [job-market/_internal/PIPELINE.md](../../job-market/_internal/PIPELINE.md), [job-market/_internal/extract_process.md](../../job-market/_internal/extract_process.md), [job-market/_internal/eval/README.md](../../job-market/_internal/eval/README.md)
- Related: [role section](role.md), [LLM wiki pattern](../concepts/llm-wiki-pattern.md) (the pipeline is the data engine feeding every role claim in this wiki)

## What it is

A scraping-and-extraction pipeline that produced the dataset behind the whole role analysis: 9,760 job descriptions from builtin.com (LA, NY, London, Amsterdam, Berlin, India), 10 monthly scrapes from Feb 4 to Nov 6, 2026, no job-ID overlap between scrapes - each month is an independent cross-section of the market, not a panel. Data lives in `data_raw/` (parsed from HTML, no LLM) and `data_structured/` (LLM-enriched: classification, responsibilities, use cases, categorized skills). The `data_*` directories and `_internal` scripts are raw material per the [schema](../CLAUDE.md) - this page covers the documents that describe them.

## Files covered

- [job-market/README.md](../../job-market/README.md) - dataset overview, highlights (68.9% AI-First, 3,112 unique companies led by Speechify/Capital One/Citi), YAML format for both data layers, and the `meta.model`/`meta.prompt_sha` fingerprinting that makes a mixed extractor corpus visible
- [job-market/_internal/PIPELINE.md](../../job-market/_internal/PIPELINE.md) - the five-step pipeline: scrape listings (requests + DataImpulse proxy) -> dedup -> download HTML -> extract to YAML (JSON-LD first, HTML fallback) -> LLM enrichment via Z.ai/GLM. Plus location handling (from JSON-LD, never from the LLM), dedup strategy, and the warning that changing the model or prompt silently rewrites what the numbers mean - the glm-5.1 to glm-5.2 switch moved AI-First share by up to 10 points that were not real
- [job-market/_internal/extract_process.md](../../job-market/_internal/extract_process.md) - the extraction design: skill categories and normalization rules, the ai-first vs ai-support classification logic (primary work focus; cloud/data/infra skills appear in both), worked examples (LangChain AI Engineer = ai-first, Snowflake AI Account Engineer = ai-support, AI Data Engineer = usually ai-support), and edge cases (FDE usually ai-first)
- [job-market/_internal/eval/README.md](../../job-market/_internal/eval/README.md) - how the extraction is validated: a 50-job stratified blind A/B of old vs new extraction (new preferred on 38/50; classification 98.0% clean vs 78.0%; skill hallucination cut from 74 invented skills to 4), plus two judge-free probes that run on every scrape (duplicate-description consistency 95.6%, named-tool recall 98.6%). Honest limits section: the judge is the author, the blind partially leaked, and two fields (`is_management`, `company_stage`) are unreliable in both extractions - the company-stage analysis rests on ~80% inferred data

## Key claims

- Measurement discipline is a first-class concern: extraction model/prompt changes are treated as instrument changes that must be evaluated before numbers are quoted (eval/README.md)
- Skills percentages are a floor, not a ceiling - a skill the description doesn't spell out is not counted (role/02-skills.md, measurement note)
- The corpus is stamped (`meta.model`, `meta.prompt_sha`) so longitudinal analysis can separate extractor drift from market drift

## What is actionable

- Before quoting any number from `data_structured/`, check the eval README's caveats - especially avoid `is_management` and `company_stage`
- Reproducing the pipeline for a new month is a documented seven-step runbook in PIPELINE.md
- The eval methodology (stratified blind A/B + judge-free consistency/recall probes + burned regression seeds) is a reusable pattern for any LLM-extraction dataset
