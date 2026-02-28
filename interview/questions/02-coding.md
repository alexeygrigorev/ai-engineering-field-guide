# Coding Problems

Coding-specific interview content: problems you code or implement, coding round formats, and implementation exercises.

For theory and conceptual questions, see [Theory Questions](01-theory.md). For system design, see [AI System Design](04-ai-system-design.md).

## Coding Round Formats

Companies use different coding formats. Some key patterns from practitioner reports:

Progressive/multi-level problems - Anthropic's 90-min coding challenge is a single problem with 4 levels: build a KV database with SET/GET/DELETE, add SCAN, add timestamped TTL, add file compression. Code must be extensible since each level builds on prior code. [^linkjob-anthropic] OpenAI also uses 4-gate progressive problems; the bar is clearing 2 of 4. [^exponent-openai]

ML coding - Implementing Transformers, LoRA, KV cache, autograd from scratch. OpenAI asks candidates to fix bugs in Transformer code (position embeddings, KV cache issues) and complete PyTorch implementations. [^linkjob-openai] Sundeep Teki reports implementing Multi-Head Attention and full Transformer layers from memory at top AI labs. [^sundeep-teki]

Refactoring rounds - OpenAI's onsite includes refactoring 100-120 lines of intentionally convoluted code for maintainability while keeping existing tests green and extending to new ones. Candidates describe it as "one of the better rounds" because it tests architectural judgment that AI tools struggle with. [^exponent-openai]

DSA as discussion - Microsoft's senior DSA round was 1+ hour of pure discussion (no code written) covering serialization approaches, compression techniques, streaming formats, backward compatibility, corruption recovery. "Senior coding rounds are not about typing speed. They are about engineering depth" [^rohit-verma]

DSA vs ML coding as separate rounds - AI Engineer and Applied Scientist roles often have distinct DSA and ML coding rounds. The DSA round has LeetCode problems; the ML coding round tests implementing ML algorithms from scratch or completing incomplete ML code. [^deepthi-sudharsan]

Speed coding with AI tools allowed - A live scenario-based round where the candidate was given a complicated JSON file, had to extract specific data following a pattern, feed it to an AI model, and get a summary - all within 30 minutes. Browser and ChatGPT use was explicitly permitted. [^khushal-kumar]

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

### LeetCode / Algorithm Style

- Word Search on Grid using Trie + DFS (LeetCode Medium). [^devto-xai]
- LRU Cache with O(1) time complexity using HashMap + Doubly Linked List. [^devto-xai]
- Prime numbers between 0 and 100. [^khushal-kumar]
- Check whether two strings are anagrams of each other. [^khushal-kumar]
- Serialize Binary Tree (space-optimized, discussion-based with compression techniques and backward compatibility). [^rohit-verma]
- LeetCode 2408: Design SQL. [^hello-interview]
- LeetCode 981: Time Based Key-Value Store. [^hello-interview]
- Unix cd command with symbolic link resolution. [^hello-interview]
- Reverse a linked list with constraints (AI-assisted coding round - candidate must prompt LLM effectively). [^reddit-microsoft-aiml]
- Find the Excel column name from its column number (e.g., column 702 = "AAA"). [^reddit-microsoft-aiml]
- Construct a tree from a list where index = node value and value = parent node (LC Medium). [^reddit-microsoft-aiml]
- CodeSignal GCA: 4 questions in 70 min - two medium-hard, one graph, one greedy with bit ops. [^reddit-xai-eng]
- Write code for a banking application using HashMap/TreeMap. Design a task executor - store and pause tasks. [^reddit-2026-prep]
- A gRPC service is timing out. Add an async boundary, handle failure modes (retries, dead letter queues, idempotency), scale with multi-threading or message queues. [^exponent-mock]
- Discuss serialization approaches, compression techniques, streaming formats, backward compatibility, and corruption recovery - no code written, pure discussion. (Microsoft senior) [^rohit-verma]

### OpenAI-Specific Coding

- KV Store Serialize/Deserialize. [^hello-interview]
- In-Memory Database: Implement SQL-Like Operations. [^hello-interview]
- Versioned key-value store implementation (Time Travel Hash variant). [^linkjob-openai]
- Credits management system - track credit state across issued and used credits with different expiration rules and usage requirements, with increasing complexity. [^exponent-openai]
- Refactoring round: 100-120 lines of intentionally convoluted, deeply nested code. Refactor for long-term maintainability while keeping existing tests green and extending to new ones. [^exponent-openai]

### Anthropic-Specific Coding

- 4-level progressive coding assessment: Level 1 (SET/GET/DELETE), Level 2 (SCAN/SCAN_BY_PREFIX), Level 3 (timestamped operations + TTL), Level 4 (file compression/decompression with storage management). [^linkjob-anthropic]

### ML / AI Coding

- Debug code handling embeddings. [^promptlayer]
- Write scripts preparing text for fine-tuning. [^promptlayer]
- Implement logistic regression with SGD, L2 regularization, and early stopping in NumPy. [^datainterview-mistral]


### Practical / Data Processing

- Given a nested JSON dataset (e.g., API response, data export), write a script to extract specific fields, construct a prompt from the extracted data, call an LLM API, and return a summary. 30-minute time limit, browser and ChatGPT allowed. [^khushal-kumar] I assume this involved streaming JSON parsing (e.g., `ijson`), otherwise the task is too simple for a 30-minute round.
- Design a concurrent web crawler handling robots.txt, rate limiting, and circular references while maintaining data integrity and freshness. [^linkjob-anthropic]


## How to Prepare

DSA prep - Grind 75 + easy/medium from NeetCode 150. For AI roles, focus on hash maps, tries, linked lists, and concurrency patterns over graph algorithms. OpenAI's problems feel more like real software challenges than pure algorithmic puzzles - KV stores, in-memory databases, iterator patterns with state management. [^hello-interview] [^mimansa-jaiswal]

ML coding prep - Practice implementing core components from scratch in NumPy or PyTorch without debugging tools: multi-head attention, full Transformer layers, LoRA adapters, decoding strategies (beam search, top-k, top-p). Use "shape suffixes" in variable naming (Noam Shazeer method) to track tensor dimensions. These rounds are typically 25-35 minutes. [^mimansa-jaiswal] [^sundeep-teki]

Design for extensibility - Anthropic's progressive problems build on prior code across 4 levels. If your Level 1 design is rigid, you'll struggle at Level 3. OpenAI similarly uses 4-gate progressive problems where the bar is clearing 2 of 4. Think about how your code will need to change before you start writing. [^linkjob-anthropic] [^exponent-openai]

Practice narrating your reasoning - AI tools are increasingly allowed during coding rounds (OpenAI, IBM, emerging formats). Interviewers watch how you use them: understanding before implementing, not blindly pasting output. Practice thinking out loud while coding, whether you're using AI tools or not. [^exponent-openai] [^khushal-kumar]

At senior levels, depth matters more than speed - Microsoft's senior DSA round was 1+ hour of pure discussion with no code written, covering serialization, compression, streaming formats, and backward compatibility. Interviewers want engineering depth, not typing speed. [^rohit-verma]

Common mistakes:

- Jumping into code without clarifying requirements or asking questions
- Writing rigid code that breaks when follow-up requirements arrive (Anthropic and OpenAI use progressive problems that build on prior code)
- Blindly pasting AI tool output without understanding it - interviewers watch for reasoning, not copying
- Not discussing time/space complexity or optimization when prompted

## Sources

[^datainterview-mistral]: [DataInterview - Mistral ML Engineer Interview](https://www.datainterview.com/blog/mistral-machine-learning-engineer-interview)
[^deepthi-sudharsan]: [Medium - Deepthi Sudharsan](https://medium.com/@deepthi.sudharsan/inside-ai-interviews-stories-patterns-and-what-actually-matters-555684c38598)
[^devto-xai]: [dev.to - xAI](https://dev.to/net_programhelp_e160eef28/xai-software-engineer-interview-2026-full-recap-pitfalls-real-prep-tips-2fl0)
[^exponent-mock]: [YouTube - Exponent Mock Interview](https://www.youtube.com/watch?v=ZE_YEn-okfk)
[^exponent-openai]: [Medium - Exponent, OpenAI](https://medium.com/exponent/what-its-actually-like-to-interview-at-openai-in-2026-03a646c9436c)
[^hello-interview]: [Hello Interview - OpenAI L5](https://www.hellointerview.com/guides/openai/l5)
[^khushal-kumar]: [Medium - Khushal Kumar](https://kaysnotes.medium.com/my-generative-ai-engineer-interview-experience-got-hired-6b3f1affc4e9)
[^linkjob-anthropic]: [linkjob - Anthropic](https://www.linkjob.ai/interview-questions/anthropic-software-engineer-interview/)
[^linkjob-openai]: [linkjob - OpenAI](https://www.linkjob.ai/interview-questions/openai-loop-interview)
[^mimansa-jaiswal]: [Mimansa Jaiswal](https://mimansajaiswal.github.io/posts/llm-ml-job-interviews-resources/)
[^promptlayer]: [PromptLayer](https://blog.promptlayer.com/the-agentic-system-design-interview-how-to-evaluate-ai-engineers/)
[^reddit-2026-prep]: [Reddit - 2026 Interview Prep](https://www.reddit.com/r/leetcode/comments/1q06zz6/2026_interview_prep) (r/leetcode)
[^reddit-ai-eng-questions-2]: [Reddit - AI Engineer Interview Questions, TonyStank-1704 comment](https://www.reddit.com/r/ArtificialInteligence/comments/1nybfr8/ai_engineer_interview_questions/) (r/ArtificialIntelligence)
[^reddit-microsoft-aiml]: [Reddit - Microsoft SWE Applied AI/ML Summer 2026](https://www.reddit.com/r/csMajors/comments/1nqfzhq/microsoft_swe_applied_aiml_summer_2026_redmond) (r/csMajors)
[^reddit-xai-eng]: [Reddit - xAI AI Engineer Backend/Infra Interview](https://www.reddit.com/r/leetcode/comments/1pjhw1i/xai_ai_engineer_backendinfra_interview_just/) (r/leetcode)
[^rohit-verma]: [Medium - Rohit Verma, Microsoft](https://medium.com/@rohitverma_87831/microsoft-senior-engineer-interview-experience-2026-the-offer-that-took-me-three-attempts-e0d6e052bdb1)
[^sundeep-teki]: [Sundeep Teki](https://www.sundeepteki.org/advice/the-ultimate-ai-research-engineer-interview-guide-cracking-openai-anthropic-google-deepmind-top-ai-labs)
[^yuan-meng]: [Yuan Meng](https://www.yuan-meng.com/posts/mle_interviews_2.0/)
