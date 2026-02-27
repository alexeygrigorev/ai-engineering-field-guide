# AI System Design Interview

AI system design is emerging as a distinct interview category, separate from both traditional software system design and classic ML system design. The shift is driven by the explosion of LLM-powered products: instead of designing training pipelines, candidates design orchestration architectures around pre-trained models.

Companies with dedicated AI system design rounds include Doctolib ("AI System Design Interview"), Sprinter Health ("AI-Focused Systems Design"), and Anthropic (distributed search + LLM inference at scale). Many more are adding AI-flavored questions to existing system design rounds. Companies known to test GenAI system design include Google, Apple, OpenAI, Anthropic, Cohere, Salesforce, and AI-first startups. [^igotanoffer]

System design with AI elements is becoming a critical interview component. Interviewers need to understand how a candidate thinks about building services and components with AI interfaces and tooling -- including understanding limitations on security, access rights, and the reality that AI systems need to scale significantly (potentially 5-10x compared to current load, to 1000+ nodes).

See also: [Awesome AI Engineering](../awesome.md) for the full collection of references, company blogs, and practitioner stories cited below.

## How It Differs from Traditional ML System Design

Traditional ML system design interviews focus on training pipelines: data collection, feature engineering, model selection, offline evaluation, and deployment. Canonical questions include "Design a recommendation system" or "Design a fraud detection system."

AI system design interviews focus on inference orchestration: retrieval, prompt composition, output validation, evaluation, and safety. Canonical questions include "Design a hallucination-free chatbot for banking" or "Design a RAG-powered enterprise search system."

The fundamental shift: when models like GPT-4 and Claude became accessible via APIs, the hard part stopped being model training and started being system orchestration [^chip-huyen-books]

A finer three-way distinction: ML system design interviews focus on full training pipelines (feature stores, model lifecycle, offline evaluation) producing structured outputs. AI system design interviews focus on systems for analysis and prediction where models produce fixed/bounded outputs (scores, labels, rankings) plus agentic systems where models reason and take actions via APIs. Generative AI system design is the specialized subset focusing on systems generating new open-ended content (text, images, code) where the same input produces different responses each time. "GenAI interviews still care about standard distributed-systems basics, but they'll push harder on evaluation, guardrails, and context/tooling design." [^igotanoffer]

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

Source: synthesized from [^yuan-meng] [^brian-kihoon-lee] [^chip-huyen-platform] and the [^promptlayer]


## What Candidates Are Asked

System design and cost/latency optimization are among the most frequently asked topics in AI engineering interviews:

| Category | Frequency | Example questions |
|----------|-----------|-------------------|
| System design | High | "Scale an AI chat feature to 1M daily users - discuss trade-offs" |
| Cost/latency | High | "Your app gets 1M queries/day - how do you optimize cost?" |

### Typical AI System Design Questions

Based on real interview experiences and practitioner guides:

- Design a customer support chatbot that must not hallucinate [^mai-chi-bao] [^bhavishya-pandit]
- Design a RAG-powered Q&A system for internal company documents
- Design a voice assistant for hospital staff
- Design an AI tool to generate legal contracts from prompts
- Design an AI search assistant for 10M+ articles
- Design a search system handling a billion documents and LLM inference for 10K+ RPS [^linkjob-anthropic]
- Design ChatGPT's cross-conversation memory feature
- Design a multi-step agentic workflow (meeting scheduling, code review, email campaigns)
- When is an agentic architecture the wrong solution? (tests judgment about when NOT to use agents -- deterministic workflows, catastrophic/irreversible failures, strict latency SLAs, or when you can't define "done") [^techeon]
- How do you define and enforce agent autonomy boundaries? (four-layer pattern: action classification by risk level, resource budgets enforced in orchestrator, scope constraints at integration layer, approval gates for high-risk actions) [^techeon]
- How do you version and roll back agent behavior? (version the complete configuration: prompts + tool schemas + policies + model version + orchestrator logic as a single deployment identifier; behavioral benchmark suites before deployment; pin model versions since provider updates can silently change behavior) [^techeon]
- Design a feedback loop system for an AI writing tool that improves from user edits [^bhavishya-pandit]
- Design a resume classifier that routes candidates to the right team [^bhavishya-pandit]
- Design ChatGPT / Design an AI chatbot [^igotanoffer] [^designgurus]
- Design a small language model that runs on a phone while ensuring politeness (Google, [^igotanoffer])
- Design the Claude chat service (Anthropic, [^igotanoffer])
- Review a junior developer's inference batching system design and explain what you'd improve (Anthropic, [^igotanoffer])
- Design a model that solves math problems - walk through data collection, SFT, post-training, and evaluation (Cohere, [^igotanoffer])
- Architect an AI agent system including agent loop, tool interfaces, memory, orchestration, and safety (Salesforce, [^igotanoffer])
- Design a system to process 10K user uploads/month (bank payslips, IDs), extract data, detect inconsistencies, and handle LLM provider downtime (Reddit, [^igotanoffer])
- Design a system that lets doctors automatically send billing info to insurers based on patient notes (Reddit, [^igotanoffer])
- Design a large-scale AI model deployment system -- model serving, GPU scaling, model versioning, result caching (OpenAI, [^designgurus])
- Design a real-time chatbot API -- low-latency inference, session management, concurrency, safety filters (OpenAI, [^designgurus])
- Design a distributed training system for deep learning -- data/model parallelism, weight synchronization, failure recovery (OpenAI, [^designgurus])
- Design a scalable data pipeline for ML applications -- streaming/batch ingestion, ETL, database selection, data consistency (OpenAI, [^designgurus])
- General system design questions commonly asked at OpenAI L5: Design GitHub Actions, Design Slack, Design Online Chess, Design a Payment System, Design a Webhook Callback System [^hellointerview]
- Design a language model that minimizes harmful outputs while remaining useful and expressive (Anthropic, [^igotanoffer])
- Design a content/policy violation detection system [^igotanoffer]
- Design the UX for an AI assistant that is often slow [^igotanoffer]

### Expected Architecture Components

Candidates typically design a composable pipeline covering:

1. Problem decomposition - breaking the problem into LLM-solvable sub-tasks
2. Retrieval layer - vector databases, embedding models, chunking strategies, hybrid search (BM25 + dense embeddings)
3. Prompt composition - system prompts, few-shot examples, context injection
4. LLM gateway - model selection/routing, rate limiting, cost management
5. Output validation - guardrails, structured output enforcement, hallucination detection
6. Evaluation system - evals (automated + human), LLM-as-judge, regression testing
7. Feedback loops - user feedback collection, data flywheels, continuous improvement
8. Safety and security - prompt injection defense, PII handling, content filtering

This maps closely to Chip Huyen's 5-step progressive architecture [^chip-huyen-platform]: enhance context (RAG) -> implement guardrails -> add model router/gateway -> reduce latency with cache -> add complex logic and write actions.


## What Interviewers Evaluate

Based on PromptLayer's agentic interview guide [^promptlayer] and multiple practitioner accounts:

- Systems thinking - can you decompose a complex problem into components an LLM can handle?
- Retrieval and context engineering trade-offs - chunking strategies, embedding selection, hybrid search
- Safety and reliability - designing for non-determinism, hallucination mitigation, prompt injection defense
- Evaluation design - how do you measure quality of open-ended outputs at scale?
- Cost reasoning - token budgets, model routing (cheap models for simple tasks, expensive for complex), caching strategies
- Tinkerer mindset - hands-on experimentation, strong opinions on model selection and tools, not just API wrapper building
- AI fluency under observation - some companies allow ChatGPT during live coding to observe how candidates construct prompts, evaluate output, and integrate AI into their workflow [^promptlayer]

Key quote from PromptLayer: "If candidates build anything functional that demonstrates multi-step reasoning, that's a strong signal - perfect accuracy matters less than thoughtful architecture and evaluation approach."

### OpenAI Evaluation Criteria

OpenAI's system design interviews (45-60 min) assess candidates on seven dimensions: scalability (horizontal scaling, sharding, load balancing), reliability and fault tolerance (replication, failover), performance (latency, caching, database choices), AI infrastructure knowledge (model serving, training, data processing), security and privacy (encryption, ethical safeguards), trade-off awareness (clear justification for architectural decisions), and communication clarity. [^designgurus]

Time allocation: ~5 min clarifying the problem, 10-15 min high-level design, 15-20 min deep dive and component design, 5-10 min trade-offs and bottlenecks, remaining time for follow-up scenarios and optimizations. [^designgurus]

### Interview Answer Frameworks

5-Step GenAI System Design Framework (Aniket, Amazon senior PM, via [^igotanoffer]):

1. Problem Framing (5-10 min) - clarify user, use cases, success criteria, constraints (latency, cost, privacy, regions), quality expectations, guardrails, reliability requirements
2. High-Level Architecture (10-15 min) - core components (client, API gateway, auth, orchestration service, retrieval, tools, model(s), storage, analytics), walk through data paths (prompt in, context build, model call, post-processing, logs/telemetry)
3. Deep Dive (20-30 min) - RAG design, tool use/agents, memory, latency/cost, evaluation (offline + online, golden sets, LLM-as-judge pitfalls), safety
4. Trade-Offs (10-15 min) - what breaks, how you detect it, how you degrade gracefully
5. Conclusion - summarize design, list risks, outline next iteration

InterviewNode's 4 Patterns [^interviewnode]: most GenAI system design interviews map to four repeatable blueprints that cover 80-90% of questions:

1. RAG (Retrieval-Augmented Generation) - The most common pattern (2025-2026). Tests system orchestration and grounding accuracy. Senior candidates distinguish themselves by balancing constraints, not just describing components
2. Feedback and reinforcement systems - "How does it get better over time?" Used by OpenAI, Anthropic, and Meta AI. Tests RLHF understanding, implicit/explicit feedback signals, active learning loops
3. Hallucination mitigation - Every senior GenAI role includes at least one hallucination-focused question. Strong answers cover retrieval-grounded pipelines, confidence estimation based on retrieval density and token entropy, source transparency
4. Scalability and cost optimization - Tests engineering realism. Strong answers discuss multi-layer caching (retrieval, prompt, response), model tiering (small distilled model for routine requests, large LLM for high-impact), prompt compression, dynamic throttling

### Common Mistakes Candidates Make

Based on [^igotanoffer] (Aniket, Amazon senior PM) and [^interviewnode]:

- Treating the LLM as a source of truth - relying on raw generation for factual answers instead of grounding with retrieval, tools, or citations
- Skipping evaluation or monitoring - designing without explaining how output quality, regressions, or safety issues will be measured
- Defaulting to fine-tuning too early - jumping to fine-tuning without considering prompting, retrieval, or tools, showing poor judgment on cost and iteration speed
- Ignoring safety and abuse vectors - failing to address prompt injection, data leakage, or unsafe tool execution
- Overlooking latency and cost constraints - designing as if model calls are unlimited without discussing token budgets, caching, or model routing
- Not addressing failure modes - avoiding discussion of what breaks, how failures are detected, and how the system degrades gracefully
- Over-indexing on tools - mentioning LangChain without explaining why; instead of "I'd use LangChain," say "I'd chain retrieval and generation modules to ensure contextual consistency and caching efficiency"
- Forgetting evaluation - never mentioning how post-deployment success will be measured
- Under-explaining data flow - omitting how retrieved context is validated or cached

Additional mistakes specific to agentic system design [^techeon]:

- Putting control flow in prompts - "think in a loop until you solve the problem" puts the LLM in charge of when to stop; this causes infinite loops and runaway costs. Control flow must live in the orchestrator
- Giving agents too much autonomy too fast - starting with agents that can do anything, then struggling to constrain them. Better: start with minimal autonomy, expand based on demonstrated reliability
- Prioritizing capability over reliability - impressive demos over consistent production behavior. "It works most of the time" isn't good enough. Expand capabilities only when current ones are stable
- Trying to solve architectural problems with better prompts - prompts can't fix bad tool designs or missing components. Recognize when the problem is structural
- Choosing agents because they're exciting - not because the problem requires autonomy. Red flag interviewers watch for

### Seniority Expectations

How interviewers differentiate levels [^interviewnode] [^igotanoffer]:

- Junior: focuses on the prompt alone
- Mid-level: describes embeddings or RAG mechanisms; expected to cover both HLD and LLD, end-to-end feature ownership
- Senior/Staff: designs an evolving ecosystem - chunking/embedding/indexing strategies, how retrieval affects context windows, how outputs are validated and stored, how feedback improves retrieval and response quality. Primarily HLD at scale with selective LLD deep dives. A senior candidate evaluates trade-offs systematically rather than selecting the obvious solution.

Three invisible evaluation axes at senior levels: (1) reasoning across uncertainty - keeping the system predictable despite unpredictable outputs, (2) trade-off fluency - discussing retrieval speed vs. context length, fine-tuning vs. prompting, GPU cost vs. latency, (3) communication clarity - narrating how information and control flow through the system logically.


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
- Anthropic's Contextual Retrieval [^anthropic-contextual-retrieval] reduced failed retrievals by 49%
- The "search engine vs answer engine" distinction: returning relevant documents isn't enough - the generation layer that synthesizes a direct answer is where user experience lives. Query classification (factual vs procedural vs comparative) enables specialized prompts that dramatically improve answer quality. Production metrics after adding answer generation: time to find answer dropped from 2.5 min to 15 sec (-94%), user satisfaction rose from 3.2/5 to 4.6/5, support ticket volume dropped 35%, answer accuracy 91%, citation inclusion 87%, 85% cache hit rate for common queries reducing response time from 380ms to 45ms. ROI: ~$120/month compute cost increase, break-even in 6 days. [^hitendra-patel]
- RAG system design in interviews should cover four distinct phases: (1) data ingestion pipeline (chunking strategies, embeddings/vectorization), (2) retrieval layer (vector database, ANN indexing with HNSW), (3) accuracy optimization (hybrid search with Reciprocal Rank Fusion, cross-encoder reranking), (4) generation phase (context construction, hallucination reduction). Scaling considerations: sharding vector indexes across machines with central aggregators, semantic caching to bypass the entire retrieval-generation pipeline for repeated queries. [^designgurus-rag]
- HyDE (Hypothetical Document Embeddings) - a retrieval technique where you generate a hypothetical answer to the query using an LLM, then use that generated answer (not the original question) as the search query against the vector database. This often retrieves more relevant documents because the hypothetical answer is semantically closer to actual stored documents than the raw question is. Questions and answers are structurally different texts, and semantic retrieval is based on similarity between two strings -- so searching with an answer-shaped text against answer-shaped documents improves match quality. Useful for knowledge base search over company documents. [^proptech-founder]

### Guardrails and Safety
- Input validation and prompt injection defense
- Output validation (structural, semantic, safety)
- PII detection and redaction
- Hallucination detection and mitigation
- Eugene Yan's LLM patterns [^eugene-yan] identifies guardrails and defensive UX as core patterns
- Hallucination mitigation as interview pattern: interviewers expect a multi-layered approach - retrieval-grounded pipelines where every generation is backed by retrieved factual context, confidence scoring based on retrieval density and token entropy (low confidence triggers regeneration or human review), source transparency displaying citations to enable external verification, and post-processing validation that checks generated claims (numbers, dates) against source context. Key phrases like "confidence estimation," "source transparency," and "regeneration policy" signal senior thinking. [^interviewnode]
- Banking/financial chatbot pattern: never permit unrestricted LLM responses to factual queries - route to structured APIs for account information, use LLM only to rephrase retrieved data politely with disclaimers, tag every answer with traceable sources, implement confidence thresholds that reject unsupported queries [^bhavishya-pandit]
- Guardrail trade-offs to discuss: reliability vs. latency (most teams find reliability gains outweigh latency cost), stream completion challenges (in streaming mode, unsafe responses may reach users before guardrails block them), self-hosted vs. third-party guardrails (self-hosting eliminates external data transmission but requires internal implementation) [^chip-huyen-platform]
- Legal contract generation pattern: use pre-approved clause templates with fillable slots rather than unrestricted generation; LLMs should paraphrase or combine existing clauses, never invent legal content; version-control all outputs and track edits [^bhavishya-pandit]

### Evaluation (Evals)
- LLM-as-judge evaluation pipelines
- Human evaluation protocols at scale
- Task-specific eval design
- Regression testing for prompt changes
- Hamel Husain [^hamel-husain]: "Unsuccessful LLM products almost always share a common root cause: a failure to create robust evaluation systems"
- Shreya Shankar [^shreya-shankar]: "Despite all the tooling, there's very little education on how to build evals"
- Evaluation topics increasingly split into offline (golden datasets, adversarial testing, red-teaming) and online (A/B testing, user feedback loops, quality dashboards). Common failure taxonomies to discuss: hallucinations, refusal errors, tool misuse, toxicity, data leakage. [^igotanoffer]
- Evaluating long-horizon agent performance: task completion alone is insufficient. Evaluation dimensions include efficiency (steps/cost/time vs baselines), trajectory quality (did the agent take obviously wrong turns or recover from mistakes?), intermediate milestones (80% completion is different from 20%), robustness across task variations, and safety (boundary violations attempted, risky actions proposed even if blocked, near-misses). Also track alignment metrics: goal adherence, unexpected behaviors, policy compliance [^techeon]
- Goal drift detection: require the agent to periodically state its current understanding of the goal and compare against the original; inject re-grounding prompts; measure semantic distance between recent outputs and original goal; monitor action distribution shifts over time; define behavioral bounds and flag deviations. Common drift patterns: proxy optimization, scope creep, local minima, mode collapse [^techeon]

### Feedback Loop Design
- Track user edits as implicit feedback - rewrites indicate dissatisfaction; record which completions get accepted, modified, or discarded
- Cluster failures by category using embedding similarity to identify patterns
- Enable explicit thumbs-up/down ratings and flagging; route flagged responses to human reviewers for supervised fine-tuning
- Design feedback as an architecture layer, not an afterthought: capture implicit satisfaction metrics (thumbs up/down, click-throughs, completion rates), aggregate signals to retrain a reward model, periodically fine-tune via RLHF or preference optimization
- Prioritize stability over speed of learning - updates weekly, not continuously; ensure sampling across diverse users to prevent feedback bias [^interviewnode] [^bhavishya-pandit]

### Multi-Agent Orchestration
- Agent loop design (ReAct, Plan-and-Execute)
- Inter-agent communication and responsibility boundaries
- Failure cascades and human-in-the-loop escalation
- Anthropic's multi-agent research system [^anthropic-multi-agent]: orchestrator-worker pattern outperformed single-agent by 90%+
- When multi-agent is the wrong choice: if the task is actually sequential (coordination overhead without parallelism gain), if a single agent with better prompting would suffice, or if the complexity isn't earned. Decision framework: Can a single agent do this well? Is the limitation fundamental or just prompt engineering? Would separate agents genuinely operate independently? [^techeon]
- Emergent behaviors to discuss: positive emergence (complementary specialization, cross-agent error correction) and negative emergence (metric gaming where a reviewer agent always approves to avoid conflict, information hoarding, inter-agent infinite loops, cascade failures). Monitor system-level outcomes, not just individual agent metrics [^techeon]
- Debugging multi-agent failures: requires distributed tracing with correlation IDs across all agents, interaction logging at every agent boundary, state snapshots to understand what each agent "knew" at each point, causal ordering of events, and replay capability. "If you can't debug it, you can't run it in production" [^techeon]

### Token Economics and Model Routing
- The "triple dipper" triangle - analogous to the CAP theorem in distributed systems, GenAI systems face a three-way trade-off between latency, cost, and retrieval accuracy/relevancy. You can optimize for two but not all three simultaneously. Reducing latency (caching, smaller models, lower embedding dimensions) often reduces cost but may hurt relevancy. Improving relevancy (re-rankers, LLM-as-judge, chain-of-thought reasoning) increases both latency and cost. Discussing how you navigate this triangle signals production maturity. [^proptech-founder]
- Per-token cost optimization
- Model routing based on query complexity (cheap model first, escalate if needed)
- Caching strategies (semantic caching, exact match)
- LockedIn AI [^lockedinai]: example scenario of 2B daily tokens costing ~$13K with GPT-4 Turbo
- Three caching layers to discuss: prompt cache (shared system prompts; 1K-token system prompt with 1M daily calls saves ~1B repetitive input tokens/day), exact cache (product summaries, vector search results; use LRU/LFU eviction, avoid caching user-specific or time-sensitive queries), semantic cache (reuse similar but not identical queries via embedding similarity; "compared to other caching techniques, semantic cache's value is more dubious" - only justified if cache hit rates are high). Scalability interview signal: mention model-choice policies per client, letting them trade cost for quality dynamically. [^chip-huyen-platform] [^interviewnode]

### Agent Memory Systems
- Four memory types for agentic systems: working memory (current task context, conversation history, scratchpad -- high fidelity, limited capacity, cleared between sessions), episodic memory (records of past executions and what worked/failed -- time-indexed, queryable by similarity), semantic memory (long-term knowledge, user preferences, domain facts -- declarative, updated based on experience), procedural memory (learned patterns for accomplishing tasks -- how-to knowledge emerging from successful episodes) [^techeon]
- Memory pollution prevention: selective storage (only confirmed facts, successful patterns, user-provided preferences), quality filtering (verify accuracy, require minimum confidence, filter contradictions), decay mechanisms (recency weighting, confidence decay, usage-based retention), validation at retrieval time (check relevance not just similarity, verify consistency with current context), and user control (view/correct/delete/reset memory). "Bad memories cause bad behavior. Once polluted, recovery is difficult." [^techeon]

### Agent Loop Design and Termination
- Orchestrator vs LLM responsibility split: orchestrator handles control flow, timeout enforcement, budget tracking, state persistence, tool dispatch, error handling, approval routing, observability. LLM handles goal understanding, plan generation, tool selection, result interpretation, completion assessment. Key principle: "Anything that must be guaranteed belongs in the orchestrator. Anything that requires judgment belongs in the LLM." Anti-pattern: putting control flow in prompts ("think in a loop until you solve the problem") -- this causes infinite loops and runaway costs [^techeon]
- Termination conditions (a common interview question for agentic systems): layered strategy with (1) LLM self-assessment as a separate reasoning step, (2) programmatic verification of completion where possible, (3) progress detection to catch stalled agents, (4) hard limits on iterations/time/cost, (5) stuck detection for repeated errors or circular reasoning. "The most insidious failure is an agent that thinks it's making progress but isn't." [^techeon]
- Preventing over-reasoning: enforce step limits in the orchestrator (not in prompts), use action-biased prompting ("take the simplest action that makes progress"), set confidence thresholds with defaults, detect planning loops via semantic similarity of recent reasoning steps, cap task decomposition depth [^techeon]
- Stateless vs stateful agents: most production systems use stateless execution with external state storage -- the orchestrator is stateless and scalable, state lives in a database, any orchestrator instance can resume any agent's work. Stateful agents are necessary for long-running tasks and personalization but risk state corruption and memory pollution [^techeon]

### Observability
- Three monitoring pillars: metrics (system + model + latency + cost), logs ("log everything"), traces (record complete execution path showing query transformation step-by-step)
- Key latency metrics: Time to First Token (TTFT), Time Between Tokens (TBT), Tokens Per Second (TPS), Total latency
- Metrics should be breakdownable by users, releases, prompt/chain versions, types, and time
- "Manual daily inspection of production data helps developers perceive what constitutes good/bad outputs" - enables prompt rewrites and eval pipeline improvements
- Tracing enables pinpointing exact failure steps: incorrect query processing, irrelevant retrieved context, or wrong model responses [^chip-huyen-platform]

### Structured Output and Tool Use
- Schema enforcement (JSON mode, Pydantic validation)
- Tool/function schema design, error handling
- Jason Liu [^jason-liu]'s Instructor library (6M+ monthly downloads): "LLMs give you strings; Instructor gives you data structures"
- Tool schema design to reduce hallucinated actions: use enums over freeform strings, make essential fields required, constrain formats (dates as date types, numbers with ranges), provide descriptions and examples for every field, validate before execution. "The cost of detailed schemas is tiny. The cost of hallucinated tool calls in production is enormous." Test schemas with adversarial prompts to catch common mistakes [^techeon]
- Tool-using agent security risks: prompt injection through tool outputs (malicious data returned by tools that the agent follows as instructions), privilege escalation via tool chains (combining tools to exceed intended privileges), data exfiltration (accessing sensitive data via one tool and leaking via another), confused deputy attacks (agent manipulated into acting on attacker's behalf using its own privileges). Mitigations: sanitize tool outputs, analyze tool compositions for privilege escalation, classify data sensitivity, strict schema validation [^techeon]

### User Experience Design for AI Products
- When and how the system should ask clarifying questions or provide partial answers
- How uncertainty or limitations in model outputs are communicated to users
- Latency masking techniques (streaming responses, progressive rendering)
- Using citations and sources to build trust - users are much more likely to trust answers with citations even if they rarely click through to verify
- Users don't read long answers: responses longer than 3-4 sentences get skipped; lead with the direct answer for factual questions
- Interview questions: "Design the UX for an AI assistant that is often slow," "How would you surface model limitations or errors to users without breaking trust?" [^igotanoffer]

### Distributed Systems Fundamentals for GenAI
GenAI system design heavily tests core distributed systems basics since LLM systems are expensive, latency-sensitive, and dependent on external providers. Candidates should be comfortable with: caching, queues, rate limiting, and backpressure to protect providers; multi-region deployment, observability, and fault isolation; cost modeling and capacity planning. "GenAI interviews still care about standard distributed-systems basics, but they'll push harder on evaluation, guardrails, and context/tooling design." [^igotanoffer]


## Real Interview Experiences

### Anthropic
30-min recruiter call, 90-min coding challenge, 1-hour hiring manager deep dive, 4-hour virtual onsite. System design questions include: designing a search system for a billion documents with LLM inference at 10K+ RPS, implementing hybrid search across 10M+ documents within 50ms. "Anthropic's evaluation differs from typical FAANG interviews by prioritizing practical, real-world problem-solving over pattern memorization." [^linkjob-anthropic]

### OpenAI
5-week process: recruiter call, 48-hour take-home, technical screen, virtual onsite (5 rounds: 2 coding, 1 system design, 1 behavioral, 1 hiring manager). System design uses Excalidraw. System design questions are directly tied to the role - e.g., design the OpenAI Playground (emphasis on frontend/UX, wireframes, developer workflow). Includes a refactoring round: 100-120 lines of intentionally convoluted code to refactor for maintainability. AI tools allowed during coding. "The overall style leans heavily toward systems and data processing, unlike the traditional big tech approach focused purely on LeetCode." [^linkjob-openai] [^exponent-openai] [^openai-guide]

At L5 (Staff), the process is more extensive: 6-8 rounds spanning 8-12 weeks, including recruiter/HM intro, coding screen, architecture/system design screen, then an onsite with coding, system design, technical project presentation (mandatory, heavily weighted - 30 min content + Q&A), behavioral-leadership, and behavioral-collaboration rounds. Notable: system design questions at L5 are often generic distributed systems problems (Design GitHub Actions, Design Slack, Design Online Chess, Design a Payment System, Design a Webhook Callback System) rather than AI-specific. Coding questions are also practical rather than LeetCode: KV store serialize/deserialize, in-memory database with SQL-like operations, Unix cd command with symbolic link resolution. The architecture round carries "enormous weight" - interviewers introduce new constraints mid-interview to test adaptability. No-reference policy for coding rounds. [^hellointerview]

OpenAI's system design questions typically focus on AI-driven and large-scale data infrastructure: design a large-scale AI model deployment system (model serving, GPU scaling, versioning), design a real-time chatbot API (low-latency, session management, safety filters), design a distributed training system (data/model parallelism, weight synchronization, failure recovery), design a scalable ML data pipeline (streaming/batch ingestion, ETL, throughput). [^designgurus]

### Sprinter Health
3-hour onsite: AI-focused Systems Design + Behavioral + Lunch. The role involves synthesizing clinical summaries using LLMs, patient risk prediction, and conversational patient support with AI voice assistants. [^wellfound-sprinter]

### Mai Chi Bao's RAG Chatbot Interview (scored 9/10)
Designed a production customer support chatbot: Llama-2 (7B/13B) with dynamic routing, BGE-M3 embeddings, Milvus for vector search, 4-bit quantization, vLLM for request batching, estimated $2K/month infrastructure. Cost breakdown: LLM service (5x g4dn.12xlarge) $1,417, backend $201, Kafka cluster $301, vector DB $101. Performance: ~0.1s retrieval + ~1.5s generation = <2s total latency for 100+ concurrent users. [^mai-chi-bao]

### Yuan Meng (Pinterest, DoorDash)
Interviewed at ~10 companies at the onsite stage (OpenAI, Roblox, Databricks, Notion, Netflix, Google, Meta). Documents new interview rounds that didn't exist before: ML Infra Design, LLM Coding (implementing Transformers, LoRA, KV cache from scratch), Research Presentations. "By now, everyone knows how to sketch a multi-stage ranking pipeline... If you sound like everyone else, that won't cut it anymore." [^yuan-meng]

### Mimansa Jaiswal (~20+ companies)
Interviewed at Anthropic, OpenAI, Scale AI, Meta, Amazon, Apple, Google, Netflix, and startups. "ML system design, LLM research design, LLM system design" appeared as three distinct interview rounds. Anthropic had seven virtual onsite rounds. "None of the unicorn companies used LeetCode-style questions." [^mimansa-jaiswal]

### Janvi Kalra (46 organizations)
Interviewed at 46 different organizations for AI engineering roles. AI Engineering interviews are "all over the place" - lack standardization. Encountered Leetcode-style challenges, traditional system design, take-homes requiring LLM application development, and domain-specific deep dives. [^pragmatic-engineer]


## What Companies Build (Informing Interview Questions)

Real production AI systems described in company engineering blogs - these are the kinds of systems you'd be asked to design:

- Doctolib - "Alfred," agentic AI for customer support: multiple specialized AI agents in a directed graph (LangGraph), processes ~17K daily messages, LLM never directly executes sensitive actions [^doctolib]
- Uber - GenAI Gateway: unified platform for all LLM use cases, supports OpenAI/Vertex/in-house models through consistent interface, PII redactor, 60+ use cases [^uber]
- Airbnb - Automation Platform v2: evolved from static workflows to LLM-powered conversational AI with Chain of Thought reasoning, context management, and guardrails [^airbnb]
- Perplexity - AI-first search: 200M daily queries, RAG on Vespa.ai, fine-tuned Sonar models, in-house ROSE inference engine, ~38 person engineering team [^bytebytego-perplexity]
- Slack - stateless RAG (all context in each request), LLMs hosted in escrow VPC so model provider has no access to customer data [^slack]
- LinkedIn - AI agent platform prioritizing execution over intelligence, strict siloing between data layers, many failures stem from missing context not model capability [^linkedin]
- Anthropic - multi-agent research: orchestrator-worker pattern, Opus as lead + Sonnet as subagents, multi-agent uses ~15x more tokens than chat [^anthropic-multi-agent]
- DoorDash - LLM chatbot simulation: AI-driven evaluation flywheel replicating real customer interactions, hierarchical RAG for personalized menu descriptions [^doordash]


## The Current State of the Field

### Interviews lack standardization
Janvi Kalra (46 companies) and others consistently note that AI engineering interviews are "all over the place." There is no consensus format yet, unlike the relatively standardized FAANG SWE interview loop. [^pragmatic-engineer]

### Some traditional questions are becoming obsolete
Brian Kihoon Lee (~70 interviews, 7 offers) identifies four problems with current ML system design interviews: generic system design disguised with ML terminology, interviewers asking hyper-specific questions from their narrow project experience, vague prompts that fail to generate substantive discussion, and outdated content that ignores LLM-era approaches. He received a text classification question solvable more effectively with a single LLM API call - but the interviewer lacked knowledge to discuss this approach. [^brian-kihoon-lee]

### Production experience matters more than theory
Multiple sources emphasize that interviewers want to know "what breaks, what you've shipped, and how you think about tradeoffs when there's no perfect answer" - not theoretical knowledge about agents. [^techeon]

### Cost awareness is now a core skill
Candidates must reason about token budgets, per-query costs, model tiering, and caching strategies - a dimension largely absent from traditional system design. [^interviewquery] [^lockedinai]

### AI-related interview questions tripled since 2023
AI-native roles surged 240% in early 2025. Rather than "Sort this array," candidates now face: "Design an algorithm using an LLM to rank user feedback by sentiment." The shift: interviews now assess "how you reason with AI" rather than "what you know." [^interviewquery]


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
| [IGotAnOffer GenAI System Design Guide](https://igotanoffer.com/en/advice/generative-ai-system-design-interview) | IGotAnOffer (Aniket, ex-Amazon) | 2025 |
| [OpenAI L5 Interview Guide](https://www.hellointerview.com/guides/openai/l5) | HelloInterview | 2025 |
| [GenAI System Design Interview Patterns](https://www.interviewnode.com/post/generative-ai-system-design-interview-patterns-you-should-know) | InterviewNode | 2025 |
| [The Complete Agentic AI System Design Interview Guide 2026](https://atul4u.medium.com/the-complete-agentic-ai-system-design-interview-guide-2026-f95d0cfeb7cf) | TechEon | 2026 |
| [System Design for RAG](https://www.designgurus.io/blog/system-design-for-rag) | Arslan Ahmad (DesignGurus) | 2026 |
| [OpenAI System Design Interview Questions](https://www.designgurus.io/blog/openai-system-design-interview-questions) | DesignGurus | 2025 |


## Comprehensive Question Bank

This section catalogs AI/ML system design interview questions that people are actually asked, organized by category. Questions are drawn from real interview experiences, practitioner accounts, company-specific interview guides, and community reports (Reddit, LeetCode, Glassdoor). Where known, the source company and guidance on what constitutes a strong answer are included.

---

### RAG & Search Systems

| # | Question | Source / Company | What Makes a Strong Answer |
|---|----------|-----------------|---------------------------|
| 1 | Design a RAG-powered Q&A system for internal company documents | Common across AI companies | Cover the full pipeline: document ingestion, chunking strategy (semantic vs. fixed-size with overlap), embedding model selection, vector database indexing (HNSW), hybrid retrieval (BM25 + dense), cross-encoder reranking, prompt construction with retrieved context, hallucination mitigation via "answer only from context" instructions, and evaluation with precision@k and retrieval hit rate. Discuss freshness (re-embedding on edits) and deletion/compliance. [^bhavishya-pandit] [^designgurus-rag] |
| 2 | Design an LLM-powered enterprise search system | OpenAI [^igotanoffer] | Distinguish between "search engine" (returning documents) and "answer engine" (synthesizing direct answers). Cover query classification (factual vs. procedural vs. comparative), specialized prompts per query type, citation inclusion, and caching strategies for common queries. Metrics: time to find answer, user satisfaction, answer accuracy, citation rate. |
| 3 | Design an AI search assistant for 10M+ articles | [^bhavishya-pandit] | Focus on scaling: shard documents by topic for distributed retrieval, use domain-specific embeddings, implement hot-query caching for trending searches, combine sparse (BM25) and dense retrieval, rerank with cross-encoders. Evaluate using precision@k and recall. Include feedback systems for ranking refinement. |
| 4 | Design a search system handling a billion documents and LLM inference for 10K+ RPS | Anthropic onsite [^linkjob-anthropic] | Requires distributed systems depth: vector index sharding across machines with central aggregators, approximate nearest neighbor algorithms at scale, sub-50ms retrieval latency, batched LLM inference, GPU serving optimization, and caching layers (prompt cache, exact cache, semantic cache). |
| 5 | Design a question-answering system over internal documentation | [^systemdesignhandbook] | Use RAG with vector retrieval over chunked documents, tune similarity thresholds using feedback loops, trigger async re-embedding on edits, schedule periodic rebuilds for volatile content. Discuss when to return "I don't know" vs. attempting an answer. |
| 6 | Design a generative AI document-processing pipeline for unstructured data (emails, PDFs, images) to automate workflows like claims processing | Reddit [^igotanoffer] | Cover multi-modal ingestion (OCR for images, text extraction for PDFs), structured data extraction, entity recognition, validation against business rules, human-in-the-loop for low-confidence extractions, and audit trail. |
| 7 | Design a system to process 10K user uploads/month (bank payslips, IDs, references), extract data, detect inconsistencies, and handle LLM provider downtime | Reddit [^igotanoffer] | Address document classification, OCR + LLM extraction pipeline, cross-document consistency checks, fallback providers for LLM downtime, queue-based async processing, and PII handling for financial documents. |
| 8 | How would you design a podcast search engine? | [^exponent] | Transcription pipeline (Whisper), chunking by topic/segment, embedding and indexing, search across both text and audio metadata, snippet extraction for preview, and ranking by relevance and recency. |
| 9 | Design multi-modal search (text + image) | [^interviewnode-hld] | Cover CLIP-style joint embedding space, separate indexing for text and image modalities, fusion strategies for cross-modal queries, and challenges of aligning different modality representations. |
| 10 | Design visual search for Pinterest | Pinterest [^exponent] | CNN-based feature extraction, approximate nearest neighbor search at scale, handling diverse image categories, query-by-image interface, and relevance feedback. |

### Chatbots & Conversational AI

| # | Question | Source / Company | What Makes a Strong Answer |
|---|----------|-----------------|---------------------------|
| 1 | Design a hallucination-free chatbot for banking | [^bhavishya-pandit] [^mai-chi-bao] | Never permit unrestricted LLM responses to factual queries. Route to structured APIs for account information; LLM only rephrases retrieved data politely with disclaimers. Tag every answer with traceable sources. Implement confidence thresholds that reject unsupported queries. Log all interactions for auditability. |
| 2 | Design ChatGPT / Design an AI chatbot | OpenAI [^igotanoffer] | Scope to a specific feature (e.g., backend architecture). Cover multi-turn conversation management, context window budgeting, streaming responses, session storage, safety filters, rate limiting, and cost management. Discuss model routing for different query complexities. |
| 3 | Design the Claude chat service | Anthropic [^igotanoffer] | Safety as first-class concern (Constitutional AI principles). Sub-200ms time-to-first-token latency, GPU memory constraints, batching strategy, content filtering integrated into inference pipeline without destroying performance, GDPR/SOC 2 compliance. [^systemdesignhandbook-anthropic] |
| 4 | Design a real-time chatbot API | OpenAI [^designgurus] | Low-latency handling, session management, concurrency, safety filters in responses. Cover WebSocket vs. SSE for streaming, stateless service scaling via Kubernetes, and graceful degradation under load. |
| 5 | Design ChatGPT's cross-conversation memory feature | Common across AI companies | Four memory types: working (current session), episodic (past interactions), semantic (user preferences), procedural (learned patterns). Cover memory pollution prevention, selective storage, confidence-based retention, user control (view/correct/delete), and privacy implications. [^techeon] |
| 6 | Design a customer support chatbot that routes tickets, drafts responses, and escalates complex issues | [^promptlayer] | Intent classification, severity routing, template-based responses for common issues, LLM-generated responses for complex ones, human escalation triggers, feedback loop from agent corrections, and analytics on resolution rates. |
| 7 | Design a conversational recommender system that suggests products based on user preferences, combining chat, retrieval, and database layers | Reddit [^igotanoffer] | Multi-turn preference elicitation, product catalog search (hybrid retrieval), personalization based on conversation history, structured output for product cards, and graceful handling when preferences are vague. |
| 8 | Design a voice assistant for hospital staff | [^bhavishya-pandit] | Deploy ASR (Whisper) on-device or at edge for latency. Fine-tune for medical terminology. Route detected intents to appropriate tools. Encrypt sensitive data. Include confirmation mechanisms ("Did you mean...?") to prevent critical errors. Provide typed fallback when audio fails. |
| 9 | Design the UX for an AI assistant that is often slow | [^igotanoffer] | Streaming responses (token-by-token rendering), progressive rendering, skeleton UIs, latency budgets communicated to users, partial answers while computing full response, and citation/source display to build trust while waiting. |
| 10 | Design an internal Slack bot answering HR questions | [^systemdesignhandbook] | RAG over HR policy documents, access control (different answers for different roles), PII handling, audit logging, confidence thresholds with "contact HR directly" fallback, and Slack-specific UX constraints (message length, threading). |

### Agentic Systems & Multi-Agent

| # | Question | Source / Company | What Makes a Strong Answer |
|---|----------|-----------------|---------------------------|
| 1 | Architect an AI agent system including agent loop, tool interfaces, memory, orchestration, and safety | Salesforce [^igotanoffer] | Cover ReAct or Plan-and-Execute loop, tool schema design (enums over freeform strings, required fields, format constraints), four memory types (working/episodic/semantic/procedural), orchestrator vs. LLM responsibility split, approval gates for high-risk actions, and termination conditions. [^techeon] |
| 2 | When is an agentic architecture the wrong solution? | [^techeon] | Tests judgment about when NOT to use agents. Strong answers identify: deterministic workflows where a simple pipeline suffices, catastrophic/irreversible failures, strict latency SLAs, cases where you cannot define "done," or when a single agent with better prompting would suffice. Decision framework: Can a single agent do this? Is the limitation fundamental or just prompt engineering? |
| 3 | How do you define and enforce agent autonomy boundaries? | [^techeon] | Four-layer pattern: action classification by risk level, resource budgets enforced in orchestrator, scope constraints at integration layer, approval gates for high-risk actions. Discuss the spectrum from fully autonomous to human-in-the-loop. |
| 4 | How do you version and roll back agent behavior? | [^techeon] | Version the complete configuration: prompts + tool schemas + policies + model version + orchestrator logic as a single deployment identifier. Behavioral benchmark suites before deployment. Pin model versions since provider updates can silently change behavior. |
| 5 | Design a multi-step agentic workflow for meeting scheduling / code review / email campaigns | Common across AI companies | Decompose into sub-tasks, define tool interfaces for each step, handle inter-step dependencies, implement checkpointing for long-running tasks, design failure recovery (retry vs. skip vs. human escalation), and set budget/time limits per agent. |
| 6 | Design an agent that reads customer CSV data and generates personalized email campaigns with evaluation metrics | [^promptlayer] | Data parsing and validation, customer segmentation, template generation with personalization, A/B testing framework for email variants, evaluation metrics (open rate prediction, relevance scoring), and batch vs. real-time generation trade-offs. |
| 7 | Design a system where agents collaborate on research reports with citations | [^promptlayer] | Orchestrator-worker pattern: lead agent decomposes research question, worker agents search different sources, synthesis agent combines findings with citation tracking. Discuss inter-agent communication, shared memory, conflict resolution, and quality verification. |
| 8 | Design a code review agent that suggests improvements | [^promptlayer] | AST parsing, diff analysis, pattern-based rule checking, LLM-powered review for higher-level suggestions, severity classification, false positive management, and integration with CI/CD pipelines. |
| 9 | How do you prevent infinite loops and runaway costs in agentic systems? | [^techeon] [^systemdesignhandbook-agentic] | Layered termination: LLM self-assessment, programmatic verification, progress detection, hard limits on iterations/time/cost, stuck detection via semantic similarity of recent reasoning steps, action-biased prompting, and cap on task decomposition depth. "The most insidious failure is an agent that thinks it's making progress but isn't." |
| 10 | How do you debug multi-agent failures? | [^techeon] | Distributed tracing with correlation IDs across all agents, interaction logging at every agent boundary, state snapshots, causal ordering of events, replay capability. "If you can't debug it, you can't run it in production." |

### Content Generation & Moderation

| # | Question | Source / Company | What Makes a Strong Answer |
|---|----------|-----------------|---------------------------|
| 1 | Design an AI tool to generate legal contracts from prompts | [^bhavishya-pandit] | Use pre-approved clause templates with fillable slots rather than unrestricted generation. LLMs should paraphrase or combine existing clauses, never invent legal content. UI for clause selection. Comprehensive clause metadata. Version-control all outputs. Track edits meticulously. |
| 2 | Design a language model that minimizes harmful outputs while remaining useful and expressive | Anthropic [^igotanoffer] | Constitutional AI approach: define principles, train model to self-critique, RLHF alignment. Discuss the tension between safety and usefulness, over-refusal as a failure mode, red-teaming methodology, and measuring both helpfulness and harmlessness simultaneously. |
| 3 | Design a content/policy violation detection system | [^igotanoffer] | Multi-stage pipeline: fast keyword/regex filter, embedding-based classifier for nuanced content, LLM-as-judge for edge cases. Discuss false positive vs. false negative trade-offs, human review queues, policy versioning, and handling adversarial content. |
| 4 | Design a feedback loop system for an AI writing tool that improves from user edits | [^bhavishya-pandit] | Track user edits as implicit feedback (rewrites indicate dissatisfaction). Record which completions get accepted/modified/discarded. Cluster failures by category using embedding similarity. Enable explicit ratings. Route flagged responses to human reviewers. Update prompts and reranker models. Prioritize stability over speed of learning. [^interviewnode] |
| 5 | Design an automated comment moderation system | Meta [^exponent] | Real-time classification (toxic, spam, off-topic), multi-language support, context-aware moderation (sarcasm, quotes), appeal workflow, human review for borderline cases, and feedback loop from user reports. |
| 6 | Design a fake news detection system | Meta [^exponent] | Multi-signal approach: content analysis (linguistic patterns), source credibility scoring, cross-reference with fact-checking databases, propagation pattern analysis, and confidence-based labeling rather than binary classification. |
| 7 | Design a spam detection system | Pinterest [^exponent] | Feature engineering from content + user behavior + network patterns, real-time vs. batch detection, adversarial robustness (spammers adapt), false positive impact on legitimate users, and model retraining cadence. |
| 8 | Design a deepfake video detection system | [^interviewnode-hld] | Frame-level analysis (facial inconsistencies, lighting artifacts), temporal analysis (unnatural movements), audio-visual sync checking, adversarial robustness, and the arms race between generation and detection. |
| 9 | Design a system that detects whether content violates policy or contains offensive material | [^igotanoffer] | Taxonomy of violations, multi-modal detection (text + image), cultural sensitivity across regions, threshold tuning per policy category, escalation paths, and transparency reporting. |
| 10 | Design a fast autocomplete system using LLMs | [^systemdesignhandbook] | Use local/small models (Mistral, LLaMA) with short context windows, stream responses token-by-token, prerender top-3 suggestions client-side, warm GPU pools to avoid cold-start, debounce rapid keystrokes. Target sub-500ms latency. |

### Traditional ML Systems (Recommendation, Fraud, Ranking)

These questions are still commonly asked at AI companies, including those focused on LLMs, because the underlying ML infrastructure and systems thinking remain foundational.

| # | Question | Source / Company | What Makes a Strong Answer |
|---|----------|-----------------|---------------------------|
| 1 | Design a recommendation system (products, movies, music) | Meta, Netflix, Spotify, Pinterest [^exponent] | Two-tower architecture for candidate retrieval + ranking model. Cover collaborative filtering, content-based filtering, cold-start problem, real-time feature updates, A/B testing framework, and business metrics (engagement, revenue, diversity). Discuss offline (AUC, NDCG) and online (CTR, session length) evaluation. |
| 2 | Design the Facebook News Feed ranking system | Meta [^exponent] [^interviewnode-hld] | Multi-objective ranking (engagement, time spent, shares, hides), multi-stage pipeline (candidate generation -> lightweight ranking -> heavy ranking -> re-ranking for diversity), feature engineering (user, post, context features), and balancing engagement with user well-being. |
| 3 | Design TikTok's "For You" page | TikTok [^exponent] [^interviewnode-hld] | Emphasis on exploration vs. exploitation trade-off, cold-start for new users, real-time feedback (watch time, replays, shares), content diversity, creator fairness, and the unique challenge of short-form video features. |
| 4 | Design an ad click prediction / ads ranking system | Meta, Google [^exponent] | Predict click-through rate and conversion rate, feature engineering from user + ad + context, calibration requirements, auction mechanics, advertiser budget management, real-time bidding constraints, and evaluation framework. |
| 5 | Design a fraud detection system | PayPal, Stripe [^exponent] [^getsdeready] | Real-time classification with extreme class imbalance, feature engineering from transaction patterns, graph-based features (user-merchant networks), semi-supervised learning with limited labels, false positive management (blocking legitimate transactions), and explainability requirements for regulatory compliance. |
| 6 | Design a "People You May Know" system | LinkedIn, Meta [^interviewnode-hld] | Graph-based features (mutual connections, shared groups), embedding-based similarity, candidate generation at scale, ranking by connection probability, privacy constraints, and handling the cold-start problem for new users. |
| 7 | Design YouTube Search / Google Search autocomplete | Google, YouTube [^interviewnode-hld] | Query understanding (intent classification, spell correction, query expansion), multi-stage retrieval + ranking, personalization, freshness vs. relevance trade-off, and Trie-based structures for prefix matching combined with semantic search. |
| 8 | Design a home price prediction system (Zillow Zestimate) | Zillow [^interviewnode-hld] | Feature engineering from property attributes + location + market conditions + comparable sales, ensemble methods, spatial modeling, handling data sparsity in some regions, and confidence intervals rather than point estimates. |
| 9 | Design Uber's ETA prediction system | Uber [^interviewquery-ml] | Real-time features (traffic, weather, events), graph-based routing, historical patterns, driver behavior modeling, and the challenge of cascading errors (ETA affects dispatch affects actual arrival time). |
| 10 | Design a resume classifier that routes candidates to the right team | [^bhavishya-pandit] | Embed resumes using professionally-focused models, multi-label classification on historical routing data, business rule overlay ("Java + ML -> Applied AI team"), recruiter override mechanism treating corrections as training data. |
| 11 | Design Spotify's Discover Weekly playlist | Spotify [^interviewquery-ml] | Collaborative filtering + content-based features (audio analysis, genre), novelty/freshness requirements, evaluation beyond accuracy (discovery, diversity, user satisfaction), and weekly batch generation at scale. |
| 12 | Design a customer churn prediction system | Common across companies [^getsdeready] | Feature engineering from usage patterns + support interactions + billing history, survival analysis, actionable predictions (which intervention?), segment-specific models, and measuring intervention effectiveness. |
| 13 | Design a supply chain optimization system using ML | [^getsdeready] | Demand forecasting (time series + external signals), inventory optimization, multi-echelon supply chains, uncertainty quantification, and integration with ERP systems. |
| 14 | Design an ML system making stock predictions from Reddit comments | JP Morgan Chase [^interviewquery-ml] | Sentiment analysis on noisy social data (slang, sarcasm, memes), feature extraction from post metadata (upvotes, awards, author history), time-series alignment with market data, and the challenge of non-stationarity. |
| 15 | Design a trending hashtags system | Twitter/X [^interviewnode-hld] | Real-time streaming aggregation, anomaly detection (distinguishing organic trends from coordinated manipulation), geographic and temporal bucketing, personalization, and handling bursty traffic. |

### Infrastructure & Serving (Model Deployment, Distributed Training, Inference Optimization)

| # | Question | Source / Company | What Makes a Strong Answer |
|---|----------|-----------------|---------------------------|
| 1 | Design a large-scale AI model deployment system | OpenAI [^designgurus] | Model serving infrastructure (TensorFlow Serving, vLLM), GPU scaling and instance management, model versioning and rollback, result caching, canary/shadow deployment strategies, A/B testing, and monitoring (latency P50/P95/P99, throughput, error rates). |
| 2 | Design a distributed training system for deep learning | OpenAI [^designgurus] [^interviewnode-hld] | Data parallelism vs. model parallelism vs. tensor parallelism vs. pipeline parallelism. All-reduce for gradient synchronization. Failure recovery (checkpointing). Efficient hardware utilization. NVLink vs. InfiniBand for inter-GPU communication. Monitoring training progress. |
| 3 | Review a junior developer's inference batching system design and explain what you'd improve | Anthropic [^igotanoffer] | Tests ability to critique existing designs. Look for: batch size optimization (throughput vs. latency trade-off), dynamic batching, padding efficiency, memory management, queue prioritization, and handling variable-length inputs. |
| 4 | Design a scalable ML data pipeline | OpenAI [^designgurus] | Streaming (Kafka) vs. batch (Spark) ingestion, ETL transformations, database selection for different data types, throughput management, data consistency, and feature store architecture to prevent training-serving skew. |
| 5 | How would you reduce LLM inference costs by 50%? | [^interviewnode-hld] [^systemdesignhandbook] | Three-layer caching (prompt cache, exact cache, semantic cache), model routing (cheap models for simple tasks), prompt compression, quantization (FP16 to INT8), model distillation, batching optimization, and tiered routing (e.g., 70% to smaller model, 20% to GPT-4, 10% to Mixtral). |
| 6 | Design a system to handle traffic spikes without overwhelming the model provider | [^igotanoffer] | Queue-based load leveling, rate limiting with backpressure, priority tiers, auto-scaling inference instances, fallback to smaller models under load, and graceful degradation (serve cached results or simplified responses). |
| 7 | How would you think about cost and capacity planning for an LLM-powered application at scale? | [^igotanoffer] | Back-of-envelope token budget calculations (users x interactions x tokens), cost estimation per model tier, peak traffic multipliers, model routing economics, and when self-hosting vs. API becomes cost-effective. Example: 100K DAU x 10 interactions x 2K tokens = 2B tokens/day, ~$13K/day with GPT-4 Turbo. [^lockedinai] [^systemdesignhandbook] |
| 8 | Design a small language model that runs on a phone while ensuring politeness | Google [^igotanoffer] | Model compression (quantization, distillation, pruning), on-device inference optimization, limited context window management, safety alignment for small models, and the trade-off between model size and quality. |
| 9 | Design an ML platform for 1000 engineers | [^interviewnode-hld] | Shared feature store, model registry with versioning, experiment tracking, CI/CD for models, compute resource management (GPU scheduling), self-service model deployment, and platform observability. |
| 10 | Handle 1M ML predictions per second | [^interviewnode-hld] | Model optimization (quantization, ONNX runtime), horizontal scaling with load balancing, prediction caching, micro-batching, feature pre-computation, and SLA-based routing between models of different sizes. |
| 11 | Optimize a model for edge devices | [^interviewnode-hld] | Quantization-aware training, knowledge distillation, pruning, TensorRT/CoreML optimization, memory-efficient architectures, and the trade-off between latency and accuracy on constrained hardware. |

### Data Processing & Pipelines

| # | Question | Source / Company | What Makes a Strong Answer |
|---|----------|-----------------|---------------------------|
| 1 | How do you handle real-time versus batch processing for data updates? When is one preferred over the other? | Common interview question [^exponent-youtube] | Real-time: data freshness is critical (fraud detection, live recommendations). More expensive, complex, requires always-on infrastructure (Kafka). Batch: delay is acceptable (embedding generation, model retraining). Cheaper, simpler, easier to debug. Default to batch unless real-time is truly needed. |
| 2 | How do you ensure the quality of data that an LLM interacts with? | Common interview question [^exponent-youtube] | Deduplication (hashing, MinHash, cosine similarity), normalization (consistent units, stripping HTML), validation schemas, data freshness checks, and PII detection/redaction. |
| 3 | How would you efficiently generate and store embeddings for a large product catalog? | Common interview question [^exponent-youtube] | Select which fields to embed (title + description, skip SKU/price), batch generation pipeline, vector database selection, index optimization (HNSW parameters), query rewriting for multi-turn conversations, and HyDE (hypothetical document embeddings) technique. |
| 4 | How do you ingest and process different types of data (structured, unstructured, event logs)? | Common interview question [^exponent-youtube] | Structured data -> SQL database (Postgres); unstructured data -> chunk, embed, vector database; high-volume event data -> message queue (Kafka) or columnar store (ClickHouse). Justify each choice based on query patterns and volume. |
| 5 | Design a feature store for a recommendation system | Netflix, Uber [^yuan-meng-infra] | Online (low-latency serving) vs. offline (batch training) stores, point-in-time correctness to prevent data leakage, feature versioning, real-time feature updates (streaming aggregations via Kafka + Flink), and preventing training-serving skew. |
| 6 | Handle data drift in production ML systems | Common across companies [^interviewnode-hld] | Statistical monitoring of input distributions, performance metric tracking, automated alerts, retraining triggers, A/B testing new models, and gradual rollout strategies. Distinguish between data drift, concept drift, and model degradation. |
| 7 | Design a data pipeline for processing large-scale user interaction logs into training data | Common ML infra question [^yuan-meng-infra] | Streaming ingestion (Kafka), ETL with Spark/Flink, deduplication and cleaning, feature extraction, label generation from implicit signals, storage in data lake + feature store, and versioned dataset management. |

### Evaluation & Monitoring Systems

| # | Question | Source / Company | What Makes a Strong Answer |
|---|----------|-----------------|---------------------------|
| 1 | Design a model that solves math problems -- walk through data collection, SFT, post-training, and evaluation | Cohere [^igotanoffer] | Data curation (math datasets, synthetic generation), supervised fine-tuning on step-by-step solutions, post-training with RLHF or DPO, evaluation on standard benchmarks (MATH, GSM8K) plus custom test sets, chain-of-thought evaluation, and error categorization (arithmetic, reasoning, formatting). |
| 2 | Design a scalable system for training a large language model | OpenAI [^igotanoffer] | Data collection and curation at scale, distributed training across thousands of GPUs, checkpointing and failure recovery, training monitoring (loss curves, gradient norms), evaluation during training, and cost management. |
| 3 | Design an A/B testing framework for ML models | Common across companies [^interviewnode-hld] | Traffic splitting strategies, metric selection (guardrail metrics vs. primary metrics), statistical significance calculation, handling network effects, long-term vs. short-term metric trade-offs, and rollback procedures. |
| 4 | How would you evaluate long-horizon agent performance? | [^techeon] | Task completion alone is insufficient. Evaluate efficiency (steps/cost/time vs. baselines), trajectory quality, intermediate milestones, robustness across task variations, and safety (boundary violations, near-misses). Track alignment metrics: goal adherence, unexpected behaviors, policy compliance. |
| 5 | How do you detect goal drift in agents? | [^techeon] | Periodic goal restatement by agent, semantic distance measurement between recent outputs and original goal, action distribution monitoring, behavioral bound checking, and re-grounding prompts. Common drift patterns: proxy optimization, scope creep, local minima, mode collapse. |
| 6 | How would you design a monitoring system for a production LLM application? | Common across companies [^chip-huyen-platform] | Three pillars: metrics (system + model + latency + cost), logs ("log everything"), traces (complete execution path). Key metrics: TTFT, TBT, TPS, hallucination rate, retrieval hit rate, filtered output percentage. Breakdowns by user, release, prompt version. Manual daily inspection of production data. |
| 7 | Design an ML monitoring system for TikTok | TikTok [^exponent] | Real-time performance monitoring across recommendation models, content moderation models, and creator analytics. Alerting on metric degradation, drift detection, and automatic rollback triggers. |
| 8 | How do you measure quality of open-ended LLM outputs at scale? | Common interview question | LLM-as-judge pipelines (with awareness of pitfalls like position bias), human evaluation protocols, golden dataset regression testing, task-specific automated metrics, user satisfaction signals (thumbs up/down, session length, task completion), and A/B testing for prompt/model changes. [^igotanoffer] |

### Domain-Specific Systems (Healthcare, Finance, Legal, Automotive)

| # | Question | Source / Company | What Makes a Strong Answer |
|---|----------|-----------------|---------------------------|
| 1 | Design a system that lets doctors automatically send billing info to insurers based on patient notes | Reddit [^igotanoffer] | Clinical NLP for extracting diagnoses and procedures from notes, ICD/CPT code mapping, validation against billing rules, human review for high-value claims, HIPAA compliance (on-premises models, data encryption, audit trails), and error handling for ambiguous notes. |
| 2 | Design a voice assistant for hospital staff | [^bhavishya-pandit] | On-device ASR with medical terminology fine-tuning, intent routing, HIPAA-compliant data handling, confirmation mechanisms for safety-critical actions, typed fallback mode, and integration with EHR systems. Cannot use public APIs -- must self-host for patient data. |
| 3 | Design an AI-powered legal assistant | [^systemdesignhandbook] | RAG over legal databases (case law, statutes, regulations), clause template library, citation verification, jurisdiction-aware responses, version control for generated documents, lawyer review workflow, and malpractice risk mitigation. LLMs paraphrase/combine existing clauses but never invent legal content. |
| 4 | Design a hallucination-free chatbot for a financial institution | [^bhavishya-pandit] | Route factual queries to structured APIs (account balances, transaction history). LLM only rephrases retrieved data with disclaimers. Confidence thresholds reject unsupported queries. Complete audit trail. Regulatory compliance (SOX, PCI-DSS). No investment advice without proper disclaimers. |
| 5 | Design Tesla's Autopilot vision system | Tesla [^interviewnode-hld] | Real-time multi-camera perception, object detection and tracking, sensor fusion, safety-critical latency requirements, edge deployment optimization, and the challenge of long-tail scenarios (rare but dangerous situations). |
| 6 | Design a medical chatbot with hallucination prevention | [^interviewnode] | Domain-specific RAG over clinical guidelines, confidence scoring with human escalation for low-confidence responses, source transparency with citations, never providing diagnoses (only information), and regulatory compliance (FDA Software as Medical Device considerations). |
| 7 | Design a generative resume builder with memory | [^systemdesignhandbook] | User profile memory across sessions, template-based generation with personalization, ATS optimization, style transfer across industries, version history, and export formats. |
| 8 | Design Airbnb's dynamic pricing system | Airbnb [^interviewquery-ml] | Demand forecasting (seasonality, events, competitor pricing), supply-side constraints, price elasticity modeling, A/B testing pricing strategies, and balancing host revenue with booking probability. |
| 9 | Design a GitHub Copilot-style code completion tool | [^systemdesignhandbook] | Sub-500ms latency requirement, local model for speed with cloud model fallback for complex completions, context window management (current file + imports + recent edits), streaming suggestions, user acceptance rate as primary metric, and privacy (code never leaves IDE for enterprise). |
| 10 | Design an ethical AI safeguards system | [^interviewnode-hld] | Bias detection and measurement across demographics, fairness constraints in model training, transparency and explainability requirements, regulatory compliance framework, and governance processes for model approval and monitoring. |

### General System Design (Still Asked at AI/LLM Companies)

These traditional distributed systems questions appear at AI companies like OpenAI (especially at L5/Staff level), testing foundational systems thinking.

| # | Question | Source / Company | What Makes a Strong Answer |
|---|----------|-----------------|---------------------------|
| 1 | Design GitHub Actions | OpenAI L5 [^hellointerview] | Event-driven architecture, workflow orchestration, container isolation, scaling runners, artifact management, and security (secret management, permission scoping). |
| 2 | Design Slack | OpenAI L5 [^hellointerview] | Real-time messaging (WebSocket), channel architecture, search across messages, file sharing, presence indicators, and multi-workspace support at scale. |
| 3 | Design Online Chess | OpenAI L5 [^hellointerview] | Real-time game state synchronization, matchmaking, Elo rating system, anti-cheating mechanisms, spectator mode, and handling disconnections gracefully. |
| 4 | Design a Payment System | OpenAI L5 [^hellointerview] | Transaction processing with ACID guarantees, idempotency, fraud detection integration, multi-currency support, retry logic with exponential backoff, and reconciliation. |
| 5 | Design a Webhook Callback System | OpenAI L5 [^hellointerview] | Reliable delivery with retry and dead-letter queues, authentication/verification, rate limiting, ordering guarantees, and monitoring delivery success rates. |
| 6 | Design the OpenAI Playground | OpenAI [^linkjob-openai] | Frontend/UX emphasis: parameter controls (temperature, top-p), streaming response display, session management, API key handling, model comparison interface, and developer workflow optimization. |
| 7 | Design an in-memory database with nested transaction support (SET, GET, BEGIN, ROLLBACK, COMMIT) | xAI [^devto-xai] | Transaction isolation with nested scopes, persistence via WAL logs, concurrency control, and scalability extensions. Tests first-principles thinking over memorized templates. |

## Sources

[^igotanoffer]: [IGotAnOffer - Generative AI System Design Interview](https://igotanoffer.com/en/advice/generative-ai-system-design-interview)
[^chip-huyen-books]: [Chip Huyen - AI Engineering](https://huyenchip.com/books/)
[^chip-huyen-platform]: [Chip Huyen - Building a Generative AI Platform](https://huyenchip.com/2024/07/25/genai-platform.html)
[^yuan-meng]: [Yuan Meng - MLE Interviews 2.0](https://www.yuan-meng.com/posts/mle_interviews_2.0/)
[^brian-kihoon-lee]: [Brian Kihoon Lee - ML Eng Interviewing](https://www.moderndescartes.com/essays/ml_eng_interviewing/)
[^promptlayer]: [PromptLayer - The Agentic System Design Interview](https://blog.promptlayer.com/the-agentic-system-design-interview-how-to-evaluate-ai-engineers/)
[^mai-chi-bao]: [Mai Chi Bao - How I Aced My LLM Interview](https://dev.to/mrzaizai2k/how-i-aced-my-llm-interview-building-a-rag-chatbot-2p6f)
[^bhavishya-pandit]: [Bhavishya Pandit - 7 Deep-Cut AI System Design Interview Questions](https://bhavishyapandit9.substack.com/p/7-deep-cut-ai-system-design-interview)
[^linkjob-anthropic]: [LinkJob - Anthropic Software Engineer Interview](https://www.linkjob.ai/interview-questions/anthropic-software-engineer-interview/)
[^techeon]: [TechEon - The Complete Agentic AI System Design Interview Guide 2026](https://atul4u.medium.com/the-complete-agentic-ai-system-design-interview-guide-2026-f95d0cfeb7cf)
[^designgurus]: [DesignGurus - OpenAI System Design Interview Questions](https://www.designgurus.io/blog/openai-system-design-interview-questions)
[^designgurus-rag]: [DesignGurus - System Design for RAG](https://www.designgurus.io/blog/system-design-for-rag)
[^hellointerview]: [HelloInterview - OpenAI L5 Interview Guide](https://www.hellointerview.com/guides/openai/l5)
[^interviewnode]: [InterviewNode - GenAI System Design Interview Patterns](https://www.interviewnode.com/post/generative-ai-system-design-interview-patterns-you-should-know)
[^interviewnode-hld]: [InterviewNode - Top 25 HLD Questions in ML Interviews](https://www.interviewnode.com/post/top-25-high-level-design-hld-questions-in-ml-interviews-at-faang-companies)
[^anthropic-contextual-retrieval]: [Anthropic - Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval)
[^anthropic-multi-agent]: [Anthropic - Multi-Agent Research System](https://www.anthropic.com/engineering/multi-agent-research-system)
[^hitendra-patel]: [Hitendra Patel - The Day I Transformed My RAG](https://medium.com/@hitendra.patel2986/the-day-i-transformed-my-rag-from-search-engine-to-answer-engine-7629f0fddf07)
[^proptech-founder]: [PropTech Founder - YouTube](https://www.youtube.com/watch?v=leXRiJ5TuQo)
[^eugene-yan]: [Eugene Yan - LLM Patterns](https://eugeneyan.com/writing/llm-patterns/)
[^hamel-husain]: [Hamel Husain - Your AI Product Needs Evals](https://hamel.dev/blog/posts/evals/)
[^shreya-shankar]: [Shreya Shankar - In Defense of AI Evals](https://www.sh-reya.com/blog/in-defense-ai-evals/)
[^lockedinai]: [LockedIn AI - LLM AI Engineer Interview Questions](https://www.lockedinai.com/blog/llm-ai-engineer-interview-questions-silicon-valley)
[^jason-liu]: [Jason Liu](https://jxnl.co/)
[^linkjob-openai]: [LinkJob - OpenAI Loop Interview](https://www.linkjob.ai/interview-questions/openai-loop-interview)
[^exponent-openai]: [Exponent - What It's Actually Like to Interview at OpenAI](https://medium.com/exponent/what-its-actually-like-to-interview-at-openai-in-2026-03a646c9436c)
[^openai-guide]: [OpenAI Interview Guide](https://openai.com/interview-guide/)
[^wellfound-sprinter]: [Wellfound - Sprinter Health Lead Software Engineer](https://wellfound.com/jobs/3265793-lead-software-engineer-applied-ai)
[^mimansa-jaiswal]: [Mimansa Jaiswal - LLM/ML Job Interviews](https://mimansajaiswal.github.io/posts/llm-ml-job-interviews-fall-2024-process/)
[^pragmatic-engineer]: [Pragmatic Engineer - From Software Engineer to AI Engineer](https://newsletter.pragmaticengineer.com/p/from-software-engineer-to-ai-engineer)
[^doctolib]: [Doctolib - Building an Agentic AI System for Healthcare Support](https://medium.com/doctolib/building-an-agentic-ai-system-for-healthcare-support-a-journey-into-practical-ai-implementation-0afd28d716e6)
[^uber]: [Uber - GenAI Gateway](https://www.uber.com/blog/genai-gateway/)
[^airbnb]: [Airbnb Engineering - Automation Platform v2](https://medium.com/airbnb-engineering/automation-platform-v2-improving-conversational-ai-at-airbnb-d86c9386e0cb)
[^bytebytego-perplexity]: [ByteByteGo - How Perplexity Built an AI Google](https://blog.bytebytego.com/p/how-perplexity-built-an-ai-google)
[^slack]: [Slack Engineering - How We Built Slack AI](https://slack.engineering/how-we-built-slack-ai-to-be-secure-and-private/)
[^linkedin]: [InfoQ - QCon AI LinkedIn](https://www.infoq.com/news/2025/12/qcon-ai-linkedin/)
[^doordash]: [DoorDash - Simulation Evaluation Flywheel](https://careersatdoordash.com/blog/doordash-simulation-evaluation-flywheel-to-develop-llm-chatbots-at-scale/)
[^interviewquery]: [InterviewQuery - AI Interview Trends](https://www.interviewquery.com/p/ai-interview-trends-tech-hiring-2025)
[^interviewquery-ml]: [InterviewQuery - Machine Learning Interview Questions](https://www.interviewquery.com/p/machine-learning-interview-questions)
[^exponent]: [Exponent - Machine Learning System Design Interview Guide](https://www.tryexponent.com/blog/machine-learning-system-design-interview-guide)
[^exponent-youtube]: [Exponent YouTube](https://www.youtube.com/watch?v=Nc1y9tYV2WM)
[^systemdesignhandbook]: [SystemDesignHandbook - Generative AI System Design Interview](https://www.systemdesignhandbook.com/guides/generative-ai-system-design-interview/)
[^systemdesignhandbook-anthropic]: [SystemDesignHandbook - Anthropic System Design Interview](https://www.systemdesignhandbook.com/guides/anthropic-system-design-interview/)
[^systemdesignhandbook-agentic]: [SystemDesignHandbook - Agentic System Design](https://www.systemdesignhandbook.com/guides/agentic-system-design/)
[^getsdeready]: [GetSDEReady - AI System Design Interview Questions 2025](https://getsdeready.com/ai-system-design-interview-questions-2025/)
[^yuan-meng-infra]: [Yuan Meng - ML Infra Interviews](https://www.yuan-meng.com/posts/ml_infra_interviews/)
[^devto-xai]: [DevTo - xAI Software Engineer Interview 2026](https://dev.to/net_programhelp_e160eef28/xai-software-engineer-interview-2026-full-recap-pitfalls-real-prep-tips-2fl0)
