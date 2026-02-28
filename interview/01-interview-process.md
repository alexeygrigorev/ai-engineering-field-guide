# Interview Process Analysis: AI Engineering Job Market

Data sources:

- 1500+ AI/ML engineering job descriptions ([job-descriptions/](data/job-descriptions/))
- 100+ reddit discussions ([discussion threads](data/sources/discussion-threads.md))
- 60+ hacker news discussions ([discussion threads](data/sources/discussion-threads.md))
- 50+ twitter posts ([discussion threads](data/sources/discussion-threads.md))
- 35+ personal blogs ([articles](data/sources/articles.md))
- 20 youtube videos ([articles](data/sources/articles.md))
- 700+ urls across 100+ domains ([all links](data/sources/all-links.md))


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

- Doctolib, Senior AI Engineer:
  1. Recruiter interview
  2. Feature building interview
  3. AI system design interview
  4. Behavioral interview
  5. Reference check and offer
- XBOW, AI Research Engineer:
  1. Head of Talent introductory chat (45 min)
  2. Head of AI conversation (60 min)
  3. Technical deep dive / case study (2-3 hours)
  4. CEO and founder meeting (30 min)
- PostHog, AI Product Engineer:
  1. Talent partner call
  2. Technical interview (60 min)
  3. Co-founder call (15 min)
  4. Paid SuperDay (full day of actual work, compensated)
- FlowFuse, Full Stack Developer (AI):
  1. Resume review by hiring manager
  2. Screening call (15 min)
  3. Engineering manager call (45 min)
  4. Take-home assignment (2-3 hours, AI tools encouraged)
  5. Technical review with 2-3 team members (60 min)
  6. Team interview on collaboration and communication (45 min)
  7. Offer
- Phare Health, AI/ML Engineer:
  1. Intro call (background and mission alignment)
  2. Technical deep-dives: pseudo-coding and systems design (explicitly "not Leetcode")
  3. Final in-person interview (travel arranged to SF, NYC, Austin, or Chicago)
  4. References and offer
- P-1 AI (same process across 3 roles):
  1. Initial screening call (30 min)
  2. Biographical/behavioral interview (45 min)
  3. Technical interview (60 min)
  4. CEO interview (30 min)
- Monarch Money, Software Engineer AI:
  1. Recruiter video call
  2. Hiring manager video call
  3. Live coding assessment
  4. Virtual onsite (3 rounds)
  5. Reference checks and offer


## What Candidates Actually Experience

Candidate reports from Reddit, X, and personal blogs confirm our data and add detail on what each round looks like in practice:

| Round | Duration | What people report |
|-------|----------|-------------------|
| Recruiter screen | 15-30 min | Basic fit, salary expectations |
| Technical/coding | 45-60 min | LeetCode-style (often medium/hard), sometimes AI-flavored |
| AI/ML deep-dive | 45-90 min | LLMs, RAG, hallucinations, fine-tuning vs prompting |
| Take-home/project | 1-7 days | Build RAG/agent system, or multi-day assignment |
| System design | 60 min | Scale LLM apps, cost/latency optimization |
| Behavioral | 30-60 min | STAR format, ownership in ambiguous AI work |

Not every company includes all rounds. Total: 3-6 rounds, 2-6 weeks.

ML/DL coding rounds are typically 25-35 minutes with no debugging allowed, covering: neural networks/LSTMs/RNNs from scratch in NumPy/PyTorch, attention mechanism variants (cached, grouped query, multi-head), transformer components, and RAG/inference implementations (embedding models, decoding strategies like top-p, top-k, beam search). [^mimansa-jaiswal-resources]

### Company-specific experiences

Model companies (building the intelligence):

- OpenAI [^exponent-openai] [^linkjob-openai] (2026):
  - 5-week process
  - Coding has 4 progressive gates (bar: clear 2 of 4)
  - Includes a refactoring round -- 100-120 lines of convoluted code to refactor for maintainability while keeping tests green
  - System design directly tied to the role (e.g., design the OpenAI Playground)
  - Behavioral digs deep into one conflict scenario
  - AI tools allowed during coding
- OpenAI L5/Staff [^hello-interview]:
  - 6-8 rounds spanning 8-12 weeks (can stretch to 4+ months)
  - Recruiter/HM intro (30 min) -> coding screen (60 min, CoderPad) -> architecture/system design screen -> onsite loop
  - Onsite: coding, system design, technical project presentation (45 min, mandatory at staff level), behavioral-leadership (45 min), behavioral-collaboration (30 min), optional domain-specific round (60 min)
  - Coding is practical rather than pure LeetCode: time-indexed data handling, iterators with state, caching mechanisms
  - Common system design: Design GitHub Actions, Design Slack, Design Online Chess
  - Staff candidates can use their own IDE with screen sharing
- Anthropic [^linkjob-anthropic] [^mimansa-jaiswal]:
  - 30-min recruiter, 90-min progressive coding challenge (4-level KV database), 1-hour HM call
  - 4-hour virtual onsite (4 rounds): distributed systems design (billion documents, 10K+ LLM inference RPS), hybrid search (<50ms)
  - Jaiswal reports 7 virtual onsite rounds: 3 OOP coding + LLM coding + fundamentals + culture fit
- xAI [^reddit-xai-eng] [^devto-xai] (Jan 2026):
  - 15-min phone screen + 3 onsite rounds (2 algorithm, 1 system design)
  - Two medium LeetCode problems (word search on grid, LRU cache)
  - System design: in-memory database with nested transactions
- DeepMind Gemini Team [^reddit-deepmind-gemini]:
  - System design for LLMs (training, serving, inference optimization)
  - Scalable ML architectures (RAG, fine-tuning pipelines, mobile inference)
  - Prepare distributed training concepts (ZeRO-1/3, Megatron, tensor parallelism)
  - Google offers mock interviews through recruiters
- Scale AI [^mimansa-jaiswal]:
  - 3 professional rounds, no LeetCode
  - Reference materials permitted during interviews

Big Tech:

- Microsoft Senior Engineer [^rohit-verma-microsoft] (2026):
  - ~5 weeks total, 4 rounds (HLD+LLD, HLD, DSA, behavioral)
  - HLD round: designing a Ghibli image generator (GPU inference, cost throttling, prompt injection defense)
  - DSA round was 1 hour of pure discussion (no code written)
- Microsoft SWE Applied AI/ML Intern [^reddit-microsoft-aiml]:
  - 3 rounds of 45 min each
  - Round 1: entirely AI-assisted coding (use ChatGPT to solve problems, interviewer modifies problem and asks to re-prompt)
  - Round 2: no AI tools allowed (testing raw coding ability)
  - Round 3: behavioral/technical discussion
- Amazon GenAI Innovation Center L6 [^reddit-amazon-genai]:
  - No dedicated MLE job family -- MLEs must pass the standard SDE technical bar (DSA coding)
  - Phone screen: LeetCode problem + practical ML coding question (cosine similarity in NumPy)
  - GenAI teams focus on LLM/ViT/DiT architectures, fine-tuning, use case ideation, ROI estimation
  - Leadership Principles (LP) behavioral questions throughout
- Google SWE AI/ML L4 [^reddit-google-aiml]:
  - Onsite ML round: either ML fundamentals (bias-variance, regularization, model architecture) or ML system design (data pipeline, feature engineering, model selection, evaluation)
  - ML system design more common at L4
  - Googleyness round: collaboration, adaptability, intellectual humility
- Big Tech general (Meta, Amazon, Apple, Google) [^mimansa-jaiswal]:
  - 1.5-2.5 months timeline
  - LeetCode coding, ML system design, LLM research design, presentations, behavioral
  - Most limit to one interview loop
  - $350K-$430K comp range averaged over 4 years
- IBM Watsonx [^raghu-teja-1] (Jan 2025):
  - 3 rounds after recruiter screen
  - Round 1: technical interview (1 hr 15 min) covering Python, SQL, Git, project deep-dives, ML/MLOps
  - Round 2: live coding (45 min) on shared whiteboard, 3 questions (easy to medium)
  - ~2 months between application and recruiter screen

AI-first companies and startups:

- Eightfold.ai [^eightfold-medium] [^reddit-eightfold-ai] (Jan 2026):
  - AI agent conducted Round 1 -- ~60 min, 2 coding questions with interactive follow-ups (edge cases, complexity analysis, alternative approaches)
  - 3-day assignment to build an AI agent
  - DSA-focused technical interview with engineering manager
- LangChain [^reddit-ai-eng-questions]:
  - Take-home assessment (develop an agent)
  - Discussion of the solution
  - Applied system design interview
- BCG X AI Engineer Intern [^reddit-bcgx-intern]:
  - Starts with CodeSignal GCA -- near-perfect score (600/600) expected to advance

### Interview landscape across 46 AI companies

Janvi Kalra [^janvi-kalra] (software engineer turned AI engineer, now at OpenAI) interviewed at 46 AI companies over a six-month period and shares structural observations:

- AI companies fall into three categories that affect interview focus: product companies (building on top of models -- Cursor, Codium, Hebbia), infrastructure companies (tools for AI product companies -- Modal, Fireworks, Together, Pinecone, Braintrust), and model companies (building the intelligence -- OpenAI, Anthropic, Google, Meta). Categorizing target companies helps narrow the search
- Interview formats are "all over the place" -- the market is trying to move away from LeetCode but still asks it, so candidates must prepare for it unless they know exactly where they're applying
- Three interview types dominate: coding (DSA/LeetCode, best prep via NeetCode), system design (Alex Xu's two books recommended), and project interviews ("go build something in a day" -- her favorite, lets you show passion for the product)
- The first half of her six-month search produced rejections while ramping up on LeetCode and system design prep; offers came in the second half
- In-person final rounds are starting to come back, at least for some companies
- Code reading and debugging are becoming more important in interviews alongside writing code

### Interview types vary by AI role

Based on 50+ interview rounds across 20+ companies, Deepthi Sudharsan [^deepthi-sudharsan] identifies these patterns:

- AI Research: resume-based round, paper peer-review round, DSA, ML fundamentals, behavioral
- AI Research Engineer: similar to research but heavier DSA emphasis + may reproduce a paper
- AI Engineer / Applied Scientist: distinct DSA and ML coding rounds, ML system design, deep ML fundamentals with math derivations
- Data Scientist: DBMS/SQL in OA, more emphasis on core ML than GenAI, take-home assignments testing ML coding
- AI PM: write PRDs for AI products, feature prioritization, roadmap building

"The interviewer doesn't just want to know how your LLM behaves if the temperature is shifted to 0 or 1, but rather how the softmax function is affected and what exactly happens to the probability distribution"

### Senior-level landscape (14+ YOE, 40 interviews)

A principal engineer who completed ~40 interviews across startups, mid-size companies, and big tech [^reddit-2026-prep] reports:

- ~70% of interviews had no LeetCode at all. NVIDIA and Anthropic had zero. When coding came up, it was practical: string manipulation, heaps, real-world logic. "I barely saw hard DP or tricky puzzle questions"
- Low-level design and concurrency came up almost everywhere. Async, correctness under load, race conditions. Anthropic was "almost entirely concurrent LLD, HLD, and coding"
- System design was a huge part of most loops, but not classic "design Dropbox" style. Most design questions were around AI/LLM integrations: scaling AI systems, latency/cost trade-offs, batching, caching, streaming, failure modes
- Many companies asked candidates to present a "proud" project to a panel, then went deep on design decisions, trade-offs, what broke, what they'd change. Common at senior+ roles
- To prepare for LLM integration questions: "You should be able to say you've deployed a working RAG pipeline, even if it's just a side project. You should be comfortable owning the full deployment -- running models locally or in the cloud, Kubernetes with GPU scheduling, batching, KV cache, streaming, latency versus cost trade-offs"

### Emerging interview formats

Several new approaches are gaining traction, reported across multiple Hacker News threads:

- Code review rounds: Candidates evaluate provided code for bugs, performance issues, and design problems rather than writing code from scratch. Tests engineering judgment -- "what they call out vs. what they don't waste time on" -- which is harder to fake with AI [^hn-40363135] [^hn-42977039] [^hn-43108673]
- Evaluating AI-generated code: Candidates retrieve a solution from an LLM, then review that solution during the interview. Shifts evaluation from code production to judgment and analysis [^hn-42268158] [^hn-42977039]
- "AI delta" assessment: Candidates tackle real GitHub issues in 2-4 hours while evaluators assess what they add beyond what AI generates -- exploration strategy, engineering rigor, edge case handling, documentation quality [^hn-46865130]
- Pair programming on real problems: 1-2 hours on production code provides stronger signal than algorithmic puzzles [^hn-43108673]
- Candidates using AI in live interviews often perform worse: Follow-up questions expose lack of understanding. LLM-generated code often contains subtle bugs that the candidate cannot explain [^hn-42909166]
- Anti-cheating tooling: Tools like BlindSpots use adversarial examples (invisible pixel and audio modifications) to disrupt AI screenshot-based and audio-based cheating tools without invasive surveillance [^hn-45492686]

See also [AI System Design](05-ai-system-design.md) for detailed interview experiences at Anthropic, OpenAI, and others.

See [Interview Trends](10-trends.md) for AI use in hiring, realistic assessments, AI cheating, AI-proctored rounds, and published AI guidelines.


[^exponent-openai]: [Exponent - OpenAI Interview 2026](https://medium.com/exponent/what-its-actually-like-to-interview-at-openai-in-2026-03a646c9436c)
[^linkjob-openai]: [linkjob - OpenAI](https://www.linkjob.ai/interview-questions/openai-loop-interview)
[^hello-interview]: [Hello Interview - OpenAI L5](https://www.hellointerview.com/guides/openai/l5)
[^linkjob-anthropic]: [linkjob - Anthropic](https://www.linkjob.ai/interview-questions/anthropic-software-engineer-interview/)
[^mimansa-jaiswal]: [Mimansa Jaiswal](https://mimansajaiswal.github.io/posts/llm-ml-job-interviews-fall-2024-process/)
[^reddit-xai-eng]: [Reddit - xAI AI Engineer Backend/Infra Interview](https://www.reddit.com/r/leetcode/comments/1pjhw1i/xai_ai_engineer_backendinfra_interview_just/) (r/leetcode)
[^devto-xai]: [dev.to - xAI Software Engineer Interview 2026](https://dev.to/net_programhelp_e160eef28/xai-software-engineer-interview-2026-full-recap-pitfalls-real-prep-tips-2fl0)
[^reddit-deepmind-gemini]: [Reddit - Preparing for DeepMind Gemini Team Interview](https://www.reddit.com/r/MachineLearning/comments/1k8gy12/d_preparing_for_a_deepmind_gemini_team_interview/) (r/MachineLearning)
[^rohit-verma-microsoft]: [Medium - Rohit Verma, Microsoft Senior Engineer Interview 2026](https://medium.com/@rohitverma_87831/microsoft-senior-engineer-interview-experience-2026-the-offer-that-took-me-three-attempts-e0d6e052bdb1)
[^reddit-microsoft-aiml]: [Reddit - Microsoft SWE Applied AI/ML Summer 2026](https://www.reddit.com/r/csMajors/comments/1nqfzhq/microsoft_swe_applied_aiml_summer_2026_redmond) (r/csMajors)
[^reddit-amazon-genai]: [Reddit - ML Engineer GenAI Amazon](https://www.reddit.com/r/datascience/comments/1jrdrpx/ml_engineer_genai_amazon/) (r/datascience)
[^reddit-google-aiml]: [Reddit - Google SWE AI/ML Interview](https://www.reddit.com/r/leetcode/comments/1kb3gmi/google_swe_aiml_interview_onsite_interview_what/) (r/leetcode)
[^raghu-teja-1]: [Medium - Raghu Teja, IBM Part 1](https://medium.com/@raghu_teja/how-i-cracked-my-ibm-ai-engineer-interview-part-1-technical-e7e4f73be5c4)
[^eightfold-medium]: [Medium - Inside Eightfold.ai Agentic AI Internship Hiring 2026](https://medium.com/@bhardwajtushar2004/inside-eightfold-ais-agentic-ai-internship-hiring-process-2026-f86dcb625aa8)
[^reddit-eightfold-ai]: [Reddit - Need Advice for Eightfold.ai Agentic AI Engineer](https://www.reddit.com/r/developersIndia/comments/1pbaj11/need_advice_for_eightfoldai_agentic_ai_engineer) (r/developersIndia)
[^reddit-ai-eng-questions]: [Reddit - AI Engineer Interview Questions](https://www.reddit.com/r/ArtificialInteligence/comments/1nybfr8/ai_engineer_interview_questions/) (r/ArtificialIntelligence)
[^reddit-bcgx-intern]: [Reddit - BCG X AI Engineer Intern Summer 2026](https://www.reddit.com/r/csMajors/comments/1pp9jht/bcg_x_ai_engineer_intern_summer_2026_interview) (r/csMajors)
[^janvi-kalra]: [Janvi Kalra - From Software Engineer to AI Engineer](https://newsletter.pragmaticengineer.com/p/from-software-engineer-to-ai-engineer)
[^deepthi-sudharsan]: [Medium - Deepthi Sudharsan, Inside AI Interviews](https://medium.com/@deepthi.sudharsan/inside-ai-interviews-stories-patterns-and-what-actually-matters-555684c38598)
[^reddit-2026-prep]: [Reddit - 2026 Interview Prep](https://www.reddit.com/r/leetcode/comments/1q06zz6/2026_interview_prep) (r/leetcode)
[^hn-40363135]: [HN - Code Review Interviews](https://news.ycombinator.com/item?id=40363135)
[^hn-42977039]: [HN - Interviewing in the AI Era](https://news.ycombinator.com/item?id=42977039)
[^hn-43108673]: [HN - Pair Programming Over LeetCode](https://news.ycombinator.com/item?id=43108673)
[^hn-42268158]: [HN - Technical Interviews in the LLM Era](https://news.ycombinator.com/item?id=42268158)
[^hn-46865130]: [HN - AI Delta Assessment](https://news.ycombinator.com/item?id=46865130)
[^hn-42909166]: [HN - AI Cheating in Interviews](https://news.ycombinator.com/item?id=42909166)
[^hn-45492686]: [HN - BlindSpots Anti-Cheating](https://news.ycombinator.com/item?id=45492686)
[^mimansa-jaiswal-resources]: [Mimansa Jaiswal - Resources](https://mimansajaiswal.github.io/posts/llm-ml-job-interviews-resources/)
