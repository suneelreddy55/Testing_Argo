from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Sample FastAPI App", version="1.0.0")


class Item(BaseModel):
    name: str
    description: str = ""


@app.get("/")
def root():
    return {"message": "Hello from FastAPI!", "status": "running"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id, "name": f"Item {item_id}"}


@app.post("/items")
def create_item(item: Item):
    return {"message": "Item created", "item": item}
