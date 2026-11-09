#!/usr/bin/env python3
"""Extract structured data from job descriptions using Z.ai LLM."""
import os
import csv
import hashlib
import yaml
import json
import random
import time
import textwrap
from pathlib import Path
from typing import Literal, Optional, List
from datetime import datetime

from dotenv import load_dotenv
from pydantic import BaseModel, Field
from anthropic import Anthropic, APIConnectionError, APITimeoutError, InternalServerError, RateLimitError

# Load .env file
load_dotenv()

# Directories
SCRIPT_DIR = Path(__file__).parent
REPO_ROOT = SCRIPT_DIR.parent  # job-market/
from pipeline_paths import (
    RAW_YAML_DIR,
    STRUCTURED_YAML_DIR,
    dated_output_path,
    find_scraped_date,
    infer_job_id_from_filename,
    iter_files,
    job_date_lookup,
    load_csv_rows,
    resolve_csv_path,
    resolve_nested_file,
)

EXTRACTED_DIR = RAW_YAML_DIR
OUTPUT_DIR = STRUCTURED_YAML_DIR

# Z.ai client
zai_client = Anthropic(
    api_key=os.getenv("ZAI_API_KEY"),
    base_url="https://api.z.ai/api/anthropic",
    max_retries=int(os.getenv("ZAI_CLIENT_MAX_RETRIES", "2")),
    timeout=float(os.getenv("ZAI_TIMEOUT", "120")),
)


# ===== YAML HELPERS =====

class LiteralString(str):
    """String that renders with | in YAML for multiline."""
    pass


def represent_literal_string(dumper, data):
    """YAML representer for literal strings."""
    if '\n' in data or len(data) > 60:
        return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
    return dumper.represent_scalar('tag:yaml.org,2002:str', data)


yaml.add_representer(LiteralString, represent_literal_string)


def write_yaml_with_wrapping(data, file):
    """Write YAML with text wrapping for long strings and inline lists for skills."""

    class FlowList(list):
        """List that renders in flow style."""
        pass

    def represent_flow_list(dumper, data):
        return dumper.represent_sequence('tag:yaml.org,2002:seq', data, flow_style=True)

    yaml.add_representer(FlowList, represent_flow_list)
    yaml.add_representer(LiteralString, represent_literal_string)

    # Fields to wrap: reasoning, use_cases, responsibilities
    wrap_fields = ['reasoning', 'use_cases', 'responsibilities', 'focus']
    # Skill categories
    skill_categories = {'genai', 'ml', 'web', 'databases', 'data', 'cloud', 'ops', 'languages', 'domains', 'other'}

    def _wrap_dict(d, parent_key=''):
        wrapped = {}
        for k, v in d.items():
            key = k
            # Text wrapping for long strings
            if isinstance(v, str) and (k in wrap_fields or any(wf in parent_key for wf in wrap_fields)):
                if len(v) > 60 or '\n' in v:
                    wrapped[k] = LiteralString(textwrap.fill(v, width=60).strip())
                else:
                    wrapped[k] = v
            elif isinstance(v, dict):
                wrapped[k] = _wrap_dict(v, parent_key=k)
            elif isinstance(v, list):
                # Use flow style for skills (under 'skills' key or parent_key is a skill category)
                if k == 'skills' or parent_key in skill_categories or k in skill_categories:
                    wrapped[k] = FlowList(v)
                else:
                    wrapped[k] = [_wrap_dict(item, parent_key=k) if isinstance(item, dict) else item for item in v]
            else:
                wrapped[k] = v
        return wrapped

    wrapped_data = _wrap_dict(data)

    with open(file, 'w', encoding='utf-8') as f:
        yaml.dump(wrapped_data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)


# ===== LLM OUTPUT (FLAT) =====

SkillCategory = Literal['genai', 'ml', 'web', 'databases', 'data', 'cloud', 'ops', 'languages', 'domains', 'other']


class Skill(BaseModel):
    name: str
    category: SkillCategory


class JobExtraction(BaseModel):
    """Flat object returned by LLM."""
    ai_type: Literal['ai-first', 'ml-first', 'ai-support', 'unknown']
    ai_type_reasoning: str
    company_stage: Optional[str] = None
    company_focus: Optional[str] = None
    responsibilities: List[str] = Field(default_factory=list)
    use_cases: List[str] = Field(default_factory=list)
    skills: List[Skill] = Field(default_factory=list)
    is_customer_facing: bool = False
    is_management: bool = False


# ===== FINAL OUTPUT (STRUCTURED) =====

class AIType(BaseModel):
    type: Literal['ai-first', 'ml-first', 'ai-support', 'unknown']
    reasoning: str


class Company(BaseModel):
    name: str
    stage: Optional[str] = None
    focus: Optional[str] = None


class SkillsSummary(BaseModel):
    genai: List[str] = Field(default_factory=list)
    ml: List[str] = Field(default_factory=list)
    web: List[str] = Field(default_factory=list)
    databases: List[str] = Field(default_factory=list)
    data: List[str] = Field(default_factory=list)
    cloud: List[str] = Field(default_factory=list)
    ops: List[str] = Field(default_factory=list)
    languages: List[str] = Field(default_factory=list)
    domains: List[str] = Field(default_factory=list)
    other: List[str] = Field(default_factory=list)


class Position(BaseModel):
    title: str = ""
    ai_type: AIType
    responsibilities: List[str] = Field(default_factory=list)
    use_cases: List[str] = Field(default_factory=list)
    skills: SkillsSummary
    is_customer_facing: bool = False
    is_management: bool = False


class StructuredJob(BaseModel):
    """Final structured object saved to YAML."""
    company: Company
    position: Position
    meta: dict = Field(default_factory=dict)


def location_meta(raw_job: dict) -> dict:
    """Carry the scraped location fields through to the structured output.

    The LLM never sees these - they come straight from the job page's JSON-LD.
    `locations` is only present for multi-location postings.
    """
    meta = {}
    if raw_job.get('location'):
        meta['location'] = raw_job['location']
    if raw_job.get('locations'):
        meta['locations'] = raw_job['locations']
    if raw_job.get('remote'):
        meta['remote'] = True
    return meta


def extractor_fingerprint() -> dict:
    """Which model and prompt produced a record.

    Without this, a silent model change is invisible in the data and has to be
    reconstructed from memory months later. The glm-5.1 to glm-5.2 switch moved
    the AI-First share by up to 10 points and added 6 skills per job before
    anyone noticed. The prompt is identified by a hash so an edit shows up as a
    new value without storing 11KB in every file.
    """
    return {
        'model': os.getenv("ZAI_MODEL", "glm-5.2"),
        'prompt_sha': hashlib.sha256(
            EXTRACTION_SYSTEM_PROMPT.encode("utf-8")).hexdigest()[:12],
    }


def to_structured(job_id: str, title: str, company_name: str, extraction: JobExtraction, extracted_at: str, location: dict = None) -> StructuredJob:
    """Transform flat LLM output into structured final object."""

    skills_by_cat = {cat: [] for cat in ['genai', 'ml', 'web', 'databases', 'data', 'cloud', 'ops', 'languages', 'domains', 'other']}

    for skill in extraction.skills:
        skills_by_cat[skill.category].append(skill.name)

    skills_summary = SkillsSummary(**skills_by_cat)

    return StructuredJob(
        company=Company(
            name=company_name,
            stage=extraction.company_stage,
            focus=extraction.company_focus,
        ),
        position=Position(
            title=title,
            ai_type=AIType(
                type=extraction.ai_type,
                reasoning=extraction.ai_type_reasoning
            ),
            responsibilities=extraction.responsibilities,
            use_cases=extraction.use_cases,
            skills=skills_summary,
            is_customer_facing=extraction.is_customer_facing,
            is_management=extraction.is_management
        ),
        meta={'job_id': job_id, **(location or {}), 'extracted_at': extracted_at,
              **extractor_fingerprint()}
    )


# ===== SYSTEM PROMPT =====

EXTRACTION_SYSTEM_PROMPT = """You are an expert at analyzing job descriptions for AI/ML roles. Extract structured information from the job description.

## AI Type Classification

Apply the steps below in order and stop at the first one that decides. Do not
weigh the steps against each other, and do not let the job title override the
responsibilities.

Step 1 - Does this person shape model behaviour or output quality?

Shaping means doing any of these themselves:
- writing or tuning prompts
- designing retrieval or RAG (chunking, embeddings, reranking, context assembly)
- designing agent flows, tool calling, or multi-agent orchestration
- training, fine-tuning, distilling, or quantizing a model
- choosing between models or evaluating models on the quality of their output
- building evals, guardrails, or output-quality monitoring for a model

Not shaping:
- calling an AI API or endpoint that somebody else designed and configured
- running, hosting, scaling, or serving models that somebody else builds
- moving data to or from a model
- using AI coding assistants to do the engineering work

Step 2 - If the answer to Step 1 is yes, pick by what kind of model is shaped:
- any LLM, agent, or text/code generation component involved -> ai-first
- only classical ML/DL (computer vision, RL, forecasting, recommenders) with no
  LLM or agent component -> ml-first
- generative models whose output is images, audio, speech, or video - TTS,
  diffusion, voice cloning, image generation - are ml-first, not ai-first. The
  work there is training and evaluating a model, not shaping an LLM through
  prompts, retrieval, or tools. A vision-language or speech model that is
  driven by prompts and produces text is ai-first.

Step 3 - If the answer to Step 1 is no -> ai-support.

Step 4 - If the description is too vague to apply Step 1 -> unknown. Use this
only when responsibilities are genuinely absent, not when they are merely brief.

### Edge cases - these are decided, do not re-litigate them

- Serving, hosting, or scaling models the person does not shape is ai-support,
  even when it names vLLM, Triton, TensorRT, KV cache, or GPU clusters. The
  deliverable is capacity, not model behaviour.
- Optimizing a model's own internals (CUDA kernels, quantization, distillation,
  custom training loops) IS shaping. Apply Step 2: ai-first for LLM/generative
  targets, ml-first for classical ones.
- A backend, full-stack, or data engineer on an AI product is ai-first if they
  write prompts or design retrieval or agent flows themselves - even when a
  separate ML team owns training. If they only consume an AI API that another
  team designed, it is ai-support.
- Rolling out AI coding tools (Cursor, Claude Code, Copilot, MCP servers) so
  that other engineers ship faster is ai-support. The deliverable is developer
  workflow. It is ai-first only when those agents or prompts are the product.
- AI named only as a "bonus", "nice to have", or as a tool the engineer uses to
  write code is ai-support.
- Building datasets or pipelines that feed someone else's training runs is
  ai-support, including at an AI lab. Moving, cleaning, and labelling data is
  plumbing.
- Judging model output quality IS shaping, even when the person never runs the
  training. An engineer who ranks, critiques, or repairs model-generated output
  and feeds that back as a reward or preference signal (RLHF, RLAIF, preference
  data, red-teaming, LLM-as-a-judge rubrics) determines what the model learns.
  Apply Step 2: ai-first for LLM targets. This overrides the dataset rule above
  - the distinction is whether the person is judging the model's output or
  merely handling data.
- Safety, governance, validation, or QA oversight of models is ai-support unless
  the person builds the evals or guardrails themselves, which is shaping.
- Forward Deployed Engineers who adapt and deploy AI solutions at customer sites
  are ai-first. Customer-facing never implies ai-support by itself.
- A role that shapes both LLM and classical ML systems is ai-first.
- Judge the role, not the employer. A generic software role at an AI company is
  ai-support.

## Skills

Extract ALL skills as Skill objects {name: string, category: string}.

Categories:
- genai: LangChain, LangGraph, LlamaIndex, DSPy, Haystack, Semantic Kernel, OpenAI/Anthropic APIs, AutoGen, CrewAI, Phidata, Instructor, Marvin, Guardrails, prompt engineering, RAG, agents, function calling, MCP, PEFT, LoRA, or similar GenAI/LLM tools and techniques
- ml: PyTorch, TensorFlow, Keras, JAX, scikit-learn, XGBoost, LightGBM, huggingface, model training, fine-tuning, CUDA, or similar ML/DL frameworks and techniques
- web: FastAPI, Flask, Django, REST, GraphQL, gRPC, Protobuf, OpenAPI, React, Vue, Next.js, or similar web frameworks and APIs
- databases: Postgres, MySQL, Redis, MongoDB, vector DBs (Pinecone, Weaviate, Chroma, Qdrant, Milvus, Faiss, pgvector), Snowflake, BigQuery, or similar databases and data warehouses
- data: Spark, Databricks, Kafka, Airflow, dbt, Prefect, Dagster, Ray, ETL, data pipelines, or similar data engineering tools
- cloud: AWS, Azure, GCP, AI services (Bedrock, SageMaker, Vertex AI, Azure AI Studio), or similar cloud platforms and services
- ops: MLflow, Kubeflow, W&B, Docker, Kubernetes, Terraform, CI/CD, monitoring (Datadog, Prometheus, Grafana, Arize, LangSmith), VLLM, Triton, TensorRT, inference/serving, or similar MLOps/DevOps tools
- languages: Python, TypeScript, Java, Go, Rust, C++, C#, SQL, Scala, or similar programming languages
- domains: CV, NLP, RL, robotics, diffusion models, or similar (ONLY when primary focus)
- other: Anything that doesn't fit the categories above

## Skill Evidence

- Extract a skill only when the description names it, or names an unambiguous
  synonym of it. Never infer a skill because the role or the company implies it.
- Always include every programming language the description names, even when it
  appears once and in passing.
- Umbrella terms - Machine Learning, LLMs, Generative AI, AI Agents, Agentic
  Workflows, Deep Learning - belong in the list only when the description itself
  uses that general term. Do not add the umbrella because a specific instance is
  present: LangChain alone is not "AI Agents", and PyTorch alone is not
  "Machine Learning".
- The reverse also holds: do not name a specific tool or technique the
  description only gestures at generally. "Parameter-efficient fine-tuning" is
  not LoRA, "containerization" is not Docker, "test, build and deploy" is not
  CI/CD, and "modern APIs" is not REST. Record the general term the description
  used, or nothing.
- Do not add process or methodology tags (Agile, Code Review, System Design,
  Responsible AI) unless the description states them as a requirement.

## Skill Normalization (prevents duplicate skills)

Always use the EXACT canonical spelling below, matching case and punctuation. Never invent variants. Most duplicate skills come from casing, parentheticals, and synonyms - eliminate all of them.

Normalization rules:
- No parenthetical expansions: write "MCP", NOT "MCP (Model Context Protocol)"; "RAG", NOT "RAG (Retrieval-Augmented Generation)".
- No casing/plural duplicates - one form only: "Prompt Engineering" (not "prompt engineering"), "REST APIs" (not "REST API" or "RESTful APIs"), "Vector Databases" (not "vector db" or "VectorDBs").
- No acronym/long-form duplicates: "LLMs" (not "Large Language Models"), "GCP" (not "Google Cloud Platform"), "AWS" (not "Amazon Web Services").
- Map synonyms to the canonical name:
  - "rag pipelines" / "rag architectures" -> "RAG"
  - "ai agents" / "agentic ai" / "agents" -> "AI Agents"
  - "agentic workflows" / "agent orchestration" / "multi-agent orchestration" -> "Agentic Workflows"
  - "multi-agent systems" -> "Multi-Agent Systems"
  - "function calling" / "tool use" -> "Function Calling"
  - "openai" / "openai apis" -> "OpenAI API"; "anthropic" / "claude api" -> "Anthropic API"
  - "fine-tuning" / "llm fine-tuning" -> "Fine-Tuning"
  - "embeddings" / "embedding models" -> "Embeddings"
- Each skill appears at most ONCE per job - deduplicate within the category.
- Do NOT emit the same tool in multiple forms (emit "LangChain" once, not also "LangChain framework").

Canonical skill vocabulary (frequently occurring skills, more than 30 postings; use these exact strings):
- genai: LangChain, LlamaIndex, RAG, Prompt Engineering, LLMs, Anthropic API, Gemini, Mistral, Llama, Agentic Workflows, OpenAI API, Azure OpenAI, MCP, Claude Code, Codex, ChatGPT, GitHub Copilot, LangGraph, Generative AI, AI Agents, Embeddings, Multi-Agent Systems, Semantic Search, Haystack, CrewAI, Semantic Kernel, Function Calling, Cursor, AutoGen, Structured Outputs, Guardrails, LoRA, DSPy, Fine-Tuning, AWS Bedrock, LLM Evaluation, Context Engineering, RLHF, Copilot Studio, Google ADK, Conversational AI, Hugging Face
- ml: scikit-learn, PyTorch, TensorFlow, Transformers, Hugging Face, Neural Networks, Machine Learning, CUDA, Fine-Tuning, Reinforcement Learning, Embeddings, Deep Learning, JAX, RLHF, Model Evaluation, NLP, Model Training, Foundation Model Training, CNNs, Anomaly Detection, Feature Engineering, Keras, XGBoost, Quantization, Pandas, NumPy
- web: FastAPI, APIs, WebSockets, React, Microservices, Node.js, REST APIs, Webhooks, Next.js, Angular, Vue, Flask, Django, REST, GraphQL, Streamlit, gRPC, Spring Boot, Playwright, OAuth, CSS, Full-Stack Development, Ruby on Rails, JSON, HTML
- cloud: Vertex AI, AWS, GCP, Azure, IAM, EKS, Azure AI Foundry, Azure OpenAI, SageMaker, Azure ML, AWS Lambda, AWS Bedrock, AWS S3, ECS, API Gateway, Azure Functions, AKS
- ops: MLOps, CI/CD, Jenkins, GitLab CI, Azure DevOps, ArgoCD, Kubernetes, Docker, Linux, TensorRT, DevOps, vLLM, Triton, Git, OpenTelemetry, MLflow, Kubeflow, Model Deployment, Prometheus, Grafana, Distributed Systems, Monitoring, Observability, Terraform, CloudFormation, LangSmith, GitHub Actions, Weights & Biases, Model Monitoring, LLMOps, Langfuse, Datadog, CloudWatch, Infrastructure as Code, GitHub, ELK Stack, Helm, GitOps, DevSecOps, Ansible
- languages: Python, Java, TypeScript, C++, JavaScript, C#, Rust, Go, Bash, PowerShell, SQL, Node.js, .NET, asyncio, Scala, Kotlin, R, Ruby
- databases: Pinecone, Neo4j, Knowledge Graphs, PostgreSQL, Redis, Vector Databases, Milvus, Chroma, Weaviate, MySQL, MongoDB, BigQuery, SQL, NoSQL, pgvector, OpenSearch, Elasticsearch, FAISS, Qdrant, Vector Search, SQL Server, Snowflake, ClickHouse, Redshift, Relational Databases, DynamoDB, Graph Databases, Oracle, Cassandra
- data: Pandas, NumPy, Kafka, Ray, Spark, Data Pipelines, PySpark, Databricks, RabbitMQ, Flink, Airflow, Dagster, Data Engineering, Data Modeling, dbt, Delta Lake, Prefect, Data Governance, Hadoop
- domains: NLP, Computer Vision
- other: Distributed Systems, Code Review, GDPR, Agile, Responsible AI, ServiceNow, Salesforce, HubSpot, System Design, GitHub Copilot, Cursor, n8n, Zapier, HIPAA Compliance, Jira, A/B Testing, Power BI, Power Automate, Tableau, Microservices, Event-Driven Architecture

For a skill not in the vocabulary, still apply the rules: use one consistent Title Case form, no parentheticals, no duplicates.

## Responsibilities

Extract as 4-8 bullet points covering key responsibilities.

CRITICAL FORMAT REQUIREMENTS:
- Each item MUST be a plain string starting with text, NOT a bullet point
- WRONG: "- Build AI systems" or "* Build AI systems" or " - Build AI systems"
- CORRECT: "Build AI systems"

## Use Cases

What the AI/ML system actually DOES - the application domain and problem it solves. Extract as 3-6 bullet points.

CRITICAL FORMAT REQUIREMENTS:
- Each item MUST be a plain string starting with text, NOT a bullet point
- WRONG: "- Enterprise search" or "* Enterprise search" or " - Enterprise search"
- CORRECT: "Enterprise search"

## AI Type Reasoning

Write 2-3 sentences maximum explaining the classification. Be concise.

## Role Flags

is_management - true only when the person manages people. Evidence means the
title is Manager, Director, Head of, VP, or Chief, or the description mentions
direct reports, headcount, hiring for the team, performance reviews, or
managing named engineers. Technical leadership is NOT management: Lead, Staff,
Principal, Architect, "lead the design", "set technical direction", "mentor
juniors", and "influence across teams" are all individual-contributor work.
When the description says individual contributor, it is false regardless of
title. Default to false.

is_customer_facing - true only when the person deals with people outside their
own company as part of the job. Evidence means customer calls or meetings,
on-site deployment, demos, pre-sales support, solution consulting, or working
directly with client engineering teams. Internal stakeholders - product,
design, other engineering squads, "the business" - are NOT customers. Shipping
a product that customers eventually use is NOT customer-facing. Default to
false.

## Company Info

- company_stage: record ONLY when the description states it in words. "Series
  B", "seed-stage", "publicly traded", "Fortune 500", "bootstrapped", "backed
  by <investors>" all count. Leave it empty otherwise. Do not infer a stage
  from what you happen to know about the company, from its size, from its
  customer list, or from the fact that it is hiring - if the text does not say
  it, this field is empty. Most job descriptions do not state a stage, so an
  empty value is the normal case.
- company_focus: What the company does in 5-10 words
"""


# ===== EXTRACTION FUNCTION =====

def retry_delay(attempt: int, *, base: float, cap: float) -> float:
    """Return exponential backoff with small jitter."""
    return min(cap, base * (2 ** attempt)) + random.uniform(0, 1)


def extract_from_job(title: str, company: str, description: str) -> JobExtraction:
    """Extract structured data from a job description using Z.ai."""

    user_prompt = f"""Job Title: {title}
Company: {company}

Description:
{description}

Extract the structured information as specified.

Return valid objects for nested fields (company_info, responsibilities, skills).
"""

    structured_output_tool = {
        "name": "job_extraction",
        "description": "Extracted job information",
        "input_schema": JobExtraction.model_json_schema()
    }

    max_attempts = int(os.getenv("ZAI_MAX_EXTRACTION_RETRIES", "8"))
    for attempt in range(max_attempts):
        try:
            response = zai_client.messages.create(
                model=os.getenv("ZAI_MODEL", "glm-5.2"),
                # Covers thinking tokens too. At 4096 the longer classification
                # prompt truncates before the tool input completes, which shows
                # up as an empty ai_type or a missing tool call.
                max_tokens=int(os.getenv("ZAI_MAX_TOKENS", "8192")),
                system=EXTRACTION_SYSTEM_PROMPT,
                messages=[{"role": "user", "content": user_prompt}],
                tools=[structured_output_tool],
                tool_choice={"type": "tool", "name": structured_output_tool['name']}
            )

            # The model may emit a text preamble before the requested tool call.
            tool_block = next(
                (block for block in response.content if hasattr(block, "input")),
                None,
            )
            if tool_block is None:
                raise ValueError("Response did not contain a tool call")

            # Parse the tool output - Z.ai may return nested JSON strings
            tool_input = tool_block.input
            if isinstance(tool_input, dict):
                # Check if any values are JSON strings that need parsing
                parsed_input = {}
                for key, value in tool_input.items():
                    if isinstance(value, str):
                        try:
                            parsed_input[key] = json.loads(value)
                        except:
                            parsed_input[key] = value
                    else:
                        parsed_input[key] = value
                tool_input = parsed_input

            extraction = JobExtraction.model_validate(tool_input)
            return extraction
        except RateLimitError:
            if attempt == max_attempts - 1:
                raise
            wait = retry_delay(attempt, base=10, cap=120)
            print(f"  Rate limited, retrying in {wait:.1f}s")
            time.sleep(wait)
        except (APIConnectionError, APITimeoutError, InternalServerError) as e:
            if attempt == max_attempts - 1:
                raise
            wait = retry_delay(attempt, base=5, cap=60)
            print(f"  Transient API error ({type(e).__name__}), retrying in {wait:.1f}s")
            time.sleep(wait)
        except Exception as e:
            print(f"  Extraction attempt {attempt + 1} failed: {e}")
            if attempt == max_attempts - 1:
                raise
            wait = retry_delay(attempt, base=3, cap=30)
            print(f"  Retrying in {wait:.1f}s")
            time.sleep(wait)

    raise Exception("Failed to extract valid output after retries")


def extract_job(
    yaml_file: Path,
    *,
    date_lookup: dict[str, str] | None = None,
) -> tuple[Path | None, dict | None]:
    """Extract structured data from a job YAML file.

    Returns:
        tuple: (output_path, structured_data_dict)
    """
    with open(yaml_file, 'r', encoding='utf-8') as f:
        job = yaml.safe_load(f)

    job_id = str(job.get('job_id', ''))
    title = job.get('title', '')
    company = job.get('company', '')
    description = job.get('description', '')

    print(f"Processing: {title} at {company}")

    # Extract using LLM
    try:
        extraction = extract_from_job(title, company, description)
    except Exception as e:
        print(f"  Error: {e}")
        import traceback
        traceback.print_exc()
        return None, None

    scraped_date = find_scraped_date(job_id, path=yaml_file, date_lookup=date_lookup)
    if not scraped_date:
        print(f"  Error: could not determine scraped_date for {yaml_file.name}")
        return None, None

    # Transform to structured output
    structured = to_structured(
        job_id=job_id,
        title=title,
        company_name=company,
        extraction=extraction,
        extracted_at=datetime.now().isoformat(),
        location=location_meta(job)
    )

    output_path = dated_output_path(OUTPUT_DIR, scraped_date, yaml_file.name)

    print(f"  AI Type: {extraction.ai_type}")
    print(f"  Skills: {len(extraction.skills)}")

    return output_path, structured.model_dump()


def load_csv_ids(csv_path):
    """Load job IDs from a CSV file."""
    ids = set()
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            job_id = row.get("id", "")
            if job_id:
                ids.add(str(job_id))
    return ids


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Enrich jobs with LLM extraction')
    parser.add_argument('yaml_file', nargs='?', help='Specific YAML file to process')
    parser.add_argument('--all', action='store_true', help='Process all YAML files')
    parser.add_argument('--csv', type=str, help='CSV file to filter which YAML files to process (by job ID)')
    parser.add_argument('--limit', type=int, help='Limit number of files to process')
    parser.add_argument('--shard-count', type=int, default=1, help='Split work into this many deterministic shards')
    parser.add_argument('--shard-index', type=int, default=0, help='Zero-based shard to process')
    parser.add_argument('--out-dir', type=str, default=None,
                        help='Staging output root (dated subdirs, same layout as data_structured). '
                             'Use for model/prompt trials - never extract trials over data_structured/')
    args = parser.parse_args()

    if args.shard_count < 1:
        parser.error('--shard-count must be at least 1')
    if not 0 <= args.shard_index < args.shard_count:
        parser.error('--shard-index must be between 0 and shard-count - 1')

    if not os.getenv("ZAI_API_KEY"):
        print("Error: ZAI_API_KEY environment variable not set")
        return

    if args.out_dir:
        global OUTPUT_DIR
        OUTPUT_DIR = Path(args.out_dir)
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        print(f"Staging output root: {OUTPUT_DIR}")

    # Load CSV filter if provided
    csv_ids = None
    csv_dates = None
    if args.csv:
        csv_path = resolve_csv_path(args.csv, relative_to=SCRIPT_DIR)
        csv_rows = load_csv_rows(csv_path)
        csv_ids = {row["id"] for row in csv_rows if row.get("id")}
        csv_dates = job_date_lookup(csv_rows)
        print(f"Filtering to {len(csv_ids)} job IDs from {csv_path.name}")

    if args.yaml_file:
        # Process single file
        yaml_file = resolve_nested_file(EXTRACTED_DIR, args.yaml_file)
        if not yaml_file.exists():
            print(f"File not found: {yaml_file}")
            return

        output_file, output = extract_job(yaml_file, date_lookup=csv_dates)
        if output:
            write_yaml_with_wrapping(output, output_file)

            print(f"\nSaved: {output_file}")

    elif args.all:
        # Process all files (optionally filtered by CSV)
        yaml_files = iter_files(EXTRACTED_DIR, "*.yaml")

        if csv_ids is not None:
            yaml_files = [f for f in yaml_files if infer_job_id_from_filename(f) in csv_ids]

        if args.shard_count > 1:
            yaml_files = [
                yaml_file
                for index, yaml_file in enumerate(yaml_files)
                if index % args.shard_count == args.shard_index
            ]
            print(f"Shard {args.shard_index + 1}/{args.shard_count}: {len(yaml_files)} files")

        if args.limit:
            yaml_files = yaml_files[:args.limit]

        print(f"Processing {len(yaml_files)} YAML files...\n")

        results = {'ai-first': 0, 'ml-first': 0, 'ai-support': 0, 'unknown': 0}
        errors = []
        skipped = 0

        for i, yaml_file in enumerate(yaml_files, 1):
            job_id = infer_job_id_from_filename(yaml_file)
            scraped_date = find_scraped_date(job_id, path=yaml_file, date_lookup=csv_dates)
            if not scraped_date:
                errors.append((yaml_file.name, "missing scraped_date"))
                print(f"[{i}/{len(yaml_files)}] {yaml_file.name[:50]}... ERROR: missing scraped_date")
                continue

            output_file = dated_output_path(OUTPUT_DIR, scraped_date, yaml_file.name)

            # Skip if already processed
            if output_file.exists():
                skipped += 1
                continue

            try:
                output_file, output = extract_job(yaml_file, date_lookup=csv_dates)
                if output:
                    write_yaml_with_wrapping(output, output_file)

                    results[output['position']['ai_type']['type']] += 1

                    print(f"[{i}/{len(yaml_files)}] {scraped_date}/{yaml_file.name[:50]}... -> {output['position']['ai_type']['type']}")
            except Exception as e:
                errors.append((yaml_file.name, str(e)))
                print(f"[{i}/{len(yaml_files)}] {yaml_file.name[:50]}... ERROR: {e}")

        print(f"\n{'='*60}")
        print(f"Results:")
        print(f"  AI-First: {results['ai-first']}")
        print(f"  ML-First: {results['ml-first']}")
        print(f"  AI-Support: {results['ai-support']}")
        print(f"  Unknown: {results['unknown']}")
        print(f"  Skipped: {skipped}")
        print(f"  Errors: {len(errors)}")

        if errors:
            print(f"\nErrors:")
            for name, err in errors[:5]:
                print(f"  {name}: {err}")
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
