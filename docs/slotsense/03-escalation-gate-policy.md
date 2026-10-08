# Escalation Gate and Policy

This is the code-grounded version of the escalation design. A previous draft described invented macros such as `collect_safety_signals` and `EscalationPolicyEngine`; those are not the implementation. The real system is centered on `FAQService`, `EscalationPolicy`, `EscalationSignals`, Redis-backed session ledgers, and the response metadata returned by the assistant API.

The decision I made was to turn escalation into a small policy layer with explicit signals, rather than scattering handoff logic across RAG, retention, game, and guardrail code. The policy is intentionally boring: classify, normalize into a few signal fields, apply deterministic rules, then stamp the same metadata shape onto the response.

## Actual Runtime Shape

```mermaid
flowchart TD
    U[User message] --> Q[Assistant query endpoint]
    Q --> S[FAQService]

    S --> C[Closure check]
    C -->|genuine closure| CSAT[End chat and trigger CSAT]
    C -->|not closed| G[Escalation gate]

    G --> EC[escalation_check.classify_escalation]
    EC --> GS[_gate_signals maps classifier result to EscalationSignals]
    GS --> L[MemoryManager reads and updates session ledger]
    L --> P[EscalationPolicy.decide_gate]

    P -->|transfer or handoff answer| O[Override response]
    P -->|continue| R[Route to RAG, retention, game, or procedure]

    R --> A[Agent response]
    A --> OH[_maybe_offer_handoff_from_signal]
    OH --> OE[_apply_outcome_escalation]
    OE --> RESP[QueryResponse with guardrail metadata]
```

## Policy Surface

The policy does not receive raw classifier JSON. `FAQService._gate_signals` translates legacy classifier categories into the typed dataclass used by the policy.

```mermaid
flowchart LR
    Raw[Classifier dict] --> Map[_gate_signals]

    Map --> Safety[category = safety]
    Map --> Human[category = human_request]
    Map --> Abuse[category = abuse]
    Map --> Agent[category = needs_agent]

    Safety --> Signals[EscalationSignals]
    Human --> Signals
    Abuse --> Signals
    Agent --> Signals

    Signals --> Decide[EscalationPolicy.decide_gate]
    Decide --> Decision[EscalationDecision]
```

Actual signal fields include:

- `category`: `safety`, `human_request`, `abuse`, or `needs_agent`.
- `sensitive_severity`: separates harm cases from other safety cases.
- `human_request` and `is_repeat_human_request`: make "first ask" different from "repeated ask".
- `abuse_over_threshold`: only repeated abuse escalates.
- `is_benign`: suppresses non-floor categories.
- `offer_live_support`: optional offer path, usually from an agent outcome.
- `unanswered`, `no_progress_over_threshold`, and `procedure_should_escalate`: outcome-stage signals.

## Gate Decision Rules

```mermaid
flowchart TD
    Start[EscalationSignals] --> Cat{category?}

    Cat -->|none| Continue[Continue with AI]

    Cat -->|non-floor category| Benign{is_benign?}
    Benign -->|yes| Continue
    Benign -->|no| AbuseCheck{abuse?}

    Cat -->|safety| Severity{sensitive_severity}
    Severity -->|harm| Assist[ASSIST_THEN_HANDOFF]
    Severity -->|other safety| Now[ESCALATE_NOW]

    Cat -->|human_request| Repeat{repeat request?}
    Repeat -->|first request| Offer[OFFER_THEN_HANDOFF, no transfer]
    Repeat -->|repeat request| Transfer[OFFER_THEN_HANDOFF, transfer]

    AbuseCheck -->|abuse, below threshold| Continue
    AbuseCheck -->|abuse, over threshold| Deescalate[DEESCALATE and transfer]
    AbuseCheck -->|needs_agent| Need[ESCALATE_NOW]

    Assist --> Meta[GuardrailsMetadata]
    Now --> Meta
    Offer --> Meta
    Transfer --> Meta
    Deescalate --> Meta
    Need --> Meta
```

Two ideas matter here:

- Safety and explicit human requests are floor signals. They are not suppressed by `is_benign`.
- Abuse is not escalated on the first bad message. It becomes an escalation only after the Redis counter crosses the configured threshold.

## Optional Handoff Is a Two-Turn Contract

The assistant can offer live support without immediately transferring the chat. This avoids burning human capacity on every weak signal while still giving the user an escape hatch.

```mermaid
sequenceDiagram
    participant User
    participant Assistant as FAQService
    participant Agent as RAG or Retention
    participant Redis as MemoryManager
    participant Policy as EscalationPolicy

    User->>Assistant: asks a question
    Assistant->>Agent: route turn
    Agent-->>Assistant: response with offer_live_support=true
    Assistant->>Redis: claim_optional_offer(chat_id)
    Redis-->>Assistant: NX set succeeds
    Assistant-->>User: answer + live support offer

    User->>Assistant: yes, connect me
    Assistant->>Assistant: classify as offer_acceptance
    Assistant->>Redis: optional_offer_was_made(chat_id)
    Redis-->>Assistant: true
    Assistant->>Policy: decide_gate(human_request repeat/accepted)
    Policy-->>Assistant: transfer_to_human=true
    Assistant-->>User: handoff response
```

The Redis key is `optional_handoff_offered:{chat_id}` with a short TTL. The write uses NX semantics, so the same conversation is not repeatedly spammed with offers.

## Outcome Escalation

Not every escalation happens before the agent answers. RAG and procedure flows can also produce outcome signals after retrieval or tool execution.

```mermaid
flowchart TD
    Agent[Agent response] --> Signals{response.escalation_signals}

    Signals -->|unanswered| Empty[update_empty_context_counter]
    Empty --> Threshold{counter over threshold?}
    Threshold -->|no| Return[Return AI response]
    Threshold -->|yes| Policy[decide_outcome]

    Signals -->|procedure_should_escalate| Policy
    Signals -->|offer_live_support| Offer[maybe offer live support]

    Policy -->|escalate| Human[Replace answer with human-operator handoff]
    Policy -->|continue| Return
    Offer --> Return
```

For RAG, the actual source signal is `EscalationSignals(unanswered=..., offer_live_support=...)`. `unanswered` comes from empty context or an explicit `answered is False` retrieval result. The no-progress counter is stored in Redis as `frustration_counter:{chat_id}` and resets on a good answer.

## Resolution Gate

Resolution is also guarded. The system does not end a chat just because a classifier sees "thanks" or a low-context acknowledgement.

```mermaid
flowchart TD
    Turn[Assistant turn before routing] --> Closure[aconversation_resolved]
    Closure --> Resolved{resolved?}
    Resolved -->|no| Continue[Continue routing]
    Resolved -->|yes| Gate[gate_resolved]
    Gate --> First{first message?}
    First -->|yes| Continue
    First -->|no| Sentiment{frustrated or anxious?}
    Sentiment -->|yes| Continue
    Sentiment -->|no| End[mark resolved and trigger CSAT]
```

This is why the user experience is less brittle: closure needs a genuine closing signal, not just a polite phrase.

## Code Anchors

- `slotsense-ai-assistant-new/src/core/escalation/models.py`: `SituationClass`, `EscalationSignals`, `EscalationDecision`.
- `slotsense-ai-assistant-new/src/core/escalation/policy.py`: deterministic gate, optional handoff, scenario latch, and outcome decisions.
- `slotsense-ai-assistant-new/src/core/faq_service.py`: `_run_escalation_gate`, `_gate_signals`, `_maybe_offer_handoff_from_signal`, `_apply_outcome_escalation`, `_compute_resolved`.
- `slotsense-ai-assistant-new/src/core/memory/service.py`: Redis counters and flags for empty context, abuse, optional offers, and repeated human requests.
- `slotsense-ai-assistant-new/src/core/agents/rag.py`: RAG outcome signal creation.

## Interview Framing

The key architectural decision was to separate "detection" from "decision." Classifiers can be messy and change over time, but the product policy needs to be inspectable. By normalizing classifier output into `EscalationSignals`, the system can explain why a handoff happened, test edge cases without the LLM, and keep retention/game/RAG behavior consistent.

