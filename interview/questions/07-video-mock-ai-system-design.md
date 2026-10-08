# Video Mock: AI System Design Interview Questions

Source: user-pasted transcript from an AI system design mock interview.

The mock designs a food-ordering voice chatbot for peak workloads. It includes
memory, ordering, bill splitting, recommendations, low-latency voice responses,
and model routing. The interviewer emphasized reasoning structure over finding a
single "correct" answer.

## AI System Design

### Requirements and scope

- What is the application's main functional requirement: recommendations, or
  executing an order the user explicitly requested?
- Which user actions must be synchronous, and which can complete asynchronously?
- What are the non-functional requirements for latency, throughput, peak load,
  availability, cost, correctness, and privacy?
- What happens when traffic spikes after a major event?
- What is the happy path and what is the failure path?

### Queues and backend architecture

- Which parts of the application need queuing?
- When does a queue protect the user-facing path, and when does it create more
  complexity than value?
- Which slow third-party or payment operations should run asynchronously?
- How do you handle retries, timeouts, idempotency, and partial completion?
- What does the AI layer look like, and which services interact with it?

### Classification and model routing

- How do you determine the complexity of an input?
- Can greetings and other bounded requests avoid an LLM call entirely?
- How do you route simple lookups, tool calls, and open-ended requests?
- How do you choose between a cheap model and a stronger model?
- Can query complexity be predicted without using another LLM?
- How would you train and evaluate a lightweight complexity or intent classifier?

### Caching

- What is the cache being used for?
- Which requests are bounded and repetitive enough to cache?
- Why should greetings use a static response rather than a cache?
- Why should unbounded questions, such as arbitrary weather questions, not use
  a semantic response cache by default?
- What are the cache key, invalidation, tenant boundary, freshness guarantee,
  and fallback behavior?
- Compare prompt-prefix caching, retrieval-context caching, and semantic
  response caching.

### Voice, latency, and throughput

- How do you make a voice or text response feel immediate?
- What is the difference between streaming and batching?
- When would you use WebSockets or WebRTC?
- How would voice-activity detection affect the design?
- What is the time-to-first-token budget versus the final-action budget?
- How do you improve throughput without damaging tail latency?
- How do you protect downstream APIs when concurrency rises sharply?

### Recommendations and actions

- How would you design recommendations for add-ons to the cart?
- Why should recommendation generation be separate from order execution?
- When would you use collaborative filtering, item associations, or a ranking
  model instead of an LLM?
- How does the system confirm an irreversible order or payment action?

## Python and Coding

- Print the numbers 1 to 10 without explicitly writing a loop. What approaches
  come to mind?
- What are the time and space complexities of your solution?
- What does "efficient" mean when the required output itself has size N?
- How would you explain a simple correct solution before optimizing it?

The interviewer feedback was to start with the simplest correct solution, then
state the optimization and its trade-off. Do not hide work performed inside a
library call when explaining complexity.

## Theory and Generative AI

- What is the difference between an RNN and a Transformer? Why can Transformers
  perform better?
- Rank these tasks for a general LLM: writing code from scratch, finding bugs in
  existing code, and translating code between languages. What assumptions make
  your ranking change?
- If a company fine-tunes a model specifically for bug fixing, does that change
  your answer?
- You have a 100-page book and want highly accurate question answering. Should
  you fine-tune an existing model, put relevant context into a strong model, or
  train a model from scratch?
- When is retrieval or context preferable to fine-tuning?
- What makes a dataset suitable for fine-tuning rather than retrieval?

## Interviewer Feedback to Apply

- Follow a visible flow: requirements -> non-functional requirements -> user
  flow -> data flow -> architecture -> security and operations.
- Do not jump into services or frameworks before clarifying the core action.
- Explicitly account for seasonality and peak traffic when the prompt gives it.
- Explain why a queue is needed and what new failure modes it introduces.
- Start with the simplest valid design, then add complexity only when a stated
  requirement demands it.
- Give specific reasoning and assumptions instead of broad theory statements.
- Most open-ended questions do not have one correct answer; the quality of the
  reasoning process is the answer.

## Practice Rubric

Score each answer from 1 to 5:

- 1: jumps to technology, misses the requirement, or gives an unsupported claim
- 2: names a plausible design but misses constraints or failure modes
- 3: covers the main flow and one trade-off
- 4: covers requirements, architecture, failures, metrics, and trade-offs
- 5: stays structured under follow-ups and adapts the design when assumptions
  change
