# Senior and Staff AI/ML System Design

This guide provides one reusable method for software, classical ML, LLM, agentic, multimodal, inference, and AI platform design interviews. The goal is not to recite a reference architecture. The goal is to make assumptions explicit, quantify the workload, choose the simplest design that meets the quality goals, and show how the system behaves when models, dependencies, data, or people fail.

Use this guide after [`01-common-core.md`](01-common-core.md). Use the [AI system design question bank](../questions/04-ai-system-design.md) for additional prompts and sources. Add role-specific depth from [`04-product-ai-engineer.md`](04-product-ai-engineer.md), [`05-forward-deployed-engineer.md`](05-forward-deployed-engineer.md), or [`06-ml-ai-platform-engineer.md`](06-ml-ai-platform-engineer.md).

## What the Interviewer Is Testing

A strong answer connects eight concerns:

- Product and user outcome - who uses the system, what decision or task it improves, and what a safe failure looks like
- Quality - the measurable meaning of a correct, useful, grounded, calibrated, or complete result
- Scale and economics - traffic, data, tokens, accelerators, latency, storage, and cost per successful outcome
- Contracts - APIs, events, schemas, versioning, identity, and ownership boundaries
- Architecture - request paths, asynchronous paths, state, control planes, and data planes
- Operations - SLOs, observability, incident response, rollback, migration, and graceful degradation
- Risk - security, privacy, safety, compliance, tenant isolation, and human authority
- Evolution - a narrow first release, evidence-driven improvements, and the path to larger scale

Senior candidates should independently drive an ambiguous design through production behavior. Staff candidates should also define durable interfaces, sequence investments, manage migration and adoption, and explain how multiple teams make safe decisions on the platform.

## Market-Weighted Default Prompt Order

When the company has not disclosed its design prompts, use this default practice spine:

1. Enterprise workflow and RAG systems
2. Agent workflows with bounded tools and durable state
3. Evaluation platforms and release gates
4. Model gateways, APIs, and enterprise integration
5. Production reliability, security, privacy, compliance, and graceful degradation

This order follows job-posting demand, not measured interview frequency. The repository's [responsibility analysis](../../role/03-responsibilities.md) reports build and implement AI systems in 98.1% of postings, deployment in 78.3%, evaluation and quality in 68.5%, API and service integration in 62.4%, agents in 48.4%, RAG in 42.0%, and security and compliance in 40.1%. [Job-market trends](../../job-market/trends.md) identify RAG app builder at 25.6%, cloud and ML platform engineer at 21.3%, and agent builder at 16.9%; the integrator stack rose from 73.6% to 77.9% while the trainer stack fell from 36.1% to 27.2%. Responsibility rates and archetype shares use all 4,894 published postings; integrator/trainer trends use only the ai-first subset. The [trends appendix](../../job-market/trends-appendix.md) provides the cluster and endpoint details.

Use classic recommendation and fraud designs as classic-ML-loop prompts: keep them in rotation when the job description, recruiter, or company evidence indicates prediction, ranking, experimentation, or conventional ML depth. Use GPU schedulers, deep inference, and self-hosted serving as Platform or job-description-specific prompts. Fine-tuning appears in 13.8% of responsibilities and self-hosting in 2.5% in the [responsibility analysis](../../role/03-responsibilities.md), so retain decision and trade-off literacy without making niche serving depth the default for every role.

## The 45-60 Minute Answer Framework

Write the section names on the board at the start. Tell the interviewer that you will adjust depth based on their priorities.

### Default 55-minute allocation

1. Minutes 0-5: clarify requirements and quality goals.
2. Minutes 5-10: estimate scale, capacity, and cost.
3. Minutes 10-14: define APIs and data contracts.
4. Minutes 14-22: draw the high-level architecture and critical flows.
5. Minutes 22-37: deep-dive into the two highest-risk components.
6. Minutes 37-44: cover evaluation, observability, security, privacy, and safety.
7. Minutes 44-50: analyze failures, graceful degradation, and trade-offs.
8. Minutes 50-55: explain rollout, evolution, and the next capacity threshold.

For a 45-minute round, combine estimates with requirements, limit the architecture to one request path and one background path, choose one deep dive, and reserve the final five minutes for failures and evolution. For a 60-minute round, keep five minutes of slack for interviewer follow-ups.

### 1. Clarify requirements and quality goals

Start with decisions that can change the architecture:

- Users and workflow - internal or external users, interactive or batch use, frequency, accessibility, and existing alternatives
- Core action - answer, rank, classify, generate, recommend, execute, or assist
- Scope - one narrow use case, supported modalities and languages, and explicit non-goals
- Quality - task completion, precision and recall, groundedness, citation correctness, acceptance rate, or human time saved
- Latency - time to first useful feedback, end-to-end deadline, and asynchronous completion expectations
- Reliability - availability, durability, recovery point objective, recovery time objective, and acceptable stale behavior
- Risk - data classes, destructive actions, regulated decisions, residency, retention, and required human review
- Scale - daily and peak requests, corpus size, tenants, models, jobs, regions, and expected growth
- Economics - cost ceiling per request, successful task, tenant, or business outcome

Turn vague goals into an initial contract. For example: "I will design an internal policy assistant for 20,000 employees. It answers only from documents the caller may access, returns citations, abstains when evidence is weak, reaches p95 latency below 4 seconds, and costs less than $0.04 per answer. It does not make policy decisions or modify source documents."

Do not assume that an AI component is required. State a non-model baseline such as keyword search, deterministic rules, templates, or a human workflow. This gives the later evaluation a meaningful comparison.

### 2. Estimate scale and cost

Calculate only the quantities that influence design. Keep units visible. Use ranges when inputs are uncertain, identify the dominant assumption, and state how you would measure it before committing capacity.

At minimum, estimate:

- Average and peak requests per second
- Input and output tokens per second
- Concurrent requests or jobs
- Data and index size
- Accelerator or provider capacity
- Queue growth during bursts
- Major monthly cost drivers

Do not hide behind "horizontal scaling." Scaling stateful indexes, large model weights, GPU memory, or external provider quotas has different constraints from scaling stateless API handlers.

### 3. Define APIs and data contracts

Define the product contract before naming infrastructure. Include identity, versioning, idempotency, deadlines, and errors.

A representative synchronous generation contract is:

```text
POST /v1/answers
Authorization: Bearer <identity>
Idempotency-Key: <key>

{
  "tenant_id": "...",
  "query": "...",
  "conversation_version": 7,
  "response_mode": "stream",
  "deadline_ms": 5000
}
```

The response should distinguish accepted work, partial results, safe abstention, validation failure, quota rejection, and retryable dependency failure. A stream needs an explicit terminal event so a client can distinguish completion from a broken connection.

For long-running work, prefer a job resource:

```text
POST /v1/jobs
GET /v1/jobs/{job_id}
POST /v1/jobs/{job_id}:cancel
```

Persist a client-supplied idempotency key with the resulting job or side effect. Define whether cancellation is best effort, which state transitions are legal, and how clients resume after disconnects.

Version important data independently:

- Source document, parser, chunker, embedding model, and index snapshot
- Dataset, labels, feature definitions, training code, and model artifact
- Prompt, model, tool schemas, policy, and evaluator
- Request, result, trace, approval, and audit event

### 4. Draw the high-level architecture

Draw left to right. Separate the online request path from background processing and the control plane from the data plane.

A useful generic shape is:

```text
Client
  -> API gateway and identity
  -> policy, quota, and request validation
  -> application or workflow orchestrator
  -> retrieval, model, or tool services
  -> validation and safety checks
  -> response or side effect

Sources
  -> durable ingestion queue
  -> parse, validate, enrich, and deduplicate
  -> versioned data, feature, or retrieval stores

Control plane
  -> registry, configuration, rollout, evaluation, policy, and audit
```

Annotate trust boundaries, durable state, caches, queues, retry ownership, and the path used during degradation. Narrate one normal request and one update or training flow before deep-diving.

### 5. Choose deep dives

Choose two areas that dominate quality or risk. Ask the interviewer which they prefer. Examples include:

- Retrieval quality and authorization for enterprise RAG
- Tool safety and durable execution for an agent
- Batching, KV-cache capacity, and admission control for inference serving
- Labels, leakage, feature freshness, and drift for classical ML
- Tenant isolation, quotas, and rollout for a shared platform
- Streaming latency and interruption handling for voice

For each deep dive, connect mechanism to metric. Explain alternatives, why the selected design fits, how it fails, and what evidence would change the decision.

### 6. Cover evaluation, observability, and risk

Evaluation asks whether the system does the right thing. Observability asks what the production system is doing now. They overlap but are not substitutes.

Cover four levels:

- Service health - rate, errors, latency distributions, saturation, queue age, capacity, and dependency health
- Component quality - parser success, feature freshness, retrieval recall, reranker quality, tool selection, model output validity, and safety-filter behavior
- End-to-end outcome - task success, user correction, escalation, time saved, conversion, or loss avoided
- Governance - lineage, access decisions, redaction, retention, policy violations, approvals, and audit completeness

Name the release gate, canary plan, rollback trigger, dashboard owner, and critical alert. Explain how traces remain useful without storing secrets or unrestricted personal data.

### 7. Analyze failures and trade-offs

Use concrete scenarios rather than saying the system is fault tolerant:

- A dependency slows down without failing.
- A client retries after the side effect succeeded but before the response arrived.
- A tenant creates a hot partition or exhausts a shared quota.
- New data is malformed, stale, duplicated, poisoned, or unauthorized.
- A model or prompt release changes behavior for one important slice.
- A region, index, provider, queue, or GPU pool becomes unavailable.
- A request exceeds its deadline while downstream work continues.
- Feedback creates a self-reinforcing error loop.

For each important failure, state detection, containment, user-visible behavior, recovery, and prevention. Degradation should preserve the safest useful behavior: cached or stale read-only data, a smaller model, reduced context, keyword retrieval, delayed batch completion, manual review, or explicit unavailability. Never silently bypass authorization or approval to improve availability.

### 8. Explain evolution

End with staged investment:

1. Establish a deterministic or simple model baseline and collect representative evaluation data.
2. Launch to a narrow cohort with hard budgets, complete traces, and manual review where risk is high.
3. Improve the largest measured error class instead of adding generic complexity.
4. Add capacity, tenancy, regional resilience, or self-hosting when measured demand justifies it.
5. Migrate with shadowing, dual writes or reads, canaries, compatibility checks, and rollback.

State what you deliberately deferred. A staff-level answer should also identify interface owners, adoption incentives, migration costs, and which capabilities belong in a shared platform rather than every product team.

## Back-of-the-Envelope Estimation

Interview estimates are decision tools, not forecasts. Write the formula, substitute assumptions with units, round sensibly, and run one sensitivity check.

### Requests, peak load, and concurrency

Use:

```text
average QPS = daily requests / 86,400 seconds
busy-hour QPS = requests in busiest hour / 3,600 seconds
concurrency = throughput x average time in system
```

Suppose 100,000 daily active users make 8 requests each. That is 800,000 requests per day, or 9.3 average QPS. If 15.0% arrives in the busiest hour, busy-hour load is 120,000 / 3,600 = 33.3 QPS. A burst multiplier of 3 produces about 100 QPS.

At 100 QPS and 2.5 seconds average end-to-end latency, Little's Law gives about 250 requests in flight. Provisioning only 250 concurrent slots leaves no room for variance, retries, or scaling delay. An initial limit near 350 may provide headroom, but load testing must establish where queueing causes the latency SLO to fail.

Caution: average concurrency does not predict p99. Service-time variance, long prompts, synchronized bursts, head-of-line blocking, and downstream rate limits can dominate the tail.

### Tokens and model throughput

Use:

```text
input tokens/day = requests/day x average input tokens/request
output tokens/day = requests/day x average output tokens/request
token throughput = QPS x tokens/request
```

For 800,000 requests with 2,000 input and 300 output tokens:

- Input volume is 1.6 billion tokens per day.
- Output volume is 240 million tokens per day.
- At 100 peak QPS, the system receives 200,000 input tokens per second and requests 30,000 output tokens per second.

Input and output tokens stress different phases. Long input increases prefill work and time to first token. Autoregressive output drives decode duration, KV-cache residency, and inter-token latency. Do not combine them into one throughput number when sizing self-hosted inference.

### Provider cost

Use:

```text
daily model cost =
  input_tokens/1,000,000 x input_price
  + output_tokens/1,000,000 x output_price
```

With illustrative prices of $0.50 per million input tokens and $1.50 per million output tokens, the preceding workload costs:

```text
1,600 x $0.50 + 240 x $1.50 = $1,160 per day
```

That is about $34,800 in a 30-day month before retrieval, embeddings, network, observability, storage, support, and failed requests. A 30.0% exact or semantic cache hit rate does not automatically reduce total cost by 30.0%; cacheable requests may have different lengths, misses still pay lookup cost, and unsafe cross-user cache keys can leak data.

Quote illustrative prices as assumptions, not current vendor facts. In a real design, verify current pricing, cached-token rules, batch discounts, minimum commitments, and regional charges.

Track cost per successful task:

```text
cost per successful task = total system cost / accepted successful outcomes
```

A cheaper model that causes more retries or human correction can cost more per successful outcome.

### Storage and retrieval indexes

For dense vectors:

```text
raw vector bytes = vector count x dimensions x bytes per dimension
```

Ten million 1,536-dimensional vectors stored in 16-bit form require:

```text
10,000,000 x 1,536 x 2 bytes = 30.72 GB
```

This excludes identifiers, metadata, additional copies, write-ahead logs, and approximate-nearest-neighbor index structures. A rough early total index-size factor of 1.2 to 2.0 times raw vector size may be useful, but the actual factor depends strongly on index type and parameters. With a 1.5 total index-size factor and 2 total copies, the vector portion is `30.72 GB × 1.5 × 2 = 92.16 GB`.

If each chunk averages 1 KB of text, ten million chunks add roughly 10 GB before database, compression, and replication overhead. Retain the source object separately so chunks and embeddings can be rebuilt. Estimate version overlap during re-indexing; a migration may temporarily require two complete indexes.

Caution: decimal GB and binary GiB differ. State which one you use when memory is tight. Filters, skewed tenants, deleted entries, and index rebuild behavior can matter more than raw size.

### GPU weight and KV-cache memory

The idealized weight footprint is:

```text
weight bytes = parameter count x bytes per parameter
```

An 8-billion-parameter model needs about 16 GB at 16 bits, 8 GB at 8 bits, or 4 GB at 4 bits for weights alone. Runtime memory also includes quantization metadata, temporary workspaces, allocator fragmentation, framework overhead, and possibly duplicated buffers. Training additionally needs gradients, optimizer state, activations, and communication buffers.

For a decoder model, an approximate KV-cache size is:

```text
KV bytes =
  2 x layers x KV heads x head dimension
  x bytes per element x cached tokens x concurrent sequences
```

For 32 layers, 8 KV heads, head dimension 128, and 16-bit cache entries:

```text
bytes per cached token =
2 x 32 x 8 x 128 x 2 = 131,072 bytes = 128 KiB
```

One 8,192-token sequence then uses about 1 GiB of KV cache. Sixteen such full sequences use about 16 GiB. This example reflects grouped-query attention; a model with more KV heads can use substantially more memory. Paged allocation reduces fragmentation and waste but does not remove the underlying bytes for live tokens.

Always leave memory headroom and measure the actual serving runtime. Quantized weights do not imply a quantized KV cache.

### Batching and replica count

Assume a measured replica sustains 800 output tokens per second for the target prompt distribution while meeting the inter-token latency objective. With 400 average output tokens, the theoretical output-limited capacity is 2 requests per second. At a 70.0% target utilization, budget 1.4 requests per second:

```text
replicas = ceiling(100 peak QPS / 1.4) = 72 replicas
```

This is only a first bound. Prefill may be the bottleneck, output lengths have a tail, tensor-parallel replicas consume multiple GPUs, continuous batching changes throughput, and utilization near saturation can destroy p99 latency. Benchmark the exact model, quantization, hardware, runtime, prompt distribution, and SLO.

Batching improves accelerator utilization by sharing work, but waiting to form a batch adds queueing latency. Continuous batching admits and removes sequences as they progress and usually fits mixed output lengths better than fixed batches. Isolate interactive and batch workload classes so large offline jobs cannot starve user traffic.

### Queue depth and backpressure

For a stable queue, long-run service capacity must exceed arrival rate. If 120 jobs per second arrive while workers serve 100, the queue grows by 20 jobs per second and is unstable while that rate continues.

Suppose a 10-second burst arrives at 120 jobs per second, then returns to 80 while service remains 100:

```text
burst backlog = (120 - 100) x 10 = 200 jobs
queueing delay immediately after burst = 200 jobs / 100 jobs per second = 2 seconds
net backlog drain rate = 100 - 80 = 20 jobs per second
time until backlog returns to zero = 200 / 20 = 10 seconds
```

Assuming first-in, first-out service, uniform job cost, no retries, and no service degradation, a job arriving immediately after the burst waits behind about 200 jobs. At 100 completed jobs per second, its predicted queueing delay is about 2 seconds, within the 5-second tolerance. The queue takes 10 seconds to return to zero because the continuing 80 jobs per second leave only 20 jobs per second of spare capacity. Add capacity, admission control, priority shedding, or a lower accepted burst only when the backlog, arrival burst, job-size distribution, or service degradation pushes predicted queueing delay beyond the 5-second SLO. Monitor oldest-message age as well as depth because depth alone does not reveal whether a low-volume queue is stuck.

Bound every queue and concurrency pool. Propagate deadlines. Reject or defer work before saturation causes all requests to miss their deadlines.

### SLOs and error budgets

Define an indicator, population, window, and target:

"Over a rolling 28-day window, 99.9% of accepted interactive requests from paid tenants return a valid first response event within 2 seconds, excluding client cancellations but including dependency failures."

In a 30-day month:

- 99.0% availability permits about 7.2 hours of unavailability.
- 99.9% permits about 43.2 minutes.
- Four nines of availability permits about 4.3 minutes.

If two independent serial dependencies each achieve 99.9%, their combined theoretical availability is about 99.8%, not 99.9%. Independence is often false because shared networks, regions, identity systems, or deployments create correlated failures.

Use separate objectives for availability, time to first token, completion latency, valid-output rate, and quality. Never promise a quality SLO that cannot be measured promptly enough to operate.

### A compact estimate checklist

Before leaving the estimate section, confirm:

- Are peak and average separated?
- Are tokens split into input and output?
- Are concurrency and queueing included?
- Does storage include replication, metadata, index overhead, and migration overlap?
- Does GPU memory include weights, KV cache, runtime overhead, and headroom?
- Does capacity use measured throughput at the target SLO rather than peak benchmark throughput?
- Does cost include failures and non-model services?
- Is the largest uncertainty named with a measurement plan?

## Distributed-System Foundations

AI components do not remove ordinary distributed-system requirements. They add expensive, probabilistic dependencies to them.

### Caches

Name what is cached and the correctness boundary:

- Exact response cache - key on tenant, authorization context, normalized request, model and prompt versions, retrieval snapshot, safety policy, and generation settings where relevant
- Semantic cache - retrieve similar prior requests, but require tenant isolation, similarity thresholds, freshness rules, and quality evaluation
- Retrieval cache - cache query-to-document identifiers only when permission and corpus versions are part of the key
- Prefix or KV cache - reuse common prompt prefixes within serving constraints
- Feature cache - include entity and feature timestamps to prevent training-serving skew

Define invalidation, time to live, maximum staleness, negative caching, stampede protection, and behavior after a policy or deletion event. Do not cache sensitive answers across principals merely because their queries look alike.

### Queues and workflows

Use queues for ingestion, training, evaluation, media processing, and other work that can complete asynchronously. Assume at-least-once delivery unless the infrastructure and complete side-effect path prove stronger semantics.

A reliable worker:

1. Validates the message and schema version.
2. Acquires or checks an idempotency record.
3. Performs bounded work with a deadline.
4. Commits the side effect and completion state atomically where possible.
5. Acknowledges only after durable completion.
6. Sends poison messages to a dead-letter path with replay tooling and ownership.

Use an outbox when a database state change and an emitted event must not diverge. Durable workflow state is preferable to a chain of ephemeral callbacks for multi-step agents or jobs that must survive process failure.

### Partitioning and hot keys

Partition by a key aligned with access and isolation, such as tenant, document, user, model, or job. Check:

- Cardinality and expected distribution
- Whether one tenant can dominate traffic
- Cross-partition query frequency
- Rebalancing and resharding cost
- Ordering requirements
- Data residency and deletion boundaries

Salting can spread a hot key but complicates ordered reads and aggregation. Dedicated partitions or workload pools may be safer for very large tenants.

### Consistency and state

Choose consistency per invariant:

- Strong consistency for authorization changes, quota debits, approvals, job leases, and irreversible side effects
- Eventual consistency for analytics, noncritical counters, replicated search indexes, and some model metadata
- Read-your-writes behavior for user-visible updates when delayed visibility would look like data loss

State the stale-read consequence. A stale document body may be tolerable for a low-risk summary; stale access control is not.

### Idempotency

Idempotency belongs at the side-effect boundary. A request-level key at the API gateway does not protect a downstream payment, email, or data mutation if the key is lost between services.

Store the idempotency key, operation identity, request hash, status, and result. Reject reuse with a different payload. Define retention long enough to cover client and workflow retries. For tools that cannot be made idempotent, use operation lookup, reconciliation, or a human checkpoint before repeating uncertain work.

### Rate limiting, quotas, and admission control

Use token buckets for bursts with a sustained rate, concurrency limits for scarce downstream slots, token budgets for model cost, and queue limits for asynchronous work. Apply limits by tenant, user, API key, model, workload class, and global dependency as needed.

Reject early with a clear retry policy. Reserve capacity for control-plane operations and critical tenants. A global limit without per-tenant fairness lets one user consume the service.

### Retries and backpressure

Retry only transient, idempotent operations. Use bounded attempts, exponential backoff with jitter, a total deadline, and a retry budget. Avoid independently layered retries. Three total attempts at each of three layers, meaning one initial attempt plus up to two retries per layer, can create up to `3^3 = 27` downstream attempts.

Backpressure must flow toward the producer. Bound in-flight work, pause queue consumption, reduce batch admission, shed low-priority requests, or return overload before memory and latency collapse. Circuit breakers stop repeated calls to an unhealthy dependency, but probes and recovery behavior still need design.

### Multi-region design

Start from residency, latency, and recovery requirements. Active-passive is easier to reason about for stateful systems. Active-active improves regional availability but requires conflict handling, global identity and quota strategy, data replication, and careful failover of model or index capacity.

Plan for:

- Regional routing and evacuation
- Replication lag and stale reads
- Region-scoped keys and globally unique operation identifiers
- Failover capacity rather than nominal capacity
- Model artifacts, indexes, secrets, policies, and configuration in the recovery region
- Regular failover tests and a route back to normal

Do not claim multi-region resilience when the model provider, identity plane, artifact store, or deployment pipeline remains a single global dependency.

### Data modeling

Model stable identities separately from versions. A RAG document may have `document_id`, `document_version`, `chunk_id`, `embedding_version`, source timestamps, access-control attributes, and tombstone state. A model prediction should retain model, feature, prompt, policy, and request lineage.

Design from access patterns and invariants:

- Online lookup, filtering, and authorization
- Append-only audit and event history
- Analytical aggregation and late events
- Retention, deletion, legal hold, and reprocessing
- Schema compatibility and backfills

Avoid putting large opaque blobs in the only operational table. Keep source artifacts in durable object storage and indexed metadata in stores suited to the query.

## Classic ML System Design

Classic ML questions still begin with the decision the prediction supports. A model score without an action, threshold, or user outcome is incomplete.

### Data, labels, and features

Define the prediction unit, observation time, label window, and action time. This prevents future information from leaking into training. Specify label source, delay, ambiguity, class imbalance, and who resolves disagreements.

For features:

- Define ownership, type, entity key, event timestamp, availability timestamp, freshness, and default behavior.
- Use point-in-time-correct joins for training.
- Reuse transformations or validate parity between offline and online paths.
- Monitor missingness, distribution, freshness, and serving errors by important slice.
- Treat sensitive attributes and proxies according to product, policy, and legal constraints.

Start with a simple rule or model. It exposes whether data and labels support the task before a complex training stack hides the problem.

### Training pipeline

A reproducible flow is:

```text
versioned source snapshot
  -> validation and point-in-time feature generation
  -> train, validation, and test split
  -> training and tuning
  -> offline evaluation by slice
  -> artifact, lineage, and approval
  -> registry
```

Use time-based or group-based splits when random splitting would leak entities or future behavior. Persist code, configuration, data references, random seeds where meaningful, environment, metrics, and artifact checksum. Retries must not register duplicate or partially written models.

### Offline and online evaluation

Choose metrics from error costs:

- Classification - precision, recall, PR-AUC, calibration, and threshold-specific cost
- Ranking - recall at k, mean reciprocal rank, normalized discounted cumulative gain, and downstream action
- Forecasting - absolute or squared error by horizon and segment
- Recommendations - ranking quality, diversity, novelty, coverage, and user outcomes

Report confidence intervals and slices, not only averages. Offline improvement does not establish causal product value. Use shadow traffic, canaries, or controlled experiments with guardrails before broad release.

### Registry and deployment

The registry stores immutable artifacts, lineage, evaluation evidence, status, and approvals. A deployment references an artifact digest rather than an ambiguous name such as "latest."

Choose batch, streaming, or online inference from the decision deadline. Deployment strategies include shadow, canary, champion-challenger, and blue-green. Define rollback for both model and feature changes. A model rollback may fail if its required feature schema was already removed.

### Drift and feedback loops

Monitor:

- Input distribution and missingness
- Prediction distribution and confidence
- Feature and label freshness
- Performance after delayed labels arrive
- Calibration and errors by segment
- Changes in the policy or population caused by model actions

Drift is a signal to investigate, not an automatic command to retrain. Retraining on model-influenced labels can amplify bias or suppress alternatives. Preserve exploration where appropriate, audit selection effects, and compare against a stable holdout or policy.

## LLM and RAG Design

RAG has two coupled systems: an asynchronous knowledge pipeline and an online answer pipeline. Evaluate them separately before attributing every error to the model.

### Ingestion and parsing

The ingestion flow should:

1. Authenticate the source connector and record tenant and source identity.
2. Receive change events or poll with a durable cursor.
3. Store the immutable source version before transformation.
4. Validate type, size, malware status, and supported encoding.
5. Parse structure, text, tables, images, and metadata.
6. Deduplicate by stable source identity and content hash.
7. Resolve access-control metadata from the source of truth.
8. Chunk, embed, and write a versioned index.
9. Atomically publish the new searchable version.
10. Process updates and deletions through the same lineage.

Parsing quality is often the retrieval bottleneck. Preserve headings, page numbers, table relationships, code boundaries, and source offsets so citations can be verified. Quarantine failures instead of indexing partial garbage silently.

### Chunking

Chunk according to document structure and retrieval unit, not one universal token count. A useful baseline might target 300-800 tokens with modest overlap, but evaluation should choose the actual values.

Use:

- Heading-aware chunks for policies and manuals
- Parent-child retrieval for long sections
- Table-aware representations that preserve headers and rows
- Function or class boundaries for code
- Page and region references for scanned documents
- Separate image descriptions and original media references for multimodal retrieval

Overlap improves boundary recall but increases index size and duplicated context. Store parent relationships so adjacent context can be expanded after retrieval rather than duplicated everywhere.

### Embeddings and indexes

Version the embedding model and normalization behavior. Compare lexical, dense, and hybrid baselines. Approximate indexes trade recall for latency and memory; filtering strategy affects both.

Plan for:

- Incremental updates and tombstones
- Full re-embedding without downtime
- Old and new index coexistence
- Tenant or regional partitions
- Filter selectivity and authorization
- Recall measurement against exact search on a sample
- Backfill rate, checkpointing, and cost

Never mix vectors from incompatible embedding spaces in one logical search without an explicit method.

### Hybrid retrieval and reranking

Lexical retrieval handles exact names, identifiers, rare terms, and quoted phrases. Dense retrieval handles semantic paraphrases. Hybrid retrieval combines candidates, then a reranker can improve ordering at additional latency and cost.

A practical pipeline is:

```text
query normalization and optional rewrite
  -> authorized lexical and dense candidate retrieval
  -> rank fusion
  -> rerank top candidates
  -> diversity and freshness checks
  -> context assembly
```

Apply access control during candidate retrieval or before any content leaves the trusted retrieval boundary. Post-generation filtering cannot undo leakage into the model or logs.

### Context assembly and generation

Allocate a token budget among instructions, conversation, retrieved evidence, tool results, and output reserve. Prefer the smallest evidence set that covers the answer. Record which chunks were selected, excluded, truncated, or compressed.

Treat retrieved content as untrusted data. Delimit it, prohibit it from changing system policy, and keep credentials and tool authority outside the prompt. Ask the model to cite stable source identifiers, then verify that each citation maps to supplied evidence and supports the associated claim.

Use schema-constrained output for machine consumers, followed by deterministic validation. Define abstention when evidence is absent, conflicting, stale, unauthorized, or below a calibrated threshold.

### Evaluation

Build a representative set with answerable, unanswerable, adversarial, permission-sensitive, stale, multilingual, and long-tail cases.

Measure stages:

- Ingestion - parse coverage, structural fidelity, freshness lag, and deletion completion
- Retrieval - recall at k, precision at k, mean reciprocal rank, and latency by slice
- Reranking - ordering lift over the candidate baseline
- Context - evidence coverage, redundancy, token use, and lost-critical-context rate
- Generation - correctness, groundedness, completeness, citation precision and recall, abstention, safety, latency, and cost
- Product - successful task completion, correction, escalation, repeat use, and time saved

Calibrate model-based graders against blinded human judgments. Keep deterministic checks for citation identity, schema, policy, and known facts. Diagnose bad answers by stage before changing the prompt.

### Freshness, deletion, and access control

Define a freshness SLO from source change to searchable version. Use source cursors, versioned documents, publish markers, and reconciliation scans to detect missed events.

Deletion includes source copies, chunks, vectors, caches, replicas, derived datasets, and logs according to retention policy. Tombstone quickly to block reads, then complete physical deletion asynchronously with auditable status.

Copying source access-control lists at ingestion can become stale. Prefer stable principals and groups with current authorization checks where latency permits, or propagate changes under a strict freshness objective. Include authorization context in caches and traces without exposing unnecessary membership data.

## Agentic Systems

Use an agent only when the path cannot be fully specified and model-selected actions create enough value to justify the additional risk. A deterministic workflow with one constrained model step is often easier to evaluate and operate.

### Orchestrator and tools

Keep control in an orchestrator:

- Explicit workflow state and legal transitions
- Step, token, time, and cost budgets
- Tool allowlists by user, tenant, task, and environment
- Typed tool schemas and deterministic argument validation
- Deadlines, retry ownership, and idempotency keys
- Checkpoints, cancellation, and resumability
- Approval gates for sensitive or irreversible actions
- Terminal success, partial, failed, cancelled, and expired states

Treat tools as production APIs. The model proposes a call; code authenticates, authorizes, validates, executes, and records it. Tool output is untrusted input and cannot grant itself more authority.

### State and memory

Separate:

- Working state - current plan, observations, tool results, and pending steps
- Durable workflow state - authoritative status needed for restart and audit
- User preferences - explicit, editable, scoped, and retained by policy
- Retrieved history - selected on relevance, trust, and permissions
- Summaries - lossy derived data with lineage to originals

Do not give the model an unbounded transcript and call it memory. Define write criteria, conflict handling, expiration, deletion, and whether a memory is factual, inferred, or user-approved.

### Permission boundaries and approval

Bind authority to the authenticated user and specific operation. Use short-lived scoped credentials, never broad platform secrets in model context. Distinguish read, draft, simulate, and execute permissions.

Require human approval for actions based on impact, confidence, reversibility, and policy. Show the proposed action, target, important inputs, expected effect, and evidence. Revalidate authorization and mutable preconditions after approval because the world may have changed.

### Termination, retries, and compensation

Stop on:

- Explicit completion validated against task criteria
- Maximum steps, tokens, cost, or wall time
- Repeated state or tool-call cycle
- No progress across a bounded number of steps
- Policy violation or missing authority
- User cancellation or expired approval

Retry reads more freely than writes, but still within deadlines. If a write's outcome is unknown, query operation status before repeating. Use compensating actions only when they are semantically valid; deleting a sent message may not undo that it was read.

### Sandboxing

For generated code or untrusted files:

- Use an ephemeral isolated runtime with no ambient credentials.
- Restrict network egress and filesystem mounts.
- Apply CPU, memory, process, storage, and time limits.
- Scan inputs and outputs.
- Broker required secrets to a narrowly scoped operation rather than exposing them to the runtime.
- Destroy the environment and preserve only policy-approved artifacts and audit data.

### Trace and evaluation

Record a structured trajectory: versions, state transitions, model decisions, tool proposals, validation outcomes, approvals, tool results, retries, costs, and termination reason. Redact or tokenize sensitive fields.

Evaluate:

- Task completion and correctness
- Tool selection and argument accuracy
- Policy and permission compliance
- Step efficiency, latency, and cost
- Recovery from tool errors and ambiguous outcomes
- Approval quality and unnecessary escalation
- Loop, abandonment, and unsafe-action rates

Final-answer quality alone can hide unsafe or wasteful trajectories.

## Multimodal and Real-Time Systems

Multimodal systems need modality-specific preprocessing, storage, evaluation, and safety. Preserve the original media and temporal or spatial references so outputs can be traced back.

### Images, documents, audio, and video

Consider:

- File validation, malware scanning, decompression limits, and unsupported formats
- Optical character recognition, layout, frames, timestamps, speakers, and language detection
- Separate raw, normalized, and derived artifacts with versioned transforms
- Embeddings that share or bridge modality spaces
- Large-object storage and signed, short-lived access
- Copyright, biometric, personal, and sensitive-content handling
- Evaluation by modality, quality level, language, lighting, noise, and device

Sampling video frames reduces cost but can miss brief events. Audio transcription loses prosody and overlapping speech. Image descriptions can omit details needed by later reasoning. Keep the original available to a capable model when policy and cost permit.

### Voice and streaming

Break latency into:

```text
capture
  -> endpointing or voice activity detection
  -> streaming speech recognition
  -> orchestration and retrieval
  -> model time to first token
  -> streaming speech synthesis
  -> network playback buffer
```

For a natural conversation, target first useful audio in roughly 500-1,000 ms when the product permits, but state this as a product assumption and measure it. Accuracy, geography, network conditions, and model choice may require a different target.

Handle:

- Partial transcripts and later corrections
- Barge-in, cancellation, and stopping in-flight synthesis
- Turn detection under pauses and background noise
- Domain vocabulary, accents, code-switching, and speaker separation
- Duplicate audio packets and reconnects
- User-visible confirmation before consequential actions
- A text or keypad fallback when speech quality is poor

Do not execute an irreversible tool call from an unstable partial transcript. Confirm the critical fields and intent.

## AI Platform and Inference Serving

A shared platform succeeds when application teams can use it safely without every team rebuilding policy, routing, evaluation, and operations. The abstraction must still expose enough control to debug quality and cost.

### Model gateway

The gateway provides a stable contract across hosted and self-hosted models:

- Authentication, authorization, tenant quotas, and budgets
- Provider-neutral request and response schema with explicit capability discovery
- Model aliases resolved to approved immutable versions
- Routing by task, policy, region, quality, latency, availability, and cost
- Streaming, cancellation, timeouts, and normalized errors
- Redaction, safety policy, audit, and usage attribution
- Exact caching where correctness permits
- Fallbacks that preserve data policy and quality floors

Avoid a lowest-common-denominator API that hides every provider capability. Use a stable core plus versioned capability-specific extensions. Do not automatically retry a partially streamed response unless the application can handle duplicate or divergent text.

### Routing

Begin with policy rules and measured model scorecards. Route simple, low-risk tasks to smaller models only after evaluation establishes a quality floor. Consider:

- Task and modality support
- Tenant allowlist and data residency
- Context length and structured-output support
- Quality by important slice
- Current latency, error rate, quota, and cost
- Fallback compatibility

Dynamic routing is itself a model or policy that needs evaluation, observability, versioning, and rollback.

### Batching and KV cache

Separate prefill and decode metrics. Use continuous batching, paged KV allocation, and length-aware admission where supported. Prefix caching helps common trusted prefixes but needs version-aware keys and memory policy.

Protect latency with:

- Workload classes for interactive, background, and batch
- Maximum prompt and output tokens
- Per-tenant concurrency and token limits
- Queue deadlines and load shedding
- Chunked prefill or separate prefill capacity where justified
- Memory-aware scheduling based on projected KV growth

A request admitted by weight memory alone can still cause an out-of-memory failure as its KV cache grows.

### Autoscaling and GPU scheduling

CPU-style utilization is not enough. Scale on queue age, pending tokens, active sequences, KV-cache pressure, time to first token, and observed throughput. Account for model download and warmup time. Keep warm capacity for strict latency SLOs.

GPU scheduling must understand:

- Accelerator type, memory, topology, and interconnect
- Tensor or pipeline parallel group placement
- Model weights and runtime compatibility
- Fractional sharing versus isolation
- Gang scheduling for distributed jobs
- Priorities, preemption, checkpoint readiness, and fairness
- Fragmentation and bin-packing trade-offs

Preemption is safe only if the workload can checkpoint and resume within the recovery objective. Interactive serving generally needs stronger isolation from opportunistic training or evaluation jobs.

### Multi-tenancy

Enforce tenancy in identity, policy, data, cache keys, queues, metrics, and cost attribution. Use per-tenant budgets and fair scheduling plus a global circuit breaker. High-cardinality telemetry must remain queryable and affordable.

Noisy-neighbor controls include concurrency limits, weighted fair queues, dedicated pools for large tenants, memory reservations, and independent failure domains. Measure fairness as delivered service relative to entitlement, not equal request counts when requests have different token costs.

### Model lifecycle

The lifecycle is:

```text
artifact registration
  -> security and compatibility checks
  -> quality and performance evaluation
  -> capacity approval
  -> shadow or canary deployment
  -> promotion
  -> monitoring
  -> rollback or retirement
```

Pin tokenizer, runtime, quantization, adapters, and serving configuration with the artifact. Warm the model and run smoke tests before receiving production traffic. Retirement needs dependency discovery, migration communication, and a rollback window.

## Security, Privacy, Safety, and Degradation

Treat these as design inputs in every section rather than a final checklist.

### Threat model

Identify assets, actors, entry points, trust boundaries, and impact. Common threats include:

- Direct and indirect prompt injection
- Cross-tenant retrieval or cache leakage
- Secret or personal-data exposure in prompts, traces, tools, and vendors
- Unauthorized tool use and confused-deputy behavior
- Malicious files, parser exploits, and decompression bombs
- Model supply-chain compromise and unsafe artifacts
- Training-data poisoning and feedback manipulation
- Resource abuse, denial of wallet, and accelerator exhaustion
- Unsafe generated code, links, SQL, or commands

Layer controls. No prompt instruction provides a security boundary.

### Privacy and governance

Classify and minimize data before sending it to any model. Define purpose, consent where required, region, encryption, retention, deletion, access logging, and vendor training or storage behavior. Redact before logging, but remember that naive redaction can miss context-specific secrets.

Keep auditable lineage for data, models, prompts, tools, policies, and approvals. Separate production access from broad development access. Use synthetic or de-identified evaluation data when it preserves the relevant behavior, and protect unavoidable sensitive test sets.

### Safety

Match controls to impact. Low-risk drafting may need user review and content policy. Medical, financial, legal, employment, or physical actions need stricter scope, calibrated abstention, authoritative sources, human oversight, and clear accountability.

Measure both false negatives and false positives. An aggressive filter can make a system unusable or create unequal failure rates. Red-team realistic end-to-end paths, not only isolated prompts.

### Graceful degradation ladder

Define a safe order before incidents:

1. Disable optional enrichment, reranking, or personalization.
2. Reduce context, output length, or expensive model use within an evaluated quality floor.
3. Serve a compatible smaller model or provider that satisfies policy and residency.
4. Use lexical retrieval, cached read-only results, or stale data within explicit freshness limits.
5. Queue noninteractive work and expose status.
6. Require manual review or provide a draft without execution.
7. Abstain or reject when authorization, evidence, or safety cannot be preserved.

Never degrade by removing access control, audit, approval, or required validation.

## Synthesized Practice Prompts

The prompts in this section are synthesized for practice. They are not attributed to any company.

1. Design a multi-tenant enterprise RAG assistant over documents, tickets, chat, and wikis. It must honor source permissions, cite evidence, process deletions, and provide fresh results within 15 minutes.
2. Design an AI coding copilot that supports repository chat, code completion, and proposed patches for 50,000 developers while preventing cross-repository leakage.
3. Design an agent workflow that investigates support cases, reads customer records, drafts a resolution, and may issue a refund only after appropriate approval.
4. Design a model gateway that gives 200 internal teams one API across several hosted and self-hosted models with quotas, policy enforcement, routing, and chargeback.
5. Design a multi-tenant inference platform for interactive and batch LLM workloads with strict time-to-first-token and cost targets.
6. Design a GPU job scheduler for training, fine-tuning, evaluation, and notebooks across heterogeneous accelerator clusters with priorities, preemption, and fairness.
7. Design an evaluation platform for prompts, RAG pipelines, agents, and model releases. It must support human labels, deterministic checks, model graders, regression gates, and experiment lineage.
8. Design a customer data integration platform that connects to customer databases, file stores, SaaS APIs, and event streams while handling schema drift, identity mapping, residency, and deletion.
9. Design a real-time hospital voice assistant that transcribes noisy conversations, retrieves approved guidance, drafts notes, and requires confirmation before modifying records.
10. Design a multimodal claims-processing system for forms, photos, scanned documents, and call audio with explainable triage and human escalation.
11. Design a classic ML fraud-decision system with delayed labels, real-time features, thresholding, feedback loops, and regulator-ready audit.
12. Design a recommendation system that combines behavioral events and content embeddings, supports cold start, and remains robust to popularity feedback loops.
13. Design a fresh web research assistant with crawling, hybrid retrieval, citations, source quality controls, and a strict latency budget.
14. Design a model and prompt release system that can shadow, evaluate, canary, roll back, and explain slice-specific regressions across hundreds of applications.

Apply the market-weighted prompt order above rather than treating list position as priority. Start with prompt 1 for enterprise RAG, prompt 3 for agents, prompt 7 for evaluation, prompt 4 for model gateway and integration, then revisit each through production reliability and security. Treat prompts 11 and 12 as classic-ML-loop practice, and prompts 5 and 6 as Platform or job-description-specific practice. Rotate every prompt to expose weak domains rather than memorizing fixed architectures.

## Anchor Walkthrough 1: Enterprise RAG Assistant

### Requirements and quality goals

Scope the first release to question answering over four enterprise sources for 20,000 employees. Assume 800,000 requests per day, 10 million chunks, 100 peak QPS, 15-minute indexing freshness, p95 completion below 4 seconds, and a $0.04 average answer-cost ceiling. Every answer must cite accessible sources or abstain. Source systems remain authoritative for content and permissions.

The highest-risk requirements are permission correctness, citation support, deletion, and source freshness. A useful baseline is existing enterprise keyword search. Measure answer correctness, citation support, abstention, task completion, p95 latency, and cost against that baseline.

### Architecture

Connectors write source change events to a durable ingestion queue. Workers store immutable source versions, parse and chunk them, resolve source identity and access metadata, generate embeddings, and write lexical and vector indexes. A publish marker makes a complete version searchable. Reconciliation jobs compare connector cursors and source inventories to detect missed updates and deletions.

The online path authenticates the employee, resolves groups and tenant policy, rewrites the query only when evaluation supports it, and runs authorized lexical and dense retrieval. Rank fusion and a reranker select evidence. A context assembler enforces token and source-diversity budgets. The model generates an answer with source identifiers; a validator checks that identifiers exist in the supplied context and that cited spans support the associated claims. Low evidence produces an explicit abstention with search suggestions.

### Deep dive: permissions and freshness

Authorization cannot be a prompt instruction. Candidate retrieval uses tenant and access filters derived from the caller's current identity. If the search engine cannot efficiently filter highly variable group lists, use tenant partitions plus a permission service to filter candidate identifiers before content fetch. Cache keys include principal or a stable authorization fingerprint and corpus version.

Permission revocation needs a tighter objective than ordinary content freshness. A revocation event can immediately invalidate authorization-cache entries and block affected documents while asynchronous re-indexing catches up. Deletion first writes a read-blocking tombstone, then removes chunks, vectors, cached answers, and retained derived data under an auditable workflow.

### Deep dive: retrieval and evaluation

Establish lexical and dense baselines before adding hybrid fusion and reranking. Label relevant documents for representative queries, including exact identifiers, paraphrases, permission boundaries, stale documents, and unanswerable requests. Optimize retrieval recall at a candidate depth that the reranker can afford. Evaluate answer quality separately so a fluent model does not hide retrieval misses.

At 10 million 1,536-dimensional 16-bit vectors, raw vector storage is about 30.72 GB. Index overhead, replicas, and migration overlap raise the actual requirement. A full embedding upgrade should build a shadow index, replay incremental changes to both versions, compare recall and answer quality, canary query traffic, and retain the old index for rollback.

### Trade-offs and failure modes

Hybrid retrieval costs more than a single retriever but handles both exact terms and semantic matches. A cross-encoder reranker can improve relevance while adding tail latency. More chunks improve recall but consume context and increase conflicting evidence. Fresh source checks on every request improve correctness but can exceed the latency budget.

If dense search fails, degrade to authorized lexical search. If the reranker fails, use fused retrieval order. If the model fails after evidence is available, return source results rather than an invented answer. If identity or authorization is unavailable, fail closed. Monitor freshness lag, unauthorized-result tests, retrieval recall, citation validity, abstention, index skew, queue age, and cost per accepted answer.

### Strong follow-ups

- How does the design handle one tenant with 50.0% of all documents and traffic?
- How do tables, images, and code change parsing and chunking?
- How do you prove a deleted document no longer appears in caches, indexes, traces, or evaluation sets?
- What happens when source permissions change during an active conversation?
- When would long-context generation replace retrieval, and how would you evaluate that decision?

## Anchor Walkthrough 2: AI Coding Copilot

### Requirements and quality goals

Design repository chat and patch suggestions for 50,000 developers. Completion may be a later workload class because it has a much tighter latency requirement. Assume source code never crosses repository authorization boundaries, proposed changes require developer review, and execution occurs only in isolated sandboxes.

Quality is not "looks plausible." Measure task completion on repository-specific exercises, accepted patch rate with caution, compile and test success, security findings, edit distance after acceptance, latency, and cost. Acceptance alone is biased by developer behavior and does not prove correctness.

### Architecture

An installation service receives repository events, stores immutable commit references, parses code into symbol-aware units, builds lexical and embedding indexes, and maintains a symbol and dependency graph. The online service authenticates the developer and installation, resolves repository and commit scope, retrieves code and documentation, and asks a code-capable model for either an answer or a structured patch.

Patch output passes syntax and policy validation. An ephemeral sandbox checks out the exact base commit, applies the patch, and runs bounded static checks and tests with restricted network and no ambient credentials. The UI shows the diff, citations to relevant code, test results, and uncertainty. Only the developer can apply or submit the change.

### Deep dive: context construction

Repository chat needs query-dependent context: exact symbol matches, references, callers, tests, configuration, ownership, and nearby documentation. Retrieve small symbol units, then expand to parents or neighbors. Include commit identifiers in every context item to prevent mixing versions. Reserve tokens for the developer's current file and selection when those are part of the task.

Completion and chat should not share one undifferentiated path. Completion needs local context, prefix and suffix handling, aggressive cancellation, and perhaps a smaller local or regional model. Chat can tolerate retrieval and longer reasoning. Separate SLOs, queues, caches, and model routes.

### Deep dive: security and sandboxing

Repository contents and issues can contain prompt injection. Treat them as data, not authority. Tools are allowlisted by task. The sandbox blocks unrestricted egress, secrets, privileged mounts, fork bombs, and excessive resource use. Dependency installation should use controlled mirrors and lockfiles where possible.

Cross-repository caches are prohibited unless content is explicitly public and keyed accordingly. Logs retain identifiers and metrics but redact code by default. Customer-controlled retention and regional processing may constrain model providers.

### Trade-offs and failure modes

Symbol graphs improve code navigation but are language-specific and can become stale. Embeddings help conceptual queries but can miss exact APIs; lexical and structural retrieval remain necessary. Running full tests increases confidence but may be too slow, so run changed-area checks first and offer a queued comprehensive result.

If indexing lags, pin chat to the latest indexed commit and disclose it. If the sandbox is unavailable, return an unverified draft marked as such rather than claiming tests passed. If context is insufficient, ask for scope or abstain. If a generated patch modifies security policy, dependencies, CI, or ownership files, require stronger review.

### Strong follow-ups

- How would you reach sub-200 ms perceived latency for inline completion?
- How do monorepos, generated code, submodules, and very large histories change indexing?
- How do you evaluate novel tasks without leaking benchmark solutions into prompts?
- Should the copilot be allowed to open pull requests, and what approval model would you use?
- How do you investigate a quality regression isolated to one programming language?

## Anchor Walkthrough 3: Support Resolution Agent

### Requirements and quality goals

The agent reads a support case, customer profile, order history, and policy; it may draft a response, propose a refund, and execute only within policy after approval. Begin with one product line and refunds below a fixed limit. The system must not invent policy, expose unrelated customer data, or issue duplicate refunds.

Measure resolved-case rate, correct policy application, tool and argument accuracy, unnecessary approval rate, human handle time, duplicate or unauthorized action rate, latency, and cost. The safety target for unauthorized financial actions should be zero in testing and production monitoring, while acknowledging that measured evidence has confidence limits.

### Architecture

A durable workflow service owns the case state. The model receives a bounded case summary and proposes the next action from typed tools. A policy engine independently authorizes each proposal against user role, refund limit, order state, geography, and current policy. Read tools use scoped customer identity. Write tools require idempotency keys and, where policy demands, a human approval record.

The workflow checkpoints after every validated observation or action. A human console shows evidence, proposed action, amount, recipient, policy basis, and editable response. Execution rechecks authorization and order state after approval. Audit events record proposal, validation, approval, tool result, and model and policy versions.

### Deep dive: uncertain outcomes and retries

Suppose the payment tool succeeds but the response is lost. The orchestrator records an operation identifier before the call. On timeout, it queries refund status using that identifier rather than issuing another refund. If status remains unknown, the case enters reconciliation instead of retrying a non-idempotent write.

Read failures can use bounded retries with jitter. Write retries require idempotent provider semantics or explicit operation lookup. The workflow deadline is distinct from individual call deadlines, and only one layer owns retries.

### Deep dive: control, termination, and memory

The model cannot alter step, cost, or permission budgets. Detect repeated state and repeated tool arguments. Stop on completion, budget exhaustion, policy denial, user cancellation, or no progress. A deterministic state machine handles the known refund flow; model autonomy is limited to interpreting the case, selecting evidence, and drafting.

Durable case facts remain separate from inferred working notes. User preferences are explicit and editable. Summaries carry source references and do not overwrite authoritative records.

### Trade-offs and failure modes

A fully autonomous loop may handle more cases but is harder to guarantee and evaluate. A deterministic workflow with model-assisted fields is safer for the initial scope. Human approval lowers action risk but can erase time savings, so calibrate approval thresholds using observed error and impact.

If the model or policy service fails, route the case to the existing human workflow with gathered evidence. If a read tool returns stale data, the final execution precondition catches changed order state. If prompt injection appears in customer text or tool output, it cannot expand the tool allowlist or credentials. Quarantine cases that repeatedly violate policy rather than spending unbounded tokens.

### Strong follow-ups

- How do you add a second action such as account cancellation without creating a permission tangle?
- How do you test recovery from failure after every workflow transition?
- What does a useful trajectory evaluation dataset contain?
- How do you prevent agents from learning from manipulated customer feedback?
- When can approval be removed, and what evidence is sufficient?

## Anchor Walkthrough 4: Multi-Provider Model Gateway

### Requirements and quality goals

Assume 200 internal teams, 800,000 daily requests, 100 peak QPS, several hosted providers, and two self-hosted models. The gateway must provide identity, quotas, policy, routing, usage attribution, normalized telemetry, and streaming. Applications retain ownership of task prompts and task-level evaluation.

Set separate SLOs for gateway overhead, accepted-request availability, time to first response event, and usage-record completeness. The gateway should add no more than an assumed 20 ms p95 excluding model work, but verify whether redaction or policy checks make that realistic.

### Architecture

Clients call a versioned core API with tenant, task class, model alias, deadline, and capability requirements. The gateway authenticates the workload identity, checks policy and token budgets, estimates request size, and resolves the alias through a routing policy. Provider adapters normalize request, stream, cancellation, usage, and error semantics.

A control plane manages model catalog, aliases, routing rules, provider credentials, tenant policy, quotas, prices, and rollout. An append-only usage pipeline supports chargeback and reconciliation. A separate evaluation service publishes task and slice scorecards that routing policy can consume.

### Deep dive: routing and fallback

Routing first applies hard constraints: data region, tenant allowlist, modality, context length, and required schema support. It then chooses among eligible models using measured quality floor, current health, latency, quota, and cost. Keep the initial policy deterministic and versioned.

Fallback is not "try any model." The fallback must satisfy the same data and capability policy and an evaluated quality floor. Do not switch after partial streaming unless the application explicitly supports a restart marker and divergent output. Cap total attempts under the caller's deadline and retry budget.

### Deep dive: quotas and accounting

Use per-team request, token, concurrency, and monetary budgets plus global provider limits. Reserve capacity for critical workloads and protect providers with circuit breakers. Estimate tokens before admission, then reconcile against actual usage.

Usage records include tenant, application, task, model version, provider, input and output tokens, cached tokens, latency, status, and policy version. Keep sensitive prompt content out of the billing event. A durable local record protects accounting when the analytics pipeline is unavailable.

### Trade-offs and failure modes

A normalized API reduces migration work but can hide provider-specific features. Offer a small stable core and explicit versioned extensions. Central redaction improves consistency but may damage task quality and cannot replace application-side minimization. Dynamic cost routing can create quality regressions that aggregate metrics miss.

If a provider reaches quota, stop admitting traffic that cannot meet the deadline rather than queueing indefinitely. If the control plane fails, data-plane instances use the last known valid signed configuration. If usage export fails, requests may continue only while durable local buffers remain within bounds. If every compliant model is unavailable, fail clearly instead of violating residency.

### Strong follow-ups

- How do you migrate a team that relies on a provider-specific tool-call schema?
- How do you prevent a routing policy from oscillating during partial outages?
- What belongs in the gateway versus application code?
- How do you canary a new model alias across heterogeneous tasks?
- How do you attribute cost when one agent request creates many model calls?

## Anchor Walkthrough 5: Multi-Tenant Inference Platform

### Requirements and quality goals

Support interactive chat, background extraction, and batch evaluation for several 8-billion to 70-billion-parameter models. Assume interactive peak demand of 100 QPS with 2,000 input and 400 output tokens on average. Target p95 time to first token below 1 second for the chosen interactive tier, while batch work has completion deadlines measured in hours.

The design must provide isolation, high accelerator utilization, model rollout, capacity planning, and chargeback. Quality parity across runtime, quantization, and model revisions is part of the release gate.

### Architecture

The control plane stores model artifacts, runtime profiles, deployment specifications, quotas, and rollout state. A scheduler places model replicas on topology-compatible GPU groups. Regional routers choose a healthy deployment by model, tenant, workload class, queue state, and policy.

Each serving replica exposes prefill and decode metrics, uses continuous batching and paged KV allocation, and enforces sequence and token limits. Separate weighted queues protect interactive work from batch traffic. An admission controller considers pending tokens, projected KV memory, deadline, and tenant entitlement before assigning a request.

### Deep dive: capacity and memory

Use measured per-replica throughput for the target prompt distribution. If a replica sustains 800 output tokens per second at the latency objective, 400 output tokens imply 2 theoretical requests per second. At 70.0% planned utilization, 100 QPS requires about 72 replicas before failover reserve. Prefill measurements may produce a stricter bound.

For the earlier 8-billion-parameter grouped-query example, 16-bit weights require about 16 GB and each 8,192-token sequence can require about 1 GiB of 16-bit KV cache. Actual runtime overhead and parallelism determine the GPU shape. Admission must reserve projected KV growth rather than only current use.

### Deep dive: scheduling and scaling

Scale on queue age, pending input and output tokens, KV pressure, time to first token, and recent per-replica throughput. Warmup can take minutes when artifacts are large, so strict tiers need warm reserve. Place tensor-parallel groups within fast interconnect domains and avoid fragmentation that leaves unusable isolated GPUs.

Use workload classes and weighted fair scheduling. Batch jobs consume spare capacity but yield to interactive reserve at safe boundaries. A preempted model replica is not instantly replaceable; draining active streams and loading another artifact have user-visible cost.

### Trade-offs and failure modes

Larger batches improve throughput but hurt queueing and inter-token latency. Quantization saves memory and can improve throughput but needs task-level quality and numerical validation. Prefix caching saves prefill work but consumes memory and risks incorrect reuse if keys omit model, prompt, adapter, or tenant boundaries.

On overload, reject low-priority requests early, cap output, or queue batch work. Do not let queues grow past deadlines. On GPU failure, reroute only if remaining capacity can absorb traffic; otherwise shed according to priority. On a bad model rollout, stop promotion, drain the canary, and restore the previous artifact and runtime configuration.

### Strong follow-ups

- Would you disaggregate prefill and decode, and what network cost would that introduce?
- How do mixture-of-experts or adapter-based models change placement?
- How do you provide failover when a region cannot keep every model warm?
- When does self-hosting beat provider APIs after staffing and utilization are included?
- How do you load-test long-tail prompts without exposing production content?

## Anchor Walkthrough 6: GPU Job Scheduler

### Requirements and quality goals

Design a scheduler for training, fine-tuning, evaluations, and notebooks across heterogeneous GPU clusters. Assume 10,000 submitted jobs per day, 2,000 GPUs across several types, jobs from one GPU-hour to hundreds of GPU-days, and organizational priorities. Distributed jobs need gang scheduling. Some jobs can checkpoint and preempt; notebooks are interactive but quota-bound.

Measure scheduling latency by class, GPU utilization, useful work rather than allocated time, fairness relative to entitlement, preemption waste, checkpoint recovery time, queue age, job success, and cost attribution. Durability of job state and reproducibility matter more than maximizing instantaneous utilization.

### Architecture

The API validates a versioned job specification containing image digest, command, resources, accelerator constraints, topology, priority class, checkpoint contract, data references, and identity. Durable job state is the source of truth. Admission applies quotas, budget, policy, and image checks before entering a tenant-aware queue.

A scheduler separates feasibility from prioritization. It filters nodes by accelerator, memory, topology, locality, and runtime constraints, then ranks feasible placements by priority, fairness, fragmentation, and data cost. A cluster agent acquires leases and launches the job. Heartbeats, checkpoint events, and completion reports update the state machine. A reconciler repairs divergence between desired and observed state.

### Deep dive: fairness and fragmentation

Dominant-resource fairness or weighted fair share can account for teams requesting different GPU types and counts. Entitlements, borrowed idle capacity, and maximum burst should be explicit. Aging prevents low-priority starvation, but production incidents may still justify an override with audit.

Packing small jobs raises utilization but can strand topology needed by an eight-GPU job. Reservations or backfilling can hold a future gang slot while allowing short jobs that will finish before it. Runtime estimates are uncertain, so penalize repeated underestimation and use historical distributions rather than trusting users blindly.

### Deep dive: preemption and recovery

Only mark a job preemptible if it has a tested checkpoint contract. The scheduler sends notice, allows a bounded checkpoint window, verifies durable checkpoint completion, then revokes the lease. Measure lost work from the last checkpoint and restore time. Frequent checkpointing reduces lost compute but adds storage and training overhead.

Distributed worker failure can restart the whole gang from a consistent checkpoint unless the framework supports elastic recovery. Operation identifiers and leases prevent two attempts from writing the same checkpoint path or registering duplicate models.

### Trade-offs and failure modes

Strict priority improves urgent-job latency but can starve research work and waste progress through preemption. Pure packing improves utilization but harms queue time for large gangs. Data-local placement reduces network cost but may worsen accelerator fragmentation.

If the scheduler leader fails, durable state and leases allow another instance to reconcile without duplicate ownership. If a node disappears, expire its leases and recover from checkpoint. If the artifact or dataset is unavailable, fail before reserving scarce GPUs. If queue estimates become inaccurate, show ranges rather than false precision and alert on oldest-job age.

### Strong follow-ups

- How do you schedule across regions with data residency and expensive checkpoint transfer?
- How do elastic jobs bid for a range of GPU counts?
- How do you keep notebooks from occupying idle GPUs indefinitely?
- How do you handle hardware health, slow GPUs, and stragglers?
- What interfaces let teams migrate from an existing scheduler safely?

## Outline Hints for the Remaining Prompts

### Evaluation platform

Define an evaluation specification that pins dataset, system under test, prompts, models, tools, graders, sampling, metrics, and pass thresholds. Run deterministic checks first, expensive model graders second, and calibrated human review on targeted samples. Store immutable result lineage and slice-level comparisons. Treat grader changes like model changes and backtest them against human labels.

The central trade-off is standardization versus task ownership. The platform should provide execution, lineage, comparison, and governance while product teams define meaningful tasks and failure costs. A release gate must include uncertainty, critical-slice regressions, safety, latency, and cost rather than one average score.

### Customer data integration

Begin with source ownership, identity mapping, residency, freshness, deletion, and support boundaries. Use connector-specific adapters behind a common versioned change-event contract. Store durable cursors, raw immutable source versions, schema observations, and normalized records. Quarantine malformed data and provide replay and reconciliation.

Schema drift is not always an error: additive fields, renamed identifiers, semantic changes, and changed permissions need different responses. Keep tenant isolation through storage, queues, keys, telemetry, and operator access. Define who owns failures when customer APIs, credentials, or source data are wrong.

### Real-time voice assistant

Set a latency budget per stage and stream partial results, but do not execute from unstable transcripts. Keep approved medical or operational guidance in an authorized retrieval layer, cite it in the clinician UI, and make note updates reviewable. Test accents, noise, interruptions, overlapping speakers, domain terms, and network loss. Degrade to transcript-only or manual entry when confidence or connectivity is poor.

### Classic fraud ML system

Define the transaction decision, loss asymmetry, review capacity, and label delay. Use point-in-time online features, a calibrated score, explicit thresholds, and a manual-review band. Protect against feedback loops because blocked transactions do not reveal the outcome they would have had. Monitor feature freshness, score distribution, delayed performance, calibration, fraud loss, false declines, and segment disparities.

## Common Weak Answers and Corrections

- "Use a vector database" - define corpus, chunking, embedding version, retrieval metric, filters, index freshness, deletion, and migration.
- "Add retries" - identify retryable errors, idempotency boundary, owner, deadline, budget, jitter, and uncertain side effects.
- "Autoscale GPUs" - quantify warmup, model placement, throughput at the SLO, KV memory, queue signal, reserve, and shedding.
- "Use an LLM judge" - define rubric, calibration against humans, bias, disagreement handling, versioning, and release decision.
- "Encrypt the data" - include classification, minimization, authorization, tenancy, retention, deletion, vendor use, and audit.
- "Add an agent" - justify autonomy, bound tools and budgets, define durable state, approval, termination, and trajectory evaluation.
- "Make it multi-region" - name authoritative state, replication, failover capacity, residency, conflict policy, and recovery tests.
- "Exactly once" - explain the actual transactional boundary and how downstream side effects handle duplicate or unknown outcomes.
- "Cache responses" - define key, tenant and permission boundary, versions, invalidation, staleness, and leakage tests.
- "We need five GPUs" - show model memory, KV cache, measured throughput, parallelism, utilization target, and failover reserve.

## Senior and Staff Scoring Rubric

Use the canonical scale and readiness rules in [mock interviews and scorecards](09-mock-interviews-and-scorecards.md). Score each dimension from 1 to 4 using observed behavior in a timed mock:

- 1 - Weak or unsafe; behavior is missing, incorrect, or requires direct rescue.
- 2 - Partial; produces a workable baseline but has important gaps or needs targeted prompting.
- 3 - Interview-ready; independently makes explicit, quantified, production-ready decisions and handles expected follow-ups.
- 4 - Strong senior or staff evidence; does everything at level 3 and handles second-order effects, organizational boundaries, migration, or novel follow-ups.

### Dimensions

1. Requirements and scope
   - A score of 3 defines users, workflow, non-goals, quality, latency, reliability, risk, and a baseline within five minutes.
   - A score of 4 prioritizes conflicting stakeholders and identifies which unknown would change the investment.
2. Estimation and economics
   - A score of 3 calculates peak QPS, tokens or work units, concurrency, storage or memory, capacity, and cost with units and a sensitivity check.
   - A score of 4 links capacity to SLOs, failure reserve, migration overlap, and cost per successful outcome.
3. APIs, data, and architecture
   - A score of 3 defines versioned contracts, identity, state, online and asynchronous flows, and ownership boundaries.
   - A score of 4 creates durable interfaces that support multiple teams without erasing necessary control.
4. AI or ML quality
   - A score of 3 decomposes the pipeline, defines stage and end-to-end evaluation, slices, release gates, and feedback.
   - A score of 4 reasons about evaluator validity, selection effects, migration evidence, and how product outcomes revise the roadmap.
5. Reliability and distributed systems
   - A score of 3 handles idempotency, retries, backpressure, partitioning, consistency, overload, rollback, and regional failure.
   - A score of 4 identifies correlated failures, operational ownership, and a credible migration or disaster-recovery exercise.
6. Security, privacy, and safety
   - A score of 3 identifies trust boundaries and enforces least privilege, tenant isolation, data lifecycle, safe tool use, and audit.
   - A score of 4 prioritizes risks by impact, resolves policy-product tension, and designs verification rather than making absolute claims.
7. Observability and operations
   - A score of 3 defines actionable service, component, quality, and business telemetry with alerts, runbooks, and trace lineage.
   - A score of 4 explains ownership, incident containment, privacy-aware diagnosis, and system learning after failure.
8. Communication, trade-offs, and evolution
   - A score of 3 drives the conversation, narrates flows, compares credible alternatives, and ends with staged rollout.
   - A score of 4 revises assumptions cleanly, manages interviewer follow-ups, sequences cross-team adoption, and states what not to build.

The maximum is 32.

- 8-15 - Foundation gap. Study the missing domains and repeat untimed before more mocks.
- 16-22 - Developing. The design works in parts but is not yet consistently senior.
- 23-27 - Interview-ready evidence is emerging. Run harder prompts and target dimensions below 3.
- 28-30 - Strong senior performance. Add staff-level organizational, platform, and migration follow-ups if relevant.
- 31-32 - Exceptional mock performance. Confirm it repeats across unfamiliar prompts and interviewers.

A total or score band describes one mock and never establishes readiness. A score of 1 in security, quality, reliability, or requirements is a failed mock for a production AI role. All eight dimensions are required. For a staff target, additionally require at least three dimensions scored 4 with evidence of interfaces, migration, multi-team leverage, or technical direction.

## Readiness Gate

The [readiness rules in module 09](09-mock-interviews-and-scorecards.md#readiness-rules) are canonical. Treat system design as interview-ready only when all of the following are true:

- [ ] My three most recent relevant full mocks use different prompts and cover three families: one RAG or agent product, one classic ML or multimodal system, and one serving or platform system.
- [ ] At least two mocks were scored by different interviewers, or one was independently double-scored before the debrief.
- [ ] Every required scorecard dimension scored at least 3 in at least two of the three mocks.
- [ ] No required dimension scored 1 in either of the two most recent mocks, and no hard fail remains unresolved.
- [ ] I finished the core scope within the 45-60 minute limit in at least two mocks.
- [ ] I handled at least one material follow-up without direct rescue in each of the two most recent mocks.
- [ ] Every known or repeated failure completed a successful re-test with a fresh prompt.
- [ ] For a staff target, at least two mocks also contain three or more scores of 4 supported by the staff evidence defined in the rubric.
- [ ] Produce peak-QPS, token, concurrency, storage, GPU-memory or model-capacity, queue, cost, and SLO estimates without notes in 10 minutes.
- [ ] Explain one normal flow, one update flow, and one failure flow without losing the main architecture.
- [ ] Diagnose a bad RAG answer by stage and an agent side-effect timeout by idempotency state.
- [ ] Define graceful degradation that never bypasses authorization, approval, validation, or audit.
- [ ] Answer at least two strong follow-ups for each of the six anchor prompts.
- [ ] Name a simple first release, a measurable launch gate, rollback criteria, and the next evidence-driven evolution.

Record each mock's prompt, date, assumptions, dimension scores, concrete misses, and repeated drill. A mock counts only when run under time constraints without reading this guide. Repeat the failed section within one week, then repeat the full prompt later with changed scale or policy constraints.

## Final Interview Checklist

Before concluding an answer, verify:

- Did I define what success and safe failure mean?
- Did I state assumptions and calculate the quantities that drive the design?
- Did I define contracts, identity, state, and versioning?
- Did I separate online, asynchronous, and control-plane flows?
- Did I choose deep dives based on quality or risk?
- Did I define offline and online evaluation with important slices?
- Did I include observability, SLOs, security, privacy, and safety?
- Did I handle retries, idempotency, backpressure, overload, and dependency failure?
- Did I provide a degradation path and rollback?
- Did I explain trade-offs, staged evolution, and what evidence changes the design?

Return to [`01-common-core.md`](01-common-core.md) for weak foundations. Use [`04-product-ai-engineer.md`](04-product-ai-engineer.md) for product and evaluation depth, [`05-forward-deployed-engineer.md`](05-forward-deployed-engineer.md) for customer integration and deployment constraints, and [`06-ml-ai-platform-engineer.md`](06-ml-ai-platform-engineer.md) for serving, scheduling, and platform depth. Use the [AI system design question bank](../questions/04-ai-system-design.md) to vary prompts after the anchor designs become familiar.
