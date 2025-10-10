# Best Practices from RAG-MCP: Mitigating Prompt Bloat in LLM Tool Selection via Retrieval-Augmented Generation

---

## 1. Managing Cognitive Load and Context Limits
- Avoid presenting all tool descriptions to the model simultaneously
- Store tool metadata externally; retrieve only relevant tool schemas on demand
- Use retrieval to filter context dynamically before inference
- Prioritize minimal, high-relevance context to reduce distraction and confusion
- Conserve context window space for reasoning rather than tool metadata
- Prevent “prompt bloat” by reducing redundant or overlapping tool definitions

## 2. Retrieval-Augmented Tool Selection
- Treat tool discovery as a retrieval problem, separate from text generation
- Represent tools in a vector index using semantic embeddings
- Use an LLM-based retriever (e.g., Qwen) to match user queries to tool schemas
- Retrieve top-k candidates, validate, then pass only the best tool to the LLM
- Validate retrieved tools via few-shot example tests before invocation
- Integrate retrieval output into the prompt or function-calling interface only after filtering

## 3. Planning and Decision-Making Enhancements
- Decouple tool discovery (retrieval) from planning and execution (generation)
- Narrow the toolset to simplify decision boundaries and reduce hallucination risk
- Use retrieval to improve focus and clarity in action selection
- Employ validation or sanity-check steps to confirm tool compatibility
- Enable dynamic retrieval for multi-turn robustness (no re-injection of all tools each turn)

## 4. Memory and Extensibility
- Maintain an external, updateable memory of tool schemas
- Allow new tools to be indexed dynamically without retraining
- Store embeddings for tool metadata to support continual system growth
- Keep the LLM stateless between tool additions; rely on retrieval for memory recall

## 5. Efficiency and Scalability
- Activate only the selected tool server to reduce computational overhead
- Support arbitrarily large toolsets through retrieval rather than pre-loading
- Minimize prompt tokens to enhance throughput and reduce latency
- Use external retrieval infrastructure to scale without context-window constraints

## 6. Evaluation and Self-Improvement
- Conduct stress tests to measure degradation under growing toolsets
- Use structured benchmarks to quantify selection accuracy and prompt efficiency
- Track average prompt and completion tokens to balance precision vs efficiency
- Analyze retrieval failures to improve precision in large tool registries
- Explore hierarchical or adaptive retrieval mechanisms for extreme-scale scenarios

## 7. Key Observed Benefits
- >50% reduction in prompt tokens via retrieval filtering
- >3× improvement in tool selection accuracy (43.13% vs 13.62% baseline)
- Maintained or improved task success rates even as tool count scales

---

## Benchmarks and Evaluations Referenced
- **MCPBench (WebSearch subset)** – benchmark for tool-augmented NLP tasks
- **Needle-in-a-Haystack (NIAH) Test** – evaluates recall limits under long contexts
- **MCP Stress Test** – custom benchmark measuring performance vs tool count
- **DeepSeek-v3 Evaluator** – automatic correctness verification
- **Llama-as-Judge** – output verification model
