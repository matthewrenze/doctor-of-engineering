# Summary of Agent Design Pattern Catalogue: A Collection of Architectural Patterns for Foundation Model Based Agents:

## Quick Reference

1. **Passive Goal Creator** - extract goals from user-provided prompts via dialogue interface  
2. **Proactive Goal Creator** - infer goals using environmental and multimodal context  
3. **Prompt/Response Optimiser** - refine prompts and responses for standardization and alignment  
4. **Retrieval Augmented Generation (RAG)** - fetch external or private knowledge to augment reasoning  
5. **One-Shot Model Querying** - generate entire plan from a single foundation model query  
6. **Incremental Model Querying** - iteratively query model step-by-step for planning  
7. **Single-Path Plan Generator** - generate a linear plan with one path toward goal  
8. **Multi-Path Plan Generator** - generate multiple options at each planning step  
9. **Self-Reflection** - agent evaluates and refines its own reasoning and outputs  
10. **Cross-Reflection** - another agent or model reviews and improves outputs  
11. **Human Reflection** - human feedback guides plan refinement and alignment  
12. **Voting-Based Cooperation** - multiple agents vote to reach a group decision  
13. **Role-Based Cooperation** - assign agents specific roles for collaboration  
14. **Debate-Based Cooperation** - agents argue and adjust to reach consensus  
15. **Multimodal Guardrails** - filter and validate inputs/outputs for safety and compliance  
16. **Tool/Agent Registry** - centralized lookup for tools and agents by capability  
17. **Agent Adapter** - interface layer to connect agents with external tools  
18. **Agent Evaluator** - test and assess agent behavior and performance


## Goal Formulation Patterns

- Passive Goal Creator
  - Extract goals from user prompts via dialogue interface
  - Retrieve relevant memory to enrich context
  - Preserve simplicity and efficiency

- Proactive Goal Creator
  - Infer goals using environmental context (e.g. sensors, screenshots)
  - Enable accessibility for users with limited input capability
  - Support multimodal input integration

## Prompt and Query Optimization Patterns

- Prompt/Response Optimiser
  - Refine inputs/outputs using templates
  - Ensure standardization and goal alignment
  - Improve interoperability and adaptability

- Retrieval Augmented Generation (RAG)
  - Retrieve relevant external/internal data to fill knowledge gaps
  - Avoid fine-tuning by supporting in-context augmentation
  - Preserve data privacy via local vector stores

## Model Querying Patterns

- One-Shot Model Querying
  - Query foundation model once to generate entire plan
  - Maximize cost-efficiency and speed
  - Risk of oversimplification or lack of explainability

- Incremental Model Querying
  - Query model at each reasoning step
  - Improve reasoning certainty and explainability
  - Support iterative refinement with human feedback

## Planning Patterns

- Single-Path Plan Generator
  - Generate linear, coherent multi-step plan
  - Favor efficiency and clarity
  - Limited flexibility and inclusiveness

- Multi-Path Plan Generator
  - Propose multiple choices at each step
  - Enable user preference alignment
  - Increase adaptability and inclusiveness

## Reflection Patterns

- Self-Reflection
  - Agent evaluates and revises its own outputs
  - Improve accuracy and support continuous learning

- Cross-Reflection
  - Use other agents or models to critique and revise outputs
  - Enhance inclusiveness and collective quality control

- Human Reflection
  - Incorporate human feedback into plan revisions
  - Ensure alignment with user intent and usability

## Cooperation Patterns

- Voting-Based Cooperation
  - Reach decisions by multi-agent voting
  - Enhance fairness and accountability
  - Promote collective intelligence

- Role-Based Cooperation
  - Assign specific roles (e.g., planner, assigner, worker) to agents
  - Support division of labor and task specialization
  - Facilitate scalable, fault-tolerant systems

- Debate-Based Cooperation
  - Facilitate argument-based agent discussions
  - Improve adaptability and critical thinking
  - Enable consensus through iterative refinement

## Control and Safety Patterns

- Multimodal Guardrails
  - Filter inputs/outputs for ethics, safety, compliance
  - Validate data across modalities (text, audio, video)
  - Enforce robustness and domain-specific standards

## Tooling and Integration Patterns

- Tool/Agent Registry
  - Central directory for discovering agents/tools
  - Support scalability and appropriate tool selection

- Agent Adapter
  - Interface layer between agent and tools
  - Automate format conversion and reduce integration cost

## Evaluation Pattern

- Agent Evaluator
  - Design-time and runtime testing of agents
  - Assess functionality, adaptability, and reliability
  - Support scenario-based testing and metric configuration
