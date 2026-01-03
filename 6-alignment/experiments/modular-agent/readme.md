# Modular Agent
An experiment to determine how modular decomposition impacts the agent's performance.

# Treatments
- baseline - a monolithic react agent with both thought and action in the same sub-step 
- modular-v1 - a modular react agent with thought and action as separate sub-steps
- modular-v2 - a modular react agent using "we" for the system and "you" for the module
- modular-v3 - a modular react agent using "we" in the example for the chain-of-thought

# Results
- For accuracy, 
  - v2 performs best (76%) compared to baseline (68%)
  - actor-only performs worst (64%) as expected
  - both v1 and v3 perform the roughly the same (71%)
- For average steps per task,
 - all performed the same as baseline (31-32) except actor-only (34)
- For average tokens per task,
 - baseline (89k) > actor-only (96k) > v1 (197k) > v2 (198k) > v3 (207k)

# Notes
- v1 didn't perform as well as I had expected and the pronoun usage in the system prompt felt weird
 - so I took a gamble and created v2 (against the advice of ChatGPT)
- v2 is essentially: "we" the multi-agent system and "you" the sub-agent module
 - The agent responds with "I" in chain of thought though
 - So, I created v3 to change the CoT examples to use "we" instead
- v3 tends to drop the pronoun from the beginning of the CoT in it's output
 - It appears to be confused about which pronoun to use, so it doesn't use any
 - Not sure if this is why performance drops, but it's interesting

## Resources
- [Code (Baseline)](baseline/) - the source code for the baseline agent
- [Code (Modular-v1)](modular-v1/) - the source code for the modular agent v1
- [Code (Modular-v2)](modular-v1/) - the source code for the modular agent v2
- [Code (Modular-v3)](modular-v1/) - the source code for the modular agent v3
- [Analysis](analysis/) - the source code for the analysis
- [Evals](data/evals/) - the eval sets
- [Results](data/results/) - the results of each eval run
- [Summaries](data/summaries.csv) - the summaries of the evals
- [Plots](data/plots/) - the data visualizations of the results

*Note: cache, logs, messages, and workspaces have been excluded for size*

## Sources
- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)
- [TextWorld: A Learning Environment for Text-based Games](https://arxiv.org/abs/1806.11532)


 
