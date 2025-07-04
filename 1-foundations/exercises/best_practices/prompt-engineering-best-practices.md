# Prompt Engineering Best Practices

## 1. Clarity and Intent
- Use clear, specific instructions  
- Define the task, scope, and audience  
- Specify desired output format and length  
- Avoid ambiguous or vague language  
- Use delimiters to separate and structure content  
- Include a verb or directive in every prompt  
- Keep prompts concise and avoid unnecessary jargon  

## 2. Context and Content
- Provide all necessary background information  
- Include relevant data or examples  
- Maintain consistent formatting throughout  
- Organize the prompt into clearly labeled sections  
- Avoid including irrelevant or distracting content  
- Reference files or documents using placeholders or tags (e.g., `@[filename]`)  

## 3. Role and Persona
- Assign a clear role or persona to guide the model's behavior  
- Set tone, style, and expertise level explicitly  
- Use personas to constrain or focus output behavior  
- Emulate expert reasoning and communication patterns  

## 4. Reasoning and Thought Process
- Prompt the model to reason step by step (e.g., "Let's think this through")  
- Ask for intermediate steps or explanations before final answers  
- Use structured reasoning scaffolds (e.g., plan first, then solve)  
- Guide model through sub-steps for complex problems  

## 5. Prompt Structure and Composition
- Use zero-shot prompting for simple or factual tasks  
- Use few-shot prompting for nuanced or structured tasks  
- Choose diverse and representative exemplars  
- Format exemplars identically to the target task  
- Ensure high-quality and balanced examples  
- Avoid prompt truncation by keeping length manageable  

## 6. Prompt Iteration and Testing
- Test multiple prompt variants to compare outputs  
- Refine wording and structure based on observed output  
- A/B test small phrasing changes for impact  
- Evaluate response quality before production use  
- Use user or model feedback to iteratively improve prompts  
- Simplify and isolate prompt components to identify issues  
- Analyze token-level completions and log probabilities for debugging  

## 7. Advanced Prompting Techniques

### 7.1 Thought Generation
- Use Chain-of-Thought (CoT) to elicit multi-step reasoning  
- Apply Zero-Shot CoT with prompting cues  
- Try Contrastive CoT to distinguish correct and incorrect reasoning  
- Use Auto-CoT to generate exemplars with explanation steps  

### 7.2 Task Decomposition
- Use Least-to-Most prompting for complex reasoning  
- Apply Plan-and-Solve frameworks  
- Explore Tree-of-Thought, Skeleton-of-Thought, and Recursion-of-Thought methods  
- Combine symbolic and natural language reasoning (e.g., Faithful CoT)  

### 7.3 Ensembling and Self-Critique
- Use Self-Consistency across multiple generations  
- Prompt for Self-Evaluation, Self-Verification, or Self-Refinement  
- Apply Prompt Paraphrasing for robustness  
- Use meta techniques (e.g., DiVeRSe, Meta-CoT, MoRE)  

## 8. Prompt Optimization

### 8.1 Manual Engineering
- Iterate through a loop: generate → evaluate → revise  
- Adjust templates, answer forms, and verbalizers  

### 8.2 Automated Engineering
- Use Meta-Prompting to refine prompt design  
- Apply AutoPrompt, APE, GrIPS, or ProTeGi  
- Use RLPrompt or DP2O for reinforcement learning-based tuning  

## 9. Multilingual and Multimodal Prompting

### 9.1 Multilingual Prompting
- Use Translate First strategy for English-optimized models  
- Align examples semantically across languages  
- Choose language based on model performance  
- Apply cross-lingual CoT (e.g., XLT, CLSP)  

### 9.2 Multimodal Prompting
- Use prompt modifiers (e.g., "high resolution," "dark background")  
- Add negative prompts to steer away from undesired outputs  
- Combine image and text inputs with paired or image-as-text prompts  
- Extend CoT techniques to image-based reasoning  

## 10. Agents and Tool Use

### 10.1 Prompt-Based Agents
- Use prompting to interface with tools (e.g., MRKL, ReAct)  
- Create specialized agents for code generation or planning (e.g., PAL, ToRA)  
- Employ observation-action-reflection loops (e.g., Reflexion)  

### 10.2 Retrieval-Augmented Generation (RAG)
- Interleave retrieval and reasoning (e.g., IRCoT)  
- Use iterative and verifiable RAG methods (e.g., FLARE, IRP)  
- Apply Verify-and-Edit or DSP for refinement  
- Prompt models to cite sources and ground outputs in retrieved evidence  

## 11. Evaluation and Scoring

### 11.1 Prompting for Evaluation
- Use in-context learning with high-quality exemplars  
- Apply role-based prompts to simulate human judgment  
- Guide evaluator reasoning with CoT  
- Provide explicit rubrics or model-generated scoring criteria  

### 11.2 Output Formatting
- Use structured output formats (e.g., JSON, tables)  
- Score using binary, Likert, or ordinal scales  
- Include model self-evaluation when applicable  

### 11.3 Evaluation Tools
- Use automated tools (e.g., LLM-EVAL, G-EVAL, ChatEval)  
- Batch prompts to reduce evaluation costs  
- Prefer single-answer scoring for clarity  

## 12. Safety and Alignment

### 12.1 Prompt Security
- Defend against prompt injection and jailbreaks  
- Use input sanitization, detectors, and guardrails  
- Avoid exposing sensitive contextual data  

### 12.2 Bias and Calibration
- Use neutral language and balanced examples  
- Avoid sycophantic or leading prompts  
- Calibrate confidence using probabilistic outputs  

### 12.3 Ambiguity and Robustness
- Add ambiguous examples to improve generalization  
- Include clarification sub-prompts to resolve uncertainty  

## 13. Generation Parameters
- Adjust temperature to control randomness and creativity  
- Use top-k and top-p to limit the sampling distribution  
- Set max tokens to control output length  
- Use frequency and presence penalties to reduce repetition  

## 14. Prompt Hygiene
- Avoid overly long or complex system messages  
- Use clean and consistent formatting for readability  
- Minimize chained dependencies to reduce fragility  
- Sanitize input to prevent unintended injection or context leakage  

