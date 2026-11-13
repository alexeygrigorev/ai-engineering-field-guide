# Wiki Schema

This directory is an LLM-maintained knowledge wiki following the LLM Wiki pattern (see `raw/2026-04-karpathy-llm-wiki.md`). The human curates sources and asks questions; the LLM does the reading, summarizing, cross-referencing, filing, and bookkeeping. The goal is a persistent, compounding artifact: cross-references exist before anyone asks for them, contradictions are flagged when they appear, and synthesis reflects everything ingested so far.

## Scope

- Default domain: AI engineering - the subject of this repo (practitioner stories, architecture patterns, RAG, agents, evals, context engineering, cost engineering, job market).
- The human can point the wiki at any topic by dropping sources in `raw/` - the same structure and operations apply.

## Layout

- `raw/` - immutable source documents fetched from outside the repo. Never edit these; they are the source of truth for external claims.
- `summaries/` - one page per source: one page per standalone document (filename mirroring the file), or one page per section for a multi-file directory, with a per-file block covering every file.
- `concepts/` - one page per concept or technique (e.g. `concepts/llm-wiki-pattern.md`).
- `entities/` - one page per person, company, or product.
- `answers/` - reusable answers filed back after queries.
- `overview.md` - the front door: main threads, current synthesis, open questions.
- `index.md` - catalog of every page with a one-line summary.
- `log.md` - append-only record of ingests, queries, and lint passes.
- `CLAUDE.md` - this schema; co-evolve it when a convention changes.

## Repo sources

The repo's own documents are sources too - the primary ones. They stay where they are instead of being copied into `raw/`: git history already makes them immutable, and duplication would create sync drift. A relative repo path (`../role/02-skills.md`) is a first-class source link.

- Authored content gets summarized: root docs, `role/`, `interview/` (including `questions/`), `portfolio/`, `learning-paths/`, `webinars/`, and the `job-market/` README plus pipeline docs.
- Data and code directories are raw research material: `job-market/data_raw/`, `job-market/data_structured/`, `job-market/_internal` scripts, `interview/data/`, `portfolio/_internal/`, `_work-in-progress/`, `.tmp/`. Reference them; never summarize them page by page. The summaries cover the documents that interpret them.
- Numbers extracted from the job-market dataset are tied to a scrape window (Feb 4 - Nov 6, 2026, 10 monthly scrapes of builtin.com) - cite the window and the analysis file, since each monthly scrape is a fresh cross-section of the market.

## Rules

1. Never modify anything in `raw/`.
2. Every claim on a wiki page links back to its source (the raw file or the original URL).
3. Read `index.md` first when answering; do not load the whole wiki when the index settles navigation.
4. Update `index.md` and append to `log.md` on every operation - no exceptions.
5. Flag contradictions inline where both claims live; never silently resolve them.
6. No copied state: mutable values (prices, version numbers, benchmark scores, headcounts) must carry the date they were true and a source link.
7. Mark my own synthesis as inference; keep it separate from what sources say.
8. One concept, one page - update the existing page instead of creating near-duplicates.
9. Follow the repo `STYLING.md` formatting: no bold, no italics, no horizontal rules, blank lines around lists.

## Operations

### Ingest

Trigger: the human drops a file into `raw/` (or hands over a URL to fetch into `raw/`) and asks to process it.

1. Read the source in full.
2. Discuss key takeaways with the human before writing, unless batch mode was requested.
3. Write `summaries/<slug>.md`: what the source says, key claims with dates, what is actionable, links to related pages.
4. Update or create the `concepts/` and `entities/` pages the source touches, with cross-links in both directions. A single source can legitimately touch 10-15 pages.
5. Revise `overview.md` if the source shifts a main thread or answers an open question.
6. Add new pages to `index.md` with one-line summaries.
7. Append to `log.md`.

### Query

Trigger: the human asks a question.

1. Read `index.md`, pick the likely pages, read those - not the whole wiki.
2. Open raw sources only when summaries cannot settle the question.
3. Answer with links to the pages and sources used, and state uncertainty where it exists.
4. If the answer is reusable (a comparison, an analysis, a discovered connection), file it as `answers/<slug>.md`, link it from related pages, update `index.md`, and log it. Answers should not evaporate into chat history.

### Lint

Trigger: periodically, or when the human asks for a health check.

Check for:

- Contradictions between pages
- Stale claims that newer sources have superseded
- Orphan pages with no inbound links
- Concepts mentioned repeatedly but lacking their own page
- Missing cross-references
- Gaps that a web search could fill

Fix what is mechanical, list what needs human input, and log the pass.

## Log format

Every entry starts with `## [YYYY-MM-DD] <operation> | <subject>` so the log stays greppable: `grep "^## \[" log.md | tail -5`.
