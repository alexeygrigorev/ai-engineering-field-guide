# Gap review: FDE walkthroughs versus Hello Interview

Reviewed the saved delivery framework, logging service, and rate-limiter articles against the first version of [questions 79–99](13-fde-practical-coding-and-cases-79-99.md).

## Finding

The first version was a useful rehearsal guide, but it was not yet as explanatory as the supplied examples. It covered many important topics without consistently showing the reasoning that produces the design. Adding more blockquotes alone would not fix that.

The supplied logger and rate-limiter pages each contain roughly 9,000–10,000 words of extracted visible text, including navigation and discussion material. Our entire 21-question first version contained about 13,000 words. That is context for the difference in depth, not a target to pad toward. The important difference is the amount of design derivation per decision.

## What the delivery framework actually asks the candidate to produce

| Stage | Approximate source pacing | Reviewable output |
|---|---|---|
| Requirements | 5 minutes | Agreed capabilities, rules, errors, scope and exclusions |
| Entities/relationships | 3 minutes | State owners, rule owners, orchestrator and dependency arrows |
| Class design | 10–15 minutes | Requirements mapped to fields, methods and ownership |
| Implementation | 10 minutes | Important methods: normal flow, then edge cases |
| Verification | 1–2 minutes within the walkthrough | A concrete initial state and operation-by-operation trace |
| Extensibility | About 5 minutes if available | Where a changed requirement lands, with consequences |

These are flexible pacing suggestions for LLD, not a promise that every interview has the same duration or expects the same output. Follow interviewer direction and ask whether they want runnable code, pseudocode, or discussion.

## Specific gaps and the changes they require

| Gap in first version | Evidence from supplied examples | Needed addition |
|---|---|---|
| Clarification was often a list rather than a design conversation | Answers narrow scope and change the model | Explain how each answer changes implementation |
| Scope exclusions were inconsistent | Examples explicitly defer async/network/config features | Separate v1 from extensions and name the assumptions |
| Entity tables named responsibilities but rarely eliminated candidates | Logger distinguishes fields, enums, value objects and entities | Show why a noun is a field/function/entity, and what not to model |
| Fields/methods appeared without a full derivation | Framework maps each requirement to remembered state and operations | Requirement → state → rule → method tables |
| Only short descriptions of alternatives | Logger compares branching, inheritance, composition, and locking | Compare plausible approaches, identify the actual failure and choose under current constraints |
| Implementation was usually one completed code block | Rate limiter builds lookup, refill, check, consume and denial separately | Explain ordering and the responsibility of each operation |
| Tests were mostly named | Examples manually execute requests and show state transitions | Before/after tables and one failure or concurrency trace |
| Extensions named mechanisms without consistently showing changes | Source discusses how config, workers, state and lifetime evolve | Identify changed fields/interfaces, preserved invariants and new problems |
| Senior evaluation was generic | Examples distinguish working basics from ownership and trade-off reasoning | Problem-specific basic, strong, and senior evidence |
| Customer answers were mostly polished scripts | LLD framework itself does not define customer role-play | Add fact gathering, decision boundaries, pushback dialogue, and evidence of resolution |

## Keep the reasoning, not every source recommendation

The reference pages are examples with their own scope. Our question 81 requires both per-user and global enforcement; the supplied article emphasizes per-client/per-endpoint algorithms. Per-user locking alone cannot protect a shared global bucket. The expanded walkthrough explains why the joint quota decision needs a shared coordination point.

Likewise, locks isolate resource mutation, but a synchronous logger can still block its caller on slow I/O. Strict caller-latency isolation needs an async policy. And dropping limiter state because an LRU cache is full can give quota back to a recently active user; safe eviction needs a semantic condition, not just a cache policy.

The framework's state-and-behavior derivation is useful across problems. Its object-model stages should not be forced into SQL analysis or customer conversations. Those need query grain and data contracts, or stakeholders, facts, choices, and ownership respectively.

## Revision approach

Keep the existing diagrams, examples and concise spoken answers. Add deeper derivation, explicit alternatives, decision/failure traces and changed-requirement walkthroughs within each question. The introduction now includes a full delivery guide and shows how it adapts to each question family. Add callouts at the points where a novice would otherwise have to infer the missing step.

## Revision completed

All 21 questions now include an additional derivation section, with problem-specific alternatives, execution or decision traces, changed requirements, and basic/strong/senior evidence. The guide grew from approximately 13,000 to 27,000 words. More explanation was added where it resolves a design decision; the coding questions received the most implementation detail, while the role-play questions gained decision preparation and pushback dialogue.

The four Python blocks were recompiled and executed, including targeted retry, quota/concurrency, and parser-failure checks. Document checks confirmed all question numbers, diagrams, derivation sections, callouts, local links, and balanced fences. PostgreSQL examples remain illustrative and were not database-executed. The walkthroughs do not reproduce the reference articles or claim their exact word count per question; they apply the depth-producing parts of their delivery method to these different prompts.

## Local references

- [Delivery framework](</Users/sandipan/Downloads/Low Level Design Interview Delivery Framework _ Hello Interview Low Level Design.html>)
- [Logging service](</Users/sandipan/Downloads/Logging Service Low Level Design _ Hello Interview Low Level Design.html>)
- [Rate limiter](</Users/sandipan/Downloads/Rate Limiter Low Level Design _ Hello Interview Low Level Design.html>)
