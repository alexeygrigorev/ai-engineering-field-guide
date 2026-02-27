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


Take-home challenges

- 33% use take-home assignments
- 5 companies (10%) use paid work trials

See the dedicated [Home Assignments Report](05-home-assignments.md) for full analysis.


## AI Use in Hiring

### Employers using AI in hiring (~40%)

Ranges from light-touch to fully AI-driven:

- Coinbase: AI conducts initial screening interviews with simulated scenarios
- Deel: AI-powered deepfake and fraud detection to verify candidate identity
- Foxelli Group: Ribbon AI asynchronous video interviews
- Block/TIDAL: "we may use automated AI tools"

Only 1 company (Viral Nation) explicitly states they do NOT use AI in recruitment.

### Banning candidates from using AI (~10%)

- Wolters Kluwer: grounds for disqualification, requires removing virtual backgrounds
- Hudson River Trading: strictly prohibited, methods to detect AI
- Marvell Technology: no ChatGPT, Copilot, transcription or note-taking bots
- Illumina: prohibits generative AI in application and interview
- Wells Fargo: must directly represent own experiences

The Wolters Kluwer paradox: their AI engineering roles require AI coding tool proficiency (GitHub Copilot, AI agents) as mandatory skills, yet the company bans all AI during interviews.

### Encouraging or evaluating AI fluency (~22%)

- FlowFuse: AI tools "explicitly allowed and encouraged" during take-home
- Toku: AI-native development is "non-negotiable"
- Miro: "AI-First Proficiency" as hiring criterion, expects Claude Code/Cursor usage
- TRM Labs: "AI fluency is a baseline expectation"
- CDW: publishes a detailed [AI Applicant Notice](https://www.cdwjobs.com/pages/ai-applicant-notice) encouraging AI for grammar checking, brainstorming, accessibility, and research — but requiring the final product to "accurately reflect your own experiences, achievements, and voice"
- Anthropic, SandboxAQ, AssemblyAI, Zapier, BetterUp, Micron Technology

### Published AI guidelines for candidates

Several companies publish formal policies on AI use during their hiring process:

- Datadog: [Interviewing at Datadog AI Guidelines](https://careers.datadoghq.com/candidate-experience/interviewing-at-datadog-ai-guidelines/)
- CDW: [AI Applicant Notice](https://www.cdwjobs.com/pages/ai-applicant-notice) — encourages AI for grammar checking, brainstorming, accessibility, and research, but requires the final product to "accurately reflect your own experiences, achievements, and voice"
- Oscar Health: [Guidelines for using AI when interviewing at Oscar](https://www.hioscar.com/careers/ai-guidelines) — AI OK for resumes and prep, but misrepresentation may lead to disqualification. Oscar also discloses using Eightfold and Greenhouse AI matching tools.
- Invisible Technologies: [AI Interview Guidelines](https://invisibletech.ai/ai-interview-guidelines) — AI OK for resumes and assessments, banned during live interviews (no AI-generated scripts), coding assessments allow AI as part of normal workflow if candidates explain their thought process

## AI-Specific Interview Practices

### Anti-fraud measures

- Arctic Wolf: mandates cameras-on for all remote interviews
- Wells Fargo: screens for proxy candidates
- Minted: verifies identity at interview start
- Deel: AI deepfake detection
- Circle.so: "we do not use AI bots to interview candidates"

### Written screening and portfolio submissions

- Apollo.io: 5 screening questions
- Strange Loop Labs: 1-2 page cover letter essay
- Dentsu Creative: GitHub + written opinion on AI implementation
- Wolters Kluwer: Statement of Exceptional Work
- SimCorp: asks candidates to exclude personal data (photos, age) for bias mitigation

### "No Whiteboard" / Realistic Assessments

- Clarium: "no abstract puzzles," info sent in advance
- Column Tax: "not code golf," interviews mimic real work
- Glass Health: realistic work simulation
- TensorOps: no live coding, no take-home
- boam: real company problems
- Phare Health: "not Leetcode"
- Doctolib: "Feature Building Interview" tests practical building, not algorithms


## AI System Design Interviews

AI-specific interview rounds are emerging - Doctolib has a dedicated "AI System Design Interview." Sprinter Health has "AI-Focused Systems Design." See [AI System Design](04-ai-system-design.md) for more.
