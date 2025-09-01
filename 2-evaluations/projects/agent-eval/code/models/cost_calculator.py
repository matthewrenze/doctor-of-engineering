class CostCalculator:
    def __init__(self):
        # Note: All costs are in USD per million tokens
        self.cost_map = {
            "claude-sonnet-4-0": {"input": 3.00, "output": 15.00},
            "claude-opus-4-1": {"input": 15.00, "output": 75.00},
            "deepseek-r1": {"input": 0.56, "output": 1.68},
            "deepseek-v3": {"input": 0.56, "output": 1.68},
            "gemini-2.5-flash": {"input": 0.30, "output": 2.50},
            "gemini-2.5-flash-lite": {"input": 0.10, "output": 0.40},
            "gemini-2.5-pro": {"input": 1.25, "output": 10.00},
            "gpt-4.1": {"input": 3.00, "output": 12.00},
            "gpt-4.1-mini": {"input": 0.80, "output": 3.20},
            "gpt-5": {"input": 1.25, "output": 10.00},
            "gpt-5-mini": {"input": 0.25, "output": 2.00},
            "grok-3": {"input": 3.00, "output": 15.00},
            "grok-3-mini": {"input": 0.30, "output": 0.50},
        }

    def get_input_cost(self, model, tokens):
        unit_cost = self.cost_map[model]["input"]
        input_cost = tokens / 1_000_000 * unit_cost
        return input_cost

    def get_output_cost(self, model, tokens):
        unit_cost = self.cost_map[model]["output"]
        output_cost = tokens / 1_000_000 * unit_cost
        return output_cost




