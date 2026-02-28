# Learning Path for AI Engineers

What to learn and in what order, based on skill demand from 895 job descriptions and the [AI Engineering Buildcamp](https://maven.com/alexey-grigorev/from-rag-to-agents) curriculum.


## Core Skills

The most important 20% that accounts for 80% of the work. Based on the [AI Engineering Buildcamp](https://maven.com/alexey-grigorev/from-rag-to-agents) curriculum and [job market research](../role/02-skills.md).

### LLM Fundamentals

- How LLMs work, what they can and cannot do
- OpenAI/Anthropic APIs - calling LLMs, getting responses
- Structured output - getting consistent, typed responses
- Prompt engineering - writing effective prompts for different tasks

### RAG and Search

- RAG - augmenting LLMs with your own data
- Text search and vector search - like Elasticsearch, Qdrant
- Chunking strategies for different document types
- Processing different data sources - PDFs, YouTube transcripts, web pages

Practice projects: FAQ assistant, document Q&A system, content management search

### AI Agents

- Function calling and tool use - LLMs that can take actions
- The agentic tool-call loop - how agents reason and act
- Agent frameworks - like PydanticAI, OpenAI Agents SDK, LangChain, Google ADK
- Model Context Protocol (MCP) - creating tools for other agents
- Multi-agent systems - routing, pipelines, coordination

Practice projects: web research agent, automated data extraction pipeline, multi-agent workflow


### Testing

- Writing tests for agents - testing tool calls, output quality
- LLM-as-judge - using one LLM to evaluate another


### Monitoring and Observability

- Logging and tracing agent runs - like OpenTelemetry, Logfire, Jaeger
- Cost monitoring and usage tracking
- User feedback tracking
- Building monitoring dashboards - like Grafana


### Evaluation

- Offline evaluation - generating eval data, validating agents
- Evaluating retrieval quality
- Synthetic data generation for evaluations
- Prompt optimization based on eval results


### Production

- Converting notebooks to production projects
- Deployment - like Streamlit for prototypes
- Cloud platforms for production - like AWS, GCP, Azure
- Guardrails - safety constraints for agents
- Parallel processing for large datasets


## Other Skills

Based on the [job market research](../role/02-skills.md). These are not covered in the core path above but frequently appear in job descriptions.

### Python and Software Engineering

- Python is mandatory - used in 82.5% of jobs
- Testing, CI/CD, code quality - expected of every engineer
- Git workflows and code review

### Web Development

- FastAPI - the most common Python web framework for AI
- React, Next.js - for full-stack AI products
- REST APIs, GraphQL, microservices

### Cloud and Infrastructure

- AWS, Azure, GCP - at least one cloud platform
- Docker and Kubernetes - containerization and orchestration
- Terraform - infrastructure as code

### Databases

- PostgreSQL - the default database
- Vector databases - Pinecone, Weaviate, Qdrant, pgvector
- Redis - caching and session management

### ML Fundamentals

- PyTorch basics - 22.0% of AI-First roles
- Embeddings - understanding vector representations
- Fine-tuning - when API-based models are not enough
- Model evaluation - traditional ML metrics

### Data Engineering

- Data pipelines - Airflow, Spark, Kafka
- ETL and data processing
- Databricks, Snowflake

### Additional Languages

- TypeScript - second most popular language for AI engineering
- Java, Go - for backend-heavy roles
- SQL - for data access and analytics


## Role-Specific Guides

Already have experience? Start from where you are:

- [From Data Engineer](from-data-engineer.md) - smoothest transition, 3-4 months
- [From Data Scientist](from-data-scientist.md) - evaluation is your superpower, add engineering
- [From ML Engineer](from-ml-engineer.md) - easiest transition, replace model call with API call
- [From Backend Engineer](from-backend-engineer.md) - 2-3 months, add AI on top of engineering
- [From Frontend Engineer](from-frontend-engineer.md) - backend first, then AI, unique full-stack advantage


## The Typical AI Engineering Stack

- Application - React, Next.js, FastAPI
- AI orchestration - LangChain, LangGraph, PydanticAI
- LLM APIs - OpenAI, Anthropic, Groq, local models
- Vector databases - Pinecone, Weaviate, Qdrant, pgvector
- Infrastructure - Docker, K8s, AWS/GCP/Azure
- Monitoring - Logfire, Grafana, OpenTelemetry
- Evaluation - LLM judges, Evidently


## Skills by Priority

### Must have

- Python
- Prompt engineering
- RAG patterns
- At least one cloud platform - AWS, Azure, GCP
- Docker

### High value

- LangChain or PydanticAI
- TypeScript
- FastAPI
- Kubernetes
- CI/CD
- PyTorch basics

### Differentiators

- Agent frameworks - LangGraph, CrewAI
- Fine-tuning
- Evaluation frameworks
- Vector databases - Pinecone, Weaviate, Qdrant
- Multi-agent patterns
