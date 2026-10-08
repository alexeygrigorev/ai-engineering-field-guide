# Mock Interviews and Scorecards for Senior AI Engineering Roles

Mock interviews turn knowledge into interview performance. This module provides a repeatable system for senior Product AI Engineer, Forward Deployed Engineer, and ML/AI Platform Engineer preparation. It covers how to run each common format, score observable behavior, choose the next drill, and decide readiness from repeated evidence.

Use the supporting modules for content depth:

- [Coding and LeetCode](02-coding-and-leetcode.md) - DSA, progressive implementation, practical coding, and solve-review drills.
- [AI/ML system design](03-ai-ml-system-design.md) - the reusable design framework, calculations, and design prompts.
- [Product AI Engineer](04-product-ai-engineer.md) - product cases, product metrics, evaluation, and role-specific judgment.
- [Forward Deployed Engineer](05-forward-deployed-engineer.md) - discovery, customer architecture, delivery, and field cases.
- [ML/AI Platform Engineer](06-ml-ai-platform-engineer.md) - platform contracts, serving, scheduling, reliability, and migration.
- [Senior and staff behavioral](07-senior-staff-behavioral.md) - story construction, question rubrics, and level evidence.
- [Project deep dives and take-homes](08-project-deep-dives-and-take-homes.md) - project dossiers, take-home execution, review, and extension.
- [Eight-week study plan](10-eight-week-study-plan.md) - weekly allocation across the full curriculum.

The prompts and rubrics here are synthesized practice material. They do not describe any particular company's process.

## Deliberate Practice, Not Repeated Performance

A mock is useful when it isolates a skill, produces evidence, and changes the next practice session. Repeating full interviews without correcting specific errors rehearses those errors.

Run each practice cycle in five steps:

1. Select one format and one or two target behaviors.
2. Run the interview under realistic time and tool constraints.
3. Record observations before discussing impressions.
4. Choose the smallest drill that addresses the highest-value error.
5. Re-test the same skill with a fresh prompt after a short delay.

Change one variable at a time when diagnosing a weakness. If a candidate misses both requirements and estimates in design, first re-test requirement framing with a ten-minute opening drill. Do not infer that the entire design skill is weak from one overloaded mock.

Use full mocks to test integration and short drills to repair components. A practical weekly mix is:

- One or two full mocks under interview conditions.
- Two targeted drills based on the latest error log.
- One re-test of a previously weak dimension.
- One short calibration review of recordings or written evidence.

Do not optimize for the average score alone. Track whether the candidate can reproduce strong behavior across unfamiliar prompts, different interviewers, and normal time pressure.

## Roles and Operating Agreement

### Candidate

The candidate should:

- Confirm the format, duration, tool policy, and evaluation level before the timer starts.
- Think aloud enough to expose decisions, assumptions, and verification.
- Ask clarifying questions rather than waiting for hidden requirements.
- Treat interviewer answers as facts and label remaining assumptions.
- Manage time visibly and state when changing direction.
- Own the final result, including mistakes, hints, and incomplete sections.

The candidate should not receive the scorecard immediately before every mock. Familiarity with the stable dimensions is useful, but rehearsing rubric phrases can produce performative answers instead of judgment.

### Interviewer

The interviewer should:

- Select the prompt and follow-ups before the session.
- Define which facts may be supplied and which ambiguities the candidate must identify.
- Keep a timestamped evidence log.
- Give only the hints allowed by the format.
- Avoid teaching, rescuing, or signaling approval during the interview.
- Score independently before the debrief.
- Separate observed behavior from inference.

Do not reward a candidate for arriving at the interviewer's preferred architecture. Reward a defensible decision tied to requirements, evidence, and trade-offs.

### Observer

An observer is optional. When present, the observer should not participate. They track time, interruptions, communication patterns, missed questions, and evidence for disputed scores. The observer scores independently before hearing the interviewer.

### Recording and consent

Ask for explicit consent before recording audio, video, screen content, shared documents, or code. State:

- What will be recorded.
- Why it is being recorded.
- Who may access it.
- Where it will be stored.
- When it will be deleted.
- Whether the candidate can stop recording without affecting the session.

If anyone declines, use timestamped notes instead. Do not record confidential employer, customer, user, or project information. Redact secrets and identifying data from project artifacts. A recording is for evidence review, not for public distribution.

### Evidence-based feedback

Useful feedback names a behavior, its consequence, and the next test:

- Observation - "At minute 12, you chose a vector database before defining corpus size, freshness, or access rules."
- Consequence - "That made the design difficult to evaluate and left authorization unresolved."
- Next action - "Run two eight-minute requirement openings and require an explicit data-access contract before naming infrastructure."

Avoid labels such as "not strategic," "weak communicator," or "not senior enough" without observable evidence. Replace personality claims with actions the candidate can repeat or change.

### Avoid friendly grading

A supportive interviewer can still grade rigorously. Friendly grading happens when familiarity, effort, confidence, shared background, or knowledge of prior improvement raises the score without evidence in the current mock.

Use these controls:

- Write anchors before selecting the candidate.
- Score before the debrief.
- Require a timestamp or artifact for every score of 1 or 4.
- Do not add points for intended behavior that was not demonstrated.
- Treat an unprompted behavior as stronger evidence than the same behavior after a direct hint.
- Record hint count and hint type separately.
- Ask a second interviewer to score one recording every two weeks.
- Hide prior scores during the first scoring pass.

## Session Setup

Before every mock, create a one-page session record:

- Candidate and interviewer.
- Date, target role, and target level.
- Format and exact duration.
- Prompt identifier.
- Allowed tools, references, and AI assistance.
- Starting information provided to the candidate.
- Clarifications the interviewer may answer.
- Planned follow-ups and their trigger points.
- Target behaviors from the previous error log.
- Recording consent and retention decision.

The interviewer prepares a prompt packet with:

- Candidate-facing prompt.
- Hidden facts that may be revealed after a relevant question.
- Non-essential details that should not be volunteered.
- Follow-ups from ordinary to adversarial.
- Expected evidence, not a single expected solution.
- Hard-fail conditions relevant to the prompt.

Use a visible timer. Stop at the agreed time even if the candidate is close to finishing. Incomplete work is evidence about prioritization and time management.

## Common Scoring Scale

Score each dimension from 1 to 4. Do not use half points. Add a short evidence note beside every score.

### 1 - Weak or unsafe

The behavior is absent, incorrect, or usable only after direct rescue.

Observable anchors:

- Misses a central requirement or constraint after a relevant prompt.
- Cannot produce a workable baseline or coherent next step.
- Makes a consequential claim without reasoning or verification.
- Repeats the same error after feedback or a hint.
- Leaves the interviewer unable to determine ownership, correctness, or operational behavior.

### 2 - Partial

The behavior appears but has important gaps.

Observable anchors:

- Identifies some relevant requirements but misses one that changes the solution.
- Produces a plausible approach but cannot defend a key trade-off.
- Verifies the happy path but not an obvious edge or failure case.
- Needs one or more targeted prompts to recover.
- Communicates the main idea but loses structure, precision, or time.

### 3 - Interview-ready

The behavior is complete, independent, and appropriate for the stated level.

Observable anchors:

- Identifies the decisions that materially change the solution.
- Builds a correct or credible baseline before adding complexity.
- Connects choices to constraints, alternatives, and evidence.
- Tests or challenges the highest-risk assumptions.
- Handles follow-ups without losing the structure of the answer.
- Finishes the important scope within time and states remaining work.

### 4 - Strong senior or staff evidence

The behavior is unusually clear, adaptive, and leveraged without becoming overbuilt.

Observable anchors:

- Reframes the problem around the decision or outcome that actually matters.
- Anticipates a consequential failure, organizational boundary, or second-order effect.
- Uses a simple model, estimate, test, or interface to resolve ambiguity.
- Changes direction promptly when evidence invalidates an assumption.
- Creates a durable decision rule or interface that helps multiple teams.
- Distinguishes senior execution from staff-level organizational scope with concrete evidence.

A 4 requires more than polish or speed. It requires an observable improvement in decision quality, risk control, or leverage.

### Scoring rules

- Score only behavior demonstrated in the mock.
- Use the lowest score supported by the evidence when observations conflict.
- Record direct hints. A correct result after a direct solution hint does not demonstrate independent performance.
- Keep dimension scores separate. Strong communication does not compensate for incorrect code, and technical depth does not compensate for missing the user or customer outcome.
- Report both the dimension profile and hard-fail result. Do not compress them into one unexplained number.

## Hard-Fail Conditions

A hard fail is a specific condition that can override otherwise adequate scoring because it makes the result unsafe, unusable, dishonest, or fundamentally incorrect. It is not a synonym for weak performance.

General hard fails:

- Fabricates experience, metrics, test results, customer facts, or system behavior.
- Exposes or proposes exposing secrets, personal data, tenant data, or confidential material without correction.
- Ignores a stated safety, privacy, authorization, or destructive-action boundary after it is raised.
- Claims work is correct or production-ready while known critical failures remain undisclosed.
- Uses prohibited tools or outside help after the policy is clear.
- Becomes abusive, discriminatory, or persistently dismissive of the interviewer or stakeholder.

Format-specific hard fails:

- Coding - no executable or coherent solution to the core problem, or knowingly returns incorrect results while claiming correctness.
- AI/ML design - no end-to-end path for the primary use case, or a design that crosses a stated data or action boundary without authorization.
- Product AI - cannot define a user outcome and still recommends launch, or removes meaningful human control from a stated high-consequence decision.
- FDE - commits to an unsupported capability or production date after the constraint is made explicit, or bypasses customer security controls.
- Platform - breaks tenant isolation or lifecycle safety by design and does not correct it when challenged.
- Project deep dive - materially misrepresents personal ownership or evidence.
- Behavioral - blames others while concealing the candidate's known decision or accountability.
- Take-home - plagiarism, undisclosed prohibited assistance, malicious code, or deliberate concealment of failing tests.

Weak performance remains scoreable and coachable. Examples include a slow implementation, shallow estimates, vague metrics, excessive prompting, weak prioritization, or an incomplete debrief. Do not call these hard fails unless they meet a condition above.

## Runnable Interview Formats

### DSA coding: 45-60 minutes

Setup:

- Use an editor equivalent to the target interview environment.
- State whether code execution, documentation, tests, and AI assistance are allowed.
- Choose one medium problem or a medium problem with an extension from [the prioritized set](02-coding-and-leetcode.md#prioritized-leetcode-set).
- Prepare examples, edge cases, constraints, and one optional hint ladder.

Timing:

Compact 45-minute schedule:

1. Minutes 0-5 - read, clarify inputs, outputs, constraints, and examples.
2. Minutes 5-12 - derive a baseline and compare approaches.
3. Minutes 12-33 - implement while maintaining invariants.
4. Minutes 33-40 - test, debug, and analyze complexity.
5. Minutes 40-45 - extension or debrief summary.

Full 60-minute schedule:

1. Minutes 0-5 - read, clarify inputs, outputs, constraints, and examples.
2. Minutes 5-12 - derive a baseline and compare approaches.
3. Minutes 12-45 - implement while maintaining invariants.
4. Minutes 45-55 - test, debug, and analyze complexity.
5. Minutes 55-60 - extension or debrief summary.

Prompt selection:

- Rotate patterns; do not tell the candidate the pattern name.
- Avoid a recently memorized problem unless testing recall resistance.
- Select an extension that changes one constraint, such as streaming input, duplicate handling, memory bounds, or concurrency.

Allowed clarifications:

- Input types, size bounds, ordering, mutation policy, duplicate behavior, error behavior, and expected complexity.
- The interviewer answers direct questions but does not volunteer the intended data structure.

Follow-ups:

- "What invariant makes this correct?"
- "What changes if the input arrives as a stream?"
- "Show a case that would break your first approach."
- "How would you test this without relying on the examples?"

Observe:

- Requirement clarification, derivation, correctness, code structure, testing, complexity, recovery, and hint dependence.

Score dimensions:

- Problem framing and assumptions.
- Algorithm and invariant.
- Implementation correctness.
- Test quality and debugging.
- Complexity analysis.
- Communication and adaptation.

Debrief:

- Candidate gives a two-minute self-assessment first.
- Interviewer replays one strong decision and the highest-value error with timestamps.
- Agree on one repair drill and a fresh re-test problem.

### Progressive implementation: 75-90 minutes

Setup:

- Start from an empty repository or a small provided skeleton.
- Choose one exercise from [progressive implementation exercises](02-coding-and-leetcode.md#progressive-implementation-exercises).
- Prepare three levels that introduce behavior sequentially.
- State package, internet, test, documentation, and AI-tool policy.

Timing:

Compact 75-minute schedule:

1. Minutes 0-8 - clarify level 1 and choose interfaces.
2. Minutes 8-27 - implement and test level 1.
3. Minutes 27-48 - reveal and implement level 2.
4. Minutes 48-65 - reveal level 3, refactor, and test.
5. Minutes 65-75 - review failures, trade-offs, and production extensions.

Full 90-minute schedule:

1. Minutes 0-8 - clarify level 1 and choose interfaces.
2. Minutes 8-30 - implement and test level 1.
3. Minutes 30-55 - reveal and implement level 2.
4. Minutes 55-75 - reveal level 3, refactor, and test.
5. Minutes 75-90 - review failures, trade-offs, and production extensions.

Prompt selection:

- Level 1 should require a usable core.
- Level 2 should stress an anticipated boundary such as time, persistence, pagination, or idempotency.
- Level 3 should test change tolerance with concurrency, retries, quotas, schema evolution, or partial failure.

Allowed clarifications:

- Current-level behavior, invalid input, ordering, consistency, dependency contracts, and expected scale.
- Do not answer questions about unrevealed levels.

Follow-ups:

- "Which part would you refactor before adding the next requirement?"
- "What state transition can fail halfway?"
- "How would you make time or network behavior deterministic in tests?"
- "What would you monitor in production?"

Observe:

- Scope control, interface quality, incremental correctness, refactoring judgment, dependency isolation, tests, and response to changing requirements.

Score dimensions:

- Requirement decomposition.
- Design for change without speculative abstraction.
- Working implementation at each level.
- Testability and failure handling.
- Refactoring and code quality.
- Time management and ownership.

Debrief:

- Review the repository state at each level, not only the final code.
- Identify the earliest decision that caused later friction.
- Select one extension to repeat on a different core problem.

### AI/ML system design: 45-60 minutes

Setup:

- Use a shared board or document.
- Select a prompt from [synthesized practice prompts](03-ai-ml-system-design.md#synthesized-practice-prompts).
- Prepare workload, quality, risk, and cost facts that are revealed only when asked.
- Use the [45-60 minute answer framework](03-ai-ml-system-design.md#the-45-60-minute-answer-framework).

Timing:

Compact 45-minute schedule:

1. Minutes 0-5 - users, outcome, scope, quality, and constraints.
2. Minutes 5-10 - workload and cost estimates.
3. Minutes 10-15 - APIs, data contracts, and baseline.
4. Minutes 15-25 - architecture and critical flows.
5. Minutes 25-35 - two risk-driven deep dives.
6. Minutes 35-41 - evaluation, failures, security, and operations.
7. Minutes 41-45 - evolution, trade-offs, and summary.

Full 60-minute schedule:

1. Minutes 0-6 - users, outcome, scope, quality, and constraints.
2. Minutes 6-12 - workload and cost estimates.
3. Minutes 12-18 - APIs, data contracts, and baseline.
4. Minutes 18-30 - architecture and critical flows.
5. Minutes 30-44 - two risk-driven deep dives.
6. Minutes 44-52 - evaluation, failures, security, and operations.
7. Minutes 52-60 - evolution, trade-offs, and summary.

Prompt selection:

- Rotate classic ML, RAG, agentic, multimodal, serving, and platform systems.
- Choose one domain where the candidate cannot rely on a memorized architecture.
- Define one primary risk that should shape the design.

Allowed clarifications:

- Users, use cases, scale, latency, reliability, data, labels, quality, cost, privacy, safety, and deployment environment.
- Give ranges where exact values are unavailable.

Follow-ups:

- "What is the non-model baseline?"
- "Which estimate changes your design?"
- "Trace one request and one failure end to end."
- "How do you know the system improved the target outcome?"
- "What breaks at ten times scale?"

Observe:

- Problem framing, quantitative reasoning, interfaces, architecture, model and data judgment, evaluation, operational behavior, risk, and evolution.

Score dimensions:

- Requirements and quality contract.
- Estimates and capacity reasoning.
- APIs, data, and architecture.
- AI/ML and evaluation judgment.
- Reliability, security, privacy, and safety.
- Trade-offs, rollout, and evolution.

Debrief:

- Ask the candidate to name the most consequential assumption.
- Compare the design against the primary risk in the prompt packet.
- Re-test the weakest stage with a 10-15 minute focused design drill.

### Product AI case: 45-60 minutes

Setup:

- Select a case from [Product AI case exercises](04-product-ai-engineer.md#product-case-exercise-1-support-copilot) or the bank below.
- Prepare user research, baseline workflow, constraints, and imperfect evaluation evidence.
- Tell the candidate whether the task is discovery, product strategy, launch review, or iteration.

Timing:

Compact 45-minute schedule:

1. Minutes 0-6 - user, job, pain, current workflow, and why now.
2. Minutes 6-12 - assumptions, baseline, and whether AI is justified.
3. Minutes 12-21 - narrow product behavior and end-to-end experience.
4. Minutes 21-29 - evaluation, metrics, and experiment.
5. Minutes 29-38 - uncertainty UX, safety, privacy, and failure recovery.
6. Minutes 38-45 - launch, iteration, trade-offs, and follow-ups.

Full 60-minute schedule:

1. Minutes 0-7 - user, job, pain, current workflow, and why now.
2. Minutes 7-14 - assumptions, baseline, and whether AI is justified.
3. Minutes 14-25 - narrow product behavior and end-to-end experience.
4. Minutes 25-35 - evaluation, metrics, and experiment.
5. Minutes 35-45 - uncertainty UX, safety, privacy, and failure recovery.
6. Minutes 45-60 - launch, iteration, trade-offs, and follow-ups.

Prompt selection:

- Rotate greenfield discovery, underperforming launch, and constrained expansion.
- Include enough ambiguity to test prioritization, not mind reading.
- Ensure rejecting or narrowing the AI use case is a defensible option.

Allowed clarifications:

- Target users, workflow frequency, baseline performance, business constraint, data availability, consequence of error, and launch authority.
- Do not provide a preferred feature or model.

Follow-ups:

- "What evidence would make you stop this project?"
- "How does the user detect and recover from a wrong answer?"
- "Which metric can improve while the product gets worse?"
- "What is the smallest experiment that changes the decision?"
- "What would you ship without generative AI?"

Observe:

- User framing, prioritization, AI necessity, experience design, evaluation, metric judgment, launch safety, learning speed, and cross-functional ownership.

Score dimensions:

- User problem and product judgment.
- Baseline, scope, and prioritization.
- AI behavior and end-to-end implementation judgment.
- Evaluation and metric hierarchy.
- UX for uncertainty, safety, and privacy.
- Launch, iteration, and organizational alignment.

Debrief:

- Require a one-sentence product decision and a one-sentence reason.
- Identify where the answer relied on an unsupported assumption.
- Assign one discovery, metric, or failure-recovery drill.

### FDE discovery and customer case: 45-60 minutes

Setup:

- Interviewer role-plays a customer sponsor, technical owner, or skeptical operator.
- Select a case from [detailed FDE role-plays](05-forward-deployed-engineer.md#detailed-role-play-and-case-walkthroughs) or the bank below.
- Prepare hidden stakeholder goals, environment facts, constraints, and one conflict.
- Decide which facts require precise discovery questions.

Timing:

Compact 45-minute schedule:

1. Minutes 0-9 - discovery conversation.
2. Minutes 9-15 - restate workflow, outcome, constraints, and unknowns.
3. Minutes 15-25 - propose scope, acceptance criteria, and technical path.
4. Minutes 25-34 - integration, deployment, security, and operational ownership.
5. Minutes 34-40 - delivery risks, adoption, and product feedback.
6. Minutes 40-45 - escalation or changed requirement.

Full 60-minute schedule:

1. Minutes 0-12 - discovery conversation.
2. Minutes 12-20 - restate workflow, outcome, constraints, and unknowns.
3. Minutes 20-32 - propose scope, acceptance criteria, and technical path.
4. Minutes 32-42 - integration, deployment, security, and operational ownership.
5. Minutes 42-50 - delivery risks, adoption, and product feedback.
6. Minutes 50-60 - escalation or changed requirement.

Prompt selection:

- Rotate ambiguous discovery, POC scoping, integration risk, poor adoption, and difficult delivery.
- Give the customer a plausible requested solution that may not solve the underlying problem.
- Include one commercial or timeline pressure without turning the case into sales trivia.

Allowed clarifications:

- Workflow, users, sponsor, acceptance criteria, systems, data, identity, network, deployment, security, support, timeline, and ownership.
- The interviewer answers in character and may say the customer does not know.

Follow-ups:

- "We need a commitment today. Will this be live in three weeks?"
- "Security will not approve that data path. What changes?"
- "The demo worked, but operators will not use it. What do you do?"
- "Which part becomes product and which remains customer-specific?"
- "How do you communicate this risk to an executive sponsor?"

Observe:

- Listening, discovery sequence, assumption control, customer communication, scope, architecture, delivery judgment, trust, escalation, and field-to-product learning.

Score dimensions:

- Discovery and outcome definition.
- Customer communication and trust.
- Integration and architecture judgment.
- Scope, acceptance criteria, and delivery plan.
- Risk, security, operations, and escalation.
- Adoption, commercial awareness, and product feedback.

Debrief:

- Interviewer leaves character before feedback.
- Compare what the candidate learned with the hidden fact sheet.
- Identify the highest-value missed question and practice that discovery branch again.

### ML/AI Platform design: 45-60 minutes

Setup:

- Select a platform prompt from [design walkthroughs](06-ml-ai-platform-engineer.md#design-walkthrough-1-multi-provider-model-gateway) or the bank below.
- Define internal customers, workload classes, current fragmented state, adoption constraints, and one operational incident.
- Prepare numerical inputs for capacity or cost.

Timing:

Compact 45-minute schedule:

1. Minutes 0-6 - internal users, repeated need, platform boundary, and non-goals.
2. Minutes 6-12 - workload classes, SLOs, capacity, and cost.
3. Minutes 12-20 - platform contract and developer workflow.
4. Minutes 20-30 - control plane, data plane, and critical internals.
5. Minutes 30-39 - isolation, reliability, observability, and lifecycle.
6. Minutes 39-45 - migration, adoption, economics, and evolution.

Full 60-minute schedule:

1. Minutes 0-7 - internal users, repeated need, platform boundary, and non-goals.
2. Minutes 7-14 - workload classes, SLOs, capacity, and cost.
3. Minutes 14-24 - platform contract and developer workflow.
4. Minutes 24-36 - control plane, data plane, and critical internals.
5. Minutes 36-47 - isolation, reliability, observability, and lifecycle.
6. Minutes 47-60 - migration, adoption, economics, and evolution.

Prompt selection:

- Rotate gateway, inference, training, evaluation, lifecycle, and data capabilities.
- Include a credible alternative such as a library, managed service, or team-owned solution.
- Include at least two workload classes with conflicting needs.

Allowed clarifications:

- Internal users, workload shape, SLOs, hardware, tenancy, security, compliance, current tools, migration constraints, support model, and budget.
- Provide enough data for one useful estimate.

Follow-ups:

- "Why is this a platform rather than a library or standard?"
- "What is the stable contract and what remains implementation detail?"
- "How do you isolate a noisy or compromised tenant?"
- "How does a team migrate and roll back?"
- "What happens during capacity exhaustion?"

Observe:

- Platform boundary, internal customer judgment, contract quality, workload mechanics, reliability, isolation, economics, migration, and organizational leverage.

Score dimensions:

- Platform strategy and boundary.
- Internal customer contract and developer experience.
- Workload, capacity, and cost reasoning.
- Architecture and ML infrastructure depth.
- Reliability, isolation, security, and operations.
- Migration, adoption, and organizational leverage.

Debrief:

- Ask which capability should not be centralized.
- Review whether the contract survives a second workload class.
- Assign one calculation, failure-mode, or migration drill.

### Project deep dive: 30-45 minutes

Setup:

- Candidate selects one prepared dossier from [the project dossier template](08-project-deep-dives-and-take-homes.md#project-dossier-template).
- Interviewer selects role-specific probes and independently identifies likely weak points.
- No confidential artifacts are required. Use sanitized diagrams and truthful ranges.

Timing:

Compact 30-minute schedule:

1. Minutes 0-2 - concise project summary.
2. Minutes 2-7 - context, outcome, scope, and personal ownership.
3. Minutes 7-16 - architecture and two consequential decisions.
4. Minutes 16-24 - evaluation, operations, failures, and results.
5. Minutes 24-30 - adversarial follow-ups, reflection, and role lens.

Full 45-minute schedule:

1. Minutes 0-2 - concise project summary.
2. Minutes 2-8 - context, outcome, scope, and personal ownership.
3. Minutes 8-20 - architecture and two consequential decisions.
4. Minutes 20-30 - evaluation, operations, failures, and results.
5. Minutes 30-45 - adversarial follow-ups, reflection, and role lens.

Prompt selection:

- Choose a project with production evidence and meaningful candidate decisions.
- Rotate the main probe among product outcome, customer delivery, platform leverage, incident, migration, and failed approach.

Allowed clarifications:

- The candidate may state confidentiality limits and use abstractions.
- The interviewer may ask for exact ownership, evidence source, timeline, alternatives, and what was known at the time.

Follow-ups:

- "What decision was yours?"
- "Which alternative did you reject, and on what evidence?"
- "Trace the most important failure end to end."
- "What result can another person verify?"
- "What would you do differently with the information available then?"

Observe:

- Narrative control, ownership precision, technical depth, evidence quality, trade-offs, operations, accountability, and level-appropriate scope.

Score dimensions:

- Problem, outcome, and scope.
- Personal ownership and decision evidence.
- Architecture and technical depth.
- Evaluation, reliability, and risk.
- Results, truthfulness, and learning.
- Senior or staff scope and role relevance.

Debrief:

- Mark every unsupported claim and every unclear "we."
- Choose one layer the candidate could not defend.
- Update the dossier, then re-test with a different interviewer.

### Behavioral: 30-45 minutes

Setup:

- Select two primary questions from the [behavioral question bank](07-senior-staff-behavioral.md#synthesized-behavioral-question-bank).
- Prepare probing follow-ups using the relevant [high-value rubric](07-senior-staff-behavioral.md#high-value-question-rubrics).
- Tell the candidate the target role and level, but not the exact competency labels.

Timing:

Compact 30-minute schedule:

1. Minutes 0-2 - introduction and first question.
2. Minutes 2-11 - first story and probes.
3. Minutes 11-20 - second story and probes.
4. Minutes 20-25 - short third question or level probe.
5. Minutes 25-30 - candidate questions and self-assessment.

Full 45-minute schedule:

1. Minutes 0-3 - introduction and first question.
2. Minutes 3-15 - first story and probes.
3. Minutes 15-27 - second story and probes.
4. Minutes 27-35 - short third question or level probe.
5. Minutes 35-45 - candidate questions and self-assessment.

Prompt selection:

- Do not let the candidate choose only success stories.
- Rotate impact, failure, conflict, influence, ambiguity, incident, prioritization, mentoring, strategy, and safety.
- Avoid using the same story for both primary questions in one mock.

Allowed clarifications:

- Candidate may ask which competency, scope, or time horizon to emphasize.
- Interviewer should not suggest a story.

Follow-ups:

- "What did you personally decide or do?"
- "What evidence did you have at that point?"
- "Who disagreed, and why was their position reasonable?"
- "What changed because of your action?"
- "What did you learn, and where did you apply it?"

Observe:

- Specificity, ownership, decision quality, influence, accountability, evidence, learning, concision, and level.

Score dimensions:

- Situation and stakes.
- Personal ownership and actions.
- Judgment and trade-offs.
- Influence and communication.
- Results, evidence, and accountability.
- Learning, leverage, and level signal.

Debrief:

- Separate story weakness from delivery weakness.
- Identify one missing fact, one unnecessary detail, and one follow-up the story could not survive.
- Update the [12-story bank](07-senior-staff-behavioral.md#build-a-12-story-bank) and re-deliver at 90 seconds.

### Take-home review and live extension

Setup:

- Use a completed take-home or a timeboxed practice repository built from [the take-home operating strategy](08-project-deep-dives-and-take-homes.md#take-home-operating-strategy).
- Interviewer reviews the repository, README, tests, decisions, and known limitations in advance.
- Prepare one small extension, one debugging task, and one architecture challenge.
- Match the original assignment's tool and AI-assistance policy.

Timing for a 60-minute review:

1. Minutes 0-8 - candidate walkthrough and scope.
2. Minutes 8-20 - code, architecture, and decision review.
3. Minutes 20-45 - live extension or debugging task.
4. Minutes 45-53 - tests, production path, and limitations.
5. Minutes 53-60 - reflection and debrief setup.

Timing for a 90-minute review:

1. Minutes 0-8 - candidate walkthrough and scope.
2. Minutes 8-20 - code, architecture, and decision review.
3. Minutes 20-75 - live extension or debugging task.
4. Minutes 75-83 - tests, production path, and limitations.
5. Minutes 83-90 - reflection and debrief setup.

Prompt selection:

- Choose an extension that fits the existing design but tests a real boundary.
- Prefer pagination, idempotency, authorization, evaluation, retries, observability, or schema evolution over unrelated feature work.
- Do not require a rewrite to satisfy a small extension.

Allowed clarifications:

- Expected behavior, compatibility, invalid input, test policy, dependency behavior, and time limit.
- Candidate may consult their own README and decision log.

Follow-ups:

- "What did you deliberately leave out?"
- "Where is the highest production risk?"
- "Show the test that protects this change."
- "How would you roll this out and observe it?"
- "Which AI-generated code, if any, did you verify and how?"

Observe:

- Repository comprehension, scope control, code quality, test strategy, change tolerance, debugging, disclosure, operational judgment, and communication.

Score dimensions:

- Original scope and decision quality.
- Code and architecture comprehension.
- Extension correctness and integration.
- Tests, debugging, and verification.
- Production, security, and operational judgment.
- Communication, disclosure, and time management.

Debrief:

- Distinguish take-home quality from live-extension performance.
- Review the diff and test evidence, not only the demo.
- Select one repository weakness and one live-reasoning weakness for separate practice.

## Specialized Scorecards

Use the common 1-4 scale for every dimension. The behaviors below define what a score of 3 looks like in each format. A 1, 2, or 4 must be justified against the common anchors and the format evidence.

### Coding scorecard

- Framing - confirms inputs, constraints, edge behavior, and target complexity before implementation.
- Derivation - explains a baseline, improves it for a stated reason, and names the invariant.
- Correctness - produces coherent executable code for the core cases without direct rescue.
- Verification - creates normal, boundary, and adversarial tests and traces failures to causes.
- Complexity - states time and space with the correct variables and notices hidden I/O or memory costs.
- Adaptation - incorporates a changed constraint or hint while preserving clarity.

### Progressive implementation scorecard

- Decomposition - delivers the smallest usable behavior at each level.
- Interfaces - separates likely change boundaries without speculative frameworks.
- Incremental correctness - keeps prior behavior passing as requirements arrive.
- Failure handling - makes time, network, persistence, and partial failure explicit where relevant.
- Refactoring - recognizes structural friction and improves it before layering more behavior.
- Ownership - leaves a runnable state, states limitations, and prioritizes under time pressure.

### AI/ML system design scorecard

- Requirements - defines user outcome, quality, scale, latency, reliability, risk, and non-goals.
- Quantitative reasoning - performs at least one decision-relevant estimate with units and assumptions.
- Contracts and architecture - defines APIs or events and traces the primary flow end to end.
- AI/ML judgment - connects data, model, retrieval, training, or inference choices to evaluation evidence.
- Operations and risk - covers observability, degradation, security, privacy, safety, and recovery.
- Evolution - gives a narrow first release, migration or rollout path, and a threshold for the next design change.

### Product AI scorecard

- User judgment - identifies the user, job, current workflow, consequence, and why the problem matters.
- Product decision - compares an AI approach with a non-model baseline and narrows scope.
- Experience - defines normal, uncertain, wrong, and recovery states from the user's perspective.
- Evaluation - creates offline and online evidence tied to a decision, not a vanity metric.
- Launch judgment - specifies guardrails, staged exposure, monitoring, and stopping conditions.
- Learning loop - uses evidence to decide whether to iterate, expand, redesign, or stop.

### FDE scorecard

- Discovery - uncovers workflow, stakeholders, baseline, constraints, unknowns, and acceptance criteria.
- Trust - listens, restates, challenges respectfully, and communicates uncertainty without false commitment.
- Integration - maps data, identity, APIs, networking, deployment, and operational ownership.
- Delivery - sequences discovery, POC, hardening, launch, adoption, support, and handoff.
- Risk - identifies the critical delivery risk, assigns an owner, and defines escalation or validation.
- Product feedback - distinguishes configuration, one-off work, and evidence for a reusable capability.

### ML/AI Platform scorecard

- Strategy - identifies a repeated need, internal customers, platform boundary, and credible alternative.
- Contract - defines a stable self-service interface, ownership model, and escape hatch.
- Mechanics - reasons correctly about workload shape, accelerators, queues, lifecycle, or data movement.
- Reliability and isolation - defines SLOs, admission control, tenant boundaries, failure containment, and recovery.
- Economics - estimates capacity or cost and defines quotas, attribution, or prioritization.
- Adoption - provides migration, compatibility, rollback, support, and deprecation paths.

### Project deep-dive scorecard

- Context - explains the problem, stakes, constraints, and success criteria before architecture.
- Ownership - distinguishes personal decisions and actions from team outcomes.
- Depth - traces data, control, failure, and operational behavior below framework names.
- Evidence - presents truthful results with source, baseline, limitations, and counterevidence.
- Judgment - defends alternatives, sequencing, reversibility, and what was knowable at the time.
- Level - demonstrates independent end-to-end ownership at senior level or cross-team leverage at staff level.

### Behavioral scorecard

- Structure - answers the question directly with enough context and no long preamble.
- Ownership - uses specific actions and decisions rather than vague collective claims.
- Judgment - explains constraints, alternatives, disagreement, and trade-offs.
- Influence - shows how other people understood, challenged, or adopted the decision.
- Accountability - names misses, consequences, and corrective action without blame shifting.
- Impact and learning - gives verifiable outcomes and shows where learning changed later behavior.

### Take-home and live-extension scorecard

- Scope - delivers a coherent vertical slice and clearly documents omissions.
- Code - uses understandable interfaces, error handling, and dependency boundaries.
- Tests - covers core behavior and the highest-risk edge or failure path.
- Evaluation - defines quality evidence appropriate to deterministic or AI behavior.
- Changeability - integrates the extension without destabilizing unrelated behavior.
- Production judgment - covers security, observability, deployment, rollback, cost, and ownership in proportion to scope.

## Feedback Template

Complete this after scoring independently.

```text
Mock:
Date:
Role and level:
Format:
Prompt:
Duration:
Tools allowed:
Hints given:
Recording or notes:

Decision:
- Ready signal, mixed signal, or not-yet-ready signal:
- Hard fail: none or condition with evidence:

Dimension evidence:
- Dimension and score:
  - Observation with timestamp or artifact:
  - Consequence:
  - What a score of 3 would have required:

Strongest repeatable behavior:
- Evidence:
- Why it matters:

Highest-value error:
- Evidence:
- Error taxonomy:
- Likely cause to test:

Next action:
- Drill:
- Success criterion:
- Fresh re-test prompt:
- Re-test date:

Candidate self-assessment:
- What I would keep:
- What I would change:
- What evidence changed my view:
```

Give no more than three improvement items after one mock. Rank them by impact on interview outcome and by how many formats they affect.

## Error Log Taxonomy

Log errors at the behavior level. One event may receive a primary and secondary tag.

### Problem framing

- `FRM-MISS` - missed a requirement that changes the solution.
- `FRM-ASSUME` - made an important assumption without labeling or testing it.
- `FRM-SCOPE` - accepted too much scope or failed to define non-goals.
- `FRM-OUTCOME` - discussed implementation without a user, customer, or platform outcome.

### Reasoning and decisions

- `RSN-BASELINE` - skipped a simple baseline.
- `RSN-ALT` - did not compare a credible alternative.
- `RSN-EVIDENCE` - chose based on preference rather than evidence.
- `RSN-REVERSAL` - failed to change direction after contrary evidence.
- `RSN-LEVEL` - showed local execution where broader level evidence was required.

### Quantitative reasoning

- `QNT-UNITS` - omitted or mixed units.
- `QNT-ASSUME` - hid the dominant assumption.
- `QNT-MATH` - arithmetic or order-of-magnitude error changed the decision.
- `QNT-USE` - calculated a number but did not connect it to design.

### Implementation

- `IMP-CORRECT` - core correctness defect.
- `IMP-STRUCTURE` - code structure blocked the next requirement.
- `IMP-EDGE` - missed an obvious edge case.
- `IMP-FAILURE` - ignored partial failure, retries, time, or invalid input.
- `IMP-TEST` - did not create evidence that the implementation works.

### AI/ML quality

- `AIM-BASELINE` - assumed AI was necessary.
- `AIM-EVAL` - evaluation did not support the product or release decision.
- `AIM-DATA` - ignored data provenance, labels, leakage, drift, or deletion.
- `AIM-UNCERTAINTY` - lacked abstention, review, correction, or recovery.
- `AIM-FEEDBACK` - created an unsafe or biased feedback loop.

### Architecture and operations

- `OPS-CONTRACT` - interface or ownership contract was unclear.
- `OPS-SLO` - lacked a measurable reliability target.
- `OPS-DEGRADE` - lacked safe behavior during dependency or capacity failure.
- `OPS-OBSERVE` - could not detect or diagnose the important failure.
- `OPS-ROLLOUT` - lacked staged rollout, migration, rollback, or compatibility.
- `OPS-COST` - ignored a material cost or capacity constraint.

### Security, privacy, and safety

- `RISK-AUTH` - authorization was not preserved end to end.
- `RISK-TENANT` - tenant isolation was weak or absent.
- `RISK-PRIVACY` - collection, retention, residency, or deletion was unresolved.
- `RISK-ACTION` - destructive or high-consequence action lacked control.
- `RISK-SECRET` - secret handling was unsafe.

### Communication and delivery

- `COM-STRUCTURE` - answer was difficult to follow.
- `COM-LISTEN` - ignored or failed to incorporate interviewer information.
- `COM-PRECISION` - used vague terms where a decision required specifics.
- `COM-TIME` - spent time on low-value detail and left core scope unfinished.
- `COM-CLAIM` - claim exceeded demonstrated evidence.

### Leadership and evidence

- `LDR-OWNERSHIP` - personal contribution was unclear.
- `LDR-INFLUENCE` - result depended on authority without evidence of alignment.
- `LDR-CONFLICT` - dismissed a reasonable opposing position.
- `LDR-ACCOUNT` - avoided accountability or blamed others.
- `LDR-LEARNING` - stated a lesson without later application.

For each logged error, record:

- Timestamp or artifact.
- Triggering condition.
- Observed behavior.
- Consequence.
- Whether a hint changed the behavior.
- Candidate's explanation after the mock.
- Repair drill.
- Re-test result.

## Choose the Next Action

Choose one next action by following this order:

1. Address any hard fail before another full mock.
2. Repair a score of 1 in a core dimension.
3. Repair a repeated score of 2 across two mocks.
4. Repair the error that affects the most formats.
5. Improve a score of 3 toward 4 only when no readiness-limiting weakness remains.

Match the drill to the error:

- Missed requirements - run three five-minute clarification openings with different prompts.
- Weak estimates - run three calculation drills and require a design consequence for each.
- Incorrect code - solve a smaller instance, state the invariant, then implement without a timer.
- Poor testing - create tests for completed solutions without changing the implementation.
- Shallow evaluation - define the decision, dataset, metrics, slices, and release rule before architecture.
- Weak discovery - role-play only the first 12 minutes and score questions asked versus hidden facts.
- Platform overbuilding - compare service, library, standard, managed offering, and team-owned alternatives.
- Vague ownership - rewrite the story using explicit decisions, actions, collaborators, and evidence.
- Time failure - rehearse section transitions with hard checkpoints and forced scope cuts.

Every next action needs a measurable success criterion. "Practice system design" is not an action. "In two fresh 10-minute openings, define users, quality, scale, risk, and non-goals before drawing architecture" is measurable.

## Re-Test Schedule

Use fresh prompts so the re-test measures transfer rather than answer memory.

- Within 24 hours - untimed repair drill with notes.
- After 2-3 days - timed focused re-test on the same dimension with a fresh prompt.
- After 7 days - full mock that includes the repaired skill.
- After 14 days - different interviewer or independently scored recording.
- During weeks 7-8 - realistic mixed mock with no disclosed target dimension.

If the same error appears twice after targeted repair, test the assumed cause. A time-management error may actually come from weak problem framing. A communication error may reflect uncertain technical reasoning. Do not prescribe more repetition until the cause is clearer.

Retire an error only after the candidate demonstrates the target behavior in two fresh prompts, including one full mock. Keep retired errors visible for spaced checks.

## Interviewer Calibration

Calibration aligns evidence standards, not preferred answers.

Before scoring together:

- Agree on target role and level.
- Read the same prompt packet and scorecard.
- Identify acceptable solution families and hard-fail boundaries.
- Decide what counts as a direct hint, a redirect, or ordinary clarification.

Every two weeks:

1. Two interviewers independently score the same recording or detailed transcript.
2. Compare dimension scores without first discussing the candidate.
3. For every difference greater than 1 point, cite the exact evidence.
4. Resolve whether the disagreement came from the anchor, missing evidence, or role expectations.
5. Rewrite an ambiguous anchor or prompt instruction.

Calibration checks:

- Severity - are scores based on the common anchors?
- Evidence - can each score be traced to a behavior?
- Consistency - would the same behavior receive the same score from another candidate?
- Independence - did prior scores, confidence, fluency, or familiarity influence the result?
- Role fit - is the interviewer scoring Product AI, FDE, or Platform behavior rather than a generic favorite profile?
- Level - is staff evidence based on cross-team leverage and durable decisions rather than vocabulary?

Do not force agreement when evidence is genuinely incomplete. Record "insufficient evidence" and adjust the next prompt to elicit the behavior.

## Readiness Rules

Do not declare readiness from one high score or reject readiness from one poor mock.

A format is ready when all of these are true:

- The three most recent full mocks use different prompts.
- At least two mocks were scored by different interviewers or one was independently double-scored.
- Every core dimension scores at least 3 in two of the three mocks.
- No core dimension scores 1 in the most recent two mocks.
- No unresolved hard fail exists.
- The candidate finishes the core scope within time in at least two mocks.
- The candidate handles at least one material follow-up without direct rescue in each of the most recent two mocks.
- Previously repeated errors have passed the re-test rule.

Role-loop readiness requires:

- Ready status in coding or practical implementation.
- Ready status in shared AI/ML design.
- Ready status in the target role case: Product AI, FDE, or Platform.
- Ready status in project deep dive.
- Ready status in behavioral.
- A take-home practice review if the target process includes one.

Use "mixed signal" when evidence is sparse or inconsistent. Schedule another mock instead of averaging away a critical weakness.

Maintain readiness with one full mock and one targeted drill each week until the interview. In the final three days, prefer familiar structure, light retrieval, and sleep over a large new prompt set.

## Mock Bank

Use these prompts as starting points. The linked modules contain detailed frameworks, walkthroughs, and larger banks. The interviewer must still prepare hidden facts, follow-ups, and hard-fail boundaries.

### DSA coding prompts

1. Design an in-memory least-recently-used cache with `get` and `put`, then discuss thread safety and expiration. Use [caches and design](02-coding-and-leetcode.md#must-do-caches-and-design).
2. Given timestamped events, return the busiest rolling interval and then adapt to a stream. Use [sliding window](02-coding-and-leetcode.md#must-do-sliding-window).
3. Merge overlapping maintenance windows and answer whether a new job can be scheduled. Use [intervals](02-coding-and-leetcode.md#must-do-intervals).

### Progressive implementation prompts

1. Build a key-value store, then add TTL, snapshots, and recovery. Use [key-value store with TTL and persistence](02-coding-and-leetcode.md#key-value-store-with-ttl-and-persistence).
2. Build a crawler, then add per-host limits, retries, and resumability. Use [crawler with rate limiting and concurrency](02-coding-and-leetcode.md#crawler-with-rate-limiting-and-concurrency).
3. Build an evaluation runner, then add concurrency, partial results, and reproducible resume. Use [evaluation runner](02-coding-and-leetcode.md#evaluation-runner).

### Shared AI/ML design prompts

1. Design an enterprise document assistant with permission-aware retrieval, citations, freshness, and deletion. Use [Anchor Walkthrough 1](03-ai-ml-system-design.md#anchor-walkthrough-1-enterprise-rag-assistant).
2. Design a support resolution agent that can read records and propose actions but requires approval for consequential changes. Use [Anchor Walkthrough 3](03-ai-ml-system-design.md#anchor-walkthrough-3-support-resolution-agent).
3. Design a real-time fraud model from event ingestion through features, inference, feedback, drift, and retraining. Use [classic ML system design](03-ai-ml-system-design.md#classic-ml-system-design).

### Product AI case prompts

1. A support organization wants an AI copilot to reduce handling effort without lowering resolution quality. Decide what to build, how to evaluate it, and how to launch it. Use [Product Case Exercise 1](04-product-ai-engineer.md#product-case-exercise-1-support-copilot).
2. Employees cannot reliably find current policy answers across documents with different access rules. Decide whether to build an assistant and define its experience, evaluation, and rollout. Use [Product Case Exercise 2](04-product-ai-engineer.md#product-case-exercise-2-enterprise-document-assistant).
3. A vendor-onboarding workflow has many handoffs and the product team proposes a fully autonomous agent. Narrow the problem, define control boundaries, and design the first experiment. Use [Product Case Exercise 3](04-product-ai-engineer.md#product-case-exercise-3-agent-workflow-for-vendor-onboarding).

### FDE discovery and customer prompts

1. A customer says, "We need an AI agent before the executive demo next month." Run discovery and propose a scoped next step. Use [Case 1](05-forward-deployed-engineer.md#case-1-ambiguous-customer-discovery).
2. A regulated enterprise wants RAG over documents spread across repositories with different identity systems. Discover constraints and propose a production path. Use [Case 2](05-forward-deployed-engineer.md#case-2-enterprise-rag-integration).
3. A pilot met offline quality targets but adoption is low and one production incident damaged trust. Diagnose the situation and reset the plan. Use [Case 3](05-forward-deployed-engineer.md#case-3-failing-pilot-and-production-incident).

### ML/AI Platform design prompts

1. Design a multi-provider model gateway with routing, quotas, fallback, auditability, and migration from direct provider calls. Use [Design Walkthrough 1](06-ml-ai-platform-engineer.md#design-walkthrough-1-multi-provider-model-gateway).
2. Design a multi-tenant high-throughput inference platform for interactive and batch workloads. Use [Design Walkthrough 2](06-ml-ai-platform-engineer.md#design-walkthrough-2-high-throughput-inference-platform).
3. Design a GPU training scheduler that supports priorities, gang scheduling, preemption, checkpointing, quotas, and cost attribution. Use [Design Walkthrough 3](06-ml-ai-platform-engineer.md#design-walkthrough-3-gpu-training-and-job-scheduler).

### Project deep-dive prompts

1. Describe a production AI system you owned. Defend one model or architecture choice, one failure, and the evidence that the system improved its target outcome. Use [project deep-dive questions](08-project-deep-dives-and-take-homes.md#synthesized-project-deep-dive-questions).
2. Describe a migration or platform capability that changed how other teams worked. Explain adoption, compatibility, rollback, and measurable leverage. Apply the [ML/AI Platform role lens](08-project-deep-dives-and-take-homes.md#mlai-platform-engineer).
3. Describe a customer or user project where the original request was wrong or incomplete. Explain discovery, reframing, delivery, and what became reusable. Apply the [FDE](08-project-deep-dives-and-take-homes.md#forward-deployed-engineer) or [Product AI](08-project-deep-dives-and-take-homes.md#product-ai-engineer) role lens.

### Behavioral prompts

1. Tell me about a consequential technical decision where reasonable people disagreed. What did you decide, and what evidence changed the outcome? Use [significant disagreement](07-senior-staff-behavioral.md#rubric-4-significant-disagreement).
2. Tell me about a failure caused partly by your judgment. How did you respond, and what changed afterward? Use [failure caused by judgment](07-senior-staff-behavioral.md#rubric-7-failure-caused-by-judgment).
3. Tell me about a time you influenced a direction without authority across team boundaries. Use [influence without authority](07-senior-staff-behavioral.md#rubric-5-influence-without-authority).

### Take-home review and extension prompts

1. Review a document assistant, then add permission-aware filtering and tests without leaking unauthorized metadata. Use [RAG or document assistant](08-project-deep-dives-and-take-homes.md#rag-or-document-assistant).
2. Review an integration agent, then add idempotent retry and safe resume after a partial external failure. Use [agent workflow or integration](08-project-deep-dives-and-take-homes.md#agent-workflow-or-integration).
3. Review a model gateway, then add per-tenant quotas, observable rejection behavior, and a rollback-safe configuration change. Use [model gateway or evaluation service](08-project-deep-dives-and-take-homes.md#model-gateway-or-evaluation-service).

## Eight-Week Mock Cadence

This cadence assumes 15-20 hours per week across the whole curriculum, not 15-20 hours of mocks. Allocate about 3-6 hours weekly to mock execution, review, and repair. Use the [eight-week study plan](10-eight-week-study-plan.md) for the complete allocation.

### Week 1: Establish baselines

- Run one 45-minute DSA mock.
- Run one 45-minute behavioral mock.
- Build the error log and choose two repair drills.
- Spend 3-4 mock-related hours; use remaining study time on shared foundations.

Exit evidence:

- Baseline scorecards exist.
- Tool, timing, and recording rules are established.
- The two highest-value errors have measurable next actions.

### Week 2: Implementation and story control

- Run one 75-90 minute progressive implementation mock.
- Run one 30-minute project deep dive.
- Re-test week 1's weakest coding or behavioral dimension.
- Spend 4-5 mock-related hours.

Exit evidence:

- Candidate can leave each implementation level runnable.
- One project has precise ownership and defensible evidence.

### Week 3: Shared design

- Run one 45-60 minute AI/ML system design mock.
- Run two 10-15 minute requirement and estimation drills.
- Re-test one retired week 1 error.
- Spend 3-5 mock-related hours.

Exit evidence:

- Design opening defines outcome, quality, scale, risk, and non-goals.
- At least one estimate changes a design decision.

### Week 4: First role mock and calibration

- Run one target-role mock: Product AI case, FDE discovery, or Platform design.
- Run one DSA or practical coding mock.
- Double-score one recording or detailed transcript.
- Spend 4-6 mock-related hours.

Exit evidence:

- First role-specific scorecard exists.
- Interviewer scoring differences have evidence and resolution.
- Repeated score-2 dimensions have targeted drills.

### Week 5: Role depth and project defense

- Run a second target-role mock with a fresh prompt.
- Run one 30-45 minute project deep dive with a different interviewer.
- Run one focused role drill based on the error log.
- Spend 4-6 mock-related hours.

Exit evidence:

- Candidate transfers the role framework to a new prompt.
- Project claims survive technical and evidence probes.

### Week 6: Take-home and difficult follow-ups

- Run one take-home review and live extension.
- Run one behavioral mock emphasizing failure, conflict, incident, or safety.
- Re-test the weakest role-specific dimension.
- Spend 5-6 mock-related hours.

Exit evidence:

- Candidate can extend unfamiliar code under time pressure.
- Difficult stories show accountability and later learning.

### Week 7: Full-loop simulation

- Run one coding or progressive implementation mock.
- Run one shared design mock.
- Run one target-role case.
- Run a combined project and behavioral session.
- Use at least two interviewers where possible.
- Spend 5-7 mock-related hours and protect time for review.

Exit evidence:

- Readiness rules can be evaluated from repeated mocks.
- No unresolved hard fail remains.
- Time management holds across multiple formats.

### Week 8: Readiness and maintenance

- Re-test only readiness-limiting dimensions with fresh prompts.
- Run one final target-role mock early in the week.
- Run one short coding or design maintenance session.
- Review project dossiers, story bank, error log, and interview logistics.
- Reduce mock volume in the final three days.
- Spend 3-5 mock-related hours.

Exit evidence:

- Each required loop format meets the repeated-mock readiness rule or is marked mixed signal with a specific mitigation.
- The candidate knows the top remaining risk and how to manage it during the interview.

## Pre-Mock Checklist

Interviewer:

- Prompt packet and hidden facts prepared.
- Follow-ups ordered from ordinary to adversarial.
- Scorecard and hard-fail conditions selected.
- Tool and clarification policy stated.
- Timer and note system ready.
- Recording consent obtained or notes chosen.
- Prior candidate scores hidden during first scoring pass.

Candidate:

- Environment tested.
- Confidential material removed.
- Format and tool rules understood.
- Visible time checkpoints prepared.
- Water, paper, and necessary accessibility support ready.

## Post-Mock Checklist

- Stop the simulation before discussing performance.
- Candidate gives self-assessment.
- Interviewer and observer score independently.
- Every 1 and 4 has evidence.
- Hard fail is evaluated separately.
- No more than three feedback items are selected.
- One next action has a measurable success criterion.
- Focused and full re-tests are scheduled.
- Error log and readiness history are updated.
- Recording is retained or deleted according to consent.

The system works when each mock changes what happens next. Scores are evidence snapshots, not identity judgments. Readiness comes from repeated, independent performance across fresh prompts under realistic constraints.
