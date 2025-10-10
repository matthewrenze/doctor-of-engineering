# Cognitive Enhancement Benchmarks for LLM Agents

This document summarizes the benchmarks used to evaluate cognitive enhancements (planning, memory, reasoning, reflection, tool use, and multi-agent collaboration) across several major survey and best-practice papers on LLM agents.

---

## 1. Planning and Decision-Making
- ALFWorld – Text-based embodied environment derived from TextWorld; tests long-horizon planning, action grounding, and reasoning-through-feedback  
- ScienceWorld – Embodied scientific reasoning tasks; evaluates procedural reasoning and goal decomposition  
- Minecraft / Voyager / GITM – Open-world planning and exploration; tests adaptive planning, resource management, and lifelong learning  
- BabyAI / VirtualHome / gSCAN – Instruction-following and compositional generalization; measures language-to-action translation and plan generalization  
- Jericho / TextWorld – Interactive fiction and text adventure frameworks; evaluate symbolic planning and multi-step reasoning  
- SMART-LLM / RocoBench / PPNL / Robotouille – Robotics and physical planning; measure embodied reasoning, spatial cognition, and causal planning  
- PlanBench / TaskBench / TravelPlanner / API-Bank – Formal task-planning and API-integration tests; assess tool-oriented planning and decision orchestration  
- WebShop / WebArena / Mind2Web / OSWorld – Web navigation tasks; evaluate goal-directed planning, multi-step tool use, and context persistence  
- AgentBench – Multi-domain environment combining coding, web, and OS tasks; measures cross-domain planning and agent robustness  

---

## 2. Memory and Context Management
- LongBench – Long-context understanding benchmark; tests retrieval accuracy, summarization, and context retention  
- ZeroScrolls – Evaluates document-level long-context reasoning and summarization quality  
- ChatDB / MemoChat / MemoryBank / ExpeL – Specialized frameworks assessing episodic and retrieval memory; measure recall precision and memory update efficiency  
- Reflexion – Evaluates verbal self-reinforcement learning via natural-language feedback; tests reflective memory formation  
- ReAct – Reasoning-and-acting benchmark measuring short-term memory use and adaptive control during environment interaction  

---

## 3. Reasoning and Reflection
- HotPotQA – Multi-hop question answering; measures multi-step reasoning and retrieval planning  
- FEVER – Fact verification; tests truth-grounded reasoning and retrieval precision  
- CommonsenseQA / StrategyQA / HellaSwag / MuSiQue / 2WikiMultihopQA – Evaluate commonsense, multi-hop, and strategic reasoning abilities  
- Reflection-Bench – Dedicated reflection benchmark; measures self-critique quality and error correction across reasoning chains  
- Game-of-24 – Arithmetic reasoning game; evaluates symbolic reasoning and goal search efficiency  

---

## 4. Programming, Tool Use, and Problem Solving
- HumanEval – Code generation with hidden unit tests; evaluates program synthesis and logical reasoning  
- MBPP (Mostly Basic Programming Problems) – Simple programming tasks; tests stepwise reasoning and syntax correctness  
- LeetcodeHardGym – Hard-level programming set for Reflexion; measures iterative debugging and self-reflection performance  
- MultiPL-E – Multi-language code translation; evaluates cross-lingual reasoning and abstraction  
- SWE-bench Verified / RE-Bench / SWAA / HCAST – Software-engineering and automation tasks; measure tool-use reliability, long-horizon persistence, and error recovery  
- ToolBench / MAgentBench / ZeroBench / MCPBench – Tool-use evaluations; test retrieval-augmented decision-making, tool selection, and prompt efficiency  
- MCP Stress Test / NIAH Test (Needle-in-a-Haystack) – Stress and recall benchmarks for long contexts; measure retrieval robustness and scaling efficiency  
- API-Bank / MINT / CodeSearchNet – API or code retrieval tasks; assess semantic search and tool invocation accuracy  
- DeepSeek-v3 Evaluator / Llama-as-Judge – Automated evaluators for correctness; test self-evaluation and verification mechanisms  

---

## 5. Retrieval and Knowledge Integration (RAG)
- BEIR / MS MARCO / TREC DL Track / Natural Questions / TriviaQA / SQuAD / WebQuestions / PopQA – Standard retrieval-QA benchmarks measuring information-seeking, context relevance, and RAG recall  
- Qasper / COVID-QA / CMB/MMCU / QMSum / NarrativeQA / ELI5 – Domain-specific RAG tasks testing scientific, medical, meeting-summary, and explanatory reasoning  
- GraphQA / AgentG / GNN-RAG / RAGBench / BERGEN / FlashRAG – Graph- and multi-agent-RAG benchmarks; measure multi-hop integration, graph reasoning, and retrieval orchestration  
- NoMIRACL – Retrieval robustness benchmark; tests resilience to noisy or missing context  

---

## 6. General Intelligence and Knowledge
- GPQA / GPQA-Diamond – Graduate-level question answering; evaluates expert-level reasoning and factual grounding  
- MMLU / MMLU-Pro / AGIEval – Academic and professional exam tasks (SAT, LSAT, etc.); test broad cognitive knowledge and reasoning  
- ARC (AI2 Reasoning Challenge) – Science-reasoning multiple-choice benchmark; measures commonsense and logical inference  
- BIG-Bench – General-purpose reasoning benchmark; evaluates emergent reasoning abilities  
- GAIA – General AI Assistant benchmark; tests multi-modal planning, tool use, and workflow persistence  
- HellaSwag / MedMCQA / Creative Writing / Mini-Crosswords – Assess narrative reasoning, medical QA, and creativity under cognitive constraints  

---

## 7. Multi-Agent and Collaborative Cognition
- AgentG / CrewAI / AutoGen / Swarm Evaluations – Measure multi-agent coordination, role specialization, and communication efficiency  
- Multi-Agent Debate (MAD) / MARS Framework Tasks – Evaluate collaborative reflection, consensus reasoning, and critique synthesis  
- WebArena Collaboration / Mind2Web Tasks – Assess coordinated web-based reasoning among multiple agents  

---

## Summary Table

| Cognitive Aspect | Representative Benchmarks |
|------------------|---------------------------|
| Planning & Decision-Making | ALFWorld, ScienceWorld, WebShop, PlanBench |
| Memory & Context | LongBench, ZeroScrolls, MemoryBank |
| Reasoning & Reflection | HotPotQA, FEVER, Reflection-Bench |
| Tool Use & Problem Solving | HumanEval, MBPP, MCPBench |
| Retrieval & Knowledge Integration | BEIR, RAGBench, GraphQA |
| General Knowledge | MMLU, GPQA, GAIA |
| Multi-Agent Cognition | AgentG, MARS, MAD |

---
