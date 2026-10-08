# Coding and LeetCode for Senior AI Engineering Interviews

Senior AI engineering coding rounds test more than algorithm recall. You may need to clarify an evolving specification, write maintainable Python, reason about data and concurrency, implement ML primitives, debug unfamiliar code, or use an AI assistant without surrendering judgment.

This module provides a prioritized 59-problem LeetCode set plus practical exercises. Use it with the repository's [coding question research](../questions/02-coding.md) and [hiring guide](../03-get-hired.md). Confirm each target company's language, editor, internet, library, and AI-tool policy before practicing.

## What Coding Rounds Measure

Across formats, interviewers look for:

- Requirement clarification and sensible assumptions
- A correct baseline before optimization
- Data-structure and interface choices tied to constraints
- Readable code with useful names and small testable units
- Edge-case handling and deliberate tests
- Time, space, I/O, and concurrency reasoning
- Ability to accept hints, revise a design, and explain trade-offs
- Production judgment about validation, failures, retries, security, and observability

For senior roles, code quality and reasoning can matter as much as reaching the optimal algorithm. Do not use seniority as an excuse for weak implementation fundamentals.

## Default Round-Prep Priority

Until recruiter or company evidence confirms the loop, allocate coding preparation in this order:

1. Practical Python, API, and data work
2. SQL
3. Progressive implementation
4. ML implementation
5. DSA

This is a market-weighted preparation default, not an estimate of interview-round frequency. The repository's [job-market trends](../../job-market/trends.md) show SQL rising from 9.8% to 34.8%, the fastest-rising listed skill in that analysis, while the integrator stack rose from 73.6% to 77.9% and the trainer stack fell from 36.1% to 27.2%. The [trends appendix](../../job-market/trends-appendix.md) records the same monthly endpoints. The [responsibility analysis](../../role/03-responsibilities.md) also places build and implement work at 98.1%, API and service integration at 62.4%, and evaluation and quality at 68.5%. Responsibility rates use all 4,894 published postings; SQL and integrator/trainer trends use only the ai-first subset.

Elevate SQL accordingly: practice joins, aggregation, windows, deduplication, grain, null behavior, and query-plan reasoning from the start rather than treating SQL as a late supplement. Treat DSA as confirmed-loop conditional. If the company confirms algorithm rounds, move DSA to the priority required by that gate; if the loop remains unknown, maintain a compact transferable floor without assuming algorithms dominate every senior AI engineering process.

## Round Types

### DSA

When recruiter or company evidence confirms a DSA round, expect one or two algorithmic problems in 30-60 minutes. The interviewer evaluates pattern recognition, correctness, complexity, communication, and testing. Common patterns include hash maps, two pointers, sliding windows, trees, graphs, heaps, intervals, and essential dynamic programming.

Prepare to:

- Derive the solution rather than naming a memorized pattern
- State invariants for windows, searches, traversals, and data structures
- Compare a simple solution with an optimized one
- Write executable code and test it without a full IDE

### Progressive implementation

Expect one system that gains requirements in levels over 45-90 minutes. Examples include a key-value store, crawler, scheduler, credits ledger, or in-memory database. The initial design should remain understandable as TTL, persistence, concurrency, or new query behavior arrives.

Prepare to:

- Ask which behaviors and guarantees matter now
- Keep domain logic separate from storage, time, network, and serialization
- Avoid speculative abstractions while preserving extension points at likely change boundaries
- Add tests at each level and refactor when evidence justifies it

### Practical Python, API, and data work

Expect JSON transformation, API integration, pagination, retries, data validation, streaming, file processing, or a small service endpoint. The challenge is often incomplete input and operational failure, not algorithmic novelty.

Prepare to:

- Handle malformed data, missing fields, duplicates, and partial results
- Set explicit deadlines and safe retry policies
- Use iterators or streaming when the input may not fit in memory
- Make dependencies injectable and side effects testable

### ML implementation

Expect NumPy or PyTorch code for metrics, optimization, clustering, attention, sampling, batching, or vector operations. Interviewers may prohibit high-level helpers.

Prepare to:

- Track tensor shapes and dtypes
- Handle numerical stability and degenerate cases
- State computational and memory complexity
- Test against a tiny hand-computed example

### SQL

Expect joins, aggregations, window functions, ranking, funnels, retention, deduplication, or debugging a slow or incorrect query.

Prepare to:

- Clarify grain, keys, null behavior, time zone, and duplicate events
- Build the query in stages and validate intermediate row counts
- Explain indexes and query plans without guessing
- Distinguish event time from processing time

### Debugging and refactoring

Expect unfamiliar code with failing tests, race conditions, poor structure, or performance problems. The goal is to localize the defect and improve the code without an unnecessary rewrite.

Prepare to:

- Reproduce before editing
- Form and test hypotheses using the smallest useful observation
- Preserve behavior with characterization tests
- Separate correctness fixes from structural changes
- Explain blast radius, rollback, and missing coverage

### AI-assisted coding

Some rounds allow or require an AI assistant. The evaluation shifts toward task decomposition, context selection, verification, and ownership. Tool access does not lower the correctness bar.

Prepare to:

- State your plan before prompting
- Give the assistant narrow, testable tasks and relevant constraints
- Inspect every generated change and ask for alternatives when trade-offs matter
- Run tests, create adversarial cases, and verify APIs rather than trusting plausible output
- Narrate what you accepted, rejected, and corrected
- Stop using the tool when manual reasoning is faster or safer

## Prioritized LeetCode Set

The set contains 46 must-do problems and 13 optional or stretch problems. The 46 must-do problems are a long-term curated bank and priority map, not an eight-week quota. It favors patterns that transfer to AI product, data, and platform work. Solve fewer problems well rather than racing through all 59 once.

### Most relevant from the FAANG frequency sheet

I filtered [`learning-paths/Top Leetcode questions of All Time - most important (1).xlsx`](../../learning-paths/Top%20Leetcode%20questions%20of%20All%20Time%20-%20most%20important%20%281%29.xlsx) against this module's AI Engineering and FDE priorities. Sheet frequency is the sum of listed company ask counts in that workbook. It is a FAANG popularity signal, not an AI-interview occurrence rate. Prefer problems that also transfer to caches, scheduling, streaming, rate limiting, dependency graphs, and top-k telemetry.

Start with these ten:

| Problem | Pattern | Sheet frequency | Why it matters for AI or FDE |
|---|---|---:|---|
| 146. LRU Cache | Design / hash map + linked list | 207 | Cache eviction, API contracts, stateful services |
| 200. Number of Islands | Graph BFS or DFS | 229 | Reachability, clustering, orchestration neighborhoods |
| 56. Merge Intervals | Intervals | 214 | Schedules, rate-limit windows, temporal joins |
| 1. Two Sum | Hash map | 225 | Indexing and complement lookup baseline |
| 3. Longest Substring Without Repeating Characters | Sliding window | 149 | Streaming windows and bounded context |
| 347. Top K Frequent Elements | Heap / counting | 125 | Telemetry, eval buckets, ranking |
| 20. Valid Parentheses | Stack | 146 | Parsing, nesting, structured output checks |
| 215. Kth Largest Element in an Array | Heap / selection | 112 | Online top-k and bounded-memory selection |
| 207. Course Schedule | Graph / topological sort | 67 | Dependency graphs and pipeline ordering |
| 359. Logger Rate Limiter | Design | 62 | Per-key rate limits and production gateways |

Solve the next tier after those ten are clean under time:

- 253. Meeting Rooms II - interval resource counting; premium on LeetCode, but high transfer to capacity planning
- 49. Group Anagrams - hashing and grouping
- 33. Search in Rotated Sorted Array - binary search boundary discipline
- 380. Insert Delete GetRandom O(1) - design under multiple operation constraints
- 210. Course Schedule II - reconstruct a valid dependency order
- 76. Minimum Window Substring - hard sliding window; useful once medium windows are solid
- 295. Find Median from Data Stream - online summary with two heaps
- 98. Validate Binary Search Tree - invariant checking on trees
- 208. Implement Trie (Prefix Tree) - prefix indexes and routing-like APIs
- 322. Coin Change - essential unbounded DP

If you only have one coding session today, do 146. LRU Cache, then either 56. Merge Intervals or 347. Top K Frequent Elements.

For each problem, record:

- First-attempt date, result, time, and hints used
- Pattern and invariant
- Time and space complexity
- Missed edge cases
- Next repetition date

### Must-do: arrays and hash maps

- 1. Two Sum
- 217. Contains Duplicate
- 242. Valid Anagram
- 49. Group Anagrams
- 347. Top K Frequent Elements

Senior transfer: indexing, deduplication, grouping, counting, and top-k aggregation appear in ingestion, evaluation, telemetry, and caching systems.

### Must-do: two pointers

- 125. Valid Palindrome
- 15. 3Sum
- 11. Container With Most Water

Senior transfer: sorted scans, deduplication, and proving why pointer movement cannot discard an optimal answer.

### Must-do: sliding window

- 3. Longest Substring Without Repeating Characters
- 424. Longest Repeating Character Replacement
- 76. Minimum Window Substring

Senior transfer: streaming windows, bounded context, session analysis, and maintaining an invariant under incremental updates.

### Must-do: stacks and queues

- 20. Valid Parentheses
- 155. Min Stack
- 739. Daily Temperatures

Senior transfer: parsing, monotonic structures, undo state, iterative processing, and amortized analysis.

### Must-do: binary search

- 704. Binary Search
- 33. Search in Rotated Sorted Array
- 875. Koko Eating Bananas

Senior transfer: boundary correctness and binary search over an answer space for capacity or threshold decisions.

### Must-do: intervals

- 56. Merge Intervals
- 57. Insert Interval
- 435. Non-overlapping Intervals

Senior transfer: reservations, schedules, rate-limit windows, temporal joins, and greedy reasoning.

### Must-do: linked lists

- 206. Reverse Linked List
- 21. Merge Two Sorted Lists
- 141. Linked List Cycle
- 19. Remove Nth Node From End of List

Senior transfer: pointer discipline and the mechanics behind LRU caches and intrusive queues.

### Must-do: trees

- 104. Maximum Depth of Binary Tree
- 226. Invert Binary Tree
- 102. Binary Tree Level Order Traversal
- 98. Validate Binary Search Tree
- 230. Kth Smallest Element in a BST

Senior transfer: recursion, iterative traversal, hierarchical data, serialization choices, and maintaining global invariants.

### Must-do: graphs

- 200. Number of Islands
- 133. Clone Graph
- 207. Course Schedule
- 994. Rotting Oranges

Senior transfer: dependency resolution, lineage, orchestration, propagation, reachability, cycle detection, and multi-source breadth-first search.

### Must-do: heaps and streams

- 215. Kth Largest Element in an Array
- 973. K Closest Points to Origin
- 703. Kth Largest Element in a Stream

Senior transfer: online top-k, bounded-memory selection, scheduling, and why a heap may beat full sorting.

### Must-do: tries

- 208. Implement Trie (Prefix Tree)

Senior transfer: prefix indexes, autocomplete, routing, memory-throughput trade-offs, and API design for mutable indexes.

### Must-do: backtracking

- 78. Subsets
- 39. Combination Sum

Senior transfer: explicit search state, pruning, rollback, and bounding combinatorial work.

### Must-do: essential dynamic programming

- 70. Climbing Stairs
- 198. House Robber
- 322. Coin Change

Senior transfer: defining state, transition, base cases, and reducing memory after proving the recurrence.

### Must-do: caches and design

- 146. LRU Cache
- 981. Time Based Key-Value Store

Senior transfer: combining structures to meet an operation contract, timestamp semantics, eviction, and discussing what changes under concurrency or persistence.

### Must-do: data streams

- 295. Find Median from Data Stream

Senior transfer: maintaining online summaries, balancing structures, and stating the limits of exact computation.

### Must-do: concurrency concepts

- 1114. Print in Order

Senior transfer: ordering, synchronization, spurious assumptions about scheduling, and explaining why a solution is safe. The specific puzzle matters less than understanding locks, semaphores, condition variables, events, and failure behavior.

### Optional and stretch

Use these after the diagnostic-selected set is stable or when the target company expects stronger algorithms. They do not belong in the eight-week workload merely because they are listed.

- 128. Longest Consecutive Sequence - arrays and hash maps
- 42. Trapping Rain Water - two pointers or monotonic stack
- 239. Sliding Window Maximum - deque and streaming windows
- 23. Merge k Sorted Lists - heaps and linked lists
- 124. Binary Tree Maximum Path Sum - tree dynamic programming
- 297. Serialize and Deserialize Binary Tree - trees and interface design
- 127. Word Ladder - implicit graphs and breadth-first search
- 212. Word Search II - trie plus backtracking
- 211. Design Add and Search Words Data Structure - trie plus search
- 51. N-Queens - constrained backtracking
- 139. Word Break - sequence dynamic programming
- 300. Longest Increasing Subsequence - dynamic programming and binary-search optimization
- 1115. Print FooBar Alternately - concurrency coordination

## Pattern Expectations

You should be able to recognize and derive:

- Hash map - expected constant-time lookup, grouping, deduplication, or complement search
- Two pointers - a monotonic choice on sorted or symmetric data
- Sliding window - a contiguous region whose invariant can be restored incrementally
- Stack or deque - nested structure, next greater element, or efficient window endpoints
- Binary search - a sorted space or monotonic feasibility predicate
- Heap - repeated min or max access, top-k, or merging ordered streams
- Graph traversal - reachability, dependencies, shortest unweighted paths, or propagation
- Backtracking - enumerate choices with reversible state and pruning
- Dynamic programming - overlapping subproblems with a precise state and recurrence
- Composite design - two or more structures combined to satisfy an operation contract

Do not force a pattern from superficial wording. State why the invariant holds.

## Progressive Implementation Exercises

Run each exercise as a 60-90 minute interview. Implement levels in order. Stop after each level to test, explain complexity, and name the next likely design pressure.

### Key-value store with TTL and persistence

Level 1:

- Implement `set`, `get`, and `delete`.
- Define behavior for missing keys and overwrites.

Level 2:

- Add optional TTL using an injected clock.
- Decide whether expiration is lazy, eager, or both.

Level 3:

- Add snapshots or an append-only log and recovery after restart.
- Define write ordering and behavior after a partial record.

Level 4:

- Make concurrent operations safe and add compare-and-set.
- Discuss lock granularity, durability, compaction, and multi-process limits.

Evaluation focus: clear semantics, testable time, expiry correctness, recovery, and acknowledgment that an in-process design is not automatically distributed.

### Crawler with rate limiting and concurrency

Level 1:

- Fetch one page, parse links, and crawl to a depth or page limit.
- Normalize URLs and avoid duplicates.

Level 2:

- Add bounded concurrency, per-request timeouts, and partial-failure reporting.
- Avoid holding all response bodies in memory.

Level 3:

- Add per-host rate limits, retry policy, robots behavior, and cancellation.
- Prevent one slow host from blocking all work.

Level 4:

- Add durable frontier state, resumability, and distributed ownership.
- Discuss duplicate fetches, politeness, content hashing, and observability.

Evaluation focus: bounded resource use, queue discipline, URL identity, host isolation, and safe retries.

### Model gateway and rate limiter

Level 1:

- Expose one generate operation over two fake providers.
- Normalize request and response schemas.

Level 2:

- Add token and request quotas by tenant with a token-bucket or leaky-bucket policy.
- Return useful rejection and retry information.

Level 3:

- Add routing, deadlines, retries, circuit breaking, streaming, and idempotency.
- Separate provider errors from application errors.

Level 4:

- Add model policy, audit logs, cost attribution, canary rollout, and overload degradation.
- Discuss global versus local rate limits and consistency requirements.

Evaluation focus: contract design, tenant isolation, retry amplification, stream failure, and measurable routing policy.

### Evaluation runner

Level 1:

- Load cases, call a candidate function, and compute deterministic metrics.
- Store case-level results, not only an average.

Level 2:

- Add concurrency, timeouts, retries, checkpointing, and resumability.
- Preserve stable case identity and avoid duplicate charges.

Level 3:

- Add model-based graders, grader versioning, repeated samples, and confidence intervals.
- Track prompt, model, tool, dataset, and code versions.

Level 4:

- Compare two candidates, slice regressions, and enforce a release policy.
- Emit a report with quality, safety, latency, and cost.

Evaluation focus: reproducibility, failure accounting, traceability, and statistical humility.

### Document ingestion pipeline

Level 1:

- Load documents, parse text, chunk content, and emit stable chunk records.
- Preserve document and source metadata.

Level 2:

- Add deduplication, batch embedding, retries, and partial-failure recovery.
- Respect provider batch and rate limits.

Level 3:

- Add updates, deletion, versioning, access-control metadata, and re-embedding.
- Prevent stale chunks from being returned during migration.

Level 4:

- Add queues, backpressure, idempotent writes, reconciliation, and operational metrics.
- Estimate throughput, storage, and re-index cost.

Evaluation focus: stable identifiers, lineage, deletion correctness, batching, and recoverability.

## ML Coding Drills

Practice first with NumPy unless the round specifies PyTorch. Avoid high-level implementations of the target algorithm.

### Linear regression

- Implement prediction, mean squared error, gradients, and gradient descent.
- Add L2 regularization without regularizing the intercept.
- Test against a tiny dataset with a known line.
- Explain closed-form versus iterative solutions and numerical conditioning.

### Logistic regression

- Implement stable sigmoid, binary cross-entropy, gradients, mini-batch SGD, and early stopping.
- Handle labels, shapes, and class imbalance explicitly.
- Explain why clipping symptoms is weaker than using stable log-domain expressions.

### Metrics

- Implement confusion matrix, precision, recall, F1, ROC points, PR points, and top-k accuracy.
- Define zero-denominator behavior.
- Select a threshold from an explicit false-positive and false-negative cost.

### K-means

- Implement initialization, assignment, centroid update, and convergence.
- Handle empty clusters, duplicate points, seeds, and maximum iterations.
- State time and memory complexity in samples, clusters, dimensions, and iterations.

### Attention

- Implement scaled dot-product attention with batch, head, sequence, and feature dimensions.
- Add padding and causal masks before stable softmax.
- Test that masked positions receive zero probability and that each row sums to one.

### Sampling

- Implement greedy, temperature, top-k, and top-p sampling.
- Handle temperature near zero, invalid distributions, and seeded reproducibility.
- Explain how filtering order changes the candidate distribution.

### Batching and masking

- Pad variable-length sequences, return lengths and masks, and compute a masked mean.
- Build a causal mask with the expected broadcast shape.
- Explain wasted padding, bucketing, packed sequences, and dynamic batching.

### Vector similarity

- Implement dot product, cosine similarity, pairwise similarity, and top-k retrieval.
- Handle zero vectors and compare normalized dot product with cosine similarity.
- Process a corpus in blocks to avoid materializing an unbounded similarity matrix.

For deeper system implications, connect these drills to [`01-common-core.md`](01-common-core.md) and [`03-ai-ml-system-design.md`](03-ai-ml-system-design.md).

## SQL Drills

Use a schema with `users`, `tenants`, `requests`, `model_calls`, `documents`, `chunks`, `evaluations`, and `experiments`. Generate enough duplicate, missing, late, and failed records to expose incorrect assumptions.

Practice:

- Daily request count, success rate, token use, and cost by tenant
- p50 and p95 latency by model and day using the target database's percentile support
- Top three failure reasons per tenant using window functions
- Seven-day rolling success rate with a clearly defined row or time window
- First successful request per user
- Users active in consecutive weeks and a cohort-retention query
- Funnel from document upload to ingestion completion to first successful answer
- Deduplication that retains the latest event by stable business key
- Experiment comparison with assignment, exposure, outcome, and guardrail metrics
- Documents whose current version has missing or stale chunks
- A recursive dependency traversal when the target database supports recursive CTEs
- Query-plan diagnosis and an index proposal for one slow query

For every solution, state:

- Input grain and output grain
- Join cardinality assumptions
- Null, duplicate, and time-zone behavior
- Why the window frame is correct
- Expected indexes and how you would inspect the plan

## Python and Concurrency Drills

Complete these without relying on framework magic:

- Write an iterator that streams newline-delimited JSON, validates records, and reports line-level errors.
- Implement a context manager that measures duration and guarantees cleanup after exceptions.
- Build a retry helper with a deadline, exponential backoff, jitter, retryable-error predicate, and injectable sleep.
- Implement a producer-consumer pipeline with a bounded queue and graceful shutdown.
- Build an async fan-out with a semaphore, per-task timeout, cancellation, and stable result ordering.
- Protect a shared token bucket under threads and explain what changes across processes or replicas.
- Diagnose an event-loop stall caused by CPU work or blocking I/O.
- Compare threads, processes, and async tasks on one CPU-bound and one I/O-bound workload.
- Implement an LRU cache, then discuss TTL, thread safety, stampede prevention, and distributed invalidation.
- Refactor nested data-processing code into pure transformations and isolated side effects.

Concurrency correctness questions to answer aloud:

- What state is shared?
- Which operations must be atomic?
- What ordering is required?
- Can work be duplicated, lost, starved, or deadlocked?
- How are cancellation and exceptions propagated?
- Is concurrency bounded?
- What happens at process or machine boundaries?

## Repeatable Solve and Review Rubric

Use this rubric for DSA, practical coding, ML implementation, and SQL. Score each category from 0 to 2.

### Clarify

- 0 - Starts coding with important ambiguity unresolved.
- 1 - Restates the task but misses a consequential constraint.
- 2 - Clarifies inputs, outputs, scale, edge cases, mutation, errors, and relevant tool policy.

### Derive

- 0 - Guesses or names a pattern without justification.
- 1 - Finds a workable approach but cannot establish correctness.
- 2 - Builds from a baseline, states the invariant, and justifies the selected structure.

### Implement

- 0 - Code is incomplete or structurally unsound.
- 1 - Core path works but naming, decomposition, or edge handling is weak.
- 2 - Code is executable, readable, appropriately scoped, and easy to test or extend.

### Verify

- 0 - Provides no meaningful test.
- 1 - Tests a happy path and notices some edges.
- 2 - Dry-runs representative, boundary, empty, duplicate, and failure cases and fixes discovered defects.

### Analyze

- 0 - Complexity or systems claims are wrong.
- 1 - Gives Big O without explaining dominant operations or practical constraints.
- 2 - Correctly states time and space and discusses I/O, allocation, contention, numerical, or operational limits when relevant.

### Communicate and adapt

- 0 - Proceeds silently, resists evidence, or cannot use a hint.
- 1 - Narrates actions but not decisions.
- 2 - Explains trade-offs concisely, incorporates hints, and revises assumptions when evidence changes.

A score of 10-12 is a strong attempt. A score below 2 in implementation or verification requires repetition even when the total is high.

After every attempt:

1. Reproduce the failure or uncertainty.
2. Identify whether the gap was recognition, invariant, implementation, language, testing, or communication.
3. Write the smallest corrected explanation.
4. Reimplement the failed part without copying.
5. Schedule a fresh attempt.

## Complexity Expectations

Be ready to state and defend:

- Time and auxiliary space in terms of named input dimensions
- Average versus worst-case behavior when hash maps or randomized methods matter
- Recursion-stack space
- Amortized cost for dynamic arrays, monotonic stacks, queues, and caches
- Output-sensitive cost when producing many combinations or records
- Database and network I/O, serialization, and memory footprint for practical tasks
- Batch, sequence, feature, head, and vocabulary dimensions for ML code
- Contention, blocking, queue growth, and boundedness for concurrent code

Common targets, not universal rules:

- Hash-map lookup or update - expected `O(1)`
- Sorting - `O(n log n)`
- Heap top-k - often `O(n log k)`
- Tree or graph traversal - `O(V + E)`
- Binary search - `O(log n)` after proving monotonicity
- Pairwise vector similarity - `O(nmd)` for `n` queries, `m` vectors, and dimension `d` unless an index or approximation changes the work

Never claim constant space while using recursion proportional to input depth. Never hide a full sort behind a top-k API. For practical rounds, a theoretically optimal algorithm that buffers unbounded input may be the wrong design.

## Eight-Week Spaced Repetition Plan

Use the detailed overall schedule in [`10-eight-week-study-plan.md`](10-eight-week-study-plan.md). This coding track assumes five focused sessions each week, adjusted to the interview mix.

At the start of the cycle, use timed diagnostic evidence to select 10-14 new must-do problems from this bank. For an unknown loop, this selected set is a transferable DSA floor, not evidence that algorithms should dominate preparation. Choose fewer when the baseline is already strong. Expand or intensify it when recruiter or company evidence confirms algorithm rounds. The selected set must represent every weak or high-priority pattern for the target loop; it does not need to represent every pattern in the bank. Record the selected set, the diagnostic reason for each choice, and any uncovered pattern that fresh timed work must continue to test.

### Repetition intervals

After a first correct solution, repeat it after:

- 2 days
- 7 days
- 21 days
- 42 days

After an incorrect solution or material hint, repeat after:

- 1 day
- 3 days
- 7 days
- 14 days

Do not recite saved code. Start from the prompt, derive the invariant, and implement again. Retire a problem only after two clean timed attempts separated by at least one week.

### Week 1: baseline and core structures

- Run one 45-minute baseline DSA mock.
- Select up to 3 new must-do problems from diagnostic weaknesses in arrays, hash maps, two pointers, or linked lists.
- Run Python drills for iterators, context managers, and retry policy.
- Start the key-value store through TTL.

### Week 2: windows, stacks, search, and SQL

- Select up to 3 new must-do problems from weak or high-priority sliding-window, stack, queue, binary-search, or interval patterns.
- Solve four SQL drills, including a window function and deduplication.
- Repeat all week 1 failures.
- Add persistence and recovery to the key-value store.

### Week 3: trees, graphs, and practical concurrency

- Select up to 3 new must-do tree or graph problems only where the diagnostic or target loop makes those patterns high priority.
- Implement bounded producer-consumer and async fan-out drills.
- Build the crawler through per-host rate limiting.
- Run one 60-minute practical coding mock.

### Week 4: heaps, streams, tries, and mid-point gate

- Select up to 2 new must-do problems from weak or high-priority heap, stream, trie, cache, or concurrency patterns.
- Solve four more SQL drills, including retention and latency percentiles.
- Complete the model gateway through routing and circuit breaking.
- Run the midpoint gate below, freeze or shrink the selected set when evidence is strong, and rebalance weeks 5-8.

### Week 5: backtracking, dynamic programming, and ML basics

- Add 1-2 selected-set problems from backtracking, essential dynamic programming, or caches only when those patterns remain weak or high priority.
- Implement linear regression, logistic regression, metrics, and k-means.
- Repeat weak graph, tree, and sliding-window problems.
- Run one DSA mock and one ML coding mock.

### Week 6: attention, sampling, and pipelines

- Implement attention, sampling, batching, masking, and vector similarity.
- Build the evaluation runner through resumability and versioning.
- Build the ingestion pipeline through updates and deletion.
- Add at most 1 new must-do problem only when a likely target-company pattern remains uncovered. Add optional problems only for a demonstrated weakness or explicit target-company priority after the selected set is current.

### Week 7: mixed simulation

- Run two mixed coding mocks under the target company's tool policy.
- Run one SQL and one debugging or refactoring mock.
- Repeat every problem in the selected set that has not yet had two clean timed attempts separated by at least one week.
- Practice one AI-assisted session and review every generated line.

### Week 8: readiness and maintenance

- Run three representative mocks on separate days.
- Repeat only failed or fragile problems; do not cram new patterns.
- Complete one progressive exercise from a blank file under a 90-minute limit.
- Review error-log themes, Python traps, SQL assumptions, ML numerical stability, and concurrency failure modes.
- Confirm editor, runtime, dependencies, and communication setup.

## Readiness Gate

You are coding-round ready when recent evidence shows:

- [ ] Your diagnostic-selected set contains 10-14 new must-do problems, or fewer when a strong baseline justifies the reduction, and covers every weak or high-priority pattern for the target loop.
- [ ] Every problem in the selected set has two clean timed attempts separated by at least one week, with no selected problem failed on its latest attempt.
- [ ] Fresh timed transfer problems not used for memorized repetition show that you can recognize, derive, implement, test, and analyze the target patterns.
- [ ] Coding or practical implementation satisfies the canonical module 09 evidence gate: the three most recent full mocks use different prompts, every core dimension scores at least 3 in two of the three, no core dimension scores 1 in the most recent two, no unresolved hard fail remains, core scope finishes within time in at least two, and the required focused and full re-tests have passed.
- [ ] You can complete a progressive implementation through at least three levels without a rewrite.
- [ ] You can write joins, aggregates, windows, ranking, and deduplication SQL while stating grain and null behavior.
- [ ] You can implement four ML drills, including attention or logistic regression, with correct shapes and stable math.
- [ ] You can build bounded concurrent Python code with cancellation, timeout, and failure handling.
- [ ] You can debug unfamiliar code by reproducing and testing hypotheses before refactoring.
- [ ] Under the expected AI-tool policy, you remain able to explain and verify every submitted line.

The selected-set size or any other total problem count cannot establish readiness without spaced clean attempts, fresh transfer, and canonical mock evidence. If a target company treats one round as an independent gate, apply module 09's repeated-evidence rules to that format even when aggregate performance is strong. Continue with [`09-mock-interviews-and-scorecards.md`](09-mock-interviews-and-scorecards.md) for formal mock scoring and use [Getting Hired](../03-get-hired.md) to align practice with the actual interview loop.
