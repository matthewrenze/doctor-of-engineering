# Calibration Methods for LLMs

## White-box Calibration

### Post-hoc Calibration
- Temperature scaling – apply scalar to logits to calibrate softmax probabilities  
- Platt scaling – fit logistic regression on model scores to improve calibration  
- Isotonic regression – use non-parametric regression for more flexible calibration  
- Histogram binning – partition predictions into bins and calibrate using empirical accuracy  
- Bayesian binning averaging (BBA) – ensemble multiple binning strategies for robust calibration  

### Training-Time Calibration
- Label smoothing – prevent overconfidence by softening target distributions  
- Confidence penalty – add entropy-maximizing regularization to loss  
- Focal loss – down-weight easy examples to mitigate overconfidence  
- Bayesian training – train with distributions over weights for calibrated uncertainty  

---

## Black-box Calibration

### Prompt Engineering
- Confidence elicitation tuning – fine-tune prompts that extract more reliable self-reported confidence  
- Self-reflection chains – calibrate outputs via iterative reasoning and self-critique  
- Consistency-based calibration – use agreement across sampled or paraphrased prompts to adjust confidence  

### Output-Level Calibration
- Empirical recalibration – compare predicted confidence to observed accuracy over a labeled validation set  
- Meta-model calibration – train an external model to map predictions to calibrated confidence scores  
- Ranking-based methods – reorder outputs using external calibrators without modifying LLM outputs  

### Evaluation-Based Calibration
- Expected calibration error (ECE) – measure the gap between predicted confidence and true accuracy  
- Brier score – penalize incorrect or overconfident predictions using squared error of probabilities  
- Log-likelihood – evaluate how well predicted probabilities match actual outcomes