# TODO:
#  - Add solution_steps (min_steps) field
#  - Add boolean "success" field

class ResultRow:
    def __init__(self):
        self.agent_name = ""
        self.model_name = ""
        self.eval_name = ""
        self.task_id = 0
        self.type = ""
        self.task = ""
        self.correct_answer = ""
        self.agent_answer = ""
        self.reward = 0.0
        self.steps = 0
        self.input_tokens = 0
        self.output_tokens = 0
        self.total_tokens = 0
        self.input_cost = 0.0
        self.output_cost = 0.0
        self.total_cost = 0.0
        self.start_time = None
        self.end_time = None
        self.total_time = None
        self.reward_per_step = 0.0
        self.reward_per_token = 0.0
        self.error = ""