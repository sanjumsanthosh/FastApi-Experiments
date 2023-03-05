from random import random

from fastapi import APIRouter
from model import baseModel, prediction
from model.training.classifier import trainData, validationData

router = APIRouter()

model = baseModel.Model.getInstance()


@router.get("generateFromTrainSet")
def generateFromTrainSet():
    randomIndex = int(random() * len(trainData))
    traindata = trainData.iloc[randomIndex]
    print(f"Random index: {randomIndex}")
    result = prediction.index.predict(traindata['Statement'], model)

    return {
        "statement": traindata['Statement'],
        "label": f"{traindata['Label']}",
        "isGood": f"{result['isGood']}",
        "score": result['score']
    }


@router.get("generateFromValidationSet")
def generateFromValidationSet():
    randomIndex = int(random() * len(validationData))
    data = validationData.iloc[randomIndex]
    print(f"Random index: {randomIndex}")
    result = prediction.index.predict(data['Statement'], model)

    return {
        "statement": data['Statement'],
        "label": f"{data['Label']}",
        "isGood": f"{result['isGood']}",
        "score": result['score']
    }
