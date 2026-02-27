# Interview Process Analysis: AI Engineering Job Market

Analysis of 1,765 AI/ML engineering job descriptions to extract and summarize hiring/interview process information.

## Summary Statistics

Out of 1,765 job descriptions analyzed, only ~80 (~4.5%) include a structured interview process across 51 unique companies. The vast majority either omit the process entirely.

Individual interview process descriptions for each of the 51 companies are in [data/](data/). Each file links to the source job description YAML.

## Interview Process

The median process has 4 steps, with most companies falling in the 3-5 range. A few lean processes have just 2 stages (Lorikeet, Infinity Constellation, Watershed), while the longest reach 7 stages (FlowFuse, Roboflow, The College Board). 

Most frequent steps:

1. Recruiter/talent screen (~78%) - Usually 15-30 min
2. Technical interview (~75%) - Live coding, system design, or code review
3. Hiring manager interview (~65%) - 45-60 min deep dive
4. Take-home challenge (~33%) - Typically 2-3 hours
5. Values/culture interview (~25%) - Separate from technical
6. CEO/founder interview (~24%) - Usually final step, 15-30 min
7. Panel interview (~20%) - Multiple interviewers
8. Reference check (~20%) - Before offer


AI system design

- Some companies include this interview round
- Doctolib has a dedicated "AI System Design Interview."
- Sprinter Health has "AI-Focused Systems Design."
- See [AI System Design](05-ai-system-design.md) for more


Take-home challenges

- 33% use take-home assignments
- 5 companies (10%) use paid work trials
- See the dedicated [report](06-home-assignments.md) for full analysis



## What Candidates Actually Experience

Candidate reports from Reddit, X, and personal blogs confirm our data and add detail on what each round looks like in practice (see [AI Interview Experiences](../awesome.md#ai-interview-experiences) for sources):

| Round | Duration | What people report |
|-------|----------|-------------------|
| Recruiter screen | 15-30 min | Basic fit, salary expectations |
| Technical/coding | 45-60 min | LeetCode-style (often medium/hard), sometimes AI-flavored |
| AI/ML deep-dive | 45-90 min | LLMs, RAG, hallucinations, fine-tuning vs prompting |
| Take-home/project | 1-7 days | Build RAG/agent system, or multi-day assignment |
| System design | 60 min | Scale LLM apps, cost/latency optimization |
| Behavioral | 30-60 min | STAR format, ownership in ambiguous AI work |

Not every company includes all rounds. Total: 3-6 rounds, 2-6 weeks.

ML/DL coding rounds are typically 25-35 minutes with no debugging allowed, covering: neural networks/LSTMs/RNNs from scratch in NumPy/PyTorch, attention mechanism variants (cached, grouped query, multi-head), transformer components, and RAG/inference implementations (embedding models, decoding strategies like top-p, top-k, beam search). ([Mimansa Jaiswal](https://mimansajaiswal.github.io/posts/llm-ml-job-interviews-resources/))

### Company-specific experiences

- **xAI** ([Reddit r/leetcode](https://www.reddit.com/r/leetcode/comments/1pjhw1i/xai_ai_engineer_backendinfra_interview_just/), [dev.to recap](https://dev.to/net_programhelp_e160eef28/xai-software-engineer-interview-2026-full-recap-pitfalls-real-prep-tips-2fl0), Jan 2026): 15-min phone screen + 3 onsite rounds (2 algorithm, 1 system design). Two medium LeetCode problems (word search on grid, LRU cache). System design: in-memory database with nested transactions. "Everything felt practical with no weird tricks"
- **Microsoft** ([Medium](https://medium.com/@rohitverma_87831/microsoft-senior-engineer-interview-experience-2026-the-offer-that-took-me-three-attempts-e0d6e052bdb1), 2026): ~5 weeks total, 4 rounds (HLD+LLD, HLD, DSA, behavioral). HLD round included designing a Ghibli image generator (GPU inference, cost throttling, prompt injection defense). DSA round was 1 hour of pure discussion (no code written). "Senior coding rounds are not about typing speed. They are about engineering depth"
- **Eightfold.ai** ([Medium](https://medium.com/@bhardwajtushar2004/inside-eightfold-ais-agentic-ai-internship-hiring-process-2026-f86dcb625aa8), [Reddit r/developersIndia](https://www.reddit.com/r/developersIndia/comments/1pbaj11/need_advice_for_eightfoldai_agentic_ai_engineer), Jan 2026): AI agent conducted Round 1 - ~60 min, 2 coding questions with interactive follow-ups (edge cases, complexity analysis, alternative approaches). Followed by a 3-day assignment to build an AI agent, then DSA-focused technical interview with engineering manager
- **OpenAI** ([Exponent](https://medium.com/exponent/what-its-actually-like-to-interview-at-openai-in-2026-03a646c9436c), [linkjob.ai](https://www.linkjob.ai/interview-questions/openai-loop-interview), 2026): 5-week process. Coding has 4 progressive gates (bar: clear 2 of 4). Includes a refactoring round - 100-120 lines of convoluted code to refactor for maintainability while keeping tests green. System design directly tied to the role (e.g., design the OpenAI Playground). Behavioral digs deep into one conflict scenario. AI tools allowed during coding. "One of the more interesting interview processes out there"
- **Anthropic** ([linkjob.ai](https://www.linkjob.ai/interview-questions/anthropic-software-engineer-interview/), [Mimansa Jaiswal](https://mimansajaiswal.github.io/posts/llm-ml-job-interviews-fall-2024-process/)): 30-min recruiter, 90-min progressive coding challenge (4-level KV database), 1-hour HM call, 4-hour virtual onsite (4 rounds). Onsite includes distributed systems design (billion documents, 10K+ LLM inference RPS) and hybrid search (<50ms). Jaiswal reports 7 virtual onsite rounds with 3 OOP coding rounds + LLM coding + fundamentals + culture fit
- **Scale AI** ([Mimansa Jaiswal](https://mimansajaiswal.github.io/posts/llm-ml-job-interviews-fall-2024-process/)): 3 professional rounds, no LeetCode, reference materials permitted during interviews
- **Big Tech (Meta, Amazon, Apple, Google)** ([Mimansa Jaiswal](https://mimansajaiswal.github.io/posts/llm-ml-job-interviews-fall-2024-process/)): 1.5-2.5 months timeline. Components: LeetCode coding, ML system design, LLM research design, presentations, behavioral. Most limit to one interview loop. $350K-$430K comp range averaged over 4 years
- **OpenAI L5/Staff** ([Hello Interview guide](https://www.hellointerview.com/guides/openai/l5)): 6-8 total rounds spanning 8-12 weeks (can stretch to 4+ months due to staff-level calibration). Structure: recruiter/HM intro (30 min) -> coding screen (60 min, CoderPad, 1-2 practical problems) -> architecture/system design screen -> onsite loop with coding, system design, technical project presentation (45 min, mandatory at staff level), behavioral-leadership (45 min, with senior manager/exec), behavioral-collaboration (30 min), and optional domain-specific round (60 min for ML infra, distributed systems, or AI safety roles). Coding problems are practical rather than pure LeetCode -- time-indexed data handling, iterators with state, caching mechanisms. Common coding questions: KV Store serialize/deserialize, in-memory SQL-like database, time-based key-value store. Common system design: Design GitHub Actions, Design Slack, Design Online Chess. No-reference policy during coding rounds. Staff candidates can use their own IDE with screen sharing during onsite coding
- **IBM Watsonx** ([Raghu Teja Manchala, Medium](https://medium.com/@raghutejamanchala), Jan 2025): 3 rounds total after recruiter screen. Round 1: Technical interview (1 hr 15 min) with Head of Watson Assistant Development and a Master Inventor -- covers Python (memory leaks, class/static methods, MRO, debugging in production), SQL (query optimization, execution order), Git (branching strategies, rebasing, conflict resolution), project deep-dives, ML/MLOps (CI/CD deployment workflow, quantization, imbalanced data, RNN vs LSTM). Round 2: Live coding (45 min) on a shared whiteboard -- 3 questions (easy to medium), 30 min to explain logic and code. Applied via LinkedIn, ~2 months between application and recruiter screen
- **Gen AI Engineer (unnamed company)** ([Khushal Kumar, Medium](https://medium.com/@khushal.kumar), Oct 2024): 3 rounds + speed test. Take-home assignment first (build AI project parsing blood test PDFs with RAG, submit within a few hours -- testing speed with new frameworks). DSA round with easy questions (primes, anagrams) plus technology questions (Docker, Selenium, Redis) and LLM/RAG concepts (embeddings, chunking). Managerial round discussing the assignment and prior experience. Speed coding test: 30 min to parse a complex JSON file and feed extracted data to an AI model for summarization -- browser and ChatGPT allowed. "If you correctly answer 80% of the questions, you're good"

### Interview landscape across 46 AI companies

[Janvi Kalra](https://newsletter.pragmaticengineer.com/p/from-software-engineer-to-ai-engineer) (software engineer turned AI engineer, now at OpenAI) interviewed at 46 AI companies over a six-month period and shares structural observations:

- AI companies fall into three categories that affect interview focus: **product companies** (building on top of models -- Cursor, Codium, Hebbia), **infrastructure companies** (tools for AI product companies -- Modal, Fireworks, Together, Pinecone, Braintrust), and **model companies** (building the intelligence -- OpenAI, Anthropic, Google, Meta). Categorizing target companies helps narrow the search
- Interview formats are "all over the place" -- the market is trying to move away from LeetCode but still asks it, so candidates must prepare for it unless they know exactly where they're applying
- Three interview types dominate: **coding** (DSA/LeetCode, best prep via NeetCode), **system design** (Alex Xu's two books recommended), and **project interviews** ("go build something in a day" -- her favorite, lets you show passion for the product)
- The first half of her six-month search produced rejections while ramping up on LeetCode and system design prep; offers came in the second half
- In-person final rounds are starting to come back, at least for some companies
- Code reading and debugging are becoming more important in interviews alongside writing code

### Interview types vary by AI role

Based on 50+ interview rounds across 20+ companies, [Deepthi Sudharsan](https://medium.com/@deepthi.sudharsan/inside-ai-interviews-stories-patterns-and-what-actually-matters-555684c38598) identifies these patterns:

- **AI Research**: resume-based round, paper peer-review round, DSA, ML fundamentals, behavioral
- **AI Research Engineer**: similar to research but heavier DSA emphasis + may reproduce a paper
- **AI Engineer / Applied Scientist**: distinct DSA and ML coding rounds, ML system design, deep ML fundamentals with math derivations
- **Data Scientist**: DBMS/SQL in OA, more emphasis on core ML than GenAI, take-home assignments testing ML coding
- **AI PM**: write PRDs for AI products, feature prioritization, roadmap building

"The interviewer doesn't just want to know how your LLM behaves if the temperature is shifted to 0 or 1, but rather how the softmax function is affected and what exactly happens to the probability distribution"

See also [AI System Design](05-ai-system-design.md) for detailed interview experiences at Anthropic, OpenAI, and others.


See [Interview Trends](10-trends.md) for AI use in hiring, realistic assessments, AI cheating, AI-proctored rounds, and published AI guidelines.
