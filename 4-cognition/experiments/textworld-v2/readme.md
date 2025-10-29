# TextWorld v2

An experiment to design a incremental-learning curriculum for LLM agents using the TextWorld environment

# Treatments
- v0 - previous agent with feedback-only state information
- v1 - new agent with full state information after each step

# Results
- [FINISH]

# Curriculum
- Simple 
  - Task: find and cook an item in a 6-room house
  - Parameters:
    - goal verbosity
      - detailed - provides a predefined path to the object
      - brief - provides the name of the object
      - None - need to read note in kitchen for name / preparation of object
    - reward density = [dense, balanced, sparse]
  - Levels 1 - 9 sublevels of decreasing goal verbosity and reward density

- Coin 
  - Task: follow a pre-defined path to pick up a coin
  - Levels: 
    - Level 1 - task length / rooms range from 1-100 [10 sublevels]
    - Level 2 - task length 1-100, adds 1x distractor rooms [10 sublevels]
    - Level 3 - task length 1-100, adds 2x distractor rooms [10 sublevels]

- Treasure 
  - Task: Follow a pre-defined path and pick up the specified item but not any other objects
  - Levels:
    - Level 1 - task length 1-10, 5 rooms, all rooms empty except two objects [10 sublevels]
    - Level 2 - task length 2-10, closed doors and objects in containers [10 sublevels]
    - Level 3 - task length 3-20, locked doors and containers [10 sublevels]

- Cooking
 - Task: prepare a meal using n ingredients with take, cut, cook, and drop skills
 - Levels:
   - Level 1 - one room, one ingredient, increasing skills [8 sublevels]
   - Level 2 - one room, two to five ingredients, all skills [18 sublevels]
   - Level 3 - 6, 9, and 12 rooms, five ingredients, all skills [15 sublevels]

# Notes
- Simple, coin, and treasure do not contain a location in their infos:
  - However, it can be pulled from description via regex of "-= Location =-"
- For the coin game, having the same random seed with different difficulty settings produces the same chain of rooms and solution path but different distractor rooms (attached to the main chain)
- Coin and treasure tell you where to find the items; simple and cooking do not.
- Treasure game level 3 tasks 90-100 take a long time to run 
  - I had to create a hack that allows me to create them separately and merge them manually
- Coin game level 2 task 100 only has a task length of 3 but all others in the same sublevel are 10. Not sure why.



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


 
