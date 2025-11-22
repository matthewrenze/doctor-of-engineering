# Top Agentic Models
An experiment to compare the (current) top agentic models to the baseline (i.e., GPT-4.1-mini)

# Treatments
- gpt-4-1-mini - a standard react agent using OpenAI's GPT-4.1-mini (baseline)
- gpt-5-1 - a standard react agent using OpenAI's GPT 5.1
- claude-sonnet-4-5 - a standard react agent using Anthropic's Claude Sonnet 4.5
- gemini-3-pro-preview - a standard react agent using Google's Gemini 3 Pro (Preview)

# Results
 - Gemini 3 Pro outperformed all models on accuracy and reward per task
  - Accuracy: Gemini 3 Pro (83%) > Claude Sonnet 4.5 (78%) > GPT 5.1 (48%) > GPT 4.1 mini (39%)
  - Reward: Gemini 3 Pro (0.91) > Claude Sonnet 4.5 (0.83) > GPT 5.1 (0.61) > GPT 4.1 mini (0.53)
- All agents were similar on steps-per-task (30-33) and tokens per task (between 206k and 286k)
  - GPT-5.1 had least steps and tokens per task (30 steps and 206k tokens)

# Notes
- Gemini-3 Pro Preview is currently rate limited to 1,000 requests per day (major bottleneck)
- Due to rate limits, time, and cost I only ran 10 tasks from each of 4 evals (total of 40 tasks)
  - Evals were simple, coin-3, treasure-3, and cooking-3
- Gemini-3 was able to successfully perform tasks up to 100 steps on coin-3 eval
  - It would have had 100% accuracy but it made a single-step error that caused it to hit 101 steps
  - It only made minor single-step mistakes in coin task 90 and 100 that it was able to correct
  - All other coin tasks were performed perfectly (optimal # of solution steps)  
- Surprisingly, the only tasks where the top models didn't outperform baseline was the Simple game eval
  - The agents appeared to "overthink" the problems it encounters (e.g. not sure if "cook" means "fry")

## Resources
- [Code](code/) - the source code for the agent
- [Analysis](analysis/) - the source code for the analysis
- [Evals](data/evals/) - the eval sets
- [Results](data/results/) - the results of each eval run
- [Summaries](data/summaries.csv) - the summaries of the evals
- [Plots](data/plots/) - the data visualizations of the results

*Note: cache, logs, messages, and workspaces have been excluded for size*

## Sources
- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)
- [TextWorld: A Learning Environment for Text-based Games](https://arxiv.org/abs/1806.11532)


 
