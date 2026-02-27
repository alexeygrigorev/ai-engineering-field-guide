# Case Study Questions

Case study interviews test how you think about approaching a problem, not how you implement it. They are similar to home assignments but without code -- a discussion on how you would approach a problem.

Case study vs. system design: Case studies focus on formulating the problem and the approach -- understanding requirements, asking clarifying questions, proposing a methodology, and reasoning about trade-offs. System design interviews (see [AI System Design](05-ai-system-design.md)) are about concrete technical implementation where you draw architecture diagrams, specify components, and discuss scaling.

## What to Expect

You get a vague or semi-defined problem and need to structure your thinking around it.

Examples: "Build a model for predicting car prices - what would you do?" or a vague question like "We want to increase user engagement - how?"

For vague questions, you need to ask clarifying questions: how do we measure engagement, what do users do on the platform.

A useful approach: start with a simple baseline, quickly iterate, roll out to production, then improve with more complex models.

## Approach Questions from Interviews

These are "how would you approach X?" questions reported by candidates -- they focus on methodology and problem-solving rather than drawing concrete architectures.

- How would you implement an AI application from start to finish, from kickoff meeting through deployment? (IBM) [^raghu-teja]
- How would you design a scalable and reliable automation workflow? What considerations for error handling, monitoring, and debugging? [^proptech-founder]
- How would you benchmark each LLM call in a multi-step pipeline to identify latency bottlenecks? [^proptech-founder]
- How do you monitor production AI systems? [^system-design-handbook]
- How would you think about cost and capacity planning for an LLM-powered application at scale? [^igotanoffer]
- How would you handle real-time versus batch processing for data updates? When is one preferred over the other? [^proptech-founder]
- How do you ingest and process different types of data (structured, unstructured, event data)? [^proptech-founder]
- How would you surface model limitations or errors to users without breaking trust? [^igotanoffer]
- How would you design the UX for an AI assistant that is often slow? [^igotanoffer]
- What are major scaling challenges for LLM-powered applications? [^system-design-handbook]


## Sources

[^raghu-teja]: [Medium - Raghu Teja, IBM Part 2](https://medium.com/@raghu_teja/how-i-cracked-my-ibm-ai-engineer-interview-part-2-ml-scenarios-88af2b46282e)
[^proptech-founder]: [YouTube - Proptech Founder](https://www.youtube.com/watch?v=proptech-founder-interview)
[^system-design-handbook]: [System Design Handbook](https://www.systemdesignhandbook.com/guides/generative-ai-system-design-interview/)
[^igotanoffer]: [igotanoffer - Generative AI System Design Interview](https://igotanoffer.com/en/advice/generative-ai-system-design-interview)
