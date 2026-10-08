# Flagship RAG-and-Agent Project Decision Map

Canonical planning artifact for selecting and shaping one business-led,
production-grade portfolio project. Resolve tickets in order; do not introduce
another project candidate unless evidence invalidates the current one.

## #1: Which role should the flagship optimize for?

Blocked by: none
Type: Discuss

### Question

Which primary hiring signal should determine the project's business problem,
scope, and technical depth?

### Answer

Optimize primarily for **Senior Applied/Product AI Engineer**, with
**Forward-Deployed AI Engineer** as the secondary position. The current CV
already names Applied AI as the primary positioning, and the local market
analysis says RAG, agents, workflow automation, evaluation, AWS, Docker, and
production operations are the strongest overlapping signals.

This means the flagship must be a useful product workflow with measurable
business value. Infrastructure is supporting evidence, not the product itself.

Evidence:

- [`job-search/cv/base.md`](../../job-search/cv/base.md)
- [`role/README.md`](../../role/README.md)
- [`role/04-use-cases.md`](../../role/04-use-cases.md)

## #2: Which business workflow should the project own?

Blocked by: #1
Type: Discuss

### Question

Should the flagship own the end-to-end workflow of resolving a policy-bound
customer case: inspect case and account/order facts, retrieve the applicable
versioned policy, calculate deterministic eligibility, propose a cited
resolution, and execute a write only after human approval?

### Answer

**Yes.** The project is a **Case Resolution Copilot** for an internal B2B
support or commerce-operations specialist. It owns one policy-bound
return/refund workflow from case intake through an evidence-backed resolution
proposal and an approved, idempotent simulated action.

This is narrower and more defensible than a generic support chatbot: RAG
supplies versioned policy evidence; tools supply live case and order facts;
deterministic code owns calculations and eligibility; a bounded agent
coordinates the workflow; and approval, tenant isolation, and an audit trail
govern side effects.

## #3: Is the problem supported by current market and workflow evidence?

Blocked by: #2
Type: Research

### Question

Which current target-company job descriptions, product documentation,
engineering posts, and public or synthetic data support this workflow and its
constraints?

### Answer

**Supported.** Current ServiceNow roles ask for agent harnesses, tool and
human-escalation boundaries, context/retrieval engineering, evals,
observability, reliability, and cost judgment. Salesforce service workflows,
Intercom's Fin API, and AWS's grounded retail-agent architecture independently
support the combination of knowledge, live records, deterministic procedures,
approval, and escalation.

The initial benchmark will use a transparent synthetic policy/case/order
dataset because public support-chat datasets do not contain the policy
versions, transaction facts, decision labels, and side-effect outcomes needed
for this workflow.

Evidence: [`research/business-workflow-evidence.md`](research/business-workflow-evidence.md)

## #4: What outcome and first delivery slice prove value?

Blocked by: #2, #3
Type: Discuss

### Question

Who is the exact user, what changes in their work, which baseline will the
system beat, what errors are unacceptable, and what is the smallest complete
case-resolution path?

### Answer

The primary user is an internal **Support Operations Specialist** accountable
for the final case outcome. The system changes their work by assembling one
reviewable Resolution Proposal from case facts, order facts, temporally valid
policy evidence, deterministic eligibility, and a suggested action.

The comparison baseline is one-shot RAG using the same model and corpus. The
first complete slice covers proposal, ambiguity/escalation, human approval, an
idempotent Simulated Action, and a joined audit trail. Twenty-four manually
reviewed canonical cases form the initial hard release gate; broader targets
will follow measured baseline difficulty.

No claim about real handling-time or support-cost reduction is permitted until
a controlled operator comparison is run. Quality, safety, latency, token use,
and model cost may be reported from the synthetic benchmark with that context.

Evidence and acceptance gates: [`PRODUCT_BRIEF.md`](PRODUCT_BRIEF.md)

## #5: What are the domain language and system boundaries?

Blocked by: #4
Type: Discuss

### Question

What are the canonical meanings and ownership boundaries for Case, Policy,
Policy Version, Evidence, Eligibility Decision, Resolution Proposal,
Approval, and Executed Action?

### Answer

Pending. Create `CONTEXT.md` when these terms are resolved. Separate model
signals from deterministic decisions and authorized state transitions.

## #6: How will retrieval and AI behavior be evaluated?

Blocked by: #4, #5
Type: Prototype

### Question

Which ingestion, chunking, hybrid retrieval, reranking, citation, abstention,
and evaluation design reliably selects the policy version that applied when
the case occurred?

### Answer

Pending. Compare against simple baselines before selecting the production
retrieval design; preserve the benchmark and failure taxonomy as public
evidence.

## #7: What may the agent do, and what must remain deterministic?

Blocked by: #4, #5
Type: Prototype

### Question

Which bounded workflow, typed tools, approval gates, retries, idempotency
rules, prompt-injection defenses, and failure policies make the agent useful
without granting it authority to invent or execute unsupported resolutions?

### Answer

Pending. The agent may gather evidence and propose; deterministic services
must validate eligibility and own irreversible actions.

## #8: What production architecture proves deployability and ownership?

Blocked by: #6, #7
Type: Research

### Question

Which minimal AWS architecture, local Docker environment, Terraform modules,
CI/CD gates, security controls, telemetry, dashboards, alerts, load tests,
failure drills, rollback path, and cost controls are justified by the measured
workload?

### Answer

Pending. AWS services must follow workload and reliability requirements; the
project will not add Kubernetes merely as a keyword.

## #9: How will each milestone become public and interview evidence?

Blocked by: #4, #6, #7, #8
Type: Discuss

### Question

How should the repository, 3–4 article series, LinkedIn derivatives, decision
log, benchmark evidence, architecture narrative, and project-deep-dive drill
be generated from the same build milestones?

### Answer

Pending. Produce one reusable project template after this flagship proves the
workflow.
