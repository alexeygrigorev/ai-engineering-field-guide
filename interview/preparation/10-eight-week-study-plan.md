# Eight-Week Senior AI Interview Study Plan

This plan prepares Product AI Engineer, Forward Deployed Engineer, and ML/AI Platform Engineer candidates in one integrated 8-week cycle. It uses a shared technical core, one focused rotation for each role, and repeated interview simulations. Budget 15-20 focused hours each week.

The goal is not complete coverage. The goal is repeated evidence that you can code, design, deliver, operate, and explain senior-level AI systems under interview constraints.

## Assumptions

This plan assumes:

- You can write production code in one interview language, preferably Python.
- You can reserve at least five study sessions each week.
- You have one substantial project to polish and may have a second project worth preparing. Do not start three new projects.
- You will choose a primary track by the end of week 1 while completing all three role rotations.
- You can use a peer, mentor, interview platform, or independently scored recording for mocks.
- You will ask each target company about format, timing, tool policy, and expected depth instead of inferring the loop from the job title.
- You will treat reading as preparation for a drill, artifact, or mock. Reading alone does not satisfy a weekly gate.

### Evidence-based scheduling rule

Front-load integrator work, then specialize. The market evidence puts building AI systems at 98.1%, productionizing them at 78.3%, evaluation at 68.5%, API integration at 62.4%, agents at 48.4%, and RAG at 42.0%; SQL rose from 9.8% to 34.8%. App-builder and agent archetypes represent 42.5% combined, while platform and DevOps archetypes represent 36.1% combined. Responsibility rates and archetype shares use all 4,894 published postings; the SQL endpoint trend uses only the ai-first subset. I therefore schedule production AI design, RAG, agents, evaluation and observability, practical Python, APIs, SQL, and context engineering before classical ML, deep training, fine-tuning, or niche GPU internals. See [responsibilities](../../role/03-responsibilities.md), [market trends](../../job-market/trends.md), and the [methodology appendix](../../job-market/trends-appendix.md).

These shares overlap conceptually and posting prevalence is not interview frequency. Keep coding, project, and behavioral practice because a job posting cannot predict the loop format. Treat DSA as a confirmed-loop or diagnostic branch, not the default first signal; treat classical or deep training depth, fine-tuning, and GPU internals as title- or job-description-confirmed depth.

If the week 1 diagnostic shows a foundation gap that prevents useful timed practice, extend the plan. Eight weeks is a schedule, not a reason to hide a critical gap.

## Target Outcomes

By the end of week 8, you should have:

- Recent, repeated scorecards for coding or practical implementation, shared AI/ML design, your primary role case, project deep dive, and behavioral interviews.
- Three full 45-60 minute shared AI/ML system-design mocks in weeks 3, 4, and 7, using fresh prompts and the canonical module 09 scorecards.
- No score of 1 in a core dimension in the two most recent mocks for a required format.
- Every core dimension at 3 or higher in two of the three most recent full mocks for a required format.
- Completed focused and full re-tests for previously repeated errors.
- One polished portfolio project and, if useful, a second defensible project rather than several unfinished builds.
- One 20-30 minute primary project deep dive, shorter 60-second and 5-minute versions, and clear answers about ownership, alternatives, failure modes, operations, and outcomes.
- A truthful 12-story bank with distinct evidence for ownership, ambiguity, disagreement, failure, influence, mentoring, prioritization, incidents, strategy, and safety.
- Completed Product AI, FDE, and Platform rotations, with deeper evidence in the primary track and credible adjacent-track answers.
- One take-home practice with a working vertical slice, tests, evaluation, documentation, a decision log, and a live extension.
- A company-specific interview packet for each active process.

## How to Use the Curriculum

Use these modules as one system:

- [Preparation overview](README.md) - Run the diagnostic, choose a profile, and use the common readiness checklist.
- [Common core](01-common-core.md) - Cover Python, APIs, SQL, distributed systems, ML, LLMs, RAG, agents, evaluation, security, observability, latency, cost, and capacity.
- [Coding and LeetCode](02-coding-and-leetcode.md) - Use the prioritized 59-problem set, practical implementation exercises, ML coding, SQL, and spaced repetition.
- [AI/ML system design](03-ai-ml-system-design.md) - Use the 45-60 minute framework, estimation methods, design domains, and anchor walkthroughs.
- [Product AI Engineer](04-product-ai-engineer.md) - Practice product framing, evaluation, UX, launch, iteration, and product cases.
- [Forward Deployed Engineer](05-forward-deployed-engineer.md) - Practice discovery, integration, deployment, customer delivery, escalation, and adoption.
- [ML/AI Platform Engineer](06-ml-ai-platform-engineer.md) - Practice serving, capacity, scheduling, reliability, multi-tenancy, economics, migration, and platform strategy.
- [Senior and staff behavioral](07-senior-staff-behavioral.md) - Build the story bank and calibrate evidence by level.
- [Project deep dives and take-homes](08-project-deep-dives-and-take-homes.md) - Build project dossiers and rehearse a realistic take-home workflow.
- [Mock interviews and scorecards](09-mock-interviews-and-scorecards.md) - Use the canonical 1-4 anchors, re-test schedule, and readiness rules.
- [Master question index](11-master-question-index.md) - Select fresh prompts by format, role, and weakness.
- [Getting Hired](../03-get-hired.md) - Connect this study plan to portfolio, application, and company-specific preparation.

Use module 09 as the canonical scoring system even when another module contains a local rubric. Score each dimension from 1 to 4: 1 is weak or unsafe, 2 is partial, 3 is interview-ready, and 4 is strong senior or staff evidence. Keep dimensions separate and record observable evidence for every score.

## Time Budget

The weekly allocations are:

- Week 1 - 17 hours: coding/implementation 2.5; common technical core 4; system design 2; rotating role track 1; project/behavioral 3.5; mocks/review 4. Cumulative: 17.
- Week 2 - 18 hours: coding/implementation 2.5; common technical core 4.5; system design 1.5; rotating role track 1; project/behavioral 4; mocks/review 4.5. Cumulative: 35.
- Week 3 - 18 hours: coding/implementation 2; common technical core 5; system design 3; rotating role track 1; project/behavioral 3; mocks/review 4. Cumulative: 53.
- Week 4 - 18 hours: coding/implementation 2; common technical core 3; system design 4.5; rotating role track 1; project/behavioral 2.5; mocks/review 5. Cumulative: 71.
- Week 5 - 18 hours: coding/implementation 2; common technical core 2; system design 2.5; rotating role track 4.5; project/behavioral 2; mocks/review 5. Cumulative: 89.
- Week 6 - 19 hours: coding/implementation 2; common technical core 2; system design 1.5; rotating role track 4.5; project/behavioral 3.5; mocks/review 5.5. Cumulative: 108.
- Week 7 - 20 hours: coding/implementation 2; common technical core 2; system design 2.5; rotating role track 5; project/behavioral 2.5; mocks/review 6. Cumulative: 128.
- Week 8 - 17 hours: coding/implementation 1.5; common technical core 1.5; system design 2; rotating role track 3; project/behavioral 5; mocks/review 4. Cumulative: 145.

Charge each activity to one category only. The coding/implementation budget covers new DSA problems and delayed DSA repetitions. SQL, ML implementation, Python concurrency, and API drills use common technical core hours. Progressive exercises, take-home construction, and portfolio implementation use project/behavioral hours. A timed mock, its scoring, and its immediate repair use mocks/review hours. When a listed mock block would exceed that allocation, use its stated compact format rather than counting the same work in two categories.

Category totals across eight weeks:

- Coding/implementation - 16.5 hours
- Common technical core - 24 hours
- System design - 19.5 hours
- Rotating role track - 21 hours
- Project/behavioral - 26 hours
- Mocks/review - 38 hours
- Total - 145 hours

The arithmetic is `16.5 + 24 + 19.5 + 21 + 26 + 38 = 145`.

## Scaling the Plan

Keep the same priority order when available time changes:

1. Repair hard fails and scores of 1.
2. Maintain coding spaced repetition.
3. Prepare the shared core and primary-track interview gates.
4. Run mocks, review evidence, and complete scheduled re-tests.
5. Maintain project and behavioral evidence.
6. Add adjacent-track breadth and optional problems.

### At 10 hours per week

Preserve the sequence and reduce volume:

- Coding/implementation - 2 hours
- Common technical core - 2 hours
- System design - 1.5 hours
- Rotating role track - 1.5 hours
- Project/behavioral - 1 hour
- Mocks/review - 2 hours
- Weekly total - 10 hours

Use one full mock or two focused re-tests each week, not every listed simulation. Read only sections tied to the week's weakest gate. Polish one portfolio project. Add at most 1 new LeetCode problem in a week, stop earlier when readiness is strong, and protect delayed repetitions.

### At 25 hours per week

Preserve the sequence and add depth:

- Coding/implementation - 4 hours
- Common technical core - 4 hours
- System design - 4 hours
- Rotating role track - 4 hours
- Project/behavioral - 3 hours
- Mocks/review - 6 hours
- Weekly total - 25 hours

Use the added time for fresh prompts, second-interviewer scoring, deeper project implementation, target-company variants, and optional coding patterns. Do not use it to add low-value reading or three new projects.

## Weekly Operating Rules

### Coding spaced repetition

The [prioritized LeetCode set](02-coding-and-leetcode.md#prioritized-leetcode-set) contains 46 must-do and 13 optional or stretch problems. It is a priority map, not an eight-week completion quota.

Activate the DSA repetition branch when the target loop confirms DSA or the diagnostic exposes it as a gate. Otherwise, preserve the coding allocation and repetition discipline with practical Python, API integration, SQL, debugging, or progressive implementation prompts, plus occasional transfer problems so a late loop-format change is measurable.

Use these intervals from the [eight-week spaced repetition plan](02-coding-and-leetcode.md#eight-week-spaced-repetition-plan):

- After a clean first solution - repeat after 2, 7, 21, and 42 days.
- After an incorrect solution or material hint - repeat after 1, 3, 7, and 14 days.
- Retire a problem only after two clean timed attempts separated by at least one week.

When the DSA branch is active and initial readiness is mixed, target 10-14 distinct new must-do problems during this plan. Choose them from uncovered patterns and weaknesses exposed by timed work. A strong baseline can reduce the target further. Stop adding new problems as soon as fresh mocks and delayed attempts demonstrate readiness, then use the remaining coding hours for repetition.

The full 59-problem set is an optional ceiling for a longer preparation period, not an eight-week target. The 46 must-do problems define priority order, not required completion. Use optional problems only for a demonstrated weakness or a target-company expectation.

Count a fresh DSA mock prompt toward the 10-14 target when it comes from the prioritized set. Do not add separate problems merely to meet a weekly count.

The selected set is complete only when it covers every weak or high-priority pattern for the target loop and every selected problem has two clean timed attempts separated by at least one week. Readiness additionally requires success on fresh timed transfer problems and the canonical module 09 mock gate. The selected-set size, the full-bank completion count, or any other total problem count cannot establish readiness by itself.

Every coding session must record:

- Prompt and pattern
- First-attempt result and time
- Hint level
- Invariant or decision rule
- Time and space complexity
- Missed tests or edge cases
- Next repetition date

### Post-mock adjustment algorithm

After every mock:

1. Stop the simulation before discussing performance.
2. Score each dimension with the [common 1-4 anchors](09-mock-interviews-and-scorecards.md#common-scoring-scale) and evaluate hard fails separately.
3. Select no more than three feedback items.
4. Choose one next action in this order: unresolved hard fail, score of 1, repeated score of 2, cross-format error, then improvement from 3 toward 4.
5. Name the likely cause and a measurable repair drill.
6. Run an untimed repair within 24 hours.
7. Run a focused re-test with a fresh prompt after 2-3 days.
8. Run a full mock containing the skill after 7 days.
9. Use a different interviewer or independently scored recording after 14 days when possible.
10. Retire the error only after success on two fresh prompts, including one full mock.
11. Move 30-60 minutes from the next week's lowest-priority reading into the repair. Do not remove coding repetition or a scheduled readiness re-test.

If the same error survives two targeted repairs, test the diagnosis. For example, a time-management miss may be weak framing, and vague communication may reflect uncertain technical reasoning.

## Week 1: Baseline and Diagnostic

Total: 17 hours. Cumulative: 17 hours.

Allocation:

- Coding/implementation - 2.5 hours
- Common technical core - 4 hours
- System design - 2 hours
- Rotating role track - 1 hour
- Project/behavioral - 3.5 hours
- Mocks/review - 4 hours

### Objectives

- Establish evidence-based baselines for production AI design, RAG, agents, evaluation, practical Python, APIs, SQL, behavioral, and all three role tracks.
- Select a primary track using target job descriptions and defensible experience.
- Start the error log, coding repetition queue, story bank, and primary project dossier.
- Confirm the tool, timer, recording, and scoring rules used in later mocks.

### Read

- [Preparation overview: Diagnostic and Readiness Assessment](README.md#diagnostic-and-readiness-assessment)
- [Preparation overview: Choose and Emphasize a Track](README.md#choose-and-emphasize-a-track)
- [Common core: How to Use This Module](01-common-core.md#how-to-use-this-module)
- [Common core: Python Runtime, GIL, Async, and Concurrency](01-common-core.md#python-runtime-gil-async-and-concurrency)
- [Common core: API and Backend Engineering](01-common-core.md#api-and-backend-engineering)
- [Common core: SQL and Data Modeling](01-common-core.md#sql-and-data-modeling)
- [Common core: Embeddings, Retrieval, and RAG](01-common-core.md#embeddings-retrieval-and-rag)
- [Common core: Agents and Tool Use](01-common-core.md#agents-and-tool-use)
- [Common core: Evaluations and Experimentation](01-common-core.md#evaluations-and-experimentation)
- [Coding: What Coding Rounds Measure](02-coding-and-leetcode.md#what-coding-rounds-measure)
- [Coding: Repeatable Solve and Review Rubric](02-coding-and-leetcode.md#repeatable-solve-and-review-rubric)
- [Behavioral: Build Answers with SAIL and STAR](07-senior-staff-behavioral.md#build-answers-with-sail-and-star)
- [Behavioral: Build a 12-Story Bank](07-senior-staff-behavioral.md#build-a-12-story-bank)
- [Projects: Select Two or Three Projects](08-project-deep-dives-and-take-homes.md#select-two-or-three-projects), adapted here to one primary project and at most one secondary project
- [Mocks: Session Setup](09-mock-interviews-and-scorecards.md#session-setup)
- [Mocks: Common Scoring Scale](09-mock-interviews-and-scorecards.md#common-scoring-scale)

### Drills and problem targets

- Run the full diagnostic in the preparation overview without notes or AI assistance unless the target interview permits it. Diagnose RAG, agent/tool use, evaluation, observability, and production failure reasoning before testing classical ML depth.
- Run one Python drill covering an iterator or generator, one API drill covering timeout, retry, validation, and error handling, and one compact SQL drill.
- If DSA is confirmed in the target loop or the diagnostic exposes a coding gate, add up to 3 new representative must-do problems from arrays, hash maps, two pointers, or linked lists, counting the baseline mock prompt when it comes from those patterns. Otherwise, use the coding allocation for practical implementation and retain one transfer problem as a loop-format reserve.
- Give 5-minute answers to one prompt from each role module. Score only enough to identify the weakest role-specific dimension.
- Record 12 story candidates as facts and outcomes. Fully draft only the four most reusable stories.

### Tangible deliverables

- Diagnostic scores and a ranked gap list
- Primary and secondary track decision with evidence from 5-10 job descriptions
- Coding log with repetition dates
- Mock error log
- Four completed story worksheets
- One selected primary portfolio project and optional secondary project
- One-page primary project inventory covering problem, users, architecture, personal contribution, evidence, gaps, and planned polish

### Mocks

- Use 4 hours total: one 45-minute practical implementation baseline, one 45-minute behavioral baseline, two focused 10-minute role openings from the [master question index](11-master-question-index.md), 70 minutes of scoring and debrief, and 60 minutes of immediate repair. Use a DSA prompt for the implementation baseline only when the target loop confirms DSA; otherwise use Python, API integration, SQL, debugging, or a progressive exercise.

### Exit and readiness gate

Advance when:

- Both baseline scorecards contain evidence for every score.
- The two highest-value errors have measurable repair drills and re-test dates.
- The primary track choice is supported by target demand and your evidence, not interest alone.
- No confidential project information is present in practice materials.
- Week 2 contains scheduled repetitions for every failed or hinted coding problem.

## Week 2: Coding and Shared Technical Core

Total: 18 hours. Cumulative: 35 hours.

Allocation:

- Coding/implementation - 2.5 hours
- Common technical core - 4.5 hours
- System design - 1.5 hours
- Rotating role track - 1 hour
- Project/behavioral - 4 hours
- Mocks/review - 4.5 hours

### Objectives

- Improve production Python, SQL, API, integration, reliability, and distributed-system reasoning before adding classical ML depth.
- Build a runnable implementation in stages and keep every stage testable.
- Turn the primary project inventory into a layered narrative.
- Repair week 1's weakest coding and behavioral dimensions.

### Read

- [Common core: SQL and Data Modeling](01-common-core.md#sql-and-data-modeling)
- [Common core: Distributed Systems and Reliability](01-common-core.md#distributed-systems-and-reliability)
- [Common core: Prompting and Context Engineering](01-common-core.md#prompting-and-context-engineering)
- [Common core: Embeddings, Retrieval, and RAG](01-common-core.md#embeddings-retrieval-and-rag)
- [Common core: Agents and Tool Use](01-common-core.md#agents-and-tool-use)
- [Common core: Evaluations and Experimentation](01-common-core.md#evaluations-and-experimentation)
- [Coding: Progressive Implementation Exercises](02-coding-and-leetcode.md#progressive-implementation-exercises)
- [Coding: SQL Drills](02-coding-and-leetcode.md#sql-drills)
- [Coding: Python and Concurrency Drills](02-coding-and-leetcode.md#python-and-concurrency-drills)
- [System design: Distributed-System Foundations](03-ai-ml-system-design.md#distributed-system-foundations)
- [Projects: Build a Layered Project Narrative](08-project-deep-dives-and-take-homes.md#build-a-layered-project-narrative)
- [Projects: Project Dossier Template](08-project-deep-dives-and-take-homes.md#project-dossier-template)
- [Mocks: Progressive Implementation](09-mock-interviews-and-scorecards.md#progressive-implementation-75-90-minutes)

### Drills and problem targets

- If DSA is confirmed or remains a diagnostic weakness, add up to 3 new must-do problems from the weakest of sliding window, stacks and queues, binary search, or intervals. Otherwise, run a fresh practical Python or API integration exercise.
- Repeat all week 1 failures on their scheduled dates.
- Timebox four SQL drills to 90 common-core minutes total: join and aggregation, window ranking, deduplication, and session or retention logic.
- Use 2 project/behavioral hours to build the key-value store through TTL and persistence, or an equivalent progressive exercise. Stop with a runnable tested level when the timebox expires.
- Run two 10-minute distributed-systems drills on idempotency, bounded retries, backpressure, and failure ownership.
- Deliver the primary project in 60 seconds and 5 minutes. Answer five ownership and trade-off follow-ups.

### Tangible deliverables

- Runnable progressive implementation with tests
- Four reviewed SQL solutions with grain and null assumptions
- Primary project dossier sections for problem, architecture, decisions, evaluation, operations, results, and reflection
- 60-second and 5-minute project scripts
- Six completed story worksheets, including failure and disagreement
- Updated error log and repetition queue

### Mocks

- Use 4.5 hours total: one 90-minute progressive implementation mock, one 30-minute project deep dive, one 30-minute focused re-test from week 1, and 120 minutes of scoring, debrief, and repair.

### Exit and readiness gate

Advance when:

- Each progressive implementation level remains runnable and reviewed.
- The project narrative distinguishes your decisions from team activity.
- SQL solutions state data grain, null behavior, and expected output.
- Week 1's selected score-of-1 repair has passed a fresh focused re-test or remains explicitly open with a new cause hypothesis.
- Delayed coding repetitions are current; new problem count does not displace them.

## Week 3: Production AI Design, Evaluation, and ML Depth

Total: 18 hours. Cumulative: 53 hours.

Allocation:

- Coding/implementation - 2 hours
- Common technical core - 5 hours
- System design - 3 hours
- Rotating role track - 1 hour
- Project/behavioral - 3 hours
- Mocks/review - 4 hours

### Objectives

- Diagnose RAG, agent, evaluation, observability, and production failures before reaching for model-training depth.
- Design evaluation before architecture and connect offline evidence to release decisions.
- Explain the classical ML and deep-learning concepts required by the target role without hiding behind framework names.
- Add evaluation, safety, observability, and cost evidence to the primary portfolio project.
- Produce the first timed shared AI/ML design.

### Read

- [Common core: Embeddings, Retrieval, and RAG](01-common-core.md#embeddings-retrieval-and-rag)
- [Common core: Agents and Tool Use](01-common-core.md#agents-and-tool-use)
- [Common core: Evaluations and Experimentation](01-common-core.md#evaluations-and-experimentation)
- [Common core: Observability](01-common-core.md#observability)
- [Common core: Prompting and Context Engineering](01-common-core.md#prompting-and-context-engineering)
- [Common core: LLM Inference](01-common-core.md#llm-inference)
- [Common core: Classical Machine Learning and Statistics](01-common-core.md#classical-machine-learning-and-statistics)
- [Common core: Deep Learning and Transformers](01-common-core.md#deep-learning-and-transformers)
- [Coding: ML Coding Drills](02-coding-and-leetcode.md#ml-coding-drills)
- [System design: Classic ML System Design](03-ai-ml-system-design.md#classic-ml-system-design)
- [System design: LLM and RAG Design](03-ai-ml-system-design.md#llm-and-rag-design)
- [Projects: Evaluation Plan Template](08-project-deep-dives-and-take-homes.md#evaluation-plan-template)
- [Mocks: AI/ML System Design](09-mock-interviews-and-scorecards.md#aiml-system-design-45-60-minutes)

### Drills and problem targets

- Add up to 3 new must-do tree or graph problems only when DSA is confirmed or those patterns remain a readiness gate. Otherwise, use the allocation for a fresh evaluation-runner, retrieval, or tool-integration exercise.
- Repeat due sliding-window, binary-search, interval, and week 1 problems.
- Timebox two implementation drills to 100 common-core minutes total: metrics or vector similarity first, then logistic regression or attention only when the title, job description, or diagnostic justifies that depth.
- Run three 10-minute evaluation drills. For each, define the decision, dataset, metrics, slices, graders, and release rule before naming components.
- Run two estimation drills covering tokens, latency, throughput, storage, or provider cost.
- Polish the primary project with a small evaluation set, explicit release criteria, failure slices, and a reproducible evaluation command. If the project is not AI-based, add an equivalent quality and reliability harness instead of forcing an LLM feature.

### Tangible deliverables

- Two reviewed ML implementations
- One evaluation plan with dataset lineage, metrics, slices, and release rule
- One small runnable evaluation harness or equivalent quality harness in the primary project
- One shared AI/ML design recording and scorecard
- Eight completed story worksheets, including an AI quality, data, safety, or cost story where truthful

### Mocks

- Use 4 hours total: the first 60-minute full shared AI/ML design mock, two 15-minute requirements and estimation drills, one 30-minute fresh re-test, and 120 minutes of scoring, debrief, and repair. Minute check: `60 + 15 + 15 + 30 + 120 = 240`.

### Exit and readiness gate

Advance when:

- The design opening states users, decision, quality, scale, risks, and non-goals before architecture.
- At least one estimate changes a design choice.
- The evaluation plan includes critical slices and a release rule rather than one average metric.
- Both ML implementations handle shapes, edge cases, and numerical stability.
- No unresolved safety, privacy, or authorization hard fail exists.

## Week 4: System Design and Midpoint Recalibration

Total: 18 hours. Cumulative: 71 hours.

Allocation:

- Coding/implementation - 2 hours
- Common technical core - 3 hours
- System design - 4.5 hours
- Rotating role track - 1 hour
- Project/behavioral - 2.5 hours
- Mocks/review - 5 hours

### Objectives

- Internalize one reusable 45-60 minute design method.
- Make explicit estimates, APIs, failure boundaries, evaluation, rollback, and evolution.
- Repeat the diagnostic and choose the primary-track-first role order for weeks 5-7.
- Test whether the primary project can survive architecture and operations follow-ups.

### Read

- [System design: The 45-60 Minute Answer Framework](03-ai-ml-system-design.md#the-45-60-minute-answer-framework)
- [System design: Back-of-the-Envelope Estimation](03-ai-ml-system-design.md#back-of-the-envelope-estimation)
- [System design: Agentic Systems](03-ai-ml-system-design.md#agentic-systems)
- [System design: AI Platform and Inference Serving](03-ai-ml-system-design.md#ai-platform-and-inference-serving)
- [System design: Security, Privacy, Safety, and Degradation](03-ai-ml-system-design.md#security-privacy-safety-and-degradation)
- [System design: Enterprise RAG Assistant](03-ai-ml-system-design.md#anchor-walkthrough-1-enterprise-rag-assistant)
- [System design: Multi-Provider Model Gateway](03-ai-ml-system-design.md#anchor-walkthrough-4-multi-provider-model-gateway)
- [Common core: Observability](01-common-core.md#observability)
- [Common core: Cost, Latency, and Capacity](01-common-core.md#cost-latency-and-capacity)
- [Projects: Defend the Architecture](08-project-deep-dives-and-take-homes.md#defend-the-architecture)
- [Mocks: Interviewer Calibration](09-mock-interviews-and-scorecards.md#interviewer-calibration)

### Drills and problem targets

- Add up to 2 new must-do problems from heaps, streams, tries, caches, or concurrency. Select them by diagnostic and target-company relevance.
- Repeat all due tree and graph problems. Do not add new patterns if delayed attempts are failing.
- Complete six estimation drills with units: peak QPS, concurrency, token volume, provider cost, storage, and replica capacity.
- Draw three 15-minute designs: enterprise RAG assistant, support agent, and model gateway.
- Run one 25-minute project architecture defense covering security, observability, incidents, rollback, and rejected alternatives.
- Repeat the preparation overview diagnostic and the [common-core self-assessment](01-common-core.md#self-assessment).

### Tangible deliverables

- Three design sheets with assumptions, estimates, interfaces, critical flows, and degradation
- Six checked calculations with explicit units
- Midpoint diagnostic comparison and a ranked weeks 5-8 repair plan
- Updated primary project architecture diagram and operations notes
- Ten completed story worksheets
- One independently double-scored mock or calibrated transcript
- A second full shared AI/ML design recording and canonical scorecard

### Mocks

- Use 5 hours total: one 60-minute primary-role mock, one 60-minute full shared AI/ML design mock with a fresh prompt, one 20-minute project defense, 100 minutes of scoring and independent double-scoring, and 60 minutes of targeted repair. Minute check: `60 + 60 + 20 + 100 + 60 = 300`.

### Exit and readiness gate

Advance when:

- A fresh design follows the framework without scripted prompting.
- The second full shared AI/ML design mock has a canonical scorecard and a scheduled focused or full re-test for every readiness-limiting error.
- Estimates are dimensionally correct and affect architecture or capacity.
- The answer includes overload, degraded behavior, observability, rollback, and evolution.
- Scoring disagreements greater than 1 point are resolved with evidence.
- Every repeated score of 2 has a targeted drill.
- The midpoint plan names what will be deprioritized, not only what will be added.

## Weeks 5-7: Primary-Track-First Rotation

Choose the order at the week 4 recalibration and keep it for all three slots:

- Balanced/default - Product AI, then Platform, then FDE.
- Product AI primary - Product AI, then Platform, then FDE.
- FDE primary - FDE, then Product AI, then Platform.
- Platform primary - Platform, then Product AI, then FDE.

For each assigned role, execute its market-informed P0 sequence before lower tiers:

- Product AI P0 - [rapid prototypes and end-to-end engineering](04-product-ai-engineer.md#rapid-prototypes-and-end-to-end-engineering), [architecture and model behavior](04-product-ai-engineer.md#architecture-and-model-behavior), [evaluation and experimentation](04-product-ai-engineer.md#evaluation-and-experimentation), and [project deep-dive preparation](04-product-ai-engineer.md#project-deep-dive-preparation).
- FDE P0 - [discovery and scoping](05-forward-deployed-engineer.md#discovery-and-scoping), [customer architecture and integration](05-forward-deployed-engineer.md#customer-architecture-and-integration), and [architecture and deployment](05-forward-deployed-engineer.md#architecture-and-deployment), paired with a Python integration drill.
- Platform P0 - [platform strategy and developer experience](06-ml-ai-platform-engineer.md#platform-strategy-and-developer-experience), cloud operations and the reliability portions of [reliability, security, and economics](06-ml-ai-platform-engineer.md#reliability-security-and-economics), and [Kubernetes concepts](06-ml-ai-platform-engineer.md#kubernetes-concepts). Keep gateways and model lifecycle at P1 and shared evaluation platforms at P2.

FDE remains in every rotation for breadth, but it is specialized: direct-title share among all AI-engineering listings rose from roughly 2.0% to 3.6%, and the dedicated analysis found 146 deduplicated direct-title roles. FDE responsibility and skill rates use that 146-role sample. See [market trends](../../job-market/trends.md), the [appendix](../../job-market/trends-appendix.md), and the [FDE analysis](../../role/06-fde.md). Candidates not targeting customer-facing roles may use one compact FDE case covering discovery, integration, production conversion, and escalation, then redirect the saved role-track time to Product AI or Platform. Do not remove the FDE slot or its readiness evidence.

## Week 5: Rotation Slot 1

Total: 18 hours. Cumulative: 89 hours.

Allocation:

- Coding/implementation - 2 hours
- Common technical core - 2 hours
- System design - 2.5 hours
- Rotating role track - 4.5 hours
- Project/behavioral - 2 hours
- Mocks/review - 5 hours

### Objectives

- Start with the primary track, or Product AI in the balanced/default order.
- Complete the assigned role's P0 sequence before sampling P1-P3.
- Apply the assigned role lens to the primary project and a fresh case.
- Transfer the role framework under time pressure.

### Read and drill

- Follow the assigned role's P0 links above and its answer framework in the relevant role module.
- Repeat due coding problems. Add up to 2 new must-do problems only for a confirmed loop or unresolved readiness gate; otherwise use the time for practical Python, API, SQL, or debugging work.
- Produce one role case packet with users or customers, success criteria, architecture, evaluation, production path, risks, and iteration or migration.
- Implement or specify one role-relevant project improvement with tests or evaluation.
- Prepare two stories that demonstrate the assigned role's ownership and trade-offs.

### Tangible deliverables

- One assigned-role case packet
- One project improvement or decision artifact
- Two assigned-role stories
- Two scored assigned-role drills using canonical module 09 anchors

### Mocks

- Use 5 hours total: one 55-minute assigned-role case, one 35-minute project deep dive, one 25-minute focused role drill, and 185 minutes for the primary-role requirement, scoring, debrief, and repair.
- Because slot 1 is the primary role for every specialized order, use the assigned-role case as the second primary-role mock required by the module 09 cadence. In the balanced/default order, treat Product AI as the default primary for this cadence.

### Exit and readiness gate

Advance when:

- The case starts from the role's user, customer, or internal-platform decision before components.
- Quality, reliability, security, cost, and release or migration criteria are connected.
- Project claims survive technical and evidence probes.
- Any assigned-role score of 1 has an untimed repair and focused re-test scheduled before week 7.

## Week 6: Rotation Slot 2

Total: 19 hours. Cumulative: 108 hours.

Allocation:

- Coding/implementation - 2 hours
- Common technical core - 2 hours
- System design - 1.5 hours
- Rotating role track - 4.5 hours
- Project/behavioral - 3.5 hours
- Mocks/review - 5.5 hours

### Objectives

- Complete the second assigned role's P0 sequence and contrast its ownership boundary with slot 1.
- Build a production path across identity, data, deployment, observability, support, and adoption.
- Complete a strictly timeboxed take-home vertical slice and rehearse a live extension without claiming production readiness.
- Demonstrate accountability in an incident, failure, migration, or difficult stakeholder story.

### Read and drill

- Follow the assigned role's P0 links above and the [take-home operating strategy](08-project-deep-dives-and-take-homes.md#take-home-operating-strategy).
- Add at most 1 new must-do problem only when a target-company pattern remains uncovered; otherwise run a practical integration or debugging drill. Repeat all due problems.
- Produce one architecture map and trace a request through identity, permissions, data, model or platform use, observability, deletion, support, and deployment.
- Spend exactly 3 project/behavioral hours on one role-relevant take-home vertical slice: 20 minutes to plan, 100 minutes to implement, 30 minutes for representative tests, 20 minutes for documentation and demo notes, and 10 minutes to record cuts.
- Prepare one assigned-role incident, migration, escalation, adoption, or launch story.

### Tangible deliverables

- One scored assigned-role opening
- One architecture map and production-path artifact
- One reviewable take-home vertical slice with representative tests, documentation, a decision log, and explicit cuts
- One 5-minute demo script
- One assigned-role story, plus a second only when readiness evidence requires it

### Mocks

- Use 5.5 hours total: one 55-minute assigned-role case, one 75-minute take-home review and live extension, one 40-minute behavioral mock, one 30-minute focused re-test, and 130 minutes of scoring, debrief, and repair.

### Exit and readiness gate

Advance when:

- The opening produces measurable success criteria and named unknowns before solutioning.
- The architecture respects identity, security, deployment, data, reliability, and ownership boundaries.
- The take-home runs, representative tests pass, cuts are explicit, and one live extension succeeds.
- Difficult stories show accountability without invented metrics or blame.

## Week 7: Rotation Slot 3 and Full-Loop Simulation

Total: 20 hours. Cumulative: 128 hours.

Allocation:

- Coding/implementation - 2 hours
- Common technical core - 2 hours
- System design - 2.5 hours
- Rotating role track - 5 hours
- Project/behavioral - 2.5 hours
- Mocks/review - 6 hours

### Objectives

- Complete the third assigned role's P0 sequence and preserve credible breadth across all three tracks.
- Contrast its contracts, failure modes, users, economics, and operating model with the first two slots.
- Run a realistic multi-format loop using the primary role and apply module 09 readiness rules.

### Read and drill

- Follow the assigned role's P0 links above and the [readiness rules](09-mock-interviews-and-scorecards.md#readiness-rules).
- Add no new coding problems unless a target-company requirement exposes a missing must-do pattern. Repeat every due or fragile problem and run one mixed coding set plus one SQL or debugging set.
- Produce one assigned-role design with explicit users, interfaces, SLOs or success metrics, non-goals, overload or degradation, observability, security, cost, and evolution.
- Complete four quantitative or decision drills suited to the assigned role. Add two only when the role is primary or evidence is below 3.
- Prepare one strategy story and one migration, adoption, launch, or customer-delivery story.
- Repeat the common-core self-assessment and compare it with weeks 1 and 4.

### Tangible deliverables

- One assigned-role design and one contrasting variant
- Four checked calculations or decision drills, plus two conditional drills
- One strategy memo with explicit non-goals
- One migration, adoption, launch, or production-conversion plan
- One assigned-role project lens added to the primary project dossier
- Full-loop scorecards and readiness matrix

### Mocks

- Use one 6-hour full-loop block aligned with module 09: 60-minute coding or progressive implementation, the third 60-minute full shared AI/ML design mock, 60-minute primary-role case using Product AI, FDE, or Platform as appropriate, 60-minute combined project and behavioral session, and 120 minutes of scoring, debrief, and repair. Minute check: `60 + 60 + 60 + 60 + 120 = 360`.
- Use at least two interviewers across the block or one independently double-scored recording where possible.

### Exit and readiness gate

Advance when:

- All three role rotations have distinct scored evidence.
- No unresolved hard fail remains.
- No core dimension scores 1 in the two most recent mocks for a required format.
- Previously repeated errors have completed their scheduled focused re-tests.
- The readiness matrix identifies ready, mixed-signal, and not-ready formats without averaging away weak dimensions.

## Week 8: Integration and Company-Specific Simulation

Total: 17 hours. Cumulative: 145 hours.

Allocation:

- Coding/implementation - 1.5 hours
- Common technical core - 1.5 hours
- System design - 2 hours
- Rotating role track - 3 hours
- Project/behavioral - 5 hours
- Mocks/review - 4 hours

### Objectives

- Convert broad preparation into target-company decisions, prompts, and evidence.
- Re-test only readiness-limiting dimensions with fresh prompts.
- Finalize project, story, take-home, logistics, and interviewer questions.
- Taper in the final three days instead of cramming.

### Read

- [Preparation overview: Expected Interview Loop](README.md#expected-interview-loop)
- [Preparation overview: Senior and Staff Expectations](README.md#senior-and-staff-expectations)
- [Preparation overview: Readiness Checklist](README.md#readiness-checklist)
- [Behavioral: Deliver the Story in 30, 90, or 180 Seconds](07-senior-staff-behavioral.md#deliver-the-story-in-30-90-or-180-seconds)
- [Behavioral: Handle Probing Follow-Ups](07-senior-staff-behavioral.md#handle-probing-follow-ups)
- [Behavioral: Questions to Ask Interviewers](07-senior-staff-behavioral.md#questions-to-ask-interviewers)
- [Projects: Prepare for Code Review](08-project-deep-dives-and-take-homes.md#prepare-for-code-review)
- [Projects: Prepare for a Live Extension](08-project-deep-dives-and-take-homes.md#prepare-for-a-live-extension)
- [Mocks: Re-Test Schedule](09-mock-interviews-and-scorecards.md#re-test-schedule)
- [Mocks: Pre-Mock Checklist](09-mock-interviews-and-scorecards.md#pre-mock-checklist)
- [Mocks: Post-Mock Checklist](09-mock-interviews-and-scorecards.md#post-mock-checklist)
- [Getting Hired: Before You Apply](../03-get-hired.md#before-you-apply)
- [Getting Hired: Common Mistakes](../03-get-hired.md#common-mistakes)

### Drills and problem targets

- Add no new coding patterns. Repeat only failed, due, or fragile problems.
- Complete one 60-minute progressive exercise from a blank file under the target company's time and tool policy. Charge it to project/behavioral hours unless it is run as the week's coding maintenance mock.
- Build one company packet per active process:
  - Role and level expectations from recruiter guidance
  - Interview format, duration, and tool policy
  - Product, users, business model, and current technical challenges
  - Relevant engineering posts and public architecture evidence
  - Three likely prompts from the [master question index](11-master-question-index.md)
  - Two project decisions and four stories that best match the role
  - One Product AI, FDE, or Platform case adapted to the company
  - Five questions for interviewers
- Run one 20-minute adversarial project defense.
- Deliver six stories in 90 seconds, then answer two follow-ups each.
- Rehearse the introduction in 30-second and 2-minute versions.

### Tangible deliverables

- Final company-specific packet for each active process
- Final primary project dossier and optional secondary dossier
- Final story bank with 12 truthful, non-duplicative stories
- Final readiness matrix by interview format
- Interview-day checklist and tested environment
- One-page residual-risk plan for every mixed-signal format

### Mocks

- Use 4 hours total: one 50-minute final primary-track mock early in the week, one 20-minute focused re-test for the highest-priority readiness-limiting dimension, one 25-minute coding or design maintenance session, one 90-minute company-specific compact loop, and 55 minutes of scoring, debrief, and repair.
- No heavy full mock in the final three days

### Exit and readiness gate

Use the [module 09 readiness rules](09-mock-interviews-and-scorecards.md#readiness-rules). A required format is ready only when:

- The three most recent full mocks use different prompts.
- At least two mocks were scored by different interviewers or one was independently double-scored.
- Every core dimension scores at least 3 in two of the three mocks.
- No core dimension scores 1 in the most recent two mocks.
- No unresolved hard fail exists.
- Core scope finishes within time in at least two mocks.
- At least one material follow-up is handled without direct rescue in each of the two most recent mocks.
- Previously repeated errors have passed focused and full re-tests.

Role-loop readiness also requires ready evidence for coding or practical implementation, shared AI/ML design, the primary role case, project deep dive, and behavioral. Include take-home evidence when the target loop uses it.

Mark a format mixed signal when evidence is sparse or inconsistent. Do not convert a mixed signal to ready by averaging dimensions. Record the mitigation: ask for format details, schedule another mock if time permits, or enter the interview with a specific pacing and recovery rule.

## Daily Templates

### Weekday template: 2-2.5 hours

Use this for four weekdays:

1. Retrieval warm-up - 15 minutes
   - Re-derive one due coding invariant, estimate, role framework, or story opening without notes.
2. Coding spaced repetition - 35-45 minutes
   - Solve one due problem or complete one focused implementation drill.
3. Weekly deep work - 50-60 minutes
   - Read only the assigned section needed for a drill, then design, implement, calculate, or role-play.
4. Verbal practice - 15-20 minutes
   - Explain one trade-off or answer one follow-up aloud.
5. Review - 10 minutes
   - Update the error log, score evidence, and next repetition date.

When the day contains a full mock, the mock and review replace coding and deep work. Move the coding repetition to the next day; do not silently drop it.

### Weekend template: 4-5 hours

Use one longer block or two separated blocks:

1. Full mock or build block - 90 minutes
2. Break - 20-30 minutes
3. Evidence review and repair - 60 minutes
4. Project, story bank, or role artifact - 60-90 minutes
5. Coding repetitions or calculations - 45 minutes
6. Weekly review and scheduling - 20 minutes

Do not run back-to-back mocks without review. The correction is part of the practice.

## Recovery and Catch-Up Rules

When a day is missed:

1. Keep the next scheduled mock if it tests a high-priority gate.
2. Move due coding repetitions within 24 hours.
3. Preserve focused re-tests for scores of 1, repeated scores of 2, and hard-fail repairs.
4. Reduce reading to the exact section needed for the next drill.
5. Shrink deliverable scope while keeping it runnable and reviewable.
6. Move optional adjacent-track breadth to the following week only if it does not disrupt that week's rotation.
7. Do not double the next day's workload or borrow from sleep.

Cut first:

- Optional or stretch LeetCode problems
- Extra company blog reading
- A second portfolio project
- Polishing diagrams or prose beyond interview utility
- Additional fresh prompts after the required mock and re-test
- Vendor-specific details not named in target roles

Never cut:

- Sleep and recovery before a mock or interview
- Repairs for hard fails or recent scores of 1
- Coding spaced repetition across the eight weeks
- Review and scoring after a mock
- Scheduled re-tests for readiness-limiting errors
- Truthfulness, confidentiality, security, or tool-policy checks
- At least one primary project deep dive and the core story bank

If backlog exceeds 3 hours at the end of a week, do not carry it all forward. Keep only work tied to an unresolved interview gate and delete or defer the rest.

## Progress Trackers

### Weekly tracker

Copy this for each week:

- Week:
- Planned hours:
- Actual hours:
- Coding/implementation:
- Common technical core:
- System design:
- Rotating role track:
- Project/behavioral:
- Mocks/review:
- Weekly total:
- Cumulative total:
- Primary objective:
- Required deliverable:
- Due coding repetitions:
- Full mocks:
- Focused re-tests:
- Highest-priority error:
- Measurable repair:
- Exit gate result: passed, mixed signal, or not passed
- Next-week adjustment:

Confirm that the six category values add to the weekly total before closing the week.

### Coding tracker

- Problem:
- Priority: must-do, optional, or company-specific
- Pattern:
- Selected for eight-week set: yes or no
- Selection reason: diagnostic weakness or target-loop priority
- Attempt date:
- Result: clean, hinted, incorrect, or incomplete
- Time:
- Invariant:
- Complexity:
- Missed cases:
- Next repetition:
- First clean timed attempt:
- Second clean timed attempt at least one week later:
- Status: active, fragile, or retired

### Mock and re-test tracker

- Date:
- Format:
- Prompt:
- Interviewer or scorer:
- Tool policy:
- Core dimension scores:
- Evidence for each score:
- Direct hints:
- Hard fail:
- Finished core scope within time:
- Material follow-up handled:
- Maximum three feedback items:
- Selected next action:
- Likely cause:
- Success criterion:
- Untimed repair date:
- Focused re-test date:
- Full re-test date:
- Independent scoring date:
- Readiness status:

### Story bank tracker

- Story title:
- Primary competency:
- Secondary competencies:
- Senior or staff scope:
- Situation:
- Action and personal decisions:
- Impact with truthful evidence:
- Learning:
- Trade-off:
- Failure or risk:
- Collaborators:
- 30-second version ready:
- 90-second version ready:
- 180-second version ready:
- Follow-up defense complete:
- Best-fit companies or values:

### Project tracker

- Project:
- Role lens: Product AI, FDE, Platform, or shared
- 60-second narrative:
- 5-minute narrative:
- 20-30 minute narrative:
- Architecture:
- Personal contribution:
- Baseline and alternatives:
- Evaluation and tests:
- Reliability and failure modes:
- Security and privacy:
- Cost and latency:
- Deployment and monitoring:
- Incident or learning:
- Outcome evidence:
- Known gaps:
- Next polish task:
- Deep-dive mock scores:

## Interview-Day Checklist

The day before:

- Confirm time zone, format, duration, interviewer names, and tool policy.
- Test camera, audio, network, power, editor, runtime, dependencies, and diagramming method.
- Remove confidential files, credentials, notifications, and unrelated browser tabs.
- Prepare water, paper, charger, and accessibility support.
- Review the company packet, one-page project summary, story index, and top residual risk.
- Stop heavy practice early enough to sleep.

Before the interview:

- Join or arrive early.
- Restate the format and tool policy when unclear.
- Keep visible time checkpoints.
- Use a simple opening: clarify outcome, users, constraints, success, and non-goals.
- State assumptions and units instead of pretending to know missing facts.
- Build a correct baseline before adding complexity.
- Test the highest-risk behavior and name failure handling.
- Ask for a moment to recover rather than bluffing.

At the end:

- Summarize the decision, main trade-off, risks, and next evidence.
- Ask questions about the team's users, interfaces, constraints, operating model, and definition of success.
- Do not disclose confidential details from current or former employers.

After the interview:

- Record prompts, decisions, misses, and evidence while fresh.
- Separate observed performance from anxiety or general impressions.
- Send any appropriate follow-up.
- Apply the post-mock adjustment algorithm only if another interview remains.

## Final Readiness Decision

Use evidence, not completed-page or problem count. Coding readiness requires the selected-set spaced-attempt rule, fresh timed transfer, and module 09's repeated-mock evidence. You are ready when all required formats satisfy module 09's repeated-mock rules and no target-company gate remains untested.

If coding, shared design, project deep dive, behavioral, and the primary role case are ready, begin or continue active interviews. Maintain readiness with one full mock and one targeted drill each week.

If one format is mixed signal, continue interviewing only with a clear mitigation and schedule a fresh mock when possible. If a core format has a recent score of 1, unresolved hard fail, or incomplete re-test, repair it before treating the loop as ready.

The plan ends at 145 scheduled hours. Strong readiness can justify doing fewer new problems or less reading, but it does not justify skipping repeated mocks, delayed retrieval, or evidence-based scoring.
