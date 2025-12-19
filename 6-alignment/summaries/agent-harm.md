# AgentHarm: A Benchmark for Measuring Harmfulness of LLM Agents

## Benchmark Design Principles
- Cover broad range of harm categories
- Include explicitly malicious multi-step agent tasks
- Pair harmful tasks with benign counterparts
- Integrate external tools and multi-step workflows
- Use synthetic tools with defined behavior
- Employ fine-grained human-written scoring rubrics

## Safety Measurement Practices
- Measure harmful compliance and capability retention
- Test robustness against jailbreak-style prompts
- Evaluate multi-step safety rather than single-turn safety
- Assess agent planning and tool-use coherence under attack

## Implications for Agent Alignment
- Assume chatbot safety does not transfer to agents
- Design safety mechanisms for long-horizon planning
- Align defenses with tool-integrated agent workflows
- Use public benchmarks to drive alignment research

## Benchmarks Referenced
- AgentHarm
