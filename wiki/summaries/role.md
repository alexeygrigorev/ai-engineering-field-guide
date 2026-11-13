# Role Section (repo: role/)

- Sources: [role/](../../role/) - analysis of the AI engineer role from 9,760 job descriptions scraped from builtin.com in 10 monthly scrapes, Feb 4 - Nov 6, 2026 ([dataset](../../job-market/README.md))
- Related: [AI engineer role](../concepts/ai-engineer-role.md), [evaluation as the differentiator](../concepts/evaluation-differentiator.md), [job-market pipeline](job-market.md), [learning paths](learning-paths.md)

## What the section says

The role section is the analytical core of the field guide. Its headline: "AI Engineer" in 2026 is a new, distinct, mostly full-stack role built on integrating pre-trained models (RAG, agents, orchestration), not training them. Three role types hide under one title: AI-First 68.9%, AI-Support 25.7%, ML rebranded 4.5% (role/README.md). 86.9% of AI-First roles need skills beyond GenAI; only 4.0% expect pure GenAI work. Evaluation skills are explicitly required by 61.8% of AI-First roles - the differentiator in a market where RAG and agents are baseline.

## Files covered

- [role/README.md](../../role/README.md) - section overview and key takeaways; the numbers above come from here
- [role/01-my-vision.md](../../role/01-my-vision.md) - Alexey Grigorev's personal definition: AI engineers integrate AI into the product via provider APIs, starting from a real user problem. Progressive complexity: plain LLM call, RAG (~5x harder), agents (~10x harder). Ten professional-practice steps beyond "just call the API" (prompt testing, eval dataset, A/B rollout, monitoring, logs, human annotators, model-update regression checks, prompt versioning, feedback loops). vs ML engineer: MLE owns model weights, AI engineer calls APIs - easiest transition. vs data scientist: no real modeling, most effort goes to prompt tuning; DS must add engineering, MLE must add evaluation
- [role/02-skills.md](../../role/02-skills.md) - the skills analysis over all 9,760 jobs: Python 71.6%, LLMs 60.5%, agents (any) 56.2%, RAG 40.1%, prompt engineering 34.8%, AWS 39.3% > Azure 29.7% > GCP 29.1%. Framework ecosystem travels together (LangChain 21.1%, LangGraph 14.4%, LlamaIndex 8.0%). Fine-tuning: 26.5% of AI-First postings mention it, but only 3.2% have it as primary responsibility and 86.0% don't mention it in responsibilities - a specialization, not core. 53.3% of AI-First roles need some ML (practical: fine-tuning 24.2%, embeddings 23.2%, PyTorch 18.8%). Research roles are 2.6% of the market. Title analysis: "AI Engineer" is the most reliable title (92% AI-First); "platform"/"data"/"enablement" titles are coin flips. MCP is the clearest steady riser: 9.9% (Feb) to 20.4% (Nov)
- [role/03-responsibilities.md](../../role/03-responsibilities.md) - 69,498 responsibilities from 9,760 jobs (Feb-Nov scrapes), categorized with AI assistance (methodology note inside). Building AI systems appears in 96.0% of jobs; evaluation and testing 71.3%, deploying/production 77.8%, monitoring 63.8%. Feb vs Nov shift: agents +10.1 points into the majority (55.8%), evaluation/testing +9.6 points (79.0%), research -22.1 points (down to 13.7%)
- [role/04-use-cases.md](../../role/04-use-cases.md) - 43,822 use cases from 9,760 jobs. Automating manual workflows (20.7% of mentions, 58.8% of jobs) and internal operational efficiency (22.5% of mentions, 57.5% of jobs) lead; agentic systems 17.7% (49.9% of jobs). Feb vs Nov: agentic systems +6.6 points into majority (50.7%), personalization -8.6, customer Q&A -13.8 - the center of gravity moves from consumer features to internal automation and agents
- [role/05-reality-vs-postings.md](../../role/05-reality-vs-postings.md) - qualitative counterweight from Reddit/X discussions: job descriptions describe ambition, not the day job ("80% prompt engineering + glue code + monitoring"). Three actual work types: orchestrators ~50%, evals specialists ~40%, efficiency wrappers ~10%. Titles are broken; combo roles (3 roles in 1) are a common complaint
- [role/06-fde.md](../../role/06-fde.md) - Forward Deployed Engineer analysis: 28 live FDE listings (Feb 2026) to 164 (Nov), 5.9x growth vs 3.4x for the whole market. 277 unique roles from 159 companies. The profile: customer-facing (86.3%), LLMs 73%, Python 68%, AI agents 58%, RAG 53%. Not entry level - only 2 of 277 titles target junior/entry-level
- [role/07-trends.md](../../role/07-trends.md) - month-over-month trends across all 10 scrapes: the integrator stack (RAG/agents/APIs) rose 80.0% to 91.7% within AI-First while the trainer stack (PyTorch/TensorFlow/fine-tuning/CUDA) fell 37.5% to 27.2% - the strongest directional signal in the dataset. Five role archetypes from k-means clustering: agent builder 29.9% (largest), RAG app builder 26.6%, DevOps/full-stack 16.9%, cloud/ML platform 14.1%, ML trainer/researcher 6.3%. Staff+ share declined (18.5% to 11.4%); junior stays pinned near 1%. The dedicated "AI infra engineer" still has not emerged (inference/serving fell to 13.5%)
- [role/08-trends-appendix.md](../../role/08-trends-appendix.md) - methodology and full tables: scrape sizes, cluster signatures with lift values, monthly mix tables, agent-framework churn (LangGraph 37.7% to 71.0% among framework users; Semantic Kernel tripled to 22.1%), extraction model/prompt fingerprinting (glm-5.2, fixed prompt_sha)

## Key claims

- The role is full-stack applied engineering: 97.4% applied vs research, 71.0% of AI-First roles combine GenAI with production/ops skills (role/README.md, role/02-skills.md)
- RAG + agents together cover most of the work: agents 56.2% of all jobs, RAG 40.1%, both listed together in 3,183 jobs (role/02-skills.md)
- Evaluation is the differentiator; RAG and agents are baseline (role/README.md; cross-confirmed by [interview](interview.md) and [home assignments](../concepts/take-home-assignments.md))
- Fine-tuning is overhyped relative to demand (role/02-skills.md) - the wiki carries this as a flagged tension with [interview](interview.md) prep sources that still teach LoRA/transformer implementation for frontier-lab coding rounds; both are true for different role segments
- The market data describes postings, not day jobs; candidate reports show a gap (role/05-reality-vs-postings.md)

## What is actionable

- Learn RAG and agents deeply first; add evaluation as the differentiator; treat fine-tuning as an optional specialization (role/02-skills.md bottom lines)
- Read "AI Platform Engineer" and "AI Data Engineer" postings carefully - the title predicts the stack badly (role/02-skills.md)
- Domain selection for projects should start from the use-case data: finance, healthcare, legal, cybersecurity ([portfolio](portfolio.md) uses exactly this)
