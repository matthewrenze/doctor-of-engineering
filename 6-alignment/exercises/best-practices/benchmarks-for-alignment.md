## Agent-specific harm and action safety

- AgentHarm: Multi-step, tool-using agent tasks with explicitly malicious goals (and benign counterparts) scored with rubrics; Evaluates harmful action compliance under long-horizon workflows
- AgentBench (Safety and Tool-Use Subsets): Agent evaluation suite with safety-relevant and tool-use scenarios; Evaluates safe tool-use, constraint adherence, and refusal during multi-step tasks
- WebArena Safety Tasks: Safety-constrained autonomous web navigation tasks; Evaluates safe decision-making during real(istic) web interaction and tool execution
- ALFWorld Safety-Constrained Tasks: Embodied/text environment tasks with constraints; Evaluates instruction following under safety or environment constraints

## Harmful instruction following and refusal

- HarmBench: Harmful instruction prompts across harm categories; Evaluates refusal vs compliance and harmful content/action generation
- AdvBench: Adversarially crafted harmful prompts; Evaluates robustness to “best-effort” misuse prompting
- Do-Not-Answer: Prompts that should be refused; Evaluates correct refusal behavior and boundary following
- XSTest: Safety edge-case set targeting over- and under-refusal; Evaluates calibration of refusals (helpful when safe, refuse when unsafe)
- BeaverTails: Large-scale harmful instruction-following/refusal dataset; Evaluates harmful compliance vs safe refusal trade-offs
- RealToxicityPrompts: Toxicity-triggering prompts; Evaluates tendency to generate toxic/harmful text under provocation

## Jailbreak and adversarial robustness

- JailbreakBench: Prompt-based safety bypass attempts; Evaluates susceptibility to jailbreaks and refusal consistency
- SafeEval: Safety evaluation under adversarial prompting; Evaluates refusal quality, consistency, and recovery after unsafe turns
- Red Teaming Prompt Sets: Curated/creative misuse prompts; Evaluates stress resistance to novel jailbreak/misuse strategies

## Helpfulness–harmlessness trade-offs and preference alignment

- Anthropic Helpful–Harmless (HH) Dataset: Preference-style comparisons emphasizing helpfulness vs harmlessness; Evaluates alignment to preference trade-offs used in RLHF-style training
- Safety-Prompts / HH-RLHF Eval Sets: Safety-oriented preference eval sets used in RLHF contexts; Evaluates policy compliance and preference-consistent refusals

## Truthfulness and factuality

- TruthfulQA: Questions designed to elicit false but appealing answers; Evaluates truthfulness vs imitation of misconceptions
- Factual precision evaluation tasks (factual vs non-factual prompt setups): Task designs that distinguish factual accuracy from plausible generation; Evaluates factual reliability under alignment-relevant prompting

## Bias, fairness, and values

- BBQ (Bias Benchmark for Question Answering): Ambiguous vs disambiguated QA across demographic contexts; Evaluates social bias and fairness in judgments
- BOLD: Open-ended generation prompts across demographics; Evaluates demographic bias/toxicity differences in generations
- StereoSet: Stereotype association measurement; Evaluates stereotypical vs anti-stereotypical preference in language modeling
- CrowS-Pairs: Minimal pairs (stereotypical vs anti-stereotypical); Evaluates preference toward stereotypes
- Parity Benchmark: Fairness parity-style tests across groups; Evaluates group-conditional performance differences as fairness signals

## Toxicity and hate speech datasets used in alignment contexts

- HateXplain: Hate/offensive content with explanations; Evaluates hate/toxicity detection or generation tendencies
- Implicit Hate: Implicit hate speech examples; Evaluates subtle toxicity and coded hate handling
- Latent Hate: Latent/indirect hate examples; Evaluates non-explicit hate recognition and safe response behavior

## Holistic evaluation suites commonly used in alignment discussions

- HELM (Holistic Evaluation of Language Models): Multi-metric suite including safety/bias/toxicity scenarios; Evaluates broad alignment-related behaviors under a standardized harness
- BIG-Bench: Broad task suite; Often used as a capability baseline when assessing alignment–capability trade-offs
- BIG-Bench Hard (BBH): Harder subset of BIG-Bench; Often used to track whether safety tuning harms challenging reasoning capabilities
- MMLU (Measuring Massive Multitask Language Understanding): Multi-domain knowledge test; Often used as a capability baseline alongside alignment metrics
- AlpacaEval: Instruction-following preference-style evaluation; Often used to track helpfulness/instruction-following quality after alignment tuning
- MT-Bench Safety Variants: Multi-turn judge-based comparisons with safety-focused prompts; Evaluates conversational safety and alignment in multi-turn dialogue

## Safety taxonomy / moderation category benchmarks

- OpenAI Moderation Evaluation Dataset: Labeled moderation examples for safety classification; Evaluates content policy classification quality
- OpenAI Moderation Categories: Category taxonomy for unsafe content; Evaluates coverage and consistency of safety categorization
- LlamaGuard Unsafe Prompt Categories: Unsafe prompt taxonomy used for guarding; Evaluates detection/labeling of unsafe requests
- Azure AI Content Safety Categories: Category taxonomy for content safety; Evaluates classification of unsafe content types
- ToxicChat: Toxic conversation dataset; Evaluates toxicity detection and safe-response handling in chat settings
