# Home Assignments

Take-home assignments, paid work trials, and asynchronous assessments for AI/ML engineering roles. Based on 1,765 job descriptions, 100+ GitHub repos of actual candidate submissions, and practitioner reports.

Of the 51 companies with disclosed interview processes, 17 (33%) include a take-home or asynchronous assignment. An additional 5 companies use paid work trials instead. Analysis of 100+ GitHub repos (Q4 2025 / Q1 2026) shows what companies actually ask:

- RAG systems (40%+) - document upload, vector databases, citation support
- Agentic systems (30%+) - tool-calling, multi-step reasoning, multi-agent orchestration
- Conversational AI (20%+) - chatbots, live chat agents, voice assistants
- Document processing (15%) - PDF parsing, data extraction, marksheet extraction
- LLM-as-judge evaluation (10%+) - build a system then evaluate it with another LLM


## Format

Asynchronous assignments completed on your own time, typically with a deadline of 2-7 days. You submit code, a writeup, or a working prototype, then discuss your solution in a follow-up interview. [^fonzi-ai]

Typical assignment formats:

- Take-home coding project (most common) - build something from scratch, typically 2-4 hours of actual work. "Not code golf" - companies emphasize decision-making and clarity over cleverness
- Defence round - present and defend your solution in a 45-90 minute walkthrough interview

Only 1 company explicitly allows AI tools in take-homes ("AI tools are explicitly allowed and encouraged"). No company explicitly bans AI for take-home assignments (bans only apply to live interviews). Most don't mention AI tool policy at all.


## Assignment Examples

Actual take-home assignments from candidate reports, job listings, and 100+ GitHub repos of real submissions.


### RAG and Document Q&A

The most common assignment type (40%+ of GitHub submissions).

- Build a RAG chatbot that ingests PDFs/documents, creates embeddings in a vector DB, and answers questions with citations. Must respond "I don't have that information" when answer is unavailable. Answers must come strictly from retrieved context (10+ candidate submissions across 5+ companies). [^gh-rokomari] [^gh-streamkar] [^gh-dge-1] [^gh-dge-2] [^gh-bmw] [^gh-ncapek]
- Build a policy document RAG assistant with mandatory source citations for every answer. Return safe fallbacks for out-of-scope questions. Comes with a 7-question evaluation set across 3 categories (answerable, partially answerable, unanswerable). [^gh-neura-dynamics]
- Build a document Q&A system with citation tracking that handles multi-hop questions (questions requiring information from multiple documents or sections to answer). [^promptlayer]
- Build a live chat agent grounded in FAQ knowledge base. Model must answer only from known FAQ data. [^gh-spur-1] [^gh-spur-2]
- Design a customer support chatbot using RAG with open-source models. Requirements: 100+ concurrent users, <2 second latency, grounded in company docs, analytics tracking. [^mai-chi-bao]
- Build a CLI tool for summarizing long PDFs with configurable models and chunking strategies. [^fonzi-ai]
- Refactor an existing messy RAG application into a clean architecture. Preserve all external behaviors (exact API endpoints), eliminate global mutable state, ensure testability without requiring running services (5+ candidate submissions for one company). [^gh-bithealth-1] [^gh-bithealth-2] [^gh-bithealth-3] [^gh-bithealth-4] [^gh-bithealth-5]
- Build an agentic RAG system for government documents. 100% open-source required (Ollama + CrewAI + pgvector). Must integrate with OpenWebUI. Evaluated using RAGAS metrics (faithfulness, answer relevancy, context precision, context recall). [^gh-govgpt]


### Agents and Tool-Calling

Second most common (30%+).

- Build an assistant agent handling database queries, document search, and bash commands. Bash commands require explicit user approval. [^gh-curling-ai]
- Build an AI agent that transforms Monday.com project management data into conversational business insights using dual-LLM architecture. [^gh-skylark]
- Build an AI agent demonstrating natural interaction, agentic behavior, and clear reasoning steps. [^tushar-eightfold]
- Build a customer support agent. [^reddit-yc-assignments]
- Build an autonomous agent using an open-source LLM with observability/eval layer. [^reddit-yc-assignments]
- Build an agent that reads customer CSV data and generates personalized email campaigns with evaluation metrics. [^promptlayer]
- Build a code review agent that analyzes Python files and provides actionable feedback. [^promptlayer]
- Build a Singapore public transport query agent that fetches live data from 7 LTA APIs about buses, trains, traffic, and station conditions. [^gh-hrytos]
- Build a sales insights agent that answers questions about subscription/revenue data. Must detect and refuse PII requests (emails, phone numbers, credit card tokens). No raw rows passed to the LLM - aggregates only. Evaluated on 3 dimensions: accuracy, safety/refusal correctness, reasoning quality. [^gh-cohere]
- Build an evaluation tool for LLM hallucination detection. [^fonzi-ai]


### Multi-Agent Systems

- Build a multi-agent content generation system: 5 core agents (research, writing, editing, SEO, publishing). Takes product JSON input, generates FAQ document, product page, and comparison page. All outputs must follow strict JSON formats. LangChain + Groq. [^gh-kasparro]
- Implement a minimal workflow engine with graph-based nodes, state management, branching/looping, and tool-based logic. Max 50 steps. Built-in infinite-cycle protection required. Unit tests mandatory (6+ candidate submissions). [^gh-tredence-1] [^gh-tredence-2] [^gh-tredence-3] [^gh-tredence-4] [^gh-tredence-5] [^gh-tredence-6]
- Build a 5-agent CBT therapy system: agents autonomously design, critique, and refine therapy exercises. Human-in-the-loop approval required before finalization.  [^gh-cerina]
- Build a 4-stage bedtime story pipeline: Spec Builder, Storyteller, LLM Judge, Rewriter. Must use gpt-3.5-turbo. Up to 2 revision cycles. LLM judge evaluates stories against the spec. [^gh-hippocratic-1] [^gh-hippocratic-2] [^gh-hippocratic-3] [^gh-hippocratic-4]


### Document Extraction and Processing

- Build a marksheet extraction API: parse complex table layouts and handwriting from academic marksheets into structured JSON. [^gh-trestle]
- Build a physician notetaker: transform physician-patient conversations into structured clinical documentation.. [^gh-emitrr-1] [^gh-emitrr-2]
- Build a legal document analysis tool for contracts: extract key information, identify risks (auto-renewal traps, liability, IP ownership, non-competes), generate structured summaries. [^gh-legal-doc]
- Build a CBT assistant combining RAG with safety mechanisms. Crisis detection mandatory. PII redaction and pseudonymization required. No secrets in logs. Educational only, not clinical advice. [^gh-mindwell]
- Take a blood test report as PDF, understand medical issues, generate suggestions by fetching content from online blog articles with source links. [^khushal-kumar]
- Build a question deduplication and clustering pipeline: exact dedup, semantic dedup, LLM-based cluster discovery, classification. Output evaluated with ARI, NMI, homogeneity, completeness metrics. [^gh-krisp]
- Build a data pipeline that processes 1,000 messy products from 4 vendors, normalizes them into a unified schema, fetches supplementary data via rate-limited async API calls (vendor-specific token-bucket rate limits), enriches products through AI-powered duplicate detection. Must support both CLI and API access. [^gh-rokomari]
- Build a transaction-to-user matching system: identify users whose names appear in transaction descriptions, find similar transactions via text matching, propose improvements (semantic embeddings, database integration). Spring Boot + Java. [^gh-deel]
- Build real-time earnings call transcription and insight streaming: streaming audio-to-text via Whisper, real-time extraction of financial signals (revenue, guidance, risks, outlook), SSE output. [^gh-voice-ai]


### Full-Stack AI Applications

- Build a Telegram bot for investment coaching with safety filtering. Educational content only - no personalized financial advice. [^gh-pineos]
- Build a multi-agent D&D dungeon simulation: Game Master agent + Player agents. Must address at least 3 of 6 challenges (long campaigns, secrets, rulings, self-aware dungeon, living world, ambiguity). LangGraph required. [^gh-context-engineering]
- Build a memory extraction and personality transformation system: extract structured long-term memory from chat history as JSON, transform responses based on personas (calm mentor, witty friend, therapist). Open-source LLMs only, no proprietary APIs. [^gh-gupshup]
- Build an AI judge for a Rock-Paper-Scissors variant: classify player inputs as VALID/INVALID/UNCLEAR, handle typos and edge cases, tool-based state management workflow (2 submissions). [^gh-upliance-1] [^gh-upliance-2]
- Build a web app that converts markdown to slide deck presentations by splitting content into logical sections based on a target slide count. Document size limited to 150K tokens, single API call. Next.js + OpenAI. [^gh-gamma]
- Build an LLM processing pipeline with intelligent routing, multi-level caching (exact + semantic), provider health monitoring with failover, and distributed tracing. Targets: 100+ req/s, p95 latency under 2s, >40% cache hit rate. [^gh-zuneko]
- Build an NPC system for a job simulation platform: three AI co-workers with distinct personalities, a "Director Agent" that detects conversation loops via semantic similarity (0.85 threshold), RAG-based knowledge retrieval. FastAPI + Claude API + FAISS. [^gh-edtronaut]
- Build an LLM-based rating prediction and prompt evaluation system with user and admin dashboards. Node.js + MongoDB + Google Generative AI. [^gh-fynd]
- Build an AI-first CRM module: React/Redux frontend, FastAPI backend, LangGraph with 5+ tools. Deliverable: GitHub repo + 10-15 minute demo video. [^fonzi-ai]


### Evaluation Criteria Found in Assignments

Many assignments include explicit evaluation criteria. Patterns across repos:

- Functional correctness - does the system work end-to-end, handle edge cases, produce correct outputs
- Code quality and architecture - modular design, clean code, extensibility, proper error handling
- Evaluation methodology - whether candidates build eval harnesses, define metrics, measure quality systematically
- Production readiness - scalability considerations, caching, monitoring, cost optimization, security (PII handling, input sanitization, rate limiting)
- Performance targets - response time (e.g., <2s p95 latency, ~0.5s per response), throughput (100+ req/s), cache hit rates (>40%), cost reduction (>30%)
- Testing - unit tests (sometimes mandatory), test coverage targets (e.g., 80%), edge case handling
- Documentation - README quality, design decision explanations, trade-off analysis
- Weighted rubrics - some assignments provide explicit scoring: e.g., 30% functionality, 30% challenge completion, 25% context engineering, 15% code quality [^gh-context-engineering]
- Quantitative metrics - ARI/NMI for clustering [^gh-krisp], RAGAS metrics for RAG (faithfulness, answer relevancy, context precision) [^gh-govgpt], confidence scores for extraction [^gh-trestle]


## How to Prepare

From observing 50+ AI engineer interviews: "most engineers put way too little effort into take-homes." The best submissions share these traits: [^fonzi-ai] [^interviewnode] [^reddit-yc-assignments]

- Start with evaluation - build an eval harness before writing the main logic. YC startups report this as the top signal: "Red flag if candidate doesn't start with evals" [^reddit-yc-assignments]
- Document design decisions and trade-offs - why you chose this approach over alternatives
- Include a Loom/video walkthrough of your submission [^fonzi-ai]
- Make it configurable - one engineer built a PDF summarizer CLI with a config file for different models and chunking strategies, got two competing offers within 72 hours [^fonzi-ai]
- Test edge cases - even if testing isn't explicitly required, include basic tests [^devto-aidi]
- Show production awareness - error handling, monitoring hooks, cost estimates
- Connect technical metrics to business outcomes [^interviewnode]
- Prepare for the defence round - practice explaining your architecture decisions, trade-offs, and what you'd do differently with more time

Ask clarifying questions before starting. Double your time estimate. [^devto-aidi]

Common mistakes:

- Putting too little effort in - "most engineers put way too little effort into take-homes" [^fonzi-ai]
- Rushing without documenting design decisions and trade-offs
- Over-engineering beyond what was asked without justification
- Ignoring evaluation and testing of AI outputs - this is the single biggest differentiator [^reddit-yc-assignments]
- Treating the LLM as a black box without discussing failure modes
- Not asking clarifying questions before starting
- Not preparing for the walkthrough/defence round - the follow-up interview is often more important than the code itself


## Sources

[^devto-aidi]: [dev.to - Learn From My Mistakes: My First Take-Home Code Challenge](https://dev.to/aidiri/learn-from-my-mistakes-my-first-take-home-code-challenge-778)
[^exponent-openai]: [Medium - Exponent, OpenAI](https://medium.com/exponent/what-its-actually-like-to-interview-at-openai-in-2026-03a646c9436c)
[^fonzi-ai]: [Medium - Fonzi AI](https://medium.com/fonzi-ai/what-ive-learned-from-sitting-in-on-50-ai-engineer-interviews-c493696453c4)
[^goncharov-anthropic]: [Blog - Goncharov, Anthropic Interview](https://blog.goncharov.page/i-failed-my-anthropic-interview-and-came-to-tell-you-all-about-it-so-you-dont-have-to)
[^interviewnode]: [InterviewNode - Cracking ML Take-Home Assignments](https://interviewnode.com/post/cracking-ml-take-home-assignments-real-examples-and-best-practices)
[^khushal-kumar]: [Medium - Khushal Kumar](https://medium.com/@khushalkumar/my-generative-ai-engineer-interview-experience-got-hired-f8a027e070b0)
[^linkjob-anthropic]: [LinkJob - Anthropic Software Engineer Interview](https://www.linkjob.ai/interview-questions/anthropic-software-engineer-interview/)
[^linkjob-openai]: [LinkJob - OpenAI Loop Interview](https://www.linkjob.ai/interview-questions/openai-loop-interview)
[^mai-chi-bao]: [Dev.to - Mai Chi Bao, RAG Chatbot Interview](https://dev.to/mrzaizai2k/how-i-aced-my-llm-interview-building-a-rag-chatbot-2p6f)
[^promptlayer]: [PromptLayer - The Agentic System Design Interview](https://blog.promptlayer.com/the-agentic-system-design-interview-how-to-evaluate-ai-engineers/)
[^reddit-yc-assignments]: [Reddit - What Is Your Interview Assignment for AI Engineers?](https://www.reddit.com/r/ycombinator/comments/1jnfijm/what_is_your_interview_assignment_for_ai_engineers/) (r/ycombinator)
[^tushar-eightfold]: [Medium - Tushar Bhardwaj, Eightfold.ai](https://medium.com/@bhardwajtushar2004/inside-eightfold-ais-agentic-ai-internship-hiring-process-2026-f86dcb625aa8)
[^gh-rokomari]: [GitHub - RokomariTask](https://github.com/gazitanbhir/RokomariTask) - Rokomari.com AI Engineer
[^gh-streamkar]: [GitHub - Streamkar-Chatbot](https://github.com/Tejasv2002/Streamkar-Chatbot) - StreamKar RAG chatbot
[^gh-dge-1]: [GitHub - DGE-assignment](https://github.com/nazar-zhcet26/DGE-assignment) - DGE agentic RAG
[^gh-dge-2]: [GitHub - DGE_RAG_APP](https://github.com/Youssef-Matloob/DGE_RAG_APP) - DGE RAG application
[^gh-bmw]: [GitHub - bmw-ai-engineer-case-study](https://github.com/SHUBHAM-max449/bmw-ai-engineer-case-study) - BMW Group AI Engineer Intern
[^gh-ncapek]: [GitHub - ai_engineer_interview_2025](https://github.com/ncapek/ai_engineer_interview_2025) - RAG chatbot with MongoDB Atlas
[^gh-bithealth-1]: [GitHub - bithealth-crfc](https://github.com/verneylmavt/bithealth-crfc) - Bithealth code refactoring
[^gh-bithealth-2]: [GitHub - bithealth_home_assesment](https://github.com/fakhrulnurmulyana/bithealth_home_assesment) - Bithealth assessment
[^gh-bithealth-3]: [GitHub - bithealth-assesment](https://github.com/futurebiomedeng/bithealth-assesment) - Bithealth assessment
[^gh-bithealth-4]: [GitHub - bithealthtest](https://github.com/Nerrad07/bithealthtest) - Bithealth intern
[^gh-bithealth-5]: [GitHub - TechnicalTest-Bithealth](https://github.com/jnny04/TechnicalTest-Bithealth) - Bithealth RAG service
[^gh-neura-dynamics]: [GitHub - Company-Policy-Assistant](https://github.com/LAWSA07/Company-Policy-Assistant---Neura-Dynamics) - Neura Dynamics AI Engineer Intern
[^gh-curling-ai]: [GitHub - hiring-challenge-alpha](https://github.com/Curling-AI/hiring-challenge-alpha) - assistant agent: database, documents, bash
[^gh-skylark]: [GitHub - skylark-bi-insight-agent](https://github.com/venki-byte/skylark-bi-insight-agent) - Skylark Drones AI Engineer
[^gh-govgpt]: [GitHub - govgpt-agentic-rag](https://github.com/AsharAhmad/govgpt-agentic-rag) - GovGPT agentic RAG
[^gh-tiktok-agent]: [GitHub - AI-Engineer-Assignment](https://github.com/ShitalMagar-dev/AI-Engineer-Assignment) - TikTok Ad Campaign Agent
[^gh-kasparro]: [GitHub - kasparro-ai-agentic-content-generation](https://github.com/rak-shi/kasparro-ai-agentic-content-generation-system-Rakshitha_Valipireddy) - Kasparro multi-agent content generation
[^gh-tredence-1]: [GitHub - Minimal-Workflow-Agent-Enigne-Tredence](https://github.com/abhishuman18/Minimal-Workflow-Agent-Enigne-Tredence-) - Tredence workflow engine
[^gh-tredence-2]: [GitHub - tredence submission 2](https://github.com/search?q=tredence+ai+engineer&type=repositories) - Tredence AI Engineer Intern
[^gh-tredence-3]: [GitHub - tredence submission 3](https://github.com/search?q=tredence+ai+engineer&type=repositories) - Tredence AI Engineer Intern
[^gh-tredence-4]: [GitHub - tredence submission 4](https://github.com/search?q=tredence+ai+engineer&type=repositories) - Tredence AI Engineer Intern
[^gh-tredence-5]: [GitHub - tredence submission 5](https://github.com/search?q=tredence+ai+engineer&type=repositories) - Tredence AI Engineer Intern
[^gh-tredence-6]: [GitHub - tredence submission 6](https://github.com/search?q=tredence+ai+engineer&type=repositories) - Tredence AI Engineer Intern
[^gh-cerina]: [GitHub - Cerina-Health-AI-Engineer-Role-Task](https://github.com/mad-99/Cerina-Health-AI-Engineer-Role-Task) - Cerina Health 5-agent CBT system
[^gh-hippocratic-1]: [GitHub - hippocratic-ai-bedtime-stories](https://github.com/tasnimhossen/hippocratic-ai-bedtime-stories) - Hippocratic AI bedtime story generator
[^gh-hippocratic-2]: [GitHub - agent_deployment_bedtime_stories](https://github.com/pranav-gilda/agent_deployment_bedtime_stories) - Hippocratic AI with guardrails
[^gh-hippocratic-3]: [GitHub - hippocratic-ai](https://github.com/zoyerz/hippocratic-ai) - Hippocratic AI bedtime stories
[^gh-hippocratic-4]: [GitHub - AI-Agent-Deployment-Engineer-Takehome](https://github.com/reonrash/AI-Agent-Deployment-Engineer-Takehome) - Hippocratic AI story service
[^gh-cohere]: [GitHub - cohere_sales_agent](https://github.com/Aaronxvc/cohere_sales_agent) - Cohere sales insights agent
[^gh-spur-1]: [GitHub - spur-live-chat-agent](https://github.com/selvamsmk/spur-live-chat-agent) - Spur live chat agent
[^gh-spur-2]: [GitHub - spur-ai-chat](https://github.com/richiesinhala/spur-ai-chat) - Spur AI chat with Prisma/Svelte
[^gh-trestle]: [GitHub - Trestle_AI_Engineer_Intern_Assignment](https://github.com/gulmittal/Trestle_AI_Engineer_Intern_Assignment-) - Trestle marksheet extraction
[^gh-emitrr-1]: [GitHub - Physician-Notetaker](https://github.com/Iammilansoni/Physician-Notetaker) - Emitrr medical transcription
[^gh-emitrr-2]: [GitHub - Emitrr submission 2](https://github.com/search?q=emitrr+ai+engineer&type=repositories) - Emitrr AI Engineer Intern
[^gh-legal-doc]: [GitHub - Files.Invis](https://github.com/Udaykeerthan67/Files.Invis) - AI-powered legal document analysis
[^gh-mindwell]: [GitHub - mindwell-assignment-2026](https://github.com/mathemage/mindwell-assignment-2026) - Mindwell AI Engineer case study
[^gh-voice-ai]: [GitHub - voice-ai-assignment](https://github.com/Viren-55/voice-ai-assignment) - real-time concall transcription
[^gh-hrytos]: [GitHub - Transport-Query-Agent](https://github.com/vaishnavip-23/Transport-Query-Agent) - Hrytos Singapore transport agent
[^gh-pineos]: [GitHub - investment_coach_bot](https://github.com/anuradhabudhar214-tech/investment_coach_bot) - PineOS.ai investment coaching bot
[^gh-context-engineering]: [GitHub - context-engineering-takehome](https://github.com/jkbrooks/context-engineering-takehome) - D&D simulation with context engineering
[^gh-gupshup]: [GitHub - GUPPSHUPP_Founding_AI_Engineer_Assignment](https://github.com/amityadav108/GUPPSHUPP_Founding_AI_Engineer_Assignment) - memory and personality engine
[^gh-upliance-1]: [GitHub - RPS-Plus-Al-Judge](https://github.com/Thejas10042001/RPS-Plus-Al-Judge) - upliance.ai conversational agents
[^gh-upliance-2]: [GitHub - upliance.ai_assignment](https://github.com/dsulzd/upliance.ai_assignment) - upliance.ai conversational agents
[^gh-gamma]: [GitHub - gamma-project](https://github.com/audoir/gamma-project) - Gamma markdown-to-slides
[^gh-zuneko]: [GitHub - Smart-LLM-Router-Observability-Platform](https://github.com/Sushma-Sangolli/Smart-LLM-Router-Observability-Platform) - Zuneko Labs LLM router
[^gh-edtronaut]: [GitHub - AI-Coworker-Engine](https://github.com/jerichosuguru/AI-Coworker-Engine) - Edtronaut NPC system
[^gh-fynd]: [GitHub - fynd-ai-feedback-system](https://github.com/pranaymanapure/fynd-ai-feedback-system) - Fynd AI feedback system
[^gh-krisp]: [GitHub - krisp_ai_engineer_role_task](https://github.com/Artush-Baghdasaryan/krisp_ai_engineer_role_task) - Krisp dedup and clustering
[^gh-deel]: [GitHub - deel-assignment](https://github.com/kamran-14/deel-assignment) - Deel transaction matching
