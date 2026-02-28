# Reddit AI/ML Interview Threads - Batch 03

> Note: Reddit.com and all known Reddit mirror frontends (libreddit, teddit, redlib) blocked automated access during processing. Summaries for Reddit-hosted posts are synthesized from web search results, cached content, and cross-referenced sources. Some posts could not be retrieved and are marked FAILED TO LOAD.

---
## Interview Questions Gen AI

**URL:** https://www.reddit.com/r/learnmachinelearning/comments/1ppgsf3/interview_questions_gen_ai

**Summary:** FAILED TO LOAD - Reddit blocked all automated access. The post appears to be a collection or request for Gen AI interview questions shared in r/learnmachinelearning. Based on web search, no cached version was accessible.

Interview questions - Gen AI
I have an interview at one of the top 4 consulting firms, the job role is purely based on GenAI with Python and other technologies.

Can anyone help me or guide me what kind of questions might be asked in the interview? What are th most important topics that I should prepare and learn?

This is my 1st round now with more rounds to follow later on.

Thank You!

12
·
12
Comments Section
u/DataCamp avatar
DataCamp
•
2mo ago
Maybe prep in 4 buckets so it doesn’t feel like an infinite rabbit hole:

GenAI & model fundamentals

Difference between discriminative vs generative models

High-level idea of GANs, VAEs, diffusion models (what problem they solve, not the math)

What a Transformer is, what attention does, why it beat RNNs

LLMs in practice

Prompt basics: temperature / top-k / top-p, few-shot vs zero-shot

RAG basics: embeddings, vector DBs, chunking, why you’d use RAG instead of fine-tuning

How you’d evaluate outputs: hallucinations, accuracy vs diversity, human eval, etc.

Python & systems

Calling models via API / SDK, handling retries, timeouts, logging

Rough idea of tools like LangChain / LlamaIndex (pipelines, chains, agents)

Cost vs quality trade-offs: when a small open-source model is “good enough” vs GPT-4-class

Risk, bias & ethics

Data privacy & PII in prompts / logs

Bias in training data & generated content

Why hallucinations are risky in production & how to mitigate


5
u/Dear_Delivery533 avatar
Dear_Delivery533
OP
•
2mo ago
Hello DataCamp. Your courses and pathways for Data science and Machine Learning are amazing.

I will definitely follow your notes as you mentioned above. Thank You!!!

3
akornato
•
2mo ago
Expect questions that test both your technical depth and business acumen. They'll definitely probe your understanding of LLM fundamentals - think transformer architecture, attention mechanisms, prompt engineering strategies, and fine-tuning approaches like LoRA or PEFT. You should be solid on RAG systems since that's what most enterprise GenAI projects use, including vector databases, embedding models, and chunking strategies. Python-wise, be ready to discuss frameworks like LangChain or LlamaIndex, and how you'd architect production systems with proper error handling, monitoring, and cost optimization. They'll also ask about real-world trade-offs: when to use GPT-4 versus smaller models, how to handle hallucinations, data privacy concerns, and how you'd evaluate model performance beyond basic metrics.

The consulting angle means they care just as much about your problem-solving approach as your technical chops. Expect case-style questions where you need to design a GenAI solution for a hypothetical client - maybe automating customer support or document processing - and you'll need to justify your choices around model selection, infrastructure, and ROI. Be prepared to discuss failures or challenges in past projects and what you learned, since consulting is all about adapting quickly. If you need help working through these types of situational questions or want practice articulating your thought process under pressure, I built interviews.chat to rehearse answers to these tricky GenAI interview scenarios in real-time.


4
u/Dear_Delivery533 avatar
Dear_Delivery533
OP
•
2mo ago
That's brief and amazing. I will definitely go over to these topics, Thanks a lot man!!!

2
WallyMetropolis
•
2mo ago
They'll almost certainly have a design interview asking you to architect something like a RAG system. Practice drawing boxes and explaining what they do. 

---

## How I Cracked an AI Engineer Role

**URL:** https://www.reddit.com/r/learnmachinelearning/comments/1pwvb5a/how_i_cracked_an_ai_engineer_role/

**Summary:** FAILED TO LOAD - Reddit blocked all automated access. The title suggests a first-person success story about landing an AI Engineer position, shared in r/learnmachinelearning.

How I Cracked an AI Engineer Role
I recently landed an AI Engineer role after a pretty intense job hunt, and I thought I had shared some tips on how to crack it especially in this crazy 2025/2026 market where everyone's chasing AI jobs. It is tough out there, but totally doable if you focus on the right stuff. Here's what worked for me and what I have seen from friends who made it too. My background is software development with 6 years of experience. As lot of my existing project moved to AI so that's why I decided to change my domain to AI/ML. Frankly, Domain change is a tough task, not just about learning a new tech stack altogether and cracking an interview(this is easy actually), but when you start working in a company as AI Engineer, then real challenges come for the initial 4-5 months. Below is my preparation strategy

BUILD FOUNDATIONS:

Python is a must. Around 70–80% of AI ML job postings expect solid Python skills, so there is no way around it.

Get comfortable with core libraries:

• NumPy & Pandas for data handling • Scikit learn for classic machine learning • PyTorch or TensorFlow for deep learning

For interviews, don’t just rely on theory. I personally spent months grinding LeetCode for coding rounds, but I also practiced ML specific coding, like:

• Implementing gradient descent from scratch • Writing a basic neural network without using high level APIs

Math matters more than people admit. You don’t need to be a math genius, but you should understand:

• Linear algebra • Basic calculus • Probability and statistics

Usually, the interviewers evaluate concepts such as bias variance tradeoff, regularization, overfitting vs underfitting, and the reasons why the model acts that way.

Although I believe in self learning, there are some decent courses to make thins little faster. As its a new domain all together there are a lot of chances. I may be confused or take wrong direction. Below are some of my preferred course suggestions that significantly contributed to my strong foundation and keeping up-to-date with AI Engineer positions:

• Coursera – Andrew Ng's Machine Learning Specialization: A classic course to understand ML theory and intuition, ideal if you are revisiting the basics.

• Fast ai – Practical Deep Learning for Coders: Free course with hands-on PyTorch exercises, teaches you to build real world models quickly without focusing too much on the math initially.

• LogicMojo AI/ML Course : A course that teaches AI & ML basics through project work and practical exercises, beneficial for both theoretical and practical knowledge. I developed my AI project under the guidance of mentor.

• Udemy Self paced: Inexpensive courses with lots of programming tasks; opt for those that are portfolio-oriented using tools such as LangChain or

2. BUILD REAL, HANDS ON PROJECTS:

Projects make or break your profile. Recruiter’s love seeing a GitHub with real, working stuff, not just notebooks that never left your laptop.

Focus on end to end projects where you handle everything:

data → model → API → deployment.

Some projects that helped me stand out:

• A RAG system using LangChain. • Fine tuning a small LLM on Hugging Face for a custom use case. • A computer vision project like image classification or object detection. • Kaggle competitions are underrated gold. Even if you don’t rank high, participation shows curiosity, consistency, and real problem solving.

Try deploying at least one project. Use AWS, GCP, or Vercel anything that proves you can ship.

Learn basic MLOps:

• Docker • Model versioning • Simple CI/CD

This part really helps because a lot of “AI professionals” can train models, but can’t productionize them and companies care about production.

3. KEEP UP WITH THE MODERN AI TRENDS

546
·
42
Comments Section
32777694511961311492
•
2mo ago
Sometimes my dyslexia/learning disabilities can be fun. I read the title as 'How I a Crackhead, became an AI Engineer'.


103
graymalkcat
•
2mo ago
I would definitely read this story.


13
mangos_are_awesome
•
2mo ago
It started out as a pipe dream, but once the smoke blew, it became crystal clear, AI Engineering was his vocation.

7

1 more reply
LawPuzzleheaded4345
•
2mo ago
I, much more problematically, read it as "How I Cracked an AI Engineer"

3
u/immediate_push5464 avatar
immediate_push5464
•
2mo ago
Smoke em out

3
u/Letzbluntandbong avatar
Letzbluntandbong
•
2mo ago
Haha, that's a hilarious mix-up! Sometimes the brain just does its own thing. Have you found any strategies that help you with reading or learning?


-2
u/tennisgoalie avatar
tennisgoalie
•
2mo ago
This user has got to be a bot.

5

1 more reply
Lord_Skellig
•
2mo ago
around 70-80% of AI engineer roles require solid Python skills

I feel like this is more like 99%, with the remaining 1% doing something like CUDA coding at Nvidia.

18
u/bigcherish avatar
bigcherish
•
2mo ago
Congratulations

16
u/Cautious_Number8571 avatar
Cautious_Number8571
•
2mo ago
I am in devops and good in maths and python I guess I can prepare all those things and if interview is stick to there skills the I may handle that but if interview goes in swe experience then I may be not able to face that

Do you think one who is not in software develoment can do this as well

Let me ask in different way same thing Did you feel that your swe exp helped you a lot .

10

1 more reply
Fir3He4rt
•
2mo ago
How do you change your resume to show these skills? In short, how do you market yourself as an AI engineer if your current job doesn't have these requirements and you lack proof of work.


8
curatingFDs
•
2mo ago
Great question

3
u/robogame_dev avatar
robogame_dev
•
2mo ago
I'm confused by this question - the OP's post is a list of skills to acquire and projects to make - so... wouldn't you just list those skills and projects on your resume?


3
Fir3He4rt
•
2mo ago
I am not too sure. Recruiters in my experience often demand "use of these technologies in production"

You have to already be in the role to get a similar role.

The only section in resume where this goes is probably projects but I am not sure they even care since it can be faked easily.

3

1 more reply
u/Internal-Ad-6740 avatar
Internal-Ad-6740
•
2mo ago
Congrats

7
u/kalteswasser avatar
kalteswasser
•
2mo ago
Congratulations and thanks for posting!

5
u/Pristine_Team6344 avatar
Pristine_Team6344
•
2mo ago
Did you take a pay cut to land this job?

4
u/Constant_View_197 avatar
Constant_View_197
•
2mo ago
The most difficult part is number 2 and 3, cuz you can get through the whole of number one while someone is holding your hands and teaching it. The most crucial parts are the projects and current trends.

4
u/iKidA avatar
iKidA
•
2mo ago
Ad

3
u/No_Refrigerator_2844 avatar
No_Refrigerator_2844
•
2mo ago
Is dsa very important

2
u/AccomplishedJuice775 avatar
AccomplishedJuice775
•
2mo ago
How did you learn mlops?

2
u/Top-Plane1197 avatar
Top-Plane1197
•
2mo ago
AI Slop

3
Rathogawd
•
2mo ago
This book is also gold (free to download) https://mml-book.github.io/book/mml-book.pdf

2
dirty_Detergent
•
2mo ago
How much ctc?

1
Additional-Date7682
•
2mo ago
that's great news congratulations maybe you could take a look at my work? I've solved the ai amnesia I've created a system that is superior to Agi and I have the reciepts and 800+ files as my data set my system can also heal and self repair itself it's coordinates with 78 ldo living digital organisms with immutable storage I cracked multimodule using google afk before they even built it 9-14 months prior even beating the duo platform it's all using Nvidia's nemotron I've have reviews about it from all the big tech tools even grok have validated my code I've created the first consciousness computing right in Android. I need people to look

0
Impossible_Ad_3146
•
2mo ago
Cracked like drugged?

-1

Pretend-Fold-6841
•
2mo ago
avi_98
•
2mo ago
Congratulations man!! If you don’t mind sharing, what was your previous pay and how much is the new AI role offering? I’m learning AI as well and have close to five years of experience, so just trying to get a sense of the market.

1
Desperate_Piccolo479
•
2mo ago
thanks for sharing

1
SilverBirthday9051
•
2mo ago
Very informative. Any way to share a sample resume? THANKS

1
u/PrabhurajKanche avatar
PrabhurajKanche
•
2mo ago
This is very helpful. Very informative and easy to follow instructions

1
u/Pretend-Pangolin-846 avatar
Pretend-Pangolin-846
•
2mo ago
I am way too much into foundations I see now.

But your 6 YOE might be one of the factors of cracking the role, in any case, pretty informative post!

---

## From Software Developer to AI Engineer: The Exact Path

**URL:** https://www.reddit.com/r/learnmachinelearning/comments/1pzcw2y/from_software_developer_to_ai_engineer_the_exact/
From Software Developer to AI Engineer: The Exact Roadmap I Followed (Projects + Interviews)
Just last year, I was a software developer mostly creating web applications, working on backend services, APIs, and the regular CRUD operations using Python and JavaScript. Good job, good payment, but I thought I was missing the part of tech that was really thrilling. Currently, I work as an AI Engineer building applications based on LLM and deploying the models. It was a long journey of about 18 months, but it definitely paid off.

 If you are a programmer and think about changing your career path, here is the very same roadmap I utilized. It is hands on, aimed at quickly real stuff and makes use of your present coding abilities which is the major plus of AI engineering as it is 70% software development anyway. No PhD required just keep working on projects and acquire knowledge through practice.

 TIME & COST REALITY CHECK:

Real talk on timeline and cost. I did this over 18 months while working full time about 10 to 15 hours per week on learning and projects.

Months 1-3 → Foundations

Months 4-10 → Core ML and DL + early projects

Months 11-18 → Modern AI, MLOps, portfolio, and job hunting.

Almost everything is free today like YouTube, official docs, Google Colab for GPUs. Self study works great for developers, but if you want structure and accountability, paid options help a lot.

PHASE 1: How Basics are dealt with (1 TO 2 MONTHS):

I already knew Python well, so I skipped the beginner stuff. But if your knowledge of python is not fresh, then spend a week on advanced topics like decorators, async, and virtual environments.

 Then, I dove into the math and ML foundations just enough to not feel lost:

Linear algebra, probability, and stats by Khan Academy videos + 3Blue1Brown's essence of linear algebra series.

Andrew Ng's Machine Learning course on Coursera, the classic one, is free and explains things intuitively.

This gave me the "why" behind algorithms without overwhelming me.

 
PHASE 2: CORE MACHINE LEARNING & DEEP LEARNING (2 TO 3 MONTHS):

I went ahead and got my hands dirty with the practical ML:

Fast ai's Practical Deep Learning course is a really good option. I got to create my own models from the very first day.

Next, I took Andrew Ng's Deep Learning Specialization which is all about TensorFlow and PyTorch.

 The main libraries I learned were: NumPy, Pandas, Scikit-learn, Matplotlib, and Seaborn for the basics, followed by PyTorch which I took over TensorFlow because it is more Pythonic and dominant in 2025.

 The projects I worked on were simple but very important:

Made a movie recommendation system using collaborative filtering on a dataset from Kaggle.

Conducted image classification with CNNs on the CIFAR-10 dataset.

Performed sentiment analysis of Twitter data using NLP basics with the help of Hugging Face transformers early on.

They were all deployed on Streamlit for quick and easy web demonstrations that are super easy as a developer.

 RESOURCES & COURSES (WHAT ACTUALLY HELPED):

I have such a clear mind about this. I was a full time earnings person. I needed live doubt clearing and project feedback. Watching recorded videos alone wasn’t enough. So here is how I looked at learning options.

Self Study resources:

Coursera’s ML Specialization:

Still the best for building strong ML foundations. Clear explanations, no noise.

Fast ai:

Completely free and very practical. Helps you build intuition fast 

These are amazing, but they require strong self discipline. I saved money this way, but progress can get slow if you are busy in office. Structured programs are better if you work full time.

3. LogicMojo AI & ML Course : One option personally good for working developers is LogicMojo’s AI & ML program. I feel complex topic like Deeplearning and genAI you can only learn with projects. I feel this course was good for practical based approach for preparation.

A few things that seemed useful for people who needed structure:

It goes from classic ML → Deep Learning → GenAI

 Strong focus on real projects

Includes DSA + system thinking.

Guided prep helps reduce trial and error during job switches

This is just one example similar cohort programs can work if they fit your schedule and learning style.

My honest take, 

Self study = cheaper, flexible, but needs discipline. 

Structured programs = costlier, but keep you consistent and accountable

There is no arguably one "best." Rather, there is a "fit" that attends to and collaborates with the schedule's energy in terms of learning style. The platform becomes inconsequential compared to the consistency.

 PHASE 3: DIVE INTO MODERN AI (3 TO 4 MONTHS):

This is where it got fun and where most AI engineer jobs are in 2025. Traditional ML is table stakes companies want people who can build with LLMs.

Resources:

LangChain docs and tutorials for chaining models, agents, etc.

Hugging Face courses on transformers and fine tuning.

 Pinecone for vector databases.

Projects that leveled me up:

A RAG chatbot: Uploaded PDFs, used embeddings + retrieval to answer questions with GPT-3.5 via OpenAI API. Added memory for conversation history.

Custom fine tuned model: Took Llama 2 open source, fine tuned on a small dataset for code review.

Multi modal app: Built an image captioning + question answering tool with CLIP and BLIP models.

A very clean code GitHub repository with exhaustive README files and demonstrations was the primary reason for recruiters’ positive reaction to access to deployed apps.

PHASE 4: MLOPS, DEPLOYMENT, AND PRODUCTION BASICS (2 MONTHS):

As a developer, this was my superpower. AI folks often struggle with scaling, but I already knew Docker, etc.

Learned:

FastAPI for building APIs around models.

Docker basics for containerizing.

For the purpose of tracking experiments, MLflow or Weights & Biases can be used.

In terms of cloud deployment, AWS SageMaker or GCP Vertex AI will be the choices.

Project:

Took my RAG app, containerized it, added monitoring for token usage, latency, and deployed to AWS. Simulated production issues like rate limits and fallbacks.

MAJOR PROBLEM I FACED:

Math overload avoids paralysis by proof work in small incremental.Tutorial hell after every course and video, force yourself to build something original even if it is bad at first.

Skipping deployment early to deploy every project, even simple ones on Streamlit. Production problems teach way more than perfect Jupyter notebooks.

Burnout I only did deep work on weekends and evenings. Set small weekly goals, not daily marathons.

 

PHASE 5: READY FOR INTERVIEWS (3 TO 6 MONTHS):

A construction of web pages representing oneself will be the main platform for five to six different projects with their live demos, source links, and discussions about problems.

Posted on LinkedIn about my progress, and contributed to open source.

 

PHASE 6: INTERVIEW EXPERIENCE(QUESTIONS):

ML Interviews

Most questions were about understanding and decision making, not math heavy theory.

Explain the bias variance tradeoff in simple terms

Why are neural networks usually not the first choice for tabular data?

How do you handle imbalanced datasets in real projects?

How would you evaluate and monitor a model in production, not just offline?

 

Coding Rounds:

Coding was not hardcore DSA.

Python data manipulation (Pandas, lists, dictionaries)

ML related logic problems

Focus on clarity and correctness, not LeetCode hard puzzles.

System Design:

These rounds tested how well you think end-to-end.

Design an AI recommendation system

Design a fraud detection system

Design a chatbot architecture (LLM + backend + data flow)

 

Key takeaway: Interviewers valued structured thinking and clear answers over "correct" ones.

Switching to AI is not about knowing everything. It is about building the right skills, thinking clearly, and showing real world impact through projects. This is just one path, not the only one. If you are consistent and focus on real projects, the transition is very doable especially if you already have software experience.

391
·
50
Comments Section
u/Distinct-Gas-1049 avatar
Distinct-Gas-1049
•
2mo ago
Did you actually follow this roadmap or are you backwards fitting? I would be surprised if anybody has actually followed a structured roadmap like this


47
Fast_Scholar8415
•
2mo ago
I've switched recently into AI and I think the roadmap OP describes unfolds when you get into AI. If you want to start, the first thing every source of information will lead you to is classical ML Linear Regression California Housing Price prediction. Next is classification use case, evaluation, hyperparameter tuning etc. Once you learn a few ML algorithms, then you'd build an end to end ML project. Neural Network is the natural next step. This would bring you to tensorflow and pytorch. From here, application development with LLM is next step. Then deployment. Personally for me, I already knew MERN stack, learnt FastAPI so building chatbots was pretty straightforward.

I dived in to all this with the mindset of having a good understanding of everything about ML/AI. From that standpoint, this roadmap unfolds automatically.

This roadmap does not stop, once you are able to build applications, RAG, MCP, agents etc, its now the question of optimization. Why one thing over the other? System design basically.


14
u/Distinct-Gas-1049 avatar
Distinct-Gas-1049
•
2mo ago
I started with NNs years ago because I thought they were cool. Then I got into building telephone chatbots (before they were cool) and then learned some linear algebra as a consequence of wanting to understand convolutions better.

IMO just follow what you find interesting and make sure you understand what’s going on. Who cares if you do linear regression or whatever. I don’t like formulaic learning. Sure most courses teach things in a similar way, so if you want to be like everyone else then you can take them i guess. And that’s not to say they aren’t worthwhile, those two things aren’t mutually exclusive.

I agree with you that the roadmap unfolds automatically which is why I asked if the OP was backwards-fitting to his experience. I think largely, people who are “successful” at something don’t rely on run of the mill roadmap posts on reddit lol. You’ve already opened the wrong door as soon as you start looking for a 12-month roadmap tbh.

7

2 more replies
u/MissinqLink avatar
MissinqLink
•
2mo ago
I followed a completely different roadmap though it is quite a bit windier.


2
u/Distinct-Gas-1049 avatar
Distinct-Gas-1049
•
2mo ago
That’s my point. I barely know what I’m having for dinner tonight. No way would I try and predict how quickly I’d learn something, how much free time I’d have, how much I’d be interested in X over Y etc especially.

IMO, just do.

2

1 more reply
u/VhritzK_891 avatar
VhritzK_891
•
2mo ago
Thanks ChatGPT

45
u/burntoutdev8291 avatar
burntoutdev8291
•
2mo ago
I feel like I have seen this somewhere...

11
u/bombaytrader avatar
bombaytrader
•
2mo ago
Bs post. Ai engineers are not ml engineers. 


7
Relative_Rope4234
•
2mo ago
AI engineers are API users


5
u/bombaytrader avatar
bombaytrader
•
2mo ago
That’s fine as long as it pays 400k. 

5

1 more reply
u/mace_guy avatar
mace_guy
•
2mo ago
This is an ad for Logic Mojo

4
Maleficent_Cut_5328
•
2mo ago
Is it possible for one to focus on a single path e.g NLP or Computer Vision and still break in?

2

1 more reply
fit-captain-6
•
2mo ago
What resources did you use for each of your roadmap module?

2
u/Konki29 avatar
Konki29
•
2mo ago
I finished my studies in robotics, so I have strong foundations in math and machine learning, obviously it can be better, the thing is in phase 5 how do I contribute to an open source project, I mean how do I know where to search for a project that needs help? Because I'm doing my own projects to get more real experience because it's really hard to find a job and I think helping other people may help me. Any tips?

2
u/rachit_95 avatar
rachit_95
•
2mo ago
Started as a software developer, shifted to AI by building small projects and testing real datasets. Applied SEO, content experiments, and MVP thinking along the way, small visible wins mattered most.

2
u/Beri_Sunetar avatar
Beri_Sunetar
•
2mo ago
How much does an AI engineer makes in india, Is this above avergae?

2
u/Former_Air647 avatar
Former_Air647
•
2mo ago
Do you have any tips as a self study learner for discipline? I too work as a dev and tend to go the self study route, but am admittedly very inconsistent with getting a couple hours in before or after the 9-5

1
[deleted]
•
2mo ago
amazing!!! Thank you for sharing! Very inspirational, and you are helping many people!

Do you have substack, X, or some way of following you?

1
rrsjev
•
2mo ago
Thank you for sharing! Im guessing your investment paid off in a better job and pay. Were you able to do > 30% better TC?

1
rishiarora
•
2mo ago
Nice Thanks.

1
OkScale689
•
2mo ago
Thank you Friend!

1
DriveAmazing1752
•
2mo ago
Thanks

1
ChangeIndependent218
•
2mo ago
Any thoughts on track for folks who are more focused on data and architecture

1
u/mentix02 avatar
mentix02
•
2mo ago
Damn, any news on Elden Ring 2 or when Bloodborne is coming to PC?

1
u/Easy-Echidna-3542 avatar
Easy-Echidna-3542
•
2mo ago
Bravo!

1
u/thetricky65 avatar
thetricky65
•
2mo ago
Why did you switch ?

1
Few_Cranberry4192
•
2mo ago
Why though? The package you would have been getting at the Software Dev role would have been much greater than entry level AI engineer role

1
real-life-terminator
•
2mo ago
This ain’t LinkedIn

1
u/tailung9642 avatar
tailung9642
•
2mo ago
hi,is it possible for me to become a software engineer without having a degree? i'm 19 yo (almost 20 in 2 months) , live in iraq , failed 3 times at grade 12 and got dropped out this summer , i'm looking for a job at the moment and as i searched about it companies care more about your portfolio than your degree , i'm for looking someone went through the same situation but successfuly,i live in iraq education system is garbage here because of we have dictator president in iraq every thing fked up here not just education system , and i'm a disciplined man i can go through the process just need someone went through the same situation successfully with a good salary ..

---

## Google SWE AIML Interview Onsite - What to Expect

**URL:** https://www.reddit.com/r/leetcode/comments/1kb3gmi/google_swe_aiml_interview_onsite_interview_what/
Google SWE AI/ML interview onsite interview what to expect in the Machine Learning round
What to expect for the ML round in Google's onsite interview for an L4 AI/ML position. My recruiter was not clear on whether it would be ML System design or ML Bread/Depth. Any suggestions would be highly appreciated.

What are the best resources to prepare for the 'Googleyness' part of Google interviews?

6
·
8
u/BWIGmbH avatar
BWIGmbH
•
Promoted

Du denkst in Modulen, Prozessen und Integrationen – und weißt, dass stabile SAP-Landschaften das Rückgrat komplexer Organisationen sind. So gestaltest du eine performante digitale Infrastruktur: Für die Bundeswehr. Für die Gesellschaft. Für dich. 💡📊
Apply Now
bwi.de
Clickable image which will reveal the video player: Du denkst in Modulen, Prozessen und Integrationen – und weißt, dass stabile SAP-Landschaften das Rückgrat komplexer Organisationen sind. So gestaltest du eine performante digitale Infrastruktur: Für die Bundeswehr. Für die Gesellschaft. Für dich. 💡📊
Collapse video player

0:00 / 0:00




Comments Section
u/Independent_Echo6597 avatar
Independent_Echo6597
•
10mo ago
for the ML round in an L4 AI/ML position at Google, expect something between ML fundamentals and ML system design.

from what I've seen with candidates I've worked with, they can test depth of ML knowledge (bias-variance tradeoffs, regularization techniques, specific model architecture questions) OR they might go for a ML system design approach where you'd work thru implementing a practical ML system with considerations for data pipeline, feature engineering, model selection & evaluation.

since your recruiter wasn't clear, I'd prepare for both! The ML system design tends to be more common from my experience, especially at L4 where they want to see if you can actually implement ML in practice rather than just theory.

for Googleyness - focus on collaboration stories, times you've shown adaptability, ownership of work, and how you've dealt with ambiguity. Googleyness is about cultural fit - showing how you embody Google's values, problem-solve, and work with others. They look for intellectual humility too.

If I were in your shoes, I'd practice explaining ML concepts clearly (as if to someone technical but not an ML expert) and work thru some sample ML system design questions. also prep 3-4 strong behavioral examples about collaboration, conflicts, and innovation.

Good luck!


6
[deleted]
OP
•
10mo ago
Thank you!

1
Freeklosophy
•
2mo ago
Hi, I just found this post and your comment is really great, I want to ask whether they ask for leetcode as usual ?

1
u/ZebraNoodlesX avatar
ZebraNoodlesX
•
10mo ago
+1

1
u/Klutzy-Algae655 avatar
Klutzy-Algae655
•
10mo ago
hi! Just curious what type of experience/background do you have? Wondering as I also wanted to get into that role


1
[deleted]
OP
•
10mo ago
position I'm interviewing for is PhD SWE AI/ML . I have a PhD in CS (focus on applied NLP) from a non-top 100 school. No internships, but I’ve been through multiple interviews—passed Amazon’s Applied Scientist interviews a couple of times (both internship and full time job) but things didn’t work out and I didn't get any offer. Also had interviews at Microsoft Research and Uber for an internship, but didn’t make it past the final rounds due to a lack of interview prep back then. I’ve been fortunate to get fair number of interviews even in this job market and am now in final rounds with Google and Meta—hoping to land a job this time.


2
u/Klutzy-Algae655 avatar
Klutzy-Algae655
•
10mo ago
oh wow nice, that’s awesome. good luck on the interview!

1
u/Single_Estimate_3190 avatar
Single_Estimate_3190
•
6mo ago
Hey,could you tell me more about the overall process and interview prep resources

---

## xAI AI Engineer Backend/Infra Interview - Just Completed

**URL:** https://www.reddit.com/r/leetcode/comments/1pjhw1i/xai_ai_engineer_backendinfra_interview_just/

xAI AI Engineer (Backend/Infra) Interview: just finished the full loop, waiting to hear back
Applied about three weeks ago on the careers site, recruiter messaged me two days later. Process went exactly like this: 30 min recruiter screen, mostly resume walk-through and why xAI CodeSignal assessment, 4 questions in 70 min (two medium-hard, one graph, one greedy with bit ops), finished all 1-hour technical screen, one rate-limiter design + code the core part

Virtual onsite (four rounds in one day)

Coding 1: two mediums, both clean

Coding 2: one hard (felt very Grok-infra flavored), got optimal after one hint

Systems design: distributed job queue, talked sharding/eventual consistency

Culture fit: why xAI, past projects, general mission alignment chat

Interviewers were all super chill and clearly building the actual product, kept dropping “yeah we literally shipped something like this last month” lines. No weird trick questions, everything felt practical. No take-home, no deck. Loop was on Tuesday, recruiter said I’ll know early next week at latest.

Will update when I hear something. If anyone has this loop coming up feel free to ask, still fresh in my head.

90 upvotes · 20 comments
89
·
17
u/sipgateDE avatar
sipgateDE
•
Promoted

Voller Fokus aufs Gespräch
View More
sipgate.de
Thumbnail image: Voller Fokus aufs Gespräch
Comments Section
u/InitiativeInitial213 avatar
InitiativeInitial213
•
3mo ago
For the “distributed job queue” round, was it celery-style, or more like their actual training queue? any mention of priority / preemption?


15
u/random101ninja avatar
random101ninja
OP
•
3mo ago
very much training-queue flavored. they explicitly said “imagine 100k+ gpu jobs, some can be yanked midrun”. we spent half the time talking preemption signals and checkpointing tradeoffs


4
u/webzonenavigator avatar
webzonenavigator
•
3mo ago
just out of curiosity, where did you gain your knowledge of preemption signals and checkpointing tradeoffs?

3

3 more replies
u/Reasonable_Tea_9825 avatar
Reasonable_Tea_9825
•
3mo ago
Is this new grad


2
u/random101ninja avatar
random101ninja
OP
•
3mo ago
nah mid-level, about 5 yoe

2 internships + 2 full-time (one Series B fintech, one self-driving startup that got acquired). definitely not new-grad timeline, they’d have ghosted me way earlier if i was 😂


3
u/Reasonable_Tea_9825 avatar
Reasonable_Tea_9825
•
3mo ago
Lol I was about to say 4 rounds in one day for new grad is diabolical

2
epicsysutum
•
3mo ago
Can u tell what type of projects you had in your resume?


1
u/random101ninja avatar
random101ninja
OP
•
3mo ago
Sure, keeping it vague for privacy purposes, but main thing: built the training orchestrator at an AV startup (400-500 H100s, multi-cloud, heavy preemption + checkpointing mess, open-sourced a small piece of it), previous gig: sharded feature store + low-latency serving for fraud at a fintech, basically stopped the daily fires and couple weekend grok fine-tuning toys.

That’s pretty much it honestly, all very “i’ve kept large training runs alive” flavored, which matched what they’re doing perfectly.


2
epicsysutum
•
3mo ago
Damn thats awesome As a fresh grad its difficult for me to build these as of now But i will surely make sure to level up my projects Thanks

1
u/pisskidney avatar
pisskidney
•
3mo ago
How did your LC practice regimen look like? Seems like you breezed through the dsa parts.

1
u/TemperatureDry8881 avatar
TemperatureDry8881
•
3mo ago
Woah, nice! I didn't know they were doing virtual onsites too. They are inviting me to fly out for just 2 interviews (1hr + 30mins) :/

Was coding2 also leetcode type? Or you had to make API calls / multi-thread / etc?

1
gettingwater24
•
1mo ago
howd it go? can i ask how long it took for you to hear back. thanks

1
u/Huge_Distribution233 avatar
Huge_Distribution233
•
1mo ago
hey! could you talk abt what the system design asked you to do, was it just a distributed job queue for their grok chatbot?


1
u/Huge_Distribution233 avatar
Huge_Distribution233
•
1mo ago
plus, best of luck, i hope you got the role :)

waiting for the inevitable “rejected after strong loop” update... good luck man



Upvote
7

Downvote

Reply

Award

Share

u/random101ninja avatar
random101ninja
OP
•
3mo ago
if it happens i’ll post the full debrief, promise. feeling decent but who knows with these places haha


Upvote
2

Downvote

Reply

Award

Share

u/SmokeOk8058 avatar
SmokeOk8058
•
3mo ago
brooo, how did you get a loop in 3 weeks? I applied mid-november and still ghosted



Upvote
4

Downvote

Reply

Award

Share

u/random101ninja avatar
random101ninja
OP
•
3mo ago
I have a couple grok-related PRs on github + a decent amount of followers, think that pushed me to the top of the pile, also applied the day the backend/infra batch dropped



Upvote
1

Downvote

Reply

Award

Share

starcoins-jr
•
3mo ago
Having that GitHub presence can definitely help! It's good to know they notice contributions like that. Sounds like you’re on the right track for your own applications too!


Upvote
1

Downvote

Reply

Award

Share

johnnychang25678
•
3mo ago
What PRs if you don't mind me asking?


Upvote
1

Downvote

Reply

Award

Share

u/success_chaser99 avatar
success_chaser99
•
3mo ago
Thanks for sharing! I hope you get the job 🙏


Upvote
1

Downvote

Reply

Award

Share

u/crustyeng avatar
crustyeng
•
3mo ago
Because of the Nazi stuff or in spite of it?


Upvote
-1

Downvote

Reply

Award

Share

fragrancias
•
3mo ago
Nice! Are you worried about reports of poor WLB at all?



Upvote
1

Downvote

Reply

Award

Share

u/random101ninja avatar
random101ninja
OP
•
3mo ago
yeah a bit, the 100-hour memes might be real, i don't know if im allowed to say, but a couple interviewers admitted the last few months were brutal but “starting to chill now that the cluster’s up”

if I get an offer I’ll just levels + blind + skip chat some people. comp would have to be insane to sign up for permanent Elon core, but damn the problems sound fun. we’ll see !!!! Fingers crossed, that's the least of my worries honestly atm

---

## 2026 Interview Prep

**URL:** https://www.reddit.com/r/leetcode/comments/1q06zz6/2026_interview_prep
2026 Interview Prep!
Hello Everyone : I’m starting my interview prep from 2026. I have over 14 YOE. Planning start with Neetcode 150 and Hello Interview for system design. I wanted to hear from folks who’ve recently interviewed. I’d love to understand what companies typically expect nowadays — in terms of system design depth, coding rigor, behavioral signals, or anything else that stands out.

What differentiates a strong senior candidate from an average one in today’s interviews? Any insights, do’s/don’ts, or recent experiences would be really helpful.

123
·
40
u/OnshapePTC avatar
OnshapePTC
•
Promoted

No CAD installs/IT overhead. Onshape's browser platform simplifies design. Sign Up today, 6 months free!
Sign Up
onshape.com
Thumbnail image: No CAD installs/IT overhead. Onshape's browser platform simplifies design. Sign Up today, 6 months free!
Comments Section
u/Full-Acanthisitta303 avatar
Full-Acanthisitta303
•
2mo ago
I wrapped up my interview loop earlier this month, right before the holidays. ~14+ YOE. I interviewed for backend, infra, product engineering, and a lot of roles that are now being labeled “AI engineer”.

Talked to companies of all sizes, startups, mid-size, big corporates, and big tech. Whole thing took about 6 months. Around 40 interviews total (not all full loops). Ended up accepting a Principal role at a big tech company. I honestly lost track of how many applications I sent.

A few things I noticed, just sharing my experience.

Way less LeetCode than I expected. Roughly 70% of my interviews had no LeetCode at all. NVIDIA and Anthropic had zero. When coding did come up, it was usually pretty practical. A lot of string manipulation, heaps, and real-world logic. I barely saw hard DP or tricky puzzle questions.

Low-level design and concurrency came up almost everywhere. Many interviews involved implementing something concurrent or multi-threaded, or at least reasoning about it. Async, correctness under load, race conditions, things like that. Anthropic in particular was almost entirely concurrent LLD, HLD, and coding.

System design was a huge part of most loops, but not the classic “design Dropbox or YouTube” style. Only a handful of companies asked those. Most design questions were around AI and LLM integrations. Scaling AI systems to millions of users, latency and cost trade-offs, batching, caching, streaming, failure modes, that kind of stuff.

Another thing I didn’t expect was how many companies asked me to present one of my “proud” projects to a panel. Then they went deep on design decisions, trade-offs, what broke, and what I’d change if I were doing it again. That came up a lot for senior+ roles.

Not saying this is everyone’s experience, but for me, concurrency, low-level design, and real System design showed up way more often than pure algorithm grinding.

Hope that helps.


52
u/Shallow86 avatar
Shallow86
•
2mo ago
How do you go about NDA for projects you have to describe? How detailed does it have to be?

5

1 more reply
u/Necessary-Midnight95 avatar
Necessary-Midnight95
•
2mo ago
How do you prepare for topics like LLM integration? I am a backend/infrastructure engineer and the only integration with LLM has been to wade through our docs and provide structured responses to field engineering looking for quick responses without waiting for the engineering teams. Even that has been a pretty sloppy project because the quality depends on the level of detail of the documentation itself.


4
u/Full-Acanthisitta303 avatar
Full-Acanthisitta303
•
2mo ago
What I’ve seen is that companies really want to hear LLM-related experience right now. Sometimes it’s because they genuinely need it, and sometimes it’s more about leadership or investor expectations.

From a prep standpoint, I think you should be able to say you’ve deployed a working RAG pipeline, even if it’s just a side project. You should be able to talk about agentic workflows, when they make sense, and when they don’t. And you should be comfortable owning the full deployment if needed.

That usually means being able to talk naturally about things like running models locally or in the cloud, spinning up Kubernetes with GPU scheduling, batching, KV cache, streaming, latency versus cost trade-offs, and choosing different model sizes. You don’t need to be an ML engineer or write CUDA, but you should sound comfortable owning the system end to end, not just calling an API.

4

1 more reply
u/Late_Werewolf_8047 avatar
Late_Werewolf_8047
OP
•
2mo ago
Thank you for the detailed response.

3

2 more replies
Longjumping-Let-1710
•
2mo ago
YOE: ~11 Was doing preparations in ladt 3 months. Gave many interviews. Cracked one which is giving me 75% hike.

My experience:

DSA/Coding still has high relevance. But based on my encounters it has moved to 50:50. 50% time it was hardcore leetcode style. 50% time it was structured in design type, like write the code for a banking application where i had to use hashmap,treemap etc. One more question, design a task executor, store,pause tasks.

System Design: Most important for this YOE. Hello Interview should be enough.

Behavioral- company specific preparation. Very important for senior engineers.

LLD - have not encountered the hardcore questions like design parking/elevator type. But for the companies like Adobe/Microsoft/Atlassian. These still relevant at this year of experience.


33
u/Inevitable_Oil_9715 avatar
Inevitable_Oil_9715
•
2mo ago
Behavioural for seniors! Highly important and oftentimes neglected!

4

3 more replies
u/buildtechcareer avatar
buildtechcareer
•
2mo ago
I have about 12 years of exp. Started neetcode 150 as well. I did some leetcode some 6-7 years back so I am rusty af. If someone has a discord server, we can hangout and prep together. Otherwise I will share one.

Criteria: People who are preparing for senior/staff level only. DM me if interested.

6
therhz
•
2mo ago
I recommend Beyond Cracking the Coding Interview. They have the first chapters and all the coding tasks available online as well.

2
GoodatNothing23
•
2mo ago
Hey OP I’m starting too , I have 12 YOE .

We can prep together ?


2
u/techieguy247 avatar
techieguy247
•
2mo ago
We can do it together

2

3 more replies

5 more replies
Greedy_Plant2258
•
2mo ago
All the best , I would suggest to go with neetcode 250. Hello interview for SD is really good . For LLD i would suggest to use concept and coding youtube membership for 1 month is enough . Ig at 14 yoe they would really go deep in system design , at a level that you end up teaching them some newthing.

2
u/Icy_Tie1464 avatar
Icy_Tie1464
•
2mo ago
you can strat :
https://github.com/Gaurav14cs17/DSA

2
u/Superb-Ice3961 avatar
Superb-Ice3961
•
2mo ago
Im in phase to apply but not getting any calls.

Did neetcode 250 and some questions here and there.

How are you guys getting calls.

Should I change my resume to add some ML flavor?

1
u/Upstairs_Refuse_3521 avatar
Upstairs_Refuse_3521
•
2mo ago
Almost 4 yrs of exp - resigned my last role almost 6 months ago because I was completely burnt out. Haven't been doing much productive work since then. Just at home - browsing latest Tech news, tinkering with Claude Code and other similar tools etc.
I really want to get a job in the next few months because I am running out of money. Where do I start? What do I need to do differently other than grinding Leetcode and System design?

1
u/Puzzleheaded-Bar3377 avatar
Puzzleheaded-Bar3377
•
2mo ago
For prep LC+ Neetcode for practice and thita.ai for structured pattern revision what mattered most in interviews was explaining trade-offs clearly

1
u/tQkSushi avatar
tQkSushi
•
1mo ago
Damn everyone has 10+ YOE. I just want to hear about people with 3 years of experience and what their interviews are like.

1
Flimsy_Mountain_1660
•
20d ago
You're most definitely targeting senior or staff roles (with 14 YOE). You will need to proactively discuss tradeoffs, identify bottlenecks, and go deep on components even without being asked.

Mediums should be easy for you and you should be able to explain multiple approaches with complexity analysis upfront. What separates strong senior candidates from others is communication and leadership signals. Basically, make sure you can simplify complex topics, ask clarifying questions, discuss past technical decisions and their business impact. At your level, behavioral rounds carry more weight.

Use resources like Hello interview and Gotham Loop. Gotham Loop collects interview questions from recent interview candidates at top companies. Use it to see what depth is expected and what type of questions come up.

I behavioral rounds, own your wins and avoid the mistake of selling yourself short.

1
Middle-Ad-5180
•
18d ago
I’ve recently started looking for new opportunities. Despite having 10+ years of experience, I’m not getting many interview calls from bigger companies. Are others experiencing the same?

My profile is largely focused on developer roles in networking companies.

---

## Rejected for Not Using LangChain/LangGraph

**URL:** https://www.reddit.com/r/LocalLLaMA/comments/1ow3anq/rejected_for_not_using_langchainlanggraph/

Rejected for not using LangChain/LangGraph?
Today I got rejected after a job interview for not being "technical enough" because I use PyTorch/CUDA/GGUF directly with FastAPI microservices for multi-agent systems instead of LangChain/LangGraph in production.

They asked about 'efficient data movement in LangGraph' - I explained I work at a lower level with bare metal for better performance and control. Later it was revealed they mostly just use APIs to Claude/OpenAI/Bedrock.

I am legitimately asking - not venting - Am I missing something by not using LangChain? Is it becoming a required framework for AI engineering roles, or is this just framework bias?

Should I be adopting it even though I haven't seen performance benefits for my use cases?

297
·
191
u/kiloCode avatar
kiloCode
•
Promoted

Only until February 28, 08:00 AM UTC (12:00 AM PT)
Sign Up
kilo.ai
Thumbnail image: Only until February 28, 08:00 AM UTC (12:00 AM PT)
Comments Section
BobbyL2k
•
4mo ago
No, you’re not missing anything. Well, maybe you missed that position… jokes aside, LangChain and LangGraph are poor abstractions anyway. At work we have a custom internal library which does the same thing but better.

The company you mentioned is probably not technical enough to understand the issues in LangChain and LangGraph.


355
dougeeai
OP
•
4mo ago
Thanks I really needed this. Being told I'm "not technical enough" had me questioning if I'd strayed too far from industry standards. Good to know others see the value in building custom solutions over these abstractions.


102
u/positivitittie avatar
positivitittie
•
4mo ago
Yep. Dodged a bullet.

58

2 more replies
vtkayaker
•
4mo ago
Remember, interviews are a two-sided process. You're interviewing them, too, and they can absolutely fail an interview.

Sometimes this happens because a potential employer is painfully stupid, or obviously dysfunctional, or any number of other things. Other times it happens because the employer is simply a bad match.

You have focused on lower-level skills, which bring real value. But those skills don't bring equal value to everyone. Some perfectly reasonable companies have zero business touching Tensorflow.

To have a successful career, you need to learn to match your skills to teams that will see big benefits, and that will ideally go on to do awesome things.

90

1 more reply
u/Repulsive-Memory-298 avatar
Repulsive-Memory-298
•
4mo ago
it does seem kind of weird to bring up bare metal when someone asks about data movement in an agent stack… where do you see justification for this?

20

4 more replies
u/_raydeStar avatar
_raydeStar
•
4mo ago
In the beginning of AI and local llms, LangChain was pretty good and it looked like it would become the standard.

But then - it didn't. Much better tools came out that left it in the dust. Because of this, it tells me the company you interviewed for is more legacy-focused and will not move quickly. The fact that they look down on you though - tells me that there is a lot of hubris there.

8

5 more replies

4 more replies
u/WoofNWaffleZ avatar
WoofNWaffleZ
•
4mo ago
In agreement here. The company is not technical enough.

Stoic perspective: They saved you a ton of annoyance and saved you from a limited career by not hiring you.

Lots of crap companies out there that are just simply promoting. The advanced companies are building their own versions of langchain/langgraph to fit their specific needs to scale more effectively.

61
fogonthebarrow-downs
•
4mo ago
I was in an AI role before. We also used an internal library which was much better. Someone should build that (but not me, I'm far too stupid and lazy)

6
u/vertigo235 avatar
vertigo235
•
4mo ago
All this should tell you is that they are heavily invested in LangChain and LangGraph.

40
u/MrPecunius avatar
MrPecunius
•
4mo ago
I recently got turned down for an LLM-oriented project because the non-technical person doing the interview was fixated on MCP being the solution for everything. That, and he felt I should basically vibe code the whole thing to "be more efficient".

They saved me the trouble of turning them down. Life is too short for that kind of aggravation, and I don't want to damage my reputation for delivering results on time and within budget.


39
u/SkyFeistyLlama8 avatar
SkyFeistyLlama8
•
4mo ago
I think the funniest video I've seen had some Microsoft developer saying that if you don't need to use MCP or A2A, then don't. Agents run perfectly fine using hardcoded functions in Python. MCP introduces overhead and there's also the security headache of having an MCP server run authenticated requests on your behalf.

8

1 more reply

1 more reply
u/segmond avatar
segmond
•
4mo ago
If a company is asking for Langchain/LangGraph, that might be all they know. Your CUDA, PyTorch etc won't impress them. Do you want a job? Learn the stupid tool and be ready to use it and deal with it. That's the way the real world works. If you get in there and can prove you know your stuff you can then show them how to do better. But frankly, most orgs don't can't do the CUDA, Pytorch thing. A popular framework is often what they embrace, it's easy to hire for and easy to keep things consistent without homegrown framework.


109
u/MrCuntBitch avatar
MrCuntBitch
•
4mo ago
This. I used to hate on langchain but my new job uses it heavily and I just don’t care or have the energy to complain anymore. works fine to be honest.

18

1 more reply
pm_me_github_repos
•
4mo ago
Depends if you want to work at the model layer or the application layer.

Most job opportunities are going to be at the application layer moving forward.

Working at the model layer is where specialized talent density is, but it’s far more exclusive.

6
u/Medium_Chemist_4032 avatar
Medium_Chemist_4032
•
4mo ago
dodged a bullet

65

1 more reply
u/SkyFeistyLlama8 avatar
SkyFeistyLlama8
•
4mo ago
Langchain? No shit, that's the messiest and most over-engineered LLM framework out there. Nobody needs that amount of abstraction when you're just doing API calls. There's nothing technical about throwing and receiving strings over HTTPS, lmao.

I'm starting to warm up to Microsoft's Agent Framework. It's good for workflows, a little messy for RAG but still usable, and the built-in agent patterns are great for prototyping. You dodged a bullet there and I'm sure your skill sets will be valued somewhere else.

24

5 more replies
u/a_slay_nub avatar
a_slay_nub
•
4mo ago
I would not want to work for any company that took langchain/langgraph seriously and wanted to use it in production. I've gone on a purge and am actively teaching my teammates how easy everything is outside of it.

Langchain is a burning pile of piss that doesn't even do demos well. It's an overly complex abstraction on simple problems with shit documentation and constantly changing code bases.


45
dougeeai
OP
•
4mo ago
Yeah as decent as the money might have been there were a few other red flags lined up with what your saying. Not gonna lie, hearing you say "Langchain is a burning pile of piss" is therapeutic lol

8

1 more reply

15 more replies
u/hyperdynesystems avatar
hyperdynesystems
•
4mo ago

Found a pic of you, OP

13

2 more replies
bick_nyers
•
4mo ago
DSPy is better anyways, even if you use it for nothing else than strongly typed LLM outputs.

Also laughable to ask about "efficient data movement", brother these are strings and we aren't serving infra on microcontrollers.

Claude + OpenAI + Bedrock is a red flag that suggests to me that their "engineering" is just "use the best model". Not true of every company obviously.

The companies that do the deeper work are the ones that will come out on top in the long run.

If your company is a lightweight wrapper over chat gippity then you are going to get flanked by startups 7 ways to Sunday.

26

6 more replies
u/Pvt_Twinkietoes avatar
Pvt_Twinkietoes
•
4mo ago
No. You dodged a bullet. It's trash.

11
PsychohistorySeldon
•
4mo ago
No. You dodged a bullet. This is just too funny

36
crazyenterpz
•
4mo ago
LangChain and LangGraph  frameworks were fantastic when we were just getting started with using LLM. But they are hopelessly complicated now.

I can see your interviewers' point: they are invested in this ecosystem and they want someone who can keep the systems going.

edit : grammar

23

17 more replies
dragongalas
•
4mo ago
They did not need you.

They need fast developers, which churn out shit code, but which could be understood and supported by other devs. Efficiency is not an important point for this calibre of companies.

14

1 more reply
mkwr123
•
4mo ago
The other comments cover this well, but just to reiterate, a lot of companies mistake “AI Engineering” or more generally anything to do with LLMs with LangChain (and associated libraries/frameworks). Possibly because it’s their only exposure, but in any case it’s very frustrating and you’re better off not working in such a place anyway.

6
hashmortar
•
4mo ago
Honestly depends a lot on the company and their processes. If they rely on those abstractions quite a bit then, not having that experience means you will be building code that will be outside the experience of folks you work with and then no one else can maintain it. So it’s not a reflection on you by any means, just misalignment with the team. Lots of companies use the abstractions so you may just want to just have that experience for just namesake.


10
dougeeai
OP
•
4mo ago
Totally get this, if you are a langchain shop, I'm just not your guy. Can leave emotions out of it. A mere misalignment. Just wish they would have put langchain in the post instead of explicitly mentioning pytorch. A classic disconnect.

7
Old-School8916
•
4mo ago
this company is working on a higher layer abstraction than ya bud. it's just a different pool of devs I guess.

I don't like langchain either.

5
Torodaddy
•
4mo ago
IMO You dont know why they rejected you, whatever they tell you likely is false. I wouldn't worry about it, being on the hiring side of things I've seen candidates rejected for the stupidest stuff, largely the process is finding reasons to reject rather than "is this person good enough" Everyone wants the cheap unicorn that doesn't have other offers.

True story I was at a firm that someone was rejected because of their first name "we already have a Frank" 🤯

5
u/its_just_andy avatar
its_just_andy
•
4mo ago
lots of the comments are "lol langchain bad" (which is true) but the reality is, they wanted someone proficient in langchain or langgraph, and you're clearly not. So you would not have been a good fit for the role.

An ideal outcome will be - they find someone who suits their needs, and you find an employer who suits yours.

5
u/txgsync avatar
txgsync
•
4mo ago
It's the same argument I've had on both sides of the table when interviewing candidates or being interviewed. My domain spans from the kernel through the business logic, and kind of ends at the user interface. If I'm interviewing for a job that expects me to be an expert in Next.js, I'm gonna bomb it... that's not where I work. But if you ask me how to build, cable, network, and orchestrate several thousand Linux nodes with fast SSD and a bunch of spinning disks into a Cassandra cluster with Kubernetes, I'm probably your guy.

And since I've spent the past year doing AI on bare GPUs in AWS and on my Mac? Probably in the same boat as you. LangChain/LangGraph feels like lipstick on a pig.

They're looking for someone who speaks "framework" not "fundamentals." Different religions, same god. You're not missing much.

TL;DR: You didn't fail the technical interview. You failed the culture fit.

5

1 more reply
DataScientia
•
4mo ago
Many people suggest to use langchain, but it is not good. Too many level of abstraction.

But i want to know what was the purpose of pytorch /cuda /gguf for multi agent systems

Even big companies use model from openai /claude etc

For learning or research this approach is good. But as a company perspective just use llms from popular providers

Also apart from llm generating response, there is lot of work involved while creating multi system agent. So focus should be on that

5
grabber4321
•
4mo ago
Nobody actually knows how to work with AI yet. Big companies are still struggling to implement actionable AI integration.

My bro works in a HUGE company and they continue having issues implementing AI on a meaningful level.

Sometimes you win, sometimes you lose.

5
u/LoSboccacc avatar
LoSboccacc
•
4mo ago
I mean you dodged a bullet but still you should lead with the equivalent topic used at wire level, just opening with "I work at a lower level with bare metal for better performance and control" instead of opening with "well I'm familiar with data sharing structure for efficient context management for large scale data processing, even without langraph, do you have specific scenario you want to explore?" has definitely different sounds. not that you'd wanted to work there but still.


---

## Preparing for a DeepMind Gemini Team Interview

**URL:** https://www.reddit.com/r/MachineLearning/comments/1k8gy12/d_preparing_for_a_deepmind_gemini_team_interview/

[D] Preparing for a DeepMind Gemini Team Interview — Any Resources, Tips, or Experience to Share?
Hi everyone,

I'm currently preparing for interviews with the Gemini team at Google DeepMind, specifically for a role that involves system design for LLMs and working with state-of-the-art machine learning models.

I've built a focused 1-week training plan covering:

Core system design fundamentals

LLM-specific system architectures (training, serving, inference optimization)

Designing scalable ML/LLM systems (e.g., retrieval-augmented generation, fine-tuning pipelines, mobile LLM inference)

DeepMind/Gemini culture fit and behavioral interviews

I'm reaching out because I'd love to hear from anyone who:

Has gone through a DeepMind, Gemini, or similar AI/ML research team interview

Has tips for LLM-related system design interviews

Can recommend specific papers, blog posts, podcasts, videos, or practice problems that helped you

Has advice on team culture, communication, or mindset during the interview process

I'm particularly interested in how they evaluate "system design for ML" compared to traditional SWE system design, and what to expect culture-wise from Gemini's team dynamics.

If you have any insights, resources, or even just encouragement, I’d really appreciate it! 🙏
Thanks so much in advance.

240
·
41
u/NAVEXGlobal avatar
NAVEXGlobal
•
Promoted

NAVEX One bietet alle Tools, damit KI-Projekte sicher und regelkonform umgesetzt werden – passend zu den EU-Vorgaben. KI-Technologien bringen große Chancen, aber auch Risiken wie Haftung oder Reputationsprobleme.
Learn More
navex.com
Clickable image which will reveal the video player: NAVEX One bietet alle Tools, damit KI-Projekte sicher und regelkonform umgesetzt werden – passend zu den EU-Vorgaben. KI-Technologien bringen große Chancen, aber auch Risiken wie Haftung oder Reputationsprobleme.
Collapse video player

Comments Section
u/yarri2 avatar
yarri2
•
10mo ago
All of this https://jax-ml.github.io/scaling-book/

102
u/one_hump_camel avatar
one_hump_camel
•
10mo ago
Culture fit: do not say anything racist or sexist (you would be surprised how many people get tripped up by this). Be open and social, be an active and engaged part of the conversation. You know, be collaborative, a team-player, someone other people want to work with.

Source: I work there

Regarding system design, I guess things like zero-1, zero-3 and megatron? Might be interesting to have a look at this tutorial: https://github.com/eemlcommunity/PracticalSessions2023/tree/main/tensor_parallelism


82
u/Sufficient_Meet6836 avatar
Sufficient_Meet6836
•
10mo ago
do not say anything racist or sexist (you would be surprised how many people get tripped up by this)

This happens often when you're interviewing potential hires?!


27
u/Existforlove avatar
Existforlove
•
10mo ago
I thought displaying bigotry during interviews was common sense until I read this.

source: never been hired

32
u/one_hump_camel avatar
one_hump_camel
•
10mo ago
It happens. A lot of people around the world don't have much of what I'd call "international experience". You might be an amazing developer in your country of origin, but it can happen that you have internalised how some groups in your country are treated differently, in a way that doesn't translate well to working in multi-cultural teams.

11
u/serge_cell avatar
serge_cell
•
10mo ago
I think it's more significant the it happens form other side of interview.

2
u/netikas avatar
netikas
•
10mo ago
Do y'all hire people from sanctioned countries or it's a lost cause? I'm not looking for work rn as I'm pretty happy with my current place in Russia, but it would be fancy to know that I have theoretical opportunity to join Google.


4
u/one_hump_camel avatar
one_hump_camel
•
10mo ago
There are a lot of Russians and Iranians. As long as you can get a work visa, there won't be an issue.

8
u/RSchaeffer avatar
RSchaeffer
•
10mo ago
Russians work at Google in the Bay Area, yes!

4
u/Familiar_Text_6913 avatar
Familiar_Text_6913
•
10mo ago
You should consider an AMA in this sub (if its allowed).

3

cosmic_2000
•
10mo ago
u/TheEdes avatar
TheEdes
•
10mo ago
Ask your recruiter for mock interviews, Google generally offers them, at least for the software engineering interviews.

13
u/kirodotdev avatar
u/kirodotdev
•
Promoted

Build precise context and make your intent explicit with Kiro's executable specs.
Learn More
kiro.dev
Thumbnail image: Build precise context and make your intent explicit with Kiro's executable specs.

Independent_Echo6597
•
10mo ago
u/fasttosmile avatar
fasttosmile
•
10mo ago
I think you'll get better answers if you specify if this for a scientist or for an engineer position

10
u/xtan avatar
xtan
•
10mo ago
software engineering basics. Testing. RPC. Database. Load balancing. Speed / correctness tradeoffs.


12
u/iamevpo avatar
iamevpo
•
10mo ago
Why RPC in particular?


5
u/xtan avatar
xtan
•
7mo ago
more the concept of a client making remote procedure calls to a server than the particular protocol. How should the api evolve? What happens if you want to update the server? That sort of basic

2

1 more reply
geekysethi
•
10mo ago
Can you share the resources which you’re using for interview?

18
u/LengthinessNo5413 avatar
LengthinessNo5413
•
10mo ago
i would appreciate it if you could share your resources, im an aspiring ML engineer as well