# Summary of Evaluating AI Agents (course)

## 1. Foundations of Agent Evaluation

* Evaluation-driven development
  * Use evals to guide design choices (e.g., prompts, logic, LLMs)
  * Avoid trial-and-error; build systematically

* Two layers of evaluation
  * LLM model evaluation (e.g., MMLU, HumanEval)
  * LLM app/system evaluation (tools, routing, prompts, etc.)

* LLM agents = non-deterministic systems
  * More like cars in traffic than trains on tracks
  * Requires qualitative, not just pass/fail tests

* Common evaluation targets
  * Hallucination
  * Retrieval relevance
  * QA accuracy
  * Toxicity
  * Overall performance

---

## 2. Agent Architecture and Components

* Core agent components
  * Router (planner) - decides which skill to call
  * Skills (tools) - perform tasks (e.g., RAG, SQL)
  * Memory/state - stores history, context, config

* Routing options
  * Rules-based - simple, deterministic
  * NLP classifier - mid-level complexity
  * LLM w/ function calling - flexible but less reliable

* Skills as logic units
  * LLM calls, application code, API calls
  * Can include multi-step logic (e.g., RAG pipelines)

---

## 3. Observability and Tracing

* Observability concepts
  * Visibility into prompts, responses, token usage
  * Essential for debugging and improvement

* Traces and spans
  * Trace = full agent run
  * Span = individual "span" of code 
    * (e.g., function call, LLM call, tool call, block of code, etc.)
  * Spans are nested (hierarchically) to show structure

* Instrumentation
  * Manual or automated (via LangChain, LlamaIndex, etc.)
  * Tools like Arize Phoenix visualize traces

* Use cases
  * Debugging during development
  * Monitoring in production
  * Basis for structured evaluations

---

## 4. Evaluation Techniques

* Three main evaluator types:
  * Code-based - regex, JSON parse, ground truth match
  * LLM-as-a-Judge - separate LLM evaluates outputs
  * Human annotations - labeling via UI or end-user feedback

* Tradeoffs
  * Code-based: deterministic, scalable, brittle
  * LLM-as-a-Judge: scalable, semi-reliable, flexible
  * Human labels: highest quality, labor-intensive, not easily scalable

* LLM-as-a-Judge tips
  * Use high-quality models (GPT-4o, Claude 3.5)
  * Prefer discrete labels (e.g., correct/incorrect)
  * Tune prompts, use few-shot examples
  * Evaluate judges with ground-truth experiments

---

## 5. Evaluating Agent Subcomponents

* Router evaluations
  * Function/tool selection accuracy
  * Parameter extraction correctness

* Skill evaluations
  * SQL generation correctness (code or LLM eval)
  * Analysis clarity, factuality (LLM-as-a-Judge)
  * Code generation validity (e.g., code runs)

* Best practices
  * Evaluate both full skill and substeps
  * Choose eval method based on metric type and required accuracy

---

## 6. Evaluating Trajectory (Path)

* Trajectory - path taken by agent per task
  * Tool sequence, decision steps, action sequence

* Why it matters
  * Efficiency - fewer steps is faster, cheaper, less variablilty

* Convergence score
  * Measures % of runs that take optimal path
  * Take min(steps) of n task runs to find pseudo-optimal path
  * Score = 1.0 means always optimal  

* Best practices
  * Use similar-but-varied inputs
  * Track only successful runs
  * Watch for common inefficiencies

---

## 7. Structuring Evaluation Experiments

* Evaluation-driven development process
  * Curate test dataset (comprehensive > exhaustive)
  * Run test cases through agent variants (model, prompt, logic)
  * Apply evaluators to outputs
  * Compare results to guide iteration

* Agent experiment examples
  * Test tool descriptions on router performance
  * Test SQL prompt quality in data lookup skill
  * Test LLM model in analysis clarity skill

* Outputs
  * Dashboard/score matrix for comparing changes
  * Continuous feedback loop: dev <-> prod

---

## 8. Production Monitoring and Continuous Improvement

* Production adds complexity
  * More tools, more user variability
  * New failure modes (e.g., unseen queries, API errors)

* Reuse dev tools in production
  * Observability (traces, spans)
  * Evals (LLM, code-based, human)
  * Experimentation pipelines (CI/CD)

* Golden datasets
  * Maintain critical and failure cases for regression testing
  * Get these from production failures

* Self-improving agents
  * Incorporate real user feedback
  * Continuously update eval sets
  * Automate re-eval for each deployment
