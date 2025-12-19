# Meta-Prompting: Enhancing Language Models with Task-Agnostic Scaffolding

## Meta-Prompting Framework
- Use a task-agnostic meta prompt as a reusable reasoning scaffold
- Keep the meta prompt fixed across tasks to enable zero-shot generalization
- Specify high-level goals and process guidance rather than task-specific instructions

## Task Decomposition
- Decompose complex problems into explicit natural-language subtasks
- Prefer structured multi-step workflows over single-shot answers
- Encode decomposition logic directly in the meta prompt

## Expert Instance Design
- Instantiate multiple expert roles using the same underlying LLM
- Assign each expert a clearly scoped subtask
- Use role instructions to induce specialization without fine-tuning

## Conductor / Orchestration
- Designate a conductor role to coordinate expert calls
- Control expert invocation order explicitly
- Aggregate, reconcile, and synthesize expert outputs centrally

## Self-Critique and Verification
- Include explicit verification or critique steps in the workflow
- Re-evaluate intermediate expert outputs before final synthesis
- Use internal consistency checks to reduce reasoning errors

## Tool Integration
- Integrate external tools (e.g., Python) within the meta-prompt loop
- Delegate exact computation or symbolic manipulation to tools
- Treat tool outputs as first-class expert inputs

## Task-Agnostic Generalization
- Avoid task-specific examples in the meta prompt
- Rely on structural guidance rather than domain heuristics
- Enable reuse across reasoning, planning, and coding tasks

## Zero-Shot Optimization
- Prioritize zero-shot performance over few-shot prompting
- Use structure and orchestration to replace example-heavy prompts
- Measure gains relative to standard zero-shot baselines

## Benchmarks Used or Referenced
- Game of 24
- Checkmate-in-One (Chess)
- Python programming problems

