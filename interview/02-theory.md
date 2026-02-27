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

Candidates interviewing at NVIDIA, Google, and Amazon report being tested on foundational LLM concepts that go beyond coding implementations ([Fahd Mirza](https://www.youtube.com/watch?v=Zt-h5BiBWH0)):

- **Model scaling laws** - how performance improves with increasing model size, data, and compute. These laws (e.g., Chinchilla scaling) guide decisions about resource allocation and model sizing
- **Tokenization strategies** - word-level, subword (BPE, WordPiece), and character-level tokenization. BPE builds vocabulary by iteratively merging frequent character pairs; WordPiece is similar but optimizes for likelihood. Understanding trade-offs: subword methods handle out-of-vocabulary words better, character-level suits complex writing systems
- **Benchmark datasets** - MMLU (massive multitask language understanding across 57 subjects), BigBench (200+ diverse reasoning tasks), HumanEval (functional code generation correctness). Know what each benchmark measures and its limitations

## Nine Interview Categories for AI Research Roles

[Dr. Sundeep Teki](https://www.sundeepteki.org/advice/the-ultimate-ai-research-engineer-interview-guide-cracking-openai-anthropic-google-deepmind-top-ai-labs) identifies these categories for AI labs (OpenAI, Anthropic, DeepMind):

1. **Theoretical foundations** - linear algebra, calculus, optimization, probability
2. **ML coding** - implement Multi-Head Attention, full Transformer layers from memory
3. **ML debugging** - broadcasting errors, dimension mismatches in non-learning models
4. **ML system design** - distributed training across thousands of GPUs
5. **Inference optimization** - KV caching, quantization, speculative decoding
6. **RAG systems** - vector DBs, retrievers, reranking
7. **Research discussion** - paper analysis, defending own research
8. **AI safety & ethics** - Constitutional AI, RLHF, red teaming, alignment
9. **Behavioral & cultural fit** - STAR, mission alignment, metrics

## Company-Specific Technical Questions

### IBM (AI Engineer)

IBM's AI Engineer interviews (for the Watsonx team) are long and cover Python, SQL, Git, ML, and MLOps in depth. Actual questions asked ([source](https://medium.com/@raghu_teja/how-i-cracked-my-ibm-ai-engineer-interview-part-1-technical-e7e4f73be5c4)):

**Python**: Memory leaks and garbage collection, class methods vs. static methods, accessing parent class methods via super(), Method Resolution Order in multiple inheritance, debugging Python code in production (logging, monitoring tools -- "In production, there will be no VS Code")

**SQL**: How to optimize SQL queries (select only needed columns, join large tables last, filter/aggregate early, minimize window functions), order of execution in SQL (FROM -> JOIN -> WHERE -> GROUP BY -> HAVING -> SELECT -> DISTINCT -> ORDER BY -> LIMIT)

**Git**: Git branching strategies for deployment (long-lived vs. short-lived branches), how to perform a rebase, combining multiple feature branches into master, handling merge conflicts

**ML/MLOps** ([source](https://medium.com/@raghu_teja/how-i-cracked-my-ibm-ai-engineer-interview-part-2-ml-scenarios-88af2b46282e)): Explain the full ML deployment workflow (CI/CD/CD, monitoring, feedback), explain quantization, how to implement an AI application from start to finish (from kickoff meeting through deployment), how to decide success metrics for an ML model, handling imbalanced data (oversampling, undersampling, SMOTE, class weighting), difference between RNN and LSTM

### Gen AI Engineer (Startup)

A Gen AI Engineer interview included these LLM/RAG questions ([source](https://medium.com/@khushalkumar21/my-generative-ai-engineer-interview-experience-got-hired-61a1299ff390)):

- What is a RAG model? Explain the complete process
- What are embeddings?
- How does chunking happen?
- Infrastructure basics: What is Docker? Why use Selenium? Have you heard about Redis?

See [AI System Design](05-ai-system-design.md) for OpenAI, Google, Apple, Anthropic, Cohere, and Salesforce system design questions, seniority expectations, and evaluation frameworks.

## ML Interview Preparation Structure

Mimansa Jaiswal documents a structured approach to preparing for ML/LLM research and engineering interviews across seven areas ([source](https://mimansajaiswal.github.io/posts/llm-ml-job-interviews-resources/)):

1. **LeetCode**: Grind 75 + easy/medium from NeetCode 150, with optimization passes after 2-day breaks
2. **ML/DL/LLM coding**: Implement from scratch (attention, transformers, decoding strategies)
3. **Statistics**: Probability, distributions, regression, Bayesian analysis, hypothesis testing (highlighted after a surprise Amazon loop exposed gaps)
4. **ML fundamentals**: Supervised/unsupervised learning, regularization, clustering, neural network architectures
5. **LLM architecture & training**: Transformers, tokenization, scaling laws, LoRA/QLoRA, MoE, RLHF/DPO, RAG fundamentals (chunking, BM25, dense retrieval, reranking, evaluation with NDCG/MRR)
6. **ML system design**: Always present both discriminative and generative approaches, letting interviewers guide direction. Spend up to 10 minutes on clarifying questions
7. **Behavioral**: STAR method with 30-second segments, distinct examples per interview to avoid sounding mechanical

Notable insight: "MLA became popular while I was interviewing" and "GRPO became popular after interviews" -- the field evolves continuously during preparation.

## Questions People Wish They Prepared For

- "How do you evaluate a chatbot?" (not just build one)
- "What happens when the LLM is confidently wrong?" (failure modes)
- "How do you reduce token costs at scale?" (production thinking)
- "Design for 1M users" (scale beyond prototype)
- "How do you debug Python code in production?" -- follow-up: "There's no VS Code in production" (IBM asked this, tripping up a candidate with analytics background) ([source](https://medium.com/@raghu_teja/how-i-cracked-my-ibm-ai-engineer-interview-part-1-technical-e7e4f73be5c4))
- Statistics questions in an ML interview loop (a surprise Amazon round exposed preparation gaps for a candidate focused on LLM/NLP) ([source](https://mimansajaiswal.github.io/posts/llm-ml-job-interviews-resources/))
- "When is an agentic architecture the wrong solution?" -- interviewers want to hear you say agents are wrong when: the task is a deterministic workflow (use Temporal/Airflow instead), failures are catastrophic and irreversible, latency SLA is under 200ms, perfect accuracy is required, or you can't define termination conditions. "The best agent architectures started as traditional systems and evolved agentic capabilities only where flexibility genuinely mattered." ([TechEon](https://atul4u.medium.com/the-complete-agentic-ai-system-design-interview-guide-2026-f95d0cfeb7cf))
- "What makes a system truly agentic?" -- key distinguishing criteria: goal-directed autonomy (determines its own path to a high-level objective), environmental interaction (uses tools, reads results, adapts behavior), and temporal extension (maintains goals across multiple steps). What doesn't qualify: RAG pipelines, single-turn function calling, workflow automation with hardcoded paths, chatbots with personality. "Agentic is a spectrum, not a binary" -- knowing where to place a system on that spectrum is a design choice ([TechEon](https://atul4u.medium.com/the-complete-agentic-ai-system-design-interview-guide-2026-f95d0cfeb7cf))

## Interview Questions

Actual questions reported by candidates and interviewers, compiled from blog posts, video transcripts, and interview guides. Source or company in parentheses where known.

### LLM Fundamentals

- Explain how Transformers work. Why are they foundational to modern AI? (commonly asked across companies)
- What is the self-attention mechanism? How does it differ from multi-head attention? (OpenAI, Anthropic, DeepMind -- [Sundeep Teki](https://www.sundeepteki.org/advice/the-ultimate-ai-research-engineer-interview-guide-cracking-openai-anthropic-google-deepmind-top-ai-labs))
- What is grouped query attention and how does it differ from standard multi-head attention? ([Mimansa Jaiswal](https://mimansajaiswal.github.io/posts/llm-ml-job-interviews-resources/))
- What are the differences between BPE, WordPiece, and character-level tokenization? What are the trade-offs? (NVIDIA, Google, Amazon -- [Fahd Mirza](https://www.youtube.com/watch?v=Zt-h5BiBWH0))
- Explain model scaling laws. How do they guide decisions about model size, data, and compute? (NVIDIA, Google, Amazon -- [Fahd Mirza](https://www.youtube.com/watch?v=Zt-h5BiBWH0))
- What is KV cache? How does it help in LLM inference? (Apple -- [igotanoffer](https://igotanoffer.com/en/advice/generative-ai-system-design-interview))
- What is the context window and what happens when you exceed it? How do you handle long documents? (commonly asked)
- How does temperature affect LLM output? What about top-p and top-k sampling? (commonly asked)
- What are embeddings? How do they represent semantic meaning? (startup Gen AI Engineer interview -- [Khushal Kumar](https://medium.com/@khushalkumar21/my-generative-ai-engineer-interview-experience-got-hired-61a1299ff390))
- Explain the difference between encoder-only, decoder-only, and encoder-decoder Transformer architectures. When would you use each? (commonly asked)
- What is positional encoding and why is it needed in Transformers? (OpenAI asks candidates to fix position embedding bugs -- [LinkJob](https://www.linkjob.ai/interview-questions/openai-loop-interview))
- What are the key MMLU, BigBench, and HumanEval benchmarks? What does each measure and what are its limitations? (NVIDIA, Google, Amazon -- [Fahd Mirza](https://www.youtube.com/watch?v=Zt-h5BiBWH0))
- What is RLHF and why is it important? Walk through the three-step process. ([proptech founder](https://www.youtube.com/watch?v=proptech-founder-interview))
- What is the difference between RLHF and DPO? When would you prefer one over the other? ([Mimansa Jaiswal](https://mimansajaiswal.github.io/posts/llm-ml-job-interviews-resources/))
- What is Mixture of Experts (MoE)? How does it improve efficiency? ([Mimansa Jaiswal](https://mimansajaiswal.github.io/posts/llm-ml-job-interviews-resources/))
- Describe the difference between generative AI and traditional programming in the context of solving a real-world problem. ([proptech founder](https://www.youtube.com/watch?v=proptech-founder-interview))
- How do LLMs actually generate text? Explain the autoregressive decoding process. (commonly asked)
- What are decoding strategies like beam search, top-k, and top-p? When do you use each? ([Mimansa Jaiswal](https://mimansajaiswal.github.io/posts/llm-ml-job-interviews-resources/))

### RAG Systems

- Design a RAG system for a customer support chatbot. How do you evaluate it? (commonly asked -- very high frequency)
- What is a RAG model? Explain the complete process. (startup Gen AI Engineer -- [Khushal Kumar](https://medium.com/@khushalkumar21/my-generative-ai-engineer-interview-experience-got-hired-61a1299ff390))
- How does chunking happen? What chunking strategies would you use and why? (startup Gen AI Engineer -- [Khushal Kumar](https://medium.com/@khushalkumar21/my-generative-ai-engineer-interview-experience-got-hired-61a1299ff390))
- You have a financial report where page 1 says "all amounts in thousands." How do you handle document-wide context when chunking page by page? ([proptech founder](https://www.youtube.com/watch?v=proptech-founder-interview))
- What is hybrid search? When would you combine vector search with keyword search (BM25)? ([DesignGurus](https://www.designgurus.io/blog/system-design-for-rag))
- What is re-ranking and why is it needed on top of vector retrieval? Explain cross-encoder vs. bi-encoder. ([DesignGurus](https://www.designgurus.io/blog/system-design-for-rag))
- How do you scale a RAG system to 10M+ articles? Discuss sharding, caching, and retrieval optimization. ([Bhavishya Pandit](https://bhavishyapandit9.substack.com/p/7-deep-cut-ai-system-design-interview))
- Design a document Q&A assistant. Walk through ingestion, retrieval, reranking, and confidence thresholds. ([Bhavishya Pandit](https://bhavishyapandit9.substack.com/p/7-deep-cut-ai-system-design-interview))
- Your RAG system returns relevant documents but users still can't find the answer. How do you transform it from a search engine into an answer engine? ([Hitendra Patel](https://medium.com/@hitendrapatel))
- How do you evaluate a RAG pipeline? What metrics would you use? (NDCG, MRR, precision@k, recall -- [Mimansa Jaiswal](https://mimansajaiswal.github.io/posts/llm-ml-job-interviews-resources/))
- How do you handle citations and source attribution in a RAG system? ([proptech founder](https://www.youtube.com/watch?v=proptech-founder-interview))
- What vector databases have you used? Compare FAISS, Pinecone, Weaviate, Milvus, and Qdrant. (commonly asked)
- How does Approximate Nearest Neighbor (ANN) search work? Explain HNSW indexing. ([DesignGurus](https://www.designgurus.io/blog/system-design-for-rag))
- Where do embeddings fail? Discuss negation, temporal reasoning, and precision requirements. ([TechEon](https://atul4u.medium.com/the-complete-agentic-ai-system-design-interview-guide-2026-f95d0cfeb7cf))
- What is semantic caching and how can it reduce cost and latency in a RAG system? ([DesignGurus](https://www.designgurus.io/blog/system-design-for-rag))

### Agents & Tool Use

- What is an AI agent and what is its role in a broader system? ([proptech founder](https://www.youtube.com/watch?v=proptech-founder-interview))
- What's the difference between an agent and a simple LLM chain? (commonly asked -- high frequency)
- What makes a system truly agentic vs. not? What doesn't qualify? (commonly asked -- [TechEon](https://atul4u.medium.com/the-complete-agentic-ai-system-design-interview-guide-2026-f95d0cfeb7cf))
- When is an agentic architecture the wrong solution? Give specific examples. ([TechEon](https://atul4u.medium.com/the-complete-agentic-ai-system-design-interview-guide-2026-f95d0cfeb7cf))
- Architect an AI agent system, including the agent loop, tool interfaces, memory design, orchestration, and safety considerations. (Salesforce -- [igotanoffer](https://igotanoffer.com/en/advice/generative-ai-system-design-interview))
- How do you define and enforce agent autonomy boundaries? (senior/staff level -- [TechEon](https://atul4u.medium.com/the-complete-agentic-ai-system-design-interview-guide-2026-f95d0cfeb7cf))
- What are the essential components of an agent beyond the LLM? (senior/staff level -- [TechEon](https://atul4u.medium.com/the-complete-agentic-ai-system-design-interview-guide-2026-f95d0cfeb7cf))
- How do you prevent agents from over-reasoning or getting stuck in planning loops? ([TechEon](https://atul4u.medium.com/the-complete-agentic-ai-system-design-interview-guide-2026-f95d0cfeb7cf))
- How do agents decide which tool to use? Walk through tool selection, schema design, and hallucinated action prevention. ([TechEon](https://atul4u.medium.com/the-complete-agentic-ai-system-design-interview-guide-2026-f95d0cfeb7cf))
- How do you sandbox tool execution safely? Discuss isolation, credential scoping, and resource limits. ([TechEon](https://atul4u.medium.com/the-complete-agentic-ai-system-design-interview-guide-2026-f95d0cfeb7cf))
- How do you handle tool failures, retries, and idempotency in an agent system? ([TechEon](https://atul4u.medium.com/the-complete-agentic-ai-system-design-interview-guide-2026-f95d0cfeb7cf))
- How do agents decide a task is "done"? What termination conditions do you implement? ([TechEon](https://atul4u.medium.com/the-complete-agentic-ai-system-design-interview-guide-2026-f95d0cfeb7cf))
- What logic belongs in the orchestrator vs. the LLM? ([TechEon](https://atul4u.medium.com/the-complete-agentic-ai-system-design-interview-guide-2026-f95d0cfeb7cf))
- Stateless vs. stateful agents -- what are the tradeoffs and when would you use each? ([TechEon](https://atul4u.medium.com/the-complete-agentic-ai-system-design-interview-guide-2026-f95d0cfeb7cf))
- What types of memory do agentic systems need? Describe working, episodic, semantic, and procedural memory. ([TechEon](https://atul4u.medium.com/the-complete-agentic-ai-system-design-interview-guide-2026-f95d0cfeb7cf))
- How do you design long-term memory without polluting it? ([TechEon](https://atul4u.medium.com/the-complete-agentic-ai-system-design-interview-guide-2026-f95d0cfeb7cf))
- Chain-of-thought vs. tree-of-thought vs. graph planning -- when would you use each? ([TechEon](https://atul4u.medium.com/the-complete-agentic-ai-system-design-interview-guide-2026-f95d0cfeb7cf))
- How do you explain agentic systems to non-technical stakeholders? ([TechEon](https://atul4u.medium.com/the-complete-agentic-ai-system-design-interview-guide-2026-f95d0cfeb7cf))
- What are the biggest security risks with tool-using agents? (prompt injection through tool outputs, privilege escalation, data exfiltration -- [TechEon](https://atul4u.medium.com/the-complete-agentic-ai-system-design-interview-guide-2026-f95d0cfeb7cf))

### Fine-tuning & Training

- When would you fine-tune vs. use prompt engineering? What about RAG vs. fine-tuning? (commonly asked -- medium frequency)
- Design a model that can solve math problems -- walk through data collection, SFT, post-training, and evaluation. (Cohere -- [igotanoffer](https://igotanoffer.com/en/advice/generative-ai-system-design-interview))
- What is LoRA? How does it reduce the cost of fine-tuning? What about QLoRA? ([Mimansa Jaiswal](https://mimansajaiswal.github.io/posts/llm-ml-job-interviews-resources/))
- Explain the RLHF pipeline: supervised fine-tuning, reward model training, and PPO. How does DPO simplify this? ([proptech founder](https://www.youtube.com/watch?v=proptech-founder-interview))
- What is instruction tuning and how does it differ from pre-training? (commonly asked)
- Explain quantization. What are the trade-offs between model size, speed, and accuracy? (IBM -- [Raghu Teja](https://medium.com/@raghu_teja/how-i-cracked-my-ibm-ai-engineer-interview-part-2-ml-scenarios-88af2b46282e))
- Design a distributed training system for deep learning. Discuss data parallelism, model parallelism, and tensor parallelism. (OpenAI -- [DesignGurus](https://www.designgurus.io/blog/openai-system-design-interview-questions))
- What is speculative decoding and how does it speed up inference? ([Sundeep Teki](https://www.sundeepteki.org/advice/the-ultimate-ai-research-engineer-interview-guide-cracking-openai-anthropic-google-deepmind-top-ai-labs))
- How do you convert implicit user behavior (edits, acceptance, rejection) into training signals for model improvement? ([Bhavishya Pandit](https://bhavishyapandit9.substack.com/p/7-deep-cut-ai-system-design-interview))
- How do you version and roll back agent or model behavior in production? ([TechEon](https://atul4u.medium.com/the-complete-agentic-ai-system-design-interview-guide-2026-f95d0cfeb7cf))

### Evaluation & Metrics

- How do you evaluate a chatbot? (not just build one -- commonly asked)
- What metrics do you consider when benchmarking and evaluating LLM performance? ([proptech founder](https://www.youtube.com/watch?v=proptech-founder-interview))
- How do you detect and mitigate hallucinations in production? (commonly asked -- very high frequency)
- What happens when the LLM is confidently wrong? How do you handle failure modes? (commonly asked)
- Design a hallucination-free banking chatbot. How do you separate generative interfaces from factual data systems? ([Bhavishya Pandit](https://bhavishyapandit9.substack.com/p/7-deep-cut-ai-system-design-interview))
- What is time to first token and why does it matter for user experience? ([proptech founder](https://www.youtube.com/watch?v=proptech-founder-interview))
- How do you measure hallucination rate in production? (commonly asked)
- What is "vibes-based" evaluation vs. a formal eval framework? How do you build proper evals? (OpenAI interviewers probe this -- [Exponent](https://medium.com/exponent/what-its-actually-like-to-interview-at-openai-in-2026-03a646c9436c))
- How do you build a golden dataset for evaluation? How do you use it for regression testing? ([proptech founder](https://www.youtube.com/watch?v=proptech-founder-interview))
- How does the system get better over time? Describe feedback and reinforcement loops. (OpenAI, Anthropic, Meta AI -- [InterviewNode](https://www.interviewnode.com/post/generative-ai-system-design-interview-patterns-you-should-know))
- What planning failures are hardest to detect in production? (silent wrong answers, goal drift, assumption propagation -- [TechEon](https://atul4u.medium.com/the-complete-agentic-ai-system-design-interview-guide-2026-f95d0cfeb7cf))
- How do you decide success metrics for an ML model? (IBM -- [Raghu Teja](https://medium.com/@raghu_teja/how-i-cracked-my-ibm-ai-engineer-interview-part-2-ml-scenarios-88af2b46282e))

### ML Fundamentals

- Explain the difference between RNN and LSTM. (IBM -- [Raghu Teja](https://medium.com/@raghu_teja/how-i-cracked-my-ibm-ai-engineer-interview-part-2-ml-scenarios-88af2b46282e))
- How do you handle imbalanced data? Discuss oversampling, undersampling, SMOTE, and class weighting. (IBM -- [Raghu Teja](https://medium.com/@raghu_teja/how-i-cracked-my-ibm-ai-engineer-interview-part-2-ml-scenarios-88af2b46282e))
- Debug a model that runs but doesn't learn. Identify broadcasting errors and dimension mismatches. (OpenAI, Anthropic, DeepMind -- [Sundeep Teki](https://www.sundeepteki.org/advice/the-ultimate-ai-research-engineer-interview-guide-cracking-openai-anthropic-google-deepmind-top-ai-labs))
- Statistics questions: probability, distributions, regression, Bayesian analysis, hypothesis testing. (Amazon -- surprise round reported by [Mimansa Jaiswal](https://mimansajaiswal.github.io/posts/llm-ml-job-interviews-resources/))
- Explain supervised vs. unsupervised learning. When would you use each? (commonly asked)
- What is regularization? Compare L1, L2, and dropout. (commonly asked)
- Explain SHAP and LIME for model interpretability. (commonly asked -- [Fahd Mirza](https://www.youtube.com/watch?v=fahd-mirza-upwork))

### Python & Software Engineering

- Explain memory leaks and garbage collection in Python. (IBM -- [Raghu Teja](https://medium.com/@raghu_teja/how-i-cracked-my-ibm-ai-engineer-interview-part-1-technical-e7e4f73be5c4))
- What is the difference between class methods and static methods? (IBM -- [Raghu Teja](https://medium.com/@raghu_teja/how-i-cracked-my-ibm-ai-engineer-interview-part-1-technical-e7e4f73be5c4))
- Explain super() and Method Resolution Order in multiple inheritance. (IBM -- [Raghu Teja](https://medium.com/@raghu_teja/how-i-cracked-my-ibm-ai-engineer-interview-part-1-technical-e7e4f73be5c4))
- How do you debug Python code in production? "In production, there will be no VS Code." (IBM -- [Raghu Teja](https://medium.com/@raghu_teja/how-i-cracked-my-ibm-ai-engineer-interview-part-1-technical-e7e4f73be5c4))
- Explain concurrency and parallelism in Python. What is the Global Interpreter Lock (GIL)? ([proptech founder](https://www.youtube.com/watch?v=proptech-founder-interview))
- How do you use asyncio for concurrent I/O in Python? When would you use threading vs. multiprocessing instead? (commonly asked)
- How do you optimize SQL queries? Explain the order of execution in SQL. (IBM -- [Raghu Teja](https://medium.com/@raghu_teja/how-i-cracked-my-ibm-ai-engineer-interview-part-1-technical-e7e4f73be5c4))
- Explain SQL vs. NoSQL databases for AI workloads. When would you use each? ([Fahd Mirza](https://www.youtube.com/watch?v=fahd-mirza-upwork))
- What are Git branching strategies for deployment? How do you perform a rebase? How do you handle merge conflicts? (IBM -- [Raghu Teja](https://medium.com/@raghu_teja/how-i-cracked-my-ibm-ai-engineer-interview-part-1-technical-e7e4f73be5c4))
- Explain the JavaScript event loop. (commonly asked in full-stack AI roles -- [proptech founder](https://www.youtube.com/watch?v=proptech-founder-interview))
- What steps would you take to diagnose performance bugs in a model or application? ([Fahd Mirza](https://www.youtube.com/watch?v=fahd-mirza-upwork))
- Have you worked with real-time communication technologies like WebRTC? (commonly asked in AI roles with live features -- [Fahd Mirza](https://www.youtube.com/watch?v=fahd-mirza-upwork))
- What is Redis? Why would you use it in an AI application? (startup Gen AI Engineer -- [Khushal Kumar](https://medium.com/@khushalkumar21/my-generative-ai-engineer-interview-experience-got-hired-61a1299ff390))
- Describe a challenging prompt engineering problem that you solved. What techniques did you use? ([proptech founder](https://www.youtube.com/watch?v=proptech-founder-interview))

### Cost & Latency Optimization

- Your app gets 1M queries/day -- how do you optimize cost? (commonly asked -- high frequency)
- How do you reduce token costs at scale? (commonly asked)
- By trimming prompts and caching embeddings, how would you reduce API spend? Walk through a before-and-after cost breakdown. (top interview answer reported by [Fonzi AI](https://medium.com/fonzi-ai))
- Explain multi-layer caching strategies: retrieval cache, prompt cache, and response cache. ([InterviewNode](https://www.interviewnode.com/post/generative-ai-system-design-interview-patterns-you-should-know))
- What is model tiering? When do you route to a small distilled model vs. a large LLM? ([InterviewNode](https://www.interviewnode.com/post/generative-ai-system-design-interview-patterns-you-should-know))
- What is prompt compression and how does it reduce cost? (commonly asked)
- How do you control cost explosions from agent tool calls? Discuss session budgets, per-operation limits, and circuit breakers. ([TechEon](https://atul4u.medium.com/the-complete-agentic-ai-system-design-interview-guide-2026-f95d0cfeb7cf))
- Latency vs. throughput optimization for LLM serving -- what are the trade-offs? ([short video](https://www.youtube.com/shorts/Nc1y9tYV2WM))
- How would you design a scalable and reliable automation workflow? What considerations for error handling, monitoring, and debugging? ([proptech founder](https://www.youtube.com/watch?v=proptech-founder-interview))
- Describe a time you optimized an existing process for efficiency or scalability. What was the bottleneck and how did you find it? ([proptech founder](https://www.youtube.com/watch?v=proptech-founder-interview))
- How would you benchmark each LLM call in a multi-step pipeline to identify latency bottlenecks? ([proptech founder](https://www.youtube.com/watch?v=proptech-founder-interview))

### Safety, Guardrails & Ethics

- How do you ensure the outputs from LLMs are consistent and accurate in complex multi-step workflows? ([proptech founder](https://www.youtube.com/watch?v=proptech-founder-interview))
- When and how would you implement LLM guardrails? Discuss input filtering, output validation, and PII detection. ([proptech founder](https://www.youtube.com/watch?v=proptech-founder-interview))
- How do you handle prompt injection attacks? (commonly asked)
- Design a legal contract generation system with compliance requirements. How do you prevent the LLM from inventing legal content? ([Bhavishya Pandit](https://bhavishyapandit9.substack.com/p/7-deep-cut-ai-system-design-interview))
- Design a hospital voice assistant. How do you handle noise, privacy, latency, and domain-specific vocabulary? ([Bhavishya Pandit](https://bhavishyapandit9.substack.com/p/7-deep-cut-ai-system-design-interview))
- What are the biggest security risks with tool-using agents? Discuss prompt injection through tool outputs, privilege escalation, data exfiltration, and confused deputy attacks. ([TechEon](https://atul4u.medium.com/the-complete-agentic-ai-system-design-interview-guide-2026-f95d0cfeb7cf))
- What is Constitutional AI? How does it relate to alignment and safety? (OpenAI, Anthropic, DeepMind -- [Sundeep Teki](https://www.sundeepteki.org/advice/the-ultimate-ai-research-engineer-interview-guide-cracking-openai-anthropic-google-deepmind-top-ai-labs))
- How do you red-team an LLM system? (OpenAI, Anthropic, DeepMind -- [Sundeep Teki](https://www.sundeepteki.org/advice/the-ultimate-ai-research-engineer-interview-guide-cracking-openai-anthropic-google-deepmind-top-ai-labs))
- How do you handle partial observability or missing information in agent systems? What do you do when the agent doesn't have enough context? ([TechEon](https://atul4u.medium.com/the-complete-agentic-ai-system-design-interview-guide-2026-f95d0cfeb7cf))
- Your application generates code that gets executed. How do you prevent malicious code generation and execution? ([proptech founder](https://www.youtube.com/watch?v=proptech-founder-interview))
