# LLM Agent Tool-Use Best Practices

## 1. Tool specification and interfaces

* Define each tool with clear name, purpose, JSON input schema, output schema, and error schema
* Keep descriptions short, capability-focused, and example-driven
* Prefer deterministic, schema-validated function calls over free-form text
* Version tools and document breaking changes with migration notes
* Provide minimal, targeted outputs to reduce context bloat

## 2. Planning for tool use

* Use plan-then-execute or ReAct loops for multi-step tasks
* Represent plans in JSON steps for executability and traceability
* Include explicit success criteria, stop conditions, and fallback branches
* Budget cost/latency per plan and enforce call caps per task
* Prefer multi-step planning with verification feedback for higher pass rates

## 3. Tool discovery, retrieval, and routing

* Maintain a tool registry with searchable metadata and examples
* Use hybrid retrieval (sparse+dense) to shortlist tools for the model
* Re-rank candidates with task-aware signals and prior usage success
* Add self-checks (e.g., “am I choosing the right tool?”) before invocation
* Organize tools hierarchically or as a graph to improve navigation

## 4. Decision: when to call a tool

* Prefer model-only answers for simple, closed-book queries
* Call tools when information is out-of-date, unseen, or requires computation
* Calibrate thresholds to avoid over-calling low-value tools
* Encourage think → decide → act scaffolds with an explicit “no-tool” option
* Log counterfactuals (what would have happened without the tool) for tuning

## 5. Parameterization and invocation

* Extract arguments with few-shot examples mapped to the JSON schema
* Validate and coerce types; default missing but safe fields explicitly
* Use reverse-chaining: pick end-goal tool first, infer prerequisites backward
* Retry on transient failures with bounded exponential backoff
* For long jobs, use async patterns with job IDs and status polling

## 6. Response handling and integration

* Summarize or compress verbose tool outputs before reinjection to context
* Prefer evidence-first integration: cite or quote key snippets, then reason
* Normalize heterogeneous outputs to a common intermediate schema
* Distinguish observations from conclusions to prevent premature closure
* Preserve source provenance for downstream audit and user trust

## 7. Error handling and repair

* Classify failures: selection error, argument error, execution error, response misuse
* Apply targeted repairs: re-route, re-arg, retry, or request clarification
* Limit recursive repair depth and escape to fallback or human review
* Capture rich error telemetry for root-cause analysis and prompt/tool fixes
* Use safe defaults and “fail closed” behavior for high-risk actions

## 8. Safety, security, and policy compliance

* Sanitize inputs/outputs to defend against prompt injection via tools
* Enforce allow-lists and permission scopes per tool and per user
* Require user identity verification before sensitive operations
* Gate irreversible changes behind explicit confirmations and summaries
* Isolate execution (sandboxes) for code, file, and web tools

## 9. Cost, latency, and reliability optimization

* Cache expensive or stable results within and across sessions
* Batch calls when APIs support it; parallelize independent steps with limits
* Throttle concurrency to protect upstream services and avoid rate limits
* Prefer lightweight tools and streaming responses where possible
* Track per-tool SLOs and degrade gracefully to cheaper/faster fallbacks

## 10. Observability and auditing of tool use

* Log every decision → call → response → integration step with metadata
* Capture inputs, normalized outputs, latency, cost, and success labels
* Redact secrets while preserving forensic value and reproducibility
* Surface live traces for debugging and post-mortems
* Version prompts, plans, and tool specs to tie behavior to artifacts

## 11. Evaluation specific to tool use

* Evaluate by stage: planning (awareness, plan accuracy), selection (tool-F1, Recall\@K), calling (argname-F1, format correctness), execution (pass rate)
* Score response integration for grounding, coherence, and completeness
* Run pass^k trials to measure reliability under sampling
* Compare with and without tools to quantify marginal utility
* Include domain policy compliance checks in task scoring

## 12. Data and memory hygiene around tools

* Store structured traces for long-term learning, not raw tool dumps
* Distill large outputs into reusable notes or embeddings with provenance
* Refresh or expire cached data based on source TTLs
* Keep training/fine-tune corpora free from sensitive tool outputs unless consented
* Separate short-term scratchpads from long-term memory with explicit gates

## 13. Training and adaptation for tool competence

* Fine-tune or augment with tool-use exemplars and filtered self-generated calls
* Mix seen and synthetic unseen tools to reduce overfitting to specific APIs
* Reinforce good behaviors with outcome-conditioned feedback signals
* Use localized verification feedback to improve argument naming and executability
* Continually mine failure cases to update prompts, routers, and specs

## 14. Interaction UX for tool actions

* Announce intended action, summarize inputs, and request confirmation when needed
* Provide structured, scannable summaries of tool results to users
* Offer “why this tool” and “what else could we try” affordances
* Support undo/rollback paths for reversible operations
* Escalate gracefully to human help when confidence or scope is insufficient

## 15. Governance and change management

* Treat tools as governed assets with owners, SLAs, and access reviews
* Run pre-deployment checklists: schema validation, sandbox tests, red-team prompts
* Canary updates and roll back on degraded pass rate or latency SLOs
* Document assumptions, constraints, and known failure modes per tool
* Align monitoring alerts to business impact, not just technical failures
