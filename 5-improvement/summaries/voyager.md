# Voyager: An Open-Ended Embodied Agent with Large Language Models

## 1. Agent Architecture & Module Design
- Modular agent design: curriculum, skill library, prompting subsystems
- Clear separation of responsibilities: exploration, learning, execution
- Skills represented as executable code artifacts
- Persistent agent state across tasks and episodes

## 2. Lifelong Exploration & Automatic Curriculum
- Automatic curriculum generation based on current capabilities
- Task proposals driven by unexplored environment affordances
- Progressive task difficulty aligned with acquired skills
- Curriculum adapts as the skill library grows
- Exploration prioritized over narrow task optimization

## 3. Skill Library Construction & Management
- Maintain an ever-growing library of reusable skills
- Skills implemented as general-purpose code functions
- Store skill descriptions alongside executable implementations
- Index skills using embedding-based similarity
- Retrieve skills conditioned on task context and environment state
- Compose existing skills to solve novel tasks
- Avoid overwriting skills; only append validated additions

## 4. Iterative Prompting & Self-Improvement Loop
- Multi-round prompt–execute–feedback loop
- Include environment state in each prompt iteration
- Incorporate execution errors as corrective feedback
- Use task success or failure signals to guide revisions
- Repeat until successful and robust behavior emerges

## 5. Code Generation Best Practices
- Generate generic, reusable, and composable code
- Avoid task-specific hard-coding in skill implementations
- Encourage modular function boundaries
- Use explicit planning or reasoning before code generation
- Validate code through execution rather than static inspection

## 6. In-Context Skill Retrieval & Use
- Retrieve relevant skills via embedding similarity
- Inject retrieved skill code into the prompt context
- Condition generation on both current task and available skills
- Use skills as building blocks rather than rewriting behaviors

## 7. Lifelong Learning & Generalization
- Continuously expand capabilities without retraining the model
- Accumulate skills across long horizons
- Enable transfer to new environments via the skill library
- Leverage prior skills to accelerate future task completion

---

## Benchmarks Referenced
- Minecraft open-ended exploration environment
- Unique items collected
- Distance traveled
- Tech tree milestone completion speed
