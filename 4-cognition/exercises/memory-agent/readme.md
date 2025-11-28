# Memory Agent
An exercise to create an LLM agent that stores persistent memories across truncated steps in a task

# Treatments
- baseline-10 - a standard react agent that truncates after 5 steps (10 evals x 10 tasks = 100 episodes)
- memory-v1 - a react agent with persistent memory
- memory-v2 - memory-v1 instructed to only remove memories if its certain they are no longer relevant

# Results
- All three agents performed similarly in terms of accuracy (41%-43%) and reward (0.53-0.55)
  - memory-v1 (43% and 0.55) slightly outperformed baseline (41% and 0.53) and memory-v2 (42% and 0.54)
- Baseline used fewer tokens (90k) than memory-v1 (115k) and memory-v2 (142k)


# Notes
- I modified the baseline agent in this experiment to incorporate the k=5 truncation
  - I also updated the system prompt and examples to reflect the new state->action format.
  - You can find the baseline-old, baseline-new, and baseline-10 (10 tasks per eval) in the data folder
- Memory v1 continuously rewrites memories and drops relevant memories
- Memory v2 records previous steps on coin tasks (good) but it doesn't help to improve score much.


## Resources
- [Code](code/) - the source code for the agent
- [Analysis](analysis/) - the source code for the analysis
- [Evals](data/evals/) - the eval sets
- [Results](data/results/) - the results of each eval run
- [Summaries](data/summaries.csv) - the summaries of the evals
- [Plots](data/plots/) - the data visualizations of the results

*Note: cache, logs, messages, and workspaces have been excluded for size*

## Sources
- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)
- [TextWorld: A Learning Environment for Text-based Games](https://arxiv.org/abs/1806.11532)


 
