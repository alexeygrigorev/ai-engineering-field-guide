# Index

Catalog of every page in the wiki. Read this first when answering queries; updated on every operation. Maintained per the schema in [CLAUDE.md](CLAUDE.md). For the mapping of repo files to wiki pages, see [answers/repo-content-map.md](answers/repo-content-map.md).

## Overviews

- [overview.md](overview.md) - front door: main threads, current synthesis, open questions

## Sources

### External

- [LLM Wiki (Karpathy, April 2026)](summaries/2026-04-karpathy-llm-wiki.md) - persistent LLM-maintained wiki as an alternative to RAG; source of the pattern this wiki follows ([raw](raw/2026-04-karpathy-llm-wiki.md))

### Repo corpus (ingested 2026-09-09)

- [Field guide overview](summaries/field-guide-readme.md) - README plus repo-meta files (CLAUDE.md, STYLING.md): what the repo is and its conventions
- [Role section](summaries/role.md) - the AI engineer role from 9,760 job descriptions: role types, skills, responsibilities, use cases, FDE, trends
- [Interview section](summaries/interview.md) - process structure, question bank (six categories), getting hired, after the interview, 2026 trends
- [Portfolio section](summaries/portfolio.md) - the seven-step project method: types, selection, start, polish, present, mistakes, worked ideas
- [Learning paths](summaries/learning-paths.md) - the core curriculum and five role-to-role transition guides
- [Webinars](summaries/webinars.md) - five webinars (Feb-Jun 2026) with the Q&A positions the written sections don't take
- [Job-market project](summaries/job-market.md) - the scraping/extraction pipeline, its data contract, and the extraction eval discipline
- [Awesome AI Engineering](summaries/awesome.md) - the curated resource list; the wiki's reading queue

## Concepts

- [LLM wiki pattern](concepts/llm-wiki-pattern.md) - three layers (raw sources / wiki / schema) and three operations (ingest / query / lint)
- [AI engineer role](concepts/ai-engineer-role.md) - integrator not trainer; AI-First/AI-Support/ML split; full-stack applied; five archetypes; the integrator-vs-trainer shift
- [Interview process](concepts/interview-process.md) - the 3-6 round funnel, six round types, what interviewers actually test, AI on both sides of the table
- [Take-home assignments](concepts/take-home-assignments.md) - what the 100+ assignment corpus asks for, how submissions are graded, what gets offers
- [Portfolio projects](concepts/portfolio-projects.md) - domain-first selection, scoped first version, README for two audiences, honest presentation
- [Evaluation as the differentiator](concepts/evaluation-differentiator.md) - the one claim every repo section makes: measuring AI systems is the scarce skill

## Entities

- [Alexey Grigorev](entities/alexey-grigorev.md) - author of the field guide, host of the webinars, his channels and stated positions

## Answers

- [Repo content map](answers/repo-content-map.md) - every authored file in the repo and where the wiki covers it

## Sibling

- The market wiki - generated data views over the raw job-description dataset (skills, use cases, industries, companies, trends) with charts - moved to the AISL wiki repo ([AI-Shipping-Labs/wiki](https://github.com/AI-Shipping-Labs/wiki), `market-wiki/`) on 2026-09-16; regenerated there by script on each new scrape
