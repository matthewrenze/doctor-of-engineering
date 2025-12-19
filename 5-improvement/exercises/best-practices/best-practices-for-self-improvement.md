# Best Practices for Self-Improvement in LLM Agents

## Core Self-Improvement Principles
- Treat self-improvement as a first-class design objective
- Favor empirical performance gains over theoretical guarantees
- Optimize for cumulative improvement across runs, not single-task success
- Prefer simple, general mechanisms over brittle handcrafted logic
- Preserve agent state, artifacts, and knowledge across episodes

## Closed-Loop Improvement Cycles
- Structure agents as iterative sense–act–evaluate–update loops
- Use task success, failure, or reward as explicit learning signals
- Condition future behavior on prior trajectories and outcomes
- Limit iteration depth to control drift, cost, and compounding errors
- Separate improvement phases from task execution phases

## Reflection, Critique, and Self-Assessment
- Insert explicit self-reflection steps after failures and successes
- Analyze concrete state–action pairs rather than abstract mistakes
- Record actionable advice tied to specific scenarios
- Use self-critique to revise plans, prompts, or skills
- Validate reflections through subsequent task performance

## Meta-Prompting and Reasoning Scaffolds
- Use task-agnostic meta-prompts as reusable cognitive scaffolds
- Encode decomposition, planning, and verification in the scaffold
- Keep scaffolds fixed to support zero-shot generalization
- Prefer structural guidance over task-specific examples
- Reuse scaffolds across domains and task families

## Skill and Knowledge Extraction
- Extract reusable knowledge from successful trajectories
- Encode skills as explicit, composable context artifacts
- Store both descriptions and executable representations
- Favor context-level reuse over parameter updates
- Treat skills as modular building blocks, not monolithic solutions

## Skill Libraries and Memory Management
- Maintain a persistent, append-only skill or memory library
- Avoid overwriting or mutating validated skills
- Index skills using semantic similarity for retrieval
- Retrieve skills conditioned on task context and state
- Compose existing skills to solve novel problems

## Archive-Based Learning and Reuse
- Archive prior solutions, failures, designs, and reflections
- Condition new attempts on archived artifacts
- Track lineage and provenance of improvements
- Preserve suboptimal variants as stepping stones
- Use archives to prevent repeated mistakes

## Automated Self-Modification
- Allow agents to modify their own prompts, code, or workflows
- Apply programmatic edits rather than free-form rewriting
- Alternate modification phases with evaluation phases
- Retain rollback paths to prior stable versions
- Constrain self-modification to auditable representations

## Search, Exploration, and Diversity
- Treat self-improvement as a search over agent behaviors or designs
- Explore beyond the current best-performing variant
- Run parallel variants to avoid local optima
- Encourage diversity in reasoning strategies and solutions
- Preserve exploration even when performance plateaus

## Evaluation-Guided Improvement
- Use explicit metrics to validate improvements
- Compare against strong internal baselines
- Separate optimization feedback from validation signals
- Require measurable gains before persisting changes
- Reject improvements that reduce generality or robustness

## Transfer and Generalization
- Prefer task-agnostic skills over domain-specific heuristics
- Validate reuse across tasks, environments, or modalities
- Scale capability via accumulated knowledge, not pipeline complexity
- Enable continual learning without retraining the base model
- Design improvements to compound over long horizons

## Safety, Stability, and Oversight
- Sandbox execution of self-modifying components
- Log all changes for inspection and auditability
- Preserve human override and intervention points
- Constrain improvement objectives to aligned outcomes
- Monitor for regressions, unsafe behavior, or reward hacking
