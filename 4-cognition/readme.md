# Module 4 - Cognitive Enhancements (Oct)

## Goals
- Learn how to create agents that can observe, plan, and remember

## Readings
- [Understanding the planning of LLM agents: A survey](https://arxiv.org/abs/2402.02716)
- [Measuring AI Ability to Complete Long Tasks](https://arxiv.org/pdf/2503.14499)
- [A Survey on Large Language Models for Automated Planning](https://arxiv.org/abs/2502.12435)
- [A Survey on the Memory Mechanism of Large Language Model based Agents](https://doi.org/10.48550/arXiv.2404.13501)
- [Agentic Retrieval-Augmented Generation: A Survey on Agentic RAG](https://arxiv.org/abs/2501.09136)
- [Episodic memory in AI agents poses risks that should be studied and mitigated](https://arxiv.org/abs/2501.11739)
- [RAG-MCP: Mitigating Prompt Bloat in LLM Tool Selection via RAG](https://arxiv.org/abs/2505.03275)
- [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366)

## Summaries
- Paper summaries can be found in the [summaries](summaries/) folder.

## Exercises
- Summarize the [best practices](exercises/best-practices/best-practices-for-cognitive-enhancements.md) for implementing cognititive enhancements
- Summarize the [benchmarks](exercises/best-practices/benchmarks-for-cognitive-enhancements.md) used for evaluating cognitive enhancements
- Create an [observation agent](exercises/observation-agent/)
- Create a [planning agent](exercises/planning-agent/)
- Create a [summary agent](exercises/summary-agent/)
- Create a [memory agent](exercises/memory-agent/)

## Experiments
- Compare [plain-text vs JSON agent](experiments/json-agent/)
- Compare [cooking curriculum A](experiments/tw-curriculum-a/) vs [cooking curriculum B](experiments/tw-curriculum-b/)
- Create a [new textworld curriculum](experiments/textworld-v2/) with a smooth learning curve for evaluating cognitive enhancements
- Optimize the number of accessible [previous k states](experiments/previous-k-states/) for an observation agent
- Create an [oracle agent](experiments/oracle-agent/)
- Optimize the number of [truncated steps](experiments/optimize-truncate/) (i.e., states-action pairs)
- Compare the current [top models](experiments/top-models/) to see if they solve long-horizon decoherence

