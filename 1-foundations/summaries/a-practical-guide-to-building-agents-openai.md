# Summary of Best Practices for Building Agents (OpenAI)

## When to Build an Agent
- Prioritize workflows with complex, nuanced decision-making
- Target systems with difficult-to-maintain, brittle rule sets
- Focus on tasks reliant on unstructured natural language data
- Avoid agents for deterministic tasks where rules suffice
- Validate need for an agent before committing development resources

## Agent Design Foundations

### Model Selection
- Start with most capable models to establish a performance baseline
- Use evaluation metrics to set and measure accuracy targets
- Replace large models with smaller ones where performance allows
- Match model choice to task complexity, latency, and cost needs

### Tool Definition
- Standardize tool definitions for reusability and consistency
- Categorize tools as data, action, or orchestration tools
- Use tools to extend agent capabilities via APIs or UI interaction
- Split tasks across agents when tool count becomes unmanageable

### Instruction Design
- Derive routines from existing SOPs or policy documents
- Break down dense content into clear, actionable steps
- Make each step correspond to a specific, unambiguous action
- Include branches and fallbacks to handle edge cases and missing inputs

## Orchestration Patterns

### General Guidelines
- Start with single-agent systems to reduce complexity
- Use orchestration loops with clear exit conditions
- Favor prompt templates over many static prompts for maintainability

### When to Split into Multiple Agents
- Divide agents when logic becomes too complex for one prompt
- Separate overlapping or ambiguous tools across distinct agents
- Maximize single-agent capabilities before introducing multi-agent setups

### Manager Pattern (Agents as Tools)
- Central manager delegates tasks to specialized agents
- Use when single point of user interaction is preferred
- Assign each specialized agent a tool name and description

### Decentralized Pattern (Handoff Between Agents)
- Allow agents to hand off workflow control to other agents
- Use when no single agent needs central control
- Ideal for triage, specialized roles, or parallel workflows

## Guardrails and Safety

### Types of Guardrails
- Use relevance classifiers to filter off-topic inputs
- Detect unsafe inputs with classifiers for jailbreaks and prompt injection
- Filter PII from outputs to protect user privacy
- Apply moderation filters to block harmful content
- Assign tool risk ratings to trigger safety checks
- Use rules-based filters (e.g., regex, blocklists) for known threats
- Validate outputs for brand alignment and policy compliance

### Guardrail Implementation
- Layer multiple types of guardrails for defense in depth
- Add guardrails based on real-world failures and edge cases
- Balance security with user experience via iterative tuning
- Treat guardrails as first-class citizens in your architecture

## Human-in-the-Loop Intervention
- Escalate to humans on high-risk or irreversible actions
- Trigger intervention when agents exceed failure thresholds
- Design handoff mechanisms to return control to users or humans
- Use early deployment feedback to identify failure modes
