# JSON Agent

An experiment to determine the effectiveness of a JSON agent vs a plain-text agent

# Treatments
- v0 - Text agent - uses YAML-like plain text for all I/O
- v1 - JSON agent - uses JSON-formatted text for all I/O

# Results
- Both agents have similar performance at 54% (text) and 52% (JSON) accuracy
- In addition, both agents take similar number of steps to complete tasks (1.8k for text vs. 1.9k for JSON)
- However, number of tokens used differed significantly (1.56M for text vs. 2.90M for JSON)

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


 
