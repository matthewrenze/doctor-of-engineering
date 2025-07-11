# Summary of Survey on Evaluation of LLM-based Agents

## 1. Evaluation Scope and Design

- Define evaluation across four dimensions: agent capabilities, application-specific tasks, generalist tasks, and frameworks
- Focus on multi-step, tool-augmented, memory-based, and self-reflective behaviors
- Avoid relying solely on single-call, static LLM benchmarks

## 2. Benchmark Design Best Practices

### 2.1 Planning & Multi-Step Reasoning
- Evaluate decomposition, causal reasoning, and strategic planning
- Use interactive, real-world-inspired tasks (e.g., Natural Plan, PlanBench)
- Prefer error recovery and state tracking metrics over one-shot correctness

### 2.2 Tool Use & Function Calling
- Break evaluation into sub-tasks: intent detection, argument extraction, function execution, response integration
- Use multi-turn, stateful environments (e.g., ToolSandbox, ComplexFuncBench)
- Test nested calls and tool interdependence

### 2.3 Self-Reflection
- Benchmark ability to update beliefs from feedback
- Include multi-turn interactive evaluation (e.g., LLF-Bench)
- Prefer fine-grained feedback response metrics over binary correctness

### 2.4 Memory
- Separate short-term vs. long-term memory capabilities
- Use multi-session and context-switching scenarios (e.g., StreamBench, LTMbenchmark)
- Track metrics like retrieval accuracy, memory hit rate, and task success

## 3. Application-Specific Evaluation

- Tailor benchmarks to task domains and interaction modalities
- Use dynamic, real-world-inspired environments over static datasets
- Measure success with granular metrics (e.g., task success, milestone completion, tool use correctness)

## 4. Evaluation Framework Practices

### 4.1 Evaluation Granularity
- Use multi-level analysis:
  - Final response correctness
  - Stepwise execution and tool selection
  - Trajectory and decision-path comparisons

### 4.2 Monitoring and Feedback
- Incorporate continuous evaluation during development
- Include custom metrics and domain-specific scoring
- Support A/B testing and human-in-the-loop corrections

### 4.3 Synthetic Data & Automation
- Use automated data generation (e.g., APIGen, IntellAgent) to scale evaluations
- Leverage LLMs as judges for step and trajectory assessment (Agent-as-a-Judge)

## 5. Evaluation Trend Alignment

- Favor realistic, complex, and evolving benchmarks over synthetic or overly-simplified ones
- Develop live and adaptive benchmarks to prevent benchmark saturation (e.g., BFCL v3, SWE-bench+)
- Track cost-efficiency alongside accuracy (e.g., token usage, latency, resource cost)

## 6. Safety and Compliance Evaluation

- Integrate policy compliance and adversarial robustness testing
- Simulate real-world risk scenarios in multi-agent and web-based environments
- Extend existing efforts like AgentHarm and ST-WebAgentBench
