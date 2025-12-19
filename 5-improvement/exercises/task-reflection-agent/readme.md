# Task-Reflection Agent
An exercise to create an LLM agent that reflects on it's own prior trajectory in a task to identify mistakes in reasoning or actions

# Treatments
- reflect-v2 - a task-reflection agent instructed to reflect on it's failure first before providing advice
- reflect-v3a - a task-reflection agent where all reflections in each eval from v2 are merged (line-by-line)
- reflect-v3b - a task-reflection agent where all reflections in each eval from v2 are merged by GPT
- reflect-v3c - a task-reflection agent where all reflections across all evals are merged by GPT

# Results (GPT-5.2)
- For accuracy:
  - reflect-v2-test (65%) outperformed v2-train (60%) indicating v2 was learning
  - reflect-v3b-test (67%) > v3c (66%) > v3a (63%) indicating that more reflection info helped
- For reward:
  - reflect-v2-test (0.75) outperformed v2-train (0.69) indicating v2 was learning
  - reflect-v3b-test (0.76) > v3c (0.74) > (0.73) indicating v3 only helped slightly compared to v2
- For avg steps:
  - reflect-v2-test (30) and train (30) were similar
  - reflect-v3a,b,c (32) were all similar but higher than v2
- For avg tokens:
  - reflect-v2-test (100k) was more than v2-train (95k)
  - reflect-v3-test (108k) was better than v3a (113k) which was better than v3c (122)
- Overall, reflect v3b performed best by multiple measures

# Results (GPT-4.1-mini)
- For accuracy, 
  - baseline-10 is 45%
  - reflect-v1-test (42%) perform worse than reflect-v1-train (46%)
  - reflect-v2-test (46%) outperforms reflect-v2-train (44%)
  - reflect-v3a-test (43%), reflect-v3b-test (43%), and reflect-v3c-test (41%) all perform worse than their source reflect-v2-train (46%)
- For reward,
  - baseline-10 is 0.56
  - reflect-v1-test (0.53) performs worse than reflect-v1-train (0.58)
  - reflect-v2-test (0.56) performs the same as reflect-v2-train (0.56)
  - reflect-v3a-test (0.52), reflect-v3b-test (0.54), and reflect-v3c-test (0.53) all performed worse than their source reflect-v2-train (0.56)
- For avg steps,
  - baseline-10 is 34
  - reflect-v1-test (33) is similar to reflect-v1-train (33)
  - reflect-v2-test (33) is similar to reflect-v2-train (34)
  - reflect-v3a-test (34), v3b-test (33), and v3c-test (32) are similar to their source reflect-v2-train (34)
- For avg tokens,
 - baseline is 98k
 - reflect-v1-test (112k) is worse than reflect-v1-train (102k)
 - reflect-v2-test (109k) is worse than reflect-v2-test (105)
 - reflect-v3a-test (120k), reflect-v3b-test (110k), and reflect-v3c-test (121k) are all worse

# Notes
- The first iteration performed poorly so I removed generalization instructions and re-ran v2 and v3 
- reflect-v1 didn't reflect on why it failed the task, so I create v2 to explicitly reflect on the failure step
- reflect-v2 still didn't produce a significant improvement in performance, so I created v3a, v3b, and v3c
- reflect-v3 (a, b, c) all performed worse than v2
- So, I tried again with GPT-5.2 and finally saw positive results

## Resources
- [Code](reflect-v1/) - the source code for the v1 agent
- [Code](reflect-v2/) - the source code for the v2 agent
- [Code](reflect-v3/) - the source code for the v3 agent
- [Analysis](analysis/) - the source code for the analysis
- [Evals](data/evals/) - the eval sets
- [Results](data/results/) - the results of each eval run
- [Summaries](data/summaries.csv) - the summaries of the evals
- [Plots](data/plots/) - the data visualizations of the results

*Note: cache, logs, messages, and workspaces have been excluded for size*

## Sources
- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)
- [TextWorld: A Learning Environment for Text-based Games](https://arxiv.org/abs/1806.11532)


 
