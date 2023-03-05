from typing import Union, List

from pydantic import BaseModel


class PredictRequest(BaseModel):
    text: Union[str, List[str]]


class PredictResponse(BaseModel):
    score: float
    isGood: bool
