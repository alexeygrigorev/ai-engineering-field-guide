# Theory Questions

Based on candidate reports from Reddit, X, and personal blogs about what they were actually asked in AI engineering interviews. This section covers knowledge-based questions: "What is X?", "How does X work?", "Explain Y."


## Most Common Technical Questions

| Category | Frequency | Example questions |
|----------|-----------|-------------------|
| RAG systems | Very high | "Design a RAG system for customer support chatbot. How do you evaluate it?" |
| Hallucinations | Very high | "How do you detect and mitigate hallucinations in production?" |
| Agents | High | "What's the difference between an agent and a simple LLM chain?" / "What makes a system truly agentic vs. not?" |


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

See [AI System Design](04-ai-system-design.md) for OpenAI, Google, Apple, Anthropic, Cohere, and Salesforce system design questions, seniority expectations, and evaluation frameworks.

## Interview Questions

Actual questions reported by candidates and interviewers, compiled from blog posts, video transcripts, and interview guides. Source or company in parentheses where known.

### LLM Fundamentals

- How do LLMs work? [^proptech-founder-2]
- How do transformers work? [^proptech-founder-2] [^reddit-genai-consulting] [^reddit-ai-eng-questions]
- What is tokenization and how does it affect LLM performance? [^fahd-mirza] [^glassdoor-quantiphi] [^glassdoor-asapp]
- What is the difference between pre-training and fine-tuning? [^fahd-mirza] [^reddit-capital-one] [^glassdoor-cognida]
- Explain context windows and their limitations. [^fahd-mirza] [^exponent-openai-ml]
- What are scaling laws and why do they matter? [^fahd-mirza] [^reddit-llm-interview-prep]
- What is temperature and top-p sampling? How do they affect outputs? [^fahd-mirza] [^reddit-genai-consulting] [^x-aryyann8]
- Explain few-shot learning and chain-of-thought prompting. [^fahd-mirza] [^reddit-genai-consulting] [^reddit-ai-eng-questions]
- What is KV cache? How does it help in LLM inference? [^igotanoffer] [^reddit-llm-interview-prep]
- Can you describe the difference between GenAI and traditional programming in the context of solving a real-world problem? [^proptech-founder-1]
- How do you ensure the outputs from large language models are consistent and accurate, especially when dealing with complex multi-step workflows? [^proptech-founder-1]
- What's an RAG model? Explain the complete process. [^khushal-kumar] [^reddit-ai-eng-questions] [^reddit-genai-consulting]
- What are embeddings? [^khushal-kumar] [^reddit-ai-eng-questions] [^reddit-genai-consulting]
- How does chunking happen? [^khushal-kumar] [^reddit-ai-eng-questions] [^reddit-genai-consulting]
- What is the difference between discriminative and generative models? [^reddit-genai-consulting]
- What is graph RAG? How does it differ from standard RAG? [^reddit-ai-eng-questions]
- What is reflection in the context of LLM agents? [^reddit-ai-eng-questions]
- Explain KL divergence. [^reddit-clear-genai]
- What is the difference between symbolic and connectionist AI? [^reddit-hiring-process]
- Describe the types of text summarization techniques and when you'd use each. [^reddit-hiring-process]
- How do you do memory management and context management with LLMs? [^reddit-ai-eng-questions]
- What is the self-attention mechanism? How does it differ from multi-head attention? [^sundeep-teki]
- What is grouped query attention and how does it differ from standard multi-head attention? [^mimansa-jaiswal]
- What are the differences between BPE, WordPiece, and character-level tokenization? What are the trade-offs? [^fahd-mirza]
- Explain the difference between encoder-only, decoder-only, and encoder-decoder Transformer architectures. When would you use each? [^tidorp] [^hn-46319888] [^reddit-llm-interview-prep]
- Why are decoder-only models dominant even for non-generation tasks? [^reddit-llm-interview-prep]
- What is positional encoding and why is it needed in Transformers? [^linkjob-openai]
- What are the key MMLU, BigBench, and HumanEval benchmarks? What does each measure and what are its limitations? [^fahd-mirza]
- What is the difference between RLHF and DPO? When would you prefer one over the other? [^mimansa-jaiswal]
- What is Mixture of Experts (MoE)? How does it improve efficiency? [^mimansa-jaiswal]
- How do LLMs actually generate text? Explain the autoregressive decoding process. [^hn-46319888] [^llmgenai]
- What are decoding strategies like beam search, top-k, and top-p? When do you use each? [^mimansa-jaiswal]
- What is FlashAttention and how does it work? [^reddit-llm-interview-prep]
- Why is LLM inference memory-bounded? [^reddit-llm-interview-prep]
- How do stop sequences work in LLMs? [^reddit-llm-interview-prep]
- What is the context window and what happens when you exceed it? How do you handle long documents? [^hn-46319888] [^llmgenai]
- What risks arise from applying a general-purpose tokenizer to specialized domains like legal or medical text? [^x-ali-shohadaee]

### RAG Systems

- Design a RAG system for a customer support chatbot. How do you evaluate it? [^process-analysis] [^reddit-genai-consulting] (reported across multiple companies)
- How would you design an LLM-powered enterprise search system? [^igotanoffer]
- Design a generative AI document-processing pipeline for unstructured data (emails, PDFs, images) to automate workflows like claims processing. [^igotanoffer]
- How would you use GPT-4 to generate accurate answers based on proprietary documents? [^interviewnode]
- Design a generative QA assistant for your company's knowledge base. [^interviewnode]
- You're making a system that processes huge PDF reports. How would you handle the problem of not keeping an entire report's context when splitting a document for a chatbot? [^proptech-founder-1]
- How would you efficiently generate and store embeddings for products and queries in a chatbot application? [^proptech-founder-2]
- How would you handle the problem of a model hallucinating when no information is found in the given context? [^proptech-founder-2]
- What retrieval-augmented generation (RAG) projects have you worked on? [^igotanoffer]
- Design a question-answering system over internal documentation. [^system-design-handbook]
- How do you ensure the quality of data that an LLM interacts with? [^proptech-founder-2]
- Compare sparse vs. dense retrieval. When would you use each? [^reddit-clear-genai]
- What are common RAG failure points and how do you debug them? [^reddit-clear-genai] [^reddit-grilled-rag] [^x-athletickoder-2]
- How do you protect sensitive/confidential data in a RAG pipeline? [^reddit-grilled-rag]
- What vector databases have you used? Which ones and why? [^reddit-ai-eng-questions] [^promptlayer] [^llmgenai]
- You have a financial report where page 1 says "all amounts in thousands." How do you handle document-wide context when chunking page by page? [^proptech-founder-1]
- What is hybrid search? When would you combine vector search with keyword search (BM25)? [^designgurus-rag]
- What is re-ranking and why is it needed on top of vector retrieval? Explain cross-encoder vs. bi-encoder. [^designgurus-rag]
- How do you scale a RAG system to 10M+ articles? Discuss sharding, caching, and retrieval optimization. [^bhavishya-pandit]
- Your RAG system returns relevant documents but users still can't find the answer. How do you transform it from a search engine into an answer engine? [^hitendra-patel]
- How do you evaluate a RAG pipeline? What metrics would you use? (NDCG, MRR, precision@k, recall) [^mimansa-jaiswal]
- How do you handle citations and source attribution in a RAG system? [^proptech-founder-1]
- How does Approximate Nearest Neighbor (ANN) search work? Explain HNSW indexing. [^designgurus-rag]
- Where do embeddings fail? Discuss negation, temporal reasoning, and precision requirements. [^techeon]
- What is semantic caching and how can it reduce cost and latency in a RAG system? [^designgurus-rag] [^hn-44796765]
- Design a RAG system that maintains context across multi-turn conversations. [^hn-44875256]
- What are the key tradeoffs when designing a RAG system (latency vs accuracy, chunk size vs context, cost vs quality)? [^reddit-genai-product]
- How do you optimize RAG latency in production? [^x-aryyann8]

### Agents and Tool Use

- What is an AI agent and what is its role in a broader system? [^proptech-founder-1]
- What's the difference between an agent and a simple LLM chain? [^process-analysis] (reported across multiple companies)
- What makes an AI system truly agentic and what does not qualify? [^techeon] [^reddit-ai-agentic] [^reddit-devsindia-genai] [^hn-43884713] [^hn-42431361] [^x-aryyann8]
- When is an agentic architecture the wrong solution? [^techeon] [^reddit-csuk-agents]
- How do you define and enforce agent autonomy boundaries? [^techeon] [^reddit-expdevs-agentic]
- What are the essential components of an agent beyond an LLM? [^techeon] [^reddit-expdevs-agentic] [^reddit-ai-agentic]
- How do you prevent agents from over-reasoning or over-planning? [^techeon] [^reddit-csuk-agents] [^reddit-expdevs-agentic]
- Walk through a production-ready agent architecture. [^techeon] [^reddit-expdevs-agentic] [^reddit-csuk-agents]
- What logic belongs in the orchestrator vs the LLM? [^techeon] [^reddit-expdevs-agentic] [^reddit-aiagents-prep]
- How do you design a safe and debuggable agent loop? [^techeon] [^reddit-expdevs-agentic] [^reddit-csuk-agents]
- How do you implement termination conditions in long-running agents? [^techeon]
- How do agents decompose high-level goals into executable steps? [^techeon] [^reddit-csuk-agents]
- Chain-of-thought vs tree-of-thought vs graph planning - when would you use each? [^techeon]
- How do you detect and stop infinite planning loops? [^techeon] [^reddit-csuk-agents] [^reddit-expdevs-agentic]
- How do you handle partial observability or missing information? [^techeon] [^reddit-csuk-agents]
- How do agents decide a task is "done"? [^techeon]
- What planning failures are hardest to detect in production? [^techeon] [^reddit-expdevs-agentic]
- How do agents decide which tool to use? [^techeon] [^reddit-csuk-agents] [^reddit-aiagents-prep]
- How do you design tool schemas that reduce hallucinated actions? [^techeon] [^reddit-grilled-rag]
- How do you sandbox tool execution safely? [^techeon] [^reddit-expdevs-agentic]
- How do you handle tool failures, retries, and idempotency? [^techeon] [^reddit-expdevs-agentic] [^reddit-csuk-agents] [^reddit-aiagents-prep]
- What are the biggest security risks with tool-using agents? [^techeon] [^reddit-expdevs-agentic] [^datainterview-mistral]
- How do you control cost explosions from tool calls? [^techeon] [^reddit-expdevs-agentic] [^reddit-csuk-agents]
- Stateless vs stateful agents - tradeoffs and use cases? [^techeon] [^reddit-expdevs-agentic]
- How do you version and roll back agent behavior? [^techeon]
- Describe how you would architect an AI agent system, including the agent loop, tool interfaces, memory design, orchestration technologies, and safety considerations. [^igotanoffer]
- Design an agent analyzing customer support tickets, drafting responses, and escalating complex issues. [^promptlayer]
- Create a system where agents collaborate on research reports with citations. [^promptlayer]
- Build an agent reviewing code and suggesting improvements. [^promptlayer]
- How do you explain agentic systems to non-technical stakeholders? [^techeon] [^reddit-expdevs-agentic]
- What types of memory do agentic systems need? Describe working, episodic, semantic, and procedural memory. [^techeon] [^reddit-expdevs-agentic]
- How do you design long-term memory without polluting it? [^techeon]
- How do you implement human-in-the-loop (HIL) patterns and decide when to trigger human review? [^reddit-expdevs-agentic]
- How do you monitor and observe autonomous agent behavior in production? [^reddit-expdevs-agentic] [^reddit-csuk-agents]
- How do you architect agents for regulated or compliance-heavy domains (e.g., financial, healthcare)? [^reddit-expdevs-agentic]
- When do you use orchestration vs choreography patterns for multi-agent systems? [^reddit-expdevs-agentic]
- How do you filter PII in agent pipelines before data reaches the LLM? [^reddit-expdevs-agentic]
- How do you evaluate agent performance? What metrics matter (tool selection quality, action advancement, context adherence)? [^reddit-aiagents-prep]

### Fine-tuning and Training

- When would you fine-tune vs use prompt engineering? [^process-analysis] [^reddit-prep-ai-eng] [^reddit-genai-consulting] [^x-ashutosh-1] (reported across multiple companies)
- What is PEFT/LoRA and when would you use it? [^fahd-mirza] [^reddit-genai-consulting] [^x-interviewstack-meta] [^x-aryyann8] [^reddit-llm-interview-prep]
- What is QLoRA and how does it differ from LoRA? When would you choose one over the other? [^x-aryyann8]
- What is RLHF and why is it important? [^proptech-founder-1]
- Fine-tune or use prompt-engineered RAG? [^system-design-handbook] [^reddit-prep-ai-eng] [^hn-39748537]
- How would you design a model that can solve math problems? Walk through data collection, supervised fine-tuning, post-training, and evaluation. [^igotanoffer]
- How would you design a scalable and efficient system for training a large language model, considering both computational and data constraints? [^igotanoffer]
- Explain the RLHF pipeline: supervised fine-tuning, reward model training, and PPO. How does DPO simplify this? [^proptech-founder-1]
- What is instruction tuning and how does it differ from pre-training? [^hn-46319888] [^llmgenai] [^reddit-llm-interview-prep]
- What is speculative decoding and how does it speed up inference? [^sundeep-teki]
- How do you convert implicit user behavior (edits, acceptance, rejection) into training signals for model improvement? [^bhavishya-pandit]
- Explain quantization. What are the trade-offs between model size, speed, and accuracy? [^raghu-teja-2] [^reddit-llm-interview-prep]

### Evaluation and Metrics

- What metrics do you consider when benchmarking and evaluating LLM performance? [^proptech-founder-1]
- How do you evaluate a chatbot? [^process-analysis] [^reddit-clear-genai] (candidates wish they prepared for this)
- How do you detect and mitigate hallucinations in production? [^process-analysis] [^reddit-ai-eng-questions] [^reddit-genai-consulting] [^hn-41541053] [^hn-46873753] (reported across multiple companies)
- How would you prevent factual errors in a summarization system? [^interviewnode]
- How would you reduce hallucinations in a medical chatbot? [^interviewnode]
- What happens when the LLM is confidently wrong? How do you debug a RAG chatbot giving confident but wrong answers? [^process-analysis] [^datainterview-mistral] (candidates wish they prepared for this)
- Explain SHAP, LIME, and model interpretability. [^fahd-mirza]
- How do you detect and mitigate hallucinations? [^system-design-handbook]
- Explain evaluation metrics: perplexity, ROUGE, BLEU. What are the pitfalls of n-gram-based metrics? [^fahd-mirza] [^reddit-genai-product] [^reddit-llm-interview-prep]
- What are your testing strategies for non-deterministic outputs? [^reddit-prep-ai-eng]
- How do you measure accuracy in generative systems where traditional metrics don't apply? [^reddit-grilled-rag]
- What operational/business metrics matter for AI systems beyond accuracy? (win rate, deflection rate, p95 latency) [^reddit-eightfold-ai]
- How would you evaluate and monitor a model in production, not just offline? [^reddit-swe-to-ai]
- How have you addressed bias/fairness in your models? Can you provide an example of a trade-off you've faced? [^reddit-hiring-process]
- What is time to first token and why does it matter for user experience? [^proptech-founder-1]
- How do you measure hallucination rate in production? [^buildml] [^llmgenai] [^hn-46959695] [^hn-42313401]
- What is "vibes-based" evaluation vs. a formal eval framework? How do you build proper evals? [^exponent-openai]
- How do you build a golden dataset for evaluation? How do you use it for regression testing? [^proptech-founder-1]
- How does the system get better over time? Describe feedback and reinforcement loops. [^interviewnode]
- How do you decide success metrics for an ML model? [^raghu-teja-2]
- How would you implement A/B testing for different prompt variations? [^hn-44875256]
- How would you test a new model before full deployment? Describe A/B testing, canary, interleaved, and shadow testing strategies. [^x-akshay-pachaar-1]
- Two models have identical accuracy but different confidence levels. Which do you choose? Explain model calibration. [^x-akshay-pachaar-3]
- A production chatbot's accuracy dropped from 95% to 80% in six weeks. How do you diagnose the root cause before retraining? [^x-ashutosh-2]

### ML Fundamentals

- How do you approach data pre-processing and feature engineering? [^fahd-mirza]
- Explain SQL versus NoSQL databases for AI workloads. [^fahd-mirza]
- What steps would you take to diagnose performance bugs in a model? [^fahd-mirza]
- Should you optimize for latency or throughput? (for a personal assistant with one request) [^youtube-short]
- Should you use data parallelism for a single-request personal assistant? Why or why not? [^youtube-short]
- Explain how Transformers work. Why are they foundational? [^process-analysis] [^reddit-genai-consulting] (reported across multiple companies)
- How would you handle real-time versus batch processing for data updates? When is one preferred over the other? [^proptech-founder-2]
- How do you ingest and process different types of data (structured, unstructured, event data)? [^proptech-founder-2]
- Explain the bias-variance tradeoff in simple terms. [^reddit-swe-to-ai]
- Why are neural networks usually not the first choice for tabular data? [^reddit-swe-to-ai]
- How do you handle imbalanced datasets in real projects? [^reddit-swe-to-ai] [^reddit-hiring-process] [^raghu-teja-2]
- Explain the difference between RNN and LSTM. [^raghu-teja-2]
- Debug a model that runs but doesn't learn. Identify broadcasting errors and dimension mismatches. [^sundeep-teki]
- Statistics questions: probability, distributions, regression, Bayesian analysis, hypothesis testing. [^mimansa-jaiswal]
- Explain supervised vs. unsupervised learning. When would you use each? [^hn-29876742] [^tidorp]
- What is regularization? Compare L1, L2, and dropout. [^hn-29876742] [^tidorp]
- What is feature scaling and when is it necessary? Compare normalization vs standardization. [^x-aryyann8]
- Implement cosine similarity in NumPy. [^reddit-amazon-genai]

### Python and Software Engineering

- How do you handle race conditions in your code? [^proptech-founder-2]
- What is the Global Interpreter Lock (GIL) in Python? [^proptech-founder-2]
- What is something unique about Python when it comes to concurrency? [^proptech-founder-2]
- What are some problems you can run into when using asynchronous programming in Python? [^proptech-founder-2]
- What is Docker? [^khushal-kumar]
- Why do we use Selenium? [^khushal-kumar]
- Have you heard about Redis? [^khushal-kumar]
- Explain the JavaScript event loop. [^proptech-founder-1]
- How do you call models via API/SDK? How do you handle retries, timeouts, and logging? [^reddit-genai-consulting]
- Which AI development platforms or tools do you regularly use, and why? [^reddit-hiring-process]
- Explain memory leaks and garbage collection in Python. [^raghu-teja-1]
- What is the difference between class methods and static methods? [^raghu-teja-1]
- Explain super() and Method Resolution Order in multiple inheritance. [^raghu-teja-1]
- How do you debug Python code in production? "In production, there will be no VS Code." [^raghu-teja-1]
- How do you use asyncio for concurrent I/O in Python? When would you use threading vs. multiprocessing instead? [^proptech-founder-1]
- How do you optimize SQL queries? Explain the order of execution in SQL. [^raghu-teja-1]
- What are Git branching strategies for deployment? How do you perform a rebase? How do you handle merge conflicts? [^raghu-teja-1]
- Have you worked with real-time communication technologies like WebRTC? [^fahd-mirza-2]

### Infrastructure and MLOps

- How would you design a large-scale AI model deployment system? [^designgurus]
- How would you design a distributed training system for deep learning? [^designgurus] [^x-akshay-pachaar-2]
- How would you design a scalable data pipeline for ML applications? [^designgurus]
- How would you design a GenAI system to handle traffic spikes without overwhelming the model provider? [^igotanoffer]
- How would you monitor production AI systems? [^system-design-handbook]
- What are major scaling challenges for LLM-powered applications? [^system-design-handbook]

### Cost and Latency Optimization

- Your app gets 1M queries/day - how do you optimize cost? [^process-analysis] (reported across multiple companies)
- How do you reduce token costs at scale? [^process-analysis] [^reddit-prep-ai-eng] [^hn-46229585] [^hn-46695170] (candidates wish they prepared for this)
- How would you think about cost and capacity planning for an LLM-powered application at scale? [^igotanoffer]
- How would you make GPT-based API calls cost-efficient under heavy load? [^interviewnode]
- How would you reduce token costs? [^system-design-handbook]
- Explain quantization and model distillation for inference optimization. [^fahd-mirza]
- Describe the latency/cost/relevancy tradeoff triangle in GenAI systems. How do you manage all three? [^proptech-founder-2]
- How do you reduce latency in GenAI applications? [^proptech-founder-2]
- Cost vs. quality trade-offs: when is a small open-source model "good enough" vs. GPT-4-class? [^reddit-genai-consulting]
- By trimming prompts and caching embeddings, how would you reduce API spend? Walk through a before-and-after cost breakdown. [^fonzi-ai]
- Explain multi-layer caching strategies: retrieval cache, prompt cache, and response cache. [^interviewnode]
- What is model tiering? When do you route to a small distilled model vs. a large LLM? [^interviewnode] [^hn-42793253] [^hn-47150302]
- What is prompt compression and how does it reduce cost? [^llmgenai] [^hn-46319888] [^hn-44013971]
- Latency vs. throughput optimization for LLM serving - what are the trade-offs? [^youtube-short]
- How would you benchmark each LLM call in a multi-step pipeline to identify latency bottlenecks? [^proptech-founder-1]
- Estimate the budget for a RAG pipeline at enterprise scale (e.g., 300,000 legal contracts). [^reddit-devsindia-genai]
- What's the real bottleneck in LLM serving throughput? How does PagedAttention address it? [^x-athletickoder-1]

### Safety and Guardrails

- When and how would you implement LLM guardrails? [^proptech-founder-1]
- How would you design a language model that minimizes harmful outputs while still being useful and expressive? [^igotanoffer]
- How would you build a system that detects whether content violates policy or contains offensive material? [^igotanoffer]
- How do you protect against prompt injection and jailbreaking? [^system-design-handbook] [^reddit-ai-eng-questions] [^reddit-expdevs-agentic] [^hn-44268335]
- What steps would you take to handle exceptions in a GenAI application? [^proptech-founder-2]
- Explain Constitutional AI and alignment considerations. [^sundeep-teki]
- How do you handle data privacy and PII in prompts and logs? [^reddit-genai-consulting] [^reddit-expdevs-agentic]
- How do you address bias in training data and generated content? [^reddit-genai-consulting] [^reddit-hiring-process]
- How do you red-team an LLM system? [^sundeep-teki]
- Your application generates code that gets executed. How do you prevent malicious code generation and execution? [^proptech-founder-1]


## How to Prepare

Mimansa Jaiswal documents a structured approach to preparing for ML/LLM research and engineering interviews across seven areas: [^mimansa-jaiswal]

1. LeetCode: Grind 75 + easy/medium from NeetCode 150, with optimization passes after 2-day breaks
2. ML/DL/LLM coding: Implement from scratch (attention, transformers, decoding strategies)
3. Statistics: Probability, distributions, regression, Bayesian analysis, hypothesis testing (highlighted after a surprise Amazon loop exposed gaps)
4. ML fundamentals: Supervised/unsupervised learning, regularization, clustering, neural network architectures
5. LLM architecture & training: Transformers, tokenization, scaling laws, LoRA/QLoRA, MoE, RLHF/DPO, RAG fundamentals (chunking, BM25, dense retrieval, reranking, evaluation with NDCG/MRR)
6. ML system design: Always present both discriminative and generative approaches, letting interviewers guide direction. Spend up to 10 minutes on clarifying questions
7. Behavioral: STAR method with 30-second segments, distinct examples per interview to avoid sounding mechanical

Notable insight: "MLA became popular while I was interviewing" and "GRPO became popular after interviews" - the field evolves continuously during preparation.

### Questions People Wish They Prepared For

- "How do you evaluate a chatbot?" (not just build one)
- "What happens when the LLM is confidently wrong?" (failure modes)
- "How do you reduce token costs at scale?" (production thinking)
- "Design for 1M users" (scale beyond prototype)
- "How do you debug Python code in production?" [^raghu-teja-1]
- "When is an agentic architecture the wrong solution?" [^techeon]
- "What makes a system truly agentic?" [^techeon]

## Sources

[^bhavishya-pandit]: [Bhavishya Pandit](https://bhavishyapandit9.substack.com/p/7-deep-cut-ai-system-design-interview)
[^buildml]: [BuildML](https://buildml.substack.com/p/top-24-llm-questions-asked-at-deepmind)
[^datainterview-mistral]: [DataInterview - Mistral ML Engineer Interview](https://www.datainterview.com/blog/mistral-machine-learning-engineer-interview)
[^designgurus]: [DesignGurus - OpenAI System Design](https://www.designgurus.io/blog/openai-system-design-interview-questions)
[^designgurus-rag]: [DesignGurus - RAG System Design](https://www.designgurus.io/blog/system-design-for-rag)
[^exponent-openai]: [Medium - Exponent/Jacob Simon, OpenAI](https://medium.com/exponent/what-its-actually-like-to-interview-at-openai-in-2026-03a646c9436c)
[^exponent-openai-ml]: [Exponent - OpenAI ML Engineer Questions](https://www.tryexponent.com/questions?role=ml-engineer&type=technical)
[^fahd-mirza]: [YouTube - Fahd Mirza](https://www.youtube.com/watch?v=yr5dRHrnbCo)
[^fahd-mirza-2]: [YouTube - Fahd Mirza (Upwork)](https://www.youtube.com/watch?v=fahd-mirza-upwork)
[^fonzi-ai]: [Medium - Fonzi AI](https://medium.com/fonzi-ai/what-ive-learned-from-sitting-in-on-50-ai-engineer-interviews-c493696453c4)
[^glassdoor-asapp]: [Glassdoor - ASAPP AI/ML Research Intern Interview](https://www.glassdoor.com/Interview/ASAPP-AI-ML-Research-Intern-Interview-Questions-EI_IE1501287.0,5_KO6,27.htm)
[^glassdoor-cognida]: [Glassdoor - Cognida.ai Software Engineer Interview](https://www.glassdoor.com/Interview/Cognida-ai-Software-Engineer-Interview-Questions-EI_IE7907039.0,10_KO11,28.htm) (Jan 2026)
[^glassdoor-quantiphi]: [Glassdoor - Quantiphi ML Engineer Interview](https://www.glassdoor.com/Interview/NLP-related-question-tokenization-fine-tuning-ML-LIFE-CYCLE-QTN_8617277.htm)
[^hitendra-patel]: [Medium - Hitendra Patel](https://medium.com/@hitendrapatel)
[^hn-29876742]: [HN - Deep Learning Interviews Book](https://news.ycombinator.com/item?id=29876742)
[^hn-39748537]: [HN - RAG vs. Fine-Tuning](https://news.ycombinator.com/item?id=39748537)
[^hn-41541053]: [HN - LLMs Will Always Hallucinate](https://news.ycombinator.com/item?id=41541053)
[^hn-42313401]: [HN - Automated Reasoning to Remove LLM Hallucinations](https://news.ycombinator.com/item?id=42313401)
[^hn-42431361]: [HN - Agentic LLM Systems in Production](https://news.ycombinator.com/item?id=42431361)
[^hn-42793253]: [HN - AI Orchestration and LLM Routing](https://news.ycombinator.com/item?id=42793253)
[^hn-43884713]: [HN - Is an AI Agent Just an LLM Wrapper?](https://news.ycombinator.com/item?id=43884713)
[^hn-44013971]: [HN - Compress Long LLM Prompts](https://news.ycombinator.com/item?id=44013971)
[^hn-44268335]: [HN - Design Patterns for Securing LLM Agents](https://news.ycombinator.com/item?id=44268335)
[^hn-44796765]: [HN - Sleipner.ai LLM Cost Reduction](https://news.ycombinator.com/item?id=44796765)
[^hn-44875256]: [HN - Interview Questions for AI Product Engineering](https://news.ycombinator.com/item?id=44875256)
[^hn-46229585]: [HN - LLM API Costs in Production](https://news.ycombinator.com/item?id=46229585)
[^hn-46319888]: [HN - LLM Interview Questions](https://news.ycombinator.com/item?id=46319888)
[^hn-46695170]: [HN - Reduce LLM Token Costs with TOON](https://news.ycombinator.com/item?id=46695170)
[^hn-46873753]: [HN - Are LLM Failures Structurally Unavoidable?](https://news.ycombinator.com/item?id=46873753)
[^hn-46959695]: [HN - Early Detection of LLM Hallucinations via ONTOS](https://news.ycombinator.com/item?id=46959695)
[^hn-47150302]: [HN - InferShrink Model Routing](https://news.ycombinator.com/item?id=47150302)
[^igotanoffer]: [igotanoffer - Generative AI System Design Interview](https://igotanoffer.com/en/advice/generative-ai-system-design-interview)
[^interviewnode]: [InterviewNode - GenAI System Design Patterns](https://www.interviewnode.com/post/generative-ai-system-design-interview-patterns-you-should-know)
[^khushal-kumar]: [Medium - Khushal Kumar](https://kaysnotes.medium.com/my-generative-ai-engineer-interview-experience-got-hired-6b3f1affc4e9)
[^linkjob-openai]: [linkjob - OpenAI](https://www.linkjob.ai/interview-questions/openai-loop-interview)
[^llmgenai]: [GitHub - LLM Interview Questions](https://github.com/llmgenai/LLMInterviewQuestions)
[^mimansa-jaiswal]: [Mimansa Jaiswal](https://mimansajaiswal.github.io/posts/llm-ml-job-interviews-resources/)
[^process-analysis]: [Process Analysis - Reddit r/cscareerquestions](https://www.reddit.com/r/cscareerquestions/)
[^promptlayer]: [PromptLayer](https://blog.promptlayer.com/the-agentic-system-design-interview-how-to-evaluate-ai-engineers/)
[^proptech-founder-1]: [YouTube - Proptech Founder Part 1](https://www.youtube.com/watch?v=leXRiJ5TuQo)
[^proptech-founder-2]: [YouTube - Proptech Founder Part 2](https://www.youtube.com/watch?v=Zt-h5BiBWH0)
[^raghu-teja-1]: [Medium - Raghu Teja, IBM Part 1](https://medium.com/@raghu_teja/how-i-cracked-my-ibm-ai-engineer-interview-part-1-technical-e7e4f73be5c4)
[^raghu-teja-2]: [Medium - Raghu Teja, IBM Part 2](https://medium.com/@raghu_teja/how-i-cracked-my-ibm-ai-engineer-interview-part-2-ml-scenarios-88af2b46282e)
[^reddit-ai-agentic]: [Reddit - What Agentic AI Am I Supposed to Learn?](https://www.reddit.com/r/ArtificialInteligence/comments/1rceuef/what_agentic_ai_am_i_even_supposed_to_learn) (r/ArtificialIntelligence, Feb 2026)
[^reddit-ai-eng-questions]: [Reddit - AI Engineer Interview Questions](https://www.reddit.com/r/ArtificialInteligence/comments/1nybfr8/ai_engineer_interview_questions/) (r/ArtificialIntelligence)
[^reddit-aiagents-prep]: [Reddit - Interview Prep: Deep Learning to Agentic Systems](https://www.reddit.com/r/AI_Agents/comments/1qrxchn/interview_prep_deep_learning_agentic_systems_what) (r/AI_Agents, Jan 2026)
[^reddit-amazon-genai]: [Reddit - ML Engineer GenAI Amazon](https://www.reddit.com/r/datascience/comments/1jrdrpx/ml_engineer_genai_amazon/) (r/datascience)
[^reddit-capital-one]: [Reddit - Capital One Data Science Interview](https://www.reddit.com/r/datasciencecareers/comments/1ojegp4/capital_one_data_science_interview) (r/datasciencecareers, Oct 2025)
[^reddit-clear-genai]: [Reddit - How to Clear Interviews in AI/GenAI/RAG/LLM](https://www.reddit.com/r/generativeAI/comments/1p4yrjk/how_to_clear_interviews_in_ai_gen_rag_llm/) (r/generativeAI)
[^reddit-csuk-agents]: [Reddit - AI Engineering Agents Interview Prep](https://www.reddit.com/r/cscareerquestionsuk/comments/1qmybi3/ai_engineering_agents_interview_prep) (r/cscareerquestionsuk, Jan 2026)
[^reddit-devsindia-genai]: [Reddit - Generative AI Engineer Interview Prep](https://www.reddit.com/r/developersIndia/comments/1oq5fdi/got_an_interview_tomorrow_for_a_generative_ai) (r/developersIndia, Nov 2025)
[^reddit-eightfold-ai]: [Reddit - Need Advice for Eightfold.ai Agentic AI Engineer](https://www.reddit.com/r/developersIndia/comments/1pbaj11/need_advice_for_eightfoldai_agentic_ai_engineer) (r/developersIndia)
[^reddit-expdevs-agentic]: [Reddit - Agentic AI System Design Interview](https://www.reddit.com/r/ExperiencedDevs/comments/1r78ipa/agentic_ai_agents_system_design_interview) (r/ExperiencedDevs, Feb 2026)
[^reddit-genai-consulting]: [Reddit - Interview Questions Gen AI (consulting)](https://www.reddit.com/r/learnmachinelearning/comments/1ppgsf3/interview_questions_gen_ai) (r/learnmachinelearning)
[^reddit-genai-product]: [Reddit - Technical Interview for GenAI Engineer Role](https://www.reddit.com/r/leetcode/comments/1rd6yki/technical_interview_for_genai_engineer_role_for_a) (r/leetcode)
[^reddit-grilled-rag]: [Reddit - Got Grilled in an ML Interview for LangGraph/RAG Projects](https://www.reddit.com/r/LangChain/comments/1k662xc/got_grilled_in_an_ml_interview_today_for_my/) (r/LangChain)
[^reddit-hiring-process]: [Reddit - What's the AI Engineering Hiring Process Like?](https://www.reddit.com/r/cscareerquestions/comments/1lmwq1e/whats_the_ai_engineering_hiring_process_like/) (r/cscareerquestions)
[^reddit-llm-interview-prep]: [Reddit - LLM Interview Prep](https://www.reddit.com/r/MachineLearning/comments/1ein9vh/d_llm_interview_prep) (r/MachineLearning)
[^reddit-prep-ai-eng]: [Reddit - How to Prepare for AI Engineering Interviews](https://www.reddit.com/r/datascience/comments/1ovf9k2/how_to_prepare_for_ai_engineering_interviews/) (r/datascience)
[^reddit-swe-to-ai]: [Reddit - From Software Developer to AI Engineer](https://www.reddit.com/r/learnmachinelearning/comments/1pzcw2y/from_software_developer_to_ai_engineer_the_exact/) (r/learnmachinelearning)
[^sundeep-teki]: [Sundeep Teki](https://www.sundeepteki.org/advice/the-ultimate-ai-research-engineer-interview-guide-cracking-openai-anthropic-google-deepmind-top-ai-labs)
[^system-design-handbook]: [System Design Handbook](https://www.systemdesignhandbook.com/guides/generative-ai-system-design-interview/)
[^techeon]: [Medium - TechEon Agentic Guide](https://medium.com/@techeon/the-complete-agentic-ai-system-design-interview-guide-2026)
[^tidorp]: [GitHub - TidorP/MLJobSearch2025](https://github.com/TidorP/MLJobSearch2025)
[^x-akshay-pachaar-1]: [X - Akshay Pachaar, ML Deployment Testing (Netflix)](https://x.com/akshay_pachaar/status/1990034795909582860)
[^x-akshay-pachaar-2]: [X - Akshay Pachaar, Distributed Training (Google)](https://x.com/akshay_pachaar/status/1992571349332804081)
[^x-akshay-pachaar-3]: [X - Akshay Pachaar, Model Calibration (Apple)](https://x.com/akshay_pachaar/status/1994020936488734823)
[^x-ali-shohadaee]: [X - Ali Shohadaee, Domain-Specific Tokenization (Anthropic)](https://x.com/alishohadaee/status/2012176441287348231)
[^x-aryyann8]: [X - AI Engineer Intern Interview](https://x.com/aryyann8/status/2009314129878896960) (Jan 2026)
[^x-ashutosh-1]: [X - Ashutosh Maheshwari, Fine-Tuning vs. Prompting](https://x.com/asmah2107/status/1977413874702745794)
[^x-ashutosh-2]: [X - Ashutosh Maheshwari, Model Drift Diagnosis (Databricks)](https://x.com/asmah2107/status/1990649811964735512)
[^x-athletickoder-1]: [X - athleticKoder, PagedAttention and LLM Serving](https://x.com/athleticKoder/status/1967925267864928669)
[^x-athletickoder-2]: [X - athleticKoder, RAG System Diagnostics](https://x.com/athleticKoder/status/2002355874786873383)
[^x-interviewstack-meta]: [X - InterviewStack.io, Meta LoRA Question](https://x.com/gnan54796/status/2007302142550565123)
[^youtube-short]: [YouTube Short](https://www.youtube.com/shorts/Nc1y9tYV2WM)
