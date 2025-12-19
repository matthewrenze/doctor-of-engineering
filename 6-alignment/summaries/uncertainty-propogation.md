# SAUP: Situation Awareness Uncertainty Propagation on LLM Agent

## Uncertainty Estimation Scope
- Account for uncertainty across the full multi-step agent trajectory
- Estimate uncertainty beyond final outputs to include intermediate reasoning states
- Incorporate environment interaction effects into uncertainty estimates

## Uncertainty Propagation
- Propagate one-step uncertainty estimates across sequential reasoning steps
- Aggregate step-wise uncertainties into a global trajectory-level uncertainty
- Preserve temporal ordering of uncertainty accumulation
- Avoid treating multi-step decisions as independent samples

## Situational Awareness Weighting
- Weight step uncertainties based on situational relevance
- Adjust uncertainty contribution using reasoning progress and context
- Incorporate observation quality into uncertainty weighting
- Adapt weighting strategies to task and environment dynamics

## Surrogate Modeling
- Use surrogate signals to estimate unobservable situational context
- Approximate hidden environment states affecting uncertainty
- Enable uncertainty estimation when direct signals are unavailable

## Method Modularity
- Support multiple one-step uncertainty estimation techniques
- Design uncertainty propagation as a plug-in compatible framework
- Allow substitution or combination of uncertainty estimators
- Maintain estimator-agnostic propagation logic

## Evaluation and Validation
- Evaluate uncertainty quality using multi-step agent benchmarks
- Compare propagated uncertainty against single-step baselines
- Validate robustness across diverse reasoning tasks

## Performance Interpretation
- Measure uncertainty estimation quality using ranking-based metrics
- Analyze uncertainty calibration under difficult reasoning conditions
- Assess relative gains from situational weighting strategies

## Benchmarks Referenced
- HotpotQA
- StrategyQA
- MMLU
