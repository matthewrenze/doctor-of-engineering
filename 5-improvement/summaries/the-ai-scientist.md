# The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery

## Background and Motivation
- Use In-Context Learning Techniques
  - Few-shot prompting for task grounding
  - Chain-of-thought prompting for reasoning transparency
  - Iterative self-reflection to refine outputs

## Overall Self-Improving Agent Loop
- Structure Agents as Closed-Loop Systems
  - Archive prior outputs, ideas, and feedback
  - Condition future generations on historical artifacts
  - Enable open-ended iteration across runs

## Idea Generation Phase
- Maintain an Archive of Prior Ideas
  - Store descriptions, experiment plans, and self-scores
  - Use archive as conditional context for new ideas
- Promote Diversity and Novelty
  - Prompt generation conditioned on existing archive
  - Use evolutionary-style mutation via LLMs
- Use Multi-Round Reasoning
  - Apply chain-of-thought for ideation
  - Apply self-reflection to refine and critique ideas
- Self-Evaluate Ideas Early
  - Score ideas for novelty, feasibility, and interestingness
- Filter Against Existing Knowledge
  - Use web search and Semantic Scholar APIs
  - Discard ideas too similar to prior literature

## Experiment Iteration Phase
- Start from Minimal, Reproducible Templates
  - Use small-scale baseline experiments
  - Optimize for fast iteration and low compute cost
- Plan Experiments Explicitly
  - Generate ordered experiment plans before execution
- Execute with Robust Error Recovery
  - Detect failures and timeouts
  - Automatically fix and retry code multiple times
- Record Experimental Memory
  - Maintain experiment journals with notes and outcomes
  - Preserve full execution history
- Adapt Plans Based on Results
  - Re-plan experiments conditional on observed outcomes
  - Limit iteration depth to control cost and drift
- Automate Visualization
  - Generate plots programmatically
  - Attach semantic descriptions to each figure

## Paper Write-Up Phase
- Generate Text Incrementally
  - Write sections sequentially using accumulated context
  - Follow standardized paper structure
- Ground Writing in Artifacts
  - Restrict content to real results, notes, and figures
  - Avoid hallucinated claims
- Use Self-Reflection During Writing
  - Refine each section with reflection passes
  - Remove redundancy and verbosity
- Separate Citation Discovery from Writing
  - Perform targeted web search for references
  - Insert citations after core text is written
- Enforce Compilation Correctness
  - Run LaTeX compilation automatically
  - Use linters and error feedback loops

## Automated Review and Feedback
- Use LLMs as Reviewers
  - Follow real conference review guidelines
  - Produce scores, strengths, weaknesses, and decisions
- Improve Reviewer Reliability
  - Apply few-shot prompting
  - Apply multi-round self-reflection
  - Ensemble multiple reviews
- Meta-Aggregate Reviewer Outputs
  - Perform higher-level synthesis of reviews
  - Reduce variance across judgments
- Archive Reviews for Future Conditioning
  - Feed reviewer feedback back into idea archive

## Model and System Design Choices
- Prefer Model-Agnostic Architectures
  - Support proprietary and open models interchangeably
- Favor Open Models for Long-Term Self-Improvement
  - Lower cost and better availability
  - Greater transparency and control
- Optimize for Cost Efficiency
  - Constrain experiment scale
  - Track per-run and per-paper costs

## Safety, Reliability, and Future Self-Improvement
- Link Claims Directly to Executed Code
  - Preserve traceability from result to implementation
- Enable Post-Hoc Human Inspection
  - Archive artifacts for interpretability
- Plan for Self-Referential Improvement
  - Allow agents to modify and improve their own code
- Address Hallucination Risks Explicitly
  - Ground outputs in executable artifacts
  - Explore automated verification and reproduction

---

## Benchmarks and Datasets Referenced
- SWE-Bench
- ICLR 2022 OpenReview Dataset
- NeurIPS 2021 Reviewer Consistency Dataset
- Shakespeare Character-Level Language Modeling
- Enwik8
- Text8
