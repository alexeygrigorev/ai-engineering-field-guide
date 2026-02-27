# AI Engineering Field Guide

Data-driven field guide to AI engineering roles, skills, and interviews.

My vision for this repo is to become **the** go-to resource for AI engineering. Like [data-science-interviews](https://github.com/alexeygrigorev/data-science-interviews) but broader:

- role analysis
- job market data
- interview questions
- learning paths
- and more

It's a work in progress, and I'm actively adding more content. Your input is very welcome - feedback and contributions help shape what goes in here.

**Star** this repo to keep an eye on updates. To get notified about new content, subscribe to my newsletter: [Alexey on Data](https://alexeyondata.substack.com/).


## The AI Engineer Role

- [My vision of the role](role/01-my-vision.md) - how I see AI engineering, comparison with DS/ML/DE roles, CRISP-DM for AI

Analysis of what AI engineers actually do, based on 895 job descriptions:

- [Skills analysis](role/02-skills.md) - top skills, job types, cloud platforms, frameworks
- [Responsibilities](role/03-responsibilities.md) - 5,694 extracted responsibilities across 895 jobs
- [Use cases](role/04-use-cases.md) - 4,525 real use cases showing what companies build with AI
- [Reality vs. job postings](role/05-reality-vs-postings.md) - what candidates experience vs. what's advertised

Key findings

- 69.4% of "AI Engineer" roles are AI-First (RAG, agents, LLMs), not traditional ML
- 93.1% need skills beyond just GenAI - this is a full-stack role
- RAG is the #1 pattern (35.9% of all jobs)
- Python (82.5%), AWS (40.1%), Docker (31.0%) are the top skills
- 64.3% of roles still require some ML knowledge
- Only 1.4% of roles expect pure GenAI work


## Learning Paths

- [General learning path](learning-paths/) - what to learn and in what order
- [From Data Engineer](learning-paths/from-data-engineer.md) - smoothest transition, 3-4 months
- [From Data Scientist](learning-paths/from-data-scientist.md) - evaluation is your superpower, add engineering
- [From ML Engineer](learning-paths/from-ml-engineer.md) - easiest transition, replace model call with API call
- [From Backend Engineer](learning-paths/from-backend-engineer.md) - 2-3 months, add AI on top of engineering
- [From Frontend Engineer](learning-paths/from-frontend-engineer.md) - backend first, then AI, unique full-stack advantage


## Portfolio

- [Project ideas](portfolio/) - real project examples that demonstrate AI engineering skills


## Job Market Data

895 job descriptions scraped from builtin.com covering LA, NY, London, Amsterdam, and Berlin.

- [Structured job descriptions](job-market/data_structured/) - YAML files with title, company, skills, compensation, and full descriptions
- [Raw extracted postings](job-market/data_raw/) - original extracted data

## Interview Preparation

Based on analysis of 1,765 job descriptions, 51 companies with disclosed interview processes.

- [Interview process analysis](interview/interview-process.md) - common patterns, step counts, time estimates, AI use in hiring, key takeaways
- [Home assignments](interview/home-assignments.md) - 17 take-home assignments and 5 paid work trials analyzed in detail
- [Interview questions](interview/interview-questions.md) - technical and behavioral questions (work in progress)
- [Company-by-company data](interview/data/) - individual interview process descriptions for 51 companies, linked to source job postings

## Coming Soon

- Salary analysis and compensation data
- Community-contributed interview experiences


## Event Series

This field guide is part of a 4-part event series on AI engineering careers:

1. [What Is an AI Engineer?](https://aishippinglabs.com/blog/what-is-an-ai-engineer-alexey-grigorev-perspective) - defining the role based on real experience (recording available)
2. **The AI Engineer Role** - this field guide (you are here)
3. [AI Engineering: The Interview Process](https://maven.com/p/69550a/ai-engineering-the-interview-process) - preparing for AI technical interviews with real hiring trends and live coding challenges (March 3, 2026)
4. [AI Engineering: Take-Home Assignments](https://maven.com/p/250595/ai-engineering-take-home-assignments) - analyzing real AI hiring assignments and building a production-ready solution (March 9, 2026)

Have questions? [Submit them here](https://app.sli.do/event/vJEZ6h5zbFRAzPfrANZxZd) - all questions will be covered during the events or afterwards.


## Learn AI Engineering

If you want to learn the core skills needed for being an AI engineer, check out my course [AI Engineering Buildcamp: From RAG to Agents](https://maven.com/alexey-grigorev/from-rag-to-agents) - a 6-week intensive on building production-ready AI applications. Use code **EARLYBIRD** for 30% off.
