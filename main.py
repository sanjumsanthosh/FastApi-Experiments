from typing import List
from fastapi import FastAPI
from utils import initializeSwagger
import api

app = FastAPI()
app.include_router(api.router)

initializeSwagger(app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
