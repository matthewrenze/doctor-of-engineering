# Observation Agent

An agent that uses observations of state for memory management

# Treatments
- v0 - agent without observation capabilities
- v1 - agent with observation capabilities  

# Results
First run:
- Accuracy: Agent with observation (v1) performs worse (44%) than without observation (57%)
- Steps: Agent with observations requires more steps (18k) than non-observing agent (12k)
- Tokens: Agent with observations generates more tokens (5.7M) than non-observing agent (4.7M)
- Note: Primary source of errors was unproductive loops from "take <object> from floor" error and "quit"+"yes" error
        So, I fixed the two issues and re-ran the experiments <results below>

Second run:
- Accuracy: Agent with observation (v1) performs better (0.60) than without observation (0.58)
- Steps: Agent with observation requires more steps (12k) than without observations (11k)
- Tokens: Agent with observation generates fewer tokens (3.3M) than without observation (3.8M)
- Note: tw-cooking is the only eval where agent with observation performs significantly worse on accuracy, steps, and tokens

# Notes
 - There were several issues with unproductive loops in textworld
 - I should try an experiment with with top-k recent state

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


 
