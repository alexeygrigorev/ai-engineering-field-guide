# Interview Process Analysis: AI Engineering Job Market

## Summary Statistics

Out of 1,765 job descriptions analyzed, only ~80 (~4.5%) include a structured interview process across 51 unique companies. The vast majority either omit the process entirely.

Individual interview process descriptions for each of the 51 companies are in [data/job-descriptions/](data/job-descriptions/). Each file links to the source job description YAML.

## Interview Process

The median process has 4 steps, with most companies falling in the 3-5 range. A few lean processes have just 2 stages (Lorikeet, Infinity Constellation, Watershed), while the longest reach 7 stages (FlowFuse, Roboflow, The College Board). 

Most frequently mentioned steps:

1. Recruiter/talent screen - Usually 15-30 min
2. Technical interview - Live coding, system design, or code review
3. Hiring manager interview - 45-60 min deep dive
4. Take-home challenge - Typically 2-3 hours
5. Behavioral interview - Interview about values and culture
6. CEO/founder interview - Usually final step, 15-30 min
7. Panel interview - Multiple interviewers

Examples from job postings ([data/job-descriptions/](data/job-descriptions/)):

Doctolib, Senior AI Engineer:

1. Recruiter interview
2. Feature building interview
3. AI system design interview
4. Behavioral interview
5. Reference check and offer

PostHog, AI Product Engineer:

1. Talent partner call
2. Technical interview (60 min)
3. Co-founder call (15 min)
4. Paid SuperDay (full day of actual work, compensated)

FlowFuse, Full Stack Developer (AI):

1. Resume review by hiring manager
2. Screening call (15 min)
3. Engineering manager call (45 min)
4. Take-home assignment (2-3 hours, AI tools encouraged)
5. Technical review with 2-3 team members (60 min)
6. Team interview on collaboration and communication (45 min)



## What Candidates Actually Experience

Candidate reports from Reddit, X, and personal blogs confirm our data and add detail on what each round looks like in practice:

| Round | Duration | What people report |
|-------|----------|-------------------|
| Recruiter screen | 15-30 min | Basic fit, salary expectations |
| Technical/coding | 45-60 min | LeetCode-style, sometimes AI-flavored |
| AI/ML deep-dive | 45-90 min | LLMs, RAG, hallucinations, fine-tuning vs prompting |
| Take-home/project | 1-7 days | Build RAG/agent system, or multi-day assignment |
| System design | 60 min | Scale LLM apps, cost/latency optimization |
| Behavioral | 30-60 min | STAR format, ownership in ambiguous AI work |

Not every company includes all rounds. Total: 3-6 rounds, 2-6 weeks.

Microsoft, SWE Applied AI/ML Intern [^reddit-microsoft-aiml]:

1. AI-assisted coding (45 min) - use ChatGPT to solve problems, interviewer modifies problem and asks to re-prompt
2. Raw coding, no AI tools allowed (45 min)
3. Behavioral/technical discussion (45 min)

Amazon, GenAI Innovation Center L6 [^reddit-amazon-genai]:

1. Phone screen: LeetCode problem + practical ML coding question (cosine similarity in NumPy)
2. Standard SDE technical bar (DSA coding) - no dedicated MLE job family
3. GenAI depth: LLM/ViT/DiT architectures, fine-tuning, use case ideation, ROI estimation
4. Leadership Principles (LP) behavioral questions throughout

Eightfold.ai, Agentic AI Engineer [^eightfold-medium] [^reddit-eightfold-ai] (Jan 2026):

1. AI agent-conducted coding round (~60 min) - 2 questions with interactive follow-ups on edge cases and complexity
2. Take-home: 3-day assignment to build an AI agent
3. DSA-focused technical interview with engineering manager

LangChain, AI Engineer [^reddit-ai-eng-questions]:

1. Take-home assessment (develop an agent)
2. Discussion of the solution
3. Applied system design interview

IBM, AI Engineer (Watsonx) [^raghu-teja-1] (Jan 2025):

1. Recruiter screen (applied via LinkedIn, ~2 months wait)
2. Technical interview (75 min) - Python, SQL, Git, project deep-dives, ML/MLOps
3. Live coding (45 min) - shared whiteboard, 3 questions (easy to medium)

Mistral AI, Applied AI Engineer [^glassdoor-mistral] (Jan 2026):

1. LLM theory
2. Coding
3. Past project deep-dive
4. Technical manager interview
5. ML system design
6. Take-home assignment
7. Value talk

Databricks, AI/ML Engineer [^yuan-meng] (late 2025):

1. Coding (LeetCode-style)
2. Multi-level OOP (scale toy systems like DB/KV store/chat room)
3. ML infra design (feature stores, distributed training, serving)
4. Pre-offer reference checks (2-3 refs required)

Goldman Sachs, Applied AI Engineer [^reddit-gs-applied-ai] (Dec 2025):

1. Technical interview for GenAI/applied AI role
2. Focus on LLM system design and production deployment

AI Engineer Intern [^x-aryyann8] (Jan 2026):

1. Deep dive on resume projects
2. QLoRA fine-tuning
3. RAG architecture and latency optimization
4. Temperature and sampling strategies
5. Agentic AI system design
6. Feature scaling and ML situational cases

GenAI Engineer, product company [^reddit-genai-product] (2025):

1. Technical interview focused on GenAI engineering
2. LLM system design, RAG tradeoffs, evaluation metrics beyond perplexity


### Patterns from practitioners

Based on 130+ interview rounds reported by Janvi Kalra (46 companies) [^janvi-kalra], Deepthi Sudharsan (50+ rounds) [^deepthi-sudharsan], and a principal engineer with 14+ YOE (~40 interviews) [^reddit-2026-prep]:

- LeetCode is declining but not dead. ~70% of senior interviews had none at all. When coding comes up, it's practical (string manipulation, real-world logic), not puzzle-based [^reddit-2026-prep] [^janvi-kalra]
- Three interview types dominate: coding (DSA/LeetCode), system design, and project interviews ("go build something in a day") [^janvi-kalra]
- System design shifted from "design Dropbox" to AI/LLM integrations: scaling AI systems, latency/cost trade-offs, batching, caching, streaming, failure modes. See [AI System Design](05-ai-system-design.md) for details [^reddit-2026-prep]
- Project presentations are common: candidates present a past project, then get grilled on design decisions, trade-offs, what broke, what they'd change [^reddit-2026-prep] [^janvi-kalra]
- Code reading and debugging are becoming more important alongside writing code [^janvi-kalra]
- In-person final rounds are coming back [^janvi-kalra]
- AI companies cluster into three types that affect interview focus: product companies (Cursor, Codium, Hebbia), infrastructure companies (Modal, Fireworks, Pinecone), and model companies (OpenAI, Anthropic, Google, Meta) [^janvi-kalra]
- Interview focus varies by AI role: AI Engineers get distinct DSA and ML coding rounds plus ML system design; AI Researchers get paper peer-review rounds; Data Scientists get more SQL and core ML than GenAI [^deepthi-sudharsan]



[^reddit-microsoft-aiml]: [Reddit - Microsoft SWE Applied AI/ML Summer 2026](https://www.reddit.com/r/csMajors/comments/1nqfzhq/microsoft_swe_applied_aiml_summer_2026_redmond) (r/csMajors)
[^reddit-amazon-genai]: [Reddit - ML Engineer GenAI Amazon](https://www.reddit.com/r/datascience/comments/1jrdrpx/ml_engineer_genai_amazon/) (r/datascience)
[^raghu-teja-1]: [Medium - Raghu Teja, IBM Part 1](https://medium.com/@raghu_teja/how-i-cracked-my-ibm-ai-engineer-interview-part-1-technical-e7e4f73be5c4)
[^eightfold-medium]: [Medium - Inside Eightfold.ai Agentic AI Internship Hiring 2026](https://medium.com/@bhardwajtushar2004/inside-eightfold-ais-agentic-ai-internship-hiring-process-2026-f86dcb625aa8)
[^reddit-eightfold-ai]: [Reddit - Need Advice for Eightfold.ai Agentic AI Engineer](https://www.reddit.com/r/developersIndia/comments/1pbaj11/need_advice_for_eightfoldai_agentic_ai_engineer) (r/developersIndia)
[^reddit-ai-eng-questions]: [Reddit - AI Engineer Interview Questions](https://www.reddit.com/r/ArtificialInteligence/comments/1nybfr8/ai_engineer_interview_questions/) (r/ArtificialIntelligence)
[^janvi-kalra]: [Janvi Kalra - From Software Engineer to AI Engineer](https://newsletter.pragmaticengineer.com/p/from-software-engineer-to-ai-engineer)
[^deepthi-sudharsan]: [Medium - Deepthi Sudharsan, Inside AI Interviews](https://medium.com/@deepthi.sudharsan/inside-ai-interviews-stories-patterns-and-what-actually-matters-555684c38598)
[^reddit-2026-prep]: [Reddit - 2026 Interview Prep](https://www.reddit.com/r/leetcode/comments/1q06zz6/2026_interview_prep) (r/leetcode)
[^glassdoor-mistral]: [Glassdoor - Mistral AI Applied AI Engineer Interviews](https://www.glassdoor.com/Interview/Mistral-AI-Applied-AI-Engineer-Interview-Questions-EI_IE9945031.0,10_KO11,30.htm)
[^yuan-meng]: [Yuan Meng - MLE Interviews 2.0](https://www.yuan-meng.com/posts/mle_interviews_2.0/)
[^reddit-gs-applied-ai]: [Reddit - Applied AI Engineer Goldman Sachs Interview](https://www.reddit.com/r/leetcode/comments/1pexaw3/applied_ai_engineer_goldman_sachs_interview) (r/leetcode)
[^x-aryyann8]: [X - AI Engineer Intern Interview](https://x.com/aryyann8/status/2009314129878896960)
[^reddit-genai-product]: [Reddit - Technical Interview for GenAI Engineer Role](https://www.reddit.com/r/leetcode/comments/1rd6yki/technical_interview_for_genai_engineer_role_for_a) (r/leetcode)
