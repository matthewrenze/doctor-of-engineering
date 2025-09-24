class SummaryRow:
    def __init__(self):
        self.agent_name = ""
        self.model_name = ""
        self.eval_name = ""
        self.chunk_size = 0
        self.tasks = 0
        self.successes = 0
        self.failures = 0
        self.errors = 0
        self.accuracy = 0.0
        self.total_reward = 0.0
        self.total_steps = 0
        self.input_tokens = 0
        self.output_tokens = 0
        self.total_tokens = 0
        self.input_cost = 0.0
        self.output_cost = 0.0
        self.total_cost = 0.0
        self.total_time = 0.0
        self.avg_reward_per_task = 0.0
        self.avg_reward_per_step = 0.0
        self.avg_reward_per_token = 0.0