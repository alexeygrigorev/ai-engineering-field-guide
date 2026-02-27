# AI System Design Interview

AI system design is emerging as a distinct interview category, separate from both traditional software system design and classic ML system design. The shift is driven by the explosion of LLM-powered products: instead of designing training pipelines, candidates design orchestration architectures around pre-trained models.

Companies with dedicated AI system design rounds include Doctolib ("AI System Design Interview"), Sprinter Health ("AI-Focused Systems Design"), and Anthropic (distributed search + LLM inference at scale). Many more are adding AI-flavored questions to existing system design rounds.

See also: [Awesome AI Engineering](../awesome.md) for the full collection of references, company blogs, and practitioner stories cited below.

## How It Differs from Traditional ML System Design

Traditional ML system design interviews focus on training pipelines: data collection, feature engineering, model selection, offline evaluation, and deployment. Canonical questions include "Design a recommendation system" or "Design a fraud detection system."

AI system design interviews focus on inference orchestration: retrieval, prompt composition, output validation, evaluation, and safety. Canonical questions include "Design a hallucination-free chatbot for banking" or "Design a RAG-powered enterprise search system."

The fundamental shift: when models like GPT-4 and Claude became accessible via APIs, the hard part stopped being model training and started being system orchestration ([Chip Huyen, "AI Engineering"](https://huyenchip.com/books/)).

| Dimension | Traditional ML System Design | AI/LLM System Design |
|---|---|---|
| Core activity | Training models | Orchestrating pre-trained models |
| Data focus | Training data, feature engineering | Context engineering, chunking, retrieval quality |
| Output type | Structured (scores, classifications) | Open-ended text, code, images |
| Determinism | Generally deterministic | Non-deterministic by default |
| Evaluation | Precision/recall/F1/AUC on held-out sets | LLM-as-judge, human evaluation, task-specific evals |
| Cost model | Training compute (periodic) + serving | Per-token inference cost (continuous) + retrieval |
| Failure modes | Data drift, training-serving skew | Hallucination, prompt injection, context overflow, cost blowup |
| Iteration speed | Slow (retrain model) | Fast (change prompt, adjust retrieval) |

Source: synthesized from [Yuan Meng](https://www.yuan-meng.com/posts/mle_interviews_2.0/), [Brian Kihoon Lee](https://www.moderndescartes.com/essays/ml_eng_interviewing/), [Chip Huyen](https://huyenchip.com/2024/07/25/genai-platform.html), and the [PromptLayer agentic interview guide](https://blog.promptlayer.com/the-agentic-system-design-interview-how-to-evaluate-ai-engineers/).


## What Candidates Are Asked

### Typical AI System Design Questions

Based on real interview experiences and practitioner guides:

- Design a customer support chatbot that must not hallucinate ([Mai Chi Bao](https://dev.to/mrzaizai2k/how-i-aced-my-llm-interview-building-a-rag-chatbot-2p6f), [Bhavishya Pandit](https://bhavishyapandit9.substack.com/p/7-deep-cut-ai-system-design-interview))
- Design a RAG-powered Q&A system for internal company documents
- Design a voice assistant for hospital staff
- Design an AI tool to generate legal contracts from prompts
- Design an AI search assistant for 10M+ articles
- Design a search system handling a billion documents and LLM inference for 10K+ RPS ([Anthropic onsite](https://www.linkjob.ai/interview-questions/anthropic-software-engineer-interview/))
- Design ChatGPT's cross-conversation memory feature ([Jack Chih-Hsu Lin, Google](https://medium.com/data-science/mastering-genai-ml-system-design-interview-2-design-chatgpt-memory-feature-fe908517d76c))
- Design a multi-step agentic workflow (meeting scheduling, code review, email campaigns)

### Expected Architecture Components

Candidates typically design a composable pipeline covering:

1. **Problem decomposition** - breaking the problem into LLM-solvable sub-tasks
2. **Retrieval layer** - vector databases, embedding models, chunking strategies, hybrid search (BM25 + dense embeddings)
3. **Prompt composition** - system prompts, few-shot examples, context injection
4. **LLM gateway** - model selection/routing, rate limiting, cost management
5. **Output validation** - guardrails, structured output enforcement, hallucination detection
6. **Evaluation system** - evals (automated + human), LLM-as-judge, regression testing
7. **Feedback loops** - user feedback collection, data flywheels, continuous improvement
8. **Safety and security** - prompt injection defense, PII handling, content filtering

This maps closely to [Chip Huyen's 5-step progressive architecture](https://huyenchip.com/2024/07/25/genai-platform.html): enhance context (RAG) -> implement guardrails -> add model router/gateway -> reduce latency with cache -> add complex logic and write actions.


## What Interviewers Evaluate

Based on [PromptLayer's agentic interview guide](https://blog.promptlayer.com/the-agentic-system-design-interview-how-to-evaluate-ai-engineers/) and multiple practitioner accounts:

- **Systems thinking** - can you decompose a complex problem into components an LLM can handle?
- **Retrieval and context engineering trade-offs** - chunking strategies, embedding selection, hybrid search
- **Safety and reliability** - designing for non-determinism, hallucination mitigation, prompt injection defense
- **Evaluation design** - how do you measure quality of open-ended outputs at scale?
- **Cost reasoning** - token budgets, model routing (cheap models for simple tasks, expensive for complex), caching strategies
- **Tinkerer mindset** - hands-on experimentation, strong opinions on model selection and tools, not just API wrapper building

Key quote from PromptLayer: "If candidates build anything functional that demonstrates multi-step reasoning, that's a strong signal - perfect accuracy matters less than thoughtful architecture and evaluation approach."


## Topics Unique to AI System Design

These topics appear in AI system design interviews but have no meaningful equivalent in traditional ML system design:

### Prompt and Context Engineering
- System prompt design, few-shot example selection
- Context window management and optimization
- Prompt versioning and A/B testing
- Chip Huyen frames context construction as "equivalent to feature engineering for classical ML models"

### Retrieval-Augmented Generation (RAG)
- Document chunking strategies (fixed-size, semantic, recursive)
- Embedding model selection
- Vector database indexing (HNSW, IVF)
- Hybrid retrieval (BM25 + dense + reranking)
- GraphRAG and Agentic RAG
- Anthropic's [Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval) reduced failed retrievals by 49%

### Guardrails and Safety
- Input validation and prompt injection defense
- Output validation (structural, semantic, safety)
- PII detection and redaction
- Hallucination detection and mitigation
- [Eugene Yan's LLM patterns](https://eugeneyan.com/writing/llm-patterns/) identifies guardrails and defensive UX as core patterns

### Evaluation (Evals)
- LLM-as-judge evaluation pipelines
- Human evaluation protocols at scale
- Task-specific eval design
- Regression testing for prompt changes
- [Hamel Husain](https://hamel.dev/blog/posts/evals/): "Unsuccessful LLM products almost always share a common root cause: a failure to create robust evaluation systems"
- [Shreya Shankar](https://www.sh-reya.com/blog/in-defense-ai-evals/): "Despite all the tooling, there's very little education on how to build evals"

### Multi-Agent Orchestration
- Agent loop design (ReAct, Plan-and-Execute)
- Inter-agent communication and responsibility boundaries
- Failure cascades and human-in-the-loop escalation
- Anthropic's [multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system): orchestrator-worker pattern outperformed single-agent by 90%+

### Token Economics and Model Routing
- Per-token cost optimization
- Model routing based on query complexity (cheap model first, escalate if needed)
- Caching strategies (semantic caching, exact match)
- [LockedIn AI](https://www.lockedinai.com/blog/llm-ai-engineer-interview-questions-silicon-valley): example scenario of 2B daily tokens costing ~$13K with GPT-4 Turbo

### Structured Output and Tool Use
- Schema enforcement (JSON mode, Pydantic validation)
- Tool/function schema design, error handling
- [Jason Liu](https://jxnl.co/)'s Instructor library (6M+ monthly downloads): "LLMs give you strings; Instructor gives you data structures"


## Real Interview Experiences

### Anthropic
30-min recruiter call, 90-min coding challenge, 1-hour hiring manager deep dive, 4-hour virtual onsite. System design questions include: designing a search system for a billion documents with LLM inference at 10K+ RPS, implementing hybrid search across 10M+ documents within 50ms. "Anthropic's evaluation differs from typical FAANG interviews by prioritizing practical, real-world problem-solving over pattern memorization." ([source](https://www.linkjob.ai/interview-questions/anthropic-software-engineer-interview/))

### OpenAI
5-week process: recruiter call, 48-hour take-home, technical screen, virtual onsite (5 rounds: 2 coding, 1 system design, 1 behavioral, 1 hiring manager). System design uses Excalidraw. "The overall style leans heavily toward systems and data processing, unlike the traditional big tech approach focused purely on LeetCode." ([source](https://www.linkjob.ai/interview-questions/openai-loop-interview), [official guide](https://openai.com/interview-guide/))

### Sprinter Health
3-hour onsite: AI-focused Systems Design + Behavioral + Lunch. The role involves synthesizing clinical summaries using LLMs, patient risk prediction, and conversational patient support with AI voice assistants. ([source](https://wellfound.com/jobs/3265793-lead-software-engineer-applied-ai))

### Mai Chi Bao's RAG Chatbot Interview (scored 9/10)
Designed a production customer support chatbot: Llama-2 (7B/13B) with dynamic routing, BGE-M3 embeddings, Milvus for vector search, 4-bit quantization, estimated $2K/month infrastructure. ([source](https://dev.to/mrzaizai2k/how-i-aced-my-llm-interview-building-a-rag-chatbot-2p6f))

### Yuan Meng (Pinterest, DoorDash)
Interviewed at ~10 companies at the onsite stage (OpenAI, Roblox, Databricks, Notion, Netflix, Google, Meta). Documents new interview rounds that didn't exist before: ML Infra Design, LLM Coding (implementing Transformers, LoRA, KV cache from scratch), Research Presentations. "By now, everyone knows how to sketch a multi-stage ranking pipeline... If you sound like everyone else, that won't cut it anymore." ([source](https://www.yuan-meng.com/posts/mle_interviews_2.0/))

### Mimansa Jaiswal (~20+ companies)
Interviewed at Anthropic, OpenAI, Scale AI, Meta, Amazon, Apple, Google, Netflix, and startups. "ML system design, LLM research design, LLM system design" appeared as three distinct interview rounds. Anthropic had seven virtual onsite rounds. "None of the unicorn companies used LeetCode-style questions." ([source](https://mimansajaiswal.github.io/posts/llm-ml-job-interviews-fall-2024-process/))

### Janvi Kalra (46 organizations)
Interviewed at 46 different organizations for AI engineering roles. AI Engineering interviews are "all over the place" - lack standardization. Encountered Leetcode-style challenges, traditional system design, take-homes requiring LLM application development, and domain-specific deep dives. ([source](https://newsletter.pragmaticengineer.com/p/from-software-engineer-to-ai-engineer))


## What Companies Build (Informing Interview Questions)

Real production AI systems described in company engineering blogs - these are the kinds of systems you'd be asked to design:

- **Doctolib** - "Alfred," agentic AI for customer support: multiple specialized AI agents in a directed graph (LangGraph), processes ~17K daily messages, LLM never directly executes sensitive actions ([source](https://medium.com/doctolib/building-an-agentic-ai-system-for-healthcare-support-a-journey-into-practical-ai-implementation-0afd28d716e6))
- **Uber** - GenAI Gateway: unified platform for all LLM use cases, supports OpenAI/Vertex/in-house models through consistent interface, PII redactor, 60+ use cases ([source](https://www.uber.com/blog/genai-gateway/))
- **Airbnb** - Automation Platform v2: evolved from static workflows to LLM-powered conversational AI with Chain of Thought reasoning, context management, and guardrails ([source](https://medium.com/airbnb-engineering/automation-platform-v2-improving-conversational-ai-at-airbnb-d86c9386e0cb))
- **Perplexity** - AI-first search: 200M daily queries, RAG on Vespa.ai, fine-tuned Sonar models, in-house ROSE inference engine, ~38 person engineering team ([source](https://blog.bytebytego.com/p/how-perplexity-built-an-ai-google))
- **Slack** - stateless RAG (all context in each request), LLMs hosted in escrow VPC so model provider has no access to customer data ([source](https://slack.engineering/how-we-built-slack-ai-to-be-secure-and-private/))
- **LinkedIn** - AI agent platform prioritizing execution over intelligence, strict siloing between data layers, many failures stem from missing context not model capability ([source](https://www.infoq.com/news/2025/12/qcon-ai-linkedin/))
- **Anthropic** - multi-agent research: orchestrator-worker pattern, Opus as lead + Sonnet as subagents, multi-agent uses ~15x more tokens than chat ([source](https://www.anthropic.com/engineering/multi-agent-research-system))
- **DoorDash** - LLM chatbot simulation: AI-driven evaluation flywheel replicating real customer interactions, hierarchical RAG for personalized menu descriptions ([source](https://careersatdoordash.com/blog/doordash-simulation-evaluation-flywheel-to-develop-llm-chatbots-at-scale/))


## The Current State of the Field

### Interviews lack standardization
Janvi Kalra (46 companies) and others consistently note that AI engineering interviews are "all over the place." There is no consensus format yet, unlike the relatively standardized FAANG SWE interview loop. ([Pragmatic Engineer](https://newsletter.pragmaticengineer.com/p/from-software-engineer-to-ai-engineer))

### Some traditional questions are becoming obsolete
Brian Kihoon Lee reports receiving a text classification question solvable more effectively with a single LLM API call - but the interviewer lacked knowledge to discuss this approach. This highlights how some interview formats haven't kept pace with the technology. ([source](https://www.moderndescartes.com/essays/ml_eng_interviewing/))

### Production experience matters more than theory
Multiple sources emphasize that interviewers want to know "what breaks, what you've shipped, and how you think about tradeoffs when there's no perfect answer" - not theoretical knowledge about agents. ([TechEon, Jan 2026](https://atul4u.medium.com/the-complete-agentic-ai-system-design-interview-guide-2026-f95d0cfeb7cf))

### Cost awareness is now a core skill
Candidates must reason about token budgets, per-query costs, model tiering, and caching strategies - a dimension largely absent from traditional system design. ([InterviewQuery](https://www.interviewquery.com/p/ai-interview-trends-tech-hiring-2025), [LockedIn AI](https://www.lockedinai.com/blog/llm-ai-engineer-interview-questions-silicon-valley))

### AI-related interview questions tripled since 2023
AI-native roles surged 240% in early 2025. Rather than "Sort this array," candidates now face: "Design an algorithm using an LLM to rank user feedback by sentiment." The shift: interviews now assess "how you reason with AI" rather than "what you know." ([InterviewQuery, 2025](https://www.interviewquery.com/p/ai-interview-trends-tech-hiring-2025))


## Key Books and Resources

| Resource | Author(s) | Year |
|---|---|---|
| [AI Engineering: Building Applications with Foundation Models](https://huyenchip.com/books/) | Chip Huyen | 2025 |
| [Generative AI System Design Interview](https://blog.bytebytego.com/p/our-new-book-generative-ai-system) | Ali Aminian, Hao Sheng (ByteByteGo) | 2024 |
| [Designing Machine Learning Systems](https://huyenchip.com/books/) | Chip Huyen | 2022 |
| [Machine Learning System Design Interview](https://www.amazon.com/Machine-Learning-System-Design-Interview/dp/1736049127) | Ali Aminian, Alex Xu | 2022 |
| [What We Learned from a Year of Building with LLMs](https://applied-llms.org/) | Eugene Yan, Hamel Husain, Jason Liu, Shreya Shankar, et al. | 2024 |
| [Building a Generative AI Platform](https://huyenchip.com/2024/07/25/genai-platform.html) | Chip Huyen | 2024 |
| [Patterns for Building LLM-based Systems](https://eugeneyan.com/writing/llm-patterns/) | Eugene Yan | 2023 |
| [Evidently AI: 800 ML/LLM Case Studies](https://www.evidentlyai.com/ml-system-design) | Evidently AI | ongoing |
| [500+ GenAI/LLM Case Studies (GitHub)](https://github.com/themanojdesai/genai-llm-ml-case-studies) | Manoj Desai | ongoing |
