# Best Practices for Prompt Engineering

## 1. Designing Prompts

### 1.1 Components of a Good Prompt
- Include a clear directive (instruction or question)
- Provide exemplars (examples or few-shot demonstrations)
- Specify output formatting (CSV, Markdown, XML, etc.)
- Use style instructions to control tone or format
- Assign a role/persona for the LLM to improve coherence
- Include additional information necessary for the task

### 1.2 Few-Shot Prompting
- Maximize quantity of exemplars within context limits
- Randomize exemplar order to ensure robustness
- Maintain balanced label distribution
- Ensure label quality of exemplars
- Use consistent exemplar formatting
- Choose exemplars similar to the test input
- Experiment with common vs. novel prompt formats

### 1.3 Zero-Shot Prompting
- Add role/persona or tone specification
- Use thought inducers like "Let's think step by step"
- Apply rephrasing/expansion techniques (e.g., RaR, Re2, Self-Ask)

---

## 2. Prompting Techniques

### 2.1 Thought Generation
- Use Chain-of-Thought (CoT) for reasoning
- Try Zero-Shot CoT with thought-inducing phrases
- Apply Contrastive CoT with correct and incorrect reasoning examples
- Use Auto-CoT to auto-generate exemplars with reasoning

### 2.2 Decomposition
- Apply Least-to-Most prompting for sequential reasoning
- Use Plan-and-Solve prompts with structured planning steps
- Explore Tree-of-Thought, Skeleton-of-Thought, or Recursion-of-Thought
- Combine symbolic and natural language with Faithful CoT or Program-of-Thought

### 2.3 Ensembling
- Use Self-Consistency across multiple reasoning paths
- Apply Prompt Paraphrasing to create diverse prompt variants
- Combine outputs using DiVeRSe, MoRE, or Meta-CoT

### 2.4 Self-Criticism
- Prompt for self-calibration (check correctness)
- Use Self-Refine for iterative improvement
- Apply Self-Verification or Chain-of-Verification
- Try Cumulative Reasoning or Reversing CoT

---

## 3. Optimizing Prompts

### 3.1 Manual Prompt Engineering
- Follow an iterative loop: inference -> evaluation -> modification
- Tune prompt templates, answer shapes, and verbalizers

### 3.2 Automated Prompt Engineering
- Use Meta-Prompting to improve or generate new prompts
- Automate with AutoPrompt, APE, GrIPS, or ProTeGi
- Apply RLPrompt or DP2O for reinforcement learning-based optimization

---

## 4. Multilingual & Multimodal Prompting

### 4.1 Multilingual Prompting
- Use Translate First if LLMs perform better in English
- Align in-context examples via semantic or label-based matching
- Choose prompt language carefully (English vs. task language)
- Use cross-lingual CoT (e.g., XLT, CLSP)

### 4.2 Multimodal Prompting
- Modify prompts with prompt modifiers (e.g., lighting, medium)
- Use Negative Prompting to discourage undesirable features
- Try Paired-Image or Image-as-Text prompts
- Extend CoT to images via Chain-of-Images or Duty-Distinct CoT

---

## 5. Agents & Tool Use

### 5.1 Prompt-Based Agents
- Create Tool-Use Agents (e.g., MRKL, CRITIC)
- Use Code Generation Agents (e.g., PAL, ToRA)
- Employ Observation-Based Agents (e.g., ReAct, Reflexion)

### 5.2 Retrieval-Augmented Generation (RAG)
- Interleave retrieval and reasoning (e.g., IRCoT)
- Use iterative RAG techniques like FLARE, IRP
- Apply Verify-and-Edit or DSP

---

## 6. Evaluation Practices

### 6.1 Evaluation Prompting
- Use In-Context Learning with exemplars for evaluation
- Apply Role-Based Evaluation for diverse judgment
- Include Model-Generated Guidelines for scoring consistency
- Use Chain-of-Thought for evaluator reasoning

### 6.2 Output Formats
- Format outputs with binary, Likert, or linear scales
- Improve reliability with XML/JSON styling
- Use Self-Evaluation prompts where models assess their own outputs

### 6.3 Evaluation Frameworks
- Use frameworks like LLM-EVAL, G-EVAL, or ChatEval
- Apply Batch Prompting for cost-effective evaluation
- Prefer individual scoring over pairwise comparisons

---

## 7. Safety and Alignment

### 7.1 Prompt Security
- Defend against prompt injection and jailbreaking
- Use prompt-based defenses, detectors, and guardrails
- Avoid sharing sensitive contextual data (e.g., private emails)

### 7.2 Bias and Calibration
- Use Vanilla prompting to instruct fairness
- Ensure balanced demonstrations to reduce model bias
- Avoid sycophantic prompts and false assumptions
- Calibrate confidence with verbalized scores or token probabilities

### 7.3 Ambiguity Handling
- Include ambiguous demonstrations to improve generalization
- Add clarification sub-prompts to disambiguate input

