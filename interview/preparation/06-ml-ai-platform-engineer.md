# Senior ML/AI Platform Engineer Interview Preparation

This module prepares senior and staff candidates to design, build, migrate, and operate shared ML and AI infrastructure. It is the platform track within the [eight-week curriculum](README.md). Pair it with the [common core](01-common-core.md), the reusable method in [AI/ML system design](03-ai-ml-system-design.md), and the [AI system design question bank](../questions/04-ai-system-design.md).

The central interview signal is leverage. A strong candidate does not merely know how to deploy a model. They define a reliable platform contract that lets many internal teams ship safely, while preserving escape hatches for workloads that genuinely need them.

Use this module across all eight weeks:

- Weeks 1-2 - build shared coding, distributed-systems, ML, and estimation foundations.
- Weeks 3-4 - study serving, scheduling, lifecycle, security, and platform interfaces.
- Weeks 5-6 - complete the two-week platform rotation in this module.
- Weeks 7-8 - run mocks, defend project evidence, and close readiness gaps.

Actual titles vary. Confirm whether the target team owns inference, training, data, evaluation, developer tooling, GPU infrastructure, or some subset before allocating preparation time.

## Role Scope and Boundaries

An ML/AI Platform Engineer builds capabilities used by application engineers, ML engineers, data scientists, and researchers. The work combines distributed systems, infrastructure, ML workload knowledge, developer experience, security, reliability, and economics.

Typical responsibilities include:

- Define stable APIs, deployment specifications, job contracts, and operational ownership.
- Operate shared inference, training, evaluation, data, or model-lifecycle systems.
- Allocate scarce accelerator capacity across tenants and workload classes.
- Build paved roads for common cases without preventing justified specialization.
- Enforce isolation, access control, privacy, quotas, and auditability.
- Set SLOs, capacity plans, incident practices, and disaster-recovery objectives.
- Reduce cost per useful workload while preserving quality and reliability.
- Migrate teams from fragmented systems with measurable adoption and safe rollback.
- Turn recurring team needs into reusable capabilities, standards, and self-service workflows.

### Market evidence and preparation priority

Platform is a proxy mapping, not a direct measurement of jobs titled ML/AI Platform Engineer. The repository's skill-cluster analysis identifies a cloud/ML platform archetype at 21.3%; within that cluster, `AWS`, `GCP`, and `Azure` appear at 94.0%, 89.0%, and 87.0% respectively. The adjacent DevOps/infra cluster has `Docker` at 76.0%, `Kubernetes` at 74.0%, and `CI/CD` at 74.0%. The archetype share uses all 4,894 published postings; the within-cluster rates use their named clusters. See the [trends summary](../../job-market/trends.md) and [methodology and cluster signatures](../../job-market/trends-appendix.md). The dedicated inference/serving stack is comparatively niche and declined from 11.4% to 6.4% within the ai-first subset only. The broader [skills](../../role/02-skills.md) and [responsibility](../../role/03-responsibilities.md) analyses provide context, but none of these sources defines a title-specific interview loop.

Use this market-informed default:

- P0 - Cloud, `Kubernetes`, `Docker`, `CI/CD`, reliability, and monitoring. Practice platform contracts, deployment, overload, SLOs, rollback, and operations across realistic cloud boundaries.
- P1 - Model gateways, MLOps and model lifecycle, multi-tenancy, security, and cost. Show reusable interfaces, policy, migration, and ownership.
- P2 - Evaluation platforms, data systems, and `SQL`. Connect them to release decisions, lineage, observability, and internal developer workflows.
- P3 - GPU kernels and deep inference optimization. Study them deeply only when the job description or recruiter confirms that the loop tests dedicated inference, CUDA, compiler, or accelerator work.

Override this default whenever the job description or recruiter confirms a different ownership boundary or interview loop.

### Contrast with Product AI Engineering

- Product AI Engineer
  - Primary customer - an external user or a product team delivering a user workflow.
  - Main outcome - product quality, adoption, task success, and business value.
  - Typical unit of change - a feature, workflow, prompt, retrieval strategy, or application service.
  - Common question - what should the user experience do when the model is uncertain or wrong?
- ML/AI Platform Engineer
  - Primary customer - internal application, ML, data, and research teams.
  - Main outcome - safe and efficient delivery across many workloads.
  - Typical unit of change - an API, runtime, scheduler, control plane, policy, or migration.
  - Common question - what contract lets teams obtain predictable behavior without operating the underlying complexity?

Platform engineers still need product judgment. Internal developers are users, adoption is not automatic, and a technically elegant platform that teams bypass has failed.

### Contrast with Forward Deployed Engineering

- Forward Deployed Engineer - adapts systems to a named customer's workflow, environment, security constraints, and delivery timeline.
- ML/AI Platform Engineer - creates reusable capabilities and governance for many internal teams or tenants.

An FDE may expose platform gaps through field deployments. A platform engineer should separate a one-off constraint from a repeated need, then design an interface that avoids encoding one customer's architecture into every workload.

### Contrast with Traditional MLOps

Traditional MLOps commonly emphasizes reproducible training pipelines, experiment tracking, feature pipelines, registries, deployment automation, and monitoring for predictive models. Modern ML/AI platform work may include all of that, plus:

- Generative-model gateways and provider routing
- Token streaming, continuous batching, and KV-cache management
- Large accelerator fleets and heterogeneous hardware
- Prompt, tool, retrieval, and evaluation versioning
- Per-token or per-request provider economics
- Model-behavior evaluation that cannot rely on one scalar metric
- Safety, privacy, and policy controls around open-ended inputs and outputs

The distinction is not that MLOps is obsolete. The interview should reveal which workload families the platform must support and where established MLOps controls still apply.

### Contrast with Research and Model Training Roles

- Research or model-training role - improves model architecture, optimization, data mixtures, training algorithms, or benchmark performance.
- Platform role - provides the compute, orchestration, serving, lifecycle, observability, and governance that make research and production workloads repeatable.

A platform engineer should understand training and inference mechanics deeply enough to design infrastructure, diagnose bottlenecks, and challenge impossible requirements. They are not necessarily expected to invent optimizers, kernels, or model architectures. Ask whether the target role includes CUDA, compiler, collective-communication, or distributed-training implementation before studying those as primary interview topics.

## Interview Signals

### Platform strategy

You can identify the repeated constraint worth centralizing, define the platform's customer and boundary, sequence investment, and state what should remain team-owned. You compare the platform against a library, template, managed service, or documentation rather than assuming every repeated task requires a service.

### Internal customer judgment

You conduct discovery with application, ML, research, security, finance, and operations teams. You measure time to first successful deployment, deployment frequency, reliability, support load, adoption, and satisfaction instead of treating cluster utilization as the only outcome.

### Paved roads and flexibility

You make the common path safe and easy through defaults, templates, validation, and self-service. You provide explicit extension points and a reviewed escape hatch. You do not offer unlimited configuration that destroys operability or force every workload into one runtime.

### Reliability and operability

You define user-visible SLIs, SLOs, error budgets, ownership, overload behavior, rollback, incident response, and recovery. You reason about control-plane and data-plane failures separately.

### Security and privacy

You preserve tenant identity through queues and downstream calls, isolate compute and data, minimize secrets exposure, constrain logs, enforce policy, and produce useful audit records. You distinguish authentication, authorization, network isolation, runtime isolation, and data governance.

### Cost and capacity

You estimate memory, throughput, concurrency, queue growth, accelerator demand, and provider spend. You state uncertainty, measure the dominant variables, allocate costs to tenants, and connect quotas to product priorities.

### Migration and adoption

You inventory workloads, segment by compatibility and risk, offer dual-run or shadow validation, publish deprecation stages, support rollback, and measure migration outcomes. You account for organizational incentives and ownership, not only data movement.

### Organizational leverage

You improve outcomes beyond your own service by setting standards, simplifying interfaces, enabling teams, resolving cross-team trade-offs, and reducing repeated operational work.

## Senior and Staff Expectations

At senior level, demonstrate independent ownership of an ambiguous platform problem through requirements, implementation, rollout, operations, and measured improvement.

Strong senior evidence includes:

- A clear internal-customer problem and baseline
- A defensible API or contract, not only infrastructure components
- Capacity estimates and bottleneck analysis
- Failure isolation, overload behavior, rollback, and on-call ownership
- Security and cost designed in from the start
- A migration plan that a real team could execute
- Metrics showing adoption or improved delivery, reliability, utilization, or cost

At staff level, demonstrate direction and leverage across teams and time horizons.

Strong staff evidence includes:

- A platform strategy tied to organization priorities and explicit non-goals
- A decision about build, buy, standardize, federate, or retire
- Interfaces that allow independent team evolution
- Multi-quarter sequencing under uncertain demand
- Capacity allocation and governance across competing priorities
- Alignment among engineering, research, product, security, and finance
- Migration, deprecation, and ownership changes across organizational boundaries
- Development of other engineers and improved decision quality

Weak staff answers describe a larger cluster or a harder personal implementation without showing broader leverage.

## Concepts Versus Vendor Details

Interviewers may ask about tools used by their team, but portable concepts should drive the answer.

### Concepts candidates must know

- Request and job contracts, versioning, idempotency, deadlines, cancellation, and error semantics
- Control plane versus data plane
- Replication, partitioning, consistency, queues, leases, retries, and backpressure
- Containers, scheduling, resource requests and limits, health checks, rollout, and service discovery
- Model memory, KV-cache growth, batching, latency, throughput, and accelerator utilization
- Work-conserving scheduling, fairness, priority, preemption, checkpointing, and gang scheduling
- Multi-tenancy, identity propagation, isolation boundaries, quotas, and auditability
- Model and prompt lifecycle, evaluation gates, canaries, rollback, and lineage
- SLOs, saturation signals, traces, cost attribution, incident response, and disaster recovery

### Vendor-specific details to learn only when relevant

- Exact custom-resource fields, command names, or console workflows
- A cloud's instance names, quota APIs, and autoscaler implementation
- A serving framework's configuration syntax
- A scheduler plugin's extension points
- A registry or experiment tracker's object model
- A gateway vendor's routing DSL

Know one implementation well enough to give concrete examples. Then translate it into portable primitives. If an interviewer asks about an unfamiliar product, state the concepts you would inspect: scheduling model, failure semantics, consistency, extension points, observability, isolation, and operational burden.

## A Platform Design Method

Use this sequence for a 45-60 minute design:

1. Identify internal customers, workloads, and the decision the design must enable.
2. Separate functional requirements, SLOs, risk constraints, and non-goals.
3. Estimate traffic, tokens, jobs, model memory, concurrency, storage, and cost.
4. Define the customer-facing API and ownership contract.
5. Separate control-plane state from latency-sensitive or compute-heavy data paths.
6. Draw the critical synchronous flow and one asynchronous lifecycle flow.
7. Deep-dive into the scarce resource or dominant failure mode.
8. Define isolation, secrets, privacy, policy, and audit behavior.
9. Define SLOs, overload behavior, rollback, and disaster recovery.
10. Sequence launch, migration, adoption, and later capacity thresholds.

State assumptions before calculations. A plausible estimate with units is more useful than a precise number based on hidden inputs.

## Foundations and Deep Preparation

### Model gateway and routing

A gateway gives applications a stable contract across hosted providers and self-hosted models. It can centralize authentication, policy, quotas, routing, retries, streaming normalization, telemetry, and cost attribution.

Know:

- Route by capability, policy, data residency, measured quality, latency, availability, and price.
- Use deadlines and retry budgets. Blind retries can duplicate cost and worsen overload.
- Retry only when semantics allow it; do not switch models if behavior changes would violate the application contract.
- Bound fallback chains and record which route served the request.
- Keep gateway availability independent from a nonessential analytics pipeline.
- Avoid logging prompts or outputs by default when they may contain sensitive data.

The gateway should not hide every provider difference. Expose portable core fields and capability discovery, then use versioned extensions for features that cannot be normalized safely.

### API contracts

A platform contract should define:

- Caller and tenant identity
- Model or capability selector
- Input and output schema
- Prompt or deployment version
- Deadline and cancellation behavior
- Idempotency semantics
- Streaming events and terminal status
- Quota and policy errors
- Retryable versus permanent failures
- Usage and route metadata
- Compatibility and deprecation policy

For asynchronous jobs, expose a resource with submit, inspect, cancel, logs, artifacts, and events. Acknowledging submission is not the same as guaranteeing execution.

### Inference serving

Separate:

- Control plane - model catalog, deployment intent, policy, rollout state, capacity targets, and placement.
- Data plane - request admission, batching, model execution, streaming, and response delivery.

Understand cold starts, model loading, weight sharing, replicas, tensor or pipeline parallelism, health checks, warm pools, and graceful draining. Avoid claiming that every model can be replicated on one GPU or that adding replicas always improves throughput.

### Dynamic and continuous batching

Static batching forms a fixed group before execution. Dynamic batching forms a batch at dispatch time from requests already waiting, often using a short delay, shape constraints, and a maximum request or token budget. Continuous batching goes further for autoregressive generation: the scheduler can admit and retire sequences between decode iterations instead of keeping the original batch together until every sequence finishes.

A production scheduler should:

1. Admit only requests whose context length, deadline, tenant quota, and estimated KV-cache demand fit current limits.
2. Budget tokens, not only request count. Bound prefill tokens scheduled in one iteration and active decode tokens so one large prompt cannot consume the entire cycle.
3. Treat prefill and decode as different workloads. Prefill processes many prompt tokens and is compute-heavy; decode usually advances each active sequence by one token and is often memory-bandwidth-heavy.
4. Use chunked prefill, separate queues or lanes, and deadline-aware scheduling when long prefills would block decode and damage inter-token latency.
5. Retire completed or cancelled sequences promptly, reclaim their cache blocks, and admit replacements without waiting for the longest output.

Batch size creates a latency-throughput trade-off. Waiting longer and batching more work can improve accelerator efficiency, but increases queueing and time to first token. Padding variable-length prompts to one shape wastes compute; length buckets, token-based batches, and paged runtimes reduce that waste. Long prompts, long outputs, and strict priority traffic can still cause head-of-line blocking.

Fairness must be explicit. Per-tenant concurrency or token shares, weighted fair or deficit scheduling, priority classes, and aging can prevent one tenant or long-context workload from monopolizing service. Priority should not mean starvation, and fairness may deliberately sacrifice some aggregate throughput.

Observe queue age, admission and rejection counts, scheduled prefill and decode tokens, batch occupancy, padding ratio, KV-cache occupancy, scheduler delay, time to first token, inter-token latency, completion latency, cancellation, and service share by tenant or class. Report prefill and decode throughput separately; aggregate tokens per second can hide stalled streams or unfairness.

Static batching is often enough for offline jobs, homogeneous fixed-shape requests, predictable low concurrency, or a simple service whose SLO has room for a bounded batching window. Dynamic or continuous batching earns its complexity when arrival times and sequence lengths vary enough that padding, idle slots, and head-of-line blocking materially hurt the target workload.

### KV cache

Transformer decoding stores attention keys and values for prior tokens. A simplified estimate for a conventional full multi-head attention model is:

`KV bytes = concurrent sequences × tokens per sequence × layers × 2 × KV heads × head dimension × bytes per element`

The factor 2 represents keys and values. Grouped-query or multi-query attention uses fewer KV heads than query heads. Runtime paging, block metadata, fragmentation, prefix sharing, speculative decoding, quantized caches, and parallelism change actual capacity. Confirm the model configuration and serving runtime before committing.

### Quantization

Quantization reduces weight and sometimes activation or KV-cache precision. It can reduce memory bandwidth and increase deployable batch size, but quality and speed gains are workload- and hardware-dependent.

Know the distinction among:

- Weight-only versus weight-and-activation quantization
- Post-training quantization versus quantization-aware training
- Integer and low-precision floating-point formats
- Model weight memory versus runtime activation and KV-cache memory

Do not assume that halving nominal bit width halves end-to-end latency or total GPU memory.

### Choosing tensor, pipeline, and data parallelism

Start with the workload and topology, not a universal rule. Before adding devices, estimate weights, training state or inference KV cache, activations, workspaces, and headroom at acceptable precision. Quantization or state sharding may change whether intra-model parallelism is needed at all.

- Tensor parallelism shards operations within each layer. It can make one model replica fit and often preserves lower latency than a deep pipeline, but introduces frequent collectives. It works best inside a high-bandwidth, low-latency fabric; crossing a slow interconnect can erase compute gains.
- Pipeline parallelism assigns different layer ranges to stages. It can fit a model across devices or nodes with mostly point-to-point activation transfers, but stage imbalance and pipeline bubbles waste capacity. Training needs enough microbatches to amortize bubbles. Interactive inference with small batches or low concurrency may expose stage latency and leave stages idle.
- Data parallelism replicates the model or model-parallel group. For inference, replicas scale independent request concurrency and provide routing and failure isolation without gradient synchronization, but replicate weights and caches. For training, workers process different samples and synchronize gradients, so communication grows with model size; a worker or link failure may still fail the whole job unless the stack supports elastic recovery.

Use this decision sequence:

1. Define whether the objective is training throughput, offline inference throughput, or interactive latency, then record batch size, concurrency, sequence-length distribution, and failure target.
2. Check whether one accelerator fits the required state with safety headroom. If it does, benchmark one device before adding communication.
3. If it does not fit, choose the smallest tensor- or pipeline-parallel group that fits. Favor tensor parallelism where fast collectives are local and latency matters; consider pipeline parallelism when layer partitioning matches available memory and enough microbatches or concurrent sequences can fill the stages.
4. Once one replica or training group fits, add data-parallel replicas or workers to meet aggregate throughput. Place replica groups across fault domains only when the network and recovery model support it.
5. Benchmark candidate combinations on the real topology and traffic mix. Tensor plus pipeline plus data parallelism may be appropriate at scale, and the best choice can change between prefill, decode, training, and different batch regimes.

Treat a tensor- or pipeline-parallel group as one failure unit for serving: losing a member usually loses that replica. Extra data-parallel replicas can improve serving availability, while spreading a tightly coupled group across weak links or fault domains may reduce both performance and reliability.

### GPU memory and throughput

Approximate weight memory as:

`weight bytes = parameter count × bits per parameter / 8`

Then add runtime overhead:

- KV cache
- Activations and temporary workspaces
- Runtime and kernel allocations
- Communication buffers
- Fragmentation and safety headroom

For training, add gradients, optimizer states, master weights where used, activations, and communication buffers. Data type, optimizer, sharding stage, activation checkpointing, sequence length, microbatch size, and parallelism dominate the result.

Throughput must name its unit: requests per second, sequences per second, input tokens per second, output tokens per second, examples per second, or training tokens per second. Report latency distributions alongside throughput.

### Activation memory bounds

State assumptions before calculating. The following framework assumes a transformer-like model with `L_local` layers resident on one device, microbatch size `B`, sequence length `S`, hidden width `H`, and `e` bytes per activation element. Let `r` be the number of hidden-state-sized tensor equivalents retained per token per layer for backward, and let `c` be the retained fraction after activation checkpointing, where `0 < c ≤ 1`.

A cautious first estimate for retained training activations per device is:

`training activation bytes ≈ L_local × B × S × H × e × r × c`

Do not guess one universal value for `r`. Derive it from the architecture and implementation by listing tensors retained for attention, MLP, normalization, residual paths, and backward. Use a range when those details are unknown. Activation checkpointing lowers `c` by retaining selected boundaries and recomputing intermediate tensors, trading memory for additional compute. Sequence parallelism, tensor parallelism, pipeline stage placement, and the number of in-flight microbatches change the per-device value.

The linear estimate is not always an upper bound. If the implementation materializes attention scores or probabilities, add a term proportional to `B × attention heads × S² × e` for each simultaneously retained layer. Memory-efficient attention kernels can avoid retaining that full matrix. Also add transient kernel workspaces, communication buffers, allocator fragmentation, and the peak overlap between forward, backward, and collective operations.

Keep training activations separate from inference KV cache:

- Training retains forward intermediates needed by backward, so memory usually scales with microbatch size, sequence length, retained tensors, and checkpointing policy.
- Inference has no backward pass. Prefill and decode still need transient activations and workspaces, but persistent per-sequence growth is usually the KV cache, estimated from layers, cached tokens, KV heads, head dimension, and element size rather than `r`.
- Model weights, gradients, optimizer states, master weights, activations, and KV cache are separate budget lines. Include only the lines that exist for the target training or serving mode.

Build lower, expected, and stress scenarios from explicit sequence lengths, microbatches, precision, checkpointing, and concurrent requests. The arithmetic is for rejecting impossible topologies and selecting candidates. Framework memory snapshots and peak profiling on the actual model, kernels, parallel layout, and hardware are authoritative because graph fusion, recomputation, allocator behavior, and runtime workspaces determine the real peak.

### Autoscaling

CPU-based autoscaling is often a poor proxy for accelerator serving. Candidate signals include:

- Queue depth and oldest-request age
- Admitted and waiting tokens
- Time to first token and inter-token latency
- GPU memory and compute utilization
- Batch occupancy
- Requests or tokens per replica
- Provider quota headroom

Scale on a leading indicator, retain SLO guardrails, and account for model-load time. Warm capacity or predictive scaling may be justified when cold starts exceed the latency budget.

### Queues and backpressure

Every finite-capacity service needs admission control. Define:

- Queue bounds by workload class or tenant
- Per-request deadline and maximum queue age
- Fairness and priority policy
- Rejection or degradation behavior
- Cancellation propagation
- Retry hints and idempotency
- Load shedding before dependencies collapse

An unbounded queue converts overload into hidden latency and eventual failure.

### GPU scheduling, preemption, and checkpointing

Training and batch inference schedulers match jobs to heterogeneous resources while balancing utilization, fairness, and completion time.

Know:

- Resource requests - accelerator type and count, CPU, memory, local storage, topology, and network needs
- Gang scheduling - allocate all workers for a distributed job together
- Bin packing versus spreading
- Queue priority, fair share, quotas, reservations, and borrowing
- Preemption cost and victim selection
- Checkpoint interval, write bandwidth, consistency, and resume compatibility
- Stragglers, failed workers, elastic versus fixed-size jobs
- Accelerator health, fragmentation, and topology-aware placement

Preemption without a usable checkpoint can destroy more work than it frees. A checkpoint is not complete until it is durable, discoverable, version-compatible, and tested by restore.

### Kubernetes concepts

Know these concepts even if the target platform uses another orchestrator:

- Declarative desired state and reconciliation
- Pod or task lifecycle
- Resource requests, limits, and scheduling
- Labels, selectors, affinity, anti-affinity, taints, and tolerations
- Services, discovery, ingress, and network policy
- Config and secret injection
- Readiness, liveness, startup, and graceful termination
- Deployments, stateful workloads, jobs, and custom controllers
- Horizontal and cluster autoscaling
- Persistent storage and failure domains
- Role-based access control and service identities

Do not spend interview time reciting object names unless they explain a design choice.

### Multi-tenancy and isolation

Isolation has multiple layers:

- Identity - authenticate workloads and preserve tenant context.
- Authorization - enforce who can invoke, deploy, inspect, or administer.
- Compute - prevent resource starvation and unauthorized co-residency where required.
- Network - restrict service-to-service and external paths.
- Data - separate artifacts, logs, caches, features, prompts, and evaluation results.
- Cryptographic - use appropriate keys and rotation boundaries.
- Operational - scope dashboards, alerts, support access, and incident blast radius.
- Economic - attribute usage and enforce budgets or quotas.

Namespace separation alone is not a complete security boundary. Define the threat model and choose process, container, node, cluster, account, or region isolation accordingly.

### Model registry and lifecycle

A registry should connect model identity to immutable artifacts, provenance, evaluation evidence, approvals, deployment state, and lineage. A mutable label such as `production` may point to an immutable version, but the artifact itself should not change.

A safe lifecycle can include:

1. Register artifact and metadata.
2. Validate format, signature, dependencies, and lineage.
3. Run offline evaluation and security checks.
4. Deploy to a shadow or isolated environment.
5. Canary by tenant, request class, or percentage.
6. Compare quality and operational guardrails.
7. Promote progressively.
8. Roll back traffic and preserve evidence if a guardrail fails.
9. Deprecate and eventually delete under retention policy.

Rollback must include compatible prompt, tokenizer, feature, schema, and runtime versions where applicable.

### Feature and data pipelines

Feature stores and training pipelines matter when workloads use structured predictive models, fine-tuning, or shared online features. Understand:

- Point-in-time correctness and leakage
- Offline and online consistency
- Event time, processing time, lateness, and backfills
- Schema evolution and data contracts
- Freshness, completeness, lineage, and ownership
- Reproducible datasets and training runs

Do not insert a feature store into a generative-model gateway unless a real shared feature problem exists.

### Observability and SLOs

Start with user-visible SLIs:

- Successful request or job completion rate
- Time to first token, end-to-end latency, or job queue-to-completion time
- Streaming interruption rate
- Freshness or deployment propagation delay
- Evaluation-platform completion and result durability

Add diagnostic signals:

- Queue age, batch occupancy, cache use, accelerator utilization, memory pressure, throttling, retries, route distribution, cold starts, and checkpoint failures
- Per-model, per-version, per-tenant, and per-region breakdowns with cardinality controls
- Traces that connect gateway, queue, runtime, provider, and policy decisions

Model-quality metrics need their own evaluation loop. Infrastructure availability cannot prove that outputs are useful.

### Evaluation platform

A shared evaluation platform should support:

- Versioned datasets and slices
- Model, prompt, retrieval, tool, and application configurations
- Deterministic and model-based graders
- Human review and adjudication
- Repeated runs with seeds and sampling metadata where supported
- Confidence intervals or uncertainty when comparing noisy results
- Cost, latency, and safety measurements
- Regression thresholds and release evidence
- Access control for sensitive examples
- Reproducible artifacts and lineage

Treat model-based graders as measured components, not ground truth. Validate them against human judgments for the target task and monitor drift.

### Prompt and version management

Store prompts as versioned, reviewable artifacts with:

- Template and variable schema
- Model and decoding compatibility
- Owner and change reason
- Evaluation evidence
- Rollout state
- Effective configuration hash
- Rollback target

Prompt versions alone are insufficient when retrieval, tools, policy, or model routing changes behavior. Track the complete execution configuration.

### Secrets, privacy, and policy

- Use workload identity and short-lived credentials when possible.
- Keep provider keys out of application code, images, prompts, logs, and client responses.
- Enforce tenant and purpose restrictions at the gateway and artifact layers.
- Minimize prompt and output retention; make redaction and deletion behavior explicit.
- Separate operational metadata from sensitive content.
- Encrypt in transit and at rest, with key boundaries matching the threat model.
- Audit administrative actions and access to sensitive traces.
- Treat model outputs, retrieved text, artifacts, and user input as untrusted.

### Cost allocation and quotas

Attribute cost by tenant, team, model, workload, environment, and priority where possible. Include:

- Hosted-provider token or request charges
- Reserved and on-demand accelerator time
- Idle warm capacity
- Storage, network transfer, observability, and control-plane cost
- Failed, retried, shadow, and evaluation traffic

Quotas can be hard limits, soft alerts, rate limits, concurrency limits, token budgets, or queue shares. Preserve emergency and critical-production capacity. A quota policy is an organizational priority encoded in software, so make ownership and exceptions explicit.

### Disaster recovery

Define recovery point objective and recovery time objective separately for:

- Control-plane metadata
- Immutable model and prompt artifacts
- Deployment desired state
- Evaluation datasets and results
- Online feature or cache state
- In-flight requests and queued jobs

Many inference requests can be retried or failed safely, while registry lineage and deployment state need durable recovery. Test restore, regional failover, credential recovery, and dependency loss. Multi-region deployment is not automatically disaster recovery if both regions depend on the same control plane, provider account, or corrupted state.

## Calculation Drills

These are interview estimates, not hardware promises. Real measurements depend on model architecture, runtime, kernels, hardware, sequence-length distribution, and parallelism.

### Drill 1: model weight memory

Prompt:

A 70 billion parameter model uses 16-bit weights. Estimate raw weight memory. Then estimate 8-bit and 4-bit raw weight memory.

Calculation:

- 16-bit - `70 × 10^9 parameters × 16 bits / 8 = 140 × 10^9 bytes`, or 140 GB decimal, about 130.4 GiB.
- 8-bit - 70 GB decimal, about 65.2 GiB.
- 4-bit - 35 GB decimal, about 32.6 GiB.

Strong interpretation:

Raw weights are only a lower bound. Add quantization scales or metadata, runtime workspaces, KV cache, fragmentation, and headroom. A 4-bit representation does not prove the model fits or performs well on one nominal 40 GB device.

### Drill 2: KV-cache capacity

Prompt:

Assume a model has 32 layers, 8 KV heads, head dimension 128, a 4,096-token cached sequence, and a 2-byte KV-cache element. Estimate cache memory per sequence.

Calculation:

`4,096 tokens × 32 layers × 2 for K and V × 8 heads × 128 dimensions × 2 bytes`

`= 536,870,912 bytes = 512 MiB per sequence`

At 20 such sequences, the simplified estimate is 10 GiB.

Strong interpretation:

This assumes all sequences have the full cached length and ignores allocator metadata, paging, prefix sharing, cache quantization, and parallel sharding. Confirm whether `8` is the number of KV heads rather than query heads.

### Drill 3: throughput and replica count

Prompt:

Peak demand is 12,000 output tokens per second. A benchmark on the target traffic mix shows 900 output tokens per second per replica at the acceptable latency. Use 65.0% target load. Estimate replicas.

Calculation:

Usable throughput per replica is `900 × 0.65 = 585 output tokens/s`.

Required replicas are `ceil(12,000 / 585) = 21`.

If one replica is lost, 20 replicas provide `20 × 585 = 11,700 output tokens/s`, below peak. Add failure headroom or accept controlled degradation. Benchmark prompt processing separately because input-heavy traffic can become the bottleneck.

### Drill 4: concurrency

Prompt:

An interactive endpoint receives 40 requests per second and has 2.5 seconds mean end-to-end latency. Estimate average in-system concurrency.

Calculation:

Using Little's Law under a stable system, `L = λW = 40 requests/s × 2.5 s = 100 requests`.

Strong interpretation:

This is an average, not a p95 capacity target. Bursts, heavy-tailed output lengths, retries, and queueing require more headroom. Little's Law does not imply stability if arrival rate exceeds service capacity.

### Drill 5: queue growth during overload

Prompt:

A service can complete 80 requests per second but receives 110 requests per second for 90 seconds. The queue starts empty. Ignore retries and scaling.

Calculation:

Net growth is `110 - 80 = 30 requests/s`.

After 90 seconds, backlog is `30 × 90 = 2,700 requests`.

At 80 requests per second after arrivals return to zero, drain time is `2,700 / 80 = 33.75 seconds`.

Strong interpretation:

Real requests have deadlines. Many queued requests would become useless before service, so bound the queue and reject early. If normal arrivals continue below capacity, drain time uses only the spare capacity, not total capacity.

### Drill 6: hosted-model cost

Prompt:

A service handles 3 million requests per month. Each request averages 1,200 input tokens and 300 output tokens. Assume illustrative prices of $2.00 per million input tokens and $8.00 per million output tokens. Estimate model charges.

Calculation:

- Input tokens - `3,000,000 × 1,200 = 3.6 billion`; cost is `3,600 × $2.00 = $7,200`.
- Output tokens - `3,000,000 × 300 = 0.9 billion`; cost is `900 × $8.00 = $7,200`.
- Total illustrative model charge - `$14,400 per month`.
- Average charge - `$14,400 / 3,000,000 = $0.0048 per request`.

Strong interpretation:

Add retries, failed calls, cache discounts, batch pricing, evaluation traffic, gateway cost, storage, observability, and network charges. Prices are assumptions for the drill, not claims about a vendor. Use the target provider's current contract in a real decision.

### Calculation practice rules

- Keep decimal GB and binary GiB distinct.
- Name whether throughput means requests, examples, or tokens.
- Separate average from percentile latency.
- Use measured workload distributions instead of one maximum sequence length when planning steady-state capacity.
- State headroom and failure assumptions.
- Give a range when architecture or hardware details are missing.
- Identify which input you would benchmark first.

## Question Practice Order

The priority labels below allocate practice time; they do not remove any questions from the bank.

- P0 - Start with [platform strategy and developer experience](#platform-strategy-and-developer-experience), cloud operations and the reliability portions of [reliability, security, and economics](#reliability-security-and-economics), and [Kubernetes concepts](#kubernetes-concepts).
- P1 - Continue with [gateway, serving, and performance](#gateway-serving-and-performance), the [multi-provider model gateway](#design-walkthrough-1-multi-provider-model-gateway), [model registry and lifecycle](#model-registry-and-lifecycle), multi-tenancy, security, cost, and [migration, leadership, and incidents](#migration-leadership-and-incidents).
- P2 - Add the evaluation and data portions of [lifecycle, evaluation, and data](#lifecycle-evaluation-and-data) and the [shared evaluation and observability platform](#design-walkthrough-4-shared-evaluation-and-observability-platform).
- P3 - Defer [scheduling and training infrastructure](#scheduling-and-training-infrastructure), GPU kernels, and deep inference optimization unless the target loop confirms them.

Practice these first 12 questions or cases, in order:

1. Question 1 - Design a platform roadmap for teams deploying models independently.
2. Question 2 - Choose among a shared service, library, template, or documentation.
3. Question 5 - Define success metrics for an internal ML platform.
4. Question 13 - Design overload and backpressure for streaming generation.
5. Question 29 - Define SLOs for shared inference.
6. Question 7 - Design a multi-provider model gateway with routing, quotas, and fallback.
7. [Design Walkthrough 1](#design-walkthrough-1-multi-provider-model-gateway) - Defend the gateway across cloud, reliability, policy, and migration constraints.
8. Question 31 - Design tenant isolation across models, prompts, caches, logs, and GPUs.
9. Question 33 - Design cost allocation, budgets, and quotas.
10. Question 37 - Migrate teams from direct provider calls to a shared gateway.
11. Question 24 - Design a shared evaluation service and release gates.
12. [Design Walkthrough 4](#design-walkthrough-4-shared-evaluation-and-observability-platform) - Defend evaluation, observability, privacy, and cost.

Then cover every remaining category. Override this order when the job description or recruiter confirms a different loop.

## Synthesized Interview Questions

All prompts in this section are synthesized for practice. They are not attributed to any company.

### Platform strategy and developer experience

1. Design a platform roadmap for ten teams that currently deploy models independently.
2. When should a capability be a shared service, a library, a template, or documentation?
3. How would you choose between one paved road and a federated platform?
4. A research team says the platform blocks experimentation. How do you respond?
5. Which metrics prove that an internal ML platform is successful?
6. How would you deprecate a platform API used by dozens of services?

#### Rubric for question 1

A strong answer:

- Discovers workload families, pain, risk, spend, and ownership before proposing architecture.
- Establishes a baseline such as deployment lead time, incident burden, duplicated cost, and adoption.
- Prioritizes one repeated high-value path and defines non-goals.
- Sequences interfaces, reliability, governance, migration, and self-service.
- Defines build-versus-buy criteria and decision checkpoints.
- Measures customer outcomes and platform health.

Red flags:

- Begins with a tool migration.
- Assumes every team should use one runtime.
- Has no adoption, staffing, or deprecation plan.

Drill:

Give a 10-minute strategy pitch with a first 90-day outcome, a one-year direction, and one investment you would reject.

#### Rubric for question 2

A strong answer compares state, latency sensitivity, security centralization, upgrade coordination, operational economies, customization, and blast radius. A service fits shared state or policy and centralized operations. A library fits in-process behavior and team-controlled deployment. A template accelerates creation without forcing runtime coupling. Documentation may be enough for a low-frequency task.

Red flags:

- Centralizes only because multiple teams wrote similar code.
- Ignores version skew and service ownership.

Drill:

Classify model input validation, provider credentials, evaluation schemas, and deployment manifests, then defend each choice.

#### Rubric for question 4

A strong answer:

- Identifies the exact blocked workflow and why the restriction exists.
- Separates fast experimentation from production guarantees.
- Offers a sandbox, versioned extension, bring-your-own-runtime contract, or reviewed exception.
- Sets promotion criteria from experimental to supported.
- Uses demand evidence before expanding the paved road.

Red flags:

- Removes guardrails immediately.
- Tells research to fork the platform with no integration contract.

Drill:

Role-play a disagreement between a platform owner, researcher, and security engineer.

### Gateway, serving, and performance

7. Design a multi-provider model gateway with routing, quotas, and fallback.
8. Explain continuous batching and when it improves throughput.
9. How would you autoscale an LLM serving deployment with a five-minute cold start?
10. Diagnose high GPU utilization with poor tokens-per-second throughput.
11. How would you isolate long-context requests from latency-sensitive chat traffic?
12. Compare hosted APIs, dedicated managed endpoints, and self-hosted inference.
13. Design overload and backpressure behavior for a streaming generation API.
14. How would you roll out a new quantized model safely?

#### Rubric for question 8

A strong answer explains admission during decode, variable sequence lengths, prompt and decode phases, memory limits, latency-throughput trade-offs, cancellation, fairness, and measurement. It avoids claiming universal gains.

Red flags:

- Describes only static request batching.
- Optimizes tokens per second while ignoring time to first token.

Drill:

Draw a timeline for three requests with different prompt and output lengths under static and continuous batching.

#### Rubric for question 9

A strong answer:

- Uses queue age, token demand, latency, and batch occupancy rather than CPU alone.
- Maintains warm capacity or predicts known traffic when cold start exceeds the SLO.
- Separates replica scaling from node provisioning.
- Defines admission control while capacity arrives.
- Accounts for scale-down draining and model-load failures.
- Benchmarks the workload mix and sets failure headroom.

Red flags:

- Scales only after latency has already failed.
- Assumes nodes and loaded replicas appear instantly.

Drill:

Propose thresholds for a bursty workload, then explain oscillation prevention.

#### Rubric for question 12

A strong answer compares quality, capability, data policy, latency, variable versus fixed cost, utilization, operational expertise, capacity availability, lock-in, and failure modes. It can recommend a hybrid path and names the demand threshold or policy constraint that would change the choice.

Red flags:

- Claims self-hosting is always cheaper.
- Compares provider token price with GPU rental while omitting idle capacity and operations.

Drill:

Make a decision with low stable traffic, then revise it for regulated data and high steady utilization.

#### Rubric for question 13

A strong answer defines bounded queues, admission by deadline and tenant quota, priority classes, cancellation, load shedding, retry semantics, degraded routes, and overload telemetry. It protects the platform from retry storms and preserves critical capacity.

Red flags:

- Uses an unbounded queue.
- Retries every error immediately.

Drill:

Describe exact client-visible behavior for queue full, deadline expired, provider throttled, and stream interrupted.

### Scheduling and training infrastructure

15. Design a scheduler for distributed GPU training jobs with priorities and quotas.
16. When is preemption worth its cost, and how should victims be chosen?
17. How do checkpoint frequency and storage bandwidth affect cluster efficiency?
18. Explain gang scheduling and the fragmentation it can create.
19. How would you place jobs across heterogeneous accelerator types?
20. Diagnose a cluster with low allocation despite a long pending queue.
21. How would you support both elastic and fixed-size distributed jobs?

#### Rubric for question 15

A strong answer:

- Defines job resources, topology, duration, priority, deadlines, and checkpoint capability.
- Uses queues, quotas, fair share, reservations, and controlled borrowing.
- Supports gang scheduling where all workers are required.
- Handles leases, heartbeats, worker failure, retry limits, and durable state.
- Makes preemption cost-aware and validates checkpoint restore.
- Measures utilization, pending age, completion time, fairness, and wasted work.

Red flags:

- Schedules workers independently for a fixed-size distributed job.
- Uses priority with no starvation control.
- Treats requested GPU count as the only placement constraint.

Drill:

Schedule five jobs manually onto a mixed cluster, then respond to an urgent job and a node failure.

#### Rubric for question 16

A strong answer estimates remaining work, checkpoint age, restart time, priority gain, topology constraints, and deadline impact. It protects non-preemptible workloads, limits repeated victimization, and considers draining or backfilling before killing work.

Red flags:

- Always preempts the lowest-priority job.
- Assumes checkpoint presence means restore is safe.

Drill:

Compare preempting a 12-hour job checkpointed 3 minutes ago with a 20-minute job that cannot resume.

### Lifecycle, evaluation, and data

22. Design a model registry and promotion workflow for hundreds of models.
23. What must be versioned to reproduce a generative AI evaluation?
24. Design a shared evaluation service for offline tests and release gates.
25. How would you detect a model-quality regression after an infrastructure change?
26. Explain point-in-time correctness and training-serving skew.
27. How would you backfill a feature pipeline without corrupting online state?
28. Design prompt versioning and rollback across many application teams.

#### Rubric for question 22

A strong answer uses immutable artifacts, lineage, validation, evaluation evidence, approval policy, signed provenance, deployment references, canaries, rollback, retention, and access control. It separates model metadata from large artifact storage and defines consistency around promotion.

Red flags:

- Overwrites a `production` artifact in place.
- Rolls back model weights but not tokenizer, schema, or features.

Drill:

Define the minimal metadata needed to answer who built, evaluated, approved, and deployed a model.

#### Rubric for question 24

A strong answer:

- Defines evaluation run, dataset, configuration, grader, result, and comparison contracts.
- Supports deterministic, model-based, and human graders.
- Versions full execution configuration and protects sensitive examples.
- Runs asynchronously with idempotency, retries, quotas, and cost controls.
- Reports slices, uncertainty, disagreement, latency, and cost.
- Integrates release gates without making one noisy score an absolute truth.

Red flags:

- Treats an LLM judge as ground truth.
- Stores only an aggregate score.

Drill:

Design an evaluation comparison where the overall score improves but one safety-critical slice regresses.

#### Rubric for question 25

A strong answer freezes the application configuration, shadows or replays representative traffic under privacy controls, compares output and operational metrics by slice, checks numerical precision and tokenization changes, and uses canaries with rollback. It recognizes nondeterminism and uses repeated samples or tolerances.

Red flags:

- Attributes all output changes to the model.
- Relies only on infrastructure dashboards.

Drill:

Investigate a quality drop after changing runtime, quantization, and batching simultaneously.

### Reliability, security, and economics

29. Define SLOs for a shared inference platform.
30. A region serving production inference fails. Walk through response and recovery.
31. Design tenant isolation for models, prompts, caches, logs, and GPUs.
32. How would you prevent provider credentials and sensitive prompts from leaking?
33. Design cost allocation, budgets, and quotas for shared AI infrastructure.
34. How do you test disaster recovery for a model platform?
35. A platform control plane is unavailable but serving replicas are healthy. What should happen?
36. How would you investigate one tenant causing latency for others?

#### Rubric for question 29

A strong answer:

- Starts with user-visible availability, latency, stream completion, and deployment propagation.
- Defines eligibility and excludes only clearly invalid traffic.
- Segments interactive and batch workloads.
- Uses percentiles and error budgets.
- Adds diagnostic indicators without turning them all into contractual SLOs.
- Defines overload, dependency, maintenance, and ownership behavior.

Red flags:

- Uses GPU utilization as an SLO.
- Promises one latency target for every model and sequence length.

Drill:

Write an SLO for interactive generation and a separate one for batch evaluation.

#### Rubric for question 31

A strong answer maps the threat model to identity, authorization, network, runtime, node, data, cache, key, log, and operational boundaries. It includes noisy-neighbor controls and explains when stronger cluster or account isolation is justified.

Red flags:

- Says namespaces provide complete isolation.
- Shares a prompt cache across tenants without authorization-aware keys.

Drill:

Revise the design for ordinary internal teams, then for regulated workloads and untrusted user code.

#### Rubric for question 33

A strong answer attributes direct and shared cost, handles idle and failed work, exposes timely usage, sets alerts and limits, reserves critical capacity, and defines exception ownership. It connects quotas to priorities and avoids incentives that make teams hide usage.

Red flags:

- Allocates all idle cost to the latest tenant.
- Enforces hard monthly budgets with no production safety mechanism.

Drill:

Create a policy for experimentation, production, evaluation, and incident capacity.

#### Rubric for question 35

A strong answer keeps existing data-plane workloads serving from cached, last-known-good configuration for a bounded period. It freezes unsafe mutations, preserves local policy needed for authorization, buffers or sheds nonessential telemetry, and defines expiration behavior. It restores control-plane state from durable sources and reconciles drift after recovery.

Red flags:

- Stops healthy serving immediately.
- Allows deployments and policy changes without authoritative state.

Drill:

List which operations remain available during a 30-minute control-plane outage.

### Migration, leadership, and incidents

37. Migrate twenty teams from direct provider calls to a shared gateway.
38. A platform launch has low adoption. How do you diagnose it?
39. Security requires a control that doubles latency. How do you lead the decision?
40. Research, product, and finance disagree on GPU allocation. Set a policy.
41. Tell me about a platform incident that changed your architecture.
42. How would you retire an expensive legacy training platform?

#### Rubric for question 37

A strong answer:

- Inventories features, data classes, traffic, failure behavior, and owners.
- Defines compatibility gaps and versioned gateway semantics.
- Starts with willing low-risk teams, then shadows or dual-runs where safe.
- Preserves rollback and avoids duplicating non-idempotent calls.
- Supplies adapters, documentation, dashboards, and support.
- Uses staged enforcement and deprecation dates.
- Measures adoption, reliability, latency, quality, and cost.

Red flags:

- Forces a flag-day cutover.
- Claims the gateway can normalize every provider behavior.

Drill:

Plan migration for streaming, tool calls, embeddings, and a regulated workload.

#### Rubric for question 40

A strong answer establishes organizational goals, workload classes, reservations, fair share, borrowing, deadlines, preemption rules, and an escalation owner. It publishes allocation and utilization, revisits policy as demand changes, and avoids treating historical possession as permanent entitlement.

Red flags:

- Allocates only first come, first served.
- Resolves every conflict through executive escalation.

Drill:

Allocate a constrained fleet among a launch, a long research run, and routine experiments.

## Design Walkthrough 1: Multi-Provider Model Gateway

### Prompt

Design a model gateway for internal product teams using several hosted providers and selected self-hosted models.

### Requirements and non-goals

Requirements:

- One authenticated API for generation, embeddings, and capability discovery
- Streaming and synchronous responses
- Routing by capability, policy, region, health, quality tier, and cost
- Tenant quotas, budgets, audit metadata, and usage attribution
- Bounded fallback and provider-independent operational telemetry
- Versioned behavior and migration from direct provider calls

Non-goals:

- Perfect semantic equivalence across models
- Hiding every provider feature
- Storing all prompts and outputs
- Training or fine-tuning models

### Estimates

Assume for discussion:

- 100 internal services across 30 tenants
- 200 average and 800 peak requests per second
- 2,000 average input and 400 average output tokens per request
- 20.0% of traffic streams
- 99.9% monthly gateway availability target, excluding valid policy and quota rejections

At peak, input demand is `800 × 2,000 = 1.6 million input tokens/s`; output demand is `800 × 400 = 320,000 output tokens/s`. These estimates determine provider quotas and route capacity. They do not imply all tokens are processed in one second because generation spans time.

Ask for traffic by model capability, region, tenant, and sequence length before final sizing.

### Architecture

1. Client obtains workload identity and calls a regional gateway endpoint.
2. Admission layer validates schema, identity, tenant, deadline, and idempotency requirements.
3. Policy layer resolves allowed providers, models, regions, retention mode, and budget.
4. Router reads a versioned route policy plus recent health and capacity signals.
5. Provider adapter translates the portable contract and preserves provider-specific error detail in normalized categories.
6. Streaming proxy returns ordered events and an explicit terminal event.
7. Usage pipeline records route, token counts, latency, status, and cost metadata without sensitive content by default.
8. Control plane manages tenants, route policies, model catalog, quotas, and rollout.

Keep the request path independent from the analytics warehouse. Cache last-known-good policy in regional gateways with a bounded validity period.

### APIs and data

```text
POST /v1/generations
Authorization: Bearer <workload-identity>
Idempotency-Key: <optional-key>

{
  "tenant_id": "support",
  "capability": "text.generate",
  "quality_tier": "standard",
  "messages": [...],
  "stream": true,
  "deadline_ms": 8000,
  "data_policy": "no_content_retention",
  "route_policy_version": "2026-07-30"
}
```

Response metadata includes request ID, selected model alias, route class, usage, policy version, and terminal status. Do not expose a provider credential or hidden internal topology.

Core records:

- Tenant policy - identity, allowed capabilities, regions, data classes, quota, and budget owner
- Model catalog entry - capabilities, context limit, regions, policy eligibility, lifecycle state, and adapter version
- Route policy - ordered constraints and scoring, version, owner, and rollout state
- Usage event - request, tenant, route, input and output units, latency, status, and estimated cost

### Reliability

- Use strict end-to-end deadlines and reserve only part of the deadline for fallback.
- Retry transient connection failures only when request semantics and provider state make it safe.
- Apply circuit breakers and health scoring, but avoid synchronizing all traffic onto one fallback.
- Bound tenant and global concurrency.
- Preserve critical routes during overload and reject early with retry guidance.
- Deploy gateway and policy cache across failure domains.
- Canary route-policy and adapter changes.

### Security and privacy

- Use workload identity and provider credentials held by gateway adapters.
- Enforce region, provider, and retention policy before routing.
- Redact or omit content from standard logs.
- Encrypt sensitive traces separately with narrow access and retention.
- Audit policy, credential, and route changes.
- Treat provider response content as untrusted.

### Cost

- Attribute tokens, requests, cached units, failed calls, retries, and gateway overhead.
- Use quality-qualified cheaper routes, not price-only routing.
- Set per-tenant alerts, rate limits, concurrency, and monthly budget policy.
- Evaluate reserved self-hosted capacity only against measured steady demand and full operating cost.

### Migration

1. Inventory provider features and direct-call workloads.
2. Define the portable core and explicit extension mechanism.
3. Release SDK adapters that preserve current behavior.
4. Migrate low-risk workloads and compare latency, errors, quality, and cost.
5. Shadow route decisions without duplicating billable calls where possible.
6. Move credentials to the gateway and establish rollback to the prior path.
7. Deprecate direct access by capability and risk tier.

### Follow-ups

- A provider begins throttling at peak. How do you prevent fallback overload?
- One model is cheaper but fails a critical quality slice. Where is that encoded?
- The control plane is unavailable. Which gateway behavior remains safe?
- A team needs an unsupported provider feature. How do extensions avoid contract fragmentation?

## Design Walkthrough 2: High-Throughput Inference Platform

### Prompt

Design a multi-tenant platform serving several open-weight generative models on GPUs for interactive and batch workloads.

### Requirements and non-goals

Requirements:

- Deploy immutable model versions through a self-service contract
- Support streaming interactive requests and asynchronous batch jobs
- Meet per-class latency and availability SLOs
- Use continuous batching and accelerator-aware placement
- Isolate tenants, enforce quotas, and attribute cost
- Canary, roll back, autoscale, and recover from node failure

Non-goals:

- Train models
- Guarantee one SLO across all sequence lengths
- Run arbitrary untrusted code in the serving process

### Estimates

Assume one initial model receives:

- 100 peak interactive requests per second
- 1,500 average input tokens and 300 average output tokens
- 3-second average request residence for the measured traffic mix
- Benchmark throughput of 750 output tokens per second per replica at the SLO
- 60.0% target operating load

At a sustained peak arrival rate in a stable system, Little's Law gives mean in-system concurrency during that peak interval of `100 requests/s × 3 s = 300 requests`.

Peak output demand is `100 × 300 = 30,000 output tokens/s`.

Usable replica throughput is `750 × 0.60 = 450 output tokens/s`, so the first estimate is `ceil(30,000 / 450) = 67 replicas`.

This rough estimate must be corrected with prompt-processing capacity, per-replica concurrent-sequence memory, sequence distributions, parallelism, and failure headroom. A benchmark using the target workload is the source of truth.

### Architecture

- Deployment API accepts model artifact, runtime profile, resource shape, SLO class, scaling bounds, and rollout policy.
- Reconciler validates lineage and policy, then creates regional deployment revisions.
- Placement service selects accelerator type, topology, and replica count.
- Model loader retrieves signed artifacts into a warm pool or node-local cache.
- Regional request router checks identity, deployment version, quota, and deadline.
- Admission controller assigns workload class and rejects requests that cannot meet deadline.
- Runtime scheduler performs prompt processing, continuous batching, KV-cache allocation, cancellation, and streaming.
- Autoscaler uses queue age, token demand, batch occupancy, and loaded capacity.
- Batch traffic uses separate queues and consumes borrowable capacity without violating interactive reservations.

Separate deployment control state from serving. Existing loaded revisions should continue during a bounded control-plane outage.

### APIs and data

```text
POST /v1/deployments

{
  "name": "assistant-70b",
  "artifact_version": "sha256:...",
  "runtime_profile": "generation-v3",
  "resource_profile": "gpu-large-x4",
  "traffic_classes": ["interactive", "batch"],
  "min_replicas": 4,
  "max_replicas": 80,
  "rollout": {
    "canary_percent": 5,
    "guardrails": ["availability", "ttft", "quality_eval"]
  }
}
```

Store immutable deployment revisions, desired and observed state, artifact lineage, evaluation evidence, traffic policy, and rollback target. High-cardinality request telemetry should flow to an observability system rather than the transactional control database.

### Reliability

- Readiness requires model loaded, warmup passed, and a real inference probe within limits.
- Drain removes new admissions, allows bounded completion, then cancels safely.
- Node failure triggers request failure or retry according to idempotency and remaining deadline.
- Preserve minimum warm capacity across zones.
- Bound KV-cache allocation and queues; reject before out-of-memory failure.
- Canary runtime, kernel, model, and quantization changes independently when possible.
- Degrade batch capacity before interactive capacity.

### Security

- Authorize deployment and invocation separately.
- Sign artifacts and verify provenance before load.
- Isolate tenant data in request buffers, caches, logs, and object storage.
- Restrict runtime network access and administrative debug access.
- Use dedicated nodes, clusters, or accounts for threat models that require stronger isolation.

### Cost

- Track loaded GPU time, useful tokens, idle warm capacity, failed requests, and batch borrowing.
- Compare model quality at a target SLO before choosing quantization or hardware.
- Use smaller models or hosted overflow only under an explicit route contract.
- Set scaling bounds to prevent a traffic bug from consuming the fleet.

### Migration

- Start with one model and one cooperative workload.
- Build conformance tests against current serving behavior.
- Replay sanitized traffic and compare output tolerances, TTFT, completion latency, and errors.
- Canary by tenant and preserve a route back to the old endpoint.
- Move batch workloads after interactive behavior is stable.
- Publish unsupported patterns and the escape-hatch process.

### Follow-ups

- Long-context traffic triples. Which resource fails first?
- A quantized revision is faster but changes output quality. What blocks promotion?
- Batch jobs starve during business hours. How do reservations and borrowing work?
- Cluster autoscaling takes ten minutes. How do you meet burst SLOs?

## Design Walkthrough 3: GPU Training and Job Scheduler

### Prompt

Design a shared scheduler for distributed training, fine-tuning, evaluation, and batch inference on a heterogeneous GPU fleet.

### Requirements and non-goals

Requirements:

- Submit, inspect, cancel, retry, and resume jobs
- Support single-node and distributed gang-scheduled jobs
- Enforce team quotas, priorities, reservations, and fair borrowing
- Place by accelerator, memory, topology, network, and storage needs
- Preempt eligible jobs using durable checkpoints
- Survive scheduler and worker failures without duplicate ownership
- Report utilization, pending time, completion time, and cost

Non-goals:

- Implement training frameworks
- Make every job elastic
- Guarantee immediate capacity for unreserved work

### Estimates

Assume:

- 1,000 GPUs across two accelerator classes
- 300 job submissions per day
- Job sizes from 1 to 128 GPUs
- Median duration 4 hours, with a long tail beyond 48 hours
- 20.0% fleet reservation for urgent production and evaluation workloads

If 800 GPUs are generally allocatable and target physical allocation is 85.0%, the planning target is `800 × 0.85 = 680 allocated GPUs` outside the reserved pool. This is not useful-work utilization. Track allocated, active compute, communication stall, checkpoint, and idle-inside-allocation time separately.

Queue simulation using real job shapes is more credible than an average GPU-hours calculation because gang size and topology create fragmentation.

### Architecture

1. Job API validates image, command, artifact locations, identity, resource shape, priority class, retry policy, and checkpoint contract.
2. Durable job store records desired state and monotonic attempts.
3. Queue manager computes eligibility from quota, fair share, reservation, age, and policy.
4. Placement engine filters nodes by hardware and topology, then scores packing, fragmentation, and data locality.
5. Lease manager atomically grants all resources for a gang.
6. Node agents start signed workloads, report heartbeats and accelerator health, and enforce resource boundaries.
7. Checkpoint controller records durable checkpoint manifests and verifies resumability metadata.
8. Preemption controller compares scheduling benefit with lost-work and restart cost.
9. Reconciler recovers expired leases and advances job state idempotently.

### APIs and data

```text
POST /v1/jobs
Idempotency-Key: <key>

{
  "project": "ranking-research",
  "workload_class": "training",
  "priority": "normal",
  "replicas": 16,
  "resources_per_replica": {
    "gpu_type": "class-b",
    "gpu_count": 8,
    "cpu": 64,
    "memory_gib": 512
  },
  "topology": "high_bandwidth_domain",
  "max_runtime_hours": 24,
  "preemptible": true,
  "checkpoint": {
    "uri": "object://project/run-123",
    "interval_minutes": 20
  }
}
```

Core data includes job, attempt, gang, resource lease, checkpoint manifest, queue entitlement, node inventory, and usage event. State transitions require compare-and-set or equivalent fencing so two scheduler instances cannot own the same attempt.

### Reliability

- Scheduler instances are replaceable; durable state and leases establish authority.
- Fencing tokens prevent a paused worker from writing after its lease is reassigned.
- Worker loss fails or shrinks a job according to its declared capability.
- Retry limits distinguish infrastructure failure from deterministic user failure.
- Checkpoints use durable storage, checksums, completion markers, retention, and restore tests.
- Large outages pause new scheduling before uncontrolled retries flood storage and networking.

### Security

- Use per-job workload identities and scoped artifact credentials.
- Admit signed or policy-approved images.
- Restrict privileged containers, host mounts, device access, and network egress.
- Separate untrusted code according to the threat model.
- Protect other tenants from debug endpoints, shared temporary storage, logs, and checkpoint paths.

### Cost and capacity

- Attribute reserved and consumed GPU time, CPU, storage, network, and checkpoint traffic.
- Expose pending reason so teams can reduce impossible resource shapes.
- Backfill short jobs into temporary gaps only when they can drain before reservations.
- Use preemptible external capacity for resumable workloads when economics and data policy permit.
- Forecast by accelerator type and topology, not aggregate GPU count.

### Migration

- Import job metadata and artifact conventions from existing systems.
- Provide an adapter for current submission syntax.
- Begin with new evaluation and fine-tuning jobs before critical long-running training.
- Validate scheduling fairness and checkpoint restore under synthetic failures.
- Run selected workloads on both systems only when duplicate compute and side effects are controlled.
- Move quotas and reservations through a published governance process.
- Stop new legacy submissions before draining existing long jobs.

### Follow-ups

- An urgent 128-GPU job arrives but the fleet is fragmented. What can the scheduler do?
- A team requests non-preemptible status for every job. Who decides?
- Checkpoint writes saturate object storage. How do you stabilize the system?
- One accelerator class has a long queue while another is idle. Can jobs move safely?

## Design Walkthrough 4: Shared Evaluation and Observability Platform

### Prompt

Design a platform that lets product and ML teams evaluate model, prompt, retrieval, and runtime changes and observe production behavior without centralizing sensitive content by default.

### Requirements and non-goals

Requirements:

- Versioned datasets, slices, configurations, graders, and comparison runs
- Deterministic, model-based, and human evaluation
- Offline release gates and sampled production monitoring
- Operational traces joined to evaluation and cost metadata
- Multi-tenant access control, privacy policy, and retention
- Reproducible results with uncertainty visible
- Scalable asynchronous execution with quotas

Non-goals:

- One universal quality metric
- Unlimited retention of prompts and outputs
- Replacing domain experts with model graders

### Estimates

Assume:

- 40 teams and 500 active evaluation configurations
- 2,000 evaluation runs per day
- Median 1,000 examples and p95 50,000 examples per run
- 5.0% of examples require human review
- Production generates 50 million requests per day, but only policy-approved samples store content

Total daily execution volume cannot be inferred from the median run size; it requires the run-size distribution or at least the arithmetic mean. If every run were the median size, `2,000 × 1,000 = 2 million example executions/day` is a rough planning baseline, but the long tail may make actual volume materially larger. Admission should estimate tokens, model calls, grader calls, and cost before accepting a large run.

For 50 million production requests per day, even a 0.1% content sample is 50,000 examples per day. Retention and access rules matter more than raw metadata storage.

### Architecture

- Evaluation API creates immutable run specifications.
- Dataset service stores manifests and references to access-controlled examples.
- Configuration registry versions model, prompt, retrieval, tool, policy, runtime, and decoding settings.
- Planner expands runs into sharded tasks and estimates cost.
- Worker pools execute applications or replay traces under isolated credentials.
- Grader service runs deterministic checks, model-based graders, and human-review workflows.
- Aggregator computes per-slice metrics, paired comparisons, disagreement, uncertainty, latency, and cost.
- Release-policy service evaluates guardrails and records evidence, with human approval for high-risk changes.
- Production telemetry pipeline records operational metadata broadly and sensitive content only under explicit policy.
- Trace explorer links request, configuration hash, route, latency, cost, and sampled evaluation outcomes.

### APIs and data

```text
POST /v1/evaluation-runs

{
  "dataset_version": "support-regression@42",
  "candidate_config": "assistant@9f3c",
  "baseline_config": "assistant@81aa",
  "graders": ["schema-valid@3", "task-judge@7", "safety@11"],
  "slices": ["language", "issue_type", "risk"],
  "sampling": {
    "repetitions": 3
  },
  "budget_usd": 500,
  "retention_policy": "restricted-30d"
}
```

Store run specification, task attempts, example-level outputs or references, grader outputs, human labels, aggregate metrics, policy decision, and provenance. Preserve raw evidence under access policy so an aggregate regression can be investigated.

### Reliability and statistical caution

- Use idempotent task keys and distinguish retries from repeated samples.
- Make partial results explicit and never present them as a complete run.
- Version graders and validate model graders against human labels.
- Use paired comparisons when candidates run on the same examples.
- Report sample size and uncertainty; avoid false precision for small slices.
- Quarantine corrupted datasets or grader revisions.
- Keep release gates available in degraded mode through cached policy, or fail closed for high-risk releases.
- Back up manifests, lineage, labels, and decisions; large reproducible outputs may use tiered retention.

### Security and privacy

- Preserve source authorization when importing production examples.
- Redact, tokenize, or synthesize sensitive fields where valid.
- Separate metadata access from content access.
- Use per-run credentials and constrain model providers by data policy.
- Audit exports, human-review access, and administrative changes.
- Support deletion requests through derived evaluation artifacts where required.

### Cost

- Estimate candidate, baseline, grader, embedding, retrieval, and human-review cost before launch.
- Set run budgets and require approval for expansion.
- Cache only when the full execution key and privacy boundary permit reuse.
- Sample intelligently by risk and failure slice rather than increasing all traffic uniformly.
- Attribute platform overhead and evaluation spend to teams while funding shared safety suites centrally if appropriate.

### Migration

- Define a minimal evaluation schema that can import existing datasets.
- Wrap team-specific graders behind a versioned interface.
- Start with one release decision where teams already feel pain.
- Compare platform results with the team's current process and resolve discrepancies.
- Integrate CI as advisory before enforcing gates.
- Migrate production sampling only after privacy and access reviews.
- Publish ownership for shared datasets and graders.

### Follow-ups

- The model judge prefers the candidate but humans do not. What happens?
- A safety slice has only 30 examples. How should the release decision use it?
- A team changes retrieval but records only a prompt version. How do you restore reproducibility?
- Production traces contain regulated data. What observability remains possible?

## Strong-Answer Habits and Common Red Flags

### Strong-answer habits

- Lead with users, workload classes, SLOs, and constraints.
- Define the platform contract before listing components.
- Keep units visible and identify the benchmark needed.
- Separate control plane, data plane, and asynchronous analysis.
- Explain overload, not only normal operation.
- Preserve identity and policy through queues and caches.
- Connect canary signals to an automatic or human rollback decision.
- State what is intentionally not centralized.
- End with migration, adoption, ownership, and the next scaling threshold.

### Red flags across platform interviews

- "Kubernetes handles it" without explaining scheduling or failure semantics.
- "Add more GPUs" without memory, throughput, quota, or lead-time estimates.
- Unbounded retries or queues.
- Average latency used as the only latency measure.
- GPU utilization treated as proof of useful throughput.
- One global model, SLO, or security boundary for every workload.
- Mutable production artifacts and incomplete rollback dependencies.
- Tenant identity dropped inside asynchronous work.
- Provider fallback that silently violates data or quality policy.
- A platform mandate with no migration or internal-customer evidence.
- Staff-level claims based only on implementation size.

## Two-Week Platform Rotation

This rotation assumes 15-20 total hours per week. Adjust after the diagnostic in [README.md](README.md).

The proxy-evidence default covers cloud platform operation, gateways, reliability, and evaluation before GPU scheduling or deep inference.

### Week 1: cloud platform, gateway, and reliability

Day 1 - role, cloud boundaries, and contracts:

- Read this module's scope, signals, and design method.
- Map three target job descriptions to inference, training, evaluation, data, and developer-platform ownership.
- Write one page defining customers, cloud boundaries, contracts, SLOs, and non-goals for a model gateway.

Day 2 - container platform and delivery:

- Trace a workload through `CI/CD`, image build, policy checks, `Kubernetes` deployment, service discovery, and rollback.
- Define health checks, rollout safety, configuration ownership, and secrets handling.
- Explain which guarantees come from the platform and which must come from the application.

Day 3 - gateway, overload, and autoscaling:

- Design provider routing, deadlines, cancellation, fallback, and policy-aware errors.
- Design bounded queues, quotas, cancellation, and load shedding.
- Compare queue age, token demand, latency, and utilization as scaling signals.

Day 4 - reliability, monitoring, and isolation:

- Define user-visible SLIs, SLOs, error budgets, dashboards, alerts, incident ownership, and disaster recovery.
- Trace identity and data policy through a gateway request.
- Practice questions 29, 31, 33, and 35.

Day 5 - mock and correction:

- Run a 55-minute multi-provider gateway mock.
- Score it with the scorecard below.
- Redo the weakest ten-minute section immediately.
- Record one corrected design and one project story that proves related experience.

Week 1 deliverables:

- One cloud and `Kubernetes` deployment map
- One gateway design
- One SLO, monitoring, and incident plan
- One tenant-isolation and cost policy
- One scored mock
- One error-log entry per material miss

### Week 2: lifecycle, evaluation, strategy, and optional depth

Day 1 - lifecycle and MLOps:

- Design registry, lineage, promotion, canary, rollback, deprecation, and ownership.
- Compare managed services with a shared internal platform.
- Practice questions 22, 25, and 37.

Day 2 - evaluation and observability:

- Define evaluation run, dataset, configuration, grader, and result contracts.
- Design release evidence for a risky model change.
- Practice questions 23-25 and walk through the shared evaluation platform.

Day 3 - data, SQL, and economics:

- Trace lineage and point-in-time correctness through one data workflow.
- Use `SQL` to inspect platform usage, cost, evaluation slices, or operational failures.
- Define cost allocation and quota policy.

Day 4 - strategy and migration:

- Prepare one platform strategy story and one migration story.
- Practice questions 1-6 and 37-42.
- Explain one paved-road decision and one justified escape hatch.

Day 5 - target-specific depth and full simulation:

- If the job description confirms dedicated inference or GPU scheduling, study the relevant calculation drills and questions 8-20. Otherwise, use this time for cloud, gateway, reliability, lifecycle, and evaluation gaps.
- Run the mock format below.
- Score senior and staff signals separately.
- Repeat any dimension below 3 within 48 hours.
- Update project and behavioral evidence using [project deep dives and take-homes](08-project-deep-dives-and-take-homes.md) and [senior and staff behavioral preparation](07-senior-staff-behavioral.md).

Week 2 deliverables:

- One lifecycle and migration design
- One evaluation-platform design
- One strategy memo with explicit non-goals
- One data or `SQL` diagnostic
- One full scored mock
- A readiness decision with evidence

Override this rotation when the job description or recruiter confirms a different loop. GPU scheduling, kernels, and deep inference become early priorities only when that evidence is explicit.

## Mock Interview Format

Use a 70-minute session:

1. 0-5 minutes - interviewer gives one synthesized prompt and answers requirement questions.
2. 5-10 minutes - candidate defines customers, requirements, SLOs, risks, and non-goals.
3. 10-16 minutes - candidate estimates scale, memory, throughput, concurrency, queueing, or cost.
4. 16-24 minutes - candidate defines APIs, data contracts, and ownership.
5. 24-39 minutes - candidate draws architecture and critical flows.
6. 39-49 minutes - interviewer probes one deep area such as batching, scheduling, isolation, or evaluation.
7. 49-57 minutes - candidate covers failures, overload, observability, and disaster recovery.
8. 57-63 minutes - candidate explains cost, rollout, migration, and adoption.
9. 63-67 minutes - interviewer asks a staff-level prioritization or disagreement follow-up.
10. 67-70 minutes - candidate summarizes decisions, risks, and next evidence.

The interviewer should inject two changes, such as:

- Traffic increases fivefold but budget stays fixed.
- A regulated tenant requires stronger isolation.
- One region or provider fails.
- A critical workload needs preemption priority.
- Quality regresses after a runtime optimization.
- Teams refuse migration because an extension is missing.

Record whether the candidate revises assumptions coherently rather than defending the original design at all costs.

## Scorecard

Use the canonical scale and readiness rules in [mock interviews and scorecards](09-mock-interviews-and-scorecards.md). Score each dimension from 1 to 4:

- 1 - weak or unsafe; behavior is missing, materially incorrect, or requires direct rescue
- 2 - partial; presents a workable baseline with important gaps or needs targeted prompting
- 3 - interview-ready; complete, independent, production-ready, and successful on expected follow-ups
- 4 - strong senior or staff evidence; unusually clear, deep, adaptive, and organization-aware

Dimensions:

1. Problem framing - identifies customers, workload classes, constraints, SLOs, risks, and non-goals.
2. Estimation - uses correct units, cautious formulas, capacity headroom, and meaningful benchmarks.
3. Contracts - defines APIs, versions, identity, deadlines, cancellation, errors, and ownership.
4. Architecture - separates control and data planes and explains critical flows.
5. ML workload depth - reasons accurately about serving, memory, batching, scheduling, lifecycle, or evaluation.
6. Reliability - covers bounded queues, overload, failure isolation, canary, rollback, incidents, and recovery.
7. Security and privacy - maps threat model to identity, isolation, secrets, retention, and audit.
8. Cost and capacity - attributes spend, sets quotas, plans scarce resources, and states trade-offs.
9. Migration and developer experience - provides paved roads, escape hatches, compatibility, adoption, and deprecation.
10. Senior or staff leverage - connects strategy, sequencing, governance, influence, and organizational outcomes.
11. Communication - drives the discussion, labels assumptions, answers follow-ups, and summarizes decisions.

The maximum is 44. All 11 dimensions are required. A total or score band describes one mock and never establishes readiness.

Per-mock interpretation:

- Developing evidence - at least one required dimension scores 1 or 2; repair and re-test the observed gap.
- Interview-ready mock performance - every required dimension scores at least 3, with no hard fail.
- Strong staff mock evidence - every required dimension scores at least 3, and cost and capacity, migration and developer experience, and senior or staff leverage score 4 with concrete cross-team or organizational evidence.

These labels describe one mock only. Readiness requires the repeated evidence below; the labels are practice heuristics, not hiring predictions.

## Readiness Gate

The [readiness rules in module 09](09-mock-interviews-and-scorecards.md#readiness-rules) are canonical. Before treating this format as interview-ready, verify:

### Role targeting

- [ ] I know whether each target role owns inference, training, evaluation, data, developer tooling, or GPU infrastructure.
- [ ] I can contrast platform work with Product AI, FDE, traditional MLOps, and research roles.
- [ ] I have mapped target requirements to evidence I personally own.

### Technical depth

- [ ] I can calculate weight memory, KV cache, concurrency, queue growth, replica count, and illustrative cost with units.
- [ ] I can explain batching, continuous batching, KV cache, quantization, autoscaling, and backpressure.
- [ ] I can explain gang scheduling, fairness, preemption, checkpointing, and heterogeneous placement.
- [ ] I can design tenant isolation, lifecycle, evaluation, observability, quotas, and disaster recovery.
- [ ] I can distinguish portable concepts from one vendor's syntax.

### Design performance

- [ ] I have completed all four walkthrough prompts without notes.
- [ ] I define APIs and ownership before deep infrastructure detail.
- [ ] I include overload, rollback, migration, and adoption without interviewer prompting.
- [ ] I can revise the design after a constraint changes.
- [ ] My three most recent relevant full platform mocks used different prompts.
- [ ] At least two mocks were scored by different interviewers, or one was independently double-scored before the debrief.
- [ ] Every required scorecard dimension scored at least 3 in at least two of the three mocks.
- [ ] No required dimension scored 1 in either of the two most recent mocks, and no hard fail remains unresolved.
- [ ] I finished the core scope within the stated time limit in at least two mocks.
- [ ] I handled at least one material follow-up without direct rescue in each of the two most recent mocks.
- [ ] Every known or repeated failure completed a successful re-test with a fresh prompt.
- [ ] For a staff target, at least two mocks also met the strong staff evidence condition in the scorecard.

### Senior and staff evidence

- [ ] I have one platform strategy story, one incident story, and one migration story.
- [ ] Each story states baseline, personal decisions, trade-offs, outcome, and learning.
- [ ] My staff examples show cross-team leverage, governance, and sequencing.
- [ ] I can state an escape hatch and an investment I would reject.
- [ ] I can discuss cost and capacity allocation as organizational decisions.

If any target-company gate remains weak or untested, delay broad interviewing or narrow the role set while you repeat that skill under timed conditions.

## Related Preparation

- [Curriculum overview](README.md) - diagnostic, profile selection, and eight-week operating rhythm
- [Common core](01-common-core.md) - coding, APIs, distributed systems, ML fundamentals, security, and estimation
- [AI/ML system design](03-ai-ml-system-design.md) - reusable 45-60 minute design method
- [Senior and staff behavioral preparation](07-senior-staff-behavioral.md) - leadership, influence, conflict, failure, and scope evidence
- [Project deep dives and take-homes](08-project-deep-dives-and-take-homes.md) - project defense and practical artifacts
- [Mock interviews and scorecards](09-mock-interviews-and-scorecards.md) - simulation cadence and feedback loops
- [Existing AI system design questions](../questions/04-ai-system-design.md) - additional serving and platform prompts
- [AI engineering job-market trends](../../job-market/trends.md) - repository evidence about role archetypes and changing skill demand
- [AI engineering skills analysis](../../role/02-skills.md) - broader role and platform-skill context

Use market analysis to prioritize target-role preparation, not to invent a universal interview loop. Use recruiter guidance, the job description, and the team's stated ownership as the final source of truth.
