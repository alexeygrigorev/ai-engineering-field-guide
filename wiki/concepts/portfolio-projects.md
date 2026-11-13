# Portfolio Projects

The repo's method for choosing, building, and presenting AI engineering portfolio projects. Sources: [portfolio section](../summaries/portfolio.md) (primary), [webinars 2 and 5](../summaries/webinars.md), [interview/03](../summaries/interview.md).

## The core principle

Start from a real domain, real companies, and real problems; choose the technology last. "I want to build a RAG app" is not a project idea - technology-first projects become buzzword demos.

## The selection method

The seven-step workflow ([portfolio/02](../../portfolio/02-how-to-pick-a-project.md), six-step in the [webinar 5](../summaries/webinars.md) version):

1. Pick five candidate domains - the data-backed starting set is finance, healthcare, legal, education, cybersecurity (the top domains in 43,822 extracted use cases)
2. Select one domain - check companies are hiring, publishing, and buildable-with-public-data
3. Pick 5-10 companies
4. Analyze their job descriptions and engineering blogs - JDs show what teams want; blogs show what teams actually do
5. Extract problems, not project ideas - each names user, input, output ("Support teams need to answer refund questions from policy documents without inventing policy")
6. Create ~five project candidates in the domain, varying the type
7. Choose technologies per candidate - RAG when answers must be grounded, agents when action is needed, structured output for validated fields, deterministic code when no LLM is needed

Prefer problems shared by several companies - one project then serves many interviews.

## What version 1 must include

One end-to-end path, an evaluation harness (20-50 examples: easy, messy, out-of-scope, refusal, citation cases), tests for deterministic behavior, local logging (request ID, model, prompt version, sources, latency, cost), and a README a hiring manager understands in under a minute. Also define what version 1 will not do.

## The hiring-manager reality

From the author's own hiring experience ([webinar 2](../summaries/webinars.md)): 5-10 minutes of attention, README first, checkboxes - solves a real problem, clear description, signs of production proximity (tests, evaluation, CI/CD, demo). Write for two audiences: the thorough peer reviewer and the time-starved hiring manager. Tutorial copies are worthless; original problem-driven projects carry enormous value. Commit history is never read.

## Presentation

The repo gets you the interview; the explanation wins it: a 60-second pitch (problem, user, solution, evidence, ownership), a deep dive ordered to match the [project deep dive interview](interview-process.md), decision stories in the form "I chose X over Y because of constraint Z", and honest failure stories (what broke / how found / what changed). Impact can be modest - "it didn't work well enough, and I can explain why" beats a solved-everything demo.

## Project types

Personal utility (shows builder mindset), role-targeted (the hiring workhorse), take-homes republished as portfolio pieces, and hackathon/community/OSS work (external review is the extra signal) - see [portfolio/01](../../portfolio/01-types-of-projects.md) for real examples of each.

## Inference (my synthesis)

- The method is essentially applied market research: the same job-description corpus that powers the [role analysis](ai-engineer-role.md) becomes the project-selection instrument - which is why portfolio projects in this repo are expected to cite evidence links in `PROJECT_PLAN.md`
- The evaluation-first rule makes the portfolio a rehearsal of the job itself: every differentiator named in [evaluation as the differentiator](evaluation-differentiator.md) is something a project can demonstrate
