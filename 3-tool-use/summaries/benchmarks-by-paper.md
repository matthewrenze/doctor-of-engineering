# Tool-Use Benchmarks

## Toolformer

* LAMA – factual cloze completion (subsets SQuAD, Google-RE, T-REx), evaluates factual recall without tools
* TEMPLAMA – temporal cloze queries from Wikidata, tests time-sensitive factual knowledge
* DATESET – synthetic temporal reasoning dataset (date math, weekdays, holidays), requires calendar tool
* ASDiv – arithmetic word problems, diverse formulations, evaluates calculator use
* SVAMP – simple math word problems designed to test weaknesses, evaluates calculator use
* MAWPS – math word problem repository, multiple formats, evaluates calculator use
* WebQuestions (WebQS) – natural-language QA linked to Freebase, tests Wikipedia search tool
* Natural Questions (NQ) – open-domain QA with Wikipedia passages, tests Wikipedia search tool
* TriviaQA – large-scale trivia-style QA, tests Wikipedia search tool
* MLQA – multilingual QA across 6 languages, evaluates machine translation + QA
* WikiText – standard LM dataset, used to validate language modeling perplexity
* CCNet – filtered Common Crawl dataset, used for training and perplexity validation

---

## Tool Learning with Large Language Models: A Survey

### General benchmarks (broad tool learning evaluation)

* API-Bank – evaluates all four stages with 73 tools, executable, manually created
* APIBench – tests tool selection + calling using 1,645 tools, public models
* ToolBench1 – open-source tool selection/calling, 232 public APIs
* ToolBench2 – largest dataset (16k tools, 126k instances), covers all stages, executable
* ToolAlpaca – generalized tool learning, 426 public APIs
* RestBench – RESTful APIs benchmark for planning, selection, calling
* MetaTool – evaluates decision of whether/when to use tools, based on OpenAI plugins
* TaskBench – public APIs for task automation, 28k instances
* T-Eval – step-by-step evaluation of tool utilization, small but precise
* ToolEyes – fine-grained evaluation across all four stages, real-world scenarios
* UltraTool – manual creation of complex scenarios, large set of 2k tools
* API-BLEND – large corpus of tool-use examples from existing datasets
* Seal-Tools – self-instruct tool learning dataset for agent tuning
* ShortcutsBench – large-scale real-world API-based tasks
* GTA – benchmark for general tool agents, multi-stage evaluation
* WTU-Eval – binary “whether-to-use tool” evaluation benchmark
* AppWorld – controllable world of apps and people, interactive coding agents

### Specialized benchmarks (task/domain specific)

* ToolQA – QA requiring external tools (can’t be answered without them)
* ToolEmu – safety evaluation via LM-emulated sandbox
* ToolTalk – conversational setting for multi-turn tool use
* ToolSandbox – interactive, stateful, conversational tool use evaluation
* VIoT – video/IoT scheduling tools with LLMs
* RoTBench – robustness evaluation under noise/interference
* ToolSword – safety evaluation across multiple stages of tool use
* StableToolBench – stable large-scale tool learning benchmark (built on ToolBench2)
* SciToolBench – scientific reasoning with tool-augmented LLMs
* InjecAgent – evaluates indirect prompt injections in tool-integrated agents
* m\&m’s – multi-step multi-modal tool-use benchmark
* MLLM-Tool – multi-modal tool use across text, image, audio
* GeoLLM-QA – remote sensing workflows with tool use
* ToolLens – tool retrieval benchmark (retriever completeness)
* SoAyBench – academic information seeking via tool use
* CToolEval – Chinese-specific tool learning evaluation

---

## Tau-Bench

* τ-bench – Evaluates tool-using agents on realistic user interactions and rule-following in retail and airline domains.
* Berkeley Function Calling Leaderboard (BFCL) – Ranks models on accuracy of function call generation.
* ToolBench – Tests LMs’ ability to execute and manipulate tools across APIs and languages.
* MetaTool – Benchmarks whether and which tools an LM chooses to use.
* ToolEmu – Uses LMs to emulate tool execution and expose safety risks in tool use.
* SWE-Bench – Evaluates models on resolving real-world GitHub issues.
* AgentBench – Tests LLMs as agents across multiple simulated environments.
* WebShop – Measures LM agents’ ability to navigate and purchase items in a simulated e-commerce site.
* WebArena – Provides a realistic web environment for evaluating autonomous web agents.
* MultiWOZ – A large-scale dataset for multi-domain task-oriented dialogue.
* Action-based Conversations Dataset – Corpus for training and testing action-rich task-oriented dialogue systems.

---

# Model Context Protocol (MCP): Landscape, Security Threats, and Future

* m\&m’s – multi-step multi-modal benchmark with 4K+ tasks and 33 real tools, human-verified executable plans
* ToolBench – large-scale tool-use benchmark with 3,451 APIs, but limited to text inputs
* ToolEmu – benchmark using LLMs to emulate tool execution instead of real tools
* TaskBench – task automation benchmark with placeholder multimodal queries, lacks real execution
* MetaTool – benchmark focused on deciding whether to use OpenAI plugins as tools
* GAIA – benchmark for general AI assistants across diverse real-world tasks
* HotpotQA – multi-hop question answering dataset for explainable QA
* WebShop – simulated online shopping benchmark for language agents in real-world interactions
* GQA – dataset for compositional visual reasoning and visual question answering
* RefCOCO – benchmark for referring expressions in images (object identification via language)
* NLVR – dataset for natural language visual reasoning with logical operations on images
* Visual Genome – large dataset linking language and vision with dense image annotations
* ImageNet – large-scale hierarchical image database for image classification
* SQuAD – 100k+ question-answering dataset for text comprehension
* MagicBrush – dataset for instruction-guided image editing tasks
* Librispeech – large ASR corpus of audiobooks for speech recognition

---

# A Survey of the Model Context Protocol (MCP)

- N/A

---
