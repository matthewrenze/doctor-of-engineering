# Summary of LLM-Based Agents for Software Engineering

## 1. General Agent Design
- Use core components: planning, memory, perception, and action
- Enable iterative interaction with the environment
- Support external tool use and multi-modal perception
- Incorporate multi-agent collaboration (roles, communication)
- Facilitate human-agent collaboration to improve alignment

---

## 2. Software Engineering Perspective

### 2.1 Requirements Engineering
- Simulate diverse stakeholder roles for requirement elicitation (RE)
- Automate RE phases using multi-agent systems
- Generate specifications through conversations and mutation
- Use formal verification tools to validate requirements

### 2.2 Code Generation
- Apply chain-of-thought reasoning for planning
- Use planning representations: pseudocode, skeletons, intermediate code
- Refine code iteratively using:
  - Model feedback (peer/self-reflection)
  - Tool feedback (compiler, test results, static analysis)
  - Human feedback (clarifications)
  - Hybrid feedback (combination of above)

### 2.3 Static Code Checking
- Collaborate via multi-agent review and critique
- Combine LLMs with static analysis tools (e.g., CodeQL, Clang)
- Use external knowledge bases for improved reasoning
- Integrate vulnerability detection with agent debate and tool support

### 2.4 Testing
- Use feedback loops to correct and improve test code
- Increase test coverage using analysis tools and guidance
- Detect faults using mutation testing feedback
- Automate system testing across multiple domains (OS, mobile, web)

### 2.5 Debugging
- Design agents for both fault localization and program repair
- Use tool-augmented iterations with compilation, execution, and test feedback
- Apply unified debugging by connecting repair and localization phases
- Incorporate static and dynamic analysis for precise patch generation

### 2.6 End-to-End Software Development
- Follow structured workflows (e.g., waterfall, Scrum, TDD)
- Assign distinct roles: product manager, architect, developer, tester
- Prefer ordered collaboration; use debate where necessary
- Measure outcomes with multi-faceted metrics:
  - Pass rate
  - Similarity (e.g., SketchBLEU)
  - Cost (time, tokens, feedback)
  - Human effort and code completeness

### 2.7 End-to-End Software Maintenance
- Follow a modular pipeline: preprocessing -> reproduction -> localization -> patching
- Use combined localization strategies:
  - Retrieval
  - Navigation
  - Spectrum analysis
  - Simulation
- Verify patches using static/dynamic testing and ranking heuristics

---

## 3. Agent Component Design

### 3.1 Planning
- Choose between:
  - Single vs. Multi-agent planning
  - Single-turn vs. Multi-turn plans
  - Single-path vs. Multi-path planning (e.g., MCTS)
- Represent plans via:
  - Natural language
  - Structured formats (e.g., JSON, pseudocode)
  - Graphs (e.g., control flow)

### 3.2 Memory
- Use both short-term (dialog, actions) and long-term (task summaries) memory
- Store memory in formats like:
  - Natural text
  - Structured messages
  - Code
  - Key-value pairs
  - Embeddings
  - Trees
- Manage memory through:
  - Preprocessing (summarization, distillation)
  - Elimination (sliding window, frequency filtering)
  - Access (reflection, retrieval, subscription)

### 3.3 Perception
- Use textual inputs for most SE tasks
- Support visual inputs for GUI or diagram-based tasks
- Leverage external models (e.g., OCR, layout analysis) for perception

### 3.4 Action
- Equip agents with tools for:
  - Web/search (e.g., DuckDuckGo, SerpAPI)
  - Static/dynamic program analysis (AST, CFG, coverage)
  - Testing (validation, mutation testing)
  - File/GUI operations and version control
- Tailor tool use to task requirements (repair, generation, testing, navigation)

---

## 4. Multi-Agent System Design

### 4.1 Roles
- Define specialized roles such as:
  - Managers (planner, coordinator)
  - Analysts (requirements, UI/UX)
  - Developers and testers
  - Reviewers and debuggers
  - Assistants (retrievers, formatters)

### 4.2 Collaboration Mechanisms
- Choose a structure suited to the workflow:
  - Layered (sequential)
  - Circular (feedback loops)
  - Tree-like (branching/parallel roles)
  - Star-like (central controller)
- Design interactions as ordered sequences or debate-based summaries

---

## 5. Human-Agent Collaboration
- Involve humans at key phases:
  - Planning: workflow editing
  - Requirements: clarifications and refinement
  - Development: strategy input and adjustment
  - Evaluation: manual review and acceptance
- Build tools/interfaces for displaying state and capturing feedback

---

## 6. Research and Evaluation Best Practices

### 6.1 Evaluation
- Design metrics beyond final success:
  - Intermediate decision quality
  - Robustness, fairness, security
  - Efficiency (runtime, cost, iteration count)

### 6.2 Benchmarks
- Build realistic, complex, and high-quality benchmarks
- Include multi-file, long-instruction tasks
- Ensure benchmarks reflect real-world challenges

### 6.3 Tool and Workflow Integration
- Integrate proven SE tools and practices (e.g., testing, repair pipelines)
- Base agent workflows on established SE process models (e.g., Agile, Waterfall)
- Train LLMs on full software lifecycle data, not just code

---
