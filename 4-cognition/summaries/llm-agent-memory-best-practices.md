# Best Practices from A Survey on the Memory Mechanism of Large Language Model-based Agents

---

## 1. Foundational Design Principles
- Treat memory as core to agent cognition, not a peripheral add-on
- Model agent-environment interaction through perception → memory → action loop
- Separate operations into writing, management, and reading functions
- Balance interpretability (textual memory) and efficiency (parametric memory)
- Combine short-term (within-trial) and long-term (cross-trial/external) memory
- Design modular, swappable memory components for flexibility
- Align memory design with cognitive psychology principles (attention, forgetting, abstraction)

---

## 2. Why Memory Matters
### Cognitive psychology basis
- Emulate human mental processes (attention, recall, abstraction)
- Support reasoning, learning, and imagination through remembered experiences

### Self-evolution
- Enable agents to accumulate experience and learn from failure
- Use memory to guide exploration and knowledge abstraction

### Application perspective
- Maintain conversational and role consistency
- Ensure contextual understanding and goal continuity

---

## 3. Implementing Memory

### 3.1 Memory Sources
- **Inside-trial information**
  - Store agent–environment interactions within a single task
  - Capture contextual metadata (time, location, dialogue state)
- **Cross-trial information**
  - Retain successful/failed experiences for future reference
  - Abstract long-term behavioral patterns from multiple trials
  - Use reflection or verbal reinforcement learning (e.g., Reflexion, ExpeL)
- **External knowledge**
  - Retrieve factual data through APIs or databases (e.g., Wikipedia, domain KBs)
  - Integrate dynamic external knowledge into decision-making
  - Ensure reliability and handle outdated or biased sources

### 3.2 Memory Forms
- **Textual memory**
  - Use natural language summaries or structured tuples
  - Common strategies:
    - Complete interaction logs
    - Recent interaction windows (short-term cache)
    - Retrieved interactions via relevance search (FAISS, LSH)
    - External knowledge storage via tool use
  - Optimize retrieval accuracy, latency, and interpretability
- **Parametric memory**
  - Encode knowledge directly into model parameters
  - Use fine-tuning for domain expertise (e.g., medicine, finance)
  - Apply knowledge editing for lightweight updates and forgetting
  - Combine offline fine-tuning with online meta-learning adaptation
- **Trade-offs**
  - Textual memory – interpretable, flexible, but length-limited
  - Parametric memory – compact, efficient, but less explainable
  - Use hybrid systems for complementary strengths

### 3.3 Memory Operations
- **Writing**
  - Extract salient information; summarize and index for retrieval
  - Filter noise and maintain structured representations
- **Management**
  - Merge redundant memories and remove outdated ones
  - Reflect to form higher-level abstractions and self-improvement
  - Apply selective forgetting to prevent overload
- **Reading**
  - Retrieve relevant entries via similarity, time, or importance weighting
  - Incorporate retrieved context into next prompt or decision
  - Optimize read efficiency for real-time tasks

---

## 4. Evaluating Memory

### 4.1 Direct Evaluation
- **Subjective methods**
  - Human ratings on coherence and rationality
  - Use diverse evaluators and consistent scoring scales
- **Objective methods**
  - *Result correctness* – accuracy on memory-based Q&A
  - *Reference accuracy* – F1 score on retrieved vs. ground-truth memory
  - *Efficiency metrics* – adaptation time, inference latency, GPU memory use

### 4.2 Indirect Evaluation
- **Conversation tasks**
  - Measure consistency, engagement, and persona retention
- **Multi-source QA**
  - Test integration of internal, cross-trial, and external memories
- **Long-context tasks**
  - Evaluate long-term retention and summarization (e.g., LongBench, ZeroScrolls)
- **Other agent tasks**
  - Use success rate, exploration degree, or ablation comparisons (with/without memory)

---

## 5. Applications and Design Insights
- **Role-playing / Social simulation**
  - Maintain persona-consistent long- and short-term memory
  - Implement human-like forgetting and reflection
- **Personal assistants**
  - Use retrieval-based textual memory for personalized dialogue continuity
- **Games / Open-world exploration**
  - Store and reuse trajectories, external guides, and learned strategies
- **Code generation**
  - Retain context across sessions; store debugging or API knowledge
- **Recommendation**
  - Store personalized user profiles and behavioral feedback
  - Update dynamically for evolving preferences
- **Expert systems (medicine, finance, science)**
  - Fine-tune or edit memory for domain-specific reasoning
  - Periodically refresh to avoid stale knowledge

---

## 6. Future Directions
- **Advances in parametric memory**
  - Develop efficient encoding/decoding from text to latent parameters
  - Improve interpretability and trust of implicit memories
- **Multi-agent memory**
  - Synchronize shared memories for coordination
  - Address information asymmetry and communication history
- **Lifelong learning**
  - Implement temporal memory with forgetting and consolidation
  - Handle memory overlap and long-term retrieval scalability
- **Humanoid agents**
  - Align memory limits, distortions, and biases with human cognition

---

## Benchmarks Referenced
- **Reflexion** (verbal reinforcement learning)
- **ReAct** (reasoning and acting tasks)
- **AlfWorld** (interactive reasoning tasks)
- **LongBench**, **ZeroScrolls** (long-context understanding)
- **Minecraft / Voyager / GITM** (open-world exploration)
- **ChatDB**, **MemoChat**, **MemoryBank**, **ExpeL** (memory-specific evaluation frameworks)
