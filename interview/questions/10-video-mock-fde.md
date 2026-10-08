# Video Mock: Forward Deployed Engineer Interview Questions

Source: user-pasted transcript from an FDE interview mock.

This interview combines project depth, customer discovery, live coding, AI
fundamentals, and system design. Its central FDE lesson is to understand the
customer's outcome and constraints before proposing technology.

## Background and Motivation

### Q: Walk me through your projects at Castle and Games 24/7. What issues did you face and how did you overcome them?

Cover the business problem, your personal ownership, architecture, difficult
trade-offs, outcome, and what changed after launch. Connect data engineering,
backend services, migrations, notification/offers systems, experimentation, and
financial APIs to production results rather than listing technologies.

### Q: Your resume shows data and backend work but not AI. Why is AI a good fit now?

Explain the bridge from existing strengths to AI: production software, data,
experimentation, APIs, and customer outcomes are foundations for AI systems.
Then explain why AI is the next problem space you want to work in without
claiming that deterministic engineering is no longer valuable.

## Round 1: Client Scoping

### Q: An agriculture client wants an AI module that hears a bug sound and warns which parts of thousands of acres are affected. What do you do?

Start with discovery, not a model:

- What decision must the alert support?
- Who receives it and how quickly?
- What does “affected” mean operationally?
- What is the baseline today and what is the cost of a false alert or missed alert?
- Where can sensors be installed and what connectivity exists?
- What data already exists, and who can label it?
- Does the client require cloud, private cloud, or on-premises deployment?
- What are the timeframe, budget, privacy, and support constraints?

Then propose a phased plan:

1. Feasibility and data collection in representative areas.
2. A baseline audio classifier with measured precision/recall and alert latency.
3. Field validation using an independent signal, such as infrared imagery or
   human inspection.
4. A risk dashboard and early-warning workflow.
5. Deployment, monitoring, retraining, and ownership handoff.

Be explicit about the technical gap. A strong FDE answer can say: “My depth is
in production AI systems rather than audio modelling. I would not pretend to
choose the final architecture before analysing the signal, labels, noise, and
deployment constraints.”

### FDE follow-ups

- What audio processing and features would you investigate?
- What would run on an edge device versus in the cloud?
- How would you handle weak labels, background noise, and changing field conditions?
- What would you show the client in the first two weeks?
- What would make you stop the project before training a larger model?

The interviewer feedback was to raise cloud versus on-premises, privacy,
timeframe, deployment location, and operating ownership proactively.

## Round 2: Live Coding

### Q: Choose a medium Python problem and solve it with edge cases.

A binary search over a library sorted by book number is a reasonable choice.
State the contract before coding: ascending or descending order, duplicate
behavior, missing target, empty input, and return value.

### Q: What is the precondition for binary search?

The sequence must be sorted, and the comparison logic must know whether it is
ascending or descending. The search is not correct if the code assumes ascending
order while the input can be descending.

### Q: Do duplicates matter?

It depends on the contract. If any matching index is acceptable, duplicates are
fine. If the caller needs the first or last occurrence, the algorithm needs a
modified boundary search.

### Q: Can you change the earlier lines of code?

Treat this as a correctness and reasoning constraint. Re-check the invariant,
run the provided examples mentally, and do not declare the code correct until
you have tested ascending, descending, duplicate, missing, and boundary cases.

### Q: What is the complexity?

Binary search is O(log N) time and O(1) auxiliary space for an array with random
access. If sorting is required first, include the O(N log N) sorting cost. Name
the precondition and whether the input is already sorted.

## Round 3: AI Concepts

### Q: What did the generative-AI revolution solve that was not solved before?

Avoid an overly broad answer. Generative models made general-purpose language
and multimodal interaction much more capable and accessible through pretrained
models. They can translate natural-language intent into drafts, extraction,
code, and tool decisions. They did not eliminate classical ML, software
engineering, or the need for reliable systems; the production problem shifted
to grounding, evaluation, latency, cost, safety, and integration.

### Q: Could you build Cursor using RNNs?

RNNs can support sequence tasks, but an IDE assistant needs long-context code
understanding, low-latency completion, retrieval, tool integration, and strong
software harnesses. Transformers are a better foundation for modern code
completion, but the product is more than the model: it includes context
selection, caching, ranking, editing, permissions, and evaluation.

### Q: When did Transformers become prominent?

The 2017 paper “Attention Is All You Need” introduced the Transformer
architecture. Explain the limitation it addressed: recurrent processing made
parallelism and long-range dependencies difficult. Do not imply that RNNs were
useless; they powered many earlier translation and sequence systems.

### Q: How did translation work before Transformers?

Earlier systems used rule-based and statistical machine translation, followed by
neural approaches using encoder-decoder RNNs, LSTMs, and attention. The useful
comparison is the trade-off: recurrent models process sequence steps in order,
while Transformers use attention and parallel computation more effectively.

## Round 4: System Design

### Q: Design a “Mad Bot” that always gives wrong or unrelated answers.

Clarify whether this is a test harness, an adversarial demo, or a production
feature. For a controlled test harness, server-side response substitution or a
deterministic policy is more reliable than asking an LLM to disobey the user.
Keep the behavior behind an explicit environment flag, isolate it from real
users, and log the test condition.

### Q: What happens if the user says, “Ignore your system instructions”?

Treat user input as untrusted data. A robust design keeps the behavior outside
the model where possible, validates the output contract, and makes the intended
test mode explicit. Prompt instructions alone are not a security boundary.

### Q: Is prompt engineering the best way to force unrelated answers?

No. For a deterministic test behavior, a backend policy or response substitution
is more controllable. Fine-tuning is unnecessary unless the behavior must be
learned across many inputs and the evaluation justifies its cost.

## FDE Closing Lessons

- FDE removes much of the product-manager insulation. You must discover the
  problem, scope the proof of concept, assess technical risk, and communicate
  trade-offs directly with the client.
- Ask requirements questions before proposing a model, framework, or cloud.
- Admit when a domain is outside your depth and describe how you would close the
  gap. Bluffing damages customer trust.
- Protect the company's reputation: do not promise a solution you cannot yet
  validate.
- For coding, state invariants and edge cases before implementation.
- For AI concepts, connect theory to product and deployment consequences.
