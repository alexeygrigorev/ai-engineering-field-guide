# AI Engineering Job Market Trends - Appendix

Detailed tables, cluster signatures, methodology, and reproduction notes for [the trends summary](07-trends.md).

## Data and methodology

10 scrapes of builtin.com, each an independent cross-section:

- Feb 4: 895 postings
- Feb 27: 870
- Mar 27: 680
- Apr 22: 645
- May 29: 919
- Jun 25: 888
- Jul 22: 846
- Aug 25: 1,222
- Sep 23: 1,086
- Nov 6: 1,709

Total: 9,760 postings. Job IDs do not overlap between scrapes, so I treat each month as a fresh sample of the market. Percentages are the share of postings (within a given denominator) whose structured skill / use-case / title fields match.

Roles are tagged ai-first (the core AI engineer), ai-support (software/ML/data roles with AI scope), ml-first (traditional ML), or unknown. The headline analyses run within ai-first unless noted, since that is where the role is actually being defined.

Extraction runs on `model: glm-5.2` with `prompt_sha: ef6fdeb19af2` in every file's `meta`, consistent across all 10 scrapes.

Skills are normalized through [canonicalize_skills.py](../job-market/_internal/analysis/canonicalize_skills.py), which collapses case, acronym, and synonym variants into one canonical form per concept and round-trips byte-stable across all 9,760 files (201,361 total skill entries). The extraction prompt in [extract_llm.py](../job-market/_internal/extract_llm.py) enforces a canonical vocabulary scoped to skills appearing more than 30 times.

The "slope" metric in the trajectory sections is the slope of an OLS line fit to the 10 monthly shares, in percentage points per scrape.

## Cluster signatures

Spherical k-means (cosine distance, k-means++ init, k=6, seed=7, implemented in numpy) on a 31-skill binary signature per posting. K-means originally split the agent-building population into two clusters (n=1,545 and n=1,373), differing almost entirely on whether `Prompt Engineering` was tagged as a skill (95% vs 0% - `Agents` and `MCP` shares were high in both). That's a skill-tagging artifact, not a distinct role, so I merged them into one Agent builder cluster below (k=5 effective).

Each cluster's top skills (share of cluster members, with lift over baseline):

- Agent builder (2,918 postings, 29.9%, ~87% ai-first). Combines the `Agents` (99%) + `MCP` (21%) cluster (1,373 postings) and the `Prompt Engineering` (95%) + `Agents` (77%) + `Function Calling` (31%) + `OpenAI`/`Anthropic API` (27%) + `Coding tools` (23%) cluster (1,545 postings). Largest archetype.
- RAG app builder (2,593 postings, 26.6%, 96% ai-first). `LangChain` 63% (x2.8), `LangGraph` 42% (x2.8), vector databases 67% (x2.6), `Fine-Tuning` 33% (x2.2), `FastAPI`/`Flask` 22% (x2.1), AI cloud services 29% (x2.1), `RAG` 89% (x2.1).
- DevOps / full-stack engineer (1,646 postings, 16.9%, only 34% ai-first). `Kubernetes` 54% (x2.1), `Docker` 52% (x2.0), `CI/CD` 75% (x1.9), `Terraform` 24% (x1.9), `React`/frontend 28% (x1.8), `SQL` 24% (x1.6), `AWS` 49% (x1.2) - the least AI-native group.
- Cloud / ML platform engineer (1,377 postings, 14.1%, 48% ai-first). `GCP` 91% (x2.9), `Azure` 71% (x2.2), `Terraform` 27% (x2.1), `AWS` 77% (x1.8), `PyTorch`/`TensorFlow` 29% (x1.5), `Agents` 30% (x0.5).
- ML trainer / researcher (618 postings, 6.3%, 49% ai-first). `PyTorch`/`TensorFlow` 75% (x4.0), inference/serving 56% (x3.7), `MLOps` 31% (x1.6). Still the smallest archetype.

## AI-type mix (% of all postings)

| Type | Feb 4 | May 29 | Aug 25 | Nov 6 |
|---|---|---|---|---|
| ai-first | 71.5 | 69.2 | 70.2 | 62.6 |
| ai-support | 22.2 | 24.5 | 23.2 | 32.9 |
| ml-first | 5.9 | 4.5 | 5.0 | 3.5 |

Ai-first held in a tight 68-72% band across the first nine scrapes before dipping to 62.6% in November as ai-support jumped to 32.9%.

## Integrator vs trainer (within ai-first)

First and last values:

- Trainer stack (`PyTorch`/`TensorFlow`/`Fine-Tune`/`CUDA`): 37.5% to 27.2%
- Integrator stack (`RAG`/agents/APIs): 80.0% to 91.7%
- Pure integrator: 50.9% to 66.8%
- Pure trainer: 8.4% to 2.3%
- Neither: 11.6% to 6.0%

## Agent-framework churn (share among jobs using any framework)

First and last values:

- `LangChain`: 86.3% to 76.8% - still largest, though share among framework users eased
- `LangGraph`: 37.7% to 71.0% - the fast riser, now nearly matching `LangChain`
- `LlamaIndex`: 28.6% to 30.6%
- `CrewAI`: 16.6% to 26.2%
- `AutoGen`: 10.9% to 25.1%
- `Semantic Kernel`: 6.9% to 22.1% - tripled share
- `DSPy`: 5.7% to 1.9%

`LangChain`'s dominance isn't disappearing so much as teams are layering orchestration frameworks alongside it - `LangGraph` most often, with `CrewAI`, `AutoGen`, and `Semantic Kernel` all taking substantial share.

## ai-first sub-archetypes (within ai-first)

First and last values:

- Has RAG skill: 43.4% to 57.7%
- Has agent skill: 63.8% to 82.3%
- Fine-tuner: 24.2% to 21.3%
- Inference / serving: 19.8% to 13.5%
- RAG and agents (both): 33.1% to 51.0% - now a majority of ai-first jobs
- Agents but not RAG: 30.6% to 31.3%

## Use-case themes (% of postings, first to last)

- Automation / workflow: 52.2% to 51.8% (peaked at 64.6% in June)
- Agents / autonomous: 43.0% to 49.9%
- Search / retrieval: 19.8% to 21.9%
- RAG / Q&A: 13.6% to 18.7%
- Copilot / dev tools: 23.0% to 17.1%
- Document / extraction: 12.3% to 15.9%
- Analytics / BI: 18.5% to 12.9%
- Recommend / personalize: 12.8% to 5.9% - fading
- Chatbot / assistant: 12.6% to 10.6%
- Customer support: 4.4% to 1.6%

## Responsibility verbs (% of postings, first to last)

- build / develop: 97.3% to 98.5% - near-universal
- design / architect: 84.9% to 69.5%
- ship / deploy / integrate: 78.2% to 64.1%
- collaborate / partner: 77.9% to 58.8%
- evaluate / test: 68.9% to 65.1%
- train / research / optimize: 64.5% to 51.3%
- scale / performance: 62.9% to 55.5%

## Eval and LLMOps maturity (% of postings, first to last)

- LLM-native eval (any of `LangSmith`, `Langfuse`, `Guardrails`, `LLM Evaluation`): 26.7% to 34.5%
- Classic MLOps (`MLflow`, `Kubeflow`): 19.9% to 14.5%
- `Guardrails`: 10.2% to 17.5%
- `LangSmith`: 1.9% to 3.6%
- `Langfuse`: 1.9% to 3.0%
- `LLM Evaluation` (explicit): 20.3% to 26.6%
- Weights & Biases: 0.9% to 1.8%
- Infrastructure monitoring (general): 6.4% to 7.0% - flat

Eval tooling is migrating from ML-style tracking toward LLM-native evaluation and guardrails, but most postings still name no dedicated eval tool at all - "LLM Evaluation" as a bare requirement is far more common than any named product.

## GenAI skill trajectories (first to last, with slope)

Rising (slope, pp per scrape):

- `MCP`: 9.9% to 20.4%, +0.94
- `Function Calling`: 9.6% to 18.5%, +0.88
- `Prompt Engineering`: 26.1% to 34.2%, +0.79
- `Guardrails`: 10.2% to 17.5%, +0.77
- Coding tools (`Claude Code`/`Copilot`/`Cursor`): 3.5% to 10.5%, +0.77
- `LLM Evaluation`: 20.3% to 26.6%, +0.76
- `RAG`: 32.8% to 38.2%, +0.68
- `LangGraph`: 7.4% to 15.2%, +0.66

Declining:

- `Fine-Tuning`: 17.1% to 9.4%, -0.93
- `PyTorch`: 20.8% to 12.5%, -0.86
- `TensorFlow`: 12.2% to 7.1%, -0.72

Roughly flat:

- `Kubernetes`: 22.5% to 21.8%, -0.08
- `Docker`: 20.9% to 23.3%, -0.02
- `AWS Bedrock`: 3.4% to 5.7%, -0.01
- `Agents`: 40.1% to 40.7%, -0.01
- `RLHF`: 0.3% to 0.8%, +0.02

`MCP` and `Function Calling` are now the fastest-rising named skills, with `Prompt Engineering`, `Guardrails`, coding tools, and `LLM Evaluation` close behind. `SQL` is not a standout riser (11.1% to 14.9%).

## AI coding tools

AI coding tools (`Claude Code`, `GitHub Copilot`, `Cursor`, `Codex`) as a listed skill: 7.6% of postings in February to 13.6% in November - peaking at 16.2% in June. The rise is present in both segments: ai-first roles went from 5.5% to 10.2%, ai-support from 2.1% to 3.3%.

## AI infra emergence (within ai-first, %)

The dedicated AI-infra role still hasn't emerged at scale:

- Any inference/serving (`vLLM`, `Triton`, `TensorRT`, `CUDA`, `Model Deployment`): 19.8% to 13.5%
- `Model Deployment`: 18.3% to 8.3%
- `CUDA`: 0.3% to 3.9%
- `vLLM`: 1.1% to 2.7%
- `Triton`: 0.5% to 1.0%
- `TensorRT`: 0.5% to 1.0%
- `Kubernetes` (general, infra proxy): 18.6% to 23.8% - rising, absorbed into platform work

This remains a null finding on the AI-infra-as-a-standalone-role question: inference/serving work is concentrating into the platform/infra archetype rather than growing its own dedicated posting category.

## Skill co-occurrence lift

Lift = P(B given A) / P(B) across all 9,760 postings. Lift above 1 means B is over-represented in A-jobs. Top pairs by lift:

- `LangChain` pulls `LangGraph` at 50% (lift 3.5) - still the strongest pair in the dataset
- `Docker` pulls `Kubernetes` at 71% (lift 3.0)
- `MCP` pulls `Function Calling` (2.4), `LangGraph` (2.4)
- `OpenAI API` pulls `LangGraph` (2.3), `FastAPI` (2.3), `Embeddings` (2.2)
- `RAG` pulls `Embeddings` (lift 2.2), vector databases (2.0), `Function Calling` (1.9), `LangGraph` (1.9)
- `Fine-Tuning` pulls `Embeddings` (2.2), `MLOps` (2.2), `LangGraph` (2.0)
- `PyTorch` pulls `MLOps` (2.3), vector databases (1.5), `AWS` (1.4), `Kubernetes` (1.3)

Two cleanly separated stacks persist: a RAG/application stack (RAG, embeddings, vector databases, LangGraph, function calling) and a PyTorch/training-infra stack (PyTorch, MLOps, Kubernetes, AWS) - `MCP` and `Fine-Tuning` both sit closer to the application stack than the training one.

## Company stage over-index (skills)

Over/under-index versus the whole-market baseline, by funding stage. Sample sizes: early (Seed-Series A) 375, growth (Series B-F) 247, public/late 311. Baseline: ai-first 68.9%, `RAG` 40.1%, agents 56.2%, `Fine-Tuning` 14.2%, coding tools 11.6%, `PyTorch`/`TensorFlow` 17.5%, `AWS` 39.3%, `Docker`/`Kubernetes` 30.7%.

- Early-stage (Seed-Series A): over-index on ai-first (x1.16) and `Fine-Tuning` (x1.28); sharply under-index on `PyTorch`/`TensorFlow` (x0.58), `AWS` (x0.58), `Docker`/`Kubernetes` (x0.55)
- Growth (Series B-F): over-index on coding tools (x1.29) and `AWS` (x1.14); under-index on `RAG` (x0.74), `Fine-Tuning` (x0.54), `PyTorch`/`TensorFlow` (x0.44)
- Public / late-stage: over-index on `RAG` (x1.22), `Fine-Tuning` (x1.22), and `Docker`/`Kubernetes` (x1.13)

## Title predicts the stack

Title-group sizes and signatures:

| Title group | n | % ai-first | % customer-facing | Signature |
|---|---|---|---|---|
| `ai engineer` | 3,006 | 88 | 17 | 56% RAG, 70% agents, 24% PyTorch/TF |
| `software` / `backend engineer` | 2,395 | 57 | 9 | 30% RAG, 51% agents, 26% Kubernetes |
| `ml engineer` / `scientist` | 750 | 73 | 10 | 46% RAG, 47% agents, 48% PyTorch/TF |
| `applied` (excludes FDE titles) | 549 | 91 | 29 | 51% RAG, 77% agents, 13% PyTorch/TF |
| Forward Deployed / FDE | 287 | 95 | 85 | 54% RAG, 78% agents, 10% PyTorch/TF |
| `platform` / `infra` / `devops` | 1,010 | 48 | 12 | 28% RAG, 49% agents, 43% Kubernetes |
| `data engineer` | 237 | 46 | 8 | 43% RAG, 39% agents, 88% Python |

Forward Deployed / FDE is the only group that is majority customer-facing, and by a wide margin - 85% versus 8-29% everywhere else.

## Forward Deployed Engineer (FDE)

I found 287 FDE postings (2.9% of the market) using the `forward[\s-]*deploy|\bfde\b` pattern in `deep_trends2.py`. Monthly share: 2.0% in February, peaking at 4.4% in July, 3.1% in September, and 3.9% in November.

| Metric | FDE | Other ai-first |
|---|---|---|
| ai-first | 95% | 100% |
| ai-support | 4% | 0% |
| customer-facing | 85% | 15% |
| RAG | 54% | 55% |
| agents | 78% | 74% |
| PyTorch/TF | 10% | 19% |
| fine-tuning | 16% | 20% |
| Python | 67% | 76% |
| AWS | 37% | 42% |

The FDE remains a customer-facing, ship-fast generalist: RAG-and-agents fluent but lighter on research than other ai-first roles. Use cases cluster around enterprise automation, workflows, and production agent systems.

## Skill breadth is roughly flat

Average skills per posting (including umbrella terms like "LLMs" and "Machine Learning"):

- Total skills: 18.4 (Feb) to 19.2 (Nov), peaking at 22.8 in Feb 27
- GenAI skills: 4.6 to 5.1 (peaking at 5.9 in June-July)

Postings aren't accumulating requirements over time - breadth has bounced in a 18-23 skill range all year rather than trending up.

## Seniority (% of postings, first to last)

- Staff and above: 18.5% to 11.4% - the clearest decline
- Senior: 30.8% to 25.7%
- Mid: 43.9% to 55.8%
- Lead: 4.6% to 5.6%
- Management / Director: 0.7% to 0.7%
- Junior / entry-level: 1.5% to 0.8% - effectively absent throughout

The bottom rung of the posted market has been essentially closed since February, and Staff+ postings have thinned as a share of the market.

## Reproduction

The analysis scripts live in [job-market/_internal/analysis/](../job-market/_internal/analysis/). Run them with uv from the `job-market/` directory:

- `uv run python _internal/analysis/canonicalize_skills.py --check` - verify skill normalization is byte-faithful
- `uv run python _internal/analysis/trends.py` - monthly volume, ai-type mix, seniority, and per-skill share tables
- `uv run python _internal/analysis/deep_trends.py` - integrator/trainer index, framework churn, co-occurrence lift, use-case themes
- `uv run python _internal/analysis/deep_trends2.py` - clustering, company-stage over-index, infra emergence, responsibility verbs, eval maturity, skill trajectories, title-to-stack, FDE
- `uv run python _internal/analysis/charts.py` - renders the five charts in [images/](../job-market/images/)

The clustering is deterministic (seed=7) and implemented in numpy so no sklearn dependency is needed.
