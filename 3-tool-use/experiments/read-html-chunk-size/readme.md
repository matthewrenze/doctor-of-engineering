# Read HTML Chunk Size

An experiment to determine the optimal HTML page chunk size for answering simple single-hop Q&A problems.

## Results
- Accuracy grows rapdily from c=1-3 then gradually to k=15
- Token efficiency grows to c=9 and levels off
- Step efficiency grows to c=12 and levels off
- c=10 seems optimal for most cases (i.e., 10,000 token chunks)

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


 
