# Module 3 - Agent Tool-Use (Sept)

## Goals
- Learn how to create agents that can use a variety of tools

## Readings
- [Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761)
- [Tool Learning with Large Language Models: A Survey](https://arxiv.org/abs/2405.17935)
- [τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains](https://arxiv.org/abs/2406.12045)
- [m&m's: A Benchmark to Evaluate Tool-Use for multi-step multi-modal Tasks](https://arxiv.org/abs/2403.11085)
- [Model Context Protocol (MCP): Landscape, Security Threats, and Future …](https://arxiv.org/abs/2503.23278)
- [A Survey of the Model Context Protocol (MCP) …](https://www.preprints.org/manuscript/202504.0245/v1)
- [Agent-to-Agent (A2A) Protocol (website)](https://a2a-protocol.org/)

## Summaries
- Paper summaries can be found in the [summaries](summaries/) folder.

## Prototypes
- [action-parser](prototypes/action-parser/) - prototypes for a multi-argument action parser
- [beep-beep](prototypes/beep-beep/) - prototypes for an audible alert for long running experiments
- [cache-hash](prototypes/cache-hash/) - prototypes for file-name hashing for a file cache
- [debug-evals](prototypes/debug-evals/) - prototypes for creating evals to debug tools
- [execute-code](prototypes/execute-code/) - prototypes for a Python code interpreter tool
- [read-html](prototypes/read-html/) - prototypes for an HTML-to-markdown tool
- [search-web](prototypes/search-web/) - prototypes for a web search tool
- [simple-qa](prototypes/simple-qa/) - prototypes for the simple-qa benchmark

## Exercises
- Summarize [agent tool-use best practices](exercises/best-practices/tool-use-best-practices.md)
- Create an agent with a [search engine tool](projects/agent-eval/code/tools/search_web_tool.py)
- Create an agent with a [web browser tool](projects/agent-eval/code/tools/read_html_tool.py)
- Create an agent with a [python interpreter tool](projects/agent-eval/code/tools/execute_code_tool.py)
- Create an MCP client/server agent
- Create a [simple-qa eval](projects/create-evals/code/create_simple_qa_evals.py)
- Create an m&ms eval
- Create a τ-bench evaluation

## Experiments
- Determine optimal [top-k search results](experiments/top-k-search-results/)
- Determine optimal [HTML page chunk size](experiments/read-html-chunk-size/)

## Projects
- Create a [set of tool-use evals](projects/create-evals/)
- Create an [tool-use eval framework](projects/agent-eval/)
