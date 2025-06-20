# Best Practices from "Agents Companion" (Google, Feb 2025)

## AgentOps
- Apply DevOps and MLOps principles to agent systems
  - Use version control, CI/CD, testing, logging, and metrics
  - Prioritize security, exception handling, throttling, and scalability
- Track detailed telemetry across agent systems
  - Measure goal completion, latency, errors, and human feedback
  - Log agent decisions with trace-level observability

## Agent Success Metrics
- Use business metrics as north star (e.g. revenue, engagement)  
- Instrument critical user tasks and track goal completion
- Collect human feedback for iterative improvement
- Monitor trace logs to understand agent decision-making
- Apply observability tools to assess agent actions at scale

## Agent Evaluation

### Assessing Agent Capabilities
- Start with public benchmarks for planning, tool use, and reasoning
- Use specialized benchmarks for specific agent tasks
- Understand inherited behavior from LLMs and system components

### Evaluating Trajectory and Tool Use
- Compare expected vs actual agent trajectories
- Use ground-truth-based automated evaluations
  - Exact match, in-order match, any-order match
  - Precision, recall, and single-tool usage

### Evaluating the Final Response
- Define custom success criteria for each use case
- Use autoraters (LLMs as judges) for automated scoring
- Tailor evaluation criteria to reflect quality standards

### Human-in-the-Loop Evaluation
- Incorporate subjective human judgment for creativity and nuance
- Use direct assessment, comparative evaluation, and user studies
- Calibrate autoraters with human feedback

## Multiple Agents & Their Evaluation
- Evaluate multi-agent systems with same principles as single-agent
- Measure agent cooperation, planning, and agent selection
- Analyze scalability and trajectory across multiple agents
- Use trace instrumentation to debug coordination issues

## Understanding Multi-Agent Architectures
- Use specialized agents with modular roles
  - Planner, Retriever, Executor, Evaluator agents
- Enable dynamic collaboration and decentralized problem-solving
- Structure systems with clear agent responsibilities

## Multi-Agent Design Patterns
- Choose design pattern based on task complexity and coordination
  - Sequential: pass tasks linearly
  - Hierarchical: orchestrator delegates to workers
  - Collaborative: agents combine responses via response mixer
  - Competitive: agents compete for best outcome
  - Peer-to-peer: agents redirect tasks among themselves

## Components of Effective Agents
- Include interaction wrapper for multimodal I/O
- Manage memory across short-term, long-term, and reflections
- Integrate cognitive functionality for reasoning and planning
- Enable dynamic tool discovery and invocation
- Establish agent-to-agent and remote communication protocols
- Maintain registry for agent and tool discovery with ontology

## Challenges in Multi-Agent Systems
- Handle message-based task communication
- Coordinate task allocation and shared reasoning
- Track context across agents and sessions
- Manage increased system complexity and latency

## Agentic RAG
- Use autonomous agents for iterative, contextual retrieval
- Perform query expansion, step-by-step reasoning, and source selection
- Validate and refine outputs before generating final response
- Improve response accuracy and adaptability in complex domains

## Better Search for RAG
- Parse documents using layout-aware chunking
- Enrich chunks with metadata for filtering and ranking
- Tune embedding models for domain-specific search
- Re-rank results post-retrieval for higher relevance
- Check grounding to ensure citation of generated content

## Agents in the Enterprise
- Deploy assistants for interactive, user-facing tasks
- Run automation agents in background for proactive workflows
- Transition knowledge workers into agent managers
- Orchestrate agents using interfaces for monitoring and control

## From Agents to Contractors
- Formalize tasks as contracts with deliverables and evaluation criteria
- Include specification, duration, cost, scope, and feedback mechanisms
- Allow agents to negotiate contracts and spawn subcontracts
- Implement iterative execution with validation checkpoints
