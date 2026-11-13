# Forward Deployed Engineers: What Our Job Data Shows

Forward Deployed Engineer (FDE) is one of the fastest-growing titles in our AI engineering job data. We found 28 live FDE listings in February 2026 and 164 in November, a 5.9x increase across 10 monthly scrapes.

We're writing a longer article about this FDE trend for Substack. [Subscribe on Substack](https://aishippingblog.com/) if you want to read it when it comes out.

The rest of the AI engineering market grew too, but more slowly. Our full scrape grew 3.4x over the same period. FDE roles also increased from 2.0% to 3.4% of all listings.

We use only data collected by the [AI Engineering Field Guide](../job-market/README.md).

We analyze the job titles and structured descriptions from our scrapes to answer three questions:

- How quickly is the role growing?
- What do FDEs do?
- Which skills do employers want?

## FDE listings grew 5.9x

We count a listing as an FDE role when its title contains `FDE` or `forward deploy`.

Across our 10 scrapes, we found:

| Scrape date | All AI engineering listings | FDE listings | FDE share |
|---|---:|---:|---:|
| 2026-02-04 | 1,416 | 28 | 2.0% |
| 2026-02-27 | 2,057 | 41 | 2.0% |
| 2026-03-27 | 2,341 | 58 | 2.5% |
| 2026-04-22 | 2,473 | 65 | 2.6% |
| 2026-05-29 | 2,751 | 80 | 2.9% |
| 2026-06-25 | 3,024 | 108 | 3.6% |
| 2026-07-22 | 3,320 | 118 | 3.6% |
| 2026-08-25 | 3,946 | 140 | 3.5% |
| 2026-09-23 | 3,909 | 127 | 3.2% |
| 2026-11-06 | 4,825 | 164 | 3.4% |

The headline count grew by 486%, from 28 to 164. The full market grew by 241%, from 1,416 to 4,825.

FDE hiring grew about 1.7 times faster than the market in our dataset. The title is still a small part of the market, but it's no longer a rounding error.

These counts measure live listings in each scrape, and the same vacancy can appear on more than one date. We use the per-scrape figures for the trend and a separate deduplicated dataset to study the jobs.

## We found 277 unique FDE roles

After deduplicating by job ID, we found 277 FDE positions from 159 companies.

No single company dominates the sample:

- NewRocket has 12 unique listings
- Databricks has nine unique listings
- Thomson Reuters has seven
- Blue Machines AI, IFS, and Turing have six each
- Mistral AI, OneStream Software, Stord, and Tiger Analytics have four each

The other employers cover many sectors. We found the title at model companies and data platforms. We also found it at enterprise software vendors, consulting firms, logistics companies, and healthcare businesses. FDE isn't limited to frontier AI labs.

## Customer work plus production ownership

We extracted and classified the responsibilities in every matched posting.

The combination is more revealing than any individual responsibility. An FDE doesn't just demo a product or advise a customer. Employers expect the engineer to discover the problem, integrate the customer's systems, write production code, and stay responsible for whether the result works.

Our structured classifier marks 239 of the 277 roles, or 86.3%, as customer-facing. Only 4 roles, or 1.4%, are management positions. FDE is primarily an individual-contributor engineering role with unusually high customer exposure.

## The skill profile is applied, not research-heavy

LLMs and Python lead the postings, followed by agents, RAG, and cloud delivery skills:

- LLMs: 202 postings, or 73%
- Python: 187, or 68%
- AI agents: 162, or 58%
- RAG: 147, or 53%
- Prompt engineering: 122, or 44%
- AWS: 105, or 38%
- GCP: 95, or 34%
- Azure: 88, or 32%
- LangChain: 78, or 28%
- CI/CD: 71, or 26%
- Docker: 61, or 22%
- Kubernetes: 56, or 20%

Employers want LLM application skills, but they also expect engineers to work with APIs and customer data. Containers, cloud platforms, and deployment pipelines appear throughout the postings.

AWS appears in 38% of the sample, GCP in 34%, and Azure in 32%. FDEs can't assume that every customer uses the same stack. They need to deploy into the environment already in place.

## This is not an entry-level title

Most titles don't state a level, but the titles that do skew senior:

- 194 titles have no seniority marker
- 46 say Senior
- 14 say Principal
- 10 say Lead
- 8 say Staff
- 3 say Founding
- 2 say Junior or entry-level

The lack of a marker doesn't mean that 194 roles are junior. Their descriptions still ask for production ownership, customer communication, and broad technical judgment. Only 2 of the 277 titles target junior or entry-level candidates.

That makes sense given the work. An FDE has to make technical decisions in an unfamiliar customer environment, often before the requirements are clear. Companies are looking for engineers who can handle both the code and the conversation.

## FDE hiring is outgrowing the market

We draw three conclusions from our dataset:

1. FDE hiring is outgrowing the AI engineering market. Live listings grew 5.9x while the full crawl grew 3.4x.
2. Employers define the role through production delivery. Around 86% of postings are classified as customer-facing.
3. Employers ask for broad technical skills. Python, RAG, agents, cloud platforms, containers, and CI/CD all appear frequently.

Job postings describe employer demand, not the exact day-to-day experience of every FDE. Our title match can miss similar jobs advertised under other names. For example, we also see Applied AI Engineer, Solutions Engineer, and Deployment Engineer. Read our numbers as a lower bound for this style of work, not a complete count.

AI companies need engineers who can bridge the gap between a working demo and a system inside a customer's business. More employers are calling that engineer an FDE.

## Methodology

We analyzed the 10 scrape snapshots in [`job-market/_internal/data/scrapes`](../job-market/_internal/data/scrapes/) from February 4 through November 6, 2026.

For the trend, we matched titles containing `FDE` or `forward deploy`, without case sensitivity. We calculated the role profile from the 277 matching job IDs in the [deduplicated dataset](../job-market/_internal/data/all_jobs_dedup.csv) and their latest available records in [`job-market/data_structured`](../job-market/data_structured/).

The customer-facing and management figures come from the structured classifications produced by the Field Guide pipeline.
