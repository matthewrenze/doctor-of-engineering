# Summary of Eval Best Practices

## 1. General Evaluation Principles

* Define clear success criteria before evaluating
* Use both automated metrics and human judgment
* Combine offline benchmarking with online monitoring
* Maintain fixed, versioned regression test sets
* Track performance across model and agent updates

## 2. Evaluating LLMs (Model-Level)

### 2.1 Benchmarking

* Benchmark on standard academic tasks (e.g. MMLU, TruthfulQA)
* Use domain-specific custom test sets for fine-tuned models
* Select metrics that align with the task (e.g. F1, BLEU, pass\@k)
* Prefer semantic metrics over surface-level metrics when needed

### 2.2 Safety and Bias

* Probe models with adversarial or sensitive queries
* Score for toxicity, bias, and policy violations
* Use classifiers or LLMs-as-judges to detect unsafe outputs

## 3. Evaluating Agents (System-Level)

### 3.1 Goal Completion

* Measure task success and completion rates
* Use realistic, end-to-end task scripts
* Validate agent behavior across diverse input scenarios

### 3.2 Reasoning and Planning

* Log and inspect reasoning traces and tool use
* Evaluate intermediate decisions for correctness
* Track efficiency (e.g. number of steps, API calls)

### 3.3 Interaction and Memory

* Test multi-turn coherence and context retention
* Evaluate memory consistency over long sessions
* Check if agent adapts to new information mid-dialogue

### 3.4 Tool Use and API Integration

* Score tool selection accuracy
* Verify input/output correctness for tool calls
* Flag redundant, invalid, or inefficient tool use

### 3.5 Multi-Agent Behavior

* Evaluate agent coordination and communication
* Check information sharing and action synchronization
* Monitor redundancy or conflict in agent decisions

## 4. Human Feedback and Alignment

* Involve human reviewers for subjective evaluation
* Use standardized rubrics for human rating consistency
* Collect pairwise preference data for reward modeling
* Train reward models to align with human judgments
* Update training and eval sets with flagged failure cases

## 5. Automated and LLM-Based Evaluation

* Use LLM-as-a-judge for scalable evals
* Provide clear rubric prompts to LLM evaluators
* Validate AI judges against human ratings
* Route low-confidence or high-stakes cases to humans
* Simulate agent interactions for stress-testing

## 6. Deployment Evaluation and Monitoring

* Log all interactions, tool calls, and metadata
* Sample interactions for live evals (random + targeted)
* Score outputs in real-time using automated tools
* Incorporate explicit and implicit user feedback
* Trigger alerts for safety or quality threshold violations
* Perform root-cause analysis of evaluation failures

## 7. Metrics and Evaluation Infrastructure

* Limit to a small set of interpretable core metrics
* Design custom metrics for system-specific tasks
* Use open-source eval frameworks for consistency
* Prefer customizable tools supporting open models
* Version and document all evaluation assets
* Ensure full transparency and reproducibility
