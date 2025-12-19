# Automated Design of Agentic Systems — Best Practices

## Fundamental Principles & Motivation
- Treat agent design as a search problem over a design space
- Represent agents as executable code for maximal expressivity
- Use foundation models to generate novel agent designs
- Prefer automated discovery over manual agent engineering
- Maintain an archive of past designs to guide future improvement

## Search Space Design
- Define entire agentic systems in code, not just prompts
- Include reasoning strategies, workflows, tool use, and control logic
- Seed search with minimal but complete primitive components
- Favor interpretable representations for analysis and debugging

## Meta Agent Search Process
- Use a meta-level LLM to propose new agent designs
- Condition generation on prior designs and evaluation results
- Apply iterative self-refinement to generated agent code
- Allow multiple regeneration attempts to fix errors
- Store successful designs and metadata back into the archive

## Evaluation & Selection
- Evaluate agents using task-specific performance metrics
- Separate search guidance data from validation data
- Compare against strong hand-designed agent baselines
- Favor designs that generalize across tasks and domains

## Emergent Design Patterns
- Combine multiple reasoning paths within a single agent
- Use parallel chains of thought with aggregation
- Incorporate internal feedback and refinement loops
- Leverage ensemble-style reasoning from diverse agent components

## Safety & Reliability
- Execute generated agents in sandboxed environments
- Inspect generated code for unsafe or unintended behavior
- Preserve agent structure for auditability and analysis
- Apply explicit constraints during execution and evaluation

## Iterative Improvement & Transferability
- Use archives to enable cumulative improvement over iterations
- Reuse successful agent designs across domains
- Enable continual refinement rather than one-shot optimization
- Treat agent design as an ongoing evolutionary process

## Future Directions & Extensions
- Explore meta-agents that improve the search process itself
- Optimize across multiple objectives such as cost and latency
- Use failure cases to inform future agent generation
- Extend to multi-model and multi-modal agent systems
- Incorporate quality-diversity and open-ended search strategies

## Benchmarks Used or Referenced
- Abstraction and Reasoning Corpus (ARC)
- DROP
- MGSM
- MMLU
- GPQA
- Hand-designed agent baselines (Chain-of-Thought, Self-Refine, Self-Consistency, Debate, Quality-Diversity)
