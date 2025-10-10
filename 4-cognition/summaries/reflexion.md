# Best Practices from Reflexion: Language Agents with Verbal Reinforcement Learning

## Core Principles of Reflexion
- Use **verbal reinforcement** instead of weight updates  
- Treat self-reflection as a **semantic gradient signal** guiding improvement  
- Convert environmental feedback into **natural language reflections**  
- Store reflections in **episodic memory** for future context  
- Enable agents to **learn from trial and error** via linguistic feedback  
- Optimize behavior without fine-tuning model parameters  

## Reflexion Architecture

### Modular Components
- **Actor (Ma)** – generates actions/text based on current state and memory  
- **Evaluator (Me)** – scores outputs with heuristic, binary, or LLM-based feedback  
- **Self-Reflection Model (Msr)** – generates verbal feedback from rewards and trajectories  

### Reflection Process
- Use **short-term memory** for recent trajectories  
- Use **long-term memory** for distilled experiences  
- Maintain **bounded memory buffer** (e.g., 1–3 reflections) to fit context window  
- Iterate: trajectory → evaluation → self-reflection → memory update  
- Condition future actions on **both current state and accumulated reflections**  
- Use **verbal summaries** as interpretable feedback loops instead of scalar rewards  

## Decision-Making Best Practices (ALFWorld)
- Integrate **self-reflection with ReAct** for long-horizon planning  
- Detect failure via simple heuristics (e.g., repeated actions, max steps)  
- Use **verbal self-analysis** to recognize early mistakes in long trajectories  
- Condense long failure histories into **short, actionable lessons**  
- Employ **episodic memory of self-hints** to reduce hallucinations  
- Balance short-term adaptation with long-term strategy refinement  
- Truncate reflections to last few experiences to maintain context efficiency  

## Reasoning Best Practices (HotPotQA)
- Combine **Chain-of-Thought (CoT)** or **ReAct** with Reflexion  
- Use **exact match** evaluation as binary feedback to trigger reflection  
- Employ **first-person verbal reasoning** to improve iterative learning  
- Favor **self-reflective refinement** over blind repetition or refinement-only loops  
- Maintain episodic memory of recent reflections for multi-hop reasoning  
- Use reflections to clarify reasoning scope (e.g., single fact vs series of facts)  
- Encourage **explicit verbalization of error types** (misread question, wrong context, etc.)  

## Programming Best Practices (HumanEval, MBPP, LeetcodeHardGym)
- Combine **self-generated unit tests** with **self-reflection** after failures  
- Use **Chain-of-Thought prompting** to produce diverse test cases  
- Filter tests for **syntactic validity (AST check)** before execution  
- Limit test suite size (e.g., ≤6 tests) for efficiency  
- Prefer **false negatives** (over false positives) to encourage deeper debugging  
- Maintain **language-agnostic design**—works across Python and Rust  
- Ensure **verbal reflection follows test results** to link cause and correction  
- Use **iterative trials** until successful compilation and test pass  
- Combine **test generation and verbal self-reflection** for highest accuracy  
- Avoid self-debugging without reflection—ineffective on complex problems  

## Memory and Reflection Design
- Separate **trajectory (short-term)** from **experience memory (long-term)**  
- Store reflections as **textual lessons learned**, not scalar values  
- Keep **bounded context** for efficiency and prevent drift  
- Use **episodic replay** of key reflections to guide next trials  
- Ensure reflections are **interpretable, actionable, and concise**  
- Treat reflection as both **diagnosis and plan revision**  

## Implementation and Evaluation Guidelines
- Use **few-shot prompting** (e.g., 2–6 shots) for Actor and Self-Reflection models  
- Cap learning iterations (e.g., ≤12 trials per environment)  
- Employ **heuristics or binary classification** for self-evaluation  
- Use **controlled truncation** of memory to prevent prompt overflow  
- Evaluate across **heterogeneous tasks** (decision, reasoning, programming)  
- Analyze **failure modes** (hallucination, inefficient planning, false positives)  

## Limitations and Future Enhancements
- Reflexion can converge to **local minima** without exploration diversity  
- Extend memory with **vector embeddings or structured databases**  
- Improve **test suite robustness** for more reliable self-evaluation  
- Incorporate **value learning or off-policy exploration** in natural language form  

## Benchmarks Referenced or Used
- **AlfWorld** (TextWorld-based decision-making)  
- **HotPotQA** (multi-hop reasoning benchmark)  
- **HumanEval** (Python code generation)  
- **MBPP** (Mostly Basic Programming Problems)  
- **LeetcodeHardGym** (new hard-level programming benchmark introduced)  
- **MultiPL-E** (multi-language compiler benchmark for code translation)  
- **WebShop** (ablation task showing Reflexion limits)  
