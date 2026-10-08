# Business Workflow Evidence: Case Resolution Copilot

Researched: 2026-09-02

## Decision

Keep the **Case Resolution Copilot** as the flagship project. The evidence
supports a narrow internal support workflow in which a human operator receives
an evidence-backed resolution proposal and approves any consequential action.

This is not a customer-facing FAQ chatbot and not an autonomous refund bot.

## Problem

Support operations specialists repeatedly assemble the same decision from
different sources:

1. understand the customer case;
2. inspect current account and order facts;
3. find the policy version that applied when the event occurred;
4. calculate eligibility and permitted remedies;
5. propose a response and action with evidence;
6. escalate ambiguity or request approval for a consequential action;
7. record what was decided and why.

The project will make that workflow faster and more consistent while keeping
policy interpretation, model uncertainty, and state-changing actions visible
to the operator.

## Current hiring evidence

### ServiceNow

The June 2026
[Staff AI Engineer, Conversational & Agentic AI](https://careers.servicenow.com/jobs/744000134539069/staff-ai-engineer-conversational-agentic-ai/)
role describes agents that reason over enterprise data and complete workflows.
It explicitly calls for:

- an execution harness that routes inputs, manages context, invokes tools,
  handles retries, and exposes execution state;
- deliberate boundaries among tool calls, subagents, hard-coded paths, and
  human escalation;
- prompt versioning and evaluation across model changes;
- production reliability, cost/latency judgment, observability, and failure
  analysis.

The August 2026
[Staff Software Engineer role in Hyderabad](https://careers.servicenow.com/jobs/744000146518464/staff-software-engineer/)
connects Customer Service Management and fulfillment workflows with agent
architectures, dynamic tool use, execution policy, context engineering,
retrieval systems, vector databases, and verification harnesses.

ServiceNow's
[Applied AI Forward Deployed Engineering team](https://careers.servicenow.com/teams/ai-engineering-product/)
embeds with customers to solve critical workflow problems and turns those
solutions into reusable product patterns. That is the secondary hiring signal
this project should demonstrate.

### Salesforce

Salesforce's official
[Agentforce for Service use cases](https://trailhead.salesforce.com/content/learn/modules/agentforce-service-agent-quick-look/explore-use-cases-for-agentforce-for-service)
combine exactly the surfaces needed here:

- case and order records;
- return and warranty knowledge;
- instructions that constrain behavior;
- tools for reads and writes;
- customer verification and live-agent escalation.

Salesforce now requires confirmation for actions such as cancelling an order,
creating a case, adding a case comment, or finalizing a delivery change. Its
[security notice](https://help.salesforce.com/s/articleView?id=005133036&language=en_US&type=1)
ties that change directly to prompt-injection risk and recommends confirmation
for sensitive custom actions.

The July 2026
[Data and AI Architect role](https://careers.salesforce.com/en/jobs/jr333757/pre-sales-data-and-ai-architect-solution-engineering-united-states/)
also reinforces the FDE-style evidence expected from the portfolio: discover
the customer's real problem, pressure-test feasibility and cost, build a
prototype, explain the architecture, and turn field learning into reusable
assets.

## Current product and architecture evidence

Intercom's
[Fin developer API](https://developers.intercom.com/docs/guides/fin-agent-api)
separates capability discovery, one-shot knowledge answers, deterministic
procedures, continued conversation, and explicit human escalation. This is a
useful boundary model: the LLM does not need to own every part of the workflow.

AWS Prescriptive Guidance documents a
[grounded agent workflow for retail customer service](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-serverless/pattern-grounded-agent-ai.html)
where answers depend on live order data, return eligibility, timelines, and
region-specific policy. The reference shape uses Bedrock, a knowledge base,
Lambda tools, security context, escalation, and an audit output.

ServiceNow reports that its support workflow surfaces relevant knowledge,
similar cases, and diagnostic information to technical support engineers. In
its published
[Customer Service Management case study](https://www.servicenow.com/content/dam/servicenow-assets/public/en-us/doc-type/resource-center/case-study/cs-non-proactive-support-case-study.pdf),
cases with an attached knowledge-base article were resolved up to 45% faster.
Treat this as vendor-reported directional evidence, not as a performance claim
for our project.

## Why this needs RAG and an agent

### RAG is justified

The applicable evidence lives in policy documents, and the correct answer can
depend on policy version, region, product, purchase date, and case state. The
system must retrieve and cite the exact policy passage rather than rely on
model memory.

### A bounded agent is justified

The workflow requires conditional tool use: inspect the case, fetch order
facts, retrieve policy evidence, request missing information, run an
eligibility check, draft a proposal, and either escalate or request approval.
The sequence depends on intermediate results, but it has a finite state model
and explicit stop conditions.

### Deterministic services remain authoritative

Code, not the language model, will own:

- date and amount calculations;
- policy-version filtering;
- eligibility rule evaluation;
- tenant and resource authorization;
- idempotency and approval validity;
- state transitions and writes.

The model may classify, retrieve, summarize, and propose. A human or an
authorized service decides and executes.

## Data strategy

Use a transparent, synthetic but realistic benchmark rather than customer
data:

- author a small time-versioned policy corpus with deliberately conflicting
  old and new clauses;
- generate tenants, customers, orders, and cases from explicit schemas with no
  real PII;
- manually review the core golden cases and expected eligibility decisions;
- generate paraphrases and adversarial variants only after the canonical cases
  are fixed;
- publish generation scripts, seeds, schemas, licenses, and dataset cards;
- label all measured results as controlled benchmark results, never real-user
  impact.

The public Bitext support dataset was considered but is not the primary data.
It contains useful support utterances, but it does not provide the order facts,
policy versions, decision labels, or action outcomes needed to evaluate this
workflow. Its CDLA-Sharing-1.0 license would also add redistribution conditions
without solving the core evidence problem.

## Scope guardrails

The first complete workflow handles **return/refund eligibility for one
synthetic commerce operator**.

It includes:

- an internal operator interface or API;
- one case type with normal, ambiguous, ineligible, and adversarial examples;
- versioned policy retrieval with citations;
- typed order/case tools;
- deterministic eligibility;
- a resolution proposal;
- escalation and human approval;
- an idempotent simulated action and audit record.

It excludes:

- a public customer-chat product;
- autonomous refunds;
- multiple specialist agents;
- every customer-support intent;
- real customer data;
- production integrations with a commerce vendor.

## Research conclusion

The workflow is sufficiently current, business-led, and hiring-relevant. It
supports both primary positioning (Applied/Product AI) and secondary
positioning (FDE), while giving every requested production artifact a concrete
reason to exist.

Proceed to defining the user outcome, baseline, success measures, unacceptable
errors, and smallest end-to-end delivery slice.
