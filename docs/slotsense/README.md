# Slotsense AI Architecture Notes

These documents explain the architecture and the engineering reasoning visible in the current Slotsense repositories. They are written for interview preparation: the emphasis is on decisions, incidents, tradeoffs, and the code that enforces each invariant.

The core system spans three services:

- `slotsense-backend` owns projects, assistants, widgets, chats, transcript persistence, and assistant publication.
- `slotsense-ai-assistant-new` owns request routing, guardrails, escalation policy, RAG, document ingestion, and retrieval caching.
- `slotsense-rnd-retention-ai` owns proactive retention decisions and reactive retention conversations.

Shared infrastructure includes Redis, Qdrant, S3, Celery, and ClickHouse. The docs distinguish code that exists from experiments, stale proposals, and future hardening work.

## Document Guide

### [01-architecture-overview.md](01-architecture-overview.md)

High-level component view of the backend, assistant service, retention service, shared transcript, and AI routing flow.

**Best for:** First-pass system orientation

### [02-system-flow-detailed.md](02-system-flow-detailed.md)

Detailed request path through conversation preparation, guardrails, escalation, agent routing, and response handling.

**Best for:** Following one user message through the system

### [03-escalation-gate-policy.md](03-escalation-gate-policy.md)

Code-grounded escalation policy: classifier output mapping, gate ordering, optional handoff state, outcome escalation, and resolution checks.

- `EscalationSignals` and `EscalationDecision`
- Safety, human-request, abuse, and needs-agent branches
- First-request versus repeat-request behavior
- Redis counters and handoff claims
- Outcome and resolution policy

**Best for:** Explaining deterministic policy around probabilistic classifiers

### [04-ingestion-pipeline.md](04-ingestion-pipeline.md)

The actual ingestion and retrieval architecture, without a fictional model-training pipeline.

- PDF ingestion through FastAPI and Celery
- Structural splitting, micro chunks, and parent macros
- Qdrant child vectors and Redis parent documents
- Raw macro versus generated-summary experiment
- Retrieval cache rollout modes
- Slot and retention-video ingestion paths

**Best for:** RAG ingestion, retrieval quality, and cache decisions

### [05-data-models-api.md](05-data-models-api.md)

Current API and persistence contracts across the backend, assistant, and retention services.

- Assistant query request and response fields
- Retention, chat, and game contracts
- Shared Redis transcript format
- Escalation ledger keys
- Qdrant and Redis data ownership

**Best for:** Integration work and contract review

### [06-architecture-thinking-interview.md](06-architecture-thinking-interview.md)

Interview-facing synthesis of the thinking deduced from ADRs, plans, issues, experiments, commits, and implementation.

- Shared transcript versus a second conversation store
- Signals versus policy decisions
- Retention objective and situation veto
- Memory, ingestion, handoff, game, resolution, and cache changes

**Best for:** Explaining engineering judgment rather than listing components

### [07-multi-tenant-assistant-architecture.md](07-multi-tenant-assistant-architecture.md)

How multiple project-owned assistants and knowledge bases share one deployment while remaining logically isolated.

- Shared API and worker deployments rather than per-assistant pods
- Project, assistant, version, widget, and chat ownership
- Pending-to-published KB lifecycle
- Chat version pinning
- Runtime language, client context, and Jinja/YAML prompt assembly
- Qdrant assistant/version filters and payload indexes
- Cross-tenant, empty-KB, and duplicate-ingestion incidents
- Current authorization, prompt-asset identity, and cleanup hardening gaps

**Best for:** SaaS tenancy, RAG platform design, and system design interviews

### [08-database-storage-architecture.md](08-database-storage-architecture.md)

Where every major data class is stored, how each database is hosted, and which store is authoritative.

- MySQL RDS as the backend and chat transaction store
- Shared Redis transcript, RAG parent macros, policy state, and retention memory
- ClickHouse Cloud chat analytics, AI metrics, and PII audit data
- Qdrant collections for knowledge, cache, games, mined chats, and retention videos
- S3 source files and attachments
- PostgreSQL's actual supporting-service role
- Consistency, recovery, availability, and secret-wired evidence boundaries

**Best for:** Database design, AI data architecture, persistence tradeoffs, and production-readiness interviews

### [09-pii-detection-and-sanitization.md](09-pii-detection-and-sanitization.md)

The actual PII detection and reversible sanitization path across the backend and AI assistant.

- Contextual BAML and Bedrock detector for CPF, PIX, account, payment, identity, and contact data
- Deterministic typed placeholders and request-scoped Redis mappings
- Full-text and chunk-aware SSE restoration
- Metadata-only ClickHouse and Langfuse auditing
- Real-traffic experiment and false-negative history
- Verified raw shared-history boundary and fail-closed gaps

**Best for:** Privacy architecture, AI guardrails, model-boundary design, and incident-driven engineering interviews

## Navigate by Question

| Question | Document |
|---|---|
| How does one user message move through the system? | [Detailed system flow](02-system-flow-detailed.md) |
| When and why is a chat handed to a human? | [Escalation gate policy](03-escalation-gate-policy.md) |
| How are PDFs converted into retrievable context? | [Ingestion pipeline](04-ingestion-pipeline.md) |
| What are the real assistant and retention API fields? | [Data models and API](05-data-models-api.md) |
| How do I explain the overall engineering reasoning? | [Architecture thinking](06-architecture-thinking-interview.md) |
| How do assistants keep separate KBs on shared infrastructure? | [Multi-tenant architecture](07-multi-tenant-assistant-architecture.md) |
| Where are chats, vectors, AI memory, analytics, and files stored? | [Database and storage architecture](08-database-storage-architecture.md) |
| How is PII detected, masked, restored, and audited? | [PII detection and sanitization](09-pii-detection-and-sanitization.md) |

## Verified Vocabulary

### Shared transcript

The backend writes visible chat turns to `message_store:<chat_id>` in Redis. The assistant and retention services read that same chronological ledger rather than maintaining competing conversation histories.

### Escalation signals

The classifier output is normalized into `EscalationSignals`. The categories used by the policy are `safety`, `human_request`, `abuse`, and `needs_agent`, with additional outcome signals such as unanswered context and optional live-support offers.

### Escalation policy

`EscalationPolicy` owns deterministic decisions such as `ESCALATE_NOW`, `ASSIST_THEN_HANDOFF`, `OFFER_THEN_HANDOFF`, and `DEESCALATE`. Classifiers report evidence; they do not directly perform a transfer.

### Memory ledger

`MemoryManager` stores per-chat operational state in Redis, including `frustration_counter`, `abuse_counter`, `optional_handoff_offered`, and `human_request`. These keys have explicit TTLs and support repeat-request and one-time-offer behavior.

### Assistant knowledge partition

The backend owns a project-scoped assistant and its versions. The AI retriever searches a shared Qdrant collection with both `assistant_id` and `version_id` filters. A chat stores the version it started with.

### Two retention paths

- Proactive: the backend calls retention `/v1/retention` for a lifecycle trigger.
- Reactive: the assistant calls retention `/v1/chat` when a user continues a retention conversation.

Both paths can reconstruct context from the shared transcript.

## Evidence Boundary

The current repositories do not support claims of:

- a Kafka or EventBridge conversation collector for these flows;
- a data-warehouse-to-model-registry training pipeline;
- a checked-in `config/escalation.yaml` controlling the policy;
- a fine-tuning loop for escalation classifiers;
- one Kubernetes deployment or vector collection per assistant;
- invented `ConversationEvent`, `EscalationPolicyEngine`, or `collect_safety_signals` implementations.

Experiments and proposals are useful evidence of thinking, but they are identified as such and are not presented as current runtime behavior.

## Repository Evidence

The principal code roots used by these documents are:

```text
/Users/sandipan/slotsense/slotsense-backend
/Users/sandipan/slotsense/slotsense-ai-assistant-new
/Users/sandipan/slotsense/slotsense-rnd-retention-ai
/Users/sandipan/slotsense/slotsense-helm-charts
/Users/sandipan/slotsense/slotsense-infrastructure
```

Each detailed document ends with code anchors for the behavior it describes.
