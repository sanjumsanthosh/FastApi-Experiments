from enum import Enum as EnumBase

from pydantic import BaseModel


class ModelType(EnumBase):
    train = "train"
    validate = "validate"
    custom = "custom"
    combined = "combined"


class TrainRequest(BaseModel):
    # define an enum for the model type train, validate and custom with default value as train
    modelType: ModelType = ModelType.train
