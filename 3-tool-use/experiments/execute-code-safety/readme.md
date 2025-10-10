# Code Execution Safety Experiment

An experiment to determine what safety mechanisms to apply to the execute-code tool.

## Treatments
- v0 - no code execution capabilities (baseline)
- v1 - full code execution capabilities with no safety header
- v2 - disabled open(), exec(), eval() and importing os, subprocess, sys, socket, and shutil

## Results
- Both v1 and v2 perform equally well.
  - This is suprising to me since I've seen the agent struggle to solve problems because of limitations imposed by the safety header.
- I added v0 to see how much code execution contributed to total accuracy but it was essentially zero
  - v0 increased token count and step count, 
  - So, it seems that the LLM can solve problems without Python by takin more steps.
  - I will need to investigate further to find the answer


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


 
