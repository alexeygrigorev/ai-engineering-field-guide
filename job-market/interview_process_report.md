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

## Home Assignments Deep Dive

Of the 51 companies with disclosed interview processes, 17 (33%) include a take-home or asynchronous assignment. An additional 5 companies use paid work trials instead of traditional assignments. Only 1 company (TensorOps) explicitly states they do not use take-homes.

### Detailed Assignment Descriptions

#### 1. Column Tax - Software Engineer (Applied AI)
File: [`6351158_Column_Tax_Software_Engineer_Applied_AI.yaml`](data_raw/6351158_Column_Tax_Software_Engineer_Applied_AI.yaml)

> We'll ask you to complete a ~3-hour project that mirrors the kind of integration or tooling work we do every day. You'll have full freedom to do it your way - this is about decision-making, clarity, and implementation, not code golf.

- Duration: ~3 hours
- Format: Project mirroring real integration/tooling work
- Paid: Not mentioned
- AI tools: Not mentioned
- When: Step 2 of 4 (after intro call with Head of Engineering)
- Evaluation: Discussed during 4.5-hour interview panels over 2 days

---

#### 2. FlowFuse - Full Stack Developer (AI-focused)
File: [`8067206_FlowFuse_FlowFuse_Full_Stack_Developer_AI-focused.yaml`](data_raw/8067206_FlowFuse_FlowFuse_Full_Stack_Developer_AI-focused.yaml)

> Candidates choose one of the following options. Both are explicitly time-boxed to 2-3 hours:
> - Option A: Build a small AI-powered feature or tool (for example: intelligent search, summarization, validation, or an assistant-style workflow) using an LLM API.
> - Option B: Contribute a small, scoped AI-related pull request or prototype demonstrating applied AI integration in an existing codebase.
> - Note: AI tools are explicitly allowed and encouraged where appropriate.

Technical interview follow-up:
> The discussion focuses on problem understanding, AI design decisions and tradeoffs, system structure, reliability considerations, and how the solution would evolve over time rather than feature completeness. There will be explicit discussion of where AI was used, how it was used, and why those choices were made.

- Duration: 2-3 hours (time-boxed)
- Format: Choice between building an AI feature or contributing a PR
- Paid: Explicitly unpaid
- AI tools: Explicitly allowed and encouraged
- When: Step 4 of 7 (after 2 calls)
- Evaluation: 60-min technical interview reviewing the work with 2-3 team members

---

#### 3. Harmonic - Full Stack Product Engineer (AI Search)
File: [`6727775_Harmonic_Full_Stack_Product_Engineer_AI_Search.yaml`](data_raw/6727775_Harmonic_Full_Stack_Product_Engineer_AI_Search.yaml)

Listed as "Take Home Exam" in the process - no further description of format, content, or duration provided.

- Duration: Not specified
- Format: Take-home exam (details not given)
- Paid: Not mentioned
- AI tools: Not mentioned
- When: Step 2 of 5 (after recruiter screening)
- Evaluation: Followed by debugging session (45 min) + jam session (1 hour)

---

#### 4. Tenex - Applied AI Engineer / Forward Deployed AI Engineer
File: [`8095486_Tenex_tenexco_Applied_AI_Engineer.yaml`](data_raw/8095486_Tenex_tenexco_Applied_AI_Engineer.yaml), [`7257124_Tenex_tenexco_Forward_Deployed_AI_Engineer.yaml`](data_raw/7257124_Tenex_tenexco_Forward_Deployed_AI_Engineer.yaml)

> Take-Home: A practical challenge to showcase your technical skills.
> Team Review: Our engineers review your submission. If it's a match, we'll invite you to the final round.

> Want to skip the screen and go straight to an onsite? Prove you can build by submitting a demo via our Build First form to fast-track your application.

- Duration: Not specified
- Format: Practical challenge
- Paid: Not mentioned
- AI tools: Not mentioned
- When: Step 3 of 5 (after screen call)
- Evaluation: Engineers review submission; then deep dive during onsite panel interview
- Notable: "Build First" fast-track option lets candidates skip the screen by submitting a demo upfront

---

#### 5. Lendable - AI Engineer / Senior AI Engineer
File: [`8029593_Lendable_AI_Engineer.yaml`](data_raw/8029593_Lendable_AI_Engineer.yaml), [`8316438_Lendable_Senior_AI_Engineer.yaml`](data_raw/8316438_Lendable_Senior_AI_Engineer.yaml)

Listed as "Take-home exercise" followed by "Walkthrough of your exercise" - no further description of the assignment itself.

- Duration: Not specified
- Format: Take-home exercise (details not given)
- Paid: Not mentioned
- AI tools: Not mentioned
- When: Step 2 of 5 (after introductory call)
- Evaluation: Dedicated walkthrough interview to discuss the exercise, then meet the day-to-day team and exec team

---

#### 6. Stacks - Staff AI Engineer
File: [`4761860_Stacks_Staff_AI_Engineer.yaml`](data_raw/4761860_Stacks_Staff_AI_Engineer.yaml)

> Step 4: Take-home and 1-hour on-site panel interview with our team at Stacks.

- Duration: Not specified
- Format: Take-home (details not given), combined with on-site panel
- Paid: Not mentioned
- AI tools: Not mentioned
- When: Step 4 of 6 (after 3 calls with talent, founder, and team member)
- Evaluation: Combined with 1-hour on-site panel interview

---

#### 7. Melotech - AI/ML Engineer + Intern
File: [`8247431_Melotech_AIML_Engineer.yaml`](data_raw/8247431_Melotech_AIML_Engineer.yaml), [`8247435_Melotech_AIML_Engineer_Intern.yaml`](data_raw/8247435_Melotech_AIML_Engineer_Intern.yaml)

> Take-home case study: Real-world project - showcase your skills and working style
> Case interview: 90-minute case discussion - getting to know you & present and debate your results with a team member

- Duration: Not specified
- Format: Real-world case study project
- Paid: Not mentioned
- AI tools: Not mentioned
- When: Step 1 of 6 - starts the process (no screen or intro call first)
- Evaluation: 90-minute case interview where candidate presents and debates results
- Notable: Same rigorous process for both senior and intern roles. Company is in stealth mode - candidates learn more as they progress.

---

#### 8. Zeely - AI Prompt Engineer (ComfyUI)
File: [`7568516_Zeely_AI_Admaker_AI_Prompt_Engineer_ComfyUI.yaml`](data_raw/7568516_Zeely_AI_Admaker_AI_Prompt_Engineer_ComfyUI.yaml)

Listed as "Test Task" in process: `Intro Call > Test Task > Final Interview > Reference check > Offer` - no further description.

- Duration: Not specified
- Format: Test task (details not given)
- Paid: Not mentioned
- AI tools: Not mentioned
- When: Step 2 of 5 (after intro call)

---

#### 9. hyperexponential - Senior Technical Writer/Documentation Engineer, AI
File: [`7298439_hyperexponential_Senior_Technical_WriterDocumentation_Engineer_-_A.yaml`](data_raw/7298439_hyperexponential_Senior_Technical_WriterDocumentation_Engineer_-_A.yaml)

> Skills Assessment - Home-based task followed by interview (60 minutes)

- Duration: Not specified (interview discussing it is 60 min)
- Format: Home-based skills assessment task
- Paid: Not mentioned
- AI tools: Not mentioned
- When: Step 3 of 4 (after talent call and manager interview)
- Evaluation: Combined with 60-min follow-up interview

---

#### 10. boam - Applied AI Engineer
File: [`8249839_boam_Applied_AI_Engineer.yaml`](data_raw/8249839_boam_Applied_AI_Engineer.yaml)

> Work Sample: Solve a real Boam-style ML/AI challenge that shows your modeling approach, pipeline thinking, and execution muscle

- Duration: Not specified
- Format: Real company-specific ML/AI challenge
- Paid: Not mentioned
- AI tools: Not mentioned
- When: Step 3 of 4 (after intro call and deep dive)
- Evaluation: Not explicitly described; followed by founder/leadership conversation

---

#### 11. SmartAssets - AI/ML Engineer
File: [`7694512_SmartAssets_AI_Engineer_Machine_Learning_Engineer.yaml`](data_raw/7694512_SmartAssets_AI_Engineer_Machine_Learning_Engineer.yaml)

> Successful applicants will receive a coding challenge to evaluate their programming knowledge and skills as outlined in this job description. This step is an essential part of our selection process to ensure a good match with our team's needs and the demands of the role.

- Duration: Not specified
- Format: Coding challenge
- Paid: Not mentioned
- AI tools: Not mentioned
- When: After application review (only assessment step described)

---

#### 12. Roboflow - Full Stack Engineer, AI Agents
File: [`8027169_Roboflow_Full_Stack_Engineer_AI_Agents.yaml`](data_raw/8027169_Roboflow_Full_Stack_Engineer_AI_Agents.yaml)

> [45m] Build a project with Roboflow and present it to our CTO, Brad Dwyer

This may involve advance preparation outside the live session (building a project with the company's product), though the presentation itself is 45 minutes live.

- Duration: ~45 min presentation (prep time not specified)
- Format: Build a project using Roboflow's product, present to CTO
- Paid: Not mentioned
- AI tools: Not mentioned
- When: Step 4 of 7 (after hiring manager intro and technical assessment)
- Evaluation: Direct presentation to CTO

---

#### 13. Wing Assistant - MERN Stack Developer (AI Agents)
File: [`8359858_Wing_Assistant_MERN_Stack_Developer_AI_Agents.yaml`](data_raw/8359858_Wing_Assistant_MERN_Stack_Developer_AI_Agents.yaml)

Listed as "Technical Task" between the introductory call and the final interview -- no further description of format, content, or duration provided.

- Duration: Not specified
- Format: Technical task (details not given)
- Paid: Not mentioned
- AI tools: Not mentioned
- When: Step 2 of 3 (after introductory call)
- Evaluation: Followed by 1-hour final interview with CEO, CPO & CTO

---

#### 14. Lendable - Senior AI Software Engineer
File: [`8440447_Lendable_Senior_AI_Software_Engineer.yaml`](data_raw/8440447_Lendable_Senior_AI_Software_Engineer.yaml)

Listed as "Take-home task" followed by "Technical interview based on the task" -- confirming Lendable's consistent use of take-homes across all AI roles.

- Duration: Not specified
- Format: Take-home task (details not given)
- Paid: Not mentioned
- AI tools: Not mentioned
- When: Step 2 of 4 (after screening call with HM)
- Evaluation: Technical interview based on the task

---

#### 15. Monzo Bank - Senior Staff Software Engineer, AI Customer Operations
File: [`8492197_Monzo_Bank_Senior_Staff_Software_Engineer_AI_Customer_Operat.yaml`](data_raw/8492197_Monzo_Bank_Senior_Staff_Software_Engineer_AI_Customer_Operat.yaml)

Candidates get a choice between a take-home task or a pair coding exercise.

- Duration: Not specified
- Format: Take-home task OR pair coding (candidate's choice)
- Paid: Not mentioned
- AI tools: Not mentioned
- When: Step 4 of 5 (after recruiter call, initial call, system design interview)
- Evaluation: Followed by final interview including behavioral and leadership rounds
- Notable: Monzo publicly shares a senior engineer's blog post about the interview experience. ~3-4 week timeline.

---

#### 16. Qonto - Senior Machine Learning Engineer for AI Product
File: [`8097536_Qonto_Senior_Machine_Learning_Engineer_for_AI_Product.yaml`](data_raw/8097536_Qonto_Senior_Machine_Learning_Engineer_for_AI_Product.yaml)

> A remote or live exercise to demonstrate your skills and give you a taste of what working at Qonto could be like.

- Duration: Not specified
- Format: Remote or live exercise (candidate may choose)
- Paid: Not mentioned
- AI tools: Not mentioned
- When: After interviews with Talent Acquisition Manager and future managers
- Evaluation: Not specified
- Notable: Average process is ~20 working days; offers follow within 48 hours of completion.

---

#### 17. Hastings Direct - Lead Quality Engineer, Automation & AI
File: [`8463501_Hastings_Direct_Lead_Quality_Engineer_-_Automation_AI.yaml`](data_raw/8463501_Hastings_Direct_Lead_Quality_Engineer_-_Automation_AI.yaml)

Listed as "Case study round" as the final step -- no further description of format or duration.

- Duration: Not specified
- Format: Case study (details not given)
- Paid: Not mentioned
- AI tools: Not mentioned
- When: Step 3 of 3 (after recruiter screen and hiring manager intro)
- Evaluation: Not described

---

### Paid Work Trials (Alternative to Traditional Assignments)

| Company | File | Role | Format | Duration | Compensation |
|---------|------|------|--------|----------|--------------|
| PostHog | [`6953405`](data_raw/6953405_PostHog_AI_Product_Engineer.yaml), [`8277537`](data_raw/8277537_PostHog_Software_Engineer_AI-Enabled_Product_Autonomy.yaml) | AI Product Eng / SWE AI | SuperDay - full day of real work | 1 day | Paid |
| Lorikeet | [`8005716`](data_raw/8005716_Lorikeet_Forward_Deployed_AI_Engineer.yaml) | Forward Deployed AI Eng | Work trial - ship with the team | ~2 days | Paid |
| Infinity Constellation | [`7309806`](data_raw/7309806_Infinity_Constellation_Founding_AI_Engineer_-_Supernal.yaml) | Founding AI Eng | Build something real with the team | 1 week | Paid |
| Fifth Dimension | [`8507147`](data_raw/8507147_Fifth_Dimension_AI_Engineer_StaffPrincipal.yaml) | AI Engineer (Staff/Principal) | Paid one-week trial as alternative to standard interview | 1 week | Paid |
| CompuGroup Medical US | [`8123883`](data_raw/8123883_CompuGroup_Medical_US_Generative_AI_Developer_Fresher.yaml) | Generative AI Developer (Fresher) | 3-month stipended internship with performance-based conversion | 3 months | Stipend |

### Summary Table

| # | Company | File ID | Duration | Format | AI OK? | Paid? | Evaluation Method |
|---|---------|---------|----------|--------|--------|-------|-------------------|
| 1 | Column Tax | [`6351158`](data_raw/6351158_Column_Tax_Software_Engineer_Applied_AI.yaml) | ~3 hrs | Real integration project | ? | ? | 4.5-hr panel discussion |
| 2 | FlowFuse | [`8067206`](data_raw/8067206_FlowFuse_FlowFuse_Full_Stack_Developer_AI-focused.yaml) | 2-3 hrs | AI feature or PR (choice) | Yes | No | 60-min review with team |
| 3 | Harmonic | [`6727775`](data_raw/6727775_Harmonic_Full_Stack_Product_Engineer_AI_Search.yaml) | ? | Take-home exam | ? | ? | Debugging + jam session |
| 4 | Tenex | [`8095486`](data_raw/8095486_Tenex_tenexco_Applied_AI_Engineer.yaml), [`7257124`](data_raw/7257124_Tenex_tenexco_Forward_Deployed_AI_Engineer.yaml) | ? | Practical challenge | ? | ? | Engineer review + panel |
| 5 | Lendable | [`8029593`](data_raw/8029593_Lendable_AI_Engineer.yaml), [`8316438`](data_raw/8316438_Lendable_Senior_AI_Engineer.yaml) | ? | Take-home exercise | ? | ? | Dedicated walkthrough |
| 6 | Stacks | [`4761860`](data_raw/4761860_Stacks_Staff_AI_Engineer.yaml) | ? | Take-home | ? | ? | On-site panel |
| 7 | Melotech | [`8247431`](data_raw/8247431_Melotech_AIML_Engineer.yaml), [`8247435`](data_raw/8247435_Melotech_AIML_Engineer_Intern.yaml) | ? | Real-world case study | ? | ? | 90-min case interview |
| 8 | Zeely | [`7568516`](data_raw/7568516_Zeely_AI_Admaker_AI_Prompt_Engineer_ComfyUI.yaml) | ? | Test task | ? | ? | Not described |
| 9 | hyperexponential | [`7298439`](data_raw/7298439_hyperexponential_Senior_Technical_WriterDocumentation_Engineer_-_A.yaml) | ? | Home-based task | ? | ? | 60-min follow-up interview |
| 10 | boam | [`8249839`](data_raw/8249839_boam_Applied_AI_Engineer.yaml) | ? | Real ML/AI challenge | ? | ? | Not described |
| 11 | SmartAssets | [`7694512`](data_raw/7694512_SmartAssets_AI_Engineer_Machine_Learning_Engineer.yaml) | ? | Coding challenge | ? | ? | Not described |
| 12 | Roboflow | [`8027169`](data_raw/8027169_Roboflow_Full_Stack_Engineer_AI_Agents.yaml) | prep+45m | Build with product, present | ? | ? | Present to CTO |
| 13 | Wing Assistant | [`8359858`](data_raw/8359858_Wing_Assistant_MERN_Stack_Developer_AI_Agents.yaml) | ? | Technical task | ? | ? | Final interview with C-suite |
| 14 | Lendable | [`8440447`](data_raw/8440447_Lendable_Senior_AI_Software_Engineer.yaml) | ? | Take-home task | ? | ? | Technical interview based on task |
| 15 | Monzo Bank | [`8492197`](data_raw/8492197_Monzo_Bank_Senior_Staff_Software_Engineer_AI_Customer_Operat.yaml) | ? | Take-home OR pair coding (choice) | ? | ? | Behavioral + leadership rounds |
| 16 | Qonto | [`8097536`](data_raw/8097536_Qonto_Senior_Machine_Learning_Engineer_for_AI_Product.yaml) | ? | Remote or live exercise | ? | ? | Not specified |
| 17 | Hastings Direct | [`8463501`](data_raw/8463501_Hastings_Direct_Lead_Quality_Engineer_-_Automation_AI.yaml) | ? | Case study | ? | ? | Not described |

### Key Observations on Home Assignments

Format trends:
- Realistic/applied work is the dominant philosophy. Column Tax says "not code golf," boam uses "a real Boam-style ML/AI challenge," Melotech uses "real-world projects," FlowFuse offers building an AI feature or contributing actual code.
- No company uses generic algorithmic puzzles as take-homes. All assignments are applied/domain-specific.
- Choice-based assignments are growing: FlowFuse lets candidates choose between building something new or contributing a PR; Monzo Bank offers a choice between take-home and pair coding; Qonto offers remote or live exercise.
- Most companies provide minimal detail about what the assignment actually involves - only Column Tax, FlowFuse, boam, Melotech, and Qonto describe the content in any detail.

Time investment:
- Only 2 companies specify duration: Column Tax (~3 hours) and FlowFuse (2-3 hours, time-boxed).
- The remaining 15 companies do not disclose expected time, creating uncertainty for candidates.
- Paid work trials range from 1 day (PostHog) to 1 week (Fifth Dimension, Infinity Constellation) to 3 months (CompuGroup Medical US internship).

Compensation:
- 5 companies (PostHog, Lorikeet, Infinity Constellation, Fifth Dimension, CompuGroup Medical US) explicitly pay candidates for assessment time.
- FlowFuse explicitly states theirs is unpaid.
- The remaining 13 companies don't mention compensation (likely unpaid).

AI tool policies for assignments:
- 1 company explicitly allows AI (FlowFuse: "AI tools are explicitly allowed and encouraged")
- 0 companies explicitly ban AI in take-home assignments specifically (bans from Wolters Kluwer and HRT apply to live interviews)
- 16 companies don't mention AI tool policy for their assignments - a significant gap given the prevalence of AI coding assistants

Placement in the process:
- Most assignments come after an initial screen (step 2-3 of the process)
- Melotech is unique: the case study is step 1 - candidates start with the assignment before any calls
- Monzo Bank places the take-home/pair coding at step 4, after a system design interview
- hyperexponential combines the take-home with the interview discussion in a single stage
- Stacks combines the take-home with the onsite panel

How assignments are evaluated:
- Dedicated walkthrough (5 companies): Lendable, FlowFuse, Melotech, hyperexponential, and Monzo Bank all have a follow-up interview to discuss the assignment
- Team review (2 companies): Tenex has engineers review the submission before deciding on final round; Stacks combines with panel
- Presentation to leadership (2 companies): Roboflow candidates present to the CTO; Melotech candidates present and debate results
- C-suite review (1 company): Wing Assistant follows the technical task with a final interview with CEO, CPO & CTO
- Not specified (7 companies): Harmonic, Zeely, SmartAssets, boam, Qonto, Hastings Direct, and Lendable (new role) don't describe how the assignment is evaluated

Companies that explicitly DON'T use take-homes:
- TensorOps - "This interview does not involve live coding or a take-home assignment"
- Glass Health - All rounds are live (no take-home)
- Clarium - Live realistic exercises with info sent in advance (no async work)
- Phare Health - Explicitly "not Leetcode," all rounds live (pseudo-coding + systems design)

---

## Company-by-Company Breakdown

### 1. Poggio Labs - Senior AI Product Engineer
File: [`8093818`](data_raw/8093818_Poggio_Labs_Senior_AI_Product_Engineer.yaml)
1. Application review
2. Recruiter meeting (15 min)
3. Intro call with engineering (30 min)
4. Technical interview - live coding (60 min)
5. Cross-functional interview (45 min)
6. System design / manager meeting (60 min)

Notable: Dedicated cross-functional interview with someone outside engineering. Six stages with clear time estimates.

---

### 2. Tenex - Applied AI Engineer / Forward Deployed AI Engineer
Files: [`8095486`](data_raw/8095486_Tenex_tenexco_Applied_AI_Engineer.yaml), [`7257124`](data_raw/7257124_Tenex_tenexco_Forward_Deployed_AI_Engineer.yaml)
1. Application - resume + portfolio review
2. Screen - intro call
3. Take-home - practical challenge
4. Team review of submission
5. Final round (onsite): Systems Design + Panel Interview

Notable: "Build First" fast-track option - submit a working demo to skip the screen and go straight to onsite.

---

### 3. FlowFuse - Full Stack Developer (AI-focused)
File: [`8067206`](data_raw/8067206_FlowFuse_FlowFuse_Full_Stack_Developer_AI-focused.yaml)
1. Resume review by hiring manager
2. Screening call (15 min)
3. Engineering manager call (45 min)
4. Take-home assignment (2-3 hours, unpaid) - choose between building an AI feature or contributing a PR
5. Technical interview (60 min) - review take-home with 2-3 team members
6. Team interview (45 min) - collaboration, communication
7. Offer

Notable: AI tools explicitly allowed and encouraged during take-home. Technical interview includes discussion of where/how AI was used.

---

### 4. Roboflow - Full Stack Engineer, AI Agents
File: [`8027169`](data_raw/8027169_Roboflow_Full_Stack_Engineer_AI_Agents.yaml)
1. Application review (LinkedIn, GitHub, open source)
2. Hiring manager intro (30 min)
3. Technical assessment (60 min)
4. Build a project with Roboflow + present to CTO (45 min)
5. Hiring manager deep dive (45 min)
6. Culture discussion with Head of Operations (45 min)
7. CEO meeting (60 min)

Notable: 6+ hours total, may happen over 1-2 days. Candidates build an actual project with the company's product and present it to the CTO.

---

### 5. Clarium - Senior Applied AI Engineer
File: [`7936875`](data_raw/7936875_Clarium_Senior_Applied_AI_Engineer.yaml)
1. Apply (every application read)
2. Exploratory interview (30 min) - 10 min reserved for candidate Qs
3. Hiring manager interview (60 min) - topics shared in advance
4. Technical interview (60 min) - no abstract puzzles, info sent in advance
5. Values interview (60 min) - 2 team members, guidance provided in advance
6. CEO interview (30 min)

Notable: Explicitly "no abstract puzzles." Topics and guidance shared in advance for multiple stages. Written personally by Head of AI.

---

### 6. Column Tax - Software Engineer (Applied AI)
File: [`6351158`](data_raw/6351158_Column_Tax_Software_Engineer_Applied_AI.yaml)
1. Intro call with Head of Engineering
2. Take-home challenge (~3 hours) - mirrors real work, "not code golf"
3. Interview panels (~4.5 hours over 2 days) - redesigning systems, debugging in sandbox, walking through past projects
4. References + offer

Notable: Panels designed to "mimic real work." ~7.5 hours total candidate time.

---

### 7. PAR Technology - AI Engineer
File: [`7937664`](data_raw/7937664_PAR_Technology_AI_Engineer.yaml)
1. Phone screen with Talent Acquisition
2. Video interview with Hiring Manager (MS Teams)
3. Technical interview + exercise with Team (MS Teams)
4. Final interview with Team (MS Teams)

---

### 8. hyperexponential (3 roles, 2 processes)
Files: [`8162183`](data_raw/8162183_hyperexponential_AI_Engineer_-_PlatformMLOps.yaml), [`7950954`](data_raw/7950954_hyperexponential_Senior_Software_Engineer_-_AI_Products.yaml), [`7298439`](data_raw/7298439_hyperexponential_Senior_Technical_WriterDocumentation_Engineer_-_A.yaml)

Engineering roles (AI Engineer Platform/MLOps, Senior SWE AI Products):
1. Talent team call (30 min)
2. Manager interview (60 min)
3. Technical assessment - code review, system design (120 min)
4. Values interview with senior tech leadership (60 min)
5. Offer

Writer role (Senior Technical Writer AI):
1. Talent team call (30 min)
2. Manager interview (60 min)
3. Skills assessment - home-based task + interview (60 min)

---

### 9. PostHog - AI Product Engineer / SWE AI-Enabled Product
Files: [`6953405`](data_raw/6953405_PostHog_AI_Product_Engineer.yaml), [`8277537`](data_raw/8277537_PostHog_Software_Engineer_AI-Enabled_Product_Autonomy.yaml)
1. Call with Talent Partner
2. Technical interview (60 min)
3. Co-founder call (15 min)
4. PostHog SuperDay - paid full day of work

Notable: Paid "SuperDay" where candidates do actual work and are compensated.

---

### 10. Harmonic - Full Stack Product Engineer (AI Search)
File: [`6727775`](data_raw/6727775_Harmonic_Full_Stack_Product_Engineer_AI_Search.yaml)
1. Recruiter screening (20 min)
2. Take-home exam
3. Technical screening: debugging session (45 min) + jam session (1 hour)
4. Behavioral: Head of Engineering (30 min) + CEO (30 min)
5. References

Notable: Unique "jam session" alongside debugging session in technical round.

---

### 11. Nearform - Senior AI Python Software Engineer
File: [`8373891`](data_raw/8373891_Nearform_Senior_AI_Python_Software_Engineer_Perm_USA_Rem.yaml)
1. Talent call (30 min, Zoom)
2. Technical assessment - live coding (1 hour, Zoom)
3. Hiring manager interview (45 min, Zoom)
4. (Possible) additional client interview

Notable: Consulting firm; may include client interview. Live coding via screen sharing.

---

### 12. Lendable - Senior AI Engineer / AI Engineer
Files: [`8316438`](data_raw/8316438_Lendable_Senior_AI_Engineer.yaml), [`8029593`](data_raw/8029593_Lendable_AI_Engineer.yaml)
1. Introductory call (or screening call with HM)
2. Take-home exercise
3. Walkthrough of exercise (or technical interview based on take-home)
4. Meet the day-to-day team
5. Meet the exec team

---

### 13. PA Consulting - Senior Gen AI Developer
File: [`8275583`](data_raw/8275583_PA_Consulting_Senior_Gen_AI_Developer.yaml)
1. Quick call with Tech Recruiter
2. Round 1 (60 min): competency OR technical interview
3. Round 2 (60 min): whichever type wasn't in Round 1
4. Final round (60 min): PA leader + mini case study

Notable: Flexible ordering of competency vs technical rounds. Case study in final round.

---

### 14. XBOW - AI Research Engineer
File: [`7297476`](data_raw/7297476_XBOW_AI_Research_Engineer.yaml)
1. Head of Talent introductory chat (45 min) - Zac Wallis
2. Head of AI conversation (60 min) - Albert Ziegler
3. Technical deep dive / case study (2-3 hours)
4. CEO and founder meeting (30 min) - Oege de Moor

Notable: Named interviewers. 2-3 hour technical deep dive is the longest single stage in the dataset.

---

### 15. Headway - AI Staff SWE / Senior IT Engineer AI Automation
Files: [`8381956`](data_raw/8381956_Headway_AI_Staff_Software_Engineer_Patient.yaml), [`7777666`](data_raw/7777666_Headway_Senior_IT_Engineer_AI_Automation.yaml)
1. Initial screen with recruiting
2. First round: live coding with engineer (or IT Manager for IT role)
3. Final rounds: technical and non-technical interviews
4. References and offer

---

### 16. P-1 AI - 3 roles (AI Product Engineer, Senior SWE Agentic AI, QA Engineer AI)
Files: [`8243631`](data_raw/8243631_P-1_AI_AI_Product_Engineer.yaml), [`8292031`](data_raw/8292031_P-1_AI_Senior_Software_Engineer_-_Agentic_AI_Platform.yaml), [`8243634`](data_raw/8243634_P-1_AI_Software_QA_Engineer_-_AI.yaml)
1. Initial screening call (30 min)
2. Biographical/behavioural interview (45 min)
3. Technical interview (60 min)
4. CEO interview (30 min)

Notable: Same 4-step process across all roles. CEO in every final round.

---

### 17. Mutiny - Senior Software Engineer (AI Products)
File: [`4476482`](data_raw/4476482_Mutiny_Senior_Software_Engineer_AI_Products.yaml)
1. Hiring manager phone screen with CTO (30 min)
2. Technical screen - coding challenge (60 min)
3. Virtual onsite: two 90-min technical + one 60-min culture

Notable: CTO conducts the initial phone screen. Virtual onsite is 4 hours.

---

### 18. Stacks - Staff AI Engineer
File: [`4761860`](data_raw/4761860_Stacks_Staff_AI_Engineer.yaml)
1. Screening call with talent partner - Peter (30 min)
2. Call with founder - Albert (30 min)
3. Call with team member - Ivan (45 min)
4. Take-home + 1-hour on-site panel
5. Meet 3 additional team members
6. Offer

Notable: Highly personalized - names specific individuals. 6-step process including both take-home and on-site.

---

### 19. Melotech - AI/ML Engineer + Intern (same process)
Files: [`8247431`](data_raw/8247431_Melotech_AIML_Engineer.yaml), [`8247435`](data_raw/8247435_Melotech_AIML_Engineer_Intern.yaml)
1. Take-home case study (real-world project)
2. Case interview (90 min) - present and debate results
3. Online assessment - motivational questionnaire + aptitude test
4. Founder interview with CEO (90 min)
5. Team interview
6. Offer

Notable: Company in stealth mode - candidates learn about Melotech progressively through stages. Can go start-to-offer in one week. Same process for intern and senior roles.

---

### 20. Glass Health - Founding AI/Data Engineer
File: [`3564658`](data_raw/3564658_Glass_Health_Founding_AIData_Engineer_Remote.yaml)
1. Initial background / light technical (45 min)
2. Live coding challenge (1 hour)
3. Final: system design + realistic work simulation (live, ~1.5-2 hours)

Notable: Final round combines system design with realistic work simulation. All rounds live (no take-home).

---

### 21. boam - Applied AI Engineer
File: [`8249839`](data_raw/8249839_boam_Applied_AI_Engineer.yaml)
1. Intro call
2. Deep dive - walk through past ML/AI work and production challenges
3. Work sample - solve a real Boam-style ML/AI challenge
4. Founder / leadership conversation

Notable: "Fast, structured, and transparent - built to respect your time."

---

### 22. Lorikeet - Forward Deployed AI Engineer
File: [`8005716`](data_raw/8005716_Lorikeet_Forward_Deployed_AI_Engineer.yaml)
1. Informal chats with cofounders Steve and Jamie
2. Paid 2-day work trial

Notable: "No nonsense recruitment process." Paid work trial. Uses AEDT for initial screening.

---

### 23. Infinity Constellation - Founding AI Engineer
File: [`7309806`](data_raw/7309806_Infinity_Constellation_Founding_AI_Engineer_-_Supernal.yaml)
1. Paid week building something real with the team

Notable: Most unconventional process in the entire dataset. Replaces all traditional interviews with a paid week of real work.

---

### 24. sciemo - AI/ML Engineer
File: [`7780697`](data_raw/7780697_sciemo_AIML_Engineer.yaml)
1. Phone screen
2. Peer interview
3. Founders' interview

Notable: Clean, lean 3-step process. Tiny company (4 employees).

---

### 25. TensorOps - Junior AI/ML Engineer
File: [`8314487`](data_raw/8314487_TensorOps_Junior_AIML_Engineer.yaml)
1. Initial conversation with recruitment
2. Technical interview - no live coding, no take-home
3. Conversation with hiring manager

Notable: Explicitly states no live coding and no take-home assignment.

---

### 26. Zeely - AI Prompt Engineer
File: [`7568516`](data_raw/7568516_Zeely_AI_Admaker_AI_Prompt_Engineer_ComfyUI.yaml)
1. Intro call
2. Test task
3. Final interview
4. Reference check
5. Offer

---

### 27. YLD - Contract Principal Operations Engineer
File: [`8252085`](data_raw/8252085_YLD_Contract_Principal_Operations_Engineer_Automation.yaml)
1. Talent team interview (30-45 min)
2. Two engineers interview (~1h30)
3. Panel: COO + Head of Client Services + Head of People (1h30)

---

### 28. Foxelli Group - AI Engineer (Technical Product Owner)
File: [`8135769`](data_raw/8135769_Foxelli_Group_AI_Engineer_Technical_Product_Owner.yaml)
1. Apply (simple form)
2. Ribbon AI interview - asynchronous AI-powered guided video
3. Manager interview

Notable: Uses Ribbon AI (asynchronous AI video interview tool). Freelance/contract role.

---

### 29. VYNYL - Senior Full Stack Engineer (AI)
File: [`8389528`](data_raw/8389528_VYNYL_Senior_Full_Stack_Engineer_Python_Serverless_AI.yaml)
1. Initial screening email
2. Technical assessment interview
3. Panel interview

Notable: First touchpoint is a screening email (not a call). Candidates must discuss their "preferred agentic tool setup."

---

### 30. Northbeam - AI Operations & Automation Engineer
File: [`8281581`](data_raw/8281581_Northbeam_AI_Operations_Automation_Engineer.yaml)
1. Recruiter interview (30 min)
2. Hiring manager video interview
3. Role-specific video interview
4. Team interviews (video or onsite)
5. CEO/Co-founder interview

Notable: 5-7 interviews total, 5-8 hours of candidate time. CEO final step.

---

### 31. The College Board - Senior AI Engineer
File: [`7602446`](data_raw/7602446_The_College_Board_Senior_AI_Engineer.yaml)
1. Resume/application submission
2. Recruiter phone/video screen
3. Hiring manager interview
4. Performance exercise (live coding or whiteboarding)
5. Panel interview
6. Leadership conversation
7. Reference checks

Notable: One of the longest processes at 7 steps. Explicitly mentions whiteboarding.

---

### 32. Watershed - Software Engineer (AI Product)
File: [`7082017`](data_raw/7082017_Watershed_Software_engineer_AI_product.yaml)
1. 1-2 introductory conversations
2. Skill/experience assessment (varies by role)
3. Virtual or in-person interview panel

---

### 33. SmartAssets - AI/ML Engineer
File: [`7694512`](data_raw/7694512_SmartAssets_AI_Engineer_Machine_Learning_Engineer.yaml)
- Coding challenge as "essential part of selection process" (no other steps described)

---

### 34. Speechify - Multiple roles
Files: [`1393425`](data_raw/1393425_Speechify_Applied_AI_Engineer_Researcher.yaml), [`3203184`](data_raw/3203184_Speechify_AI_Engineer_Researcher_Inference.yaml), [`6591465`](data_raw/6591465_Speechify_Senior_Software_Engineer_AI_Model_Serving.yaml), [`7836400`](data_raw/7836400_Speechify_Senior_Software_Engineer_AI_Model_Serving_-_Berli.yaml), [`7836450`](data_raw/7836450_Speechify_Senior_Software_Engineer_AI_Model_Serving_-_Taipe.yaml)
- "Several technical interviews, aim to complete within 1 week" (no specific steps listed)

---

### 35. BJAK - 3 roles (Android, Backend, iOS Developer AI)
Files: [`8286147`](data_raw/8286147_BJAK_Android_Developer_AI_Apps.yaml), [`8286139`](data_raw/8286139_BJAK_Backend_Engineer_AI.yaml), [`8286159`](data_raw/8286159_BJAK_iOS_Developer_AI_Apps.yaml)
- 3-4 interviews maximum
- Evaluated by technical team members (not recruiters)

---

### 36. Xenon Seven - AI/ML Engineer
File: [`7358381`](data_raw/7358381_Xenon_Seven_AIML_Engineer_-_Join_our_growing_community.yaml)
1. Screening - review of application and experience in Data & AI, ML engineering
2. Technical Assessment - 2-step process: interactive problem-solving test + verbal interview about skills
3. Matching to Opportunity - explore how skills align with ongoing projects

Notable: A staffing/consulting model where the interview is also a matching process to specific projects.

---

### 37. Wing Assistant - MERN Stack Developer (AI Agents)
File: [`8359858`](data_raw/8359858_Wing_Assistant_MERN_Stack_Developer_AI_Agents.yaml)
1. Introductory Call (30 min) - culture, product vision, expectations
2. Technical Task
3. Final Interview (1 hour) - with CEO, CPO & CTO

Notable: Compact 3-step process with full C-suite involvement in the final round.

---

### 38. Qonto - Senior Machine Learning Engineer for AI Product
File: [`8097536`](data_raw/8097536_Qonto_Senior_Machine_Learning_Engineer_for_AI_Product.yaml)
1. Interviews with Talent Acquisition Manager and future managers
2. A remote or live exercise to demonstrate skills
3. Offer

Notable: ~20 working days average process; offers within 48 hours of completion.

---

### 39. Hastings Direct - Lead Quality Engineer, Automation & AI
File: [`8463501`](data_raw/8463501_Hastings_Direct_Lead_Quality_Engineer_-_Automation_AI.yaml)
1. Recruiter screening call
2. Intro call with hiring manager
3. Case study round

Notable: Lean 3-step process ending with a case study rather than live coding.

---

### 40. Phare Health - AI/ML Engineer
File: [`8449234`](data_raw/8449234_Phare_Health_AIML_Engineer.yaml)
1. Intro call - background & mission alignment
2. Technical deep-dives - pseudo-coding exercise and systems design (not Leetcode)
3. Final in-person interview at one of their hubs (SF, NYC, Austin, or Chicago; travel arranged)
4. References
5. Offer

Notable: Explicitly states "not Leetcode." In-person final round with travel arranged for out-of-area candidates.

---

### 41. Doctolib - Senior AI Engineer
File: [`8492018`](data_raw/8492018_Doctolib_Senior_AI_Engineer_xfm.yaml)
1. Recruiter Interview
2. Feature Building Interview
3. AI System Design Interview
4. Behavioral Interview
5. Reference check
6. Offer

Notable: Dedicated "Feature Building Interview" (practical exercise) alongside a separate "AI System Design Interview." Domain-specific technical assessment for AI roles.

---

### 42. Monzo Bank - Senior Staff Software Engineer, AI Customer Operations
File: [`8492197`](data_raw/8492197_Monzo_Bank_Senior_Staff_Software_Engineer_AI_Customer_Operat.yaml)
1. Recruiter Call
2. Initial Call
3. System Design Interview
4. Take-home task or pair coding exercise (candidate's choice)
5. Final interview including behavioral and leadership rounds

Notable: Offers candidates a choice between take-home and pair coding. Publicly shares a senior engineer's blog about the experience. ~3-4 week timeline.

---

### 43. Sprinter Health - Applied AI Senior/Staff Software Engineer, Lead
File: [`8492296`](data_raw/8492296_Sprinter_Health_Applied_AI_-_Senior_Staff_Software_Engineer_Lead.yaml)
1. Recruiter Screen (30 min)
2. Technical Assessment (45 min)
3. Onsite Interview: AI-focused Systems Design + Behavioral + Lunch with the Team (3 hours)
4. References

Notable: AI-focused systems design round. Explicit time estimates for each stage. ~2-3 week process.

---

### 44. Fifth Dimension - AI Engineer (Staff/Principal)
File: [`8507147`](data_raw/8507147_Fifth_Dimension_AI_Engineer_StaffPrincipal.yaml)
1. Submit CV + answers to screening questions
2. Call with CTO to explore initial fit
3. Live task and competency interview
4. In-person culture fit interview with founders and team
5. **Alternative:** Paid one-week trial for available candidates

Notable: Offers a paid one-week work trial as an alternative to the standard interview pipeline. Live task (not take-home). Both founders in culture fit round.

---

### 45. Monarch Money - Software Engineer, AI (Senior/Staff)
File: [`8531817`](data_raw/8531817_Monarch_Money_Software_Engineer_AI_SeniorStaff.yaml)
1. Recruiter Video Call
2. Hiring Manager Video Call
3. Technical Assessment (Live Coding)
4. Virtual Onsite (3 rounds)
5. Reference Checks
6. Offer

Notable: Transparent 6-step process. Live coding (not take-home).

---

### 46. Pattern - AI Engineer II
File: [`8489458`](data_raw/8489458_Pattern_AI_Engineer_-_II_Experience_with_Financial_projec.yaml)
1. Initial phone interview with talent acquisition team
2. Video interview with hiring manager
3. Onsite interview with panel of department leaders
4. Offer review by executive team
5. Offer

Notable: Provides explicit interview preparation tips: "Be prepared to talk about professional accomplishments with specific data," "talk about side projects related to data and analytics."

---

### 47. GoFasti - AI Engineer (Backend focus)
File: [`8591405`](data_raw/8591405_GoFasti_1027-_AI_Engineer_Backend_focus.yaml)
1. Application review/approval
2. Screening interview with GoFasti's team
3. GoFasti builds and sends candidate profile to client
4. Profile review/approval by client
5. Interview with the client
6. Hiring and onboarding

Notable: Staffing agency model with dual screening (agency + client).

---

### 48. RelationalAI - Senior Software Engineer, Symbolic AI
File: [`8590709`](data_raw/8590709_RelationalAI_Senior_Software_Engineer_-_Symbolic_AI.yaml)
- Short screening process followed by 4-5 stage interview loop

Notable: Emphasis on speed ("We move quickly") with full transparency on compensation throughout.

---

### 49. Microstrategy - AI Engineer I / Senior AI Engineer I
Files: [`6178416`](data_raw/6178416_Microstrategy_AI_Engineer_I.yaml), [`6440280`](data_raw/6440280_Microstrategy_Senior_AI_Engineer_I.yaml)
- Online assessments as the first step of recruitment (sent via email)

Notable: Same online assessment process for both junior and senior roles.

---

### 50. Prudential plc (PHI) - Senior AI Engineer
File: [`8561275`](data_raw/8561275_Prudential_plc_PHI_-_Senior_AI_Engineer.yaml)
- Technical interview focuses on: most complex build-from-scratch backend project, architectural sovereignty, system ownership

Notable: Transparent about specific technical interview focus areas, giving candidates time to prepare.

---

### 51. Nearform (UK Perm) - Senior AI Python Software Engineer
File: [`8492964`](data_raw/8492964_Nearform_Senior_AI_Python_Software_Engineer_Perm_UK.yaml)
1. Talent Call (30 min, Zoom)
2. Technical Assessment - live coding challenge (1 hour, Zoom) - build a working solution via screen sharing
3. Hiring Manager Interview (45 min, Zoom)
4. (Possible) additional client interview

Notable: Same structure as US role. Live coding uses "trained interviewers" (standardized evaluation). Detailed description of each step included in posting.

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

### AI-Specific Interview Practices (New)

Notable interview-adjacent practices related to AI:
| Practice | Companies |
|----------|-----------|
| On-camera policy for remote interviews | Arctic Wolf (company-wide: "candidates are expected to be on camera during all video interviews") |
| Anti-fraud / identity verification | Wells Fargo (anti-proxy), Minted (identity verification at start), Deel (deepfake detection), Circle.so ("We do not use AI bots to interview candidates") |
| Application screening questions (written) | Apollo.io (5 written screening questions required), Strange Loop Labs (1-2 page cover letter essay on Engineering Principles) |
| Portfolio/project submission required | Dentsu Creative (GitHub + written opinion on AI implementation), Wolters Kluwer (Statement of Exceptional Work), Waystone (portfolio with measurable impact) |
| Bias-mitigated applications | SimCorp ("exclude personal data such as photo, age, or any non-professional information") |

### Take-Home Challenges

17 of 51 companies (33%) use take-home assignments; 5 more use paid work trials. See [Home Assignments Deep Dive](#home-assignments-deep-dive) for full analysis including format details, time estimates, AI tool policies, and evaluation methods.

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
