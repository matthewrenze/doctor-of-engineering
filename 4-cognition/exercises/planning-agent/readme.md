# Planning Agent

An exercise to implement an agent that can create and execute a plan

# Treatments
- v0-baseline - agent has no planning capabilities
- v1-simple - agent completely (re-)writes it's plan every step
- v2-stateful - agent stores plan in state and modifies the plan only as needed
- v3-tool - agent uses a plan tool to create, update, check, and uncheck the plan
- v4-subagent - agent delegates plan creation and maintenance to a subagent

# Results
- [FINISH]

## v0 Resources
- [v0-Baseline Code](v0-baseline/) - the source code for the agent
- [Analysis Code](analysis/) - the source code for the final analysis
- [Evals](data/evals/) - the eval sets
- [Results](data/results/) - the results of each eval run
- [Summaries](data/summaries.csv) - the summaries of the evals
- [Plots](data/plots/) - the data visualizations of the results

*Note: cache, logs, messages, and workspaces have been excluded for size*

## Sources
- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)
- [TextWorld: A Learning Environment for Text-based Games](https://arxiv.org/abs/1806.11532)


 
