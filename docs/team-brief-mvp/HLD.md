# Async Team Coordination — high-level design

Version 0.1 · 6 October 2026 · Proposed architecture

Product requirements: [PRD v0.2](PRD.md). This document describes a system to build, not a deployed product or Supabase's internal implementation. It replaces the architectural baseline in the earlier reporting-only implementation plan. That plan still needs a separate rewrite.

## 1. What the system does

The platform helps employees answer three everyday questions: What changed? What can I use now? What still needs someone's decision?

It brings together permitted evidence from Slack, Jira, Confluence and repositories. Agents answer questions, prepare briefs and identify missing context. When a person is needed, they receive a focused question rather than another broad request for an update.

People keep authority over commitments. An agent can explain an existing owner, deadline or status. It cannot choose and write a new one into a shared work system.

The first pilot serves two engineering/product teams in one company. Each customer gets an isolated deployment. Reporting and Q&A go live first, while narrow drafting, linting, triage and observer agents prove the shared platform works across different jobs.

## 2. Architecture at a glance

```text
EMPLOYEES AND AGENT AUTHORS

 Slack / repository client / browser review UI
                      |
                      v
             API and identity checks
                      |
         +------------+-------------------+
         |                                |
         v                                v
 AGENT CONTROL                      WORK EXECUTION
 Define -> validate                 Request / event / schedule
 -> compile -> evaluate                   |
 -> approve -> register                   v
         |                         Durable inbox + outbox
         v                                |
 Versioned packages                       v
 and deployment inventory          Temporal task queues
         |                                |
         +---- approved version ----------+
                                          v
                                  Python agent workers
                                          |
                    +---------------------+------------------+
                    v                     v                  v
             Read broker            Model gateway     Review / contact
             + permission           + provider        requests
             checks                 adapters                |
                    |                                       v
                    v                               Policy + exact consent
          Slack / Jira / Confluence                         |
          / approved repository                             v
                                                    Isolated executor
                                                           |
                                                           v
                                                    Narrow external write

 SHARED RECORDS
 Postgres: definitions, grants, evidence metadata, consent, receipts
 Object storage: protected evidence and complete trace payloads
 BigQuery: run history, audit index, work ledger, team metrics
```

The boxes describe responsibilities. Most application logic stays in one Python codebase. Deployment separation is reserved for different trust levels: the worker, read broker, model gateway and write executor have different identities and credentials.

## 3. Main decisions

| Decision | Choice and reason | Trade-off |
|---|---|---|
| Customer boundary | One isolated company deployment for the MVP | More infrastructure per customer, simpler isolation and incident containment |
| Application | Python/FastAPI API, small browser UI, typed workflow templates | New workflow types need engineering review |
| Durable runtime | Temporal with Python workers; managed Temporal service by default | Adds a service and operational model; region and data-processing terms need approval |
| Agent reasoning | Bounded steps using a model gateway and provider adapters | Less flexibility than arbitrary agent code; easier to test and control |
| Operational database | Cloud SQL for PostgreSQL | Must manage migrations, connections and recovery drills |
| Evidence and traces | Encrypted object storage with restricted access | Requires retention and deletion across several stores |
| Analytics | BigQuery, fed asynchronously from the audit outbox | Metrics can lag; it never grants authority or drives recovery |
| Search | Scoped structured retrieval and Postgres full-text search first | Add semantic retrieval only when measured relevance requires it |
| Deployment | GCP, Terraform, managed Kubernetes for long-running workers and services | Kubernetes has operational cost; use a small set of deployments |
| Tool protocol | Typed internal adapters; narrow MCP interface for repository clients | MCP adds an access surface and must use the same policies |

Temporal's Python SDK exposes workflows, activities and workers. We use that execution model; model calls and provider I/O belong in activities, outside deterministic workflow logic. [Temporal Python documentation](https://docs.temporal.io/develop/python).

Temporal is the selected runtime for this design. A short implementation spike must prove crash recovery, review resumption and worker upgrades before real company data is enabled. If managed hosting is disallowed, revisit hosting through a recorded architecture decision rather than silently substituting an in-memory runner.

## 4. Components and their responsibilities

| Component | Owns | Must not do |
|---|---|---|
| API and identity layer | Login, verified company/user context, signed webhooks, review forms | Trust a company ID or reviewer identity supplied by the model |
| Registry and compiler | Definitions, versions, validation, release manifests, deployment inventory | Install arbitrary tools or execute model-generated code |
| Policy module | Source scope, effective permissions, tool grants, risk tier, review rules | Let model text override a denial |
| Runtime workers | Registered workflow steps, bounded reasoning, structured outputs | Hold provider write tokens or update consent records |
| Read broker | Scoped retrieval, source versions, access checks, connector health | Treat an integration's broad access as the user's access |
| Model gateway | Approved models, provider credentials, request limits, usage records | Decide action authority |
| Review and contact service | Immutable revisions, human-authored submissions, consent, recipient budgets | Convert approval into unrestricted write access |
| Action executor | Exact permitted effect, fresh checks, delivery journal, reconciliation | Accept arbitrary URLs, API methods or Jira fields |
| Audit exporter and observer | Export complete run records; detect failures, drift and missing ownership | Change grants, grading rules or its own deployment |

The policy module is shared code, enforced independently by the read broker and executor. The worker cannot mark its own request as authorized. Database roles and network restrictions reinforce this separation.

## 5. Define, compile and distribute an agent

An agent definition contains its purpose, accountable owner, workflow template, risk tier, allowed sources/tools, model configuration, output schema, review rules, contact policy and evaluation suite. References identify approved resources; they do not contain credentials.

```text
Version-controlled definition
           |
           v
Validate schema, owner, references and forbidden capabilities
           |
           v
Compile into an immutable manifest + context/tool references
           |
           v
Run behavioral, permission and recovery evaluations
           |
           v
Release approval -> signed package hash -> active registry entry
           |
           +-------------------+-------------------+
           v                   v                   v
      Chat commands      Repository package    Runtime workers
           |                   |                   |
           +---- resolve and verify active version-+
```

Compilation means resolving approved templates and dependencies into a reproducible package. It does not mean generating arbitrary Python. The package pins prompt, tool schema, context, evaluation and model configuration versions. Each deployment records both desired and observed package versions.

A repository package supplies reviewed instructions, scoped context references and MCP tool definitions. Sensitive source material is fetched at use time. Packages contain no provider tokens. Central checks reject a revoked version even if a repository has an old copy. Distribution cannot make a local developer tool trustworthy; the server still authenticates each request and limits each capability.

MCP is an interface, not a permission shortcut. Its transport authorization identifies access to the server; our application must still enforce resource and action policy. Pin and test the supported protocol revision. [MCP authorization specification](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization).

## 6. End-to-end employee workflows

### A. Answer a question

Maya asks: “Can the frontend use API v2 in staging?”

1. The API verifies Maya and the destination audience. It stores a request and outbox event in one transaction.
2. The dispatcher starts a workflow with a stable request ID and approved agent version. Repeated delivery resolves to the same logical run.
3. The broker retrieves allowed Jira, Slack and Confluence evidence. It records source revisions, coverage and access context.
4. The model produces structured claims with source references, uncertainty and any missing information. Retrieved text is data, never authority to change tools or policy.
5. Validators check the schema, source references, audience and required safety conditions. Quality checks assess support for claims; a model judge cannot grant access.
6. The delivery path rechecks disclosure permission and returns the answer. If a channel audience cannot be verified, use a private authorized view.
7. Missing deployment evidence becomes an explicit uncertainty. A clarification is prepared separately and must pass contact policy before sending.

The response can say implementation was reported complete while deployment is unconfirmed. It cannot turn those signals into a “Done” Jira update.

### B. Prepare and publish a team brief

A schedule creates a run for a specific team and reporting interval. The reporting agent gathers permitted changes and produces an immutable brief revision. The configured reviewer sees its evidence, missing coverage and intended audience.

Approval binds to the exact revision and destination. Editing the brief invalidates that approval. The executor checks current access and publication rules before delivery. A channel receives content only if the source permissions support that audience; otherwise it receives a neutral link to an authenticated view.

Reporting uses the same registry, runtime, evidence broker and action journal as Q&A. It is one workflow on the platform.

### C. Carry a human-authored update

```text
Ravi enters exact comment in authenticated form
                     |
                     v
Store immutable submission + author + target + payload hash
                     |
                     v
Ravi consents to that exact submission
                     |
                     v
Executor checks consent, access, expiry and allowed operation
                     |
                     v
Claim logical action + record send intent durably
                     |
                     v
Add comment to Jira API-142
                     |
             +-------+----------------+
             v                        v
      Confirmed receipt         Outcome unknown
             |                        |
             v                        v
       Mark delivered           Reconcile; no blind resend
```

The initial write contract is `add_human_comment(submission_id)`. The executor loads the trusted submission; it does not accept model-supplied comment text. Jira owner, due-date and status mutation operations do not exist in this interface.

Human authorship is established through an authenticated, human-controlled submission and explicit attestation. This proves who submitted the text, not whether they composed it without outside help. The system must not claim it can detect copied AI text. A generated draft has different provenance and cannot be automatically promoted into this transfer path.

## 7. Make the authority boundary enforceable

```text
AGENT WORKER
  Can: ask for scoped evidence, generate a draft, request review
  Cannot: read write secrets, modify consent, call provider writes
       |
       v
NARROW ACTION SERVICE
  Checks trusted submission / approved output and current policy
  Accepts registered operations only
       |
       v
ISOLATED CONNECTOR
  Holds provider credential; constructs the exact API request
  Exposes no generic HTTP proxy and no arbitrary field updater
```

Enforce this using separate workload identities, database roles, service authentication and default-deny network egress. Model traffic goes through the model gateway; provider reads and writes go through their respective brokers. Network policy must be tested against direct internet access, redirects and alternate endpoints, not merely documented.

If a provider requires a broad write token, only the isolated executor can access it. Agent workers cannot enqueue executable writes by directly editing action or consent tables. They can submit proposals through validated APIs. Only the human review path can record human consent.

The hard guarantee concerns autonomous system operations. Textual reports also need grounding and review so they do not invent commitments, but no architecture can guarantee the meaning of arbitrary prose through a permission check alone. Model-generated reports use separate, destination-scoped publication operations and never enter commitment-field update paths.

Risk, authority and interruption budget are separate checks. Higher risk does not grant more autonomy. External-facing publication is disabled in the pilot. Platform operators can pause an agent, revoke a grant or disable all external writes; the model cannot reverse those decisions.

## 8. Evidence, search and permissions

Each connector ingests approved events or polls within a bounded scope. It handles pagination, edits, deletions, source revisions and provider limits. Webhook ingestion durably records an event before acknowledging it. Provider event IDs and payload hashes help reject replays and duplicates.

Search is constrained by company, source scope and current user permissions before evidence reaches the model. Start with issue IDs, linked documents, thread relationships, time windows and full-text search. Store evidence references and source versions so an answer can be inspected later.

Permissions are checked again before disclosure. A past snapshot or successful ingestion is not proof of current access. Shared briefs use an explicit, verifiable audience. Unknown membership, inherited restrictions or failed access checks block disclosure. For the pilot, start with selected internal spaces and channels; exclude guests and externally shared channels.

A connector spike must establish how effective user access is verified for each provider. Until that works, use synthetic data or explicitly approved common-access sources. Do not silently substitute a privileged service account.

Access revocation invalidates retrieval caches and prevents future reads and disclosure. Cached answers retain their evidence dependencies and require authorization on reuse. Deletions produce tombstones and trigger retention processing. Previously delivered content cannot be recalled from someone's memory or screenshots.

## 9. Durable execution and data ownership

Temporal owns workflow progression, timers and waiting for review. Postgres owns product authority: active grants, immutable submissions, approvals, action receipts and contact reservations. The workflow's cached state never overrides those records.

All external I/O happens in bounded activities. Results are saved before dependent steps continue. Model retries may produce different text; save the chosen output as an immutable revision and never regenerate it under an existing approval.

Use stable IDs at each boundary:

- Request/event ID for workflow creation.
- Run and step ID for accepted model results and checkpoints.
- Revision hash for content and evidence dependencies.
- Logical action ID for every attempted external effect.
- Audit event ID for repeat-safe warehouse export.

Postgres transactions pair a state change with its outbox record. Dispatchers retry until acknowledged. No distributed transaction is assumed between Postgres, Temporal, BigQuery or external tools. A reconciliation worker compares pending outbox entries, workflow IDs and receipts to repair gaps.

```text
QUEUED -> RUNNING -> VALIDATING -> COMPLETED (permitted private answer)
                         |
                         v
                  WAITING_FOR_REVIEW
                         |
                         v
                      READY -> EXECUTING -> COMPLETED
                                    |
                                    v
                              OUTCOME_UNKNOWN
                                    |
                                    v
                               RECONCILING

Other terminal states: BLOCKED, REJECTED, EXPIRED, CANCELLED, FAILED
```

Human waiting does not occupy a worker process. Review submission is durably stored before a resume signal is sent. Duplicate signals are harmless because workers reload the authoritative revision and consent.

A database claim prevents concurrent executors from owning the same action. A provider idempotency key is used where supported. When a timed-out write may have succeeded, do not let a worker lease expiry trigger a new send: quarantine the action and reconcile using provider receipts or bounded lookup. If the outcome cannot be established, require operator resolution. Exactly-once delivery is not promised where the provider cannot support it.

## 10. Core records

| Record | Purpose |
|---|---|
| Principal / IntegrationGrant | Verified user, company, provider identity, permitted sources and secret reference |
| AgentVersion / Deployment | Immutable manifest, owner, evaluations, active status and observed surface versions |
| SourceVersion / EvidenceSnapshot | Source revision, protected content reference, access metadata and provenance |
| Run / StepResult | Workflow ID, pinned versions, accepted results, coverage, time and cost |
| OutputRevision / Claim | Immutable text, source dependencies, fact/inference labels and hash |
| HumanSubmission / Consent | Human-controlled text, identity, target, operation, hash, expiry and revocation |
| Action / Attempt / Receipt | One logical effect, send history, confirmed result or uncertain outcome |
| ContactReservation | Recipient, policy window, budget reservation and delivery outcome |
| AuditEvent / Outbox | Durable decision history and pending dispatch/export |
| Feedback / WorkLedger | Corrections, measured human effort, baseline and benefit assumptions |

Company context is derived from authenticated identity. IDs alone never authorize access. Append-only audit records use restricted writer roles and protected export; calling a table append-only does not make it tamper-proof against privileged administrators.

## 11. Contact budgets across agents

Before proactive contact, the service checks existing questions, recipient timezone, quiet hours and whether the missing information affects real work. It combines related questions when useful.

Budget reservations are atomic in Postgres and shared across all agents for the same recipient and policy window. A scheduled send rechecks the current budget and working hours immediately before execution. Confirmed sends consume the reservation; confirmed unsent cancellations release it. Unknown outcomes keep it reserved until reconciled.

User-requested replies have their own rate limits. An agent cannot label a message urgent to bypass policy. The pilot measures helpful contacts and interruptions, rather than rewarding message volume.

## 12. Deployment and operations

```text
One customer GCP project / selected region
 |
 +-- HTTPS entry: identity-aware UI/API and signed provider callbacks
 +-- Managed Kubernetes
 |     +-- API / registry / review service
 |     +-- Dispatcher and Temporal workers
 |     +-- Read broker and model gateway (separate identities)
 |     +-- Action executor (separate identity and network policy)
 |     +-- Audit exporter / observer
 +-- Cloud SQL Postgres, private connectivity, HA and PITR
 +-- Protected object storage and Secret Manager
 +-- BigQuery restricted datasets
 +-- Telemetry, alerts and operator runbooks
 |
 +-- Managed Temporal endpoint
 +-- Approved model and source providers through controlled egress
```

Use Terraform for infrastructure, versioned containers, separate staging/production identities and compatible database migrations. Keep the deployment small; these identities do not require separate repositories or independently managed product teams.

Regional Cloud SQL HA protects against some infrastructure failures; it does not replace backups or regional disaster recovery. Test restoration explicitly. [Cloud SQL HA documentation](https://docs.cloud.google.com/sql/docs/postgres/high-availability).

Proposed pilot objectives, to validate under representative load:

| Objective | Proposed target / boundary |
|---|---|
| Interactive answer | P95 under 30 seconds for bounded questions with healthy sources; show progress and partial coverage otherwise |
| API availability | 99.5% monthly service objective, with provider-dependent completion tracked separately |
| Database disaster recovery | RPO at most 15 minutes and RTO at most 4 hours, demonstrated by restore drills |
| Audit export | Under 5 minutes during healthy operation; durable local backlog during warehouse outage |
| Safety | All deterministic authorization and forbidden-action tests pass before release |

These are design targets, not measured performance or customer guarantees. Size the pilot using active users, questions per day, evidence per run and provider quotas. Separate interactive and batch task queues so briefs cannot starve questions. Bound tokens, concurrency, retries and per-company daily model spend.

## 13. Audit, evaluation and the observer

Record input, context versions, prompts, model responses, tool calls, policy decisions, human review, effects, errors and cost under one run ID. Restrict sensitive payloads in object storage and expose a complete warehouse index with protected payload references. Authorized investigators can reconstruct the run; broad analytics readers see only permitted fields. Temporal history carries identifiers and minimal payloads, not unnecessary copies of private source text.

Export through the transactional outbox with stable event IDs. Warehouse failure must not lose the local record. If the operational audit store cannot persist an action intent, block the effect. Define retention for source snapshots, model traces, workflow histories, backups and analytics together; after lawful deletion, reconstruction may intentionally be incomplete and must say so.

Every release includes versioned golden examples, behavioral assertions, written rubrics and permission/recovery tests. Calibrate model judges against human labels. Run deterministic safety checks on every execution; apply deeper quality checks according to risk. Model or prompt changes require evaluation again.

The observer reads approved operational views. It can flag stale packages, failures, missing owners or recurring corrections and propose a reviewable fix. It cannot deploy changes, edit consent or weaken a test threshold.

The work ledger links completed workflows to human effort and comparable baselines. Monthly benefit reports state assumptions and avoid double-counting reused answers. A query-backed team maturity view measures ownership, evaluated use and operating practices. Teams can inspect and dispute its evidence; it is not an individual productivity score.

## 14. Failure behavior and rollback

| Failure | Required behavior |
|---|---|
| One source unavailable or rate-limited | Retry within bounds; label coverage; never imply a complete answer |
| Model timeout or invalid result | Bounded retry or fail visibly; no side effect from an unvalidated result |
| Worker crashes | Resume workflow and reuse accepted results; reconcile unfinished effects |
| Access revoked after drafting | Block disclosure or execution at the fresh check |
| Review edited, expired or withdrawn | Invalidate consent; require a new exact revision review |
| External write times out | Mark outcome unknown; reconcile before retry |
| Warehouse unavailable | Keep durable audit backlog and alert on age |
| Bad agent release | Disable its active version; stop new runs and block pending effects |
| Database restored to earlier point | Pause writes; reconcile Temporal and provider receipts before resuming |

Internal changes within one Postgres transaction roll back atomically. A release pointer can atomically switch back to a prior approved package; already-running workflows require explicit cancellation or compatible continuation. Each activity rechecks revocation before accessing data or acting.

External rollback is operation-specific. Deleting a published message is a new authorized action and does not erase prior disclosure. A compensating update is not an atomic undo. The Jira comment pilot must document whether deletion is permitted and who can authorize it. Never advertise all-provider atomic rollback.

Revocation prevents future permitted execution after its check. A provider request already in flight may still complete; record and reconcile it rather than claiming cancellation can recall the request.

## 15. Build sequence and acceptance

| Slice | Demonstration |
|---|---|
| 1. Shared foundation | Register and compile a Q&A definition; reject missing ownership and forbidden tools |
| 2. First useful answer | Read scoped evidence, show sources and uncertainty, survive a worker restart |
| 3. Reporting and review | Generate a brief, review an exact revision, block changed or expired approval |
| 4. Human transfer and contact | Record one human-authored Jira comment; enforce shared recipient budget under concurrency |
| 5. Portfolio and distribution | Run narrow drafting, linting, triage and observer workflows; distribute and revoke chat/repository packages |
| 6. Production pilot | Reconstruct runs, restore data, reconcile uncertain writes and compare coordination effort with baseline |

Safety, evaluation and audit controls are built alongside each slice. Completion requires the twelve platform MVP gates in the PRD, not just a successful demo. The earlier reporting-only delivery estimate remains withdrawn.

Before implementation, resolve these customer-dependent details: provider identity/access mapping; first permitted write and its reconciliation contract; hosting/data-residency approval; repository host; model provider; contact budgets; retention and numeric pilot capacity. Record deviations from this HLD as architecture decisions.

## 16. PRD coverage

| PRD requirement | Design location |
|---|---|
| Reduce async coordination work | Employee flows (6), contact budgets (11), work ledger (13) |
| Agent portfolio and compiler | Components (4), release/distribution (5), delivery gates (15) |
| Governance and human authority | Human transfer (6), enforceable boundary (7), permissions (8) |
| Headless durable runtime | Runtime decision (3), durable execution (9) |
| Inventory integrity and chat/repository distribution | Versioned packages (5), core records (10) |
| Complete logging, evaluations and meta layer | Audit and observer (13) |
| Recovery and rollback | Execution journal (9), operations (12), failure behavior (14) |

The ASCII mockups in the [PRD](PRD.md#5-what-employees-experience) show the employee experience. This HLD explains the services and records that make those screens trustworthy. Detailed endpoint schemas, table DDL, connector contracts and deployment manifests belong in the subsequent low-level design.
