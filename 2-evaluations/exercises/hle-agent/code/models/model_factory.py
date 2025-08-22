from models.model import Model
from common.parameters import Parameters

class ModelFactory():

    def create(self, params: Parameters):
        return Model(params.model_name)