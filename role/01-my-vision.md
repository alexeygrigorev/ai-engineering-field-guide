# My Vision of the AI Engineer Role

Based on [What Is an AI Engineer? Alexey Grigorev's Experience-Based Definition](https://aishippinglabs.com/blog/what-is-an-ai-engineer-alexey-grigorev-perspective).

This is my personal vision of the role. To see how it compares with what companies actually look for, I analyzed 895 job descriptions - the rest of this [role section](README.md) is based on that research.


## Core Responsibility

- Integrating AI into the product
- Working with LLM providers (OpenAI, Anthropic) through their APIs
- Working with product managers to identify real user problems AI can solve
- Not "AI is cool, let's use it" - starts from a real problem


## Beyond "Just Call the API"

Even for a simple use case like extracting attributes from a picture, professional AI engineering requires:

1. Prompt testing - tests with known inputs and expected outputs
2. Evaluation dataset - set of inputs to verify quality, gives a metric
3. Iterating on the prompt - change prompt, run eval set, verify no degradation
4. Rolling out to users - A/B test with a small portion first
5. Production monitoring - dashboard for error rates, failure cases
6. Collecting logs - inspect inputs, outputs, find misalignments
7. Human annotators - sample production data, verify quality, add problematic cases to eval set
8. Model updates - new model from provider? Run eval set to check for regressions
9. Prompt versioning - version control for prompts, experiment tracking (MLflow, Git)
10. Feedback from users - explicit (thumbs up/down) and implicit (user corrects output)

See the [Trova marketplace example](https://github.com/alexeygrigorev/simple-sell/) for a working implementation with tests and CI/CD.


## Progressive Complexity

- Simple case: user input -> prompt + LLM API -> response
- RAG (~5x harder): add data pipelines, search engine (vector/text), retrieval, infrastructure, reliability
- Agents (~10x harder): add tool calls, multiple LLM rounds, multi-step evaluation, trace instrumentation, tool rollout management


## How It Compares to Other Roles

### vs ML Engineer

- Very similar roles
- ML engineers own model weights, AI engineers use third-party models via APIs
- Replace a call to a locally hosted model with a call to OpenAI - the rest is the same
- Easiest transition path to AI engineering
- ML engineers need to add: evaluation skills

### vs Data Scientist

- Data scientists focus on model creation: translating requirements to ML, designing datasets, training
- AI engineers do both science and engineering, but no real modeling - model already exists
- Most effort goes to prompt tuning instead of model training
- AI teams don't necessarily need a separate data scientist
- Data scientists need to add: engineering skills (tests, CI/CD, deployment)

### What AI Engineers Don't Do

- Create models from scratch
- Build custom model architectures
- Heavy feature engineering

### What AI Engineers Focus On

- Engineering best practices for AI systems
- Prompt design and versioning
- Integration of AI into products
- Evaluation and monitoring


## In Bigger Organizations

- AI responsibilities often split between existing data scientists and ML engineers
- Data scientists: prompt tuning, validation framework
- ML engineers: engineering aspects, deployment
- Eventually a dedicated AI engineer might be hired
- LLMs are not the answer to all problems - traditional ML work continues
