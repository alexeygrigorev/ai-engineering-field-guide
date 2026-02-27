# Interview Process Analysis: AI Engineering Job Market

Analysis of 1,765 AI/ML engineering job descriptions to extract and summarize hiring/interview process information.

## Summary Statistics

| Metric | Count |
|--------|-------|
| Total job descriptions analyzed | 1,765 |
| JDs with actual structured interview processes | ~80 (across 51 unique companies) |
| JDs with no interview process details | ~1,685 |

Only ~4.5% of job descriptions include a structured interview process. The vast majority either omit the process entirely or mention "interview" only in boilerplate (accommodations, EEO statements, etc.).

---

## Common Interview Patterns

### Typical Number of Steps

| Steps | Companies | % of those with processes |
|-------|-----------|--------------------------|
| 2 stages | Lorikeet, Infinity Constellation, Watershed | 6% |
| 3 stages | sciemo, TensorOps, Glass Health, Nearform, Foxelli, VYNYL, hyperexponential (writer role), BJAK, Wing Assistant, Hastings Direct, Xenon Seven, Circle.so | 24% |
| 4 stages | P-1 AI, Lendable, PAR Technology, XBOW, Headway, PA Consulting, PostHog, boam, Column Tax, Sprinter Health, RelationalAI | 22% |
| 5 stages | Tenex, Harmonic, Zeely, Northbeam, Lendable (AI Eng), hyperexponential (eng roles), Monzo Bank, Phare Health, Pattern, Fifth Dimension, Qonto | 22% |
| 6 stages | Poggio Labs, Clarium, Stacks, Melotech, Doctolib, Monarch Money, GoFasti | 14% |
| 7 stages | FlowFuse, Roboflow, The College Board | 6% |

Median: 4 steps. Most common: 3-5 steps.

### Most Frequent Step Types

1. Recruiter/talent screen (40 of 51 companies) - Usually 15-30 min
2. Technical interview (38 of 51) - Live coding, system design, or code review
3. Hiring manager interview (33 of 51) - 45-60 min deep dive
4. Take-home challenge (17 of 51) - Typically 2-3 hours
5. Values/culture interview (13 of 51) - Separate from technical
6. CEO/founder interview (12 of 51) - Usually final step, 15-30 min
7. Panel interview (10 of 51) - Multiple interviewers
8. Reference check (10 of 51) - Before offer

### Estimated Total Candidate Time

| Time Range | Companies |
|------------|-----------|
| < 2 hours | sciemo, TensorOps, Foxelli, BJAK, Wing Assistant (~1.5h), Hastings Direct |
| 2-3 hours | P-1 AI (~2h45), Nearform (~2h15), Speechify, Xenon Seven |
| 3-5 hours | Clarium (~4h), Glass Health (~3.5h), boam, PA Consulting, Headway, hyperexponential (~4.5h), YLD (~3.5h), Sprinter Health (~4.25h), Monarch Money, Doctolib |
| 5-8 hours | Mutiny (~5.5h), Stacks, Northbeam (5-8h), Roboflow (6+h), Poggio Labs, Column Tax (~7.5h), Monzo Bank, Pattern |
| 1+ day | PostHog (SuperDay), Lorikeet (2-day trial), Infinity Constellation (1-week trial), Fifth Dimension (1-week paid trial option) |

---

## Home Assignments

See the dedicated **[Home Assignments Report](home-assignments.md)** for the full analysis of all 17 take-home assignments and 5 paid work trials, including detailed descriptions, summary tables, and key observations.

---

## Company-by-Company Breakdown

Individual interview process descriptions for each company. Each file links to the source job description YAML.

| # | Company | Role(s) |
|---|---------|---------|
| 1 | [Poggio Labs](data/01_8093818.md) | Senior AI Product Engineer |
| 2 | [Tenex](data/02_8095486.md) | Applied AI Engineer / Forward Deployed AI Engineer |
| 3 | [FlowFuse](data/03_8067206.md) | Full Stack Developer (AI-focused) |
| 4 | [Roboflow](data/04_8027169.md) | Full Stack Engineer, AI Agents |
| 5 | [Clarium](data/05_7936875.md) | Senior Applied AI Engineer |
| 6 | [Column Tax](data/06_6351158.md) | Software Engineer (Applied AI) |
| 7 | [PAR Technology](data/07_7937664.md) | AI Engineer |
| 8 | [hyperexponential](data/08_8162183.md) | 3 roles, 2 processes |
| 9 | [PostHog](data/09_6953405.md) | AI Product Engineer / SWE AI-Enabled Product |
| 10 | [Harmonic](data/10_6727775.md) | Full Stack Product Engineer (AI Search) |
| 11 | [Nearform](data/11_8373891.md) | Senior AI Python Software Engineer |
| 12 | [Lendable](data/12_8316438.md) | Senior AI Engineer / AI Engineer |
| 13 | [PA Consulting](data/13_8275583.md) | Senior Gen AI Developer |
| 14 | [XBOW](data/14_7297476.md) | AI Research Engineer |
| 15 | [Headway](data/15_8381956.md) | AI Staff SWE / Senior IT Engineer AI Automation |
| 16 | [P-1 AI](data/16_8243631.md) | AI Product Engineer, Senior SWE Agentic AI, QA Engineer AI |
| 17 | [Mutiny](data/17_4476482.md) | Senior Software Engineer (AI Products) |
| 18 | [Stacks](data/18_4761860.md) | Staff AI Engineer |
| 19 | [Melotech](data/19_8247431.md) | AI/ML Engineer + Intern |
| 20 | [Glass Health](data/20_3564658.md) | Founding AI/Data Engineer |
| 21 | [boam](data/21_8249839.md) | Applied AI Engineer |
| 22 | [Lorikeet](data/22_8005716.md) | Forward Deployed AI Engineer |
| 23 | [Infinity Constellation](data/23_7309806.md) | Founding AI Engineer |
| 24 | [sciemo](data/24_7780697.md) | AI/ML Engineer |
| 25 | [TensorOps](data/25_8314487.md) | Junior AI/ML Engineer |
| 26 | [Zeely](data/26_7568516.md) | AI Prompt Engineer |
| 27 | [YLD](data/27_8252085.md) | Contract Principal Operations Engineer |
| 28 | [Foxelli Group](data/28_8135769.md) | AI Engineer (Technical Product Owner) |
| 29 | [VYNYL](data/29_8389528.md) | Senior Full Stack Engineer (AI) |
| 30 | [Northbeam](data/30_8281581.md) | AI Operations & Automation Engineer |
| 31 | [The College Board](data/31_7602446.md) | Senior AI Engineer |
| 32 | [Watershed](data/32_7082017.md) | Software Engineer (AI Product) |
| 33 | [SmartAssets](data/33_7694512.md) | AI/ML Engineer |
| 34 | [Speechify](data/34_1393425.md) | Multiple roles |
| 35 | [BJAK](data/35_8286147.md) | Android, Backend, iOS Developer AI |
| 36 | [Xenon Seven](data/36_7358381.md) | AI/ML Engineer |
| 37 | [Wing Assistant](data/37_8359858.md) | MERN Stack Developer (AI Agents) |
| 38 | [Qonto](data/38_8097536.md) | Senior Machine Learning Engineer for AI Product |
| 39 | [Hastings Direct](data/39_8463501.md) | Lead Quality Engineer, Automation & AI |
| 40 | [Phare Health](data/40_8449234.md) | AI/ML Engineer |
| 41 | [Doctolib](data/41_8492018.md) | Senior AI Engineer |
| 42 | [Monzo Bank](data/42_8492197.md) | Senior Staff Software Engineer, AI Customer Operations |
| 43 | [Sprinter Health](data/43_8492296.md) | Applied AI Senior/Staff Software Engineer, Lead |
| 44 | [Fifth Dimension](data/44_8507147.md) | AI Engineer (Staff/Principal) |
| 45 | [Monarch Money](data/45_8531817.md) | Software Engineer, AI (Senior/Staff) |
| 46 | [Pattern](data/46_8489458.md) | AI Engineer II |
| 47 | [GoFasti](data/47_8591405.md) | AI Engineer (Backend focus) |
| 48 | [RelationalAI](data/48_8590709.md) | Senior Software Engineer, Symbolic AI |
| 49 | [Microstrategy](data/49_6178416.md) | AI Engineer I / Senior AI Engineer I |
| 50 | [Prudential plc](data/50_8561275.md) | Senior AI Engineer |
| 51 | [Nearform (UK)](data/51_8492964.md) | Senior AI Python Software Engineer |

---

## Notable & Unique Practices

### Paid Work Trials
| Company | Format | Duration |
|---------|--------|----------|
| PostHog | SuperDay - paid full day of real work | 1 day |
| Lorikeet | Paid work trial with the team | ~2 days |
| Infinity Constellation | Paid trial building something real | 1 week |
| Fifth Dimension | Paid one-week trial as alternative to standard interview | 1 week |
| CompuGroup Medical US | 3-month stipended internship with performance-based conversion | 3 months |

### AI Use in Hiring

Companies using AI to screen/evaluate applications:
| Company | Details |
|---------|---------|
| Block / TIDAL | "We may use automated AI tools to evaluate job applications" |
| Thomson Reuters | Uses AI to assess candidates; opt-out available |
| PointClickCare | Uses AI tools for candidate screening and assessment |
| Broadridge | Uses AI-powered tools to review and evaluate applications |
| Foxelli Group | Uses Ribbon AI asynchronous video interview tool |
| Lorikeet | Uses Automated Employment Decision Tools (AEDT) for initial screening |
| Coinbase | AI tool conducts initial screening interviews (simulating realistic scenarios + dynamic conversation); AI transcribes and summarizes later interview notes |
| Deel | Uses AEDT + AI-powered deepfake and fraud detection to verify candidate identity during interviews |
| LogicMonitor | AI tools assist with reviewing applications and identifying candidates; opt-out available |
| Twilio | "We use AI to help make our hiring process efficient" |
| Quora | AI sorts applications and records interview notes |
| WGSN | AI screens applications with anonymization to reduce bias |
| HubSpot | "HubSpot may use AI to help screen or assess candidates" |
| Grafana Labs | AI matches CVs to job postings; manual review continues alongside |
| NVIDIA | "NVIDIA uses AI tools in its recruiting processes" |
| Minted | Uses Brainner AI tool + identity verification at start of interviews |
| Assent | AI for note-taking and initial shortlisting; AI does not make hiring decisions |
| BDO Canada | AI tools support hiring process; human decisions final |
| McCain Foods | AI leveraged in hiring; human final decisions |
| Tide | AI in recruitment process (references separate AI Policy document) |

Companies explicitly NOT using AI in recruitment:
| Company | Details |
|---------|---------|
| Viral Nation | "Viral Nation does not use AI-enabled tools to screen, assess, rank, or select candidates" |

Companies banning AI during interviews:
| Company | Policy |
|---------|--------|
| Wolters Kluwer | "Use of AI-generated responses or third-party support during interviews will be grounds for disqualification." Requires removal of virtual backgrounds. Includes in-person interviews. Company-wide policy across all roles. |
| Hudson River Trading | "Use of AI tools during interviews or assessments is strictly prohibited" - employs methods to detect AI assistance |
| Marvell Technology | Candidates may not use AI tools (ChatGPT, Copilot, transcription apps, note-taking bots) during interviews. "Use of AI tools without prior instruction from the interviewer will result in disqualification." |
| Illumina | "Illumina prohibits the use of generative artificial intelligence (AI) in the application and interview process" |
| Wells Fargo | "Wells Fargo requires you to directly represent your own experiences during the recruiting and hiring process." Third-party recordings prohibited. (Company-wide across all roles.) |
| Datadog | Publishes formal "Interviewing at Datadog AI Guidelines" document |

Companies encouraging AI use by candidates:
| Company | Details |
|---------|---------|
| FlowFuse | AI tools "explicitly allowed and encouraged" during take-home assignment |
| Zapier | Provides guidance on AI use during hiring process |
| BetterUp | Welcomes AI-assisted applications |
| Micron Technology | "Candidates are encouraged to use AI tools to enhance their resume and/or application materials" - misuse to fabricate leads to disqualification |
| CDW | "AI can help you present yourself more clearly and effectively" - references AI Applicant Notice |
| Toku | AI-native development is a non-negotiable; "we do not expect handwritten code as the default path." Recommends Rezi.ai for resume preparation |
| Miro | "AI-First Proficiency" is a hiring criterion -- expects candidates to have integrated AI agents into their entire SDLC using tools like Claude Code, Cursor |
| TRM Labs | "AI fluency is a baseline expectation" -- candidates evaluated on applied AI fluency during interviews |
| Anthropic | References formal policy on candidates' use of AI during the application process |
| SandboxAQ | References formal guidance document on AI tool use in interviews |
| AssemblyAI | References external resource on how the company approaches AI use in interviews |

### AI-Specific Interview Practices

Notable interview-adjacent practices related to AI:
| Practice | Companies |
|----------|-----------|
| On-camera policy for remote interviews | Arctic Wolf (company-wide: "candidates are expected to be on camera during all video interviews") |
| Anti-fraud / identity verification | Wells Fargo (anti-proxy), Minted (identity verification at start), Deel (deepfake detection), Circle.so ("We do not use AI bots to interview candidates") |
| Application screening questions (written) | Apollo.io (5 written screening questions required), Strange Loop Labs (1-2 page cover letter essay on Engineering Principles) |
| Portfolio/project submission required | Dentsu Creative (GitHub + written opinion on AI implementation), Wolters Kluwer (Statement of Exceptional Work), Waystone (portfolio with measurable impact) |
| Bias-mitigated applications | SimCorp ("exclude personal data such as photo, age, or any non-professional information") |

### Take-Home Challenges

17 of 51 companies (33%) use take-home assignments; 5 more use paid work trials. See the dedicated [Home Assignments Report](home-assignments.md) for full analysis including format details, time estimates, AI tool policies, and evaluation methods.

### CEO/Founder Involvement
12 of 51 companies (24%) include a CEO or founder interview:
- P-1 AI - CEO interview (30 min), final step
- Clarium - CEO interview (30 min), final step
- XBOW - CEO and founder (30 min), final step
- Roboflow - CEO meeting (60 min), final step
- Northbeam - CEO/Co-founder, final step
- PostHog - Co-founder call (15 min)
- Stacks - Founder call (30 min), early in process
- boam - Founder conversation, final step
- Melotech - CEO (90 min), deep dive
- Lorikeet - Cofounders do the initial chats
- Wing Assistant - CEO, CPO & CTO in final interview (1 hour)
- Fifth Dimension - Both founders in culture fit round

### "No Whiteboard" / Realistic Assessments
Several companies explicitly reject abstract coding puzzles:
- Clarium - "No abstract puzzles," realistic exercises, info sent in advance
- Column Tax - "Not code golf," interviews mimic real work
- Glass Health - Realistic work simulation in final round
- TensorOps - No live coding, no take-home at all
- boam - Work sample uses real company problems
- Phare Health - "Not Leetcode," pseudo-coding exercise and systems design
- Doctolib - "Feature Building Interview" tests practical building, not algorithms

### Fastest Processes
- Speechify - "Aim to complete within 1 week"
- Melotech - "Start to offer within a week"
- Roboflow - "All conversations may happen over a day or two"
- boam - "Fast, structured, and transparent"
- Tenex - "Build First" fast-track skips early stages
- Qonto - ~20 working days, offers within 48 hours of completion
- Sprinter Health - "Aim to complete between 2-3 weeks"
- RelationalAI - "We move quickly"

---

## Key Takeaways

1. **Very few AI/ML job postings disclose the interview process** - only ~4.5% of 1,765 JDs include structured interview steps. This remains a significant transparency gap.

2. **4 steps is the sweet spot** - the most common processes have 3-5 stages, typically: recruiter screen -> technical assessment -> hiring manager -> team/culture round.

3. **Take-homes are popular** - 33% of companies with disclosed processes use a take-home challenge. Choice-based formats are emerging: Monzo Bank offers take-home vs pair coding, Qonto offers remote vs live exercise. Some explicitly welcome AI tool usage (FlowFuse), while others ban it in live interviews (Wolters Kluwer, Marvell).

4. **Paid work trials are growing** - PostHog (SuperDay), Lorikeet (2-day trial), Infinity Constellation (paid week), and Fifth Dimension (paid week alternative) represent a trend toward compensating candidates for evaluation time.

5. **CEO/founder involvement is common at startups** - 24% of companies include a founder or CEO interview, almost always as the final step.

6. **AI's role in hiring has exploded** - The landscape has become much more complex:
   - **20+ companies** now disclose using AI in their own screening/hiring (up from 6). Coinbase uses AI to *conduct* initial screening interviews. Deel uses deepfake detection on candidates.
   - **6 companies** explicitly ban candidates from using AI during interviews (Wolters Kluwer, HRT, Marvell, Illumina, Wells Fargo, Datadog).
   - **11 companies** encourage or evaluate AI fluency: Miro and TRM Labs evaluate AI tool mastery as a hiring criterion, Toku considers AI-native development a "non-negotiable."
   - **The Wolters Kluwer paradox**: multiple AI engineering roles require AI coding tool proficiency (GitHub Copilot, AI agents) as mandatory skills, yet the company bans all AI during interviews.
   - **1 company** (Viral Nation) explicitly states they do NOT use AI in their recruitment process.

7. **Total time commitment ranges widely** - from ~1.5 hours (TensorOps, sciemo, Wing Assistant) to 7.5+ hours (Column Tax) or even a full paid week (Infinity Constellation, Fifth Dimension).

8. **"No whiteboard" is a selling point** - Multiple companies explicitly advertise realistic, work-simulation-based interviews as a differentiator from LeetCode-style assessments. Phare Health says "not Leetcode," Doctolib has a dedicated "Feature Building Interview."

9. **Anti-fraud measures are proliferating** - Wells Fargo requires candidates to "directly represent your own experiences." Arctic Wolf mandates cameras-on during remote interviews. Deel uses AI deepfake detection. Minted verifies identity at interview start. Circle.so explicitly states "we do not use AI bots to interview candidates."

10. **AI-specific interview rounds are emerging** - Doctolib has a dedicated "AI System Design Interview." Sprinter Health has "AI-Focused Systems Design." These domain-specific rounds reflect the maturation of AI engineering as a distinct discipline.
