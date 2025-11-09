# Oracle Agent
An experiment to compare the baseline (react) agent to an oracle agent

# Treatments
- v0-baseline - a standard react agent
- v99-oracle - an agent that executes the optimal solution

# Results
- Oracle agent performs at 100% accuracy and 1.0 reward per task (as expected)

# Notes
- Need a more effective way to load solutions into the oracle agent
  - Currently using an if statement in run_eval.py to call set_solution() on oracle
- Can't count tokens as-is but I could use a tokenizer like tiktoken


## Resources
- [v0-Baseline Code](v0-baseline/) - the source code for the baseline (react) agent
- [v99-Oracle Code](v9-oracle/) - the source code for the oracle agent
- [Analysis Code](analysis/) - the source code for the final analysis
- [Evals](data/evals/) - the eval sets
- [Results](data/results/) - the results of each eval run
- [Summaries](data/summaries.csv) - the summaries of the evals
- [Plots](data/plots/) - the data visualizations of the results

*Note: cache, logs, messages, and workspaces have been excluded for size*

## Sources
- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)
- [TextWorld: A Learning Environment for Text-based Games](https://arxiv.org/abs/1806.11532)


 
