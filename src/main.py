import os
import sys
import uvicorn
from fastapi import FastAPI

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from src.config import settings
from src.models import Base
from src.api_v1.kittens.models import Kitten
from src.api_v1.breeds.models import Breed
from src.api_v1 import internal_router


app = FastAPI()
app.include_router(router=internal_router, prefix=f"{settings.api_v1_prefix}")

@app.get("/")
def welcome():
    return {"message": "Welcome to the kitten show!"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
