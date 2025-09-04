# Best Practices Summaries

##  Toolformer: Language Models Can Teach Themselves to Use Tools

### Introduction: Principles for Tool Use

* Learn tool use in a self-supervised way, not heavy human annotation
* Let model decide when and how to use tools, not tied to specific tasks
* Preserve general language modeling ability while adding tool use

### Approach: Training Method

* Represent APIs with text sequences using special tokens
* Use few human-written examples per API to bootstrap
* Sample candidate API calls via in-context learning
* Execute candidate calls with real APIs
* Filter calls by measuring loss reduction on next tokens
* Finetune model on original data plus filtered API calls
* Train on same dataset as pretraining to preserve generality
* During inference, insert API responses when “→” token is produced

### Tools: Design Choices

* Inputs/outputs must be text sequences
* Require only a few usage demonstrations per tool
* Use simple, general-purpose APIs: QA, Wikipedia search, calculator, calendar, machine translation
* Provide minimal, targeted responses (QA → factoid, calculator → basic arithmetic, etc.)

### Experiments: Evaluation Practices

* Evaluate zero-shot without in-context task-specific examples
* Compare with stronger baselines and larger models
* Limit API calls per input to prevent infinite loops
* Allow API token if among top-k likely tokens (not only most likely)
* Ensure API integration does not harm perplexity on LM benchmarks

### Scaling and Model Size

* Tool use emerges only above \~775M parameters
* Larger models improve both without tools and with tools
* Maintain a clear performance gap with and without tools

### Analysis: Practical Insights

* Adjust decoding strategy (k > 1) to encourage API calls
* Model shows calibration when k = 1 (calls APIs when needed most)
* High filtering scores usually correlate with useful API calls
* Some noise in API calls can improve robustness (model not blindly trusting APIs)

### Related Work and Positioning

* Unlike prior work, Toolformer avoids heavy supervision
* Enables general-purpose, task-agnostic tool use
* Uses bootstrapping with self-generated data plus filtering

### Limitations: Known Gaps

* No support for chaining multiple tools
* No interactive tool use (e.g., refining queries, browsing results)
* Sensitive to prompt wording
* Sample-inefficient for some APIs (e.g., calculator)
* Ignores computational cost of API calls

### Benchmarks Referenced

* **Knowledge/facts**: LAMA (SQuAD, Google-RE, T-REx), TEMPLAMA, DATESET
* **Math**: ASDiv, SVAMP, MAWPS
* **QA**: WebQuestions, Natural Questions, TriviaQA
* **Multilingual QA**: MLQA
* **Language modeling**: WikiText, CCNet

---

## Tool Learning with Large Language Models: A Survey

### General paradigm

* Break tool learning into four stages: task planning → tool selection → tool calling → response generation
* Prefer iterative/feedback-based task solving over single-step planning
* Combine retrieval-based narrowing with LLM-based reasoning for tool selection

### Task planning

* Use chain-of-thought or reasoning+acting (e.g., ReAct) for decomposing tasks
* Retrieve task exemplars (few-shot) from a task library to guide planning
* Refine plans iteratively (coarse-to-fine, clustering, summarizing progress)
* Represent tool usage space as decision trees or graphs for structured exploration
* Incorporate budget/cost constraints into planning
* Use feedback from tools to adjust or repair plans dynamically
* Fine-tune with API call data to improve planning reliability (Toolformer, etc.)
* Generate synthetic datasets of tool usage for training planners

### Tool selection

* Use retrievers to filter large tool libraries before passing to LLMs
* Employ hybrid retrieval: sparse (BM25) + dense (Sentence-BERT, Contriever)
* Re-rank retrieved tools with adaptive, hierarchy-aware methods
* Use LLM reasoning (CoT, ReAct) to select tools based on query context
* Organize tools into graphs or hierarchies to improve navigation
* Add self-verification/self-questioning to reduce mis-selection
* Fine-tune with tool usage datasets for improved tool discrimination

### Tool calling

* Extract parameters via few-shot demonstrations or schema prompts
* Rewrite or compress tool documentation for clarity and shorter context
* Use reverse chaining: select end-goal tool first, then infer required inputs
* Delegate parameter extraction to specialized sub-agents for robustness
* Fine-tune models to encode tool call formats directly (e.g., special tokens/tool embeddings)
* Add automatic error handling and repair when tool calls fail
* Avoid over-reliance on seen tools by mixing in synthetic unseen tools for training

### Response generation

* Prefer information integration methods over direct insertion of tool outputs
* Compress or summarize long tool outputs before re-feeding to LLM
* Use schema-free adaptive extraction for unstructured outputs
* Refine generated responses using tool feedback loops
* Validate tool outputs before integration to mitigate adversarial/harmful inputs

### Evaluation and benchmarks

* Evaluate each stage independently (planning, selection, calling, response)
* Use awareness, pass rate, and accuracy for planning
* Use Recall\@K, NDCG, COMP for selection
* Enforce strict parameter/format compliance for calling
* Evaluate responses with BLEU, ROUGE, Exact Match, F1

### Challenges / meta-practices

* Reduce latency by avoiding unnecessary tool calls and keeping tools lightweight
* Develop unified frameworks spanning all four stages (avoid fragmented solutions)
* Build real-world benchmarks with authentic user queries (not just LLM-generated)
* Extend tool learning to multi-modal inputs for richer tasks
* Ensure robustness and safety: defend against noise, prompt injections, adversarial tool outputs

---

## τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains

### Benchmark design

* Model tasks as partially observable Markov decision processes (POMDPs)
* Require interaction with both simulated users and programmatic APIs
* Provide domain-specific policy documents to enforce rule adherence
* Ensure tasks have unique database outcomes for faithful evaluation
* Use modular benchmark construction: databases, APIs, policies, tasks

### Benchmark construction process

* Stage I: manually design simple but realistic database schemas, APIs, and policies
* Stage II: use LMs to auto-generate large-scale data, refine with manual fixes
* Stage III: manually annotate tasks, validate with agent trials to remove ambiguity

### User simulation

* Simulate users with LMs for diverse, natural, and stochastic utterances
* Guarantee only one possible ground-truth outcome per task instruction
* Use stochastic sampling to test agent consistency across runs

### Evaluation methodology

* Compare final database state with ground-truth outcome (objective evaluation)
* Require agent responses to contain all necessary information for success
* Introduce **pass^k** metric to measure agent reliability across k trials
* Trade quantity for quality: fewer high-quality tasks run multiple times

### Agent requirements

* Authenticate user identity before taking actions
* Provide action details and obtain explicit confirmation before database changes
* Handle only one user per conversation, deny unrelated requests
* Restrict tool use to one call at a time, separate from user responses
* Transfer to human agent only when tasks exceed agent scope
* Never invent knowledge or make subjective recommendations

### Domain-specific practices

* Retail:

  * Cancel or modify only pending orders (with rules on refund/payment methods)
  * Return/exchange only delivered orders, and only once per order
  * Confirm all items to modify/exchange before single allowed action call
* Airline:

  * Enforce strict rules on flight modifications, cancellations, baggage, insurance
  * Check complex conditions (membership, cabin class, timing) before API calls
  * Restrict payments to specific combinations (gift cards, certificates, credit cards)
  * Require full passenger info collection before booking

### Research and evaluation practices

* Run multiple trials per task to capture stochasticity and measure consistency
* Use function calling where possible (outperforms text-based ReAct/Act methods)
* Analyze failure cases systematically (wrong arguments, wrong info, wrong decisions, partial resolutions)
* Test with and without domain policies to measure true rule-following capacity
* Limit tasks to a maximum number of agent actions for practicality (≤30 actions)

### Directions for improvement

* Improve LM simulators (reduce typos/ambiguities, enhance reasoning and memory)
* Increase complexity of domain policies for realism
* Add more evaluation metrics (e.g., rule-following checks beyond database state)
* Explore domain-specific fine-tuning and agent scaffolding for better rule adherence

---

## Model Context Protocol (MCP): Landscape, Security Threats, and Future

### Planning strategy

* Prefer multi-step planning over step-by-step planning
* Multi-step planning improves tool selection (tool-F1)
* Multi-step planning improves executability (pass rate)
* Larger models benefit less but still gain from multi-step planning
* Step-by-step planning risks premature termination after positive feedback

### Plan format

* Use JSON format for plan representation
* JSON leads to more executable plans than code generation
* JSON’s rigid structure reduces parsing and execution errors
* Code generation (Python) performs comparably in tool selection but worse in execution reliability
* Code LLMs (e.g., CodeLlama) narrow the gap but JSON remains safer

### Feedback mechanisms

* Incorporate verification and execution feedback for tool invocation
* Feedback improves argument name prediction (argname-F1)
* Feedback improves executability (pass rate)
* Verification feedback is more helpful than execution feedback for argument naming
* Execution feedback can be vague, leading to incorrect fixes
* Feedback may slightly reduce tool selection accuracy (<5%) but overall benefit outweighs cost
* Use fine-grained and localized feedback to minimize wrong fixes

### Evaluation metrics and design

* Measure tool-F1 for tool selection quality
* Measure argname-F1 for argument accuracy
* Measure pass rate for executability of plans
* Optionally include argvalue-F1, edge-F1, edit distance, plan accuracy, AST accuracy (for code), CodeBLEU
* Consider both step-level and plan-level evaluation

### Dataset and benchmark construction

* Build realistic, executable benchmarks with actual tool implementations
* Avoid synthetic placeholders (e.g., “example.png”)
* Ensure tasks cover multiple modalities (text, image, audio)
* Verify plans with multiple annotators for correctness
* Balance tool usage to prevent bias toward frequent tools
* Support alternative valid plans to account for diversity in tool use

### General takeaways

* Best overall setup: multi-step planning + JSON format + feedback
* Balance tool invocation reliability with tool selection accuracy
* Larger models require less feedback but still benefit from structured planning
* Step-by-step planning does not scale well for complex multi-tool tasks

---

## A Survey of the Model Context Protocol (MCP)

### Architecture

* Use client-server architecture for modularity and scalability
* Maintain one-to-one client-server connections for reliability
* Standardize message formats to simplify integration
* Support asynchronous communication for efficiency
* Implement robust error handling for resilience
* Select transport layer based on use case (stdio for local, HTTP/SSE for remote)
* Use structured message types: requests, results, errors, notifications

### Resources

* Use standardized URIs for discoverability and consistency
* Categorize resources into text (UTF-8) and binary (base64)
* Provide metadata: URI, name, description, MIME type
* Support both static listings and dynamic URI templates
* Enable subscription-based notifications for updates
* Ensure strong security: access control, encryption, input sanitization
* Validate URIs and handle errors gracefully
* Apply clear naming conventions for resources

### Prompts

* Define structured, reusable templates for consistent interactions
* Integrate dynamic resource context into prompts
* Support multi-step workflows and composability
* Include descriptive metadata: name, description, argument schema
* Provide discoverability via prompts/list endpoint
* Validate inputs and handle errors gracefully
* Sanitize inputs to avoid security vulnerabilities

### Tools

* Use JSON schema for precise input definition and validation
* Clearly define tool name, description, inputs, and expected outputs
* Provide structured error reporting for corrective actions
* Discover tools dynamically via tools/list endpoint
* Invoke tools securely via tools/call with validation
* Ensure access control, logging, and auditing for accountability
* Emphasize input sanitization to prevent unsafe executions

### Sampling

* Use structured sampling/createMessage requests with clear parameters
* Include contextual messages with roles and content types
* Allow human-in-the-loop approval for oversight
* Specify model preferences (cost, latency, intelligence)
* Control execution with parameters: temperature, token limits, stop sequences
* Provide structured responses with model details and termination reasons
* Define context inclusion policies to enhance relevance
* Maintain security with validation and execution policies

### Roots

* Define logical boundaries with URIs for resource scope
* Use roots to contextualize operations within boundaries
* Prioritize resource use based on root definitions
* Support multi-context management (multiple environments)
* Allow adaptive updates to roots during runtime
* Ensure servers respect boundaries for clarity and security

### Building Effective Agents

* Use sampling to centralize control on the client side for privacy and cost-efficiency
* Apply composability: agents act as both client and server for modular workflows
* Chain agents for hierarchical, specialized architectures
* Integrate human oversight where needed
* Combine sampling and composability for federated, secure agent networks
* Employ centralized orchestration for complex workflows

### Applications

* Standardize integrations to reduce API fragmentation
* Leverage domain-specific MCP servers (finance, healthcare, education, CRM, e-commerce, etc.)
* Automate workflows with secure, real-time data access
* Support personalization, adaptive learning, and intelligent customer support
* Enhance scalability, interoperability, and secure data exchange across industries

### Challenges and Future Work

* Foster adoption and community-driven standardization
* Strengthen security and privacy mechanisms
* Ensure low-latency performance at scale
* Build robust ecosystem of compatible tools and services