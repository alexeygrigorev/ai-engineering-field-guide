# Portfolio Section (repo: portfolio/)

- Sources: [portfolio/](../../portfolio/) - a seven-step guide to choosing, building, polishing, and presenting AI engineering portfolio projects
- Related: [portfolio projects concept](../concepts/portfolio-projects.md), [take-home assignments](../concepts/take-home-assignments.md), [role section](role.md) (the use-case and skills data the method is grounded in), [webinars](webinars.md)

## What the section says

A portfolio project should prove you can build, evaluate, and operate a small AI system for a real user - not demo a prompt. The method: start from a real domain and real companies, extract problems from job descriptions and engineering blogs, choose technology last, scope a finishable first version, and polish the README for a hiring manager who gives it minutes, not hours.

## Files covered

- [portfolio/README.md](../../portfolio/README.md) - the progression and the signal checklist: real user and problem, realistic inputs, tests, evaluation, logging, reproducible setup, README with decisions and trade-offs. The bar is grounded in the From RAG to Agents Buildcamp
- [portfolio/01-types-of-projects.md](../../portfolio/01-types-of-projects.md) - four project types (personal, role-targeted, take-home, hackathon/community/OSS) with what each signals and real examples from DataTalks.Club episodes and Reddit. Key data link: 86.9% of AI-First roles need skills beyond GenAI and 71.0% of AI-First roles need production/ops skills, so role-targeted projects must show build-evaluate-deploy-operate
- [portfolio/02-how-to-pick-a-project.md](../../portfolio/02-how-to-pick-a-project.md) - the seven-step selection workflow: five candidate domains (starting set from the use-case data: finance 3,877 mentions, healthcare 2,380, legal 1,798, education 1,349, cybersecurity 1,317) -> one domain -> 5-10 companies -> analyze JDs and blogs -> extract problems (user, input, output) -> ~five project candidates -> choose technologies last. "Technology-first projects often become buzzword demos"
- [portfolio/03-start-a-project.md](../../portfolio/03-start-a-project.md) - repo scaffolding before coding: `PROJECT_PLAN.md` with evidence links (target companies, JDs, blogs, datasets), problem statement, five candidates, selected project, build plan, version-1 definition including what it will NOT do, boring-stack defaults, one end-to-end path first
- [portfolio/04-polishing.md](../../portfolio/04-polishing.md) - README answers nine questions; code structure scannable; tests for deterministic behavior (one `pytest` command); evaluation for AI behavior (20-50 examples: easy, messy, out-of-scope, refusal, citation; metrics matched to project type; results saved in-repo with dates); local JSONL logging of requests, cost, latency; one demo format plus fallback screenshots; a final pre-share checklist
- [portfolio/05-present-the-project.md](../../portfolio/05-present-the-project.md) - the presentation layer: project page, 60-second pitch (problem, user, solution, evidence, ownership), the nine-part deep-dive order matching the [project deep dive interview](../../interview/questions/03-project-deep-dive.md), the "I chose X over Y because of constraint Z" decision structure, real failure stories (what broke / how found / what changed), honest evaluation discussion, precise ownership claims, prepared follow-up answers
- [portfolio/06-common-mistakes.md](../../portfolio/06-common-mistakes.md) - the failure catalog: picking technology first, random companies by brand, passive blog reading, no extracted problem, generic "chat with your documents", tools that don't fit, no evaluation plan, no monitoring plan, no repo plan. Ends with a nine-question quick check
- [portfolio/07-project-ideas.md](../../portfolio/07-project-ideas.md) - six worked domain exercises (finance, healthcare, legal, cybersecurity, developer tools, marketplace/e-commerce), each with real hiring companies and builtin.com job links, problems to look for, open-source repos to study (SEC Insights, ExtractThinker, Qodo PR Agent...), candidate projects, and likely technology - plus a study checklist. "Don't copy these projects"

## Key claims

- The repo gets you the interview; the explanation helps you use it (portfolio/05-present-the-project.md)
- Weak projects usually break before coding starts - skip problem discovery, evaluation, or a runnable repo plan and nothing downstream saves them (portfolio/06-common-mistakes.md)
- "It didn't work well enough, and I can explain why" beats a polished demo story (portfolio/05-present-the-project.md)

## What is actionable

- Run the seven-step selection workflow in portfolio/02 before writing any code
- Write the README for two audiences identified in [webinar 2](webinars.md): the peer reviewer who checks everything, and the hiring manager with 5-10 minutes
- An eval harness is part of version 1, not an enhancement
