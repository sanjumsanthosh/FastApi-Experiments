from fastapi import APIRouter

from api.schema.train import ModelType
from model import baseModel, training

router = APIRouter()

model = baseModel.Model.getInstance()


@router.post("")
def trainModel(modelType: ModelType):
    training.index.train(modelType, model)
    return {
        "train": "done!",
        "message": f"Model trained and saved to {training.index.outFile}"
    }


@router.get("/validateModel")
def validateModel(modelType: ModelType):
    metrics = training.index.validate(modelType)
    return metrics
