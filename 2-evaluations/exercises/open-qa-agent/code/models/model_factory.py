from models.model import Model

class ModelFactory():

    def create(self, model_name):
        return Model(model_name)