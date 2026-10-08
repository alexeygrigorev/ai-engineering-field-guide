# Case Resolution

Language for the policy-bound customer-case workflow. Terms describe the
business domain only; implementation and architecture decisions live
elsewhere.

## Language

**Support Operations Specialist**:
An internal person accountable for reviewing evidence and deciding how a
Customer Case should be resolved.
_Avoid_: Agent, support user, reviewer

**Customer Case**:
A work item representing one customer request or problem, including the
relevant event time and references needed to investigate it.
_Avoid_: Ticket, conversation, query

**Resolution Proposal**:
A non-authoritative package of facts, policy evidence, eligibility reasoning,
and a suggested remedy prepared for a Support Operations Specialist.
_Avoid_: Answer, AI decision, resolution

**Simulated Action**:
A portfolio-safe representation of a consequential business action that
records the intended effect without calling a real commerce or payment system.
_Avoid_: Refund, tool call, mock
