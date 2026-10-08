# Video Mock: AI Engineer Interview Questions (Medium)

Source: user-pasted transcript from a medium-difficulty AI Engineer mock
interview.

This interview tests backend fundamentals, project explanation, LLM and SLM
concepts, AI quality measurement, Python complexity, RAG retrieval choices,
computer vision, and multimodal system design.

## Background and Backend Fundamentals

### Q: Introduce yourself.

Give a concise role-aligned answer: current engineering identity, production AI
experience, strongest technical differentiator, and why the role.

### Q: What is the difference between TypeScript and JavaScript? How does Python compare?

TypeScript adds static type checking and compiles to JavaScript. Python usually
optimizes for development speed and readability, while TypeScript/JavaScript can
be strong for event-driven and web workloads. Python may be slower for
CPU-bound work, but its AI/ML ecosystem and integration with model tooling are
major advantages. Always qualify the answer by workload rather than claiming one
language is universally better.

### Q: What is the difference between WebSockets and REST responses?

REST is request/response over HTTP; the client usually makes a new request for a
new result. WebSockets maintain a long-lived, bidirectional connection, which is
useful for streaming tokens, live progress, and interactive voice or chat. The
trade-offs include connection management, load balancing, authentication,
backpressure, and reconnect behavior.

### Q: Which Gemini model did you use?

Be specific about the model, task, version, latency/cost trade-off, and fallback.
Naming a model without explaining why it was selected is incomplete.

### Q: What is an LLM, and how does it differ from an SLM?

An LLM is a large pretrained model with broad capability and substantial
compute/memory requirements. An SLM is smaller and may be specialized, distilled,
or optimized for lower latency and cost. The trade-off is not simply knowledge:
compare quality, reasoning, context length, privacy, hardware, and operational
cost for the target task.

## LLM Quality Dashboard

### Q: Design a monthly dashboard for Gemini API call count, cost, and response quality.

Start with the observability contract rather than jumping into RAG optimization.
Capture request/model/version identifiers, timestamps, token usage, latency,
status, retries, tool calls, user or task outcome, and cost. Store structured
events, aggregate them by day and month, and support drill-down from a metric to
the original trace with privacy redaction.

### Q: How do you calculate whether a response is good?

Define quality by task. For a RAG answer, measure groundedness, citation or
source correctness, answer relevance, completeness, and abstention quality. For
an agent, add tool-selection correctness, action success, and task completion.
Combine a labelled golden set, deterministic checks, human review, and calibrated
LLM judges. Validate offline results against online signals such as acceptance,
edits, escalation, repeat questions, and task completion. There is no universal
"accuracy" number for all generated responses.

## Python and Complexity

### Q: Find a query string or substring in an array of about one million strings.

Clarify whether the query must match an entire element or may span element
boundaries. For element membership, use a set for repeated exact lookups. For a
substring that may cross boundaries, define the concatenation and separator
rules, join the bounded strings, and search the resulting text. Stream or use a
text-search algorithm if the full material cannot fit in memory.

### Q: What happens if the query is absent?

Return `-1` consistently. Test the empty input, empty query policy, first and
last positions, repeated matches, and absent query.

### Q: If the query crosses spaces or string boundaries, how do you handle it?

Normalize or concatenate according to an explicit contract. Do not manually
construct every substring unless the requirements demand it; joining once and
searching is easier to reason about when the input is bounded.

### Q: What is the complexity?

Use named variables. If there are N strings and average string length M, scanning
all strings and searching each one is approximately O(MN), plus any input
construction cost. `O(M) * O(N)` is normally written as `O(MN)`; it describes the
same multiplication of work. If M is a fixed small bound, the practical growth
with N is close to linear, but state the assumption explicitly.

## RAG and Vector Search

### Q: What vector databases could you use, and how would you shortlist one?

Consider data size and growth, filtering, tenant isolation, metadata support,
index/update behavior, query latency, durability, replication, availability,
operational burden, cost, ecosystem, and migration risk. Possible options
include a managed vector database, a relational database with vector support,
and an embedded/local index. Do not choose from product names alone; tie the
choice to workload and operating constraints.

### Q: What are vector and keyword similarity metrics?

Vector search commonly uses cosine similarity, dot product, or Euclidean
distance. Keyword search may use exact matching, inverted indexes, BM25, or
other term-based ranking. Hybrid retrieval is useful when semantic similarity
and exact identifiers, names, or codes both matter.

### Q: How do you calculate cosine similarity?

For vectors A and B:

```text
cosine_similarity(A, B) = (A dot B) / (||A|| * ||B||)
```

It is the cosine of the angle between the vectors, not the angle itself. It is
undefined when a vector has zero magnitude, so handle zero vectors explicitly.

### Q: Why are Transformers called Transformers, and when were they introduced?

The Transformer architecture was introduced in the 2017 paper “Attention Is All
You Need.” It uses attention-based layers to transform representations while
processing sequences in parallel, avoiding the strict sequential recurrence of
RNNs. Explain the problem it solved: better parallelism and long-range
dependency handling for sequence tasks.

## Multimodal Code-Checking System

### Q: Design an app that reads a meeting recording, extracts shared code, runs it, and reports solved questions.

Clarify consent, supported languages, security, execution isolation, accuracy,
latency, and whether the user can provide a transcript. A reasonable flow is:

1. Store the recording securely and transcribe it.
2. Locate code-related segments using timestamps, transcript cues, or a cheap
   classifier.
3. Extract code from only the relevant clipped segments.
4. Parse and validate the code before execution.
5. Run it in a sandbox with CPU, memory, network, filesystem, and time limits.
6. Generate tests or compare against a controlled test suite.
7. Report confidence, solved-question evidence, failures, and human-review paths.

### Q: Should you send the entire video to the LLM?

Usually no. Whole-video multimodal inference is expensive and unnecessary. Use
transcription and segmentation first, then send only the relevant text or short
clips downstream. This reduces cost, latency, privacy exposure, and irrelevant
context.

### Q: How would you actually run extracted code?

Never execute model-generated or user-provided code directly in the application
process. Use an isolated sandbox or job runner with least privilege, resource
quotas, no unintended network access, timeout enforcement, cleanup, logging,
and a clear result contract. An IDE or execution service can be exposed as a
restricted tool, but the tool boundary must enforce the safety policy.

## Interviewer Feedback

- Push back politely when an interviewer states something technically wrong.
  Confirm the premise, explain the correction, and continue without becoming
  combative.
- Improve system design by focusing on observability, quality measurement,
  vector-database decision criteria, and model cost before optimizing RAG.
- Tighten complexity analysis with explicit variables and assumptions.
- Go deeper on DSA and backend fundamentals.
- Tailor resume summaries to the job description rather than keeping one static
  summary.
- Keep projects whose API credits are exhausted if the product is otherwise
  useful; handle quota failures cleanly with a user-facing fallback.

## Practice Rubric

Score each answer from 1 to 5:

- 1: gives a tool or definition without matching it to the problem
- 2: has the right direction but misses assumptions or operational concerns
- 3: gives a reasonable design and one relevant trade-off
- 4: connects requirements, implementation, metrics, and failure handling
- 5: catches incorrect premises, simplifies the design, and defends alternatives
