# TextWorld Curriculum (Version A)

An experiment to design a incremental-learning curriculum for LLM agents using the TextWorld environment

# Treatments

# Results
- [FINISH]

# Notes
- There are five random seeds (map, objects, quest, grammar, recipe)
  - All five need to be set to the same value to create a completely deterministic episode
  - Holding recipe_seed constant but varying all others creates random recipes
  - Varying recipe_seed but keeping all others constant creates random recipes
  - Setting options.seeds appears to override individual seeds and make them random
- Issue: When take=0 and recipe_seed != 0, then "Shuffle recipe requires the 'take' skill" (Assertion Error)
  - Solution is to set recipe_seed=0 when take=0
- Issue: When take=0, inventory contains distractor items
  - Solution: Set Drop=True for recipe=1, take=0



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


 
