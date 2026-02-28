# Webinar 2: Defining the AI Engineer Role

- Date: February 24, 2026
- Host: [Alexey Grigorev](https://www.linkedin.com/in/agrigorev/)
- [Maven](https://maven.com/p/f0cada/defining-the-ai-engineer-role)
- [Recording on YouTube](https://www.youtube.com/watch?v=7NijlAdqk9U)
- [Slides](slides/ai-engineer-role.pdf)

## Description

AI job titles are inconsistent. This webinar examines 1,500+ current job descriptions and industry research to clarify what companies actually hire for, helping professionals transition from simply using AI tools to building professional-grade AI products.

## Topics Covered

- Data analysis: scraping and processing job descriptions using LLMs to identify patterns
- Role classification: distinguishing between research-focused and product-oriented AI positions
- Technical skills: RAG and full-stack engineering fundamentals
- ML frameworks: GenAI frameworks and machine learning knowledge requirements
- Production focus: fine-tuning versus productionization and evaluation methodologies
- Career strategy: actionable approaches for securing AI engineering positions
- Industry trends: interview patterns and evolving skill expectations

## Key Findings

### Dataset

The analysis is based on approximately 895 job descriptions scraped from the Built In website in January 2026. Jobs were collected from five cities: Berlin, Amsterdam, London, Los Angeles, and New York. After removing duplicates and filtering out unrelated roles, each description was processed using an LLM to extract structured information: company details, position type (AI-first, AI-support, or ML), responsibilities, use cases, and skills categorized by type.

All data, scraping scripts, and analysis notebooks are in the [AI Engineering Field Guide repository](https://github.com/alexeygrigorev/ai-engineering-field-guide).

### Skills

70% of the positions were AI-first roles. The remaining 30% were AI-support roles or traditional ML positions relabeled as "AI engineer."

RAG is the number one skill pattern, mentioned in about 35% of AI-first positions. 93% of AI engineer roles require skills beyond just GenAI.

Top skills from job descriptions:
- Python is the dominant language (82.5%), TypeScript in second place (23.4%)
- Cloud platforms: AWS is the leader, but any cloud works
- Docker, CI/CD, Kubernetes are commonly expected
- LangChain is the most popular framework mentioned, followed by LlamaIndex and LangGraph
- 64% of roles require some ML knowledge - likely because AI teams evolved from existing ML teams
- Fine-tuning is a niche skill (only ~25 out of 895 jobs mention it)
- Evaluation is commonly required across positions

The key takeaway: an AI engineer is first an engineer, then a specialist. Just knowing Python and calling the OpenAI API is not enough - you also need Docker, CI/CD, testing, monitoring, and cloud skills.

### Responsibilities

Very common: building AI systems, productionizing (testing, QA, monitoring), evaluation and quality, working with provider APIs (OpenAI, Anthropic, Google), RAG implementation, context engineering.

Common: data processing, collaboration, infrastructure and platform work, building agents.

Less common: frontend work, self-hosting models. Most companies use external providers rather than hosting LLMs themselves.

## Q&A During the Webinar

### Data sample size and limitations

About 895 job descriptions. For these specific cities (LA, NY, Amsterdam, London, Berlin) and time period (January 2026), the sample is sufficient. Extrapolating to other regions like Asia or Africa would require more data, but New York sets the trends and Europe follows, so the patterns should generalize. The code is available in the repository for anyone who wants to reproduce the analysis with more cities.

### AI engineer as a software engineer who productionizes AI

Yes, this is an accurate description. An AI engineer is a software engineer with specialization in AI, just like data engineers specialize in data and ML engineers in machine learning. They all need tests, CI/CD, Docker, deployment. A software engineer can learn the core AI skills (RAG, agents, evaluation) in about 3-4 months and become an AI engineer. For someone without an engineering background, it requires more effort because they also need to learn the general engineering skills.

### Context layer for AI tools

It depends on what "context layer" means. It could be: how you build prompts, how you inject things into prompts, selecting which tools or MCP tools to include, using RAG, or maintaining agent memory (files or graph databases). All of this falls within the domain of AI engineering.

### Vertex AI experience value

Vertex AI is Google's ML platform, similar to SageMaker on AWS. For AI engineering specifically, it is not super important. General cloud skills are more valuable - knowing how to host your agent as a microservice, which tools to use for deployment. In most cases you use an LLM provider (OpenAI, Anthropic, or through cloud services like Azure or Bedrock), so you do not need to think about serving the LLM yourself. You focus on your own services.

### Data scientist with Docker/Kubernetes transitioning to AI engineering

Data scientists are well equipped for it. The mindset of tuning knobs, evaluating results, and making data-driven decisions is exactly what AI engineering needs. Instead of training models yourself, you specify prompts and call the API, but the evaluation mindset is the same. Data scientists can start using AI at their current workplace without switching titles. Take on more engineering tasks gradually.

### LeetCode interviews

This is changing but not everywhere. Some companies now allow coding agents and focus on walking through the solution. But many companies still use classical whiteboard interviews. The reasoning: "what if the internet is down, can you still program?" Whether LeetCode is a good way to check that is debatable, but companies still do it and it is not going away anytime soon.

### Differentiating AI engineer and ML engineer

When I hear "AI engineer," I mean someone working with GenAI technologies like LLMs, not necessarily traditional machine learning. Some companies jumped on the hype train and renamed their ML engineers to AI engineers, but the role is still traditional ML. Sometimes the opposite happens too - a data science position has GenAI skills and responsibilities. The boundaries are blurry and some companies use the titles interchangeably.

### Are software engineering jobs disappearing?

No. From a study analyzing 180 million job postings across years, ML engineering is actually the number one growing job. Just today I was working with Claude Code (Opus 4.6) - it decided not to do something because "it is too complex," and sometimes it removes failing tests and reports all tests pass. They are like enthusiastic interns - capable but sometimes sloppy. You need engineers to set up processes so agents cannot break production: tests, hooks, code reviews, CI/CD, monitoring. Engineers are safe.

Current AI tool pricing is heavily subsidized. If API costs become 10-100x higher, writing some things by hand will make more sense again.

### Market for data engineers in RAG and vector databases

Yes. RAG on the surface is just three lines of code: search, build prompt, call LLM. The complicated part is the search. You need a search index, and data needs to get there reliably. This is nothing but a data engineering job - moving data from source to destination. Data engineers have been doing this their entire career. Even with agentic RAG and agentic search, the database is not going anywhere. Agents need data, and that data needs to be ingested and maintained.

### Portfolio skills for masters students

Focus on what universities typically do not teach: testing, evaluation, monitoring - the core AI engineering skills. Also learn the full stack around AI: infrastructure, vector databases, cloud deployment.

The way to add skills is through projects. Pick a project, implement it end to end, and each time focus on one area. For example: one project focused on building an agent that analyzes a GitHub repo, another on deployment and CI/CD, another on Kafka ingestion for RAG. Build 5-6 small focused projects rather than one large project. Spend 1-2 weeks on each.

### Course content for the next cohort

The [course on Maven](https://maven.com/alexey-grigorev/from-rag-to-agents) focuses on core AI engineering skills: RAG, agents, testing, evaluation, monitoring. Infrastructure like Docker and CI/CD is outside scope because the ideal profile is a software engineer who already knows these things. LangChain was added to the course despite personal preference for Pydantic AI, because there is demand. Making one single agent work well with a few well-picked tools is more important than multi-agent systems.

### Coding tools integration in industry

Very few engineers do not use any coding agents. It is pretty well integrated across data scientists, ML engineers, AI engineers, and software engineers. It is a general tool for software engineering - frontend, backend, infrastructure.

### Evaluating AI generated work

Create a ground truth dataset with input and expected output. Run your agent on it, compare actual output with expected output, and compute a relevance score across all items. This is the standard evaluation approach.

### Securing a job at an AI startup

Build projects, yes. Cold outreach emails, probably not the most effective strategy.

Better approach: pick a domain by looking at companies hiring in your area. Read their engineering blogs to understand what problems they solve. Build 2-3 projects in that domain using relevant datasets. At interviews, you have relevant things to discuss.

Instead of cold outreach, practice "learning in public" - share everything you learn on social media. People who work in the same domain will notice you. When you contact them later, it will not be cold outreach because they already saw your content. Also attend meetups and talk to people. If you are shy, speak at meetups instead - people come to you with questions.

## Q&A After the Webinar

### Programming languages in AI engineering

From the analysis of 895 job descriptions:

- Python - 738 jobs (82.5%)
- TypeScript - 209 jobs (23.4%)
- Java - 133 jobs (14.9%)
- Go - 101 jobs (11.3%)
- SQL - 88 jobs (9.8%)

Python is the dominant language. TypeScript is in second place, which aligns with what we see in the field. Java and Go also appear frequently.

### PhD in ML to AI engineering

For a researcher, the core AI skills are easy. Sending requests to OpenAI, doing prompt tuning, running experiments with different prompts - all of that is straightforward for someone with a research background.

The hard part for researchers is the engineering side: tests, monitoring, evaluation. These are the areas that need the most attention.

For core AI engineering skills beyond basic API calls:
- Testing your agents - approaching it the same way you test regular code with pytest and similar tools
- Monitoring - setting up proper monitoring for your AI applications
- Evaluation - this should actually be easier for researchers since they already think in terms of metrics

For infrastructure skills:
- Docker - important to learn
- CI/CD - important to learn
- Cloud basics - knowing how to deploy something simple
- Kubernetes - can skip this, not essential

There are tools like Claude Code that make all of this much easier. The key approach: use AI assistants, but try to thoroughly understand what they recommend rather than just blindly executing.

### AI application security roles

I did not encounter separate AI application security roles in the data. But it would be interesting to investigate. All the scraping scripts are in the repository - if someone wants to repeat the analysis specifically for security roles, it would not be too hard.

### Data engineers moving to AI engineering

For data engineers, the core AI engineering skills are exactly what you should focus on beyond RAG: testing, monitoring, and evaluation. The transition is relatively fast - maybe 3-4 months and you are ready. You already have the engineering skills.

When job searching: "I am a data engineer, I know engineering, I can build data pipelines, and because I am a great data engineer, I have an advantage over other AI engineers who do not have this skill."

### Are data scientist jobs safe?

Historically, to productionize a model, for every 1-2 data scientists you needed several engineers. With AI, this became even easier - any engineer who can run code can train an XGBoost model.

What makes data scientists valuable? ML and product management skills. They are also very good with experiments and evaluation. If data scientists want to move into AI engineering, they should focus on the engineering side and showcase their strong evaluation and metrics skills.

For example, search is very important and data scientists typically know how to evaluate ranking models. Engineers may know less about this. That is the kind of edge data scientists have.

### TDD and testing in job descriptions

TDD is not explicitly mentioned in job descriptions, but it is an important practice. It might fall under the evaluation cluster, because sometimes when we do evaluation, we can split our dataset into parts - one part with things that must pass. This is essentially a test that just looks and is configured a bit differently.

The reason TDD might not appear explicitly: look at ML engineer or software engineer job descriptions - do they often mention tests? Not really. But all ML engineers and software engineers write tests. It is simply assumed as a best engineering practice.

I ran additional analysis the job descriptions to verify this:

- 73% mention any quality practice (testing, CI/CD, monitoring, evaluation, code review)
- 52% mention CI/CD, monitoring, or evaluation specifically
- 26% mention testing explicitly ("testing", unit/integration/e2e tests, automated tests, QA)
- 0.4% mention TDD by name (5 jobs out of 1,397)

Companies care about quality outcomes (CI/CD, monitoring, evaluation), not specific methodologies. TDD, agile, SOLID - all could be expected from any engineer but almost never spelled out in job descriptions.

### Software engineering experience vs end-to-end AI projects

Having an end-to-end AI project is always useful. Fine-tuning LLMs is not a core skill, it is more of a niche skill. If we are talking about what is generally more valuable based on the data, regular software engineering skills are more useful than niche LLM skills.

### Do recruiters check your GitHub?

Recruiters themselves most likely do not check. Who will actually look is the hiring manager.

When I was hiring people, I did not have time to look in detail. Maybe 5-10 minutes before the interview I would open the resume, look at the GitHub link, and see what is there in general. I would not have time to read details. A project would have to really interest me for me to want to look at the code.

That is why I invest a lot of attention in the README - it is the most important part of the project. I look at the README to see what is described there, and that is usually it.

Organization plays a very important role. Links to code, to important implementations right in the README can be very helpful.

### What do hiring managers focus on?

As a hiring manager, what I want to see:
1. The project solves a real problem - what it does, why it exists
2. A clear description so I can open the README and immediately understand what is going on
3. Signs that the project is close to production: tests, evaluation, CI/CD, deployment

The more of these checkboxes I see, the better. Tests add a plus, CI/CD adds a plus, good code adds a plus, images, demos, videos add a plus.

Does this mean every personal project must have evaluation or tests? Of course not. Pet projects are pet projects. But if a project solves a real problem and has multiple iterations invested in it, I will be interested in discussing it even without tests.

### README quality

This is probably the most important part of your project. You need to make sure it is not too big and not too small, that it has all the important information but not too much.

For me the most important thing: the README should describe the project clearly, the project should solve a specific problem, and there should be a reasonable description so I can open the project and immediately understand what is happening. Everything else adds bonus points: having tests described, having CI/CD, having good code, having images, demos, videos.

### Two audiences for your README

Write your README for two different audiences:

1. The first audience is a peer reviewer (or another student) who has time to check everything and verify all criteria are satisfied. This motivates you to write good code, clearly and without cutting corners.

2. The second audience is a hiring manager. They have almost no time at all, and you need to convey the maximum amount of information in the shortest time.

You can also imagine this is your take-home assignment and the hiring manager will read it. Try to guess what their internal checklist looks like and try to check all the boxes.

### How deeply do interviewers inspect code?

If we are talking about a hiring manager - there is no time to check in detail. I open it, look for 1-2 minutes, and that is probably it. In rare cases I might look at the prompts, maybe look at the tools, check if tests exist at all. I will not read the tests - I just open them, look if they are there.

But for take-home assignments, people will read more carefully. Some hiring managers actually run the code. For take-home assignments, it is better to follow engineering best practices: write tests, have code coverage ideally.

### Commit history and contribution consistency

I have never in my life looked at commit history. And I do not think anyone will look at this. When I look at a project, I look at the project in its current state.

### End-to-end projects vs experimental notebooks

The answer is obvious. No additional comments needed.

### Tutorial-based vs original projects

If someone tells me in an interview "this was a course, I just copied from there" - I immediately lose interest. If someone tells me they had an idea or a problem and they solved it using some tool - that is a huge plus.

Important distinctions:
- If it is a course with step-by-step instructions that you just repeat - everyone will have the same project with the same code. Not much value in that
- If it is a course homework where the task is given but the implementation is yours - that is much more valuable
- If it is an original project that you came up with and built from scratch - that has enormous value

The level of commitment is very different and it shows. When you were really involved in the task, you will have answers to questions because you lived through it, not just copied it.

### Production-level practices in personal projects

Companies do not expect production-level engineering practices in personal projects. That would be over-engineering - it would look forced. It is very hard to have real production-level problems in personal projects.

Clarity is more important - everything should be clean and understandable, solving your problem. But do not forget about basic best practices. We are not talking about thousands of requests per second - just a normal project that solves your specific task.

If you have a personal project that genuinely requires production-level infrastructure, you probably do not need a job - you already have one.

### Tests and CI/CD pipelines

Tests and CI/CD are pretty easy to implement, especially with AI assistants. You need to write tests regardless. And once you have tests, asking Claude to wrap them in GitHub Actions is a 5-minute thing.

Start with regular unit tests, then integration tests, then end-to-end tests, then LLM-as-judge evaluations.

### Using Claude Code in your portfolio

For me this is neutral. If you do not use Claude Code or some assistant, you are missing out. But I do not see a reason to specifically mention it.

If you want to be open about it, you can say at the end that the project was built using AI-assisted development and indicate your contribution. If you discuss this with the hiring manager, the conversation might go into how exactly you used the assistant, how you gave instructions, how you made sure the agent did not make mistakes. If your answer is "I gave a prompt and everything worked from the first try" - I will have questions. Because it never works from the first try.

Whether to write about it or not is your call. I see nothing wrong with writing it. I see nothing wrong with not writing it.

### AI developer vs AI engineer

For me this is all semantics. I cannot say there is some huge difference. There is supposedly an industry opinion that a developer is a level below in the sense that a developer is more of an executor while an engineer thinks more holistically. I think this is all semantics.

### AI engineer vs software engineer using AI

The line is pretty thin. Most likely, from software engineers the expectation is more of a generalist. While AI engineer is probably a more focused role. But in practice, like duck typing in Python - if the methods are the same, there is essentially no difference regardless of what you call it.

### Job description quality and filtering

I did not have a filter for low-quality job descriptions when scraping data. The number of such descriptions is likely not zero. Some job postings exist just for show - to signal to investors that the company is actively hiring. I did not do any filtering for this.

### ML understanding and reasoning skills

Understanding ML and neural networks is useful for AI engineers. About 64% of AI engineering roles require some ML knowledge. But if we look purely at AI engineering core skills, the ML component is not always required.

However, at large volumes, LLMs become expensive. You need to be able to do what the LLM does but faster and cheaper. Typically this means: take the LLM, use it to label data, and train a classical model on that data that works faster and cheaper. Such use cases exist especially at scale.

### Market pushing AI adoption

Yes, this happens. There are stories where management sends down the order: "we need to show investors that we use AI, so everyone start doing AI immediately."

If you are suddenly told to do AI but there is no real problem that AI solves: on one hand, this could be a good opportunity to learn something new. On the other hand, you can say "I think we have many other unsolved problems to focus on." It all depends on the specific situation.

### ML jobs becoming GenAI/LLM

It would be interesting to verify whether 99% of ML engineer jobs are now related to GenAI/LLMs. I might try to run the same analysis but for ML engineers. Take New York as a representative city and see what is there.

### Frontend skills for data engineers and AI engineers

From the data: 31.4% of AI-first roles mention frontend skills, 49.6% mention backend skills, and 21.6% mention full-stack (both). So it is more backend-focused.

In general, AI engineer is a full-stack role - the data confirms this. But the expectation is not that an AI engineer will proactively push things to the frontend. Each role has its specialization. Data engineers should work on pipelines, frontend developers on frontend. But if the need arises, it is fine.

About Jupyter Notebooks: everything that happens outside Jupyter Notebooks is useful. Even data scientists spend time outside notebooks. If a data engineer only does things in notebooks, I have serious questions about what they are doing.

### Top 3 projects for FAANG interviews

For FAANG specifically: they care more about LeetCode and system design than about projects. LeetCode you just have to grind, and system design you have to study. Pet projects do not help with either of these.

There is also ML system design and now AI system design. Big companies ask about system design for senior roles and above.

### Local hardware for running models

There are justified cases. In some companies, data is very sensitive and must not go to any cloud. If you want to work with financial or medical data, you need to be maximally careful.

Some startups keep their own GPUs to host their own models for compliance reasons.

About the future of local LLMs: right now models from Anthropic and others are heavily subsidized through subscriptions - you pay much less than the actual cost. This cannot last forever. On the other hand, local models are gradually catching up with cloud models. You can already run something like Qwen3 on a MacBook and it will work reasonably well.

### EU-remote work percentage

This can be checked in the data. It would also be great if someone from the community dug into the data and answered this question themselves.

### Identifying first/only AI role from job description

This is hard. You need to talk to people and ask. From a job description alone, it is hard to tell. But sometimes you can see it when the requirements are too broad - when it looks like a job description for a data engineer, AI engineer, and ML engineer all in one. That is likely a first hire.

But being the first AI hire is not necessarily bad. Sometimes when you join a startup as the first person, you can learn a lot.

### Entry-level AI engineer positions

You can figure out the answer by analyzing the data. Collect the data, analyze it, draw conclusions, and based on those conclusions create a concrete learning plan.

Write about this - every day share what you learn, do learning in public, building in public. You will grow your network, people will notice you.

### Will AI engineer replace traditional MLE?

I do not think so completely. The overlap is large and right now there is more hype around AI engineering. But this is temporary. Things will calm down and there will be more understanding of when to use AI and when not.

GenAI is here to stay. But through the hype cycle, traditional ML is still needed and important. There are use cases you can optimize with ML later, guardrails made with ML (not GenAI) because they need to be fast.

Right now it is like data science 10 years ago - everyone wanted to do it but nobody understood what it was. Now there is understanding. The same will happen with AI engineering.

### Is SaaS dead?

Of course not. Many services provide value that is hard to replicate. Stripe is not going anywhere. You can now vibe-code alternatives for some things, but not for everything.

Some things are becoming more commoditized - if you have a very specific use case and cannot find anything ready-made, you can now build it faster. But SaaS is definitely not dead.

### How I use AI/ML in daily activities

ML - very little. AI for automation - everywhere. I use coding agents frequently, then I use various AI tools for work automation. In my personal work, I use assistants extensively - to write code faster and to automate things.

### How to adapt to AI

If you are worried that AI will take your job, study automation tools and automate your own work. The 20 hours you invest in learning this will pay off within a couple of months at most.

For specific first steps: it depends on what you want to learn. If you do not have your own ideas, look at what others are doing, see what resonates, try to repeat it and adapt to your situation.

The key thing: do not fall into dopamine traps. Focus on what interests you personally and do not rush.

### Comparing AI roles: LLMOps, AI Platform Engineer, AI Production Engineer

LLMOps is like DevOps - a set of practices about how you deploy models to production. But there is a role called MLOps Engineer - usually they are the people who organize the platform so that ML engineers can deploy models.

LLMOps and AI Platform Engineer could be the people who do the same but for LLMs. This might include deploying your own models (or not), but overall it is about organizing the process: setting up monitoring, making it so that when you press a button your agent deploys and monitoring automatically connects, you can collect logs and do evaluation based on those logs.

### Learning without LangChain frameworks

Yes, you can absolutely learn without LangChain. I even recommend not starting with LangChain. Start with the basics: tool calling, the tool calling loop. And only then start using a framework.

This is better because you understand what happens inside. LangChain is not a bad framework, though I would not use it in my own projects. You can definitely learn without it.

### Fine-tuning for healthcare

It all depends on the use case. You might not need fine-tuning at all. There is a movement called small language models - take a small model, distill it to the minimum, fine-tune it for your specific task, and it handles that task very well, cheaply and quickly.

Based on the data I collected, I would not focus on fine-tuning right now. There are many other things to learn first. Unless you know a specific company and position needs it.

### Do local LLMs have a future?

Yes. Right now models from Anthropic and others are very subsidized - you pay much less than the real cost through subscriptions. This cannot last forever. On the other hand, local models are gradually catching up with cloud models. My hope is that by the time cloud providers raise prices significantly, local models will be comparable in quality.
