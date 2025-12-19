# A Survey on Uncertainty Quantification of Large Language Models: Taxonomy, Open Research Challenges, and Future Directions

## Core Concepts
- Treat uncertainty as distinct from confidence
- Define uncertainty types explicitly
- Interpret uncertainty as reliability signal

## Taxonomy of Uncertainty Quantification Methods
- Token-level uncertainty via probabilities and entropy
- Self-verbalized uncertainty via natural language expressions
- Semantic-based uncertainty via agreement and clustering
- Mechanistic uncertainty via internal model signals
- Combine multiple method categories for robustness

## Uncertainty Metrics
- Use token entropy and probability dispersion
- Apply perplexity and log-probability statistics
- Measure semantic agreement using embedding similarity
- Compare metrics across tasks to identify reliable signals

## Calibration Techniques
- Apply temperature scaling for probabilistic calibration
- Use Platt scaling or isotonic regression when applicable
- Evaluate calibration separately from accuracy
- Optimize calibration for downstream decision quality

## Applications of Uncertainty
- Detect hallucinations and factual errors
- Guide abstention and deferral decisions
- Support interactive clarification with users
- Improve safety in robotics and embodied agents
- Inform planning and control in multi-step agents

## Integration Best Practices
- Fuse multiple uncertainty signals
- Select task-appropriate uncertainty metrics
- Use uncertainty as a control signal for agent behavior
- Ensure uncertainty outputs are interpretable and actionable

## Open Challenges and Practical Guidance
- Improve robustness to distribution shift and adversarial inputs
- Extend uncertainty to reasoning and multi-step processes
- Address overconfidence and underconfidence
- Monitor calibration drift over time
- Develop realistic uncertainty evaluation benchmarks

## Uncertainty Benchmarks Referenced
- TruthfulQA
- FEVER
- HaluEval
- FActScore
- MMLU
- GPQA
- HellaSwag
- GSM8K
- CalibratedMath
- ParaRel
- AmbigQA
- AmbigInst




