# Module 1 - Foundations of AI Agents (July)

## Goals
- Review foundational literature on LLM/LMM agents
- Review literature on uncertainty quantification in LLMs
- Review empirical research methods for computer science

## Course Reviews
- Lecture slides for [CSC 2130 - Empirical Research Methods for Computer Scientists](https://www.cs.toronto.edu/~sme/CSC2130/)
- Lecture slides for [COSC 6321 - Research Methods in Computer Science](https://www2.cs.uh.edu/~gnawali/courses/cosc6321-f21/index.html)

## Readings
- [The Rise and Potential of LLM Based Agents: A Survey (Xi 2023)](https://arxiv.org/abs/2309.07864)
- [LLM Agent: A Survey on Methodology, Applications and Challenges (Luo 2025)](https://arxiv.org/abs/2503.21460)  
- [Agent Design Patterns (Liu 2024)](https://arxiv.org/abs/2405.10467)  
- [Large Language Model-Based Agents for Software Engineering: A Survey (Liu 2025)](https://arxiv.org/abs/2409.02977)
- [A Practice Guide to Building Agents (OpenAI 2025)](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf)
- [Agent Companion Whitepaper (Google 2025)](https://www.kaggle.com/whitepaper-agent-companion)
- [Building Effective Agents (Anthropic 2024)](https://www.anthropic.com/engineering/building-effective-agents)
- [Prompting Guide 101 (Google 2024)](https://services.google.com/fh/files/misc/gemini-for-google-workspace-prompting-guide-101.pdf)
- [The Prompt Report: A Systematic Survey of Prompting Techniques (Schulhoff 2025)](https://arxiv.org/abs/2406.06608)

## Summaries
Paper summaries can be found in the [summaries folder](summaries/).

## Notes
 - [Uncertainty Quantification in LLMs](https://github.com/matthewrenze/doctor-of-engineering/tree/main/1-foundations/notes/calibrating-uncertainty-in-llms.md)
 - [Cailbrating Uncertainty in LLMs](https://github.com/matthewrenze/doctor-of-engineering/tree/main/1-foundations/notes/calibrating-uncertainty-in-llms.md)

## Prototypes
 - [ask_confidence](https://github.com/matthewrenze/doctor-of-engineering/tree/main/1-foundations/prototypes/ask_confidence) - asks the LLM to predict its confidence for each answer option
 - [ensemble_analysis](https://github.com/matthewrenze/doctor-of-engineering/tree/main/1-foundations/prototypes/ensemble_analysis) - an analysis my previous LLM temperature data for ensemble answer disagreement at various temperatures
 - [get_ensemble](https://github.com/matthewrenze/doctor-of-engineering/tree/main/1-foundations/prototypes/get_ensemble) - gets the answer agreement (certianty) of LLM by answering 10 times with temp 0.7
 - [get_log_probs](https://github.com/matthewrenze/doctor-of-engineering/tree/main/1-foundations/prototypes/get_log_probs) - gets the log probablity of an LLMs answer to a multiple-choice question
 - [reasoning_tokens](https://github.com/matthewrenze/doctor-of-engineering/tree/main/1-foundations/prototypes/reasoning_tokens) - gets the number of reasoning tokens for reasoning models like o3
 - [responses_api](https://github.com/matthewrenze/doctor-of-engineering/tree/main/1-foundations/prototypes/responses_api) - compares OpenAI's chat completions API with the new responses API

 ## Exercises
- Create a simple [ReAct](https://arxiv.org/abs/2210.03629) agent  
  - 1A - [Simple ReAct agent](exercises/react_simple/)
  - 1B - [Improved ReAct agent](exercises/react_improved/)
- Summarize best practices
  - 2A - [Prompt Engineering Best Practices](exercises/best_practices/prompt-engineering-best-practices.md)
  - 2B - [LLM Agent Best Practices](exercises/best_practices/llm-agent-best-practices.md)
  - 3C - [LLM Agent Design Patterns](exercises/best_practices/llm-agent-design-patterns.md)



