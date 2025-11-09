from models.model import Model

class OracleModel(Model):
    def __init__(self, model_name: str):
        self.model_name = model_name
        self.input_tokens = 0
        self.output_tokens = 0
        self.total_tokens = 0

    def reset(self):
        pass

    def get_response(self, messages: list[dict[str, str]]) -> str:
        pass
