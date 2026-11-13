# Pick a Portfolio Project

Start from a real domain and real companies, not from a technology you want to use.

Use this workflow:

1. Pick five candidate domains
2. Select one domain
3. Pick companies in that domain
4. Analyze job descriptions and company blog posts
5. Extract problems
6. Create about five project candidates
7. Choose technologies for each candidate

The order matters because technology-first projects often become buzzword demos.

## Pick Five Domains

Start with five candidate domains.

The [use-case analysis](../role/04-use-cases.md#domains-served) shows these domains most often:

- finance: 3,877 mentions
- healthcare: 2,380 mentions
- legal / regulatory: 1,798 mentions
- education: 1,349 mentions
- cybersecurity: 1,317 mentions

These aren't the only good domains. They're a practical starting set based on the data in this repo.

Other useful domains:

- developer tools
- customer support
- manufacturing and industrial
- retail and e-commerce
- logistics

## Select One Domain

Choose one domain from the five.

Use three checks:

- companies are hiring for AI engineering work in this domain
- companies publish job descriptions, blogs, docs, or demos you can study
- you can build a realistic project with public or synthetic data

If you're unsure which domain to pick, pick a company first, and use that company's domain as your initial domain.

## Pick Companies

Choose 5-10 companies in the domain.

Collect:

- current job descriptions
- company blog posts
- product docs when they explain workflows
- public demos or support docs
- public datasets or sample documents

Save the links because they explain why the project exists later.

## Analyze Job Descriptions and Blog Posts

Analyze two source types:

1. Job descriptions: what companies want engineers to do
2. Company blog posts: what problems teams actually work on

Use job descriptions to find:

- responsibilities
- required skills
- repeated tools
- deployment or operations expectations

Use blog posts to find the problems companies solve and how they solve them.

Useful clues:

- workflows they describe
- constraints they mention
- failure modes they hit
- systems they built
- trade-offs they made

Then read the technical blogs and product docs for workflows.

## Extract Problems

Turn notes into problem statements.

Don't write project ideas yet.

Write problems like this:

```text
Support teams need to answer refund questions from policy documents without inventing policy.
Analysts need to compare earnings-call transcripts and surface risk changes over time.
Developers need to turn messy bug reports into reproducible GitHub issues.
```

Each problem should name:

- user
- input
- output

If you can't name the input or success check, the problem is still too vague.

## Create Project Candidates

Create about five possible projects from the problem list.

Use this format:

```text
Project: Refund policy support assistant
User: support agent
Input: customer question plus refund policy pages
Output: grounded answer with cited policy section and escalation flag
Why it fits: RAG, refusal behavior, evals, support-domain context
```

Stay in one domain, but vary the project type.

For customer support:

- grounded FAQ assistant
- ticket triage tool
- conversation summarizer
- policy-compliance reviewer
- support analytics agent

These are options, not commitments.

## Choose Technologies

Choose technology after the problem is clear:

- RAG: when the answer must come from a knowledge source
- agents: when the system needs tools, state, or multi-step work
- structured output: when the user needs validated fields, labels, summaries, or actions
- deterministic code: when the task doesn't need an LLM

Every candidate should include some hiring signals:

- tests
- eval harness
- cost or latency notes
- logging or monitoring
- README with trade-offs
- demo, deployment, video, or exact run commands

Choose the project with the best mix of:

- role relevance
- realistic data
- clear evaluation
- finishable scope
- engineering depth

Next, turn the selected project into a repo plan and first-version scope.
