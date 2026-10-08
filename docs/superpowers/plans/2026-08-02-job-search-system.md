# Job-Search Operating System Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking. NOTE: Tasks 4-7 are interactive sessions with the user and cannot be delegated to subagents.

**Goal:** Build the job-search operating system from the approved spec: `job-search/` directory, `/daily` and `/weekly` commands, story bank, company list, first weekly plan.

**Architecture:** Plain markdown files in a gitignored `job-search/` directory act as the database. Two Claude Code slash commands (`.claude/commands/daily.md`, `.claude/commands/weekly.md`) encode the daily and weekly rituals. Notion MCP is the task-delivery channel with markdown fallback.

**Tech Stack:** Markdown, Claude Code slash commands, Notion MCP (user-connected).

## Global Constraints

- NEVER run `git commit` or `git push` (user's global rule). Stage files and provide commit message text only.
- `job-search/` is gitignored - personal data (contacts, application status) never gets committed.
- Repo files follow `STYLING.md`: no bold, no italics, no horizontal rules, lists preferred, H1 once per doc.
- Command names are `/daily` and `/weekly` (NOT `/schedule` - collides with existing schedule skill).
- Spec is authoritative: `docs/superpowers/specs/2026-08-02-job-search-system-design.md`.
- Tasks 4-7 require the user present. Do not fabricate stories, companies, or CV content.

---

### Task 1: Gitignore + directory skeleton + strategy.md

**Files:**

- Modify: `.gitignore` (create if absent)
- Create: `job-search/strategy.md`
- Create: `job-search/cv/`, `job-search/companies/`, `job-search/stories/`, `job-search/content/`, `job-search/practice/`, `job-search/weekly/` (via the files in Tasks 1-2)

**Interfaces:**

- Produces: `job-search/strategy.md` - read by `/daily` and `/weekly` commands (Task 3) for time splits, rotation, rubrics.

- [ ] **Step 1: Add gitignore entry**

Append to `.gitignore` (create file if it does not exist):

```
# Personal job-search data - never commit
job-search/
```

- [ ] **Step 2: Verify ignore works**

Run: `mkdir -p job-search && touch job-search/probe.md && git check-ignore job-search/probe.md && rm job-search/probe.md`
Expected: prints `job-search/probe.md` (exit 0).

- [ ] **Step 3: Write strategy.md**

Create `job-search/strategy.md` with exactly this content:

```markdown
# Job-Search Strategy

Goal: maximize interviews. Offers by early November 2026.
Budget: ~17h/week (2h weekdays, 3.5h weekend days).
Spec: docs/superpowers/specs/2026-08-02-job-search-system-design.md

## Spike (differentiator)

Status: not yet selected. Pick during week-1 story mining from:

- Evals and measurement
- Reliability and edge cases
- Inference engineering
- Natural interaction

Once selected, record it here and thread through headline, 60%+ of
content, flagship take-home, story rehearsal order, Tier-1 outreach.

## Company tiers

- Tier 1 - AI-brand: labs (OpenAI, Anthropic, Google DeepMind, Mistral,
  Cohere), AI-forward tech (Cloudflare, Vercel, Bloomberg, Stripe),
  reputed new-category AI companies. Full effort.
- Tier 2 - implementation-heavy customer AI: Databricks, Palantir,
  Salesforce, Oracle, ServiceNow, Snowflake. Standard effort.
- Tier 3 - internal AI in regulated industries, only with public AI
  reputation. Apply-only, last resort.

Early-stage gate, must hold 2+:

- Founders from Tier-1 labs/companies
- Top-tier VCs (a16z, Sequoia, Index, top YC batch)
- Real mindshare (viral product, press, developer buzz)
- Named enterprise customers

## Time split by phase

- Phase 1, weeks 1-2: assets 40 / pipeline 40 / visibility 20
- Phase 2, weeks 3-8: pipeline 40 / prep 30 / visibility 25 / assets 5
- Phase 3, weeks 9-12: prep 50 / pipeline 30 / visibility 20

Rule: pipeline never zero.

## Practice rotation (ranked)

1. AI system design - business problem, LLM as brain, tools, knowledge,
   scaling, latency, cost, reliability
2. Evals as art - fuzzy metrics per company, flywheel, LLM-judge vs
   deterministic, benchmark analysis (pass^k, failure taxonomy)
3. Decision defense - attack my project/story decisions; repo
   walkthrough grilling of flagship take-home
4. Requirements-gathering roleplay - Claude plays SME, I extract tacit
   knowledge in 20 min
5. Applied ML troubleshooting - e.g. RAG retrieves wrong chunks
6. Coding maintenance - 2x/week

## Take-home rubric (score every take-home and design session)

Differentiators: evals framework, cost/latency awareness, observability,
fallbacks, architecture diagram, explaining why.
Instant rejects: no metrics, unhandled bad data, ignored hallucinations,
over-prompting.

## Content pillars

1. Production war stories (sanitized)
2. Decision-defense posts
3. Evals series, incl. take-home build-in-public
4. Market observation (light)

Rules: every post carries production specificity. 60%+ of posts feed the
spike. Cadence: 2 posts/week from week 2 + daily 15-min engagement.

## Weekly rhythm

- Sunday: /weekly planning session
- Mon-Sat: /daily - tasks to Notion + practice session
- Friday: follow-up sweep, applications older than 7 days
```

- [ ] **Step 4: Verify**

Run: `ls job-search/ && head -5 job-search/strategy.md`
Expected: `strategy.md` listed, header prints.

- [ ] **Step 5: Stage .gitignore, provide commit message**

Run: `git add .gitignore`
Provide commit message: `chore: gitignore personal job-search directory`
Do NOT commit.

### Task 2: Templates and scaffolds

**Files:**

- Create: `job-search/companies/_template.md`
- Create: `job-search/stories/work-stories.md`
- Create: `job-search/practice/log.md`
- Create: `job-search/content/ideas.md`
- Create: `job-search/content/calendar.md`
- Create: `job-search/cv/base.md`

**Interfaces:**

- Produces: company template consumed by Task 6; log format consumed by `/daily` (Task 3); story format consumed by Task 4.

- [ ] **Step 1: Company template**

Create `job-search/companies/_template.md`:

```markdown
# <Company>

- Tier: 1 | 2 | 3
- Status: researching
- Roles: <role names + links to postings>
- Contact: <name, how known, channel - or none yet>
- CV version: product-ai | fde | platform
- Applied: <date or ->
- Last touch: <date or ->

## Notes

<recent launches, team, why interesting>

## Subtasks

- [ ] Research team and recent launches
- [ ] Find warm intro or hiring manager
- [ ] Tailor CV headline and top bullets
- [ ] Apply on portal
- [ ] Follow-up message day 7
```

Tier 2: delete warm-intro and follow-up lines. Tier 3: keep apply line only.

- [ ] **Step 2: Story bank scaffold**

Create `job-search/stories/work-stories.md`:

```markdown
# Work Stories

Each story: mined once, used twice (sanitized post + full interview
answer). Spike tags assigned after spike selection.

Format per story:

## S<N>: <short title>

- Spike relevance: <spike name or ->
- Problem: <what was broken/needed, scale, constraints>
- Decision: <what I chose>
- Alternatives rejected: <options + why not>
- Outcome: <metric, before/after>
- Confidential elements: <what must be sanitized before posting>
- Post status: not-drafted | drafted | published
- Rehearsed verbally: no | yes (<date>)
```

- [ ] **Step 3: Practice log scaffold**

Create `job-search/practice/log.md`:

```markdown
# Practice Log

## Weak areas (live list, prune when fixed)

- none logged yet

## Sessions

Format:

### <date> - <rotation type> - <topic>

- Score: <1-5>
- Weak: <specific gaps>
- Next: <what to drill again>
```

- [ ] **Step 4: Content scaffolds**

Create `job-search/content/ideas.md`:

```markdown
# Post Ideas Backlog

Format: - [ ] <pillar> | <one-line idea> | source: <story id or event>

Backlog low-water mark: 4 ideas. /weekly prompts mining when below.
```

Create `job-search/content/calendar.md`:

```markdown
# Content Calendar

Format: - <date> | <platform> | <idea ref> | status: planned | posted
Cadence: 2 posts/week from week 2.
```

- [ ] **Step 5: CV notes scaffold**

Create `job-search/cv/base.md`:

```markdown
# Base CV Notes

Master CV location: <fill in - file path or link>

Role-track deltas live in product-ai.md, fde.md, platform.md (created
in Task 5 with the user). Each delta file records: headline, summary
line, top 3 bullets to swap, keywords for that track.
```

- [ ] **Step 6: Verify**

Run: `find job-search -name "*.md" | sort`
Expected: 7 files (strategy + 6 from this task).

### Task 3: /daily and /weekly commands

**Files:**

- Create: `.claude/commands/daily.md`
- Create: `.claude/commands/weekly.md`

**Interfaces:**

- Consumes: `job-search/strategy.md`, `job-search/weekly/<ISO-week>.md`, `job-search/practice/log.md`, `job-search/companies/*.md`.
- Produces: Notion tasks (or markdown fallback), practice session, updated log.

- [ ] **Step 1: Write /daily command**

Create `.claude/commands/daily.md`:

```markdown
Run the daily job-search ritual. Act as proactive coach throughout.

1. Read job-search/strategy.md, the current ISO-week file in
   job-search/weekly/ (e.g. 2026-W32.md), and the last 5 entries plus
   weak-areas list in job-search/practice/log.md. If the weekly file is
   missing, say so and offer to run /weekly first.
2. Assemble today's tasks, fitting 2-3 hours total:
   - Unfinished items from the weekly plan, respecting the current
     phase's time split in strategy.md
   - Always exactly one practice session (45-60 min). Choose type from
     the ranked rotation: prioritize live weak areas, then the type
     least recently practiced. Coding counts max 2x/week.
   - If today is Friday: scan job-search/companies/*.md for Status:
     applied with Applied date older than 7 days and Last touch older
     than 7 days; add one follow-up task per company.
3. Deliver tasks: if Notion MCP tools are available, add each task to
   the Notion daily todo for today and confirm. Otherwise print a
   markdown checklist for manual paste and remind the user once to
   connect Notion MCP.
4. Start the practice session immediately: announce type and topic,
   then run it per the rotation description in strategy.md. Score
   against the take-home rubric where applicable. Real interview
   pacing: one question at a time, push for out-loud-style full
   answers, then feedback.
5. After the session, append an entry to job-search/practice/log.md
   (date, type, topic, score 1-5, weak areas, next) and update the
   weak-areas list.
6. Close by listing what remains for today and any overdue items
   (posts behind cadence, applications below weekly target).
```

- [ ] **Step 2: Write /weekly command**

Create `.claude/commands/weekly.md`:

```markdown
Run the Sunday planning session. Act as proactive coach.

1. Read job-search/strategy.md, last week's file in job-search/weekly/
   (if any), job-search/practice/log.md, job-search/content/ideas.md,
   job-search/content/calendar.md, and every job-search/companies/*.md
   frontmatter list (Tier, Status, Applied, Last touch).
2. Review out loud with the user: what got done vs planned, pipeline
   counts by status, posts published vs cadence, practice scores trend,
   weak areas. Flag anything behind the spec's weekly targets
   (phase 2: 5-8 applies, 3 outreaches, 2 posts).
3. Determine current phase (week number since 2026-08-03) and time
   split from strategy.md.
4. Agree next week's tasks interactively, then write
   job-search/weekly/<ISO-week>.md:

   # Week <ISO-week> (<date range>)

   Phase: <1|2|3>

   ## Targets

   - Applications: <n>
   - Outreach: <n>
   - Posts: <n>
   - Practice sessions: 6

   ## Pipeline

   - [ ] <task per company, from companies/*.md subtasks>

   ## Visibility

   - [ ] <post drafts, engagement, connection targets>

   ## Prep

   - [ ] <rotation focus for the week, take-home work if scheduled>

   ## Assets

   - [ ] <CV tweaks, profile edits - often empty after week 2>

5. If content/ideas.md has fewer than 4 unchecked ideas, run a short
   story-mining top-up: ask about recent work, add stories to
   work-stories.md, add ideas to ideas.md.
6. Close with the week's single most important outcome, named.
```

- [ ] **Step 3: Verify commands load**

Run: `ls .claude/commands/`
Expected: `daily.md`, `weekly.md`. Tell the user both are invocable as `/daily` and `/weekly` next session.

- [ ] **Step 4: Stage, provide commit message**

Run: `git add .claude/commands/daily.md .claude/commands/weekly.md`
Provide commit message: `feat: add /daily and /weekly job-search ritual commands`
Do NOT commit.

### Task 4: Story mining session + spike selection (INTERACTIVE)

**Files:**

- Modify: `job-search/stories/work-stories.md`
- Modify: `job-search/strategy.md` (Spike section)
- Modify: `job-search/content/ideas.md`

**Interfaces:**

- Consumes: story format from Task 2.
- Produces: 15-20 stories; selected spike recorded in `strategy.md`; 8+ post ideas.

- [ ] **Step 1: Run mining interview (~90 min)**

Interview the user about production work. Question tracks, one at a time, dig for decision + alternatives + metric on each:

- Hardest bug you fixed in the AI system - what did it turn out to be?
- A technical decision you made that others pushed back on
- A time the LLM was confidently wrong in production - what did you do?
- Messy/unstructured data you had to make usable
- Something you measured that changed a decision (evals, metrics)
- Cost or latency problem and what you traded off
- An edge case that broke everything and the fix
- Something you built that users touched directly - what surprised you?
- A time requirements were wrong and you found out late

Capture each story in the work-stories.md format immediately, target 15-20.

- [ ] **Step 2: Select spike**

Tally stories by candidate spike (evals, reliability/edge-cases, inference engineering, natural interaction). Present tally, recommend the densest cluster (merge evals+reliability if both strong). User decides. Update `strategy.md` Spike section: replace status line with selected spike and one-line identity statement.

- [ ] **Step 3: Tag stories and seed content backlog**

Fill Spike relevance on every story. Add 8+ entries to `content/ideas.md` from the strongest stories, pillar-tagged, spike-heavy.

- [ ] **Step 4: Verify**

Count stories: `grep -c "^## S" job-search/stories/work-stories.md` - expected 15+. Spike section no longer says "not yet selected".

### Task 5: CV role-track versions (INTERACTIVE)

**Files:**

- Modify: `job-search/cv/base.md` (master CV location filled)
- Create: `job-search/cv/product-ai.md`
- Create: `job-search/cv/fde.md`
- Create: `job-search/cv/platform.md`

**Interfaces:**

- Consumes: user's base CV (user provides file/text); spike from Task 4.
- Produces: three delta files referenced by company files' CV version field.

- [ ] **Step 1: Get base CV**

Ask user for the master CV (path or pasted text). Record location in `cv/base.md`. Read it.

- [ ] **Step 2: Draft three delta files**

Each delta file, same structure:

```markdown
# CV Delta: <track>

- Headline: <one line, spike-forward>
- Summary: <2-3 lines for this track>
- Top bullets to lead with: <3 bullets, reordered/rewritten from base>
- Keywords to ensure present: <ATS terms for this track>
- Cut for this version: <what to drop>
```

Track emphases: product-ai = shipped LLM features, users, product metrics; fde = customer-facing, requirements-gathering, deployment stories; platform = infra, serving, evals platform, cost/latency. Spike headlines all three; each stays broad enough to pass screens. Draft with user, iterate until approved.

- [ ] **Step 3: Verify**

Run: `ls job-search/cv/`
Expected: 4 files. User has confirmed each delta.

### Task 6: Company list build (INTERACTIVE)

**Files:**

- Create: `job-search/companies/<company>.md` (~40 files)

**Interfaces:**

- Consumes: `_template.md` (Task 2), tier definitions in `strategy.md`, `job-market/` repo data.
- Produces: tiered company files consumed by `/weekly` and `/daily`.

- [ ] **Step 1: Seed candidate list**

Sources: tier examples in strategy.md, `job-market/` data (check `job-market/data_structured/` and `trends.md` for companies actually posting AI eng roles), user's own list from head. Target ~60 candidates before filtering.

- [ ] **Step 2: Tier and gate together**

Walk the list with the user. Assign tier per strategy.md definitions. Run every young company through the early-stage gate (2+ criteria or skip). Check remote-global/EU or relocation feasibility. Keep ~40.

- [ ] **Step 3: Create company files**

One file per keeper from `_template.md`, subtasks trimmed by tier. Fill Roles only where a live posting is known; otherwise first subtask is finding one.

- [ ] **Step 4: Verify**

Run: `ls job-search/companies/ | wc -l` - expected ~41 (40 + template). Spot-check 3 files for correct tier-trimmed subtasks.

### Task 7: First weekly plan + first daily run (INTERACTIVE)

**Files:**

- Create: `job-search/weekly/<current-ISO-week>.md`
- Modify: `job-search/practice/log.md`

**Interfaces:**

- Consumes: everything above.
- Produces: running engine.

- [ ] **Step 1: Run /weekly**

Invoke the `/weekly` command flow (Task 3 content). Week 1 targets per spec: story mining done (Task 4), spike done, CV versions done (Task 5), company list done (Task 6), so plan covers: LinkedIn/X profile rewrites (spike headline), first Tier-3 applications, first post draft, 6 practice sessions.

- [ ] **Step 2: Check Notion MCP**

If Notion MCP not connected yet, tell the user: Claude Code settings, add Notion connector, share the daily-todo database with the integration. Markdown fallback active until then.

- [ ] **Step 3: Run first /daily**

Full ritual including first practice session (rotation start: AI system design). Log entry written.

- [ ] **Step 4: Verify engine on**

Checklist with user: weekly file exists, tasks delivered (Notion or markdown), practice log has first scored entry, user knows tomorrow = just type `/daily`.
