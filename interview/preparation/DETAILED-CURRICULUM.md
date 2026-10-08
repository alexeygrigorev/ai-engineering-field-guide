# AI Engineering Interview Preparation Hub

This is the one place to start when preparing for AI engineering interviews.
It is an eight-week default curriculum for Product AI Engineer, Forward
Deployed Engineer, and ML/AI Platform Engineer roles, with a shorter route when
time is limited. It assumes 15-20 focused hours each week only for the full
version; the diagnostic decides what to skip.

The goal is not to memorize every topic. The goal is to show that you can clarify an ambiguous problem, choose an appropriate design, deliver it in production, measure whether it works, and explain the trade-offs. Use the diagnostic below to decide where to spend your limited preparation time.

This curriculum extends the repository's [interview guide](../README.md). Read [Getting Hired](../03-get-hired.md) for broader preparation and hiring guidance.

## Start here: one hub, four connected sources

```text
                         THIS PAGE
                             |
          +------------------+------------------+
          |                  |                  |
       diagnose          learn/build         practice
          |                  |                  |
          v                  v                  v
   role + gap map      selected lessons     timed answers
          |                  |                  |
          +------------------+------------------+
                             |
                             v
                    SlotSense examples
              production evidence and stories
```

Use this page as the control panel. Follow links outward only for the current
topic, then return here to record the result.

| Source | Use it for | Do not use it for |
|---|---|---|
| This field guide | Job-market evidence, role priority, diagnostic, schedule, and readiness | Treating a study chapter as project evidence |
| [AI Engineering from Scratch](../../../ai-engineering-from-scratch/README.md) | Filling foundation gaps by running lessons and keeping artifacts | Reading all 523 lessons linearly |
| [AI System Design Guide integration](12-ai-system-design-guide-integration.md) | Selecting interview questions, frameworks, whiteboards, RAG/agent/eval/ops references | Replacing your own implementation or measurements |
| `~/slotsense` production workspace | Studying real production patterns, incidents, evals, and delivery decisions | Treating every repository or planned feature as completed production evidence |

The field guide remains the source for market analysis. The other repositories
are learning and evidence sources connected from this hub.

## Your default route

Use this sequence unless a target job description gives stronger evidence for a
different order:

1. Diagnose gaps and choose a primary role track.
2. Learn only the missing foundation from `ai-engineering-from-scratch`.
3. Study one SlotSense production example related to that topic and extract the decision.
4. Use the system-design guide to practice the matching design questions.
5. Save a test, evaluation, trace, decision, or failure as evidence.
6. Practice the answer aloud and record it in the interview log.
7. Review three target postings weekly and adjust emphasis, not the whole plan.

```text
job requirement -> study lesson -> production example -> evidence -> interview answer
```

## Targeted `ai-engineering-from-scratch` route

The source repository is broad. For your AI Engineer goal, use these focused
parts when the diagnostic shows a gap:

### AI application core

- [Phase 11: LLM Engineering](../../../ai-engineering-from-scratch/phases/11-llm-engineering/)
  - prompt engineering, structured outputs, embeddings, context engineering,
    RAG, function calling, evaluation, caching/cost, guardrails, and a
    production app;
  - prioritize lessons 01, 03-07, 09-13, and 16-17.
- [Phase 13: Tools and Protocols](../../../ai-engineering-from-scratch/phases/13-tools-and-protocols/)
  - tool contracts, structured output, MCP, OAuth, OpenTelemetry GenAI,
    routing, reliability, and supply-chain controls;
  - start with lessons 01-05, then use the focused MCP route only when a real
    client and use case justify it.
- [Phase 14: Agent Engineering](../../../ai-engineering-from-scratch/phases/14-agent-engineering/)
  - agent loops, tools, workflow patterns, memory, and LangGraph stateful
    graphs;
  - prioritize lessons 01, 06, 12, and 13 before framework comparisons.

### Production and evaluation depth

- [Phase 17: Infrastructure and Production](../../../ai-engineering-from-scratch/phases/17-infrastructure-and-production/)
  - prioritize LLM observability, model routing, AI gateways, progressive
    delivery, load testing, SRE for AI, security, and FinOps;
  - defer GPU fleet, vLLM internals, multi-region, and accelerator lessons
    unless a target role requires them.
- [Phase 19: Capstone Projects](../../../ai-engineering-from-scratch/phases/19-capstone-projects/)
  - use the production RAG system, eval pipeline, observability, and safety
    capstones as practice references;
  - use capstones to deepen a current production example; do not start another
    large project simply to collect tools.

Every lesson you complete should leave one small artifact: a command output,
test, diagram, benchmark, eval case, or code change. Link that artifact from
the interview answer rather than claiming the lesson itself as experience.

## How the other interview reference fits

Use the [AI System Design Guide integration](12-ai-system-design-guide-integration.md)
for the route through its 128 questions, answer frameworks, whiteboard
exercises, case studies, and dated market chapter.

The practical rule is:

- use `ai-engineering-from-scratch` to understand and build;
- use `ai-system-design-guide` to rehearse and compare designs;
- use SlotSense production examples to discuss ownership, trade-offs, failures,
  and operational judgment;
- use this field guide to choose what matters for the jobs you want.


## Market-Weighted Priority

Use this as the default allocation before the diagnostic, target job descriptions, and recruiter guidance provide better evidence:

- P0 - 40.0%: production AI system design, RAG, agents, and evaluation
- P1 - 30.0%: Python, APIs, SQL, prompt and context engineering, and enterprise workflows
- P2 - 20.0%: cloud, containers, reliability, security, privacy, and compliance
- P3 - 10.0%: role-specific deep ML, GPU and inference internals, self-hosting, and fine-tuning

This ordering follows repository job-market evidence. [Responsibilities](../../role/03-responsibilities.md) show build and implement AI systems in 98.1% of postings, deployment in 78.3%, evaluation and quality in 68.5%, API and service integration in 62.4%, agents in 48.4%, RAG in 42.0%, and security and compliance in 40.1%. [Market trends](../../role/07-trends.md) identify RAG app builder at 25.6%, cloud and ML platform engineer at 21.3%, and agent builder at 16.9%; the integrator stack rose from 73.6% to 77.9% while the trainer stack fell from 36.1% to 27.2%. Responsibility rates and archetype shares use all 4,894 published postings; integrator/trainer and SQL trends use only the ai-first subset. The [trends appendix](../../role/08-trends-appendix.md) documents the clustering and monthly endpoints, including SQL rising from 9.8% to 34.8%.

Posting prevalence is a demand signal, not a direct estimate of how often a topic appears in interviews. The balanced curriculum deliberately preserves breadth across possible interview gates; that breadth is not a claim about market share and should not force equal study time.

Apply title-conditioned overrides after the default allocation:

- Product AI - move time toward P0 evaluation, RAG, agents, and product workflows; keep Python, APIs, and integration at P1 and full-stack implementation at P2.
- Forward Deployed Engineer - move time toward P0 production delivery, customer discovery, Python, and integration; keep evaluation at P1.
- ML/AI Platform Engineer - move time toward P0 cloud, `Kubernetes`, `Docker`, `CI/CD`, and reliability; keep gateways and model lifecycle at P1 and shared evaluation platforms at P2. Promote P3 serving, GPU, and inference depth only when the job description or confirmed loop requires it.

Fine-tuning appears in 13.8% of responsibilities and self-hosting in 2.5% in the [responsibility analysis](../../role/03-responsibilities.md). Keep decision literacy for both, but do not let them displace the default production and integration spine without role evidence.

## Recent Role-Specific Job Postings

This role-balanced sample contains three Product AI, three FDE, and three AI Platform postings from the latest `2026-07-22` data snapshot. It is sorted by the source `posted_date` in descending order, so the most recent postings appear first. Jobs with the same date are grouped together. Treat availability as historical because employers can close or change postings after collection.

| Posted | Track | Job | Interview signals |
|---|---|---|---|
| 2026-07-22 | Product AI | [Sr Full-Stack AI Engineer](https://builtin.com/job/sr-full-stack-ai-engineer-remote/10304351) - Superbench, Bengaluru or remote | RAG, multi-agent workflows, MCP, full-stack delivery, APIs, evaluation |
| 2026-07-22 | Product AI | [Senior Applied AI Engineer](https://www.builtinla.com/job/senior-applied-ai-engineer-position-statements/9949812) - Pivotal Health, Santa Monica | Production ownership, evaluation, agents, RAG, observability, Python and SQL |
| 2026-07-22 | Product AI | [Product Engineer, AI](https://builtin.com/job/product-engineer-ai/9960458) - Kestra | Agent workflows, rapid prototypes, full-stack product delivery, cloud and Kubernetes |
| 2026-07-22 | FDE | [Forward Deployed AI Engineer](https://builtin.com/job/forward-deployed-ai-engineer-genai-aws/10299613) - Provectus | Customer discovery, enterprise GenAI deployment, AWS, integration |
| 2026-07-22 | FDE | [Forward Deployed AI Engineer](https://builtin.com/job/forward-deployed-ai-engineer/9956515) - ICEYE, Berlin | Secure deployment, RAG, agents, MCP, data fusion, Docker and Kubernetes |
| 2026-07-22 | AI Platform | [Sr. AI Infrastructure Engineer](https://www.builtinla.com/job/senior-ai-infrastructure-engineer-llm-ai-platforms/10081292) - CrowdStrike, remote USA | GPU infrastructure, serving, lifecycle management, evaluation, MLOps |
| 2026-07-21 | AI Platform | [Senior Software Engineer, Search and AI Platform](https://builtin.com/job/senior-software-engineer-i-search-and-ai-platform/9910372) - RELX | Search APIs, knowledge graphs, AWS data services, Kubernetes, monitoring |
| 2026-07-21 | AI Platform | [Senior Software Engineer, AI Platform](https://www.builtinla.com/job/senior-software-engineer-ai-platform-us/10296834) - PointClickCare, USA | Kubernetes, CI/CD, identity, observability, vector databases, model deployment |
| 2026-07-21 | FDE | [Forward Deployed AI Product Engineer](https://www.builtinla.com/job/forward-deployed-ai-product-engineer/9935531) - Tribe AI, USA | User discovery, client delivery, RAG, agents, full-stack production hardening |

Source: [raw job postings](../../job-market/data_raw/2026-07-22/) and [structured extractions](../../job-market/data_structured/2026-07-22/). The interview signals summarize the responsibilities and skills in those records rather than claiming a confirmed interview format.

## Who This Guide Is For

Use this guide if you already have substantial experience in software engineering, machine learning, data, infrastructure, technical consulting, or production AI and want to prepare for senior-level interviews. It is especially useful when your experience is strong but uneven across coding, AI systems, product delivery, infrastructure, or customer work.

The guide expects that you can already write production code in at least one language. It does not require equal depth in every track. It does require enough shared foundation to reason about APIs, data, models, evaluation, reliability, security, latency, and cost.

If you are still building those foundations, start with the [AI engineering learning paths](../../learning-paths/README.md) and extend the schedule beyond eight weeks. If you need stronger project evidence, use the [portfolio guide](../../portfolio/README.md) before starting intensive mock interviews.

## The Four Preparation Profiles

Treat these as preparation profiles, not rigid job-title definitions. Actual responsibilities vary by company, team, product, and customer. Read the job description, ask the recruiter what each interview evaluates, and adjust the emphasis.

### Balanced and shared core

Choose the balanced profile when you are applying across multiple role families or have not yet selected a specialty.

Emphasize:

- Production-quality Python, APIs, SQL, testing, and debugging
- ML and LLM fundamentals
- Evaluation, observability, security, cost, and latency
- Coding and AI system design
- Project deep dives and senior behavioral stories
- Enough exposure to all three role tracks to recognize where your evidence is strongest

This profile gives you broad coverage, but it is not permission to stay shallow. Pick at least one area in which you can defend decisions from requirements through production outcomes.

### Product AI Engineer

Choose this profile when the role centers on building user-facing AI capabilities and improving them through product and evaluation feedback.

Emphasize:

- Product framing and selecting the right AI capability for the user problem
- Full-stack delivery, API integration, and rapid but maintainable prototyping
- RAG, agents, structured outputs, model selection, and fallback behavior
- Offline and online evaluation, experimentation, feedback loops, and UX
- Safety, privacy, quality, latency, and cost as product constraints
- Evidence that you shipped, measured, learned, and iterated

A strong candidate can connect model behavior to user experience and business outcomes rather than discussing the model in isolation.

### Forward Deployed Engineer

Choose this profile when the role combines customer discovery, technical delivery, integration, and production ownership.

Emphasize:

- Requirements discovery when the problem or success criteria are unclear
- Customer communication, expectation setting, and scope negotiation
- Integration with unfamiliar APIs, data, identity, security, and cloud environments
- Fast proof-of-concept work followed by a credible path to production
- Deployment, incident response, handoff, adoption, and field-to-product feedback
- Architecture explanations that work for both technical and nontechnical audiences

The repository's [FDE role analysis](../../role/06-fde.md) provides evidence about recurring responsibilities and skills in current postings. Use it to understand the role category, not to infer the interview process of a specific employer.

### ML/AI Platform Engineer

Choose this profile when the role centers on shared infrastructure for training, inference, evaluation, or AI application teams.

Emphasize:

- Distributed systems, cloud infrastructure, containers, orchestration, and networking
- Model serving, gateways, batching, caching, routing, and capacity planning
- Reliability, observability, incident response, and service-level objectives
- Multi-tenancy, isolation, access control, data governance, and safe deployment
- GPU or accelerator utilization, scheduling, throughput, latency, and cost
- Platform interfaces, developer experience, migration strategy, and adoption

A strong platform answer serves internal users as well as infrastructure. Explain the contract offered to application teams, the operational model behind it, and how you would measure adoption and reliability.

### Compare the profiles directly

- Balanced and shared core
  - Focus - Broad senior AI engineering judgment with enough exposure to product, customer delivery, and platform work to pursue more than one role family.
  - Interview emphasis - Coding, AI system design, project depth, behavioral evidence, and representative cases from all three specialized tracks.
  - Evidence expected - End-to-end production ownership plus one defensible area of depth.
  - Common gaps - Broad vocabulary without deep examples, unclear role preference, or equal study time spent on low-priority topics.
- Product AI Engineer
  - Focus - User-facing AI features that improve through evaluation, experimentation, and product feedback.
  - Interview emphasis - Product framing, full-stack delivery, AI application design, evaluation, UX, and iteration.
  - Evidence expected - A shipped feature with clear user need, technical trade-offs, quality measures, and learning after release.
  - Common gaps - Prototype-only experience, weak evaluation, model-first thinking, or no connection between technical metrics and user outcomes.
- Forward Deployed Engineer
  - Focus - Customer discovery, integration, deployment, and production outcomes in constrained environments.
  - Interview emphasis - Ambiguous cases, discovery role plays, customer architecture, scoping, implementation, and incident judgment.
  - Evidence expected - A customer or stakeholder problem taken from unclear requirements to adoption or a supported production result.
  - Common gaps - Strong demos without a production path, weak expectation management, shallow integration detail, or no account of customer trade-offs.
- ML/AI Platform Engineer
  - Focus - Reliable shared infrastructure for model, evaluation, or AI application workloads.
  - Interview emphasis - Distributed systems, model serving, capacity, reliability, multi-tenancy, observability, and cost.
  - Evidence expected - A platform or infrastructure change with clear interfaces, operational results, adoption, and migration reasoning.
  - Common gaps - Infrastructure discussed without internal-user needs, missing capacity estimates, weak failure isolation, or no rollout and adoption plan.

## Diagnostic and Readiness Assessment

Complete this assessment before week 1 and repeat it at the end of weeks 4 and 7. Do the exercises without notes, search, or an AI assistant unless the interview you are preparing for explicitly permits those tools.

Score each capability:

- 0 - I cannot complete or explain it without substantial help
- 1 - I can make progress, but I miss important details or need prompts
- 2 - I can complete it independently and defend alternatives, risks, and failure modes

### Shared-core capabilities

- Solve a medium-difficulty coding problem in 35-45 minutes, test it, and state time and space complexity.
- Build or debug a small Python API that calls a model or retrieval service and handles timeouts, retries, validation, and errors.
- Write SQL that joins, aggregates, filters, and ranks realistic product or operational data.
- Explain training, inference, embeddings, attention, fine-tuning, RAG, tool use, and evaluation at the depth required by your target role.
- Design an AI feature from requirements through deployment, evaluation, monitoring, and rollback.
- Estimate traffic, tokens, storage, throughput, latency, and cost with explicit assumptions.
- Identify security and safety risks such as prompt injection, data leakage, excessive tool permissions, and untrusted output handling.
- Present one project for 15 minutes, then answer detailed questions about decisions, failures, metrics, and your personal contribution.
- Tell six distinct senior-level stories covering ownership, disagreement, failure, influence, mentoring, and ambiguous execution.

### Role-specific capabilities

For Product AI Engineer:

- Turn a user problem into a measurable AI product hypothesis.
- Design an evaluation set and explain how offline results connect to user outcomes.
- Make a model, UX, latency, quality, and cost trade-off without hiding uncertainty.

For Forward Deployed Engineer:

- Run a discovery conversation and convert ambiguous needs into scope, constraints, and acceptance criteria.
- Design around a customer's existing data, security, deployment, and operational constraints.
- Explain how a proof of concept becomes a supported production system.

For ML/AI Platform Engineer:

- Design a multi-tenant model-serving or evaluation platform with clear interfaces and failure boundaries.
- Reason about capacity, scaling, scheduling, backpressure, reliability, and cost.
- Explain rollout, observability, incident response, and migration for a shared platform.

### Interpreting the result

Add the nine shared-core scores for a shared-core total from 0 to 18. Add the three scores under each specialized profile separately for a Product AI, FDE, and Platform track score from 0 to 6.

For a specialized profile, add the shared-core total and that profile's track score. The result ranges from 0 to 24.

For the balanced profile, average the three track scores and round to the nearest whole number, then add that number to the shared-core total. The result also ranges from 0 to 24. Keep all three track scores visible because the average can hide a weak area.

Use these ranges to prioritize preparation:

- 0-10 - Foundation gap. Extend the timeline and use the learning paths before intensive interview simulation.
- 11-16 - Developing. Follow the eight-week schedule and spend most deliberate practice on zeros and interview-critical ones.
- 17-20 - Practice ready. Keep targeted review, but shift substantial time to timed drills, mocks, and follow-up questions.
- 21-24 - Simulation ready. Emphasize realistic mocks, adversarial follow-ups, project defense, and company-specific preparation.

These ranges are planning heuristics, not a prediction of an interview result. A score of 2 should reflect demonstrated performance under the stated constraints, not familiarity with the topic.

Do not let a high total hide a critical zero. Coding, system design, project evidence, and communication can each be independent interview gates. Confirm which ones matter for your target role.

## Choose and Emphasize a Track

Choose a primary track using evidence, not only interest:

1. Collect 5-10 target job descriptions.
2. Mark the repeated responsibilities, required skills, and interview signals.
3. Map each requirement to a project, incident, design, or leadership story from your experience.
4. Select the track with the strongest overlap between target demand and evidence you can defend.
5. Name a secondary track that fills likely gaps without displacing the shared core.

Select the balanced profile when your current applications span two or more role families, when you have not chosen a target family, or when your top two role-track diagnostic scores are within 1 point and the target job descriptions do not establish a clear specialization. Otherwise, select the specialized profile best supported by both the target jobs and your evidence. Do not select a profile from the diagnostic score alone.

Use these starting allocations for preparation time, then adjust after the diagnostic:

- Balanced - 60.0% shared core, 15.0% Product AI, 15.0% FDE, and 10.0% Platform
- Product AI - 55.0% shared core, 35.0% Product AI, and 10.0% adjacent-track work
- FDE - 50.0% shared core, 40.0% FDE, and 10.0% adjacent-track work
- Platform - 55.0% shared core, 35.0% Platform, and 10.0% adjacent-track work

Adjacent-track work should reinforce the target role. A Product AI candidate might borrow platform observability and serving exercises. An FDE candidate might borrow Product AI evaluation and Platform integration exercises. A Platform candidate might borrow product discovery to improve internal platform design.

Rebalance at the end of each week. If a mock exposes an interview-critical weakness, move time toward it even when it is outside your preferred track.

## Expected Interview Loop

There is no universal AI engineering interview process. A company may omit, combine, reorder, or repeat any of these categories. Ask the recruiter for the format, timing, tool policy, evaluation criteria, and expected role level.

Prepare for some combination of:

1. Recruiter or hiring-manager screen - motivation, role alignment, experience scope, constraints, and communication.
2. Technical screen - coding, debugging, SQL, ML fundamentals, or discussion of a past project.
3. Coding round - algorithms, practical Python, data manipulation, API work, ML implementation, or code review.
4. System-design round - software, ML, AI application, agent, serving, or platform architecture.
5. Role case - product framing, customer discovery, deployment planning, incident response, platform design, or prioritization.
6. Project deep dive - decisions, alternatives, failures, metrics, individual contribution, and lessons.
7. Behavioral and leadership rounds - ownership, conflict, influence, mentoring, execution, and judgment.
8. Take-home or live working session - implementation, analysis, architecture, presentation, or a customer-style scenario.

Do not invent company-specific expectations from a job title. Use the company's own instructions and recruiter guidance as the source of truth.

## Use the Curriculum Modules

The modules are designed to be used together. Start with the diagnostic, study the shared core, add one primary role track, and convert reading into timed practice.

1. [`01-common-core.md`](01-common-core.md) - Build the shared foundation in Python, SQL, APIs, distributed systems, ML, LLMs, security, evaluation, latency, and cost. Use your diagnostic zeros and ones to set priorities.
2. [`02-coding-and-leetcode.md`](02-coding-and-leetcode.md) - Practice prioritized algorithm patterns, practical coding, ML implementation, and SQL. Track correctness, time, testing quality, and explanation quality rather than counting completed problems alone.
3. [`03-ai-ml-system-design.md`](03-ai-ml-system-design.md) - Learn one reusable design method, then apply it to software, ML, RAG, agentic, multimodal, serving, and platform prompts. Practice estimates and failure analysis aloud.
4. [`04-product-ai-engineer.md`](04-product-ai-engineer.md) - Use this as the primary role module for product-facing AI work. Convert each topic into a product decision, evaluation plan, and shipped-project example.
5. [`05-forward-deployed-engineer.md`](05-forward-deployed-engineer.md) - Use this as the primary role module for customer-facing delivery. Practice discovery, scope, integration, deployment, and difficult customer scenarios as role plays.
6. [`06-ml-ai-platform-engineer.md`](06-ml-ai-platform-engineer.md) - Use this as the primary role module for AI infrastructure. Draw designs, estimate capacity, define interfaces, and rehearse operational follow-ups.
7. [`07-senior-staff-behavioral.md`](07-senior-staff-behavioral.md) - Build a reusable story bank with specific decisions, outcomes, and learning. Prepare different evidence for senior execution and staff-level influence.
8. [`08-project-deep-dives-and-take-homes.md`](08-project-deep-dives-and-take-homes.md) - Prepare two project narratives and a repeatable take-home workflow. Audit whether the artifacts prove production judgment rather than only implementation speed.
9. [`09-mock-interviews-and-scorecards.md`](09-mock-interviews-and-scorecards.md) - Run timed mocks and score observable behavior. Turn every weak score into a specific drill for the next week.
10. [`10-eight-week-study-plan.md`](10-eight-week-study-plan.md) - Follow the 15-20 hour weekly schedule, deliverables, mock cadence, and readiness gates. Replace low-value review with drills when you already know a topic.
11. [`11-master-question-index.md`](11-master-question-index.md) - Select questions by interview type, track, and weakness. Use it for retrieval practice and mock assembly, not as a list of answers to memorize.
12. [`12-video-resources.md`](12-video-resources.md) - Talks worth watching, grouped by the topic they support. Watch inside a preparation slot and record what changed in your mental model.

The modules may link back to the repository's existing interview research. Use [Getting Hired](../03-get-hired.md) for preparation patterns and the [portfolio guide](../../portfolio/README.md) to strengthen projects that lack realistic inputs, tests, evaluation, monitoring, or a clear account of trade-offs.

## Eight-Week Operating Rhythm

The detailed schedule lives in `10-eight-week-study-plan.md`. Use this rhythm throughout:

- Spend 15-20 hours each week across learning, implementation, verbal practice, and mocks.
- Keep at least half of the schedule active: solve, design, build, debug, explain, or role-play.
- Maintain an error log with the failure, likely cause, corrected approach, and next repetition date.
- Produce one visible weekly artifact such as a design, implementation, scorecard, project narrative, or recorded explanation.
- Run the readiness assessment again after week 4 and narrow the remaining work.
- Shift the final two weeks toward full interview simulations and target-company context.

A practical session structure is:

1. Attempt the problem under interview constraints.
2. Review the result against a rubric or reference.
3. Record one or two concrete gaps.
4. Repeat the weak part without notes.
5. Schedule a later retrieval attempt.

Reading can support this loop, but reading alone does not demonstrate interview readiness.

## Senior and Staff Expectations

At senior level, show that you can independently own an ambiguous, production-relevant problem. Your answers should connect requirements to architecture, execution, measurement, operations, and iteration.

Senior evidence should include:

- Clear scoping and assumptions before implementation
- Decisions between credible alternatives, including why the rejected options were wrong for the context
- Production failure modes, detection, mitigation, rollback, and learning
- Quantified or directly observable outcomes where your experience supports them
- Security, privacy, reliability, quality, latency, and cost as design inputs
- Collaboration across engineering, product, data, security, operations, or customer teams
- Honest boundaries around your personal contribution and unknowns

At staff level, doing a harder individual project is not enough. Show leverage beyond your own execution.

Staff evidence should include:

- Setting technical direction across teams or a meaningful organizational boundary
- Creating interfaces, standards, platforms, or decision frameworks that enable other engineers
- Resolving disagreement through evidence and aligning people with different incentives
- Sequencing a multi-stage investment under uncertainty rather than designing only the final state
- Managing migrations, adoption, operational ownership, and long-term maintenance
- Developing engineers and improving the quality of decisions around you
- Connecting technical strategy to customer, product, risk, and business constraints

Do not inflate a story to sound staff-level. A precise senior story is stronger than a vague claim of organization-wide impact. If your evidence does not match the advertised level, identify the gap early and discuss leveling explicitly with the recruiter.

## Readiness Checklist

You are ready to begin active interviewing when most of these statements are true and none of the target company's likely gates remains untested.

### Target and plan

- [ ] I have selected a primary preparation profile and 5-10 representative job descriptions.
- [ ] I know which interview categories my target companies use, or I have questions ready for the recruiter.
- [ ] I completed the diagnostic under realistic constraints and prioritized the resulting gaps.
- [ ] I can sustain the remaining weekly schedule without relying on last-minute cramming.

### Technical execution

- [ ] I can solve representative coding and SQL tasks within the expected time while explaining and testing my work.
- [ ] I can explain the ML and LLM fundamentals that appear in my target roles without hiding behind framework names.
- [ ] I can design at least three relevant systems from requirements through operations and rollback.
- [ ] I can estimate scale, latency, throughput, storage, model usage, and cost with explicit assumptions.
- [ ] I include evaluation, observability, security, privacy, and failure handling in AI system answers.

### Role depth

- [ ] I can complete a realistic case for my primary track and defend the trade-offs.
- [ ] I can explain how my primary track works with product, customer, application, data, security, and infrastructure partners.
- [ ] I have at least two examples that prove role-relevant judgment in production.
- [ ] I can answer adjacent-track follow-ups without losing depth in my primary track.

### Senior or staff evidence

- [ ] I have two project deep dives with clear personal contribution, decisions, failures, and outcomes.
- [ ] I have distinct stories for ownership, ambiguity, disagreement, failure, influence, mentoring, and prioritization.
- [ ] My examples match the scope of the level I am targeting.
- [ ] I can explain what I would change now without discrediting the original decision.
- [ ] I can state uncertainty, ask for missing information, and revise a position when evidence changes.

### Interview simulation

- [ ] I have completed timed mocks for coding, design, project deep dive, behavioral, and my primary role case.
- [ ] I used scorecards and repeated weak sections instead of relying on general impressions.
- [ ] I can present a concise introduction and adapt it to the role.
- [ ] I have tested my setup, editor, diagramming method, audio, video, and tool policy for remote rounds.
- [ ] I have prepared thoughtful questions about the team's problems, interfaces, constraints, and definition of success.

## Start Here

1. Read the [existing interview overview](../README.md) and [Getting Hired](../03-get-hired.md).
2. Complete the diagnostic in this document.
3. Choose a primary track and write down the evidence behind that choice.
4. Open [`10-eight-week-study-plan.md`](10-eight-week-study-plan.md) and allocate 15-20 hours for week 1.
5. Begin [`01-common-core.md`](01-common-core.md) and schedule the first baseline mock from [`09-mock-interviews-and-scorecards.md`](09-mock-interviews-and-scorecards.md).

Keep the plan adaptive. The best use of eight weeks is not equal coverage of every topic. It is enough shared breadth to clear common interview gates, deep evidence in the target role, and repeated practice explaining sound decisions under pressure.
