# Top-k Search Results

An experiment to determine the optimal top-k search results for simple single-hop Q&A problems.

## Results
- Accuracy gradually increases as top-k increases leveling out around k=7
- Token efficiency peaks around k=4 and gradually decreases
- Step efficiency grows rapidly and until k=5 then gradually to k=10
- k=5 seems to be a good starting point for most cases

## Resources
- [Code](code/) - the source code for the agent
- [Evals](data/evals/) - the eval sets
- [Results](data/results/) - the results of each eval run
- [Summaries](data/summaries.csv) - the summaries of the evals
- [Plots](data/plots/) - the data visualizations of the results

*Note: cache, logs, messages, and workspaces have been excluded for size*

## Sources
- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)
- [SimpleQA: Measuring short-form factuality in large language models](https://arxiv.org/abs/2411.04368)



 
