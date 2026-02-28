# TechEon Question Corroboration Map

Mapping each TechEon-only question to evidence from fetched Reddit posts and other verified sources.

## Sources key

- **[ED]** r/ExperiencedDevs/1r78ipa — Staff-level agentic AI system design interview (Feb 2026, 36 comments). Includes an interviewer (u/Realistic_Tomato1816) who says "Out of 30 people I've interviewed, only 4 or 5 have actual design experience."
- **[UK]** r/cscareerquestionsuk/1qmybi3 — AI Engineering Agents Interview Prep (Jan 2026)
- **[AG]** r/AI_Agents/1qrxchn — Interview prep: deep learning to agentic systems (Jan 2026)
- **[AI]** r/ArtificialIntelligence/1rceuef — "What agentic AI am I even supposed to learn?" (Feb 2026)
- **[IN]** Intuit SWE 2 interview, Neha Garg blog (Dec 2025) — dedicated AI round
- **[DI]** r/developersIndia/1oq5fdi — Generative AI Engineer interview (Nov 2025)

## Corroborated (have second source)

1. **"What makes an AI system truly agentic and what does not qualify?"**
   - [IN] Intuit Round 4 directly asks "Agentic AI vs GenAI vs AI Agents"
   - [AI] Company asked "do you have experience with agentic AI?" — implies they need candidates to define it
   - [DI] Comment: "Agentic GenAI roles are just software dev roles + GenAI tooling... You don't need to know any ML to do a GPT API call"

2. **"When is an agentic architecture the wrong solution?"**
   - [UK] "when agents are overkill versus when they shine"
   - [IN] "When AI should and should not be used"

3. **"How do you define and enforce agent autonomy boundaries?"**
   - [ED] "What information does the agent need? What should it NOT see? How do you prevent it from going off-rails?"
   - [ED] "Do not capture personal data and ensure no financial advice is given" — real example of scope boundaries

4. **"What are the essential components of an agent beyond an LLM?"**
   - [ED] "clear tool definitions, strict context files, and always server-authoritative"
   - [AI] "orchestrating them to do tasks autonomously... manage workflows, make decisions, call tools, interact with other systems"

5. **"How do you prevent agents from over-reasoning or over-planning?"**
   - [UK] "error recovery and looping"
   - [ED] "How do you prevent it from going off-rails?"

6. **"Walk through a production-ready agent architecture."**
   - [ED] Entire post is about preparing for this. Real interviewer confirms this is what they test.
   - [UK] "throw you a system design question about building an agent for a specific use case"

7. **"What logic belongs in the orchestrator vs the LLM?"**
   - [ED] "orchestration layers between agents"
   - [AG] "Can you explain the role of orchestration in multi-agent systems?"
   - [ED] "the agentic part is just a loop with guardrails" — implies clear separation

8. **"How do you design a safe and debuggable agent loop?"**
   - [ED] "guard rails, HIL, jail break circuit breaker questions, auditing/logging"
   - [UK] "how you'd prevent them from going off the rails in production scenarios"
   - [ED] "Observability in quality of responses, spot checks? QA test plans?"

9. **"How do agents decompose high-level goals into executable steps?"**
   - [UK] "how agents break down complex tasks into subtasks"

10. **"How do you detect and stop infinite planning loops?"**
    - [UK] "error recovery and looping"
    - [ED] circuit breaker pattern mentioned

11. **"How do you handle partial observability or missing information?"**
    - [UK] "what observability looks like when your AI is making autonomous decisions"

12. **"What planning failures are hardest to detect in production?"**
    - [ED] "failure recovery when agents make poor decisions" + extensive discussion of real failure modes (hallucinated policies, PII leaks, wrong refund info)
    - [ED] "What happens when the retrieval step returns semantically similar but factually wrong documents"

13. **"How do agents decide which tool to use?"**
    - [UK] "which tools you'd give the agent access to"
    - [AG] "Tool Selection Quality: Evaluates if the correct tools and arguments were chosen"

14. **"How do you sandbox tool execution safely?"**
    - [ED] PII filtering via interceptor service, "sandbox HIL testing"
    - [ED] "No PII means you need some resolver, interceptor service that filters everything"

15. **"How do you handle tool failures, retries, and idempotency?"**
    - [ED] "failure recovery when agents make poor decisions" + "idempotency"
    - [UK] "error recovery"
    - [AG] "How do you ensure reliability in agent workflows?"

16. **"What are the biggest security risks with tool-using agents?"**
    - [ED] PII leakage, jailbreaking, financial advice risks — real production example
    - [ED] "testing will involve jail breaking"

17. **"How do you control cost explosions from tool calls?"**
    - [ED] "rate limiting and cost management since these things can burn through api calls fast"
    - [UK] "cost control, latency constraints"

18. **"Stateless vs stateful agents -- tradeoffs and use cases?"**
    - [ED] "state management across async workflows" + "state management and context boundaries"

19. **"What types of memory do agentic systems need?"**
    - [ED] HIL discussion covers feedback loops and how data is captured/reused — touches episodic/procedural memory concepts
    - Weak corroboration, mostly conceptual overlap

20. **"How do you explain agentic systems to non-technical stakeholders?"**
    - [ED] Entire subthread on explaining HIL pattern with analogies (Waze, airport security, online banking, emergency room nurse)


## Partially corroborated (tangential evidence)

21. **"How do you design tool schemas that reduce hallucinated actions?"**
    - [^reddit-grilled-rag] Candidate grilled on "structured output, tool calling/function calling" for reliability — tangentially about schema design
    - Grok search (Feb 2026): datainterview.com describes OpenAI and Mistral interviews asking about constrained typed tool schemas, but these are prep guides, not first-person accounts
    - No direct "I was asked this" found

## NOT corroborated (no second source found)

22. **"How do you implement termination conditions in long-running agents?"**
23. **"Chain-of-thought vs tree-of-thought vs graph planning -- when would you use each?"**
24. **"How do agents decide a task is 'done'?"**
25. **"How do you version and roll back agent behavior?"**
26. **"How do you design long-term memory without polluting it?"**
27. **"Where do embeddings fail?" (line 67, separate from agents section)**

Grok search (Feb 2026) with web_search + x_search found no first-person interview accounts for questions 22-27.


## Summary

- **20 out of 27** TechEon-only questions have corroborating evidence from real interview discussions
- **1 question** has tangential corroboration (tool schemas — related to structured output discussions)
- **6 questions** remain single-sourced (mostly the more theoretical/specific ones)
- The r/ExperiencedDevs post is the strongest source — an actual interviewer describes what they test
- The topics most strongly validated: production architecture, safety/guardrails, failure modes, orchestration, cost control
- The topics with no corroboration tend to be more academic: CoT vs ToT planning, formal termination conditions, memory taxonomy, agent versioning
