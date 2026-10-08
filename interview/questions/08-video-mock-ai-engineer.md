# Video Mock: AI Engineer Interview Questions

Source: user-pasted transcript from the AI Engineer mock interview at
`O-kuHMOdjX4`.

The interviewer tested breadth across classical ML, GenAI, RAG, embeddings,
backend Python, metrics, computer vision, and production judgment. The main
lesson was to avoid reaching for RAG, multi-agent systems, or complex pipelines
when a simpler design is more accurate and cheaper.

## Background and Scoping

### Q: Introduce yourself.

No specific correction was given. Keep the answer concise: current identity,
production AI experience, one differentiator, and why this role.

### Q: How would you rate yourself in pre-generative-AI ML knowledge?

Be honest and name the areas behind the rating. A rating is less useful than
explaining what you can design, implement, evaluate, and debug independently.

### Q: What is generative AI good at versus core ML, and when would you use ML?

Use classical ML for stable prediction, classification, ranking, clustering, or
forecasting with a well-defined target. Use generative AI for language,
open-ended synthesis, extraction with flexible schemas, and tasks where the
output is not a fixed label. Do not use an LLM for a simple classification task
just because it is available.

## NLP and Embeddings

### Q: You have about 500 IMDb reviews to classify as positive, negative, or mixed. ML or GenAI?

Prefer a supervised NLP classifier when the labels are clear and the task is
bounded. Consider the dataset size, label quality, required accuracy, latency,
explainability, privacy, maintenance, and API cost. A fine-tuned or pretrained
encoder, embeddings plus a classifier, or a smaller Transformer may be more
appropriate than a general-purpose generative API.

### Q: How would you get the embeddings?

Choose a pretrained embedding model appropriate for the language and domain,
then validate it on the target classification or retrieval task. For a small
labelled dataset, compare frozen embeddings plus a simple classifier against
fine-tuning. Avoid assuming that a larger embedding model is automatically
better.

### Q: If you use an LSTM, how do embeddings come into the picture?

Tokens are mapped to dense vectors before entering the LSTM. The LSTM consumes
the vector sequence and models order and temporal dependencies. Embeddings may
be pretrained or learned during training.

### Q: What is the difference between an embedding and an encoding?

Encoding is the general process of representing information in another form.
One-hot encoding is a sparse identifier representation and does not express
semantic similarity. An embedding is a dense learned representation where
similar items can be close in vector space.

### Q: Is one-hot encoding the same as encoding?

No. One-hot encoding is one kind of encoding. The important distinction is that
one-hot values identify categories, while embeddings can capture relationships
and semantics.

## RAG Judgment: Invoice Chatbot

### Q: Design a chatbot for questions over 100 one-page invoices. What challenges do short documents pose?

First clarify the questions, fields, accuracy requirement, access control, and
whether the documents fit comfortably into a model context window. For only 100
short documents, a simple extraction-plus-structured-query approach or putting
the relevant documents directly into context may be better than a full RAG
system. Use RAG when the corpus or query volume makes retrieval useful.

### Q: Is there a problem extracting invoice text with OCR?

Yes. Plain OCR can lose table structure, column relationships, reading order,
and line-item boundaries. Preserve layout with a table-aware/document-aware
parser, or convert the document into a structure that explicitly represents
tables and fields before indexing it. Always validate extraction against the
original invoices.

### Q: For only 100 one-page documents, do you need MapReduce or big-data processing?

Usually no. MapReduce is justified by scale, parallelism, or a specific batch
processing constraint. For 100 short documents, it adds operational overhead
without solving the main problem. Start with a simple, testable pipeline.

### Q: Why use KNN instead of cosine similarity with a threshold?

Clarify the terminology first. KNN is commonly a supervised classification or
regression method; vector search can retrieve nearest neighbors using cosine,
Euclidean, or another distance. For a small corpus, direct similarity search
with a threshold may be simpler. Choose top-k when you need a bounded candidate
set, then validate whether the threshold or ranking produces correct answers.

### Q: How does nearest-neighbor retrieval work?

Embed the query, compare it with document or chunk vectors using a chosen metric,
rank candidates by similarity or distance, and return the top results that pass
the relevance policy. In production, add tenant and document-version filters,
metadata, access control, and an abstention path when no result is reliable.

### Q: Why can a two-stage distance-then-cluster pipeline be worse?

Every extra stage adds another opportunity for error, latency, and tuning
complexity. If stage accuracies are roughly 0.9 each, three dependent stages can
have an approximate combined success rate of 0.9 x 0.9 x 0.9. With few
documents, prefer the simplest pipeline that meets the quality requirement.

## Cheating Detection System

### Q: How would you detect cheating on a coding-test platform?

Combine several signals rather than relying on a single classifier:

- unusual solve times or sudden difficulty jumps
- similarity between code submissions
- account, IP, device, and session relationships
- edits, copy/paste behavior, and answer timing
- historical performance and outlier detection

Use a risk score and route high-risk cases for review. Protect privacy, explain
the signals, and measure false positives because an automatic accusation is a
high-cost action.

### Q: What visualization helps detect outliers?

Use box plots for distributions and outliers, then add scatter plots or time
series to expose relationships between difficulty, time, score, and submission
behavior. Visualizations support investigation; they do not prove cheating.

### Q: How can graph databases find group cheating?

Represent users, submissions, problems, devices, and sessions as nodes, with
edges for shared code, shared infrastructure, timing overlap, or suspicious
similarity. Graph traversal can expose clusters and multi-hop relationships.
Finding the original source is harder than finding a connected group, so use
timestamps, problem difficulty, and independent evidence rather than assuming
the earliest node is the source.

## Attention and Model Architecture

### Q: Attention is O(n^2). How would you reduce the complexity?

Discuss the constraint first: sequence length, quality loss allowed, training or
inference, and hardware. Possible approaches include sliding-window or local
attention, sparse attention, linear-attention approximations, and multi-query or
grouped-query attention for reducing KV-cache memory and inference cost. Be
clear that these techniques address different bottlenecks; MQA/GQA primarily
reduce key/value head memory rather than changing every attention computation to
linear time.

## Python, Data Structures, and Metrics

### Q: How would you rate yourself in Python backend work?

State the production scope you can defend: APIs, async work, testing, databases,
observability, concurrency, and debugging. Do not rely only on the language name
or on competitive-programming experience.

### Q: Why is a Python dictionary lookup usually O(1)?

A dictionary is a hash table. A key is hashed to locate a bucket, giving average
constant-time lookup under a healthy load factor. Collisions and resizing can
affect behavior, so O(1) is an average-case statement rather than a universal
guarantee.

### Q: Given 90/100 correct in binary classification, how do you calculate precision and recall?

Accuracy alone is insufficient. Define the confusion matrix first:

- precision = true positives / (true positives + false positives)
- recall = true positives / (true positives + false negatives)

You need the actual positive and negative counts, not just the total number of
correct predictions, to calculate both values.

### Q: For identifying financially dangerous people, precision or recall?

It depends on the cost of false positives versus false negatives. If missing a
dangerous case is very costly, prioritize recall and add review or a second
stage. If incorrectly flagging safe people causes serious harm, precision is
more important. Use a threshold and metric chosen from the business costs; F1
can summarize a balance but should not replace the cost analysis.

## Object Detection and YOLO

### Q: What is YOLO good at?

YOLO is a one-stage object-detection family that predicts object classes and
bounding boxes in an image. It is useful when real-time or near-real-time
detection matters, with a speed/accuracy trade-off controlled by the model
variant and deployment hardware.

### Q: What metric would you use for object detection?

Confidence is not a performance metric by itself. Use precision and recall over
predicted boxes, intersection over union (IoU), and mean average precision
(mAP) at specified IoU thresholds. Also measure latency and false positives in
the target environment.

### Q: How does YOLO produce bounding boxes?

At a high level, the network predicts objectness, class scores, and box
coordinates for candidate locations or queries. Decode the coordinates,
discard low-confidence candidates, and apply non-maximum suppression or the
model's equivalent post-processing to remove duplicate boxes. Be ready to
explain the exact version-specific head if the interviewer asks about a model
you used.

## Model Landscape and Enterprise AI

### Q: Do companies build enterprise AI systems for privacy?

They may use hosted APIs with contractual data controls, private cloud or
VPC-hosted inference, or open-source models deployed on-premises. The choice
depends on data sensitivity, regulatory constraints, latency, cost, model
quality, and operational capacity.

### Q: Do you build multi-agent or swarm systems with A2A collaboration?

Unstructured swarm coordination can be expensive, hard to test, and unreliable.
Prefer explicit orchestration, bounded handoffs, structured outputs, and clear
termination conditions. Specialized smaller models can be useful when a task is
narrow and the quality/cost trade-off has been measured.

## Interviewer Feedback

- The candidate performed well; the interview was intentionally difficult.
- Logical approach and thought process matter more than perfect recall.
- Do not over-apply RAG. Ask whether the corpus is large, changing, or outside
  the model context before adding retrieval.
- Fine-tuning may help with domain behavior, specialized roles, or answer format;
  RAG is better for changing facts and focused external context.
- For a few short documents, neither RAG nor fine-tuning may be necessary.
- An SLM is not a magic replacement for fine-tuning. It can reduce cost and
  latency, but may lose complex reasoning capability.
- Simpler systems often have better accuracy because each extra stage can fail.
- The final improvement from 95% to 99% usually requires system design, cost,
  latency, database, reliability, and evaluation judgment.

## Practice Rubric

Score each answer from 1 to 5:

- 1: names a tool or model without matching it to the task
- 2: gives a plausible technique but misses scale, cost, or failure modes
- 3: chooses a reasonable approach and explains the main trade-off
- 4: compares alternatives using requirements and measurable outcomes
- 5: starts simple, handles follow-ups, and explains when the chosen technique
  should not be used
