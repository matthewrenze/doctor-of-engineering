# Benchmarks for Uncertianty in LLM Agents

## Uncertainty Benchmarks and Datasets (from attached docs)

- AmbigQA: QA dataset designed around ambiguous questions with multiple valid interpretations/answers; evaluates ambiguity (aleatoric uncertainty) handling, uncertainty-aware clarification vs confident single-answering
- AmbigInst: Instruction-style ambiguous-query dataset; evaluates uncertainty under underspecification and whether agents surface uncertainty or ask clarifying questions
- AttaQ: Attack-style adversarial prompt set used to induce unsafe behavior; evaluates whether uncertainty scores can help abstain from unsafe responses (safety-oriented uncertainty)
- AutoDAN: Automated jailbreak/adversarial attack benchmark; evaluates safety uncertainty for abstention/filtering under adversarial inputs
- CalibratedMath: Math-focused calibration benchmark; evaluates probability calibration and uncertainty quality on mathematical reasoning (often where overconfidence is common)
- CoQA: Conversational QA dataset; evaluates uncertainty in multi-turn QA where context accumulation can cause compounding uncertainty
- FActScore: Factual consistency scoring benchmark/protocol for long-form generation; evaluates uncertainty for factuality/hallucination risk in generated text
- FEVER: Fact verification dataset (claims supported/refuted/not enough info); evaluates uncertainty for factuality and “known-unknown” detection (abstain when evidence is missing)
- GPQA: Graduate-level, difficult QA benchmark; evaluates uncertainty under hard questions where models should be less confident and abstain/hedge appropriately
- GSM8K: Grade-school math word problems; evaluates uncertainty calibration and abstention effectiveness on step-by-step quantitative reasoning
- HaluEval: Hallucination evaluation benchmark; evaluates uncertainty signals for hallucination detection/abstention
- HellaSwag: Commonsense inference benchmark; evaluates uncertainty under commonsense completion where distribution-shift and spurious cues can affect confidence
- HotpotQA: Multi-hop QA requiring combining evidence across documents; evaluates step-wise/trajectory uncertainty in multi-step reasoning agents (propagation across steps)
- LM-Polygraph: Uncertainty estimation benchmark suite/tooling used to compare UQ methods across tasks; evaluates robustness of uncertainty metrics across datasets/models
- MMLU: Broad multi-domain knowledge benchmark; evaluates uncertainty across heterogeneous subject areas (domain-dependent miscalibration/uncertainty quality)
- ParaRel: Factual knowledge probing via paraphrased relation prompts; evaluates uncertainty under paraphrase sensitivity and prompt-variation instability
- SciQA: Science QA dataset; evaluates uncertainty on technical/science questions (often used for correctness-oriented abstention)
- SelfAware: Unanswerable/“I don’t know” style dataset; evaluates known-unknown detection and abstention/hedging behavior
- StrategyQA: Implicit reasoning QA dataset; evaluates uncertainty in multi-step reasoning and abstention/selection when confidence is low
- TriviaQA: Open-domain trivia QA; evaluates correctness uncertainty and abstention tradeoffs in factual recall settings
- TruthfulQA: Benchmark targeting false-but-plausible answers; evaluates uncertainty for resisting hallucinations and signaling low confidence on misleading prompts

## Evaluation Metrics/Protocols Referenced (used to score uncertainty, not datasets)

- Expected Calibration Error (ECE): Bucketed gap between predicted confidence and empirical accuracy; evaluates calibration quality
- Brier Score: Proper scoring rule (squared error of predicted probabilities); evaluates both calibration and sharpness of probabilistic uncertainty
- Reliability Diagrams: Confidence vs accuracy plot; visual calibration diagnostic
- AUROC / AUPR (discrimination): How well uncertainty ranks correct vs incorrect (or safe vs unsafe); evaluates separability/ranking quality
- Accuracy–Rejection Curve: Accuracy as a function of abstention rate; evaluates abstention usefulness for correctness/hallucination/safety
- AUARC: Area under the Accuracy–Rejection Curve; aggregate abstention-performance metric
