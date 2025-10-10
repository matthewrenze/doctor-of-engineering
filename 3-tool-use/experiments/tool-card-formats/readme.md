# Tool I/O Format Experiment

An experiment to determine the performance of plain-text vs JSON tool I/O format.

## Treatments
- v0 - just function signatures - no description, args, or returns
- v1 - function signatures and descriptions - no args or returns
- v2 - function signatures, args, returns, notes
- v3 - JSON formated version of v2

## Results
- Accuracy remains the same across treatments from v0 to v2.
  - v3 consistantly called tools incorrectly because it was biased towards JSON tool-call I/O format
- Number of tokens decreased from v0 to v2
- Number of steps decreased from v0 to v2 
  - Simpler tool cards made more step-wise errors and had to correct them

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


 
