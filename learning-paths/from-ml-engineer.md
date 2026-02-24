# From ML Engineer to AI Engineer

This is probably the easiest transition. The roles are very similar. You just replace a call to a locally hosted model with a call to OpenAI. The rest is the same.


## What You Already Have

- Production ML systems - deployment, serving, monitoring
- Python, PyTorch/TensorFlow
- Docker, Kubernetes, CI/CD
- Model evaluation and metrics
- Cloud platforms (AWS, Azure, GCP)
- MLOps practices - MLflow, experiment tracking
- Infrastructure management
- Fine-tuning experience


## What You Need to Learn

- LLM APIs - OpenAI, Anthropic (you are used to hosting models yourself)
- Prompt engineering and prompt versioning
- RAG patterns - vector databases, retrieval strategies, chunking
- Agent patterns - LLMs with tools, orchestration loops, step limits
- LLM-specific evaluation - different from traditional ML metrics. Think about hallucination detection, answer quality, tool usage correctness
- Frameworks - LangChain, LangGraph, LlamaIndex


## Why This Transition Works

The task of an ML engineer is to integrate machine learning into the product. The task of an AI engineer is to integrate AI into the product. The difference: AI engineers typically use third-party models via APIs, while ML engineers own the model weights.

Everything you know about model serving, monitoring, CI/CD, and production reliability applies directly. ML engineers are more focused on engineering but would need to work on the evaluation side specific to LLMs.


## Suggested Path

1. Start calling LLM APIs - OpenAI, Anthropic. Understand structured outputs, function calling
2. Learn prompt engineering - iteration, testing, versioning (similar to experiment tracking you already know)
3. Build a RAG system - vector DBs, embeddings (you know embeddings), retrieval + generation
4. Build an agent - tool use, orchestration loops, multi-step evaluation
5. Learn LLM-specific evaluation - LLM-as-judge, golden datasets for generation quality


## Timeline

The fastest transition of all roles. You already have the engineering foundation and production mindset. Focus on the LLM-specific patterns and you can be productive quickly.


## Your Advantage

You understand model behavior deeply. When an LLM is not performing well, you can reason about why - is it a prompt issue, context issue, or model limitation? You also know how to serve models locally when API-based solutions are not suitable (privacy, latency, cost). This is valuable for the subset of roles that need self-hosted LLMs.
