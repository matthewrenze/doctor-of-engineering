from common.parameters import Parameters
from models.claude_model import ClaudeModel
from models.azure_model import AzureModel
from models.gemini_model import GeminiModel
from models.gpt_model import GptModel

class ModelFactory():

    def create(self, params: Parameters):

        if params.model_name.startswith("claude"):
            return ClaudeModel(params.model_name)

        elif params.model_name.startswith("deepseek"):
            return AzureModel(params.model_name)

        elif params.model_name.startswith("gemini"):
            return GeminiModel(params.model_name)

        elif params.model_name.startswith("gpt"):
            return GptModel(params.model_name)
        
        elif params.model_name.startswith("grok"):
            return AzureModel(params.model_name)

        else:
            raise ValueError(f"Unknown model name: {params.model_name}")