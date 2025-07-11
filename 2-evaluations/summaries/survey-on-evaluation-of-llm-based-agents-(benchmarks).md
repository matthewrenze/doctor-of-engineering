# Summary of Survey on Evaluation of LLM-based Agents (Benchmarks)

---

## 1. Agentic Capabilities Evaluation

### 1.1 Planning & Multi-Step Reasoning

* GSM8K - Grade school math problems requiring step-by-step reasoning (8,500 training, 1,319 test).
* MATH - Advanced math problems from competitions (12,500+ problems).
* AQUA-RAT - Algebraic reasoning with rationales (100k+ problems).
* HotpotQA - Multi-hop QA using multiple documents (112k examples).
* StrategyQA - Implicit multi-step reasoning with yes/no answers (2,900 questions).
* MultiRC - Multi-sentence reading comprehension with multiple correct answers (9,872 examples).
* ARC - Commonsense science problems for 3rd-9th grade (7,787 train, 1,722 test).
* FOLIO / P-FOLIO - Deductive logic reasoning over text (FOLIO: 7.2k examples).
* Game of 24 - Arithmetic puzzles (typically 100s of variations).
* MUSR - Multistep soft reasoning over natural language.
* BBH - BigBench Hard: \~23 diverse challenging tasks.
* PlanBench - Planning-focused benchmark over real-world tasks (task count not specified).
* AutoPlanBench - Automatically generated PDDL-style planning tasks.
* ToolEmu - Simulated tool execution with state-tracking; task count unspecified.
* MINT - Multistep Interactive Task benchmark for sustained planning; tasks vary by domain.
* FlowBench - Workflow-based planning in expert domains.
* ACPBench - Analytical planning benchmark focused on core skills.
* NaturalPlan - Natural-language planning for interacting with common software.

---

### 1.2 Function Calling & Tool Use

* ToolBench - Synthetic function call task suite.
* ToolAlpaca - 3,000 simulated tool-use cases.
* APIBench - Function call sequences with structured API inputs.
* BFCL - Berkeley Function Calling Leaderboard; task count varies as it's a live benchmark.
* ToolSandbox - Interactive tool-use in stateful simulated environments.
* Seal-Tools - Tool-use data from self-instruct approach.
* API-Bank - Real-world tool-use conversations with APIs.
* NexusRaven - Validated zero-shot tool-calling evaluation suite.
* API-Blend - API detection and slot-filling tasks.
* RestBench - Multi-API composition benchmark.
* APIGen - Synthetic generation of function call datasets.
* StableToolBench - Tool-use benchmark with API caching and error simulation.
* ComplexFuncBench - Long-context tool use with constraints and implicit dependencies.
* NESTFUL - Evaluates nested tool sequences and input-output dependencies.

---

### 1.3 Self-Reflection

* LLF-Bench - Interactive feedback benchmark with randomized instructions; \~300 tasks.
* LLM-Evolve - Measures improvement from prior examples; task count not specified.
* Reflection-Bench - Evaluates belief revision, counterfactual reasoning, and meta-reflection.

---

### 1.4 Memory

* NarrativeQA - Comprehension of long narrative stories (1,572 stories, 10k Q\&A pairs).
* QMSum - Multi-document summarization (1,808 meetings across domains).
* QUALITY - QA benchmark focused on information quality (10k+ Q\&A).
* RAISE - Episodic memory for reading tasks; task count unspecified.
* ReadAgent - Multi-document reading and memory benchmarking.
* MemGPT - Episodic memory over long multi-domain interactions.
* LoCoMo - Tests long-term coherence in memory.
* A-MEM - Multi-domain conversational memory benchmark.
* StreamBench - Memory continuity across stream-like inputs.
* LTMbenchmark - Long conversations with task-switching.

---

## 2. Application-Specific Agent Evaluation

### 2.1 Web Agents

* MiniWob / MiniWob++ - GUI-based web task mini-games (100+ tasks).
* WebShop - Online shopping simulation with 1,819 products and 12k+ tasks.
* Mind2Web - Task-based interaction with real websites (1,000+ tasks).
* WebVoyager - Expands Mind2Web with more task types.
* WebLinX - Real-time navigation tasks with UI changes.
* WebArena / VisualWebArena - Rich UIs with dynamic visual cues.
* MMInA - Multimodal multi-hop tasks across internet domains.
* AssistantBench - 100+ long-horizon online tasks.
* WebCanvas - Path-based web interaction success metrics.
* ST-WebAgentBench - Combines static and dynamic web task types.
* WorkArena / WorkArena++ - Office-style web workflow simulations.

---

### 2.2 Software Engineering Agents

* HumanEval - 164 programming tasks with input-output tests.
* SWE-bench - 2,294 real-world GitHub issues with test suites.
* SWE-bench Lite - 300 filtered bug-fix issues.
* SWE-bench Verified - Curated subset with robust issue/test quality.
* SWE-bench+ - Improved SWE-bench mitigating test leakage.
* SWE-bench Multimodal - JavaScript-based app tasks with visual elements.
* TDD-Bench Verified - Test-driven development patch benchmarks.
* SWT-Bench - Validates agent-generated bug fixes against test cases.
* ITBench - Complex automation scenarios for IT operations.
* SWELancer - Freelance SWE tasks with monetary value assessments.

---

### 2.3 Scientific Agents

* ScienceQA - Science questions with diagrams (21k+ QA pairs).
* QASPER - QA over academic papers (5,000+ examples).
* MS2 - Summarization of 20k medical studies.
* SUPER - Research repository task execution.
* SciCode - 250+ scientific code challenges.
* DiscoveryWorld - Interactive lab simulations (task count unspecified).
* LAB-Bench - Biology-focused experiments and data interpretation.
* MLGym-Bench - Simulated ML experimentation environments.
* AAAR-1.0 - 150+ full pipeline scientific tasks (e.g., hypothesis + experiment).
* ScienceAgentBench - End-to-end data-to-insight scientific reasoning.
* CORE-Bench - Reproducibility-focused scientific tasks.
* Ideation - Creative scientific hypothesis generation.

---

### 2.4 Conversational Agents

* ABCD - 10,000+ crowdsourced dialogues with 55 user intents.
* MultiWOZ - 10,438 multi-domain task-oriented dialogues.
* SMCalFlow - Structured dialogue for calendar and assistant tasks.
* ALMITA - 192 dialogues, 14 intents, 1,420 tests.
* τ-Bench - 165 customer service tasks (115 retail, 50 airline).
* IntellAgent - Dynamic policy-based dialogue benchmarking framework.

---

## 3. Generalist Agent Evaluation

* GAIA - 466 real-world, human-created tasks across web, tools, and reasoning.
* AgentBench - Interactive OS, games, SQL, and home task environments.
* OSWorld - Real OS task execution with multimodal inputs.
* OmniACT - Multi-app control tasks for agents.
* AppWorld - App interaction simulations for complex goals.
* TheAgentCompany - Simulated internal company agent coordination.
* CRMArena - CRM tools benchmark with UI and API integration.
* HAL - Holistic leaderboard aggregating benchmarks across domains.
