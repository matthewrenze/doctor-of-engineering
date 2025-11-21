# GPT-4.1-mini vs GPT-5-mini
An experiment to compare GPT-4.1-mini to GPT-4-mini on performance and cost.

# Treatments
- gpt-4.1-mini - a standard react agent using the GPT-4.1-mini model
- gpt-5-mini - a standard react agent using the GPT-5-mini model

# Results
- gpt-5-mini outperforms gpt-4.1-mini on accuracy (61% vs. 48%) and reward per task (0.66 vs 0.58)
- gpt-5-mini uses more avg tokens per task than gpt-4.1-mini (250k vs 213k)
- Both models have similar avg steps per task (30 vs 31)

# Notes
- The largest accuracy and reward improvements are for cooking tasks
  - cooking 2 (85% vs 22% accuracy) (0.91 vs 0.59)
  - cooking 3 (53% vs 2% accuracy) and (0.74 vs 0.37)
- GPT-4-mini failures involve:
  - Incorrectly cooking items (e.g., frying instead of roasting)
  - Getting stuck in unproductive navigation loops
  - Getting stuck in unproductive pickup/drop item loops
  - Failing to find all ingredients (e.g., in fridge or in garden)
  - Trying to prepare meal with items on counter instead of in inventory
- GPT-5-mini failures mostly involved:
  - Incorrectly cooking items and unproductive loops
  - It seems to be able to get itself unstuck from loops though

## Resources
- [Code](code/) - the source code for the baseline (react) agent
- [Analysis Code](analysis/) - the source code for the final analysis
- [Evals](data/evals/) - the eval sets
- [Results](data/results/) - the results of each eval run
- [Summaries](data/summaries.csv) - the summaries of the evals
- [Plots](data/plots/) - the data visualizations of the results

*Note: cache, logs, messages, and workspaces have been excluded for size*

## Sources
- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)
- [TextWorld: A Learning Environment for Text-based Games](https://arxiv.org/abs/1806.11532)


 
