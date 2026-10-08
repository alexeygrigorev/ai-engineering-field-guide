# Job Market Data

6,964 AI Engineer job descriptions from builtin.com (February - August 2026, 8 monthly scrapes) covering LA (Global), New York, London, Amsterdam, Berlin, and India.

For analysis and insights based on this data, see [role/](../role/).

## Contents

- [data_structured/](data_structured/) - LLM-enriched YAML files grouped into `YYYY-MM-DD/` scrape-date folders
- [data_raw/](data_raw/) - raw extracted YAML files grouped into `YYYY-MM-DD/` scrape-date folders
- [analysis.ipynb](analysis.ipynb) - Jupyter notebook with data analysis
- [_internal/](_internal/) - scraping scripts, processing scripts, and `_internal/data/` for pipeline CSVs
- [_internal/eval/](_internal/eval/) - how I check the LLM extraction is accurate, and what the last check found

## Startup Intros Company Shortlist

Run this periodically to refresh well-funded AI companies with evidence of traction:

```bash
cd ai-engineering-field-guide/job-market
uv run python _internal/find_startupintros_ai_companies.py
```

To enrich profile text through Firecrawl's rendered markdown scrape, put `FIRECRAWL_API_KEY` in `job-market/.env` and pass `--use-firecrawl`:

```bash
cd ai-engineering-field-guide/job-market
uv run python _internal/find_startupintros_ai_companies.py --use-firecrawl
```

The script searches Startup Intros, filters out companies below $8M disclosed funding, very new companies, weak AI-product matches, investor/fund profiles, inactive/acquired targets, and companies without concrete traction evidence. Outputs are written to `_internal/data/startupintros/YYYY-MM-DD/` and copied to `_internal/data/startupintros/latest/`.

## Highlights

- 4,874 jobs (70.0%) are AI-First (RAG, agents, LLMs)
- 1,685 jobs (24.2%) are AI-Support (platforms, infrastructure, tooling)
- 340 jobs (4.9%) are traditional ML rebranded as "AI Engineer"
- 2,499 unique companies, led by Capital One (120), Citi (98), Optum (90)

Top skills:

- Python (70.8%), TypeScript (19.5%), Java (17.7%)
- RAG (39.8%), prompt engineering (34.7%), CI/CD (36.8%)
- AWS (40.3%), Docker (24.4%), Kubernetes (24.0%)
- LangChain (22.0%), SQL (19.1%), PyTorch (18.2%)

Umbrella terms like "LLMs" and "Machine Learning" are excluded from this list - the extraction prompt tags them so broadly (any GenAI-adjacent posting) that their share reflects wording, not what the job actually needs. See [_internal/analysis/common.py](_internal/analysis/common.py) for the full skill taxonomy.

## Data Format

`data_raw/YYYY-MM-DD/{job_id}_{company}_{title}.yaml` holds what's parsed directly from the HTML, no LLM involved:

```yaml
job_id: 1393425
title: Applied AI Engineer & Researcher
company: Speechify
location: USA
work_type: FULL_TIME
level: Expert/Leader
skills: [Python, PyTorch, TensorFlow]
company_size: 96 Employees
description: |
  Full job description...
```

`data_structured/YYYY-MM-DD/{job_id}_{company}_{title}.yaml` is the same posting after LLM enrichment - classified, categorized, with responsibilities and use cases pulled out:

```yaml
company:
  name: Speechify
  stage: null
  focus: Text-to-speech reading and AI voice products
position:
  title: Applied AI Engineer & Researcher
  ai_type:
    type: ml-first
    reasoning: |-
      The core work is researching and building TTS and image-generation
      models, which is classical (non-LLM) ML. No LLM, prompt, retrieval,
      or agent component is named.
  responsibilities:
  - Research and implement state-of-the-art techniques in NLP, TTS, and CV
  - Deploy NLP or TTS models to production at large scale
  use_cases:
  - Text-to-speech conversion of PDFs, books, articles, and websites into audio
  skills:
    genai: []
    ml: [Machine Learning, PyTorch, TensorFlow]
    languages: [Python]
    domains: [NLP, TTS, Computer Vision, Image Generation]
    # ...other skill categories: web, databases, data, cloud, ops, other
  is_customer_facing: false
  is_management: false
meta:
  job_id: '1393425'
  location: USA
  extracted_at: '2026-08-15T20:53:40.880698'
  model: glm-5.2
  prompt_sha: ef6fdeb19af2
```

`meta.model` and `meta.prompt_sha` fingerprint which extractor produced the record - see [_internal/eval/](_internal/eval/) for why that matters.
