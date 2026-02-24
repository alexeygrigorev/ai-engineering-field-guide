# Defining the AI Engineer Role

Analysis of what AI engineers actually do, based on 895 job descriptions from builtin.com (January 2026).

## Key Takeaways

### What is an "AI Engineer" in 2026?

- It's a new role, distinct from ML Engineer. AI engineers integrate pre-trained models into applications (RAG, agents, orchestration). ML engineers train models. But titles are broken - "AI Engineer" means different things at different companies.
- Three types of roles hide under the same title:
  - AI-First (69.4%) - builds RAG systems, agents, LLM-powered features
  - AI-Support (28.5%) - builds platforms, infrastructure, tooling for AI teams
  - ML (1.8%) - traditional ML rebranded
- It's fundamentally a full-stack role. 93.1% of roles need skills beyond GenAI. Only 1.4% expect pure GenAI work. You need cloud, Docker, CI/CD, often web development too.

### What they actually build

- RAG + Agents dominate. RAG appears in 35.9% of all jobs, agents in 14.4%. Together they cover 70%+ of use cases. If you learn these two patterns deeply, you cover most of the work.
- The #1 problem AI solves is automating manual workflows (15.4% of use cases). Not glamorous - it's reducing repetitive work at scale.
- Knowledge access is universal. Every domain (healthcare, legal, finance, enterprise) has the same problem: too much information, can't find what's needed. RAG solves this everywhere.

### Skills that matter

- Python is mandatory (82.5%). After that: AWS (40.1%), RAG (35.9%), Docker (31.0%), prompt engineering (29.1%), Kubernetes (29.1%).
- Fine-tuning is overhyped. Only 4.0% of roles focus on it as a primary responsibility. 80.8% don't mention it at all. Focus on RAG and agents first.
- 64.3% still require some ML knowledge - but it's practical ML (PyTorch basics, fine-tuning, embeddings), not deep research expertise.

### What actually gets you hired

- Evaluation is the differentiator. 39.6% of AI-First roles explicitly require evaluation skills. Anyone can build a chatbot - companies hire people who can measure if it works (LLM-as-judge, golden datasets, hallucination detection).
- Production thinking wins over accuracy obsession. 50.2% of AI-First roles require production/ops skills (Docker, Kubernetes, CI/CD, MLOps, Terraform). "deploy" appears in 565 of 5,694 responsibilities, "monitor" in 258.
- 95.6% of roles are applied/production, not research. Only 4.4% are research roles. The market wants people who ship, not people who publish.


## Contents

1. [My vision of the role](01-my-vision.md) - how I see AI engineering, comparison with DS/ML/DE roles, CRISP-DM for AI
2. [Skills analysis](02-skills.md) - top skills, job types, cloud platforms, frameworks
3. [Responsibilities](03-responsibilities.md) - 5,694 extracted responsibilities across 895 jobs
4. [Use cases](04-use-cases.md) - 4,525 real use cases showing what companies build with AI
5. [Reality vs. job postings](05-reality-vs-postings.md) - what candidates experience vs. what's advertised
