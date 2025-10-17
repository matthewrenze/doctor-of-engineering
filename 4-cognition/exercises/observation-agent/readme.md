# Observation Agent

An agent that uses observations of state for memory management

# Treatments
- v0 - agent without observation capabilities
- v1 - agent with observation capabilities  

# Results
- Accuracy: Agent with observation (v1) performs worse (44%) than without observation (57%)
- Steps: Agent with observations takes more steps (18k) than non-observing agent (12k)
- Tokens: Agent with observations takes more tokens (5.7M) than non-observing agent (4.7M)

# Notes
 - There were several issues with unproductive loops in textworld
 - I should try an experiment with with top-k recent state

## Resources
- [Code](code/) - the source code for the agent
- [Evals](data/evals/) - the eval sets
- [Results](data/results/) - the results of each eval run
- [Summaries](data/summaries.csv) - the summaries of the evals
- [Plots](data/plots/) - the data visualizations of the results

*Note: cache, logs, messages, and workspaces have been excluded for size*

## Sources
- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)
- [GAIA: a Benchmark for General AI Assistants](https://arxiv.org/abs/2311.12983)
- [GPQA: A Graduate-Level Google-Proof Q&A Benchmark](https://arxiv.org/abs/2311.12022)
- [Humanity's Last Exam](https://arxiv.org/abs/2501.14249)
- [MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding Benchmark](https://arxiv.org/abs/2406.01574)
- [SimpleQA: Measuring short-form factuality in large language models](https://arxiv.org/abs/2411.04368)
- [TextWorld: A Learning Environment for Text-based Games](https://arxiv.org/abs/1806.11532)


 
