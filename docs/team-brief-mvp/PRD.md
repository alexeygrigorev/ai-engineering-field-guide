# Async Team Coordination — product requirements

Version 0.2 · 6 October 2026 · Proposed for review

This replaces the reporting-only scope in version 0.1. Team Brief is now one workflow within the product. This is our interpretation of the Supabase role and a proposed product for companies, not an approved Supabase specification.

## 1. What we are building

A shared platform that runs agents to reduce the effort of keeping an async team coordinated.

**Help people continue their work without waiting for a colleague to come online when the information already exists. When human input is needed, make the question smaller, clearer and less disruptive.**

Agents gather context, answer questions, prepare updates, find inconsistencies and help record human decisions. People retain control of commitments: who owns work, what has been promised and whether something is complete.

The product includes both the agents employees use and the shared machinery for defining, testing, running and controlling those agents.

## 2. The problem today

Information is spread across Slack, Jira, Confluence and repositories. Finding a message is only part of the job. Someone must work out whether it is current, reconcile conflicting sources and explain what it means for another person's work.

Across time zones, a small clarification can take a day. The same explanation is repeated to colleagues, a team lead and leadership. Teams spend effort maintaining shared understanding even when no new decision is needed.

### A concrete example

A frontend engineer in Europe needs an API built by a backend engineer in India. Jira says “In Progress.” A Slack discussion says implementation is finished. Confluence describes an older interface.

The frontend engineer searches three tools, asks for clarification and waits. The answer arrives but does not say whether the API is deployed to staging. Another exchange follows. Later, the product manager asks the same question.

The platform should gather the available evidence and explain:

> Implementation was reported complete in this discussion. I cannot confirm deployment. Jira still records the work as in progress, and the interface document appears older. Here are the sources.

It can prepare a focused question:

> Is version 2 deployed to staging, and which interface document should the frontend team use?

If its policy and contact budget permit, it bundles that question with other necessary questions for the right person. After a human answers, the platform can reuse the clarification where the audience is allowed to see it.

It must not decide that the API is ready, mark the issue Done or promise a delivery date.

## 3. Who uses it

| User | Current effort | How they use the product | Expected benefit |
|---|---|---|---|
| Individual contributor | Search, ask repeated questions, wait for context | Ask in chat or a repository; receive relevant updates and cited answers | Continue work with fewer human handoffs |
| Team lead | Chase updates, reconcile conflicting information, prepare reports | Review briefs, resolve focused questions and approve necessary actions | Less coordination work and clearer exceptions |
| Executive | Request summaries and follow up to understand risks | Read approved cross-team reports within their access | Understand what needs attention without repeated requests |
| Agent author / platform team | Build each automation separately | Register an agent using shared tools, context, policies and tests | Add useful workflows without rebuilding infrastructure |
| Administrator / data owner | Control access and investigate misuse | Approve sources and grants, inspect runs, revoke access | Keep company information and authority under control |

The initial pilot is two engineering/product teams working across time zones. Slack, Jira Cloud and Confluence Cloud are the first integrations. Repository integration is included for distributing approved context and capabilities. The exact repository host is selected with the pilot company.

## 4. Outcomes we want

- Fewer questions that require a colleague to respond.
- Less time searching and reconciling information across tools.
- Shorter waits for usable context.
- Fewer repeated explanations and status requests.
- Less effort preparing updates and recording decisions.
- Reliable automation that people choose to use.

The product cannot resolve a real disagreement or make an undecided dependency ready. It should make those cases visible and easier for humans to handle.

## 5. What employees experience

The following mockups show proposed screens and messages, using one fictional API rollout. Names, times, source references and limits are illustrative. Buttons show intended behavior; they do not represent working integrations.

### Ask and continue working

An employee asks a question in an approved chat or repository surface. The agent retrieves information within that person's permissions and answers with sources. It distinguishes known facts from uncertainty. When it cannot answer, it prepares the smallest useful clarification instead of guessing.

```text
+-----------------------------------------------------------------+
| SLACK  /  Private answer to Maya                                |
|                                                                 |
| Maya: Can the frontend use API v2 in staging?                   |
|                                                                 |
| Coordination assistant                                          |
| Implementation is reported complete. Deployment is unconfirmed. |
|                                                                 |
| Evidence you can access:                                        |
|   [1] Slack: Ravi reported implementation complete at 09:10.    |
|   [2] Jira API-142: still recorded as In Progress.              |
|   [3] Confluence: the linked interface page describes v1.       |
|                                                                 |
| Still needed: staging deployment confirmation and the v2 spec.  |
|                                                                 |
| [Open sources]  [Prepare clarification]                         |
|                                                                 |
| No message sent. No Jira fields changed.                        |
+-----------------------------------------------------------------+
```

The answer helps Maya see exactly what is known. Preparing a clarification does not send it; the contact policy is checked separately.

### Catch up without chasing everyone

An agent prepares a relevant brief on a schedule or after a meaningful event. The brief explains changes, existing decisions and unresolved dependencies. Shared publication follows the configured review policy. It does not automatically send every source event as a notification.

```text
+----------------------------------------------------------+
| TEAM BRIEF  /  API team  /  Draft for lead review        |
|                                                          |
| What changed                                             |
|   API v2 implementation was reported complete. [1]       |
|                                                          |
| What still needs a human answer                          |
|   Is it deployed to staging? Which spec should Maya use? |
|                                                          |
| Existing recorded state                                  |
|   API-142 remains In Progress. [2]                       |
|                                                          |
| Publication check                                        |
|   Destination: #api-team                                 |
|   Source access for this audience: verified              |
|   Human review: required by this reporting agent policy  |
|                                                          |
| [Review sources]  [Edit brief]  [Approve this version]   |
|                                                          |
| Editing after approval requires a new review.            |
+----------------------------------------------------------+
```

This gives the lead an exception to resolve instead of asking everyone for another status update. Approval here covers publishing a report; it does not authorize a change to project commitments.

### Resolve conflicting information

An agent identifies a possible mismatch between a work item, document and discussion. It presents the evidence and suggests who could clarify it based on existing ownership. It does not assign new ownership, change status or repeatedly chase someone.

```text
+----------------------------------------------------------------+
| CLARIFICATION  /  Prepared, not sent                           |
|                                                                |
| To: Ravi  /  Existing API-142 owner in Jira                    |
| Why ask: Maya needs deployment and interface confirmation.     |
|                                                                |
| Proposed message:                                              |
|   Is API v2 deployed to staging?                               |
|   Which interface document should the frontend use?            |
|   Context: [implementation discussion] [API-142]               |
|                                                                |
| Contact checks across ALL agents:                              |
|   Duplicate question: none found                               |
|   Recipient local time: outside working hours                  |
|   Shared budget: one contact available                         |
|                                                                |
| Next step: wait for working hours, then recheck policy.        |
| [Keep queued]  [Cancel]                                        |
|                                                                |
| If the budget is exhausted, wait. Do not send extra reminders. |
+----------------------------------------------------------------+
```

The platform uses existing ownership to route a question. It does not make Ravi responsible for new work or choose a response deadline.

### Record a human decision

A person authors an exact update, chooses its destination and consents to its transfer. The platform carries that update into the approved system and records the result. It must not silently add an owner, deadline or status inferred by a model.

```text
+--------------------------------------------------------+
| RECORD MY UPDATE  /  Signed in as Ravi                 |
|                                                        |
| Destination: Jira API-142                              |
| Operation: Add comment                                 |
|                                                        |
| Text entered by Ravi:                                  |
|   API v2 is deployed to staging. The current interface |
|   document is Confluence / API / v2.                   |
|                                                        |
| Exact effect: add this comment, attributed to Ravi.    |
| Owner, due date and status fields will not be edited.  |
|                                                        |
| [Cancel]  [Authorize this exact comment]               |
|                                                        |
| After success:                                         |
|   Comment recorded. [Open Jira comment] [View receipt] |
|   If the outcome is unknown, show Checking result.     |
|   Do not submit the comment again until reconciled.    |
+--------------------------------------------------------+
```

The form starts empty and records Ravi as the author. A model-generated draft cannot enter this path merely because someone clicked approve. The executor checks current permission and the exact authorized text before sending it.

### Work inside existing tools

People can use approved agents from chat and repositories. A browser interface supports configuration, detailed review and audit inspection. Employees should not have to move all their work into a new application.

## 6. The agent portfolio

The MVP must prove that different kinds of agents use the same platform. Each starts with a narrow job and a named owner; this is not a requirement to build a large autonomous agent network.

| Agent | First useful job | Typical users | Boundary |
|---|---|---|---|
| Question-answering | Answer a scoped question with evidence; admit missing context | Individual contributors | No access beyond the requester and approved sources |
| Reporting | Prepare a team brief and an approved leadership summary | Leads and executives | Do not invent progress or redistribute restricted evidence |
| Drafting | Prepare a decision note or response for human review | All levels | A generated draft is not a human-authored commitment |
| Linting | Flag stale context, missing references or inconsistent statements | Contributors and leads | Findings are suggestions, not silent document changes |
| Triage | Organize incoming questions and identify likely existing owners | Leads and contributors | No autonomous assignment, due date or status change |
| Platform observer | Find failed runs, outdated agent packages or missing ownership | Platform team | Propose fixes; cannot broaden grants or deploy itself |

Question-answering and reporting are the first live workflows. Thin examples of drafting, linting, triage and observation must also pass through the common registration and execution path before calling this a platform MVP.

## 7. Governance is part of the product

The platform decides what an agent is allowed to do before it runs and checks again when it attempts an action. A sentence in a prompt is not an access control.

### Risk tiers

The following tiers are proposed for this product. They are not claimed to be Supabase's existing tier names.

| Tier | Example | Required control |
|---|---|---|
| Internal read | Answer a person's question using authorized sources | Registered owner, scoped reads, source access checks and baseline safety tests |
| Shared internal output | Publish a team summary | Stronger factuality/privacy tests, destination checks and the configured human review gate |
| Consented system update | Carry an exact human-authored update into a work system | Proof of human authorship, explicit consent, exact payload and action validation |
| External output | Publish or communicate outside the company | Additional evaluation and designated human approval; disabled in the first pilot |

Every agent has a registered review policy. This does not mean a person must approve every read or every private answer. Review depth follows the action's risk. Missing policy blocks registration.

### Authority is separate from risk

A higher risk tier does not unlock unlimited autonomy. The platform distinguishes:

- **Read and explain:** describe existing information without changing shared work.
- **Draft:** prepare suggested text without presenting it as an accepted decision.
- **Carry a human decision:** transfer exactly what an authorized person authored and consented to.
- **Contact:** ask or notify only within the agent's permission and the recipient's shared interruption budget.
- **Forbidden autonomous action:** create or change a commitment such as owner, due date or status.

An approval click on an arbitrary model-generated payload does not by itself prove human authorship. Protected updates use a separate human-controlled form or authenticated source record. The person supplies the relevant values, reviews the destination and authorizes the exact update. How that authorship is established is part of the action's contract.

### Make forbidden actions unreachable

Agent runtimes do not receive broad write credentials. They call narrow, approved operations. A separate executor handles permitted changes after checking authority and consent.

If a provider has only broad API permissions, an isolated connector holds that credential and exposes only the allowed operations. The agent cannot retrieve the token or call around the connector. There must be no general-purpose “update anything” tool in the agent's grant.

For the first pilot, demonstrate one consented transfer path, such as a human-authored Jira comment. Autonomous Jira field changes remain unavailable. Adding a protected-field transport later requires its own human-authorship contract and tests; it does not grant the agent authority to choose those values.

## 8. Shared platform requirements

### Register every agent

The inventory records each agent's purpose, owner, risk tier, permitted sources/tools, triggers, model configuration, review policy, contact budget, tests and deployed version.

Nothing runs with missing ownership, unknown tools or an unapproved version. Owners can pause agents and administrators can revoke grants.

```text
+----------------------------------------------------------+
| AGENT INVENTORY  /  Platform team                        |
|                                                          |
| Agent             Owner       Version   State            |
| Team Q&A          API lead    v3        Enabled          |
| Team Brief        API lead    v2        Enabled          |
| Context Linter    Docs lead   v1        Paused           |
|                                                          |
| Selected: Team Q&A v3                                    |
|   Purpose: answer API team questions with sources        |
|   Risk: internal read                                    |
|   Reads: approved Slack, Jira and Confluence scope       |
|   Writes: none                                           |
|   Review: private answers allowed after access checks    |
|   Evaluation: passed for this version                    |
|   Distribution: Slack v3 / repository package v2 (stale) |
|                                                          |
| [View definition]  [View runs]  [Pause agent]            |
|                                                          |
| Stale or revoked packages cannot bypass central checks.  |
+----------------------------------------------------------+
```

This screen makes ownership, capability and version drift visible. A healthy-looking chat response alone is not evidence that the agent is safe to operate.

### Compile and validate definitions

An author describes the agent in a standard format. The compiler turns that definition into a versioned package the runtime and work surfaces can use.

The validator rejects missing fields, invalid dependencies, forbidden capabilities and missing required tests. A new agent should reuse execution, permission, review and logging services rather than rebuilding them.

The MVP does not need a drag-and-drop builder or a system that generates arbitrary agent code.

```text
Agent author
    |
    v
Definition: purpose + owner + sources + tools + review policy
    |
    v
Validate ---- invalid or forbidden capability ----> Reject
    |
    v
Compile a versioned package
    |
    v
Evaluate ---- required tests fail ----------------> Block release
    |
    v
Approve release and register the deployed version
    |
    +---------------------+-----------------------+
    v                     v                       v
Chat surface       Repository surface       Scheduled / event job
    |                     |                       |
    +---------------------+-----------------------+
                          |
                          v
              Shared queue and durable runtime
                          |
                          v
              Check access and allowed actions
                          |
                +---------+----------+
                v                    v
          Read and answer     Exact human review
          within policy       when required
                |                    |
                +---------+----------+
                          v
              Record result and complete trace
```

Every surface uses the same registered permissions. A chat command, repository package or scheduled job cannot grant itself additional authority. The review step cannot make a permanently forbidden autonomous action available.

### Distribute context and capabilities

Approved packages make the right instructions, context references and tool interfaces available in chat and repositories. They carry a version and can be updated or revoked.

Distribution does not copy secrets or broad credentials into repositories. A stale local package cannot bypass the central permission check. The inventory must show which version is deployed where and flag drift.

### Run without an open chat window

Agents run from schedules, incoming events and explicit requests. Work enters a queue, runs under time/cost limits and saves progress durably. A failed process can resume without starting every step again.

The runtime supports different model providers through a common interface. Changing the model does not change permissions or erase the need to evaluate the agent again.

A run waiting for a person saves its state and releases compute. Retrying an event must not repeat a completed external action.

### Review exact actions

Review shows the proposed output, evidence, destination and requested effect. Consent binds to that exact version and expires. Changed content or destination requires fresh review. The executor checks current permission immediately before acting.

### Recover safely

Internal state changes should commit or roll back together. For external tools, the action contract states whether an operation can be reversed, compensated or only reconciled.

If a write times out after it may have succeeded, stop and establish the outcome before retrying. Do not promise a universal atomic undo across Slack, Jira and Confluence. Confirm the intended rollback boundary before enabling each action.

### Reconstruct every run

Record the input, context/source versions, prompts, model responses, tool calls, policy decisions, reviews, effects, errors and costs. Link them with a run ID and agent version.

The warehouse must support a complete reconstruction through appropriately restricted records and protected payload storage. A cost dashboard or sanitized summary alone is insufficient. Access controls and retention apply to the trace itself; logging must not become a new route for private information to leak.

## 9. How the external tools fit

| Tool | Role in the MVP | Main constraint |
|---|---|---|
| Slack | Questions, approved answers, bundled clarifications and notices | Receiving content in a channel is a disclosure; source access and destination audience both matter |
| Jira Cloud | Existing work, ownership, recorded status and change history; one consented human-authored transfer path | An agent cannot infer and write a commitment |
| Confluence Cloud | Plans, decisions and explanatory context | Respect page/space restrictions and show document versions |
| Repository host | Approved agent definitions, context packages, instructions and reviewable changes | Distribution cannot introduce secrets or bypass permission gates |

The pilot starts with selected internal sources. Private channels, external guests and external-facing communication remain disabled until their access and audience behavior is proven.

Use direct chat answers when the audience is authorized. If that cannot be established, deliver a neutral link to an authenticated view. A link is a fallback for protecting access, not a requirement that every useful answer live outside chat.

Installing an integration does not authorize reading every resource it can technically reach. Configure source scope explicitly and preserve the user's effective permissions. Withdrawn access stops future retrieval and disclosure. Revocation cannot erase content someone has already read.

## 10. Contact people carefully

A contact budget belongs to the person across all agents, not separately to each agent. Ten agents must not each decide they can send one harmless reminder.

The platform should:

- Give the useful evidence or partial answer before asking for help.
- Bundle related questions and suppress duplicates.
- Respect working hours, timezone and quiet periods.
- Ask only when missing information affects a real task.
- Stop or wait when the budget is exhausted.
- Distinguish user-requested replies from proactive interruptions, while rate-limiting both.

Budget rules are company-configurable. The pilot begins conservatively and measures whether contacts were useful. Agents cannot label their own work urgent to bypass policy.

## 11. Evaluation and release gates

Every agent has tests for its job and its permitted actions. Shared tests cover platform rules. Agents that do more than read internal data cannot be enabled without the required evaluation evidence.

Start with concrete ways the agent can fail:

- Invent progress or claim that discussion was a decision.
- Reveal a private source to a wider audience.
- Credit the wrong person or use accusatory wording.
- Follow instructions hidden in a retrieved document.
- Attempt a forbidden update or exceed a contact budget.
- Publish an edited action under stale consent.
- Repeat an external action after a timeout.

Use fixed test examples, behavioral assertions and written grading rubrics. Test any model used as a judge against human-labeled cases. Permission rules are deterministic checks, not a judge's opinion.

Run evaluation in CI before a release and mandatory safety checks during execution. Record versions and results. The observer can propose new cases after an incident; it cannot weaken the gate or approve its own changes.

## 12. How we measure success

Measure the coordination problem, not just how much text the system produces.

| Measure | What it tells us |
|---|---|
| Time to a useful answer | Whether employees wait less for context; count a wrong fast answer as a failure |
| Human handoffs per resolved question | Whether fewer clarification exchanges are needed |
| Search, preparation and review effort | Whether total coordination work falls after correction/review is included |
| Repeated questions | Whether existing answers are reused appropriately |
| Useful versus unwanted contacts | Whether agents preserve attention |
| Accuracy, permission failures and corrections | Whether people can trust the output |
| Voluntary repeat use | Whether employees choose to rely on the product |
| Cost per completed workflow | Whether operating cost is justified by demonstrated benefit |

Before activating the pilot, collect comparable examples of the existing process. Review at least four weekly pilot cycles and a sample of everyday questions. Agree numerical targets after observing the baseline; do not invent savings from the number of agent runs.

Maintain a work ledger showing what each agent completed, human effort still required and measured or clearly labeled estimated benefit. Produce a monthly view with its assumptions and queries.

Also provide a simple, query-backed team adoption/maturity view: registered ownership, evaluated workflows, safe operating practices and reliable use. These are proposed dimensions to agree with the company. Teams can inspect and dispute the underlying records. This is not an individual performance ranking.

## 13. What counts as a platform MVP

The MVP is ready for a limited company pilot when:

1. A new agent can be registered, validated, evaluated and made available without a separate deployment design.
2. Reporting and Q&A are useful to pilot teams; narrow examples cover the other portfolio functions.
3. An agent can run from an event, schedule or request without an open UI.
4. A crash/retry preserves state and does not blindly repeat an effect.
5. Forbidden autonomous commitment writes cannot be performed through the available tools or credentials.
6. One human-authored update can be transferred with exact consent and an auditable receipt.
7. Contact budgets apply across agents.
8. An approved package reaches both a chat and repository surface; an outdated or revoked package cannot bypass policy.
9. A reviewer can reconstruct a run and inspect the evidence for a challenged result.
10. The observer can identify a real platform problem and propose a reviewed fix.
11. Backups, restore, integration revocation, retention, release rollback and an operator response have been tested.
12. The team can compare the coordination effort and cost against its previous process.

A weekly summary alone does not satisfy these gates. A configurable framework without a useful employee workflow does not satisfy them either.

## 14. Delivery order

1. Validate the coordination problem and permissions with pilot teams; establish a baseline.
2. Build the shared inventory, validator, basic compiler and durable read-only execution path.
3. Deliver reporting and Q&A through that path, with source permissions and evaluations.
4. Add exact review, one consented transfer and the shared contact budget.
5. Prove distribution into chat and a repository; add thin drafting, linting and triage agents.
6. Add the observer, warehouse reconstruction and work/maturity queries; complete production drills and pilot measurement.

Shared safety and audit controls grow with every slice. They are not deferred until the last step. External-facing output, wider connectors and more autonomy require separate evidence and approval before activation.

The previous reporting-only 8–12 week estimate is withdrawn. Re-estimate this platform scope after validating integration access, runtime choices and the smallest portfolio with the pilot company.

## 15. Open decisions

- Which repeated questions and handoffs currently cost the pilot teams the most?
- Who owns each agent, source scope, review decision and policy?
- Which model/runtime and repository distribution format fit the company?
- How will each connector enforce effective permissions and protect destinations?
- Which exact human-authored update is the first transfer operation?
- What rollback guarantees does that operation support?
- What contact budgets, retention periods and maturity rules will the company adopt?

These are implementation and pilot decisions. They do not change the central product boundary: reduce coordination work while leaving commitments under human control.

## 16. Demonstrable demo before the company pilot

Build a laptop-runnable demonstration of one complete coordination workflow. It should show useful work, human control and recovery in a way someone can inspect. This is an earlier milestone than the production MVP in section 13; it does not replace those acceptance gates.

### The story to demonstrate

Use a fictional team and synthetic company data. Maya needs API v2 for frontend work. Jira records API-142 as In Progress, Ravi has reported implementation complete in Slack, and the interface document still describes v1.

| Step | What the viewer sees | What it proves |
|---|---|---|
| Ask | Maya asks whether API v2 can be used in staging | A concrete coordination need |
| Explain | The agent cites the sources and says deployment is unconfirmed | Evidence gathering and honest uncertainty |
| Clarify | One focused question is prepared for Ravi; contact policy controls sending | Smaller handoffs and bounded interruptions |
| Record | Ravi authors a confirmation and consents to its exact transfer as a Jira comment | Human authorship and controlled execution |
| Reuse | Maya asks again and receives the confirmation with its source | The clarification becomes reusable context |
| Challenge | A forbidden status update is rejected; a worker is restarted during another run | Enforced authority boundaries and durable recovery |

Ravi's response is a cited human confirmation, not independently verified deployment telemetry. The agent must describe that distinction correctly.

### A small frontend

Build one browser application with three views. Slack can serve as the conversational entry point. Link to real source screens rather than rebuilding Slack or Jira.

| View | What it shows |
|---|---|
| Ask & Evidence | Question, answer, source links, conflicting evidence and missing information |
| Review Inbox | Exact text, author, destination, consent, expiry and delivery receipt |
| Agent & Run Inspector | Registered owner, package version, allowed tools, run steps, policy decisions and failures |

Use the mockups in section 5 as the starting point. Label simulated users, fixture sources and live integrations clearly. Demo identity switching must not be presented as production authentication.

### What is real and what can be mocked

Start with fixture connectors, then connect a dedicated Slack workspace and Jira test project. Keep Confluence as local documents initially. All data in connected test accounts must also be synthetic.

| Part | Demo implementation |
|---|---|
| Slack | Real custom app in a test workspace for questions, scoped source reads and permitted replies |
| Jira | Real test project for scoped reads and the human-authored comment operation |
| Confluence | Local documents behind the same typed connector interface as a future live integration |
| Company identities | Seeded users in fixture mode; verified platform identity mapping for live consent and writes |
| Agent inventory and compiler | Real minimal implementation: validate definitions, compile versioned manifests and reject forbidden capabilities |
| Approval and contact budgets | Real backend checks and durable Postgres records |
| Write executor | Separate process and credential boundary; only the permitted comment operation is exposed |
| Workflow recovery | Real durable execution and worker restart |
| Audit and warehouse | Real local run records and export; BigQuery can wait |
| Cloud infrastructure | Local services; managed cloud deployment can wait |

Fixture connectors must support permission denial, conflicting or stale content, rate limits and uncertain write outcomes. Passing these cases demonstrates application behavior. It does not prove enterprise OAuth, provider permissions, data residency or production availability.

For live writes, the executor must use a verified human session or trusted platform identity. A demo user selector cannot authorize real provider actions.

### Local stack and cost

Use React with Vite for the frontend, FastAPI for the backend, local PostgreSQL for product state, the Temporal development server for durable workflows, and local files for protected evidence and trace payloads. Configure persistent local storage so restarting services does not erase the demonstration state. These are development choices; the [HLD](HLD.md) describes the production architecture.

Use a local model through Ollama when the laptop can run a suitable model. A hosted model API is optional and may incur usage charges. Keep a clearly labelled deterministic fixture mode for repeatable failure demonstrations; do not present prerecorded answers as live reasoning.

A local demo can avoid hosting and model API fees using existing hardware. Hardware capacity, electricity and model licensing still apply. Free platform accounts are enough for the proposed small test setup: Slack Free allows up to ten custom or third-party app installations, and Jira Free supports up to ten users. These limits were checked on 6 October 2026 and should be checked again when setting up the accounts. Free plans do not establish that enterprise permission features are available.

Sources: [Temporal local development](https://docs.temporal.io/self-hosted-guide), [Slack Free limits](https://slack.com/help/articles/27204752526611-Feature-limitations-on-the-free-version-of-Slack), [Jira pricing](https://www.atlassian.com/en/software/jira/pricing), [Ollama local models](https://ollama.com/search?c=local).

### Build in two passes

1. **Repeatable local story:** Build the complete flow with fixture connectors, the three frontend views, one registered Q&A agent, a real model option, durable state, review and the isolated executor. Seed the scenario and provide a reset command for local fixture data.
2. **Connected demonstration:** Replace Slack and Jira fixture adapters with real adapters. Prove a real scoped read and one consented comment in the test accounts. Keep fixture mode for reliable demonstrations of outages and permission failures. Resetting local state must not silently delete or replay real provider actions.

### Demo acceptance criteria

- A viewer can follow the story from question to reusable human confirmation, with source links and uncertainty visible.
- An unregistered agent or forbidden capability is rejected by the backend.
- Autonomous Jira owner, due-date and status changes are unavailable through the executor, even if the model requests them.
- A human-authored comment is delivered only with valid consent for its exact content and destination; editing it invalidates previous consent.
- Two agents attempting proactive contact share the same recipient budget.
- Restarting a worker preserves a waiting review and does not blindly repeat a completed external effect.
- An uncertain write enters reconciliation rather than automatic resending.
- A denied source does not appear in the answer or its evidence view.
- The inspector shows the run, policy decisions, consent and receipt, with simulated and live behavior clearly distinguished.

The demo is successful when someone can see both the coordination effort removed and the authority the system leaves with people. Full portfolio coverage, enterprise access validation, cloud operations and measured company-wide benefit remain production MVP work.

## References

- [Supabase AI Platform Engineer JD](https://jobs.ashbyhq.com/supabase/3b5d54ca-741b-45ac-bd3f-31605a0d3541), reread 6 October 2026.
- [Slack Events API](https://docs.slack.dev/apis/events-api/) and [rate limits](https://docs.slack.dev/apis/web-api/rate-limits/).
- [Jira OAuth](https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps/) and [REST API](https://developer.atlassian.com/cloud/jira/platform/rest/v3/).
- [Confluence OAuth](https://developer.atlassian.com/cloud/confluence/oauth-2-3lo-apps/) and [page API](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-page/).

The product examples, tier names, portfolio jobs and rollout choices are our proposed design. Exact Supabase implementation details are not established by the JD.
