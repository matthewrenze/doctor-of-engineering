# Modular Agent
An experiment to determine how modular decomposition impacts the agent's performance.

# Treatments
- baseline - a monolithic react agent with both thought and action in the same sub-step 
- modular-v1 - a modular react agent with thought and action as separate sub-steps

# Results

# Notes

## Resources
- [Code (Baseline)](baseline/) - the source code for the baseline agent
- [Code (Modular-v1)](modular-v1/) - the source code for the modular agent
- [Analysis](analysis/) - the source code for the analysis
- [Evals](data/evals/) - the eval sets
- [Results](data/results/) - the results of each eval run
- [Summaries](data/summaries.csv) - the summaries of the evals
- [Plots](data/plots/) - the data visualizations of the results

*Note: cache, logs, messages, and workspaces have been excluded for size*

## Sources
- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)
- [TextWorld: A Learning Environment for Text-based Games](https://arxiv.org/abs/1806.11532)


 
