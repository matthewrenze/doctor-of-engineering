# Summary of Best Practices for Uncertainty in LLM Agents

## Uncertainty Foundations
- Explicitly treat uncertainty as a first-class reliability signal
- Distinguish uncertainty from confidence in design and evaluation
- Differentiate epistemic uncertainty from aleatoric uncertainty
- Select uncertainty methods based on failure mode and task type

## Statistical Uncertainty Estimation
- Use token-level log probabilities as a baseline uncertainty signal
- Compute predictive entropy for single-pass uncertainty estimates
- Use negative log-likelihood to rank likely incorrect answers
- Prefer statistical uncertainty for correctness and safety detection
- Avoid relying on raw softmax probabilities without calibration

## Multi-Sample and Ensemble Estimation
- Generate multiple samples to approximate predictive distributions
- Use self-consistency agreement as a confidence proxy
- Measure disagreement across samples as uncertainty
- Prefer semantic entropy over lexical entropy for RLHF-tuned models
- Use cross-model agreement when multiple models are available

## Semantic and Meaning-Level Uncertainty
- Cluster multiple generations by semantic similarity
- Treat high semantic diversity as high uncertainty
- Aggregate meaning-level disagreement into scalar uncertainty scores
- Use semantic uncertainty for free-form and open-ended tasks

## Input Robustness and Perturbation
- Paraphrase or perturb inputs to test answer stability
- Treat output variance under perturbation as uncertainty
- Use adversarial or ambiguous reformulations to expose fragility
- Flag unstable answers for abstention or clarification

## Verbalized and In-Dialogue Uncertainty
- Detect hedge language as an implicit uncertainty signal
- Use verbalized uncertainty as a complement to statistical signals
- Prefer in-dialogue uncertainty for unanswerable question detection
- Avoid relying solely on explicit “confidence prompting”

## Reflection and Self-Assessment
- Ask the model to critique or reassess its own answer
- Use self-identified doubts as uncertainty evidence
- Compare pre- and post-reflection answers for consistency
- Treat changing answers after reflection as increased uncertainty

## Multi-Step and Agentic Uncertainty
- Estimate uncertainty at every reasoning or action step
- Propagate step-level uncertainty across trajectories
- Aggregate uncertainty over the full multi-step episode
- Avoid assuming independence across sequential decisions
- Weight uncertainty by situational relevance and observation quality

## Calibration and Post-Hoc Adjustment
- Apply temperature scaling to reduce overconfidence
- Use Platt scaling or isotonic regression when labels are available
- Tune calibration using held-out validation data
- Evaluate calibration separately from accuracy
- Monitor calibration drift over time

## Abstention and Deferral
- Use uncertainty thresholds to decide when not to answer
- Prefer abstention over overconfident incorrect outputs
- Optimize accuracy–abstention trade-offs for deployment goals
- Accept small false refusals to reduce hallucinations
- Treat abstention as a core safety and reliability mechanism

## Training-Time Calibration
- Fine-tune models to express uncertainty when appropriate
- Train models to say “I don’t know” on uncertain inputs
- Penalize overconfident errors during preference learning
- Add lightweight calibration heads when feasible
- Optimize selective prediction objectives during training

## Uncertainty-Guided Agent Control
- Use uncertainty to trigger clarification questions
- Use uncertainty to request human assistance
- Use uncertainty to defer decisions in high-stakes contexts
- Integrate uncertainty into planning and control policies
- Treat uncertainty as a control signal, not just a diagnostic

## Domain-Specific Deployment Practices
- Require evidence or retrieval support for factual claims
- Increase uncertainty when evidence is missing or conflicting
- Use runtime checks and tests to reduce code-generation uncertainty
- Abstain or escalate when uncertainty exceeds domain thresholds
- Surface uncertainty explicitly in high-risk applications
