from fastapi import APIRouter
from model import baseModel, prediction
from ..schema import predict

router = APIRouter()

model = baseModel.Model.getInstance()


@router.post("", response_model=predict.PredictResponse)
def predict(request: predict.PredictRequest):
    return prediction.index.predict(request.text, model)
