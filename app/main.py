from fastapi import FastAPI
from pydantic import BaseModel

class ComputeInput(BaseModel):
    x: float
    y: float

app = FastAPI()

@app.get("/")
def read_root():
    return { "msg": "Hello! - CCGE Assignment 2", "v": "0.1" }


@app.get("/items/{id}")
def read_item(item_id: int, q: str = None):
    return {"id": id, "q": q}

@app.post("/compute")
def compute(data: ComputeInput):
    result = data.x + data.y
    return {"result": result}