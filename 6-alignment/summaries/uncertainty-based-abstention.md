# Uncertainty-Based Abstention in LLMs Improves Safety and Reduces Hallucinations

## Problem Framing and Motivation
- Treat abstention as a first-class action for unreliable LLM outputs
- Use uncertainty to decide when not to answer rather than forcing an answer
- Target three failure modes: incorrect answers, hallucinations, unsafe responses

## Types of Uncertainty
- Distinguish statistical uncertainty from verbalized uncertainty
- Match uncertainty type to task setting rather than using a single metric everywhere
- Prefer uncertainty measures that require no additional prompting or finetuning

## Statistical Uncertainty Estimation
- Use token-level probability distributions to estimate confidence
- Prefer negative log-likelihood for single-pass uncertainty estimation
- Use predictive entropy for multi-sample uncertainty estimation
- Use semantic entropy to capture meaning-level diversity across generations
- Prefer semantic entropy over lexical entropy for RLHF-finetuned models
- Avoid explicit uncertainty elicitation prompts due to brittleness and overhead

## In-Dialogue Uncertainty (InDU)
- Leverage natural hedge words as implicit uncertainty signals
- Measure uncertainty via hedge-word frequency in generated responses
- Treat verbalized uncertainty as complementary to statistical uncertainty
- Prefer In-Dialogue Uncertainty for detecting unanswerable questions
- Exploit RLHF-enhanced human-like uncertainty expressions

## Correctness-Oriented Abstention
- Use statistical uncertainty to identify likely incorrect answers
- Apply uncertainty thresholding to reject high-risk responses
- Improve overall accuracy by abstaining on most-uncertain samples
- Use Accuracy–Rejection Curves to evaluate abstention effectiveness
- Prefer AUARC over calibration metrics for free-form QA evaluation
- Expect RLHF to preserve uncertainty ranking despite miscalibration

## Hallucination Reduction for Unanswerable Questions
- Treat unanswerable questions as a distinct uncertainty regime
- Use In-Dialogue Uncertainty instead of statistical uncertainty
- Detect unanswerable questions via hedge-word usage
- Reduce hallucinations by abstaining when InDU exceeds threshold
- Accept small false-refusal rates to substantially reduce hallucinations
- Exploit RLHF to amplify InDU signal for known-unknown detection

## Safety-Oriented Abstention
- Use statistical uncertainty to identify unsafe responses
- Apply abstention on RLHF-finetuned models rather than base models
- Avoid In-Dialogue Uncertainty for safety detection
- Filter unsafe responses via uncertainty thresholding
- Achieve large safety gains with minimal abstention rates
- Use abstention as a lightweight safety layer on top of alignment

## Evaluation Methodology
- Use AUROC to assess uncertainty quality across tasks
- Use Accuracy–Rejection Curves to measure abstention benefits
- Evaluate uncertainty separately for correctness, hallucinations, and safety
- Validate automatic metrics against human judgments
- Prefer fuzzy exact match over exact match for correctness labeling

## Practical Deployment Guidance
- Choose uncertainty metric based on failure mode
- Prefer abstention over overconfident incorrect answers
- Use uncertainty as a low-cost reliability improvement
- Accept abstention trade-offs in high-stakes applications
- Treat uncertainty as a core capability, not an auxiliary feature

---

## Benchmarks and Datasets Referenced
- TriviaQA
- SciQA
- CoQA
- StrategyQA
- GSM8K
- SelfAware
- AutoDAN
- AttaQ

