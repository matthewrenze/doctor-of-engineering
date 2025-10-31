# Previous-k States

An experiment to determine the optimal number of previous states (k) for an observing agent

# Treatments
- v0 - agent has access to all previous states
- v1 - agent has access to only the current state
- v2 - agent has access to only the last 2 states
- vn - agent has access to only the last n states

# Results
- Accuracy (task completion rate) remains similar for all agents (between 79% and 86%)
- Avg steps per task goes up from 14 to 18 from v0 to v1 and then gradually decreases to 13 by v8 and remains to v10
- Avg tokens per task drops significantly (122k -> 76k) from v0 to v1 and remains between 51k to 74k to v9
  - However, v10 has an anomaly tokens generated jumps up to 141k (not sure why)
- Avg reward per task for v0 is 0.93, then drops to 0.82 for v1, then gradually increase to 0.93 by v10
- Avg reward per token increases significantly from v0 at 0.8 (1e-5) to 1.1 (1e-5) for v1
  - Avg reward per token ranges between 1.1 and 1.7 (1e-5) from v1 to v9
  - However, it drops to 0.7 for v10 due to an anomaly 
  - Peak is at v5 at 1.7 (1e-5)

# Notes:
- I only evaluated at n=100 (10 tasks per eval) so I don't have a clean signal to make definitive decisions
- I should re-run at n=1,000, however, it will take multiple days and cost approximately $700
- However, in the meantime, k=5 appears to be the optimal trade-off -- based on these preliminary results

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


 
