# Companies and Project Mapping

This is the canonical company page for the portfolio project system. It turns the project-selection method from [Choosing a Portfolio Project: The Definite Guide](https://aishippingblog.com/p/choosing-a-portfolio-project-the) into an evolving working map:

1. Start with a domain.
2. Track several companies in that domain.
3. Extract the problems they share from job descriptions, engineering blogs, and product documentation.
4. Link those shared problems back to projects on the [project ideas page](07-project-ideas.md).
5. Mark companies of interest and deepen only the mappings that matter.

The `Interest` column is the user-maintained shortlist. It starts empty and should be updated as target companies are named. The project relationships should be kept here and reflected in the mapping column on the project page.

## Current company roster

| ID | Company | Domain | Signals to investigate | Interest | Related project ideas |
|---|---|---|---|---|---|
| C01 | Capital One | Finance | GenAI platform services, financial document workflows | — | Finance document intelligence; serving, evaluation, and production AI |
| C02 | Wells Fargo | Finance | Financial data, electronic trading, analyst workflows | — | Finance document intelligence; RAG and structured extraction |
| C03 | BlackRock | Finance | AI for portfolio management, research, and high-performance systems | — | Finance document intelligence; inference efficiency and serving |
| C04 | Optum | Healthcare | Healthcare automation, search, and workflow integration | — | Healthcare and insurance workflows; safe RAG |
| C05 | GE HealthCare | Healthcare | Intelligent automation and clinical workflows | — | Healthcare and insurance workflows; multimodal extraction |
| C06 | Commure | Healthcare | AI integrations and healthcare operations | — | Healthcare and insurance workflows; agents and tool use |
| C07 | Thomson Reuters | Legal and regulatory | Legal CoCounsel, document review, and grounded assistance | — | Legal and regulatory review; RAG and evaluation |
| C08 | Wolters Kluwer | Legal and regulatory | Enterprise GenAI and regulated information workflows | — | Legal and regulatory review; structured extraction |
| C09 | Diligent | Legal and regulatory | Governance, compliance, and auditable workflows | — | Legal and regulatory review; safety and human review |
| C10 | CrowdStrike | Cybersecurity | AI-assisted security operations and alert workflows | — | Security operations; agents, tools, and observability |
| C11 | Arctic Wolf | Cybersecurity | SOC automation, triage, and incident response | — | Security operations; production FAQ/knowledge assistant |
| C12 | Cisco | Cybersecurity | GenAI software, networking, security, and developer platforms | — | Security operations; serving and agent workflows |
| C13 | JetBrains | Developer tools | IDE assistance, code understanding, and developer productivity | — | Developer tools; code retrieval and evaluation |
| C14 | Grafana Labs | Developer tools | AI for observability, telemetry, and engineering workflows | — | Serving, evaluation, and production AI; operational agents |
| C15 | Coinbase | Developer tools / finance | AI platform engineering and internal developer workflows | — | Developer tools; serving, evaluation, and production AI |
| C16 | Airbnb | Marketplace and e-commerce | Marketplace intelligence, ranking, and recommendations | — | Marketplace and e-commerce; multimodal and retrieval evaluation |
| C17 | eBay | Marketplace and e-commerce | AI platform, listings, catalog, and search | — | Marketplace and e-commerce; structured extraction and ranking |
| C18 | Toast | Marketplace and e-commerce | AI for commerce and operational workflows | — | Marketplace and e-commerce; agents and production delivery |

## How to update the mapping

When a company becomes interesting, update its `Interest` cell and add a short evidence note in `Signals to investigate`. Then update the corresponding row in the [project ideas mapping](07-project-ideas.md#project--company-mapping) with the company name and the shared problem that justifies the connection.

Use these values consistently:

- `Watch` — interesting, but not yet a priority
- `Target` — actively shaping projects and applications around it
- `Priority` — strongest current fit
- `Passed` — deliberately deprioritized

Do not map a project just because a company uses the same framework. Map it when the project demonstrates a problem, workflow, or engineering constraint that appears in the company’s evidence.
