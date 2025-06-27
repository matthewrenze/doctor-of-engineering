
# Best Practices from "Building Effective Agents" (Anthropic, Dec 2024)

## General Principles for Agentic Systems
- Start with simple solutions before adding agentic complexity  
- Use workflows for predictable, well-defined tasks  
- Use agents for open-ended tasks requiring flexible decision-making  
- Favor low-latency and cost-effective single LLM calls when possible  
- Add agentic complexity only when it measurably improves performance  
- Combine and customize common patterns to fit specific use cases  
- Measure performance continuously and iterate on implementations  

## Framework Usage
- Avoid unnecessary abstractions from frameworks  
- Understand underlying code and prompt interactions  
- Begin with direct LLM API usage and minimal components  
- Use frameworks only to simplify boilerplate, not to obscure logic  

## Augmented LLMs
- Tailor retrieval, tool use, and memory to specific use cases  
- Provide clear, well-documented interfaces for augmentation  
- Leverage the Model Context Protocol (MCP) to integrate external tools  

## Workflow Patterns

### Prompt Chaining
- Decompose tasks into sequential LLM calls  
- Add programmatic checks at intermediate steps  
- Use when task can be cleanly broken into fixed subtasks  

### Routing
- Classify inputs and route to specialized prompts or tools  
- Separate different categories to improve accuracy and efficiency  
- Use traditional classifiers or LLMs for routing logic  

### Parallelization
- Use sectioning to run independent subtasks in parallel  
- Use voting to obtain diverse outputs and higher confidence  
- Handle complex tasks by splitting concerns across calls  

### Orchestrator-Workers
- Use central LLM to dynamically generate and assign subtasks  
- Enable flexible task decomposition not predefined in code  
- Synthesize results programmatically after worker execution  

### Evaluator-Optimizer
- Use one LLM to generate, another to evaluate and iterate  
- Apply when clear evaluation criteria are available  
- Improve quality through feedback loops  

## Agent Implementation
- Use agents for tasks with uncertain steps or decision paths  
- Rely on real-world feedback (e.g. tool results, code execution)  
- Include stopping conditions to prevent uncontrolled execution  
- Design clear, well-documented toolsets for agents  
- Test extensively in sandbox environments  
- Add guardrails to mitigate compounding errors  

## Agent Design Principles
- Maintain simplicity in design  
- Show agent planning steps transparently  
- Engineer agent-computer interfaces with same care as HCI  

## Tool Design and Prompt Engineering

### Format Design
- Use formats the model has seen in natural internet text (e.g., markdown)
- Avoid formats with unnecessary overhead (e.g. escaping, diff headers)  
- Give the model enough tokens to plan before generating  

### Tool Specification
- Make tool use obvious with clear names and descriptions  
- Include examples, edge cases, and input/output formats  
- Disambiguate similar tools with distinct boundaries  
- Test tool usage extensively and iterate based on model behavior  

### Error Prevention
- Redesign tools to make misuse difficult ("poka-yoke")
- Adjust arguments to avoid common model mistakes  
- Favor absolute paths, simplified formats, and low-ambiguity inputs  
