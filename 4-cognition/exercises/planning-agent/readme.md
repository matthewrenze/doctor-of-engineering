# Planning Agent

An exercise to implement an agent that can create and execute a plan

# Treatments
- v0-baseline - agent has no planning capabilities
- v1-simple - agent completely (re-)writes it's plan every step
- v2-stateful - agent stores plan in state and modifies the plan only as needed [TO-DO]
- v3-tool - agent uses a planning tool to create, update, check, and uncheck the plan [TO-DO]
- v4-subagent - agent delegates plan creation and maintenance to a subagent [TO-DO]

# Results
- Accuracy and reward per task were similar for both baseline (non-planning) and simple planning agents
- Steps per task remained similar as well
- However, token usage per task almost doubled
- Accuracy and reward per task did improve significantly on coin-1, -2, and -3
  - So, there appears to be some benefit on specific types of tasks

# Notes
- Agents continue to struggle on all tasks with task-length greater than 20
  - This long-task decoherence is experienced with or without planning
  - However, all three coin games experienced a benefit of further steps without decoherence
- Agents give up on planning after a given number of steps (not sure why or when this happens)
  - They just stop outputting a plan in their response

## v0 Resources
- [v0-Baseline Code](v0-baseline/) - the source code for the baseline (non-planning) agent
- [v1-Simple Code](v0-simple/) - the source code for the simple planning agent
- [Analysis Code](analysis/) - the source code for the final analysis
- [Evals](data/evals/) - the eval sets
- [Results](data/results/) - the results of each eval run
- [Summaries](data/summaries.csv) - the summaries of the evals
- [Plots](data/plots/) - the data visualizations of the results

*Note: cache, logs, messages, and workspaces have been excluded for size*

## Sources
- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)
- [TextWorld: A Learning Environment for Text-based Games](https://arxiv.org/abs/1806.11532)


 
