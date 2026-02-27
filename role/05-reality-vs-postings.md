# AI Engineer Role: Reality vs. Job Postings

Based on real discussions from Reddit and X (assessed via deep research with ChatGPT, Gemini, Grok) and anecdotal stories shared with me privately. Complements the quantitative job analysis with qualitative insights from what candidates and hiring managers actually report.

![Event series announcement and a response from @thewhychain about the gap between job descriptions and actual AI engineer work](../assets/images/event-series-tweet.jpg)

From Dmitrii Malakhov ([@thewhychain](https://x.com/thewhychain)): "hired for 'AI engineer' roles twice. the job description said RAG and embeddings. the job turned out to be 80% prompt engineering + glue code + monitoring. the 1500 JDs probably have the same problem - they describe ambition, not what you do all day"


## AI Engineer vs ML Engineer: The Confusion

Problem: Titles are misaligned. Recruiters post "AI Engineer" but mean ML Engineer, or vice versa.

Sources:
- [AI Engineer Vs ML Engineer, what's the difference?](https://www.reddit.com/r/learnmachinelearning/comments/1nu6ug7/ai_engineer_vs_ml_engineer_whats_the_difference/) - r/learnmachinelearning

Consensus from discussions:
- ML engineers focus on training/tuning models
- AI engineers integrate pre-trained models into applications
- "AI Engineer" often just a rebrand driven by the GenAI boom

### What People Actually Report

- Applying for AI Engineer → Get grilled on classical ML
- Expecting agentic workflows → Asked to train models from scratch
- Wanting LLM integration work → Evaluated on infrastructure


## What AI Engineers Actually Do


### Three Primary Work Types

Orchestrators (~50%): RAG pipelines, vector DBs, agentic workflows
- Building "ATOM": Local assistant with long-term memory consolidation
- Slack conversation QA: Ingesting threads, handling context decay
- Wireframe-to-UI agents: Transforming designs into code
- Multi-tenant backends: Per-user vector namespaces, token budgeting
- Agentic debate systems: Agents that tune each other's parameters

Evals Specialists (~40%): Building evaluation frameworks
- LLM-as-judge systems: Using models to score other model outputs
- Golden datasets: Curated test sets for measuring RAG performance
- Hallucination detection: Tracking when answers drift from retrieved context
- Production metrics: Recall@K, latency per query, cost per 1k requests

Efficiency Wrappers (~10%): Streaming, prompt caching, speculative decoding
- Semantic caching: Storing responses to similar queries
- Token optimization: Domain-specific tokenizers to reduce sequence length
- Rate limit handling: Fallback across multiple providers
- Model routing: Cheap models for simple tasks, expensive ones when needed

### Day-to-Day vs. Assumptions

- "Write prompts all day" → Writing code that dynamically generates prompts based on context
- "Call OpenAI API" → Building systems with fallbacks, monitoring, cost tracking, multiple providers
- "Train models" → Rarely. Use pre-trained models via APIs or open-source weights
- "Work in notebooks" → Moving to production APIs (FastAPI/Go) with Docker, CI/CD

### The Debug Loop

Real challenges people report:
- Debugging why an LLM ignored an instruction in a 50-step agentic chain
- Figuring out which retrieval chunk caused a hallucination
- Optimizing token usage without degrading output quality
- Handling rate limits across multiple API providers


## Skills That Get You Hired

See [Skills That Actually Get You Hired](../interview/04-skills-that-get-you-hired.md) for the full breakdown: baseline expectations, differentiators, the "top 1%" candidate profile, and portfolio strategy.


## Jobs vs. Reality Gap

| Dimension | Job Postings Say | People Actually Experience |
|-----------|------------------|---------------------------|
| RAG | Core skill (35.9% mention it) | Assumed baseline—evaluations matter more |
| Fine-tuning | Often mentioned | Rarely tested directly unless role-specific |
| ML knowledge | 64% require some ML | Often lighter weight than production skills |
| Full-stack | 93% require beyond-GenAI | Confirmed—end-to-end delivery expected |
| AI tools | Not usually mentioned | Increasingly tested (or ironically banned in interviews) |


## The "Combo Role" Problem


Common complaint: Jobs demand 3 roles in 1.

Reality: "AI Engineer" often means:
- ML Engineer (training models)
- MLOps Engineer (deployment infrastructure)
- Data Engineer (pipelines)
- Or actual AI Engineering (LLM orchestration)


## Key Takeaways

1. Titles are broken: "AI Engineer" means different things at different companies
2. Production thinking wins: Cost, latency, observability—not just accuracy
3. Evaluation is the real skill: Anyone can build; few can measure if it works
4. System owners get hired: People who can build → deploy → scale → measure
5. Gap remains: Job postings don't fully reflect what's actually tested
