# Alita: Generalist Agent Enabling Scalable Agentic Reasoning with Minimal Predefinition and Maximal Self-Evolution

## High-Level Principles for Self-Improvement
- Favor minimal predefinition over complex handcrafted pipelines
- Maximize agent autonomy in capability growth
- Treat self-evolution as a first-class design goal

## Architectural Design Best Practices
- Use a single core reasoning component
- Avoid rigid, multi-stage agent workflows
- Centralize task solving in one general problem-solving loop
- Design components to be task-agnostic and reusable

## Self-Evolution and Learning Mechanisms
- Automatically extract reusable knowledge from successful trajectories
- Encode reusable behaviors as task-specific Model Context Protocols (MCPs)
- Store MCPs as externalized procedural memory
- Re-invoke MCPs to accelerate future task solving
- Iteratively refine MCPs through repeated use
- Enable agent-driven creation of new capabilities without manual programming

## Knowledge and Skill Reuse
- Treat skills as composable context artifacts rather than hardcoded tools
- Prefer context-level reuse over parameter-level retraining
- Accumulate a growing library of task-conditioned reasoning templates

## Generalization and Scalability
- Avoid domain-specific heuristics that limit transfer
- Support open-ended task coverage through self-generated context
- Scale reasoning ability by expanding skill memory rather than agent complexity

## Evaluation and Validation Practices
- Measure performance improvements from self-evolution explicitly
- Compare against strong generalist agent baselines
- Validate across diverse reasoning and perception-reasoning tasks

## Benchmarks Referenced
- GAIA
- MathVista
- PathVQA
