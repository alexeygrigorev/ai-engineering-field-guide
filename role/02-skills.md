# AI Engineering Jobs Analysis

Generated from 9,760 job descriptions extracted from builtin.com.

I searched for jobs containing "AI Engineer" keyword from LA (Global), New York, London, Amsterdam, Berlin and India. This is the combined result of 10 monthly scrapes between February 4 and November 6, 2026.

There is no overlap in job IDs between scrapes, so each month is an independent cross-section of the market rather than the same postings re-counted.

All numbers here come from quantitative analysis in the [analysis notebook](../job-market/analysis.ipynb) and the scripts in [_internal/analysis/](../job-market/_internal/analysis/). For how these numbers moved month over month, see [trends](07-trends.md).

Summary

- 68.9% of roles work directly on AI (RAG, agents)
- 86.9% need skills beyond just GenAI - it's a full-stack role
- 40.1% of roles mention RAG - the most common named pattern in all jobs
- 53.3% of AI-First roles require some ML knowledge
- AWS (3,831 jobs) > Azure (2,898 jobs) > GCP (2,838 jobs)


## A Note on Measurement

Skills are extracted by an LLM from the job description text, then normalized through [canonicalize_skills.py](../job-market/_internal/analysis/canonicalize_skills.py), which collapses case, acronym, and synonym variants (e.g. "rag", "RAG pipelines", "retrieval-augmented generation") into one canonical skill name. Extraction runs on a single model (`glm-5.2`) with one fixed prompt across all 10 scrapes, so skill shares are comparable month to month.

Treat all skill percentages as a floor, not a ceiling - a skill the description doesn't spell out doesn't get counted.


## "AI Engineering" Job Types

Job positions we analyzed fall into these categories:

- AI-first
- AI-support
- ML

93 jobs (1.0%) could not be classified.

### AI-First: 6,721 jobs (68.9%)

Working ON AI/ML systems directly.

What they build:

- RAG (Retrieval-Augmented Generation) systems
- AI agents and agentic workflows
- Fine-tuned LLMs for specific domains
- Model serving and inference pipelines
- Prompt engineering and optimization

Example responsibilities:

- "Build RAG system for knowledge retrieval"
- "Implement agent workflows for automation"
- "Fine-tune Llama 3 for domain-specific tasks"
- "Deploy AI models to production"
- "Optimize prompts and model performance"

Position title examples

- AI Engineer
- Senior AI Engineer
- Applied AI Engineer
- Lead AI Engineer
- Staff AI Engineer
- Principal AI Engineer
- AI/ML Engineer


### AI-Support: 2,504 jobs (25.7%)

Working NEAR AI but NOT ON AI itself.

These roles enable AI work by building the platforms, infrastructure, and tools that AI-First engineers use.

What they build:

- AI platforms and internal tooling
- GPU clusters and inference infrastructure
- Data pipelines for training/fine-tuning
- Frontend for AI products
- Deployment and monitoring systems

Example responsibilities:

- "Build platform for RAG systems"
- "Pipeline data for fine-tuning"
- "Build deployment infrastructure"
- "Build prompt management UI"
- "Create internal tooling for AI experimentation"

Position title examples

- AI Sales Engineer
- AI Data Engineer
- AI Infrastructure Engineer
- AI Platform Engineer
- Backend Engineer - AI Systems
- Full-Stack Engineer (AI/LLM Platform)


### Machine Learning: 442 jobs (4.5%)

Traditional ML/DL work without LLMs/agents.

What they build:

- Classical ML models (scikit-learn, XGBoost)
- Deep learning models (PyTorch, TensorFlow)
- Computer vision systems
- Recommendation systems
- Model training pipelines

Position title examples

- Computer Vision AI Engineer
- AI Research Engineer - AI Safety
- AI Research Engineer - Reinforcement Learning
- AI Research Engineer - Robotics, Control, RL
- Sr. AI/Machine Learning Engineer - Supply Chain

These "AI Engineer" roles are traditional ML roles rebranded with the AI title. They do classical ML work (PyTorch, TensorFlow, computer vision) without any GenAI components.


### How to Tell the Difference

The key question is: Does this role work ON AI systems, or NEAR them?

AI-First:

- Builds RAG systems
- Fine-tunes models
- Implements agent workflows
- Optimizes prompts
- Deploys AI features

AI-Support:

- Builds platforms for others
- Manages GPU infrastructure
- Builds data pipelines
- Creates deployment tooling
- Builds UIs for AI products

ML:

- Trains traditional ML models
- Works with structured data
- Builds computer vision systems
- Does NOT work with LLMs/agents


## Dataset Statistics

Unique companies: 3,112

Top 20 companies by job count:

- Speechify - 248 jobs
- Capital One - 195 jobs
- Citi - 123 jobs
- Optum - 118 jobs
- NVIDIA - 90 jobs
- BJAK - 67 jobs
- JPMorganChase - 65 jobs
- Thomson Reuters - 65 jobs
- Hewlett Packard Enterprise - 63 jobs
- Vrinda International - 56 jobs
- Microsoft - 54 jobs
- PwC - 51 jobs
- Wells Fargo - 50 jobs
- G2i - 48 jobs
- Wolters Kluwer - 47 jobs
- Ecolab - 43 jobs
- Cisco - 42 jobs
- Jack & Jill AI - 39 jobs
- NextHire Consulting - 39 jobs
- Mastercard - 38 jobs

The long tail is where the jobs are: 3,112 companies for 9,760 postings, and the largest single hirer (Speechify) accounts for 2.5% of the market. The biggest identifiable names include Speechify, Capital One, Citi, Optum, and NVIDIA - mostly large public financial, healthcare, and tech enterprises rather than frontier AI labs.

Roles:

- Customer-facing roles: 1,651 (16.9%)
- Management roles: 246 (2.5%)

Most common job titles (exact match):

- AI Engineer - 458 jobs
- Senior AI Engineer - 280 jobs
- Applied AI Engineer - 105 jobs
- AI/ML Engineer - 103 jobs
- Lead AI Engineer - 90 jobs
- Staff AI Engineer - 70 jobs
- Senior AI/ML Engineer - 66 jobs
- Principal AI Engineer - 64 jobs
- Senior Applied AI Engineer - 41 jobs
- AI Product Engineer - 40 jobs


## Skills Analysis

Percentages are the share of all 9,760 jobs.

Top GenAI skills:

- LLMs - 5,908 jobs (60.5%)
- AI Agents - 4,018 jobs (41.2%)
- RAG - 3,916 jobs (40.1%)
- Prompt Engineering - 3,392 jobs (34.8%)
- Agentic Workflows - 3,199 jobs (32.8%)
- LangChain - 2,057 jobs (21.1%)
- Embeddings - 1,594 jobs (16.3%)
- MCP - 1,518 jobs (15.6%)
- Function Calling - 1,470 jobs (15.1%)
- OpenAI API - 1,425 jobs (14.6%)
- LangGraph - 1,401 jobs (14.4%)

Counting any agent skill (AI agents, agentic workflows, multi-agent systems) once per job: 5,482 jobs (56.2%).

MCP is the clearest steady riser in the dataset. It grew from 9.9% of jobs in the February scrape to 20.4% in November, more than doubling over the 10 scrapes.

Top ML skills:

- Machine Learning - 3,369 jobs
- PyTorch - 1,664 jobs
- Model Evaluation - 1,203 jobs
- TensorFlow - 1,176 jobs
- Deep Learning - 811 jobs
- Model Training - 776 jobs
- scikit-learn - 693 jobs
- Hugging Face - 652 jobs
- Transformers - 500 jobs

Fine-tuning is now tracked under GenAI rather than ML skills - see [Fine-Tuning Requirements](#fine-tuning-requirements) below.

Top web skills:

- APIs - 2,515 jobs
- REST APIs - 1,630 jobs
- Microservices - 1,382 jobs
- React - 1,373 jobs
- FastAPI - 928 jobs
- Full-Stack Development - 515 jobs
- Flask - 367 jobs

Top database skills:

- Vector Databases - 2,201 jobs
- PostgreSQL - 1,020 jobs
- Pinecone - 678 jobs
- Vector Search - 639 jobs
- NoSQL - 625 jobs
- Snowflake - 564 jobs
- Weaviate - 463 jobs

Top cloud skills:

- AWS - 3,831 jobs (39.3%)
- Azure - 2,898 jobs (29.7%)
- GCP - 2,838 jobs (29.1%)
- AWS Bedrock - 580 jobs (5.9%)
- Vertex AI - 505 jobs (5.2%)
- SageMaker - 468 jobs (4.8%)

Top ops skills:

- CI/CD - 3,603 jobs
- Docker - 2,366 jobs
- Kubernetes - 2,307 jobs
- Observability - 2,018 jobs
- MLOps - 1,581 jobs
- Distributed Systems - 1,437 jobs
- Monitoring - 1,414 jobs

Top languages:

- Python - 6,991 jobs (71.6%)
- TypeScript - 1,859 jobs (19.0%)
- Java - 1,690 jobs (17.3%)
- SQL - 1,428 jobs (14.6%)
- Go - 1,109 jobs (11.4%)
- JavaScript - 1,081 jobs (11.1%)


## GenAI Framework Ecosystem

Framework popularity:

- LangChain - 2,057 jobs (21.1%)
- LangGraph - 1,401 jobs (14.4%)
- LlamaIndex - 778 jobs (8.0%)
- CrewAI - 639 jobs (6.5%)
- AutoGen - 528 jobs (5.4%)

Frameworks travel together rather than compete. 1,030 jobs ask for LangChain and LangGraph, 747 for LangChain and LlamaIndex. Companies list the ecosystem, not a single tool.


## Supporting Roles: What AI-Support Engineers Do

2,504 jobs (25.7%) classified as AI-Support

| Category | Jobs | Description |
|----------|------:|-------------|
| Platform/Infrastructure | 1,523 | Build AI platforms, GPU clusters, MLOps tooling |
| Frontend/UI | 408 | Build UIs for AI products, chatbots, AI dashboards |
| Sales/Solutions | 244 | Pre-sales, customer demos, AI solutions consulting |
| Backend/General SWE | 196 | APIs, microservices, internal tools for AI teams |
| Data/Pipelines | 74 | Data pipelines, ETL, dataset preparation for ML |
| Other | 59 | QA/test, observability tooling, SRE, hardware for AI systems |

Do AI-Support roles need AI knowledge?

- 53.0% of AI-Support roles list some GenAI skill (or 37.5% excluding broad umbrella terms like LLMs)
- 47.0% list no GenAI skills at all

GenAI skills in AI-Support roles:

- GitHub Copilot - 8.3%
- Claude Code - 8.1%
- RAG - 7.6%
- Prompt Engineering - 7.3%
- Cursor - 6.7%

GitHub Copilot, Cursor, and Claude Code appear prominently in AI-Support roles. For support engineers, "AI skills" increasingly means using AI coding tools as well as building platforms for AI teams.


### Skill Comparison (AI-First vs AI-Support)

| Skill | AI-First | AI-Support |
|:-------|---------:|------------:|
| RAG | 56.0% | 9.7% |
| Prompt engineering | 47.6% | 7.3% |
| Agents (any) | 55.0% | 15.3% |
| LangChain | 29.1% | 3.9% |
| Fine-tuning | 24.2% | 1.5% |
| Python | 75.9% | 56.9% |
| Docker | 25.2% | 23.2% |
| Kubernetes | 22.7% | 28.3% |
| CI/CD | 36.7% | 40.7% |
| AWS | 45.4% | 35.6% |
| React | 15.2% | 15.7% |

The GenAI skills separate the two groups cleanly. The infrastructure skills don't - and where they differ, AI-Support asks for more of them.


## Research vs Applied Roles

| Role Type | Jobs | Percentage |
|----------|-----:|------------:|
| Research | 252 | 2.6% |
| Applied/Production | 9,508 | 97.4% |

Research roles work on:

- Novel algorithms and techniques
- Model architecture design
- Training methods and optimization
- Safety and alignment research
- Publishing papers, pushing SOTA
- Experimental work with uncertain outcomes

Keywords: research, scientist, publication, novel, algorithm, architecture, state of the art, experimental

Sample research titles:

- AI Research Engineer
- Applied Scientist / Research Engineer
- AI Research Engineer - Reinforcement Learning
- AI Research Engineer (Kernel & Inference Optimization)
- Research Engineer, AI
- Lead AI Engineer (AI Foundations, LLM Customization and Finetuning)

Applied / Production roles work on:

- Implementing existing models in production
- Building applications with AI APIs
- Deploying and monitoring AI systems
- Customer-facing AI solutions
- Infrastructure and platforms for AI
- Fine-tuning models for specific use cases

Keywords: production, deploy, customer, enterprise, product, API integration, shipping, implementation

The market wants people who ship, not people who publish.


### Example Comparison

| Research | Applied |
|----------|---------|
| "Run pre-training and post-training of state-of-the-art models on clusters with thousands of GPUs" (Mistral AI) | "Deploy production AI solutions with measurable business impact across various industries" (Mistral FDE) |
| "Develop novel reinforcement learning algorithms" | "Implement RAG patterns with vector store integration" |
| "Publish papers at top conferences" | "Ship AI features to customers" |


## What Other Titles Do "AI Engineers" Go Under?

Titles here are grouped across seniority levels, so "AI Engineer" includes Senior, Staff, Lead and Principal variants.

Strongly AI-First titles (75%+ classified as AI-First):

- AI Engineer - 1,064 jobs (92% AI-First)
- Applied AI Engineer - 162 jobs (94% AI-First)
- AI Software Engineer - 78 jobs (82% AI-First)
- AI Developer - 69 jobs (80% AI-First)
- Software Engineer - AI - 62 jobs (84% AI-First)
- AI Product Engineer - 58 jobs (86% AI-First)
- Software Engineer, AI - 52 jobs (94% AI-First)
- Agentic AI Engineer - 46 jobs (96% AI-First)
- AI Solutions Engineer - 46 jobs (85% AI-First)
- AI Automation Engineer - 40 jobs (90% AI-First)
- Forward Deployed AI Engineer - 38 jobs (97% AI-First)
- Generative AI Engineer - 32 jobs (100% AI-First)
- AI Research Engineer - 31 jobs (77% AI-First)
- Full Stack AI Engineer - 20 jobs (85% AI-First)

Strongly AI-Support titles (75%+ classified as AI-Support):

- AI Infrastructure Engineer - 18 jobs (83% AI-Support)

Titles that predict nothing:

- AI Platform Engineer - 72 jobs (56% AI-First, 44% AI-Support)
- AI Data Engineer - 49 jobs (63% AI-First, 35% AI-Support)
- AI Enablement Engineer - 21 jobs (52% AI-First, 48% AI-Support)
- Software Engineer (AI) - 22 jobs (73% AI-First, 23% AI-Support)

Key insight: "AI Engineer" is still the most common title and still the most reliable one (92% AI-First). But anything with "platform", "data", or "enablement" in it is a coin flip - always check the responsibilities.

Agentic AI Engineer and Generative AI Engineer are almost exclusively AI-First and did not exist as titles at the start of the dataset. Forward Deployed Engineer remains one of the fastest-growing titles - see [Forward Deployed Engineers](06-fde.md) for the full picture on that role.


## How Much ML Do AI Engineers Need to Know?

53.3% of AI-First roles require some ML knowledge

Most common ML skills in AI-First roles:

- fine-tuning - 1,629 jobs (24.2%)
- embeddings - 1,559 jobs (23.2%)
- PyTorch - 1,262 jobs (18.8%)
- model evaluation - 1,043 jobs (15.5%)
- TensorFlow - 860 jobs (12.8%)
- model training - 670 jobs (10.0%)
- scikit-learn - 506 jobs (7.5%)

Key findings:

1. About half of AI Engineers need some ML knowledge - 53.3% require specific ML skills
2. Fine-tuning and embeddings are the most common ML-adjacent tasks - more common than model training from scratch
3. PyTorch dominates - about 1.5x more common than TensorFlow in AI-First roles

Bottom Line: AI Engineers need practical ML knowledge (PyTorch basics, fine-tuning, embeddings) but don't need deep ML expertise unless specifically working on model development. See [trends](07-trends.md) for how the trainer stack is shrinking against the integrator stack.


## What Else (Besides GenAI) Do AI Engineers Need?

86.9% of AI-First roles require skills BEYOND just GenAI

Skill combinations in AI Engineer roles:

- GenAI + Ops (Docker, K8s, CI/CD) - 71.0%
- GenAI + Web skills - 59.2%
- GenAI + ML skills - 39.3%
- GenAI + ANY other tech - 86.9%
- Pure GenAI (nothing else) - 4.0%

### Non-GenAI Skills Expected

| Category | Skills | % |
|----------|--------|--:|
| Cloud | AWS (41.8%), Azure (31.5%), GCP (28.6%) | - |
| Ops | CI/CD (36.7%), Docker (25.2%), Observability (23.3%) | - |
| Web | APIs (29.8%), REST APIs (17.5%), React (14.4%) | ~59% do web work |
| Languages | Python (75.9%), TypeScript (21.2%), Java (16.7%) | Python mandatory |

Full-stack expectations (AI-First roles):

- Frontend skills - 2,070/6,721 (30.8%)
- Backend skills - 4,102/6,721 (61.0%)
- Full-stack (both) - 1,553/6,721 (23.1%)

Bottom Line: AI Engineers are full-stack engineers who specialize in AI. Only 4.0% of roles expect pure GenAI work. Most need cloud deployment (AWS/Azure/GCP), containerization (Docker, K8s), CI/CD, and often web development (React, FastAPI).


## Fine-Tuning Requirements

26.5% of AI-First roles mention fine-tuning anywhere in the posting

### Depth of Fine-Tuning Expectation

| Level | Jobs | % | Description |
|-------|------:|--:|-------------|
| Primary FT responsibility | 212 | 3.2% | FT is main focus (model architecture, LoRA, PEFT) |
| Secondary/occasional FT | 731 | 10.9% | FT mentioned but not core |
| No FT in responsibilities | 5,778 | 86.0% | No fine-tuning expected |

### Fine-Tuning Use Cases

- Instruction following - Agents that follow complex instructions, task execution
- Domain knowledge - Medical, legal, finance, industry-specific applications
- Style/Tone - Brand voice, personality, formatting requirements
- Company data - Internal documents, proprietary data
- Performance - Smaller/faster models, latency optimization
- Language - Multilingual, non-English support
- Privacy - On-prem, offline, secure environments

Key findings:

1. Most AI Engineers don't fine-tune - it's absent from the responsibilities of 86.0% of roles
2. Primary FT roles are rare - only 3.2% focus on fine-tuning as main responsibility
3. Fine-tuning is a specialization - not a core AI Engineer skill, more advanced

Bottom Line

- Fine-tuning is optional for most AI Engineers.
- Focus on RAG and agents first.
- Learn fine-tuning if targeting domain-specific roles (healthcare, finance, legal), performance optimization roles, or specialized model development.


## Evaluation Skills

61.8% of AI-First roles require evaluation-related skills (model evaluation, LLM evaluation, guardrails, monitoring, observability, model monitoring).

That share moved from 55.9% in February to 69.3% in November, remaining the majority of roles all year.

The specific skills inside that group:

- LLM evaluation - 33.5%
- Observability - 23.6%
- Guardrails - 19.8%
- Model evaluation - 15.5%
- Monitoring - 15.4%
- Model monitoring - 7.2%

"Evaluat" appears in 4,797 of 69,498 extracted responsibilities, so the real demand is broader than the skill lists suggest.

This is the differentiator. RAG and agents are now baseline expectations. The ability to measure whether an AI system actually works - LLM-as-judge, golden datasets, hallucination detection, drift monitoring - is what separates candidates.


## Key Insight: RAG + Agents = Most Use Cases

The two dominant patterns are:

- RAG - connect LLMs to your data (documents, databases). 40.1% of all jobs, 55.2% of AI-First jobs
- Agents - LLMs that use tools to accomplish tasks. 56.2% of all jobs, 74.0% of AI-First jobs

They are usually asked for together: 3,183 jobs list both. In the responsibility text, "agent" appears in 9,670 of 69,498 responsibilities and "rag" in 3,645.

If you learn these two patterns deeply, you can handle most AI Engineering use cases. See [use cases](04-use-cases.md) for what companies actually build with them.


## Learning Path for AI Engineers

- Foundation - Python, APIs, basic web development (FastAPI/React)
- LLM Basics - Prompt engineering, OpenAI/Anthropic APIs
- RAG - Vector databases, embeddings, retrieval patterns
- Frameworks - LangChain or LlamaIndex
- Agents - LangGraph, agent orchestration, MCP
- Evaluation - LLM-as-judge, golden datasets, guardrails, monitoring
- Production - Docker, Kubernetes, CI/CD, observability

The typical AI engineering stack:

- APPLICATION layer - React, Next.js, FastAPI
- AI ORCHESTRATION layer - LangChain, LangGraph, LlamaIndex
- LLM APIS layer - OpenAI, Anthropic, local models
- VECTOR DATABASES layer - Pinecone, Weaviate, pgvector
- INFRASTRUCTURE layer - Docker, K8s, AWS/GCP/Azure
