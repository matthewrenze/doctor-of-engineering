# Exercise 1A: Simple ReAct Agent

A simple [ReAct](https://arxiv.org/abs/2210.03629) agent evaluated on the [HotpotQA](https://hotpotqa.github.io/) benchmark using [GPT-4.1-mini]().

## Resources
- [Code](code/) - the source code for the agent
- [Evals](data/evals/) - the HotpotQA eval set
- [Results](data/results/) - the eval results

## Notes
 - Sentence-level parsing is very fragile  
   - it breaks mid-sentence (e.g. ... U.S. <break> president)  
   - it doesn't break on references (e.g., ... [1][2]) 
 - Agent often appends additional search terms after entity name 
   - (e.g., "Search[Alicia Ramsey's plays]")
   - I'm not sure if it's biased by Google-style search query format or the Lookup query format
 - Agent often outputs multiple thoughts and actions in a single response 
   - (e.g. Thought 1: ... Action 1: ... Thought 2: ... Action 2: ...)
 - Agent often hallucinates search results (containing correct answers)
   - These take the form "(Result 1 / 1) Emilia Clarke's body double ..." 
 - Agent often doesn't use the similar wikipedia entities provided on search misses
 - Agent sometimes selects "Action (n): Finish" with no brackets or arguments
 - Existing code requires exact text match -- need to use LLM as a Judge pattern
 - Agent doesn't correctly generate action responses in the correct format which causes a regex parsing error
 - Agent often excludes ending bracket in actions (e.g. "Action 3: Finish[Answer")
 - Max tokens limit of 100 (in original ReAct agent) significantly harms performance

 ## To Do
  1. Cache wikipedia pages
  2. Add method to track experiments
  3. Remove max token limit
  4. Add LLM as a Judge
  5. Strip out excess whitespace from observations
  6. Loosen Action pattern-match format ("Action:" vs "Action (n):)

 ## Sources
 - [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)
 - [ReAct (Code)](https://github.com/ysymyth/ReAct:)
 - [HotpotQA: A Dataset for Diverse, Explainable Multi-hop Question Answering](https://arxiv.org/abs/1809.09600)
 - [HotpotQA (Code)](https://hotpotqa.github.io/)
 - [Hello GPT-4o](https://openai.com/index/hello-gpt-4o/)
 
