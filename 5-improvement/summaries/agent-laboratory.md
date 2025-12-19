# Agent Laboratory: Using LLM Agents as Research Assistants

## Framework Design Principles
- Structure agent workflows to mirror human research processes
- Decompose complex tasks into specialized agent roles
- Use role-specific prompts tailored to each research function
- Maintain modular agent components for reuse and replacement
- Insert explicit review and feedback checkpoints between stages

## Literature Review and Knowledge Acquisition
- Perform targeted literature search instead of broad retrieval
- Summarize papers into distilled, task-relevant insights
- Iteratively refine literature focus using higher-level agent feedback
- Preserve citations and context for downstream experiment design

## Experiment Design and Execution
- Translate literature insights directly into executable experiments
- Start with simple baseline experiments before scaling complexity
- Reuse prior experiment results as context for follow-on runs
- Automate code generation with task-scoped prompts
- Include automatic code repair loops to handle runtime errors

## Interpretation and Iterative Refinement
- Use multi-agent dialogue to critique and refine interpretations
- Assign senior agents to review junior agent conclusions
- Carry forward experimental context across iterations
- Explicitly separate hypothesis generation from validation

## Writing and Reporting
- Follow standard scientific paper structure in generation prompts
- Generate drafts incrementally rather than in a single pass
- Use reviewer-style agents to critique clarity, rigor, and novelty
- Align writing with peer-review evaluation criteria

## Human-in-the-Loop Control
- Enable human intervention at all major pipeline stages
- Allow humans to redirect agent focus when quality degrades
- Use human feedback to correct hallucinations and misalignment
- Support co-pilot modes rather than fully autonomous execution

## Model Selection and Cost Management
- Use different models for different cognitive roles
- Evaluate tradeoffs between cost, reasoning quality, and speed
- Track agent performance metrics across tasks and models
- Prefer stronger models for planning and weaker models for execution

## Benchmarks Referenced
- MLR-Bench
