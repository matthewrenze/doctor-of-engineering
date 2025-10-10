# Best Practices from A Survey on LLMs for Automated Planning

---

## 1. Using LLMs as Standalone Planners

### Hierarchical Task Breakdown
- Decompose complex planning problems into manageable subtasks  
- Use structured prompting methods (CoT, Least-to-Most, Plan-and-Solve)  
- Focus LLM reasoning on short-horizon subgoals  
- Explicitly restrict available action space to executable options  
- Provide examples of successful plans to guide reasoning  

**Limitations to mitigate:**  
- Avoid over-reliance on handcrafted prompts  
- Minimize context length and demonstration overload  
- Recognize performance drops beyond few-shot exemplars  
- Address limited optimality in solutions  

---

### Plan Refinement and Self-Reflection
- Employ iterative plan generation and revision loops  
- Incorporate external or simulated feedback to refine plans  
- Separate reasoning (plan proposal) from acting (execution)  
- Use self-reflection or self-evaluation to detect and correct errors  
- Allow dynamic strategy updates in stochastic or partially observable settings  

**Limitations to mitigate:**  
- Prevent feedback loops that degrade performance  
- Validate correctness of self-generated feedback  
- Limit excessive iteration cycles to reduce computational cost  

---

### Search-Based Planning
- Represent reasoning as search (tree, graph, or beam)  
- Combine LLM generators (expand actions) and evaluators (score options)  
- Aggregate reasoning paths for robustness (self-consistency, ToT, GoT)  
- Enable pruning and exploration based on reasoning quality  

**Limitations to mitigate:**  
- Manage exponential search growth in long-horizon tasks  
- Avoid reliance on unreliable internal evaluators  
- Balance accuracy with computational and monetary efficiency  

---

### Fine-Tuning for Planning
- Fine-tune on structured datasets of planning problems and solutions  
- Optimize model parameters to align generated plans with ground-truth trajectories  
- Use diverse and high-quality data to learn general planning heuristics  

**Limitations to mitigate:**  
- Avoid overfitting to specific task distributions  
- Account for data inefficiency in covering diverse scenarios  
- Recognize performance degradation under distributional shift  

---

## 2. Integrating LLMs with Traditional Planners

### Text-to-Formal Specification Translation
- Use LLMs as interfaces between natural language and formal planning languages (PDDL, temporal logic, code)  
- Allow users to specify goals in natural language for accessibility  
- Automate translation to structured symbolic or logical representations  
- Combine LLM interpretability with the rigor of symbolic planners  

**Limitations to mitigate:**  
- Handle ambiguity in natural language inputs  
- Implement iterative verification and feedback loops for translation accuracy  

---

### Enhancing Planners with Commonsense Knowledge
- Leverage LLMs pre-trained commonsense knowledge for heuristic guidance  
- Use LLMs to check action preconditions and effects  
- Generate high-level subgoals and environmental insights  
- Reduce need for manual domain knowledge encoding  
- Integrate statistical priors (likelihoods, relations, constraints) into symbolic planning  
- Combine with external verifiers (LLM-modulo frameworks)  

**Limitations to mitigate:**  
- Guard against hallucinations and non-factual reasoning  
- Detect and compensate for missing or domain-specific knowledge gaps  

---

### Plan Evaluation and Reward Design
- Use LLMs/VLMs as qualitative and stylistic evaluators of plans  
- Generate or refine reward/objective functions for reinforcement learning  
- Serve as off-the-shelf critics to score plans against human-like preferences  
- Employ VLMs for multimodal evaluation of behavior (e.g., detecting undesirable outcomes)  
- Break ties between multiple feasible plans using human-aligned criteria  

**Limitations to mitigate:**  
- Ensure reliability in metric and numerical reasoning  
- Improve transparency and interpretability in plan evaluations  

---

## 3. Challenges and Future Opportunities

### Language Formalization
- Develop disambiguation techniques for translating natural language to formal task representations  
- Use iterative feedback between user and model to refine task definitions  

### Cost and Efficiency
- Improve numerical reasoning for cost estimation and optimization  
- Design adaptive reasoning trajectories to balance speed and accuracy  

### Knowledge and Generalization
- Identify and fill knowledge gaps in underrepresented domains  
- Integrate multimodal and embodied knowledge to strengthen world modeling  

### Interpretability and Causality
- Improve interpretability of LLM-based decisions in planning  
- Incorporate causal reasoning for robust generalization under distributional shifts  

### Multi-Agent Coordination
- Develop efficient communication and coordination methods for multi-agent LLM systems  
- Minimize computational overhead in multi-agent planning  

---

## 4. Benchmarks Referenced

**Interactive Games**
- TextWorld (2018)  
- Jericho (2020)

**Web and Computer Navigation**
- WebShop (2022)  
- WebArena (2024)  
- Mind2Web (2024)  
- OSWorld (2024b)

**Instruction Following and Task Planning**
- BabyAI (2019)  
- gSCAN (2020)  
- AlfWorld (2021)  
- VirtualHome (2018)

**Robotics and Physical Planning**
- SMART-LLM (2024)  
- RocoBench (2024)  
- PPNL (2024a/b)  
- Robotouille (2025)

**Tool Use and API Integration**
- API-Bank (2023b)  
- MINT (2024c)  
- TravelPlanner (2024a)  
- TaskBench (2024)

**Multi-Domain**
- AgentBench (2024)  
- PlanBench (2023)
