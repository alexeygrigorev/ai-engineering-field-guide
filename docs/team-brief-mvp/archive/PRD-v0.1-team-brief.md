# Team Brief — production MVP PRD

Status: proposed, ready for product/engineering review. Version 0.1, 6 October 2026.

This is a reusable company product inspired by the internal-agent operating requirement discussed in this conversation. It is not Supabase's approved specification. Targets, workloads and schedule below are proposed validation criteria, not observed results.

## 1. Product in one sentence

A team lead receives a reviewable weekly brief assembled from authorized Jira activity, Confluence context and selected Slack discussions; the team gets an approved, evidence-linked report without everyone writing another status update.

## 2. Problem and customer

Engineering and product teams distribute their work across issue trackers, documents and chat. Leads repeatedly collect updates, resolve inconsistencies and prepare reports. Leadership lacks a reliable view unless it interrupts teams. Generic AI summaries can mistake discussion for decisions, claim unsupported progress or expose information to the wrong audience.

Initial customer: a company using Slack plus Jira Cloud and Confluence Cloud, with an engineering/product team willing to compare the product with its existing weekly reporting process. Pilot two teams, approximately 10–25 people each. The buyer/sponsor is an engineering or operations leader; the day-to-day owner is a team lead; an IT/security administrator controls integrations and data scope. Not an employee productivity scoring product.

### Users and jobs

| User | Job | Product interaction | Value |
|---|---|---|---|
| Team lead / editor | Produce a trustworthy team update | Review, correct, omit or approve a draft | Less assembly work; retain editorial responsibility |
| Team member | Understand current work without extra reporting | Open a report and follow evidence links; report mistakes | Shared context without another status form |
| Engineering/product leader | See progress, risks and decisions needed | Read approved reports for teams they can access | Fewer ad-hoc requests for updates |
| Company administrator | Control company data and access | Connect tools, configure sources/audience/retention; pause/disconnect | Bounded, auditable access |
| Platform operator | Keep the workflow dependable | Monitor source health, recover runs, respond to incidents | Operable service with explicit failure states |

## 3. MVP scope and primary workflow

Exactly one agent workflow: a scheduled weekly Team Brief, with manual rerun. Source events maintain freshness; they do not generate a stream of notifications. The schedule, reporting period, timezone, owner and audience are human-configured.

1. Administrator connects a Slack workspace and Atlassian site using approved OAuth grants; verifies permitted source and audience boundaries.
2. Team lead selects Jira projects/filter, up to 50 relevant Confluence pages and a small allowlist of internal public Slack channels. No company-wide crawl.
3. Lead defines the brief's reporting period, sections, reviewer and recipient group. Preview the source scope and a sample draft before activation.
4. Platform collects authorized changes, snapshots evidence and exposes source coverage and synchronization times.
5. Agent prepares a draft: completed work, work in progress, explicitly evidenced blockers, documented decisions, unresolved questions and coverage gaps. Every material source-derived claim links to evidence.
6. Lead reviews a browser-based draft, inspects evidence, edits or omits claims, and approves one immutable revision for a specified audience and delivery destination.
7. Publisher sends a neutral Slack notification linking to the approved report. Full report content remains behind authentication and current source-access checks.
8. Recipients open the report; the service checks their identity, report audience and current authorization to its supporting evidence before returning content. They can flag errors. Lead can withdraw or replace the report.
9. Platform records time spent reviewing, source coverage, model/API cost, delivery outcome and feedback. Team compares this with a measured manual baseline.

### Example output

- Completed: JIRA-124 moved to Done during the reporting period, with the issue history cited. This reports recorded state, not independently verified production deployment.
- In progress: JIRA-129 is currently In Progress; a relevant design-page change is linked.
- Needs clarification: Slack contains a discussion of a possible delay, but no confirmed decision; a Jira item records a different target. Cite both without silently choosing one.
- Coverage: Confluence synchronization failed for one selected page; it was not treated as evidence of no work.

Do not infer deadlines, owners, delivery commitments or work completion from conversational tone. Quote existing commitments only with provenance; distinguish observed facts, human editorial additions and explicitly labeled interpretations.

## 4. Goals, non-goals and success measures

Goals: reduce the total work of preparing a useful report, preserve decision authority and data boundaries, provide inspectable evidence, and run reliably under ordinary company API failures.

Non-goals for MVP: general chat/Q&A; automatic Jira creation, comments, assignments or transitions; Confluence publication; private Slack channels, DMs, Slack Connect/external guests; proactive person-by-person chasing; employee scoring; autonomous workflow creation; multi-agent collaboration; self-modification; GitHub/CRM integrations; on-prem installation; Jira/Confluence Data Center.

### Proposed pilot exit criteria

These are targets to validate with the first customer, not contractual guarantees.

| Measure | Definition and target | Collection |
|---|---|---|
| Net preparation effort | Median at least 30% lower total collection + editing + review time against comparable manual reports | Record at least two manual baseline cycles and four pilot cycles per team; include all reviewer work |
| Material claim correctness | At least 95% of sampled draft factual claims supported by cited evidence; unsupported claims and interpretations tracked separately | Human adjudication with written rubric; report sample size and disagreements |
| Citation coverage | 100% of material source-derived claims have a valid evidence reference | Deterministic validation plus sampled entailment review |
| Human adoption | Both pilot leads choose to continue after four cycles; document why | Voluntary feedback, not mandated usage |
| Review burden | Median <=15 minutes per brief at pilot workload | Measured in-product activity, confirmed with lead; idle time excluded |
| Reliable execution | >=99% scheduled workflows reach a reviewable draft or explicit actionable failure within 30 minutes | Measure platform behavior separately from upstream outages and human waiting time |
| Safety | Zero observed unauthorized content disclosures or unapproved publication; all hard safety cases pass release gates | Fault-injection/security tests and incident review; zero observed is not proof of zero future risk |
| Unit economics | Cost per approved brief and total operating cost measured; initial adjustable hard model cap $2/run | Token/provider charges plus separately reported connector, infrastructure and review costs |

No assumed "hours saved" from run counts. Do not count work that staff would not otherwise have done. No expansion claim until the baseline supports it.

## 5. Functional requirements

### Onboarding and administration

FR-01: Authenticate reviewers/readers through company OIDC; bind identities to a single organization and maintain explicitly verified Slack/Atlassian identity mappings. Never infer mappings solely from a display name.

FR-02: Record consented integration grants, site/workspace IDs, token owner, source scope, connection health and revocation state. Encrypt credentials in managed secret storage; no credentials in logs or model context.

FR-03: Show exactly what will be collected, retained and sent to the model. Require source-owner/company data-policy authorization for the pilot. No automatic scope expansion.

FR-04: Configure one workflow owner, reviewer, approved audience, destination channel, schedule/timezone, data scope and retention profile. Missing owner or reviewer blocks activation.

FR-05: Pause a workflow, revoke a connection and disable publication independently. Offboarding disables new runs and queued publications, removes pending contact intents and initiates retention/deletion processing.

### Connectors and ingestion

FR-06: Jira retrieves issue fields and relevant change history for configured projects/filters. Jira state is evidence of recorded workflow state, not proof of shipping. Issue-level permissions still apply.

FR-07: Confluence retrieves selected page bodies and versions as explanatory context. Page and inherited access restrictions apply. Do not ingest attachments in MVP.

FR-08: Slack ingests selected internal public-channel messages, threads and edits/deletions where observable. Prefer incremental events; limited historical backfill shows progress and gaps. Do not ingest DMs/private/shared channels.

FR-09: Deduplicate source events, use cursor/checkpoint-based pagination, respect provider rate limits and reconcile periodically. Webhook loss or delayed synchronization must not masquerade as complete coverage.

FR-10: Preserve source URL, stable ID, revision/time, evidence excerpt, acquisition time, integration principal and scope. Record deletions/revocations as tombstones. Exclude secrets and sensitive categories outside approved policy.

### Generation and review

FR-11: Render a stable brief template using structured claims with evidence IDs. Model-generated text cannot alter audiences, permissions, schedules or tool capabilities.

FR-12: Treat source text as untrusted data. Requests embedded in documents/messages cannot grant tools, change the workflow or trigger publication.

FR-13: If source coverage is incomplete, label affected sections. Required-source failure blocks an ordinary publishable draft; lead may approve an explicitly partial report only when the missing source is a coverage problem, not an authorization/safety failure.

FR-14: Review UI displays reporting period, source health, evidence, claim categories, changes from prior revision and destination/audience. Editing creates a new revision. Human-added assertions are labeled editorial and attributed, never presented as model-verified facts.

FR-15: Approvals bind reviewer identity, exact revision hash, audience/policy version, destination and expiry. Proposed default expiry 24 hours. Any edit, target change, audience change or withdrawal invalidates queued consent.

FR-16: Publication rechecks current approval, reviewer authority, connection state, workflow policy and notification budget. One logical publication has one durable identity and an external receipt.

### Consumption and feedback

FR-17: Slack sends only a neutral authenticated report link; no issue titles, blockers, counts, private quotations or source snippets in the notification. Links contain no bearer credential. Disable link unfurling; unauthenticated metadata must be generic.

FR-18: Report access requires both configured audience membership and currently demonstrable source permissions. MVP uses connected recipient identities to verify access to all evidence underlying the full report; if that cannot be established, withhold the report. Do not rely on the bot's access as a substitute. Customer onboarding must prove this connector capability before admitting real data.

FR-19: Changing Slack membership does not grant report access. Adding recipients requires verified identity/source authorization. Revocation removes access to hosted content; already viewed content cannot be recalled.

FR-20: A recipient can flag an incorrect claim. Lead can withdraw the hosted report, post a neutral correction notice or issue a replacement revision. The audit history remains restricted according to retention policy.

### Measurement

FR-21: Show run cost, preparation/review effort, errors, corrections and source coverage per workflow. Separate measured values from estimates and missing data.

FR-22: Export company-owned reports/metrics and allow deletion of retained content. Audits retain only the minimum legally/customer-authorized metadata; retention is not indefinite by default.

## 6. Permission and action contract

| Capability | Allowed in MVP? | Enforcement |
|---|---|---|
| Read configured authorized sources | Yes | OAuth scopes, provider permissions and server-side source allowlists |
| Draft internal reports | Yes | Bounded model context, validated output and review state |
| Publish neutral Slack link | After exact approval | Separate publisher identity and narrow typed operation |
| Read arbitrary channels/projects/pages | No | Scope validation before connector call; runtime cannot supply arbitrary site IDs |
| Modify Jira or Confluence | No | No write scopes, credentials or exposed methods |
| Set owner, due date or status | No | No corresponding tool/endpoint route; denied at connector/IAM/egress boundaries |
| Modify grants, evaluations or its own deployment | No | Human-controlled versioned release pipeline |

OAuth scope is necessary but not the whole authorization decision. Provider user/site permissions constrain Atlassian delegated access. A single all-powerful API token is not an MVP shortcut. Native field-level restrictions cannot be assumed; the strongest MVP boundary is to expose no Jira/Confluence write capability at all.

## 7. Production and data requirements

Initial delivery model: managed, isolated deployment per customer, using automated infrastructure templates. Application records carry organization IDs and enforce isolation even within a customer's deployment. Multi-company shared SaaS is postponed. GCP is the reference environment; hosting/provider region must match the first customer's approved policy.

- Postgres is durable authority for workflows, attempts, evidence metadata, report revisions, approvals, publication intents and outbox. Backup/PITR configured and restore tested.
- Python services on Cloud Run: application/API, bounded worker, isolated publisher. Small shared codebase; separate service identities. Cloud Tasks, Cloud Scheduler, Secret Manager, encrypted artifact storage and BigQuery. No Kubernetes requirement.
- Runtime executes bounded graph steps and checkpoints; a review wait releases the worker. Transactional outbox avoids state/dispatch gaps. Leases/fencing prevent stale attempts from changing current state.
- Reference pilot load: <=5 workflows/customer, <=200 candidate Jira issues and <=50 Confluence pages/run, <=20,000 incremental Slack messages/week/customer, <=10 concurrently runnable steps. Exceeding caps displays explicit limited coverage; load test before changing them.
- Proposed API target P95 <500ms excluding external calls; draft target <15 minutes at pilot load when dependencies are healthy; authenticated report read <3 seconds excluding fresh provider-access checks. Present access verification separately; never skip it to meet latency.
- Proposed recovery targets RPO <=15 minutes and RTO <=4 hours for pilot platform data; validate backups and restore drills before promising them to a customer.
- Proposed default retention: source snapshots/model artifacts 30 days; reports 90 days; audit metadata 180 days. Customer review/region requirements determine final values. Do not put unrestricted prompt payloads in broadly readable analytics tables.
- Model provider must offer an acceptable business-data processing agreement, approved region/retention behavior and appropriate training-use settings. If unavailable, hold pilot activation. Tokens/cost budgets and provider timeout policies are enforced.
- Accessibility, keyboard review and explicit status/error messages; selected schedule timezone handles DST. No silent fail-open authorization.

## 8. Reliability and failure UX

| Failure | Expected behavior |
|---|---|
| Duplicate event/task | Reuse logical run/step identity; no duplicate report or intended publication |
| Source 429 | Respect Retry-After, persist progress, back off within source budget |
| Source token revoked/403 | Pause dependent workflow; do not treat inaccessible data as empty |
| Upstream outage | Mark source unhealthy; retry boundedly; explicit partial/blocked draft |
| Worker crashes | Resume checkpoint; completed reads/model outputs reused where safe |
| Unsupported model output | Validation fails; bounded retry or needs-review failure, never publish |
| Approval arrives after edit | Reject stale approval; request review of latest revision |
| Slack send succeeds but receipt save fails | OUTCOME_UNKNOWN; reconcile when possible; no blind send retry |
| Deletion/access change | Tombstone source, invalidate dependent hosted content or block until revalidated |
| User withdraws approval during dispatch | Cancellation before send is enforced; in-flight send may be irreversible, visible receipt/reconciliation required |

No universal exactly-once guarantee from Slack. Store delivery identity in supported metadata, perform safe reconciliation when supported and escalate ambiguity to an operator. A duplicate neutral notification is still an incident to track. Report rollback means withdrawing/replacing hosted content; it cannot erase something a recipient already read.

## 9. User stories

1. As a lead, I want to configure an existing team's sources so that I do not create a second reporting system.
2. As an administrator, I want minimal requested grants so that a pilot cannot mutate company work records.
3. As a lead, I want a sample before scheduling so that I can assess whether the product understands the workflow.
4. As a lead, I want claims linked to evidence so that review is faster than rereading all sources.
5. As a lead, I want uncertainty shown so that guesses do not become commitments.
6. As a lead, I want to edit/omit a claim so that I remain responsible for published communication.
7. As a reviewer, I want approval attached to a specific revision so that nothing changes after consent.
8. As a reader, I want current permissions respected so that the report does not bypass source restrictions.
9. As a reader, I want a neutral Slack link so that confidential content is not permanently copied into chat.
10. As a team member, I want no repeated pings so that the product saves attention.
11. As an administrator, I want to revoke access immediately so that offboarding is effective.
12. As an operator, I want durable recovery and receipts so that retries do not cause duplicate actions.
13. As a lead, I want incomplete coverage clearly marked so that silence is not interpreted as no work.
14. As a reader, I want to flag a mistake so that corrections improve future reports.
15. As a sponsor, I want total effort/cost compared with a manual baseline so that adoption is justified.
16. As a customer, I want export/deletion controls so that I retain control of company data.

## 10. Release and acceptance gates

Release gate combines deterministic authorization/action assertions with human-labeled factuality cases and calibrated rubric-based evaluation. Test the product through its workflow API and real sandbox connector contracts, with controllable external-provider fakes for failures. No existing application test seams assumed: this repository is a field guide, not the implementation.

Before real-data pilot: OAuth grants reviewed; report/source authorization behavior demonstrated; forbidden writes unreachable; release safety suite passes; restore drill passes; source-rate-limit measurements made; logging/secrets retention verified; support owner and runbooks assigned.

Before paid/expanded operation: four consecutive pilot cycles, measured effort improvement, tolerable correction rate, no unresolved severe safety incident, tested upgrade/rollback, customer admin can disconnect and delete, operator can reconcile an ambiguous publication.

## 11. Decisions and discovery still required

Chosen: one reporting workflow, Cloud-only tools, read-only Jira/Confluence, authenticated report UI, approved neutral Slack delivery, isolated customer deployment, no self-modifying agents.

Validate before implementation locks: company identity provider, OAuth deployment/distribution path, Slack app classification and method limits, supported audience-permission checks in Atlassian, pilot source sizes, customer data agreement/region, baseline reporting behavior and final retention. If permission preservation cannot be demonstrated, use synthetic data only; never relax it to reach a demo date.

## 12. Primary documentation checked 6 October 2026

- [Slack Events API](https://docs.slack.dev/apis/events-api/) — event visibility and retries.
- [Slack request verification](https://docs.slack.dev/authentication/verifying-requests-from-slack/) — request authentication/replay handling.
- [Slack rate limits](https://docs.slack.dev/apis/web-api/rate-limits/) — app classification affects history/replies access; honor Retry-After. Do not assume an internal app and a commercially distributed non-Marketplace app have identical limits.
- [Jira OAuth 2.0](https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps/) and [Jira REST](https://developer.atlassian.com/cloud/jira/platform/rest/v3/) — consented delegated access and per-operation requirements.
- [Confluence OAuth](https://developer.atlassian.com/cloud/confluence/oauth-2-3lo-apps/) and [page API](https://developer.atlassian.com/cloud/confluence/rest/v2/api-group-page/) — delegated content access and page versions.

These sources establish integration constraints, not market demand or the proposed pilot targets.
