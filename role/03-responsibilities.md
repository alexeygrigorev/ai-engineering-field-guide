# AI Engineering Responsibilities Analysis

Based on 69,498 responsibilities extracted from 9,760 job descriptions across 10 monthly scrapes (Feb-Nov 2026).

Methodology note: I collected all responsibilities into a single file and used AI (Claude) to analyze and categorize them. This is not a quantitative analysis like the [skills analysis](02-skills.md) (see the [analysis notebook](../job-market/analysis.ipynb) for that) - it's based on the questions I asked and the patterns Claude identified in the data. The prevalence numbers (percent of jobs) come from keyword matching, so a single responsibility can count toward more than one category. It may be less precise than a strict statistical analysis, but I believe it's still representative of what's happening in the market.

Across all 69,498 responsibilities:

- AI-First roles: 48,793 responsibilities (70.2%)
- AI-Support roles: 17,293 responsibilities (24.9%)
- ML-First and unclassified roles: 3,412 responsibilities (4.9%)


## Feb vs Nov: How the Market Shifted

Comparing the first scrape (Feb 2026, 895 jobs) with the latest (Nov 2026, 1,709 jobs) shows a clear direction. Postings averaged 7.1 responsibilities per job in February and 6.7 in November, while AI-Support roles grew from 22.2% to 32.9% of listings.

The role is becoming more agentic and more evaluation-focused, and much less exploratory. Agents crossed into the majority of jobs, while research and experimentation dropped sharply.

Biggest movers (change is in percentage points of jobs):

| Area | Feb | Nov | Change |
|------|-----|-----|--------|
| Agents and Agentic Workflows | 45.7% | 55.8% | +10.1 |
| Data and Pipelines | 19.7% | 29.7% | +10.0 |
| Evaluation and Testing | 69.4% | 79.0% | +9.6 |
| Prompt Engineering | 15.3% | 22.8% | +7.5 |
| Security, Safety and Compliance | 33.4% | 37.5% | +4.1 |
| Research and Experimentation | 35.8% | 13.7% | -22.1 |
| Deploy and Production | 83.7% | 66.5% | -17.2 |
| Infrastructure and Platform | 68.4% | 51.4% | -17.0 |
| Customer and Client Work | 43.0% | 28.0% | -15.0 |
| Fine-tuning and Training | 13.7% | 7.3% | -6.5 |

What this tells me:

- Agents went from under half of jobs to a clear majority (55.8%).
- Evaluation and testing climbed +9.6 points to 79.0% of jobs, while prompt engineering rose +7.5 points to 22.8%.
- Research and experimentation fell the most (-22.1 points, down to 13.7%). Fewer roles are framed around exploration and prototyping; more are framed around shipping and evaluating systems.
- Fine-tuning and training responsibilities also declined (-6.5 points to 7.3%), consistent with the broader pattern that the core job is building and evaluating applications rather than training models.


## Frequency Guide

I measured each responsibility area by how many of the 9,760 job descriptions it appears in, not just raw mention counts. A responsibility in 96.0% of jobs is genuinely universal; one in 11.0% is specialized.

| Prevalence | Meaning |
|------------|---------|
| Very common | Appears in a majority of descriptions (over 50%) |
| Common | Appears in many descriptions (25.0-50.0%) |
| Uncommon | Appears in some descriptions (15.0-25.0%) |
| Rare | Appears in few descriptions (under 15.0%) |


## Typical Job Titles

AI Engineers work under various titles. The job title alone does not reliably indicate whether the role is AI-First, AI-Support, or ML-First.

The most common titles in the dataset:

- AI Engineer - 458 postings; of all titles containing "AI Engineer", 91.6% of normalized base `AI Engineer` roles are AI-First
- Senior AI Engineer - 280 postings
- Applied AI Engineer - 105 postings
- AI/ML Engineer - 103 postings
- Lead AI Engineer - 90 postings
- Staff AI Engineer - 70 postings
- Senior AI/ML Engineer - 66 postings
- Principal AI Engineer - 64 postings
- Senior Applied AI Engineer - 41 postings
- AI Product Engineer - 40 postings

AI-First titles (working ON AI):

- AI Engineer - Most common, 91.6% are AI-First
- Senior AI Engineer / Lead AI Engineer / Staff / Principal AI Engineer
- Applied AI Engineer
- AI/ML Engineer
- AI Product Engineer
- AI Research Engineer
- Forward Deployed AI Engineer
- Generative AI Engineer

AI-Support titles (working NEAR AI):

- AI Platform Engineer
- AI Infrastructure Engineer
- AI Data Engineer
- AI Solutions Engineer
- Software Engineer, AI (can be either)

ML-First titles (traditional ML):

- Machine Learning Engineer (when focused on classical ML)
- ML Engineer
- Data Scientist (when doing model training, not GenAI)

Overall, 68.9% of all 9,760 roles classify as AI-First, 25.7% as AI-Support, and only 4.5% as ML-First.


## Problems AI Engineers Solve

Organized by the problem they address, not the technology. Grouped by how widespread each responsibility is across jobs.


## Very Common

### Building AI Systems

Appears in 96.0% of jobs (27,893 mentions).

Problem: Organizations need AI systems built to solve specific business problems.

What AI Engineers do:

- Implement LLM-based features including computer use, evals, and voice agents
- Design, build, and own AI models and applications using governed datasets
- Design UX patterns for AI interactions including streaming responses, retries, and partial results
- Develop automation for model deployment, rollback, scaling, and lifecycle management

Sub-patterns:

- AI Agents and Agentic Workflows - Build autonomous agents using frameworks with multi-step planning and tool use
- Chatbots and Conversational AI - Design conversational interfaces with context management
- RAG Systems - Implement retrieval-augmented generation with vector databases
- Evaluation Systems - Build frameworks to measure AI quality and performance
- LLM-Powered Recommendations - Personalization using LLMs rather than classical ML
- Generative Vision - Image/video generation using diffusion models and GenAI (not classical CV)

Core challenge: Translating business problems into working AI systems that are reliable, scalable, and maintainable.


### Collaboration and Communication

Appears in 81.0% of jobs (14,455 mentions).

Problem: AI Engineers cannot work in isolation. They must collaborate with product, data, engineering, and business teams.

What AI Engineers do:

- Collaborate with engineers and product managers to formulate hypotheses, solutions, and desired outcomes
- Collaborate with business teams to identify automation opportunities and translate requirements into technical work
- Partner with algorithms team on integration with signal processing and computer vision pipelines
- Synthesize stakeholder input, visualize results, and communicate findings to leadership

Sub-patterns:

- Cross-Functional Collaboration - Work with engineers, researchers, product managers, domain experts
- Stakeholder Management - Elicit requirements, manage expectations, prioritize requests
- Technical Leadership - Mentorship, code reviews, raising technical bar, knowledge sharing
- Documentation - Maintain docs for models, processes, workflows, best practices
- Client Communication - Technical sales cycles, solution architecture, customer feedback

Core challenge: Bridging technical and non-technical communication while managing competing priorities.


### Productionizing AI

Deploy/production in 77.8% of jobs (14,574 mentions); monitoring/maintenance in 63.8% (10,052 mentions).

Problem: AI that works in notebooks often fails in production. Reliability, scalability, and monitoring are hard.

What AI Engineers do:

- Build AI-enabled systems including LLM- or RAG-based solutions from MVP through to production
- Own features from concept through deployment: frontend UI, API design, backend services, data pipelines
- Work closely with software and product teams to ship reliable AI features at scale
- Drive adoption of shared platform services including LLM gateway, evaluation frameworks, and monitoring
- Own on-call runbooks, SLOs, incident reviews, and embed observability for AI solutions

Sub-patterns:

- API Design and Model Serving - Build high-throughput, low-latency AI workloads
- LLM Deployment Strategies - Choose between providers, open-source models, or fine-tuned models
- Monitoring and Observability - Track LLM-specific metrics: token usage, costs, latency, hallucinations
- Scaling and Infrastructure - Handle burst traffic, manage GPU resources, maintain high availability
- Production Reliability - On-call participation, incident response, runbooks, post-mortems

Core challenge: Making probabilistic AI systems reliable enough for production use while managing costs and scalability.


### Evaluation and Quality

Appears in 71.3% of jobs (12,132 mentions).

Problem: AI systems can hallucinate, produce biased outputs, or fail unexpectedly. Quality assurance is critical.

What AI Engineers do:

- Develop evaluation frameworks: offline benchmarks, safety tests, regression suites, and LLM-as-judge pipelines
- Ensure safe, reliable AI outputs with guardrails, monitoring, and evaluation frameworks
- Build and evaluate supervised and unsupervised ML models for security use cases
- Validate RAG pipelines including embedding accuracy, retrieval quality, and model responses

Sub-patterns:

- Evaluation Frameworks - Build automated testing systems for AI quality before production
- Safety Guardrails - Implement content filters, validation, human-in-the-loop workflows
- Hallucination Detection - Use RAG with citations, faithfulness metrics, context engineering
- Bias and Fairness - Conduct bias testing, ensure equitable outcomes across user groups
- Human-in-the-Loop - Design efficient review workflows with feedback mechanisms

Core challenge: Defining meaningful metrics for non-deterministic systems and catching edge cases before production.


### Integrating APIs and Services

Appears in 62.4% of jobs (4,724 responsibilities).

Problem: Companies need to integrate LLM capabilities into existing products and data systems without rebuilding everything.

What AI Engineers do:

- Integrate AI orchestration with Python, SQL, and Snowflake data pipelines
- Integrate AI capabilities into secure, HIPAA-compliant SaaS platforms and EHR systems
- Work across the stack to connect frontend features to Python/FastAPI backends
- Develop MCP servers and tool integrations
- Integrate observability solutions using OpenTelemetry or Datadog for distributed tracing

Sub-patterns:

- Provider API Integration - Connect OpenAI, Anthropic, Google, and other LLM APIs
- API Key Management and Rate Limiting - Handle errors, retries, fallbacks, cost controls
- Tool and Function Calling - Wire LLMs to internal systems, MCP servers, and SDKs
- Legacy System Integration - Connect AI to ERPs, CRMs, EHRs, and other enterprise systems

Core challenge: Building reliable applications on top of third-party APIs and internal systems while managing costs, rate limits, and API changes.


### Infrastructure and Platforms

Appears in 64.6% of jobs (10,917 mentions).

Problem: AI requires specialized infrastructure - GPU clusters, MLOps tooling, scalable platforms.

What AI Engineers do:

- Set technical direction for the AI platform layer through design documents and personally ship core components
- Build and optimize secure, scalable Gen AI platforms supporting enterprise document management and data security
- Establish and enforce architecture standards for production AI systems including data pipelines and model serving
- Automate workflows and operations using scripting and infrastructure as code

Sub-patterns:

- AI Platform Engineering - Build internal AI platforms with evaluation, experimentation, and context management
- GPU/Compute Infrastructure - Manage GPU resource allocation, control costs, ensure high availability
- Vector Database Infrastructure - Implement RAG systems with vector search, reranking, attribution
- Model Registries - Version LLMs, fine-tuned models, prompt templates, and RAG configurations
- Experiment Tracking - Track prompt experiments, RAG configurations, and evaluation results
- Security and Compliance Infrastructure - Authentication, authorization, PHI/PII handling, encryption

Core challenge: Building flexible platforms that accommodate diverse use cases while maintaining stability amid rapid AI evolution.


### Performance Optimization

Appears in 63.9% of jobs (9,843 mentions).

Problem: AI systems can be slow, expensive, or unreliable. Optimization is necessary for production use.

What AI Engineers do:

- Optimize AI agent performance, latency, and cost through profiling, prompt optimization, and caching strategies
- Implement monitoring, observability, and performance tuning across GPU and compute platforms
- Customize and fine-tune models to optimize performance for specific use cases
- Identify opportunities to improve library performance and reduce compute through re-architecture

Sub-patterns:

- Latency Reduction - Caching, batching, streaming, model distillation
- Cost Optimization - Token tracking, model routing, prompt compression
- Throughput Scaling - Batch inference, GPU scheduling, autoscaling
- Resource Efficiency - Quantization, smaller models, efficient retrieval

Core challenge: Reducing latency while maintaining quality, managing compute costs, and optimizing for different deployment environments.


### Agents and Agentic Workflows

Appears in 53.3% of jobs (10,274 mentions).

Problem: Companies want AI that can take actions, not just generate text. Agents need orchestration, memory, and tools.

What AI Engineers do:

- Provide technical leadership through architecture decisions, code reviews, and coaching on agentic design patterns
- Embed with customers to understand business processes and identify automation opportunities using AI agents
- Implement adversarial testing to systematically identify and prevent agent failure modes
- Translate business goals into clear, measurable AI use cases and Virtual Agent strategies
- Collaborate with MLOps team on continuous agent updating and deployment

Core challenge: Designing agents that can reliably plan multi-step tasks, maintain coherent context, handle failures gracefully, and coordinate between multiple specialized agents.


## Common

### RAG and Retrieval

Appears in 41.1% of jobs (5,214 mentions).

Problem: Companies need AI that can access their proprietary data. Keyword search is not enough.

What AI Engineers do:

- Design, implement, and optimize retrieval-augmented generation (RAG) systems that leverage the latest LLM technology
- Build and deploy production RAG workflows and intelligent internal tools
- Implement data processing pipelines for cleaning, transformation, chunking, and embedding generation
- Develop AI systems including RAG, fine-tuning pipelines, prompt engineering recipes, and agentic patterns

Sub-patterns:

- Document Processing and Chunking - Handle diverse formats (PDFs, Word, HTML, audio, video)
- Vector Search and Semantic Retrieval - Implement high-precision semantic search with optimized indexes
- Knowledge Graphs and Hybrid Retrieval - Combine graph traversal with vector similarity
- Query Rewriting and Expansion - Understand user intent, handle ambiguity, maintain context
- Re-Ranking and Result Optimization - Balance relevance scoring, optimize for different query types
- Context Window Management - Maximize relevant information within token limits

Core challenge: Achieving accurate semantic retrieval at scale while handling domain-specific terminology and optimizing for latency.


### Security and Compliance

Appears in 38.8% of jobs (5,552 mentions).

Problem: AI systems can pose security, privacy, and compliance risks. These must be addressed.

What AI Engineers do:

- Harden CI/CD and release processes to improve deployment safety and velocity
- Ensure code security, model governance, and adherence to Responsible AI practices
- Ensure alignment with privacy, security, and ethical AI guardrails
- Design and build central AI platform governance using an LLM gateway with access controls

Sub-patterns:

- Data Privacy - PHI/PII handling, redaction, encryption at rest and in transit
- Model Governance - Versioning, audit trails, approval workflows for production models
- Responsible AI - Bias testing, fairness, transparency, explainability
- Threat Modeling - Prompt injection, data poisoning, model extraction defenses

Core challenge: Balancing security with usability, ensuring compliance across jurisdictions, and protecting against AI-specific threats.


### Working with Customers

Appears in 35.4% of jobs (5,791 mentions).

Problem: AI solutions must be delivered to actual customers. This requires understanding their needs and ensuring success.

What AI Engineers do:

- Act as the primary developer for AI use cases across solution assets and customer-ready frameworks
- Work embedded with client teams to conduct use case discovery and develop AI deployment solutions
- Experiment, prototype, and ship rapidly, moving innovations from idea to production in live customer environments
- Identify and expand AI use cases across customer organizations

Core challenge: Translating technical concepts for business audiences, managing customer expectations, and ensuring successful adoption.


## Uncommon

### Data Processing

Appears in 23.2% of jobs (3,161 mentions).

Problem: AI systems need clean, well-structured data. Data processing is foundational work.

What AI Engineers do:

- Design and implement scalable ML/AI systems and pipelines
- Implement data processing pipelines for cleaning, transformation, chunking, and embedding generation
- Work with large spans of datasets including image, video, audio, text, and structured data
- Work with large datasets of IT operational data including data cleaning and feature engineering

Sub-patterns:

- Data Ingestion - Build pipelines for ingesting diverse data types and sources
- Data Transformation - Preprocess, clean, and transform raw data for AI applications
- Dataset Management - Curate, version, and maintain datasets for training and evaluation
- Data Quality - Implement validation, cleaning, and quality checks

Core challenge: Ensuring data quality at scale while handling diverse formats and maintaining pipeline reliability.


### Prompt Engineering

Appears in 21.5% of jobs (2,566 mentions).

Problem: Getting reliable behavior from LLMs requires deliberate prompt design, treated as an engineering discipline rather than ad hoc writing.

What AI Engineers do:

- Develop and maintain prompt engineering frameworks, evaluation pipelines, and feedback loops
- Own prompt engineering and evaluation, treating evals and prompts as code
- Implement prompt engineering patterns, RAG pipelines, and tool-augmented agents using established frameworks
- Optimize prompt engineering strategies and model interactions for accuracy and performance

Core challenge: Making prompts reproducible, versioned, and testable rather than fragile one-off strings.


### Research and Experimentation

Appears in 21.4% of jobs (2,920 mentions).

Problem: AI technology evolves rapidly. Companies need to experiment with new techniques and stay current.

What AI Engineers do:

- Continuously research AI advancements, multi-agent orchestration, and agentic autonomy
- Collaborate with ML Scientists and Data Scientists to transition prototypes and models into production
- Design, develop, and test AI/ML prototypes to address business needs
- Build infrastructure for managing experiments, simulations, and results

Core challenge: Balancing experimental innovation with production reliability while keeping pace with rapid technological change.


### Frontend and User Interfaces

Appears in 16.4% of jobs (2,112 mentions).

Problem: AI capabilities need user-friendly interfaces. Chatbots, dashboards, and web applications are how users interact with AI.

What AI Engineers do:

- Contribute to the development lifecycle with backend (Node.js/Python) and frontend (React/Next.js) work
- Build and maintain full-stack features using React, TypeScript, and Python
- Integrate AI/ML components with frontend, backend, data, and compute infrastructure
- Connect front-end components with backend APIs and AI services to display real-time results

Core challenge: Making AI capabilities accessible through intuitive interfaces while handling streaming responses and managing context limits.


## Rare

### Fine-tuning Models

Appears in 11.0% of jobs (1,144 mentions).

Problem: Generic models do not always work for specialized use cases. Fine-tuning can improve performance on specific tasks.

What AI Engineers do:

- Develop prompt engineering strategies and fine-tuning techniques (LoRA, PEFT, RLHF)
- Assist in model training, fine-tuning, evaluation, and experimentation
- Lead LLM fine-tuning, evaluation, and deployment with optimized retrieval pipelines
- Fine-tune open-weight LLMs using LoRA/QLoRA, PEFT, or RLHF methods

Core challenge: Acquiring quality training data, avoiding catastrophic forgetting, and measuring improvement effectively.


### Self-Hosting Models

Appears in 3.1% of jobs (338 mentions).

Problem: Some companies cannot use provider APIs due to privacy, cost, or latency requirements.

What AI Engineers do:

- Build and optimize LLM inference systems using vLLM, TensorRT-LLM, and custom serving solutions
- Integrate and optimize NVIDIA Enterprise Suite components including CUDA, NeMo, Triton, and TensorRT
- Contribute to open source communities like FlashInfer, vLLM, and SGLang
- Fine-tune open-source models (Llama, Mistral) for specific domain tasks and optimize for latency and cost

Why self-hosting is rare:

- Frontier models (GPT-4, Claude) are API-only
- Significant operational overhead
- GPU costs are high at low scale
- Requires specialized infrastructure skills

When self-hosting is necessary:

- Data privacy requirements - cannot send data to external APIs
- Cost at scale - high volume makes self-hosting cheaper
- Low latency needs - on-premise for edge or regional requirements
- Custom models - fine-tuned models that you host yourself


## Key Insights

### 1. Building is the Primary Responsibility

Building systems appears in 96.0% of jobs. AI Engineers are builders first and foremost.

### 2. Production is a Major Responsibility

When you combine deployment (77.8%), monitoring (63.8%), and infrastructure (64.6%), productionizing AI is most of the work - much larger than initially apparent.

### 3. Quality is Not Optional

Evaluation and quality appear in 71.3% of jobs. AI Engineers are expected to build systems that work reliably and safely.

### 4. APIs and Integration Dominate Over Self-Hosting

Integrating APIs and services appears in 55.8% of jobs, while self-hosting models appears in only 3.1%. The market overwhelmingly uses provider APIs rather than running its own inference infrastructure.

### 5. RAG and Agents are Mainstream

RAG/retrieval (41.1%) and agents (53.3%) are now standard responsibilities, not niche. Over half of all AI Engineers work on agentic systems.

### 6. Fine-tuning is Uncommon

Despite the hype, fine-tuning appears in only 11.0% of jobs and prompt engineering in 21.5%. Most roles use existing models with RAG, prompting, and integration rather than training or tuning.


## Most Common Words in Responsibilities

- build: 10,028 mentions
- data: 9,591 mentions
- design: 7,448 mentions
- systems: 6,689 mentions
- technical: 5,403 mentions
- solutions: 5,351 mentions
- develop: 4,880 mentions
- workflows: 4,537 mentions
- teams: 4,514 mentions
- engineering: 4,403 mentions
- product: 4,239 mentions
- implement: 4,238 mentions
- model: 4,234 mentions
- production: 4,127 mentions
- models: 4,045 mentions
- pipelines: 4,009 mentions

The language emphasizes action: build, design, implement, collaborate, deploy.
