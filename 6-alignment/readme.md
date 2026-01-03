# Module 6 - Alignment (Dec)

## Goals
- Learn how to align agents to human goals and values
- Learn how to measure uncertainty in agents and create agents that defer to humans

## Readings (to-do)
- [AI Alignment: A Comprehensive Survey](https://arxiv.org/abs/2310.19852)
- [Large Language Model Alignment: A Survey](https://arxiv.org/abs/2309.15025)
- [Safeguarding AI Agents: Developing and Analyzing Safety Architectures](https://arxiv.org/abs/2409.03793)
- [AgentHarm: A Benchmark for Measuring Harmfulness of LLM Agents](https://arxiv.org/abs/2410.09024)
- [A Survey on Uncertainty Quantification of Large Language Models](https://arxiv.org/abs/2412.05563)
- [SAUP: Situation Awareness Uncertainty Propagation on LLM Agent](https://arxiv.org/abs/2412.01033)
- [Uncertainty-Based Abstention in LLMs Improves Safety and Reduces Hallucinations](https://arxiv.org/abs/2404.10960)

## Summaries (to-do)
- Paper summaries can be found in the [summaries folder](summaries/).

## Exercises
- Summarize [best practices](exercises/best-practices/best-practices-for-alignment.md) for alignment
- Summarize the [benchmarks](exercises/best-practices/benchmarks-for-alignment.md) for alignment
- Summarize [best practices](exercises/best-practices/best-practices-for-uncertainty.md) for uncertainty
- Summarize the [benchmarks](exercises/best-practices/benchmarks-for-uncertainty.md) for uncertainty
- Create an agent that measures its own uncertainty
- Create an agent that learns to defer (L2D) unsafe tasks to humans

## Experiments
- Create a [modular agent](experiments/modular-agent/) by decomposing thoughts and actions

## Prototypes
- [token-level-uncertainty](prototypes/token-level-uncertainty/) - quick tests for estimating uncertainty using log probability, probability, entropy, and margin on a single token
- [sequence-level-uncertainty](prototypes/sequence-level-uncertainty/) - quick tests for estimating uncertainty using min probability, mean entropy, and min margin over a sequence of tokens
- [sample-based-uncertainty](prototypes/sample-based-uncertainty/) - quick tests for estimating uncertainty using self-consistency, centroid similarity, and pairwise similarity over multiple rollouts (samples)
- [distribution-based-uncertainty] - quick tests for estimating uncertainty using predictive entropy, expected entropy, and mutual information over a token distribution
- [verbalized-uncertainty](prototypes/verbalized-uncertainty/) - quick tests for estimating probability by asking the LLM for its confidence using qualitative and quantitative scales



