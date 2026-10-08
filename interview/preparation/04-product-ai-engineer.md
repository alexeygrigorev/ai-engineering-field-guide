# Senior Product AI Engineer Interview Preparation

This module prepares you to build and defend user-facing AI products from discovery through production iteration. It is a two-week role rotation inside the broader [eight-week curriculum](README.md), not a substitute for the [common core](01-common-core.md), [AI/ML system design](03-ai-ml-system-design.md), coding practice, or behavioral preparation.

The central interview signal is judgment across the whole product loop:

1. Identify a valuable user job.
2. Choose the smallest credible way to improve it.
3. Build a reliable end-to-end experience.
4. Evaluate model and system behavior.
5. Launch with guardrails.
6. Learn from real use and decide what to change.

Do not treat this track as prompt engineering with a user interface. A strong Product AI Engineer connects product discovery, software engineering, model behavior, user experience, measurement, and operations.

## Role Scope

A Product AI Engineer owns AI capabilities that users encounter directly or that materially change a user workflow. The role often spans product discovery, prototyping, backend and full-stack implementation, model and retrieval choices, evaluation, experimentation, production reliability, and iteration.

Typical responsibilities include:

- Translate an uncertain user problem into a testable product hypothesis.
- Decide whether AI is useful and where deterministic software should remain in control.
- Build a vertical slice across the interface, application backend, data, model, and observability layers.
- Choose models and context strategies based on quality, latency, cost, privacy, and operational constraints.
- Design evaluations before optimizing prompts, retrieval, tools, or fine-tuning.
- Create user experiences that communicate uncertainty and support correction, review, and recovery.
- Launch progressively, monitor behavior, investigate failures, and improve the product from feedback.
- Align product, design, engineering, data, legal, safety, security, and operations around decisions and guardrails.

### Market evidence and preparation priority

Product AI is a proxy mapping, not a direct measurement of jobs titled Product AI Engineer. The repository's broader [`ai engineer` title group](../../job-market/trends.md) contains 1,472 postings and has `RAG` in 61.0% and agents in 43.0%. Its skill-cluster analysis identifies RAG app builder as the largest archetype at 25.6% and agent builder at 16.9%; the [appendix](../../job-market/trends-appendix.md) documents the cluster signatures and method. Across the broader responsibility analysis, [building systems appears in 98.1% of postings](../../role/03-responsibilities.md), evaluation and quality in 68.5%, and API or service integration in 62.4%. Responsibility rates and archetype shares use all 4,894 published postings. These sources support a default practice order, but they do not establish the interview loop for this title.

Use this market-informed default:

- P0 - End-to-end shipping, `RAG`, and evaluation. Prove that you can build a vertical slice, diagnose retrieval and generation separately, define release evidence, and connect quality to product outcomes.
- P1 - Agents, prompting and context, API integration, and enterprise workflows. Bound autonomy and preserve permissions, failure handling, and workflow ownership.
- P2 - Full-stack implementation, `SQL` and data work, security, and cost. Practice these as constraints on a shipped product rather than disconnected trivia.
- P3 - Fine-tuning and model training. Study them deeply only when the job description or recruiter confirms that the loop tests them.

Override this default whenever the job description or recruiter confirms a different ownership boundary or interview loop.

### Product AI Engineer versus Forward Deployed Engineer

Both roles work through ambiguity, integrate systems, and ship practical AI. The center of gravity differs.

- Product AI Engineer
  - Primary unit of success - A reusable product capability and its sustained user outcome.
  - Discovery focus - User jobs, product behavior, interaction design, adoption, and retention.
  - Delivery shape - Product code and systems that can serve a broader user population.
  - Feedback loop - Product analytics, evaluations, user research, support signals, and experiments.
  - Common ownership - Feature roadmap, experience quality, application architecture, and iteration.
- Forward Deployed Engineer
  - Primary unit of success - A customer deployment or workflow outcome in a specific environment.
  - Discovery focus - Customer requirements, integration constraints, stakeholders, and acceptance criteria.
  - Delivery shape - Adaptation, integration, and deployment across customer systems.
  - Feedback loop - Customer usage, implementation outcomes, field observations, and account feedback.
  - Common ownership - Scoping, integration, deployment, adoption, and handoff.

A Product AI Engineer may work closely with customers, and an FDE may contribute reusable product improvements. Distinguish the roles by repeated ownership and success criteria rather than by whether customer contact occurs.

### Product AI Engineer versus ML/AI Platform Engineer

Both roles care about serving, evaluation, reliability, and cost. Their users and interfaces differ.

- Product AI Engineer
  - Primary user - An external customer or end user completing a product task.
  - Main interface - A workflow, application feature, API behavior, or interactive experience.
  - Optimization target - User value within quality, safety, latency, reliability, and cost constraints.
  - Typical question - What product behavior should we ship, and how will we know it helps?
- ML/AI Platform Engineer
  - Primary user - Internal application, ML, data, or research teams.
  - Main interface - Serving, evaluation, orchestration, training, data, or developer-platform contracts.
  - Optimization target - Safe, reliable, scalable, and efficient capabilities shared across teams.
  - Typical question - What platform contract lets teams build and operate AI systems effectively?

The Product AI Engineer should understand platform constraints without turning every product design into a platform build. The Platform Engineer should understand product needs without owning every end-user interaction.

## Likely Interview Loop and Signals

There is no universal loop. Ask the recruiter which rounds exist, how long they last, which tools are allowed, and what level each round evaluates. Prepare for some combination of:

1. Hiring-manager or product screen
   - Signals - Role motivation, product judgment, ownership scope, communication, and ability to connect technical work to user outcomes.
2. Practical coding or full-stack round
   - Signals - Working code, API and data design, testing, error handling, maintainability, and appropriate use of AI tools if allowed.
3. AI application or system-design round
   - Signals - Requirement clarification, architecture, model and context choices, evaluation, failure handling, privacy, latency, cost, rollout, and evolution.
4. Product or case exercise
   - Signals - User and job framing, prioritization, baseline choice, experiment design, metrics, guardrails, and willingness to reject weak AI use cases.
5. Project deep dive
   - Signals - Personal contribution, decisions, alternatives, technical depth, production failures, measurable outcomes, and learning.
6. Evaluation or model-behavior round
   - Signals - Failure taxonomy, dataset design, graders, human review, offline-to-online reasoning, and diagnosis rather than blind prompt iteration.
7. Senior or staff behavioral round
   - Signals - Strategy, prioritization, influence, conflict resolution, cross-team architecture, risk management, mentoring, and durable leverage.
8. Take-home or live prototype
   - Signals - Scope control, vertical-slice delivery, product quality, testability, documentation, and a credible path from demonstration to production.

Avoid guessing company-specific expectations from a title. Use the job description and recruiter guidance as the source of truth.

## Skill Map

Use this map to connect each competency to evidence from a project, a design decision, and a timed drill.

### Product discovery and user framing

- Product discovery - Observe the current workflow, its frequency, stakes, alternatives, and failure costs before selecting a model capability.
- User and job framing - Name the user, trigger, desired outcome, current workaround, constraints, and evidence that the problem matters.
- Product hypothesis - State how a specific intervention should improve a measurable outcome for a defined population.
- Prioritization - Compare expected value, confidence, effort, reversibility, dependencies, and downside risk.
- Rapid prototypes - Build the cheapest artifact that resolves the largest uncertainty, then discard or harden it deliberately.

### Product and application engineering

- Full-stack and backend - Design interaction state, APIs, persistence, queues, streaming, authentication, authorization, observability, and tests.
- Model selection - Compare candidate models on task-specific quality, tool use, structured output, context limits, latency, cost, privacy, and operational fit.
- Prompt and context engineering - Separate instructions, user data, retrieved evidence, tool results, conversation state, and output schemas.
- RAG and agents - Use retrieval for grounded knowledge and agents for bounded action; do not add autonomy when a deterministic workflow is sufficient.
- Reliability - Define timeouts, retries, idempotency, fallbacks, degraded modes, rollback, and operational ownership.
- Cost and latency - Budget the full request path, not only model inference, and connect constraints to user experience and unit economics.

### Learning and product quality

- Evaluation - Define task-level success, failure categories, representative datasets, graders, thresholds, and regression checks.
- Experimentation - Separate model-quality experiments from product-behavior experiments and interpret noisy outcomes cautiously.
- Feedback loops - Collect explicit, implicit, sampled, and operational signals without treating all feedback as ground truth.
- UX for uncertainty - Expose sources, confidence cues when calibrated, editable drafts, previews, approvals, undo, escalation, and recovery.
- Safety and privacy - Minimize data, enforce permissions, treat retrieved and user content as untrusted, and constrain high-impact actions.
- Launch and iteration - Roll out by risk, inspect traces and failures, update evaluations, and choose whether to improve, narrow, pause, or remove the feature.

## Senior and Staff Depth

### Senior-level evidence

A senior candidate should independently own an ambiguous product problem through launch and operation. Strong evidence includes:

- Clarifying the user job and defining success before selecting an AI technique.
- Choosing among deterministic code, search, RAG, model generation, and tool-using workflows.
- Owning a coherent architecture across product, application, model, data, and operations.
- Prioritizing the next experiment from evidence rather than from model novelty.
- Making explicit quality, safety, privacy, latency, reliability, and cost trade-offs.
- Coordinating with product, design, data, platform, security, legal, support, and operations.
- Defining product metrics and technical guardrails, then changing course when evidence contradicts the original hypothesis.

### Staff-level evidence

Staff depth requires leverage beyond one difficult feature. Strong evidence includes:

- Set a product and technical strategy across multiple teams or a product area.
- Create architectural boundaries, evaluation standards, safety patterns, or shared components that improve many teams' decisions.
- Sequence investments under uncertainty, including what not to build and when to revisit it.
- Resolve disagreement among teams with different incentives through evidence, explicit decision rights, and reversible tests.
- Define metrics and guardrails that connect portfolio-level product outcomes to technical behavior.
- Plan migrations, ownership, adoption, and long-term maintenance rather than only the target architecture.
- Raise organizational capability through mentoring, review mechanisms, incident learning, and reusable decision frameworks.

Do not inflate a senior feature into a staff story. State the actual scope, the decisions you owned, who else contributed, and what changed beyond your direct implementation.

## A Product AI Answer Framework

Use this sequence for product cases and system-design prompts:

1. Frame the user and job.
   - Who has the problem?
   - What triggers the workflow?
   - What outcome matters?
   - How frequent, painful, and risky is it?
2. Establish the current baseline.
   - What does the user do today?
   - What deterministic or non-AI solution is available?
   - What baseline metric can you measure now?
3. State the hypothesis and non-goals.
   - What behavior should change?
   - For which users?
   - What will the first version deliberately not do?
4. Define success and guardrails.
   - Task success, adoption, retention, latency, cost, safety, quality, and reliability.
   - Stop conditions and unacceptable failure modes.
5. Choose the interaction and control model.
   - Suggestion, draft, answer, automation, or autonomous action.
   - Preview, citation, edit, approval, undo, escalation, and recovery.
6. Design the system.
   - Data flow, model, context, retrieval, tools, state, permissions, storage, observability, and fallbacks.
7. Design evaluation.
   - Representative tasks, failure taxonomy, graders, human review, thresholds, and regression suite.
8. Plan rollout and learning.
   - Internal test, shadow mode, limited cohort, progressive exposure, rollback, and review cadence.
9. Explain trade-offs and evolution.
   - What you would change if quality, scale, risk, latency, or economics differ from assumptions.

## Detailed Preparation Areas

### Product discovery, framing, and prioritization

Questions to practice:

- When is AI the wrong solution for a product problem?
- How would you determine whether a proposed assistant solves a meaningful user job?
- Which uncertainty would you test first: demand, model capability, data access, UX, or economics?
- How would you prioritize two AI features with different value and risk profiles?

Strong-answer criteria:

- Starts with users, workflow, baseline, stakes, and decision context.
- Separates problem validation from technical feasibility.
- Proposes the cheapest test for the largest uncertainty.
- Includes a deterministic baseline and an explicit reason to use AI.
- Defines success, guardrails, non-goals, and a decision after the test.

Red flags:

- Starts by choosing a model or agent framework.
- Treats a compelling demo as evidence of demand.
- Uses engagement as the only measure of value.
- Cannot explain when to narrow or reject the feature.
- Ignores workflow change, trust, or error cost.

Practical drills:

1. Take a familiar SaaS workflow and write a one-page job statement, baseline, hypothesis, riskiest assumption, and first experiment in 20 minutes.
2. Generate three solutions: deterministic, assistive AI, and automated AI. Defend one and reject two.
3. Rank five candidate features using value, confidence, effort, reversibility, and downside risk. Explain the top choice aloud in five minutes.

### Rapid prototypes and end-to-end engineering

Questions to practice:

- What should a prototype prove, and what should it avoid pretending to prove?
- How would you turn a notebook or demo into a supported product feature?
- Where should state live in a conversational or agentic application?
- How do you design streaming, cancellation, retries, and duplicate-request handling?

Strong-answer criteria:

- Builds a vertical slice around a specific uncertainty and user path.
- Separates disposable exploration from production interfaces and data contracts.
- Covers authentication, authorization, validation, persistence, concurrency, observability, tests, and failure handling.
- Uses idempotency for actions and bounded retries for transient failures.
- Names a hardening plan with ownership, service levels, rollout, and rollback.

Red flags:

- Equates a successful happy-path demo with production readiness.
- Stores sensitive context indiscriminately or mixes users' state.
- Retries nondeterministic or side-effecting actions without idempotency.
- Omits cancellation, timeout, fallback, and partial-failure behavior.
- Builds a general platform before validating the product need.

Practical drills:

1. Build a small API that accepts a task, calls a model, validates structured output, stores a trace, and handles timeout and retry behavior.
2. Add a simple user interface with loading, streaming, cancellation, edit, and retry states.
3. Write a production-gap audit for an existing prototype under security, privacy, reliability, observability, cost, and supportability.

### Model, prompt, context, RAG, and agent decisions

Questions to practice:

- How would you choose a model for a user-facing feature?
- What belongs in the prompt, retrieved context, application code, or fine-tuning data?
- When should you use RAG instead of long context or fine-tuning?
- When is an agent justified, and how would you constrain it?

Strong-answer criteria:

- Starts from task distribution, quality threshold, risk, latency, cost, privacy, and operational needs.
- Evaluates candidates on representative tasks instead of relying on generic benchmarks.
- Treats context construction as typed, permissioned data flow.
- Separates retrieval failure from generation failure.
- Uses deterministic orchestration when possible and bounds agent tools, steps, time, spend, and permissions.

Red flags:

- Chooses the largest model by default.
- Treats prompt injection as solvable only through a system prompt.
- Uses fine-tuning to add changing factual knowledge.
- Adds agents where a fixed workflow is clearer and safer.
- Cannot explain grounding, citations, retrieval evaluation, or tool authorization.

Practical drills:

1. Compare three model candidates on a 30-item task set and write a recommendation with quality, latency, cost, and risk trade-offs.
2. Debug ten failed RAG traces by labeling ingestion, retrieval, reranking, context assembly, generation, and citation failures.
3. Convert an open-ended agent into a bounded workflow with explicit tools, state transitions, approvals, budgets, termination, and compensation.

### Evaluation, experimentation, and feedback loops

Questions to practice:

- How would you create an evaluation set before enough production data exists?
- How do offline evaluations relate to online product outcomes?
- How would you investigate an A/B test that improves adoption but worsens task success?
- Which user feedback should become labels, and which should not?

Strong-answer criteria:

- Defines the unit of evaluation and a failure taxonomy before selecting metrics.
- Builds representative slices from expert examples, historical tasks, synthetic augmentation, adversarial cases, and later production samples.
- Combines deterministic checks, model-based graders, human review, and end-to-end task measures where appropriate.
- Validates graders against human judgments and monitors disagreement.
- Treats feedback as biased evidence that needs context, deduplication, privacy controls, and sampling.

Red flags:

- Uses one aggregate model score with no slices.
- Calls thumbs-up feedback ground truth.
- Optimizes offline quality without checking the user workflow.
- Runs repeated experiments without controlling false discoveries or novelty effects.
- Changes prompts without a regression suite or versioned traces.

Practical drills:

1. Create a 50-case evaluation plan with task categories, risk slices, failure labels, graders, thresholds, and adjudication.
2. Review 20 traces and produce a Pareto chart of failure categories, then choose one intervention.
3. Design an online experiment with eligibility, randomization unit, primary metric, guardrails, exposure logging, stopping rule, and post-test decision.

### UX for uncertainty, safety, and privacy

Questions to practice:

- How should the interface behave when the model is uncertain or evidence is missing?
- When should an AI action require human approval?
- How would you handle prompt injection in retrieved documents?
- What data should be retained for improvement, and for how long?

Strong-answer criteria:

- Matches autonomy to reversibility, detectability, user expertise, and harm.
- Uses citations, previews, editable drafts, confirmations, undo, escalation, and explicit unsupported states where useful.
- Enforces authorization at data retrieval and tool execution, not in model instructions alone.
- Minimizes collected data and defines purpose, access, retention, deletion, and audit behavior.
- Separates content safety, security, privacy, and product-quality risks.

Red flags:

- Displays an uncalibrated confidence number as truth.
- Hides uncertainty to make the experience feel polished.
- Lets the model decide its own permissions.
- Logs complete prompts and responses without a data policy.
- Uses a human reviewer as an undefined catch-all control.

Practical drills:

1. Sketch low-, medium-, and high-risk versions of the same AI workflow and vary approval and recovery controls.
2. Threat-model a RAG assistant for data leakage, prompt injection, insecure output handling, and cross-tenant access.
3. Write a data-flow inventory covering source, purpose, processor, retention, access, deletion, and evaluation use.

### Reliability, cost, latency, launch, and iteration

Questions to practice:

- What is the latency budget for this experience, and where is it spent?
- How would you degrade gracefully during a model-provider incident?
- How do you know whether the feature has viable unit economics?
- What evidence would cause you to roll back, narrow, or remove it?

Strong-answer criteria:

- Sets product-facing service objectives and budgets each stage of the request path.
- Covers timeout, retry, fallback, circuit breaking, backpressure, caching, idempotency, monitoring, and rollback.
- Calculates cost per completed valuable task, not only cost per request.
- Uses staged rollout based on uncertainty and potential harm.
- Connects incidents and production failures back into evaluations and product priorities.

Red flags:

- Optimizes model latency while ignoring retrieval, tools, queues, and client rendering.
- Uses unlimited retries or silent fallbacks that change product behavior.
- Treats token cost as the entire unit cost.
- Launches broadly because offline averages look good.
- Monitors infrastructure but not task failure or harmful behavior.

Practical drills:

1. Build a latency and cost budget for one workflow using explicit traffic, token, retrieval, tool, and support assumptions.
2. Write a degradation ladder: smaller model, reduced context, read-only mode, deterministic fallback, queue, and temporary disablement.
3. Run a launch review with entry criteria, cohort plan, dashboards, alerts, on-call owner, rollback trigger, and next evaluation date.

## Product Metrics and Evaluation

### Metric hierarchy

Use metrics as a connected system rather than a dashboard checklist.

- Task success
  - Did the user complete the intended job correctly and with acceptable effort?
  - Measure completion, acceptance after review, correction burden, resolution quality, and time to outcome.
- Adoption
  - Did eligible users discover and try the feature?
  - Separate exposure, activation, first successful use, and repeat use.
- Retention
  - Do users return because the feature remains useful?
  - Use a cadence that matches the job; daily retention is meaningless for a quarterly workflow.
- Latency and reliability
  - Track time to first useful response, time to completion, timeout rate, availability, and degraded-mode rate.
  - Use percentiles and workflow slices rather than only averages.
- Cost
  - Track model, retrieval, tool, storage, observability, human review, support, and retry costs.
  - Prefer cost per successful task or retained user over cost per call.
- Safety and privacy
  - Track policy violations, sensitive-data exposure, unauthorized access, unsafe actions, escalation quality, and audit completion.
  - Rare high-severity events require case review and explicit thresholds, not only averages.
- Quality
  - Track task-specific correctness, groundedness, completeness, instruction following, citation support, format validity, and user correction.
  - Report by task, user, language, risk, and complexity slices when they change decisions.

### Offline evaluation

Offline evaluation is fast, reproducible, and useful for regression detection and candidate comparison. It cannot prove that users will adopt the feature or that the workflow improves.

A credible offline program includes:

1. A defined task unit and failure taxonomy.
2. Representative and difficult examples, including important slices.
3. Versioned inputs, system configuration, prompts, models, tools, and outputs.
4. Deterministic checks where possible.
5. Model-based graders with documented rubrics and validation against human review.
6. Human adjudication for ambiguous or high-risk examples.
7. Thresholds for launch, regression, and investigation.
8. Trace review to diagnose causes rather than only rank systems.

Avoid test-set leakage. Keep a stable regression set, a rotating challenge set, and fresh production samples when volume permits.

### Online evaluation

Online evaluation measures behavior in the real workflow. Use:

- Product analytics for exposure, activation, task completion, repeat use, abandonment, correction, escalation, and downstream outcomes.
- Sampled trace review for nuanced quality and new failure discovery.
- Operational monitoring for latency, errors, availability, saturation, and cost.
- User research and support evidence for trust, workflow fit, and reasons behind behavior.
- Safety and privacy review for incidents and near misses.

Do not infer quality from engagement alone. A verbose or addictive system can increase usage while worsening outcomes.

### A/B testing limits in nondeterministic systems

A/B testing remains useful, but nondeterminism and interference require care:

- Repeated calls for the same input may produce different outputs, increasing outcome variance.
- Model or provider updates can change treatment behavior during the experiment.
- Shared caches, conversation state, retrieval indexes, and human collaborators can contaminate assignment.
- Users may learn how to use the feature, creating novelty and carryover effects.
- Rare safety failures may not appear in an experiment sized for adoption or task success.
- Judge models can introduce correlated measurement error.
- Multiple prompts, models, and segments increase false-discovery risk.

Mitigate these limits by versioning the full treatment, logging assignment and exposure, choosing the right randomization unit, monitoring sample ratio mismatch, predefining primary metrics and guardrails, running long enough to cover the workflow cadence, and combining experiments with offline evaluation, trace review, and qualitative research.

An A/B result estimates the effect of a specific product treatment on an eligible population during a specific period. It does not establish that the model is generally better.

## Question Practice Order

The priority labels below allocate practice time; they do not remove any questions from the bank.

- P0 - Start with end-to-end shipping in [rapid prototypes and end-to-end engineering](#rapid-prototypes-and-end-to-end-engineering), [architecture and model behavior](#architecture-and-model-behavior), [evaluation and experimentation](#evaluation-and-experimentation), and [project deep-dive preparation](#project-deep-dive-preparation).
- P1 - Continue with Python, APIs, integration, [prompt, context, RAG, and agents](#prompt-context-rag-and-agents), and enterprise workflow cases.
- P2 - Add [full-stack and backend delivery](#full-stack-and-backend-delivery), [UX, safety, and operations](#ux-safety-and-operations), and [reliability, economics, and leadership](#reliability-economics-and-leadership).
- P3 - Go deep on fine-tuning or training only when the target loop confirms it.

Practice these first 12 questions or cases, in order:

1. Question 21 - Turn a notebook prototype into a multi-tenant service with tests and observability.
2. Question 4 - Design a user-facing document assistant that answers with citations.
3. Question 6 - Diagnose fluent but unsupported answers from a RAG assistant.
4. Question 8 - Build an evaluation plan with little production data.
5. Question 9 - Diagnose why offline quality rose while task completion fell.
6. Question 10 - Design an A/B test for a nondeterministic feature.
7. [Product Case Exercise 2](#product-case-exercise-2-enterprise-document-assistant) - Defend an enterprise document assistant end to end.
8. [Project Deep-Dive Preparation](#project-deep-dive-preparation) - Rehearse one shipped project with evaluation, failures, and measured outcomes.
9. Question 20 - Design API and state boundaries for streaming conversation.
10. Question 24 - Test slow, costly, nondeterministic model calls.
11. Question 25 - Choose among long context, RAG, fine-tuning, and deterministic rules.
12. Question 30 - Create a failure taxonomy for an AI drafting feature.

Then cover every remaining category. Override this order when the job description or recruiter confirms a different loop.

## Synthesized Interview Questions

The questions in this section are synthesized practice questions. They are not attributed to a specific company, and they do not claim to reproduce any employer's interview loop. Use the linked [theory questions](../questions/01-theory.md) and [project deep-dive questions](../questions/03-project-deep-dive.md) separately when you want the repository's sourced question collections.

### Core questions with answer rubrics

#### Product discovery and strategy

1. Core question: A product manager proposes an AI assistant because competitors have one. How do you decide whether to build it?
   - Key points - Identify target users and jobs; study the current workflow and alternatives; define expected value and risks; test demand separately from feasibility; establish a deterministic baseline; choose the cheapest test of the largest uncertainty; set a decision rule.
2. Core question: When is AI the wrong solution even if a model can perform the task?
   - Key points - Prefer deterministic behavior when rules are stable, exactness is required, errors are costly and hard to detect, data or permissions are unsuitable, economics fail, or workflow value is weak; explain a safer alternative.
3. Core question: You can fund only one of three AI features. How do you prioritize them?
   - Key points - Compare user value, reach, confidence, effort, risk, reversibility, strategic fit, dependencies, and learning value; name assumptions; choose a staged bet; state what evidence would change the ranking.

#### Architecture and model behavior

4. Core question: Design a user-facing document assistant that answers questions with citations.
   - Key points - Clarify users, corpus, freshness, permissions, and stakes; define baseline and task metrics; design ingestion, parsing, chunking, retrieval, reranking, context assembly, generation, citation verification, and unsupported behavior; include evaluation, latency, cost, rollout, and deletion.
5. Core question: How would you choose among a small model, a frontier model, and a model cascade?
   - Key points - Use a representative task set; compare quality by slice, structured output, tool behavior, latency, cost, privacy, availability, and operational complexity; define routing confidence and fallback behavior; account for cascade error and added latency.
6. Core question: A RAG assistant gives fluent but unsupported answers. How do you diagnose and fix it?
   - Key points - Inspect traces; separate corpus, parsing, chunking, retrieval, reranking, context, generation, and citation failures; measure retrieval recall and answer support independently; add abstention or clarification; change one layer at a time and rerun regressions.
7. Core question: When should a product use an agent rather than a fixed workflow?
   - Key points - Justify variable planning or tool selection; compare with deterministic orchestration; bound tools, permissions, steps, time, spend, state, and termination; require approval for high-impact actions; design idempotency, compensation, traceability, and fallback.

#### Evaluation and experimentation

8. Core question: Build an evaluation plan for an AI feature with little production data.
   - Key points - Define task and failure taxonomy; collect expert and historical examples; add carefully reviewed synthetic and adversarial cases; cover important slices; combine deterministic, model, and human graders; validate graders; set thresholds; add fresh production samples after launch.
9. Core question: Offline quality improved, but task completion fell after launch. What do you do?
   - Key points - Verify instrumentation and treatment stability; segment by user and task; inspect latency, UX, corrections, and traces; check offline-online distribution gaps and proxy mismatch; protect users with rollback or narrowed exposure; update evaluations from observed failures.
10. Core question: How would you A/B test a nondeterministic AI feature?
   - Key points - Define eligibility, randomization unit, exposure, stable treatment versions, primary metric, guardrails, power assumptions, and stopping rule; account for repeated-output variance, contamination, novelty, provider changes, and rare harms; pair the test with trace review and offline evaluation.

#### UX, safety, and operations

11. Core question: Design the user experience for a system that may be wrong but can save substantial time.
   - Key points - Match autonomy to stakes and reversibility; show evidence or source context; support edit, preview, confirm, undo, retry, and escalation; distinguish unsupported answers; avoid false precision; measure correction burden, task success, and trust behavior.
12. Core question: How do you defend a tool-using assistant against prompt injection and excessive agency?
   - Key points - Treat all external content as untrusted data; isolate instructions from content; enforce least privilege outside the model; authorize each tool action; validate inputs and outputs; sandbox execution; use approvals, budgets, termination, audit logs, and red-team evaluations.
13. Core question: Design a rollout for an AI action that can affect customer records.
   - Key points - Start read-only or draft-only; use shadow evaluation; gate by user and risk; require preview and approval; enforce idempotency and audit logs; monitor quality and unauthorized changes; define rollback and incident ownership; expand only after entry criteria pass.

#### Senior and staff ownership

14. Core question: Two teams disagree between shipping quickly with a provider API and building a shared internal capability. How do you lead the decision?
   - Key points - Clarify product deadlines and durable requirements; identify reversible and irreversible choices; compare total cost, risk, lock-in, operational burden, reuse, and opportunity cost; define decision rights; run a bounded test if uncertainty is material; document triggers for revisiting the decision.

### Additional drill prompts

#### Discovery and product judgment

15. Synthesize a product hypothesis for an AI feature that reduces support-handoff time without lowering resolution quality.
16. Explain how you would interview users without leading them toward an AI solution.
17. Decide whether to improve an existing workflow or create a new AI-first workflow.
18. Define non-goals for the first release of a meeting assistant.
19. Describe evidence that would cause you to stop investing in an AI feature.

#### Full-stack and backend delivery

20. Design API and state boundaries for a streaming conversational application.
21. Turn a notebook prototype into a multi-tenant service with tests and observability.
22. Handle cancellation, retry, and duplicate submissions in a long-running generation workflow.
23. Design conversation retention and deletion across application, model provider, and analytics systems.
24. Explain how you would test a feature whose model calls are slow, costly, and nondeterministic.

#### Prompt, context, RAG, and agents

25. Decide whether a changing policy corpus needs long context, RAG, fine-tuning, or deterministic rules.
26. Design context selection for a coding assistant with repository, editor, and conversation signals.
27. Evaluate chunking and retrieval strategies for scanned documents with tables.
28. Design tool contracts and termination conditions for a research agent.
29. Explain when structured outputs fail and how the application should recover.

#### Evaluation, metrics, and iteration

30. Create a failure taxonomy for an AI email-drafting feature.
31. Validate whether a model-based grader is reliable enough for regression testing.
32. Interpret high adoption, low retention, and high correction rates for an AI feature.
33. Design a feedback loop that does not treat every user edit as a negative label.
34. Choose launch thresholds when aggregate quality is strong but one high-risk slice is weak.

#### Reliability, economics, and leadership

35. Reduce median latency without worsening tail latency, quality, or cost per successful task.
36. Respond to a provider model update that changes output behavior without an application deploy.
37. Decide whether to cache responses, retrieved context, embeddings, or tool results.
38. Present an incident in which AI output caused user harm and explain the systemic changes that followed.
39. Align product, legal, security, and engineering on a launch when each team has different risk tolerance.
40. Set a one-year technical strategy for AI product development across several product teams.

This bank contains 40 synthesized questions: 14 core questions with answer rubrics and 26 additional drill prompts.

## Product Case Exercise 1: Support Copilot

Prompt: Design a copilot that helps support agents resolve customer tickets faster while preserving answer quality and policy compliance.

### Structured walkthrough

1. User value and job
   - User - Support agent handling a queue of customer issues.
   - Job - Understand the issue, find relevant evidence, draft a correct response, take approved actions, and resolve or escalate.
   - Value hypothesis - Reduce agent effort and time to resolution without increasing reopen, escalation, policy-violation, or customer-dissatisfaction rates.
2. Baseline
   - Measure current handling time, first-response time, resolution rate, reopen rate, escalation rate, quality-review scores, search time, and policy defects.
   - Compare with better search, response templates, and workflow shortcuts before assuming generation is needed.
3. First scope
   - Summarize the ticket, retrieve relevant account and policy context, suggest sources, and draft an editable response.
   - Keep account-changing actions out of the first release.
4. Evaluations
   - Offline tasks - Issue classification, evidence retrieval, policy selection, answer support, completeness, tone, and escalation decisions.
   - Slices - Product area, language, customer tier, new policy, ambiguous request, and high-risk account state.
   - Human review - Support experts score correctness, evidence, policy compliance, and whether escalation was required.
5. Architecture
   - Ticket event enters an application service.
   - Service retrieves authorized customer context and policy documents.
   - Reranker and context builder produce traceable evidence.
   - Model returns structured summary, recommended response, citations, and escalation flags.
   - Agent interface supports source inspection, edit, regenerate, accept, and escalate.
   - Traces record versions, retrieved evidence, latency, costs, agent edits, and outcomes under a controlled retention policy.
6. Rollout
   - Start with historical replay and internal support experts.
   - Run in shadow mode, then expose read-only suggestions to a small trained cohort.
   - Expand by issue category after quality and latency gates pass.
   - Add low-risk tool actions only after draft quality and audit controls are stable.
7. Risks and controls
   - Incorrect policy - Require citations, policy-version filtering, and an unsupported state.
   - Sensitive data leakage - Enforce field-level access, tenant isolation, minimization, and redaction.
   - Automation bias - Keep editable drafts, show evidence, sample accepted responses, and monitor low-edit acceptance.
   - Stale knowledge - Track ingestion freshness, policy effective dates, deletion, and index lag.
   - Prompt injection in ticket content - Treat tickets as untrusted data and enforce tool permissions outside the model.
8. Metrics and decision
   - Primary - Correctly resolved tickets per agent hour or time to correct resolution.
   - Product - Activation, weekly retained use among eligible agents, acceptance with edits, and abandonment.
   - Guardrails - Reopen, escalation, policy defect, safety incident, customer complaint, tail latency, and cost per correct resolution.
   - Decision - Expand only if workflow outcomes improve without guardrail regression; otherwise diagnose by issue category and failure type.

### Interview follow-ups

- Would you optimize for draft acceptance rate?
- How do you distinguish model error from bad source data?
- When would you allow the copilot to issue refunds?
- How would you evaluate a policy that changed yesterday?
- What would change for a customer-facing self-service assistant?

## Product Case Exercise 2: Enterprise Document Assistant

Prompt: Design an assistant that answers employee questions across internal documents while respecting permissions and showing reliable sources.

### Structured walkthrough

1. User value and job
   - User - Employee trying to find and apply internal knowledge.
   - Job - Obtain a current, supported answer without searching several systems or exposing restricted information.
   - Value hypothesis - Increase successful self-service and reduce time to a supported answer.
2. Baseline
   - Measure search success, query reformulation, time to answer, click-through to source, help-desk deflection, and unresolved searches.
   - Compare with improved keyword search, navigation, and document hygiene.
3. First scope
   - Start with one valuable, well-maintained corpus and answer questions with citations.
   - Exclude high-stakes legal, HR, or security decisions until the system and ownership model are proven.
4. Evaluations
   - Retrieval - Relevant-document and passage recall, permission correctness, freshness, and citation coverage.
   - Generation - Groundedness, completeness, contradiction handling, unsupported behavior, and citation entailment.
   - End to end - Whether a user can complete the target task correctly.
   - Slices - Department, permission level, document type, language, ambiguity, stale documents, and no-answer cases.
5. Architecture
   - Connectors ingest documents and authorization metadata.
   - Parsing and chunking preserve headings, tables, source identity, version, and effective dates.
   - Hybrid retrieval applies access filters before reranking.
   - Context assembly deduplicates evidence and stays within a token budget.
   - Generation returns a structured answer with citations or asks for clarification.
   - The interface lets users inspect sources, report problems, and continue to the source system.
6. Rollout
   - Validate permissions with deterministic tests before model-quality testing.
   - Launch to corpus owners and a small user cohort.
   - Monitor zero-result, unsupported-answer, permission-denial, stale-source, latency, and cost rates.
   - Add corpora only when ownership, freshness, deletion, and access semantics are defined.
7. Risks and controls
   - Cross-user leakage - Enforce source-system identity and authorization in retrieval; never rely on model compliance.
   - Stale or conflicting documents - Rank by authority and effective date, expose conflicts, and route users to owners.
   - Unsupported synthesis - Require evidence coverage and allow refusal or clarification.
   - Deleted content remains indexed - Propagate deletion, audit lag, and block uncertain content.
   - Feedback leaks document contents - Apply access controls and minimization to traces and review tools.
8. Metrics and decision
   - Primary - Successful supported answer rate and time to correct answer.
   - Product - Eligible-user activation, retained use by job cadence, source-open rate, and escalation.
   - Quality - Retrieval recall, supported-answer rate, citation correctness, and correction rate.
   - Guardrails - Unauthorized retrieval, stale-answer incidents, safety and privacy defects, tail latency, and cost per successful answer.

### Interview follow-ups

- Would you use one index or several?
- How do you evaluate permission filters?
- What happens when sources disagree?
- When is a long-context approach better than retrieval?
- How would you support document deletion and legal holds?

## Product Case Exercise 3: Agent Workflow for Vendor Onboarding

Prompt: Design an agent-assisted workflow that collects vendor information, checks requirements, coordinates approvals, and updates internal systems.

### Structured walkthrough

1. User value and job
   - User - Operations specialist coordinating vendor onboarding.
   - Job - Gather complete information, validate requirements, route approvals, create records, and communicate status.
   - Value hypothesis - Reduce cycle time and manual coordination while preventing unauthorized or incorrect changes.
2. Baseline
   - Measure cycle time, touch time, handoffs, missing-information loops, rework, policy exceptions, and incorrect-record incidents.
   - Compare with forms, workflow automation, validation rules, and better status visibility.
3. First scope
   - Let AI extract submitted information, identify missing fields, draft communications, and recommend the next approved step.
   - Keep external messages and system mutations behind human approval.
4. Evaluations
   - Extraction accuracy by field and document type.
   - Requirement-check precision and recall, especially for blocking conditions.
   - Correct tool selection and valid tool arguments.
   - Workflow completion, unnecessary steps, termination, and recovery from tool failures.
   - Human review of approval recommendations and external communications.
5. Architecture
   - A durable workflow engine owns state, transitions, timers, and retries.
   - The model extracts data, classifies exceptions, drafts messages, and proposes bounded actions.
   - Typed tool contracts validate input and output.
   - A policy service and authorization layer decide which actions are permitted.
   - Side effects use idempotency keys, audit logs, and compensating actions where possible.
   - Approval tasks show source evidence, proposed changes, and expected impact.
6. Rollout
   - Replay historical cases, then run recommendations in shadow mode.
   - Launch extraction and drafting before action execution.
   - Enable low-risk, reversible actions for a trained cohort.
   - Expand by vendor type and action after task and safety gates pass.
7. Risks and controls
   - Infinite or wasteful loops - Set step, time, and spend budgets with explicit terminal states.
   - Duplicate side effects - Use durable state, idempotency, and result reconciliation.
   - Excessive permissions - Grant task-scoped credentials and authorize every action outside the model.
   - Wrong approval route - Encode deterministic policies and require evidence for exceptions.
   - Unrecoverable action - Require approval, preview, and compensation or prohibit automation.
8. Metrics and decision
   - Primary - Correct onboarding completion time.
   - Product - Cases assisted, specialist retention, approval acceptance with edits, and manual takeover.
   - Reliability - Workflow completion, tool-error recovery, duplicate-action rate, and stuck-workflow age.
   - Guardrails - Unauthorized action, incorrect record, policy exception, external-message defect, cost per completed case, and tail cycle time.

### Interview follow-ups

- Why is a workflow engine preferable to an unconstrained agent loop?
- Which actions could become automatic first?
- How do you recover when a tool succeeds but the response times out?
- What state should the model see?
- How do you test compensation and manual takeover?

## Project Deep-Dive Preparation

Prepare two projects using [project deep dives and take-homes](08-project-deep-dives-and-take-homes.md) and the existing [project deep-dive question bank](../questions/03-project-deep-dive.md). Choose at least one project that reached real users or production-like constraints.

For each project, prepare a 12-minute narrative:

1. User and business context.
2. Baseline workflow and why the problem mattered.
3. Your role, team, constraints, and decision rights.
4. Product hypothesis and initial scope.
5. Architecture and the two hardest technical decisions.
6. Evaluation and launch plan.
7. Production failures or surprises.
8. User, quality, safety, latency, reliability, and cost outcomes.
9. Iterations and what evidence changed your mind.
10. What you would do differently now.

Expect probes on:

- Why AI was necessary.
- Why you selected that model, retrieval strategy, or agent design.
- What you personally implemented or decided.
- How you established the baseline and evaluation set.
- Which metric could be misleading.
- How the system failed and how users recovered.
- How privacy, authorization, and retention worked.
- What you cut and why.
- How you influenced partners without direct authority.
- What made the work senior or staff scope.

Strong answers are specific about constraints, rejected alternatives, ownership, and outcomes. Red flags include framework tours, vague team-level claims, no baseline, no failure discussion, and metrics disconnected from the user job.

## Two-Week Role Rotation

Use this rotation after enough work in [common core](01-common-core.md) and [AI/ML system design](03-ai-ml-system-design.md) to explain the underlying systems. It fits within the overall eight-week program by concentrating Product AI depth in two weeks while continuing coding, project, and behavioral practice.

### Week 1: End-to-end shipping, RAG, and evaluation

Target 15-20 hours:

- 2 hours - Run the Product AI diagnostic and select two weak areas.
- 3 hours - Build or harden one end-to-end vertical slice with API contracts, validation, traces, tests, and failure handling.
- 3 hours - Complete the enterprise document-assistant case under a 50-minute design constraint, then review retrieval and generation failures separately.
- 3 hours - Build an evaluation plan and 30-50 representative cases for the vertical slice or a shipped portfolio project.
- 2 hours - Practice product metrics, offline-to-online reasoning, and one A/B design.
- 2 hours - Rehearse one project deep dive with measurable user, quality, reliability, latency, and cost outcomes.
- 2 hours - Frame three user jobs, baselines, hypotheses, non-goals, and first experiments.
- 1-3 hours - Continue coding and common-core retrieval practice.

Week 1 deliverables:

- One production-oriented vertical slice or hardening review.
- One timed RAG case design.
- One versioned evaluation plan with failure taxonomy.
- One scored project-deep-dive recording.
- Three one-page product hypotheses.

### Week 2: Agents, enterprise workflows, and launch

Target 15-20 hours:

- 3 hours - Complete the support-copilot or agent-workflow case and compare deterministic orchestration with bounded agency.
- 2 hours - Compare at least two model, context, or API approaches on task quality, latency, cost, privacy, and complexity.
- 2 hours - Create a privacy and safety threat model plus a UX recovery flow.
- 2 hours - Produce a latency, cost, reliability, and degradation budget.
- 2 hours - Prepare two senior or staff stories on prioritization and cross-functional influence using [senior and staff behavioral preparation](07-senior-staff-behavioral.md).
- 2 hours - Run a product and architecture mock.
- 2 hours - Run a project deep-dive or practical prototype review.
- 2-5 hours - Remediate the two lowest scorecard dimensions and continue shared-core practice. Add fine-tuning or training depth only when the target loop confirms it.

Week 2 deliverables:

- One production-oriented vertical slice or hardening review.
- One threat model and rollout plan.
- One latency and cost model.
- One agent-versus-workflow decision memo.
- Two scored mocks.
- A readiness decision with named gaps and next drills.

Do not postpone all Product AI work until the final two weeks of the eight-week curriculum. Revisit the cases and question bank during later full-loop simulations.

This rotation is the proxy-evidence default. Override it when the job description or recruiter confirms a different loop.

## Mock Format

### Product and AI architecture mock

Run a 60-minute session:

1. 5 minutes - Clarify user, job, constraints, stakes, scale, and success.
2. 8 minutes - Establish baseline, hypothesis, non-goals, metrics, and guardrails.
3. 15 minutes - Design interaction, application architecture, model, context, data, and permissions.
4. 10 minutes - Design offline evaluation and online learning.
5. 8 minutes - Cover reliability, safety, privacy, latency, and cost.
6. 7 minutes - Explain rollout, rollback, and iteration.
7. 7 minutes - Handle adversarial follow-ups.

### Project deep-dive mock

Run a 45-minute session:

1. 10-12 minutes - Candidate narrative.
2. 20 minutes - Progressive technical and product probes.
3. 8 minutes - Senior or staff scope, influence, and prioritization.
4. 5 minutes - Reflection and feedback.

### Practical build or take-home review

Use the workflow in [project deep dives and take-homes](08-project-deep-dives-and-take-homes.md):

- Time-box scope and state assumptions.
- Demonstrate the primary user path.
- Review architecture, tests, evaluation, failure handling, privacy, and operations.
- Explain shortcuts and the path to production.
- Defend what you did not build.

## Scorecard

Use the canonical scale and readiness rules in [mock interviews and scorecards](09-mock-interviews-and-scorecards.md). Score each dimension from 1 to 4:

- 1 - Weak or unsafe; behavior is missing, materially incorrect, or requires direct rescue.
- 2 - Partial; needs targeted prompting or misses important risks.
- 3 - Interview-ready; complete, independent, appropriate for the stated level, and successful on expected follow-ups.
- 4 - Strong senior or staff evidence; unusually clear and adaptive, shapes strategy, creates leverage, and handles second-order effects.

Dimensions:

1. User and job framing
   - Names the user, workflow, baseline, stakes, and desired outcome.
2. Product hypothesis and prioritization
   - Defines value, non-goals, riskiest assumption, sequencing, and decision criteria.
3. Architecture and implementation
   - Designs coherent application, data, model, state, tool, and operational boundaries.
4. Model and context judgment
   - Chooses models, prompts, retrieval, fine-tuning, or agents from evidence and constraints.
5. Evaluation and diagnosis
   - Defines task-level evals, slices, graders, thresholds, traces, and failure-driven iteration.
6. Metrics and experimentation
   - Connects offline quality to task success, adoption, retention, guardrails, and credible experiments.
7. UX and human control
   - Represents uncertainty and supports review, correction, approval, undo, escalation, and recovery.
8. Safety, privacy, and security
   - Applies data minimization, authorization, least privilege, untrusted-content handling, and audits.
9. Reliability, latency, and cost
   - Uses service objectives, budgets, fallbacks, degradation, unit economics, and rollback.
10. Senior or staff leadership
   - Shows ownership, prioritization, strategy, cross-functional influence, and durable leverage at the claimed level.
11. Communication
   - Structures the answer, states assumptions, compares alternatives, and responds directly to evidence.

The maximum is 44. All 11 dimensions are required. A total or score band describes one mock and never establishes readiness. Add short evidence for every score. General impressions such as "good product sense" do not produce useful practice.

Use [mock interviews and scorecards](09-mock-interviews-and-scorecards.md) to combine this role scorecard with the curriculum's full-loop practice.

## Readiness Gate

The [readiness rules in module 09](09-mock-interviews-and-scorecards.md#readiness-rules) are canonical. Treat Product AI loops as interview-ready only when all of the following are true:

- [ ] You can frame an ambiguous user problem, baseline, product hypothesis, and first experiment in 10 minutes.
- [ ] You can explain when deterministic software, search, RAG, generation, fine-tuning, or an agent is appropriate.
- [ ] You can design three user-facing AI systems from experience through operations and rollout.
- [ ] You can create a task-specific evaluation set, failure taxonomy, graders, slices, and launch thresholds.
- [ ] You can connect offline quality to task success, adoption, retention, latency, cost, safety, and reliability.
- [ ] You can explain the limits of A/B testing for a nondeterministic system.
- [ ] You can design uncertainty, review, approval, undo, escalation, and recovery into the user experience.
- [ ] You can threat-model prompt injection, data leakage, excessive tool permissions, and unsafe actions.
- [ ] You can estimate and defend latency and cost per successful task.
- [ ] You can describe launch stages, rollback triggers, degraded modes, and operational ownership.
- [ ] You have two project stories with clear personal contribution, decisions, failures, metrics, and iteration.
- [ ] Your senior or staff claims match your actual strategy, architecture, prioritization, influence, and leverage.
- [ ] Your three most recent relevant full Product AI mocks use different prompts.
- [ ] At least two mocks were scored by different interviewers, or one was independently double-scored before the debrief.
- [ ] Every required scorecard dimension scored at least 3 in at least two of the three mocks.
- [ ] No required dimension scored 1 in either of the two most recent mocks, and no hard fail remains unresolved.
- [ ] You finished the core scope within the stated time limit in at least two mocks.
- [ ] You handled at least one material follow-up without direct rescue in each of the two most recent mocks.
- [ ] Every known or repeated failure completed a successful re-test with a fresh prompt.

If one dimension remains at 1, treat it as a gate even when the total score is high. Use the weakest observed behavior to choose the next drill.

## Related Modules

- [Curriculum overview](README.md) - Track selection, interview loop, diagnostic, and eight-week operating rhythm.
- [Common core](01-common-core.md) - Python, APIs, distributed systems, ML, LLMs, evaluation, safety, observability, cost, and latency.
- [AI/ML system design](03-ai-ml-system-design.md) - Reusable design method, estimation, RAG, agents, serving, and failure analysis.
- [Senior and staff behavioral](07-senior-staff-behavioral.md) - Ownership, influence, conflict, prioritization, mentoring, and level-appropriate stories.
- [Project deep dives and take-homes](08-project-deep-dives-and-take-homes.md) - Project narratives, implementation exercises, and artifact review.
- [Mock interviews and scorecards](09-mock-interviews-and-scorecards.md) - Full-loop simulation, scoring, remediation, and readiness decisions.
- [Theory questions](../questions/01-theory.md) - Existing sourced conceptual questions across LLM, RAG, agents, and evaluation.
- [Project deep-dive questions](../questions/03-project-deep-dive.md) - Existing sourced questions and follow-up probes for project interviews.

Use the synthesized questions in this module for deliberate practice. Use the existing question files when you need their sourced collections. Do not present synthesized prompts as questions reported from a specific employer.
