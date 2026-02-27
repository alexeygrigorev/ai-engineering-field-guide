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

Build 5-6 small focused projects rather than one large project. Spend 1-2 weeks on each. Each time focus on one area: one project on building an agent, another on deployment and CI/CD, another on data ingestion for RAG. At the end you have a good overview of different technologies.

When targeting specific companies: look at companies hiring in your area. Read their engineering blogs to understand what problems they solve. Build 2-3 projects in that domain using relevant datasets. At interviews, you have relevant things to discuss.


## What Hiring Managers Actually Look At

Based on Q&A from [Webinar 2: Defining the AI Engineer Role](../webinars/02-defining-the-role.md).

Recruiters do not look at your GitHub. They check whether some project exists or not and move on.

Hiring managers have 5-10 minutes before an interview. They open the GitHub link, look at what is there in general. They will not read code in detail. A project would have to really interest them for them to look deeper.

What hiring managers want to see:
1. The project solves a real problem - what it does, why it exists
2. A clear description so they can immediately understand what is going on
3. Signs that the project is close to production: tests, evaluation, CI/CD, deployment

The more checkboxes you check, the better. Tests add a plus, CI/CD adds a plus, good code adds a plus, images, demos, videos add a plus.

For take-home assignments, people read more carefully. Some hiring managers actually run the code. For take-home assignments, follow engineering best practices: write tests, have code coverage ideally.

Nobody looks at commit history. When looking at a project, people look at the project in its current state.


## Writing a Good README

The README is the most important file in your project. It is the first and often only thing a hiring manager reads.

Write your README for two audiences:

1. A peer reviewer who has time to check everything and verify all criteria are met. This motivates you to write good code, clearly and without cutting corners.
2. A hiring manager who has almost no time. Convey the maximum amount of information in the shortest time.

The README should: describe the project clearly, explain what specific problem it solves, and link directly to important parts (prompts, tools, evaluation). Everything else adds bonus points: tests described, CI/CD mentioned, images, demos, videos.

Not too big and not too small. AI-generated READMEs are obvious and mix useful information with filler. Write it yourself or heavily edit what the AI produces.


## Original Projects vs Tutorials

If someone says in an interview "this was a course, I just copied from there" - hiring managers immediately lose interest.

There are important distinctions:
- Course with step-by-step instructions that you repeat - everyone has the same code. Not much value.
- Course homework where the task is given but the implementation is yours - much more valuable.
- Original project you came up with and built from scratch - enormous value, both for you and for the interviewer.

When you were really involved in the task, you will have answers to questions because you lived through it, not just copied it.


## Production Practices in Personal Projects

Companies do not expect production-level engineering in personal projects. That would be over-engineering - it would look forced. It is very hard to have real production-level problems in personal projects.

Clarity is more important - everything should be clean and understandable, solving your problem. Do not forget about basic best practices, but do not overdo it.

If you have a personal project that genuinely requires production-level infrastructure, you probably do not need a job - you already have one.

Tests and CI/CD, however, are easy to add - especially with AI assistants. You need to write tests regardless. And once you have tests, wrapping them in GitHub Actions is a 5-minute thing. Start with unit tests, then integration tests, then end-to-end tests, then LLM-as-judge evaluations.


## Using AI Assistants in Your Portfolio

Using Claude Code or similar assistants is neutral on a portfolio. If you do not use any AI assistant, you are missing out. But there is no reason to specifically mention it.

If you want to be open about it, you can say at the end that the project was built using AI-assisted development and indicate your contribution.

If a hiring manager asks about it, the conversation will go into how you used the assistant, how you gave instructions, how you made sure the agent did not make mistakes. If your answer is "I gave a prompt and everything worked from the first try" - that raises questions. Because it never works from the first try. Having many iterations is very valuable and is considered a useful skill.

If the code is 100% written by the assistant and you fully understand it - great. But if something goes wrong in production and you do not have access to the agent, can you fix the problem? For personal projects, not understanding 50% is fine. For critical production projects, you should have a deeper understanding.
