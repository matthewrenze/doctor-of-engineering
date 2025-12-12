# Step-Reflection Agent
An exercise to create an LLM agent that reflects on it's own prior chain-of-thought and action to identify mistakes in reasoning

# Treatments
- baseline-10 - a standard react agent that truncates after 5 steps (10 evals x 10 tasks = 100 episodes)
- reflection-v1 - a react agent with with step-reflection capabilities
- reflection-v2 - step-reflection agent with prompt improvements suggested by ChatGPT (5.1)

# Results
- For accuracy, reflection-v1 (45%) only slightly outperforms baseline-10 (44%) and reflection-v2 (44%)
- For reward, reflection-v1 (0.56) slightly outperforms baseline-10 (0.55) and reflection-v2 (0.54)
- For avg steps, reflection-v1 (33) is slightly worse than baseline-10 (32) and reflection-v2 (32)
- For avg tokens, baseline-10 (93k) outperforms reflection-v1 (105k) and reflection-v2 (110k)

# Notes
- I was surprised that reflection-v1 didn't offer more performance improvements
  - so I have ChatGPT review the v1 system prompt; reflection-v2 was based on it's suggestions

## Resources
- [Code](reflection/) - the source code for the agent
- [Analysis](analysis/) - the source code for the analysis
- [Evals](data/evals/) - the eval sets
- [Results](data/results/) - the results of each eval run
- [Summaries](data/summaries.csv) - the summaries of the evals
- [Plots](data/plots/) - the data visualizations of the results

*Note: cache, logs, messages, and workspaces have been excluded for size*

## Sources
- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)
- [TextWorld: A Learning Environment for Text-based Games](https://arxiv.org/abs/1806.11532)


 
