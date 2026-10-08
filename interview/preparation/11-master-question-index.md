# Master Question Index for Senior AI Engineering Interviews

This index is a routing layer, not another exhaustive question bank. Use it to find the right preparation guide, choose a compact set of high-value prompts, and track whether an answer survives follow-up questions.

## How the Index Is Organized

Questions are organized in three layers:

1. The category index routes a topic to preparation guides and reported-question collections.
2. The prioritized set gives 100 synthesized prompts for senior candidates. Each prompt links to the section that contains the relevant framework, rubric, walkthrough, or drill.
3. The playlists turn prompt IDs into realistic interview loops for different timelines and tracks.

Track labels mean:

- `[Shared]` - useful for Product AI, Forward Deployed Engineer, and ML/AI Platform interviews.
- `[Product AI]` - emphasizes product judgment, end-to-end delivery, user experience, and learning loops.
- `[FDE]` - emphasizes discovery, customer architecture, integration, delivery, and adoption.
- `[Platform]` - emphasizes developer platforms, inference, reliability, capacity, governance, and migration.

The three priority groups serve different purposes:

- Must-answer - prepare these before specializing. A ready answer should withstand assumptions, trade-offs, failure modes, and measurement follow-ups.
- Track-specific - select the 13 prompts for the primary track, then sample from the other tracks where the target loop overlaps.
- Stretch/frontier - use after the must-answer set is stable or when targeting staff-level, infrastructure-heavy, or frontier-lab loops.

## Market-Priority Methodology

The order inside each priority section follows a market-weighted sequence:

- P0 - production AI system design, RAG, agents and tool use, evaluation, and observability.
- P1 - Python, APIs and integration, SQL and data, prompt and context engineering, and enterprise automation or workflows.
- P2 - cloud, containers, `CI/CD`, security and compliance, cost and latency, and full-stack delivery.
- P3 or title-confirmed - classical or deep training depth, fine-tuning, and GPU or inference internals unless the title, job description, recruiter, or diagnostic confirms them.

Apply these role-specific overrides:

- Product AI - P0 end-to-end shipping, `RAG`, and evaluation; P1 agents, prompt and context work, Python, APIs, integration, and workflows; P2 full-stack implementation, `SQL` and data, security, and cost.
- FDE - P0 production delivery, customer discovery, Python, and integration; P1 `RAG`, prompt engineering, evaluation, agents, and cloud deployment; P2 demos, POCs, adoption, and product feedback.
- Platform - P0 cloud, `Kubernetes`, `Docker`, `CI/CD`, reliability, and monitoring; P1 gateways, model lifecycle, multi-tenancy, security, and cost; P2 shared evaluation platforms, data systems, and `SQL`.

I use [responsibility prevalence](../../role/03-responsibilities.md), [market trends](../../job-market/trends.md), the [methodology appendix](../../job-market/trends-appendix.md), and the [FDE analysis](../../role/06-fde.md) as scheduling evidence. Building appears in 98.1% of postings, productionizing in 78.3%, evaluation in 68.5%, API integration in 62.4%, agents in 48.4%, and RAG in 42.0%; SQL rose from 9.8% to 34.8%. App-builder and agent archetypes represent 42.5% combined, while platform and DevOps archetypes represent 36.1% combined. Responsibility rates and archetype shares use all 4,894 published postings; the SQL trend uses only the ai-first subset. Product AI and Platform are proxy mappings. Direct FDE title share among all AI-engineering listings rose from roughly 2.0% to 3.6%; direct FDE rates use 146 deduplicated direct-title roles.

These shares overlap conceptually and posting prevalence is not interview frequency. The ordering changes what candidates practice first; it does not remove coding, project, behavioral, or role-specific reserves, because postings alone do not predict loop format. Priority membership remains must-answer, track-specific, or stretch/frontier; market tier controls order within those sections.

## Sourced Reports and Synthesized Practice Prompts

The files under [`../questions/`](../questions/) collect reported formats, questions, assignments, and source links. Treat a company association as sourced only when the question file supports it. Reports can be incomplete, role-dependent, or stale, so use them to learn the shape of a loop rather than predict an exact prompt.

The preparation modules and the 100 prompts below are synthesized practice material. They combine recurring interview skills into reusable drills and do not claim that any named company asks a particular question. Prompt labels identify preparation scope, not company attribution.

When adding a new question:

1. Record the source URL and date if it is a report.
2. Mark it `sourced` only when the attribution is explicit.
3. Mark rewritten, combined, or newly created prompts `synthesized`.
4. Link to a rubric or guide instead of copying a long answer into this index.

## Preparation Module Map

- [`README.md`](README.md) - choose a profile, diagnose readiness, and understand expected loops.
- [`01-common-core.md`](01-common-core.md) - shared software, ML, LLM, RAG, agent, evaluation, safety, and operations foundations.
- [`02-coding-and-leetcode.md`](02-coding-and-leetcode.md) - DSA, progressive implementation, practical Python, ML coding, SQL, and repetition.
- [`03-ai-ml-system-design.md`](03-ai-ml-system-design.md) - traditional, ML, LLM, RAG, agent, multimodal, and platform design.
- [`04-product-ai-engineer.md`](04-product-ai-engineer.md) - Product AI cases, metrics, evaluation, delivery, and senior ownership.
- [`05-forward-deployed-engineer.md`](05-forward-deployed-engineer.md) - discovery, customer architecture, deployment, delivery, adoption, and escalation.
- [`06-ml-ai-platform-engineer.md`](06-ml-ai-platform-engineer.md) - model gateways, inference, scheduling, lifecycle, reliability, security, cost, and migration.
- [`07-senior-staff-behavioral.md`](07-senior-staff-behavioral.md) - story bank, behavioral rubrics, leadership signals, and role-specific evidence.
- [`08-project-deep-dives-and-take-homes.md`](08-project-deep-dives-and-take-homes.md) - project narratives, architecture defense, take-home execution, and live extension.
- [`09-mock-interviews-and-scorecards.md`](09-mock-interviews-and-scorecards.md) - runnable mock formats, scorecards, error logs, and retest rules.
- [`10-eight-week-study-plan.md`](10-eight-week-study-plan.md) - weekly sequencing, study budgets, readiness gates, and trackers.

## Category Index

### Theory and foundations

- [Common-core must-know foundation](01-common-core.md#must-know-foundation) - Python, backend, SQL, distributed systems, ML, deep learning, and AI foundations.
- [Reported theory questions](../questions/01-theory.md#interview-questions) - reported and collected theory prompts.
- [Aggregate technical questions](../questions/questions.md#technical-questions) - broad technical bank with source notes.

### Coding and LeetCode

- [Coding round types](02-coding-and-leetcode.md#round-types) - DSA, implementation, practical coding, SQL, debugging, and AI-assisted rounds.
- [Prioritized LeetCode set](02-coding-and-leetcode.md#prioritized-leetcode-set) - pattern-based problem list.
- [Reported coding formats](../questions/02-coding.md#coding-round-formats) - implementation and algorithm round reports.
- [Aggregate coding problems](../questions/questions.md#coding-problems) - algorithm, practical, and AI-oriented coding prompts.

### ML coding

- [ML coding drills](02-coding-and-leetcode.md#ml-coding-drills) - regression, metrics, clustering, attention, sampling, batching, and similarity.
- [Reported ML and AI coding](../questions/02-coding.md#ml--ai-coding) - collected ML implementation examples.
- [Aggregate ML and AI coding](../questions/questions.md#ml--ai-coding) - additional implementation prompts.

### Traditional system design

- [Distributed-system foundations](03-ai-ml-system-design.md#distributed-system-foundations) - caching, queues, partitioning, consistency, idempotency, and multi-region design.
- [Traditional system design reports](../questions/04-ai-system-design.md#traditional-system-design) - distinction and expectations.
- [Aggregate traditional system design](../questions/questions.md#traditional-system-design) - collected non-AI design prompts.

### ML system design

- [Classic ML system design](03-ai-ml-system-design.md#classic-ml-system-design) - data, labels, training, evaluation, deployment, drift, and feedback.
- [AI system design reports](../questions/04-ai-system-design.md#questions) - reported design questions and formats.
- [System design answer structure](../questions/04-ai-system-design.md#how-to-prepare) - preparation guidance.

### LLM and RAG

- [LLM and RAG design](03-ai-ml-system-design.md#llm-and-rag-design) - ingestion through generation, evaluation, freshness, deletion, and access control.
- [Common-core embeddings, retrieval, and RAG](01-common-core.md#embeddings-retrieval-and-rag) - foundational trade-offs.
- [Reported RAG questions](../questions/01-theory.md#rag-systems) - collected theory prompts.
- [Aggregate RAG questions](../questions/questions.md#rag-systems) - broader RAG bank.

### Agents

- [Agentic systems design](03-ai-ml-system-design.md#agentic-systems) - orchestration, tools, state, permissions, termination, sandboxing, and evaluation.
- [Common-core agents and tool use](01-common-core.md#agents-and-tool-use) - foundational concepts.
- [Reported agent questions](../questions/01-theory.md#agents-and-tool-use) - collected theory prompts.
- [Aggregate agent questions](../questions/questions.md#agents-and-tool-use) - broader agent bank.

### Evaluation

- [Common-core evaluations and experimentation](01-common-core.md#evaluations-and-experimentation) - datasets, metrics, graders, experiments, and decision rules.
- [LLM and RAG evaluation](03-ai-ml-system-design.md#evaluation) - evaluation inside a system design.
- [Reported testing and evaluation questions](../questions/01-theory.md#testing-and-evaluation) - collected prompts.
- [Aggregate evaluation questions](../questions/questions.md#evaluation-and-metrics) - metrics and evaluation bank.

### Product AI

- [Product AI detailed preparation](04-product-ai-engineer.md#detailed-preparation-areas) - discovery through launch and iteration.
- [Product metrics and evaluation](04-product-ai-engineer.md#product-metrics-and-evaluation) - metric hierarchy and offline/online learning.
- [Product AI mock format](09-mock-interviews-and-scorecards.md#product-ai-case-45-60-minutes) - runnable case interview.

### FDE and customer cases

- [FDE discovery and requirement decomposition](05-forward-deployed-engineer.md#discovery-and-requirement-decomposition) - discovery and acceptance criteria.
- [FDE role-play and case walkthroughs](05-forward-deployed-engineer.md#detailed-role-play-and-case-walkthroughs) - customer cases from discovery through incident response.
- [FDE mock format](09-mock-interviews-and-scorecards.md#fde-discovery-and-customer-case-45-60-minutes) - runnable case interview.

### Platform and inference

- [Platform foundations and deep preparation](06-ml-ai-platform-engineer.md#foundations-and-deep-preparation) - gateway, serving, scheduling, lifecycle, SLOs, governance, and economics.
- [AI platform and inference serving](03-ai-ml-system-design.md#ai-platform-and-inference-serving) - system-design view.
- [Platform calculation drills](06-ml-ai-platform-engineer.md#calculation-drills) - memory, throughput, concurrency, queues, and cost.
- [Platform mock format](09-mock-interviews-and-scorecards.md#mlai-platform-design-45-60-minutes) - runnable platform interview.

### Project deep dive

- [Project narrative and architecture defense](08-project-deep-dives-and-take-homes.md#build-a-layered-project-narrative) - prepare 60-second, 5-minute, and 20-30 minute versions.
- [Synthesized deep-dive questions](08-project-deep-dives-and-take-homes.md#synthesized-project-deep-dive-questions) - practice bank.
- [Reported project questions](../questions/03-project-deep-dive.md#questions) - collected opening questions and probes.
- [Aggregate project deep dive](../questions/questions.md#project-deep-dive) - additional prompts.

### Take-home

- [Take-home operating strategy](08-project-deep-dives-and-take-homes.md#take-home-operating-strategy) - scope, vertical slice, testing, documentation, submission, and cuts.
- [Take-home archetypes](08-project-deep-dives-and-take-homes.md#three-take-home-archetypes) - RAG, agent, and gateway/evaluation variants.
- [Reported home assignments](../questions/06-home-assignments.md#assignment-examples) - collected assignment formats with sources.
- [Aggregate take-home assignments](../questions/questions.md#take-home-assignments) - broader assignment bank.

### Behavioral and leadership

- [Senior and staff evidence](07-senior-staff-behavioral.md#how-senior-and-staff-evidence-differ) - scope, ambiguity, influence, leverage, judgment, and accountability.
- [High-value behavioral rubrics](07-senior-staff-behavioral.md#high-value-question-rubrics) - 14 anchor rubrics.
- [Reported behavioral questions](../questions/05-behavioral.md#common-behavioral-questions) - collected behavioral prompts.
- [Aggregate behavioral questions](../questions/questions.md#behavioral-questions) - broader behavioral bank.

### Company-specific

- [Aggregate question collection](../questions/questions.md) - contains explicitly labeled company-specific coding and assignment subsections plus its source list.
- [Reported home assignments](../questions/06-home-assignments.md) - contains named examples and source links where available.
- [Theory question sources](../questions/01-theory.md#sources), [coding sources](../questions/02-coding.md#sources), [project sources](../questions/03-project-deep-dive.md#sources), [system design sources](../questions/04-ai-system-design.md#sources), and [behavioral sources](../questions/05-behavioral.md#sources) - verify attribution here before using a company name.

## Prioritized Senior Question Set

All 100 prompts in this section are synthesized. They are intentionally concise and distinct; the linked section supplies the answer method, rubric, or technical depth.

### Must-answer

#### P0 - Production AI, RAG, agents, evaluation, and observability

- Q012 `[Shared]` Design an enterprise RAG assistant from ingestion through grounded answer generation. [Walkthrough](03-ai-ml-system-design.md#anchor-walkthrough-1-enterprise-rag-assistant)
- Q013 `[Shared]` Preserve document permissions, deletion guarantees, and freshness across a RAG index. [Guide](03-ai-ml-system-design.md#freshness-deletion-and-access-control)
- Q014 `[Shared]` Define tool contracts and orchestration for an agent that acts on external systems. [Guide](03-ai-ml-system-design.md#orchestrator-and-tools)
- Q015 `[Shared]` Prevent loops, duplicate side effects, and runaway cost in a long-running agent. [Guide](03-ai-ml-system-design.md#termination-retries-and-compensation)
- Q016 `[Shared]` Build a representative evaluation set and release gate for a nondeterministic AI feature. [Guide](01-common-core.md#evaluations-and-experimentation)
- Q017 `[Shared]` Reconcile strong offline quality with weak online product outcomes. [Guide](04-product-ai-engineer.md#online-evaluation)
- Q018 `[Shared]` Design and calibrate an LLM-as-judge without treating its scores as ground truth. [Guide](01-common-core.md#evaluations-and-experimentation)
- Q021 `[Shared]` Define traces, metrics, logs, and SLOs that distinguish model, retrieval, tool, and application failures. [Guide](01-common-core.md#observability)
- Q026 `[Shared]` Design an AI coding copilot with secure context construction and measurable quality. [Walkthrough](03-ai-ml-system-design.md#anchor-walkthrough-2-ai-coding-copilot)
- Q027 `[Shared]` Design a support-resolution agent with human approval, durable state, and recovery from uncertain outcomes. [Walkthrough](03-ai-ml-system-design.md#anchor-walkthrough-3-support-resolution-agent)
- Q032 `[Shared]` Implement a concurrent evaluation runner with bounded work, retries, timeouts, and resumability. [Exercise](02-coding-and-leetcode.md#evaluation-runner)
- Q037 `[Product AI]` Turn an ambiguous user problem into a narrow AI use case, baseline, and launch decision. [Guide](04-product-ai-engineer.md#product-discovery-framing-and-prioritization)
- Q038 `[Product AI]` Choose among prompting, RAG, tools, fine-tuning, and deterministic code for a product feature. [Guide](04-product-ai-engineer.md#model-prompt-context-rag-and-agent-decisions)
- Q039 `[Product AI]` Define a metric hierarchy that connects AI quality to user behavior and business value. [Guide](04-product-ai-engineer.md#metric-hierarchy)
- Q040 `[Product AI]` Launch an AI feature with uncertainty-aware UX, safety controls, rollback, and a learning loop. [Guide](04-product-ai-engineer.md#reliability-cost-latency-launch-and-iteration)
- Q041 `[FDE]` Run discovery when a customer asks for an agent but cannot define success. [Rubric](05-forward-deployed-engineer.md#1-customer-asks-for-an-agent-without-success-criteria)
- Q042 `[FDE]` Convert ambiguous customer goals into acceptance criteria, architecture constraints, and a delivery plan. [Rubric](05-forward-deployed-engineer.md#2-convert-ambiguity-into-acceptance-criteria)
- Q043 `[FDE]` Scope a three-week POC that maximizes learning and has a credible production path. [Rubric](05-forward-deployed-engineer.md#9-scope-a-three-week-poc)
- Q044 `[FDE]` Respond when a technically successful pilot has low adoption and conflicting stakeholders. [Rubric](05-forward-deployed-engineer.md#10-pilot-meets-technical-metrics-but-lacks-adoption)
- Q045 `[Platform]` Define the product strategy and success metrics for an internal AI platform. [Guide](06-ml-ai-platform-engineer.md#platform-strategy-and-developer-experience)
- Q046 `[Platform]` Design a high-throughput inference service and calculate its capacity bottlenecks. [Walkthrough](06-ml-ai-platform-engineer.md#design-walkthrough-2-high-throughput-inference-platform)
- Q047 `[Platform]` Set SLOs, overload behavior, observability, and recovery for a shared model platform. [Guide](06-ml-ai-platform-engineer.md#observability-and-slos)
- Q048 `[Platform]` Migrate teams from fragmented model access to a paved road without blocking legitimate exceptions. [Guide](06-ml-ai-platform-engineer.md#migration-leadership-and-incidents)

#### P1 - Python, APIs, SQL, context, workflows, and loop reserves

- Q001 `[Shared]` Explain when Python threads, processes, and `asyncio` are appropriate in an AI service. [Guide](01-common-core.md#python-runtime-gil-async-and-concurrency)
- Q002 `[Shared]` Design an idempotent API operation that safely survives client retries and partial failure. [Guide](03-ai-ml-system-design.md#idempotency)
- Q003 `[Shared]` Model tenants, documents, versions, and access rules in SQL for an enterprise assistant. [Guide](03-ai-ml-system-design.md#data-modeling)
- Q005 `[Shared]` Design queue retries, dead-letter handling, and backpressure for a document pipeline. [Guide](03-ai-ml-system-design.md#queues-and-workflows)
- Q010 `[Shared]` Decide what belongs in the prompt, retrieved context, model weights, tools, and application code. [Guide](01-common-core.md#prompting-and-context-engineering)
- Q011 `[Shared]` Choose an embedding and similarity strategy, then describe how you would validate retrieval quality. [Guide](01-common-core.md#embeddings-retrieval-and-rag)
- Q028 `[Shared]` Design a multi-provider model gateway with routing, quotas, fallback, and accounting. [Walkthrough](03-ai-ml-system-design.md#anchor-walkthrough-4-multi-provider-model-gateway)
- Q033 `[Shared]` Implement precision, recall, F1, and threshold selection without library metric helpers. [Drills](02-coding-and-leetcode.md#metrics)
- Q034 `[Shared]` Explain one major project at 60-second, 5-minute, and 20-minute depth without changing the facts. [Guide](08-project-deep-dives-and-take-homes.md#build-a-layered-project-narrative)
- Q035 `[Shared]` Describe the largest outcome you owned and isolate your decisions, leverage, and measurable impact. [Rubric](07-senior-staff-behavioral.md#rubric-1-largest-owned-outcome)
- Q036 `[Shared]` Describe a failure caused by your judgment, the repair, and the durable change that followed. [Rubric](07-senior-staff-behavioral.md#rubric-7-failure-caused-by-judgment)

#### P2 - Security, cost, distributed delivery, and confirmed coding loops

- Q004 `[Shared]` Choose a cache policy and explain invalidation, stampede control, and stale-data behavior. [Guide](03-ai-ml-system-design.md#caches)
- Q019 `[Shared]` Threat-model prompt injection, malicious documents, and unsafe tool use. [Guide](03-ai-ml-system-design.md#threat-model)
- Q020 `[Shared]` Handle sensitive data, retention, auditability, and deletion in an AI application. [Guide](03-ai-ml-system-design.md#privacy-and-governance)
- Q022 `[Shared]` Reduce cost and latency while protecting quality and tail behavior. [Guide](01-common-core.md#cost-latency-and-capacity)
- Q023 `[Shared]` Estimate peak QPS, token throughput, concurrency, storage, and provider cost for a proposed service. [Guide](03-ai-ml-system-design.md#back-of-the-envelope-estimation)
- Q009 `[Shared]` Break end-to-end LLM latency into queueing, prefill, generation, network, and tool time. [Guide](01-common-core.md#llm-inference)
- Q024 `[Shared]` Design a multi-region notification service and defend consistency, partitioning, retries, and failure recovery. [Guide](03-ai-ml-system-design.md#distributed-system-foundations)
- Q029 `[Shared]` Solve a sliding-window problem while narrating invariants, complexity, and edge-case tests. [Drills](02-coding-and-leetcode.md#must-do-sliding-window)
- Q030 `[Shared]` Implement an LRU cache and explain concurrency, expiration, and production extensions. [Drills](02-coding-and-leetcode.md#must-do-caches-and-design)
- Q031 `[Shared]` Solve a graph traversal problem and justify representation, visited state, and complexity. [Drills](02-coding-and-leetcode.md#must-do-graphs)

#### P3 or title-confirmed - Classical ML, deep learning, recommendation, and inference depth

- Q006 `[Shared]` Diagnose data leakage and distribution shift in an apparently strong offline ML result. [Guide](03-ai-ml-system-design.md#data-labels-and-features)
- Q007 `[Shared]` Select metrics and thresholds for a high-cost false-positive, imbalanced classification problem. [Guide](01-common-core.md#classical-machine-learning-and-statistics)
- Q008 `[Shared]` Explain transformer attention, masking, positional information, and the main inference bottlenecks. [Guide](01-common-core.md#deep-learning-and-transformers)
- Q025 `[Shared]` Design an ML recommendation system covering labels, features, training, serving, drift, and feedback loops. [Guide](03-ai-ml-system-design.md#classic-ml-system-design)

### Track-specific

#### P0 - Product AI shipping, RAG, agents, and evaluation

- Q050 `[Product AI]` Design a support copilot from user workflow through evaluation, rollout, and iteration. [Case](04-product-ai-engineer.md#product-case-exercise-1-support-copilot)
- Q051 `[Product AI]` Design an enterprise document assistant and choose where citations, refusal, and feedback belong in the UX. [Case](04-product-ai-engineer.md#product-case-exercise-2-enterprise-document-assistant)
- Q052 `[Product AI]` Design a vendor-onboarding workflow and justify where agent autonomy should stop. [Case](04-product-ai-engineer.md#product-case-exercise-3-agent-workflow-for-vendor-onboarding)
- Q054 `[Product AI]` Define graceful degradation when the preferred model, retrieval service, or critical tool is unavailable. [Guide](03-ai-ml-system-design.md#graceful-degradation-ladder)
- Q055 `[Product AI]` Design feedback capture that supports learning without rewarding engagement or annotation noise blindly. [Guide](04-product-ai-engineer.md#evaluation-experimentation-and-feedback-loops)
- Q056 `[Product AI]` Explain when an A/B test is misleading for a nondeterministic AI experience. [Guide](04-product-ai-engineer.md#ab-testing-limits-in-nondeterministic-systems)
- Q060 `[Product AI]` Defend the end-to-end architecture and rejected alternatives for your strongest shipped AI product. [Guide](04-product-ai-engineer.md#project-deep-dive-preparation)
- Q061 `[Product AI]` Review a take-home AI application for product clarity, evaluation evidence, failure handling, and maintainability. [Guide](08-project-deep-dives-and-take-homes.md#prepare-for-code-review)

#### P0 - FDE customer production, discovery, Python, and integration

- Q062 `[FDE]` Map a customer's data, identity, network, deployment, and operational constraints before proposing architecture. [Guide](05-forward-deployed-engineer.md#customer-architecture-checklist)
- Q063 `[FDE]` Integrate with an unreliable customer API and an unrealistic sandbox without hiding delivery risk. [Rubric](05-forward-deployed-engineer.md#3-unreliable-api-and-unrealistic-sandbox)
- Q064 `[FDE]` Preserve permissions and tenant isolation in an enterprise RAG deployment. [Rubric](05-forward-deployed-engineer.md#4-preserve-permissions-in-enterprise-rag)
- Q065 `[FDE]` Turn a demo-quality prototype into a supported production system with explicit ownership boundaries. [Rubric](05-forward-deployed-engineer.md#5-prototype-to-production)
- Q067 `[FDE]` Diagnose why a strong demo fails on production customer data and reset expectations credibly. [Rubric](05-forward-deployed-engineer.md#7-poor-production-data-after-a-strong-demo)
- Q069 `[FDE]` Respond to a possible cross-tenant retrieval incident during a customer rollout. [Rubric](05-forward-deployed-engineer.md#11-possible-cross-tenant-retrieval)

#### P0 - Platform cloud and reliability

- Q079 `[Platform]` Design autoscaling signals that avoid oscillation and account for queueing, cold starts, and long requests. [Guide](06-ml-ai-platform-engineer.md#autoscaling)
- Q085 `[Platform]` Design regional disaster recovery for model artifacts, control plane, data plane, and queued work. [Guide](06-ml-ai-platform-engineer.md#disaster-recovery)
- Q087 `[Platform]` Explain a platform incident, including detection gaps, mitigation, customer communication, and systemic prevention. [Guide](06-ml-ai-platform-engineer.md#migration-leadership-and-incidents)

#### P1 - Product AI framing, prototyping, and workflow ownership

- Q049 `[Product AI]` Prioritize an AI feature when user value is plausible but model quality is not yet measurable. [Guide](04-product-ai-engineer.md#product-discovery-framing-and-prioritization)
- Q053 `[Product AI]` Build a prototype that tests the riskiest product assumption without becoming throwaway architecture. [Guide](04-product-ai-engineer.md#rapid-prototypes-and-end-to-end-engineering)
- Q059 `[Product AI]` Decide whether a recurring user request belongs on the roadmap, in configuration, or outside the product. [Guide](04-product-ai-engineer.md#senior-and-staff-ownership)

#### P1 - FDE evaluation, enterprise workflows, stakeholders, and reuse

- Q068 `[FDE]` Evaluate an AI workflow when labels are scarce, experts disagree, and customer feedback is delayed. [Rubric](05-forward-deployed-engineer.md#8-evaluate-without-reliable-labels)
- Q070 `[FDE]` Negotiate a high-value custom request that conflicts with the product roadmap. [Rubric](05-forward-deployed-engineer.md#12-high-value-customer-request-conflicts-with-roadmap)
- Q071 `[FDE]` Lead a customer program across sales, product, security, and engineering without direct authority. [Rubric](05-forward-deployed-engineer.md#13-lead-without-authority)
- Q072 `[FDE]` Give an executive update when technical uncertainty and schedule risk remain high. [Rubric](05-forward-deployed-engineer.md#14-executive-communication-under-uncertainty)
- Q073 `[FDE]` Convert a pattern learned across several accounts into reusable product or delivery capability. [Rubric](05-forward-deployed-engineer.md#15-productize-a-pattern-across-accounts)
- Q074 `[FDE]` Repair trust after sales committed an unsupported capability. [Rubric](05-forward-deployed-engineer.md#16-sales-committed-an-unsupported-capability)

#### P1 - Platform gateways, lifecycle, serving, and multi-tenant interfaces

- Q075 `[Platform]` Design stable model-gateway APIs that allow provider changes without leaking every provider feature. [Guide](06-ml-ai-platform-engineer.md#api-contracts)
- Q076 `[Platform]` Compare static batching, dynamic batching, and continuous batching under latency SLOs. [Guide](06-ml-ai-platform-engineer.md#dynamic-and-continuous-batching)
- Q081 `[Platform]` Enforce multi-tenant isolation without destroying accelerator utilization. [Guide](06-ml-ai-platform-engineer.md#multi-tenancy-and-isolation)
- Q082 `[Platform]` Manage model registration, validation, promotion, rollback, and deprecation across teams. [Guide](06-ml-ai-platform-engineer.md#model-registry-and-lifecycle)
- Q086 `[Platform]` Plan a progressive gateway migration that preserves provider-specific capabilities, rollback, and usage accounting. [Walkthrough](06-ml-ai-platform-engineer.md#design-walkthrough-1-multi-provider-model-gateway)

#### P2 - Product trust and cost-aware delivery

- Q057 `[Product AI]` Handle a failed AI launch where headline quality was acceptable but user trust fell. [Rubric](07-senior-staff-behavioral.md#rubric-9-failed-ai-launch)
- Q058 `[Product AI]` Make a cost-quality trade-off that changes the product experience, not only the model configuration. [Rubric](07-senior-staff-behavioral.md#rubric-12-cost-quality-trade-off)

#### P2 - FDE cloud and restricted deployment

- Q066 `[FDE]` Adapt one solution across vendor cloud, customer cloud, and restricted on-premises environments. [Rubric](05-forward-deployed-engineer.md#6-deploy-across-vendor-cloud-customer-cloud-and-on-premises)

#### P2 - Platform shared evaluation and economics

- Q083 `[Platform]` Build a shared evaluation platform with reproducibility, lineage, judge calibration, and release gates. [Guide](06-ml-ai-platform-engineer.md#evaluation-platform)
- Q084 `[Platform]` Allocate inference cost and enforce quotas while preserving capacity for critical workloads. [Guide](06-ml-ai-platform-engineer.md#cost-allocation-and-quotas)

#### P3 or title-confirmed - Platform GPU and inference internals

- Q077 `[Platform]` Estimate KV-cache capacity and explain prefix reuse, eviction, fragmentation, and admission control. [Drill](06-ml-ai-platform-engineer.md#drill-2-kv-cache-capacity)
- Q078 `[Platform]` Choose quantization and parallelism strategies for a model that does not fit on one accelerator. [Guide](06-ml-ai-platform-engineer.md#choosing-tensor-pipeline-and-data-parallelism)
- Q080 `[Platform]` Design GPU scheduling with priorities, quotas, preemption, gang scheduling, and checkpoint recovery. [Guide](06-ml-ai-platform-engineer.md#gpu-scheduling-preemption-and-checkpointing)

### Stretch and frontier

#### P1 - Product strategy and field-pattern leverage

- Q092 `[Product AI]` Design a product experiment that separates model improvement from workflow novelty and selection effects. [Guide](04-product-ai-engineer.md#product-metrics-and-evaluation)
- Q093 `[Product AI]` Decide when a product should expose model uncertainty, hide it, ask for clarification, or escalate to a human. [Guide](04-product-ai-engineer.md#ux-for-uncertainty-safety-and-privacy)
- Q094 `[Product AI]` Set a multi-quarter AI product strategy when model capabilities and unit economics are changing quickly. [Guide](04-product-ai-engineer.md#senior-and-staff-depth)
- Q096 `[FDE]` Build a portfolio-level risk view across accounts and decide which recurring field problems deserve product investment. [Guide](05-forward-deployed-engineer.md#multi-account-patterns)

#### P2 - Restricted delivery and commercial support cost

- Q095 `[FDE]` Design a restricted-environment deployment with no public egress, customer-managed keys, and audited updates. [Guide](05-forward-deployed-engineer.md#cloud-on-premises-and-restricted-environments)
- Q097 `[FDE]` Balance technical feasibility, customer value, contractual commitments, and long-term support cost in an escalation. [Guide](05-forward-deployed-engineer.md#risk-and-commercial-trade-offs)

#### P3 or title-confirmed - Training, fine-tuning, multimodal, and GPU internals

- Q088 `[Shared]` Explain data, tensor, pipeline, and expert parallelism and the communication bottleneck each introduces. [Guide](01-common-core.md#training-systems-and-scaling)
- Q089 `[Shared]` Reason about speculative decoding, paged attention, prefix caching, and kernel fusion under real workloads. [Guide](01-common-core.md#inference-kernels-and-advanced-serving)
- Q090 `[Shared]` Compare supervised fine-tuning, preference optimization, reward modeling, and inference-time search. [Guide](01-common-core.md#advanced-model-architecture-and-post-training)
- Q091 `[Shared]` Design a real-time multimodal assistant with interruption handling, streaming, safety, and latency budgets. [Guide](03-ai-ml-system-design.md#multimodal-and-real-time-systems)
- Q098 `[Platform]` Design a GPU training scheduler that supports elastic and gang-scheduled jobs, preemption, checkpointing, and fair sharing. [Walkthrough](06-ml-ai-platform-engineer.md#design-walkthrough-3-gpu-training-and-job-scheduler)
- Q099 `[Platform]` Derive model-weight, activation, and KV-cache memory bounds before selecting serving topology. [Guide](06-ml-ai-platform-engineer.md#activation-memory-bounds)
- Q100 `[Platform]` Evolve an inference platform for new accelerators and model architectures without forcing synchronized migrations. [Guide](06-ml-ai-platform-engineer.md#model-registry-and-lifecycle)

## Interview-Loop Playlists

Use the linked guide for timing and scoring, and use prompt IDs here to avoid duplicating content.

### One-day screen prep

Use this only for triage. Complete one spoken answer, one coding problem, one design outline, and one story; do not attempt to read every linked module.

- Production AI diagnosis - Q012, Q016, Q021
- Practical integration - Q001, Q002, or Q032
- Design - one of Q026-Q028, then Q023 if time permits
- Coding reserve for a confirmed loop - Q029 or Q030
- Project and behavioral - Q034, Q035, Q036
- Track finish - Product AI: Q037; FDE: Q041; Platform: Q046
- Score with the [common scoring scale](09-mock-interviews-and-scorecards.md#common-scoring-scale)

### One-week onsite prep

- Day 1 - diagnose with Q012-Q018, Q021, and the [readiness assessment](README.md#diagnostic-and-readiness-assessment).
- Day 2 - practice Python, integration, SQL, and evaluation with Q001-Q003, Q010, Q032, and Q033; keep Q029-Q031 as a confirmed-loop coding reserve under the [solve-and-review rubric](02-coding-and-leetcode.md#repeatable-solve-and-review-rubric).
- Day 3 - design two of Q026-Q028, then Q019-Q023; use Q024-Q025 only when distributed or classical ML depth is relevant.
- Day 4 - answer Q034-Q036 and two role-specific behavioral prompts from Q057-Q060, Q070-Q074, or Q087.
- Day 5 - run the primary-track playlist below.
- Day 6 - run one [project deep-dive mock](09-mock-interviews-and-scorecards.md#project-deep-dive-30-45-minutes) and one full design mock.
- Day 7 - retest only `needs work` items and stop heavy practice early.

### Product AI loop

- Shipping, RAG, and workflow cases - Q050-Q052, Q060, Q061
- Evaluation and product learning - Q039, Q055, Q056, Q092
- Architecture and AI choices - Q038, Q054
- Product sense, framing, and prototyping - Q037, Q049, Q053, Q059
- Delivery, trust, cost, and leadership - Q040, Q057, Q058, Q093, Q094
- Practical or take-home review - Q061
- Shared coding reserve - Q029, Q032, Q033
- Shared system-design reserve - Q023, Q026, Q027
- Shared project deep-dive reserve - Q034
- Shared behavioral and leadership reserve - Q035, Q036

Run the [Product AI case format](09-mock-interviews-and-scorecards.md#product-ai-case-45-60-minutes) and score against the [Product AI scorecard](09-mock-interviews-and-scorecards.md#product-ai-scorecard).

### FDE loop

- Customer production and integration - Q062-Q065, Q067
- Discovery, scoping, and Python integration - Q041-Q043, Q063
- RAG, evaluation, and incidents - Q064, Q068, Q069
- Production conversion and adoption - Q044, Q065, Q067
- Commercial and stakeholder judgment - Q070-Q074
- Restricted deployment and portfolio judgment - Q095-Q097
- Shared coding reserve - Q029, Q032, Q033
- Shared system-design reserve - Q012, Q014, Q020, Q023
- Shared project deep-dive reserve - Q034
- Shared behavioral and leadership reserve - Q035, Q036

Run the [FDE case format](09-mock-interviews-and-scorecards.md#fde-discovery-and-customer-case-45-60-minutes) and score against the [FDE scorecard](09-mock-interviews-and-scorecards.md#fde-scorecard).

### Platform loop

- Cloud operating model, reliability, and migration - Q047, Q048, Q079, Q085-Q087
- Platform strategy, gateway, and APIs - Q045, Q075, Q086
- Lifecycle, evaluation, and tenancy - Q081-Q083
- Serving and capacity - Q046, Q076
- Economics - Q084
- Title-confirmed GPU and inference internals - Q077, Q078, Q080, Q098-Q100
- Shared coding reserve - Q030-Q033
- Shared system-design reserve - Q023, Q028
- Shared project deep-dive reserve - Q034
- Shared behavioral and leadership reserve - Q035, Q036

Run the [Platform design format](09-mock-interviews-and-scorecards.md#mlai-platform-design-45-60-minutes) and score against the [ML/AI Platform scorecard](09-mock-interviews-and-scorecards.md#mlai-platform-scorecard).

### Frontier-lab variant

Start with the Platform loop's P0 and P1 groups, then modify it:

- Add Q008, Q009, Q023, and Q088-Q091 only after the role confirms frontier depth.
- Add Q098-Q100 for infrastructure-oriented roles.
- Add ML coding drills for [attention](02-coding-and-leetcode.md#attention), [sampling](02-coding-and-leetcode.md#sampling), and [batching and masking](02-coding-and-leetcode.md#batching-and-masking).
- Replace one behavioral prompt with Q010 or Q036 to test technical judgment and accountability.
- Keep frontier depth secondary unless the role description or recruiter confirms it.

## Question Tracking Template

Allowed statuses are `unseen`, `attempted`, `needs work`, and `ready`. A prompt becomes `ready` only after a timed answer earns the target score and survives at least two unprepared follow-ups.

Copy one block per prompt:

```text
Prompt ID:
Prompt title:
Track: shared | product-ai | fde | platform
Source type: synthesized | sourced
Source URL or report date:
Status: unseen | attempted | needs work | ready
Last attempt:
Retest date:
Time used:
Score:
Missed dimensions:
Weakest follow-up:
Next drill:
Evidence or artifact to improve:
```

Use this retest rhythm:

- `unseen` - schedule the first attempt within 7 days.
- `attempted` - review notes, then retry in 3-5 days.
- `needs work` - isolate one weakness and retry in 1-3 days.
- `ready` - retest in 7-14 days with a different interviewer or altered constraints.
- Any failed follow-up moves `ready` back to `needs work`.

The [error log taxonomy](09-mock-interviews-and-scorecards.md#error-log-taxonomy) standardizes missed dimensions, and the [retest schedule](09-mock-interviews-and-scorecards.md#re-test-schedule) provides the fuller practice loop.

## Random Mock Selection Rules

Randomization should preserve interview realism, not produce an arbitrary trivia mix.

1. Choose the loop first: shared design, Product AI, FDE, Platform, project, behavioral, or coding.
2. Exclude prompts attempted in the previous 72 hours.
3. Preserve the priority-membership mix over each rolling block of 20 prompts: 12 must-answer, 6 from the selected track's track-specific set, and 2 stretch/frontier prompts.
4. Weight the first 10 draws toward P0 and P1 with 6 P0, 3 P1, 1 P2, and no P3. Use the next 10 draws for 4 P0, 3 P1, 1 P2, and 2 P3 or title-confirmed prompts. This creates a 50.0%/30.0%/10.0%/10.0% P0/P1/P2/P3 mix while placing depth and stretch coverage later.
5. Place the 2 stretch/frontier membership slots in draws 11-20 unless an imminent confirmed loop requires one sooner. If P3 is not relevant, replace each P3 slot with P1 track-specific work.
6. In a full loop, include at least one coding prompt, one design or case prompt, one project prompt, and one behavioral prompt.
7. For a track mock, include at least one shared prompt and two prompts carrying that track label.
8. Do not reveal the selected prompt before the timer starts.
9. Have the interviewer draw two follow-ups from failure modes, scale changes, security, economics, ambiguous requirements, or conflicting metrics.
10. Record the random seed or selected IDs so the session can be reconstructed, but do not immediately repeat the same set.

For sessions shorter than 20 prompts, keep persistent shuffled queues for both priority membership and market tier, then consume the next compatible pair across sessions. Do not round each small session independently. Refill only after all 20 slots are consumed.

A simple manual draw:

```text
1. Filter by eligible priority and track.
2. Remove prompts used in the last 72 hours.
3. Create priority slots for 20 draws: 12 M, 6 T, and 2 S; constrain S to draws 11-20.
4. Create tier slots: early = P0 P0 P0 P0 P0 P0 P1 P1 P1 P2; later = P0 P0 P0 P0 P1 P1 P1 P2 P3 P3.
5. Shuffle within the early and later halves, then pair each priority slot with a compatible tier slot.
6. For a small session, consume the next compatible pair from the saved queues.
7. Draw one eligible prompt for each pair and satisfy the loop category rules.
8. Save unused slots for the next session; refill after draw 20.
9. Draw two follow-up dimensions separately.
10. Save prompt IDs only after the mock begins.
```

## Anti-Memorization Guidance

- Memorize answer structures, definitions, and verified personal facts, not scripts.
- Start each retry with changed scale, latency, privacy, deployment, data, or stakeholder constraints.
- Ask for assumptions before presenting architecture; do not force a memorized design onto a different problem.
- Require causal explanations: why a choice works, what would falsify it, and when another choice wins.
- Practice answers in 30-second, 2-minute, and full-depth forms.
- Rotate between whiteboard, spoken, and written formats.
- Use counterfactual follow-ups such as “What changes at 100 times traffic?” and “What if labels are unavailable?”
- For behavioral prompts, keep facts fixed while changing the interviewer’s probe order.
- For coding, reimplement the pattern on an unseen problem and explain invariants before syntax.
- For project deep dives, let the interviewer choose the branch instead of following a rehearsed presentation.
- Treat fluent recall without measurement, trade-offs, or failure analysis as `needs work`.

## Coverage and Maintenance Notes

The prioritized set contains 100 unique prompts:

- Must-answer - 48 prompts: 36 shared, 4 Product AI, 4 FDE, and 4 Platform.
- Track-specific - 39 prompts: 13 Product AI, 13 FDE, and 13 Platform.
- Stretch/frontier - 13 prompts: 4 shared, 3 Product AI, 3 FDE, and 3 Platform.
- Overall label balance - 40 shared prompts and 20 exclusive prompts for each of the three tracks.
- Market-tier balance - P0: 40 prompts; P1: 29 prompts; P2: 17 prompts; P3 or title-confirmed: 14 prompts.

Shared prompts count toward all three tracks in an actual study plan. Exclusive labels are balanced exactly so the index does not quietly privilege product, customer-delivery, or platform preparation.

When maintaining this file:

- Keep the prioritized set between 80 and 120 prompts.
- Check for duplicate intent, not only duplicate wording.
- Preserve exact track balance unless hiring evidence justifies a change.
- Verify every target file and heading before adding an anchored link.
- Link to a file without an anchor when heading behavior is uncertain.
- Keep company attribution in sourced-report files, not in synthesized prompt labels.
- Move detailed answers, rubrics, and large banks into the relevant module rather than expanding this index.
