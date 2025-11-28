# Optimize Truncate
An experiment to optimize an agent that truncates it's context after k previous steps

# Treatments
- baseline - an agent with all full state-action history
- summary-k(n) - an agent with k(n) steps of state-action history and a summary of all previous steps
- truncate-k(n) - an agent with full k(n) steps of state/action history but all other are truncated

# Results
- Accuracy and reward increase from k=0 to k=5 and then level off out to k=10 
  - Accuracy at k=5 is 46% compared to baseline of 48%
  - Avg reward at k=5 is 0.57 compared to baseline of 0.58
- Average steps decreases fro k=0 to k=5 and levels off out to k=10
  - Avg steps at k=5 is 30 steps compared to baseline of 30 steps
- Optimal reward per M tokens is k=5 (7.15) vs baseline (2.73)
- Truncating at k=5 is optimal

## Resources
- [Code](code/) - the source code for the baseline (react) agent
- [Analysis](analysis/) - the source code for the data analysis
- [Evals](data/evals/) - the eval sets
- [Results](data/results/) - the results of each eval run
- [Summaries](data/summaries.csv) - the summaries of the evals
- [Plots](data/plots/) - the data visualizations of the results

*Note: cache, logs, messages, and workspaces have been excluded for size*

## Sources
- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)
- [TextWorld: A Learning Environment for Text-based Games](https://arxiv.org/abs/1806.11532)


 
