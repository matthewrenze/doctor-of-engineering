# Safeguarding AI Agents: Developing and Analyzing Safety Architectures

## Context And High-Level Principles
- Treat alignment and safety as first-class architectural concerns
- Assume LLM agents can take unsafe actions beyond text generation
- Address risks from autonomy, tool use, and delegation
- Evaluate safety using realistic unsafe prompt categories
- Balance safety, capability, and system complexity

## Input–Output Filtering With LLMs
- Place a safety LLM between user and agent
- Filter user inputs before agent execution
- Filter agent outputs before user exposure
- Detect jailbreaks and prompt injection attempts
- Block interactions containing unsafe content
- Use semantic safety judgments instead of keyword rules
- Favor simplicity and low integration overhead

## Dedicated Safety Agent Architecture
- Introduce a specialized safety agent within the system
- Route agent outputs through the safety agent for review
- Modify unsafe outputs instead of fully rejecting when possible
- Preserve safe information while removing harmful content
- Encode explicit safety guidelines in the safety agent
- Support flexible, policy-driven safety behavior
- Enable multimodal safety review for images and tools

## Hierarchical Safety And Delegation
- Embed safety checks at every delegation boundary
- Require safety approval before task assignment
- Review intermediate outputs from subordinate agents
- Apply safety reasoning at each planning and execution step
- Prevent unsafe behavior propagation across agents
- Favor hierarchical safety for high-stakes or complex tasks

## Evaluation And Measurement Practices
- Test against diverse unsafe prompt categories
- Score responses on graded safety levels
- Compare safety architectures under identical tasks
- Evaluate multiple LLM backends for robustness
- Measure safety alongside cost and latency tradeoffs

## Deployment And Operational Guidance
- Select safety architecture based on risk tolerance
- Use filtering for lightweight or low-risk applications
- Use safety agents for nuanced content control
- Use hierarchical safety for maximum oversight
- Customize safety policies to domain constraints
- Anticipate role-play and fictional bypass attempts
- Extend evaluations with domain-specific unsafe data

## Benchmarks And Datasets Referenced
- ToxicChat
- OpenAI Moderation Evaluation Dataset
- LlamaGuard Unsafe Prompt Categories
- Azure AI Content Safety Categories
- OpenAI Moderation Categories
