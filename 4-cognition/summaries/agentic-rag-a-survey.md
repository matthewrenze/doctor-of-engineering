# Best Practices from Agentic RAG: A Survey

---

## 1. Core Cognitive Principles of Agentic Intelligence

- **LLM as reasoning engine**
  - Define clear role and task for each agent  
  - Maintain coherence across multi-step reasoning

- **Memory systems**
  - Use short-term memory for immediate context tracking  
  - Use long-term memory for persistent learning and experience accumulation  
  - Maintain contextual continuity across agent interactions  

- **Planning**
  - Decompose complex problems into smaller, manageable subtasks  
  - Employ self-critique and reflection to refine intermediate reasoning  
  - Adapt plans dynamically to task complexity  

- **Reflection**
  - Integrate self-evaluation loops for continuous improvement  
  - Use feedback from internal critique or external validation tools  
  - Implement dual-agent critique roles for improved accuracy (e.g., generator and evaluator agents)

- **Tool use**
  - Extend agent capability with retrieval, computation, and external API access  
  - Dynamically select tools based on task requirements  
  - Employ heuristic or learned strategies for tool selection  
  - Validate results from tools via self-check or critic agent  

- **Multi-agent collaboration**
  - Specialize agents for subtasks and coordinate via shared context  
  - Use message passing and role-based communication  
  - Parallelize or hierarchically organize agents for scalability  
  - Balance autonomy with orchestration to avoid coordination overhead  

---

## 2. Agentic Workflow Patterns

- **Prompt chaining**
  - Break tasks into sequential sub-prompts  
  - Propagate refined outputs step by step  
  - Use for tasks with predictable dependencies  

- **Routing**
  - Classify input type and send to specialized processing path  
  - Use smaller models for simple cases, larger for complex ones  
  - Employ routing for efficiency in multi-domain tasks  

- **Parallelization**
  - Split independent subtasks for concurrent processing  
  - Use voting or consensus to increase confidence  
  - Apply to speed-sensitive or ensemble-style tasks  

- **Orchestrator–worker model**
  - Central orchestrator delegates subtasks dynamically  
  - Assign specialized workers for modular scalability  
  - Merge results into unified outputs via top-level agent  

- **Evaluator–optimizer**
  - Iteratively refine outputs using feedback loops  
  - Employ evaluator models for quality control  
  - Use for creative or precision tasks needing multiple passes  

---

## 3. Taxonomy-Specific Cognitive Enhancements

- **Single-agent RAG (Router model)**
  - Centralized control for simple task management  
  - Direct dynamic routing to diverse retrieval sources  
  - Optimize for low-latency and simplicity  

- **Multi-agent RAG**
  - Distribute specialized roles (retrieval, reasoning, synthesis)  
  - Enable parallel, domain-specific processing  
  - Integrate results through a coordinating agent  

- **Hierarchical RAG**
  - Organize agents in multi-tier control hierarchy  
  - Use top-tier for strategic delegation and aggregation  
  - Improve decision quality through structured oversight  

- **Corrective RAG**
  - Include relevance evaluators and query refiners  
  - Re-assess retrieved context iteratively  
  - Employ corrective agents to reduce hallucinations  

- **Adaptive RAG**
  - Dynamically select retrieval complexity based on query classification  
  - Use lightweight classifiers for efficiency  
  - Avoid unnecessary retrieval for fact-based tasks  

- **Graph-based RAG (Agent-G, GeAR)**
  - Integrate graph-structured and unstructured knowledge  
  - Use critic or feedback modules for quality control  
  - Support multi-hop reasoning via graph expansion  

- **Agentic Document Workflows (ADW)**
  - Maintain document state across multi-step reasoning  
  - Use specialized agents for parsing, retrieval, and synthesis  
  - Apply business rules and domain logic within agent orchestration  

---

## 4. Cognitive Optimization Across Agentic Systems

- Enable **contextual reasoning** through memory and reflection  
- Balance **autonomy and coordination** to minimize overhead  
- Use **multi-agent planning** for long-horizon workflows  
- Employ **critic loops** and **feedback refinement** for factual accuracy  
- Ensure **dynamic adaptability** through planning and routing mechanisms  
- Maintain **traceability** and **state persistence** for transparency and reproducibility  

---

## 5. Tools and Framework Best Practices

- Use **LangChain / LangGraph** for modular, stateful orchestration  
- Employ **LlamaIndex ADW** for structured document workflows  
- Combine **Hugging Face + Qdrant** for hybrid retrieval (dense + sparse)  
- Use **CrewAI / AutoGen / Swarm** for multi-agent collaboration  
- Integrate **Neo4j** for graph reasoning and **vector DBs** for semantic retrieval  
- Apply **Semantic Kernel** or **Vertex AI** for enterprise-level orchestration and API integration  

---

## Benchmarks Referenced

### Retrieval and QA
- BEIR  
- MS MARCO  
- TREC Deep Learning Track  
- Natural Questions (NQ)  
- TriviaQA  
- SQuAD  
- WebQuestions  
- PopQA  

### Multi-hop and Reasoning
- HotpotQA  
- 2WikiMultihopQA  
- MuSiQue  
- StrategyQA  
- CommonsenseQA  
- HellaSwag  

### Domain-Specific QA and Summarization
- Qasper  
- COVID-QA  
- CMB/MMCU (Medical)  
- QMSum  
- NarrativeQA  
- ELI5  

### Graph and Agentic Benchmarks
- AgentG (Agentic RAG for Knowledge Fusion)  
- GNN-RAG (Graph-based RAG evaluation)  
- GraphQA  

### Comprehensive RAG Benchmarks
- RAGBench  
- BERGEN  
- FlashRAG Toolkit  

### Other Categories
- FEVER (fact verification)  
- CodeSearchNet (code retrieval)  
- GSM8K (math reasoning)  
- WikiText-103 (language modeling)  
- NoMIRACL (retrieval robustness)
