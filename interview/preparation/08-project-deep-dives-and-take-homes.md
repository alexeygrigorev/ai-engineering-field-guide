# Senior AI and FDE Project Deep Dives and Take-Homes

This guide prepares you to defend production work and deliver a scoped take-home for senior Product AI Engineer, Forward Deployed Engineer, and ML/AI Platform Engineer roles. Use it with the [curriculum overview](README.md), [common core](01-common-core.md), [AI/ML system design](03-ai-ml-system-design.md), and [senior and staff behavioral guide](07-senior-staff-behavioral.md).

The goal is not a polished story that hides uncertainty. The goal is a precise account of the problem, your contribution, the decisions you made, the evidence available at the time, what happened in production, and what you learned.

Company formats, time limits, tool policies, and evaluation criteria vary. Confirm them from the assignment, recruiter, or interviewer. The questions and rubrics in this guide are synthesized preparation material, not claims about any company's process.

## What These Rounds Test

A project deep dive asks whether you can:

- Own an ambiguous problem from requirements through operations.
- Explain why the work mattered before describing the technology.
- Separate your contribution from the team's contribution.
- Defend architecture against requirements, constraints, and credible alternatives.
- Connect model behavior and system metrics to user, customer, or platform outcomes.
- Discuss failures, incidents, and limitations without becoming vague or defensive.
- Move between a concise summary and implementation-level detail.
- Show senior judgment about sequencing, risk, security, cost, and organizational boundaries.

A take-home adds evidence about how you work with limited time:

- Clarify incomplete requirements and label assumptions.
- Choose a small vertical slice that works end to end.
- Design for testability and evaluation.
- Write maintainable code without building an unnecessary platform.
- Communicate decisions, limitations, setup, and next steps.
- Defend and extend the work after submission.

Treat both formats as demonstrations of judgment. More code, more services, and more agent autonomy are not automatically stronger.

## Select Two or Three Projects

Prepare two projects deeply and a third as a useful backup. Two strong, complementary projects are better than three shallow ones.

### Selection criteria

Use the canonical 1-4 scale from [module 09](09-mock-interviews-and-scorecards.md#common-scoring-scale). Score each candidate project on these dimensions:

- Production ownership
  - 1 - prototype, coursework, or a narrow implementation task with no operational responsibility.
  - 2 - contributed to a shipped system but owned only part of the lifecycle.
  - 3 - independently owned meaningful work from framing or design through launch, operations, and iteration.
  - 4 - owned unusually consequential work with broader operational or organizational leverage.
- Role fit
  - 1 - little connection to repeated responsibilities in the target role.
  - 2 - demonstrates adjacent skills.
  - 3 - directly demonstrates the role's central unit of success.
  - 4 - demonstrates the central unit of success plus strong senior or staff scope.
- Outcome evidence
  - 1 - no evidence beyond completion or a materially unsafe claim.
  - 2 - partial qualitative evidence, adoption, stakeholder acceptance, or technical results with clear limitations.
  - 3 - credible quantitative or directly observable outcomes tied to the original objective.
  - 4 - strong, independently defensible outcomes with limitations and broader effects made explicit.
- Technical depth
  - 1 - cannot explain the system below framework names.
  - 2 - can defend one component or decision in depth but has important gaps.
  - 3 - can trace data and control flow, failure behavior, trade-offs, and implementation details end to end.
  - 4 - can also adapt the explanation under changed constraints and expose second-order risks.
- Decision ownership
  - 1 - followed a predetermined design or cannot establish ownership.
  - 2 - influenced decisions within a component.
  - 3 - framed alternatives, gathered evidence, made or drove consequential decisions, and owned the result.
  - 4 - shaped decisions across boundaries and created a durable decision rule or mechanism.
- Operational evidence
  - 1 - no deployment, monitoring, or incident experience.
  - 2 - understands production behavior but did not own it.
  - 3 - can discuss rollout, monitoring, support, incidents, rollback, and evolution from direct experience.
  - 4 - can also show durable improvements to reliability, operations, or ownership across teams.
- Communication range
  - 1 - story only works as an unclear or overly detailed technical explanation.
  - 2 - can explain it coherently to one audience.
  - 3 - can adapt it for executives, customers, product partners, application engineers, and specialists.
  - 4 - adapts precisely under probing while preserving facts, decisions, and appropriate depth.

The minimum is 7 and the maximum is 28. Prioritize projects with strong dimension profiles, then check that the set is complementary. A total alone must not hide a 1 in ownership, outcome evidence, technical depth, or operational evidence. A useful pair often includes:

- One project with strong end-user or customer outcomes.
- One project with deeper infrastructure, reliability, data, model, or evaluation complexity.
- Different failure modes, stakeholders, and organizational scope.
- At least one recent project whose details you can still defend.

Do not choose only greenfield successes. A migration, rescue, incident-driven redesign, or deliberately stopped project can be strong when it proves judgment and learning.

### Map projects to target roles

For each target job description:

1. Extract five to eight repeated responsibilities or constraints.
2. Map each one to direct evidence from a project.
3. Mark evidence as strong, adjacent, or absent.
4. Choose projects that cover the central responsibilities with the least stretching.
5. Prepare an honest sentence for every important gap.

Do not infer the company's interview rubric from the title alone. Use the actual job description and recruiter guidance.

### Use truthful outcomes

Never invent revenue, adoption, accuracy, latency, cost, or scale. If an exact number is confidential or was never measured, use the strongest truthful evidence available.

Preferred evidence, in order:

1. Exact measured result you are allowed to disclose.
2. Approved range, relative change, order of magnitude, or normalized measure.
3. Direct operational evidence such as launch scope, sustained usage, incident reduction, support load, or migration completion.
4. Qualitative evidence tied to a named observation, decision, or stakeholder behavior.
5. A clear statement that the outcome was not measured, followed by what you would measure now.

Useful formulations include:

- "I cannot share the absolute volume, but the system served a high-four-figure daily request load at launch."
- "We measured a material reduction in review time, but I cannot disclose the exact internal figure."
- "We did not instrument task completion, so I cannot claim product impact. We did verify adoption across three operating teams and measured API reliability."
- "The project was stopped after the pilot because the quality threshold was not met. The valuable outcome was an evaluation set and a decision not to scale the wrong approach."

Avoid false precision. Do not convert memory, estimates, or correlation into measured causation. Label each number as measured, estimated, sampled, or confidential.

## Build a Layered Project Narrative

Prepare the same project at three levels. Do not create three different stories; create three resolutions of one factual account.

### The 60-second version

Use this for introductions and interviewer selection.

Cover:

1. Context - user or customer, workflow, and why the problem mattered.
2. Scope - what you personally owned.
3. Decision - the most important architectural or execution choice.
4. Result - the strongest truthful outcome.
5. Depth hook - one hard problem the interviewer can explore.

Template:

> I led [scope] for [user or customer] because [problem and consequence]. The existing baseline was [baseline]. I owned [personal contribution] and chose [approach] over [credible alternative] because [constraint]. We shipped [bounded result], and the evidence was [measured or observable outcome]. The hardest part was [technical or organizational challenge], which changed how we handled [evaluation, reliability, security, cost, or rollout].

Rehearse it until it fits in 45-75 seconds without rushing.

### The 5-minute version

Use a compact sequence:

1. Problem and stakes - 45 seconds.
2. Requirements, constraints, and baseline - 40 seconds.
3. Architecture and data flow - 80 seconds.
4. Two consequential decisions and alternatives - 50 seconds.
5. Launch, incident, or iteration - 45 seconds.
6. Results, limitations, and learning - 40 seconds.

Pause after the high-level architecture and invite direction: "I can go deeper on retrieval and evaluation, the deployment constraints, or the incident that changed the design."

### The 20-30 minute version

Plan for dialogue rather than a memorized monologue.

- Minutes 0-3 - establish context, stakes, scope, and your role.
- Minutes 3-7 - define requirements, constraints, baseline, and success criteria.
- Minutes 7-12 - draw the architecture and trace one representative request or workflow.
- Minutes 12-17 - defend two or three major decisions and rejected alternatives.
- Minutes 17-21 - explain evaluation, rollout, monitoring, security, reliability, and cost.
- Minutes 21-25 - discuss a failure, incident, or surprising result.
- Minutes 25-28 - present outcomes, limitations, evolution, and what you would change.
- Remaining time - follow-up questions.

If the interviewer interrupts early, answer the question directly and reconnect it to the architecture. Do not insist on finishing prepared slides.

## Defend the Architecture

Use the following sequence to prepare every project. For deeper design practice, use [AI/ML system design](03-ai-ml-system-design.md).

### Requirements and success

State:

- Primary user, customer, or internal team.
- Trigger, workflow, decision, and desired outcome.
- Functional requirements and explicit non-goals.
- Quality, latency, availability, throughput, privacy, and cost expectations.
- Acceptance criteria and who approved them.
- Unknowns that could have invalidated the project.

Separate requirements that existed at the start from requirements discovered later.

### Constraints

Name the constraints that materially shaped the design:

- Deadline, team size, skills, ownership, and support capacity.
- Existing APIs, identity, data stores, networks, cloud, or on-premises environment.
- Data availability, quality, labeling, retention, residency, and licensing.
- Model availability, context limits, rate limits, latency, and provider policy.
- Regulatory, security, privacy, contractual, or customer-review requirements.
- Budget, unit economics, migration risk, and backward compatibility.

Explain which constraints were fixed, negotiable, assumed, or later disproved.

### Baseline

Define what the system had to beat:

- Existing manual workflow.
- Deterministic rules or search.
- Current model or prompt.
- Managed service.
- No-op option.

Give baseline quality, effort, latency, cost, reliability, or user behavior where measured. A sophisticated AI system without a baseline is difficult to justify.

### Data

Be ready to explain:

- Sources, ownership, permissions, lineage, freshness, and representativeness.
- Collection, labeling, deduplication, normalization, splitting, and versioning.
- Leakage, imbalance, missing data, schema drift, and feedback bias.
- Access control, retention, deletion, redaction, and audit requirements.
- How online data differed from development data.
- How data failures appeared in downstream behavior.

Trace one example from source to model input to output to persisted record.

### Model choice

Defend the choice against task-specific criteria:

- Quality on representative examples.
- Structured output and tool-use reliability.
- Context window and multimodal requirements.
- Latency, throughput, rate limits, and regional availability.
- Cost per useful task, not only cost per token.
- Privacy, data processing, retention, and deployment constraints.
- Operational stability, versioning, fallback, and vendor risk.

Describe the evaluation or evidence used to choose. "It was the best model" is not sufficient.

### RAG decision

Explain whether retrieval was needed:

- What knowledge changed too often or was too private to place in model weights?
- Why search, database queries, or direct context injection were insufficient.
- How documents were parsed, chunked, enriched, indexed, filtered, retrieved, reranked, and cited.
- How authorization was preserved during retrieval.
- How unanswerable, conflicting, stale, or malicious sources were handled.
- Which retrieval and answer metrics were used.

If you did not use RAG, explain why the simpler approach was appropriate.

### Agent decision

Use an agent only when the system must choose among actions or adapt a bounded plan. Be ready to explain:

- Why a deterministic workflow, state machine, or ordinary function calling was insufficient.
- Allowed tools, permissions, input and output schemas, and side-effect boundaries.
- Maximum steps, timeout, budget, cycle detection, and termination.
- Approval gates, previews, undo, idempotency, and compensation.
- State persistence, replay, tracing, and auditability.
- Tool and policy tests, including prompt-injection resistance.

Do not defend autonomy as a goal. Defend the minimum autonomy required by the task.

### Evaluation

Connect evaluation to the original decision:

- Unit of evaluation - request, answer, citation, trajectory, workflow, user task, or deployment.
- Dataset sources, categories, size rationale, ownership, and version.
- Deterministic checks, model-based graders, human review, and calibration.
- Quality thresholds and release gates.
- Slice analysis and failure taxonomy.
- Regression policy and how production failures entered the evaluation set.
- Relationship between offline metrics and online user or business outcomes.

State what the evaluation could not prove.

### Reliability

Cover:

- Timeouts, retries, jitter, circuit breakers, queues, and backpressure.
- Idempotency, deduplication, partial failure, and safe replay.
- Fallback model or deterministic degraded mode.
- Dependency failure and provider outage behavior.
- SLOs, SLIs, error budgets, rollback, recovery objectives, and ownership.
- Capacity assumptions, overload behavior, and load tests.

For AI outputs, distinguish service reliability from semantic quality.

### Security and privacy

Be ready to defend:

- Authentication, authorization, tenant isolation, and least privilege.
- Data minimization, encryption, retention, deletion, and residency.
- Secret storage and rotation.
- Prompt injection, indirect injection, untrusted retrieval, and output handling.
- Tool permissions, egress controls, sandboxing, and approval for side effects.
- PII handling, logs, traces, analytics, and support access.
- Abuse prevention, rate limiting, audit events, and incident response.
- Third-party model and dependency review.

Avoid claiming that a system was secure because inputs were sanitized or a system prompt prohibited bad behavior.

### Cost

Show a simple cost model:

- Requests or jobs per period.
- Input and output tokens, embedding volume, storage, compute, and data transfer.
- Retry, fallback, cache, evaluation, and observability overhead.
- Peak versus average demand.
- Cost per request, successful task, tenant, or business outcome.
- Dominant uncertainty and sensitivity analysis.

Explain the quality, latency, reliability, and engineering-cost trade-offs behind optimizations.

### Deployment

Describe:

- Development, test, staging, and production environments.
- Infrastructure and application packaging.
- Configuration and secret handling.
- CI checks, artifact versioning, schema changes, and migrations.
- Feature flags, canaries, shadow traffic, cohorts, and rollback.
- Model, prompt, retrieval, tool, and evaluation versioning.
- Customer-specific deployment constraints where relevant.

### Monitoring

Separate:

- Service health - traffic, errors, latency, saturation, queues, dependency health.
- AI behavior - groundedness, refusals, tool errors, schema validity, safety, drift, and sampled review.
- Product or customer outcomes - task success, adoption, completion, corrections, escalation, and retention.
- Economics - tokens, cache behavior, provider spend, compute utilization, and cost per useful task.

Name alert owners, thresholds, dashboards, and the action each signal triggers.

### Incidents

Prepare at least one incident or near miss:

1. Detection and user impact.
2. Timeline and immediate containment.
3. Technical and organizational contributing factors.
4. Diagnosis and evidence.
5. Recovery and stakeholder communication.
6. Corrective and preventive actions.
7. What changed in tests, evaluations, monitoring, runbooks, or architecture.

Avoid a story in which you were the lone hero. Show coordination, explicit ownership, and system improvement.

### Evolution

Explain the sequence rather than only the final architecture:

- First experiment and uncertainty it resolved.
- Minimum viable production slice.
- Hardening after real usage.
- Scaling, migration, or platformization.
- Components removed or simplified.
- Current limitations and next decision.

Senior judgment is visible in sequencing investment under uncertainty.

### Alternatives rejected

For each major decision, prepare:

- The chosen option.
- Two credible alternatives.
- Decision criteria.
- Evidence available at the time.
- Trade-offs accepted.
- Trigger that would justify revisiting the choice.

Do not create weak alternatives merely to make the chosen design look inevitable.

## Project Dossier Template

Create one dossier per project. Keep the primary dossier to two to four pages, then link evidence.

### Summary

- Project name and one-sentence purpose.
- Date, duration, stage, and current status.
- User, customer, or internal platform consumer.
- Team composition and decision makers.
- Your role, authority, and boundaries.
- Strongest truthful outcome.
- Two depth areas and one limitation.

### Problem and context

- User workflow and pain.
- Why the work became a priority.
- Existing baseline and cost of doing nothing.
- Functional and nonfunctional requirements.
- Constraints, assumptions, unknowns, and non-goals.
- Success criteria and measurement plan.

### Architecture

- Context diagram and one deeper component or sequence diagram.
- Data flow and control flow.
- Model, retrieval, tool, storage, queue, API, and identity boundaries.
- Deployment topology.
- Trust boundaries and failure boundaries.
- One representative request trace.

### Decisions

For each of three to five decisions:

- Decision and owner.
- Options considered.
- Criteria and evidence.
- Chosen trade-off.
- Result and revisit trigger.

### Evaluation and testing

- Baseline and target.
- Dataset and slice design.
- Deterministic, model-based, and human checks.
- Offline results with uncertainty.
- Online or operational validation.
- Regression and release policy.

### Operations

- Rollout and rollback.
- SLOs, alerts, dashboards, and ownership.
- Capacity and cost model.
- Incident or near miss.
- Runbook and support model.

### Results and reflection

- Measured outcomes and their source.
- Qualitative evidence and its limitations.
- Unmet goals or unknown effects.
- What changed after launch.
- What you would repeat, change, or stop.
- Staff-level leverage, if applicable: standards, interfaces, migration, adoption, or cross-team direction.

## Evidence Checklist

Use evidence to refresh your memory and validate claims. Remove confidential material before sharing.

- [ ] Repository or approved code excerpts that show your contribution.
- [ ] Unit, integration, contract, end-to-end, load, and security tests.
- [ ] Architecture, sequence, deployment, and trust-boundary diagrams.
- [ ] Dashboard screenshots or metric definitions with dates and scope.
- [ ] Evaluation dataset description, version, categories, and provenance.
- [ ] Evaluation results, confidence or sample limitations, and failure slices.
- [ ] Product experiment or customer acceptance evidence.
- [ ] Runbook, alert definitions, escalation path, and rollback steps.
- [ ] Architecture decision records or decision log.
- [ ] Incident review and follow-up actions.
- [ ] Launch plan, migration plan, or customer handoff.
- [ ] Cost estimate and actual-cost comparison where available.
- [ ] Feedback showing adoption, correction, support burden, or unmet needs.
- [ ] A clear list of what the team did and what you personally did.
- [ ] Disclosure boundaries for confidential, proprietary, customer, or regulated information.

You normally will not present all of these artifacts. They make your verbal account more accurate and give you optional material for an approved presentation.

## Apply the Role Lens

Use the same facts, but change emphasis according to the target role. Do not rewrite your contribution to fit a title.

### Product AI Engineer

Lead with:

- User job, current workaround, product hypothesis, and baseline.
- Why AI was appropriate and where deterministic behavior remained.
- End-to-end experience, uncertainty UX, and recovery.
- Evaluation design, failure taxonomy, feedback, and experimentation.
- Quality, latency, cost, safety, and adoption trade-offs.
- Launch sequence and product iteration.

Likely weak signals:

- Starting with model or framework selection.
- Reporting only offline model metrics.
- No user behavior, product outcome, or correction path.
- Treating RAG or agents as the product rather than implementation choices.

See [Product AI Engineer preparation](04-product-ai-engineer.md).

### Forward Deployed Engineer

Lead with:

- Customer workflow, sponsor, users, and acceptance criteria.
- Discovery that changed the stated problem.
- Existing data, API, identity, network, security, and deployment constraints.
- Proof-of-concept boundary and production hardening path.
- Scope negotiation, risks, ownership, communication, and handoff.
- Adoption, support, incident response, and field-to-product learning.

Likely weak signals:

- Describing a demo without production integration.
- Ignoring customer ownership, readiness, or change management.
- Agreeing to requested architecture without challenging assumptions.
- Building customer-specific complexity without a maintenance or reuse decision.

See [Forward Deployed Engineer preparation](05-forward-deployed-engineer.md).

### ML/AI Platform Engineer

Lead with:

- Internal customer and repeated problem worth centralizing.
- Platform contract, paved road, extension points, and ownership boundary.
- Multi-tenancy, isolation, reliability, capacity, and cost.
- Control-plane and data-plane design.
- Developer experience, migration, adoption, and support load.
- SLOs, incident response, rollout, and escape hatches.

Likely weak signals:

- Infrastructure without internal-user discovery.
- A platform built before repeated demand was established.
- Utilization presented as the only outcome.
- No tenant isolation, migration, operational contract, or adoption plan.

See [ML/AI Platform Engineer preparation](06-ml-ai-platform-engineer.md).

## Synthesized Project Deep-Dive Questions

The 36 questions below are synthesized practice prompts. They are not attributed to, or requirements from, any company. Fifteen questions include a concise strong-answer rubric and likely follow-ups.

### Context, scope, and ownership

1. [Synthesized] Walk me through the project and explain why it mattered.
   - Strong-answer rubric - Names the user, workflow, baseline, stakes, personal scope, key decision, and strongest truthful outcome in under two minutes.
   - Likely follow-ups - Why then? Who disagreed? What would have happened without the project?
2. [Synthesized] What did you personally own, and what did others own?
   - Strong-answer rubric - Separates decisions, implementation, influence, and operational responsibility without using "we" to obscure attribution.
   - Likely follow-ups - Which decision could you make independently? Where did you need approval? Who deserves credit?
3. [Synthesized] How did you know this was the right problem to solve?
   - Strong-answer rubric - Uses workflow evidence, baseline pain, frequency, consequence, and a falsifiable success condition rather than executive preference alone.
   - Likely follow-ups - What evidence was weak? What alternative problem competed for resources?
4. [Synthesized] Which requirement was hardest to clarify?
5. [Synthesized] What was explicitly out of scope, and how did you hold that boundary?
6. [Synthesized] How did the project scope or objective change after work began?

### Architecture and technical decisions

7. [Synthesized] Draw the architecture and trace one request end to end.
   - Strong-answer rubric - Shows data and control flow, state, identity, trust and failure boundaries, model calls, persistence, observability, and user-visible response.
   - Likely follow-ups - Where can data be lost? What is synchronous? Which component owns retries?
8. [Synthesized] What was the most consequential technical decision?
   - Strong-answer rubric - Gives requirements, two credible alternatives, decision criteria, evidence available then, accepted trade-off, and revisit trigger.
   - Likely follow-ups - Who challenged it? What evidence would reverse it? Was the decision reversible?
9. [Synthesized] Why did you choose this model, and how did you compare it?
   - Strong-answer rubric - Uses task-specific quality, structured behavior, latency, cost, privacy, context, and operational evidence; avoids generic benchmark claims.
   - Likely follow-ups - What happens when the model changes? Why not a smaller or self-hosted model?
10. [Synthesized] Why did this system need RAG, and where did retrieval fail?
11. [Synthesized] Why did this workflow need an agent rather than deterministic orchestration?
   - Strong-answer rubric - Identifies the bounded decision that required adaptation, limits tools and steps, controls side effects, and explains termination, audit, and fallback.
   - Likely follow-ups - What could be a state machine? How do you prevent loops? Which actions require approval?
12. [Synthesized] Which component would fail first at ten times the load?
13. [Synthesized] How did you version prompts, models, schemas, retrieval indexes, and tools?
14. [Synthesized] What did you build that you later removed or simplify?

### Data and evaluation

15. [Synthesized] How did you create the evaluation dataset?
   - Strong-answer rubric - Explains provenance, permissions, representative slices, hard negatives, leakage controls, versioning, human ownership, and known gaps.
   - Likely follow-ups - How large was it and why? How did production failures enter it? Who adjudicated disagreements?
16. [Synthesized] How did you know the system was good enough to launch?
   - Strong-answer rubric - Combines baseline comparison, release thresholds, critical slices, human review, safety gates, operational tests, and a risk-based rollout.
   - Likely follow-ups - Which metric could improve while users suffered? Who accepted residual risk?
17. [Synthesized] How did offline evaluation relate to online outcomes?
18. [Synthesized] Which failure category was most important but least frequent?
19. [Synthesized] How did you validate model-based graders or human labels?
20. [Synthesized] What data leakage, bias, drift, or feedback-loop risk did you encounter?

### Production, reliability, and security

21. [Synthesized] Tell me about a production incident or near miss.
   - Strong-answer rubric - Gives impact and timeline, containment, contributing factors, evidence-based diagnosis, communication, recovery, and durable changes without blame.
   - Likely follow-ups - Why did monitoring miss it? What was the rollback? Which action prevented recurrence?
22. [Synthesized] What happened when the model provider or a critical dependency failed?
23. [Synthesized] How did you secure retrieved content and agent tools?
   - Strong-answer rubric - Preserves authorization, treats content as untrusted, limits tool permissions and egress, validates outputs, gates side effects, and records audit events.
   - Likely follow-ups - How would indirect prompt injection work? What appeared in logs? How were secrets rotated?
24. [Synthesized] Which SLOs and alerts mattered, and what action did each trigger?
25. [Synthesized] How did you roll out and roll back model or prompt changes?
26. [Synthesized] How did you protect tenant data across queues, caches, vector stores, and logs?

### Cost, outcomes, and evolution

27. [Synthesized] What drove cost, and how did you calculate cost per useful outcome?
   - Strong-answer rubric - Includes full-path demand, token or compute usage, retries, caching, evaluation, storage, observability, uncertainty, and quality trade-offs.
   - Likely follow-ups - What changes at peak? Which optimization had the best return? Who owned the budget?
28. [Synthesized] What measurable outcome can you defend?
   - Strong-answer rubric - Names source, period, population, baseline, measurement method, and limitations; uses ranges or qualitative evidence honestly when exact metrics are unavailable.
   - Likely follow-ups - Was it causal? What metric did not improve? Can you separate adoption from value?
29. [Synthesized] What would you do differently if you started now?
   - Strong-answer rubric - Respects the original constraints, identifies new evidence, proposes a concrete change, and explains why it was not obvious or affordable then.
   - Likely follow-ups - Which original decision was wrong? What would you keep? What is the first experiment?
30. [Synthesized] When did you decide to harden, scale, platformize, or stop?
31. [Synthesized] Which outcome remained unknown after launch?
32. [Synthesized] What technical debt was intentional, and what was accidental?

### Leadership and role fit

33. [Synthesized] Describe a disagreement about architecture, scope, or launch readiness.
   - Strong-answer rubric - Presents both positions fairly, identifies incentives and evidence, explains the decision process, and shows the relationship and outcome after disagreement.
   - Likely follow-ups - What would the other person say? When did you change your mind? Who made the final call?
34. [Synthesized] How did field or user evidence change the product or platform roadmap?
35. [Synthesized] What part of this project demonstrates senior or staff-level leverage?
36. [Synthesized] How would you adapt this project for the role you are interviewing for?

For additional prompts, use the existing [project deep-dive question bank](../questions/03-project-deep-dive.md). Convert questions into dialogue by asking two or three follow-ups after every initial answer.

## Take-Home Operating Strategy

The assignment and written clarifications are the source of truth. Do not add imagined requirements because they sound production-ready.

### Clarify scope

Before implementation, ask only questions that could change the design or evaluation:

- What is the expected time budget, deadline, and review format?
- Which requirements are mandatory, optional, or illustrative?
- What input volume, file types, concurrency, or latency should be assumed?
- Is a local demo sufficient, or is deployment expected?
- Which languages, frameworks, models, services, or environments are required or prohibited?
- Are paid APIs acceptable, and will reviewers have credentials?
- What data may be stored, logged, or sent to external providers?
- What is the policy for AI coding tools, generated code, and disclosure?
- What will reviewers score, and will there be a code-review or extension round?

If answers are unavailable, record assumptions in the README and proceed.

### Timebox

Convert the allowed time into a budget before coding. For an eight-hour assignment, a reasonable starting allocation is:

- 45 minutes - read, clarify, list assumptions, and define acceptance checks.
- 45 minutes - sketch architecture, repository, interfaces, and evaluation cases.
- 3 hours - implement the smallest end-to-end path.
- 1 hour - tests and failure handling.
- 45 minutes - evaluations and results.
- 45 minutes - README, decision log, and limitations.
- 30 minutes - demo recording or walkthrough preparation.
- 30 minutes - clean-environment verification and final review.

Adjust to the actual assignment. Stop expanding scope when the time budget is exhausted. Record unfinished work explicitly.

### Plan the vertical slice

Write a one-page plan:

- User-visible flow.
- Mandatory acceptance criteria.
- Inputs, outputs, interfaces, and boundaries.
- One architecture diagram.
- Three highest risks.
- Minimum test and evaluation set.
- Explicit cuts.
- Checkpoints at 25.0%, 50.0%, and 75.0% of the time budget.

Get one happy path working early, but do not confuse a happy path with completion.

### Implement for review

Prefer:

- Clear modules and dependency boundaries.
- Typed or validated request and response schemas.
- Configuration separated from code.
- Dependency injection around models, tools, clocks, and storage.
- Explicit errors, timeouts, and bounded retries.
- Deterministic seams for tests.
- Structured logs without secrets or sensitive content.
- One-command setup, test, evaluation, and demo.

Avoid:

- Framework abstractions that hide control flow.
- Multiple deployable services without a requirement.
- Distributed infrastructure for local-scale input.
- Unbounded agents or tool permissions.
- Polished UI that displaces correctness, tests, evaluation, or explanation.

### Test and evaluate

Build tests and evaluations as part of the implementation, not as an afterthought.

- Unit-test parsing, validation, routing, policy, scoring, and state transitions.
- Integration-test storage, model adapters, retrieval, tools, and APIs at their boundaries.
- Test unhappy paths: invalid input, empty results, timeout, malformed model output, duplicate request, partial tool failure, and unauthorized access.
- Create a small evaluation set before prompt or retrieval tuning.
- Report actual results, examples, failure categories, and limitations.
- Keep stochastic model calls out of the default unit-test path.

### Document and demonstrate

The README should let a reviewer understand and run the submission without a meeting. A short video can accelerate review but should not compensate for a broken setup.

In the demo:

- State the problem and scope.
- Run the primary workflow.
- Show one failure or refusal path.
- Show tests and evaluation results.
- Trace the architecture and one decision.
- Name limitations and the next change.

### Submit safely

- Use environment variables or a secret manager interface.
- Provide `.env.example` with fake values.
- Scan repository history and generated artifacts for secrets.
- Do not commit customer, proprietary, personal, or licensed data without permission.
- Pin or lock dependencies as appropriate.
- Verify license and usage constraints for data, models, and packages.
- State external network calls and data sent to providers.
- Confirm the repository permissions and recipient list.
- Follow the requested naming, branch, archive, or submission method.

### Disclose AI-tool use

Follow the company's stated policy. If the policy is silent, ask. If no answer is available, disclose material use concisely:

- Tool and purpose.
- Which parts received assistance.
- How you reviewed, tested, and take responsibility for the result.
- Any generated assets or code with licensing implications.

Do not claim authorship of code you cannot explain. Assume every line may be discussed or modified live.

### Decide what to cut

Cut in this order unless the assignment says otherwise:

1. Extra UI polish.
2. Optional providers, file types, and integrations.
3. Premature caching, queues, and distributed deployment.
4. Broad configuration and plugin systems.
5. Advanced retrieval or multi-agent orchestration.
6. Deployment automation that is not required.

Protect:

- Mandatory behavior.
- A working vertical slice.
- Input validation and safe failure.
- Core tests.
- Small, relevant evaluations.
- Setup and decision documentation.
- Security basics and secret handling.

## Practical Repository Structure

Adapt names to the language and assignment. A compact structure is:

```text
.
├── README.md
├── pyproject.toml
├── .env.example
├── src/
│   ├── api/
│   ├── domain/
│   ├── services/
│   ├── adapters/
│   └── config.py
├── tests/
│   ├── unit/
│   ├── integration/
│   └── fixtures/
├── evals/
│   ├── dataset.jsonl
│   ├── run.py
│   └── results/
├── docs/
│   ├── architecture.md
│   ├── decisions.md
│   ├── test-plan.md
│   ├── eval-plan.md
│   └── demo-script.md
├── scripts/
│   ├── setup.sh
│   └── demo.sh
└── docker-compose.yml
```

Do not add empty directories merely to resemble production. Every artifact should help the reviewer run, inspect, test, or defend the system.

## README Outline

1. Problem and user.
2. Scope, mandatory behavior, assumptions, and non-goals.
3. What works, with a short example.
4. Architecture and request flow.
5. Setup and prerequisites.
6. Configuration and external services.
7. Run commands.
8. Test commands and coverage boundaries.
9. Evaluation dataset, method, results, and limitations.
10. Security and privacy considerations.
11. Key decisions and alternatives.
12. Failure behavior and operational notes.
13. Known limitations.
14. Next steps in priority order.
15. AI-tool disclosure, if required or appropriate.

Use exact commands. Test them from a clean environment.

## Decision Log Template

Keep decisions short and dated:

```text
Decision: Use deterministic workflow with one model classification step
Date: YYYY-MM-DD
Status: Accepted
Context: The assignment requires three known actions and a four-hour implementation limit.
Options: Free-form agent; explicit state machine; rule-only routing.
Choice: Explicit state machine with model classification and schema validation.
Why: Preserves flexibility in intent recognition while keeping actions testable and bounded.
Trade-offs: New actions require code changes; ambiguous intent may need clarification.
Evidence: Evaluation cases cover supported, ambiguous, and unsupported requests.
Revisit when: The action set becomes dynamic or multi-step planning is an observed requirement.
```

Record only decisions with meaningful alternatives.

## Test Plan Template

### Objectives

- Verify mandatory behavior and contracts.
- Verify safe behavior under invalid input and dependency failure.
- Keep model-dependent behavior observable without making unit tests flaky.

### Test layers

- Unit - validation, parsing, chunking, ranking, routing, policy, budget, state, and formatting.
- Contract - model, tool, storage, provider, and API adapter schemas.
- Integration - real or containerized dependencies where practical.
- End to end - one primary flow and one important failure flow.
- Nonfunctional - focused latency, concurrency, security, or load checks only when relevant.

### Required cases

- [ ] Happy path.
- [ ] Empty and malformed input.
- [ ] Boundary-size input.
- [ ] Dependency timeout and error.
- [ ] Malformed or schema-invalid model output.
- [ ] Duplicate or replayed request.
- [ ] Unauthorized or cross-tenant request.
- [ ] Unsupported or unanswerable request.
- [ ] Destructive action without approval.
- [ ] Regression for each discovered bug.

### Reporting

State:

- Commands run.
- Passing and failing counts.
- Mocked versus real dependencies.
- Coverage exclusions.
- Known untested risks.

## Evaluation Plan Template

### Decision

State what the evaluation will decide, such as whether retrieval strategy A is good enough for the minimum viable release.

### Dataset

- Source and permission.
- Number of examples and why that is sufficient for this timebox.
- Categories and difficult slices.
- Expected answer, evidence, action, or outcome.
- Unanswerable, adversarial, and malformed cases.
- Version and change policy.

### Metrics and graders

- Deterministic correctness for schemas, citations, tool selection, permissions, and state.
- Task-specific quality measures for retrieval, generation, or workflow completion.
- Human review for nuanced usefulness or risk.
- Model-based grading only with a rubric, calibration examples, and acknowledged limitations.
- Latency and cost per case where relevant.

### Release criteria

- Threshold for mandatory behavior.
- Zero-tolerance safety or authorization failures.
- Acceptable quality by critical slice.
- Maximum latency or cost if required.
- Manual review criteria.

### Results

Report:

- Aggregate result.
- Slice results.
- Representative successes and failures.
- Variability and sample limitations.
- Changes made after evaluation.
- Remaining risk and next experiment.

## Demo Script

Use a five- to eight-minute walkthrough unless instructed otherwise:

1. 30 seconds - problem, user, and scoped objective.
2. 30 seconds - assumptions and explicit non-goals.
3. 90 seconds - run the primary workflow.
4. 60 seconds - show an unanswerable, unauthorized, or dependency-failure path.
5. 60 seconds - architecture and one request trace.
6. 60 seconds - tests and evaluation results.
7. 60 seconds - key decision and rejected alternative.
8. 30 seconds - limitations, next step, and exact run command.

Keep backup output for unreliable external APIs, but disclose when a result is recorded rather than live.

## Three Take-Home Archetypes

These archetypes are preparation scaffolds, not company requirements.

### RAG or document assistant

Minimum viable:

- Ingest one documented file type or a provided corpus.
- Parse and chunk deterministically.
- Embed and retrieve with a simple local or managed index.
- Answer from retrieved context with source references.
- Refuse or qualify when evidence is insufficient.
- Include a small dataset spanning answerable, unanswerable, and ambiguous cases.
- Test parsing, retrieval filters, citation formatting, and failure behavior.
- Document data flow, limitations, and setup.

Strong:

- Compare a baseline against one improved retrieval strategy.
- Preserve document or tenant authorization in retrieval.
- Add metadata filtering, reranking, or hybrid search only when evals justify it.
- Validate citations against retrieved spans.
- Version the corpus and evaluation set.
- Show latency, cost, retrieval metrics, answer metrics, and failure slices.
- Handle malformed documents and provider failures.

Over-engineered:

- Multiple vector databases or model providers without a requirement.
- Distributed ingestion, queues, and Kubernetes for a small static corpus.
- Knowledge graphs, query decomposition, or agentic retrieval without evidence.
- Elaborate UI while grounding, refusal, tests, or evals remain weak.
- Claiming production readiness without access control, monitoring, or operational ownership.

### Agent workflow or integration

Minimum viable:

- Support a small, explicit set of tools.
- Use validated tool inputs and outputs.
- Keep state and control flow inspectable.
- Bound steps, time, and cost.
- Require approval before consequential side effects.
- Handle unsupported requests, tool errors, and duplicate actions.
- Include unit tests for routing, policy, state transitions, and termination.
- Provide execution traces without exposing secrets.

Strong:

- Justify which decisions require model adaptation and which remain deterministic.
- Use idempotency keys, previews, compensation, or undo where appropriate.
- Test prompt injection, permission boundaries, malformed tool output, loops, and partial failure.
- Evaluate task completion, tool choice, policy compliance, latency, and cost.
- Separate user identity, tool authorization, and model context.
- Include replayable traces and a clear failure taxonomy.

Over-engineered:

- Multiple agents for roles that ordinary functions can perform.
- Open-ended tool discovery or shell access.
- Unbounded planning, recursion, memory, or retries.
- A custom orchestration framework built instead of the requested workflow.
- Simulated autonomy without realistic permissions, failure behavior, or evaluation.

### Model gateway or evaluation service

Minimum viable:

- Expose one stable request and response contract.
- Adapt two providers or one provider plus a deterministic fake.
- Apply timeouts, bounded retries, and normalized errors.
- Record model, version, latency, token usage, and request outcome.
- Provide a small evaluation runner and versioned cases.
- Keep credentials out of code and logs.
- Test adapter contracts, routing, malformed output, and provider failure.

Strong:

- Route by explicit policy such as task, quality tier, latency budget, or data constraint.
- Add fallback with tested semantic and operational behavior.
- Enforce budgets, quotas, or tenant policy.
- Separate online request serving from offline evaluation.
- Calibrate model-based graders and preserve raw evidence safely.
- Show cost-quality-latency comparisons and regression gates.
- Include trace correlation, audit events, and a migration or versioning strategy.

Over-engineered:

- Dynamic routing learned from insufficient data.
- Semantic caching without privacy, staleness, or correctness analysis.
- A distributed control plane, service mesh, or autoscaling platform for local review.
- Provider-specific features leaking through a supposedly stable contract.
- Dashboards with fabricated traffic instead of meaningful tests and evaluation evidence.

For more examples and source-backed research, use the existing [home-assignment guide](../questions/06-home-assignments.md).

## Prepare for Code Review

Assume the reviewer will ask you to navigate, critique, and modify the submission.

Before the review:

- Re-read every file and remove code you cannot explain.
- Trace the primary request without an IDE search.
- Identify three intentional shortcuts and their consequences.
- Identify the weakest module and propose a bounded refactor.
- Know where validation, authorization, retries, logging, and configuration occur.
- Run tests, evaluations, formatting, linting, and type checks.
- Inspect dependency and secret scans if available.
- Practice reviewing your own diff for correctness, security, testability, and unnecessary complexity.

During the review:

- Explain intent before mechanics.
- Acknowledge defects directly.
- Distinguish a bug from a timeboxed limitation.
- Ask whether the reviewer wants diagnosis, design discussion, or a live fix.
- Think aloud about invariants, edge cases, and test impact.
- Prefer a small safe change over an unverified rewrite.

Likely review prompts:

- What is the least maintainable part?
- Where is control flow hidden?
- What happens under concurrent requests?
- Which test gives false confidence?
- What should be an interface versus a function?
- Where could sensitive data leak?
- What would you delete?

## Prepare for a Live Extension

Practice extensions that fit in 20-40 minutes:

- Add a new validated tool or provider adapter.
- Add an authorization or metadata filter.
- Handle a timeout, malformed response, or duplicate request.
- Add one evaluation slice and regression test.
- Change routing policy without breaking contracts.
- Add a citation or audit field through the stack.
- Refactor a dependency behind a testable interface.

Use this sequence:

1. Restate behavior and constraints.
2. Identify affected contracts and tests.
3. Implement the narrowest vertical change.
4. Run focused tests.
5. Check adjacent failure modes.
6. Summarize the trade-off and remaining work.

Do not silently rely on AI tools during a live extension. Follow the stated policy and narrate what you are doing.

## Common Failure Modes

### Project deep dives

- Selecting a famous project where your ownership was narrow.
- Starting with a technology list instead of the problem and baseline.
- Saying "we" when asked about personal contribution.
- Reporting metrics without source, period, denominator, or limitation.
- Describing the final architecture but not how it evolved.
- Offering fake alternatives that were never credible.
- Treating model quality, service reliability, and product value as one metric.
- Avoiding incidents, conflict, or wrong decisions.
- Claiming staff scope from technical complexity alone.
- Giving a memorized monologue that does not answer the question asked.

### Take-homes

- Coding before clarifying mandatory behavior.
- Spending most of the time on UI or infrastructure.
- Adding agents, services, or abstractions without a requirement.
- Omitting a baseline, evaluation set, or failure examples.
- Testing only deterministic helpers while the core workflow remains untested.
- Requiring undocumented credentials or manual setup.
- Committing secrets, private data, model outputs with sensitive content, or oversized artifacts.
- Hiding known failures or presenting mocked behavior as real.
- Failing to disclose material AI-tool use when required.
- Submitting code that cannot be explained or extended live.

## Mock Deep-Dive Format

Run a 45-minute mock with a partner using [mock interviews and scorecards](09-mock-interviews-and-scorecards.md).

### Interviewer

- Minutes 0-2 - ask the candidate to choose and summarize a project.
- Minutes 2-8 - probe context, role, requirements, baseline, and outcome.
- Minutes 8-20 - request an architecture trace and challenge two decisions.
- Minutes 20-28 - probe data, evaluation, security, reliability, and cost.
- Minutes 28-35 - probe an incident, disagreement, or failed assumption.
- Minutes 35-40 - ask role-specific and counterfactual questions.
- Minutes 40-45 - give evidence-based feedback and scores.

Use progressive follow-ups:

- Why?
- What evidence supported that?
- What did you reject?
- What failed?
- How did you know?
- What would change under a different constraint?
- What exactly did you do?

### Candidate

- Begin with the 60-second narrative.
- Ask whether the interviewer wants the architecture or decision path first.
- Draw while explaining one concrete flow.
- Answer directly before adding context.
- Label measured facts, estimates, assumptions, and hindsight.
- Stop after answering and allow the next question.

### Observer

Record:

- Claims that lacked evidence.
- Places where ownership was unclear.
- Decisions without alternatives or criteria.
- Missing operational, security, cost, or evaluation detail.
- Answers that exceeded two minutes without a check-in.
- Follow-ups that caused confusion or contradiction.

## Scorecard

Use the canonical scale from [module 09](09-mock-interviews-and-scorecards.md#common-scoring-scale). Score each dimension from 1 to 4:

- 1 - weak or unsafe; absent, incorrect, materially misleading, or usable only after direct rescue.
- 2 - partial; needs substantial prompting or stays generic.
- 3 - interview-ready; specific, credible, independent, and appropriate for senior scope.
- 4 - strong senior or staff evidence; connects evidence, trade-offs, failure modes, adaptation, and broader leverage without overclaiming.

Dimensions:

1. Problem framing and baseline.
2. Personal ownership and decision authority.
3. Architecture clarity and implementation depth.
4. Data and model judgment.
5. Evaluation and outcome evidence.
6. Reliability, deployment, and incident response.
7. Security, privacy, and safety.
8. Cost, capacity, and operational economics.
9. Alternatives, trade-offs, and evolution.
10. Communication and adaptation to follow-ups.
11. Role fit.
12. Senior or staff leverage.

Interpretation:

- 12-23 - weak profile. Rebuild the dossier and close factual, safety, ownership, or technical gaps before more mocks.
- 24-32 - developing profile. The project is usable, but repeated probing exposes important gaps.
- 33-41 - practice-ready profile. Evidence is broadly credible; repair every required dimension below 3.
- 42-48 - strong profile. Confirm the repeated-mock readiness rules before declaring the format ready.

The minimum is 12 and the maximum is 48. A total score cannot confer readiness or compensate for a 1 in personal ownership, architecture depth, truthful outcome evidence, or safety. A staff-level target should score at least 3 on leverage and influence, not only technical complexity.

## Readiness Gate

[Module 09 readiness rules](09-mock-interviews-and-scorecards.md#readiness-rules) are canonical. The requirements below add project and take-home evidence; they do not replace or weaken the canonical rules.

You are ready to use a project when:

- [ ] I can deliver its 60-second, 5-minute, and 20-30-minute versions.
- [ ] I can state the user, baseline, constraints, non-goals, and success criteria.
- [ ] I can separate my contribution from the team's contribution.
- [ ] I can draw the architecture and trace data, identity, control, and failure paths.
- [ ] I can defend three decisions against credible alternatives.
- [ ] I can explain data, model, RAG, or agent choices at implementation depth where relevant.
- [ ] I can describe evaluation design, results, slices, and limitations.
- [ ] I can explain deployment, rollback, monitoring, cost, and security.
- [ ] I have one incident, failure, or wrong assumption and its durable follow-up.
- [ ] Every metric is sourced, scoped, and honestly labeled.
- [ ] I know what is confidential and how I will discuss it safely.
- [ ] I have adapted the emphasis to the target role.
- [ ] My three most recent full project mocks used different prompts or probe sets.
- [ ] At least two mocks were scored by different interviewers, or one was independently double-scored.
- [ ] Every required dimension scored at least 3 in at least two of the three mocks.
- [ ] No required dimension scored 1 in either of the two most recent mocks.
- [ ] I finished the core scope within time in at least two mocks.
- [ ] I handled at least one material follow-up without direct rescue in each of the two most recent mocks.
- [ ] Every known repeated failure completed the focused and full re-tests required by module 09.
- [ ] No unresolved hard fail remains.

You are ready to submit a take-home when:

- [ ] Mandatory behavior works from a clean environment.
- [ ] Setup, test, evaluation, and demo commands are exact.
- [ ] Core happy and unhappy paths are tested.
- [ ] The evaluation set and actual results are included.
- [ ] Assumptions, non-goals, decisions, limitations, and next steps are explicit.
- [ ] Secrets and sensitive data are absent from files, logs, outputs, and history.
- [ ] External data and model use are disclosed appropriately.
- [ ] AI-tool use follows the stated policy and is disclosed when required.
- [ ] I can explain and modify every important part of the submission.
- [ ] I stopped at the timebox and did not hide unfinished work.

No total or score band overrides the per-dimension, timing, follow-up, independence, hard-fail, and re-test requirements.

## Related Preparation

- [Senior AI and FDE curriculum](README.md) - Diagnostic, tracks, schedule, and readiness expectations.
- [Common core](01-common-core.md) - APIs, data, ML, LLMs, evaluation, security, reliability, latency, and cost.
- [AI/ML system design](03-ai-ml-system-design.md) - Reusable architecture and estimation method.
- [Product AI Engineer](04-product-ai-engineer.md) - User-facing product, evaluation, UX, and iteration lens.
- [Forward Deployed Engineer](05-forward-deployed-engineer.md) - Discovery, customer integration, deployment, and handoff lens.
- [ML/AI Platform Engineer](06-ml-ai-platform-engineer.md) - Platform contract, multi-tenancy, reliability, capacity, and adoption lens.
- [Senior and staff behavioral](07-senior-staff-behavioral.md) - Ownership, influence, conflict, failure, and level calibration.
- [Mock interviews and scorecards](09-mock-interviews-and-scorecards.md) - Timed practice and observable scoring.
- [Existing project deep-dive questions](../questions/03-project-deep-dive.md) - Source-backed question patterns and follow-up probes.
- [Existing home assignments](../questions/06-home-assignments.md) - Assignment research, examples, and source links.
- [Portfolio guide](../../portfolio/README.md) - Strengthen project evidence with realistic data, tests, evaluation, and documentation.

Use the dossiers to become more accurate, not more theatrical. The strongest deep dive and take-home show that you can choose the right problem, build the smallest credible system, operate it responsibly, measure what happened, and change course when the evidence demands it.
