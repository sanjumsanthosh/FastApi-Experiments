import os

from model.training.Config import Config

configPath = os.path.join(os.path.dirname(__file__), '../config.yaml')
config = Config(configPath)

modelPath = config.get("model.modelOutFile")


def loadModelFromFile():
    import pickle
    with open(modelPath, 'rb') as f:
        model = pickle.load(f)
    return model


class Model:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Model, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        print("Model init")
        self.model = None
        self.loadModel()

    def loadModel(self):
        if self.model is None:
            self.model = loadModelFromFile()

    def predict(self, statement):
        return self.model.predict_proba([statement])

    @classmethod
    def getInstance(cls):
        if not cls._instance:
            cls._instance = cls()
        return cls._instance
