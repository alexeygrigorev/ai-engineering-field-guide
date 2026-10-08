# Video Resources

Talks and videos worth watching for interview preparation, grouped by
the topic they support. Each entry notes which preparation file it
backs and what to take away.

## LLM Fundamentals and Cost

- [Prompt Caching with LLMs](https://www.youtube.com/watch?v=tGqvoEuoU5M) - how prompt caching works, what gets cached, and where the savings come from. Supports the cost and latency reasoning in [`03-ai-ml-system-design.md`](03-ai-ml-system-design.md) and the platform track in [`06-ml-ai-platform-engineer.md`](06-ml-ai-platform-engineer.md). Interviewers ask what you cache and why; be ready to state cache-hit assumptions and the cost delta they produce.

- [Context in LLMs](https://www.youtube.com/watch?v=VWNoSjQ798I) - what the context window actually holds and how context is assembled. Supports context engineering questions in [`01-common-core.md`](01-common-core.md) and retrieval design in [`03-ai-ml-system-design.md`](03-ai-ml-system-design.md). Connect it to what you drop first when the window is full.

## Agents and System Design

- [LLM vs Agent](https://www.youtube.com/watch?v=d-98DZZrS7M) - the boundary between a model call and an agent loop. Supports [`03-ai-ml-system-design.md`](03-ai-ml-system-design.md) and [`04-product-ai-engineer.md`](04-product-ai-engineer.md). Directly relevant to the common interview trap of defending agent count: use a single agent while the task stays simple, and be able to say what forces the split.

## How to Use These

Watch inside a preparation slot, not instead of one. After each video,
write two lines: what changed in your mental model, and one decision
from your own work that the video explains or contradicts. Those two
lines are what an interviewer hears, not the video summary.
