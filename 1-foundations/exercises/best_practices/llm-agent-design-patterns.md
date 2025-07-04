# LLM Agents Design Patterns

## 1. Reasoning Patterns
- **Chain-of-Thought (CoT)** - prompt agent to think step by step  
- **Plan-then-Execute** - separate planning from action execution  
- **Self-Ask** - decompose tasks into sub-questions  
- **Split-and-Combine** - divide task, process parts, merge results  
- **Self-Consistency** - sample multiple outputs, vote on answer  
- **Tree-of-Thought** - explore multiple reasoning branches with backtracking  
- **Graph-of-Thought** - share intermediate states across reasoning branches  
- **One-Shot Model Querying** - generate entire plan from a single foundation model query  
- **Incremental Model Querying** - iteratively query model step-by-step for planning  
- **Single-Path Plan Generator** - generate a linear plan with one path toward goal  
- **Multi-Path Plan Generator** - generate multiple options at each planning step  

## 2. Memory and Context Patterns
- **Retrieval-Augmented Generation (RAG)** - fetch relevant documents to enrich context  
- **Vector Memory** - store and retrieve persistent long-term facts  
- **Summarized Memory** - compress past context into concise summaries  
- **Episodic Recall** - selectively retrieve and reuse prior interactions  
- **Context Minimization** - strip prompt text post-processing to reduce exposure  

## 3. Tool Use and Integration Patterns
- **ReAct** - interleave reasoning and tool actions  
- **Toolformer** - autonomously insert tool/API calls  
- **Code-Execution** - generate and run code to compute results  
- **Function Calling** - call structured APIs with argument completion  
- **Tool Registry** - index tool specs for dynamic selection  
- **Tool/Agent Registry** - centralized lookup for tools and agents by capability  
- **DSL Output (CaMeL)** - output safe DSL code for execution  
- **Safe Tool DSL** - constrain tool calls to interpretable, verifiable code  
- **Agent Adapter** - interface layer to connect agents with external tools  

## 4. Self-Correction and Evaluation Patterns
- **Self-Refinement** - critique and revise own outputs  
- **Reflexion** - reflect on past errors and adapt  
- **Critique-Then-Answer** - critique solution before finalizing  
- **Answer-Then-Critique** - write solution, then reflect  
- **Self-Reflection** - agent evaluates and refines its own reasoning and outputs  
- **Cross-Reflection** - another agent or model reviews and improves outputs  
- **Human Reflection** - human feedback guides plan refinement and alignment  
- **Agent Evaluator** - test and assess agent behavior and performance  

## 5. Collaboration and Multi-Agent Patterns
- **Multi-Agent Debate** - agents argue opposing views  
- **Debate-Based Cooperation** - agents argue and adjust to reach consensus  
- **Voting-Based Cooperation** - multiple agents vote to reach a group decision  
- **Roleplay** - simulate personas or roles for specialization  
- **Role-Based Cooperation** - assign agents specific roles for collaboration  
- **Modular Agents** - split tasks across agent modules  
- **Society of Mind** - orchestrate diverse expert agents  

## 6. Goal Formulation Patterns
- **Passive Goal Creator** - extract goals from user-provided prompts via dialogue interface  
- **Proactive Goal Creator** - infer goals using environmental and multimodal context  

## 7. Prompt and Interaction Optimization
- **Prompt/Response Optimiser** - refine prompts and responses for standardization and alignment  

## 8. Safety and Robustness Patterns
- **Action-Selector** - isolate decision from tool output  
- **Plan-and-Execute Sandbox** - finalize plan before execution in a safe context  
- **Privileged/Quarantined Agents** - separate trusted from exposed models  
- **Prompt Injection Filtering** - sanitize tool/API inputs/outputs  
- **Multimodal Guardrails** - filter and validate inputs/outputs for safety and compliance  

