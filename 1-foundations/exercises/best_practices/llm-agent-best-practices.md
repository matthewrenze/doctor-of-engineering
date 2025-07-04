# LLM Agent Best Practices

## 1. Core Design Principles
- Start simple; add complexity only as needed
- Use modular architecture to separate planning, memory, tools, and control
- Design for testability, interpretability, traceability, and debugging
- Match agent type (single vs multi-agent) to task complexity
- Ensure components are loosely coupled and easily swappable

## 2. Prompting and Reasoning
- Define agent role and goals via clear system prompts
- Break down tasks into step-by-step instructions or subgoals
- Use chain-of-thought (CoT) or ReAct-style prompting for structured reasoning
- Include scratchpads or reasoning buffers to externalize thought processes
- Prompt agents to reflect, critique, or self-evaluate before finalizing answers
- Prefer prompting over tool use when the task is simple and self-contained

## 3. Planning and Control Flow
- Use explicit planning when tasks involve multiple steps or branches
- Represent plans as natural language, pseudocode, graphs, or JSON
- Incorporate feedback-driven iteration from tools, users, or environment
- Use planning strategies like:
  - Sequential (prompt chaining)
  - Hierarchical (manager-worker)
  - Routing (input classification)
  - Parallelization (sectioning or voting)
  - Evaluator-optimizer loops

## 4. Action and Tool Use
- Define tools with clear names, input/output specs, and example usage
- Group tools by type: data access, action execution, orchestration
- Validate tool inputs before execution to avoid cascading errors
- Separate reasoning and acting to improve transparency and recovery
- Include a "Final Answer" or termination action to end loops
- Use "poka-yoke" techniques to make it difficult to use tools incorrectly
- Recover from failures using retries, alternate tools, or fallback paths

## 5. Memory and Context Management
- Use short-term memory for immediate task history and observations
- Use long-term memory (vector DBs, KGs, structured logs) for persistent knowledge
- Retrieve relevant memories before decision-making or response generation
- Summarize or distill long interactions to reduce context length and prevent drift
- Manage memory with techniques like:
  - Sliding windows
  - Frequency filters
  - Reflection and distillation
  - Subscription or tagging for relevance

## 6. Retrieval-Augmented Generation (RAG)
- Use RAG to ground responses in up-to-date or domain-specific information
- Perform query expansion and decomposition to improve retrieval quality
- Chunk and embed documents using structure-aware methods
- Re-rank retrieved results before generation using LLMs or scoring models
- Include citations or source justifications to reduce hallucination
- Validate final outputs for factual grounding and internal consistency

## 7. Orchestration and Multi-Agent Design
- Start with single-agent systems and scale up as complexity demands
- Use orchestration loops with clear exit and failure conditions
- Split tasks across agents when:
  - Tool count exceeds manageable limits
  - Task logic diverges into distinct workflows
  - Specialized reasoning or perception is required

### Multi-Agent Patterns
- Sequential - pass task control linearly from agent to agent
- Hierarchical - orchestrator delegates subtasks to workers
- Collaborative - combine agent outputs via voting, mixing, or consensus
- Competitive - select best output from agents solving in parallel
- Peer-to-Peer - agents dynamically hand off control or collaborate

### Agent Roles
- Define roles like planner, executor, retriever, evaluator, memory manager
- Use prompt-based role differentiation or dedicated agents per function
- Establish clear communication protocols for coordination

## 8. Evaluation and Monitoring
- Track business and user-centric metrics (e.g., goal success, satisfaction)
- Evaluate at multiple levels:
  - Trajectory (sequence of actions)
  - Tool use correctness
  - Final output quality
- Use autoraters (LLMs as judges) and human-in-the-loop scoring
- Calibrate scoring criteria with human feedback
- Log decisions and reasoning steps for traceability and improvement

## 9. Feedback and Learning
- Use failure cases and user feedback to guide prompt/tool/memory revision
- Employ self-reflection and reruns with different strategies to improve results
- Incorporate reinforcement learning or human-in-the-loop correction loops
- Allow agents to modify or generate their own tools over time

## 10. Safety and Guardrails
- Use classifiers to detect unsafe, irrelevant, or malicious inputs
- Apply moderation and PII filters to outputs
- Implement blocking or alerting for unsafe tool actions
- Add risk ratings to tools and trigger review for high-risk use
- Escalate to human intervention when confidence is low or impact is high
- Use multi-layered defenses:
  - Regex and keyword filters
  - Relevance and safety classifiers
  - Tool permission boundaries
- Continuously test and tune guardrails based on real-world failures

## 11. Human-in-the-Loop and Oversight
- Route irreversible or high-risk actions to human reviewers
- Design clear handoff mechanisms for human override or intervention
- Use sandboxed environments for testing agent behavior before deployment
- Monitor agent behavior at runtime to catch drift or unintended execution

## 12. Operations and Reliability (AgentOps)
- Track detailed telemetry on goal success, latency, and errors
- Log agent decisions and reasoning traces for observability
- Version prompts, tools, and configurations for reproducibility
- Use CI/CD practices to update and roll back agent behavior
- Isolate tool execution to prevent system-level failures

## 13. Deployment Patterns
- Use single-agent setups for simple, instruction-following tasks
- Use decentralized agents for parallel workflows or brainstorming
- Use manager-executor setups for task decomposition and coordination
- Design interface wrappers for multimodal I/O and human collaboration
- Support both proactive (autonomous) and reactive (user-guided) behaviors

## 14. Agent Evolution and Learning
- Enable agents to iteratively improve via self-reflection and tool feedback
- Use self-rewarding and self-correcting patterns for autonomous learning
- Apply evolutionary patterns:
  - Mutation and variation
  - Competitive debate and critique
  - Cooperative refinement across agents

## 15. Environment and Embodiment (if applicable)
- Design environments that allow perception → planning → action → feedback loops
- Use text-based, virtual, or real-world environments depending on embodiment level
- Provide agents with feedback signals to evaluate outcomes and learn

## 16. Trust, Alignment, and Ethical Design
- Align agent goals with user intent through prompt design and constraints
- Encourage transparent reasoning and justification of actions
- Constrain unsafe actions through permissions and filtering
- Address social impact concerns through responsible deployment policies
- Plan for governance, accountability, and long-term oversight mechanisms
