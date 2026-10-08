# Common Core for Senior AI Engineering Interviews

This module is the shared technical foundation for Product AI Engineer, Forward Deployed Engineer, and ML/AI Platform Engineer interviews. It is intentionally prioritized. A senior candidate should be able to reason from requirements to production behavior across every must-know domain, then go deeper where the role demands it.

Use this module with the repository's [theory question bank](../questions/01-theory.md) and [hiring guide](../03-get-hired.md). Do not memorize definitions. Practice making a decision, naming a credible alternative, identifying failure modes, and defining how you would measure the result.

## How to Use This Module

For each domain:

1. Explain the concepts without notes in five minutes.
2. Answer one representative question aloud.
3. Complete the drill under a time limit.
4. Record gaps in an error log and repeat the weak part within one week.
5. Attach the topic to a real project, incident, or design decision from your experience.

A strong senior answer usually follows this shape:

1. Clarify the workload, users, constraints, and success criteria.
2. State assumptions and choose a simple baseline.
3. Compare alternatives using quality, reliability, security, latency, cost, and operability.
4. Describe failure modes, observability, degradation, and rollback.
5. Explain what evidence would cause you to revise the decision.

## Priority Levels

### Must-know

These topics are common gates across all three role families. The expected depth varies, but a critical gap can end an interview even when the rest of the profile is strong.

### Role-dependent

These topics deepen the shared core. Prioritize them when the job description, recruiter, or interview loop indicates product delivery, customer integration, or platform ownership.

### Frontier-lab-only

These topics matter mainly for research engineering, model training, inference-kernel, or frontier-model infrastructure roles. Do not displace production fundamentals unless the target role explicitly asks for them.

## Market-First Fast Path

When time is limited and the interview loop is not yet confirmed, study the must-know material in this sequence:

1. Evaluations and experimentation
2. Embeddings, retrieval, and RAG
3. Agents and tool use
4. API and backend engineering, distributed reliability, and production integration
5. Python concurrency, SQL and data modeling, prompting and context engineering, safety, observability, cost, and capacity
6. Classical ML, deep learning, transformer internals, and advanced inference at the depth required to make sound system choices

This sequence is market-first, not a claim about interview occurrence. The repository's [responsibility analysis](../../role/03-responsibilities.md) reports build and implement AI systems in 98.1% of postings, deployment in 78.3%, evaluation and quality in 68.5%, API and service integration in 62.4%, agents in 48.4%, RAG in 42.0%, and security and compliance in 40.1%. [Job-market trends](../../job-market/trends.md) show the integrator stack rising from 73.6% to 77.9% while the trainer stack fell from 36.1% to 27.2%; RAG app builder, cloud and ML platform engineer, and agent builder account for 25.6%, 21.3%, and 16.9% of the reported archetypes. Responsibility rates and archetype shares use all 4,894 published postings; integrator/trainer trends use only the ai-first subset. The [appendix](../../job-market/trends-appendix.md) provides the underlying cluster and endpoint details.

Classical ML and training depth are confirmed-loop or job-description dependent. Fine-tuning appears in 13.8% of responsibilities, compared with 2.5% for self-hosting, in the [responsibility analysis](../../role/03-responsibilities.md). You still need decision literacy: explain when classical ML, prompting, RAG, fine-tuning, hosted inference, or self-hosting is appropriate, what evidence would justify the choice, and which risks follow. Increase implementation and mathematical depth only when the target role or interview loop calls for it.

## Must-Know Foundation

### Python Runtime, GIL, Async, and Concurrency

Concrete concepts:

- Python object references, mutability, iterators, generators, context managers, decorators, typing, exceptions, and resource cleanup
- CPython reference counting, cyclic garbage collection, and why object lifetime is not a portable resource-management mechanism
- The global interpreter lock in standard CPython, what it protects, and why it does not make compound application operations atomic
- Threads for blocking I/O, processes or native code for CPU-bound parallelism, and `asyncio` for high-concurrency cooperative I/O
- Event loops, tasks, futures, cancellation, timeouts, backpressure, bounded concurrency, race conditions, locks, queues, and structured cleanup
- Serialization and process-boundary costs, thread-safety of clients, and the difference between concurrency, parallelism, and asynchrony

Representative interview questions:

- A Python API makes 100 independent model calls. When would you use threads, processes, or `asyncio`?
- What does the GIL prevent, and what races can still occur?
- Why can an async service become slower after adding more concurrent tasks?
- How would you cancel a fan-out request without leaking tasks or sockets?

What a strong senior answer demonstrates:

- Connects the choice to CPU time, blocking behavior, library support, memory, cancellation, and operational complexity
- Uses bounded concurrency rather than unbounded task creation
- Distinguishes language-level guarantees from implementation details and measures instead of relying on slogans about the GIL
- Accounts for client connection pools, timeouts, partial failure, retry amplification, and cleanup

Practice drills:

- Implement a bounded async worker pool that preserves input order, enforces per-item timeouts, and reports partial failures.
- Diagnose a race in a shared in-memory token counter, then fix it with both a lock-based and message-passing design.
- Benchmark sequential, threaded, process-based, and async versions of one I/O-heavy and one CPU-heavy workload.

### API and Backend Engineering

Concrete concepts:

- HTTP semantics, status codes, headers, authentication, authorization, TLS, request validation, pagination, streaming, and content negotiation
- Idempotency keys, retries, deadlines, circuit breakers, bulkheads, rate limits, quotas, and load shedding
- REST, RPC, webhooks, server-sent events, and WebSockets as workload-dependent choices
- Stateless handlers, connection pooling, dependency injection, configuration, schema evolution, backward compatibility, and contract tests
- Synchronous requests versus queued jobs; polling, callbacks, and resumable long-running operations
- Testing boundaries: unit, integration, end-to-end, fault injection, and load tests

Representative interview questions:

- Design an API for a long-running document extraction job that clients may retry.
- A model provider returns intermittent `429` and `503` responses. How should your service react?
- How would you evolve a response schema without breaking existing customers?
- Where should authentication, authorization, validation, and prompt construction occur?

What a strong senior answer demonstrates:

- Defines the contract and error model before implementation details
- Separates retryable from permanent failures and prevents duplicate side effects
- Propagates deadlines, caps retries with jittered backoff, and protects downstream dependencies
- Includes versioning, auditability, tenant isolation, tests, and rollout strategy

Practice drills:

- Build a small model-proxy API with validation, idempotency, deadlines, streaming, and a fake provider.
- Write a failure matrix for invalid input, client cancellation, provider timeout, quota exhaustion, and partial stream failure.
- Review an API for ambiguous status codes, unsafe retries, and missing authorization checks.

### SQL and Data Modeling

Concrete concepts:

- Joins, grouping, conditional aggregation, subqueries, common table expressions, window functions, and query plans
- Primary, foreign, unique, and check constraints; normalization, denormalization, and slowly changing dimensions
- Transactions, isolation levels, write skew, lost updates, locks, optimistic concurrency, and deadlocks
- B-tree and composite indexes, selectivity, covering indexes, partitioning, and the leftmost-prefix principle
- Online schema changes, backfills, dual reads or writes, data validation, and rollback
- Operational schemas versus analytical schemas; event time, processing time, late data, and deduplication

Representative interview questions:

- Write a query for each tenant's seven-day success rate and p95 latency, then rank regressions.
- Model documents, versions, chunks, embeddings, and access-control metadata for a RAG system.
- Why did an index fail to improve a query?
- How would you migrate a billion-row table without a long write outage?

What a strong senior answer demonstrates:

- Starts from access patterns, integrity requirements, retention, and scale
- Handles nulls, duplicate events, time zones, late arrival, and denominator definitions
- Reads an execution plan and explains index write costs, not only read benefits
- Treats migrations as staged production changes with validation and rollback

Practice drills:

- Solve joins, windows, funnels, retention, sessionization, and deduplication queries on a small event schema.
- Design the RAG schema above and list the three highest-volume queries and required indexes.
- Explain two transaction anomalies with concrete interleavings.

### Distributed Systems and Reliability

Concrete concepts:

- Partial failure, unreliable networks, timeouts, retries, idempotency, duplicate delivery, and ordering
- Replication, partitioning, leader election, quorum trade-offs, consistency models, and consensus at a conceptual level
- Queues, at-least-once delivery, deduplication, dead-letter handling, outbox patterns, and workflow state
- Backpressure, admission control, load shedding, graceful degradation, and dependency isolation
- Service-level indicators, objectives, error budgets, recovery objectives, incident response, and post-incident learning
- Stateless and stateful scaling, hot keys, skew, cache invalidation, and regional failure

Representative interview questions:

- A queue delivers the same document twice. How do you prevent duplicate downstream effects?
- Design for a provider outage without turning retries into a retry storm.
- When is eventual consistency acceptable in an AI product?
- What happens to your design when one tenant generates 50.0% of traffic?

What a strong senior answer demonstrates:

- Assumes partial failure and makes consistency guarantees explicit
- Places idempotency at the side-effect boundary and explains residual failure windows
- Uses budgets, bounded queues, and overload behavior instead of claiming infinite horizontal scaling
- Defines detection, ownership, runbooks, recovery, and learning

Practice drills:

- Trace a request across three services and enumerate every timeout, retry, and duplicate-execution path.
- Design an at-least-once ingestion worker with idempotent writes and poison-message handling.
- Write an SLO and alert policy for a user-facing answer-generation service.

### Classical Machine Learning and Statistics

Treat implementation and mathematical depth here as confirmed-loop or job-description dependent. Retain enough decision literacy to select metrics, detect leakage and shift, compare a simple classical baseline with an LLM approach, and defend when conventional ML is the better system.

Concrete concepts:

- Train, validation, and test splits; leakage; distribution shift; bias and variance; regularization; and cross-validation
- Linear and logistic regression, trees and ensembles, clustering, feature scaling, missing data, and class imbalance
- Precision, recall, specificity, F1, ROC-AUC, PR-AUC, log loss, calibration, ranking metrics, and threshold selection
- Sampling, confidence intervals, hypothesis tests, power, multiple comparisons, and practical versus statistical significance
- Offline versus online metrics, causal limitations of observational data, and experiment guardrails
- Model interpretability, feature importance limits, drift, retraining triggers, and reproducibility

Representative interview questions:

- Which metric would you use for a rare harmful-output detector, and how would you choose its threshold?
- Your validation score improved but production performance fell. What do you investigate?
- Explain regularization through both an optimization and a generalization lens.
- How would you decide whether a 1.0% experiment lift is real and worth shipping?

What a strong senior answer demonstrates:

- Grounds the metric in asymmetric error costs and the decision being made
- Audits labels, splits, leakage, segments, calibration, and distribution shift before changing the model
- Separates correlation, statistical confidence, and business significance
- Defines a reproducible baseline and an incremental experiment

Practice drills:

- Implement classification metrics and threshold selection without a metrics library.
- Find leakage in three deliberately flawed dataset-splitting scenarios.
- Draft an experiment with hypothesis, randomization unit, power assumptions, guardrails, and stopping rule.

### Deep Learning and Transformers

Transformer behavior and model-selection literacy remain part of the shared core. Treat deep-training and fine-tuning depth as confirmed-loop or job-description dependent rather than allowing it to displace evaluation, RAG, agents, or production integration by default.

Concrete concepts:

- Tensors, matrix multiplication, computation graphs, backpropagation, gradient descent, normalization, initialization, and regularization
- Embedding layers, sequence batching, padding, masks, and numerical stability
- Self-attention, scaled dot products, multi-head attention, positional information, residual connections, layer normalization, and feed-forward blocks
- Encoder-only, decoder-only, and encoder-decoder architectures
- Pretraining, supervised fine-tuning, preference optimization, parameter-efficient fine-tuning, and catastrophic forgetting
- Tokenization and how vocabulary, sequence length, and data distribution affect behavior and cost

Representative interview questions:

- Walk through the shapes and computation of causal self-attention.
- Why divide attention logits by the square root of key dimension?
- When would you use prompting, RAG, or fine-tuning?
- Why can training loss improve while task quality does not?

What a strong senior answer demonstrates:

- Tracks tensor shapes and masks precisely
- Connects architecture to memory, compute, data, latency, and task fit
- Avoids treating fine-tuning as a way to inject frequently changing facts
- Distinguishes optimization objectives from product quality and proposes task-level evaluation

Practice drills:

- Implement single-head causal attention with stable softmax and tests for mask behavior.
- Explain one transformer block at a whiteboard, including every tensor shape.
- Create a decision memo comparing prompting, RAG, and fine-tuning for one product feature.

### LLM Inference

Concrete concepts:

- Prefill and decode phases, time to first token, inter-token latency, throughput, and end-to-end latency
- Autoregressive decoding, temperature, greedy decoding, top-k, top-p, stop conditions, and structured outputs
- KV caching, continuous batching, memory bandwidth, prompt length, output length, and head-of-line blocking
- Quantization, model routing, speculative decoding, caching, and quality-efficiency trade-offs
- Hosted versus self-hosted serving, cold starts, accelerator utilization, replicas, and admission control
- Tokenization differences, context limits, truncation, and reproducibility limits

Representative interview questions:

- Why does a long prompt affect time to first token differently from output length?
- How does KV caching change decode compute and memory?
- Design a serving policy for mixed interactive and batch workloads.
- When should you route to a smaller model?

What a strong senior answer demonstrates:

- Separates prefill, decode, queueing, network, and application latency
- Reasons with tokens per second, concurrent sequences, memory, and quality rather than model size alone
- Protects interactive traffic from large batch requests and defines overload behavior
- Requires evaluation before routing or quantization changes

Practice drills:

- Estimate capacity and monthly cost from request rate, prompt tokens, output tokens, concurrency, and target latency.
- Benchmark two models with warmup, fixed datasets, latency percentiles, quality checks, and cost per successful task.
- Implement top-k and top-p sampling with deterministic seeded tests.

### Prompting and Context Engineering

Concrete concepts:

- Clear task instructions, delimiters, examples, output schemas, constraints, and abstention behavior
- System, developer, user, retrieved, and tool content as sources with different trust levels
- Context selection, ordering, compression, truncation, long-context failure, and prompt versioning
- Structured generation, validation, repair, and separation of instructions from untrusted data
- Few-shot examples, decomposition, self-checks, and the limits of hidden reasoning requests
- Prompt tests, regression datasets, model-specific behavior, and reproducibility

Representative interview questions:

- A prompt works in a notebook but fails in production. How do you debug it?
- How would you fit a large case history into a limited context window?
- When do examples help, and when do they anchor the model incorrectly?
- How do you prevent retrieved text from overriding application instructions?

What a strong senior answer demonstrates:

- Treats prompts as versioned application logic with tests and observability
- Selects context by task value, trust, freshness, and token budget
- Uses schemas and deterministic validators for machine-consumed output
- Recognizes prompt injection as a trust-boundary problem, not a wording problem

Practice drills:

- Create three prompt versions, a 30-case dataset, and a blind comparison rubric.
- Reduce a prompt's token count while preserving measured task quality.
- Build a context packer that reserves output tokens and records every included or excluded item.

### Embeddings, Retrieval, and RAG

Concrete concepts:

- Dense, sparse, and hybrid retrieval; cosine similarity, dot product, normalization, and embedding dimensionality
- Chunking by structure or semantics, overlap, metadata, document versions, and access control
- Approximate nearest-neighbor indexes, recall-latency-memory trade-offs, filtering, and index freshness
- Query rewriting, multi-query retrieval, reranking, context assembly, citations, and abstention
- Retrieval evaluation with recall at k, precision at k, mean reciprocal rank, normalized discounted cumulative gain, and answer-level evaluation
- Ingestion, deduplication, deletion, re-embedding, tenant isolation, and source-of-truth boundaries

Representative interview questions:

- A RAG answer is wrong. How do you determine whether retrieval or generation failed?
- How would you chunk tables, code, or long policy documents?
- When is keyword search better than embeddings?
- How do you enforce document permissions throughout retrieval?

What a strong senior answer demonstrates:

- Decomposes the pipeline and evaluates each stage independently
- Establishes lexical and simple dense baselines before adding complex retrieval
- Treats authorization as a hard filter, not a prompt instruction
- Plans for update, deletion, versioning, citations, and no-answer behavior

Practice drills:

- Build a small hybrid retrieval benchmark with labeled relevant documents and report recall at k plus latency.
- Perform failure analysis on 20 bad answers and classify ingestion, retrieval, reranking, context, or generation causes.
- Design deletion and re-indexing behavior for a multi-tenant corpus.

### Agents and Tool Use

Concrete concepts:

- Workflows versus agents, model-driven decisions versus deterministic orchestration, and explicit state machines
- Tool schemas, argument validation, permissions, authentication, idempotency, retries, and compensation
- Planning, memory, context management, termination, budgets, checkpoints, and human approval
- Sandboxing, least privilege, untrusted tool output, prompt injection, and irreversible actions
- Trace-based evaluation, tool-selection accuracy, task completion, step efficiency, and recovery behavior
- Durable execution, resumability, concurrency conflicts, and audit logs

Representative interview questions:

- When is an agent the wrong architecture?
- How would you stop loops and uncontrolled spending?
- A tool succeeds but its response is lost. What happens on retry?
- How do you safely let an agent send messages or execute code?

What a strong senior answer demonstrates:

- Chooses deterministic workflows when the path is known and spends autonomy only where it adds value
- Enforces budgets and permissions in code outside the model
- Designs tools as production APIs with typed schemas and idempotency
- Evaluates complete trajectories and recovery, not only final-answer style

Practice drills:

- Implement a bounded tool loop with a step budget, deadline, allowlist, argument validation, and approval gate.
- Draw failure transitions for a three-tool workflow and identify safe retry points.
- Compare an agent with a deterministic workflow on the same 25 tasks.

### Evaluations and Experimentation

Concrete concepts:

- Task definition, acceptance criteria, representative datasets, slices, hard negatives, and contamination
- Deterministic checks, human review, model-based graders, pairwise comparison, and grader calibration
- Retrieval, generation, agent-trajectory, safety, latency, and cost metrics
- Regression tests, confidence intervals, inter-rater agreement, error taxonomies, and release gates
- Offline evaluation, shadow traffic, canaries, A/B tests, counterfactual limits, and feedback loops
- Versioning of data, prompts, models, tools, graders, and code

Representative interview questions:

- Design an evaluation for a customer-support assistant.
- When can an LLM judge be trusted?
- Offline quality improved but user retention did not. What does that mean?
- How would you detect a regression affecting only one tenant or language?

What a strong senior answer demonstrates:

- Starts with the product decision and failure costs, not a generic metric list
- Uses multiple complementary evaluators and calibrates automated graders against humans
- Reports slices, uncertainty, and regressions instead of only an average
- Connects offline gates to staged online evidence and rollback

Practice drills:

- Create a 50-case golden set with taxonomy, source, expected behavior, and critical slices.
- Calibrate a model-based grader against blinded human labels and inspect disagreement.
- Write a release policy combining quality, safety, latency, and cost thresholds.

### Safety, Security, and Privacy

Concrete concepts:

- Threat modeling, trust boundaries, authentication, authorization, least privilege, secret management, and auditability
- Prompt injection, indirect injection, data exfiltration, insecure output handling, unsafe code execution, and excessive agency
- Input and output controls, sandboxing, allowlists, human approval, rate limits, and abuse monitoring
- Data classification, minimization, encryption, retention, deletion, residency, and vendor use
- Tenant isolation, access-controlled retrieval, logging redaction, and incident response
- Safety policy, refusal behavior, false-positive trade-offs, red teaming, and defense in depth

Representative interview questions:

- A retrieved document instructs the agent to reveal secrets. How does your design contain it?
- What data may be sent to a third-party model provider?
- How would you execute model-generated code?
- How do safety filters change for low-risk summarization versus a high-impact workflow?

What a strong senior answer demonstrates:

- Builds a threat model around assets, actors, entry points, and impact
- Enforces authorization and permissions outside the model
- Minimizes sensitive data and verifies provider, retention, and residency constraints
- Uses layered controls, monitoring, drills, and response plans without claiming perfect prevention

Practice drills:

- Threat-model a RAG agent with five attack paths and concrete mitigations.
- Review a logging schema for secrets, personal data, retention, and access.
- Design a sandbox and approval flow for code execution and external side effects.

### Observability

Concrete concepts:

- Metrics, logs, traces, profiles, correlation identifiers, and structured events
- Request rate, errors, latency percentiles, saturation, queue depth, and dependency health
- Prompt, model, retrieval, tool, and evaluation version lineage
- Time to first token, inter-token latency, tokens per second, cache hit rate, tool failures, and cost per successful task
- Quality proxies, sampled review, drift, data freshness, and privacy-aware trace capture
- Symptom-based alerts, dashboards, runbooks, sampling, and cardinality control

Representative interview questions:

- What would you instrument in a multi-step RAG agent?
- How do you monitor quality when ground truth arrives late?
- A p95 latency alert fires. How do you localize the cause?
- What should never appear in traces?

What a strong senior answer demonstrates:

- Links telemetry across user request, retrieval, generation, and tools without exposing sensitive content
- Separates service health, model behavior, product outcomes, and business metrics
- Uses distributions and slices rather than averages
- Makes telemetry actionable with ownership, alerts, runbooks, and retention policy

Practice drills:

- Define a trace schema for an AI request and mark sensitive fields.
- Diagnose three synthetic incidents using only metrics, logs, and traces.
- Design one operational dashboard and one quality dashboard, each with explicit decisions it supports.

### Cost, Latency, and Capacity

Concrete concepts:

- Requests per second, concurrency, Little's Law, utilization, queueing, throughput, and tail latency
- Token-based pricing, accelerator-hour cost, storage, retrieval, network egress, and engineering overhead
- Prompt and output token budgets, caching, batching, model routing, quantization, and asynchronous processing
- Peak versus average load, tenant quotas, burst handling, headroom, autoscaling delay, and cold starts
- Cost per request, per successful task, per tenant, and per product outcome
- Capacity experiments, load tests, admission control, and degradation policies

Representative interview questions:

- Estimate the monthly cost of one million daily requests.
- Why did average latency remain flat while p99 doubled?
- How many replicas do you need, and what assumptions dominate the estimate?
- What would you degrade first during overload?

What a strong senior answer demonstrates:

- Calculates with explicit units and ranges, then tests sensitivity to uncertain assumptions
- Optimizes cost per successful outcome rather than raw token price
- Reserves headroom and accounts for queueing, bursts, failures, and scaling delay
- Protects critical work with quotas, priorities, and graceful degradation

Practice drills:

- Complete a 15-minute back-of-the-envelope estimate for three traffic scenarios.
- Build a load-test plan that identifies the saturation point and tail-latency behavior.
- Propose three cost reductions and specify the quality regression test for each.

## Role-Dependent Depth

The shared core remains mandatory. Add the following depth based on the role rather than studying every branch equally.

### Product AI Engineer

Prioritize:

- API and backend engineering for streaming UX, background jobs, fallbacks, and product integration
- Prompting, RAG, agents, and structured outputs tied to a clear user workflow
- Evaluation design that connects task quality to adoption, completion, retention, or human effort
- Safety, privacy, latency, and cost as visible product constraints
- Experiment design, feedback capture, and rapid rollback

Representative interview questions:

- Should this feature use a workflow, an agent, or no model at all?
- How would you launch an assistant when the ideal quality metric arrives weeks later?
- What UX should appear when retrieval confidence is low or generation times out?

Strong senior answers connect model behavior to user decisions, define a narrow first release, instrument it, and explain how evidence changes the roadmap.

Practice drills:

- Write a one-page feature proposal with user problem, baseline, evaluation, launch gate, failure UX, and cost target.
- Compare two models using quality per dollar and user-visible latency.
- Use [`04-product-ai-engineer.md`](04-product-ai-engineer.md) for deeper product cases.

### Forward Deployed Engineer

Prioritize:

- API, identity, networking, SQL, data mapping, and deployment in unfamiliar customer environments
- Discovery, scope control, acceptance criteria, and the path from proof of concept to supported production
- Reliability, observability, security, privacy, and incident ownership across organizational boundaries
- Data-quality diagnosis and integration testing
- Clear communication for technical and nontechnical stakeholders

Representative interview questions:

- A customer asks for an agent but cannot define success. What do you do in the first week?
- Their identity provider, data schema, and deployment constraints differ from your assumptions. How do you re-scope?
- The demo works, but production data quality is poor. How do you handle expectations and delivery?

Strong senior answers uncover constraints before prescribing architecture, separate reversible discovery from production commitments, and define ownership and handoff.

Practice drills:

- Run a 30-minute discovery role-play and produce requirements, risks, open questions, and acceptance criteria.
- Design an integration test plan for a customer API with unreliable sandbox data.
- Use [`05-forward-deployed-engineer.md`](05-forward-deployed-engineer.md) for deeper customer-delivery cases.

### ML/AI Platform Engineer

Prioritize:

- Distributed systems, multi-tenancy, reliability, observability, and capacity
- Inference scheduling, batching, routing, caching, accelerator utilization, and workload isolation
- Platform contracts, quotas, identity, policy, audit, versioning, and developer experience
- Rollouts, migrations, canaries, incident response, and cost allocation
- Training or evaluation pipelines when required by the platform scope

Representative interview questions:

- Design a multi-tenant model gateway with per-team budgets and reliability targets.
- How would you isolate interactive inference from batch evaluation?
- When should application teams receive a shared abstraction versus direct provider access?

Strong senior answers define the platform's users and contract, quantify workloads, expose appropriate control, and include adoption and migration rather than only infrastructure.

Practice drills:

- Design a serving platform with workload classes, quotas, routing, observability, and chargeback.
- Estimate accelerator capacity under peak load and model three failure scenarios.
- Use [`06-ml-ai-platform-engineer.md`](06-ml-ai-platform-engineer.md) for deeper platform cases.

## Frontier-Lab-Only Depth

Prioritize this section only when the role explicitly covers model research, large-scale training, inference kernels, or frontier-model systems.

### Training systems and scaling

Concrete concepts:

- Data, tensor, pipeline, and expert parallelism
- Collective communication, checkpointing, fault recovery, stragglers, and reproducibility
- Mixed precision, gradient accumulation, activation checkpointing, optimizer state, and memory accounting
- Scaling laws, data quality, deduplication, contamination, and curriculum

Representative interview questions:

- Partition a transformer training workload across accelerators and identify communication bottlenecks.
- Estimate memory for parameters, gradients, optimizer state, and activations.
- How would you recover from worker failure without corrupting training state?

Strong answers track tensor shapes, bytes, communication, failure boundaries, and experimental validity. A useful drill is to calculate memory and communication for a toy transformer, then explain which parallelism strategy fits two different cluster topologies.

### Inference kernels and advanced serving

Concrete concepts:

- GPU execution, memory hierarchy, kernel fusion, arithmetic intensity, and profiling
- Paged KV caches, prefix caching, continuous batching, speculative decoding, and disaggregated prefill or decode
- Quantization calibration, quality loss, tensor parallel communication, and topology-aware placement

Representative interview questions:

- Is decode compute-bound or memory-bandwidth-bound for this workload?
- How does paged attention reduce KV-cache fragmentation?
- What would you profile before writing a custom kernel?

Strong answers measure before optimizing, distinguish hardware limits from scheduling limits, and preserve numerical and task-level correctness. A useful drill is to profile an attention or matrix-multiplication workload and explain each bottleneck with roofline-style reasoning.

### Advanced model architecture and post-training

Concrete concepts:

- Grouped-query and multi-query attention, mixture-of-experts routing, rotary position embeddings, and long-context methods
- Instruction tuning, preference data, reward models, direct preference optimization, reinforcement-learning variants, and rejection sampling
- Distributed evaluation, contamination controls, capability and safety trade-offs, and emergent failure analysis

Representative interview questions:

- Compare multi-head, grouped-query, and multi-query attention at inference.
- What failure modes can preference optimization introduce?
- How would you know whether a benchmark gain reflects generalization or contamination?

Strong answers connect objective, data, architecture, systems cost, and measured behavior. A useful drill is to implement a small architectural component, track shapes and memory, and design an ablation that isolates its effect.

## Cross-Domain Senior Questions

Use these to test whether isolated knowledge transfers into production judgment:

- Design a document assistant from ingestion through retrieval, generation, evaluation, authorization, observability, and deletion.
- A provider model update improves average quality but worsens one high-value tenant and doubles p99 latency. Decide whether and how to ship.
- An agent repeatedly calls a non-idempotent billing tool after network timeouts. Contain the incident and redesign the workflow.
- A new embedding model improves offline recall but requires a full re-index. Plan validation, migration, capacity, rollback, and cost.
- Traffic grows by 10 times during a launch. Estimate capacity, define admission control, and choose degradation behavior.

For full design practice, continue to [`03-ai-ml-system-design.md`](03-ai-ml-system-design.md). For project evidence, use [`08-project-deep-dives-and-take-homes.md`](08-project-deep-dives-and-take-homes.md). Use [`09-mock-interviews-and-scorecards.md`](09-mock-interviews-and-scorecards.md) to score observable performance.

## Self-Assessment

Score each item from 0 to 2:

- 0 - I cannot explain or apply it without substantial help.
- 1 - I know the main idea but miss trade-offs, failure modes, or implementation details.
- 2 - I can solve a representative problem, defend alternatives, and connect it to production evidence.

Assess the must-know domains:

- [ ] Python runtime, GIL, async, and concurrency
- [ ] API and backend engineering
- [ ] SQL and data modeling
- [ ] Distributed systems and reliability
- [ ] Classical ML and statistics
- [ ] Deep learning and transformers
- [ ] LLM inference
- [ ] Prompting and context engineering
- [ ] Embeddings, retrieval, and RAG
- [ ] Agents and tool use
- [ ] Evaluations and experimentation
- [ ] Safety, security, and privacy
- [ ] Observability
- [ ] Cost, latency, and capacity

The maximum shared-core score is 28.

- 0-13 - Foundation gaps dominate. Extend the schedule and repair zeros before running many mocks.
- 14-20 - Developing. Alternate focused study with timed drills and verbal follow-ups.
- 21-25 - Practice ready. Shift toward integrated designs, project defense, and mock interviews.
- 26-28 - Simulation ready. Maintain retrieval practice and target role-specific depth.

Do not let the total hide a zero in a likely interview gate. Repeat the assessment at the end of weeks 4 and 7, and require recent timed evidence before assigning a 2.

## Completion Gate

Move from shared-core study to mostly mock interviews when you can:

- Explain every must-know domain in plain language and answer two levels of follow-up.
- Complete at least one drill in each domain and repeat failed drills successfully.
- Solve the cross-domain document-assistant prompt with explicit estimates and failure handling.
- Tie at least eight domains to specific decisions from your own work.
- State where your target role needs deeper knowledge and where frontier-lab depth is unnecessary.
- Pass the coding readiness gate in [`02-coding-and-leetcode.md`](02-coding-and-leetcode.md).
- Follow the broader preparation guidance in [Getting Hired](../03-get-hired.md) and use [`10-eight-week-study-plan.md`](10-eight-week-study-plan.md) to schedule the remaining work.
