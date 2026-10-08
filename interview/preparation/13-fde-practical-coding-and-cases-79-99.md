# FDE interview walkthroughs: questions 79–99

The [complete 1–99 edition](14-fde-complete-question-walkthroughs-01-99.md) adds the remaining role, foundations, RAG, agent, evaluation, deployment, and security questions and includes these detailed chapters.

Step-by-step preparation for practical coding, data engineering, case decomposition, and customer communication.

These walkthroughs expand the questions you supplied. Their delivery structure draws on the saved Hello Interview delivery framework, logging example, and rate-limiter example: understand the problem, clarify requirements, identify responsibilities, derive the contract and state, walk through the implementation, verify scenarios, and discuss extensions. The examples, assumptions, numbers, and customer scripts below are practice material, not claims about your experience or a particular company's interview.

## How to use this file

Read one question at a time. First understand the diagram. Then explain the decisions aloud without looking at the interview answer. For coding questions, reproduce the implementation from a blank file. For cases, draw the flow and defend one trade-off. Return the next day and answer one follow-up without rereading.

> **Explanation:** Recognizing an answer while reading is easier than producing it in an interview. Your practice is complete when you can explain *why* each decision follows from the requirements and adapt when one requirement changes.

Callouts have different jobs:

- **Explanation** translates a concept into plain language.
- **Interview move** gives you words or a useful action during the interview.
- **Correctness** highlights a condition your design depends on.
- **Pitfall** shows where a plausible answer breaks.

For coding and design: requirements → contract/state → flow → implementation → tests → trade-offs. For customer conversations: acknowledge → state facts → explain impact → offer a concrete plan → agree on ownership and next update.

## Delivering the answer: the missing bridge between requirements and code

The supplied Hello Interview delivery framework uses five major stages: requirements, entities and relationships, class design, implementation, and extensibility. Verification is an explicit part of the implementation walkthrough. Treat this as a sequence of outputs the interviewer can inspect, not a list of headings to recite.

```text
Vague prompt
    |
    v
Agreed requirements + explicit exclusions
    |     "What behavior must hold?"
    v
Entities / functions / data contracts + ownership
    |     "Who owns the state and the rule?"
    v
Fields + methods derived from requirements
    |     "What must we remember, and what can callers ask us to do?"
    v
Core implementation: normal path -> failures
    |     "In what order do operations happen?"
    v
Trace initial state -> calls -> changed state -> final result
    |     "Can we show that the rules actually hold?"
    v
Changed requirement -> local modification + new trade-off
          "What changes, and which guarantees survive?"
```

### Requirements: ask questions that change the design

Use four themes: capabilities; rules/completion; invalid operations/errors; and scope. Ask a focused question, listen to its answer, then say what that answer changes. “Is it distributed?” matters because it changes state ownership and coordination. “Are writes safe to repeat?” changes whether a timeout may trigger another call. Questions that do not affect a decision can wait.

> **Interview move:** “That means we can keep state in one process for the first version. I will leave cross-instance coordination out of this implementation and discuss it as an extension.”

Write a numbered contract with unambiguous units and boundaries. Examples: four *total* attempts; an accepted request consumes one token from *both* quotas; returns are counted per *order*, not per return row. State what is out of scope so the interviewer can correct it before you build the wrong thing.

### Entities and relationships: show your filtering process

A noun in the prompt is not automatically a class. A customer identifier is usually a field. A result grouping several facts may be an immutable record. A component with state/rules/lifecycle may deserve a class. A pure transform can remain a function. A real external system is a dependency, not an object you implement in the interview.

> **Explanation:** This stage is about responsibility, not object count. Ask: “If this rule breaks, which component would I inspect?” If the answer is “everywhere,” your ownership boundary needs work.

Draw a few ASCII boxes and arrows. Label owns/uses/creates when relevant. Formal UML is not needed unless the interviewer asks for it. Do not build a factory for one implementation or an inheritance hierarchy merely to display a pattern.

### Class or contract design: derive, then write

For every component, build this chain:

```text
Requirement -> remembered state -> owner -> operation -> invariant
```

The invariant is a rule that must remain true after every operation. Example: a denied request consumes no admission tokens. Show the top-level API first, then supporting types. Describe input validity, return values, errors, and who may mutate the state. Keep time units in names.

### Implementation and verification: make order visible

Ask whether the interviewer wants executable code or pseudocode. Choose the core method that proves your design, not every getter. Start with one normal flow. Then place each failure check where it protects the operation: validate before mutation, claim before external execution, durable write before advancing a cursor.

> **Explanation:** “I handle errors” is a claim. “I do not advance the cursor until this page's required writes are durable” is an inspectable rule. The second lets the interviewer reason about a crash.

Trace one useful example with initial state, inputs, operations, changed state, and final output. Include a boundary, competing request, or recovery case. If you find a logical mistake, fix it and rerun the trace; that demonstrates verification rather than weakening your answer.

### Extensibility: name the modification and its cost

Do not answer “it is extensible because I used interfaces.” Explain which field, method, or boundary changes. If a new algorithm requires joint reservation across two quotas, a single destructive `allow()` call may not be a sufficient interface. If execution becomes asynchronous, sleeping becomes persisted scheduling and cancellation becomes a lifecycle concern.

> **Interview move:** “The first version does not need that feature. If we add it, this is the component that changes, the state we must preserve, and the new failure we need to handle.”

### Pacing and adapting to the round

The source suggests approximately five minutes for requirements, three for entities, ten to fifteen for class design, ten for implementation, and five for extensions when time permits; verification takes a short trace within the implementation discussion. Adapt to the actual slot and interviewer. Leave time to prove one core behavior rather than designing indefinitely.

| Questions | Adapt the framework this way |
|---|---|
| 79–82 | Function/object contracts, local state, error categories, implementation and execution traces |
| 83 | Metric contract, table grain, relational stages, query, row-count verification, plan-driven optimization |
| 84–90 | User/decision contract, component ownership, persisted states, operational flow, validation and rollout gates |
| 91–99 | Facts and authority, stakeholder needs, choices, conversation sequence, pushback and a reviewable resolution |

The customer scenarios do not need manufactured class diagrams. They do need the same depth of cause, consequence, evidence, and ownership. The gap comparison is saved in [the companion review](13-fde-walkthrough-gap-review.md).

## Contents

- [79. Exponential backoff with jitter](#q79)
- [80. Idempotency](#q80)
- [81. Per-user and global rate limiting](#q81)
- [82. Parsing messy CSV and JSON](#q82)
- [83. SQL for high-return-rate customers](#q83)
- [84. Ingestion from fragmented sources](#q84)
- [85. A dashboard the ops team cannot trust](#q85)
- [86. Shipment rerouting with SAP and weather data](#q86)
- [87. Prompting, RAG, fine-tuning, or an agent](#q87)
- [88. Reducing emergency-response times](#q88)
- [89. Fraud detection across acquired systems](#q89)
- [90. Claim summarization at large scale](#q90)
- [91. Communicating a three-week deployment delay](#q91)
- [92. Explaining why RAG cannot promise perfect accuracy](#q92)
- [93. Working without production credentials](#q93)
- [94. Challenging a customer's architecture](#q94)
- [95. Turning customer patterns into product changes](#q95)
- [96. Discussing ROI after a failed AI pilot](#q96)
- [97. Handling demands for immediate autonomy](#q97)
- [98. Scoping the first discovery call](#q98)
- [99. Working with a threatened engineering team](#q99)

<a id="q79"></a>
## 79. Implement exponential backoff with jitter for a flaky API

### 1. Understand the problem

Your application calls a customer API. A temporary failure may disappear on another attempt. But immediate, unlimited retries can worsen the outage and leave your caller waiting indefinitely.

```text
Application                      Customer API
    |----- fetch shipment ----------->|
    |<---- 503 unavailable -----------|
    |
    +-- Is repeating safe?
    +-- Is this failure temporary?
    +-- Are attempts and time left?
    +-- If yes: wait, then try again
```

### 2. Clarify and fix the contract

| Ask | Example agreed requirement |
|---|---|
| Helper or durable background service? | Synchronous Python helper inside one process |
| Is the operation safe to repeat? | A read, or a write protected by provider idempotency |
| Which errors are transient? | Timeouts and contract-approved 429/502/503/504 failures |
| What does the retry cap mean? | Four total attempts: one initial call plus three retries |
| What are the time budgets? | Two seconds per call; ten seconds overall |
| How do we wait? | One-second initial ceiling, doubling up to four seconds, full jitter |

> **Correctness:** A timeout means you did not receive a timely result. It does not prove the server did nothing. A payment might have succeeded before the response was lost. Safe repetition must come from the operation's semantics or the provider's idempotency contract. See [AWS on retry safety](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).

### 3. Separate responsibilities

```text
Caller -> retry helper -> API adapter -> customer API
             |               |
             |               +-- HTTP, authentication, parsing, error mapping
             +-- attempts, time budget, backoff, waiting
```

The operation accepts a timeout and returns a result or raises. The helper does not know shipment URLs or authentication. The adapter translates transient failures into a known exception. Other exceptions propagate immediately. No class hierarchy is needed for this contract.

### 4. Explain the mechanisms

| Mechanism | Problem it solves |
|---|---|
| Retry | Temporary failure |
| Backoff | Repeated calls pressuring a struggling service |
| Jitter | Many clients retrying together |
| Backoff cap | Individual waits growing too large |
| Attempt cap | Too many calls |
| Per-call timeout | One call blocking indefinitely |
| Overall deadline | Calls and waits accumulating beyond the caller's budget |

```text
Failed attempt:          1       2       3       4
Backoff ceiling:        1s      2s      4s      STOP
Possible random wait:  .3s     1.7s     .8s

ceiling = min(max_delay, base_delay * 2 ** (attempt - 1))
delay   = random value between 0 and ceiling
```

> **Explanation:** With full jitter, the *ceiling* grows exponentially. Actual waits can decrease because they are random. Jitter spreads traffic; it does not guarantee a hard request-rate limit. See [AWS on full jitter](https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/).

### 5. Walk through the flow

```text
Check time remaining
        |
Call operation with min(per-call timeout, remaining time)
        |
        +-- success ----------------------------> return
        +-- permanent failure ------------------> raise
        +-- retryable failure
                   |
             Last attempt? -- yes --------------> raise
                   |
                  no
                   |
             Choose jittered delay
                   |
             Fits time budget? -- no -----------> raise deadline error
                   |
                  yes
                   |
                  sleep -> next attempt
```

### 6. Implement

```python
import random
import time


class RetryableError(Exception):
    """The API adapter uses this for transient failures."""


class RetryDeadlineExceeded(TimeoutError):
    """The overall time budget has been exhausted."""


def retry(
    operation,
    *,
    max_attempts=4,
    base_delay=1.0,
    max_delay=4.0,
    attempt_timeout=2.0,
    total_timeout=10.0,
    clock=time.monotonic,
    sleep=time.sleep,
    uniform=random.uniform,
):
    if max_attempts < 1:
        raise ValueError("max_attempts must be at least 1")
    if base_delay <= 0 or max_delay <= 0:
        raise ValueError("backoff delays must be positive")
    if attempt_timeout <= 0 or total_timeout <= 0:
        raise ValueError("timeouts must be positive")

    deadline = clock() + total_timeout
    ceiling = min(base_delay, max_delay)

    for attempt in range(1, max_attempts + 1):
        remaining = deadline - clock()
        if remaining <= 0:
            raise RetryDeadlineExceeded("No time for another attempt")

        try:
            return operation(min(attempt_timeout, remaining))
        except (RetryableError, TimeoutError) as error:
            if attempt == max_attempts:
                raise

            remaining = deadline - clock()
            if remaining <= 0:
                raise RetryDeadlineExceeded("API call used the budget") from error

            delay = uniform(0.0, ceiling)
            if delay >= remaining:
                raise RetryDeadlineExceeded("Backoff exceeds remaining budget") from error

            sleep(delay)
            ceiling = min(max_delay, ceiling * 2)
```

> **Explanation:** `time.monotonic()` measures elapsed time without being affected by wall-clock corrections. If only 0.5 seconds remain, the next operation gets at most a 0.5-second timeout.

> **Correctness:** The operation must enforce its timeout through the HTTP client. This wrapper cannot interrupt arbitrary blocking code. Scheduling, socket timeout semantics, and cancellation behavior can cause overruns; do not promise an exact hard ten-second completion guarantee.

> **Pitfall:** A library-specific timeout exception may not inherit from built-in `TimeoutError`. Translate it in the adapter. Do not catch every exception and retry programming bugs or invalid requests.

### 7. Trace and test

```text
Attempt 1: fails after .2s -> wait .4s
Attempt 2: fails after .2s -> wait 1.3s
Attempt 3: succeeds after .2s
Total: .2 + .4 + .2 + 1.3 + .2 = 2.3s
```

```python
class FakeClock:
    def __init__(self):
        self.now = 0.0
        self.delays = []

    def monotonic(self):
        return self.now

    def sleep(self, seconds):
        self.delays.append(seconds)
        self.now += seconds


fake = FakeClock()
calls = []


def flaky_operation(timeout):
    calls.append(timeout)
    if len(calls) < 3:
        raise RetryableError("Temporary outage")
    return {"shipment_id": "S123"}


result = retry(
    flaky_operation,
    clock=fake.monotonic,
    sleep=fake.sleep,
    uniform=lambda low, high: high / 2,
)
assert result == {"shipment_id": "S123"}
assert len(calls) == 3
assert fake.delays == [0.5, 1.0]
```

Also test immediate success, permanent failure, four failures with only three sleeps, deadline exhaustion, reduced timeout near the deadline, invalid settings, and the backoff cap. State complexity: O(A) helper work for A attempts, O(1) auxiliary state; real elapsed time includes calls and waits.

### 8. Follow-ups and interview answer

- **`Retry-After`?** Respect the server's requested wait if it fits the deadline. Do not jitter below that minimum. The adapter should carry retry metadata if this becomes a requirement.
- **Payment timeout?** Reuse the same logical operation key and payload; without provider support, reconcile the unknown outcome before repeating.
- **Circuit breaker?** It acts across calls and temporarily blocks a failing dependency. Backoff controls retries within one call.
- **Nested retries?** Three layers allowing three attempts each can produce 27 downstream calls. Choose who owns retries.
- **Concurrency?** Helper state is local to each call. The operation and injected dependencies still need suitable concurrency behavior.

> **Say it aloud:** “I first establish whether repeating is safe and classify transient failures. Then I use a bounded retry loop, per-call timeouts, and an overall deadline. After a retryable failure, I choose a random wait within a capped exponential ceiling. I stop on permanent errors, the final attempt, or exhausted time. Time and randomness are injectable so I can test every branch without real waiting.”

**Recall check:** Why does a retry cap alone fail to bound latency? Because an individual API call can still block without a timeout.

### Design derivation: how to arrive at the implementation yourself

#### Translate interviewer answers into choices

**You:** “Can the caller wait during retries?” **Interviewer:** “Yes, this is a synchronous helper.” That authorizes a local loop and sleeping. If the answer were no, returning a durable job ID and scheduling future attempts would be a different design.

**You:** “Do we know whether a timed-out write completed?” **Interviewer:** “This operation is a safe read.” That allows retrying the timeout. If the operation were a non-idempotent write, you would need an outcome-query or provider deduplication contract before using the same loop.

**You:** “Does ten seconds include waits?” **Interviewer:** “Everything.” Now a maximum attempt count is insufficient. Store an absolute deadline and recalculate the remaining budget before every call and wait.

> **Explanation:** Each answer removes a design branch. The interview signal is not the number of questions you ask; it is showing that you use the answers.

#### Derive state and reject unnecessary entities

| Requirement | State or dependency | Why it exists |
|---|---|---|
| At most four calls | `attempt`, `max_attempts` | Decide whether another call is permitted |
| Ten seconds in total | Absolute `deadline`, injected `clock` | Account for actual elapsed calls and waits |
| Doubling capped waits | Current `ceiling`, delay settings | Carry the next waiting bound without unbounded growth |
| A different random wait | Injected `uniform` | Spread traffic and make tests deterministic |
| Return or raise | Operation return value / current exception | Preserve the caller's success or failure contract |

“Attempt” does not need its own mutable object in v1. It is a counter. “API” is the supplied dependency. “Deadline” can be a number. If configurations become reusable across many call sites, an immutable `RetryPolicy` record can group the settings without changing the algorithm.

```text
Optional reusable design, only if needed:

RetryPolicy [immutable settings]
          |
          v
RetryExecutor [operation + clock + sleeper + randomness]
          |
          +-- each execute() owns its own attempt and deadline

No shared mutable attempt counter across calls.
```

#### Compare three plausible implementations

1. **Immediate retries.** A loop catches transient errors and instantly tries again. It can recover from a brief glitch, but during overload it adds more work exactly when the service has less capacity. It is unsuitable for our stated backoff requirement.
2. **Exponential waits without jitter.** This reduces each caller's frequency. But clients failing together still wake at similar times, producing repeated bursts. It meets one requirement while missing synchronization control.
3. **Capped exponential ceilings plus full jitter and budgets.** This meets our specified behavior and makes completion bounded under the adapter's timeout contract. It adds timing and randomness dependencies, which we inject for verification.

> **Trade-off:** Full jitter can choose a very short wait. It spreads attempts but does not enforce a minimum delay. If the API requires a minimum cooldown, encode that as a separate lower bound; do not claim this policy satisfies it automatically.

#### Build the method in the right order

Start with `return operation(timeout)`. Add a catch for transient errors. Add the attempt limit before scheduling the next attempt. Add the waiting calculation. Finally, add deadline checks before calling and after failure, because time passed inside the operation.

```text
retry(operation):
    validate policy
    compute deadline once
    for each permitted attempt:
        compute remaining time
        if exhausted: stop
        try operation with bounded timeout
        if success: return
        if permanent error: propagate
        if last attempt: propagate transient error
        recompute remaining time
        choose next wait
        if wait cannot fit: stop
        sleep
        grow ceiling for the NEXT failure
```

The retry loop has no rollback responsibility. It cannot undo the provider's action. That is why repeat safety is a precondition, not a problem the catch block solves.

#### Verify one boundary tick by tick

Let total budget be 1.2 seconds, first call consume 0.8 seconds, and selected wait be 0.3 seconds.

| Step | Clock | Remaining | Result |
|---|---:|---:|---|
| Start | 0.0 | 1.2 | Deadline set to 1.2 |
| Attempt 1 starts | 0.0 | 1.2 | Operation gets timeout 1.2 rather than 2 |
| Attempt 1 fails | 0.8 | 0.4 | Still eligible to consider retry |
| Sleep finishes | 1.1 | 0.1 | Next timeout must shrink to about 0.1 |
| Attempt 2 starts | 1.1 | 0.1 | Recheck budget; never reuse the original timeout |

> **Correctness:** Reusing `remaining` from before sleep is wrong. The implementation recalculates it at the top of the next iteration. A final failed attempt raises immediately and never sleeps.

#### Work an extension instead of merely naming it

For asynchronous I/O, make the operation and sleeper awaitable and use nonblocking waiting. Cancellation must propagate; do not classify it as a temporary API failure. For retries that must survive process death, persist attempt count, operation key, next scheduled time, and state. A worker claims due work, invokes the adapter, and durably records the next state. That is a scheduler, not a cosmetic change to `time.sleep`.

For `Retry-After`, the adapter supplies a minimum wait. Combine it with the local policy so the actual wait is never shorter than the server's minimum, and stop if it cannot fit the deadline. Keep parsing HTTP headers outside the generic retry loop.

**Level check:** A basic answer writes a bounded loop. A strong answer explains error classification, jitter and timeout semantics. A senior answer identifies unknown write outcomes, nested retries, cancellation, provider guidance, and where retry traffic itself must be budgeted.

<a id="q80"></a>
## 80. What is idempotency and why does it matter for customer integration?

### 1. Understand the problem

```text
Client -> charge $100 -> Provider records payment
Client <- response lost <- network failure
Client -> charge $100 again -> duplicate payment?
```

Idempotency means repeating the same logical operation produces the same intended effect as performing it once. Reads commonly have this property; “append a row” and “send an email” usually do not. Duplicate delivery is possible in many integrations, especially with at-least-once queues; not every network or queue has the same delivery contract.

> **Explanation:** “Set the balance to $100” is idempotent. “Add $100 to the balance” is not. Idempotency concerns the business effect; repeated requests may still produce additional logs or metrics.

### 2. Clarify requirements

Ask what constitutes one logical operation, who generates its key, how long duplicates can arrive, whether identical payloads represent separate intentions, and where the side effect occurs. Assume a customer asks us to create a payment, supplies a stable request key, and may retry after timeouts.

### 3. Model the state and contract

```text
Idempotency record
  tenant_id + operation_type + key  [unique]
  canonical_payload_hash           [detect changed intent]
  state                            [pending / completed / unknown]
  stored_result                    [replay completed outcome]
  created_at                       [retention policy]
```

```text
Request + key
      |
Atomic insert/claim in durable store
      |
      +-- existing key, different payload -> reject conflict
      +-- existing completed operation ---> return stored result
      +-- existing pending/unknown -------> report state or reconcile
      +-- new operation ------------------> execute once, record result
```

> **Correctness:** Two requests can both pass “check if key exists” before either inserts. A unique constraint or equivalent atomic claim enforces exclusivity. A Python dictionary or unlocked check-then-write cannot protect multiple service instances.

### 4. Implement the database part

For importing an entity with a stable source ID, PostgreSQL can enforce uniqueness and upsert it:

```sql
CREATE TABLE source_shipments (
    tenant_id text NOT NULL,
    source_id text NOT NULL,
    shipment_id text NOT NULL,
    status text NOT NULL,
    source_version bigint NOT NULL,
    PRIMARY KEY (tenant_id, source_id, shipment_id)
);

INSERT INTO source_shipments
    (tenant_id, source_id, shipment_id, status, source_version)
VALUES
    ('tenant-a', 'sap', 'S123', 'delivered', 7)
ON CONFLICT (tenant_id, source_id, shipment_id)
DO UPDATE SET
    status = EXCLUDED.status,
    source_version = EXCLUDED.source_version
WHERE EXCLUDED.source_version > source_shipments.source_version;
```

This prevents duplicate entities and prevents an older version from overwriting newer state, under the assumption that the source version increases reliably. See [PostgreSQL's `ON CONFLICT` contract](https://www.postgresql.org/docs/current/sql-insert.html).

> **Pitfall:** An upsert is not a universal idempotency solution. An update that increments a counter can duplicate the effect. A local unique record also cannot atomically control an external payment provider.

### 5. Handle external effects

If the provider supports idempotency, pass the same key on every retry. If it times out, query its operation status or retry according to that contract. Persist enough information to reconcile after a crash. Without provider support, a crash after payment but before local completion leaves an unknown outcome; do not blindly execute again.

Test same key/same payload, same key/different payload, simultaneous requests, restart, and crash after the side effect. Key retention must cover the retry/replay horizon; expiring it too early reopens duplication risk.

> **Say it aloud:** “Idempotency protects the intended business effect when requests repeat. I define a stable operation key, scope it by tenant and operation, claim it atomically, and replay the stored result. For external writes I need provider idempotency or reconciliation; local deduplication alone cannot guarantee one payment.”

**Follow-up:** Why not hash the payload as the key? Two identical purchases can be separate legitimate operations. A key represents intent, not merely equal data.

### Design derivation: durable deduplication and the crash boundary

#### Agree on an explicit first-version contract

For a complete service design, clarify whether we own only a database mutation or call an external provider. Start with a database-only order creation: one tenant sends a stable key, duplicate keys with identical normalized payloads replay the same result, changed payloads conflict, and concurrent requests must not create two orders. External payments are the extension below.

> **Interview move:** “If order creation and the idempotency record live in the same database, I can commit them in one transaction. If payment happens outside that database, I need to discuss the separate provider outcome.”

#### Derive the model and contract

| Requirement | Owner | Necessary data or operation |
|---|---|---|
| Repeated logical requests map together | Idempotency repository | Unique `(tenant, operation, key)` |
| A key cannot silently change intent | Record | Hash of normalized relevant request fields |
| Completed requests replay results | Record | Stored response or stable result reference |
| Order and completion must agree | Service + database | One transaction covering both writes |
| Pending requests cannot both execute | Repository | Atomic insertion/claim, not separate unlocked checks |

```text
OrderService.create(tenant, key, request)
       | uses
       v
IdempotencyRepository.claim / lookup / complete
       |
       +---- same database transaction ----> OrderRepository.insert

API adapter parses input; service owns operation lifecycle;
database constraints enforce unique claims across instances.
```

A record groups facts; it does not itself decide authorization. Authenticate and authorize the caller before returning a stored result. Scope keys so one tenant cannot fetch another tenant's result. Normalize only fields that define the operation; an arbitrary raw JSON byte hash can treat harmless field ordering as a conflict.

#### Compare naive checks, durable claims, and provider-aware execution

**Check then insert:** both instances can see no record and both create an order. The check is not a lock.

**Durable unique claim:** the database permits only one claimant. This solves local concurrency but not external execution if a crash occurs between provider success and saving that success.

**Transactional local writes plus provider idempotency/reconciliation where needed:** use the strongest available boundary for each effect. This is more complex, but its guarantees correspond to the actual systems involved.

```text
Instance A                         Instance B
lookup key: absent                 lookup key: absent
insert unique claim: succeeds      insert unique claim: conflicts
create order                      load existing outcome/state
store result
commit

B must not proceed to create a second order after losing the claim.
```

#### Walk through local transactional pseudocode

```text
create_order(tenant, key, request):
    validate and authorize
    normalize relevant fields and hash them
    begin database transaction
    try atomic insertion of scoped key with payload hash

    if insertion did not win:
        load existing record using suitable transaction visibility
        if hash differs: reject key-reuse conflict
        if completed: return stored result
        otherwise: report pending / apply agreed wait policy

    create order
    store result and mark completed
    commit order and completion together
    return result
```

> **Correctness:** This is architectural pseudocode. Actual conflict handling depends on the database and isolation level. For example, a uniqueness error may abort a transaction unless handled using an appropriate conflict statement or savepoint. Do not pretend the pseudocode is a drop-in database library implementation.

#### Trace crash points

| Failure point | Database-only operation | External payment operation |
|---|---|---|
| Before claim | Retry can claim | Retry can claim |
| After uncommitted claim | Transaction rolls back | A separately committed pending record may remain |
| After local order insert, before commit | Order and claim both roll back | Not applicable to a remote payment |
| After database commit, before response | Retry replays committed result | Replay if provider result is recorded |
| Provider succeeds, local result not saved | No remote effect in baseline | Outcome unknown; query/retry with provider's same key contract |

If pending records persist, distinguish work not started from work with an uncertain side effect. A lease expiring may permit another worker to investigate; it does not prove the first worker failed to charge. Use ownership/fencing where supported, and reconcile before creating another external effect.

> **Explanation:** Exactly-once business effect is something you establish across the relevant boundaries. It is not a consequence of adding a table named `idempotency_keys`.

#### Extend with retention and outbox delivery

Retention must cover realistic redelivery, offline client retries and delayed backfills. On expiry, preserve a longer-lived business uniqueness constraint when the effect must never duplicate. For an order-created message, write an outbox event in the same transaction as the order; a publisher may redeliver it, so the receiving consumer still needs deduplication.

Verification includes two concurrent requests, changed payload under the same key, response loss after commit, restarted processes, authorization on replay, and expiry behavior. A basic answer defines repeat effects; a senior answer identifies transaction boundaries and proves the uncertain-outcome path rather than claiming a universal guarantee.

<a id="q81"></a>
## 81. Design a rate limiter with per-user and global limits

### 1. Understand and clarify

A shared API must protect downstream capacity while preventing one user from consuming everything. Ask whether limits are strict rolling windows or token-bucket rates, what bursts are permitted, how users are identified, whether a request costs one token, and whether state is local or shared across instances.

For the coding baseline: one process, concurrent callers, one token per accepted request, immediate rejection, each user has capacity 2 and refills at 1 token/second; the global bucket has capacity 3 and refills at 2 tokens/second.

> **Explanation:** A token bucket allows an immediate burst up to its capacity and then replenishes at a fixed rate. It is not the same contract as “at most N calls in every rolling W-second interval.” Clarify which behavior the customer needs.

### 2. Draw the decision

```text
Authenticated user -> RateLimiter.allow(user_id)
                               |
                      refill both buckets
                               |
                user >= 1 AND global >= 1 ?
                       /               \
                     yes                no
                      |                  |
             subtract 1 from both    subtract neither
             allow downstream call   return denied + wait estimate
```

> **Correctness:** “Pass both checks” must be atomic with consuming both tokens. Otherwise, concurrent requests can overspend. If the user bucket rejects, consuming a global token would waste shared quota on a request that never ran.

### 3. Derive the entities

| Entity | State and responsibility |
|---|---|
| Bucket | Capacity, refill rate, tokens, last update; calculate replenishment |
| RateLimiter | User bucket map, global bucket, clock, lock; atomic decision |
| Decision | Immutable allowed flag and retry-after seconds |

Refill only when a request arrives; no timer is needed:

```text
new_tokens = min(capacity, old_tokens + elapsed_seconds * refill_rate)
wait_for_one_token = max(0, 1 - tokens) / refill_rate
```

> **Explanation:** Fractional tokens preserve elapsed time. At one token/second, waiting half a second adds half a token. Capping at capacity prevents a quiet user from accumulating unlimited burst allowance.

### 4. Implement the single-process baseline

```python
from dataclasses import dataclass
from threading import Lock
import time


@dataclass
class Bucket:
    capacity: int
    rate: float
    tokens: float
    updated_at: float

    def refill(self, now):
        elapsed = max(0.0, now - self.updated_at)
        self.tokens = min(self.capacity, self.tokens + elapsed * self.rate)
        self.updated_at = now

    def wait_for_token(self):
        return max(0.0, 1.0 - self.tokens) / self.rate


@dataclass(frozen=True)
class Decision:
    allowed: bool
    retry_after_seconds: float | None


class RateLimiter:
    def __init__(
        self,
        user_capacity=2,
        user_rate=1.0,
        global_capacity=3,
        global_rate=2.0,
        clock=time.monotonic,
    ):
        if user_capacity < 1 or global_capacity < 1:
            raise ValueError("capacities must be at least 1")
        if user_rate <= 0 or global_rate <= 0:
            raise ValueError("refill rates must be positive")
        self.user_capacity = user_capacity
        self.user_rate = user_rate
        self.clock = clock
        self.users = {}
        self.lock = Lock()
        self.global_bucket = Bucket(
            global_capacity, global_rate, float(global_capacity), clock()
        )

    def allow(self, user_id):
        if not user_id:
            raise ValueError("user_id is required")

        with self.lock:
            now = self.clock()
            user = self.users.get(user_id)
            if user is None:
                user = Bucket(
                    self.user_capacity, self.user_rate,
                    float(self.user_capacity), now,
                )
                self.users[user_id] = user

            user.refill(now)
            self.global_bucket.refill(now)

            if user.tokens >= 1 and self.global_bucket.tokens >= 1:
                user.tokens -= 1
                self.global_bucket.tokens -= 1
                return Decision(True, None)

            wait = max(
                user.wait_for_token(),
                self.global_bucket.wait_for_token(),
            )
            return Decision(False, wait)
```

The shared lock protects both bucket updates and the decision. Do not hold it while making the downstream API call. Each call does O(1) expected map work; space is O(U) for U seen users. This baseline retains inactive users; production cleanup is an explicit extension.

### 5. Work a small example

```text
Time 0: global has 3; user A has 2
A request 1 -> allowed; global 2, A 1
A request 2 -> allowed; global 1, A 0
A request 3 -> denied;  global 1, A 0  [no quota consumed]
B request 1 -> allowed; global 0, B 1

Time 0.5: global refills to 1; A refills to 0.5
A request -> denied; needs another 0.5s for user quota
```

> **Explanation:** Use the maximum of the two wait estimates because *both* buckets need a token. It is an estimate assuming no competing requests; another caller can consume global capacity before this user retries.

### 6. Tests, scaling, and interview answer

Test independent users, global exhaustion, user exhaustion without global consumption, fractional refill, capacity cap after a long pause, invalid parameters, and concurrent calls. For HTTP, reject with 429 and translate the wait estimate into a suitable `Retry-After` value.

For multiple service instances, local locks do not coordinate quota. Move the read/refill/check/decrement operation into one atomic shared-store operation. Redis scripting can execute a short script atomically; see [Redis scripting guarantees](https://redis.io/docs/latest/develop/programmability/eval-intro/). Redis Cluster additionally requires the relevant keys to share a slot for this approach. One global bucket creates coordination pressure; strict global enforcement may require a centralized owner, while regional allocations trade exactness for scale.

> **Pitfall:** “Put counters in Redis” is incomplete. Separate reads and writes still race. Also, resetting a user's bucket too early during eviction restores capacity they have not earned. Evict only after enough idle time to be equivalent to a full bucket.

Decide explicitly what happens if the store fails: rejecting protects a fragile downstream but reduces availability; permissive fallback needs a bounded local policy. Never accept a spoofable user ID as the fairness boundary. Per-user caps limit domination; they do not guarantee equal scheduling fairness.

> **Say it aloud:** “I use a per-user bucket and a global bucket. A request consumes one token from both only when both have capacity. Refill and consumption are one atomic decision. In one process I protect that decision with a lock; across processes I use a shared atomic operation. I clarify burst semantics, rejection behavior, identity, cleanup, and store-failure policy.”

**Recall check:** Why must rejecting a user not consume a global token? Because that request did not use downstream capacity, and consuming the token would deny capacity to other users.

### Design derivation: the global bucket changes the locking problem

#### Confirm what is intentionally excluded

The v1 code has one user identity, one global quota, one algorithm, fixed startup settings, a single process, and immediate rejection. Endpoint-specific algorithms, distributed state, dynamic configuration, weighted requests and queued admission are extensions. This is a different contract from the supplied reference's configurable endpoint limiter; copy its reasoning process rather than automatically copying its factory.

**You:** “Must every rejected attempt consume quota?” **Interviewer:** “No, count admitted requests.” That makes all-or-nothing consumption a rule. If abuse monitoring should count attempts, maintain separate telemetry; do not confuse it with admission tokens.

**You:** “Can the global limit be approximate?” **Interviewer:** “Not in v1.” Every accepted request must coordinate against the same global state.

#### Derive every field

| Field | Requirement it supports | Why a simpler alternative breaks |
|---|---|---|
| `users` map | Independent history per user | One user counter would mix unrelated callers |
| `global_bucket` | Shared capacity across users | Per-user limits alone allow total overload |
| `tokens` float | Fractional continuous refill | Truncation loses short-interval accumulation |
| `updated_at` | Refill once for elapsed time | Reusing old time grants the same refill repeatedly |
| `capacity` | Maximum burst | Unlimited idle accumulation allows huge bursts |
| `rate` | Sustained refill | Capacity alone never replenishes |
| `lock` | Joint check and consumption | Independent updates overspend or lose quota |
| `clock` | Stable elapsed timing/test control | Wall-clock jumps distort replenishment |

`Bucket.refill` owns token arithmetic because the bucket owns that state. `RateLimiter.allow` owns the conjunction of two quotas because that rule spans both buckets. `Decision` is immutable data so a caller cannot alter the limiter's past decision by mutating a return object.

> **Explanation:** Ownership does not mean every bucket can independently admit a request. The coordinator owns the rule that both permissions must exist together.

#### Compare the algorithms under actual requirements

| Algorithm | Memory per active key | Boundary behavior | Fits this v1? |
|---|---|---|---|
| Fixed-window counter | O(1) | Bursts can straddle a window reset | Only if calendar-window semantics are accepted |
| Sliding-window log | O(accepted requests in the window) | Exact rolling-window accounting | If a strict rolling maximum is required |
| Token bucket | O(1) | Immediate capacity burst then smooth refill | Yes: this is the stated contract |

For a strict rolling window `(now-W, now]`, expire timestamps `<= now-W`, check both counts, then append to both logs only if both permit admission. Agree on the exact boundary before coding. A timestamp exactly one window old cannot remain in the count while simultaneously producing a zero wait estimate.

> **Pitfall:** An algorithm can be correct but implement the wrong policy. A bucket with capacity 100 and refill 10/second does not promise at most 100 admissions in every rolling ten seconds; available initial tokens plus ongoing refill permit a larger count.

#### Compare locking approaches with a concrete race

```text
Initial: user A = 1 token, global = 1 token

Thread 1                           Thread 2
reads global = 1                   reads global = 1
reads user quota available         reads its user quota available
allows                             allows

Two admissions used one global token -> broken protection.
```

**No lock** fails under concurrent callers. **Per-user lock only** fixes races within one user but two different users still race on global state. **One short shared lock** correctly protects the joint operation in our single-process implementation. It serializes admission, but does no network calls or sleeps inside the lock.

Per-user plus global locks can work with a consistent acquisition order and safe bucket creation/removal. However, the global lock still becomes a shared coordination point; separate user locks do not eliminate that requirement. Prefer the easier correct implementation until contention measurements justify more complexity.

> **Interview move:** “The reference's per-key locking is useful when requests mutate independent client quotas. This prompt adds a global quota, so I also need synchronization for the shared global state. I will keep the atomic decision small rather than claim per-key locking removes all contention.”

#### Verify a global rejection preserves user capacity

| Step | User A | User B | Global | Result |
|---|---:|---:|---:|---|
| Initial, same instant | 2 | 2 | 1 | One global admission available |
| A admitted | 1 | 2 | 0 | Both relevant balances decremented |
| B requests | 1 | 2 | 0 | Denied; B retains its full two tokens |
| Later global refills to 1 | 1 plus refill | 2 | 1 | B may now be admitted |

Refill may update timestamps or balances on a denied request; the invariant is “no consumption on denial,” not “no mutation whatsoever.” The wait estimate assumes no new competing traffic. When several threads contend, admission order is not promised.

#### Handle changed configuration without gifting quota

Suppose a user has 0.4 tokens at rate 1/second and capacity 2. A new policy raises capacity to 5 and rate to 2/second. Preserve earned tokens; do not reset to five. First settle elapsed time under the old rate, then apply the new policy and clamp tokens to the new capacity under synchronization. A capacity reduction to 1 likewise clamps excess tokens.

Changing algorithms needs a migration policy: bucket state cannot reconstruct the last minute's exact request timestamps. Say whether a temporary reset/overlap is accepted or keep both policies during transition. State preservation is not automatic just because both algorithms implement an interface.

#### Handle cleanup and distributed coordination

A completely idle bucket can be safely recreated full once enough time has passed that refill would reach capacity anyway. Compute that condition from state and synchronize removal with admission. LRU eviction of a recently exhausted user grants an unearned reset. A fixed cache-size cap alone cannot preserve strict quota semantics.

In a distributed version, the authoritative store owns timing and the atomic decision. Do not compare one process's monotonic timestamp with another process's unrelated monotonic clock. Keep both bucket updates together, and address hot-key contention, store failure and restart semantics. If global coordination becomes too expensive, regional token allocations can improve throughput but require an explicit guarantee about total allocation and replenishment.

> **Explanation:** A strict global limit is inherently shared. You cannot remove coordination while retaining the same exact promise merely by adding more servers.

**Level check:** Basic: refill and reject correctly. Strong: explicit burst contract, fractional arithmetic and return semantics. Senior: joint atomicity, safe cleanup, configuration continuity, distributed time authority, and a measured decision about strictness versus scale.

<a id="q82"></a>
## 82. Robustly parse messy CSV or JSON

### 1. Understand and clarify

The customer sends a CSV export. Some rows are valid; others have extra fields, missing amounts, or unexpected types. Your job is to preserve usable records while making rejected records visible and recoverable.

Ask for real samples, encoding, delimiter, schema, null rules, money format, maximum file size, duplicate policy, and whether partial ingestion is acceptable. For this example, agree on UTF-8 CSV with a possible BOM, comma delimiter, required headers `customer_id,amount`, and nonnegative decimal amounts. Money has at most two decimal places. Invalid records go to quarantine; a structurally broken file stops processing because safe record boundaries are no longer certain.

> **Explanation:** A parser understands the file format. Validation decides whether a parsed record satisfies your business contract. Keep those decisions separate: a valid CSV row can still contain an invalid amount.

### 2. Draw the responsibilities

```text
Raw file [preserved]
       |
Decode using source's configured encoding
       |
CSV parser -> schema/header check
       |
Each record -> validation + explicit type conversion
                  /                      \
                valid                   invalid
                  |                       |
             normalized sink         quarantine sink
                                      reason + source location

Malformed CSV structure -> stop file, record failure for repair/replay
```

> **Pitfall:** `line.split(',')` corrupts values containing quoted commas or embedded newlines. Use a CSV parser. The Python module handles dialects and quoted fields; open files with `newline=''`. See [Python CSV documentation](https://docs.python.org/3/library/csv.html).

### 3. Implement a streaming baseline

The callbacks write records to external sinks. This avoids collecting an entire large file in memory. The raw file is retained separately; quarantine stores a pointer and reason rather than exposing sensitive raw rows in general application logs.

```python
import csv
from decimal import Decimal, InvalidOperation


def ingest_csv(path, emit_valid, emit_bad):
    counts = {"parsed": 0, "accepted": 0, "quarantined": 0}
    expected = {"customer_id", "amount"}

    with open(path, encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle, strict=True)
        headers = reader.fieldnames
        if (
            headers is None
            or len(headers) != len(set(headers))
            or set(headers) != expected
        ):
            raise ValueError("Expected unique customer_id and amount headers")

        for record_number, row in enumerate(reader, start=1):
            counts["parsed"] += 1
            try:
                if None in row or any(value is None for value in row.values()):
                    raise ValueError("Wrong number of fields")

                customer_id = row["customer_id"].strip()
                if not customer_id:
                    raise ValueError("Missing customer_id")

                try:
                    amount = Decimal(row["amount"].strip())
                except InvalidOperation as error:
                    raise ValueError("Invalid decimal amount") from error

                if not amount.is_finite() or amount < 0:
                    raise ValueError("Amount must be finite and nonnegative")
                if amount.as_tuple().exponent < -2:
                    raise ValueError("Amount has more than two decimal places")

                normalized = {"customer_id": customer_id, "amount": amount}
            except ValueError as error:
                emit_bad({
                    "source": str(path),
                    "record_number": record_number,
                    "ending_line": reader.line_num,
                    "reason": str(error),
                })
                counts["quarantined"] += 1
            else:
                emit_valid(normalized)
                counts["accepted"] += 1

    return counts
```

> **Correctness:** Sink failures propagate rather than being mislabeled as invalid input. If the sink fails halfway through, mark the job incomplete and replay using idempotent writes. Accepted counts are meaningful only after successful sink writes; a durable run manifest is a production extension.

> **Explanation:** `Decimal` represents decimal money without introducing binary floating-point rounding. Rejecting `NaN` and infinity is necessary: they can parse successfully but are not valid business amounts. This contract also rejects `1.000`; change that rule only after agreeing whether extra zero precision is acceptable.

`csv.Error` or a decoding failure propagates to the file-level runner. Preserve the raw file and record the failure location; do not assume the next physical line is a new record because quoted fields can span lines. Enforce file, field, and identifier size limits at the ingestion boundary.

### 4. Apply the same design to JSON

For newline-delimited JSON, one valid record per line provides a natural quarantine boundary: decode each line with `json.loads`, require an object, then validate it. For a whole-file JSON array, a syntax error can invalidate the document; do not pretend every broken element is independently recoverable. Stream large arrays with a suitable parser rather than loading everything into memory. Define duplicate-object-key and unknown-field policies explicitly.

> **Pitfall:** Guessing encodings, stripping punctuation from money, or silently replacing undecodable bytes can convert bad data into plausible wrong data. A source-specific adapter is safer than a universal “fix anything” parser.

### 5. Test and speak

Test quoted commas, extra/missing columns, BOM, duplicate headers, blank identifiers, nonnumeric/negative/nonfinite amounts, excessive precision, broken quotes, sink failure, and a large file. For a completed run, `parsed = accepted + quarantined`. Processing is O(bytes read); helper memory is proportional to the largest record, excluding sink storage.

> **Say it aloud:** “I inspect real samples and agree on the source contract. Then I separate format parsing from record validation, stream valid rows into a normalized sink, and quarantine invalid records with reasons and source pointers. Structural file errors stop the file. Raw data stays available for replay, and idempotent writes make recovery safe.”

**Recall check:** Why not quarantine every exception? Because a database outage is an operational failure, not evidence that the customer's row is malformed.

### Design derivation: what “robust parsing” actually guarantees

#### Narrow the first version through dialogue

**You:** “Can one file mix comma and semicolon rows?” **Interviewer:** “Different sources have different formats, but each source export uses one configured dialect.” This makes per-source dialect configuration appropriate; do not detect a new format on every row.

**You:** “Is partial import allowed?” **Interviewer:** “Valid records can be staged, but the reporting table must publish only completed accepted runs.” This creates a distinction between parsing, durable staging and publication. The baseline function handles parsing and callbacks; a run coordinator must own the publication rule.

**You:** “What is an empty amount?” **Interviewer:** “Invalid, not zero.” Now `''` must fail validation. Filling it with zero would change customer data while hiding uncertainty.

> **Explanation:** Robustness does not mean inventing a plausible value for every input. It means predictable behavior, visible errors, preserved evidence, and controlled recovery.

#### Derive components and reject a universal repair engine

| Responsibility | Required state/contract | Why it is separate |
|---|---|---|
| Source format | Encoding, delimiter, quoting, schema version | Source owner determines these rules |
| Parser | Iterator of parsed records and source positions | Format validity differs from business validity |
| Validator/normalizer | Required fields, conversion and domain rules | Reusable across representations when contracts match |
| Valid sink | Durable write with a stable replay identity | Storage outages must not become data errors |
| Quarantine sink | Restricted raw pointer, position, reason code | Supports inspection and controlled repair |
| Run coordinator | Input version, counts, state, output version | Determines whether partial progress may publish |

For a small interview implementation, functions and callbacks are enough. If many adapters share validation, extract a `validate_customer_record(record)` function instead of copying amount logic into CSV and JSON code. The CSV parser should still keep CSV-specific rules such as wrong column counts.

```text
CSV adapter --+
              +-> common normalized record contract -> validator -> valid sink
JSON adapter -+                                      |
                                                     +-> quarantine

Adapter handles representation. Validator handles meaning.
```

#### Compare implementation strategies

**String splitting:** fast to write, but breaks quoted separators and multiline fields. It fails the file-format requirement before validation begins.

**Load everything and catch all errors:** convenient for a tiny demo, but large inputs exceed memory and broad exception handling hides sink failures. It cannot tell the operator whether bad data or unavailable infrastructure caused a failure.

**Stream through a standard parser, explicit validation and separate sinks:** bounded parser memory, clear failure categories and replayable results. It adds a run lifecycle to manage partial progress; that is an honest operational cost.

> **Trade-off:** Heuristic format detection is useful for investigation or onboarding. Once a source contract is known, store it explicitly and alert on drift. A guesser changing behavior unnoticed can make yesterday's and today's exports incomparable.

#### Walk through the code operation by operation

1. Open using the agreed encoding and newline handling. `utf-8-sig` accepts UTF-8 with or without a leading BOM; it does not decode arbitrary legacy encodings.
2. Read the header. Reject duplicate or unexpected names rather than letting one field overwrite another.
3. Parse a logical CSV record. Several physical lines may belong to one record.
4. Check field count before conversion. `DictReader` exposes extra values under a `None` key and missing values as `None`.
5. Strip the identifier under an agreed normalization rule; do not convert `000123` to integer 123.
6. Parse amount explicitly, check finite/nonnegative/precision rules, and construct the normalized record.
7. Write it to the correct sink. Only mark accepted after the sink reports success.

The example counts parser-level records, not physical lines. `ending_line` helps locate the parser position; the original raw file and record number remain necessary for reconstruction.

#### Show a useful failure trace

```text
Run R1 uses source file version V1
Record 1: A,12.30          -> normalized and staged
Record 2: B,NaN            -> quarantine: nonfinite amount
Record 3: C,7.10           -> normalized and staged
Record 4: D,2.00           -> database sink unavailable

Run becomes FAILED, not COMPLETED.
No output version is published if the contract requires completed runs.
Retry R1/V1 with stable row identities:
  records 1 and 3 deduplicate, record 2's quarantine is repeat-safe,
  record 4 is written after the sink recovers.
```

> **Correctness:** Record-number identities are safe only when tied to an immutable source file version. Row 4 in a new export may represent a different entity. Business entity keys and source versions are preferable for normalized updates.

#### JSON needs its own structural boundary

For NDJSON, require one JSON object per line and define blank-line behavior. For each line: decode JSON, check it is an object, enforce known/required fields, normalize with the common validator, and route validation errors to quarantine. A JSON object such as `{"customer_id": "A", "amount": "12.30"}` avoids treating binary floats as the authoritative representation of money.

```text
NDJSON:
line 1 -> parse succeeds -> validate -> accepted
line 2 -> JSON syntax error -> quarantine this bounded line
line 3 -> parse succeeds -> validate -> accepted

Whole JSON array:
[ record, broken syntax, record ] -> document parse failure
Do not pretend the parser can always recover record boundaries.
```

Oversized lines must fail a size limit before consuming unbounded memory. Duplicate JSON object keys need an explicit reject-or-accept policy; the standard decoder's default behavior is not automatically the business contract.

#### Work the extension: schema evolution

Suppose a new source adds `currency`. For v1, unexpected headers deliberately fail. For v2, update the schema version and normalization rules, require a supported currency, and test whether existing consumers can accept the new field. Replay V1 data under the V1 mapping, or explicitly backfill with the new mapping version. Do not silently reinterpret old accepted records.

**Level check:** Basic: use the right parser and validate types. Strong: distinguish row/file/sink failures and prove count reconciliation. Senior: define publication, replay identities, sensitive quarantine, size limits and schema-version behavior.

<a id="q83"></a>
## 83. Write SQL for high-return-rate customers and speed it up

### 1. Clarify the metric before querying

Ask whether “return rate” means returned orders, returned units, or refunded value; whether partial returns count; which order statuses qualify; and whether the window selects order date or return date.

Assume an **order cohort**: completed orders placed in a given UTC interval; an order counts as returned if it has at least one approved return recorded before the report's `as_of` timestamp. Require at least ten orders and a return rate above 30%. A customer returning one of one orders should not outrank a customer returning 40 of 100 without showing the denominator.

```text
orders:  one row per order
returns: possibly several rows per order

Eligible orders -> exists an approved return as of report time?
                         |
                 one boolean per order
                         |
              aggregate once per customer
                         |
              filter volume + return ratio
```

> **Explanation:** The denominator is the eligible order cohort. Returns can happen after the order window closes, provided they occur before `as_of`. Recent orders have had less time to be returned, so comparisons may need a maturation window.

### 2. Define the schema and query

Assume `orders(order_id PK, customer_id, ordered_at, status)` and `returns(return_id PK, order_id FK, returned_at, status)`. Timestamps are timezone-aware. Parameters below use named bind placeholders supported by an appropriate database client.

```sql
WITH order_flags AS (
    SELECT
        o.order_id,
        o.customer_id,
        EXISTS (
            SELECT 1
            FROM returns r
            WHERE r.order_id = o.order_id
              AND r.status = 'approved'
              AND r.returned_at < :as_of
        ) AS was_returned
    FROM orders o
    WHERE o.status = 'completed'
      AND o.ordered_at >= :start_at
      AND o.ordered_at < :end_at
      AND o.ordered_at < :as_of
), customer_stats AS (
    SELECT
        customer_id,
        COUNT(*) AS order_count,
        COUNT(*) FILTER (WHERE was_returned) AS returned_order_count
    FROM order_flags
    GROUP BY customer_id
)
SELECT
    customer_id,
    order_count,
    returned_order_count,
    returned_order_count::numeric / NULLIF(order_count, 0) AS return_rate
FROM customer_stats
WHERE order_count >= :min_orders
  AND returned_order_count::numeric / NULLIF(order_count, 0) > :threshold
ORDER BY return_rate DESC, order_count DESC, customer_id;
```

> **Correctness:** `EXISTS` preserves one row per order even when an order has several returns. A raw one-to-many join can inflate counts. The cast avoids integer division. A half-open interval `[start, end)` prevents overlapping report windows from counting the boundary twice.

### 3. Work through an example

```text
Customer A: 10 eligible orders, 4 orders returned -> 40% -> included
Customer B:  2 eligible orders, 2 orders returned -> 100% -> excluded (<10)
Customer C: 10 eligible orders, 3 orders returned -> 30% -> excluded (>30 required)

If A's first returned order has 3 return records:
It still contributes 1 returned order, not 3.
```

### 4. Optimize using evidence

Inspect `EXPLAIN`, then use `EXPLAIN (ANALYZE, BUFFERS)` in an appropriate environment to compare actual row counts, timing, and I/O. `ANALYZE` executes the query. See [PostgreSQL on query plans](https://www.postgresql.org/docs/current/using-explain.html).

Candidate indexes, subject to the real workload:

```sql
CREATE INDEX orders_completed_date_idx
    ON orders (ordered_at)
    INCLUDE (order_id, customer_id)
    WHERE status = 'completed';

CREATE INDEX returns_approved_order_time_idx
    ON returns (order_id, returned_at)
    WHERE status = 'approved';
```

> **Pitfall:** Correlation is not automatically slow. An indexed `EXISTS` can be a good semi-join or lookup plan. For broad windows, aggregating distinct returned order IDs first may win. Compare plans rather than claiming every correlated query must be rewritten.

If repeated reports remain expensive, preaggregate with a clear freshness contract. Late returns can change old cohorts, so updates must revisit affected summaries. Indexes add storage and write cost; a sequential scan can be appropriate when most rows qualify.

### 5. Tests and interview answer

Test multiple returns per order, pending returns, no returns, exact threshold, exact window boundaries, minimum sample size, and late returns. State that query cost depends on cardinality, indexes, and plan rather than assigning a simplistic universal Big-O.

> **Say it aloud:** “I first define the denominator and window. I compute one returned flag per eligible order, then aggregate by customer and filter by rate and sample size. I inspect the actual plan before adding indexes or changing query shape. For repeated reporting I consider incremental summaries while accounting for late returns.”

**Follow-up:** If we measure refunded value instead, what changes? Aggregate money at a consistent currency and grain, reconcile adjustments, and divide refunded value by eligible sales value rather than counting orders.

### Query derivation: defend grain, boundaries, and the plan

#### Translate the prompt into a metric contract

“High-return-rate customer” hides at least three choices: what counts as a return, what set of purchases is eligible, and how much evidence is needed. State them before writing SQL. In a cohort metric, returns are linked to orders selected by order time. In an activity metric, this month's returns and this month's sales can refer to different orders; that ratio answers a different question.

> **Interview move:** “I will use orders placed in the requested interval as the denominator and count each one once if it had an approved return by the report time. If you mean units or refund value, I will change the grain before aggregating.”

#### Design the relational stages

| Stage | Grain | Columns needed | Rule it protects |
|---|---|---|---|
| Eligible orders | One row per order | Order ID, customer ID | Denominator respects status and window |
| Return evidence | Zero or more records per order | Order ID, status, return time | Only approved evidence available as of report |
| Order flags | One row per eligible order | Customer, returned boolean | Multiple returns cannot duplicate an order |
| Customer statistics | One row per customer | Counts and ratio | Aggregation occurs at reporting grain |
| Final selection | One row per qualifying customer | Counts plus ratio | Minimum sample and threshold explicit |

You do not need `CustomerStatsRepository` or a class per CTE. In SQL, the clean boundaries are row sets with explicit grain. The important question is where cardinality changes.

#### Prove the join problem with actual rows

```text
Orders
O1, customer A
O2, customer A

Approved return rows
R1 -> O1
R2 -> O1
R3 -> O1

Naive LEFT JOIN result
O1, R1
O1, R2
O1, R3
O2, NULL

COUNT(return row)/COUNT(joined row) = 3/4 = 75%
Returned-order rate                = 1/2 = 50%
```

> **Explanation:** Neither 3 nor 4 is the intended customer-level count here. `EXISTS` creates the returned flag without changing order grain. Counting distinct IDs can also work, but a clear grain makes later changes easier to reason about.

#### Compare alternatives fairly

**One-to-many join with raw counts:** incorrect for our definition because duplicates change the denominator and numerator.

**Distinct counts after a join:** can be correct if filters and denominators are placed properly. The database may need to process a large intermediate result and distinct aggregation. Test its plan rather than rejecting it categorically.

**`EXISTS` or preaggregated return IDs:** both keep order-level meaning explicit. Indexed existence checks can be efficient for narrow cohorts; preaggregation may be attractive when many orders qualify. Neither is universally fastest.

```text
Alternative:
approved_returned_orders = DISTINCT order IDs satisfying status/as_of
eligible_orders LEFT JOIN approved_returned_orders
GROUP BY customer

Because the right side is unique per order, the join preserves order grain.
```

#### Explain each query boundary

`status='completed'` defines eligibility. `ordered_at >= start` and `< end` define a half-open window; two adjacent reports then share no order at the boundary. `< as_of` prevents future orders from entering a historical report. The return predicate likewise stops future evidence from altering that report definition.

`COUNT(*) FILTER (WHERE was_returned)` counts true flags. The numeric cast keeps `4/10` from truncating. `NULLIF` makes denominator intent explicit, although groups produced by this query contain at least one order. The strict `>` threshold excludes exactly 30%; use `>=` only if that is the agreed rule.

> **Correctness:** A return status overwritten in place after the report time can leak future knowledge into a supposedly historical report. If true historical reconstruction is required, retain status history or snapshots; timestamps alone do not solve it.

#### Read the performance evidence before changing the design

In the plan, look at how many eligible orders are scanned, whether return lookups repeatedly scan the full returns table, actual versus estimated row counts, sort/hash memory behavior, and buffer reads. Explain a candidate change with its expected effect: “This index may reduce approved-return lookup work for each order,” not “indexes make SQL fast.”

For a broad report, a sequential scan may be cheaper than random lookup. For a narrow interval, date filtering can be selective. Inspect statistics and the production distribution. Benchmark representative windows and compare output equivalence before accepting a faster plan.

#### Verify rows and extend the metric

Use a fixture with repeated returns, a pending return, an order at `start`, one exactly at `end`, and a return exactly at `as_of`. State which qualify under the chosen inequalities. Check intermediate counts before looking only at the final sorted list.

If the customer wants unit-return rate, move to an order-item/quantity grain, handle partial quantities and duplicate events, and ensure numerator cannot exceed eligible quantity without an explained adjustment. If they want currencies combined, define conversion timing/rates; do not sum dollars and euros directly.

For a daily summary extension, store sufficient cohort facts to update an old customer's numerator when a late approved return arrives. A summary that only records “returns today divided by orders today” cannot reproduce the original cohort metric.

**Level check:** Basic: correct aggregation and division. Strong: one-to-many cardinality, sample sizes and time boundaries. Senior: historical information availability, delayed outcomes, actual-plan evidence, and maintenance of incremental summaries.

<a id="q84"></a>
## 84. Design ingestion for twelve fragmented sources with no clean schema

### 1. Understand and clarify

The business wants a unified view, but twelve sources disagree on identifiers, fields, update timing, and definitions. Ask which decision the unified data supports, which entities matter first, source access/owners, data volumes, required freshness, deletion rules, and acceptable partial results.

For a first slice, assume an ops dashboard needs shipment status from one warehouse and one carrier. Do not begin by modeling every entity in all twelve systems.

### 2. Map the pipeline

```text
SAP / carrier APIs / CSV / databases
              |
        source adapters [cursor, auth, rate limits]
              |
        restricted raw landing [version + source + fetched_at]
              |
        transform + schema validation
              |                       \
              |                        -> quarantine + reason
              v
        normalized source records
              |
        identity mapping + reconciliation rules
              |
        canonical entities -> serving table -> ops dashboard
              |
        lineage + freshness + quality metrics throughout
```

> **Explanation:** Raw data lets you rerun a corrected transform without asking the source to reproduce the past. “Raw” does not mean keep everything forever: apply access controls, retention, and deletion requirements to this layer too.

### 3. Identify responsibilities and data contracts

| Component | Responsibility |
|---|---|
| Source adapter | Extract with pagination/checkpoints and source-specific limits |
| Raw envelope | Payload pointer, tenant/source, source ID/version, fetch time |
| Transformer | Normalize fields and validate against a versioned schema |
| Entity resolver | Map source identifiers to canonical identities |
| Writer | Idempotently commit updates and reject stale versions |
| Run manifest | Record progress, counts, mapping version, and failures |

> **Correctness:** Source A's `customer_id=123` and source B's `customer_id=123` need not name the same person. Start with namespaced IDs and explicit mappings. Fuzzy matches need confidence and review; similarity alone must not silently merge identities.

### 4. Walk through one end-to-end run

1. Extract one page and retain its raw records with stable source identifiers.
2. Validate and normalize each record; quarantine ambiguity with a reason.
3. Write accepted versions using unique source keys and version ordering.
4. Record lineage and successful progress durably.
5. Advance the checkpoint only after the necessary writes are durable, or commit checkpoint and writes together when feasible.
6. Replay safely after failure. Use a staging version and publish only after acceptance checks if the dashboard needs a consistent snapshot.

> **Pitfall:** Advancing a cursor before saving its page loses data after a crash. Saving the page before advancing can cause duplicates on replay, which idempotency handles. A source timestamp alone is not always a reliable cursor: use a tie-breaker or overlap window.

### 5. Sequence delivery and measure

First agree on one entity and definition, then ship one source to one visible consumer. Add a second source to test reconciliation before expanding to twelve. Track source-to-output freshness, extracted/accepted/quarantined counts, duplicate suppression, unmatched IDs, and reconciliation differences. Exercise schema drift, API outage, backfill overlap, out-of-order updates, and source deletion.

> **Say it aloud:** “I preserve permitted raw data, isolate source quirks in adapters, and normalize through versioned contracts. I use stable source keys, explicit identity mappings, idempotent writes, and durable checkpoints. I prove one source-to-dashboard slice, then add sources based on business value and integration risk.”

**Follow-up:** What if two sources disagree? Define field-level authority and freshness rules with the business owner; keep both observations and the rule that produced the selected value.

### Design derivation: ownership, checkpoints, and publication

#### Pin down the first slice

**You:** “Which dashboard decision must work first?” **Interviewer:** “Managers need to know whether today's shipments have left the warehouse.” This narrows the canonical schema to shipment identity, dispatch status, event time and evidence. Billing, customer histories and route optimization are excluded.

**You:** “Can data from different sources arrive at different times?” **Interviewer:** “Yes, but the UI must disclose source freshness.” That means you need per-source watermarks, not one green run-success badge.

**You:** “Can we reread historical pages?” **Interviewer:** “Yes, with quota limits.” That enables controlled replay and overlap windows. If the source is a destructive stream, persist input before acknowledging it instead.

#### Derive state and interfaces

```text
IngestionCoordinator.run(source, cursor, mapping_version)
    |
    +-> Adapter.fetch_page(cursor) -> records + next_cursor
    +-> RawStore.persist(envelopes) -> stable raw references
    +-> Transformer.normalize(envelope) -> valid | rejected
    +-> Writer.upsert(valid, source_version)
    +-> Quarantine.write(rejected)
    +-> RunStore.commit_progress(cursor, counts, lineage)

Publisher.promote(output_version) only after agreed run validation
```

| Requirement | Remembered state | Owner |
|---|---|---|
| Resume after failure | Source cursor/checkpoint and run state | Run store/coordinator |
| Reprocess original inputs | Raw location and source/input version | Raw store |
| Explain a transformed value | Mapping version and source lineage | Transform output |
| Reject older updates | Source version/event-order rule | Writer |
| Distinguish source identities | Source namespace and mapping table | Entity resolver |
| Display freshness | Source event watermark and fetch time | Serving/quality contract |

> **Explanation:** Fetch time tells you when you obtained data. Event time tells you when the source says it happened. A newly fetched export can still contain yesterday's operational state.

#### Compare integration shapes

**Direct source-to-dashboard writes:** quick for one clean source, but schema changes and partial failures leak directly into the consumer. Replay may be impossible once data is overwritten.

**One universal parser and schema for all sources:** looks consistent, but source-specific meaning and identity rules become hidden conditionals. It can force false equivalence among fields called `status`.

**Adapters plus raw evidence and versioned transforms:** makes quirks and recovery explicit. It costs storage, schema ownership and additional lifecycle work. Choose this when replay, audit and multiple unreliable sources are required; it is not ceremony for its own sake.

#### Implement the page lifecycle explicitly

```text
run_page(source, checkpoint):
    fetch bounded page using deadline/rate-limit policy
    persist page's raw records with identity/version
    normalize each record under the selected mapping version
    persist rejected records with reasons
    durably write accepted records idempotently
    validate page accounting
    persist committed progress and next cursor
```

If the raw store, serving store and run store are different systems, do not promise one database transaction spans them. Use replay-safe writes and a recoverable progress state. If the same transactional database owns page output and checkpoint, an atomic commit simplifies the boundary.

#### Verify a crash trace

```text
Checkpoint = page 7
Fetch page 8 -> raw saved -> 80 rows normalized -> 70 written
Process crashes before remaining writes and checkpoint update

Restart still sees checkpoint page 7
Replay page 8:
  first 70 rows are repeat-safe
  remaining rows are written
  quarantine and accounting reconciled
  checkpoint advances to page 8
```

If instead checkpoint page 8 were saved before the final writes, the restart would skip incomplete work. That is data loss, even though the job's next run could report success.

> **Correctness:** Idempotency protects duplicate replay; it does not protect skipped input. Checkpoint ordering is a separate guarantee.

#### Handle schema change and conflicting sources

Suppose one carrier changes `dispatched` to `in_transit`. The adapter observes a schema/value drift, quarantines or maps it only under a reviewed policy, and records a new mapping version. Validate before promoting output. A shipment disappearing from an export might mean deletion, filter change or source failure; agree on tombstone/snapshot semantics before deleting canonical rows.

When SAP says “packed” and a carrier says “collected,” ask whether those are contradictory or sequential observations. Define a canonical lifecycle using source evidence. Preserve observations rather than silently choosing the newest fetched value. Business owners decide authority for disputed fields.

#### Work an extension: backfill during live ingestion

Backfill workers and live workers may update the same entity. Preserve source-version ordering so older backfill data cannot overwrite a newer live observation. Isolate capacity so historical work does not starve freshness SLAs. Track backfill scope and mapping version; prove output equivalence on a sample before broad promotion.

**Level check:** Basic: adapters and validation. Strong: replay, quarantine and lineage. Senior: multi-store recovery, watermarks versus fetch times, source-version ordering, deletion semantics, and a publication contract that consumers can trust.

<a id="q85"></a>
## 85. Logistics ops cannot trust the dashboard: investigate and propose a plan

### 1. Frame the business problem

“Trust” is too broad to debug. Ask an operator to show one shipment or metric that caused a bad decision. Learn what action they take, what they compare against, the expected freshness, and the business impact. Bring in the metric owner and the source/pipeline owners.

> **Interview move:** “Can you show me one recent case where the dashboard disagreed with what your team knew? What decision did that disagreement affect?”

### 2. Decompose the evidence path

```text
Operational event -> source -> extraction -> transformation -> warehouse
                                                                     |
                                                               metric/query
                                                                     |
                                                                cache -> UI

Actual event time ---------------- compare with ---------------- shown time
```

Common hypotheses: delayed ingestion, incorrect join/deduplication, timezone conversion, ambiguous metric definition, stale cache, or misleading presentation. Rank them by evidence, investigation cost, and impact. Do not pick a root cause before tracing a failing example.

### 3. Trace a concrete discrepancy

Suppose the dashboard says “20 delayed shipments,” while ops counts 12. Freeze the report time, warehouse, timezone, and shipment set. Extract the contributing IDs. Compare the sets and trace a few discrepant IDs from UI back to source.

```text
Dashboard set: 20 shipment IDs
Ops set:       12 shipment IDs
Difference:    8 IDs
    5 already delivered but cache stale?
    3 counted twice after join?
These are hypotheses to verify, not conclusions.
```

> **Explanation:** Comparing identifiers reveals *which* records disagree. Comparing totals alone cannot distinguish stale data, duplicates, and different definitions.

### 4. Propose a bounded repair

Agree on one metric's precise definition and owner. Repair the verified defect, add reconciliation checks against an agreed source, show freshness/caveats in the UI, and run the corrected slice alongside the current workflow. Expand after operators confirm the metric supports their decisions.

Acceptance might include zero unexplained ID-level differences on sampled cases and freshness within an agreed operating window. These are negotiated criteria, not universal thresholds. Track discrepancy rate, freshness violations, and whether operators stop maintaining duplicate spreadsheets.

> **Pitfall:** Adding a green “healthy” badge without validating the underlying rows hides the problem. Technical pipeline success does not establish business correctness.

### 5. Failures, follow-ups, and answer

If a source is delayed, show the last successful event time and degraded state. If metric definitions conflict, escalate to an accountable business owner and document the chosen meaning. Correct historical reports where needed and communicate their impact.

> **Say it aloud:** “I would turn ‘untrustworthy’ into one reproducible discrepancy tied to an ops decision. I would compare underlying shipment IDs and trace them through source, pipeline, query, cache, and UI. Then I would repair the verified cause and prove one agreed metric with reconciliation and freshness indicators before expanding.”

**Follow-up:** How do you rebuild trust after fixing the bug? Demonstrate reconciled real cases with operators, disclose limitations, and measure continued use rather than declaring trust restored from a deploy.

### Investigation derivation: a reproducible discrepancy becomes a work plan

#### Turn vague answers into an investigation contract

**You:** “Which decision did the dashboard get wrong?” **Ops:** “We escalated shipments that had already arrived.” That identifies a workflow impact and narrows the investigation to status transitions, freshness and exception selection.

**You:** “Can you show the exact report and shipment IDs?” **Ops:** “Yes, from the 9 a.m. warehouse report.” Freeze the report parameters and compare information available at 9 a.m.; comparing with current state at noon would produce misleading differences.

**You:** “What is the authoritative arrival event?” **Data owner:** “The carrier scan, not the warehouse's manually entered label.” Now source authority is a testable requirement. It may reveal the dashboard was implementing a different definition rather than a coding defect.

> **Explanation:** You have three distinct questions: did the source have the fact, did the pipeline carry it correctly, and did the dashboard mean what the user thought? Fixing the wrong layer wastes time.

#### Identify evidence owners and required artifacts

| Artifact | Needed fields | Purpose |
|---|---|---|
| Report snapshot | Filters, timezone, report time, query/version | Reproduce what the operator saw |
| Shipment discrepancy | ID, expected value, shown value | Bound the problem to specific records |
| Source evidence | Event/status history and timestamp | Verify what was available then |
| Pipeline evidence | Ingestion watermark, transform version, errors | Identify missing/delayed/changed facts |
| Metric definition | Eligibility, deduplication, source authority | Separate semantic disagreement from implementation error |

One investigator coordinates the trace. Source teams provide event evidence; data teams own transforms; the business owner settles definitions; frontend owners verify displayed state. Ownership is part of decomposition, not an afterthought once a root cause appears.

#### Compare investigation approaches

**Rewrite the dashboard:** acts before diagnosing and can recreate the same underlying data defect. **Run a broad infrastructure audit:** may find issues but can take too long without isolating this discrepancy. **Trace one representative incorrect result end to end:** produces a concrete hypothesis quickly, then lets you test whether it generalizes. Expand investigation if the example is unrepresentative or evidence points to multiple causes.

```text
Shown "delayed" for S123 at 09:00
          |
Did source report delivered BEFORE 09:00?
    no -> investigate metric expectation / source availability
   yes
    |
Did warehouse receive that version before its promised cutoff?
    no -> investigate ingestion lag / failed update
   yes
    |
Does query select the latest eligible version correctly?
    no -> investigate query / transform / deduplication
   yes
    |
Does UI/cache display that query version?
    no -> investigate cache / frontend freshness
```

> **Correctness:** A latest-state table may not preserve what the source said at the time of the report. If history is absent, explicitly mark that conclusion as unverifiable and capture the evidence needed for the next incident.

#### Verify a repair rather than merely deploy it

For a stale-cache cause, test the complete source-update-to-UI path, not just the cache TTL setting. For a duplicated join, compare shipment IDs before/after and run boundary cases. Add a regression fixture from the real discrepancy and a freshness alert tied to the user's tolerated delay.

Run the repaired metric alongside the agreed source on representative shifts. Track which cases reconcile, which remain unexplained and whether any metric definition changed. If fixing a definition changes historical numbers, communicate that change rather than portraying it as an invisible bug fix.

> **Interview move:** “My first deliverable is a verified explanation for one harmful discrepancy, with its scope. My second is a corrected slice that reconciles under the agreed definition and visibly reports stale data.”

#### Changed requirement and senior evidence

If the customer now asks for multiple warehouses, preserve the same metric contract but add region/timezone/source coverage to validation. A single warehouse's source adapter does not establish global correctness. If they want the dashboard to trigger actions automatically, freshness and reconciliation become action eligibility requirements, with explicit stop behavior.

Basic evidence is a plausible cause list. Strong evidence is a reproducible trace and verified repair. Senior evidence separates facts from hypotheses, assigns owners, defines historical uncertainty and proves the served output and user decision are corrected.

<a id="q86"></a>
## 86. Scope shipment rerouting using SAP, weather APIs, and 500 managers

### 1. Understand the decision

Ask what disruption triggers rerouting, who owns the shipment, which constraints are hard, what a wrong reroute costs, what managers currently do, and whether we recommend or execute. Clarify SAP read/write access, carrier APIs, stock/capacity, delivery commitments, and weather freshness.

Success is improved operational outcomes at acceptable cost and risk, not merely a high count of agent actions. Establish the current baseline with ops.

### 2. Draw a bounded workflow

```text
SAP shipment state + weather + carrier/warehouse constraints
                              |
                      detect disruption
                              |
                 generate feasible route options
                              |
               validate cost, capacity, delivery rules
                              |
              recommendation + evidence + expiry
                              |
                    manager approves revision
                              |
                  revalidate current conditions
                              |
                 execute using stable operation key
                              |
                 confirm outcome / reconcile unknown
```

> **Explanation:** An LLM can interpret a manager's request or explain options. A routing solver and deterministic checks may be better for feasibility and optimization. “AI agent” is not a reason to let a model invent capacity or delivery constraints.

### 3. Model the important state

Use `Shipment`, `Disruption`, `RerouteProposal`, `Approval`, and `ExecutionAttempt`. A proposal stores route terms, cost, evidence timestamps, version, and expiry. An approval binds to that exact version. The manager sees what changes and why.

```text
Proposed -> Approved -> Revalidated -> Executing -> Confirmed
                 |            |             |
                 |            +-> Expired   +-> Unknown -> Reconcile
                 +-> Withdrawn
```

> **Correctness:** Approval of a $200 route must not authorize a later $500 route. If capacity, cost, or terms change, create a new proposal and get approval again. A timeout during execution requires outcome reconciliation before retrying.

### 4. Deliver in phases

1. Historical analysis: confirm data coverage and label decision outcomes.
2. Shadow mode: generate recommendations without affecting shipments.
3. Recommendation-only pilot: one region/workflow, managers approve every action.
4. Limited execution: only well-defined cases meeting evidence and operational gates.
5. Broader rollout: expand with ops ownership, training, rollback, and incident procedures.

500 managers imply identity, role/region permissions, assignment rules, audit trails, and adoption support. It does not by itself imply 500 concurrent requests; ask for traffic patterns.

Measure constraint violations, manager overrides and reasons, decision time, reroute cost, delivery outcomes, and feed freshness. Historical comparisons inform feasibility; a controlled operational pilot is needed to establish real improvement.

### 5. Failure handling and answer

Stale weather or SAP data should suppress execution or mark recommendations as stale. An unavailable carrier leaves a proposal unconfirmed. Preserve the current process as fallback and make manager override explicit.

> **Say it aloud:** “I separate detecting a disruption, proposing a feasible reroute, and committing the change. I start with grounded recommendations and manager approval. Approval binds to immutable terms, execution revalidates freshness and constraints, and unknown API outcomes are reconciled. I expand only after measuring operational value and failure behavior in a bounded pilot.”

**Follow-up:** Would you build a multi-agent system? Only if independent responsibilities justify it. Begin with one explicit workflow and typed tools; extra agents add coordination and evaluation cost.

### Design derivation: propose, authorize, commit, and reconcile are separate steps

#### Clarify the hidden business rules

**You:** “May a manager reroute any shipment?” **Interviewer:** “Only shipments in their region.” That implies authorization at proposal access and execution, not merely a region filter in the UI.

**You:** “Is accepting a route a recommendation or a carrier commitment?” **Interviewer:** “It commits capacity and cost.” Now immutable terms, current availability, durable execution ownership and outcome reconciliation are required.

**You:** “Can we change an approved proposal?” **Interviewer:** “Not without reapproval.” That makes proposal revision part of the domain model.

#### Derive records and operations from rules

| Record/component | State | Operation/rule |
|---|---|---|
| Shipment snapshot | Current route, owner/region, version | Read authoritative current state |
| Disruption evidence | Weather event, severity, timestamp | Decide whether evidence is fresh enough |
| Proposal | Route, cost, constraints, revision, expiry | Present exact terms and explanation |
| Approval | Approver, proposal revision, time | Bind consent to specific terms |
| Execution | Operation key, state, provider reference | Claim, submit, confirm or reconcile |
| Workflow coordinator | Current proposal/execution identifiers | Enforce legal transitions |

```text
readShipment(id) -> versioned snapshot
propose(snapshot, evidence) -> proposal revision
approve(proposal_id, revision, manager) -> approval
execute(approval) -> confirmed | rejected | unknown
reconcile(operation_key) -> authoritative outcome or still unknown
```

> **Explanation:** A proposal is data describing an intended change. Approval is authority to make that specific change. Execution is the attempt to cause it. Keeping them separate makes auditing and failure recovery possible.

#### Compare execution choices

**Model directly calls rerouting API:** low friction, but no reliable boundary around changed terms, permissions or repeated execution. **Manager clicks approval and we submit immediately:** better authority, but can still commit stale terms or duplicate after a timeout. **Versioned approval plus revalidation and durable execution claim:** preserves the binding between consent and the action; costs additional state and recovery logic.

The recommendation may use an LLM for explanation, but it should not manufacture factual availability. Feasibility checks and provider terms come from controlled data/services. If the provider can hold capacity, use the hold's expiry contract; if it cannot, identify the race between checking and booking and how the provider rejects or confirms changed availability.

#### Walk the core execution pseudocode

```text
execute(approval):
    authorize manager and verify approved proposal revision
    reject expired/withdrawn proposal
    re-read shipment and validate expected version
    validate current cost/capacity/evidence according to provider contract
    atomically claim logical execution using a stable key
    if already confirmed: return saved result
    if pending/unknown: return state or reconcile, do not resubmit blindly
    submit with provider idempotency key / hold reference if supported
    on definitive rejection: record rejection
    on confirmed success: persist provider reference and result
    on timeout: record unknown and schedule reconciliation
```

If the provider lacks atomic conditional booking or idempotency, acknowledge the weakened guarantee and narrow automation accordingly. A local proposal table cannot eliminate external races by itself.

#### Verify two managers and a lost response

```text
Manager A approves proposal P7/revision 2
Manager B attempts a conflicting change for the same shipment
Coordinator checks shipment version and execution ownership
Only the valid owner proceeds under the agreed concurrency policy

Provider completes A's reroute; response is lost
Execution becomes UNKNOWN
Retry worker queries provider using operation reference/key
Confirmed outcome is stored; B's stale proposal must be revised
```

> **Correctness:** “Unknown” is not “failed.” Treating every timeout as failure can reserve capacity twice or reroute a shipment a second time.

#### Work an extension: allow eligible automatic actions

Add a deterministic eligibility policy evaluated against current data and a policy version. It substitutes an explicitly authorized policy for per-action human approval only for its permitted cases. Keep the same proposal terms, execution claims and reconciliation. Evaluate the new authority boundary; do not remove recovery merely because the action is automatic.

For scale, ask about event volume, active disruptions and provider quotas. Partition work by shipment/region where appropriate; bulk weather outages can trigger many recommendations at once. Bound work, deduplicate triggers and give managers a usable queue rather than hundreds of duplicate alerts.

Basic evidence: a plausible recommendation pipeline. Strong: approval, constraints and monitoring. Senior: immutable consent, concurrency and external-provider guarantees, recovery from unknown effects, and rollout based on observed outcomes.

<a id="q87"></a>
## 87. Choose between prompting, RAG, fine-tuning, and an agent

### 1. Classify the missing capability

Ask what inputs/outputs are required, whether knowledge changes, whether citations matter, whether actions are necessary, what examples exist, and where the current baseline fails.

```text
What is missing?
    |
    +-- clear instructions / output structure -> prompting + validation
    +-- external or changing knowledge ------> retrieval / live data tools
    +-- repeatable task behavior ------------> evaluate fine-tuning
    +-- multi-step state and actions --------> bounded workflow / agent

These can be combined. They are different design dimensions.
```

> **Explanation:** RAG changes what evidence is available at request time. Fine-tuning changes learned behavior. An agent changes how the system chooses and performs steps. They are not four interchangeable upgrades on one ladder.

### 2. Work through examples

| Customer need | Starting point | Why |
|---|---|---|
| Extract fields from a short supplied invoice | Prompt + structured schema + validation | The input already contains the evidence |
| Answer questions about changing internal policies | Permission-aware RAG with citations | Knowledge must be refreshed and traceable |
| Classify thousands of tickets into a stable taxonomy | Prompt baseline; compare fine-tuning | Repeated behavior may justify training investment |
| Read a shipment, assess options, submit an approved change | Explicit workflow with typed tools | Needs state, external actions, and recovery |

For structured operational facts such as account balance or live availability, query the system of record through a controlled tool. Embedding search is not always the right data access mechanism.

### 3. Run an evidence-based comparison

Build representative examples covering common cases and expensive mistakes. Start with a simple baseline and measure correctness, latency, cost, and operator workload. Inspect errors: missing facts require better evidence; inconsistent classification might need examples or tuning; broken tool execution needs workflow engineering.

> **Pitfall:** Fine-tuning is not a dependable live database. It does not guarantee factual answers or remove the need for evals. RAG also does not guarantee correctness: retrieval and generation can each fail.

Use an agent when the task needs adaptive step selection, not merely because it contains several fixed steps. A deterministic workflow is easier to audit for a known sequence. Bound tool access, iterations, duration, and spend either way.

### 4. Follow-ups and interview answer

If customer data cannot leave its environment, deployment and model choices are constrained before quality comparisons. If labelled examples are scarce, improve the baseline and collect reviewed data before promising fine-tuning. If decisions have side effects, add authorization and approval independently of the model choice.

> **Say it aloud:** “I identify whether the gap is instructions, evidence, stable behavior, or execution. I start with a measured baseline and improve the component responsible for its failures. I use retrieval for changing knowledge, evaluate tuning for repeatable tasks, and add bounded agency only when adaptive actions are needed. Security and approval remain application responsibilities.”

**Recall check:** A model knows the policy but repeatedly submits duplicate changes. Would more RAG fix it? No; improve execution idempotency and workflow state.

### Decision derivation: use error evidence to select the intervention

#### Define an evaluation contract first

Choose a real task, such as answering shipping-policy questions for support staff. Collect representative cases with expected evidence, permissible answers, exceptions and unsupported cases. Fix the evaluation set and success dimensions before comparing approaches. Keep holdout cases separate from tuning examples.

```text
Observed failure
     |
     +-- correct fact absent from context -> retrieval / live lookup
     +-- fact present but output wrong ---> prompt/examples/model behavior
     +-- decision correct, action broken -> workflow/tool contract
     +-- correct but too slow/expensive --> optimize measured hot path
```

> **Explanation:** A technique should respond to a diagnosed gap. Adding all four techniques at once makes it difficult to know what improved the result or caused a regression.

#### Compare the controls and their costs

| Choice | What you control | Added lifecycle | What it does not solve |
|---|---|---|---|
| Prompt/context | Instructions and examples at request time | Versioning and regression evaluation | Missing inaccessible facts or safe external actions |
| RAG | Evidence selection from maintained sources | Ingestion, permissions, deletion, retrieval quality | Guaranteed interpretation or live transactional truth |
| Fine-tuning | Learned behavior on task examples | Dataset quality, training, holdout evaluation, version deployment | Automatically refreshed knowledge or execution authority |
| Agent/workflow | Step selection and external tool use | State, limits, recovery, authorization, traces | Reliable facts without good tools/evidence |

A prompt might be the correct baseline for extraction while a smaller tuned classifier wins later at high volume. RAG may add no value for a short document already passed in full. An agent can combine retrieval and a tuned component without changing who authorizes actions.

#### Work a small diagnostic experiment

Suppose the baseline gets 100 expert-reviewed policy cases: 20 wrong answers lack the necessary policy passage, 8 misread a passage that was available, and 5 need live order facts unavailable in documents. These are illustrative categories, not performance claims.

1. Test retrieval fixes for the 20 evidence gaps and check whether retrieved sources are authorized/current.
2. Test clearer instructions/examples or a model comparison for the 8 interpretation errors.
3. Add a controlled order lookup for the 5 live-data cases, or abstain if access is not permitted.
4. Reevaluate all cases, not just the previously failed subset; improvements can introduce regressions elsewhere.

> **Correctness:** Selecting architecture on a few cherry-picked examples overstates progress. Evaluate common traffic, expensive mistakes, unsupported cases, latency and cost together. Report uncertainty when the sample is small.

#### Derive interfaces if the interviewer asks for design

```text
AnswerService.answer(user, question)
    -> EvidenceSource.fetch(user, question)  [permissions enforced]
    -> Generator.generate(question, evidence)
    -> OutputValidator.check(answer, evidence)
    -> answer with support / abstention / review state

Workflow execution is a separate authorized contract if actions are added.
```

These boundaries let you compare evidence and generation independently. Do not make a `TechniqueFactory` that randomly selects prompting/RAG/fine-tuning/agent for every request unless explicit routing requirements justify it. They are design decisions, not a menu of interchangeable algorithm objects.

#### Handle changed requirements

If citations become mandatory, the output contract needs source identifiers and support checks; tuning alone does not supply evidence provenance. If policies update hourly, the source-refresh and cache contracts become critical. If the customer needs automatic refunds, add a separate authorized execution path and idempotency. If data residency constrains deployment, eliminate infeasible providers before comparing accuracy.

Basic evidence: describe techniques accurately. Strong: map need to mechanism and measure a baseline. Senior: localize failures, compare whole-system cost/quality, avoid overtraining on holdouts, and maintain independent knowledge and execution boundaries.

<a id="q88"></a>
## 88. A city wants to reduce emergency-response times: scope it in 60 minutes

### 1. Clarify what the hour is for

Treat the 60 minutes as a discovery/design exercise, not a promise to deploy an emergency system in an hour. Ask which segment of response time is slow, how it is measured, which agencies and users are involved, and what dispatch constraints already exist. This walkthrough proposes engineering discovery, not clinical or jurisdiction-specific operating rules; those must come from the city's qualified owners.

```text
Call received -> call assessed -> unit dispatched -> unit travels -> arrival
      |               |                 |                |
      +-- handling ---+-- dispatch -----+--- travel ------+

Which segment drives delay? Different segments require different changes.
```

> **Explanation:** GPS and traffic data help travel/assignment decisions. They do not automatically solve slow call handling or unavailable crews. An overall average can hide a severe delay in one neighborhood or call category.

### 2. Sequence the hour

| Minutes | Output |
|---|---|
| 0–10 | Agree on response-time definition and the operational problem |
| 10–20 | Map current dispatcher workflow, authority, and fallback |
| 20–35 | Assess timestamps, GPS freshness, unit availability, and traffic feeds |
| 35–50 | Design one decision-support slice and its failure behavior |
| 50–60 | Agree on validation, owners, dependencies, and go/no-go conditions |

### 3. Design a decision-support baseline

```text
Incident details + eligible unit status + GPS age + traffic estimates
                                |
                       eligibility constraints
                                |
                      rank feasible options
                                |
              recommendation + evidence + uncertainty
                                |
                      dispatcher decides
                                |
             existing dispatch system + audit record

Stale/missing critical feed -> explicit degraded state -> existing process
```

Do not assume the nearest unit is eligible: capability, current assignment, staffing, and coverage constraints matter. Let operational experts define those constraints. A routing/optimization baseline may be sufficient; an LLM is not a prerequisite.

> **Correctness:** “Human in the loop” is incomplete if the operator cannot see data age, inspect the reason, override quickly, or continue without the tool. Design the review interaction and fallback, not merely an approval button.

### 4. Validate before live influence

Inspect historical timestamps and missingness; replay decisions using only information available at that moment. Compare feasible options with expert review, then evaluate in shadow mode. Historical replay can estimate routing behavior but cannot prove a counterfactual improvement in real response times; controlled operational evaluation needs the city's approval and safeguards.

Measure response segments and tail latency, recommendation delay, stale-feed rate, ineligible-unit suggestions, operator overrides, and performance across relevant regions/categories. Agree on unacceptable failures and stop criteria with the accountable owners.

> **Pitfall:** Reporting a faster average while worsening the slowest responses is not enough. Likewise, comparing with future-known traffic leaks information into the retrospective evaluation.

### 5. Interview answer and follow-up

> **Say it aloud:** “I first split response time into handling, dispatch, and travel so we target the actual bottleneck. I map dispatcher authority, available units, feed freshness, and constraints. I propose one decision-support slice with transparent recommendations and the existing process as fallback. Historical replay and shadow evaluation establish feasibility; operational owners decide the conditions for any live pilot.”

**Follow-up:** What if leadership insists on full automation? Explain which failure guarantees and operational controls are unproven, propose the bounded slice, and ask the accountable operations/safety owners to define the acceptance gate. Do not invent an acceptable risk threshold yourself.

### Case derivation: from response-time goal to a bounded experiment

#### Clarification changes the proposed system

**You:** “Is most delay before dispatch or during travel?” **City owner:** “We suspect travel, but do not yet have a reliable segment breakdown.” Your first deliverable is validating timing evidence; a routing product is still a hypothesis.

**You:** “Does GPS position imply availability?” **Dispatcher:** “No, a unit may be assigned or unsuitable.” An eligibility service/contract is needed before distance ranking.

**You:** “Who makes the operational decision?” **Owner:** “The dispatcher.” The interface supports their decision and records override reasons. This does not authorize autonomous dispatch.

> **Explanation:** A good case answer can conclude that the next step is data validation, not model development. That is progress because it avoids spending effort on an unverified bottleneck.

#### Derive data and rule ownership

| Requirement | Evidence/state | Accountable owner |
|---|---|---|
| Know which segment is slow | Consistent event definitions and timestamps | Operations + data owners |
| Suggest eligible units | Capability, assignment and status | Dispatch operations |
| Rank feasible travel options | GPS age, traffic time, route estimate | Integration/routing component |
| Preserve human authority | Suggestion, evidence and override | Dispatcher workflow |
| Continue during failure | Existing procedure and visible degraded status | Operational owner |

An `IncidentSnapshot` groups known incident facts. A `UnitSnapshot` groups eligibility and position/version. A `Recommendation` contains feasible alternatives and the evidence time. This supports an inspectable interface without pretending we design the city's entire dispatch domain in an hour.

```text
recommend(incident_snapshot, eligible_unit_snapshots, traffic_snapshot)
    -> options + evidence ages + excluded-option reasons

This function proposes; the existing dispatch workflow commits.
```

#### Compare baselines and avoid a misplaced model

**Closest by straight-line distance:** cheap and explainable, but can ignore roads, eligibility and traffic. **Shortest estimated travel time among eligible units:** a stronger deterministic baseline, still dependent on current input quality and coverage constraints. **More complex prediction/optimization:** may improve estimates, but requires data and evidence that it beats the baseline under actual operating rules.

Start with the smallest comparison that can change a decision. An LLM explaining a route does not fix a wrong ETA or unavailable crew. Separate user presentation from route feasibility.

#### Verify a failure trace

```text
Incident I1 arrives
Unit A looks closest; GPS age is beyond the agreed limit
Unit B is farther; location fresh, but already assigned
Unit C passes freshness and operational eligibility

System does not silently treat A/B as valid options.
It presents C with evidence and makes missing coverage visible.
If no candidate passes, it returns no reliable recommendation,
and the dispatcher continues using the agreed existing procedure.
```

> **Correctness:** A fallback is a known operational process, not “ask the LLM for its best guess” when critical feeds are missing. The exact degraded behavior belongs to the city's approved workflow.

#### Work the evaluation extension

For historical replay, align all source snapshots to the decision time and audit missing/late records. For shadow evaluation, preserve recommendations without influencing dispatch and have experts review errors. For live influence, agree on training, observability, escalation and stop conditions with accountable owners. Data analysis alone does not authorize operational deployment.

Examine distributions by time/region and relevant call classes, not only averages. A faster recommendation computation may have no value if unit availability is the bottleneck. State that causal outcome improvement requires an appropriate operational evaluation, not just lower model error.

Basic evidence: identify users/data and a plausible solution. Strong: separate response segments and show eligibility/freshness behavior. Senior: prove information availability, retain decision authority, expose counterfactual limits and tie rollout to operational acceptance.

<a id="q89"></a>
## 89. Unify fraud detection across three acquired systems in 90 days

### 1. Define the outcome and the ambiguity

Ask whether the first goal is detecting more fraud, reducing customer friction, reducing analyst workload, or consolidating operations. Clarify units of decision (transaction/account), latency, existing rules, who reviews alerts, and how labels become final.

```text
System A: fraud = disputed transaction
System B: fraud = analyst suspicion
System C: fraud = confirmed chargeback
                         |
                 These are not equal labels
                         |
                agreed label definitions
                         |
                unified evaluation cohort
```

> **Explanation:** One system's positive label might mean “suspected,” while another's means “confirmed.” Pooling them without reconciliation trains and evaluates against inconsistent targets. Unlabelled transactions are not automatically confirmed negatives.

### 2. Design the data and decision path

```text
3 systems -> raw staging -> source-specific normalization
                                  |
                      identity + label reconciliation
                                  |
                   versioned decision-time feature set
                                  |
                   baseline rules / candidate model
                                  |
                unified analyst queue + explanation
                                  |
                   reviewed outcomes + feedback
```

Preserve source labels, evidence, event times, label-finalization times, and mapping versions. Keep customer/account identity mapping explicit. Bring the bank's security, compliance, and risk owners into discovery; exact obligations depend on their operating context and require their determination.

### 3. Sequence the 90 days

| Period | Concrete deliverable | Gate |
|---|---|---|
| Days 1–30 | Source/access map, label glossary, one reconciled cohort, quality report | Risk/analyst owners accept definitions and identify unresolved labels |
| Days 31–60 | One decision slice, baseline comparison, shadow results, analyst feedback | Evidence supports the agreed quality/workload trade-off |
| Days 61–90 | Controlled integration, monitoring, recovery, operational handoff | Data coverage, review capacity, auditability, and rollback pass |

> **Correctness:** A feature must have been available at transaction time. Using a later chargeback outcome as an input leaks the answer. Time-based evaluation should reflect delayed labels and changing conditions.

### 4. Measure and handle failure

Compare precision/recall at an agreed operating point, false positives by relevant segment, loss/cost estimates, alert volume relative to analyst capacity, decision latency, and data completeness. Estimate business impact with assumptions rather than translating offline accuracy directly into saved money.

If one source has weak labels, retain uncertain examples separately and use expert adjudication or a narrower cohort. If integration is delayed, keep existing detection active and pilot the agreed slice without silently removing protection. Do not automatically block transactions until the bank's owners approve that behavior.

> **Pitfall:** An excellent detector that produces more alerts than analysts can process can worsen operations. Queue capacity and review policy are part of the design.

### 5. Interview answer and follow-up

> **Say it aloud:** “The first dependency is agreeing on what fraud means across the three systems. I preserve original labels, reconcile a narrow cohort, and prevent future information from leaking into features. I compare against current rules, run a shadow slice with analysts, then harden integration and recovery. The 90-day plan has evidence gates rather than an unconditional model-launch promise.”

**Follow-up:** What if label reconciliation takes longer than 30 days? Narrow the first cohort to cases with accepted evidence, make the schedule impact explicit, and continue independent work on adapters, queue integration, and auditability.

### Case derivation: the shared target matters more than a shared model

#### Turn the three-system problem into explicit contracts

**You:** “What event turns a transaction into confirmed fraud?” **Risk team:** “Our acquired systems disagree.” That means `fraud=true` cannot yet be treated as one stable supervised target.

**You:** “How late can labels become final?” **Analysts:** “Some outcomes arrive long after the transaction.” Evaluation needs mature cohorts and an explicit unknown state.

**You:** “Do we alert, block, or rank for review?” **Owner:** “Start with ranking a unified analyst queue.” This narrows the first behavior and avoids silently changing transaction-blocking authority.

> **Explanation:** You can unify source observations and the review workflow before every source supports the same model. A single score on incompatible labels can hide disagreement rather than resolve it.

#### Derive a usable record model

```text
TransactionObservation
  source + original ID + canonical mapping
  event time + availability time + source fields

LabelObservation
  original label + evidence + label time + mapping version
  state: confirmed / suspected / unresolved / reviewed-negative

ReviewCase
  related transactions + reasons + score/rule version
  assigned analyst + disposition + disposition evidence
```

Source adapters own extraction, identity mapping owns entity joins, label mapping records the agreed definitions, and detection/ranking consumes decision-time features. Analysts own final dispositions under the bank's policy. Preserve provenance when labels are corrected; a training dataset version should be reproducible.

#### Compare integration approaches

**Union all rows and train one model:** fast but potentially incoherent labels and features. **Keep three independent detectors and combine alerts:** useful as an interim baseline, but duplicates/workflow fragmentation remain. **Reconcile a narrow cohort and unify review with measured detection:** produces comparable evidence and limits risk; requires upfront definition and data work.

A staged answer can use the second as baseline while building the third. Explain why you are not discarding working protections before a replacement is verified.

#### Trace leakage and review capacity

```text
Transaction at day 0
Chargeback evidence at day 30
Fraud confirmed at day 45

Features for day-0 decision: only facts available on day 0
Label for mature offline evaluation: may use confirmed day-45 outcome
Unresolved day-2 transaction: not automatically a negative
```

For workload, suppose a candidate policy produces 5,000 alerts/day and the team can meaningfully review 500. Even with good recall, the workflow can fail. Compare operating points and queue prioritization; quantify missed-case trade-offs with the risk owners rather than maximizing one model metric in isolation.

> **Correctness:** A model may reduce false positives in aggregate while worsening a segment with different source coverage. Validate relevant segments and missing-feature paths before presenting a single headline result.

#### Make the 90-day plan conditional and reviewable

Each phase should end with an artifact: approved label glossary, reconciled cohort/quality report, baseline/shadow comparison, or an operational runbook and readiness decision. Name the critical access and expert-review dependencies. If a gate fails, state which scope or date changes and which independent work continues.

For a new acquisition, onboard its observations first, compare label semantics and feature availability, and test queue deduplication. Do not assume a fourth source inherits the same quality simply because its fields have familiar names.

Basic evidence: a phased plan. Strong: label definitions and workflow capacity. Senior: decision-time availability, delayed-label evaluation, source-specific coverage, unchanged protections during transition and auditable phase gates.

<a id="q90"></a>
## 90. Summarize 30 million insurance claims across jurisdictions

### 1. Define who uses the summary

Ask whether adjusters, reviewers, or customer-service staff read it; what decision it supports; what facts must be present; whether readers can inspect the source; how claims change; and which jurisdictions/lines of business are in scope. Determine applicable handling and review requirements with the insurer's compliance owners rather than guessing state rules.

Thirty million is a corpus size, not a request rate. Ask what fraction needs processing, whether summaries are generated on demand or in bulk, and which updates invalidate them.

> **Explanation:** “Short and readable” is insufficient when a missing date, exclusion, or contradictory document changes a decision. Define a summary rubric with claims experts before picking a model.

### 2. Draw the flow

```text
Authorized claim + jurisdiction/workflow policy
                         |
                 collect permitted documents
                         |
               OCR / parsing + source versioning
                         |
               extract material facts + evidence
                         |
                  draft structured summary
                         |
            completeness / contradiction checks
                         |
               expert review when required
                         |
           summary + source links + version + audit
```

For one claim, fetching its full bounded document set may be better than generic top-k retrieval. Long claims can need hierarchical extraction and summarization, with each statement linked to source evidence.

### 3. Define the output and evaluation

An illustrative summary includes incident/timeline, parties, claimed loss, evidence, unresolved conflicts, and missing documents. Required fields come from the insurer's rubric. Retain claim/document versions, model/template versions, reviewer decisions, and source citations.

```text
Claim source v7 -> summary v7 -> reviewed
Claim source v8 -> old summary marked stale -> regenerate/review
```

> **Correctness:** A citation can point to a document that does not support the statement. Evaluate citation support, factual fidelity, material omissions, and contradiction handling separately. A model-generated confidence score is not sufficient evidence of correctness.

### 4. Sequence and estimate scale

Start with one line of business, jurisdiction, and user workflow. Build an expert-reviewed evaluation set including long/poorly scanned/conflicting claims. Compare with existing practice, then shadow and pilot. For backfill, use queues, bounded concurrency, checkpointed per-claim jobs, and versioned idempotent outputs.

Estimate tokens per claim, retry/review rate, throughput, storage, and cost before promising full-corpus processing. Prioritize claims with actual demand. Use human-reviewed quality gates before increasing coverage; keep original documents available for decisions.

> **Pitfall:** Grounded summarization does not mean every claim needs a vector database. Nor does a successful batch job mean its summaries are faithful. Measure output quality and job completion separately.

### 5. Failures and interview answer

Low-quality OCR should surface uncertainty or trigger review. Conflicting evidence should remain visible rather than being resolved by plausible prose. Source updates invalidate summaries. Failed jobs enter a recoverable state without silently publishing partial output.

> **Say it aloud:** “I start with the reader's decision and a claims-expert completeness rubric. I produce evidence-linked, versioned summaries from permitted documents and preserve uncertainty. I prove one workflow and jurisdiction with expert evaluation, then scale through bounded, resumable processing. Compliance owners determine the handling and review requirements.”

**Follow-up:** How do you handle deletion? Trace source-to-summary lineage, apply the approved retention/deletion policy across derived data and raw storage, and verify the resulting access state.

### Design derivation: evidence completeness, versions, and publication

#### Clarify output meaning before scaling

**You:** “What must an adjuster never miss?” **Claims expert:** “Material dates, stated loss, exclusions relevant to this review, and contradictory accounts.” Those become rubric dimensions and structured output fields, not a vague instruction to be accurate.

**You:** “Should the summary settle conflicting statements?” **Expert:** “No, identify them.” The output includes unresolved contradictions rather than choosing whichever story sounds most plausible.

**You:** “Are all 30 million claims requested now?” **Owner:** “No, most are archival.” Prioritize demand and evaluate a backfill separately; corpus size does not justify processing all records immediately.

> **Explanation:** A summary is a derived view of evidence at a version. The system must distinguish “no fact exists,” “parsing failed,” and “the generator omitted a fact.” Those require different corrective actions.

#### Derive ownership and interfaces

| Component | Stored/returned information | Rule it owns |
|---|---|---|
| Claim access layer | Authorized document set and versions | Only permitted sources enter the job |
| Parser/extractor | Text, extraction status, source locations | Parsing failure remains visible |
| Fact collector | Facts with supporting spans and conflicts | Evidence availability and provenance |
| Summary generator | Structured draft with source links | Output format and bounded generation |
| Reviewer/validator | Material-fact checks and review disposition | Publication gate |
| Summary store | Source/model/template/policy versions | Reuse only under a valid version/access contract |

```text
summarize(claim_id, authorized_context, source_version)
    -> draft + supporting evidence + missing/conflicting items

publish(draft_id, review_result, expected_source_version)
    -> published version | stale-source rejection
```

If the source changes between generation and publication, apply the agreed stale-result policy. Reusing a cached summary must still check current authorization; permission at generation time is not permission forever.

#### Compare evidence strategies

**One prompt with every document:** simple for a small bounded claim, but can exceed context or bury material facts. **Top-k retrieval:** useful for focused questions, but a generic summary can omit rare important facts that were not retrieved. **Structured extraction followed by evidence-linked synthesis:** improves inspectability and coverage tracking for large claims, but adds passes, costs, and compound errors.

Choose using claim lengths and the rubric. Evaluate extraction recall separately from synthesis fidelity. A flawless synthesis cannot include evidence its extractor missed.

#### Verify a source-update trace

```text
Source claim version 7 includes two incident accounts
Extractor identifies their disagreement
Draft includes both accounts with citations and an unresolved flag
Reviewer accepts the representation

Before publication, a new document creates source version 8
Publisher detects version mismatch
It does not label the v7 draft as current without the agreed policy
Regenerate or explicitly publish a versioned historical summary
```

> **Correctness:** Model, prompt and source versions answer different audit questions. Source version tells you which evidence was available; template/model versions tell you how it was processed; review history tells you who accepted it.

#### Work the large-scale extension

A job identity can combine claim ID, source version, summary-spec version and processing configuration. Retry the same logical job safely, store per-stage progress, and avoid publishing a half-complete result. Bound concurrent provider calls and review queues. For long documents, checkpoint extraction stages so a final-stage failure does not require rereading everything.

Estimate `claims_to_process × average_tokens_per_claim × token_cost`, then add retries, extra extraction passes and review effort. Add a separate latency estimate using achievable throughput under quotas. These are planning assumptions to validate on a representative sample, not proof from a model's advertised limits.

Basic evidence: summarize with grounding and review. Strong: define material completeness and evidence-linked output. Senior: layered error diagnosis, current authorization, version-safe publication, demand-based processing and resumable scale.

<a id="q91"></a>
## 91. Your deployment slipped three weeks: tell the CTO

### 1. Understand the conversation

The CTO needs an accurate impact assessment and a decision, not a recital of engineering activity. Establish the verified cause, what changed, what remains uncertain, business impact, and available recovery options before speaking.

```text
Missed date -> business impact -> verified cause -> recovery choices
                                                   |
                                      owner + next evidence checkpoint
```

> **Explanation:** Ownership means telling the truth early, explaining what you control, and making the recovery plan inspectable. It does not mean blaming yourself for facts you have not established or blaming another team.

### 2. Prepare a concrete example

Assume the pilot was expected October 7 and the current estimate is October 28 because end-to-end identity integration took longer than planned. Treat these as illustrative facts. Know whether the delay estimate is validated, which tasks are on the critical path, and what milestone would increase confidence.

Separate three things: the original commitment, the current forecast, and the next date on which evidence will improve the forecast. Do not turn an uncertain estimate into another unconditional promise.

### 3. Deliver the answer

> **Say it aloud:** “The current deployment forecast is three weeks later than the date we committed to. That delays the operations pilot and its planned benefits. The critical issue is identity integration, and I underestimated the time needed to validate it end to end. I should have raised that risk earlier.
>
> “We have two concrete options: keep the agreed scope and target the revised date, or reduce the initial pilot to the user group we can securely support sooner. I recommend the smaller pilot if it still answers the agreed business question. I will confirm that with the ops owner rather than treating any launch as success.
>
> “I own the recovery plan. The next checkpoint is a working identity-to-application flow, after which I will update the forecast and remaining risks. I will send a short progress update at the agreed cadence and escalate immediately if the critical path changes.”

### 4. Explain why it works

You lead with impact, give a verified cause, acknowledge a planning miss, offer options with consequences, and establish accountability. Replace all sample facts with real evidence if using this in an actual incident.

> **Pitfall:** “We are working hard and should be done soon” provides no decision or evidence. Adding people does not automatically shorten a dependency-bound critical path.

### 5. Follow-ups

- **“Why should I trust this date?”** Show completed work, remaining dependencies, owners, and the checkpoint that validates the forecast; state uncertainty plainly.
- **“Launch now.”** Explain which acceptance condition is unmet and what narrower verified release is possible. Do not conceal a failed control to meet a date.
- **“How will this not recur?”** Add earlier end-to-end dependency validation and explicit milestone risk reviews; tie the change to the actual cause.

**Recall check:** What should the CTO know after one minute? Impact, cause, choices, recommendation, ownership, and when the next useful evidence arrives.

### Conversation derivation: prepare the facts, then handle the CTO's decisions

#### Build the evidence behind the opening

| Fact to gather | Why it changes the conversation |
|---|---|
| Which milestone slipped | A blocked pilot differs from a blocked full rollout |
| Critical-path evidence | Separates a real dependency from a vague excuse |
| Business commitments affected | Shows the consequence the CTO must manage |
| Remaining tasks, owners and uncertainty | Determines credibility of the revised forecast |
| Smaller scope with verified readiness | Determines whether an earlier release is meaningful |
| Customer/support communication already sent | Avoids conflicting messages |

Do not state “three weeks” simply because someone added three weeks to the old date. Link the forecast to remaining work and dependencies. If confidence is low, state what must be demonstrated before confirming it.

> **Explanation:** A forecast describes the current best estimate. A commitment allocates responsibility around agreed conditions. Mixing them creates another trust problem when uncertainty resolves badly.

#### Compare response strategies

**Hide the issue until certain:** preserves apparent progress temporarily but removes the CTO's ability to change scope or commitments. **Blame security/customer engineering:** may name a dependency but avoids your responsibility for planning and escalation. **Report impact, evidence and choices early:** supports a real decision and makes recovery inspectable.

```text
CTO: "I need the original date."
You: "That requires changing scope or accepting unmet criteria.
      This smaller user group has passed the identity checks;
      the wider group has not. Does the smaller pilot still
      meet the business milestone?"

CTO: "Will it definitely be ready in three weeks?"
You: "That is the current forecast, conditioned on these dependencies.
      This checkpoint will verify the remaining integration risk.
      I will update you when that evidence changes."
```

#### Verify that the conversation produced an outcome

The CTO chooses scope or requests more evidence; a named owner updates affected stakeholders; acceptance criteria remain explicit; the recovery checkpoint has a date and observable output. Record the decision and new assumptions. “The CTO seemed reassured” is not a sufficient outcome.

If the remaining work changes again, report the new fact and its consequence. Do not wait until the next scheduled update if the decision is time-sensitive. For a fixed external event, explain what demonstrably ready capability can be used then and what follows later.

**Level check:** Basic: disclose the delay. Strong: explain impact and realistic options. Senior: evidence-backed forecast, early escalation, explicit trade-off and a prevention change grounded in the actual planning failure.

<a id="q92"></a>
## 92. Explain to a nontechnical VP why RAG cannot guarantee 100% accuracy

### 1. Translate the system into the VP's workflow

Ask what they mean by accuracy and which mistake would be costly. Answering a policy question incorrectly is different from missing a relevant document or citing an outdated version. Avoid an architecture lecture.

```text
Employee asks a question
          |
Assistant finds relevant permitted documents
          |
Assistant writes an answer from those documents
          |
Employee checks evidence / reviewer handles consequential decisions
```

> **Explanation:** Retrieval supplies evidence; generation turns it into an answer. Documents can be incomplete, retrieval can miss the right passage, and the answer can misinterpret what it found. Each is a separate source of error.

### 2. Make the uncertainty concrete

Imagine an old policy says a refund window is 14 days, while a new one says 30 days for a specific customer group. The assistant can fail by finding the old version, missing the exception, or combining both incorrectly. Adding a citation helps inspection, but a citation alone does not certify the claim.

### 3. Offer a controlled business commitment

> **Say it aloud:** “The assistant first finds relevant company documents and then writes an answer using them. That reduces unsupported answers, but it cannot guarantee that the documents are complete, that it finds the right passage, or that it interprets every exception correctly.
>
> “We can make a useful, measurable commitment instead: define the questions it supports, test those questions with your experts, show the evidence behind each answer, and route unsupported or consequential cases to a person. We will also check document freshness and permissions.
>
> “For a contractual or financial decision, the assistant should support the accountable person. We should decide the acceptable error types and review requirements together before expanding its use.”

### 4. Measure and handle follow-ups

Use an expert-labelled set with expected evidence and answers. Measure supported factual claims, relevant-source retrieval, material omissions, and appropriate abstention separately; include real production failures in regression tests.

> **Pitfall:** “It is 95% accurate” is unhelpful without the dataset, definition, and remaining errors. Five harmless formatting issues are different from five wrong eligibility decisions.

- **“Can it just say it is uncertain?”** Yes, but validate abstention behavior. Self-reported confidence is not a reliable correctness test.
- **“Why pay for something imperfect?”** Compare verified task value and review cost with the current baseline, within an explicit scope.
- **“Then can we guarantee no wrong answers?”** Narrow scope and deterministic checks can improve guarantees for specific fields, but do not promise perfect unrestricted language answers.

**Recall check:** Explain the system without saying “embedding,” “vector,” or “reranker.”

### Conversation derivation: translate uncertainty into a service contract

#### Discover the meaning of the VP's request

**VP:** “I need 100% accuracy.” **You:** “Which answers lead to a costly decision, and which are informational?” If the answer is eligibility for a refund, that may require a deterministic policy check plus human-reviewed exceptions. If it is drafting internal replies, evidence-backed suggestions may have useful value with correction.

> **Explanation:** The useful alternative to a universal promise is a precise contract: supported inputs, current evidence, defined review requirements, and measured behavior when the system cannot support an answer.

#### Derive controls from failure types

| Failure | User-visible consequence | Matching control |
|---|---|---|
| Wrong/old source | Obsolete policy answer | Source version/freshness and authority rules |
| Correct source not found | Unsupported or incomplete answer | Retrieval coverage evaluation and abstention |
| Exception misread | Wrong applicability | Expert examples, field checks, review |
| Permission mismatch | Inappropriate disclosure | Enforced source access, not just a prompt |
| Unsupported citation | False appearance of proof | Claim-to-evidence support evaluation |

Do not suggest every failure needs a larger model. Explain that controls target the source of error. Some fields can be computed from a rules engine; the assistant can still explain the verified result.

#### Compare the ways you could respond

**Promise perfection:** easy agreement, impossible to substantiate for unrestricted answers. **Give a jargon-heavy limitation lecture:** technically interesting but leaves the business decision unresolved. **Explain the evidence chain and offer a bounded operating contract:** preserves candor while making useful deployment possible.

```text
VP: "Then why can we trust it?"
You: "By limiting what it is authorized to do, showing its evidence,
      and measuring representative tasks. For this decision,
      a person remains accountable until the specific review
      conditions we agree on are satisfied."

VP: "What result will we get from the pilot?"
You: "A measured quality and review-cost comparison on your cases,
      with the remaining failure types, not just one accuracy number."
```

#### Verify the outcome and work the extension

The VP should be able to explain what users may rely on, what needs review, what happens without sufficient evidence, and which metrics determine expansion. If the requirement becomes “quote the exact latest clause,” narrow generation and validate source selection/version; that is a different contract from general advice.

Basic: acknowledge limitations. Strong: explain separate retrieval/generation failures in plain words. Senior: propose source, review and abstention controls tied to decisions, with an evidence-based acceptance process.

<a id="q93"></a>
## 93. Security will not give you production credentials: unblock yourself

### 1. Understand the restriction

Ask which task requires access, which data or action is needed, what security concern blocks it, and what approved alternatives exist. Production credentials are a means; a verified integration is the goal.

```text
Required task
    |
Minimum evidence or permission needed?
    |
    +-- contract tests ------> sandbox / synthetic fixtures
    +-- data quality --------> approved redacted export / customer-run query
    +-- integration check ---> scoped temporary identity / customer-run test
    +-- deploy --------------> customer's approved pipeline
```

> **Explanation:** You may need to prove an API call works without personally holding broad credentials. A customer engineer can run a reviewed diagnostic or deployment while you inspect approved outputs together.

### 2. Propose a narrow contract

For example: read shipment status from a test tenant, use one endpoint, forbid writes, retain only approved metadata, and expire access after the validation window. Route access through the customer's identity/secrets mechanisms; avoid shared credentials in chats or developer machines.

If a sandbox is available, document gaps: auth, representative data, rate limits, network routes, and error responses. Build adapters and contract tests there, while tracking production-only checks as unresolved acceptance conditions.

### 3. Deliver the answer

> **Say it aloud:** “I do not need broad production access to keep making progress. I would first identify the exact validation that is blocked and ask your security team which approved route fits it. We can build against a sandbox, validate schemas with redacted fixtures, and have your engineers run reviewed diagnostics.
>
> “If a production check is essential, I would request a narrowly scoped, audited, time-limited identity or use your existing deployment pipeline. I would list the remaining production-only acceptance checks so sandbox progress is not mistaken for production readiness. We can then agree on an owner and date for the access decision.”

### 4. Boundaries and follow-ups

If all access is denied, continue useful local work and report the evidence gap plus impact on the milestone. Escalate the dependency through the agreed project owner, without framing security as an obstacle to defeat.

> **Pitfall:** A sandbox success does not prove production DNS, authorization, data coverage, or quota behavior. Also, “read-only” does not remove exposure risk if the data is sensitive.

- **“Use my admin token.”** Ask for the approved scoped route and make the needed permissions concrete.
- **“We have no sandbox.”** Offer customer-run checks and approved representative fixtures; identify what cannot be validated yet.
- **“Can you launch anyway?”** State which acceptance evidence is missing and propose the work that can safely proceed within scope.

**Recall check:** How do you distinguish progress from readiness? Track finished implementation separately from production acceptance evidence.

### Conversation derivation: make the blocked task and approved route concrete

#### Map the request to the minimum evidence

Suppose the blocked task is validating shipment status lookup. You need endpoint behavior, auth scope, sample data, production connectivity and response/error semantics. You do not need unrestricted database administration. Separate which evidence can be obtained in development and which requires a production run.

| Need | Possible approved route | Remaining gap |
|---|---|---|
| Parse representative payloads | Redacted fixtures | May not reflect full production distribution |
| Validate API behavior | Sandbox contract tests | Production auth/network/quotas may differ |
| Confirm network/auth path | Customer-run reviewed probe | You depend on their operator and allowed outputs |
| Observe a real integration | Narrow identity + monitored test | Requires approved access scope and data handling |
| Deploy change | Customer pipeline | Need operational ownership and rollout evidence |

> **Explanation:** Alternatives should answer the actual blocked question. Synthetic fixtures cannot prove production network access, and broad access does not replace a well-designed acceptance test.

#### Compare unblock strategies

**Borrow an administrator's credentials:** appears quick but undermines ownership, audit and permission boundaries. **Wait idle for unrestricted access:** wastes independent implementation opportunities. **Break validation into approved evidence paths:** allows progress and transparently identifies what remains blocked.

```text
Security: "No direct production account for external engineers."
You: "Understood. Can your team run this reviewed read-only probe
      through your identity and share these approved outputs?
      I will document the endpoint, data scope and expected evidence."

Project owner: "Can we still call the integration finished?"
You: "The adapter and sandbox checks are complete. Production
      network/auth validation is still pending; it remains a
      release acceptance condition owned by this team."
```

#### Verify the resolution and changed requirement

A useful resolution names the test, approved executor or identity, scope, owner, planned date and acceptance output. Logs record the relevant access decisions and test results without leaking sensitive data. If a write endpoint becomes necessary, re-scope the request and require a controlled test plan; read-only approval does not authorize writes.

If no permitted route exists, make the dependency's schedule impact concrete and ask the project owner to decide a narrower scope or revised milestone. That is a project decision, not a reason to bypass the customer.

Basic: respect the restriction. Strong: offer specific productive alternatives. Senior: map minimum evidence to permission, keep production gaps explicit and demonstrate readiness through the approved operating path.

<a id="q94"></a>
## 94. Push back on the customer's architecture without damaging trust

### 1. Understand why they chose it

Ask what constraints drove the choice: existing expertise, approved vendors, data location, procurement, cost, portability, or a previous failure. State their goal in terms they recognize before discussing your preferred design.

```text
Customer's choice -> underlying constraint -> observed technical risk
                                                   |
                                        test competing options
                                                   |
                                      shared decision + record
```

> **Explanation:** An architecture that looks inefficient technically may satisfy a real organizational constraint. Challenge the consequence, not the customer's competence.

### 2. Build a concrete trade-off

Assume the customer wants every ingestion, indexing, and answer-generation step in a synchronous API request. Their real constraint is limited operational capacity. The concern is that long-running work makes user latency and partial-failure recovery difficult.

| Option | Benefit | Cost/risk |
|---|---|---|
| Entire workflow in request | Simple initial deployment | Long response time, retries can repeat work |
| Persist job; process asynchronously | Recoverable work, quick job acknowledgment | Queue/worker operations and progress UI |
| Keep small tasks synchronous; queue large ones | Smaller first change | Two paths and a threshold to maintain |

> **Interview move:** “I understand why you want one service: your team needs to keep operations manageable. My concern is the behavior when a large document takes longer than the request timeout. Can we test that case before committing?”

### 3. Deliver the answer

> **Say it aloud:** “I would first understand the constraint behind your choice. Then I would describe the specific failure I am concerned about and its business impact, rather than saying the architecture is wrong. I would compare a small number of options against shared criteria such as latency, recovery, operating cost, and team ownership.
>
> “For this workflow, I recommend persisting large jobs and returning a job ID while keeping small tasks simple. We can run a representative load and failure test to see whether that added complexity is justified. I would document the decision, assumptions, and the condition that would make us revisit it.”

### 4. Follow-ups

If the customer chooses a supported trade-off you dislike, explain the accepted consequences, document them, and work within that decision. If it cannot meet a required control or acceptance condition, escalate that specific mismatch with alternatives and an accountable decision owner.

> **Pitfall:** A vague appeal to “best practices” cannot resolve competing priorities. A huge redesign proposal can also obscure the smallest change needed to meet the requirement.

**Recall check:** What evidence would change your recommendation? Name it before running the test so the discussion is not a contest of preferences.

### Conversation derivation: disagree using the customer's decision criteria

#### Gather constraints before recommending

For the synchronous workflow example, establish typical and tail document size, timeout behavior, current queue operations, failure recovery needs, available platform services, and who will support the result. The customer might already operate a managed queue, or might have a legitimate constraint against new dependencies.

> **Explanation:** The cost of an architectural choice includes the customer's ability to operate it. A theoretically elegant design that nobody can support may be the wrong first release.

#### Derive the experiment

```text
Shared criteria: request latency, completed work, duplicate effects,
                 operator effort, deployment complexity

Test 1: typical document -> normal completion
Test 2: large document -> request timeout while work continues?
Test 3: process crash -> can work resume without duplication?
Test 4: downstream outage -> what blocks and what recovers?

Compare synchronous baseline with persisted-job prototype.
```

Agree on what evidence favors each option. If all documents reliably finish within the target and recovery is simple, the synchronous approach may be suitable. If large tasks consistently outlive request deadlines and repeat effects occur, durable jobs have a concrete justification.

#### Handle pushback without abandoning judgment

```text
Customer: "Queues always make systems too complex."
You: "They add operating work, which is a real concern.
      Here is the failure the synchronous version must handle.
      Can we compare the smallest queue-backed path with an
      improved synchronous path under that same test?"

Customer: "We still choose synchronous."
You: "If it meets these criteria, I can support that choice.
      We will keep the size/time limits explicit and revisit
      when this observed condition changes."
```

Your preference should remain revisable. If an option violates a required security or correctness condition, state the specific unmet condition and the decision path for an acceptable alternative. Do not make disagreement about status or authority.

#### Verify a decision

Record options considered, measured evidence, constraints, chosen approach, owner and revisit trigger. A decision record should explain why the choice fits this customer now; it need not claim universal best practice. If the business later doubles allowed document size, rerun relevant acceptance rather than assuming the old design still fits.

Basic: polite disagreement. Strong: alternatives tied to business constraints. Senior: a falsifiable recommendation, agreed experiment, transparent accepted risk and measurable revisit condition.

<a id="q95"></a>
## 95. Turn a recurring customer pattern into a product change

### 1. Separate an anecdote from a recurring need

Capture the user's job, environment, workaround, impact, and current product limitation. Compare multiple customers: are they solving the same underlying problem, or asking for superficially similar features?

```text
Customer observations -> shared need -> evidence of impact
                                             |
                                  narrow reusable capability
                                             |
                                product experiment + field pilot
                                             |
                             release + migration + adoption evidence
```

> **Explanation:** Three customers requesting three SAP customizations may reveal one common capability: resumable connectors with clear failure reporting. Productizing each customer's exact code may miss the shared need.

### 2. Make an evidence-backed proposal

Assume several customers manually restart connector imports after rate-limit failures. Record frequency, engineering time, lost/duplicated records, support burden, and known constraints. Avoid invented metrics: in the interview, explain what you would measure.

Define the common contract: stable source cursor, durable checkpoint, idempotent write, retry metadata, and visible run status. Keep source-specific mappings in adapters. Propose one connector pilot before committing to universal connector coverage.

> **Correctness:** A feature is reusable only if its guarantees fit multiple contexts. Different sources have different ordering, deletion, and cursor semantics. An abstraction must make those differences explicit rather than hide them.

### 3. Deliver the answer

> **Say it aloud:** “I would collect the underlying workflow, workaround, and cost across customers, then identify the common failure rather than copy one customization into the product. For repeated interrupted imports, I would propose a resumable-ingestion capability with explicit checkpoint and replay contracts.
>
> “I would bring product a concise brief: affected users, evidence, current workaround, proposed minimum scope, expected benefit, and acceptance criteria. We would pilot with a small set of customers, measure reliability and support effort, and plan migration before retiring bespoke solutions.”

### 4. Follow-ups and acceptance

Measure successful resume, data completeness, reduced recovery time, onboarding effort, and adoption among customers with the need. A feature shipped but unused is not evidence that the problem was solved.

- **“Only one customer needs it.”** It may belong in an extension; assess strategic value and maintenance rather than forcing it into core.
- **“Product has no capacity.”** Share the evidence, contain the workaround behind a clear interface, and agree on ownership/support limits.
- **“Can you promise it to the customer?”** Communicate only agreed scope and dates; a field request is not a roadmap commitment.

> **Pitfall:** Counting requests measures interest, not value. Include consequence, frequency, and the cost of supporting the capability.

**Recall check:** What belongs in the shared product and what remains in the adapter? Shared execution guarantees versus source-specific extraction and mapping.

### Product derivation: prove the pattern and define its boundary

#### Build a field-evidence record

For each affected customer, capture user/workflow, environment, workaround frequency, failure consequence, support effort and current product gap. Separate observations from interpretations. “The operator manually restarts five imports a week” is evidence; “they need our proposed new platform” is a hypothesis.

| Proposed common capability | Stable part | Variable part |
|---|---|---|
| Resumable import | Run lifecycle, durable progress, status, replay contract | Source pagination and ordering |
| Error reporting | Reason category and affected scope | Source-specific error payload |
| Normalized ingestion | Output schema/version contract | Mapping and identity reconciliation |
| Operator recovery | Resume/cancel/retry rules | Source permission and quota constraints |

> **Explanation:** A good product seam groups behavior that can honestly share guarantees. It does not force different systems into a misleading one-size-fits-all API.

#### Compare responses to recurring demand

**Keep duplicating fixes:** fast for the next engagement but grows support and drift. **Build a universal connector framework immediately:** may overfit a small sample and delay delivery. **Extract one verified common lifecycle behind explicit adapter contracts:** improves repeat work while preserving source differences.

The decision includes product ownership, migration, test coverage and support. A new capability that field engineers still patch differently for each customer may not have solved the shared problem.

#### Handle product and customer pushback

```text
Product: "Is this just one large customer's request?"
You: "These observations show the same recovery task across these
      environments. Here are the differences the adapter must keep.
      I propose a small pilot before generalizing further."

Customer: "Will that feature ship next month?"
You: "The request and evidence are with the product owner.
      I can commit to our agreed interim scope and update date;
      the broader release is not yet an agreed commitment."
```

#### Verify the product outcome

Compare onboarding and recovery effort before/after, completion correctness, operator understanding, support burden and actual adoption. Review an additional source not used to design the abstraction: does it fit without special behavior leaking into the orchestrator? If not, refine the seam or retain an extension instead of declaring universal coverage.

For a new source with no replayable cursor, the generic “resume” contract may need a durable landed input or a snapshot restart. Document that limit rather than pretending it implements the same semantics.

Basic: pass feedback to product. Strong: synthesize evidence and a narrow reusable capability. Senior: defend the abstraction boundary, prevent unsupported customer promises, and validate migration/support economics.

<a id="q96"></a>
## 96. Discuss ROI with an executive after a failed AI pilot

### 1. Diagnose the prior failure before proposing another pilot

Ask what the previous pilot promised, what evidence it produced, why users did not adopt it, and what outcome still matters. Failure may have come from poor quality, workflow friction, slow integration, hidden review costs, or no meaningful problem.

```text
Prior promise -> actual evidence -> why value was not realized
                                           |
                                measurable current baseline
                                           |
                                  narrow hypothesis + cost
                                           |
                                  pilot -> continue or stop
```

> **Explanation:** ROI means the value actually realized after costs, not how impressive a demo looked. Time saved becomes business value only if the organization can use it productively.

### 2. Make the calculation explicit

Use assumptions the executive can challenge. Illustrative monthly scenario:

```text
10,000 tasks * 3 net minutes saved = 30,000 minutes = 500 hours
500 hours * $40/hour              = $20,000 capacity value
Operating/review costs           =  $8,000/month
Integration cost                 = $60,000 one-time

Potential net monthly benefit    = $12,000
Simple payback if realized       = 5 months
```

The three minutes must be measured end-to-end, including review and corrections. Operating costs include model/provider spend, infrastructure, monitoring, and ongoing support. Include error consequences where relevant; avoid double-counting review time or cost. Capacity value is not automatically cash savings.

> **Correctness:** Adoption is a multiplier. If only a fraction of eligible tasks use the system, benefits shrink. Show conservative/base/optimistic assumptions rather than presenting one speculative number as a result.

### 3. Deliver the answer

> **Say it aloud:** “Before asking you to fund another pilot, I would establish why the last one failed and whether the same workflow still offers measurable value. I would measure today's completion time, review burden, error costs, and task volume.
>
> “Then I would propose a bounded experiment with a spending limit, an accountable business owner, and explicit stop criteria. We would measure net time saved and quality in the actual workflow, include operating and integration costs, and verify adoption. If the evidence does not meet the agreed bar, we stop or change scope rather than relabeling a demo as ROI.”

### 4. Follow-ups

- **“We saved hours, so why no ROI?”** Check adoption, displaced/redeployed work, support costs, and whether hours translated into a useful business outcome.
- **“Give me a guarantee.”** Commit to the experiment, evidence, cost limit, and decision gate; distinguish a forecast from demonstrated value.
- **“Why use AI?”** Compare with simpler automation and process changes. Use the option that meets the business objective economically.

> **Pitfall:** Multiplying every employee's time by salary assumes all users adopt it, all savings are real, and capacity is monetized. Each is a hypothesis to validate.

**Recall check:** What finding would make you recommend stopping? State an observable quality, adoption, or economics condition.

### Economics derivation: separate a forecast from realized value

#### Ask questions that reveal the previous failure

**You:** “Did users stop using it because answers were poor or because it added work?” **Executive:** “They had to reenter its output into another system.” That suggests integration/workflow friction, not necessarily model quality.

**You:** “Did the benefit estimate include review time?” **Executive:** “No.” Now the previous savings calculation needs correction before comparing technologies.

**You:** “What would make a second pilot worth funding?” **Executive:** “A measurable reduction in handling time with no increase in costly mistakes.” That defines the outcome and guardrail together.

> **Explanation:** Do not defend AI as a category. Determine whether this particular intervention can improve the measured workflow after its real costs.

#### Derive a model that can be challenged

```text
Eligible task volume
   * adoption fraction
   * measured NET minutes saved per used task
   / 60
   * realistic value per released hour
   = potential realized capacity value

Subtract incremental operation, review and support costs
Account separately for one-time integration and change-management costs
```

If net minutes already include reviewer time, do not subtract those same labor minutes again. If review costs are outside that measured workflow, include them explicitly. Model reduced error losses separately and label the uncertainty; avoid adding overlapping benefits twice.

For the earlier 10,000-task example, 25% adoption reduces the time-based gross capacity estimate to $5,000, assuming savings per used task stay unchanged. If monthly operating cost remains $8,000 in this simplified sensitivity scenario, it exceeds that benefit before other gains. In a real model, separate fixed costs from usage-dependent costs. This makes adoption and fixed costs decision-relevant.

#### Compare intervention options

**Another impressive demo:** produces little evidence about workflow adoption. **A narrow integrated pilot:** tests end-to-end value within a controlled spend. **Deterministic automation or process repair:** may be cheaper if the task is rule-based or the real bottleneck is duplicate entry. Compare these against the same outcome.

```text
Executive: "Are you saying the last pilot was worthless?"
You: "It may have established technical feasibility, but it did
      not establish realized workflow value. I would preserve
      that learning and test the missing adoption/cost assumptions."

Executive: "What is the first investment decision?"
You: "Approve this bounded experiment, with this cost limit,
      evidence plan and stop condition—not the full rollout."
```

#### Verify and extend

Track actual task usage, net handling time, correction burden, quality and spend. Compare representative traffic with a credible baseline rather than measuring only enthusiasts. If the pilot works, estimate rollout-specific integration/training/support costs before extrapolating to all teams.

Basic: compute a plausible savings number. Strong: include net costs and adoption. Senior: diagnose prior failure, separate capacity from cash, test causality/selection effects and recommend stopping when evidence fails the economics gate.

<a id="q97"></a>
## 97. A customer wants immediate autonomy in a consequential workflow

### 1. Understand what autonomy means

Ask which exact actions the customer wants automated, their reversibility, potential loss, who currently authorizes them, available evidence, and which controls must hold. Distinguish drafting, recommending, approving, and committing.

```text
Draft recommendation
        |
Evidence + deterministic constraints
        |
Human-approved execution
        |
Restricted automatic execution for explicitly eligible cases
        |
Expansion only after agreed evidence and controls
```

> **Explanation:** Autonomy can differ by action and context. Reading a shipment and drafting a suggestion have a different risk profile from changing the route, making a payment, or denying a claim.

### 2. Define a concrete eligibility contract

For shipment rerouting, an illustrative eligibility rule might require permitted shipment classes, fresh data, validated capacity, bounded cost change, and an approved operating region. The customer's accountable owners set the actual limits.

```text
Eligible AND fresh AND authorized AND constraints pass?
                       /                      \
                     yes                       no
                      |                         |
              bounded execution          human review / fallback
                      |
           outcome verification + audit
```

Approval, policy checks, and tool permissions belong in the application. A prompt saying “be careful” is not an execution control. Use versioned proposals, idempotent action keys, cancellation/override, and recovery for unknown outcomes.

> **Correctness:** A high average success rate can hide an unacceptable rare failure. Evaluate failure severity, critical slices, adversarial inputs, and stale-data conditions, not only overall accuracy.

### 3. Deliver the answer

> **Say it aloud:** “I understand the goal is to reduce manual work. I would separate actions we can already constrain from actions whose failure impact is still unproven. We can start with recommendations and approved execution while gathering evidence in the real workflow.
>
> “For limited autonomy, we need explicit eligibility rules, authorization, fresh inputs, outcome checks, auditability, and a tested fallback. I would propose a narrow class of actions and agree on the quality and incident gates with the responsible owners. Expansion follows evidence; it is not a switch we turn on for the whole workflow.”

### 4. Follow-ups

- **“Humans make mistakes too.”** Compare both systems on representative tasks and total workflow cost. Human imperfection does not establish automated readiness.
- **“We accept the risk.”** Make the specific risk and responsible decision owner explicit; required controls still need to be met.
- **“Approval defeats the purpose.”** Automate preparation and validation first; measure remaining review time and gradually remove review for proven eligible cases.

> **Pitfall:** A kill switch cannot reverse every completed action. Prevention, bounded authority, and reconciliation matter before the switch is used.

**Recall check:** Name an action you could automate early and an action you would initially send to review; explain the different failure consequences.

### Authority derivation: turn “autonomy” into permissions and state transitions

#### Decompose the requested authority

| Action | Reversibility and evidence | Possible first boundary |
|---|---|---|
| Read an authorized shipment | No shipment mutation | Allow within access permissions |
| Draft a route explanation | Reviewable suggestion | Allow with evidence/uncertainty |
| Select a feasible option | Requires current constraints | Recommend or narrowly validated policy |
| Commit cost/capacity | External consequential effect | Explicit approval or authorized eligibility policy |
| Retry an unknown commitment | Can duplicate effects | Reconcile before repeating |

> **Explanation:** The same assistant may be autonomous for reading and drafting while tightly constrained for committing. Authority should be attached to an action and context, not to a broad label such as “trusted agent.”

#### Derive the execution contract

An eligible action requires authenticated authority, policy version, exact terms, fresh evidence, passed constraints and a durable execution key. A result records confirmed/rejected/unknown rather than using one vague success boolean. Reviewers need sufficient context, time and authority to reject; otherwise the human checkpoint can become a rubber stamp.

```text
Proposal -> eligibility check -> authority check -> execution claim
                                                       |
                                     provider call -> outcome verification
                                                       |
                                            confirmed / reconcile unknown
```

Compare immediate full authority, mandatory review for every case and policy-bounded authority. Full authority removes review delay but increases unproven consequences. Universal review provides control but may bottleneck routine tasks. Policy-bounded execution can reduce workload where evidence supports it, but requires measurable eligibility and recovery behavior.

#### Handle insistence with a concrete alternative

```text
Customer: "We cannot review every action."
You: "Let's define the routine class where terms, freshness
      and constraints can be verified. That class can be the
      automation candidate; exceptions stay in review."

Customer: "The model did well in our demo."
You: "That establishes some task behavior. We still need to
      test expired terms, conflicting requests, provider timeouts
      and recovery before granting commitment authority."
```

#### Verify the authority boundary

Trace an action just outside a cost limit, stale input, changed proposal revision, missing permission and unknown provider result. None should silently execute as an eligible action. Exercise override and cancellation before and during execution; acknowledge when the provider has already committed and cancellation is no longer guaranteed.

If automation expands to a new region or action type, treat it as a new eligibility/authority contract. Reuse the workflow mechanics, but revalidate constraints and outcomes. Basic evidence is cautious scoping; senior evidence makes that scope enforceable and proves the failure path.

<a id="q98"></a>
## 98. Scope the first discovery call without overcommitting

### 1. Establish the purpose of the call

The goal is a shared problem statement and a bounded next step, not a final architecture or delivery promise. Ask who owns the workflow, who uses the result, the current baseline, pain frequency/cost, existing systems, data/access constraints, and the desired decision date.

```text
Business pain -> current workflow -> evidence + constraints
                                            |
                                  explicit first-slice hypothesis
                                            |
                                  acceptance + exclusions + owners
                                            |
                                     next validation step
```

> **Interview move:** “Let me summarize what I heard: your team manually reviews delayed shipments each morning, and you want a faster way to identify which ones need action. Is that the first outcome we should focus on?”

### 2. Convert vague scope into a reviewable brief

For a shipment pilot:

| Dimension | Example first-slice agreement |
|---|---|
| User | Morning-shift warehouse managers in one region |
| Input | Shipment feed from one source with agreed freshness |
| Output | Ranked exceptions with evidence; no automatic rerouting |
| Outcome | Reduce review effort without missing agreed critical exceptions |
| Acceptance | Ops-defined quality/time criteria on representative cases |
| Dependencies | Approved access, representative sample, named business reviewer |
| Exclusions | All regions, automated carrier changes, every source connector |
| Next step | Validate data/access and baseline before estimating delivery |

> **Explanation:** Scope includes dependencies and acceptance, not just a list of features. A date is credible only after checking the work and external conditions behind it.

### 3. Deliver the answer

> **Say it aloud:** “I use the first call to agree on the user's decision and the current baseline. I ask for a real example, map the workflow and source systems, and identify access, deployment, and review dependencies. Then I restate one narrow outcome, what it includes, and what it excludes.
>
> “I distinguish confirmed facts from assumptions and unknowns. Rather than promise the complete system, I agree on the next validation step, who owns each input, and what evidence we need to estimate a pilot. After the call, I send a short scope summary for correction and make changes explicit.”

### 4. Follow-ups

If asked for a date immediately, give only an assumption-labelled planning range if there is a reasonable basis, or commit to when you can provide an estimate after a specific validation. Do not invent a range merely to sound helpful. If the customer adds scope, show the impact on time, cost, dependencies, and acceptance.

> **Pitfall:** Agreeing that a request is technically possible is not a delivery commitment. Make feasibility, pilot scope, and production rollout separate decisions.

**Recall check:** End the discovery call with three named items: the first outcome, the next evidence-producing action, and its owner.

### Scope derivation: convert the call into a testable engagement boundary

#### Follow the workflow before listing technologies

Ask the user to narrate one real instance: trigger, information gathered, decision, action, exception and handoff. Identify where time or error accumulates. Then ask which part the proposed system should change. A request for “an AI copilot” may really mean a prioritized exception list or a better source reconciliation process.

```text
Observed workflow
   -> friction / error / delay
   -> proposed first change
   -> required inputs and access
   -> acceptance evidence
   -> dependency owners
```

> **Explanation:** A feature list says what you intend to build. Acceptance says how the customer and engineer will know whether it helped. Both are necessary to bound work.

#### Produce a facts/assumptions/unknowns ledger

| Category | Illustrative item | What follows |
|---|---|---|
| Confirmed | Managers review shipment exceptions every morning | First user/workflow identified |
| Assumed | Source data is updated frequently enough | Validate watermark before promising real-time output |
| Unknown | SAP API access is approved | Name owner and validation date |
| Decision needed | Recommend or execute reroutes | Scope action authority explicitly |
| Excluded | All warehouses in first pilot | Adding them changes coverage/testing work |

Each important unknown gets an evidence-producing task, not just a question mark. For access, the task may be an approved read test. For data quality, it may be a representative export and reconciliation. For value, it may be timing the current workflow.

#### Compare commitment strategies

**Promise a broad system during the call:** maximizes apparent momentum but hides dependency and scope risks. **Refuse to discuss anything until exhaustive discovery:** provides little value and may be unnecessary. **Agree on a narrow next validation with a provisional scope:** gives the customer a concrete step without inventing certainty.

```text
Customer: "Can you have it live in four weeks?"
You: "The scoped pilot may fit that target, but access and data
      freshness are unverified. I can commit to this validation
      step and then provide a forecast tied to its findings."

Customer: "And add automated rerouting too."
You: "That adds action permissions, approval terms, provider
      integration and recovery. We should decide whether it
      replaces part of the first slice or becomes a later phase."
```

#### Verify the call and extend responsibly

Read back the agreed outcome, users, inputs, exclusions, acceptance, dependencies and next action. Send a concise record that invites correction. If the customer later changes the outcome, revise scope and acceptance rather than silently treating the change as another small feature.

Basic: ask discovery questions. Strong: produce a bounded brief and next step. Senior: separate facts from assumptions, name critical dependencies, negotiate scope changes and tie estimates to evidence.

<a id="q99"></a>
## 99. The customer's engineering team feels threatened: work with them

### 1. Understand the concern without assuming motive

Ask the engineering lead privately about ownership, workload, architecture constraints, support responsibilities, and what would make the engagement useful. They may reasonably worry about being handed an unsupported system, losing context, or being bypassed in decisions.

```text
Customer engineers' concerns
             |
Shared outcome + clear decision boundaries
             |
Joint discovery -> co-design -> paired implementation -> shared review
                                                        |
                                             operational handoff
```

> **Explanation:** Collaboration is concrete: access to decisions, code, tests, runbooks, and the ability to operate the result. Reassuring words alone do not resolve an unclear ownership model.

### 2. Define responsibilities together

An illustrative agreement: customer engineers own platform standards and ongoing operations; you own delivery of the agreed integration slice; both review interfaces, acceptance, and production readiness. Adapt to the customer's actual team boundaries.

Pair on the first vertical slice, use their approved toolchain, and document assumptions. Schedule short design reviews before major decisions. Make code and configuration inspectable, and teach while implementing so knowledge transfer is continuous.

> **Correctness:** “Their team owns it after launch” is incomplete. Confirm access, deployment, dashboards, incident response, recovery, dependencies, and support capacity. Run a handoff exercise where they deploy or diagnose a representative failure themselves.

### 3. Deliver the answer

> **Say it aloud:** “I would talk with the engineering lead to understand their concerns and make the engagement's purpose and ownership explicit. I want their team involved in architecture and operational decisions because they know the environment and will live with the result.
>
> “I would co-design the first slice, pair on integration, use their delivery standards, and make code, tests, and runbooks accessible throughout. We would agree on who decides, who implements, and who supports each component. Before handoff, their team should be able to deploy and troubleshoot it, with a clear escalation route for anything we still own.”

### 4. Follow-ups

- **“They are slowing us down.”** Identify the specific dependency or disagreement, propose a joint resolution, and escalate transparently through the agreed owner when needed. Avoid bypassing them.
- **“Their manager wants us to replace them.”** Clarify the mandate with leadership; do not promise job outcomes you cannot control. Keep communications factual and responsibilities explicit.
- **“They will not engage.”** Offer a small useful pairing task, ask what is blocking participation, and record the operational risk if ownership remains unresolved.

> **Pitfall:** A launch achieved by excluding the operating team can leave nobody able or willing to support it. Adoption by engineers is part of delivery success.

**Recall check:** What action would demonstrate trust this week? Let the team influence a real interface/operational decision and pair on its implementation.

### Collaboration derivation: make participation and ownership real

#### Diagnose the concern with respectful evidence

**You:** “Which part of the engagement creates risk for your team?” **Lead:** “We will be on call for a service we did not design.” This is an operational ownership problem, not resistance to AI.

**You:** “Which decisions must follow your platform standards?” **Lead:** “Identity, deployment and observability.” Put those reviews before implementation depends on them.

**You:** “What would a successful handoff look like?” **Lead:** “Our engineers can deploy, diagnose a failure and roll back.” Those become acceptance exercises, not just a documentation task.

> **Explanation:** An engineer's concern often identifies a real delivery risk. Listening changes the design and plan; it is not merely a social courtesy.

#### Derive an ownership agreement

| Area | Example responsibility to agree | Evidence of participation |
|---|---|---|
| Workflow requirements | Business owner + customer engineers + FDE | Shared first-slice brief |
| Integration interfaces | Joint design with named decision owner | Reviewed contract and error semantics |
| Platform controls | Customer platform owner | Approved identity/deployment configuration |
| Implementation | Agreed component owners | Shared repository, paired work, reviews |
| Operations | Named support owner with capacity | Dashboards, runbooks, recovery exercise |
| Post-launch gaps | Explicit escalation/support agreement | Known dependencies and response path |

Do not presume the customer team can absorb all maintenance. Ask about capacity, expertise and funding. Temporary FDE support is an explicit agreement; indefinite implicit support is a future incident.

#### Compare delivery approaches

**Build around the team and hand over at the end:** can appear faster but creates unfamiliar systems and lost context. **Hold many meetings without transferring decisions:** feels inclusive but leaves ownership unchanged. **Co-design and pair on a small visible slice:** gives the team a meaningful role and creates operational knowledge as code is built.

```text
Lead: "You are going to leave us with another black box."
You: "Let's make deployment and troubleshooting part of acceptance.
      We will review interfaces together, work in the agreed repo,
      and have your team run a recovery exercise before handoff."

Sponsor: "Can you bypass them to meet the deadline?"
You: "They own these operating constraints. Here is the specific
      blocked decision and a joint resolution option. Bypassing
      it would leave this readiness gap after launch."
```

#### Verify the handoff and changed requirements

Ask a customer engineer to deploy a known version, interpret an alert, find a failed job, safely resume or roll back, and identify who owns an unresolved provider issue. Record missing access or knowledge and close it before claiming readiness. Credit the team's contributions and make decision history discoverable.

If a team cannot operate the proposed stack, consider an existing supported platform or an explicitly funded support model. If personnel change, repeat onboarding and critical exercises; a document alone does not recreate practical understanding.

Basic: maintain respectful communication. Strong: share interfaces, code and meaningful decisions. Senior: make operating ownership an acceptance requirement, expose support capacity, and leave the team able to act independently.

## Rehearsal plan and scorecard

Use one question per session rather than trying to memorize the entire document.

```text
Read diagram + explanation
           |
Close the file
           |
Explain the design / conversation aloud
           |
Code or draw the core flow from memory
           |
Answer one changed requirement
           |
Score -> repair weakest point -> repeat next day
```

For 79–83, clarify for 3–5 minutes, implement for 20–30, and test/explain for 10. For 84–90, use a 10-minute initial answer and 10–15 minutes of follow-ups. For 91–99, give a calm 60–90-second opening, then answer two pushbacks. These are practice timings, not claims about your interview format.

| Dimension | 0 | 1 | 2 |
|---|---|---|---|
| Problem framing | Assumes the goal | Partly clarifies | User, decision, outcome, and scope clear |
| Mechanism | Names tools | Explains components | Explains state/flow and why choices fit |
| Correctness | Ignores failure | Names a failure | Handles concurrency, ambiguity, or recovery |
| Evidence | Makes claims | Mentions metrics | Defines observable acceptance and validation |
| Communication | Rambling/defensive | Understandable | Clear, concrete, owned, and adaptable |

> **Explanation:** Treat a score as a diagnostic, not proof of readiness. If you need hints to explain the core invariant or recover from a changed requirement, repeat that question before adding more.

Suggested interleaving: 79 + 80 (retry safety), 81 + 93 (fairness and access), 82 + 84 + 85 (data trust), 83 + 96 (metrics and value), 86 + 97 (actions and autonomy), 87 + 92 (model choice and limitations), 88 + 89 + 90 (consequential workflows), and 91 + 94 + 95 + 98 + 99 (delivery conversations).

## Reference map

The walkthroughs are original worked examples built around your pasted questions. The saved Hello Interview delivery framework, logger and rate-limiter pages informed the sequence of explanation and requirement-driven interface design, not the customer scenarios. The companion review records their differences from the first version.

- [Saved delivery framework](</Users/sandipan/Downloads/Low Level Design Interview Delivery Framework _ Hello Interview Low Level Design.html>)
- [Saved logging example](</Users/sandipan/Downloads/Logging Service Low Level Design _ Hello Interview Low Level Design.html>)
- [Saved rate-limiter example](</Users/sandipan/Downloads/Rate Limiter Low Level Design _ Hello Interview Low Level Design.html>)
- [Comparison and gap review](13-fde-walkthrough-gap-review.md)
- [Field Guide FDE preparation](05-forward-deployed-engineer.md)
- [Field Guide coding preparation](02-coding-and-leetcode.md)
- [Field Guide AI system-design method](03-ai-ml-system-design.md)
- [AWS: exponential backoff and jitter](https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/)
- [AWS: making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/)
- [Python CSV API](https://docs.python.org/3/library/csv.html)
- [Redis atomic scripting](https://redis.io/docs/latest/develop/programmability/eval-intro/)
- [PostgreSQL INSERT and ON CONFLICT](https://www.postgresql.org/docs/current/sql-insert.html)
- [PostgreSQL query-plan interpretation](https://www.postgresql.org/docs/current/using-explain.html)

If a step is unclear, ask about that question number and the exact line of reasoning. Rehearse the answer in your own words; use real project evidence only where you can explain your personal contribution.

## Example verification

The Python snippets were executed and checked for retry success/exhaustion/deadlines, permanent-error propagation, backoff caps, per-user/global quota enforcement, concurrent quota consumption, refill, and CSV validation/structural/sink failures. The SQL examples use PostgreSQL syntax and illustrative schemas; they have not been executed against a database. Architecture acceptance criteria and customer scripts are rehearsal examples, not verified deployment outcomes.
