# Uncertainty Quantification in LLMs

## White-box Methods  

### Logit-Based
- Max softmax probability – use the highest softmax probability
- Entropy of output distribution – measure entropy over logits
- Margin between top logits – compute difference between top-2 logits
- Monte Carlo Dropout – use dropout at inference to simulate posterior samples

### Sampling-Based
- Self-consistency – sample multiple outputs and measure agreement  
- Log probability mean/variance – analyze statistics over sampled outputs  
- Sampling + Entropy/JS divergence – estimate uncertainty over diverse generations  

### Model-Based
- Bayesian neural networks (BNNs) – maintain distributions over weights  
- Deep ensembles – average predictions from multiple fine-tuned LLMs  

---

## Black-box Methods 

### Prompt-Based
- Confidence elicitation – ask the model to estimate its own confidence  
- Self-reflection – ask the model to critique its answer first
- Chain-of-thought verification – evaluate internal reasoning consistency  

### Output Analysis
- Sampling agreement – generate n completions and measure diversity/agreement  
- Input Permutation – rephrase input n times and compare outputs  
- External LLM judge – use another model to assess answer correctness  

### Surrogate Measures
- Embedding distance – compare output embeddings to known/canonical answers  
- Retrieval confidence – measure confidence based on similarity of retrieved context