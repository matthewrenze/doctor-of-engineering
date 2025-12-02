# Summary Agent
An exercise to create an agent that summarizes it's previous action-state pairs for memory efficiency

# Treatments
- baseline - a standard react agent with full action-state history
- summary-k(n) - an agent with full k(n) action-state pairs but all others are summarized
- truncate-k(n) - an agent with full k(n) action-state pairs but all other are truncated

# Results
- baseline agent outperformed all summarize and truncate agents on accuracy (48%) and reward (0.58)
 - For the truncate and summarize  agents, accuracy and reward increased with k 
   - truncate-10 (46% and 0.57) > truncate-5 (46% and 0.57) > truncate 1 (36% and 0.46)
   - summary-10 (47% and 0.56) > summary-5 (46% and 0.55) > summary-1 (43% and 0.50)
   - Performance increased to 5 and leveled off
- All agents performed similar for avg steps per task (29 to 31)
  - Except for truncate-1 at 36 steps per task
- Baseline performed worst for avg tokens per task (213k)
  - truncate-1 (66k) > truncate-5 (79k) > truncate-10 (100k)
  - summary-1 (82k) > summary-5 (96k) > summary-10 (115k)
- Optimal agent is summary-5 

# Notes
- In this experiment, I had k=1 mean that only the current state is visible
  - However, in future experiments, k=1 means that current state and 1 previous state-action is available

## Resources
- [Baseline Agent Code](baseline/) - the source code for the baseline (react) agent
- [Summary Agent Code](summary/) - the source code for the summary agent
- [Analysis Code](analysis/) - the source code for the final analysis
- [Evals](data/evals/) - the eval sets
- [Results](data/results/) - the results of each eval run
- [Summaries](data/summaries.csv) - the summaries of the evals
- [Plots](data/plots/) - the data visualizations of the results

*Note: cache, logs, messages, and workspaces have been excluded for size*

## Sources
- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)
- [TextWorld: A Learning Environment for Text-based Games](https://arxiv.org/abs/1806.11532)


 
