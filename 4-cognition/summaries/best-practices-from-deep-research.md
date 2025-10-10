# Modern Cognitive Enhancements for LLM Agents
_(best practices to improve multi-step problem solving)_

## Planning & Reasoning Strategies
- **Chain-of-Thought prompting** – step-by-step reasoning via intermediate rationales to improve multi-step problem solving
- **Tree-of-Thought exploration** – deliberate search over multiple reasoning paths with self-evaluation and backtracking for complex tasks
- **ReAct loop (Reason+Act)** – intermix reasoning steps with actions (tool use or environment queries) and observations, adjusting the plan based on feedback
- **Self-consistency decoding** – sample diverse reasoning chains for the same query and derive the answer by majority vote to boost reliability
- **Hierarchical/decision-tree planning** – formulate high-level plans (or decision trees) and refine sub-tasks iteratively, considering all options; integrate domain-specific planners for specialized problems
- **Modular planning architecture** – assign specialized LLM modules for subgoal decomposition, action proposal, error monitoring, state prediction, and outcome evaluation to generate complex plans

## Memory & Context Mechanisms
- **Long context windows** – utilize extended token context or summarization to retain pertinent dialogue history and facts for ongoing tasks
- **Retrieval-augmented memory** – fetch relevant external knowledge (documents, databases) on-the-fly to supplement the model’s working memory (e.g. RAG systems)
- **Persistent long-term memory** – maintain an external store of past interactions or learned facts for reuse across sessions, enabling the agent to accumulate knowledge over time
- **Structured memory representations** – use organized memory formats (e.g. note-taking databases or graph-based knowledge stores) to improve recall and rule formation for self-improvement

## Self-Reflection & Correction
- **Self-reflection prompts** – after producing an answer, the agent critiques its own reasoning (spotting logic errors, math mistakes, hallucinations) and generates guidance to improve the solution
- **Iterative solution refinement** – allow the agent to attempt a problem multiple times, learning from failures by analyzing mistakes and trying new approaches (simulated “learning from feedback”)
- **Verifiers/critics for answers** – introduce a verification step (rule-based or LLM-based) to review intermediate steps and final answers for errors, ensuring flawed reasoning is caught and corrected
- **Reusable reflective memory** – convert insights from self-reflection into persistent rules or constraints that guide future decisions (e.g. storing “lessons learned” to avoid repeating errors)

## Tool Use & External Aids
- **Tool-augmented prompting** – equip the agent with the ability to call external tools/APIs (e.g. calculators, web search, code interpreter) during reasoning to handle computations or fetch information beyond its internal knowledge
- **Tool-specific fine-tuning** – train or adapt the LLM to invoke APIs and software (e.g. Toolformer, TALM) so it learns when and how to use tools for domain-specific tasks (math, database queries, etc.)
- **Model orchestration** – use the LLM as a controller that delegates subtasks to expert models or services (e.g. HuggingGPT routing tasks to other AI models) and then integrates the results into a coherent answer

## Multi-Agent Collaboration
- **Debate frameworks (MAD)** – deploy multiple agent instances to discuss and challenge each other’s answers in a round-table style, refining reasoning through dissent and reaching a final answer via consensus or vote
- **Reviewer–advisor roles (MARS)** – assign agents distinct roles (e.g. single “author” solves the problem, several “reviewers” independently critique the solution, and a “meta-reviewer” synthesizes feedback and guides a revision) to catch mistakes efficiently without costly all-to-all debates
- **Peer cross-checking** – have agents verify and fact-check each other’s outputs (acting as mutual critics) so that one agent’s knowledge can correct another’s errors, improving overall solution quality

## Benchmarks for Evaluation
GPQA; MMLU; GSM8K; ARC (AI2 Reasoning Challenge); AGIEval (e.g. SAT & LSAT exams); HellaSwag; MedMCQA; Reflection-Bench; AlfWorld text-based tasks; API-Bank; Game-of-24 puzzle; Creative Writing & Mini-Crosswords
