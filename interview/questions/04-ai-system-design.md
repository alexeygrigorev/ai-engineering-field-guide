# AI System Design Interview

AI system design is emerging as a distinct interview category, separate from both traditional software system design and classic ML system design. The shift is driven by the explosion of LLM-powered products: instead of designing training pipelines, candidates design orchestration architectures around pre-trained models.

Companies with dedicated AI system design rounds include Doctolib ("AI System Design Interview"), Sprinter Health ("AI-Focused Systems Design"), and Anthropic (distributed search + LLM inference at scale). Many more are adding AI-flavored questions to existing system design rounds. Companies known to test GenAI system design include Google, Apple, OpenAI, Anthropic, Cohere, Salesforce, and AI-first startups. [^igotanoffer]

System design with AI elements is becoming a critical interview component. Interviewers need to understand how a candidate thinks about building services and components with AI interfaces and tooling - including understanding limitations on security, access rights, and the reality that AI systems need to scale significantly (potentially 5-10x compared to current load, to 1000+ nodes).

See also: [Awesome AI Engineering](../../awesome.md) for the full collection of references, company blogs, and practitioner stories cited below.

https://github.com/alexeygrigorev/ai-engineering-field-guide/blob/main/awesome.md

## Format

Typically 45-60 minutes. You drive the conversation through: [^designgurus]

- Clarify requirements, constraints, and success criteria
- Sketch a high-level architecture
- Deep-dive into specific components
- Discuss trade-offs, failure modes, and bottlenecks

Time allocation: [^designgurus]

- ~5 min clarifying the problem
- 10-15 min high-level design
- 15-20 min deep dive into components
- 5-10 min trade-offs and bottlenecks
- Remaining time for follow-up scenarios

Common delivery formats:

- Whiteboard or virtual drawing (Excalidraw, Miro) where you sketch components and data flows
- Discussion-based where you walk through the architecture verbally and the interviewer probes specific areas



## Questions

System design and cost/latency optimization are among the most frequently asked topics in AI engineering interviews:

- Scale an AI chat feature to 1M daily users - discuss trade-offs
- Your app gets 1M queries/day - how do you optimize cost?


### Typical AI System Design Questions

Based on real interview experiences and practitioner guides:

- Design an AI chatbot (ChatGPT, Claude chat service). [^igotanoffer] [^designgurus] [^process-analysis] [^reddit-swe-to-ai]
- Design a Document Q&A Assistant / RAG system. [^bhavishya-pandit] [^reddit-eightfold-ai]
- Design an AI co-pilot like GitHub Copilot [^colin-zhou]
- Design a Hospital Voice Assistant (handle noise, privacy, latency, domain vocabulary). [^bhavishya-pandit]
- Design a Legal Contract Generation system with compliance requirements. [^bhavishya-pandit]
- Design an AI-powered Candidate Sourcing System. [^colin-zhou] [^bhavishya-pandit]
- Design a system to process 10K user uploads/month (bank payslips, IDs, references). [^igotanoffer]
- Design a system that lets doctors automatically send billing info to insurers based on patient notes. [^igotanoffer]
- Design a fraud detection system. [^reddit-swe-to-ai]
- Design ChatGPT's cross-conversation memory feature. [^igotanoffer]
- Design a multi-step agentic workflow (meeting scheduling, code review, email campaigns). [^promptlayer]
- Design a content/policy violation detection system. [^igotanoffer]
- Design a unified query engine across dispersed data sources like email, calendar, documents, and chat. [^x-avi-chawla-1]
- Design a Perplexity.ai / real-time LLM-powered search engine. [^colin-zhou]


### Near-AI / AI Serving Systems / Platforms (more Engineering)

- How would you handle real-time versus batch processing for data updates? When is one preferred over the other? [^proptech-founder-2]
- How do you ingest and process different types of data (structured, unstructured, event data)? [^proptech-founder-1]
- Design a scalable image-generation pipeline for millions of users. [^interviewnode]
- Design a distributed job queue for 100k+ GPU training jobs with preemption and checkpointing. [^reddit-xai-eng]
- Design a large-scale AI model deployment system - model serving, GPU scaling, model versioning, result caching. (OpenAI) [^designgurus]


## Expectations

AI system design is primarily a senior-level round. Mid-level candidates may get system design questions but interviewers don't expect depth - a reasonable high-level architecture is sufficient.

At senior and staff levels, interviewers expect: [^interviewnode] [^igotanoffer]

- Reasoning across uncertainty - keeping the system predictable despite unpredictable outputs
- Trade-off fluency - retrieval speed vs context length, fine-tuning vs prompting, GPU cost vs latency
- Communication clarity - narrating how information flows through the system


## AI System Design vs System Design

The fundamental shift: when models like GPT-4 and Claude became accessible via APIs, the hard part stopped being model training and started being system orchestration. [^chip-huyen-books]

- Traditional ML focuses on training pipelines
- AI/LLM system design focuses on orchestrating pre-trained models

Key differences: [^yuan-meng] [^brian-kihoon-lee] [^chip-huyen-platform] [^promptlayer]

- Data focus - training data and feature engineering vs context engineering, chunking, retrieval quality
- Output type - structured (scores, classifications) vs open-ended text, code, images
- Determinism - generally deterministic vs non-deterministic by default
- Evaluation - precision/recall/F1/AUC on held-out sets vs LLM-as-judge, human evaluation, task-specific evals
- Cost model - training compute (periodic) + serving vs per-token inference cost (continuous) + retrieval
- Failure modes - data drift, training-serving skew vs hallucination, prompt injection, context overflow, cost blowup
- Iteration speed - slow (retrain model) vs fast (change prompt, adjust retrieval)

### ML system design

ML system design interviews focus on full training pipelines (feature stores, model lifecycle, offline evaluation):

- Design a recommendation system
- Design a fraud detection system
- Design a spam classifier
- Design a search ranking system
- Design an ad click prediction system

"GenAI interviews still care about standard distributed-systems basics, but they'll push harder on evaluation, guardrails, and context/tooling design." [^igotanoffer]

### Traditional system design

General system design questions commonly asked at OpenAI L5 and other AI companies (for *software engineers*): [^hellointerview] [^colin-zhou]

- Design a distributed key-value store (like DynamoDB / Cassandra). [^colin-zhou]
- Design a rate limiter (global, per-user, distributed). [^colin-zhou]
- Design GitHub Actions. [^hellointerview]
- Design Online Chess. [^hellointerview]
- Design Instagram / TikTok / X (timeline, posting, followers). [^colin-zhou]
- Design YouTube / Netflix video streaming platform. [^colin-zhou]
- Design Uber (ride-sharing backend: matching, ETA, pricing surges). [^colin-zhou]
- Design WhatsApp / Messenger (1:1 + group chat at global scale). [^colin-zhou]
- Design Google Docs collaborative editing (real-time, eventually consistent). [^colin-zhou]


## How to Prepare

### Structure your answer

Follow a five-step progression [^igotanoffer]:

1. Problem framing (5-10 min) - clarify users, constraints, quality expectations, guardrails
2. High-level architecture (10-15 min) - core components and data paths from prompt to response
3. Deep dive (20-30 min) - RAG design, tool use, memory, evaluation, safety
4. Trade-offs (10-15 min) - what breaks, how you detect it, graceful degradation
5. Conclusion - summarize, list risks, outline next iteration

Most questions map to four repeatable patterns [^interviewnode]:

- RAG - system orchestration and grounding accuracy (the most common pattern)
- Feedback and reinforcement - implicit/explicit signals, active learning loops
- Hallucination mitigation - retrieval-grounded pipelines, confidence estimation, source transparency
- Scalability and cost optimization - multi-layer caching, model tiering, prompt compression


### What companies build

Real production AI systems from engineering blogs - these inform the kinds of systems you'd be asked to design:

- Doctolib - agentic AI for customer support: specialized agents in a directed graph, ~17K daily messages [^doctolib]
- Uber - GenAI Gateway: unified LLM platform, PII redactor, 60+ use cases [^uber]
- Airbnb - LLM-powered conversational AI with Chain of Thought reasoning and guardrails [^airbnb]
- Perplexity - 200M daily queries, RAG on Vespa.ai, fine-tuned Sonar models [^bytebytego-perplexity]
- Slack - stateless RAG, LLMs in escrow VPC for data privacy [^slack]
- LinkedIn - AI agent platform, strict data layer siloing [^linkedin]
- Anthropic - multi-agent research: Opus orchestrator + Sonnet subagents, ~15x more tokens than chat [^anthropic-multi-agent]
- DoorDash - AI-driven evaluation flywheel for LLM chatbots, hierarchical RAG [^doordash]

### Common mistakes

- Jumping to a solution without clarifying requirements, constraints, and success criteria [^igotanoffer]
- Treating the LLM as a source of truth instead of grounding with retrieval, tools, or citations [^interviewnode]
- Designing only the happy path without failure modes, monitoring, or evaluation [^igotanoffer]
- Over-indexing on tool names - "I'd use LangChain" instead of explaining why you'd chain retrieval and generation [^interviewnode]
- Ignoring cost and latency - token budgets, model tiering, caching strategies [^igotanoffer]
- Ignoring safety - prompt injection, data leakage, unsafe tool execution [^igotanoffer]
- Putting control flow in prompts instead of the orchestrator (agentic designs) [^techeon]
- Choosing agents because they're exciting, not because the problem requires autonomy [^techeon]

## Sources

[^igotanoffer]: [IGotAnOffer - Generative AI System Design Interview](https://igotanoffer.com/en/advice/generative-ai-system-design-interview)
[^chip-huyen-books]: [Chip Huyen - AI Engineering](https://huyenchip.com/books/)
[^chip-huyen-platform]: [Chip Huyen - Building a Generative AI Platform](https://huyenchip.com/2024/07/25/genai-platform.html)
[^yuan-meng]: [Yuan Meng - MLE Interviews 2.0](https://www.yuan-meng.com/posts/mle_interviews_2.0/)
[^brian-kihoon-lee]: [Brian Kihoon Lee - ML Eng Interviewing](https://www.moderndescartes.com/essays/ml_eng_interviewing/)
[^promptlayer]: [PromptLayer - The Agentic System Design Interview](https://blog.promptlayer.com/the-agentic-system-design-interview-how-to-evaluate-ai-engineers/)
[^bhavishya-pandit]: [Bhavishya Pandit - 7 Deep-Cut AI System Design Interview Questions](https://bhavishyapandit9.substack.com/p/7-deep-cut-ai-system-design-interview)
[^techeon]: [TechEon - The Complete Agentic AI System Design Interview Guide 2026](https://atul4u.medium.com/the-complete-agentic-ai-system-design-interview-guide-2026-f95d0cfeb7cf)
[^designgurus]: [DesignGurus - OpenAI System Design Interview Questions](https://www.designgurus.io/blog/openai-system-design-interview-questions)
[^hellointerview]: [HelloInterview - OpenAI L5 Interview Guide](https://www.hellointerview.com/guides/openai/l5)
[^interviewnode]: [InterviewNode - GenAI System Design Interview Patterns](https://www.interviewnode.com/post/generative-ai-system-design-interview-patterns-you-should-know)
[^anthropic-multi-agent]: [Anthropic - Multi-Agent Research System](https://www.anthropic.com/engineering/multi-agent-research-system)
[^proptech-founder-1]: [YouTube - Proptech Founder Part 1](https://www.youtube.com/watch?v=leXRiJ5TuQo)
[^doctolib]: [Doctolib - Building an Agentic AI System for Healthcare Support](https://medium.com/doctolib/building-an-agentic-ai-system-for-healthcare-support-a-journey-into-practical-ai-implementation-0afd28d716e6)
[^uber]: [Uber - GenAI Gateway](https://www.uber.com/blog/genai-gateway/)
[^airbnb]: [Airbnb Engineering - Automation Platform v2](https://medium.com/airbnb-engineering/automation-platform-v2-improving-conversational-ai-at-airbnb-d86c9386e0cb)
[^bytebytego-perplexity]: [ByteByteGo - How Perplexity Built an AI Google](https://blog.bytebytego.com/p/how-perplexity-built-an-ai-google)
[^slack]: [Slack Engineering - How We Built Slack AI](https://slack.engineering/how-we-built-slack-ai-to-be-secure-and-private/)
[^linkedin]: [InfoQ - QCon AI LinkedIn](https://www.infoq.com/news/2025/12/qcon-ai-linkedin/)
[^doordash]: [DoorDash - Simulation Evaluation Flywheel](https://careersatdoordash.com/blog/doordash-simulation-evaluation-flywheel-to-develop-llm-chatbots-at-scale/)
[^colin-zhou]: [Medium - Colin Zhou](https://levelup.gitconnected.com/how-i-fought-and-passed-technical-interviews-with-llms-in-2025-f328e9df8e84)
[^process-analysis]: [Process Analysis - Reddit r/cscareerquestions](https://www.reddit.com/r/cscareerquestions/)
[^proptech-founder-2]: [YouTube - Proptech Founder Part 2](https://www.youtube.com/watch?v=Zt-h5BiBWH0)
[^reddit-eightfold-ai]: [Reddit - Need Advice for Eightfold.ai Agentic AI Engineer](https://www.reddit.com/r/developersIndia/comments/1pbaj11/need_advice_for_eightfoldai_agentic_ai_engineer) (r/developersIndia)
[^reddit-swe-to-ai]: [Reddit - From Software Developer to AI Engineer](https://www.reddit.com/r/learnmachinelearning/comments/1pzcw2y/from_software_developer_to_ai_engineer_the_exact/) (r/learnmachinelearning)
[^reddit-xai-eng]: [Reddit - xAI AI Engineer Backend/Infra Interview](https://www.reddit.com/r/leetcode/comments/1pjhw1i/xai_ai_engineer_backendinfra_interview_just/) (r/leetcode)
[^x-avi-chawla-1]: [X - Avi Chawla, Unified Query Engine (Google)](https://x.com/_avichawla/status/1986320178783867036)
