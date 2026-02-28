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
- Safety Awareness: For agentic AI roles, convincing answers signal three things: production experience, safety awareness, and strong system design taste. "The best answers aren't the most confident ones -- they're the ones that show you understand the problem deeply enough to know where the hard parts are." ([TechEon](https://atul4u.medium.com/the-complete-agentic-ai-system-design-interview-guide-2026-f95d0cfeb7cf))
- Honest Uncertainty: Calibrated uncertainty is a feature, not a weakness. Agents that never say "I don't know" are poorly designed -- the same applies to candidates. Knowing what you don't know signals real production experience ([TechEon](https://atul4u.medium.com/the-complete-agentic-ai-system-design-interview-guide-2026-f95d0cfeb7cf))


## Portfolio Strategy That Works (2026)

- Single high-quality project > Multiple certifications: A multi-agent system that scales to 100k+ queries impresses more
- Production evolution: Show optimization from prototype to cost-efficient production
- Clean GitHub: Exhaustive README, demos, clear documentation — cited as primary reason for recruiter interest. An xAI candidate credited Grok-related PRs on GitHub and a decent follower count for getting "pushed to the top of the pile" and hearing back within days ([Reddit](https://www.reddit.com/r/leetcode/comments/1pjhw1i/xai_ai_engineer_backendinfra_interview_just/))
- Evaluation included: Every RAG system should have an eval harness (LLM-as-judge, golden sets). One interviewer reported "most candidates don't seem to start with evals and that's a red flag in the first 10-15 mins" ([Reddit r/ycombinator](https://www.reddit.com/r/ycombinator/comments/1jnfijm/what_is_your_interview_assignment_for_ai_engineers/))

## What to Have Ready Before You Apply

Some companies require more than a resume upfront. Having these ready saves time and strengthens your application:

- A GitHub portfolio with AI projects - Dentsu Creative asks candidates to submit "portfolio or GitHub showcasing AI/automation projects you've built"
- A "best project" story with metrics - Wolters Kluwer asks for a "Statement of Exceptional Work" covering your role, technical challenges, and measurable impact
- Opinions on AI, not just skills - Dentsu Creative asks "your thoughts on where most companies go wrong with AI implementation"
- Be ready to write, not just code - Strange Loop Labs requires a 1-2 page essay. Apollo.io requires 5 short screening questions answered in the application - "applications without answers will not be reviewed"

## What Separates Candidates Who Get Hired

From 50+ AI engineer interviews observed at top startups ([Fonzi AI](https://medium.com/fonzi-ai/what-ive-learned-from-sitting-in-on-50-ai-engineer-interviews-c493696453c4)):

- The first 5 minutes decide everything. Lead with impact: "I built a RAG pipeline that reduced customer support response time by 40%" beats listing model names
- Talk like a builder, not a researcher. Trade-off thinking wins: "We tried fine-tuning but it hallucinated too often, so we switched to hybrid RAG - lost some nuance but gained reliability"
- Cost awareness is a superpower. One engineer showed a before-and-after cost breakdown proving 70% reduction in OpenAI spend - got an offer the next day
- Honesty about gaps beats bluffing. "I haven't worked with LangSmith yet, but if you're using it for evals, I'd love to understand how you've set up your metrics" - turned into a 10-minute discussion and a job offer
- You don't need to be a unicorn. Companies want full-stack AI engineers, but will hire strong generalists with depth in 1-2 areas who can collaborate and grow
- One brilliant answer on a fundamental concept can carry a mediocre interview -- and conversely, failing on one fundamental concept can tank an otherwise strong performance. From an interviewer who hires AI engineers: a candidate can go through the whole interview seeming "meh," then answer one question exceptionally well and that carries their candidacy forward. But if an otherwise strong candidate fails on a core concept (e.g., race conditions, GIL, async fundamentals), it raises serious doubts about their qualifications regardless of how well they answered everything else. ([PropTech Founder](https://www.youtube.com/watch?v=leXRiJ5TuQo))

## The 90/10 Rule

[Dr. Sundeep Teki](https://www.sundeepteki.org/advice/the-ultimate-ai-research-engineer-interview-guide-cracking-openai-anthropic-google-deepmind-top-ai-labs) (guide for OpenAI, Anthropic, DeepMind interviews): 90% of interview success comes from prior career decisions - university, internships, companies, relationships. Only 10% is application strategy, networking, resume optimization, and negotiation.

## Preparation Advice from People Who Succeeded

1. Build 2-3 end-to-end projects: RAG app, autonomous agent, something deployed
2. Practice explaining trade-offs aloud: verbal reasoning matters more than perfect code. "Practice verbally explaining concepts without hesitation -- fluency signals experience" ([Reddit r/generativeAI](https://www.reddit.com/r/generativeAI/comments/1p4yrjk/how_to_clear_interviews_in_ai_gen_rag_llm/))
3. Learn evaluation early: Ragas, DeepEval, LLM-as-judge frameworks
4. Show production readiness: Docker, CI/CD, monitoring - not just notebooks
5. Understand cost/latency: caching, batching, model routing decisions
6. Practice storytelling, not memorized answers - refine how you talk through your work with clarity and confidence. Record yourself explaining your last project in 60 seconds ([Fonzi AI](https://medium.com/fonzi-ai/what-ive-learned-from-sitting-in-on-50-ai-engineer-interviews-c493696453c4))
7. For agentic AI roles: at senior/staff levels, interviewers typically pick 3-5 questions and drill deep into failure modes, trade-offs, and "what went wrong last time" rather than covering many topics superficially. They expect architecture diagrams and war stories from real systems. Prepare to explain the orchestrator vs LLM responsibility split, how you enforce autonomy boundaries structurally (not via prompts), and how you handle agent termination conditions ([TechEon](https://atul4u.medium.com/the-complete-agentic-ai-system-design-interview-guide-2026-f95d0cfeb7cf))

### Preparation by the numbers
Mimansa Jaiswal, who interviewed at 20+ companies (Anthropic, OpenAI, Meta, Amazon, Apple, Google): completed 150+ NeetCode problems, ~6 interview prep hours daily over 12 weeks, ~10 iterations on self-presentation blurb. Transparency about limitations performed better than bluffing ([source](https://mimansajaiswal.github.io/posts/llm-ml-job-interviews-fall-2024-process/))

### Fit and domain expertise matter more than perfect execution
Yuan Meng, who received offers from nearly all 5-10 onsite companies at the senior+ level: "Why you? Why not anyone else?" is the central hiring question. Interview success correlates more with domain expertise and passion alignment than perfect execution across all rounds. His competitive advantage came from deep recommender systems knowledge spanning every aspect of RecSys since 2022, which interviewers recognized even when other rounds weren't flawed ([source](https://www.yuan-meng.com/posts/mle_interviews_2.0/))

### Take-homes: treat them like a mini job
Most engineers put too little effort into take-homes. The best candidates document their decisions, test edge cases, and submit with a Loom video walking through the design. One engineer built a CLI tool for summarizing PDFs and included a config file so the hiring manager could test different models and chunking strategies - they had two competing offers within 72 hours ([Fonzi AI](https://medium.com/fonzi-ai/what-ive-learned-from-sitting-in-on-50-ai-engineer-interviews-c493696453c4))

## Transitioning from SWE to AI Engineer

Janvi Kalra ([Pragmatic Engineer](https://newsletter.pragmaticengineer.com/p/from-software-engineer-to-ai-engineer), [YouTube interview](https://www.youtube.com/watch?v=GEqJrKYnhbY)) transitioned from SWE at Coda to AI engineering at OpenAI after interviewing at 46 companies over 6 months:

- Don't wait for permission. When initially rejected for Coda's AI team, she self-taught by building LLM apps, attending hackathons, and writing about it publicly. Five months later, she was welcomed onto the team: "We see that you truly care about this because you've been working on it in your free time"
- Categorize the AI market to focus your search: product companies (Cursor, Codium), infrastructure companies (Modal, Fireworks, Pinecone, Braintrust), and model companies (OpenAI, Anthropic, Google, Meta). Decide which segment excites you most
- Do startup due diligence like an investor. Your career growth at a startup is contingent on the startup growing. Evaluate: (1) revenue and revenue growth rate, (2) large market with room to expand, (3) loyal/obsessed customers, (4) competitive positioning. "All engineers that take a pay cut to go to a startup should have an informed thesis on why they think that company is going to grow during their tenure." If a startup won't share financials after you have an offer, that's a red flag
- Learn by doing. Hackathons (weekend and multi-week online), building in public, and reading blogs/Twitter were more effective than courses when the field moves this fast

A SWE with 6 YOE who transitioned to AI engineering over 18 months shares a similar trajectory ([Reddit r/learnmachinelearning](https://www.reddit.com/r/learnmachinelearning/comments/1pwvb5a/how_i_cracked_an_ai_engineer_role/)): foundations (Python, math, Andrew Ng courses) → ML/DL projects (Kaggle, Hugging Face) → modern AI (RAG chatbot, fine-tuned LLMs, multi-modal apps) → MLOps (FastAPI, Docker, monitoring) → interviews. Key insight: "AI engineering is 70% software development anyway. As a developer, deployment was my superpower -- AI folks often struggle with scaling, but I already knew Docker." Interview questions were about understanding and decision-making, not math-heavy theory

## Key Resources

### Books and courses
- [Chip Huyen: AI Engineering (2025)](https://huyenchip.com/books/) - the definitive book on building with foundation models
- ["Understanding Deep Learning" by Simon Prince](https://udlbook.github.io/udlbook/) - recommended for ML fundamentals prep; develop deep conceptual understanding rather than checkbox memorization ([Yuan Meng](https://www.yuan-meng.com/posts/mle_interviews_2.0/))
- ["Designing Data-Intensive Applications"](https://dataintensive.net/) - skim chapters 1-11 for system design prep ([Yuan Meng](https://www.yuan-meng.com/posts/mle_interviews_2.0/))
- [Andrej Karpathy: Neural Networks - Zero to Hero](https://karpathy.ai/zero-to-hero.html) - in-depth courses on neural networks and Transformers

### Articles and patterns
- [Eugene Yan: Patterns for Building LLM-based Systems](https://eugeneyan.com/writing/llm-patterns/) - 7 core patterns (evals, RAG, fine-tuning, caching, guardrails, defensive UX, data flywheel)
- [What We Learned from a Year of Building with LLMs](https://applied-llms.org/) - collective lessons from 6 practitioners

### Coding and practice platforms
- [NeetCode 250](https://neetcode.io/) - recommended by multiple successful candidates for LeetCode-style prep. Yuan Meng: focus on problem-solving intuition over memorization; connect problems to real web-scale data processing challenges ([source](https://www.yuan-meng.com/posts/mle_interviews_2.0/)). Janvi Kalra: use spaced repetition ([source](https://newsletter.pragmaticengineer.com/p/from-software-engineer-to-ai-engineer))
- [Deep-ML](https://www.deep-ml.com/) - ML-specific coding practice platform for implementing architectures from scratch ([Yuan Meng](https://www.yuan-meng.com/posts/mle_interviews_2.0/), [Mimansa Jaiswal](https://mimansajaiswal.github.io/posts/llm-ml-job-interviews-resources/))
- [Great Frontend](https://www.greatfrontend.com/) - front-end interview questions for full-stack AI engineer roles ([Janvi Kalra](https://newsletter.pragmaticengineer.com/p/from-software-engineer-to-ai-engineer))

### ML/LLM coding prep (implementation interviews)
Mimansa Jaiswal's detailed breakdown of what to implement from scratch for ML coding rounds (25-35 min, no debugging): neural networks, LSTMs, RNNs in NumPy/PyTorch; attention mechanisms (cached, grouped query, multi-head); Transformer components; RAG/inference decoding strategies (top-p, top-k, beam search). Use "shape suffixes" (Noam Shazeer method) in variable naming to track tensor dimensions ([source](https://mimansajaiswal.github.io/posts/llm-ml-job-interviews-resources/))

### System design
- [Alex Xu: System Design Interview books](https://www.amazon.com/System-Design-Interview-insiders-Second/dp/B08CMF2CQF) - "just reading those, really understanding them, doing them again and again" ([Janvi Kalra](https://newsletter.pragmaticengineer.com/p/from-software-engineer-to-ai-engineer))
- Company engineering blogs from Netflix, Uber, Pinterest, and other target companies for ML infra design prep ([Yuan Meng](https://www.yuan-meng.com/posts/mle_interviews_2.0/))

### Evals and courses
- [Maven: AI Evals for Engineers & PMs](https://maven.com/parlance-labs/evals) - Hamel Husain & Shreya Shankar

### Behavioral
- SAIL structure (Situation, Action, Impact, Learning) for behavioral interviews - map stories explicitly to company values, not just rigid frameworks ([Yuan Meng](https://www.yuan-meng.com/posts/mle_interviews_2.0/))
- Prepare distinct examples per interview - "repeatedly telling the same stories can make responses sound mechanical." Vary personal introductions across interviews. Use water breaks between STAR paragraphs to maintain presence ([Mimansa Jaiswal](https://mimansajaiswal.github.io/posts/llm-ml-job-interviews-resources/))

- See [Awesome AI Engineering](../awesome.md) for the full collection

---

## Comprehensive Hiring Guide

A deep, categorized collection of advice on what gets you hired as an AI/ML engineer -- drawn from interview experiences, hiring manager observations, career blogs, YouTube transcripts, and web research. Each piece notes its source perspective where known: (candidate), (interviewer/hiring manager), (industry observer).

---

### Skills & Knowledge That Matter Most

What interviewers actually test versus what job postings list. The gap between the two is significant.

What job postings list (baseline everyone claims):
- Python, TensorFlow/PyTorch, SQL
- "Experience with LLMs" or "familiarity with machine learning"
- Cloud platforms (AWS/GCP/Azure)
- Generic "strong communication skills"

What interviewers actually test and value:

- Evaluation frameworks over model building. Companies assume anyone can build a chatbot. They hire people who can measure one. "Unsuccessful LLM products almost always share a common root cause: a failure to create robust evaluation systems" -- Hamel Husain. Every RAG system you present should have an eval harness: LLM-as-judge, golden sets, precision@k, retrieval hit rates. (interviewer perspective; [Hamel Husain](https://hamel.dev/blog/posts/evals/))

- Cost and latency reasoning. Candidates must reason about token budgets and per-query costs -- a dimension largely absent from traditional interviews. One engineer showed a before-and-after cost breakdown proving 70% reduction in OpenAI spend and got an offer the next day. Being able to estimate: "100K daily users x 10 interactions x ~2K tokens = 2 billion tokens/day = $13K/day on GPT-4 Turbo" separates production thinkers from prototype thinkers. (interviewer perspective; [InterviewQuery 2025](https://www.interviewquery.com/p/ai-interview-trends-tech-hiring-2025), [Fonzi AI](https://medium.com/fonzi-ai/what-ive-learned-from-sitting-in-on-50-ai-engineer-interviews-c493696453c4), [System Design Handbook](https://www.systemdesignhandbook.com/guides/generative-ai-system-design-interview/))

- Trade-off fluency. "Can you explain why you chose X over Y?" is the senior-level question. Not "what is RAG?" but "when would you NOT use RAG? When would you fine-tune instead? When is prompting enough?" Interviewers evaluate your ability to discuss retrieval speed vs. context length, fine-tuning vs. prompting, GPU cost vs. latency. (interviewer perspective; [InterviewNode](https://www.interviewnode.com/post/generative-ai-system-design-interview-patterns-you-should-know), [DesignGurus](https://www.designgurus.io/blog/openai-system-design-interview-questions))

- Systems thinking, not model knowledge. "Generative AI system design is no longer about pipelines, it's about lifecycles." Interviewers assess architectural reasoning, decision-making under constraints, and communication clarity. They want to see you think in loops: retrieval loops, generation loops, feedback loops. (interviewer perspective; [InterviewNode](https://www.interviewnode.com/post/generative-ai-system-design-interview-patterns-you-should-know))

- Observability and monitoring. Logging, tracing, drift detection, hallucination rate tracking. Chip Huyen: "Log everything" and integrate observability from project inception, not as an afterthought. Track TTFT, TBT, tokens per second, per-user costs, and retrieval hit rates. (industry observer; [Chip Huyen](https://huyenchip.com/2024/07/25/genai-platform.html))

- Safety and guardrails as first-class concerns. Especially at Anthropic: "A system that achieves excellent availability while producing toxic content represents a fundamental failure." Candidates who skip discussion of prompt injection, data leakage, and unsafe tool execution signal weak awareness of GenAI-specific risks. (interviewer perspective; [System Design Handbook - Anthropic Guide](https://www.systemdesignhandbook.com/guides/anthropic-system-design-interview/), [IGotAnOffer](https://igotanoffer.com/en/advice/generative-ai-system-design-interview))

- AI fluency with coding tools. Hands-on proficiency with AI coding tools (Cursor, Claude Code) is increasingly tested directly in interviews. Exponent's mock interview format now allows and expects AI coding agents -- interviewers assess how you prompt, verify, and direct the AI rather than just whether you can code. The biggest pitfall: "relying on AI to make decisions for you." (interviewer perspective; [Exponent mock interview](https://www.youtube.com/watch?v=example), [InterviewQuery 2025](https://www.interviewquery.com/p/ai-interview-trends-tech-hiring-2025))

- Python depth beyond basics. Race conditions, the Global Interpreter Lock, async programming patterns, concurrency vs. parallelism. "I basically try to look for strong Python programmers because we're still at a point where we can't expect people to have GenAI experience. So instead I look for how well does this person know Python backend." (interviewer perspective; Fahd Mirza, AI engineer interviewer, [YouTube](https://www.youtube.com/watch?v=example))

- DSA fundamentals still matter. Even AI-focused roles at Eightfold, OpenAI, Anthropic, and xAI include algorithm rounds. Anthropic conducts a challenging 90-minute CodeSignal assessment requiring perfect correctness. xAI prioritizes LeetCode Hard over volume grinding. (candidate perspective; [Eightfold internship experience](https://medium.com/@bhardwajtushar2004/inside-eightfold-ais-agentic-ai-internship-hiring-process-2026-f86dcb625aa8), [Dr. Sundeep Teki](https://www.sundeepteki.org/advice/the-ultimate-ai-research-engineer-interview-guide-cracking-openai-anthropic-google-deepmind-top-ai-labs))

- ML implementation from scratch. Implementing Multi-Head Attention, full Transformer layers, LoRA, KV cache, and autograd mechanics from memory is tested at frontier labs. Use "shape suffixes" (Noam Shazeer method) in variable naming to track tensor dimensions. (candidate perspective; [Mimansa Jaiswal](https://mimansajaiswal.github.io/posts/llm-ml-job-interviews-resources/), [Dr. Sundeep Teki](https://www.sundeepteki.org/advice/the-ultimate-ai-research-engineer-interview-guide-cracking-openai-anthropic-google-deepmind-top-ai-labs))

- Full-stack capability. "A lot of AI engineer roles are low-key full stack roles or at least backend roles on top of some AI stuff." Be prepared for questions about the JavaScript event loop, database choices, message queues, and API design alongside GenAI topics. (candidate perspective; Fahd Mirza, [YouTube](https://www.youtube.com/watch?v=example))

What matters by seniority level:

| Level | What interviewers focus on |
|---|---|
| Junior/Intern | Coding fundamentals, basic ML concepts, willingness to learn, project enthusiasm |
| Mid-level | End-to-end system knowledge, RAG pipelines, embeddings, production awareness |
| Senior | Trade-off fluency, system design at scale, failure mode reasoning, cost optimization |
| Staff+ | Technical leadership, cross-team influence, project presentations, organizational impact |

---

### Portfolio & Project Strategy

Quality over quantity -- always.

- A single high-quality project that scales to 100K+ queries impresses more than multiple certifications. Show the optimization journey from prototype to cost-efficient production. (industry consensus)

- "Most recruiters spend less than two minutes looking at a GitHub repo. They scan for README clarity, and a deployment link." A live demo on Streamlit, Gradio, or Hugging Face Spaces is gold. ([InterviewNode](http://www.interviewnode.com/post/ml-engineer-portfolio-projects-that-will-get-you-hired-in-2025))

- Every project should include evaluation. "A RAG system without an eval harness is an incomplete project." Include golden datasets, metrics, and before/after comparisons. (interviewer perspective; [PromptLayer](https://blog.promptlayer.com/the-agentic-system-design-interview-how-to-evaluate-ai-engineers/))

Project ideas that actually impress (2026):

1. Production RAG system with eval. Build a document Q&A assistant with hybrid retrieval (dense + keyword), cross-encoder reranking, confidence thresholds, and fallback responses. Include precision@k metrics and a cost analysis. Score: Mai Chi Bao achieved 9/10 on an interview by designing exactly this with open-source tools, including infrastructure cost breakdown ($2,070/month) and dual-model routing. ([Mai Chi Bao](https://dev.to/mrzaizai2k/how-i-aced-my-llm-interview-building-a-rag-chatbot-2p6f))

2. Multi-agent system with scaling. Design agents that collaborate on a task (research reports with citations, customer support with escalation). Show orchestration, error handling, and how you prevent infinite loops and hallucinated tool calls. ([System Design Handbook](https://www.systemdesignhandbook.com/guides/agentic-system-design/))

3. Cost optimization case study. Take a working AI application and show optimization from expensive (GPT-4 for everything) to smart routing (70% to cheaper models, caching, prompt compression). Document the token savings. (industry observer)

4. End-to-end deployed project. Docker, CI/CD, monitoring with Prometheus/Grafana, not just a notebook. Include Kubernetes auto-scaling if you want to stand out. ([Mai Chi Bao](https://dev.to/mrzaizai2k/how-i-aced-my-llm-interview-building-a-rag-chatbot-2p6f))

5. Fraud detection or recommendation engine with real-time features, feedback loops, and model monitoring. Shows classical ML + production engineering. ([InterviewNode](http://www.interviewnode.com/post/ml-engineer-portfolio-projects-that-will-get-you-hired-in-2025))

Portfolio presentation tips:

- Exhaustive README with architecture diagrams, design decisions, and demo links -- cited as the primary reason for recruiter interest (multiple sources)
- Include a config file so hiring managers can test different parameters. One engineer built a CLI tool for summarizing PDFs with configurable models and chunking strategies -- had two competing offers within 72 hours. ([Fonzi AI](https://medium.com/fonzi-ai/what-ive-learned-from-sitting-in-on-50-ai-engineer-interviews-c493696453c4))
- Record a Loom video walking through the design for take-home assignments (candidate perspective; [Fonzi AI](https://medium.com/fonzi-ai/what-ive-learned-from-sitting-in-on-50-ai-engineer-interviews-c493696453c4))

- Open-source contributions as signal. Some companies review contribution history as an alternative or complement to traditional assessments. Architecture-level challenges are better for filtering because AI struggles with them more than routine coding tasks. ([HN](https://news.ycombinator.com/item?id=43882116), [HN](https://news.ycombinator.com/item?id=42182365))

---

### Resume & Application Tips (AI-Specific)

- Lead with impact, not model names. "I built a RAG pipeline that reduced customer support response time by 40%" beats "Experience with LangChain and GPT-4." The first 5 minutes of an interview decide everything. ([Fonzi AI](https://medium.com/fonzi-ai/what-ive-learned-from-sitting-in-on-50-ai-engineer-interviews-c493696453c4))

- Avoid multi-column LaTeX formats. They create ATS parsing issues. Mimansa Jaiswal recommends Typst for future versions. (candidate perspective; [Mimansa Jaiswal](https://mimansajaiswal.github.io/posts/llm-ml-job-interviews-fall-2024-process/))

- Prepare a self-presentation blurb. Focus on 2-3 areas of expertise. Mimansa Jaiswal refined hers through approximately 10 iterations over 12 weeks, covering synthetic data generation, LLM orchestration/agents, and robust evaluation. (candidate perspective; [Mimansa Jaiswal](https://mimansajaiswal.github.io/posts/llm-ml-job-interviews-fall-2024-process/))

- Have a "best project" story with metrics ready. Wolters Kluwer asks for a "Statement of Exceptional Work" covering your role, technical challenges, and measurable impact. ([job posting analysis](../job-market/))

- Have opinions on AI, not just skills. Dentsu Creative asks "your thoughts on where most companies go wrong with AI implementation." Companies want thinkers, not just implementers. ([job posting analysis](../job-market/))

- Be ready to write, not just code. Strange Loop Labs requires a 1-2 page essay. Apollo.io requires 5 short screening questions answered in the application -- "applications without answers will not be reviewed." ([job posting analysis](../job-market/))

- Create a website or blog for professional visibility. Direct LinkedIn outreach to founders and hiring managers proved effective for startups. Employee referrals are crucial but insufficient alone. (candidate perspective; [Mimansa Jaiswal](https://mimansajaiswal.github.io/posts/llm-ml-job-interviews-fall-2024-process/))

---

### Preparation Timelines & Study Plans

From people who actually succeeded:

Mimansa Jaiswal -- 20+ companies (Anthropic, OpenAI, Meta, Amazon, Apple, Google), multiple offers:
- 12 weeks of preparation, ~6 hours daily of interview-specific practice
- 150+ NeetCode problems completed
- ~10 iterations on self-presentation blurb
- Organized preparation in Notion with 7 major sections and categorized questions ("Aced it," "Took time," "Didn't get it," "Just saw it somewhere")
- Transparency about limitations performed better than bluffing: openly disclosed experience with 0.5-1B parameter models only, LoRA focus, no pretraining experience
- ([source](https://mimansajaiswal.github.io/posts/llm-ml-job-interviews-fall-2024-process/))

Yuan Meng -- 5-10 onsite companies at senior+ level, offers from nearly all:
- Deep domain expertise was the competitive advantage: "every aspect of RecSys since 2022"
- NeetCode 250 with focus on problem-solving intuition, not memorization
- Read "Understanding Deep Learning" by Simon Prince thoroughly
- Skimmed "Designing Data-Intensive Applications" chapters 1-11
- Studied engineering blogs from Netflix, Uber, Pinterest for ML infra design prep
- Used SAIL structure (Situation, Action, Impact, Learning) for behavioral interviews
- ([source](https://www.yuan-meng.com/posts/mle_interviews_2.0/))

Janvi Kalra -- 46 companies, SWE to AI engineer, now at OpenAI:
- 6 months of interviewing across product, infrastructure, and model companies
- Used Cracking the Coding Interview and NeetCode Blind 75 with spaced repetition
- Hackathons (weekend and multi-week online) were more effective than courses
- Built LLM apps and wrote about them publicly; self-taught when denied internal AI team role
- Alex Xu System Design Interview books: "just reading those, really understanding them, doing them again and again"
- Great Frontend for full-stack AI engineer front-end prep
- ([source](https://newsletter.pragmaticengineer.com/p/from-software-engineer-to-ai-engineer))

Suggested preparation plan (8-12 weeks):

| Week | Focus |
|---|---|
| 1-2 | Coding fundamentals: NeetCode 150/250, focus on patterns not memorization |
| 3-4 | ML/LLM implementation: Transformers, attention mechanisms, LoRA from scratch using NumPy/PyTorch. Practice on Deep-ML platform |
| 5-6 | System design: Study RAG architecture, agentic design patterns, model serving. Read Chip Huyen's AI Engineering and engineering blogs from target companies |
| 7-8 | Build or polish 1-2 portfolio projects with evaluation, deployment, and documentation |
| 9-10 | Mock interviews: practice verbal trade-off explanations, behavioral stories (SAIL/STAR), system design walkthroughs aloud |
| 11-12 | Company-specific prep: study target company blog posts, products, values. Refine self-presentation blurb. Practice with recording yourself |

---

### Networking & Job Search Strategy

- Categorize the AI market to focus your search. Three categories: product companies (Cursor, Codium), infrastructure companies (Modal, Fireworks, Pinecone, Braintrust), and model companies (OpenAI, Anthropic, Google, Meta). Decide which segment excites you most. (candidate perspective; [Janvi Kalra](https://newsletter.pragmaticengineer.com/p/from-software-engineer-to-ai-engineer))

- The 90/10 rule. 90% of interview success comes from prior career decisions -- university, internships, companies, relationships. Only 10% is application strategy, networking, and negotiation. This means: invest in your career trajectory, not just interview prep. (industry observer; [Dr. Sundeep Teki](https://www.sundeepteki.org/advice/the-ultimate-ai-research-engineer-interview-guide-cracking-openai-anthropic-google-deepmind-top-ai-labs))

- Direct outreach works. LinkedIn messages to founders and hiring managers proved effective for startups. "Reach out to connections despite unpublished work -- most people were immensely supportive." (candidate perspective; [Mimansa Jaiswal](https://mimansajaiswal.github.io/posts/llm-ml-job-interviews-fall-2024-process/))

- Hackathons as networking and learning. Weekend and multi-week online hackathons serve as both skill development and networking. Building in public (blog posts, Twitter threads) was more effective than courses when the field moves this fast. (candidate perspective; [Janvi Kalra](https://newsletter.pragmaticengineer.com/p/from-software-engineer-to-ai-engineer))

- In-person interviews are back. In-person rounds increased from 24% (2022) to 38% (2025) to counter cheating concerns. More frontier labs require in-person onsites. Be prepared to travel. ([InterviewQuery 2025](https://www.interviewquery.com/p/ai-interview-trends-tech-hiring-2025))

- Referrals matter more than cold applications. Network-based hiring is increasing as AI-generated applications flood pipelines. Recruiters can detect when candidates feed resumes directly into ChatGPT. Authentic application materials outperform AI-polished generic submissions. ([HN](https://news.ycombinator.com/item?id=45932838))

- Top candidates accept offers within 2-3 weeks. Companies with slow processes lose strong applicants. Be prepared to move quickly, and manage your interview timeline so onsites cluster together. ([AI Recruitment report](https://juicebox.ai/blog/ai-recruitment-mistakes))

- References matter more than before. Most top companies now require 2-3 references from recent managers and colleagues. Team matching has become competitive; strong candidates may wait weeks for ideal teams. Companies prioritize exact fit over generic strength. (candidate perspective; [Yuan Meng](https://www.yuan-meng.com/posts/mle_interviews_2.0/))

---

### Negotiation & Offer Evaluation

- Your strongest negotiation move is a competing offer. Direct all leverage toward the equity grant size, not base salary, since base bands at each level are relatively narrow. ([TeamRora AI/ML Salary Negotiation Guide](https://www.teamrora.com/post/aiml-salary-negotiation))

- Always benchmark by total compensation, not just base pay. Equity, bonuses, and cloud credits for AI experimentation can add 20-40% to your real annual package. At Meta, total compensation for an E4 MLE is ~$332K, E5 ~$492K, E6 ~$648K annually. ([InterviewQuery salary data](https://www.interviewquery.com/p/ai-engineer-salary-2025-guide))

- AI engineers earn 10-20% more than general software engineers due to specialized expertise. Professionals with AI expertise earn 56% more on average than peers without it. ([Multiple salary surveys](https://www.ziprecruiter.com/Salaries/Ai-Ml-Engineer-Salary))

- Startup due diligence like an investor. "All engineers that take a pay cut to go to a startup should have an informed thesis on why they think that company is going to grow during their tenure." Evaluate: (1) revenue and revenue growth rate, (2) large market with room to expand, (3) loyal/obsessed customers, (4) competitive positioning. If a startup will not share financials after you have an offer, that is a red flag. (candidate perspective; [Janvi Kalra](https://newsletter.pragmaticengineer.com/p/from-software-engineer-to-ai-engineer))

- Watch for offer expiration pressure. "Seven-day expiration windows -- too short in my view -- forcing me to request extensions." Ask for extensions when needed; companies that refuse may signal cultural issues. (candidate perspective; [Mimansa Jaiswal](https://mimansajaiswal.github.io/posts/llm-ml-job-interviews-fall-2024-process/))

- Compensation ranges (2025-2026 US market):

| Level | Big Tech Total Comp | AI Startup Range |
|---|---|---|
| Junior/New Grad | $150K-$250K | $120K-$200K + equity |
| Mid-level | $250K-$400K | $180K-$300K + equity |
| Senior | $350K-$500K | $250K-$400K + equity |
| Staff+ | $500K-$800K+ | $350K-$600K + equity |

(Ranges approximate; varies significantly by company, location, and specific role. Source: [InterviewQuery](https://www.interviewquery.com/p/ai-engineer-salary-2025-guide), [Mimansa Jaiswal](https://mimansajaiswal.github.io/posts/llm-ml-job-interviews-fall-2024-process/))

---

### Career Transitions

SWE to AI Engineer:

Janvi Kalra's transition from SWE at Coda to AI engineering at OpenAI is the canonical example:
- When initially rejected for the internal AI team, she self-taught by building LLM apps, attending hackathons, and writing about it publicly. Five months later, she was welcomed onto the team: "We see that you truly care about this because you've been working on it in your free time"
- AI Engineering blurs traditional boundaries between data science, frontend, backend, and product management. Expect to discard work when model advances render it obsolete
- Your SWE skills are an asset: production deployment, testing, CI/CD, scaling -- these are exactly what differentiates "production AI" from "notebook AI"
- ([Janvi Kalra](https://newsletter.pragmaticengineer.com/p/from-software-engineer-to-ai-engineer))

Analytics/Data Science to AI Engineer:

Raghu Teja Manchala's transition from analytics to AI Engineering at IBM:
- "Transitioning from an Analytics role to an Engineering role in AI is often one of the most challenging shifts for data professionals. Unlike analytics roles, AI Engineer and Machine Learning Engineer positions come with broader responsibilities, ranging from core machine learning to software engineering"
- Focus on strengthening software engineering fundamentals: Docker, CI/CD, APIs, production deployment
- Your data intuition is an asset; couple it with systems-level thinking
- ([IBM interview experience](https://medium.com/))

Research to Industry:

From Dr. Sundeep Teki's guide on research engineer interviews at OpenAI, Anthropic, DeepMind:
- The distinction between research scientists and engineers has blurred. Modern AI Research Engineers must combine "theoretical physics intuition with systems engineering capability and safety awareness"
- OpenAI emphasizes pragmatism and scalability; Anthropic prioritizes safety and alignment; Google DeepMind maintains academic rigor
- Acceptance rates below 1% at elite labs reflect extraordinary competition
- Having publications helps, but production experience increasingly matters alongside them
- ([Dr. Sundeep Teki](https://www.sundeepteki.org/advice/the-ultimate-ai-research-engineer-interview-guide-cracking-openai-anthropic-google-deepmind-top-ai-labs))

Cloud/DevOps/Backend to AI Engineer:

- Your infrastructure skills are in high demand. ML systems need Kubernetes, Docker, CI/CD, monitoring, and cloud deployment -- exactly what you already know
- Layer on: understanding of embeddings, vector databases, RAG architecture, and LLM API patterns
- "Don't think that if you are coming from cloud background, programming background, databases background -- your skills are obsolete. None at all." (industry observer; [Fahd Mirza](https://www.youtube.com/watch?v=Zt-h5BiBWH0))
- The Full-Stack AI Engineer role is a hybrid: "you need the discipline of a software engineer and the intuition of a data scientist" ([Towards Data Science](https://towardsdatascience.com/a-realistic-roadmap-to-start-an-ai-career-in-2026/))

Key principle for all transitions: "Start the job before you have it. Start writing code to do the things you'd like it to do. Building something yourself is what gets you specific knowledge, the type of knowledge you can't get from courses." ([Zero to Mastery](https://zerotomastery.io/blog/how-to-become-an-ai-engineer-from-scratch/))

---

### Common Mistakes to Avoid

In the interview itself:

- Jumping to fine-tuning too early. "Defaulting to fine-tuning without considering prompting, retrieval, or tools suggests poor judgment around cost, iteration speed, and maintainability." Default to prompt engineering with RAG; fine-tune only if extreme specialization or latency requirements demand it. (interviewer perspective; [IGotAnOffer](https://igotanoffer.com/en/advice/generative-ai-system-design-interview))

- Treating the LLM as a source of truth. Relying on raw generation for factual answers instead of grounding with retrieval, tools, or citations raises immediate concerns. (interviewer perspective; [IGotAnOffer](https://igotanoffer.com/en/advice/generative-ai-system-design-interview))

- Skipping evaluation and monitoring. Designing without explaining how output quality, regressions, or safety issues will be measured signals lack of production readiness. (interviewer perspective; [IGotAnOffer](https://igotanoffer.com/en/advice/generative-ai-system-design-interview))

- Name-dropping tools without understanding trade-offs. Instead of "I'd use LangChain," say: "I'd chain retrieval and generation modules to ensure contextual consistency and caching efficiency." If you mention Redis, be prepared to discuss when it might not be the right choice. (interviewer perspective; [InterviewNode](https://www.interviewnode.com/post/generative-ai-system-design-interview-patterns-you-should-know), [HelloInterview OpenAI L5 Guide](https://www.hellointerview.com/guides/openai/l5))

- Ignoring failure modes. "Not addressing failure modes" is a red flag. Discuss what breaks, how failures are detected, and how the system degrades gracefully. (interviewer perspective; [IGotAnOffer](https://igotanoffer.com/en/advice/generative-ai-system-design-interview))

- Over-engineering from the start. "Avoid over-engineering your solution from the start. Focus on getting a working implementation first, then optimize based on the interviewer's follow-up questions." (interviewer perspective; [HelloInterview OpenAI L5 Guide](https://www.hellointerview.com/guides/openai/l5))

- Bluffing on topics you don't know. "I haven't worked with LangSmith yet, but if you're using it for evals, I'd love to understand how you've set up your metrics" -- turned into a 10-minute discussion and a job offer. Admitting "I need a hint" performed better than attempting to bluff. (candidate perspective; [Fonzi AI](https://medium.com/fonzi-ai/what-ive-learned-from-sitting-in-on-50-ai-engineer-interviews-c493696453c4), [Mimansa Jaiswal](https://mimansajaiswal.github.io/posts/llm-ml-job-interviews-fall-2024-process/))

- Failing on fundamental concepts. "If a candidate does very well throughout the interview, but they fail on a certain concept that is very fundamental, it can really make me question their abilities as an engineer." Know how LLMs work (tokenization, transformers, next-token prediction), race conditions, the GIL. (interviewer perspective; Fahd Mirza, [YouTube](https://www.youtube.com/watch?v=example))

In the job search:

- Pursuing only compensation. Recruiters now ask "What problem do you want to solve?" and pass on candidates who cannot articulate this, regardless of technical fit. ([Fonzi AI](https://medium.com/fonzi-ai/i-reviewed-50-failed-ai-hires-from-2025-00770218130d))

- Overselling outdated or disconnected skills. "Most AI & ML candidates fail interviews not because they lack skills, but because they describe the wrong ones." Demonstrate applied skills that reduce business risk and increase system reliability. ([Fonzi AI](https://medium.com/fonzi-ai/i-reviewed-50-failed-ai-hires-from-2025-00770218130d))

- Misunderstanding role fragmentation. "ML Engineer" has fragmented into distinct career paths: Applied ML, MLOps, LLM Systems, Research Engineering. Understand what you are targeting. ([Amplework](https://www.amplework.com/blog/why-hiring-a-machine-learning-engineer-is-so-hard/))

- Not having projects ready before applying. Some companies require portfolio or GitHub showcase upfront. Have 2-3 polished projects before you start applying. (industry consensus)

- Too little effort on take-homes. "Most engineers put too little effort into take-homes. The best candidates document their decisions, test edge cases, and submit with a Loom video walking through the design." ([Fonzi AI](https://medium.com/fonzi-ai/what-ive-learned-from-sitting-in-on-50-ai-engineer-interviews-c493696453c4))

- Not asking clarifying questions. In both take-home challenges and live interviews: "Asking questions is never a bad thing -- it demonstrates communication skills and prevents costly mistakes." ([Aidi Rivera](https://dev.to/aidiri/learn-from-my-mistakes-my-first-take-home-code-challenge-778))

---

### Interview Format Guide by Company Type

Frontier Labs (OpenAI, Anthropic, Google DeepMind):

- 4-8 week process, 4-7+ rounds
- Coding: practical problems (not puzzle-based at OpenAI), OOP at Anthropic, math-heavy at some
- ML coding: implement Transformers, attention mechanisms, KV cache from scratch
- System design: LLM infrastructure, distributed training, safety considerations
- Research discussions: analyzing papers, presenting your own work
- Behavioral: mission alignment, safety awareness, collaboration in research environments
- Anthropic requires a 90-minute CodeSignal assessment with perfect correctness and conducts rigorous reference checks
- OpenAI: "relentless pursuit of depth" with focus on real-world scenarios
- (Compiled from [Dr. Sundeep Teki](https://www.sundeepteki.org/advice/the-ultimate-ai-research-engineer-interview-guide-cracking-openai-anthropic-google-deepmind-top-ai-labs), [HelloInterview](https://www.hellointerview.com/guides/openai/l5), [OpenAI Loop Interview](https://www.linkjob.ai/interview-questions/openai-loop-interview), [Mimansa Jaiswal](https://mimansajaiswal.github.io/posts/llm-ml-job-interviews-fall-2024-process/))

Big Tech (Meta, Google, Amazon, Apple, Microsoft):

- 1.5-2.5 months typical
- LeetCode-style coding rounds (still present)
- ML system design and LLM research design
- Presentations required across multiple role types
- Behavioral rounds with STAR framework
- Most limit candidates to one interview loop; Microsoft most flexible
- Compensation: $350K-$430K averaged over four years at mid-senior level
- ([Mimansa Jaiswal](https://mimansajaiswal.github.io/posts/llm-ml-job-interviews-fall-2024-process/), [Yuan Meng](https://www.yuan-meng.com/posts/mle_interviews_2.0/))

AI Startups:

- 5-6 rounds: general coding, ML coding, ML fundamentals, culture fit
- Often include take-home assignments (3-day window typical)
- Some require in-person work trials
- Misleading job titles possible -- "research" may mean productization
- Interviews are less standardized; expect wide variation
- ([Mimansa Jaiswal](https://mimansajaiswal.github.io/posts/llm-ml-job-interviews-fall-2024-process/), [Janvi Kalra](https://newsletter.pragmaticengineer.com/p/from-software-engineer-to-ai-engineer))

Newer format: AI-assisted coding interviews:

- Some companies now allow or expect AI coding agents (Claude Code, Cursor) during interviews
- What they evaluate: how you prompt the AI, whether you verify its output, whether you understand what it produces
- Candidates using AI in live interviews often perform worse than those coding independently -- follow-up questions expose lack of understanding. LLM-generated code often contains subtle bugs despite appearing correct ([HN](https://news.ycombinator.com/item?id=42909166))
- "The biggest pitfall: relying on the AI to make decisions for you"
- "It's like we're co-workers, but we're now using AI at the same time. And I want to see how you use AI as a software engineer"
- (interviewer perspective; [Exponent mock interview](https://www.youtube.com/watch?v=example))

---

### Resources & Tools for Preparation

Books and courses:
- [Chip Huyen: AI Engineering (2025)](https://huyenchip.com/books/) - the definitive book on building with foundation models
- ["Understanding Deep Learning" by Simon Prince](https://udlbook.github.io/udlbook/) - for ML fundamentals prep; develop deep conceptual understanding rather than checkbox memorization ([Yuan Meng](https://www.yuan-meng.com/posts/mle_interviews_2.0/))
- ["Designing Data-Intensive Applications"](https://dataintensive.net/) - skim chapters 1-11 for system design prep ([Yuan Meng](https://www.yuan-meng.com/posts/mle_interviews_2.0/))
- [Andrej Karpathy: Neural Networks - Zero to Hero](https://karpathy.ai/zero-to-hero.html) - in-depth courses on neural networks and Transformers

Articles and architecture patterns:
- [Chip Huyen: Building a Generative AI Platform](https://huyenchip.com/2024/07/25/genai-platform.html) - 5-step progression from simple to complex GenAI architecture
- [Eugene Yan: Patterns for Building LLM-based Systems](https://eugeneyan.com/writing/llm-patterns/) - 7 core patterns
- [What We Learned from a Year of Building with LLMs](https://applied-llms.org/) - collective lessons from 6 practitioners

Coding and practice platforms:
- [NeetCode 250](https://neetcode.io/) - recommended by multiple successful candidates. Focus on problem-solving intuition over memorization; use spaced repetition
- [Deep-ML](https://www.deep-ml.com/) - ML-specific coding practice: implementing architectures from scratch
- [Great Frontend](https://www.greatfrontend.com/) - front-end interview questions for full-stack AI engineer roles

System design:
- [Alex Xu: System Design Interview books](https://www.amazon.com/System-Design-Interview-insiders-Second/dp/B08CMF2CQF) - repeatedly study and practice
- [System Design Handbook - GenAI Guide](https://www.systemdesignhandbook.com/guides/generative-ai-system-design-interview/) - 9-step framework with practice prompts
- Company engineering blogs from Netflix, Uber, Pinterest, Snap for ML infra design
- [IGotAnOffer: GenAI System Design Interview](https://igotanoffer.com/en/advice/generative-ai-system-design-interview) - 5-step answer framework from Amazon senior PM

Evals and observability:
- [Maven: AI Evals for Engineers & PMs](https://maven.com/parlance-labs/evals) - Hamel Husain & Shreya Shankar
- Ragas, DeepEval, LLM-as-judge frameworks for practical evaluation

Interview experience write-ups (primary sources):
- [Mimansa Jaiswal: LLM/ML Job Interviews](https://mimansajaiswal.github.io/posts/llm-ml-job-interviews-fall-2024-process/) - process, and [resources](https://mimansajaiswal.github.io/posts/llm-ml-job-interviews-resources/)
- [Yuan Meng: MLE Interview 2.0](https://www.yuan-meng.com/posts/mle_interviews_2.0/) and [ML Infra System Design](https://www.yuan-meng.com/posts/ml_infra_interviews/)
- [Janvi Kalra: From SWE to AI Engineer](https://newsletter.pragmaticengineer.com/p/from-software-engineer-to-ai-engineer)
- [Fonzi AI: What I Learned from 50+ AI Engineer Interviews](https://medium.com/fonzi-ai/what-ive-learned-from-sitting-in-on-50-ai-engineer-interviews-c493696453c4)
- [Dr. Sundeep Teki: AI Research Engineer Interview Guide](https://www.sundeepteki.org/advice/the-ultimate-ai-research-engineer-interview-guide-cracking-openai-anthropic-google-deepmind-top-ai-labs)

Behavioral:
- SAIL structure (Situation, Action, Impact, Learning) -- map stories explicitly to company values
- Prepare distinct examples per interview to avoid sounding mechanical
- GitHub's awesome-behavioral-interviews repository for question lists

Organization tools:
- Notion for tracking preparation across 7+ sections (recommended by Mimansa Jaiswal)
- Zotero and Raindrop for paper and research tracking
- Record yourself explaining projects in 60 seconds to refine storytelling
