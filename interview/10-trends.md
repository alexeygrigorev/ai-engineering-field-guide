# Interview Trends (2026)

Emerging patterns in AI engineering interviews based on candidate experiences, job descriptions, and industry discussions.

See also: [Awesome AI Engineering](../awesome.md) for the full collection of sources.


## Market Data (2025)

- 62,000 tech layoffs in 2025 (including 9,000 at Microsoft), but layoffs became strategic restructuring rather than survival measures - companies now prioritize AI-fluent talent ([InterviewQuery](https://www.interviewquery.com/p/ai-interview-trends-tech-hiring-2025))
- Tech job openings stabilized around 230,000 (up 22% from 2024 lows). Companies like Amazon and Apple hired more than they laid off ([InterviewQuery](https://www.interviewquery.com/p/ai-interview-trends-tech-hiring-2025))
- AI-native roles (AI Engineer, ML Engineer, Analytics Engineer) surged 240% in early 2025 ([InterviewQuery](https://www.interviewquery.com/p/ai-interview-trends-tech-hiring-2025))
- AI and LLM-related interview questions tripled since 2023 ([InterviewQuery](https://www.interviewquery.com/p/ai-interview-trends-tech-hiring-2025))
- AI/LLM mentions in job postings increased across all roles: ML Engineers 8% to 29.5%, Data Scientists 4% to 18.4%, Analysts & BI 3.8% to 15.8%, Backend Engineers 6.7% to 13%, Data Engineers 3% to 9.7% ([InterviewQuery](https://www.interviewquery.com/p/ai-interview-trends-tech-hiring-2025))


## "No Whiteboard" - Realistic Assessments

A growing number of companies explicitly reject algorithm-heavy interviews in favor of realistic work:

- Clarium: "no abstract puzzles," info sent in advance
- Column Tax: "not code golf," interviews mimic real work
- Phare Health: "not Leetcode"
- Doctolib: "Feature Building Interview" tests practical building, not algorithms
- Glass Health: realistic work simulation
- TensorOps: no live coding, no take-home
- boam: real company problems

For candidates, this means preparation should focus on building and discussing real systems rather than memorizing algorithms.


## Framework Bias in Hiring

Some companies equate "AI engineering" with specific framework knowledge, leading to rejections of technically stronger candidates. A developer using PyTorch/CUDA/GGUF with FastAPI for multi-agent systems was [rejected for not knowing LangChain/LangGraph](https://www.reddit.com/r/LocalLLaMA/comments/1ow3anq/rejected_for_not_using_langchainlanggraph/) -- despite working at a lower level than what the role required. The community was split:

- "The company is not technical enough to understand the issues in LangChain and LangGraph" (355 upvotes)
- "Do you want a job? Learn the stupid tool" -- pragmatic view that popular frameworks are what companies hire for
- "You didn't fail the technical interview. You failed the culture fit" -- the best framing

For candidates: know what layer the company operates at (model vs. application) and align your language accordingly. For companies: framework-specific requirements filter out candidates who may have deeper expertise.


## Real-Time AI Cheating During Interviews

Real-time AI cheating is an increasing problem. Tools listen to the conversation, transcribe questions, and tell candidates what to say, and companies now explicitly address this in their hiring process.

This doesn't necessarily mean that they forbid using AI for coding tasks.

- Marvell Technology: "candidates do not use AI tools (transcription apps or real-time answer generators) during interviews"
- Hudson River Trading: "use of AI tools is strictly prohibited... we evaluate the authenticity of candidate responses"
- Wolters Kluwer: "use of AI or third-party support during interviews will be grounds for disqualification"
- Wells Fargo: "you're required to directly represent your experiences during the hiring process"


## AI Surveillance During Remote Interviews

AI surveillance during remote interviews is an emerging concern: camera monitoring, browser extensions, and audio analysis tools are being deployed by employers. Most candidate experiences remain remote, but monitoring tools add a new layer of stress. This trend is partly driving the return of in-person interviews at top companies. ([Reddit r/datascience, State of Interviewing 2025](https://www.reddit.com/r/datascience/comments/1p1dklk/state_of_interviewing_2025_heres_how_tech/))


## AI-Proctored Early Rounds

AI agents are starting to conduct early technical screens.

- Eightfold.ai (Jan 2026): Round 1 was an AI-conducted coding interview - ~60 min, 2 coding questions. The AI agent asked interactive follow-ups: edge cases, alternative approaches, complexity analysis. "This round felt more like a conversational technical discussion than a standard online test" (sources: [Medium](https://medium.com/@bhardwajtushar2004/inside-eightfold-ais-agentic-ai-internship-hiring-process-2026-f86dcb625aa8), [Reddit r/developersIndia](https://www.reddit.com/r/developersIndia/comments/1pbaj11/need_advice_for_eightfoldai_agentic_ai_engineer))
- Coinbase: AI conducts initial screening interviews with simulated scenarios
- [Deepthi Sudharsan](https://medium.com/@deepthi.sudharsan/inside-ai-interviews-stories-patterns-and-what-actually-matters-555684c38598) reports being interviewed by AI three times at US-based AI companies. The AI typically asks general or scenario-based questions; in rare cases uses RAG with the candidate's resume for targeted technical questions


## The "No AI Tools" Irony

Roles centered on productionizing LLMs and agents sometimes ban AI tools during coding tests. Candidates report cognitive dissonance: the job requires AI fluency, but the interview tests "raw" coding.

The Wolters Kluwer paradox: their AI engineering roles require AI coding tool proficiency (GitHub Copilot, AI agents) as mandatory skills, yet ban all AI during interviews.

Meanwhile, other companies lean into it:
- FlowFuse: AI tools "explicitly allowed and encouraged" during take-home
- Miro: "AI-First Proficiency" as hiring criterion, expects Claude Code/Cursor usage


## Employers Using AI in Hiring

Many explicitly say that they use AI in the recruitment process:

- Coinbase: AI conducts initial screening interviews with simulated scenarios
- Foxelli Group: Ribbon AI asynchronous video interviews
- Block/TIDAL: "we may use automated AI tools"

Only 1 company (Viral Nation) explicitly states they do NOT use AI in recruitment.


## Encouraging or Evaluating AI Fluency

- FlowFuse: AI tools "explicitly allowed and encouraged" during take-home
- Toku: AI-native development is "non-negotiable"
- Miro: "AI-First Proficiency" as hiring criterion, expects Claude Code/Cursor usage
- TRM Labs: "AI fluency is a baseline expectation"
- BetterUp: "during our interview process, you'll have opportunities to showcase how you harness AI"
- Micron Technology: "candidates are encouraged to use AI tools to enhance their resume and/or application materials"


## Published AI Guidelines for Candidates

Many companies share guidelines on how candidates should use AI:

- Datadog: [Interviewing at Datadog AI Guidelines](https://careers.datadoghq.com/candidate-experience/interviewing-at-datadog-ai-guidelines/)
- Invisible Technologies: [AI Interview Guidelines](https://invisibletech.ai/ai-interview-guidelines) - AI OK for resumes and assessments, banned during live interviews (no AI-generated scripts), coding assessments allow AI as part of normal workflow if candidates explain their thought process
- Anthropic: [Guidance on Candidates' AI Usage](https://www.anthropic.com/candidate-ai-guidance)
- Zapier: [How to Collaborate with AI During Zapier's Hiring Process](https://zapier.com/l/jobs/ai-at-zapier)
- AssemblyAI: [Candidate AI Guidance](https://www.assemblyai.com/candidate-ai-guidance)
- SandboxAQ: [AI in Interviews](https://www.sandboxaq.com/ai-in-interviews)
- CDW: [AI Applicant Notice](https://www.cdwjobs.com/pages/ai-applicant-notice) - encourages AI for grammar checking, brainstorming, accessibility, and research, but requires the final product to "accurately reflect your own experiences, achievements, and voice"
- Oscar Health: [Guidelines for using AI when interviewing at Oscar](https://www.hioscar.com/careers/ai-guidelines) - AI OK for resumes and prep, but misrepresentation may lead to disqualification.


## In-Person Interviews Are Coming Back

In-person interview rounds increased from 24% (2022) to 38% (2025), driven by concerns about AI-assisted cheating during remote interviews ([InterviewQuery](https://www.interviewquery.com/p/ai-interview-trends-tech-hiring-2025)). More frontier AI labs are requiring in-person onsites ([Yuan Meng](https://www.yuan-meng.com/posts/mle_interviews_2.0/)).


## AI Tools Allowed During Live Coding

Some companies now explicitly allow AI tools during live technical interviews:

- OpenAI: AI tools allowed during coding rounds - candidates share screen and narrate reasoning. "The boundary is that you shouldn't dump the entire problem into ChatGPT and paste back the output. They're watching for reasoning and judgment" ([source](https://medium.com/exponent/what-its-actually-like-to-interview-at-openai-in-2026-03a646c9436c))
- PromptLayer: allows ChatGPT during live coding to observe how candidates construct prompts and evaluate AI output ([source](https://blog.promptlayer.com/the-agentic-system-design-interview-how-to-evaluate-ai-engineers/))
- Microsoft SWE Applied AI/ML: Round 1 is entirely AI-assisted (use ChatGPT to solve problems), Round 2 bans AI tools. The format explicitly tests both AI-augmented productivity and baseline coding skills ([Reddit r/csMajors](https://www.reddit.com/r/csMajors/comments/1nqfzhq/microsoft_swe_applied_aiml_summer_2026_redmond))
- Exponent mock interview: a senior FAANG engineer conducts a combined coding + system design round where the candidate uses Claude Code throughout. The interviewer evaluates HOW the candidate uses the AI tool -- prompting strategy, ability to verify and understand generated code, and whether they let AI make architectural decisions for them. Key interviewer warning: "Not understanding what the AI is going to do is the biggest pitfall. Relying on AI to make decisions for you." The format merges coding and system design into a single round, reflecting how AI-assisted interviews collapse traditional round boundaries. ([Exponent](https://www.youtube.com/watch?v=C6CdzcU7I18))


## AI Engineering Interviews Lack Standardization

The AI engineering role is still being defined, and interviews reflect this. Janvi Kalra, who interviewed at 46 AI companies, found the process "all over the place" - combining LeetCode-style coding, system design, and project-based assessments with no consistent format. "The market is trying to move away from LeetCode but still asks LeetCode, so you end up having to study LeetCode as well." She hopes the industry moves toward project interviews, code reading, and debugging - but "as an industry we haven't fully formed an opinion here" ([Pragmatic Engineer](https://newsletter.pragmaticengineer.com/p/from-software-engineer-to-ai-engineer), [YouTube](https://www.youtube.com/watch?v=GEqJrKYnhbY))


## ML System Design Interviews Are Often Broken

Brian Kihoon Lee (~70 interviews, 7 offers from ~15 companies) critiques common ML system design interview failures ([source](https://www.moderndescartes.com/essays/ml_eng_interviewing/)):

- System design in ML clothing: Generic systems questions with superficial ML terminology that fail to assess either domain
- Outdated content: Interview problems become obsolete as ML advances rapidly. One interviewer expected traditional embedding + classifier approaches when LLMs offered superior solutions
- Algorithmic rederivation: Expecting candidates to independently derive established algorithms (like MinHash) in 45 minutes - testing memorization, not learning capacity
- "Cog in a machine" interviewers: Hyper-specific questions about their narrow project experience while missing big-picture evaluation

Lee proposes that ML system design interviews require staff-level execution expertise to conduct well and should only appear in senior candidate evaluations. His recommended alternative loop varies by seniority, replacing ML system design at junior levels with data modeling (live coding on real datasets with intentional bugs) and project deep dives.


## Junior vs. Senior Expectations Are Diverging

System design interviews increasingly test seniority through depth of thinking rather than tool knowledge ([InterviewNode](https://www.interviewnode.com/post/generative-ai-system-design-interview-patterns-you-should-know)):

- Junior: Focus on the prompt alone
- Mid-level: Describe embeddings or RAG mechanisms
- Senior: Design an evolving ecosystem - document chunking strategies, how retrieval affects context windows, how outputs are validated and stored, how user feedback improves retrieval scoring

"At senior levels, system design interviews aren't about frameworks, they're about foresight."


## Read the Room: LLM Hype Can Backfire

An interviewer [gave a borderline senior candidate a "soft thumbs down"](https://www.reddit.com/r/datascience/comments/15t69mt/failed_an_interviewee_because_they_wouldnt_shut/) because the candidate kept insisting LLMs could help with a regression problem the team was working on -- in a way that didn't make sense technically. The takeaway: at senior levels, candidates are expected to demonstrate judgment about when AI solutions are and aren't appropriate. Knowing the latest AI tools is table stakes; knowing when NOT to use them signals maturity.


## The Bar Feels Higher

Because everyone uses AI tools daily, the focus has shifted:
- Explaining architecture and trade-offs over memorization
- Demonstrating production thinking over coding speed
- Showing how you reason with AI, not just raw coding ability

Candidates report that "can you build an LLM app?" is no longer enough. The question is now "can you ship, scale, and evaluate production AI?"

InterviewQuery frames it as: "Knowledge is free -- judgment isn't." The interview philosophy shifted from "Can you code?" to "Can you reason with the AI that codes with you?" ([source](https://www.interviewquery.com/p/ai-interview-trends-tech-hiring-2025))


## Exploitative Take-Homes at AI Startups

AI startups are increasingly using take-home assignments as low-cost product ideation, with scope that amounts to real product work. Community discussions highlight a growing pattern:

- A French candidate was asked to [build a complete LLM agent for financial document analysis](https://www.reddit.com/r/developpeurs/comments/1m84v47/on_ma_demand%C3%A9_de_construire_un_agent_llm_complet/) -- community estimated 6,000-10,000 EUR worth of consulting effort
- An AI real-estate startup asked candidates to [build an end-to-end feature aggregating property information](https://www.reddit.com/r/ExperiencedDevs/comments/1nyzx77/is_this_type_of_takehome_assignment_becoming_the/) into a comprehensive brief -- vague scope with a 2-hour timeframe
- Experienced developers recommend declining any assignment that could constitute a deployable product, and refuse take-homes sent before any human conversation

The trend is accelerating as AI tools make it easier to build more in less time, raising scope expectations. "Founding Engineer" roles at AI startups often pair high expectations with exploitative screening processes.


## Emerging Interview Formats

Several new approaches are gaining traction, reported across multiple Hacker News threads:

- Code review rounds: Candidates evaluate provided code for bugs, performance issues, and design problems ([HN](https://news.ycombinator.com/item?id=40363135), [HN](https://news.ycombinator.com/item?id=42977039), [HN](https://news.ycombinator.com/item?id=43108673))
- Evaluating AI-generated code: Candidates retrieve a solution from an LLM, then review that solution during the interview ([HN](https://news.ycombinator.com/item?id=42268158), [HN](https://news.ycombinator.com/item?id=42977039))
- "AI delta" assessment: Candidates tackle real GitHub issues in 2-4 hours while evaluators assess what they add beyond what AI generates - exploration strategy, engineering rigor, edge case handling, documentation quality ([HN](https://news.ycombinator.com/item?id=46865130))
- Pair programming on real problems: 1-2 hours on production code provides stronger signal than algorithmic puzzles ([HN](https://news.ycombinator.com/item?id=43108673))
- Candidates using AI in live interviews often perform worse: Follow-up questions expose lack of understanding. LLM-generated code often contains subtle bugs that the candidate cannot explain ([HN](https://news.ycombinator.com/item?id=42909166))
- Anti-cheating tooling: Tools like BlindSpots use adversarial examples (invisible pixel and audio modifications) to disrupt AI screenshot-based and audio-based cheating tools without invasive surveillance ([HN](https://news.ycombinator.com/item?id=45492686))


## New Interview Round Types Emerging

Yuan Meng identifies several scarier rounds now appearing at top companies that didn't exist in earlier interview cycles ([source](https://www.yuan-meng.com/posts/mle_interviews_2.0/)):

- ML Infra Design: Detailed questions about feature stores, distributed training, and online serving (not just modeling)
- Multi-level OOP: Building toy backend systems with incremental complexity
- LLM Coding: Implementing Transformers, LoRA, KV cache, and autograd mechanics from scratch
- Research Presentations: Job talk-style presentations defending technical work
- References becoming standard: Most top companies now require 2-3 references from recent managers/colleagues
