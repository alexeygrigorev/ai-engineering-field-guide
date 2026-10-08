# Senior Forward Deployed Engineer Interview Preparation

This module prepares senior and staff candidates for Forward Deployed Engineer interviews. It fits the eight-week curriculum in [`README.md`](README.md): use the shared foundation in [`01-common-core.md`](01-common-core.md), the design method in [`03-ai-ml-system-design.md`](03-ai-ml-system-design.md), and this module for customer-facing delivery practice.

The goal is to show that you can enter an unfamiliar customer environment, discover the real problem, agree on measurable scope, build and integrate a production system, manage delivery risk, and turn field evidence into product direction. A polished demo is not enough. The interviewer needs evidence that you can own the path from ambiguity to a supported outcome.

Use the source-based [FDE video mock question set](../questions/10-video-mock-fde.md) for a complete practice round covering client scoping, live coding, AI concepts, and system design.

The repository's [FDE role analysis](../../role/06-fde.md) is the source for market claims in this guide. Its dataset contains 146 deduplicated direct-title roles from 94 companies collected through July 2026. Of those postings, 90.0% mention building or deploying production systems, 88.0% mention direct customer work, 64.0% mention integration, and 52.0% mention discovery or requirements scoping. Treat these figures as evidence about the sampled postings, not as a universal job definition or a prediction of any company's interview.

## Define the Role Before Preparing

An FDE combines customer discovery with engineering delivery. The center of gravity is the customer outcome inside a real environment: existing data, identity, networking, security review, operational ownership, deadlines, and commercial commitments all affect the design.

The [role analysis](../../role/06-fde.md) supports this combination. In the same 146-role sample, production work and customer interaction appear in about nine in ten postings, while integration appears in nearly two thirds. Evaluation, testing, or monitoring appears in 49.0%; field-to-product feedback in 31.0%; and prototypes, proofs of concept, or demos in 29.0%. Taken together, the data supports production ownership beyond prototyping. The adjacent-role comparisons below, including the distinction from generic consulting, are synthesized preparation framing rather than conclusions from the dataset.

### Direct market evidence and preparation priority

This is direct title-specific evidence from [146 deduplicated direct-title FDE roles](../../role/06-fde.md), not a proxy from adjacent titles. The source reports production work in 90.0% of postings, direct customer work in 88.0%, and 91.0% classified as customer-facing. Python appears in 91.0%, integration in 64.0%, and discovery or requirements scoping in 52.0%. AI-specific mentions include prompt engineering at 55.0%, `RAG` at 52.0%, evaluation, testing, or monitoring at 49.0%, and agents at 42.0%. POCs, prototypes, or demos appear in 29.0%, while travel or onsite work appears in 9.0%. These percentages preserve the source's rounding and describe the sampled postings, not every employer's loop.

Use this market-informed default:

- P0 - Production delivery, customer discovery, Python, and integration. Practice moving from an ambiguous workflow through production-quality code, customer systems, acceptance criteria, deployment, and operational ownership.
- P1 - `RAG`, prompt engineering, evaluation, agents, and cloud deployment. Apply them inside customer constraints rather than as isolated framework questions.
- P2 - Demos, POCs, adoption, and product feedback. Show how field evidence supports a production investment or reusable product change.
- P3 - Travel logistics and model training or fine-tuning. Confirm travel directly, and study training depth only when the target role requires it.

Override this default whenever the job description or recruiter confirms a different ownership boundary or interview loop.

Actual boundaries vary by company. Ask the recruiter:

- Which stages does the FDE own: discovery, design, implementation, deployment, support, expansion, or handoff?
- How much code is customer-specific versus part of the core product?
- Who owns the account relationship, commercial terms, product roadmap, security review, and production support?
- What environments are common: vendor cloud, customer cloud, private network, on-premises, or air-gapped?
- How are utilization, delivery, adoption, reliability, expansion, and reusable product improvements measured?
- How much travel or onsite work is expected, and how predictable is it?

The role analysis found travel or onsite language in 9.0% of the 146 sampled postings. That number does not mean travel is rare in every FDE job; postings can omit practical expectations. Confirm the actual cadence, geography, notice period, and whether incident or launch support changes it.

### Contrast with adjacent roles

These are preparation distinctions, not rigid title definitions.

- Product AI Engineer - starts from a reusable user or product problem and owns product quality, evaluation, UX, and iteration across users. An FDE starts from a named customer's workflow and environment, then decides what can remain configuration, what requires integration, and what should become product.
- Solutions or Sales Engineer - usually emphasizes technical discovery, solution fit, demos, and pre-sales validation. An FDE is more likely to write production code, own integration and deployment, and remain accountable after the technical sale. Some companies combine these responsibilities.
- Consulting engineer - may advise, implement, or transform a customer process across many vendors. An FDE is normally tied more closely to a product or technical platform and should feed repeated field lessons back into it.
- ML/AI Platform Engineer - builds shared infrastructure and interfaces for application teams. An FDE consumes, extends, and sometimes shapes those capabilities while solving customer-specific data, security, deployment, and adoption constraints.
- Customer success or implementation specialist - usually emphasizes onboarding, configuration, enablement, and adoption. An FDE should be ready to make architectural decisions and build or debug production software where standard configuration is insufficient.

A strong interview answer does not defend one title definition. It identifies the operating model, names the ownership boundaries, and adapts its examples to the employer's actual role.

## What Interviewers Look For

### Discovery under ambiguity

You can turn a request such as "we need an AI agent" into a workflow, users, decision, baseline, constraints, risks, owners, and measurable success. You distinguish facts from assumptions and identify the unknown that could invalidate the project.

### Customer communication

You listen before prescribing, explain technical choices at the audience's level, write decisions down, and communicate bad news early. You can challenge a requested design without dismissing the underlying need.

### Production coding

You can build, test, review, deploy, and operate production software. Python appears in 91.0% of the 146 postings in the [role analysis](../../role/06-fde.md), but interviews may test another language or practical integration work. Prepare for APIs, SQL, data transformations, concurrency, error handling, tests, and debugging.

### Integration judgment

You can map customer data, APIs, identity, networks, security controls, and operational systems. You define contracts, detect data-quality problems, handle schema drift, and preserve authorization through every layer.

### Architecture

You choose a design that fits the current environment and a credible path to production. You can deploy across different clouds or on-premises without assuming identical services. In the 146-role sample, the role analysis found AWS in 47.0% of postings, GCP in 38.0%, Azure in 34.0%, Docker in 40.0%, Kubernetes in 35.0%, and CI/CD in 34.0%. These are overlapping mentions, not market shares. They support preparing for varied environments rather than memorizing one cloud.

### Delivery ownership

You sequence discovery, proof of concept, hardening, rollout, support, and handoff. You expose risks, resolve blockers, revise plans, and define who owns the system after launch.

### Product feedback

You separate one customer's request from a repeated product gap. You collect evidence across accounts, propose a reusable interface or capability, and close the loop with product and platform teams.

### Commercial judgment

You can protect trust and delivery economics without acting as the salesperson. You understand that scope, time, support burden, opportunity cost, adoption, renewal risk, and strategic learning affect technical choices.

## The FDE Answer Method

Use this method for discovery, architecture, incidents, and behavioral cases:

1. Establish the customer outcome - user, workflow, current pain, consequence, sponsor, and why now.
2. Clarify the current state - systems, data, identity, security, operations, owners, and existing baseline.
3. Define the decision - what must be learned or delivered, by when, and what is explicitly outside scope.
4. State assumptions and unknowns - label each one and give the fastest safe validation.
5. Propose the thinnest credible path - begin with a reversible spike or narrow workflow rather than the final platform.
6. Define acceptance - technical, user, operational, security, and commercial success criteria.
7. Assign ownership - vendor, customer, shared, and third-party responsibilities.
8. Plan production behavior - reliability, observability, support, incident response, rollback, and handoff.
9. Communicate trade-offs - show the effect of each choice on time, quality, risk, cost, and reuse.
10. Close the loop - record decisions, next actions, owners, dates, and evidence that will change the plan.

In an interview, narrate where you are in the method. Do not spend the entire round asking questions. After enough discovery, summarize what you heard and make a provisional recommendation.

## Discovery and Requirement Decomposition

### Discovery call structure

For a 30-minute discovery role-play:

1. Minutes 0-3 - align on purpose, participants, and the decision this call should enable.
2. Minutes 3-10 - understand the user workflow, pain, baseline, and business consequence.
3. Minutes 10-17 - map data, systems, identity, security, deployment, and operations.
4. Minutes 17-22 - test urgency, constraints, decision authority, and customer capacity.
5. Minutes 22-26 - summarize requirements, assumptions, and top risks.
6. Minutes 26-30 - propose the next artifact, owners, evidence, and date.

Ask questions that change the plan:

- Who performs the workflow today, how often, and where does it fail?
- What decision or action should the system improve?
- What is the current baseline for quality, time, cost, and error?
- Which errors are merely inconvenient, and which are unacceptable?
- What data is authoritative, who owns it, and how fresh must it be?
- Which identities and permissions must carry through to the output or action?
- Where may data be processed, stored, logged, and retained?
- Which systems must be read, written, or notified?
- What must be demonstrated to security, operations, legal, or compliance?
- Who can approve scope, architecture, production access, and launch?
- What customer engineers, subject-matter experts, and users are available?
- What date matters, why does it matter, and what can be reduced if it cannot move?

Avoid a questionnaire recital. Follow the customer's language, probe contradictions, and periodically summarize.

### Requirement decomposition

Convert the conversation into:

- Outcome - measurable change in a customer workflow or decision
- Users - primary user, affected user, approver, and operator
- Functional scope - inputs, actions, outputs, supported cases, and non-goals
- Quality - task-specific acceptance, bad outcomes, abstention, and human review
- Data - sources, formats, volume, freshness, lineage, and deletion
- Integration - APIs, events, batch files, identity, networks, and rate limits
- Deployment - regions, cloud or on-premises target, runtime, secrets, and release path
- Operations - SLOs, alerts, support hours, runbooks, backup, recovery, and ownership
- Risk - security, privacy, safety, compliance, commercial, and schedule exposure
- Adoption - workflow entry point, training, champions, friction, and usage measurement
- Delivery - milestones, dependencies, owners, acceptance, and change control

Every requirement should be testable or explicitly marked as an assumption. "Enterprise ready" is not testable. "The caller can retrieve only documents permitted by the source system, permission revocations block reads within five minutes, and access decisions are auditable" is testable.

## Customer Architecture Mapping

Draw the current state before the target state. The current-state map reveals integration and ownership constraints that a reference architecture hides.

### Customer architecture checklist

Use this checklist during discovery and design:

- Business workflow
  - Trigger, actors, steps, handoffs, decisions, exceptions, and current workaround
  - Volume, seasonality, deadlines, and consequence of delay or error
- Users and identity
  - Human users, service identities, tenants, groups, roles, and source of truth
  - Authentication protocol, authorization model, provisioning, revocation, and break-glass access
- Data
  - Systems of record, owners, classifications, formats, volumes, quality, and freshness
  - Lineage, consent, residency, retention, deletion, legal hold, and backup
- Interfaces
  - APIs, events, queues, files, database access, webhooks, and user interfaces
  - Schema versions, rate limits, pagination, retries, idempotency, and sandbox fidelity
- Network
  - Ingress, egress, proxies, private links, DNS, certificates, firewalls, and allowlists
  - Connectivity from build, test, production, and support environments
- Runtime
  - Cloud accounts, regions, clusters, virtual machines, on-premises hosts, or air-gapped zones
  - Containers, orchestration, accelerators, storage, quotas, and approved base images
- Security
  - Threat model, secrets, encryption, keys, vulnerability management, audit, and incident obligations
  - Vendor review, model-provider policy, data processing terms, and operator access
- Delivery
  - Repositories, branching, CI/CD, artifact registry, infrastructure as code, approvals, and rollback
  - Environment promotion, change windows, release ownership, and separation of duties
- Operations
  - SLOs, telemetry, ticketing, on-call, escalation, runbooks, recovery objectives, and status communication
  - Log access, redaction, trace retention, and customer-visible health
- AI quality
  - Baseline, evaluation set, domain experts, critical slices, release gate, drift, and feedback
  - Prompt, model, retrieval, tool, and policy versioning
- Ownership
  - Accountable customer owner, technical owner, security approver, data owner, user champion, and vendor owner
  - Handoff conditions and responsibility after launch

Annotate trust boundaries, data movement, durable state, manual handoffs, single points of failure, and systems no participant can change.

## Integration and Deployment Depth

### Data and API integration

A strong answer covers:

- Contract discovery - schemas, examples, semantics, ownership, compatibility, and missing documentation
- Data profiling - completeness, validity, duplicates, skew, late arrival, identifiers, and representative edge cases
- Mapping - source-to-target fields, units, time zones, enumerations, null behavior, and semantic mismatches
- Reliable exchange - deadlines, bounded retries, idempotency, checkpoints, dead letters, replay, and reconciliation
- Change - schema versioning, additive versus breaking changes, backfills, dual reads or writes, and rollback
- Testing - fixtures, contract tests, integration tests, sandbox gaps, fault injection, and production canaries
- Operations - telemetry by customer and dependency, owner, runbook, rate limits, quota, and support boundary

When a sandbox is unrealistic, do not claim integration confidence from happy-path tests. Record gaps, use customer-approved sanitized samples, create a simulator for known failures, and run a controlled production validation.

### Identity and security integration

Treat authorization as a system property:

- Authenticate the user or workload at the boundary.
- Bind every request to tenant, principal, purpose, and approved scope.
- Enforce permissions outside the model and before sensitive data enters model context.
- Use short-lived, least-privilege credentials and keep secrets out of prompts and logs.
- Preserve source permissions in retrieval, caches, tools, exports, and audit.
- Define revocation, deletion, retention, residency, and operator access.
- Fail closed when identity or policy cannot be verified.
- Test cross-tenant, stale-permission, replay, confused-deputy, and prompt-injection paths.

### Cloud, on-premises, and restricted environments

Begin from constraints rather than translating cloud service names one for one:

- Managed vendor cloud - fastest operations path, but customer policy may restrict data, regions, networking, or provider use.
- Customer cloud account - stronger customer control, but requires account bootstrapping, private networking, identity federation, observability, upgrades, and shared support boundaries.
- On-premises or private data center - hardware procurement, capacity, disconnected upgrades, certificates, storage, backup, and local operations become first-class constraints.
- Air-gapped or heavily restricted - artifact import, dependency mirroring, license checks, offline evaluation, telemetry export, patching, and incident diagnosis need explicit workflows.

For each environment, define:

- Supported topology and minimum capacity
- Installation and upgrade mechanism
- Configuration and secret ownership
- Connectivity and dependency requirements
- Telemetry available to each party
- Backup, recovery, rollback, and uninstall
- Security patch and vulnerability process
- Compatibility test matrix and support lifecycle

Do not promise identical operations across every environment. Explain which capabilities are portable, which require adapters, and which environments need a separate support tier or are out of scope.

## Proof of Concept, Demo, and Production Path

### POC one-pager outline

Keep the proof of concept narrow enough to answer a decision:

1. Decision - what the customer and vendor will decide from the POC
2. Problem - user, workflow, current baseline, and consequence
3. Hypothesis - why the proposed capability should improve the outcome
4. In scope - one workflow, users, data slice, integrations, and environment
5. Out of scope - production scale, unsupported cases, automation, or hardening not included
6. Success criteria - quality, user, technical, security, schedule, and commercial evidence
7. Method - baseline, prototype, evaluation, demo, and user validation
8. Data and access - exact inputs, classifications, approvals, owners, and due dates
9. Architecture - temporary components, production assumptions, and known gaps
10. Milestones - checkpoints, decision reviews, final demonstration, and exit
11. Responsibilities - customer, vendor, and third-party owners
12. Risks - top risks, trigger, mitigation, contingency, and owner
13. Exit paths - proceed, revise, pause, or stop; cleanup and data deletion for each

A POC is not a production promise. Mark temporary controls and explain what hardening remains: tenancy, scale, reliability, security evidence, deployment automation, observability, support, documentation, and ownership.

### Demo plan

A demo should support a decision, not display every feature:

1. Audience and decision - who attends and what should be agreed afterward
2. Story - customer workflow, current friction, and target outcome
3. Scenarios - one representative happy path, one hard case, and one safe failure
4. Data - realistic and authorized examples with known expected results
5. Environment - pinned versions, seeded state, connectivity check, and backup
6. Narration - explain user value first, then relevant architecture and limitations
7. Evidence - quality results, latency, logs, citations, or audit trail
8. Boundaries - distinguish live behavior, mocked integration, and future work
9. Failure plan - screenshots or recording, alternate environment, and transparent recovery
10. Close - summarize evidence, unresolved risks, proposed scope, owners, and next decision

Never hide a mocked dependency or a precomputed result. Trust lost in a demo is harder to recover than a visible technical failure handled honestly.

### Production conversion

Before calling a pilot production-ready, close these gaps:

- Representative data and critical-slice evaluation
- Source authorization, tenant isolation, privacy, retention, and deletion
- Capacity, load, latency, quota, and cost tests
- Idempotency, retries, timeouts, backpressure, and graceful degradation
- Versioned deployment, canary, rollback, migration, and recovery
- Monitoring, alerts, runbooks, on-call, severity model, and status communication
- User workflow, training, support, adoption instrumentation, and feedback
- Ownership, service expectations, maintenance, handoff, and end-of-life

## Delivery, Adoption, and Difficult Situations

### Scope changes

When scope changes:

1. Restate the new need and why it matters.
2. Compare it with the agreed decision, acceptance criteria, and non-goals.
3. Assess impact on architecture, data, security, schedule, support, and reuse.
4. Offer explicit choices: swap scope, move date, add capacity, stage delivery, or decline.
5. Record the decision, owner, and revised acceptance criteria.

"We'll try" is not a scope decision. A senior FDE makes the trade-off visible without turning every conversation into contract negotiation.

### Stakeholder conflict

Map incentives before arguing:

- Executive sponsor - outcome, timing, strategic value, and confidence
- User - workflow fit, trust, speed, and disruption
- Customer engineering - integration effort, maintainability, and on-call burden
- Security or legal - control evidence, exposure, and accountability
- Product - repeatability, roadmap integrity, and opportunity cost
- Sales or account team - commitment, relationship, expansion, and timing
- FDE team - delivery feasibility, support load, and reusable learning

Bring the disagreement back to shared facts, decision rights, and customer impact. Use a reversible experiment when evidence is missing. Escalate when the decision exceeds your authority, not merely because agreement is difficult.

### Roadmap versus custom work

Evaluate a request using:

- Customer outcome and urgency
- Revenue or relationship exposure known to the appropriate commercial owner
- Number and strategic diversity of customers with the same need
- Fit with product direction and target architecture
- Ability to express the need as configuration, extension, adapter, or core capability
- Engineering and long-term support cost
- Security, reliability, and compatibility risk
- Time to evidence and reversibility
- Opportunity cost against committed roadmap work

Possible decisions:

- Configure existing product behavior.
- Build a narrow customer-owned integration against a stable product interface.
- Create a supported extension point.
- Run a time-boxed experiment to test repeat demand.
- Productize the capability with named owners and migration.
- Decline because the request creates unsafe or unsustainable divergence.

Do not present commercial judgment as private revenue arithmetic. Partner with the account and product owners, state technical and delivery consequences, and preserve a written decision.

### Travel and onsite realities

Prepare a direct answer about:

- Sustainable travel frequency and geographic limits
- Short-notice travel, launch periods, and incident support
- Time-zone overlap and recovery after travel
- Effective onsite goals: discovery, architecture, unblock, training, launch, or executive alignment
- Secure handling of devices, credentials, and customer data
- Capturing decisions so remote and onsite participants remain aligned

An onsite visit should have a decision or delivery purpose. It should not compensate indefinitely for missing ownership or poor written communication.

## Risk Register and Escalation

### Risk register

For each risk, record:

- Identifier and concise description
- Category: customer, data, integration, architecture, security, operations, adoption, schedule, commercial, or product
- Evidence and assumption status
- Probability and impact
- Leading indicator or trigger
- Prevention or mitigation
- Contingency and rollback
- Owner and decision deadline
- Status and last update
- Residual risk accepted by whom

Representative risks include unavailable production-like data, delayed security approval, unclear source permissions, customer API instability, missing customer engineering capacity, model quality below threshold, unbounded custom support, and a launch date fixed before dependencies are known.

Review risks as decisions, not as documentation. The highest risks should change the next experiment, milestone, or escalation.

### Escalation framework

Use severity, impact, urgency, and decision authority:

1. Detect - state the observed fact, source, time, and uncertainty.
2. Stabilize - stop unsafe work, preserve evidence, and maintain a safe customer path.
3. Classify - identify affected users, data, systems, commitments, and time sensitivity.
4. Own - name the incident or decision owner and establish a communication channel.
5. Notify - tell affected stakeholders what is known, unknown, being done, and when the next update will arrive.
6. Decide - present options, trade-offs, recommendation, and required authority.
7. Execute - track actions, owners, deadlines, validation, and rollback.
8. Close - confirm recovery or decision, customer impact, follow-up, and prevention.

Escalate immediately for suspected security or privacy exposure, safety risk, unauthorized action, data loss, material production outage, or a commitment that cannot be met safely. Escalate early for cross-team priority conflict, scope without an owner, repeated customer dependency failure, or a product gap that creates unsustainable custom work.

Avoid two failure modes: silently absorbing risk until the deadline and escalating without a recommendation. A useful escalation is concise, evidence-based, and decision-ready.

## Senior and Staff Depth

### Technical leadership without authority

Show that you can:

- Build shared understanding through current-state maps, decision records, prototypes, and measured evidence
- Separate decision owner, subject-matter expert, implementer, approver, and informed stakeholder
- Earn trust by making uncertainty and commitments visible
- Create interfaces and tests that let independent teams integrate safely
- Disagree clearly, then support the decision unless it creates an unacceptable risk
- Develop customer and internal engineers instead of becoming the permanent bottleneck

### Executive communication

Use an executive update with:

- Outcome - what customer or business result is at stake
- Status - on track, at risk, or blocked, with evidence
- Change - what changed since the last update
- Risk - impact and timing if no action is taken
- Recommendation - one proposed choice and credible alternatives
- Decision - owner and deadline
- Next update - date and evidence expected

Do not lead with an architecture dump. Translate technical detail into outcome, exposure, options, and confidence while retaining enough evidence for scrutiny.

### Multi-account patterns

At staff level, look across accounts:

- Identify repeated workflow, integration, deployment, and operational patterns.
- Distinguish shared need from coincidental implementation similarity.
- Normalize field evidence into problem statements, not feature votes.
- Quantify support burden and adoption blockers without exposing customer-confidential information.
- Propose stable interfaces, extension points, reference architectures, or tooling.
- Pilot the reusable capability across materially different customers.
- Define migration from customer-specific code and an owner for the common path.

### Productizing field lessons

Use this sequence:

1. Capture the field observation with customer context and current workaround.
2. Test whether the problem repeats across accounts and segments.
3. Identify the stable capability and variable customer-specific edges.
4. Compare configuration, adapter, extension, service, and core-product options.
5. Estimate adoption, migration, support, security, and opportunity cost.
6. Agree on product ownership and compatibility contract.
7. Prove the common path with more than one environment.
8. Deprecate or contain bespoke paths once migration is viable.

### Risk and commercial trade-offs

A senior answer protects the customer and the company:

- It does not trade away security or reliability to save a demo.
- It does not overbuild a reusable platform before repeated evidence exists.
- It does not accept a fixed date, full scope, and fixed resources while hiding infeasibility.
- It recognizes support and maintenance as real costs.
- It makes strategic exceptions explicit, time-bounded, owned, and reviewed.
- It knows when loss of trust from a missed or misleading commitment outweighs short-term expansion.

## Detailed Role-Play and Case Walkthroughs

Run each case with another person. The interviewer should reveal constraints only when the candidate asks relevant questions.

### Case 1: Ambiguous customer discovery

Interviewer prompt:

"A large operations team wants an AI agent to reduce ticket handling time. The executive sponsor wants a pilot in six weeks. Run the first discovery meeting."

Clarifying questions:

- Which ticket types, users, systems, and regions are in scope?
- What are volume, handle-time distribution, backlog, escalation, and error baselines?
- Does the agent advise, draft, route, or execute actions?
- Which actions are irreversible or policy-sensitive?
- Where are ticket history, policy, customer records, and resolution outcomes stored?
- What permissions should the agent inherit, and who can approve actions?
- How is success measured: handle time, resolution, quality, user adoption, or cost?
- Why six weeks, and which customer resources and approvals are available?

Artifacts:

- Current-state workflow and architecture map
- Requirement and assumption log
- POC one-pager
- Risk register
- Responsibility map with customer and vendor owners
- Evaluation set outline and baseline plan

Technical choices:

- Start with one high-volume, low-risk ticket category.
- Compare deterministic routing and retrieval-assisted drafting before an autonomous agent.
- Keep policy and authorization enforcement outside the model.
- Use read-only tools first, typed schemas, bounded workflow state, and human review.
- Capture traces for retrieval, model, validation, and user edits without unrestricted sensitive content.

Customer communication:

Summarize: "I hear that the desired outcome is shorter handling time without increasing incorrect resolutions. We do not yet know whether action execution is needed. I recommend a six-week pilot for retrieval-assisted drafts on one ticket class, with no autonomous writes. This lets us test data quality, policy grounding, user acceptance, and integration while security reviews the later action path."

Success metrics:

- Task-specific correctness and policy compliance
- Accepted draft rate and edit distance
- Median and p95 handling time
- Escalation and unsafe-action rates
- User participation and repeat usage
- Latency and cost per accepted resolution

Follow-ups:

- What if the sponsor insists on autonomous action?
- What if no reliable resolution labels exist?
- What if the user team refuses to change its workflow?
- What if the ticket API sandbox lacks representative data?
- What would make you stop after two weeks?

Strong performance narrows the decision without dismissing the sponsor's request. Weak performance either accepts "agent" as the requirement or spends the call collecting facts without proposing a next step.

### Case 2: Enterprise RAG integration

Interviewer prompt:

"A customer wants a RAG assistant over a document system, ticket system, and internal wiki. It must run in the customer's cloud account and respect existing permissions. Design the integration and delivery plan."

Clarifying questions:

- Who uses it, for which decisions, and what is the current search baseline?
- What content types, corpus size, update rate, languages, and query load apply?
- Which source owns identity and permissions? How quickly must revocation propagate?
- Are model-provider calls allowed, in which region, with what retention policy?
- What are answer, citation, freshness, latency, availability, and cost targets?
- How do deletions, legal holds, document versions, and group changes work?
- What cluster, network, keys, logs, CI/CD, and support access are available?

Artifacts:

- Current and target architecture diagrams
- Source and permission matrix
- Data-flow and trust-boundary diagram
- Evaluation and integration test plans
- Deployment runbook and production-readiness checklist
- Risk register and phased milestone plan

Technical choices:

- Use source-specific connectors behind a versioned change-event contract.
- Store immutable source versions, durable cursors, lineage, and reconciliation state.
- Preserve structure while parsing; quarantine failures.
- Use authorized lexical and dense retrieval with current identity context.
- Keep source access checks before content reaches the model; include authorization and version context in cache keys.
- Validate citations against supplied evidence and abstain when evidence is weak.
- Tombstone deleted or revoked content quickly, then remove derived data asynchronously.
- Deploy pinned artifacts through the customer's approved pipeline with canary and rollback.

Customer communication:

Explain that permission correctness and revocation are release gates, not prompt features. Separate ordinary content freshness from stricter permission-revocation behavior. State which source-system limitations could block the target and propose a test in the first week.

Success metrics:

- Retrieval recall at k by source and query class
- Answer correctness, groundedness, citation support, and abstention
- Unauthorized result rate in adversarial permission tests
- Content freshness and permission-revocation lag
- p95 latency, availability, and cost per accepted answer
- Task completion and search-time reduction against baseline

Follow-ups:

- How do you handle a group with hundreds of thousands of users?
- What happens when one source has no change-event API?
- How do you upgrade the embedding model without downtime?
- How do support engineers diagnose issues without broad data access?
- What differs in an air-gapped deployment?

Strong performance treats permissions, deletion, deployment, and operations as first-class. Weak performance begins with a vector database and leaves identity to a prompt.

### Case 3: Failing pilot and production incident

Interviewer prompt:

"A pilot went live to 200 users yesterday. This morning, answer quality dropped, p95 latency tripled, and one user reports seeing a document title they may not be authorized to access. The executive demo is tomorrow. Take ownership."

Clarifying questions:

- Is the title exposure confirmed, and could content also have leaked?
- Which tenants, users, sources, versions, regions, and time window are affected?
- What changed in model, prompt, index, permissions, cache, code, data, or traffic?
- Is there a safe mode such as authorized keyword search or full shutdown?
- What evidence and audit logs are available, and what retention restrictions apply?
- Who owns incident command, security response, customer communication, and demo decision?

Artifacts:

- Incident timeline and hypothesis log
- Impact and exposure assessment
- Containment decision record
- Customer update cadence
- Recovery checklist and validation results
- Follow-up action list and post-incident review

Technical choices:

- Treat the suspected authorization failure as the highest-severity signal.
- Disable affected retrieval or the entire assistant if authorization cannot be guaranteed.
- Preserve logs and versions under the security process; do not copy sensitive evidence into ad hoc channels.
- Compare release, index, identity, permission, cache, and traffic changes.
- Validate with known allowed and denied principals before restoring access.
- Address latency and quality only after safe containment, using rollback or authorized degradation.

Customer communication:

Initial update: "We have a report of a potentially unauthorized document title. We have disabled the affected path while we verify scope. We are preserving evidence and testing permission behavior by user and source. We will update you in 30 minutes with confirmed impact, recovery options, and a recommendation for tomorrow's demo."

Do not promise no data exposure before the investigation proves it. Do not allow tomorrow's demo to weaken containment.

Success metrics:

- Time to containment and validated safe recovery
- Confirmed affected principals, items, and duration
- Authorization test pass across critical cases
- Restored quality and latency against pre-incident baseline
- Communication timeliness and action completion
- Recurrence prevention verified through tests or controls

Follow-ups:

- The sponsor asks you to quietly use screenshots for the demo. What do you do?
- The issue is a stale authorization cache. How do you redesign it?
- Security and the account executive disagree on disclosure. How do you proceed?
- The customer caused the bad permission data. Does ownership change?
- What goes in the post-incident review?

Strong performance prioritizes containment and transparent communication while maintaining a path to diagnosis. Weak performance debugs latency first, minimizes an unconfirmed exposure, or protects the demo over the customer.

### Case 4: Demo and POC scope negotiation

Interviewer prompt:

"A prospective customer wants a three-week POC covering six data sources, multilingual RAG, automated CRM updates, custom dashboards, and an on-premises deployment. Sales has described all items as feasible. Negotiate a credible scope."

Clarifying questions:

- What decision must the POC enable, and who makes it?
- Which workflow and user group has the highest value?
- Which capabilities are required to prove product fit versus production readiness?
- Which source is representative of identity, permissions, and data complexity?
- Are CRM writes required to validate value, or can the POC draft and simulate?
- What on-premises environment exists today, and how long do access and security approval take?
- Which acceptance criteria and date are truly fixed?
- Which customer engineers and domain experts can work during the three weeks?

Artifacts:

- Option-based POC one-pager
- Scope and non-goal statement
- Milestone and dependency plan
- Demo plan
- Risk register
- Written decision and change-control record

Technical choices:

- Propose one representative source plus one contrasting source.
- Choose one language plus a small evaluation slice for a second if multilingual evidence is essential.
- Simulate or require approval for CRM writes; do not rush irreversible automation.
- Use an approved temporary environment if on-premises setup cannot finish in time, while separately validating deployment prerequisites.
- Build a thin integration and evaluation harness that can expand after the POC.

Customer communication:

Offer choices:

- Option A - three weeks, one workflow, two sources, read-only output, one primary language, and a decision-quality evaluation.
- Option B - six weeks, adds controlled CRM writes, broader language evaluation, and deployment validation.
- Option C - keep three weeks and full breadth, but treat it as a scripted demo with mocked integrations; it will not validate production feasibility.

Recommend one option and explain why. Do not present impossible breadth as an engineering challenge that more effort will solve.

Success metrics:

- Agreed decision and acceptance criteria before build starts
- Required access and representative data received by milestone
- Quality against baseline on the selected workflow
- Demonstrated integration and safe failure
- Named production gaps and credible next-phase estimate
- Stakeholder agreement on proceed, revise, or stop

Follow-ups:

- Sales says narrowing scope risks the deal. How do you respond?
- The customer accepts Option A, then adds CRM writes in week two.
- The on-premises cluster lacks required capacity.
- The demo fails because a source API is unavailable.
- The POC succeeds technically but users do not adopt it.

Strong performance preserves the customer's decision while making trade-offs visible. Weak performance blames sales, accepts hidden scope, or removes safety and production caveats to meet the date.

## Question Practice Order

The priority labels below allocate practice time; they do not remove any questions from the bank.

- P0 - Start with [discovery and scoping](#discovery-and-scoping), [customer architecture and integration](#customer-architecture-and-integration), and [architecture and deployment](#architecture-and-deployment). Pair the questions with a Python integration drill.
- P1 - Continue with [AI quality and evaluation](#ai-quality-and-evaluation) and the cloud, `RAG`, prompt, and agent constraints in the case walkthroughs.
- P2 - Add [delivery, demos, and adoption](#delivery-demos-and-adoption) plus [product and commercial judgment](#product-and-commercial-judgment).
- P3 - Prepare travel specifics and training or fine-tuning only when the target role confirms them.

Practice these first 12 questions or cases, in order:

1. Question 1 - Respond when a customer requests an agent without defining success.
2. Question 4 - Convert ambiguous stakeholder statements into acceptance criteria.
3. [Case 1](#case-1-ambiguous-customer-discovery) - Run ambiguous customer discovery and make a recommendation.
4. Question 7 - Map systems of record that lack a shared identifier.
5. Question 8 - Integrate with an unreliable API and unrealistic sandbox.
6. Question 11 - Define an integration contract and test suite.
7. Question 12 - Handle incomplete, duplicated, and inconsistent customer data.
8. Question 14 - Move a notebook prototype to supported production.
9. Question 10 - Preserve permissions through an enterprise RAG pipeline.
10. Question 20 - Reset a RAG plan when production data quality is poor.
11. Question 21 - Evaluate a workflow without reliable customer labels.
12. [Case 2](#case-2-enterprise-rag-integration) - Defend enterprise RAG integration through deployment and operations.

Then cover every remaining category. Override this order when the job description or recruiter confirms a different loop.

## Synthesized Interview Questions

All questions in this section are synthesized for practice. They are not attributed to any company.

### Discovery and scoping

1. A customer asks for an AI agent but cannot define success. What do you do in the first week?
2. How do you distinguish the requested feature from the underlying customer outcome?
3. Run the first ten minutes of discovery for a claims-processing workflow.
4. How do you convert ambiguous stakeholder statements into acceptance criteria?
5. A sponsor has fixed the date before technical discovery. How do you plan?
6. What evidence tells you a POC should stop rather than expand?

### Customer architecture and integration

7. Map the current state for a customer with three systems of record and no shared identifier.
8. How do you integrate with an unreliable customer API and an unrealistic sandbox?
9. A source schema changes without notice. How do you contain and recover?
10. How do you preserve customer permissions through an enterprise RAG pipeline?
11. What belongs in an integration contract and its test suite?
12. How do you handle customer data that is incomplete, duplicated, and semantically inconsistent?
13. Design identity federation and service-to-service authorization for a customer-cloud deployment.

### Architecture and deployment

14. Design the path from a notebook prototype to supported production.
15. How would you deploy the same capability in vendor cloud, customer cloud, and on-premises environments?
16. What changes for an air-gapped customer?
17. How do you design installation, upgrade, rollback, and support for customer-managed clusters?
18. A customer insists on a cloud service unavailable in its approved region. What do you do?
19. When should an FDE create an adapter, an extension point, or a core product change?

### AI quality and evaluation

20. A RAG demo looks good, but production data quality is poor. How do you reset the plan?
21. How do you evaluate a workflow when the customer has no reliable labels?
22. Quality improves offline, but users continue using the old workflow. What do you investigate?
23. How do you define safe failure for a model-assisted operational decision?
24. A model works for the majority language but fails a strategic customer segment. How do you decide whether to launch?

### Delivery, demos, and adoption

25. Scope a three-week POC that can support a production investment decision.
26. How do you design a demo that is credible when one integration is mocked?
27. A pilot meets technical metrics but misses adoption goals. What do you do next?
28. The customer repeatedly misses its data and access commitments. How do you manage delivery?
29. How do you hand off a production system without becoming permanent first-line support?
30. What should a weekly customer delivery update contain?

### Incidents and difficult customers

31. A customer reports possible cross-tenant retrieval. Walk through your first hour.
32. An executive demo is tomorrow, but you find a security issue today. What do you do?
33. Production latency degrades only in one customer's environment. How do you diagnose it?
34. A customer engineer publicly rejects your architecture. How do you respond?
35. Security, users, and the executive sponsor want incompatible outcomes. How do you drive a decision?
36. Tell me about a time you communicated a material delay or failure to a customer.

### Product and commercial judgment

37. A high-value customer requests a feature that conflicts with the roadmap. How do you decide?
38. When does customer-specific code become an unacceptable support burden?
39. How do you turn repeated field requests into product evidence rather than a list of anecdotes?
40. Sales has committed to a capability the product does not support. What do you do?
41. How do you balance delivery speed, reusable product work, and near-term account risk?
42. What technical evidence belongs in an expansion or no-go recommendation?

### Senior and staff leadership

43. How do you lead a customer and three internal teams when none reports to you?
44. Describe how you would standardize a pattern found across five accounts.
45. How do you communicate an uncertain technical risk to an executive?
46. Tell me about a time you changed technical direction using field evidence.
47. How do you decide which decision to make locally and which to escalate?
48. What operating mechanisms would you introduce for a growing FDE organization?

## Answer Rubrics for 16 Anchor Questions

Use the rubrics to evaluate structure and judgment, not to memorize wording.

### 1. Customer asks for an agent without success criteria

Strong-answer criteria:

- Discovers user workflow, current baseline, decision, error cost, and why now
- Challenges "agent" as a solution while preserving the underlying goal
- Proposes a narrow read-only or human-reviewed first slice
- Defines data, integration, security, evaluation, owners, and stop criteria
- Produces a POC one-pager and risk-based first-week plan

Red flags:

- Starts choosing frameworks immediately
- Promises autonomy before understanding actions and permissions
- Uses generic accuracy as the only success metric

Drill:

Run a 20-minute role-play, then produce a one-page scope in ten minutes.

### 2. Convert ambiguity into acceptance criteria

Strong-answer criteria:

- Separates outcome, functional behavior, quality, operations, risk, and adoption
- Makes each criterion observable and names the measurement source
- Labels assumptions and identifies owners
- Defines safe failure, non-goals, and exit decision

Red flags:

- Uses terms such as "fast," "accurate," or "enterprise ready" without thresholds
- Defines only technical criteria and ignores user or operational success

Drill:

Rewrite ten vague requirements into tests and decision thresholds.

### 3. Unreliable API and unrealistic sandbox

Strong-answer criteria:

- Establishes contract, rate limits, error semantics, ownership, and observed gaps
- Uses bounded retries, deadlines, idempotency, replay, reconciliation, and schema validation
- Builds a simulator and contract tests without treating them as proof of production behavior
- Plans a controlled production canary and actionable telemetry

Red flags:

- Adds retries at every layer
- Assumes sandbox behavior matches production
- Has no plan for duplicate or uncertain side effects

Drill:

Design the client state machine and failure matrix on one page.

### 4. Preserve permissions in enterprise RAG

Strong-answer criteria:

- Treats source identity and authorization as authoritative
- Filters before content reaches the model and isolates tenants in data, indexes, caches, and logs
- Defines revocation freshness, deletion, audit, and fail-closed behavior
- Tests allowed, denied, stale-group, cache, and prompt-injection cases

Red flags:

- Places permission text in the prompt
- Filters only after generation
- Omits cache keys, revocation, or deletion

Drill:

Threat-model five permission bypass paths and design a test for each.

### 5. Prototype to production

Strong-answer criteria:

- Audits prototype assumptions and temporary components
- Stages data, security, reliability, scale, deployment, observability, and support hardening
- Defines canary, rollback, migration, handoff, and ownership
- Uses release gates tied to customer outcomes and critical risks

Red flags:

- Describes production as putting the prototype in a container
- Adds infrastructure without identifying measured bottlenecks
- Omits operations and adoption

Drill:

Take one past prototype and write its production-gap inventory.

### 6. Deploy across vendor cloud, customer cloud, and on-premises

Strong-answer criteria:

- Starts from data, residency, network, identity, capacity, and support constraints
- Defines a portable core plus environment adapters
- Covers install, upgrade, telemetry, backup, security patches, and compatibility
- States unsupported combinations and support tiers

Red flags:

- Renames cloud services without addressing operating model
- Claims feature and SLO parity without validation
- Ignores disconnected upgrades or customer-owned incidents

Drill:

Create a deployment decision tree for three customer profiles.

### 7. Poor production data after a strong demo

Strong-answer criteria:

- Profiles failures by source, field, slice, and workflow impact
- Communicates the gap without blaming the customer
- Separates data repair, product tolerance, and reduced scope
- Revises acceptance criteria, owners, schedule, and stop decision

Red flags:

- Tunes prompts to hide upstream data defects
- Continues the same delivery plan
- surprises stakeholders at the final demo

Drill:

Prepare a five-minute customer update with three options and a recommendation.

### 8. Evaluate without reliable labels

Strong-answer criteria:

- Defines the decision and error taxonomy first
- Uses sampled expert review, weak signals, adjudication, and a prospective golden set
- Establishes a current-workflow baseline
- Separates offline evaluation from adoption and business outcome
- Plans confidence, slices, and label improvement

Red flags:

- Uses an uncalibrated model judge as ground truth
- Treats user clicks as correctness
- Reports one average score

Drill:

Design a 50-case evaluation set and reviewer rubric in 30 minutes.

### 9. Scope a three-week POC

Strong-answer criteria:

- Names the decision, narrow workflow, representative data, and non-goals
- Separates product-fit evidence from production readiness
- Defines customer dependencies, milestones, and exit paths
- Reserves time for evaluation, demo rehearsal, and decision review

Red flags:

- Accepts breadth that prevents meaningful validation
- Builds without a baseline or acceptance criteria
- Leaves production gaps implicit

Drill:

Reduce an intentionally oversized request to three option-based scopes.

### 10. Pilot meets technical metrics but lacks adoption

Strong-answer criteria:

- Investigates user selection, workflow entry point, trust, latency, incentives, training, and metric validity
- Observes real workflows and segments users
- Distinguishes product failure from change-management or access failure
- Runs a targeted experiment and defines a stop condition

Red flags:

- Declares success from model metrics
- Blames users
- Adds features without evidence

Drill:

Create an adoption funnel and five interview questions for non-users.

### 11. Possible cross-tenant retrieval

Strong-answer criteria:

- Contains first, preserves evidence, and activates security ownership
- Assesses scope by tenant, principal, data, version, and time
- Communicates knowns, unknowns, action, and next update
- Restores only after adversarial authorization validation
- Produces prevention and verification follow-up

Red flags:

- Waits for full proof before containment
- Continues a demo or pilot
- Makes an unsupported "no data leaked" claim

Drill:

Run a timed first-hour incident simulation with updates at 15 and 45 minutes.

### 12. High-value customer request conflicts with roadmap

Strong-answer criteria:

- Clarifies outcome and checks existing configuration or extension paths
- Brings product, account, and engineering owners into a decision
- Assesses repeated demand, strategic fit, support cost, risk, and opportunity cost
- Offers time-bounded experiment, adapter, productization, or decline
- Records ownership and migration or sunset

Red flags:

- Uses account value as the only criterion
- Says "no" without alternatives
- Creates permanent bespoke code with no owner

Drill:

Write a decision memo with four options and consequences.

### 13. Lead without authority

Strong-answer criteria:

- Establishes shared outcome, decision rights, owners, and operating cadence
- Uses artifacts and evidence to reduce ambiguity
- Resolves disagreement at the lowest capable level
- Escalates with options when authority or priorities exceed the group
- Builds capability in others and avoids becoming the hub

Red flags:

- Relies on charisma or executive escalation
- Confuses consensus with decision
- Claims all key work personally

Drill:

Tell a six-minute story that names each stakeholder's incentive and your mechanism of influence.

### 14. Executive communication under uncertainty

Strong-answer criteria:

- Leads with outcome, status, impact, and decision
- Separates observed facts, estimates, and unknowns
- Gives options and one recommendation
- States confidence, evidence plan, owner, and next update

Red flags:

- Hides uncertainty or floods the audience with technical detail
- Reports activity without outcome or decision
- Escalates a problem with no recommendation

Drill:

Convert a one-page technical incident into a 90-second executive update.

### 15. Productize a pattern across accounts

Strong-answer criteria:

- Uses evidence from materially different accounts
- Identifies stable need and variable edges
- Compares configuration, adapter, extension, and core-product designs
- Defines interface ownership, migration, adoption, support, and success
- Protects confidential customer context

Red flags:

- Counts feature requests without understanding workflows
- Generalizes from one strategic customer
- Builds a platform before testing commonality

Drill:

Cluster five fictional requests into a capability map and identify counterexamples.

### 16. Sales committed an unsupported capability

Strong-answer criteria:

- Verifies the exact commitment and customer decision at risk
- Aligns privately with sales, product, and engineering before correcting externally
- Presents feasible alternatives with scope, time, evidence, and risk
- Communicates transparently to the customer without assigning blame
- Improves the commitment and technical-validation process afterward

Red flags:

- Blames sales in front of the customer
- silently accepts an unsafe or impossible commitment
- Solves only the immediate account and leaves the mechanism unchanged

Drill:

Role-play the internal alignment and customer correction as separate conversations.

## Eight-Week Curriculum Integration

Use this role track alongside the shared curriculum rather than replacing coding, design, project, and behavioral preparation.

### Week 1: Baseline and role model

- Read [`README.md`](README.md), [`01-common-core.md`](01-common-core.md), and the [FDE role analysis](../../role/06-fde.md).
- Collect 5-10 target job descriptions and identify actual ownership, environment, travel, and interview format.
- Run one discovery baseline and one practical coding baseline.
- Deliverable - role evidence map and scored discovery recording.

### Week 2: Discovery and scoping

- Practice workflow discovery, requirement decomposition, acceptance criteria, and POC one-pagers.
- Run Case 1 twice with different hidden constraints.
- Deliverable - current-state map, scope, assumption log, and risk register.

### Week 3: Integration fundamentals

- Practice APIs, SQL, data profiling, identity, permissions, networking, schema drift, and contract tests.
- Build or debug one small customer-style integration.
- Deliverable - integration contract, failure matrix, tests, and runbook.

### Week 4: Architecture and deployment

- Use [`03-ai-ml-system-design.md`](03-ai-ml-system-design.md) for production design.
- Practice customer cloud, on-premises, and restricted-environment variants.
- Run Case 2 under a 55-minute limit.
- Deliverable - current and target architecture plus production-readiness gap analysis.

### Week 5: POC, demo, and adoption

- Scope two POCs, rehearse one demo, and define pilot adoption measures.
- Run Case 4 with a partner playing sales and another playing customer security.
- Deliverable - POC one-pager, demo plan, decision memo, and adoption funnel.

### Week 6: Incidents and difficult stakeholders

- Practice incident command, customer updates, scope changes, conflict, and escalation.
- Run Case 3 and two stories from [behavioral questions](../questions/05-behavioral.md).
- Use [`07-senior-staff-behavioral.md`](07-senior-staff-behavioral.md) to strengthen ownership and influence evidence.
- Deliverable - incident timeline, executive update, and revised story bank.

### Week 7: Senior and staff leverage

- Practice multi-account synthesis, field-to-product feedback, roadmap trade-offs, and leadership without authority.
- Prepare project evidence with [`08-project-deep-dives-and-take-homes.md`](08-project-deep-dives-and-take-homes.md).
- Run one staff-level case with product, account, platform, and customer conflicts.
- Deliverable - productization memo and 15-minute project deep dive.

### Week 8: Simulation and readiness

- Run the two-week rotation below at compressed cadence if time permits.
- Complete one full loop: practical coding, system design, FDE case, project deep dive, and behavioral.
- Score with [`09-mock-interviews-and-scorecards.md`](09-mock-interviews-and-scorecards.md).
- Repeat the lowest-scoring section with changed constraints.
- Deliverable - three recent scorecards, error log, and readiness decision.

## Two-Week FDE Rotation Plan

Use this as the final two weeks of the curriculum or as a standalone intensive. Budget 2-3 hours per weekday and one longer mock block each weekend.

The default sequence starts with P0 discovery, Python integration, and production delivery before generic product, POC, or demo cases.

### Rotation week 1: discovery, integration, and production

Day 1:

- Run a 30-minute ambiguous discovery role-play.
- Produce requirements, assumptions, acceptance criteria, and next actions in 20 minutes.
- Review whether every question changed scope, risk, or ownership.

Day 2:

- Implement or debug a Python API integration with timeouts, retries, pagination, schema validation, and idempotency.
- Write contract tests, a failure matrix, and a customer-facing incident note.

Day 3:

- Draw a current-state architecture from a written customer scenario.
- Add identity, data classification, network, deployment, operational owners, and unknowns.
- Present the production path to technical and executive audiences in five minutes each.

Day 4:

- Design enterprise RAG integration with permissions, deletion, freshness, evaluation, and customer-cloud deployment.
- Answer three adversarial security and operations follow-ups.

Day 5:

- Create a POC one-pager and demo plan for an oversized request.
- Negotiate scope with a partner and record the final decision.

Weekend:

- Run a 75-minute mock: 30-minute discovery, 30-minute architecture, and 15-minute executive readout.
- Score it, repeat the weakest ten minutes immediately, and schedule a full repeat.

### Rotation week 2: operations, product feedback, and leadership

Day 6:

- Run the failing-pilot incident.
- Send simulated updates at 15, 30, and 60 minutes.
- Produce containment, recovery, and follow-up decisions.

Day 7:

- Practice scope change, stakeholder conflict, and roadmap-versus-custom scenarios.
- Give one option-based recommendation for each.

Day 8:

- Present a project deep dive that proves customer discovery, production coding, delivery, and adoption.
- Answer ownership, failure, commercial, and productization follow-ups.

Day 9:

- Synthesize five fictional account requests into reusable patterns.
- Write a one-page productization proposal and migration path.

Day 10:

- Run an executive briefing covering status, risk, options, recommendation, and decision.
- Repeat it at 5-minute, 2-minute, and 30-second lengths.

Weekend:

- Run the full mock format below with a different interviewer.
- Compare the last three scorecards and apply the readiness gate.

Override this rotation when the job description or recruiter confirms a different loop. Keep discovery and integration ahead of generic product cases for an FDE-primary loop.

## Full Mock Format

Use a 100-minute simulation:

1. Discovery role-play - 25 minutes
2. Requirement summary and POC recommendation - 10 minutes
3. Customer architecture and integration design - 30 minutes
4. Incident or scope-change interruption - 15 minutes
5. Executive readout - 5 minutes
6. Senior or staff follow-ups - 10 minutes
7. Candidate questions - 5 minutes

Interviewer instructions:

- Reveal only information the candidate asks for or could reasonably infer.
- Introduce one contradiction between sponsor, user, security, and engineering needs.
- Change one major constraint after the design begins.
- Ask who owns each critical dependency and production operation.
- Require a recommendation, not only a list of options.
- Score observable behavior before discussing feedback.

## FDE Scorecard

Use the canonical scale and readiness rules in [mock interviews and scorecards](09-mock-interviews-and-scorecards.md). Score each dimension from 1 to 4:

- 1 - weak or unsafe; behavior is missing, incorrect, counterproductive, or requires direct rescue
- 2 - partial; recognizes the topic or gives a workable answer with important gaps or targeted prompting
- 3 - interview-ready; independently produces a credible approach for the stated level and handles expected follow-ups
- 4 - strong senior or staff evidence; adds unusual clarity and leverage across teams, accounts, interfaces, or strategy

Dimensions:

1. Discovery and listening
   - A 3 uncovers workflow, baseline, users, constraints, decision, urgency, and unknowns while adapting to answers.
   - A 4 resolves conflicting stakeholder frames and identifies the highest-value uncertainty.
2. Scope and acceptance
   - A 3 creates narrow scope, non-goals, measurable criteria, dependencies, owners, and exit paths.
   - A 4 protects portfolio and commercial trade-offs while preserving customer value.
3. Technical architecture
   - A 3 maps current state and designs appropriate contracts, data flows, identity, deployment, and failure handling.
   - A 4 creates reusable boundaries that work across materially different environments.
4. Production execution
   - A 3 covers code quality, tests, CI/CD, observability, reliability, rollback, operations, and handoff.
   - A 4 sequences delivery across organizations and reduces long-term support burden.
5. AI quality and risk
   - A 3 defines baseline, evaluation, critical slices, security, privacy, safe failure, and release gates.
   - A 4 connects field evidence to durable quality and governance mechanisms.
6. Customer communication
   - A 3 summarizes accurately, explains trade-offs plainly, communicates bad news early, and closes with actions.
   - A 4 adapts across users, engineers, security, and executives without changing the underlying facts.
7. Delivery and adoption
   - A 3 manages milestones, dependencies, change, pilot evidence, workflow adoption, and ownership.
   - A 4 identifies multi-account delivery patterns and improves the operating model.
8. Incident and escalation judgment
   - A 3 prioritizes safety, contains, assigns ownership, communicates, recovers, and follows through.
   - A 4 handles commercial and executive pressure while improving cross-team prevention.
9. Product and commercial judgment
   - A 3 evaluates custom work through customer outcome, repeatability, cost, risk, and opportunity cost.
   - A 4 converts field patterns into product direction, interfaces, and migration.
10. Leadership and self-awareness
   - A 3 leads without authority, states personal contribution, revises assumptions, and develops others.
   - A 4 changes decision quality across teams or accounts and names limits honestly.

The maximum is 40.

- 10-19 - foundation gap; repair technical, discovery, or communication basics before more full mocks
- 20-27 - developing; repeat focused sections with explicit rubrics
- 28-33 - interview-ready evidence is emerging; target every dimension below 3
- 34-37 - strong senior performance; add staff follow-ups if relevant
- 38-40 - exceptional mock result; verify it repeats across unfamiliar cases and interviewers

A total or score band describes one mock and never establishes readiness. A score of 1 in technical architecture, AI quality and risk, customer communication, or incident judgment fails the mock. All ten dimensions are required. For a staff target, additionally require at least three scores of 4 supported by cross-team or multi-account evidence.

## Readiness Gate

The [readiness rules in module 09](09-mock-interviews-and-scorecards.md#readiness-rules) are canonical. Treat the FDE track as interview-ready only when all are true:

- [ ] I can run a 30-minute discovery call without a script and produce an accurate decision-ready summary.
- [ ] I can map current-state workflow, data, identity, network, deployment, operations, and ownership.
- [ ] I can scope a POC with explicit non-goals, acceptance criteria, risks, customer dependencies, and exit paths.
- [ ] I can design and debug representative API and data integrations in production-quality code.
- [ ] I can explain deployment in vendor cloud, customer cloud, on-premises, and restricted environments without claiming false parity.
- [ ] I can design enterprise RAG with authorization, freshness, deletion, evaluation, observability, and rollback.
- [ ] I can run a suspected security incident without allowing customer or commercial pressure to weaken containment.
- [ ] I can present the same situation to a user, engineer, security reviewer, and executive.
- [ ] I have distinct stories for ambiguity, customer conflict, failure, scope change, incident ownership, influence, and product feedback.
- [ ] I can make a roadmap-versus-custom recommendation with technical, support, product, and commercial consequences.
- [ ] I can explain sustainable travel and onsite expectations directly.
- [ ] My three most recent relevant full FDE mocks used different unfamiliar scenarios and the stated time limit.
- [ ] At least two mocks were scored by different interviewers, or one was independently double-scored before the debrief.
- [ ] Every required scorecard dimension scored at least 3 in at least two of the three mocks.
- [ ] No required dimension scored 1 in either of the two most recent mocks, and no hard fail remains unresolved.
- [ ] I finished the core scope within the stated time limit in at least two mocks.
- [ ] I handled at least one material follow-up without direct rescue in each of the two most recent mocks.
- [ ] Every known or repeated failure completed a successful re-test with a fresh prompt.
- [ ] For a staff target, at least two mocks also contained three or more scores of 4 supported by cross-team or multi-account evidence.

## Final Interview Checklist

Before ending an FDE answer, verify:

- Did I identify the customer outcome rather than accept the requested implementation?
- Did I summarize the current workflow and architecture accurately?
- Did I state assumptions, unknowns, and the fastest safe validations?
- Did I define measurable technical, user, operational, security, and delivery success?
- Did I choose a narrow first step and state non-goals?
- Did I cover data, APIs, identity, network, deployment, and ownership?
- Did I preserve authorization, privacy, audit, and safe failure?
- Did I explain production hardening, rollout, support, adoption, and handoff?
- Did I name scope, schedule, support, product, and commercial trade-offs?
- Did I give a recommendation, owners, decision date, and next evidence?
- Did I communicate uncertainty without becoming vague?
- Did I show what can become reusable product and what should remain customer-specific?

Continue with [`07-senior-staff-behavioral.md`](07-senior-staff-behavioral.md) for leadership stories, [`08-project-deep-dives-and-take-homes.md`](08-project-deep-dives-and-take-homes.md) for evidence and working sessions, and [`09-mock-interviews-and-scorecards.md`](09-mock-interviews-and-scorecards.md) for interview simulation. Use the existing [behavioral question bank](../questions/05-behavioral.md) to vary prompts. Return to [`01-common-core.md`](01-common-core.md) for technical gaps and [`03-ai-ml-system-design.md`](03-ai-ml-system-design.md) for deeper architecture practice.
