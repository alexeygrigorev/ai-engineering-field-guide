# AI System Design Guide Integration

This document explains how to use the local `ai-system-design-guide` repository
with this field guide and the production examples in `~/slotsense`.

It is a preparation map, not a second question bank. The external repository
stays separate so it can be updated independently.

Source snapshot used for this integration:

- repository: `../ai-system-design-guide/`
- commit: `3d391f62635922923eecf66014522a955cab5236`
- snapshot date: 2026-08-15

## What each repository is responsible for

```text
ai-engineering-field-guide
  market evidence, role strategy, portfolio decisions, preparation schedule

ai-system-design-guide
  system-design explanations, question bank, answer frameworks, exercises

~/slotsense
  production patterns, incidents, evaluations, deployment evidence, and decisions
```

Keep the boundaries clear:

- The field guide remains the source for the 6,964-job analysis and your job
  search decisions.
- The system-design guide is a study reference and question generator. Its
  market chapter is useful qualitative context, but it does not replace the
  field guide's dataset.
- SlotSense is the current production-example source. Use its code and reports
  to study decisions and failure modes, while distinguishing personal
  contribution from repository history.

## SlotSense production-example index

Start with these paths when an interview topic needs a real example:

| Interview topic | SlotSense material |
|---|---|
| RAG ingestion and retrieval | `~/slotsense/slotsense-ai-assistant-new/docs/ingestion_retrieval_improvements.md`, `docs/bug_missing_docs_chunks_collection.md` |
| Observability and trace context | `~/slotsense/slotsense-ai-assistant-new/docs/langfuse_observability_and_rag_fixes.md` |
| PII and privacy boundaries | `~/slotsense/slotsense-ai-assistant-new/docs/pii_filtering_feature_report.md`, `docs/bug_pii_false_negatives.md` |
| Speculative execution and streaming | `~/slotsense/slotsense-ai-assistant-new/docs/PRs/PR-87-Parallel-Guardrails.md`, `docs/speculative-rag-flush-gate.md` |
| Caching decisions | `~/slotsense/slotsense-ai-assistant-new/docs/cache-shadow-experiment-proposal.md`, `docs/cache-historical-metrics-investigation-report.md`, `docs/adr/0004-retrieval-context-cache-not-response-replay.md` |
| Agent boundaries and escalation | `~/slotsense/slotsense-ai-assistant-new/docs/signals-not-decisions.md`, `docs/adr/0007-agents-signal-offers-service-renders-them.md` |
| Retention and event workflows | `~/slotsense/slotsense-rnd-retention-ai/docs/architecture.md`, `docs/retention_logic.md` |
| Evaluation and judging | `~/slotsense/slotsense-qa-eval/README.md`, `QA_GUIDE.md`, and the evaluation reports |
| Telemetry analysis | `~/slotsense/clickhouse-analysis/REPORT.md`, `ESCALATION_ANALYSIS.md`, and `INVENTORY.md` |
| Helm and Kubernetes | `~/slotsense/slotsense-helm-charts/` |
| Terraform and Argo CD | `~/slotsense/slotsense-infrastructure/`, `~/slotsense/slotsense-argocd-image-updater/` |
| CI/CD workflows | `~/slotsense/slotsense-cicd-centralized-workflows/` |

Use the repository code and reports to answer: what was the problem, what did
the evidence show, what alternative was rejected, what changed, and what risk
remains. Do not present a design note as a production result unless the source
clearly shows that it was implemented and measured.

## The preparation loop

Use every question to understand a production decision, then use a SlotSense
example to practice explaining it.

```text
question from reference guide
          |
          v
answer using the SPIDER structure
          |
          v
find the matching SlotSense example
          |
          v
trace the code, incident, evaluation, or deployment evidence
          |
          v
save evidence and a decision
          |
          v
practice the answer again with specific production facts
```

For each question, write only five things:

1. The requirement or decision.
2. The architecture diagram.
3. The most important trade-off.
4. One failure mode and fallback.
5. The measurement or test that would decide whether it works.

Do not read all 128 questions linearly. Use the routes below.

## Priority route for this job search

### Route A - Product and AI system design

Use this before deep infrastructure study. It matches the primary Applied or
Product AI direction for the portfolio.

1. [Answer frameworks](../../../ai-system-design-guide/00-interview-prep/02-answer-frameworks.md)
2. [Question bank: core questions](../../../ai-system-design-guide/00-interview-prep/01-question-bank.md)
3. [Whiteboard: enterprise RAG](../../../ai-system-design-guide/00-interview-prep/04-whiteboard-exercises.md)
4. [RAG fundamentals](../../../ai-system-design-guide/06-retrieval-systems/01-rag-fundamentals.md)
5. [Production RAG](../../../ai-system-design-guide/06-retrieval-systems/14-production-rag-at-scale.md)
6. [Multi-tenant SaaS case study](../../../ai-system-design-guide/16-case-studies/08-multi-tenant-saas.md)
7. [Customer-support automation case study](../../../ai-system-design-guide/16-case-studies/09-customer-support-automation.md)

Practice prompt:

> Design a multi-tenant support AI system that retrieves trusted knowledge,
> protects customer data, handles ambiguity, and escalates safely.

Use the SlotSense assistant, retrieval, privacy, and escalation examples to
make the answer concrete rather than leaving it as a generic exercise.

### Route B - RAG, data, and retrieval quality

Use this while studying the SlotSense ingestion and retrieval paths.

1. [Chunking strategies](../../../ai-system-design-guide/06-retrieval-systems/02-chunking-strategies.md)
2. [Embedding models](../../../ai-system-design-guide/06-retrieval-systems/03-embedding-models.md)
3. [Vector databases](../../../ai-system-design-guide/06-retrieval-systems/04-vector-databases.md)
4. [Hybrid search](../../../ai-system-design-guide/06-retrieval-systems/05-hybrid-search.md)
5. [Reranking](../../../ai-system-design-guide/06-retrieval-systems/06-reranking-strategies.md)
6. [RAG evaluation patterns](../../../ai-system-design-guide/06-retrieval-systems/13-rag-evaluation-patterns.md)
7. [Data engineering for AI](../../../ai-system-design-guide/06-retrieval-systems/15-data-engineering-for-ai.md)
8. [RAG production questions](../../../ai-system-design-guide/00-interview-prep/01-question-bank.md)

Project exercise:

```text
Take one production retrieval question.
  -> trace ingestion, chunking, embedding, and retrieval
  -> identify the tenant, assistant, version, and locale filters
  -> find the telemetry that proves what context was retrieved
  -> deliberately remove one isolation key in a local test
  -> explain the failure and the recovery
```

### Route C - Agents, tools, MCP, and human approval

Use this while studying SlotSense agent boundaries, signals, state, and
retention workflows.

1. [Agent fundamentals](../../../ai-system-design-guide/07-agentic-systems/01-agent-fundamentals.md)
2. [Tool use and MCP](../../../ai-system-design-guide/07-agentic-systems/03-tool-use-and-mcp.md)
3. [Error handling and recovery](../../../ai-system-design-guide/07-agentic-systems/07-error-handling-and-recovery.md)
4. [Human-in-the-loop patterns](../../../ai-system-design-guide/07-agentic-systems/08-human-in-the-loop-patterns.md)
5. [Agent security and sandboxing](../../../ai-system-design-guide/07-agentic-systems/09-agentic-security-and-sandboxing.md)
6. [Agent evaluation](../../../ai-system-design-guide/07-agentic-systems/10-evaluating-agentic-systems.md)
7. [Durable execution](../../../ai-system-design-guide/07-agentic-systems/11-durable-execution.md)
8. [MCP knowledge-agent case study](../../../ai-system-design-guide/16-case-studies/20-mcp-knowledge-agent.md)

Project exercise:

```text
Agent or model signal -> deterministic service decides -> state changes safely
```

Draw the same flow with an LLM outage, a malformed tool result, a replayed
approval, and untrusted retrieved content. The model must not gain authority in
any of those branches.

### Route D - Evals and observability

Use this throughout interview preparation. SlotSense provides concrete eval,
trace, telemetry, and failure examples for explaining production AI quality.

1. [LLM evaluation](../../../ai-system-design-guide/14-evaluation-and-observability/01-llm-evaluation.md)
2. [Observability](../../../ai-system-design-guide/14-evaluation-and-observability/02-observability.md)
3. [Eval-gated CI/CD case study](../../../ai-system-design-guide/16-case-studies/18-eval-gated-cicd.md)
4. [Evaluation pipeline whiteboard exercise](../../../ai-system-design-guide/00-interview-prep/04-whiteboard-exercises.md)
5. [Comprehensive eval study guide](../../../ai-system-design-guide/ai_evals_comprehensive_study_guide.md)

Project exercise:

- Read one SlotSense eval or incident report and identify the failure owner.
- Separate retrieval, prompt, model, workflow, and infrastructure failures.
- Trace one user turn through request handling, retrieval, model calls, and
  telemetry.
- Explain how an eval or release check would prevent recurrence.

### Route E - Delivery and AI platform reliability

Use this with the SlotSense deployment and infrastructure repositories, so
infrastructure answers have a real system behind them.

1. [LLM infrastructure](../../../ai-system-design-guide/11-infrastructure-and-mlops/01-llm-infrastructure.md)
2. [CI/CD for AI](../../../ai-system-design-guide/11-infrastructure-and-mlops/02-cicd.md)
3. [AI gateways and model routing](../../../ai-system-design-guide/11-infrastructure-and-mlops/03-ai-gateways-and-model-routing.md)
4. [FinOps and token economics](../../../ai-system-design-guide/11-infrastructure-and-mlops/04-finops-and-token-economics.md)
5. [Reliability patterns](../../../ai-system-design-guide/13-reliability-and-safety/03-reliability-patterns.md)
6. [Multi-tenant isolation questions](../../../ai-system-design-guide/00-interview-prep/01-question-bank.md)

Project exercise:

```text
GitHub Actions -> image digest -> Git desired state -> Argo CD -> Helm -> EKS
                                                    |
                                                    +--> rollback
```

Explain why Terraform creates infrastructure, GitHub Actions verifies and
publishes artifacts, Helm packages workloads, and Argo CD reconciles runtime
state.

## SlotSense evidence-to-question mapping

| SlotSense evidence area | Interview capability | Reference material |
|---|---|---|
| Assistant request and agent state | Trace a multi-step AI request | Agent chapters, answer frameworks |
| Ingestion and retrieval fixes | Data pipelines and RAG reliability | RAG chapters, data engineering |
| Tenant, assistant, version, and locale keys | Permission-aware multi-tenant retrieval | Access-control and multi-tenant case |
| Signals versus decisions | Tool use, state, recovery, and authority | Agent chapters |
| QA eval runner and judged suites | Quality definition and regression gates | Eval chapters and case study |
| Langfuse, ClickHouse, Loki, and Grafana | Diagnose model, data, and platform failures | Observability chapters |
| Helm, Terraform, Argo CD, and CI workflows | Production delivery and rollback | CI/CD and infrastructure chapters |
| PII redaction and audit paths | Privacy, trust boundaries, and reversible transformations | Security and reliability chapters |
| Retention triggers and deduplication | Event-driven product workflows | Agent and reliability chapters |

## A repeatable weekly preparation session

Use one session for one SlotSense-backed interview answer:

```text
10 min  choose one question and clarify requirements
15 min  draw the architecture from memory
10 min  explain one deep dive and one trade-off aloud
10 min  add one failure, metric, or eval
10 min  connect it to a SlotSense file, trace, report, or commit
 5 min  write the answer in the interview log
```

The output is not a summary of the chapter. It is a one-page answer with a
diagram, a decision, a failure mode, and a concrete SlotSense reference.

## What to skip for now

The source guide is broad. Defer these until a target job requires them:

- training a foundation model from scratch;
- advanced GPU kernel and accelerator fleet design;
- every agent framework comparison;
- multimodal, voice, and computer-use systems;
- multi-agent orchestration before one bounded workflow is reliable;
- detailed model-price comparisons before the LLM gateway exists;
- memorising changing model names, prices, or market claims.

Read them when a job description or interview loop makes them relevant. Your
current artifact earns more signal from a measured RAG, eval, safety, and
recovery story.

## Market analysis and hiring sources

Keep market analysis separate from interview study.

### Quantitative source

Use this field guide's [role and skill analysis](../../role/02-skills.md) and
[responsibility analysis](../../role/03-responsibilities.md) for counts,
frequencies, and portfolio priorities. Refresh it through the existing
`job-market/` pipeline rather than mixing another guide's numbers into it.

### Qualitative source

Use the source guide's [August 2026 job-market chapter](../../../ai-system-design-guide/00-interview-prep/06-job-market-trends-2026.md)
for role vocabulary, interview formats, and themes such as Applied AI,
Forward Deployed Engineer, evals, AI reliability, agent infrastructure, and
MCP integration. Treat its claims as dated notes, not a live vacancy feed.

### Places to verify live hiring

The source guide points to useful starting points:

- [Anthropic careers](https://www.anthropic.com/careers)
- [OpenAI careers search](https://openai.com/careers/search/)
- [OpenAI applied evals](https://openai.com/careers/software-engineer-applied-evals-san-francisco/)
- [OpenAI agent infrastructure](https://openai.com/careers/software-engineer-agent-infrastructure-san-francisco/)
- [Anthropic roles on Greenhouse](https://job-boards.greenhouse.io/anthropic/jobs/4985877008)
- [Descope MCP engineering role](https://careers.descope.com/p/fe57f6224769-mcp-model-context-protocol-software-engineer)
- [Levels.fyi AI and ML role data](https://www.levels.fyi/t/software-engineer/focus/ml-ai)

Use these as source categories, not as an endorsement that a specific role is
open today. When applying, verify the current posting, location, seniority,
work authorization, and closing date on the company's own career page.

### How to connect market evidence to preparation

Once per week:

1. Select three target postings from the field guide's job pipeline or an
   official company career page.
2. Extract repeated responsibilities and required skills.
3. Map them to one Route A-E topic above.
4. Add one question to the interview log.
5. Add one missing proof item to your interview story bank or portfolio.

This keeps the preparation responsive to hiring demand without letting daily
market changes rewrite the product architecture.

## Updating the external reference

The source repository is a separate Git checkout. Update it deliberately:

```bash
cd ../ai-system-design-guide
git pull --ff-only origin main
git log -1 --format='%H %ad %s' --date=iso
```

After an update, review these files first:

- `00-interview-prep/01-question-bank.md`
- `00-interview-prep/02-answer-frameworks.md`
- `00-interview-prep/04-whiteboard-exercises.md`
- `00-interview-prep/06-job-market-trends-2026.md`
- `14-evaluation-and-observability/`
- `16-case-studies/`

Then update the snapshot commit and date at the top of this document. Do not
copy the entire source repository into the field guide and do not describe a
reference chapter as personal experience.
