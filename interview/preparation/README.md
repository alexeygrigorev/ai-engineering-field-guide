# Interview Preparation Hub

Use this page when you sit down to prepare. Pick a category, answer a
question, check the reference answer, and practice the weak part.

The detailed curriculum is kept separately in
[DETAILED-CURRICULUM.md](DETAILED-CURRICULUM.md). You do not need to open it
during a normal practice session.

For the supplied FDE bank, use the [complete 99-question walkthroughs](14-fde-complete-question-walkthroughs-01-99.md): explanations, ASCII diagrams, worked scenarios, trade-offs, follow-ups, and spoken answers. The [detailed coding and customer-case edition](13-fde-practical-coding-and-cases-79-99.md) covers questions 79–99 separately.

## Categories

| Priority | Category | Topics | Question bank | Answer references |
|---|---|---|---|---|
| 1 | AI foundations | LLMs, tokens, embeddings, attention, structured output, model choice | [Theory questions](../questions/01-theory.md) | [LLM foundations](../../../ai-system-design-guide/01-foundations/), [LLM engineering](../../../ai-engineering-from-scratch/phases/11-llm-engineering/) |
| 2 | RAG and data | ingestion, chunking, embeddings, Qdrant, hybrid search, reranking, permissions | [AI system design](../questions/04-ai-system-design.md) | [RAG chapters](../../../ai-system-design-guide/06-retrieval-systems/), [RAG lessons](../../../ai-engineering-from-scratch/phases/11-llm-engineering/06-rag/) |
| 3 | Agents and tools | tool contracts, state, retries, human approval, MCP, durable execution | [Theory questions](../questions/01-theory.md) | [Agent chapters](../../../ai-system-design-guide/07-agentic-systems/), [tools and protocols](../../../ai-engineering-from-scratch/phases/13-tools-and-protocols/), [agent engineering](../../../ai-engineering-from-scratch/phases/14-agent-engineering/) |
| 4 | Evals and observability | golden sets, graders, regression gates, traces, metrics, logs, cost, failure analysis | [AI system design](../questions/04-ai-system-design.md) | [Eval and observability](../../../ai-system-design-guide/14-evaluation-and-observability/), [production lessons](../../../ai-engineering-from-scratch/phases/17-infrastructure-and-production/) |
| 5 | Backend and distributed systems | Python, APIs, SQL, queues, caching, idempotency, consistency, security | [Coding questions](../questions/02-coding.md), [theory questions](../questions/01-theory.md) | [Common core](01-common-core.md), [system-design frameworks](../../../ai-system-design-guide/00-interview-prep/02-answer-frameworks.md) |
| 6 | Delivery and platform | Docker, Kubernetes, Terraform, Helm, GitHub Actions, Argo CD, rollout, rollback | [AI system design](../questions/04-ai-system-design.md) | [Platform track](06-ml-ai-platform-engineer.md), [CI/CD](../../../ai-system-design-guide/11-infrastructure-and-mlops/02-cicd.md) |
| 7 | Product and FDE | requirements, user value, scoping, integration, trade-offs, communication | [Project deep dive](../questions/03-project-deep-dive.md), [home assignments](../questions/06-home-assignments.md) | [Product AI track](04-product-ai-engineer.md), [FDE track](05-forward-deployed-engineer.md) |
| 8 | Behavioral and project stories | ownership, disagreement, failure, influence, ambiguity, technical decisions | [Behavioral questions](../questions/05-behavioral.md) | [Behavioral preparation](07-senior-staff-behavioral.md), [project deep dives](08-project-deep-dives-and-take-homes.md) |

The external [128-question bank](../../../ai-system-design-guide/00-interview-prep/01-question-bank.md)
is the broad question source. Use the category above to choose a small slice;
do not read it from Q1 to Q128 in order.

## Production examples

For concrete examples while answering, use `~/slotsense`:

- RAG and ingestion: `slotsense-ai-assistant-new/docs/ingestion_retrieval_improvements.md`
- observability: `slotsense-ai-assistant-new/docs/langfuse_observability_and_rag_fixes.md`
- privacy: `slotsense-ai-assistant-new/docs/pii_filtering_feature_report.md`
- agent boundaries: `slotsense-ai-assistant-new/docs/signals-not-decisions.md`
- evaluations: `slotsense-qa-eval/`
- telemetry analysis: `clickhouse-analysis/`
- deployment: `slotsense-helm-charts/`, `slotsense-infrastructure/`, and `slotsense-cicd-centralized-workflows/`

Use these as production examples. Keep the distinction between code you
personally changed, a team decision, and a design that was only proposed.

## Practice loop

```text
1. Pick one category.
2. Choose one question.
3. Clarify requirements and draw the system.
4. Answer aloud in 10 minutes.
5. Check the linked reference answer.
6. Add one failure mode, metric, or trade-off.
7. Score the answer and write the missing point.
```

Use the [answer frameworks](../../../ai-system-design-guide/00-interview-prep/02-answer-frameworks.md)
for system-design answers and the [whiteboard exercises](../../../ai-system-design-guide/00-interview-prep/04-whiteboard-exercises.md)
for timed practice.

## Answer record

```text
Date:
Category:
Question:
My design in one paragraph:
Diagram or key components:
Main trade-off:
Failure and fallback:
Metric or evaluation:
Reference answer:
Missing point:
Score: 0 / 1 / 2
```

## Choose today

- Product AI or applied role: practice categories 2, 3, 4, and 7.
- FDE role: practice categories 2, 5, 6, and 7.
- AI platform role: practice categories 4, 5, and 6, then add category 1.
- Any role: do one coding or SQL problem from category 5 every practice day.

For a full diagnostic, schedule, and readiness assessment, open
[DETAILED-CURRICULUM.md](DETAILED-CURRICULUM.md). For the system-design source
map and hiring-source notes, open the [integration guide](12-ai-system-design-guide-integration.md).
