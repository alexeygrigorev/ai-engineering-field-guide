# AI Engineering Interview Questions

Consolidated from 100+ sources including blog posts, YouTube transcripts, Reddit threads, Medium articles, and interview guides. Every question was extracted from actual interview experiences or preparation materials.

## Technical Questions

### LLM Fundamentals

- How do LLMs work? [^proptech-founder-2]
- How do transformers work? [^proptech-founder-2] [^reddit-genai-consulting] [^reddit-ai-eng-questions]
- What is tokenization and how does it affect LLM performance? [^fahd-mirza]
- What is the difference between pre-training and fine-tuning? [^fahd-mirza]
- Explain context windows and their limitations. [^fahd-mirza]
- What are scaling laws and why do they matter? [^fahd-mirza]
- What is temperature and top-p sampling? How do they affect outputs? [^fahd-mirza] [^reddit-genai-consulting] [^x-aryyann8]
- Explain few-shot learning and chain-of-thought prompting. [^fahd-mirza] [^reddit-genai-consulting] [^reddit-ai-eng-questions]
- What is KV cache? How does it help in LLM inference? [^igotanoffer]
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
- Explain the difference between encoder-only, decoder-only, and encoder-decoder Transformer architectures. When would you use each? [^tidorp] [^hn-46319888]
- What is positional encoding and why is it needed in Transformers? [^linkjob-openai]
- What are the key MMLU, BigBench, and HumanEval benchmarks? What does each measure and what are its limitations? [^fahd-mirza]
- What is the difference between RLHF and DPO? When would you prefer one over the other? [^mimansa-jaiswal]
- What is Mixture of Experts (MoE)? How does it improve efficiency? [^mimansa-jaiswal]
- How do LLMs actually generate text? Explain the autoregressive decoding process. [^hn-46319888] [^llmgenai]
- What are decoding strategies like beam search, top-k, and top-p? When do you use each? [^mimansa-jaiswal]
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
- Chain-of-thought vs tree-of-thought vs graph planning -- when would you use each? [^techeon]
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
- Stateless vs stateful agents -- tradeoffs and use cases? [^techeon] [^reddit-expdevs-agentic]
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
- What is PEFT/LoRA and when would you use it? [^fahd-mirza] [^reddit-genai-consulting] [^x-interviewstack-meta] [^x-aryyann8]
- What is QLoRA and how does it differ from LoRA? When would you choose one over the other? [^x-aryyann8]
- What is RLHF and why is it important? [^proptech-founder-1]
- Fine-tune or use prompt-engineered RAG? [^system-design-handbook] [^reddit-prep-ai-eng] [^hn-39748537]
- How would you design a model that can solve math problems? Walk through data collection, supervised fine-tuning, post-training, and evaluation. [^igotanoffer]
- How would you design a scalable and efficient system for training a large language model, considering both computational and data constraints? [^igotanoffer]
- Explain the RLHF pipeline: supervised fine-tuning, reward model training, and PPO. How does DPO simplify this? [^proptech-founder-1]
- What is instruction tuning and how does it differ from pre-training? [^hn-46319888] [^llmgenai]
- What is speculative decoding and how does it speed up inference? [^sundeep-teki]
- How do you convert implicit user behavior (edits, acceptance, rejection) into training signals for model improvement? [^bhavishya-pandit]
- Explain quantization. What are the trade-offs between model size, speed, and accuracy? [^raghu-teja-2]

### Evaluation and Metrics

- What metrics do you consider when benchmarking and evaluating LLM performance? [^proptech-founder-1]
- How do you evaluate a chatbot? [^process-analysis] [^reddit-clear-genai] (candidates wish they prepared for this)
- How do you detect and mitigate hallucinations in production? [^process-analysis] [^reddit-ai-eng-questions] [^reddit-genai-consulting] [^hn-41541053] [^hn-46873753] (reported across multiple companies)
- How would you prevent factual errors in a summarization system? [^interviewnode]
- How would you reduce hallucinations in a medical chatbot? [^interviewnode]
- What happens when the LLM is confidently wrong? How do you debug a RAG chatbot giving confident but wrong answers? [^process-analysis] [^datainterview-mistral] (candidates wish they prepared for this)
- Explain SHAP, LIME, and model interpretability. [^fahd-mirza]
- How do you detect and mitigate hallucinations? [^system-design-handbook]
- Explain evaluation metrics: perplexity, ROUGE, BLEU. [^fahd-mirza] [^reddit-genai-product]
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

### Case Study / Approach

- How would you implement an AI application from start to finish, from kickoff meeting through deployment? (IBM) [^raghu-teja-2]
- How would you design a scalable and reliable automation workflow? What considerations for error handling, monitoring, and debugging? [^proptech-founder-1]

### Infrastructure and MLOps

- How would you design a large-scale AI model deployment system? [^designgurus]
- How would you design a distributed training system for deep learning? [^designgurus] [^x-akshay-pachaar-2]
- How would you design a scalable data pipeline for ML applications? [^designgurus]
- How would you design a GenAI system to handle traffic spikes without overwhelming the model provider? [^igotanoffer]
- How would you monitor production AI systems? [^system-design-handbook]
- What are major scaling challenges for LLM-powered applications? [^system-design-handbook]

### Cost and Latency Optimization

- Your app gets 1M queries/day -- how do you optimize cost? [^process-analysis] (reported across multiple companies)
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
- Latency vs. throughput optimization for LLM serving -- what are the trade-offs? [^youtube-short]
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

---

## System Design Questions

### AI System Design

- Design ChatGPT. [^igotanoffer]
- Design our Claude chat service. [^igotanoffer]
- Design a small language learning model that could run on a phone while making sure it's polite. [^igotanoffer]
- Here's a junior developer's design for an inference batching system. Can you review it and explain what you'd change or improve? [^igotanoffer]
- Design the OpenAI Playground -- specifically the feature that lets developers simulate full conversations and threads. [^exponent-openai]
- Design a real-time chatbot API (low-latency handling, session management, concurrency, safety filters). [^designgurus]
- Design a Document Q&A Assistant. [^bhavishya-pandit]
- Design a Hallucination-Free Banking Chatbot. [^bhavishya-pandit]
- Design a Hospital Voice Assistant (handle noise, privacy, latency, domain vocabulary). [^bhavishya-pandit]
- Design a Feedback Loop for Writing Tools. [^bhavishya-pandit]
- Design a Legal Contract Generation system with compliance requirements. [^bhavishya-pandit]
- Design an AI Search system scaling to 10M+ articles. [^bhavishya-pandit]
- Design a Resume Classifier for Team Routing. [^bhavishya-pandit]
- Design an AI-powered Candidate Sourcing System with 750M profiles, semantic search, and <500ms latency. [^colin-zhou]
- Scale an AI chat feature to 1M daily users -- discuss trade-offs. [^process-analysis] (reported across multiple companies)
- Design for 1M users (scale beyond prototype). [^process-analysis] (candidates wish they prepared for this)
- Design a system to process 10k user uploads per month (bank payslips, IDs, references). How would you extract data, detect inconsistencies, reject invalid files, and handle LLM provider downtime? [^igotanoffer]
- Design a system that lets doctors automatically send billing info to insurers based on patient notes. [^igotanoffer]
- Design a conversational recommender system that suggests products based on user preferences, combining chat, retrieval, and database layers. [^igotanoffer]
- Design a fast autocomplete system using LLMs. [^system-design-handbook]
- Design an AI-powered legal assistant. [^system-design-handbook]
- Build a generative resume builder with memory. [^system-design-handbook]
- Create an internal Slack bot answering HR questions. [^system-design-handbook]
- Design a GitHub Copilot-style JavaScript development tool. [^system-design-handbook]
- Design an AI co-pilot like GitHub Copilot (real-time streaming completions). [^colin-zhou]
- Design a Midjourney/Stable Diffusion image generation service (queueing, GPU scheduling). [^colin-zhou]
- Design a Perplexity.ai / real-time LLM-powered search engine. [^colin-zhou]
- Design a Ghibli Image Generator (text prompt ingestion, model selection, GPU inference, cost throttling, safety filters). [^rohit-verma]
- Design a Dynamic Questionnaire Engine for an Insurance Platform (JSON-driven, frontend decision tree without backend calls). [^rohit-verma]
- Design a user profile system addressing storage, multi-device tracking, and preference flexibility. Optimize for 100 million users with batch migration. [^linkjob-openai]
- Design a distributed search system capable of handling a billion documents and a million QPS, while also managing LLM inference for over 10,000 requests per second. [^linkjob-anthropic]
- Design hybrid search combining traditional text retrieval with semantic similarity -- top-k similar documents from a corpus of over 10M documents with a response time under 50ms. [^linkjob-anthropic]
- Design a workflow to remove all dead links for hundreds of client websites assuming you have API access to overwrite their HTML. [^proptech-founder-2]
- How would you design the UX for an AI assistant that is often slow? [^igotanoffer]
- How would you surface model limitations or errors to users without breaking trust? [^igotanoffer]
- Design a scalable image-generation pipeline for millions of users. [^interviewnode]
- How would you scale a generative content platform for millions of users? [^interviewnode]
- Design an In-Memory Database with SET, GET, BEGIN, ROLLBACK, COMMIT, and nested transaction support. [^devto-xai]
- Design an AI recommendation system. [^reddit-swe-to-ai]
- Design a fraud detection system. [^reddit-swe-to-ai]
- Design a chatbot architecture end-to-end (LLM + backend + data flow). [^reddit-swe-to-ai]
- Design a distributed job queue for 100k+ GPU training jobs with preemption and checkpointing. [^reddit-xai-eng]
- Design a temperature prediction system handling inconsistent global datasets (hybrid ML-LLM). [^reddit-grilled-rag]
- Design an end-to-end RAG service: data ingestion, indexing, retrieval, generation, evals, tracing, guardrails. [^reddit-eightfold-ai]
- Design a rate-limiter and code the core part. [^reddit-xai-eng]
- Scaling AI systems to millions of users: latency and cost trade-offs, batching, caching, streaming, failure modes. [^reddit-2026-prep]
- Design ChatGPT's cross-conversation memory feature. [^igotanoffer]
- Design a multi-step agentic workflow (meeting scheduling, code review, email campaigns). [^promptlayer]
- Design a content/policy violation detection system. [^igotanoffer]
- Design a unified query engine across dispersed data sources like email, calendar, documents, and chat. [^x-avi-chawla-1]

### Traditional System Design

- Design GitHub Actions. [^hello-interview]
- Design Slack. [^hello-interview]
- Design Online Chess. [^hello-interview]
- Design a Payment System. [^hello-interview]
- Design a Webhook Callback System. [^hello-interview]
- Design TinyURL (Bitly). [^colin-zhou]
- Design Instagram / TikTok feed. [^colin-zhou]
- Design Twitter / X (timeline, posting, followers, trending topics). [^colin-zhou]
- Design YouTube / Netflix video streaming platform. [^colin-zhou]
- Design Uber (ride-sharing backend: matching, ETA, pricing surges). [^colin-zhou]
- Design WhatsApp / Messenger (1:1 + group chat at global scale). [^colin-zhou]
- Design a distributed key-value store (like DynamoDB / Cassandra). [^colin-zhou]
- Design Google Docs collaborative editing (real-time, eventually consistent). [^colin-zhou]
- Design Yelp / Google Maps nearby search. [^colin-zhou]
- Design a rate limiter (global, per-user, distributed). [^colin-zhou]
- Design Discord (voice + text chat, millions concurrent in voice channels). [^colin-zhou]
- Design Stripe payment processing system (high consistency, PCI compliance). [^colin-zhou]
- Design a distributed job scheduler (like AWS Batch at planetary scale). [^colin-zhou]
- Design a notification system that can send 1B notifications/day with <1% loss. [^colin-zhou]
- Design a strongly-consistent distributed database (Spanner / CockroachDB-like). [^colin-zhou]
- Design a high-frequency trading exchange matching engine. [^colin-zhou]
- Our p99 latency went from 50ms to 2s overnight -- how would you debug and fix? [^colin-zhou]
- Design a global WebSocket service (10M+ concurrent connections). [^colin-zhou]
- Design a global feature flag / config service (multi-region, zero-downtime rollouts). [^colin-zhou]

### System Troubleshooting

- A system's 95th percentile latency spiked from 100ms to 2000ms. Identify bottlenecks rapidly. [^linkjob-anthropic]
- How would you handle a 10x traffic spike during a product launch? [^hello-interview]
- What happens if your primary data center goes offline for six hours? [^hello-interview]

---

## Coding Problems

### LeetCode / Algorithm Style

- Word Search on Grid using Trie + DFS (LeetCode Medium). [^devto-xai]
- LRU Cache with O(1) time complexity using HashMap + Doubly Linked List. [^devto-xai]
- Prime numbers between 0 and 100. [^khushal-kumar]
- Check whether two strings are anagrams of each other. [^khushal-kumar]
- Serialize Binary Tree (space-optimized, discussion-based with compression techniques and backward compatibility). [^rohit-verma]
- LeetCode 2408: Design SQL. [^hello-interview]
- LeetCode 981: Time Based Key-Value Store. [^hello-interview]
- Unix cd command with symbolic link resolution. [^hello-interview]
- Reverse a linked list with constraints (AI-assisted coding round -- candidate must prompt LLM effectively). [^reddit-microsoft-aiml]
- Find the Excel column name from its column number (e.g., column 702 = "AAA"). [^reddit-microsoft-aiml]
- Construct a tree from a list where index = node value and value = parent node (LC Medium). [^reddit-microsoft-aiml]
- CodeSignal GCA: 4 questions in 70 min -- two medium-hard, one graph, one greedy with bit ops. [^reddit-xai-eng]
- Union Find problem + AI question (use DistilBERT to categorize CSV text with sentiments, must pass 5 test cases checking embeddings length, output structure). [^reddit-ai-eng-questions-2]
- Write code for a banking application using HashMap/TreeMap. Design a task executor -- store and pause tasks. [^reddit-2026-prep]
- A gRPC service is timing out. Add an async boundary, handle failure modes (retries, dead letter queues, idempotency), scale with multi-threading or message queues. [^exponent-mock]
- Discuss serialization approaches, compression techniques, streaming formats, backward compatibility, and corruption recovery -- no code written, pure discussion. (Microsoft senior) [^rohit-verma]

### OpenAI-Specific Coding

- KV Store Serialize/Deserialize. [^hello-interview]
- In-Memory Database: Implement SQL-Like Operations. [^hello-interview]
- Versioned key-value store implementation (Time Travel Hash variant). [^linkjob-openai]
- Credits management system -- track credit state across issued and used credits with different expiration rules and usage requirements, with increasing complexity. [^exponent-openai]
- Refactoring round: 100-120 lines of intentionally convoluted, deeply nested code. Refactor for long-term maintainability while keeping existing tests green and extending to new ones. [^exponent-openai]

### Anthropic-Specific Coding

- 4-level progressive coding assessment: Level 1 (SET/GET/DELETE), Level 2 (SCAN/SCAN_BY_PREFIX), Level 3 (timestamped operations + TTL), Level 4 (file compression/decompression with storage management). [^linkjob-anthropic]

### ML / AI Coding

- 1-NN (simplest KNN case) and feedforward neural network implementation. [^linkjob-openai]
- Transformer bug-fixing exercise with position embedding and KV cache issues. [^linkjob-openai]
- PyTorch code completion with complexity analysis. [^linkjob-openai]
- Implement Multi-Head Attention from memory. [^sundeep-teki]
- Implement a full Transformer layer from memory. [^sundeep-teki]
- Implement LoRA adapter from scratch. [^yuan-meng]
- Implement efficient LLM API batch processing. [^promptlayer]
- Debug code handling embeddings. [^promptlayer]
- Write scripts preparing text for fine-tuning. [^promptlayer]
- Build a gRPC service for financial report generation (async conversion, thread management, error handling, batch processing). [^exponent-mock]
- Implement neural networks, LSTMs, and RNNs from scratch using NumPy or PyTorch. [^mimansa-jaiswal]
- Implement cached attention and grouped query attention variants. [^mimansa-jaiswal]
- Implement beam search, top-k, and top-p decoding strategies from scratch. [^mimansa-jaiswal] [^datainterview-mistral]
- Implement autoregressive generation with top-p sampling. [^datainterview-mistral]
- Implement logistic regression with SGD, L2 regularization, and early stopping in NumPy. [^datainterview-mistral]
- Implement stratified K-fold splitting. [^datainterview-mistral]

### Practical / Data Processing

- Speed coding: given a complicated JSON file, extract a specific part following some pattern, then feed that to an AI model and get the summary. 30-minute time limit, browser/ChatGPT allowed. [^khushal-kumar]
- Design a concurrent web crawler handling robots.txt, rate limiting, and circular references while maintaining data integrity and freshness. [^linkjob-anthropic]

---

## Behavioral Questions

### Project Deep Dives

- Walk me through an AI project you built end-to-end. [^process-analysis] [^reddit-2026-prep] (very common in 2026)
- Tell me about a project you're most proud of, and what role you played? [^fahd-mirza] [^reddit-2026-prep]
- What is your most challenging work in GenAI? [^igotanoffer]
- Describe a time you reduced hallucinations/cost in production. [^process-analysis] (very common in 2026)
- Describe a time you had to optimize an existing process or workflow for efficiency or scalability. [^proptech-founder-1]
- Describe a challenging prompt engineering problem that you solved. [^proptech-founder-1]
- Is there an actual eval framework, or is it vibes-based? [^exponent-openai]
- Present a "proud" project to a panel: design decisions, trade-offs, what broke, and what you'd change. [^reddit-2026-prep]
- Tell me about your past projects. (Apple, Discord, Anduril) [^exponent-behavioral]
- Tell me about a recent/favorite project and some of the difficulties you had. (Meta) [^igotanoffer-meta]
- Tell me about a technical challenge that you have overcome. [^exponent-behavioral]
- Tell me about the greatest accomplishment of your career. (Meta) [^igotanoffer-meta]
- What level of prompts have you written? What kind of projects did you work on? [^khushal-kumar]

### Conflict and Collaboration

- Give a specific example of conflict with another person, how resolution took form, and the rationale behind the choices you made. [^exponent-openai]
- How do you collaborate with non-technical stakeholders? [^fahd-mirza]
- How do you manage workload in a distributed team? [^fahd-mirza]
- Conflict handling. [^rohit-verma]
- Describe a time you disagreed with a team member about how to approach a problem. How did you handle it? [^interviewnode-behavioral]
- Tell me about a time you struggled to work with one of your colleagues. (Meta) [^igotanoffer-meta]
- Tell me about a time you handled a difficult stakeholder. [^exponent-behavioral]
- Tell me about a time you had to explain a complex technical concept to someone without a technical background. [^interviewnode-behavioral]
- Tell me about a time you convinced someone to change their mind. [^exponent-behavioral]
- What types of team members do you find difficult to work with? (Visa) [^exponent-behavioral]
- Describe communication to resolve ambiguity. (Anthropic) [^prachub-anthropic]
- Describe a time you had trouble communicating with stakeholders and how you overcame it. (OpenAI) [^exponent-openai-behavioral]

### Leadership and Ownership

- Have you mentored teammates remotely? [^fahd-mirza]
- Describe a time you drove technical decisions at scale and guided teams through complex challenges. [^hello-interview]
- Describe a time you mentored engineers who went on to senior roles. [^hello-interview]
- Tell me about a time you showed leadership. (OpenAI EM) [^igotanoffer-openai]
- Tell me about a time you led an initiative or took ownership of a challenging task. [^interviewnode-behavioral]
- Tell me about a time you took the initiative to solve a problem. [^interviewnode-behavioral]
- Tell me about a time when you made short-term sacrifices for long-term gains. [^exponent-behavioral]
- How do you prioritize tasks? [^exponent-behavioral]
- How do you lead under risk and uncertainty? (Anthropic) [^prachub-anthropic]
- As a manager, how do you handle trade-offs? (OpenAI EM) [^igotanoffer-openai]
- How do you manage your team's career growth? (OpenAI EM) [^igotanoffer-openai]
- Tell me about a time when you worked on a project with a tight deadline. [^exponent-behavioral]
- Explain management style, execution strategy, and culture choices. (Anthropic) [^prachub-anthropic]

### Technical Decision-Making

- Which model provider do you prefer for creative writing tasks? [^promptlayer]
- How do you compare AI coding assistants like Cursor, Windsurf, or Claude Code? [^promptlayer]
- What recent AI paper or development caught your attention? [^promptlayer]
- What side projects have you built with AI? [^promptlayer]
- Why a particular storage solution over alternatives? [^exponent-openai]
- How did you decide which model to use for inference? [^exponent-openai]
- What frameworks are you familiar with? What have you built before? [^reddit-ai-eng-questions]
- Which models have you worked with? Which cloud providers are you familiar with? [^reddit-ai-eng-questions]
- Tell me about a time when you solved a complex problem and how you went about it. [^exponent-behavioral]
- Tell me about a time when a technical misjudgment led to a project delay. What did you learn? (Anthropic) [^linkjob-anthropic]
- What would you do if, midway through a project, you realized it was actually unfeasible? (Anthropic) [^linkjob-anthropic]
- Describe a time you had to quickly learn a new technology or methodology to complete a project. [^interviewnode-behavioral] [^x-allie-miller]
- How would you handle real-time versus batch processing for data updates? When is one preferred over the other? [^proptech-founder-2]

### Failure and Learning

- Most challenging project. [^rohit-verma]
- What would you do differently? [^exponent-openai]
- Tell me about a time when you received negative feedback and how you handled it. [^exponent-behavioral]
- What's a mistake you made, and what did you learn from it? [^interviewnode-behavioral]
- Describe a project that didn't go as planned. What did you learn? (Anthropic) [^interviewquery-anthropic]
- Describe a project where your AI solution failed and how you addressed it. (Google DeepMind) [^educative-deepmind]
- Why do you think we should NOT hire you? (Google, Visa) [^exponent-behavioral]
- Tell me about a time when you had to think outside the box to complete a task. [^interviewnode-behavioral]

### AI-Specific Behavioral

- How do you stay updated with fast-changing AI tech? [^process-analysis] [^exponent-behavioral] [^x-michael-taiwo] (very common in 2026)
- How do you collaborate with non-technical stakeholders on AI features? [^process-analysis] (very common in 2026)
- Can you give an example of a time when you addressed ethical concerns in an ML project? [^interviewnode-behavioral]
- Tell me about a time you made a safety-first decision in a project. (Anthropic) [^interviewquery-anthropic]
- Tell me about a time you identified a major risk in an AI system — what did you do? (Mistral) [^datainterview-mistral]
- Describe a time you reduced cost or latency in a production AI system. [^fonzi-ai]
- How do you manage ambiguity in ML projects where requirements and data evolve over time? [^interviewnode-behavioral]
- How do you use AI coding agents in your work? [^youtube-proptech]
- Did you apply GenAI techniques to solve a problem not usually solved with GenAI? [^reddit-devsindia-genai]
- Do you fact-check AI outputs or just trust them? How do you validate AI-generated content? [^x-michael-taiwo]

### Culture and Motivation

- Why OpenAI? / Why Microsoft? / Why this company? [^exponent-openai] [^rohit-verma]
- Why change now? [^rohit-verma]
- Tell me about yourself. [^exponent-behavioral]
- Walk me through your resume. (OpenAI) [^igotanoffer-openai]
- Describe career decisions and culture fit. (Anthropic) [^prachub-anthropic]
- How do you handle AI-safety conflicts with project goals? (Anthropic) [^prachub-anthropic]
- Why do you want to pursue research? (for research roles) [^deepthi-sudharsan]

### AI-Conducted Interview Follow-ups

These are follow-up probes from AI agents conducting interviews (emerging trend at Eightfold.ai):

- How would you handle edge cases? [^eightfold]
- What alternative approaches did you consider? [^eightfold]
- Time and space complexity analysis. [^eightfold]
- Why did you choose this specific data structure? [^eightfold]

---

## Take-Home Assignments

### RAG / Chatbot Systems

- Blood test report AI: Create a project that takes a blood test report in PDF format, understands medical issues, and provides suggestions by fetching them from online blog articles. Submit in a few hours. [^khushal-kumar]
- Customer support RAG chatbot: Design a production-ready chatbot using open-source tools. Requirements: 100+ concurrent users, <2 second latency, grounded in company docs, cost-effective, analytics tracking. Score: 9/10. [^devto-mai-chi-bao]
- Document Q&A system: Build a document Q&A system with citation tracking for multi-hop questions. [^promptlayer]

### Agent Systems

- Build an AI agent demonstrating natural interaction, agentic behavior, clear reasoning steps, and strong technical decision-making. 3-day window. Company: Eightfold.ai. [^eightfold]
- Customer email campaign agent: Build an agent reading customer CSV data and generating personalized email campaigns with evaluation metrics. [^promptlayer]
- Code review agent: Implement a code review agent for Python files with actionable feedback. [^promptlayer]
- Conversational Calendar Booking Agent: LangGraph/LangChain orchestration, Streamlit chat interface, FastAPI backend, Google Calendar integration via Service Accounts, function calling for booking logic. [^process-analysis]
- Create a customer support agent relevant to the company's product within 1.5 hours. Red flag if candidate doesn't start with evals. [^reddit-yc-assignment]
- Build a simple autonomous agent using an open-source LLM with a task-specific goal and an observability/eval layer. [^reddit-yc-assignment]

### Full-Stack AI Applications

- AI-First CRM: HCP Module: React/Redux frontend, FastAPI backend, LangGraph with 5+ tools (summarization, entity extraction). Models: gemma2-9b-it or llama-3.3-70b via Groq API. Deliverable: GitHub repo + 10-15 minute demo video. Expected time: ~60 hours. [^process-analysis]
- Login page with validations: Create a login page accepting email and password with basic validations. Estimated 2-3 hours within 2-3 day window. [^devto-aidi-rivera]

### Evaluation

- Build an evaluation tool for LLM hallucination detection. [^hn-42182365]

### Performance / Optimization

- Anthropic performance take-home: Code optimization for speed. 4-hour limit. Python workload simulating TPU-like operations. Tests low-level optimization skills. Now open-sourced for practice. [^process-analysis]

### OpenAI-Specific

- 48-hour technical project: Take-home assignment delivered day after recruiter call, 48-hour completion window. Practical coding, not puzzle-based. [^linkjob-openai]

### Red Flags (Unreasonable Assignments)

Reported by candidates:
- 72-hour "Round 1" demanding full RAG + agents + UI. [^process-analysis]
- Build an LLM agent to ingest years of financial reports with stock price analysis and chart generation using only freemium APIs. Candidate withdrew, calling it "an unpaid mini-consulting project." [^process-analysis-fr]
- 45 minutes for 3 complex tasks. [^process-analysis]

---

## Sources

[^proptech-founder-1]: [YouTube - Proptech Founder Part 1](https://www.youtube.com/watch?v=leXRiJ5TuQo)
[^proptech-founder-2]: [YouTube - Proptech Founder Part 2](https://www.youtube.com/watch?v=Zt-h5BiBWH0)
[^fahd-mirza]: [YouTube - Fahd Mirza](https://www.youtube.com/watch?v=yr5dRHrnbCo)
[^exponent-mock]: [YouTube - Exponent Mock Interview](https://www.youtube.com/watch?v=ZE_YEn-okfk)
[^youtube-short]: [YouTube Short](https://www.youtube.com/shorts/Nc1y9tYV2WM)
[^igotanoffer]: [igotanoffer - Generative AI System Design Interview](https://igotanoffer.com/en/advice/generative-ai-system-design-interview)
[^interviewnode]: [InterviewNode - GenAI System Design Patterns](https://www.interviewnode.com/post/generative-ai-system-design-interview-patterns-you-should-know)
[^system-design-handbook]: [System Design Handbook](https://www.systemdesignhandbook.com/guides/generative-ai-system-design-interview/)
[^process-analysis]: [Process Analysis - Reddit r/cscareerquestions](https://www.reddit.com/r/cscareerquestions/)
[^process-analysis-fr]: [Process Analysis - Reddit r/developpeurs](https://www.reddit.com/r/developpeurs/)
[^techeon]: [Medium - TechEon Agentic Guide](https://medium.com/@techeon/the-complete-agentic-ai-system-design-interview-guide-2026)
[^promptlayer]: [PromptLayer](https://blog.promptlayer.com/the-agentic-system-design-interview-how-to-evaluate-ai-engineers/)
[^khushal-kumar]: [Medium - Khushal Kumar](https://kaysnotes.medium.com/my-generative-ai-engineer-interview-experience-got-hired-6b3f1affc4e9)
[^exponent-openai]: [Medium - Exponent/Jacob Simon, OpenAI](https://medium.com/exponent/what-its-actually-like-to-interview-at-openai-in-2026-03a646c9436c)
[^colin-zhou]: [Medium - Colin Zhou](https://levelup.gitconnected.com/how-i-fought-and-passed-technical-interviews-with-llms-in-2025-f328e9df8e84)
[^rohit-verma]: [Medium - Rohit Verma, Microsoft](https://medium.com/@rohitverma_87831/microsoft-senior-engineer-interview-experience-2026-the-offer-that-took-me-three-attempts-e0d6e052bdb1)
[^eightfold]: [Medium - Eightfold.ai](https://medium.com/@bhardwajtushar2004/inside-eightfold-ais-agentic-ai-internship-hiring-process-2026-f86dcb625aa8)
[^designgurus]: [DesignGurus](https://www.designgurus.io/blog/openai-system-design-interview-questions)
[^bhavishya-pandit]: [Bhavishya Pandit](https://bhavishyapandit9.substack.com/p/7-deep-cut-ai-system-design-interview)
[^sundeep-teki]: [Sundeep Teki](https://www.sundeepteki.org/advice/the-ultimate-ai-research-engineer-interview-guide-cracking-openai-anthropic-google-deepmind-top-ai-labs)
[^yuan-meng]: [Yuan Meng](https://www.yuan-meng.com/posts/mle_interviews_2.0/)
[^hello-interview]: [Hello Interview - OpenAI L5](https://www.hellointerview.com/guides/openai/l5)
[^linkjob-openai]: [linkjob - OpenAI](https://www.linkjob.ai/interview-questions/openai-loop-interview)
[^linkjob-anthropic]: [linkjob - Anthropic](https://www.linkjob.ai/interview-questions/anthropic-software-engineer-interview/)
[^devto-xai]: [dev.to - xAI](https://dev.to/net_programhelp_e160eef28/xai-software-engineer-interview-2026-full-recap-pitfalls-real-prep-tips-2fl0)
[^devto-mai-chi-bao]: [dev.to - Mai Chi Bao](https://dev.to/mrzaizai2k/how-i-aced-my-llm-interview-building-a-rag-chatbot-2p6f)
[^devto-aidi-rivera]: [dev.to - Aidi Rivera](https://dev.to/aidiri/learn-from-my-mistakes-my-first-take-home-code-challenge-778)
[^reddit-ai-eng-questions]: [Reddit - AI Engineer Interview Questions](https://www.reddit.com/r/ArtificialInteligence/comments/1nybfr8/ai_engineer_interview_questions/) (r/ArtificialIntelligence)
[^reddit-ai-eng-questions-2]: [Reddit - AI Engineer Interview Questions, TonyStank-1704 comment](https://www.reddit.com/r/ArtificialInteligence/comments/1nybfr8/ai_engineer_interview_questions/) (r/ArtificialIntelligence)
[^reddit-hiring-process]: [Reddit - What's the AI Engineering Hiring Process Like?](https://www.reddit.com/r/cscareerquestions/comments/1lmwq1e/whats_the_ai_engineering_hiring_process_like/) (r/cscareerquestions)
[^reddit-prep-ai-eng]: [Reddit - How to Prepare for AI Engineering Interviews](https://www.reddit.com/r/datascience/comments/1ovf9k2/how_to_prepare_for_ai_engineering_interviews/) (r/datascience)
[^reddit-eightfold-ai]: [Reddit - Need Advice for Eightfold.ai Agentic AI Engineer](https://www.reddit.com/r/developersIndia/comments/1pbaj11/need_advice_for_eightfoldai_agentic_ai_engineer) (r/developersIndia)
[^reddit-clear-genai]: [Reddit - How to Clear Interviews in AI/GenAI/RAG/LLM](https://www.reddit.com/r/generativeAI/comments/1p4yrjk/how_to_clear_interviews_in_ai_gen_rag_llm/) (r/generativeAI)
[^reddit-grilled-rag]: [Reddit - Got Grilled in an ML Interview for LangGraph/RAG Projects](https://www.reddit.com/r/LangChain/comments/1k662xc/got_grilled_in_an_ml_interview_today_for_my/) (r/LangChain)
[^reddit-genai-consulting]: [Reddit - Interview Questions Gen AI (consulting)](https://www.reddit.com/r/learnmachinelearning/comments/1ppgsf3/interview_questions_gen_ai) (r/learnmachinelearning)
[^reddit-swe-to-ai]: [Reddit - From Software Developer to AI Engineer](https://www.reddit.com/r/learnmachinelearning/comments/1pzcw2y/from_software_developer_to_ai_engineer_the_exact/) (r/learnmachinelearning)
[^reddit-microsoft-aiml]: [Reddit - Microsoft SWE Applied AI/ML Summer 2026](https://www.reddit.com/r/csMajors/comments/1nqfzhq/microsoft_swe_applied_aiml_summer_2026_redmond) (r/csMajors)
[^reddit-xai-eng]: [Reddit - xAI AI Engineer Backend/Infra Interview](https://www.reddit.com/r/leetcode/comments/1pjhw1i/xai_ai_engineer_backendinfra_interview_just/) (r/leetcode)
[^reddit-2026-prep]: [Reddit - 2026 Interview Prep](https://www.reddit.com/r/leetcode/comments/1q06zz6/2026_interview_prep) (r/leetcode)
[^reddit-yc-assignment]: [Reddit - What Is Your Interview Assignment for AI Engineers?](https://www.reddit.com/r/ycombinator/comments/1jnfijm/what_is_your_interview_assignment_for_ai_engineers/) (r/ycombinator)
[^mimansa-jaiswal]: [Mimansa Jaiswal](https://mimansajaiswal.github.io/posts/llm-ml-job-interviews-resources/)
[^buildml]: [BuildML](https://buildml.substack.com/p/top-24-llm-questions-asked-at-deepmind)
[^hn-46319888]: [HN - LLM Interview Questions](https://news.ycombinator.com/item?id=46319888)
[^hn-29876742]: [HN - Deep Learning Interviews Book](https://news.ycombinator.com/item?id=29876742)
[^llmgenai]: [GitHub - LLM Interview Questions](https://github.com/llmgenai/LLMInterviewQuestions)
[^tidorp]: [GitHub - TidorP/MLJobSearch2025](https://github.com/TidorP/MLJobSearch2025)
[^designgurus-rag]: [DesignGurus - RAG System Design](https://www.designgurus.io/blog/system-design-for-rag)
[^hitendra-patel]: [Medium - Hitendra Patel](https://medium.com/@hitendrapatel)
[^raghu-teja-1]: [Medium - Raghu Teja, IBM Part 1](https://medium.com/@raghu_teja/how-i-cracked-my-ibm-ai-engineer-interview-part-1-technical-e7e4f73be5c4)
[^raghu-teja-2]: [Medium - Raghu Teja, IBM Part 2](https://medium.com/@raghu_teja/how-i-cracked-my-ibm-ai-engineer-interview-part-2-ml-scenarios-88af2b46282e)
[^fahd-mirza-2]: [YouTube - Fahd Mirza (Upwork)](https://www.youtube.com/watch?v=fahd-mirza-upwork)
[^zen-van-riel]: [Zen Van Riel](https://zenvanriel.com/ai-engineer-blog/ai-engineering-interview-big-tech-guide/)
[^fonzi-ai]: [Medium - Fonzi AI](https://medium.com/fonzi-ai/what-ive-learned-from-sitting-in-on-50-ai-engineer-interviews-c493696453c4)
[^exponent-behavioral]: [Exponent - ML Engineer Behavioral Questions](https://www.tryexponent.com/questions?role=ml-engineer&type=behavioral)
[^exponent-openai-behavioral]: [Exponent - OpenAI Behavioral Questions](https://www.tryexponent.com/questions?company=openai&type=behavioral)
[^igotanoffer-openai]: [IGotAnOffer - OpenAI](https://igotanoffer.com/en/advice/openai-interview-questions)
[^igotanoffer-meta]: [IGotAnOffer - Meta ML Engineer](https://igotanoffer.com/blogs/tech/facebook-machine-learning-engineer-interview)
[^interviewnode-behavioral]: [InterviewNode - Behavioral Guide for ML Engineers](https://www.interviewnode.com/post/acing-the-behavioral-interview-a-guide-for-ml-engineers-by-interviewnode)
[^prachub-anthropic]: [Prachub - Anthropic Behavioral & Leadership](https://prachub.com/companies/anthropic/categories/behavioral-and-leadership)
[^interviewquery-anthropic]: [InterviewQuery - Anthropic](https://www.interviewquery.com/interview-guides/anthropic)
[^educative-deepmind]: [Educative - Google DeepMind](https://www.educative.io/blog/google-deepmind-interview-questions)
[^deepthi-sudharsan]: [Medium - Deepthi Sudharsan](https://medium.com/@deepthi.sudharsan/inside-ai-interviews-stories-patterns-and-what-actually-matters-555684c38598)
[^youtube-proptech]: [YouTube - PropTech Mock Interview](https://www.youtube.com/watch?v=proptech-mock)
[^reddit-expdevs-agentic]: [Reddit - Agentic AI System Design Interview](https://www.reddit.com/r/ExperiencedDevs/comments/1r78ipa/agentic_ai_agents_system_design_interview) (r/ExperiencedDevs, Feb 2026)
[^reddit-csuk-agents]: [Reddit - AI Engineering Agents Interview Prep](https://www.reddit.com/r/cscareerquestionsuk/comments/1qmybi3/ai_engineering_agents_interview_prep) (r/cscareerquestionsuk, Jan 2026)
[^reddit-aiagents-prep]: [Reddit - Interview Prep: Deep Learning to Agentic Systems](https://www.reddit.com/r/AI_Agents/comments/1qrxchn/interview_prep_deep_learning_agentic_systems_what) (r/AI_Agents, Jan 2026)
[^reddit-ai-agentic]: [Reddit - What Agentic AI Am I Supposed to Learn?](https://www.reddit.com/r/ArtificialInteligence/comments/1rceuef/what_agentic_ai_am_i_even_supposed_to_learn) (r/ArtificialIntelligence, Feb 2026)
[^reddit-devsindia-genai]: [Reddit - Generative AI Engineer Interview Prep](https://www.reddit.com/r/developersIndia/comments/1oq5fdi/got_an_interview_tomorrow_for_a_generative_ai) (r/developersIndia, Nov 2025)
[^datainterview-openai]: [DataInterview - OpenAI AI Engineer Interview](https://www.datainterview.com/blog/openai-ai-engineer-interview) (prep guide based on candidate reports)
[^datainterview-mistral]: [DataInterview - Mistral ML Engineer Interview](https://www.datainterview.com/blog/mistral-machine-learning-engineer-interview) (prep guide based on candidate reports)
[^hn-39748537]: [HN - RAG vs. Fine-Tuning](https://news.ycombinator.com/item?id=39748537)
[^hn-41541053]: [HN - LLMs Will Always Hallucinate](https://news.ycombinator.com/item?id=41541053)
[^hn-42182365]: [HN - Best Take-Home Coding Tasks](https://news.ycombinator.com/item?id=42182365)
[^hn-42268158]: [HN - Technical Interviews in the LLM Era](https://news.ycombinator.com/item?id=42268158)
[^hn-42313401]: [HN - Automated Reasoning to Remove LLM Hallucinations](https://news.ycombinator.com/item?id=42313401)
[^hn-42431361]: [HN - Agentic LLM Systems in Production](https://news.ycombinator.com/item?id=42431361)
[^hn-42793253]: [HN - AI Orchestration and LLM Routing](https://news.ycombinator.com/item?id=42793253)
[^hn-43884713]: [HN - Is an AI Agent Just an LLM Wrapper?](https://news.ycombinator.com/item?id=43884713)
[^hn-44013971]: [HN - Compress Long LLM Prompts](https://news.ycombinator.com/item?id=44013971)
[^hn-44268335]: [HN - Design Patterns for Securing LLM Agents](https://news.ycombinator.com/item?id=44268335)
[^hn-44796765]: [HN - Sleipner.ai LLM Cost Reduction](https://news.ycombinator.com/item?id=44796765)
[^hn-44875256]: [HN - Interview Questions for AI Product Engineering](https://news.ycombinator.com/item?id=44875256)
[^hn-46229585]: [HN - LLM API Costs in Production](https://news.ycombinator.com/item?id=46229585)
[^hn-46695170]: [HN - Reduce LLM Token Costs with TOON](https://news.ycombinator.com/item?id=46695170)
[^hn-46873753]: [HN - Are LLM Failures Structurally Unavoidable?](https://news.ycombinator.com/item?id=46873753)
[^hn-46959695]: [HN - Early Detection of LLM Hallucinations via ONTOS](https://news.ycombinator.com/item?id=46959695)
[^hn-47150302]: [HN - InferShrink Model Routing](https://news.ycombinator.com/item?id=47150302)
[^x-akshay-pachaar-1]: [X - Akshay Pachaar, ML Deployment Testing (Netflix)](https://x.com/akshay_pachaar/status/1990034795909582860)
[^x-akshay-pachaar-2]: [X - Akshay Pachaar, Distributed Training (Google)](https://x.com/akshay_pachaar/status/1992571349332804081)
[^x-akshay-pachaar-3]: [X - Akshay Pachaar, Model Calibration (Apple)](https://x.com/akshay_pachaar/status/1994020936488734823)
[^x-ali-shohadaee]: [X - Ali Shohadaee, Domain-Specific Tokenization (Anthropic)](https://x.com/alishohadaee/status/2012176441287348231)
[^x-allie-miller]: [X - Allie K. Miller, Adaptability Interview Questions](https://x.com/alliekmiller/status/1967970071248015679)
[^x-ashutosh-1]: [X - Ashutosh Maheshwari, Fine-Tuning vs. Prompting](https://x.com/asmah2107/status/1977413874702745794)
[^x-ashutosh-2]: [X - Ashutosh Maheshwari, Model Drift Diagnosis (Databricks)](https://x.com/asmah2107/status/1990649811964735512)
[^x-athletickoder-1]: [X - athleticKoder, PagedAttention and LLM Serving](https://x.com/athleticKoder/status/1967925267864928669)
[^x-athletickoder-2]: [X - athleticKoder, RAG System Diagnostics](https://x.com/athleticKoder/status/2002355874786873383)
[^x-avi-chawla-1]: [X - Avi Chawla, Unified Query Engine (Google)](https://x.com/_avichawla/status/1986320178783867036)
[^x-interviewstack-meta]: [X - InterviewStack.io, Meta LoRA Question](https://x.com/gnan54796/status/2007302142550565123)
[^x-michael-taiwo]: [X - Michael Taiwo, AI Literacy Interview Questions](https://x.com/AskMichaelTaiwo/status/1987201166157946887)
[^x-aryyann8]: [X - AI Engineer Intern Interview](https://x.com/aryyann8/status/2009314129878896960) (Jan 2026)
[^reddit-genai-product]: [Reddit - Technical Interview for GenAI Engineer Role](https://www.reddit.com/r/leetcode/comments/1rd6yki/technical_interview_for_genai_engineer_role_for_a) (r/leetcode)
[^reddit-amazon-genai]: [Reddit - ML Engineer GenAI Amazon](https://www.reddit.com/r/datascience/comments/1jrdrpx/ml_engineer_genai_amazon/) (r/datascience)
