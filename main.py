from model import model_pipeline

from typing import Union

from fastapi import FastAPI, UploadFile
from PIL import Image

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/ask")
def ask(text: str, image: UploadFile):
    # content = image.file.read()
    image = Image.open(image.file)
    result = model_pipeline(text=text, image=image)
    return {"answer": result}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

