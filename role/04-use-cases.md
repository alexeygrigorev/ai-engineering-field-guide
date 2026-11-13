# AI Use Cases Analysis

Based on 43,822 extracted use cases from 9,760 job descriptions across 10 monthly scrapes (Feb-Nov 2026).

Methodology note: I collected all use cases into a single file and used AI (Claude) to analyze and categorize them. This is not a quantitative analysis like the [skills analysis](02-skills.md) (see the [analysis notebook](../job-market/analysis.ipynb) for that) - it's based on the questions I asked and the patterns Claude identified in the data. The category counts come from keyword matching, so a single use case can count toward more than one category, and the percentages below are mentions divided by the 43,822 total. It may be less precise than a strict statistical analysis, but I believe it's still representative of what's happening in the market.

## Summary

The use cases reveal what companies are actually building with AI today. This is the real-world application landscape that AI Engineers work on daily.

Total use cases extracted: 43,822

- AI-First roles: 31,537 use cases (72.0%)
- AI-Support roles: 10,210 use cases (23.3%)
- ML-First and unclassified roles: 2,075 use cases (4.7%)


## Feb vs Nov: How the Market Shifted

Comparing the first scrape (Feb 2026, 895 jobs) with the latest (Nov 2026, 1,709 jobs) shows what companies are shifting toward.

Agentic systems, retrieval, and document processing grew, while customer-facing Q&A and personalization declined.

Biggest movers (change is in percentage points of jobs):

| Use case | Feb | Nov | Change |
|----------|-----|-----|--------|
| Agentic Systems | 44.1% | 50.7% | +6.6 |
| Finding Information (RAG/Search) | 28.3% | 31.7% | +3.4 |
| Document Processing | 13.3% | 16.0% | +2.7 |
| Internal Operational Efficiency | 50.7% | 51.4% | +0.6 |
| Automating Manual Workflows | 52.7% | 52.1% | -0.6 |
| Answering Customer Questions | 44.7% | 30.9% | -13.8 |
| Personalizing Experiences | 14.9% | 6.3% | -8.6 |
| Deploying AI to Production | 38.5% | 31.7% | -6.8 |
| Data Analysis and Insights | 19.9% | 13.8% | -6.1 |
| Creating Content at Scale | 33.5% | 27.6% | -6.0 |

What this tells me:

- Agentic systems became a majority use case (50.7% in November, up +6.6 points), matching the rise of agents in responsibilities.
- Automation (52.1%) and internal enterprise operations (51.4%) remain the steady core of what companies build.
- Customer-facing Q&A (-13.8 points) and personalization (-8.6 points) fell the most. The center of gravity continues to move from consumer-facing features toward internal automation, agentic workflows, and enterprise operations.


## Problems AI Solves Today

Organized by the user problem, not the technology. Ordered by frequency.


### Automating Manual Workflows

9,056 mentions (20.7%); appears in 58.8% of jobs.

Problem: Employees spend time on repetitive tasks that could be automated - data entry, document processing, workflow coordination, monitoring and alerting.

AI Solution: Agents that can execute multi-step workflows autonomously.

Concrete examples:

- Automate construction permitting and licensing workflows
- CI/CD pipeline automation and lifecycle management
- AI-assisted automation for airline cargo operational workflows
- Operations and compliance copilots to streamline internal workflows and ensure regulatory adherence
- Enterprise AI agent deployment for business automation
- Automate business workflows and reduce manual work across Salesforce platforms


### Internal Operational Efficiency

9,866 mentions (22.5%); appears in 57.5% of jobs.

Problem: Enterprises have complex operations - risk management, compliance, regulatory reporting, revenue operations, fraud detection. These require specialized AI solutions.

AI Solution: Enterprise-grade AI systems for internal operations.

Concrete examples:

- AI-powered revenue operations and lead management
- Fraud detection and prevention through advanced ML and computer vision
- Enterprise-scale AI agents with tool-calling capabilities
- Automated reasoning and evaluation of insurance claims
- Early signal detection of emerging risks, events, and threats before they unfold
- Supporting secure, compliant AI infrastructure that meets enterprise regulatory requirements


### Agentic Systems

7,749 mentions (17.7%); appears in 49.9% of jobs.

Problem: Companies want AI that can take coordinated action across multiple steps, tools, and roles rather than answering a single prompt.

AI Solution: Multi-agent architectures that plan, call tools, and hand off work between specialized agents.

Concrete examples:

- Agentic AI architectures for workflow orchestration
- Sales process automation through agentic workflows
- Reasoning agents for risk assessment, safety analysis, and decision support
- Demand package generation: coordinating researcher, drafter, and validator agents to gather case law and write petitions
- Enterprise conversational agents and agentic systems to reduce operational friction
- Governed and observable AI agent platforms


### Deploying AI to Production Reliably

4,993 mentions (11.4%); appears in 37.5% of jobs.

Problem: AI models work in notebooks but fail in production. Latency, scalability, reliability, and cost are major challenges.

AI Solution: Production ML infrastructure - inference serving, model deployment, monitoring.

Concrete examples:

- Production AI/ML model deployment and serving at enterprise scale
- High-throughput inference services for manufacturing systems
- Platform services enabling multiple teams to deploy GenAI applications
- Enterprise-scale AI deployments in secure and regulated environments
- Low-latency production inference systems for AI applications
- Automated data pipeline orchestration for AI/ML workflows


### Making Decisions from Data

3,300 mentions (13.5%); appears in 43.0% of jobs.

Problem: Companies have data but cannot extract insights or make data-driven decisions quickly enough.

AI Solution: AI-powered data analysis and insights.

Concrete examples:

- LLM-powered tools and assistants that help teams surface insights and work more efficiently
- AI-driven financial data transformation and insights
- Healthcare analytics and predictive modeling for improved health outcomes
- High-performance marketing analytics with sub-second query performance
- Ticket analytics for service operations
- RAG-powered data processing and analysis


### Finding Information in Company Data

3,089 mentions (12.6%); appears in 43.8% of jobs.

Problem: Companies have massive amounts of documents, knowledge bases, and data. Employees cannot find what they need. Keyword search is not enough.

AI Solution: RAG and Semantic Search - AI that understands meaning and retrieves relevant information from proprietary data.

Concrete examples:

- RAG-based knowledge retrieval for financial data and instruments
- Insurance pricing intelligence by transforming millions of messy regulatory documents into queryable, trustworthy knowledge
- Semantic search and retrieval over enterprise unstructured data
- Retrieval-augmented generation for contract insights
- RAG and retrieval-augmented generation for government knowledge bases
- Medical literature search over millions of processed articles


### Answering Customer Questions at Scale

2,754 mentions (11.2%); appears in 36.4% of jobs.

Problem: Companies have too many customer inquiries for human support teams. Customers expect instant, 24/7, personalized responses.

AI Solution: Customer-facing AI that can understand questions, retrieve relevant information, and provide accurate answers.

Concrete examples:

- Chatbot experience enhancement for consumer operations
- Omnichannel user experience for banking customers
- HR service delivery automation through conversational AI and self-service
- Conversational AI systems for patient interactions and follow-up care
- LLM-powered customer support with access to company knowledge
- Process customer inquiries without human intervention


### Creating Content at Scale

2,281 mentions (9.3%); appears in 33.4% of jobs.

Problem: Marketing, education, and content teams need to produce large amounts of text, images, audio, and video.

AI Solution: Generative AI for content creation.

Concrete examples:

- Automated content and asset generation for automotive brand marketing campaigns
- Text-to-speech conversion for PDFs, books, docs, and web content
- Creative content generation using generative AI to produce ad copy and optimize campaigns
- Content generation at scale for educational materials
- Scalable generative AI platform for enterprise productivity


### Ensuring AI Quality and Safety

1,298 mentions (5.3%); appears in 20.0% of jobs.

Problem: AI systems can hallucinate, produce unsafe content, or behave unpredictably. Companies need to ensure quality and safety.

AI Solution: AI evaluation, testing, and safety systems.

Concrete examples:

- AI governance, trust validation, and compliance monitoring
- Hallucination detection and mitigation in high-trust production AI systems
- Testing AI agents with AI agents to validate conversational AI interactions
- AI system safety evaluations and red teaming
- Enforcing data privacy and security guardrails for AI agents and models


### Personalizing User Experiences

717 mentions (2.9%); appears in 12.0% of jobs.

Problem: Users want relevant recommendations, not generic content. One-size-fits-all doesn't work.

AI Solution: Recommendation systems and personalization engines.

Concrete examples:

- AI-powered personalization across consumer engagement platforms
- Content recommendations for personalized consumer experiences
- Real-time hyper-personalized email content generation based on user interests and behaviors
- E-commerce recommendations to help merchants compete effectively
- Context-aware AI-powered recommendations


### Helping Developers Write Code

575 mentions (2.3%); appears in 9.5% of jobs.

Problem: Developer productivity is limited by repetitive coding tasks, debugging, and learning new APIs.

AI Solution: AI coding assistants and developer tools.

Concrete examples:

- Coding automation and SDLC acceleration through AI-assisted development tools
- Developer productivity enhancement through AI coding agent integration
- Provide instant code generation and editing capabilities directly in the browser
- AI-enabled developer productivity tools and automation
- Internal developer platforms integrating AI capabilities


### Handling Specialized Domain Knowledge

250 mentions (1.0%); appears in 5.0% of jobs.

Problem: Generic models don't understand industry-specific language, regulations, or knowledge.

AI Solution: Fine-tuned models for specialized domains.

Concrete examples:

- Fine-tuned models for domain-specific applications
- Industry-specific LLM fine-tuning and deployment
- Domain-specific multimodal AI for fintech and digital finance use cases
- Generating reward signals from expert code reviews to fine-tune model behavior
- Domain-specific model fine-tuning for specialized tasks


## Domains Served

Based on the use cases, AI is being applied across virtually all industries. Counts below are use cases that mention each domain.

### Finance (2,321 mentions, 9.5%)

- Fraud detection
- Risk assessment and underwriting
- Algorithmic trading and alpha generation
- Claims processing automation
- Revenue operations and lead management

### Healthcare (1,783 mentions, 7.3%)

- Clinical decision support for physicians
- Medical literature search over millions of articles
- AI-powered diagnostics assistance
- Medical documentation and note generation
- Patient engagement and follow-up care

### Legal / Regulatory (1,094 mentions, 4.5%)

- Contract review and analysis
- Legal document processing
- Compliance monitoring
- Legal research assistance
- Regulatory document intelligence

### Cybersecurity (1,028 mentions, 4.2%)

- Threat detection and analysis
- Alert summarization for security defenders
- Malware classification
- Automated security reasoning
- Attack prevention

### Education (571 mentions, 2.3%)

- Personalized learning recommendations
- Automated grading and feedback
- Educational content generation
- Student engagement systems
- Course recommendation

### Manufacturing / Industrial (533 mentions, 2.2%)

- Robotics and automation
- Supply chain optimization
- Quality control and defect detection
- Predictive maintenance
- Process automation

### Retail / E-commerce (226 mentions, 0.9%)

- Product recommendations
- Semantic search for products
- Inventory optimization
- Customer experience personalization
- Supply chain optimization


## Key Insights

### 1. Automation is the Primary Use Case

The most common problem AI solves is automating manual workflows - 5,848 mentions (23.9%), appearing in 69.0% of jobs. This is not glamorous; it's about reducing repetitive work, coordinating processes, and handling scale.

### 2. Enterprise Operations Are Nearly as Large

Internal operational efficiency is the second biggest category at 21.3% - risk, compliance, revenue operations, fraud, and claims. Enterprise AI is a dominant theme, not a niche.

### 3. Agents Went Mainstream

Agentic systems account for 15.5% of use cases and appear in 49.4% of jobs. Roughly half of all postings now describe multi-agent, tool-using systems - a clear shift from the earlier "single LLM call" pattern.

### 4. Knowledge Access is Universal

Every domain has the same problem: too much information, cannot find what's needed. RAG and semantic search solve this across healthcare (medical literature), finance (regulations), legal (contracts), and general enterprise (internal docs).

### 5. Customer Support is a Major Driver

Customer-facing solutions are 11.2% of use cases because they directly impact revenue and customer satisfaction. The ROI is clear: reduce support costs while improving response times.

### 6. Production is Hard

13.7% of use cases focus on deployment infrastructure. This reflects the real challenge of getting AI models from notebooks to production reliably.

### 7. Domain Specialization is Niche but High-Value

Only 1.0% of use cases involve fine-tuned models for specific domains (insurance, legal, cybersecurity, fintech). Few in number, but they represent high-value applications where generic models are insufficient.


## Most Common Words in Use Cases

- data: 2,866 mentions
- systems: 2,514 mentions
- automation: 2,499 mentions
- enterprise: 2,283 mentions
- workflows: 1,957 mentions
- ai-powered: 1,548 mentions
- applications: 1,518 mentions
- business: 1,393 mentions
- agents: 1,093 mentions
- solutions: 1,090 mentions
- customer: 1,051 mentions
- agentic: 1,042 mentions
- platform: 1,017 mentions
- operations: 956 mentions
- intelligent: 898 mentions
- financial: 885 mentions

The language emphasizes practical value: systems, automation, workflows, business outcomes - not just technology.
