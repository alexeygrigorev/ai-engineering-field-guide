# Skills That Actually Get You Hired

Based on real discussions from Reddit and X (assessed via deep research with ChatGPT, Gemini, Grok) and anecdotal stories shared with me privately. These are patterns from what candidates and hiring managers actually report.

## Baseline (Expected of Everyone)

- RAG: Design/implementation questions
- Vector DBs: Trade-off discussions (Pinecone vs. FAISS vs. Qdrant)
- Tool Calling: Agent system design, function calling
- Python: Coding rounds, project implementations
- APIs: Integration questions, deployment considerations

## Differentiators (What Separates Candidates)

- Evaluation frameworks: Companies assume anyone can build a chatbot. They hire people who can measure one. [Hamel Husain](https://hamel.dev/blog/posts/evals/): "Unsuccessful LLM products almost always share a common root cause: a failure to create robust evaluation systems"
- Cost & latency awareness: Production thinking around token usage, batching, caching, model routing. Candidates must reason about token budgets and per-query costs — a dimension largely absent from traditional interviews ([InterviewQuery 2025](https://www.interviewquery.com/p/ai-interview-trends-tech-hiring-2025))
- Observability: Logging, monitoring, tracking hallucinations, drift detection
- System diagrams: Clear architecture thinking, trade-off explanations
- Production experience: Docker, CI/CD, actual deployment—not just notebooks
- AI fluency: Hands-on with AI coding tools (Cursor, Claude Code). Miro lists "AI-First Proficiency" as a hiring criterion. TRM Labs: "AI fluency is a baseline expectation"


## The "Top 1%" Candidate Profile

From successful candidates' stories:
- System Ownership: Can build, deploy, AND scale—not just integrate APIs
- Production Awareness: Token tracking, latency, hallucination rates as first-class concerns
- Trade-off Fluency: Can explain why they chose X over Y in architectural decisions
- Failure Stories: Can describe what went wrong and what they learned (not just successes)
- Tinkerer Mindset: Hands-on experimentation, strong opinions on model selection and tools, staying current with developments. [PromptLayer](https://blog.promptlayer.com/the-agentic-system-design-interview-how-to-evaluate-ai-engineers/) values "tinkerers who thrive in uncertainty" over rigid academic approaches


## Portfolio Strategy That Works (2026)

- Single high-quality project > Multiple certifications: A multi-agent system that scales to 100k+ queries impresses more
- Production evolution: Show optimization from prototype to cost-efficient production
- Clean GitHub: Exhaustive README, demos, clear documentation — cited as primary reason for recruiter interest
- Evaluation included: Every RAG system should have an eval harness (LLM-as-judge, golden sets)

## Key Resources

- [Chip Huyen: AI Engineering (2025)](https://huyenchip.com/books/) - the definitive book on building with foundation models
- [Eugene Yan: Patterns for Building LLM-based Systems](https://eugeneyan.com/writing/llm-patterns/) - 7 core patterns (evals, RAG, fine-tuning, caching, guardrails, defensive UX, data flywheel)
- [What We Learned from a Year of Building with LLMs](https://applied-llms.org/) - collective lessons from 6 practitioners
- [Maven: AI Evals for Engineers & PMs](https://maven.com/parlance-labs/evals) - Hamel Husain & Shreya Shankar
- See [Awesome AI Engineering](../awesome.md) for the full collection
