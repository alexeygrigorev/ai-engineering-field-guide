# Job Market Data

895 job descriptions from builtin.com (January 2026) covering LA, NY, London, Amsterdam, and Berlin.

For analysis and insights based on this data, see [role/](../role/).

## Contents

- [data_structured/](data_structured/) - 895 structured YAML files with title, company, skills, compensation, and full descriptions
- [data_raw/](data_raw/) - 895 raw extracted YAML files from job postings
- [analysis.ipynb](analysis.ipynb) - Jupyter notebook with data analysis
- [_internal/](_internal/) - scraping scripts, processing scripts, CSVs

## Highlights

- 621 jobs (69.4%) are AI-First (RAG, agents, LLMs)
- 255 jobs (28.5%) are AI-Support (platforms, infrastructure, tooling)
- 16 jobs (1.8%) are traditional ML rebranded as "AI Engineer"
- 590 unique companies, led by Capital One (28), G2i (15), Scale AI (10)

Top skills:

- Python (82.5%), TypeScript (23.4%), Java (14.9%)
- RAG (35.9%), prompt engineering (29.1%), LLMs (25.4%)
- AWS (40.1%), Docker (31%), Kubernetes (29.1%)
- LangChain (18.8%), LangGraph (8.0%), LlamaIndex (5.8%)

## Data Format

Each YAML file in `data_structured/` contains:

```yaml
title: Senior AI/Data Engineer
company: WorkWave
location: USA
work_type: FULL_TIME
level: Expert/Leader
skills: [Python, AWS, Airflow, dbt]
company_size: 1,000 Employees
compensation: $160,000 - $180,000/year
description: |
  Full job description...
posted_date: 2026-01-18
url: https://builtin.com/job/...
source: Built In
```
