# Coding Problems

Coding-specific interview content: problems you code or implement, coding round formats, and implementation exercises.

For theory and conceptual questions, see [Theory Questions](02-theory.md). For system design, see [AI System Design](05-ai-system-design.md).

## Coding Round Formats

Companies use different coding formats. Some key patterns from practitioner reports:

Progressive/multi-level problems - Anthropic's 90-min coding challenge is a single problem with 4 levels: build a KV database with SET/GET/DELETE, add SCAN, add timestamped TTL, add file compression. Code must be extensible since each level builds on prior code ([source](https://www.linkjob.ai/interview-questions/anthropic-software-engineer-interview/)). OpenAI also uses 4-gate progressive problems; the bar is clearing 2 of 4 ([source](https://medium.com/exponent/what-its-actually-like-to-interview-at-openai-in-2026-03a646c9436c))

ML coding - Implementing Transformers, LoRA, KV cache, autograd from scratch. OpenAI asks candidates to fix bugs in Transformer code (position embeddings, KV cache issues) and complete PyTorch implementations ([source](https://www.linkjob.ai/interview-questions/openai-loop-interview)). Sundeep Teki reports implementing Multi-Head Attention and full Transformer layers from memory at top AI labs ([source](https://www.sundeepteki.org/advice/the-ultimate-ai-research-engineer-interview-guide-cracking-openai-anthropic-google-deepmind-top-ai-labs))

Refactoring rounds - OpenAI's onsite includes refactoring 100-120 lines of intentionally convoluted code for maintainability while keeping existing tests green and extending to new ones. Candidates describe it as "one of the better rounds" because it tests architectural judgment that AI tools struggle with ([source](https://medium.com/exponent/what-its-actually-like-to-interview-at-openai-in-2026-03a646c9436c))

DSA as discussion - Microsoft's senior DSA round was 1+ hour of pure discussion (no code written) covering serialization approaches, compression techniques, streaming formats, backward compatibility, corruption recovery. "Senior coding rounds are not about typing speed. They are about engineering depth" ([source](https://medium.com/@rohitverma_87831/microsoft-senior-engineer-interview-experience-2026-the-offer-that-took-me-three-attempts-e0d6e052bdb1))

DSA vs ML coding as separate rounds - AI Engineer and Applied Scientist roles often have distinct DSA and ML coding rounds. The DSA round has LeetCode problems; the ML coding round tests implementing ML algorithms from scratch or completing incomplete ML code ([source](https://medium.com/@deepthi.sudharsan/inside-ai-interviews-stories-patterns-and-what-actually-matters-555684c38598))

Take-home assignments - Some companies start with a take-home project before live rounds. One Gen AI Engineer candidate received a timed assignment to build an AI pipeline that parses a blood test PDF, identifies health issues, and fetches suggestions from online articles with source links -- testing speed of learning new frameworks under time pressure ([source](https://medium.com/@khushalkumar21/my-generative-ai-engineer-interview-experience-got-hired-61a1299ff390))

Speed coding with AI tools allowed - A live scenario-based round where the candidate was given a complicated JSON file, had to extract specific data following a pattern, feed it to an AI model, and get a summary -- all within 30 minutes. Browser and ChatGPT use was explicitly permitted ([source](https://medium.com/@khushalkumar21/my-generative-ai-engineer-interview-experience-got-hired-61a1299ff390))

Async/background processing problem pattern - A common coding interview problem type: a gRPC service is timing out and needs an async boundary. The interviewer evaluates candidates through progressive gates: (1) recognize that async processing is the solution, (2) identify where to place the async boundary in the system, (3) handle failure modes (retries, dead letter queues, idempotency), (4) scale with multi-threading or message queues. This pattern merges coding with system design in a single round. ([Exponent](https://www.youtube.com/watch?v=C6CdzcU7I18))

### OpenAI Coding Problems

The most commonly asked coding questions at OpenAI (L5/Staff level) are practical problems that feel more like real software challenges than pure algorithmic puzzles. Candidates can use their own IDE with screen-sharing or CoderPad. The no-reference policy means coding from memory ([source](https://www.hellointerview.com/guides/openai/l5)):

1. KV Store Serialize/Deserialize - Implement a key-value store with serialization
2. In-Memory Database with SQL-Like Operations - Build a database supporting SQL-like queries
3. Design SQL (LeetCode 2408)
4. Time-Based Key-Value Store (LeetCode 981) - Time-indexed data handling
5. Unix cd Command with Symbolic Link Resolution

Problems emphasize concurrency, OOP design, and iterator patterns with state management. Sessions contain 1-2 problems; interviewers watch pace to decide depth vs. breadth. After the initial solution, interviewers introduce additional constraints or ask for optimizations to test scalability thinking.

### ML/DL Coding Topics

For ML coding rounds (typically 25-35 minutes, no debugging tools), candidates are asked to implement from scratch using NumPy or PyTorch ([source](https://mimansajaiswal.github.io/posts/llm-ml-job-interviews-resources/)):

- Basic ML: Neural networks, LSTMs, RNNs from scratch
- Attention mechanisms: Cached attention, grouped query attention, multi-head attention variants
- Transformer components: Embeddings, layer normalization, full encoder layers
- RAG/inference: Embedding models, decoding strategies (top-p, top-k, beam search)
- Practical tip: Use "shape suffixes" in variable naming (Noam Shazeer method) to track tensor dimensions throughout implementations

## Interview Questions

### Coding / DSA

- Implement a key-value store with SET/GET/DELETE, then add SCAN, timestamped TTL, and file compression (progressive 4-level problem). (Anthropic -- [LinkJob](https://www.linkjob.ai/interview-questions/anthropic-software-engineer-interview/))
- Implement a versioned key-value store (Time Travel Hash variant). (OpenAI -- [LinkJob](https://www.linkjob.ai/interview-questions/openai-loop-interview))
- Build an in-memory database with SQL-like operations. (OpenAI -- [HelloInterview](https://www.hellointerview.com/guides/openai/l5))
- Design SQL (LeetCode 2408). (OpenAI -- [HelloInterview](https://www.hellointerview.com/guides/openai/l5))
- Time-Based Key-Value Store (LeetCode 981). (OpenAI -- [HelloInterview](https://www.hellointerview.com/guides/openai/l5))
- Implement Unix cd command with symbolic link resolution. (OpenAI -- [HelloInterview](https://www.hellointerview.com/guides/openai/l5))
- Implement a credits management system: track credit state across issued and used credits with expiration rules. (OpenAI -- [Exponent](https://medium.com/exponent/what-its-actually-like-to-interview-at-openai-in-2026-03a646c9436c))
- Refactor 100-120 lines of convoluted code for maintainability while keeping tests green and extending to new requirements. (OpenAI onsite -- [Exponent](https://medium.com/exponent/what-its-actually-like-to-interview-at-openai-in-2026-03a646c9436c))
- Implement Word Search using Trie + DFS. (xAI -- [candidate report](https://www.reddit.com/r/cscareerquestions/comments/1jqq06y/got_an_offer_from_xai/))
- Design and implement an LRU Cache. (xAI -- [candidate report](https://www.reddit.com/r/cscareerquestions/comments/1jqq06y/got_an_offer_from_xai/))
- Implement 1-NN (simplest KNN case) and a feedforward neural network. (OpenAI -- [LinkJob](https://www.linkjob.ai/interview-questions/openai-loop-interview))
- Fix bugs in Transformer code: position embeddings, KV cache issues. (OpenAI -- [LinkJob](https://www.linkjob.ai/interview-questions/openai-loop-interview))
- A gRPC service is timing out. Add an async boundary, handle failure modes (retries, dead letter queues, idempotency), scale with multi-threading or message queues. ([Exponent](https://www.youtube.com/watch?v=C6CdzcU7I18))
- Find prime numbers between 0 and 100. Check whether two strings are anagrams. (startup Gen AI Engineer -- [Khushal Kumar](https://medium.com/@khushalkumar21/my-generative-ai-engineer-interview-experience-got-hired-61a1299ff390))
- Given a complicated JSON file, extract specific data following a pattern, feed it to an AI model, and get a summary -- within 30 minutes, browser and ChatGPT allowed. (startup Gen AI Engineer -- [Khushal Kumar](https://medium.com/@khushalkumar21/my-generative-ai-engineer-interview-experience-got-hired-61a1299ff390))
- Discuss serialization approaches, compression techniques, streaming formats, backward compatibility, and corruption recovery (no code written, pure discussion). (Microsoft senior -- [Rohit Verma](https://medium.com/@rohitverma_87831/microsoft-senior-engineer-interview-experience-2026-the-offer-that-took-me-three-attempts-e0d6e052bdb1))

### ML Fundamentals (Implementation)

- Implement Multi-Head Attention from scratch. (OpenAI, Anthropic, DeepMind -- [Sundeep Teki](https://www.sundeepteki.org/advice/the-ultimate-ai-research-engineer-interview-guide-cracking-openai-anthropic-google-deepmind-top-ai-labs))
- Implement a full Transformer layer from memory using NumPy or PyTorch. ([Sundeep Teki](https://www.sundeepteki.org/advice/the-ultimate-ai-research-engineer-interview-guide-cracking-openai-anthropic-google-deepmind-top-ai-labs))
- Implement neural networks, LSTMs, and RNNs from scratch. ([Mimansa Jaiswal](https://mimansajaiswal.github.io/posts/llm-ml-job-interviews-resources/))
- Implement cached attention and grouped query attention variants. ([Mimansa Jaiswal](https://mimansajaiswal.github.io/posts/llm-ml-job-interviews-resources/))
- Implement beam search, top-k, and top-p decoding strategies from scratch. ([Mimansa Jaiswal](https://mimansajaiswal.github.io/posts/llm-ml-job-interviews-resources/))
- How would you design an ML system to scale for millions of users? (commonly asked -- [Fahd Mirza](https://www.youtube.com/watch?v=fahd-mirza-upwork))

### Infrastructure & MLOps (Implementation)

- Explain the full ML deployment workflow: CI/CD, monitoring, and feedback loops. (IBM -- [Raghu Teja](https://medium.com/@raghu_teja/how-i-cracked-my-ibm-ai-engineer-interview-part-2-ml-scenarios-88af2b46282e))
- Design a large-scale AI model deployment system. Discuss model serving, GPU scaling, model versioning, and result caching. (OpenAI -- [DesignGurus](https://www.designgurus.io/blog/openai-system-design-interview-questions))
- Design a real-time chatbot API. Discuss low-latency inference, session management, concurrency, and safety filters. (OpenAI -- [DesignGurus](https://www.designgurus.io/blog/openai-system-design-interview-questions))
- Design a scalable data pipeline for ML applications. Discuss streaming vs. batch ingestion, ETL, and data consistency. (OpenAI -- [DesignGurus](https://www.designgurus.io/blog/openai-system-design-interview-questions))
- Design an AI co-pilot like GitHub Copilot with real-time streaming completions. (Staff+, commonly asked -- [Colin Zhou](https://medium.com/@colinzhou))
- Design a user profile system for 100 million users with multi-device tracking and batch migration. (OpenAI -- [LinkJob](https://www.linkjob.ai/interview-questions/openai-loop-interview))
- Design the OpenAI Playground: developer workflow, thread history, conversation remixing, intuitive API feel. (OpenAI -- [Exponent](https://medium.com/exponent/what-its-actually-like-to-interview-at-openai-in-2026-03a646c9436c))
- What is Docker? Why use containers for AI applications? (startup Gen AI Engineer -- [Khushal Kumar](https://medium.com/@khushalkumar21/my-generative-ai-engineer-interview-experience-got-hired-61a1299ff390))
- Design a small language learning model that could run on a phone while making sure it's polite. (Google -- [igotanoffer](https://igotanoffer.com/en/advice/generative-ai-system-design-interview))
- Design our Claude chat service. (Anthropic -- [igotanoffer](https://igotanoffer.com/en/advice/generative-ai-system-design-interview))
- Here's a junior developer's design for an inference batching system -- can you review it and explain what you'd change? (Anthropic -- [igotanoffer](https://igotanoffer.com/en/advice/generative-ai-system-design-interview))
- Walk through a production-ready agent architecture. Discuss separation of concerns, fail-safe defaults, observability, and stateless orchestration. ([TechEon](https://atul4u.medium.com/the-complete-agentic-ai-system-design-interview-guide-2026-f95d0cfeb7cf))
- How would you design a system to serve Midjourney/Stable Diffusion style image generation at scale? Discuss queueing and GPU scheduling. (Staff+ -- [Colin Zhou](https://medium.com/@colinzhou))
