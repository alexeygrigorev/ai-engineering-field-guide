# Portfolio Project Ideas

Project ideas that demonstrate AI engineering skills relevant to the job market. Each project covers patterns that appear frequently in job descriptions.


## Marketplace with AI Pre-filling

Build an online classifieds platform where users upload item photos and the system auto-fills listing details (title, description, category, price).

Skills demonstrated:

- LLM API integration (vision + structured output)
- Prompt engineering and iteration
- Evaluation dataset and testing
- FastAPI backend
- CI/CD pipeline

Example: [Trova / simple-sell](https://github.com/alexeygrigorev/simple-sell/)

Complexity: beginner. Good first AI engineering project.


## Personal Knowledge Management Bot

Build a Telegram bot that processes multi-modal input (voice notes, images, links, text) and uses an AI agent to organize content into structured articles.

Skills demonstrated:

- Multi-modal input handling (voice transcription, vision APIs)
- Agent orchestration with skills/commands pattern
- Subagents for parallel processing
- Git as a knowledge base
- Message queuing and rate limiting
- Production reliability (session persistence, retries)

Complexity: intermediate. Shows real-world agent patterns.


## Community Platform with Multi-Agent System

Build a web platform using a multi-agent orchestrator: separate agents for software engineering, testing, on-call monitoring, and product management.

Skills demonstrated:

- Multi-agent architecture (orchestrator pattern)
- Agent role specialization
- Autonomous task decomposition
- Testing strategy for AI-generated code
- Long-running agent management (16+ hours)

Complexity: advanced. Shows multi-agent coordination at scale.


## RAG-based FAQ/Support System

Build a question-answering system over company documentation using retrieval-augmented generation.

Skills demonstrated:

- Document ingestion pipeline
- Vector/text search (Elasticsearch, Pinecone, pgvector)
- Retrieval and reranking strategies
- Evaluation with golden datasets
- LLM-as-judge for answer quality
- Production monitoring (retrieval quality, latency, cost)

Complexity: intermediate. The most in-demand pattern (35.9% of jobs mention RAG).


## AI Agent with Tool Use

Build an agent that can use multiple tools to accomplish tasks (web search, database queries, API calls, code execution).

Skills demonstrated:

- Tool definition and schema design
- Agent loop with step limits and timeouts
- Guardrails and business rule constraints
- Multi-step evaluation (correct tools, correct sequence)
- Cost and latency instrumentation
- Trace logging and observability

Complexity: intermediate to advanced. Agents appear in 14.4% of jobs and growing.


## How to Pick a Project

1. Pick a specific domain (e-commerce, healthcare, finance, real estate)
2. Go to a real company's website, see what problems they solve
3. Think about how you would solve one of those problems with AI
4. Build it, with tests, evaluation, and monitoring
5. Do this multiple times, then go to interviews and talk about these projects

A single high-quality project with evaluation, tests, and a clean README is worth more than multiple certifications.
