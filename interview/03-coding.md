# Coding Problems

Coding-specific interview content: problems you code or implement, coding round formats, and implementation exercises.

For theory and conceptual questions, see [Theory Questions](02-theory.md). For system design, see [AI System Design](05-ai-system-design.md).

## Coding Round Formats

Companies use different coding formats. Some key patterns from practitioner reports:

Progressive/multi-level problems - Anthropic's 90-min coding challenge is a single problem with 4 levels: build a KV database with SET/GET/DELETE, add SCAN, add timestamped TTL, add file compression. Code must be extensible since each level builds on prior code. [^linkjob-anthropic] OpenAI also uses 4-gate progressive problems; the bar is clearing 2 of 4. [^exponent-openai]

ML coding - Implementing Transformers, LoRA, KV cache, autograd from scratch. OpenAI asks candidates to fix bugs in Transformer code (position embeddings, KV cache issues) and complete PyTorch implementations. [^linkjob-openai] Sundeep Teki reports implementing Multi-Head Attention and full Transformer layers from memory at top AI labs. [^sundeep-teki]

Refactoring rounds - OpenAI's onsite includes refactoring 100-120 lines of intentionally convoluted code for maintainability while keeping existing tests green and extending to new ones. Candidates describe it as "one of the better rounds" because it tests architectural judgment that AI tools struggle with. [^exponent-openai]

DSA as discussion - Microsoft's senior DSA round was 1+ hour of pure discussion (no code written) covering serialization approaches, compression techniques, streaming formats, backward compatibility, corruption recovery. "Senior coding rounds are not about typing speed. They are about engineering depth" [^rohit-verma]

DSA vs ML coding as separate rounds - AI Engineer and Applied Scientist roles often have distinct DSA and ML coding rounds. The DSA round has LeetCode problems; the ML coding round tests implementing ML algorithms from scratch or completing incomplete ML code. [^deepthi-sudharsan]

Take-home assignments - Some companies start with a take-home project before live rounds. One Gen AI Engineer candidate received a timed assignment to build an AI pipeline that parses a blood test PDF, identifies health issues, and fetches suggestions from online articles with source links -- testing speed of learning new frameworks under time pressure. [^khushal-kumar]

Speed coding with AI tools allowed - A live scenario-based round where the candidate was given a complicated JSON file, had to extract specific data following a pattern, feed it to an AI model, and get a summary -- all within 30 minutes. Browser and ChatGPT use was explicitly permitted. [^khushal-kumar]

Async/background processing problem pattern - A common coding interview problem type: a gRPC service is timing out and needs an async boundary. The interviewer evaluates candidates through progressive gates: (1) recognize that async processing is the solution, (2) identify where to place the async boundary in the system, (3) handle failure modes (retries, dead letter queues, idempotency), (4) scale with multi-threading or message queues. This pattern merges coding with system design in a single round. [^exponent-mock]

### OpenAI Coding Problems

The most commonly asked coding questions at OpenAI (L5/Staff level) are practical problems that feel more like real software challenges than pure algorithmic puzzles. Candidates can use their own IDE with screen-sharing or CoderPad. The no-reference policy means coding from memory: [^hello-interview]

1. KV Store Serialize/Deserialize - Implement a key-value store with serialization
2. In-Memory Database with SQL-Like Operations - Build a database supporting SQL-like queries
3. Design SQL (LeetCode 2408)
4. Time-Based Key-Value Store (LeetCode 981) - Time-indexed data handling
5. Unix cd Command with Symbolic Link Resolution

Problems emphasize concurrency, OOP design, and iterator patterns with state management. Sessions contain 1-2 problems; interviewers watch pace to decide depth vs. breadth. After the initial solution, interviewers introduce additional constraints or ask for optimizations to test scalability thinking.

### ML/DL Coding Topics

For ML coding rounds (typically 25-35 minutes, no debugging tools), candidates are asked to implement from scratch using NumPy or PyTorch: [^mimansa-jaiswal]

- Basic ML: Neural networks, LSTMs, RNNs from scratch
- Attention mechanisms: Cached attention, grouped query attention, multi-head attention variants
- Transformer components: Embeddings, layer normalization, full encoder layers
- RAG/inference: Embedding models, decoding strategies (top-p, top-k, beam search)
- Practical tip: Use "shape suffixes" in variable naming (Noam Shazeer method) to track tensor dimensions throughout implementations

## Interview Questions

### Coding / DSA

- Implement a key-value store with SET/GET/DELETE, then add SCAN, timestamped TTL, and file compression (progressive 4-level problem). (Anthropic) [^linkjob-anthropic]
- Implement a versioned key-value store (Time Travel Hash variant). (OpenAI) [^linkjob-openai]
- Build an in-memory database with SQL-like operations. (OpenAI) [^hello-interview]
- Design SQL (LeetCode 2408). (OpenAI) [^hello-interview]
- Time-Based Key-Value Store (LeetCode 981). (OpenAI) [^hello-interview]
- Implement Unix cd command with symbolic link resolution. (OpenAI) [^hello-interview]
- Implement a credits management system: track credit state across issued and used credits with expiration rules. (OpenAI) [^exponent-openai]
- Refactor 100-120 lines of convoluted code for maintainability while keeping tests green and extending to new requirements. (OpenAI onsite) [^exponent-openai]
- Implement Word Search using Trie + DFS. (xAI) [^reddit-xai]
- Design and implement an LRU Cache. (xAI) [^reddit-xai]
- Implement 1-NN (simplest KNN case) and a feedforward neural network. (OpenAI) [^linkjob-openai]
- Fix bugs in Transformer code: position embeddings, KV cache issues. (OpenAI) [^linkjob-openai]
- A gRPC service is timing out. Add an async boundary, handle failure modes (retries, dead letter queues, idempotency), scale with multi-threading or message queues. [^exponent-mock]
- Find prime numbers between 0 and 100. Check whether two strings are anagrams. (startup Gen AI Engineer) [^khushal-kumar]
- Given a complicated JSON file, extract specific data following a pattern, feed it to an AI model, and get a summary -- within 30 minutes, browser and ChatGPT allowed. (startup Gen AI Engineer) [^khushal-kumar]
- Discuss serialization approaches, compression techniques, streaming formats, backward compatibility, and corruption recovery (no code written, pure discussion). (Microsoft senior) [^rohit-verma]

### ML Fundamentals (Implementation)

- Implement Multi-Head Attention from scratch. (OpenAI, Anthropic, DeepMind) [^sundeep-teki]
- Implement a full Transformer layer from memory using NumPy or PyTorch. [^sundeep-teki]
- Implement neural networks, LSTMs, and RNNs from scratch. [^mimansa-jaiswal]
- Implement cached attention and grouped query attention variants. [^mimansa-jaiswal]
- Implement beam search, top-k, and top-p decoding strategies from scratch. [^mimansa-jaiswal]
- How would you design an ML system to scale for millions of users? [^fahd-mirza]

### Infrastructure & MLOps (Implementation)

- Explain the full ML deployment workflow: CI/CD, monitoring, and feedback loops. (IBM) [^raghu-teja]
- Design a large-scale AI model deployment system. Discuss model serving, GPU scaling, model versioning, and result caching. (OpenAI) [^designgurus]
- Design a real-time chatbot API. Discuss low-latency inference, session management, concurrency, and safety filters. (OpenAI) [^designgurus]
- Design a scalable data pipeline for ML applications. Discuss streaming vs. batch ingestion, ETL, and data consistency. (OpenAI) [^designgurus]
- Design an AI co-pilot like GitHub Copilot with real-time streaming completions. (Staff+) [^colin-zhou]
- Design a user profile system for 100 million users with multi-device tracking and batch migration. (OpenAI) [^linkjob-openai]
- Design the OpenAI Playground: developer workflow, thread history, conversation remixing, intuitive API feel. (OpenAI) [^exponent-openai]
- What is Docker? Why use containers for AI applications? (startup Gen AI Engineer) [^khushal-kumar]
- Design a small language learning model that could run on a phone while making sure it's polite. (Google) [^igotanoffer]
- Design our Claude chat service. (Anthropic) [^igotanoffer]
- Here's a junior developer's design for an inference batching system -- can you review it and explain what you'd change? (Anthropic) [^igotanoffer]
- Walk through a production-ready agent architecture. Discuss separation of concerns, fail-safe defaults, observability, and stateless orchestration. [^techeon]
- How would you design a system to serve Midjourney/Stable Diffusion style image generation at scale? Discuss queueing and GPU scheduling. (Staff+) [^colin-zhou]


## Sources

[^linkjob-anthropic]: [linkjob - Anthropic](https://www.linkjob.ai/interview-questions/anthropic-software-engineer-interview/)
[^linkjob-openai]: [linkjob - OpenAI](https://www.linkjob.ai/interview-questions/openai-loop-interview)
[^exponent-openai]: [Medium - Exponent, OpenAI](https://medium.com/exponent/what-its-actually-like-to-interview-at-openai-in-2026-03a646c9436c)
[^exponent-mock]: [YouTube - Exponent Mock Interview](https://www.youtube.com/watch?v=C6CdzcU7I18)
[^sundeep-teki]: [Sundeep Teki](https://www.sundeepteki.org/advice/the-ultimate-ai-research-engineer-interview-guide-cracking-openai-anthropic-google-deepmind-top-ai-labs)
[^rohit-verma]: [Medium - Rohit Verma, Microsoft](https://medium.com/@rohitverma_87831/microsoft-senior-engineer-interview-experience-2026-the-offer-that-took-me-three-attempts-e0d6e052bdb1)
[^deepthi-sudharsan]: [Medium - Deepthi Sudharsan](https://medium.com/@deepthi.sudharsan/inside-ai-interviews-stories-patterns-and-what-actually-matters-555684c38598)
[^khushal-kumar]: [Medium - Khushal Kumar](https://medium.com/@khushalkumar21/my-generative-ai-engineer-interview-experience-got-hired-61a1299ff390)
[^hello-interview]: [HelloInterview - OpenAI L5](https://www.hellointerview.com/guides/openai/l5)
[^mimansa-jaiswal]: [Mimansa Jaiswal](https://mimansajaiswal.github.io/posts/llm-ml-job-interviews-resources/)
[^reddit-xai]: [Reddit - xAI candidate report](https://www.reddit.com/r/cscareerquestions/comments/1jqq06y/got_an_offer_from_xai/)
[^raghu-teja]: [Medium - Raghu Teja, IBM Part 2](https://medium.com/@raghu_teja/how-i-cracked-my-ibm-ai-engineer-interview-part-2-ml-scenarios-88af2b46282e)
[^designgurus]: [DesignGurus - OpenAI System Design](https://www.designgurus.io/blog/openai-system-design-interview-questions)
[^colin-zhou]: [Medium - Colin Zhou](https://medium.com/@colinzhou)
[^techeon]: [Medium - TechEon Agentic Guide](https://atul4u.medium.com/the-complete-agentic-ai-system-design-interview-guide-2026-f95d0cfeb7cf)
[^igotanoffer]: [igotanoffer - Generative AI System Design Interview](https://igotanoffer.com/en/advice/generative-ai-system-design-interview)
[^fahd-mirza]: [YouTube - Fahd Mirza](https://www.youtube.com/watch?v=fahd-mirza-upwork)
