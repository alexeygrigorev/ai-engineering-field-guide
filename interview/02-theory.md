# Theory Questions

Based on candidate reports from Reddit, X, and personal blogs about what they were actually asked in AI engineering interviews. This section covers knowledge-based questions: "What is X?", "How does X work?", "Explain Y."


## Most Common Technical Questions

| Category | Frequency | Example questions |
|----------|-----------|-------------------|
| RAG systems | Very high | "Design a RAG system for customer support chatbot. How do you evaluate it?" |
| Hallucinations | Very high | "How do you detect and mitigate hallucinations in production?" |
| Agents | High | "What's the difference between an agent and a simple LLM chain?" / "What makes a system truly agentic vs. not?" |
| Fine-tuning | Medium | "When would you fine-tune vs. use prompt engineering?" |
| Transformers | Medium | "Explain how Transformers work. Why are they foundational?" |


## LLM Fundamentals Tested at NVIDIA, Google, Amazon

Candidates interviewing at NVIDIA, Google, and Amazon report being tested on foundational LLM concepts that go beyond coding implementations: [^fahd-mirza]

- Model scaling laws - how performance improves with increasing model size, data, and compute. These laws (e.g., Chinchilla scaling) guide decisions about resource allocation and model sizing
- Tokenization strategies - word-level, subword (BPE, WordPiece), and character-level tokenization. BPE builds vocabulary by iteratively merging frequent character pairs; WordPiece is similar but optimizes for likelihood. Understanding trade-offs: subword methods handle out-of-vocabulary words better, character-level suits complex writing systems
- Benchmark datasets - MMLU (massive multitask language understanding across 57 subjects), BigBench (200+ diverse reasoning tasks), HumanEval (functional code generation correctness). Know what each benchmark measures and its limitations

## Nine Interview Categories for AI Research Roles

Dr. Sundeep Teki [^sundeep-teki] identifies these categories for AI labs:

1. Theoretical foundations - linear algebra, calculus, optimization, probability
2. ML coding - implement Multi-Head Attention, full Transformer layers from memory
3. ML debugging - broadcasting errors, dimension mismatches in non-learning models
4. ML system design - distributed training across thousands of GPUs
5. Inference optimization - KV caching, quantization, speculative decoding
6. RAG systems - vector DBs, retrievers, reranking
7. Research discussion - paper analysis, defending own research
8. AI safety & ethics - Constitutional AI, RLHF, red teaming, alignment
9. Behavioral & cultural fit - STAR, mission alignment, metrics

## Company-Specific Technical Questions

### IBM (AI Engineer)

IBM's AI Engineer interviews (for the Watsonx team) are long and cover Python, SQL, Git, ML, and MLOps in depth. Actual questions asked: [^raghu-teja-1]

Python: Memory leaks and garbage collection, class methods vs. static methods, accessing parent class methods via super(), Method Resolution Order in multiple inheritance, debugging Python code in production (logging, monitoring tools - "In production, there will be no VS Code")

SQL: How to optimize SQL queries (select only needed columns, join large tables last, filter/aggregate early, minimize window functions), order of execution in SQL (FROM -> JOIN -> WHERE -> GROUP BY -> HAVING -> SELECT -> DISTINCT -> ORDER BY -> LIMIT)

Git: Git branching strategies for deployment (long-lived vs. short-lived branches), how to perform a rebase, combining multiple feature branches into master, handling merge conflicts

ML/MLOps [^raghu-teja-2]: Explain the full ML deployment workflow (CI/CD/CD, monitoring, feedback), explain quantization, how to implement an AI application from start to finish (from kickoff meeting through deployment), how to decide success metrics for an ML model, handling imbalanced data (oversampling, undersampling, SMOTE, class weighting), difference between RNN and LSTM

### Gen AI Engineer (Startup)

A Gen AI Engineer interview included these LLM/RAG questions: [^khushal-kumar]

- What is a RAG model? Explain the complete process
- What are embeddings?
- How does chunking happen?
- Infrastructure basics: What is Docker? Why use Selenium? Have you heard about Redis?

See [AI System Design](05-ai-system-design.md) for OpenAI, Google, Apple, Anthropic, Cohere, and Salesforce system design questions, seniority expectations, and evaluation frameworks.

## ML Interview Preparation Structure

Mimansa Jaiswal documents a structured approach to preparing for ML/LLM research and engineering interviews across seven areas: [^mimansa-jaiswal]

1. LeetCode: Grind 75 + easy/medium from NeetCode 150, with optimization passes after 2-day breaks
2. ML/DL/LLM coding: Implement from scratch (attention, transformers, decoding strategies)
3. Statistics: Probability, distributions, regression, Bayesian analysis, hypothesis testing (highlighted after a surprise Amazon loop exposed gaps)
4. ML fundamentals: Supervised/unsupervised learning, regularization, clustering, neural network architectures
5. LLM architecture & training: Transformers, tokenization, scaling laws, LoRA/QLoRA, MoE, RLHF/DPO, RAG fundamentals (chunking, BM25, dense retrieval, reranking, evaluation with NDCG/MRR)
6. ML system design: Always present both discriminative and generative approaches, letting interviewers guide direction. Spend up to 10 minutes on clarifying questions
7. Behavioral: STAR method with 30-second segments, distinct examples per interview to avoid sounding mechanical

Notable insight: "MLA became popular while I was interviewing" and "GRPO became popular after interviews" - the field evolves continuously during preparation.

## Questions People Wish They Prepared For

- "How do you evaluate a chatbot?" (not just build one)
- "What happens when the LLM is confidently wrong?" (failure modes)
- "How do you reduce token costs at scale?" (production thinking)
- "Design for 1M users" (scale beyond prototype)
- "How do you debug Python code in production?" [^raghu-teja-1]
- "When is an agentic architecture the wrong solution?" [^techeon]
- "What makes a system truly agentic?" [^techeon]

## Interview Questions

Actual questions reported by candidates and interviewers, compiled from blog posts, video transcripts, and interview guides. Source or company in parentheses where known.

### LLM Fundamentals

- Explain how Transformers work. Why are they foundational to modern AI? [^buildml] [^hn-44875256]
- What is the self-attention mechanism? How does it differ from multi-head attention? [^sundeep-teki]
- What is grouped query attention and how does it differ from standard multi-head attention? [^mimansa-jaiswal]
- What are the differences between BPE, WordPiece, and character-level tokenization? What are the trade-offs? [^fahd-mirza]
- Explain model scaling laws. How do they guide decisions about model size, data, and compute? [^fahd-mirza]
- What is KV cache? How does it help in LLM inference? [^igotanoffer]
- What is the context window and what happens when you exceed it? How do you handle long documents? [^hn-46319888] [^llmgenai]
- How does temperature affect LLM output? What about top-p and top-k sampling? [^llmgenai] [^hn-46319888]
- What are embeddings? How do they represent semantic meaning? [^khushal-kumar]
- Explain the difference between encoder-only, decoder-only, and encoder-decoder Transformer architectures. When would you use each? [^tidorp] [^hn-46319888]
- What is positional encoding and why is it needed in Transformers? [^linkjob-openai]
- What are the key MMLU, BigBench, and HumanEval benchmarks? What does each measure and what are its limitations? [^fahd-mirza]
- What is RLHF and why is it important? Walk through the three-step process. [^proptech-founder]
- What is the difference between RLHF and DPO? When would you prefer one over the other? [^mimansa-jaiswal]
- What is Mixture of Experts (MoE)? How does it improve efficiency? [^mimansa-jaiswal]
- Describe the difference between generative AI and traditional programming in the context of solving a real-world problem. [^proptech-founder]
- How do LLMs actually generate text? Explain the autoregressive decoding process. [^hn-46319888] [^llmgenai]
- What are decoding strategies like beam search, top-k, and top-p? When do you use each? [^mimansa-jaiswal]

### RAG Systems

- Design a RAG system for a customer support chatbot. How do you evaluate it? [^buildml] [^hn-44875256]
- What is a RAG model? Explain the complete process. [^khushal-kumar]
- How does chunking happen? What chunking strategies would you use and why? [^khushal-kumar]
- You have a financial report where page 1 says "all amounts in thousands." How do you handle document-wide context when chunking page by page? [^proptech-founder]
- What is hybrid search? When would you combine vector search with keyword search (BM25)? [^designgurus-rag]
- What is re-ranking and why is it needed on top of vector retrieval? Explain cross-encoder vs. bi-encoder. [^designgurus-rag]
- How do you scale a RAG system to 10M+ articles? Discuss sharding, caching, and retrieval optimization. [^bhavishya-pandit]
- Design a document Q&A assistant. Walk through ingestion, retrieval, reranking, and confidence thresholds. [^bhavishya-pandit]
- Your RAG system returns relevant documents but users still can't find the answer. How do you transform it from a search engine into an answer engine? [^hitendra-patel]
- How do you evaluate a RAG pipeline? What metrics would you use? (NDCG, MRR, precision@k, recall) [^mimansa-jaiswal]
- How do you handle citations and source attribution in a RAG system? [^proptech-founder]
- What vector databases have you used? Compare FAISS, Pinecone, Weaviate, Milvus, and Qdrant. [^promptlayer] [^llmgenai]
- How does Approximate Nearest Neighbor (ANN) search work? Explain HNSW indexing. [^designgurus-rag]
- Where do embeddings fail? Discuss negation, temporal reasoning, and precision requirements. [^techeon]
- What is semantic caching and how can it reduce cost and latency in a RAG system? [^designgurus-rag]

### Agents & Tool Use

- What is an AI agent and what is its role in a broader system? [^proptech-founder]
- What's the difference between an agent and a simple LLM chain? [^hn-44875256]
- What makes a system truly agentic vs. not? What doesn't qualify? [^techeon]
- When is an agentic architecture the wrong solution? Give specific examples. [^techeon]
- Architect an AI agent system, including the agent loop, tool interfaces, memory design, orchestration, and safety considerations. [^igotanoffer]
- How do you define and enforce agent autonomy boundaries? (senior/staff level) [^techeon]
- What are the essential components of an agent beyond the LLM? (senior/staff level) [^techeon]
- How do you prevent agents from over-reasoning or getting stuck in planning loops? [^techeon]
- How do agents decide which tool to use? Walk through tool selection, schema design, and hallucinated action prevention. [^techeon]
- How do you sandbox tool execution safely? Discuss isolation, credential scoping, and resource limits. [^techeon]
- How do you handle tool failures, retries, and idempotency in an agent system? [^techeon]
- How do agents decide a task is "done"? What termination conditions do you implement? [^techeon]
- What logic belongs in the orchestrator vs. the LLM? [^techeon]
- Stateless vs. stateful agents - what are the tradeoffs and when would you use each? [^techeon]
- What types of memory do agentic systems need? Describe working, episodic, semantic, and procedural memory. [^techeon]
- How do you design long-term memory without polluting it? [^techeon]
- Chain-of-thought vs. tree-of-thought vs. graph planning - when would you use each? [^techeon]
- How do you explain agentic systems to non-technical stakeholders? [^techeon]
- What are the biggest security risks with tool-using agents? (prompt injection through tool outputs, privilege escalation, data exfiltration) [^techeon]

### Fine-tuning & Training

- When would you fine-tune vs. use prompt engineering? What about RAG vs. fine-tuning? [^promptlayer] [^llmgenai]
- Design a model that can solve math problems - walk through data collection, SFT, post-training, and evaluation. [^igotanoffer]
- What is LoRA? How does it reduce the cost of fine-tuning? What about QLoRA? [^mimansa-jaiswal]
- Explain the RLHF pipeline: supervised fine-tuning, reward model training, and PPO. How does DPO simplify this? [^proptech-founder]
- What is instruction tuning and how does it differ from pre-training? [^hn-46319888] [^llmgenai]
- Explain quantization. What are the trade-offs between model size, speed, and accuracy? [^raghu-teja-2]
- Design a distributed training system for deep learning. Discuss data parallelism, model parallelism, and tensor parallelism. [^designgurus]
- What is speculative decoding and how does it speed up inference? [^sundeep-teki]
- How do you convert implicit user behavior (edits, acceptance, rejection) into training signals for model improvement? [^bhavishya-pandit]
- How do you version and roll back agent or model behavior in production? [^techeon]

### Evaluation & Metrics

- How do you evaluate a chatbot? (not just build one) [^hn-41271833] [^hn-44875256]
- What metrics do you consider when benchmarking and evaluating LLM performance? [^proptech-founder]
- How do you detect and mitigate hallucinations in production? [^buildml] [^hn-45904921]
- What happens when the LLM is confidently wrong? How do you handle failure modes? [^hn-45904921] [^llmgenai]
- Design a hallucination-free banking chatbot. How do you separate generative interfaces from factual data systems? [^bhavishya-pandit]
- What is time to first token and why does it matter for user experience? [^proptech-founder]
- How do you measure hallucination rate in production? [^buildml] [^llmgenai]
- What is "vibes-based" evaluation vs. a formal eval framework? How do you build proper evals? [^exponent-openai]
- How do you build a golden dataset for evaluation? How do you use it for regression testing? [^proptech-founder]
- How does the system get better over time? Describe feedback and reinforcement loops. [^interviewnode]
- What planning failures are hardest to detect in production? (silent wrong answers, goal drift, assumption propagation) [^techeon]
- How do you decide success metrics for an ML model? [^raghu-teja-2]

### ML Fundamentals

- Explain the difference between RNN and LSTM. [^raghu-teja-2]
- How do you handle imbalanced data? Discuss oversampling, undersampling, SMOTE, and class weighting. [^raghu-teja-2]
- Debug a model that runs but doesn't learn. Identify broadcasting errors and dimension mismatches. [^sundeep-teki]
- Statistics questions: probability, distributions, regression, Bayesian analysis, hypothesis testing. [^mimansa-jaiswal]
- Explain supervised vs. unsupervised learning. When would you use each? [^hn-29876742] [^tidorp]
- What is regularization? Compare L1, L2, and dropout. [^hn-29876742] [^tidorp]
- Explain SHAP and LIME for model interpretability. [^fahd-mirza-2] [^tidorp]

### Python & Software Engineering

- Explain memory leaks and garbage collection in Python. [^raghu-teja-1]
- What is the difference between class methods and static methods? [^raghu-teja-1]
- Explain super() and Method Resolution Order in multiple inheritance. [^raghu-teja-1]
- How do you debug Python code in production? "In production, there will be no VS Code." [^raghu-teja-1]
- Explain concurrency and parallelism in Python. What is the Global Interpreter Lock (GIL)? [^proptech-founder]
- How do you use asyncio for concurrent I/O in Python? When would you use threading vs. multiprocessing instead? [^proptech-founder]
- How do you optimize SQL queries? Explain the order of execution in SQL. [^raghu-teja-1]
- Explain SQL vs. NoSQL databases for AI workloads. When would you use each? [^fahd-mirza-2]
- What are Git branching strategies for deployment? How do you perform a rebase? How do you handle merge conflicts? [^raghu-teja-1]
- Explain the JavaScript event loop. (full-stack AI roles) [^proptech-founder]
- What steps would you take to diagnose performance bugs in a model or application? [^fahd-mirza-2]
- Have you worked with real-time communication technologies like WebRTC? (AI roles with live features) [^fahd-mirza-2]
- What is Redis? Why would you use it in an AI application? [^khushal-kumar]
- Describe a challenging prompt engineering problem that you solved. What techniques did you use? [^proptech-founder]

### Cost & Latency Optimization

- Your app gets 1M queries/day - how do you optimize cost? [^buildml] [^zen-van-riel]
- How do you reduce token costs at scale? [^zen-van-riel] [^llmgenai]
- By trimming prompts and caching embeddings, how would you reduce API spend? Walk through a before-and-after cost breakdown. (top interview answer) [^fonzi-ai]
- Explain multi-layer caching strategies: retrieval cache, prompt cache, and response cache. [^interviewnode]
- What is model tiering? When do you route to a small distilled model vs. a large LLM? [^interviewnode]
- What is prompt compression and how does it reduce cost? [^llmgenai] [^hn-46319888]
- How do you control cost explosions from agent tool calls? Discuss session budgets, per-operation limits, and circuit breakers. [^techeon]
- Latency vs. throughput optimization for LLM serving - what are the trade-offs? [^youtube-short]
- How would you design a scalable and reliable automation workflow? What considerations for error handling, monitoring, and debugging? [^proptech-founder]
- Describe a time you optimized an existing process for efficiency or scalability. What was the bottleneck and how did you find it? [^proptech-founder]
- How would you benchmark each LLM call in a multi-step pipeline to identify latency bottlenecks? [^proptech-founder]

### Safety, Guardrails & Ethics

- How do you ensure the outputs from LLMs are consistent and accurate in complex multi-step workflows? [^proptech-founder]
- When and how would you implement LLM guardrails? Discuss input filtering, output validation, and PII detection. [^proptech-founder]
- How do you handle prompt injection attacks? [^llmgenai]
- Design a legal contract generation system with compliance requirements. How do you prevent the LLM from inventing legal content? [^bhavishya-pandit]
- Design a hospital voice assistant. How do you handle noise, privacy, latency, and domain-specific vocabulary? [^bhavishya-pandit]
- What are the biggest security risks with tool-using agents? Discuss prompt injection through tool outputs, privilege escalation, data exfiltration, and confused deputy attacks. [^techeon]
- What is Constitutional AI? How does it relate to alignment and safety? [^sundeep-teki]
- How do you red-team an LLM system? [^sundeep-teki]
- How do you handle partial observability or missing information in agent systems? What do you do when the agent doesn't have enough context? [^techeon]
- Your application generates code that gets executed. How do you prevent malicious code generation and execution? [^proptech-founder]


## Sources

[^fahd-mirza]: [YouTube - Fahd Mirza](https://www.youtube.com/watch?v=Zt-h5BiBWH0)
[^fahd-mirza-2]: [YouTube - Fahd Mirza](https://www.youtube.com/watch?v=fahd-mirza-upwork)
[^sundeep-teki]: [Sundeep Teki](https://www.sundeepteki.org/advice/the-ultimate-ai-research-engineer-interview-guide-cracking-openai-anthropic-google-deepmind-top-ai-labs)
[^raghu-teja-1]: [Medium - Raghu Teja, IBM Part 1](https://medium.com/@raghu_teja/how-i-cracked-my-ibm-ai-engineer-interview-part-1-technical-e7e4f73be5c4)
[^raghu-teja-2]: [Medium - Raghu Teja, IBM Part 2](https://medium.com/@raghu_teja/how-i-cracked-my-ibm-ai-engineer-interview-part-2-ml-scenarios-88af2b46282e)
[^khushal-kumar]: [Medium - Khushal Kumar](https://medium.com/@khushalkumar21/my-generative-ai-engineer-interview-experience-got-hired-61a1299ff390)
[^mimansa-jaiswal]: [Mimansa Jaiswal](https://mimansajaiswal.github.io/posts/llm-ml-job-interviews-resources/)
[^techeon]: [Medium - TechEon Agentic Guide](https://atul4u.medium.com/the-complete-agentic-ai-system-design-interview-guide-2026-f95d0cfeb7cf)
[^buildml]: [BuildML](https://buildml.substack.com/p/top-24-llm-questions-asked-at-deepmind)
[^hn-44875256]: [HN - AI Product Engineering Interview Questions](https://news.ycombinator.com/item?id=44875256)
[^hn-46319888]: [HN - LLM Interview Questions](https://news.ycombinator.com/item?id=46319888)
[^hn-41271833]: [HN - Eugene Yan Interview Guide](https://news.ycombinator.com/item?id=41271833)
[^hn-45904921]: [HN - Tech Interview in Late 2025](https://news.ycombinator.com/item?id=45904921)
[^hn-29876742]: [HN - Deep Learning Interviews Book](https://news.ycombinator.com/item?id=29876742)
[^igotanoffer]: [igotanoffer - Generative AI System Design Interview](https://igotanoffer.com/en/advice/generative-ai-system-design-interview)
[^interviewnode]: [InterviewNode - GenAI System Design Patterns](https://www.interviewnode.com/post/generative-ai-system-design-interview-patterns-you-should-know)
[^llmgenai]: [GitHub - LLM Interview Questions](https://github.com/llmgenai/LLMInterviewQuestions)
[^tidorp]: [GitHub - TidorP/MLJobSearch2025](https://github.com/TidorP/MLJobSearch2025)
[^linkjob-openai]: [linkjob - OpenAI](https://www.linkjob.ai/interview-questions/openai-loop-interview)
[^promptlayer]: [PromptLayer](https://blog.promptlayer.com/the-agentic-system-design-interview-how-to-evaluate-ai-engineers/)
[^designgurus]: [DesignGurus - OpenAI System Design](https://www.designgurus.io/blog/openai-system-design-interview-questions)
[^designgurus-rag]: [DesignGurus - RAG System Design](https://www.designgurus.io/blog/system-design-for-rag)
[^bhavishya-pandit]: [Bhavishya Pandit](https://bhavishyapandit9.substack.com/p/7-deep-cut-ai-system-design-interview)
[^hitendra-patel]: [Medium - Hitendra Patel](https://medium.com/@hitendrapatel)
[^exponent-openai]: [Medium - Exponent, OpenAI](https://medium.com/exponent/what-its-actually-like-to-interview-at-openai-in-2026-03a646c9436c)
[^proptech-founder]: [YouTube - Proptech Founder](https://www.youtube.com/watch?v=proptech-founder-interview)
[^youtube-short]: [YouTube Short](https://www.youtube.com/shorts/Nc1y9tYV2WM)
[^zen-van-riel]: [Zen Van Riel](https://zenvanriel.com/ai-engineer-blog/ai-engineering-interview-big-tech-guide/)
[^fonzi-ai]: [Medium - Fonzi AI](https://medium.com/fonzi-ai)
