# Case Resolution Copilot: Product Brief

Status: Project framing
Updated: 2026-09-02

## Objective

Help an internal support-operations specialist resolve a policy-bound
return/refund case from one review surface. The system assembles live case and
order facts, retrieves the policy version that applied at the event time,
calculates eligibility deterministically, and returns a cited resolution
proposal. A consequential action occurs only after explicit human approval.

The product is successful when the operator can make a defensible decision
without reconstructing the evidence across separate systems, while the system
remains safe under ambiguity, retries, malicious document content, and tenant
boundary attacks.

## Primary user

The primary user is an **internal support-operations specialist** accountable
for resolving customer cases. The customer is affected by the outcome but does
not interact with the system in the first release.

This choice keeps human judgment and accountability visible and lets the
project evaluate the evidence packet, recommendation, approval, and action
boundary separately.

## Job to be done

When a customer asks for a return or refund, the specialist needs to determine
what happened, which policy applied, whether the request is eligible, what
remedy is permitted, and what to communicate or execute. Today that decision
requires switching among the case record, order system, policy documents, and
action interface.

The copilot should produce one **Resolution Proposal** containing:

- case and order facts used;
- the applicable policy version and cited clauses;
- a deterministic eligibility result with reason codes;
- a proposed remedy and draft operator response;
- missing or conflicting information;
- a recommendation to approve, reject, or escalate;
- the action that would run after approval.

## Value hypothesis

The system should reduce evidence-gathering and make policy application more
consistent. This is a hypothesis until an operator comparison is run.

The portfolio may claim measured benchmark quality, latency, cost, isolation,
and idempotency. It must not claim reduced real-world handling time, support
cost, or customer impact from synthetic data.

After the vertical slice works, run a small controlled comparison:

1. resolve a fixed set of cases with separate case/order/policy views;
2. review the same difficulty-balanced set with the copilot;
3. measure time to decision, corrections, evidence lookups, and confidence;
4. label the result as a limited usability study, not production ROI.

## System baseline

Build and preserve a **one-shot RAG baseline** before the bounded agent:

```text
case + order snapshot
  -> keyword retrieval over current policy text
  -> one LLM call
  -> unvalidated answer
```

The baseline deliberately has no tool loop, temporal policy filter,
deterministic eligibility service, approval state, or action execution. It
must use the same model, cases, and policy corpus as the proposed system so the
comparison isolates the value of the workflow design.

Compare the baseline and final system on:

- correct policy-version selection;
- retrieval recall and citation validity;
- eligibility and remedy accuracy;
- appropriate escalation;
- unsupported policy claims;
- task completion;
- latency, token use, and model cost.

Do not assume the agent wins. If the one-shot baseline performs as well on a
slice, keep the simpler path for that slice.

## Unacceptable errors

The release is blocked by any of these failures in the canonical test suite:

- a case, order, policy, cache entry, trace, or action crosses a tenant
  boundary;
- the proposal applies or cites a policy version that was not effective at the
  event time;
- the proposal recommends an ineligible refund without escalation;
- an unsupported policy claim is presented as evidence;
- missing or contradictory facts are silently guessed instead of escalated;
- a state-changing action runs without a valid approval for the same proposal,
  actor, tenant, and proposal version;
- a retry or concurrent request creates a duplicate action;
- untrusted policy or case text can override tool, approval, or authorization
  rules;
- raw secrets or sensitive fixture fields appear in prompts, logs, traces, or
  evaluation exports where they are not required.

These are hard gates, not weighted quality metrics.

## Initial evaluation set

Start with 24 manually reviewed canonical cases:

| Slice | Cases | Purpose |
| --- | ---: | --- |
| Eligible | 6 | Correct policy, calculation, remedy, and approval path |
| Ineligible | 5 | Correct rejection with evidence |
| Ambiguous or incomplete | 5 | Clarification or escalation instead of guessing |
| Temporal conflicts | 4 | Old and new policy clauses deliberately disagree |
| Adversarial and isolation | 4 | Prompt injection, cross-tenant IDs, approval replay, duplicate request |

After the contracts stabilize, expand to at least 100 cases with reviewed
paraphrases, boundary dates, amount boundaries, missing fields, tool failures,
and adversarial variants. Keep the 24 canonical cases as an immutable release
gate.

## Initial success gates

For the 24 canonical cases:

- 100% correct tenant and policy-version selection;
- 100% recall on cases requiring escalation;
- 100% valid citations: every citation resolves to the selected policy
  version and quoted clause;
- 100% deterministic eligibility agreement with the golden reason codes;
- zero unsupported consequential recommendations;
- zero unauthorized or duplicate actions;
- every run ends in one explicit state: `proposed`, `needs_information`,
  `escalated`, or `failed`;
- latency, token use, and model cost are captured for every run.

These gates are intentionally strict because the initial cases are authored
and reviewable. Broader paraphrase-set targets will be set only after the
baseline exposes the real difficulty distribution.

## Smallest complete delivery slice

The first vertical slice handles one eligible return/refund case and one
ambiguous case through the same production-shaped interfaces:

```text
operator selects case
  -> system loads tenant-scoped case and order facts
  -> temporal retrieval selects policy version and clauses
  -> deterministic service evaluates eligibility
  -> bounded workflow creates Resolution Proposal
  -> operator approves, rejects, or escalates
  -> approved simulated refund is recorded idempotently
  -> audit event and trace explain the full decision
```

The slice is complete only when it can be run locally from documented commands
and demonstrates:

1. a proposal with cited evidence;
2. an ambiguity that cannot reach approval;
3. an approval followed by one simulated action;
4. a repeated action request that returns the original result;
5. an audit record joining case, proposal, approval, action, actor, policy
   version, and trace;
6. deterministic tests and an evaluation command.

## First-slice interface

Start with a small API plus a minimal operator review page or CLI. The exact UI
is secondary to exposing the state transitions and evidence clearly.

Required user operations:

- open a case;
- request a resolution proposal;
- inspect facts, citations, eligibility, and warnings;
- approve, reject, or escalate;
- inspect the resulting action and audit history.

## First-slice data

Seed two synthetic tenants to make isolation testable. Only one tenant appears
in the happy-path demo; the second exists for negative tests.

Seed:

- two conflicting policy versions with effective date ranges;
- customers and orders with synthetic identifiers and no real PII;
- the 24 canonical cases and golden outcomes;
- one approval replay and one duplicate-action scenario.

## Non-goals for the first slice

- customer-facing chat;
- email, Slack, or CRM integrations;
- real payment or commerce APIs;
- multiple support domains or specialist agents;
- semantic caching, reranking, or provider routing before the baseline exists;
- Kubernetes;
- a polished multi-page frontend;
- claims of production scale or business ROI.

Docker, CI, AWS infrastructure, observability, security hardening, load tests,
and failure drills remain required for the finished flagship. They follow the
verified vertical slice instead of expanding its first implementation.

## Evidence produced by this slice

- baseline versus bounded-workflow evaluation report;
- immutable canonical case set and dataset card;
- test results for temporal policy selection, authorization, approval, and
  idempotency;
- trace and audit example for one completed case;
- decision record explaining why the model proposes while services decide;
- material for the first article: business problem, baseline, scope, and first
  measured failure taxonomy.
