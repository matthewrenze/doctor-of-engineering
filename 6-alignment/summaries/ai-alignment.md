# AI Alignment Best Practices — arXiv:2310.19852

## Alignment Objectives (RICE framework)
- Robustness
  - Maintain reliable behavior under distribution shift
  - Resist adversarial inputs and perturbations
- Interpretability
  - Enable human understanding of model decisions
  - Support debugging and auditing of behaviors
- Controllability
  - Preserve human ability to steer, correct, or shut down systems
  - Prevent unintended autonomy or goal drift
- Ethicality
  - Align behavior with human values and social norms
  - Avoid harmful, biased, or deceptive outcomes

## Forward Alignment (Alignment Training)
- Learning from feedback
  - Train using explicit human preferences
  - Incorporate evaluative signals beyond task success
- Reinforcement learning from human feedback
  - Use reward models to encode alignment objectives
  - Iteratively refine policies with preference data
- Scalable oversight
  - Decompose hard judgments into simpler evaluations
  - Use AI assistance to amplify human supervision
- Goal specification and generalization
  - Reduce goal misgeneralization across contexts
  - Align learned objectives with intended goals
- Robust training under uncertainty
  - Train across diverse scenarios and environments
  - Anticipate deployment-time distribution shifts
- Hybrid alignment strategies
  - Combine offline data with online interaction
  - Adapt models post-deployment when needed

## Backward Alignment (Assurance and Governance)

### Assurance Practices
- Safety evaluation
  - Test for harmful, deceptive, or misaligned behavior
  - Evaluate across increasingly realistic settings
- Interpretability-based auditing
  - Inspect internal representations and reasoning paths
  - Detect latent objectives or unsafe heuristics
- Value compliance verification
  - Measure adherence to human values post-training
  - Validate alignment claims empirically
- Continuous monitoring
  - Re-evaluate alignment throughout the lifecycle
  - Detect degradation or emergent risks over time

### Governance Practices
- Regulatory oversight
  - Establish external constraints on development and deployment
  - Enforce safety and alignment requirements
- Lifecycle standards
  - Define alignment practices from pre-training to deployment
  - Maintain documentation and accountability
- Institutional coordination
  - Encourage collaboration across academia, industry, and government
  - Share best practices and failure cases
- Adaptive governance
  - Update policies as system capabilities evolve
  - Anticipate long-term and systemic risks


## Alignment Benchmarks for LLM Agents

### Safety and Harm Avoidance
- TruthfulQA
  - Measures propensity to produce false or misleading answers
- RealToxicityPrompts
  - Evaluates toxic content generation under adversarial prompts
- HarmBench
  - Tests model responses to harmful instructions across multiple harm categories
- AdvBench
  - Assesses robustness to adversarially crafted harmful prompts
- XSTest
  - Evaluates over-refusal and under-refusal behavior in safety-critical queries
- Do-Not-Answer
  - Tests whether models appropriately refuse unsafe or disallowed requests
- BeaverTails
  - Large-scale dataset for harmful instruction following and refusal behavior

### Bias, Fairness, and Values
- BBQ (Bias Benchmark for Question Answering)
  - Measures social bias in ambiguous and disambiguated contexts
- BOLD
  - Evaluates bias in open-ended text generation across demographic groups
- StereoSet
  - Measures stereotypical associations in language modeling
- CrowS-Pairs
  - Tests preference for stereotypical vs anti-stereotypical statements

### Helpfulness, Honesty, and Harmlessness
- Anthropic Helpful–Harmless (HH) Dataset
  - Evaluates trade-offs between being helpful and avoiding harm
- Safety-Prompts / HH-RLHF Eval Sets
  - Preference-based evaluations used in RLHF alignment training

### Robustness to Jailbreaks and Misuse
- JailbreakBench
  - Measures susceptibility to prompt-based safety bypass attacks
- SafeEval
  - Evaluates refusal quality, consistency, and recovery under adversarial prompting
- Red Teaming Prompt Sets
  - Stress-test alignment under creative misuse scenarios

### Agent-Specific Alignment and Safety
- AgentBench (Safety and Tool-Use Subsets)
  - Evaluates agent behavior in multi-step, tool-using environments with safety constraints
- WebArena Safety Tasks
  - Tests safe decision-making during autonomous web interactions
- ALFWorld Safety-Constrained Tasks
  - Evaluates instruction-following agents under environment-level constraints

### Holistic and Framework-Level Evaluations
- HELM Safety Scenarios
  - Standardized evaluation of harmfulness, bias, and toxicity across models
- MT-Bench Safety Variants
  - Human-judged safety and alignment comparisons in multi-turn dialogues



