# Job-Search Operating System - Design

Date: 2026-08-02
Status: Approved pending user review
Goal: maximize interviews flowing in within 3 months.

## Context

- Working full-time, 2-3h/day for job search (~17h/week)
- Timeline: offers within 3 months (by early November 2026)
- Base CV ready. No company list. LinkedIn/X presence cold.
- Geography: remote (global/EU) plus relocation OK
- Target roles: AI Engineer (product), Forward Deployed Engineer, ML/AI Platform Engineer
- System of record: this repo (markdown). Daily execution: Notion daily todo via Notion MCP.
- Positioning problem: market flooded with shallow "AI engineers". Differentiation = production experience, decision defense, evals ability.

## Structure

New directory `job-search/` at repo root, gitignored (contains personal data: contacts, application status).

```
job-search/
  strategy.md            # categories, time split, tiers, content pillars
  cv/
    base.md              # notes on master CV
    product-ai.md        # role-track tailoring deltas
    fde.md
    platform.md
  companies/
    <company>.md         # one file per target company
  stories/
    work-stories.md      # story bank mined from production work
  content/
    ideas.md             # post ideas backlog
    calendar.md          # what posts when
  practice/
    log.md               # session log: date, type, topic, score, weak areas
  weekly/
    2026-Wxx.md          # weekly plan from Sunday planning session
```

Company file format (human-editable, parseable by `/schedule`):

```markdown
# <Company>

- Tier: 1 | 2 | 3
- Status: researching | applied | interviewing | rejected | offer
- Roles: <role names>
- Contact: name, how known, channel
- CV version: product-ai | fde | platform

## Subtasks

- [ ] Research team and recent launches
- [ ] Find warm intro or hiring manager
- [ ] Tailor CV headline and top bullets
- [ ] Apply on portal
- [ ] Follow-up message day 7
```

Tier 1 gets the full subtask set. Tier 2: research, apply, one outreach. Tier 3: apply only.

## Company Tiers (brand signal, not effort)

- Tier 1 - AI-brand companies. Name alone certifies AI credibility. Labs (OpenAI, Anthropic, Google DeepMind, Mistral, Cohere), AI-forward tech (Cloudflare, Vercel, Bloomberg, Stripe), new-category AI companies with real reputation. Full effort: deep research, warm intro hunt, tailored CV, multi-touch follow-up.
- Tier 2 - Implementation-heavy, customer-deployed AI. Databricks, Palantir, Salesforce, Oracle, ServiceNow, Snowflake. Standard effort.
- Tier 3 - Internal AI in traditional industries (banks, insurance, law, healthcare), only those with public AI reputation. Apply-only, last resort - talent often undervalued.

Early-stage reputation gate. A young company passes only if 2 or more hold:

- Founders from Tier-1 labs/companies
- Backed by top-tier VCs (a16z, Sequoia, Index, top YC batch)
- Real mindshare (viral product, press, developer buzz)
- Named enterprise customers

Fails gate = skip. Borderline cases judged together during company-list build.

Strategic note: Tier 1 rarely responds to cold applies. Content/visibility is the Tier-1 entry weapon - when a hiring manager googles the name, they must see someone shipping production AI.

## Differentiator (Spike)

Being broadly competent is the flooded category. The whole system orients around one named spike. Candidate spikes, all defensible from production work:

- Evals and measurement - "anyone can build, I can measure": eval flywheels, LLM-judges, benchmark analysis
- Reliability and edge cases - AI systems that survive the real world: outliers, bad data, hallucination handling, graceful failure
- Inference engineering - cost, latency, caching, routing, fallbacks at scale
- Natural interaction - agents that talk to users like humans, conversation design, escalation judgment

Selection rule: pick during week-1 story mining, wherever the strongest story cluster sits. Evals and reliability pair well as one identity ("I make AI systems measurable and unbreakable") if stories support both.

Once picked, the spike threads through everything:

- LinkedIn/X headline and bio state it explicitly
- Content: at least 60% of posts feed the spike; pillars reweighted accordingly
- Flagship take-home theme showcases it
- Story mining tags each story by spike relevance; spike stories get rehearsed first
- Tier-1 outreach leads with it ("I do X" beats "I do AI")
- Practice rotation: spike-relevant drills get extra weight in the log

CV note: spike headlines the CV summary, but role-track versions stay broad enough to pass screens.

## Task Categories and Time Allocation

Four categories:

1. Pipeline - company research, applications, outreach, follow-ups
2. Visibility - LinkedIn/X posts, engagement, connection requests, DMs
3. Prep - daily practice with Claude (see rotation), reuses `interview/preparation/`
4. Assets - CV versions, portfolio, profile rewrites

Time split, ~17h/week, phased:

- Phase 1, weeks 1-2 (setup): assets 40%, pipeline 40%, visibility 20%
- Phase 2, weeks 3-8 (engine): pipeline 40%, prep 30%, visibility 25%, assets 5%
- Phase 3, weeks 9-12 (interview-heavy): prep 50%, pipeline 30%, visibility 20%

Rule: pipeline never drops to zero, even mid-interviews. Dead funnel costs ~3 weeks to restart.

## Content Strategy

Pillars, in priority order:

1. Production war stories - sanitized stories from the work-story bank: messy data, outliers, bug forensics
2. Decision-defense posts - "why I chose X over Y, what broke" (mirrors the dominant interview question)
3. Evals series - "how I'd eval X", including take-home build-in-public posts
4. Market observation - light, occasional

Rule: every post carries production specificity - traces, numbers, failure modes. No framework summaries without personal evidence.

Cadence: 2 posts/week from week 2, plus daily 15-minute engagement habit.

## Story Bank

`stories/work-stories.md`. Each story structured as: problem, decision made, alternatives rejected, outcome/metric. Each story used twice:

1. Sanitized version becomes a LinkedIn/X post (confidential details removed together)
2. Full version becomes interview deep-dive ammo, following `interview/preparation/08-project-deep-dives-and-take-homes.md` format

First mining session: Claude interviews the user, target 15-20 stories in one sitting.

## Daily Practice with Claude

45-60 minutes daily. Ranked rotation (weights reflect what interviews actually test, per Reganti insights and `interview/data/research-exports/home-assignments.md`):

1. AI system design - business problem, LLM as brain, tools, knowledge systems, scaling, latency, cost, reliability. Heaviest weight across all tiers.
2. Evals as art - fuzzy metric definition per company context, offline vs online, eval flywheel, LLM-judge vs deterministic checks, benchmark analysis drills (tau-bench-style: pass^k degradation, failure taxonomy)
3. Decision defense - Claude attacks project and story decisions ("why 4 agents not 1"), including repo-walkthrough grilling of the flagship take-home
4. Requirements-gathering roleplay - Claude plays SME (scriptwriter, underwriter), user extracts tacit knowledge in 20 minutes. FDE-specific signal.
5. Applied ML troubleshooting - e.g. RAG retrieves wrong chunks, what do you evaluate first
6. Coding maintenance - 2x/week, Tier-2 insurance. Not zero, not dominant.

Practice log (`practice/log.md`) records every session: date, type, topic, score, weak areas. Weak areas resurface until fixed. Scorecards from `interview/preparation/09-mock-interviews-and-scorecards.md`, extended with the take-home differentiator rubric.

Learn-together sessions include paper reading (tau-bench, evals papers) so drills share vocabulary.

## Take-Home Strategy

Evidence: `interview/data/research-exports/home-assignments.md`. Five archetypes exist; RAG and agent/tool-use dominate. Companies assume anyone can build; they hire people who can measure.

- Weeks 2-3: one flagship take-home. Archetype: agent over messy documents with a full evals framework. Dataset chosen at build time (tau-bench, support tickets, or financial docs). Built against the differentiator rubric: evals framework, cost/latency awareness, observability, fallbacks, architecture diagram, explaining why. Anti-checklist: no "it works" without metrics, no unhandled bad data, no ignored hallucinations, no over-prompting.
- Weeks 5-6: one 3-hour timeboxed speed-run (different muscle - some real assignments are timeboxed).
- Flagship serves three uses: format rehearsal, portfolio repo to defend, 4-6 build-in-public posts.

## Weekly and Daily Flow

- Sunday, 30 min: planning session with Claude. Review pipeline, pick week's tasks from company files, write `weekly/2026-Wxx.md`, mine 1-2 new stories if content backlog low.
- Mon-Sat: `/schedule` reads weekly plan + company files + practice log, picks today's tasks fitting the 2-3h budget, writes them to Notion daily todo via Notion MCP, prints today's practice session type. Until Notion MCP is connected, prints markdown for manual paste.
- Friday: follow-up sweep - every application older than 7 days gets a nudge.

Typical day: 45-60 min practice with Claude, 60-90 min pipeline/visibility/assets work.

## 12-Week Phasing

- Week 1: story mining session, spike selection, 3 CV versions, LinkedIn/X profile rewrites (spike in headline), company list v1 (~40 companies, tiered)
- Weeks 2-3: flagship take-home, first 10 applications (Tier 2/3), posting starts 2x/week
- Weeks 4-8: full engine - 5-8 applications/week, 3 warm outreaches/week, daily practice, Tier-1 outreach with content as proof, week 5-6 speed-run
- Weeks 9-12: interview-heavy - prep 50%, live loops, pipeline stays warm

## Build Order (implementation plan input)

1. `job-search/` skeleton + `strategy.md` (encodes tiers, splits, pillars, rotation, rubrics) + gitignore entry
2. Story mining session (needs nothing but a conversation)
3. Company list build (uses `job-market/` data + tier gate)
4. `/schedule` command + Notion MCP hookup (user connects Notion MCP; markdown fallback until then)
5. First weekly plan - engine on

## Out of Scope

- Funnel metrics dashboards and scripts (revisit if pipeline exceeds ~50 companies)
- Notion-native databases beyond the daily todo
- Fine-tuning/research-track interview prep

## Error Handling and Edge Cases

- Notion MCP unavailable: `/schedule` degrades to printed markdown, system still functional
- Week missed: Sunday session replans from current company-file state; no debt tracking
- Interview load spikes: Phase 3 split applies early; pipeline floor stays above zero
- Confidentiality: content sanitization is a joint step before any post; company files hold personal data and stay gitignored
