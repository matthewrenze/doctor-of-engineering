# Summary of Best Practices for Alignment of LLM Agents

## Define Alignment Targets
- Write explicit target behaviors (helpful, honest, harmless) as testable requirements
- Specify non-goals and forbidden behaviors (deception, manipulation, unsafe tool actions)
- Separate outer-alignment targets (what you want) from inner-alignment risks (what it learns)
- Scope alignment by capability tier (chat-only vs tool-using vs autonomous)

## Train for Multi-Turn Agent Behavior
- Collect preference feedback on full multi-step trajectories, not single turns
- Optimize for “safe completion” of tasks, not just task success
- Use preference-based fine-tuning (e.g., DPO/RLHF-style) on agent traces
- Use multi-objective signals (helpfulness vs harmlessness) and tune trade-offs explicitly
- Add adversarial training examples that include prompt injection + tool misuse attempts

## Use Principle-Based Constraints
- Encode a short, explicit “constitution” of policies the agent must follow
- Require policy-check reasoning before finalizing risky outputs or actions
- Train/finetune with critique-and-revision data that references written policies
- Prefer actionable constraints (“must ask for confirmation before X”) over vague values

## Add Independent Oversight
- Separate roles: planner/actor vs safety reviewer/evaluator
- Require plan approval before executing multi-step or high-impact actions
- Use debate/critique passes (second model instance) for policy and risk review
- Escalate to human review for pre-defined high-risk categories

## Control Memory to Prevent Drift and Injection
- Persist the user’s approved goals and constraints across turns (“instruction persistence”)
- Treat retrieved memory and tool outputs as untrusted until reviewed
- Filter what gets stored; avoid retaining harmful content or unverified claims
- Add periodic “context audits” that restate goals, constraints, and current plan
- Reset or quarantine context when injection is detected

## Make Planning Safer by Construction
- Force a plan-first format for long-horizon tasks
- Insert step-level safety checks between plan steps and before each tool call
- Use checkpoints for irreversible actions (payments, messages, deletion, submissions)
- Require explicit user confirmation for any action that changes external state

## Harden Tool Use
- Restrict tools via least privilege (minimal set, minimal scopes)
- Enforce strict schemas and argument validation for every tool call
- Sandbox execution (code, browsing, file ops) with resource and permission limits
- Filter tool outputs before the agent can use them (prompt-injection sanitization)
- Log and review tool-call traces; alert on anomalous sequences

## Monitor and Intervene at Runtime
- Cap autonomy: max steps, max spend, max retries, max time
- Add confidence/uncertainty triggers that switch to “ask” or “stop”
- Run output moderation and policy checks on every user-visible response
- Use staged rollout: sandbox → limited users → expanded autonomy
- Keep a reliable kill switch and an out-of-band human override path

## Build Safety Architecture Layers
- Put an input filter in front of the agent to detect jailbreaks/injection early
- Put an output filter after the agent to block or rewrite unsafe content
- Use a dedicated safety agent for nuanced decisions (not just keyword filters)
- Add hierarchical safety gates at every delegation boundary in multi-agent systems
- Prefer simpler architectures when risk is low; add layers as risk increases

## Evaluate and Iterate Like Engineering
- Evaluate alignment on realistic agent tasks (tool use + multi-step workflows)
- Measure “harmful compliance” and “capability retention” after safety training
- Stress-test with jailbreak-style prompts and multi-turn escalation attempts
- Track regressions over time; re-run alignment evals continuously post-deploy
- Turn failures into new training data and new automated tests
