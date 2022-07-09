"""Hello Budget"""
from typing import Union
from pydantic import BaseModel
import uvicorn
from fastapi import FastAPI

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "Budget"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_price": item.price, "item_id": item_id}


def main():
    uvicorn.run("budget.__main__:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    main()
