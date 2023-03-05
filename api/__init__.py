from fastapi import APIRouter
from .endpoints import train, predict, testing

router = APIRouter()
router.include_router(train.router, prefix="/train", tags=["training"])
router.include_router(predict.router, prefix="/predict", tags=["predict"])
router.include_router(testing.router, prefix="/testing", tags=["testing"])
