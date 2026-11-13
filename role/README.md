# Defining the AI Engineer Role

Analysis of what AI engineers actually do, based on 9,760 job descriptions from builtin.com, collected in 10 monthly scrapes between February and November 2026.

## Contents

1. [My vision of the role](01-my-vision.md) - how I see AI engineering, comparison with DS/ML/DE roles, CRISP-DM for AI
2. [Skills analysis](02-skills.md) - top skills, job types, cloud platforms, frameworks
3. [Responsibilities](03-responsibilities.md) - 69,498 extracted responsibilities across 9,760 jobs
4. [Use cases](04-use-cases.md) - 43,822 real use cases showing what companies build with AI
5. [Reality vs. job postings](05-reality-vs-postings.md) - what candidates experience vs. what's advertised
6. [Forward Deployed Engineers](06-fde.md) - growth, responsibilities, and skills from 277 FDE job postings
7. [Trends](07-trends.md) - month-over-month analysis of role archetypes, skill stacks, and trajectories across 10 scrapes ([appendix](08-trends-appendix.md))

## Key Takeaways

### What is an "AI Engineer" in 2026?

- It's a new role, distinct from ML Engineer. AI engineers integrate pre-trained models into applications (RAG, agents, orchestration). ML engineers train models. But titles are broken - "AI Engineer" means different things at different companies.
- Three types of roles hide under the same title:
  - AI-First (68.9%) - builds RAG systems, agents, LLM-powered features
  - AI-Support (25.7%) - builds platforms, infrastructure, tooling for AI teams
  - ML (4.5%) - traditional ML rebranded
- It's fundamentally a full-stack role. 86.9% of AI-First roles need skills beyond GenAI. Only 4.0% expect pure GenAI work. You need cloud, Docker, CI/CD, often web development too.

### What they actually build

- RAG + Agents dominate. RAG appears in 40.1% of all jobs, agents (any) in 56.2%. If you learn these two patterns deeply, you cover most of the work.
- The #1 problem AI solves is automating manual workflows (58.8% of jobs) and internal operational efficiency (22.5% of use cases). Not glamorous - it's reducing repetitive work at scale.
- Knowledge access is universal. Every domain (healthcare, legal, finance, enterprise) has the same problem: too much information, can't find what's needed. RAG solves this everywhere.

### Skills that matter

- Python is mandatory (71.6%). After that: AWS (39.3%), RAG (40.1%), CI/CD (36.9%), prompt engineering (34.8%), Azure (29.7%).
- Fine-tuning is overhyped. Only 3.2% of AI-First roles focus on it as a primary responsibility. 86.0% don't mention it in responsibilities at all. Focus on RAG and agents first.
- 53.3% of AI-First roles still require some ML knowledge - but it's practical ML (PyTorch basics, fine-tuning, embeddings), not deep research expertise.

### What actually gets you hired

- Evaluation is the differentiator. 61.8% of AI-First roles explicitly require evaluation skills - the majority all year, climbing to 69.3% in November. Anyone can build a chatbot - companies hire people who can measure if it works (LLM-as-judge, golden datasets, hallucination detection).
- Production thinking wins over accuracy obsession. 71.0% of AI-First roles combine GenAI with production/ops skills (Docker, Kubernetes, CI/CD, MLOps, Terraform).
- 97.4% of roles are applied/production, not research. Only 2.6% are research roles. The market wants people who ship, not people who publish.

