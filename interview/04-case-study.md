# Case Study Questions

Case study interviews test how you think about approaching a problem, not how you implement it. They are similar to home assignments but without code -- a discussion on how you would approach a problem.

**Case study vs. system design**: Case studies focus on formulating the problem and the approach -- understanding requirements, asking clarifying questions, proposing a methodology, and reasoning about trade-offs. System design interviews (see [AI System Design](05-ai-system-design.md)) are about concrete technical implementation where you draw architecture diagrams, specify components, and discuss scaling.

## What to Expect

You get a vague or semi-defined problem and need to structure your thinking around it.

Examples: "Build a model for predicting car prices - what would you do?" or a vague question like "We want to increase user engagement - how?"

For vague questions, you need to ask clarifying questions: how do we measure engagement, what do users do on the platform.

A useful approach: start with a simple baseline, quickly iterate, roll out to production, then improve with more complex models.

## Approach Questions from Interviews

These are "how would you approach X?" questions reported by candidates -- they focus on methodology and problem-solving rather than drawing concrete architectures.

- How would you implement an AI application from start to finish, from kickoff meeting through deployment? (IBM -- [Raghu Teja](https://medium.com/@raghu_teja/how-i-cracked-my-ibm-ai-engineer-interview-part-2-ml-scenarios-88af2b46282e))
- How would you design a scalable and reliable automation workflow? What considerations for error handling, monitoring, and debugging? ([proptech founder](https://www.youtube.com/watch?v=proptech-founder-interview))
- How would you benchmark each LLM call in a multi-step pipeline to identify latency bottlenecks? ([proptech founder](https://www.youtube.com/watch?v=proptech-founder-interview))
- How do you monitor production AI systems? ([System Design Handbook](https://www.systemdesignhandbook.com/guides/generative-ai-system-design-interview/))
- How would you think about cost and capacity planning for an LLM-powered application at scale? ([igotanoffer](https://igotanoffer.com/en/advice/generative-ai-system-design-interview))
- How would you handle real-time versus batch processing for data updates? When is one preferred over the other? ([proptech founder](https://www.youtube.com/watch?v=proptech-founder-interview))
- How do you ingest and process different types of data (structured, unstructured, event data)? ([proptech founder](https://www.youtube.com/watch?v=proptech-founder-interview))
- How would you surface model limitations or errors to users without breaking trust? ([igotanoffer](https://igotanoffer.com/en/advice/generative-ai-system-design-interview))
- How would you design the UX for an AI assistant that is often slow? ([igotanoffer](https://igotanoffer.com/en/advice/generative-ai-system-design-interview))
- What are major scaling challenges for LLM-powered applications? ([System Design Handbook](https://www.systemdesignhandbook.com/guides/generative-ai-system-design-interview/))

## Four GenAI System Design Patterns

According to InterviewNode, most GenAI system design interviews follow four repeatable patterns that cover 80-90% of questions ([source](https://www.interviewnode.com/post/generative-ai-system-design-interview-patterns-you-should-know)):

1. **RAG (Retrieval-Augmented Generation)** - The most common pattern (2025-2026). Tests system orchestration and grounding accuracy. Senior candidates distinguish themselves by balancing constraints, not just describing components
2. **Feedback and reinforcement systems** - "How does it get better over time?" Used by OpenAI, Anthropic, and Meta AI. Tests RLHF understanding, implicit/explicit feedback signals, active learning loops
3. **Hallucination mitigation** - Every senior GenAI role includes at least one hallucination-focused question. Strong answers cover retrieval-grounded pipelines, confidence estimation based on retrieval density and token entropy, source transparency
4. **Scalability and cost optimization** - Tests engineering realism. Strong answers discuss multi-layer caching (retrieval, prompt, response), model tiering (small distilled model for routine requests, large LLM for high-impact), prompt compression, dynamic throttling

## Common Mistakes in GenAI System Design

Red flags identified by interviewers ([source](https://igotanoffer.com/en/advice/generative-ai-system-design-interview)):

- **Treating the LLM like a source of truth** instead of grounding with retrieval, tools, or citations
- **Skipping evaluation/monitoring** -- signals lack of production readiness
- **Defaulting to fine-tuning too early** without considering prompting, retrieval, or tools first
- **Ignoring safety and abuse vectors** -- prompt injection, data leakage, unsafe tool execution
- **Overlooking latency and cost** -- designing as if model calls are unlimited
- **Not addressing failure modes** -- avoiding discussion of what breaks and how the system degrades

Additional pitfalls from practitioner reports ([source](https://www.interviewnode.com/post/generative-ai-system-design-interview-patterns-you-should-know)):

- **Over-indexing on tools** -- mentioning LangChain without explaining why you chose it
- **Under-explaining data flow** -- omitting how retrieved context is validated or cached
- **Forgetting evaluation** -- never mentioning post-deployment quality measurement
