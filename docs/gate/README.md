# GATE Voice Assessment Architecture Notes

These documents explain the architecture and engineering reasoning visible in the local GATE voice-assessment project.

The project is a LiveKit-based spoken English assessment agent for ISKCON/GATE. The interesting part is not only that it talks over audio. The project separates the problem into two layers:

- a real-time LiveKit voice worker that guides the learner through a small assessment conversation;
- a BAML assessment layer that turns the completed transcript into typed comprehension, grammar, and vocabulary evaluations.

The notes are written in the same spirit as the SlotSense docs: explain what exists in the repository, where the boundaries are, and which decisions made the system easier to reason about.

## Document Guide

### [01-architecture-overview.md](01-architecture-overview.md)

High-level component view of the LiveKit worker, frontend event path, transcript persistence, and BAML scoring layer.

**Best for:** First-pass system orientation.

### [02-livekit-conversation-flow.md](02-livekit-conversation-flow.md)

Detailed runtime path through room startup, voice pipeline setup, task progression, frontend text-stream events, transcript capture, backend persistence, and room cleanup.

**Best for:** Following one learner session through the system.

### [03-baml-assessment-engines.md](03-baml-assessment-engines.md)

How BAML is used to define typed assessment outputs for comprehension, grammar, and vocabulary, including suppression rules and scoring decisions.

**Best for:** Explaining structured LLM evaluation rather than free-form grading.

### [04-state-machine-and-decisions.md](04-state-machine-and-decisions.md)

The state-machine shape hidden inside the LiveKit tasks and frontend triggers, plus the key architectural decisions visible in the repo.

**Best for:** Interview-style explanation of engineering judgment.

## Verified Vocabulary

### Assessment task

A bounded LiveKit `AgentTask` that owns one phase of the conversation. The implemented tasks are `intro`, `history`, and `purpose`.

### Frontend gate

The frontend sends a `start_next_task` message on the `gate.server` topic. The worker converts that into an `asyncio.Event`, which lets the next task begin.

### Transcript event

The runtime transcript mixes spoken conversation entries with system events such as `session_started`, `task_complete`, `assessment_completed`, `agent_hung_up`, and `session_ended`.

### BAML engine

A typed evaluator function such as `EvaluateTranscriptComprehension`, `EvaluateTranscriptGrammar`, or `EvaluateTranscriptVocabulary`. Each function has a schema, a prompt, a model client, and test cases.

### Suppression rule

A guard that prevents one assessment engine from scoring the wrong thing. For example, grammar and vocabulary are suppressed when comprehension is C03 or C04.

## Evidence Boundary

The repository supports claims about:

- LiveKit Agents running a voice pipeline with STT, LLM, TTS, VAD, turn detection, and noise cancellation;
- frontend progress events sent over LiveKit text streams;
- frontend-controlled progression between later assessment tasks;
- local transcript files and backend persistence to `PUT /assessment/{session_id}`;
- BAML schemas and prompts for comprehension, grammar, and vocabulary evaluation;
- generated TypeScript BAML clients.

The repository does not show a complete production backend implementation, a frontend implementation, a deployed evaluation runner that invokes the generated BAML client after each session, or a database schema for assessment results. Those may exist elsewhere, but they are not present in this inspected tree.

## Repository Evidence

The principal code root used by these documents is:

```text
/Users/sandipan/projects/audio-project/GATE_brain
```

Key files inspected:

```text
agent-gate/conversation_flow.py
agent-gate/pyproject.toml
agent-gate/livekit.toml
agent-gate/Dockerfile
agent-gate/conversation_report_*.json
assessment/baml_src/*.baml
assessment/*_engine.md
assessment_prompts/assessment_phase_1.md
assessment_prompts/assessment_phase_2.md
```

