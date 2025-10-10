# Agent Tool Use

An evaluation framework for agent tool use.

# Treatments
- v0 - react agent with no tools  
- v1 - react agent with 10 tools  

# Results
- Agent with tools (54% accuracy) outperforms agent without tools (32% accuracy).  
- Token usage for tool-use agent went up from 105k to 1.5M (10x increase)  
- Largest performance gains were in SimpleQA and GAIA (as expected)  

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


 
