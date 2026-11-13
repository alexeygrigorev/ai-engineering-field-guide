# AI Engineer Role

What "AI engineer" actually denotes in the 2026 job market, synthesized across the repo's data sections. Sources: [role section](../summaries/role.md) (primary), [webinars 1-2](../summaries/webinars.md), [learning paths](../summaries/learning-paths.md), [field guide overview](../summaries/field-guide-readme.md).

## The definition

An AI engineer integrates AI into the product. The model already exists - work happens through provider APIs (OpenAI, Anthropic) - so the job is engineering: prompt design and versioning, RAG, agents, evaluation, deployment, monitoring. "An AI engineer is first and foremost an engineer. The AI part comes second." ([role/01-my-vision.md](../../role/01-my-vision.md), [learning-paths/from-backend-engineer.md](../../learning-paths/from-backend-engineer.md))

## The three role types under one title

From 9,760 postings, Feb-Nov 2026 ([role/02-skills.md](../../role/02-skills.md)):

- AI-First - 68.9%: works ON AI (RAG systems, agents, LLM features)
- AI-Support - 25.7%: works NEAR AI (platforms, infrastructure, tooling, UIs for AI products)
- ML - 4.5%: traditional ML rebranded with the AI title

The test: does the role work on AI systems or near them? Titles are unreliable - "AI Engineer" is the most trustworthy title (92% AI-First) while "AI Platform Engineer" is a coin flip. Candidate reports confirm the confusion from the other side ([role/05-reality-vs-postings.md](../../role/05-reality-vs-postings.md)).

## Full-stack and applied

- 86.9% of AI-First roles need skills beyond GenAI; 71.0% combine GenAI with production/ops (Docker, Kubernetes, CI/CD); only 4.0% expect pure GenAI work
- 97.4% of roles are applied/production, not research
- Python is mandatory (71.6%); one cloud (AWS 39.3% > Azure 29.7% > GCP 29.1%) is the norm

## What the work actually is

- RAG (40.1% of all jobs) and agents (56.2%) are the two dominant patterns, usually asked together
- The #1 use case is automating manual workflows (58.8% of jobs) and internal operational efficiency (22.5% of mentions) - unglamorous reduction of repetitive work at scale
- Five role archetypes from clustering ([role/07-trends.md](../../role/07-trends.md)): agent builder 29.9%, RAG app builder 26.6%, DevOps/full-stack 16.9%, cloud/ML platform 14.1%, ML trainer/researcher 6.3%

## The directional shift

The strongest signal in the dataset (Feb -> Nov 2026): within AI-First roles the integrator stack (RAG/agents/APIs) rose from 80.0% to 91.7% while the trainer stack (PyTorch/TensorFlow/fine-tuning/CUDA) fell from 37.5% to 27.2%. Fine-tuning is a specialization, not core: 86.0% of AI-First roles never mention it in responsibilities. The dedicated "AI infra engineer" has not emerged - inference/serving work fell to 13.5% and stays inside platform roles. Meanwhile the FDE variant - customer-facing production deployers - grew 5.9x across the 10 scrapes.

## Comparison with adjacent roles

- ML engineer - owns model weights; AI engineer calls APIs. "Replace a call to a locally hosted model with a call to OpenAI - the rest is the same." Easiest transition into the role
- Data scientist - owns model creation and experiments; AI engineers do no real modeling. DS bring evaluation mindset (their advantage) and must add engineering
- Software engineer - the base identity; adds AI-specific skills: prompt engineering/versioning, RAG, agents, LLM-specific evaluation and monitoring

## Inference (my synthesis, not a source claim)

- Reading the repo together: the role is consolidating around "software engineer who ships reliable LLM systems" - every section independently converges on evaluation plus production skills as what separates candidates, while model-training skills fade
- The junior market being pinned near 1% of postings all 10 scrapes, combined with full-stack expectations, suggests the role is hired as a second specialization, not an entry point - consistent with the [learning paths](../summaries/learning-paths.md) premise that you transition from an adjacent role
