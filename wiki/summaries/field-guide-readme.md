# Field Guide Overview (repo: README.md and repo-meta files)

- Sources: [README.md](../../README.md), [CLAUDE.md](../../CLAUDE.md), [STYLING.md](../../STYLING.md)
- Related: [role](role.md), [interview](interview.md), [portfolio](portfolio.md), [learning paths](learning-paths.md), [webinars](webinars.md), [job-market](job-market.md), [awesome.md](awesome.md)

## What it says

The AI Engineering Field Guide is a data-driven guide to AI engineering roles, skills, and interviews: 9,760 real job descriptions, real interview experiences, and practitioner stories - explicitly positioned against AI-generated filler. The README is the repo's table of contents and maps its five content sections plus the dataset and the webinar series.

## Files covered

- [README.md](../README.md) - repo front door: the role section (7 files), interview preparation (5 chapters + 6 question categories + per-company data), learning paths (5 transitions), portfolio guide, job-market data (9,760 builtin.com postings across six geographies), awesome.md, and the five webinars. Also the author's channels: AI Shipping Blog, the From RAG to Agents Maven course, AI Shipping Labs
- [CLAUDE.md](../CLAUDE.md) - agent instructions: loads [STYLING.md](../../STYLING.md) and points any agent working in `wiki/` to the [wiki schema](../CLAUDE.md)
- [STYLING.md](../../STYLING.md) - repo writing conventions, which this wiki also follows: no bold, no italics, no horizontal rules; blank lines around lists; single-dash separators; links with descriptive text; one H1 per document; percentages with one decimal place; first person for research findings; tables only for small comparisons

## Key claims

- Everything in the guide is derived from data the repo itself collected - the [job-market pipeline](job-market.md) is the provenance for every role-section number
- The repo is the work of one author ([Alexey Grigorev](../entities/alexey-grigorev.md)) and doubles as the companion material for his courses and community

## What is actionable

- Treat README.md as the authoritative map of what exists; if a file is not reachable from it, flag it in a [lint](../CLAUDE.md) pass
- New top-level sections should be added both to README.md and to this wiki's [index](../index.md)
