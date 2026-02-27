# Webinar 1: A Day of an AI Engineer

- Date: February 16, 2026
- Host: [Alexey Grigorev](https://www.linkedin.com/in/agrigorev/)
- [Maven](https://maven.com/p/bf6ef3/a-day-of-ai-engineer)
- [AI Shipping Labs](https://aishippinglabs.com/blog/what-is-an-ai-engineer-alexey-grigorev-perspective)

## Description

The role of an AI Engineer is often misunderstood as purely research-focused. This session cuts through theory to show the practical reality of the role.

## Topics Covered

- Defining the AI Engineer from a personal perspective
- Core responsibilities: integrating AI into products
- Prompt engineering and evaluation datasets
- Production concerns: A/B testing, monitoring, and feedback loops
- Advanced systems: CI/CD, RAG, and agent complexity
- Essential skills for modern AI Engineers
- Q&A session

## Key Takeaways

1. Define the AI Engineer's Role - understanding core responsibilities bridging software engineering and ML research
2. Collaborate with Others - how AI Engineers work within teams
3. Processes - applying traditional processes like CRISP-DM to AI Engineering


## Q&A During the Webinar

### How can a data engineer transition to become an AI engineer?

For data engineers, it's primarily an engineering role, not a research or science role. Most "AI" work is just tweaking prompts and other engineering tasks. Data engineers already know tests, CI/CD, monitoring. The flavor might differ - data monitoring vs AI monitoring - but the tools are very similar.

The specific skills to learn: how to interact with LLM providers, how to tune prompts, how to evaluate models. After 3-4 months of learning AI-specific testing and evaluation, a data engineer should be ready to transition.

For RAG specifically, you need a search engine, which needs data, which needs an ingestion pipeline. This is what data engineers have been doing their entire career.

### How to narrow down what to focus on when preparing for interviews?

The most important parts to focus on:
1. Learn how to interact with LLM APIs
2. Understand how to create agents - LLMs with tools
3. Know about RAG - it's the foundation for many AI applications
4. Testing - how to test your agents, how to make sure they behave the way you want
5. Monitoring - AI-specific monitoring aspects
6. Evaluation - this is the most important part

For projects: pick a specific domain, like e-commerce or online classifieds. Go to their website, see what problems they solve, think about how to solve them, and create a small project showing you can do it.

### Why do AI automation specialists call themselves AI engineers?

Since the role is new and there is no strict definition, anyone can call themselves AI engineers and be partially correct. But are people who only do clicking in tools like N8N engineers? In my opinion, not really. Without engineering rigor, best practices, and tests - I wouldn't call myself an engineer.

### What backgrounds make good AI engineers?

Data scientists and ML engineers are excellent future AI engineers. For ML engineers, it's probably the easiest transition - you just replace a call to a locally hosted model with a call to OpenAI, and the rest is the same.

For any engineer: you know engineering best practices, you know testing. It's way easier to start with an engineering background and add AI on top of that, rather than start with a research background and add engineering on top.

Generalists make good AI engineers. If you know how to do many things, not necessarily at an expert level, but a bit of everything, you'll be a good AI engineer.

### Is traditional NLP/ML engineering now effectively legacy tech?

Probably yes. gpt-4o-mini is insanely cheap - I haven't managed to spend a dollar yet in my course. The effort calculation is obvious: how much effort do you need for traditional NLP models versus just sending your stuff to gpt-4o-mini?

There are still some cases where traditional NLP makes sense - simple cases like a spellchecker, or in search where you need sub-millisecond latency. But in general, the answer is clear.

### What about the future of engineering roles as AI gets smarter?

I don't think engineering is in danger. We still need to watch after AI, we still need to enforce best engineering practices. Without that, AI will create something that doesn't work and is dangerous.

Just today, I was working with Claude Code (Opus 4.6 - the best coding model we have). It tried to cover up that it didn't want to fix my test by deleting the old test and creating a new one. They are sometimes sneaky and lazy. It's like a very enthusiastic intern - they can work really well, but sometimes they're sloppy and we need to look after them.

With data science, maybe not so sure. A lot of data science work is now easy to automate. Data scientists who don't really do engineering - if they get laid off, it's not so easy for them to find a job.


## Q&A After the Webinar

### What "proof of work" makes a candidate stand out as a legitimate AI engineer rather than a hobbyist?

The difference between an engineer and a non-engineer: engineers know and follow best engineering practices. Tests are familiar to them. Monitoring is a must. They know how to collect feedback.

For a hobbyist - when I do something for myself, it's not a product. I don't have a good test suite, I don't have good monitoring. And that's fine for personal use. But if you're integrating an AI product at a company, that's when you need all of it.

### How uniform are AI Engineer job posting descriptions? What are the top 3 must-have skills?

Answered at [Webinar 2: Defining the AI Engineer Role](02-defining-the-role.md) with data-driven analysis from 1,500+ job descriptions.

### What should a recent or new grad focus on to break into this role?

Projects. You need to do as many projects as possible. Do projects in the areas of AI that interest you, and based on that, go to interviews.

Also important: networking, knowing people who are hiring, attending meetups. Right now many people know how to make a request to OpenAI, but not everyone knows about testing and evaluation. This is where new graduates can really differentiate themselves.

### Bayesian ML with hybrid LLM approach - what does the investment pipeline look like?

This is too complex for a generic answer and would require a one-on-one consultation to figure everything out.

### Data Engineering vs AI Engineering - which has more stable demand and is more remote-friendly?

For stability, data engineering has been growing steadily. Data engineers continue to be in demand - there's always a need to build pipelines. For remote-friendliness, I don't have the data - you could actually make a project out of this by scraping and analyzing job postings.

### AI Engineer title vs traditional Developer title - are they essentially the same?

The overlap is very large. An AI engineer is first and foremost an engineer - the AI part comes second. But there are some AI-specific things: prompt engineering, prompt versioning, model tuning, and tests that are somewhat specific to AI. Evaluation is also specific to AI - closer to what data scientists do.

Realistically, you can take a software engineer and make them a ready AI engineer in two to three months.

### With 20 years as a telecom engineer and no coding background - must I first become a software engineer?

Becoming a data scientist first - no, that won't help. But learning software engineering fundamentals - yes. Start with Python, learn testing. From there, move into AI engineering and focus on projects.

Start applying for jobs right away while learning. Initially they probably won't call you back, but you should still do it. By trying to become a better AI engineer, you also become a better software engineer.

Learn to use AI tools like Claude Code and GitHub Copilot - they really help with becoming a generalist and leveling up.

### What practical tools do you recommend for evaluation?

The best tool is the one you write yourself, based on your specific needs. But in general, Evidently is very good. Given current AI capabilities, it's very easy to build evaluation tools from scratch.

The approach: first do it in Excel, then run it in Python with pandas, then move it to CI/CD.

### If you were launching Trova - what would your engineering team look like?

First, work alone for several months and see if it's viable. When there are many customers, hire a software engineer generalist and give them a Claude Code Pro subscription. Next hire: a frontend engineer. I probably wouldn't hire AI engineers very soon, because most of the work is engineering work.

A startup doesn't need specialists - a startup needs generalists. Later, when the company grows to maybe 50-60 people and there's role specialization, then you'd need someone purely focused on AI.

### Do AI engineers need to do data monitoring, or is monitoring model outputs sufficient?

You can't limit yourself to just data monitoring or just output monitoring. You need to do everything comprehensively: all function calls, costs, the health of the microservice. If we're talking about RAG with a database, then naturally the data quality matters too.

### Are product engineers expected to also be AI engineers?

Product sense is a very useful skill for any engineer, especially seniors. Not just doing whatever, but understanding what impact your work has, what metrics you're optimizing. For example, you optimize latency not because it's a cool engineering challenge, but because you understand how it leads to increased revenue.

### What is the most critical non-technical skill for leading AI systems in production?

Stakeholder management, product sense, business understanding. Being able to listen to people who tell you what's important, understand why, and translate requirements into code. For governance specifically: understanding the domain to properly assess what risks exist and how to mitigate them.

### How can frontend engineers transition into AI engineering?

Frontend engineers would need to build up their backend skills. For technologies: instead of Python, TypeScript is perfectly fine - it's used a lot in AI engineering right now.

From frontend, transition to full stack. Your advantage: you can close the entire stack end-to-end, from backend to product integration. Start with an AI assistant like Cursor or Claude Code, try doing backend with its help, then start learning AI.

### Is the Data Scientist role outdated?

Not completely outdated, but finding work has become much harder for some data scientists. A lot of data science work is now easy to automate with AI assistants. An AI engineer with a Claude Code subscription can figure out data science tasks very quickly.

Full-stack data scientists and generalists have never had problems and likely never will. But data scientists who can only do analytics and train models without going beyond notebooks - the trend is that it's been hard for them for quite a while.

There are still many tasks involving traditional ML. In large companies, tuning models with specific constraints still needs traditional approaches. As for the AI engineering trend - if you have engineering understanding, you'll always find something to do.
